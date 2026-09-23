"""Behavior and failure-path coverage for the optional offline helper."""

import contextlib
import copy
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import exec_ctrl as ec


def facts(kind="docs", risk="low", signals=(), whole_project=False):
    return {"kind": kind, "risk": risk, "signals": list(signals), "whole_project": whole_project}


class FrameworkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = ec.load_catalog()

    def record(self):
        return ec.read_json(ec.ROOT / "examples/v2/docs-record.json")

    def rules(self):
        return ec.read_json(ec.ROOT / "examples/v2/team-rules.json")

    def assert_invalid_record(self, record, rules=()):
        with self.assertRaises(ec.Invalid):
            ec.check_record(record, self.catalog, rules)

    def test_typo_is_inline_and_only_loads_baseline_and_docs(self):
        plan = ec.route(facts(), self.catalog)
        self.assertEqual(plan["mode"], "inline")
        self.assertEqual([m["id"] for m in plan["modules"]], ["policy", "git", "documentation"])
        self.assertEqual(plan["required_gates"], ["scope", "policy", "verification", "review", "git-review", "documentation"])

    def test_fix_includes_behavior_and_diagnosis(self):
        plan = ec.route(facts("fix"), self.catalog)
        self.assertTrue({"behavior", "diagnosis", "git-review"} <= set(plan["required_gates"]))
        self.assertNotIn("security-review", plan["required_gates"])

    def test_auth_cannot_be_downgraded_by_low_risk_or_docs_label(self):
        plan = ec.route(facts(signals=["auth"]), self.catalog)
        self.assertEqual(plan["effective_risk"], "high")
        self.assertEqual(plan["mode"], "initiative")
        self.assertTrue({"behavior", "security-review"} <= set(plan["required_gates"]))

    def test_each_sensitive_signal_escalates(self):
        for signal in ["auth", "data", "payments", "production", "destructive"]:
            with self.subTest(signal=signal):
                plan = ec.route(facts(signals=[signal]), self.catalog)
                self.assertEqual(plan["effective_risk"], "high")
                self.assertIn("security-review", plan["required_gates"])

    def test_incident_and_migration_have_high_risk_even_if_low_declared(self):
        for kind in ["incident", "migration"]:
            with self.subTest(kind=kind):
                self.assertEqual(ec.route(facts(kind), self.catalog)["mode"], "initiative")

    def test_unknown_risk_does_not_default_to_low(self):
        plan = ec.route(facts(risk="unknown"), self.catalog)
        self.assertEqual(plan["mode"], "task")
        self.assertIn("security-review", plan["required_gates"])
        self.assertIn("behavior", plan["required_gates"])

    def test_project_requires_explicit_flag(self):
        self.assertEqual(ec.route(facts("planning"), self.catalog)["mode"], "task")
        self.assertEqual(ec.route(facts("planning", whole_project=True), self.catalog)["mode"], "project")

    def test_team_or_multiple_services_require_coordination(self):
        for signal in ["team", "multi-service"]:
            with self.subTest(signal=signal):
                self.assertEqual(ec.route(facts(signals=[signal]), self.catalog)["mode"], "initiative")

    def test_production_has_delivery_gate(self):
        self.assertIn("delivery-readiness", ec.route(facts(signals=["production"]), self.catalog)["required_gates"])

    def test_agent_tools_add_security_without_assuming_production(self):
        plan = ec.route(facts("fix", signals=["agent-tools"]), self.catalog)
        self.assertIn("security-review", plan["required_gates"])
        self.assertNotIn("delivery-readiness", plan["required_gates"])

    def test_selection_explains_reason(self):
        plan = ec.route(facts(signals=["ci"]), self.catalog)
        selected = {m["id"]: m for m in plan["modules"]}
        self.assertIn("signal:ci", selected["security"]["reasons"])
        self.assertEqual(selected["policy"]["reasons"], ["baseline"])

    def test_invalid_facts_rejected(self):
        mutations = [("risk", "safe"), ("signals", ["unknown-signal"]), ("signals", ["auth", "auth"]),
                     ("signals", "auth"), ("signals", [{}]), ("whole_project", "false"), ("kind", [])]
        for key, value in mutations:
            with self.subTest(key=key, value=value):
                data = facts()
                data[key] = value
                with self.assertRaises(ec.Invalid):
                    ec.route(data, self.catalog)

    def test_unrecognized_fact_cannot_silently_disable_security(self):
        data = facts()
        data["skip_security"] = True
        with self.assertRaises(ec.Invalid):
            ec.route(data, self.catalog)

    def test_rules_add_modules_and_gates(self):
        plan = ec.route(facts(), self.catalog, [self.rules()])
        self.assertEqual(plan["mode"], "task")
        self.assertTrue({"enterprise-policy", "security-review", "handoff", "org-independent-review", "org-license-review"} <= set(plan["required_gates"]))
        self.assertEqual(plan["rulesets"][0]["revision"], "fictional-1")

    def test_multiple_rulesets_compose(self):
        second = self.rules()
        second["id"] = "second"
        second["gates"] = [{"id": "org-data-retention", "description": "Retention reviewed", "source": "example://policy", "owner": "Example owner"}]
        plan = ec.route(facts(), self.catalog, [self.rules(), second])
        self.assertIn("org-data-retention", plan["required_gates"])
        self.assertIn("org-independent-review", plan["required_gates"])

    def test_rule_cannot_override_baseline_gate(self):
        rule = self.rules()
        rule["gates"][0]["id"] = "policy"
        with self.assertRaises(ec.Invalid):
            ec.route(facts(), self.catalog, [rule])

    def test_rule_cannot_remove_gates_or_change_risk(self):
        for key in ["remove_gates", "risk", "commands"]:
            with self.subTest(key=key):
                rule = self.rules()
                rule[key] = []
                with self.assertRaises(ec.Invalid):
                    ec.route(facts(), self.catalog, [rule])

    def test_rule_requires_known_modules_and_provenance(self):
        for key, value in [("required_modules", ["unknown"]), ("source", ""), ("owner", " "), ("revision", None), ("schema_version", True)]:
            with self.subTest(key=key):
                rule = self.rules()
                rule[key] = value
                with self.assertRaises(ec.Invalid):
                    ec.route(facts(), self.catalog, [rule])

    def test_duplicate_rules_or_gate_ids_rejected(self):
        with self.assertRaises(ec.Invalid):
            ec.route(facts(), self.catalog, [self.rules(), self.rules()])
        rule = self.rules()
        rule["id"] = "second"
        with self.assertRaises(ec.Invalid):
            ec.route(facts(), self.catalog, [self.rules(), rule])

    def test_valid_synthetic_record_is_structurally_ready(self):
        result = ec.check_record(self.record(), self.catalog)
        self.assertTrue(result["ready_to_close"])
        self.assertIn("Structure", result["limits"])

    def test_failure_cannot_be_called_complete(self):
        for status in ["fail", "blocked", "not_run", "not_applicable"]:
            with self.subTest(status=status):
                record = self.record()
                record["gates"][0].update(result=status, reason="Unresolved scope")
                self.assert_invalid_record(record)

    def test_in_progress_blocker_is_valid_but_not_ready(self):
        record = self.record()
        record["state"] = "in_progress"
        record["gates"][0].update(result="blocked", reason="Need scope decision")
        result = ec.check_record(record, self.catalog)
        self.assertFalse(result["ready_to_close"])
        self.assertEqual(result["unresolved_gates"], ["scope"])

    def test_nonpassing_gate_needs_reason(self):
        record = self.record()
        record["state"] = "blocked"
        record["gates"][0].update(result="blocked", reason="")
        self.assert_invalid_record(record)

    def test_non_git_scope_can_be_not_applicable(self):
        record = self.record()
        for gate in record["gates"]:
            if gate["id"] == "git-review":
                gate.update(result="not_applicable", evidence=[], reason="Illustrative target is not a Git repository")
        self.assertTrue(ec.check_record(record, self.catalog)["ready_to_close"])

    def test_missing_required_gate_rejected_even_before_completion(self):
        record = self.record()
        record["state"] = "in_progress"
        record["gates"].pop()
        self.assert_invalid_record(record)

    def test_new_risk_requires_new_gates(self):
        record = self.record()
        record["facts"]["signals"] = ["auth"]
        self.assert_invalid_record(record)

    def test_extra_product_acceptance_gate_blocks_close(self):
        record = self.record()
        record["gates"].append({"id": "live-acceptance", "result": "not_run", "evidence": [], "reason": "Runtime unavailable"})
        self.assert_invalid_record(record)

    def test_pass_without_evidence_is_invalid(self):
        record = self.record()
        record["gates"][0]["evidence"] = []
        self.assert_invalid_record(record)

    def test_pass_with_missing_evidence_is_invalid(self):
        record = self.record()
        record["gates"][0]["evidence"] = ["nonexistent"]
        self.assert_invalid_record(record)

    def test_pass_cannot_cite_failed_evidence(self):
        record = self.record()
        record["evidence"][0]["result"] = "fail"
        self.assert_invalid_record(record)

    def test_changed_subject_invalidates_passing_evidence(self):
        record = self.record()
        record["subject"] = "changed-dirty-snapshot"
        self.assert_invalid_record(record)

    def test_empty_or_duplicate_evidence_metadata_rejected(self):
        for key, value in [("summary", ""), ("reference", " "), ("kind", "guess"), ("result", "not_run")]:
            with self.subTest(key=key):
                record = self.record()
                record["evidence"][0][key] = value
                self.assert_invalid_record(record)
        record = self.record()
        record["evidence"].append(copy.deepcopy(record["evidence"][0]))
        self.assert_invalid_record(record)

    def test_duplicate_gates_rejected(self):
        record = self.record()
        record["gates"].append(copy.deepcopy(record["gates"][0]))
        self.assert_invalid_record(record)

    def test_record_version_and_unknown_fields_rejected(self):
        for key, value in [("framework_version", "1.0.0"), ("schema_version", True), ("state", "done"), ("waive_policy", True)]:
            with self.subTest(key=key):
                record = self.record()
                record[key] = value
                self.assert_invalid_record(record)

    def test_record_cannot_drop_recorded_ruleset_at_check_time(self):
        record = self.record()
        record["rulesets"] = [ec.rule_identity(self.rules())]
        self.assert_invalid_record(record)

    def test_rule_revision_change_invalidates_record_identity(self):
        rule = self.rules()
        record = self.record()
        record["rulesets"] = [ec.rule_identity(rule)]
        rule["revision"] = "changed-policy"
        self.assert_invalid_record(record, [rule])

    def test_ruleset_content_change_is_detected_even_with_same_revision(self):
        rule = self.rules()
        record = self.record()
        record["rulesets"] = [ec.rule_identity(rule)]
        rule["gates"][0]["description"] = "Materially changed obligation"
        with self.assertRaisesRegex(ec.Invalid, "content"):
            ec.check_record(record, self.catalog, [rule])

    def test_ruleset_hash_ignores_object_key_order(self):
        rule = self.rules()
        reordered = dict(reversed(list(rule.items())))
        self.assertEqual(ec.rule_identity(rule), ec.rule_identity(reordered))

    def test_unknown_policy_cannot_be_reported_passed(self):
        record = self.record()
        record["facts"]["signals"] = ["policy-unknown"]
        record["gates"].append({"id": "enterprise-policy", "result": "pass", "evidence": ["synthetic-review"], "reason": ""})
        with self.assertRaisesRegex(ec.Invalid, "unknown policy"):
            ec.check_record(record, self.catalog)
        record["state"] = "blocked"
        for gate in record["gates"]:
            if gate["id"] == "policy":
                gate.update(result="blocked", evidence=[], reason="Source inaccessible")
        self.assertFalse(ec.check_record(record, self.catalog)["ready_to_close"])

    def test_ruleset_record_requires_org_gates(self):
        rule = self.rules()
        record = self.record()
        plan = ec.route(record["facts"], self.catalog, [rule])
        record["rulesets"] = plan["rulesets"]
        self.assert_invalid_record(record, [rule])
        for gate in set(plan["required_gates"]) - {g["id"] for g in record["gates"]}:
            record["gates"].append({"id": gate, "result": "pass", "evidence": ["synthetic-review"], "reason": ""})
        self.assertTrue(ec.check_record(record, self.catalog, [rule])["ready_to_close"])

    def test_json_duplicate_keys_and_nonfinite_values_are_errors(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "input.json"
            for body in ['{"risk":"high","risk":"low"}', '{"value":NaN}', '{"x":Infinity}']:
                with self.subTest(body=body):
                    path.write_text(body, encoding="utf-8")
                    with self.assertRaises(ec.Invalid):
                        ec.read_json(path)

    def test_utf8_bom_json_is_accepted(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "input.json"
            path.write_text('{"value":1}', encoding="utf-8-sig")
            self.assertEqual(ec.read_json(path), {"value": 1})

    def test_catalog_rejects_unknown_trigger_and_baseline_removal(self):
        catalog = copy.deepcopy(self.catalog)
        catalog["modules"][0]["signals"] = ["imaginary"]
        with self.assertRaises(ec.Invalid):
            ec.validate_catalog(catalog)
        catalog = copy.deepcopy(self.catalog)
        catalog["modules"][0]["always"] = False
        with self.assertRaises(ec.Invalid):
            ec.validate_catalog(catalog)

    def test_catalog_rejects_gate_collisions(self):
        catalog = copy.deepcopy(self.catalog)
        catalog["modules"][0]["gates"] = ["scope"]
        with self.assertRaises(ec.Invalid):
            ec.validate_catalog(catalog)

    def test_local_file_cannot_escape_repository(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "repo"
            root.mkdir()
            (root.parent / "outside.md").write_text("outside", encoding="utf-8")
            with self.assertRaises(ec.Invalid):
                ec.local_file(root, "../outside.md")

    def test_link_check_handles_code_external_and_encoded_paths(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "with spaces.md").write_text("# Good\n", encoding="utf-8")
            (root / "README.md").write_text("[a](with%20spaces.md#good)\n[web](https://example.com/missing)\n```md\n[x](missing.md)\n```", encoding="utf-8")
            self.assertEqual(ec.check_links(root), 1)
            (root / "broken.md").write_text("[x](missing.md)", encoding="utf-8")
            with self.assertRaises(ec.Invalid):
                ec.check_links(root)

    def test_cli_exit_codes_and_output(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "record.json"
            record = self.record()
            for expected, state, result in [(0, "complete", "pass"), (1, "blocked", "blocked"), (2, "complete", "blocked")]:
                with self.subTest(expected=expected):
                    record["state"] = state
                    record["gates"][0].update(result=result, reason="Test blocker" if result != "pass" else "")
                    path.write_text(json.dumps(record), encoding="utf-8")
                    out, err = io.StringIO(), io.StringIO()
                    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                        code = ec.main(["check-record", str(path)])
                    self.assertEqual(code, expected)
                    self.assertIsInstance(json.loads(out.getvalue() or err.getvalue()), dict)

    def test_cli_malformed_input_reports_json_error_without_traceback(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "bad.json"
            for body in ["[]", "null", "{bad json", '{"schema_version": 1}']:
                with self.subTest(body=body):
                    path.write_text(body, encoding="utf-8")
                    err = io.StringIO()
                    with contextlib.redirect_stderr(err):
                        code = ec.main(["check-record", str(path)])
                    self.assertEqual(code, 2)
                    self.assertFalse(json.loads(err.getvalue())["valid"])

    def test_cli_invocation_works_from_another_directory_and_is_read_only(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            sentinel = root / "do-not-touch.txt"
            sentinel.write_text("user work", encoding="utf-8")
            result = subprocess.run([sys.executable, "-B", str(ec.ROOT / "tools/exec_ctrl.py"), "route", "--kind", "docs", "--risk", "low"], cwd=root, capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["mode"], "inline")
            self.assertEqual(list(root.iterdir()), [sentinel])
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "user work")

    def test_references_are_data_and_never_executed(self):
        record = self.record()
        with tempfile.TemporaryDirectory() as temp:
            marker = Path(temp) / "should-not-exist"
            record["evidence"][0]["reference"] = "$(touch " + str(marker) + ")"
            ec.check_record(record, self.catalog)
            self.assertFalse(marker.exists())


if __name__ == "__main__":
    unittest.main()
