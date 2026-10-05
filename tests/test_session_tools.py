"""Practical session tools: pending work, typed evidence and current-file identity."""

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import exec_ctrl as ec


class SessionTools(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = ec.load_catalog()

    def facts(self, kind="docs", signals=()):
        return {"kind": kind, "risk": "low", "signals": list(signals), "whole_project": False}

    def record(self):
        return ec.read_json(ec.ROOT / "examples/v2/docs-record.json")

    def rule(self):
        return {"schema_version": 1, "id": "fixture-live-rule", "source": "fixture://policy",
                "revision": "1", "owner": "Fixture owner", "required_modules": ["delivery"],
                "gates": [{"id": "fixture-live-acceptance", "description": "Declared deployed and live evidence",
                           "source": "fixture://policy/live", "owner": "Fixture owner", "requires": ["deployment", "live"]}]}

    def test_template_is_valid_pending_work_without_evidence(self):
        record = ec.record_template(self.facts("fix", ["auth"]), self.catalog, "requested-id", "Fix access", "files-1")
        result = ec.check_record(record, self.catalog)
        self.assertEqual(record["id"], "requested-id")
        self.assertEqual(record["state"], "not_started")
        self.assertEqual(record["evidence"], [])
        self.assertFalse(result["ready_to_close"])
        self.assertEqual(set(result["unresolved_gates"]), set(result["route"]["required_gates"]))
        self.assertTrue(all(g["result"] == "not_run" for g in record["gates"]))

    def test_template_copies_policy_provenance_and_requirements(self):
        rule = self.rule()
        record = ec.record_template(self.facts(), self.catalog, "id", "Objective", "files-1", [rule])
        self.assertEqual(record["rulesets"], [ec.rule_identity(rule)])
        gate = next(g for g in record["gates"] if g["id"] == "fixture-live-acceptance")
        self.assertEqual(gate["requires"], ["deployment", "live"])
        self.assertFalse(ec.check_record(record, self.catalog, [rule])["ready_to_close"])

    def test_template_does_not_alias_input_signal_list(self):
        facts = self.facts("fix", ["auth"])
        record = ec.record_template(facts, self.catalog, "id", "Objective", "files")
        facts["signals"].clear()
        self.assertEqual(record["facts"]["signals"], ["auth"])

    def test_template_rejects_missing_outcome_identity_and_subject(self):
        for args in [("", "Objective", "subject"), ("id", " ", "subject"), ("id", "Objective", None)]:
            with self.subTest(args=args), self.assertRaises(ec.Invalid):
                ec.record_template(self.facts(), self.catalog, *args)

    def test_build_cannot_satisfy_explicit_live_gate(self):
        record = self.record()
        record["evidence"][0]["kind"] = "build"
        record["gates"].append({"id": "actual-runtime", "result": "pass", "evidence": ["synthetic-review"],
                                "reason": "", "requires": ["live"]})
        with self.assertRaisesRegex(ec.Invalid, "required evidence kinds"):
            ec.check_record(record, self.catalog)

    def test_all_required_evidence_kinds_must_be_present(self):
        record = self.record()
        record["gates"][0]["requires"] = ["inspection", "test"]
        with self.assertRaises(ec.Invalid):
            ec.check_record(record, self.catalog)
        test = {**record["evidence"][0], "id": "synthetic-test", "kind": "test"}
        record["evidence"].append(test)
        record["gates"][0]["evidence"].append(test["id"])
        self.assertTrue(ec.check_record(record, self.catalog)["ready_to_close"])

    def test_policy_requirements_cannot_be_removed_from_record_gate(self):
        rule = self.rule()
        record = ec.record_template(self.facts(), self.catalog, "id", "Objective", "synthetic", [rule])
        record["state"] = "complete"
        record["evidence"] = [{"id": "inspect", "kind": "inspection", "subject": "synthetic", "result": "pass",
                              "reference": "fixture://inspect", "summary": "Synthetic only"}]
        for gate in record["gates"]:
            gate.update(result="pass", evidence=["inspect"], reason="")
            gate.pop("requires", None)
        with self.assertRaises(ec.Invalid):
            ec.check_record(record, self.catalog, [rule])
        for kind in ("deployment", "live"):
            record["evidence"].append({**record["evidence"][0], "id": kind, "kind": kind})
        next(g for g in record["gates"] if g["id"] == "fixture-live-acceptance")["evidence"] += ["deployment", "live"]
        self.assertTrue(ec.check_record(record, self.catalog, [rule])["ready_to_close"])

    def test_policy_and_local_requirements_compose(self):
        rule = self.rule()
        record = ec.record_template(self.facts(), self.catalog, "id", "Objective", "synthetic", [rule])
        record["state"] = "complete"
        record["evidence"] = [{"id": k, "kind": k, "subject": "synthetic", "result": "pass",
                              "reference": "fixture://" + k, "summary": "Synthetic only"} for k in ("inspection", "deployment", "live")]
        for gate in record["gates"]:
            gate.update(result="pass", evidence=["inspection", "deployment", "live"], reason="")
        record["gates"][-1]["requires"] = ["review"]
        with self.assertRaises(ec.Invalid):
            ec.check_record(record, self.catalog, [rule])

    def test_malformed_requirements_are_rejected_even_for_pending_gates(self):
        for value in (None, True, "live", ["unknown"], ["test", "test"], [{}]):
            with self.subTest(value=value):
                record = ec.record_template(self.facts(), self.catalog, "id", "Objective", "subject")
                record["gates"][0]["requires"] = value
                with self.assertRaises(ec.Invalid):
                    ec.check_record(record, self.catalog)
                rule = self.rule()
                rule["gates"][0]["requires"] = value
                with self.assertRaises(ec.Invalid):
                    ec.route(self.facts(), self.catalog, [rule])

    def test_required_evidence_still_requires_current_subject_and_passing_result(self):
        for field, value in [("subject", "old"), ("result", "fail")]:
            with self.subTest(field=field):
                record = self.record()
                record["gates"][0]["requires"] = ["inspection"]
                record["evidence"][0][field] = value
                with self.assertRaises(ec.Invalid):
                    ec.check_record(record, self.catalog)

    def test_subject_comparison_rejects_relabelled_or_old_record(self):
        record = self.record()
        self.assertTrue(ec.check_record(record, self.catalog, expected_subject=record["subject"])["ready_to_close"])
        with self.assertRaisesRegex(ec.Invalid, "current snapshot"):
            ec.check_record(record, self.catalog, expected_subject="changed-content")

    def fixture(self, root):
        (root / "source.txt").write_bytes(b"one\n")
        (root / "with spaces.txt").write_bytes(b"two\n")
        (root / ".env").write_text("fictional private value", encoding="utf-8")

    def test_snapshot_is_portable_order_independent_and_explicit(self):
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            roots = [Path(first), Path(second)]
            for root in roots:
                self.fixture(root)
            one = ec.snapshot(roots[0], ["source.txt", "with spaces.txt"])
            two = ec.snapshot(roots[1], ["with spaces.txt", "source.txt"])
            self.assertEqual(one, two)
            self.assertEqual({item["path"] for item in one["files"]}, {"source.txt", "with spaces.txt"})
            self.assertNotIn("private", json.dumps(one))
            self.assertEqual(ec.check_snapshot(one, roots[1]), one["subject"])

    def test_changed_same_size_content_invalidates_snapshot(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.fixture(root)
            manifest = ec.snapshot(root, ["source.txt"])
            (root / "source.txt").write_bytes(b"new\n")
            with self.assertRaisesRegex(ec.Invalid, "changed"):
                ec.check_snapshot(manifest, root)

    def test_unselected_file_changes_do_not_claim_to_be_covered(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.fixture(root)
            manifest = ec.snapshot(root, ["source.txt"])
            (root / ".env").write_text("changed fictional value", encoding="utf-8")
            self.assertEqual(ec.check_snapshot(manifest, root), manifest["subject"])
            self.assertIn("unlisted", manifest["limits"])

    def test_missing_selected_file_invalidates_snapshot(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "source.txt").write_bytes(b"source")
            manifest = ec.snapshot(root, ["source.txt"])
            (root / "source.txt").rename(root / "renamed.txt")
            with self.assertRaises(ec.Invalid):
                ec.check_snapshot(manifest, root)

    def test_snapshot_paths_cannot_escape_or_alias(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "target"
            root.mkdir()
            self.fixture(root)
            (root.parent / "outside.txt").write_bytes(b"outside")
            for paths in [["../outside.txt"], [str(root / "source.txt")], ["source.txt", "./source.txt"],
                          ["source.txt", "source.txt"], ["missing.txt"], ["."], [], [{}], ["source\\file.txt"]]:
                with self.subTest(paths=paths), self.assertRaises(ec.Invalid):
                    ec.snapshot(root, paths)

    def test_snapshot_symlink_escape_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "target"
            root.mkdir()
            outside = root.parent / "outside.txt"
            outside.write_bytes(b"outside")
            try:
                (root / "link.txt").symlink_to(outside)
            except OSError:
                self.skipTest("Symlink creation unavailable on this host")
            with self.assertRaises(ec.Invalid):
                ec.snapshot(root, ["link.txt"])

    def test_manifest_tampering_and_malformed_fields_are_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.fixture(root)
            manifest = ec.snapshot(root, ["source.txt"])
            for path, value in [(('schema_version',), True), (('files',), []), (('files',), {}),
                                (('subject',), "wrong"), (('limits',), "whole repository"),
                                (('files', 0, 'bytes'), True), (('files', 0, 'sha256'), "0" * 64),
                                (('files', 0, 'path'), "../outside")]:
                with self.subTest(path=path, value=value):
                    changed = copy.deepcopy(manifest)
                    field = changed
                    for key in path[:-1]:
                        field = field[key]
                    field[path[-1]] = value
                    with self.assertRaises(ec.Invalid):
                        ec.check_snapshot(changed, root)

    def test_snapshot_rejects_internal_symlink_that_could_be_repointed(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "real.txt").write_bytes(b"real")
            try:
                (root / "current.txt").symlink_to(root / "real.txt")
            except OSError:
                self.skipTest("Symlink creation unavailable on this host")
            with self.assertRaisesRegex(ec.Invalid, "symbolic links"):
                ec.snapshot(root, ["current.txt"])

    def test_snapshot_resource_limits(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "a").write_bytes(b"abc")
            (root / "b").write_bytes(b"def")
            with patch.object(ec, "MAX_SNAPSHOT_FILE_BYTES", 2), self.assertRaises(ec.Invalid):
                ec.snapshot(root, ["a"])
            with patch.object(ec, "MAX_SNAPSHOT_TOTAL_BYTES", 5), self.assertRaises(ec.Invalid):
                ec.snapshot(root, ["a", "b"])
            with self.assertRaises(ec.Invalid):
                ec.snapshot(root, ["file-" + str(i) for i in range(257)])

    def test_cli_round_trip_is_read_only_and_rejects_changed_target(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "target"
            root.mkdir()
            self.fixture(root)
            helper = str(ec.ROOT / "tools/exec_ctrl.py")

            def cli(*args, expected=0):
                result = subprocess.run([sys.executable, "-B", helper, *args], cwd=temp,
                                        text=True, capture_output=True, timeout=10)
                self.assertEqual(result.returncode, expected, result.stderr)
                return json.loads(result.stdout or result.stderr)

            before = {p.name: p.read_bytes() for p in root.iterdir()}
            manifest = cli("snapshot", "--target", str(root), "--path", "source.txt")
            record = cli("record-template", "--kind", "docs", "--risk", "low", "--id", "fixture",
                         "--objective", "Review fixture", "--subject", manifest["subject"])
            manifest_path = Path(temp) / "snapshot.json"
            record_path = Path(temp) / "record.json"
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            record_path.write_text(json.dumps(record), encoding="utf-8")
            pending = cli("check-record", str(record_path), "--snapshot", str(manifest_path), "--target", str(root), expected=1)
            self.assertFalse(pending["ready_to_close"])
            self.assertEqual({p.name: p.read_bytes() for p in root.iterdir()}, before)
            (root / "source.txt").write_bytes(b"changed")
            self.assertFalse(cli("check-record", str(record_path), "--snapshot", str(manifest_path), "--target", str(root), expected=2)["valid"])

    def test_cli_snapshot_flags_require_the_pair(self):
        for extra in [["--snapshot", "unused.json"], ["--target", "."]]:
            result = subprocess.run([sys.executable, "-B", str(ec.ROOT / "tools/exec_ctrl.py"), "check-record",
                                     str(ec.ROOT / "examples/v2/docs-record.json"), *extra],
                                    capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 2)
            self.assertIn("supplied together", json.loads(result.stderr)["error"])

    def test_nonfunctional_signals_select_contract_and_behavior_controls(self):
        for signal in ("performance", "accessibility", "compatibility"):
            plan = ec.route(self.facts("planning", [signal]), self.catalog)
            self.assertIn("behavior", plan["required_gates"])
            if signal != "accessibility":
                self.assertIn("design", plan["required_gates"])

    def test_pending_release_example_and_policies_are_coherent(self):
        rules = [ec.read_json(ec.ROOT / "examples/v2/release-rules.json")]
        record = ec.read_json(ec.ROOT / "examples/v2/pending-release-record.json")
        result = ec.check_record(record, self.catalog, rules)
        self.assertFalse(result["ready_to_close"])
        self.assertIn("release-runtime-acceptance", result["unresolved_gates"])
        self.assertEqual(record["evidence"], [])


if __name__ == "__main__":
    unittest.main()
