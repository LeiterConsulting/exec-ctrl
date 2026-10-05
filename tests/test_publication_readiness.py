"""Reproducible acceptance workflows; synthetic targets, no provider claims."""

import copy
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import exec_ctrl as ec


class PublicationReadiness(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = ec.load_catalog()

    def test_routing_matrix_keeps_baselines_and_escalates_sensitive_work(self):
        observed_modes = set()
        observed_modules = set()
        for kind in self.catalog["kinds"]:
            for risk in self.catalog["risks"]:
                for whole in (False, True):
                    facts = {"kind": kind, "risk": risk, "signals": [], "whole_project": whole}
                    with self.subTest(facts=facts):
                        plan = ec.route(facts, self.catalog)
                        self.assertTrue({"scope", "policy", "verification", "review", "git-review"} <= set(plan["required_gates"]))
                        self.assertTrue({"policy", "git"} <= {m["id"] for m in plan["modules"]})
                        self.assertEqual(plan["mode"] == "project", whole)
                        if kind in {"incident", "migration"}:
                            self.assertEqual(plan["effective_risk"], "high")
                        observed_modes.add(plan["mode"])
                        observed_modules.update(m["id"] for m in plan["modules"])
        for signal in self.catalog["signals"]:
            facts = {"kind": "docs", "risk": "low", "signals": [signal], "whole_project": False}
            with self.subTest(signal=signal):
                plan = ec.route(facts, self.catalog)
                self.assertNotEqual(plan["mode"], "inline")
                if signal in self.catalog["high_risk_signals"]:
                    self.assertEqual(plan["effective_risk"], "high")
                    self.assertIn("security-review", plan["required_gates"])
                observed_modules.update(m["id"] for m in plan["modules"])
        self.assertEqual(observed_modes, {"inline", "task", "initiative", "project"})
        self.assertEqual(observed_modules, {m["id"] for m in self.catalog["modules"]})

    def cli(self, cwd, *args, expected=0, audited=False):
        command = [sys.executable, "-B"]
        if audited:
            command.append(str(ec.ROOT / "tests/audit_cli.py"))
        command.extend([str(ec.ROOT / "tools/exec_ctrl.py"), *args])
        result = subprocess.run(command, cwd=cwd, capture_output=True, text=True, timeout=20)
        self.assertEqual(result.returncode, expected, result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertEqual(result.stdout == "", expected == 2)
        self.assertEqual(result.stderr == "", expected != 2)
        return json.loads(result.stderr if expected == 2 else result.stdout)

    def save(self, path, value):
        path.write_text(json.dumps(value, indent=2), encoding="utf-8")

    def test_project_fix_failure_repair_and_current_evidence_closure(self):
        with tempfile.TemporaryDirectory(prefix="exec-ctrl-project-") as temp:
            root = Path(temp) / "project with spaces"
            root.mkdir()
            (root / "tests").mkdir()
            instructions = b"Synthetic project. Preserve user work; Python standard library only.\n"
            user_work = b"Unfinished user notes; do not overwrite.\n"
            (root / "AGENTS.md").write_bytes(instructions)
            (root / "USER_NOTES.md").write_bytes(user_work)
            (root / "service.py").write_text("def can_read(actor, owner):\n    return True\n", encoding="utf-8")
            (root / "tests/test_access.py").write_text(
                "import unittest\nfrom service import can_read\n"
                "class Access(unittest.TestCase):\n"
                "    def test_owner(self):\n        self.assertTrue(can_read('blue', 'blue'))\n"
                "    def test_other_tenant(self):\n        self.assertFalse(can_read('blue', 'green'))\n", encoding="utf-8")
            rules = copy.deepcopy(ec.read_json(ec.ROOT / "examples/v2/team-rules.json"))
            rules["id"] = "synthetic-regression-policy"
            rules["gates"] = [{"id": "tenant-regression", "description": "Run synthetic tenant denial tests",
                               "source": "fixture://policy", "owner": "Fixture", "requires": ["test"]}]
            policy = Path(temp) / "policy.json"
            manifest_path = Path(temp) / "snapshot.json"
            record_path = Path(temp) / "record.json"
            self.save(policy, rules)

            def capture():
                return self.cli(temp, "snapshot", "--target", str(root), "--path", "service.py",
                                "--path", "tests/test_access.py", "--path", "AGENTS.md", audited=True)

            def generate(subject):
                return self.cli(temp, "record-template", "--kind", "fix", "--risk", "low", "--signal", "auth",
                                "--rules", str(policy), "--id", "tenant-fix", "--objective", "Deny cross-tenant access",
                                "--subject", subject, audited=True)

            def check(expected):
                return self.cli(temp, "check-record", str(record_path), "--rules", str(policy),
                                "--snapshot", str(manifest_path), "--target", str(root), expected=expected, audited=True)

            def run_project_tests():
                return subprocess.run([sys.executable, "-B", "-m", "unittest", "discover", "-s", "tests", "-v"],
                                      cwd=root, capture_output=True, text=True, timeout=20)

            original = capture()
            self.save(manifest_path, original)
            pending = generate(original["subject"])
            self.save(record_path, pending)
            self.assertIn("tenant-regression", check(1)["unresolved_gates"])
            failed = run_project_tests()
            self.assertEqual(failed.returncode, 1, failed.stderr)
            self.assertIn("test_other_tenant", failed.stderr)
            failing = copy.deepcopy(pending)
            failing["state"] = "in_progress"
            failing["evidence"] = [{"id": "denial-test", "kind": "test", "subject": original["subject"],
                                    "result": "fail", "reference": "fixture://original-test-run", "summary": failed.stderr}]
            gate = next(g for g in failing["gates"] if g["id"] == "tenant-regression")
            gate.update(result="fail", evidence=["denial-test"], reason="Cross-tenant denial failed")
            self.save(record_path, failing)
            self.assertFalse(check(1)["ready_to_close"])
            gate["result"] = "pass"
            self.save(record_path, failing)
            self.assertIn("failed evidence", check(2)["error"])

            # The test harness repairs its disposable app; the helper never edits it.
            (root / "service.py").write_text("def can_read(actor, owner):\n    return actor == owner\n", encoding="utf-8")
            self.assertIn("changed", check(2)["error"])
            passed = run_project_tests()
            self.assertEqual(passed.returncode, 0, passed.stderr)
            current = capture()
            self.assertNotEqual(current["subject"], original["subject"])
            self.save(manifest_path, current)
            self.assertIn("current snapshot", check(2)["error"])
            ready = generate(current["subject"])
            ready["state"] = "complete"
            ready["evidence"] = [
                {"id": "current-tests", "kind": "test", "subject": current["subject"], "result": "pass",
                 "reference": "fixture://repaired-test-run", "summary": passed.stderr},
                {"id": "fixture-inspection", "kind": "inspection", "subject": current["subject"], "result": "pass",
                 "reference": "fixture://scope-diff", "summary": "Synthetic harness inspected one equality fix; no production approval"}]
            for gate in ready["gates"]:
                gate.update(result="pass", evidence=["current-tests", "fixture-inspection"], reason="Synthetic acceptance only")
            self.save(record_path, ready)
            self.assertTrue(check(0)["ready_to_close"])
            changed_policy = copy.deepcopy(rules)
            changed_policy["gates"][0]["requires"].append("review")
            self.save(policy, changed_policy)
            self.assertIn("ruleset identities", check(2)["error"])
            self.assertEqual((root / "AGENTS.md").read_bytes(), instructions)
            self.assertEqual((root / "USER_NOTES.md").read_bytes(), user_work)
            self.assertEqual({p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()},
                             {"AGENTS.md", "USER_NOTES.md", "service.py", "tests/test_access.py"})

    def test_every_cli_command_is_offline_and_read_only_under_audit(self):
        with tempfile.TemporaryDirectory(prefix="exec-ctrl-audit-") as temp:
            root = Path(temp)
            sentinel = root / "must-not-exist.txt"
            # Both a network URL and executable-looking text remain inert metadata.
            record = ec.read_json(ec.ROOT / "examples/v2/docs-record.json")
            for evidence in record["evidence"]:
                evidence["reference"] = "__import__('pathlib').Path(" + repr(str(sentinel)) + ").write_text('executed')"
                evidence["summary"] = "URL metadata https://example.invalid/ must not be fetched"
            path = root / "record.json"
            self.save(path, record)
            before = path.read_bytes()
            self.cli(temp, "validate", audited=True)
            self.cli(temp, "route", "--kind", "release", "--signal", "production", audited=True)
            self.cli(temp, "record-template", "--kind", "docs", "--risk", "low", "--id", "audit",
                     "--objective", "Audit helper", "--subject", "fixture", audited=True)
            self.cli(temp, "snapshot", "--target", temp, "--path", "record.json", audited=True)
            self.assertTrue(self.cli(temp, "check-record", str(path), audited=True)["ready_to_close"])
            path.write_text('{"duplicate": 1, "duplicate": 2}', encoding="utf-8")
            self.cli(temp, "check-record", str(path), expected=2, audited=True)
            self.assertFalse(sentinel.exists())
            self.assertEqual({p.name for p in root.iterdir()}, {"record.json"})
            self.assertIn(b"example.invalid", before)

    def test_audit_guard_itself_denies_file_writes_and_network_and_processes(self):
        for operation in ["open('forbidden', 'w')", "__import__('os').mkdir('forbidden')",
                          "__import__('socket').socket()", "__import__('subprocess').run(['unused'])"]:
            with self.subTest(operation=operation), tempfile.TemporaryDirectory() as temp:
                script = Path(temp) / "probe.py"
                script.write_text(operation, encoding="utf-8")
                result = subprocess.run([sys.executable, "-B", str(ec.ROOT / "tests/audit_cli.py"), str(script)],
                                        cwd=temp, capture_output=True, text=True, timeout=20)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("read-only audit denied", result.stderr)
                self.assertFalse((Path(temp) / "forbidden").exists())

    def test_unknown_policy_is_pending_until_resolved_without_overwriting_history(self):
        facts = {"kind": "docs", "risk": "low", "signals": ["policy-unknown"], "whole_project": False}
        pending = ec.record_template(facts, self.catalog, "policy", "Resolve policy", "current")
        historical = copy.deepcopy(pending)
        gate = next(g for g in pending["gates"] if g["id"] == "policy")
        gate.update(result="blocked", reason="Expected policy unavailable")
        self.assertIn("policy", ec.check_record(pending, self.catalog)["unresolved_gates"])
        pending["state"] = "complete"
        with self.assertRaisesRegex(ec.Invalid, "unresolved gates"):
            ec.check_record(pending, self.catalog)
        revised_facts = {**facts, "signals": []}
        revised = ec.record_template(revised_facts, self.catalog, "policy", "Resolve policy", "current")
        self.assertEqual(ec.route(revised_facts, self.catalog)["mode"], "inline")
        self.assertFalse(ec.check_record(revised, self.catalog)["ready_to_close"])
        self.assertEqual(historical["state"], "not_started")
        self.assertEqual(historical["facts"]["signals"], ["policy-unknown"])

    def test_historical_version_is_rejected_without_rewriting_record(self):
        record = ec.read_json(ec.ROOT / "examples/v2/docs-record.json")
        record["framework_version"] = "2.0.0-preview.2"
        original = copy.deepcopy(record)
        with self.assertRaisesRegex(ec.Invalid, "version mismatch"):
            ec.check_record(record, self.catalog)
        self.assertEqual(record, original)

    def unstable_snapshot(self, mutate, after_close=False):
        with tempfile.TemporaryDirectory(prefix="exec-ctrl-capture-") as temp:
            root = Path(temp)
            path = root / "source.txt"
            path.write_bytes(b"original")
            original_open = Path.open

            class MutatingReader:
                def __init__(self, stream):
                    self.stream = stream
                    self.changed = False

                def __enter__(self):
                    self.stream.__enter__()
                    return self

                def __exit__(self, *args):
                    result = self.stream.__exit__(*args)
                    if after_close:
                        mutate(path, root)
                    return result

                def fileno(self):
                    return self.stream.fileno()

                def read(self, size):
                    value = self.stream.read(size)
                    if value and not self.changed and not after_close:
                        self.changed = True
                        mutate(path, root)
                    return value

            def hooked_open(candidate, *args, **kwargs):
                stream = original_open(candidate, *args, **kwargs)
                if candidate == path and args == ("rb",):
                    return MutatingReader(stream)
                return stream

            with patch.object(Path, "open", hooked_open), self.assertRaisesRegex(ec.Invalid, "changed during capture"):
                ec.snapshot(root, ["source.txt"])

    def test_snapshot_rejects_same_size_edit_during_capture(self):
        def change(path, root):
            before = path.stat()
            path.write_bytes(b"modified")
            os.utime(path, ns=(before.st_atime_ns, before.st_mtime_ns + 2_000_000_000))
        self.unstable_snapshot(change)

    def test_snapshot_rejects_file_replacement_during_capture(self):
        def replace(path, root):
            path.rename(root / "historical.txt")
            path.write_bytes(b"replaced")
        self.unstable_snapshot(replace, after_close=True)

    def test_snapshot_rejects_truncation_during_capture(self):
        self.unstable_snapshot(lambda path, root: path.write_bytes(b""))

    def test_snapshot_rejects_deletion_during_capture(self):
        self.unstable_snapshot(lambda path, root: path.unlink(), after_close=True)

    def test_snapshot_accepts_stable_files_immediately_after_rewrites(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "source.txt"
            for count in range(20):
                value = str(count).encode("ascii")
                path.write_bytes(value)
                manifest = ec.snapshot(temp, ["source.txt"])
                self.assertEqual(manifest["files"][0]["bytes"], len(value))
                self.assertEqual(ec.check_snapshot(manifest, temp), manifest["subject"])


if __name__ == "__main__":
    unittest.main()
