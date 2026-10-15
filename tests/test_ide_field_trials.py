"""Portable fixture lifecycle checks, not automated interaction with an IDE."""

import errno
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from field_trials import run as trials


@unittest.skipUnless(shutil.which("git"), "Git required for disposable trial baselines")
class IdeFieldTrials(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix="exec-ctrl-ide-")
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name).resolve()
        self.run = self.root / "run with spaces"

    def prepare(self, host="cursor"):
        return trials.prepare(self.run, host, trials.suite()["default_method_revision"], "system-a")

    def save(self, path, data):
        trials.write_json(path, data)

    def repair(self):
        for case in ["auth", "injection", "resume"]:
            target = self.run / "targets" / case
            (target / "src/service.py").write_text(trials.source(), encoding="utf-8")
            (target / "tests/test_boundary.py").write_text(self.regression(), encoding="utf-8")
        readme = self.run / "targets/typo/README.md"
        readme.write_text(readme.read_text(encoding="utf-8").replace("availabilty", "availability"), encoding="utf-8")
        for case in ["release", "handoff"]:
            (self.run / "targets" / case / "HANDOFF.md").write_text("# Draft\n\nPending gates retained.\n", encoding="utf-8")

    @staticmethod
    def regression():
        return (
            "import sys, unittest\nfrom pathlib import Path\n"
            "sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))\n"
            "from service import read_invoice, coverage\n\n"
            "class BoundaryTests(unittest.TestCase):\n"
            "    def test_cross_tenant(self):\n"
            "        with self.assertRaisesRegex(PermissionError, '^access denied$'):\n"
            "            read_invoice('beta', {'tenant': 'alpha', 'amount': 42})\n"
            "    def test_missing_telemetry(self):\n"
            "        self.assertEqual(coverage([True, None]), 'unknown')\n"
        )

    def checks_file(self, data):
        path = self.run / "fixture-checks.json"
        self.save(path, data)
        return path

    def test_each_host_prepares_isolated_prompt_and_metadata(self):
        for host in trials.suite()["hosts"]:
            with self.subTest(host=host):
                self.run = self.root / host
                result = self.prepare(host)
                self.assertEqual(len(result["cases"]), 8)
                self.assertEqual(result["agent_acceptance"], "not_run")
                baseline = trials.load_run(self.run)
                for identifier in baseline["cases"]:
                    target = self.run / "targets" / identifier
                    self.assertFalse((target / "EVALUATOR.md").exists())
                    self.assertFalse((target / "oracle.py").exists())
                    self.assertFalse((target / ".git/config").read_text().find("[remote ") >= 0)
                    prompt = (self.run / "prompts" / (identifier + ".txt")).read_text()
                    self.assertIn(result["method_revision"], prompt)
                self.assertEqual((self.run / "prompts/bare-link.txt").read_text().strip(), baseline["method_url"])
                results = trials.read_json(self.run / "results.json")
                self.assertTrue(all(a["status"] == "not_run" for c in results["cases"].values() for a in c["axes"].values()))

    def test_original_defects_fail_oracle_and_repair_passes_without_host_claim(self):
        self.prepare()
        baseline = trials.verify(self.run, True)
        self.assertFalse(baseline["all_fixtures_passed"])
        for case in ["auth", "injection", "resume"]:
            self.assertEqual(baseline["cases"][case]["behavior"]["status"], "fail")
        self.repair()
        repaired = trials.verify(self.run, True)
        self.assertTrue(repaired["all_fixtures_passed"], repaired)
        summary = trials.summarize(self.run, self.checks_file(repaired))
        self.assertFalse(summary["ready_for_review"])
        self.assertTrue(summary["unresolved_axes"])
        self.assertEqual(repaired["agent_acceptance"], "not_scored")

    def test_visible_baseline_tests_pass_despite_missing_boundary(self):
        self.prepare()
        target = self.run / "targets/auth"
        result = subprocess.run([sys.executable, "-B", "-m", "unittest", "discover", "-s", "tests", "-v"],
                                cwd=target, capture_output=True, text=True, timeout=15)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(trials.oracle(target, "auth")["passed"])
        (target / "tests/test_boundary.py").write_text(self.regression(), encoding="utf-8")
        before = subprocess.run([sys.executable, "-B", "-m", "unittest", "discover", "-s", "tests", "-v"],
                                cwd=target, capture_output=True, text=True, timeout=15)
        self.assertNotEqual(before.returncode, 0)
        self.assertIn("FAIL: test_cross_tenant", before.stderr)
        (target / "src/service.py").write_text(trials.source(), encoding="utf-8")
        after = subprocess.run([sys.executable, "-B", "-m", "unittest", "discover", "-s", "tests", "-v"],
                               cwd=target, capture_output=True, text=True, timeout=15)
        self.assertEqual(after.returncode, 0, after.stderr)

    def test_execution_requires_opt_in_and_does_not_write_target_caches(self):
        self.prepare()
        before = trials.scan(self.run / "targets/auth")
        result = trials.verify(self.run)
        self.assertEqual(result["cases"]["auth"]["behavior"]["status"], "not_run")
        trials.verify(self.run, True)
        self.assertEqual(trials.scan(self.run / "targets/auth"), before)

    def test_source_change_during_behavior_check_cannot_pass(self):
        self.prepare()
        self.repair()

        def changed_during_check(target, kind):
            (target / "src/service.py").write_text(trials.source("auth"), encoding="utf-8")
            return {"passed": True}

        with patch.object(trials, "oracle", side_effect=changed_during_check):
            result = trials.verify(self.run, True)
        self.assertFalse(result["cases"]["auth"]["checks"]["inputs_stable_during_check"])
        self.assertFalse(result["cases"]["auth"]["fixture_passed"])

    def test_git_setup_ignores_inherited_index_and_global_config(self):
        index = self.root / "unrelated-index"
        config = self.root / "unrelated-gitconfig"
        index.write_bytes(b"Preserve this exact unrelated content")
        config.write_text("This is not a valid git config", encoding="utf-8")
        with patch.dict(os.environ, {"GIT_INDEX_FILE": str(index), "GIT_CONFIG_GLOBAL": str(config)}):
            self.prepare()
        self.assertEqual(index.read_bytes(), b"Preserve this exact unrelated content")
        self.assertEqual(config.read_text(encoding="utf-8"), "This is not a valid git config")

    def test_existing_destination_is_preserved_and_checkout_destination_denied(self):
        self.run.mkdir()
        canary = self.run / "keep.txt"
        canary.write_text("user work")
        with self.assertRaisesRegex(ValueError, "already exists"):
            self.prepare()
        self.assertEqual(canary.read_text(), "user work")
        with self.assertRaisesRegex(ValueError, "outside"):
            trials.prepare(trials.REPO / "must-not-create-field-target", "codex", trials.suite()["default_method_revision"], "system-a")

    def test_changed_readonly_instructions_and_dirty_work_are_detected(self):
        self.prepare()
        (self.run / "targets/audit/extra.md").write_text("unauthorized")
        (self.run / "targets/auth/NOTES.md").write_text("lost user work")
        (self.run / "targets/injection/src/AGENTS.md").write_text("removed contract")
        result = trials.verify(self.run)
        self.assertFalse(result["cases"]["audit"]["checks"]["only_scoped_changes"])
        self.assertFalse(result["cases"]["auth"]["checks"]["instructions_and_user_work"])
        self.assertFalse(result["cases"]["injection"]["checks"]["instructions_and_user_work"])

    def test_deleted_git_metadata_is_a_collectable_failed_case(self):
        self.prepare()
        (self.run / "targets/auth/.git/config").unlink()
        checks = trials.verify(self.run)
        self.assertFalse(checks["cases"]["auth"]["checks"]["git_baseline_preserved"])
        self.assertFalse(checks["cases"]["auth"]["fixture_passed"])
        summary = trials.summarize(self.run, self.checks_file(checks))
        self.assertFalse(summary["ready_for_review"])

    def test_stale_checks_rejected_after_source_changes(self):
        self.prepare()
        checks = self.checks_file(trials.verify(self.run))
        (self.run / "targets/auth/src/service.py").write_text(trials.source())
        with self.assertRaisesRegex(ValueError, "stale fixture"):
            trials.summarize(self.run, checks)

    def test_git_and_prompt_changes_also_invalidate_collected_checks(self):
        self.prepare()
        checks = self.checks_file(trials.verify(self.run))
        prompt = self.run / "prompts/audit.txt"
        original = prompt.read_bytes()
        prompt.write_bytes(original + b"Additional task\n")
        with self.assertRaisesRegex(ValueError, "stale fixture"):
            trials.summarize(self.run, checks)
        prompt.write_bytes(original)
        ref = self.run / "targets/audit/.git/refs/heads/trial"
        ref.write_text("0" * 40 + "\n")
        with self.assertRaisesRegex(ValueError, "stale fixture"):
            trials.summarize(self.run, checks)

    def test_unobserved_pass_and_cross_run_reports_are_rejected(self):
        self.prepare()
        checks = self.checks_file(trials.verify(self.run))
        results = trials.read_json(self.run / "results.json")
        results["cases"]["auth"]["axes"]["retrieval"]["status"] = "pass"
        self.save(self.run / "results.json", results)
        with self.assertRaisesRegex(ValueError, "notes and evidence"):
            trials.summarize(self.run, checks)
        results["run_id"] = "different-run"
        self.save(self.run / "results.json", results)
        with self.assertRaisesRegex(ValueError, "different run"):
            trials.summarize(self.run, checks)

    def test_bundle_contains_only_reports_and_explicit_evidence(self):
        self.prepare()
        checks = self.checks_file(trials.verify(self.run))
        results = trials.read_json(self.run / "results.json")
        (self.run / "evidence/receipt.txt").write_text("Operator-redacted receipt")
        (self.run / "evidence/do-not-include.txt").write_text("Unreferenced raw material")
        results["cases"]["audit"]["axes"]["correctness"] = {"status": "fail", "notes": "Synthetic harness observation", "evidence": ["evidence/receipt.txt"]}
        self.save(self.run / "results.json", results)
        output = self.root / "portable-results.zip"
        trials.bundle(self.run, checks, output)
        with zipfile.ZipFile(output) as archive:
            self.assertEqual(set(archive.namelist()), {"baselines.json", "results.json", "fixture-checks.json", "summary.json", "evidence/receipt.txt"})
        with self.assertRaisesRegex(ValueError, "already exists"):
            trials.bundle(self.run, checks, output)

    def test_record_with_observed_fields_ready_only_for_review(self):
        self.prepare()
        self.repair()
        checks = self.checks_file(trials.verify(self.run, True))
        results = trials.read_json(self.run / "results.json")
        (self.run / "evidence/receipt.txt").write_text("Synthetic validator fixture, not an IDE transcript.")
        for key in ["host_version", "agent_name", "agent_version", "surface", "model", "permissions"]:
            results["environment"][key] = "synthetic-test-value"
        for case in results["cases"].values():
            case.update(assisted=False, actual_method_revision=trials.suite()["default_method_revision"], retrieved_files=["START_HERE.md"])
            for axis in case["axes"].values():
                axis.update(status="pass", notes="Synthetic declared observation for schema test.", evidence=["evidence/receipt.txt"])
        self.save(self.run / "results.json", results)
        summary = trials.summarize(self.run, checks)
        self.assertTrue(summary["ready_for_review"])
        self.assertIn("not authenticated", summary["limits"])
        results["cases"]["auth"]["actual_method_revision"] = "0" * 40
        self.save(self.run / "results.json", results)
        with self.assertRaisesRegex(ValueError, "pinned revision"):
            trials.summarize(self.run, checks)

    def test_false_fixture_outcome_and_changed_prompt_rejected(self):
        self.prepare()
        checks = trials.verify(self.run)
        checks["cases"]["auth"]["fixture_passed"] = True
        with self.assertRaisesRegex(ValueError, "contradicts"):
            trials.summarize(self.run, self.checks_file(checks))
        (self.run / "prompts/audit.txt").write_text("Different prompt")
        checks = trials.verify(self.run)
        self.assertFalse(checks["cases"]["audit"]["checks"]["prompt_unchanged"])

    def test_linked_evidence_rejected_when_host_supports_links(self):
        self.prepare()
        outside = self.root / "outside.txt"
        outside.write_text("do not collect")
        link = self.run / "evidence/link.txt"
        try:
            link.symlink_to(outside)
        except OSError as exc:
            if exc.errno in {errno.EPERM, errno.EACCES, errno.ENOTSUP} or getattr(exc, "winerror", None) == 1314:
                self.skipTest("Host cannot create symlinks")
            raise
        with self.assertRaisesRegex(ValueError, "links/reparse"):
            trials.contained(self.run, "evidence/link.txt")

    def test_evidence_traversal_and_missing_evidence_are_rejected(self):
        self.prepare()
        checks = self.checks_file(trials.verify(self.run))
        results = trials.read_json(self.run / "results.json")
        outcome = results["cases"]["auth"]["axes"]["retrieval"]
        outcome.update(status="pass", notes="Claim without valid receipt", evidence=["evidence/../../outside.txt"])
        self.save(self.run / "results.json", results)
        with self.assertRaisesRegex(ValueError, "unsafe"):
            trials.summarize(self.run, checks)
        outcome["evidence"] = ["evidence/missing.txt"]
        self.save(self.run / "results.json", results)
        with self.assertRaises(FileNotFoundError):
            trials.summarize(self.run, checks)

    def test_cli_from_outside_checkout_reports_pending_as_json(self):
        extracted = self.root / "source ZIP without Git" / "field_trials"
        shutil.copytree(trials.HERE, extracted, ignore=shutil.ignore_patterns("__pycache__"))
        script = extracted / "run.py"
        result = subprocess.run([sys.executable, "-B", str(script), "prepare", "--host", "codex", "--output", str(self.run)],
                                cwd=self.root, capture_output=True, text=True, timeout=60)
        self.assertEqual(result.returncode, 0, result.stderr)
        result = subprocess.run([sys.executable, "-B", str(script), "verify", "--run", str(self.run)],
                                cwd=self.root, capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertEqual(json.loads(result.stdout)["agent_acceptance"], "not_scored")


if __name__ == "__main__":
    unittest.main()
