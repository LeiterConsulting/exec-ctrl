"""Second-pass regressions: resume semantics, Markdown, and hostile inputs."""

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import exec_ctrl as ec


class AdversarialTests(unittest.TestCase):
    def setUp(self):
        self.catalog = ec.load_catalog()

    def test_policy_argument_order_does_not_change_saved_record_validity(self):
        first = ec.read_json(ec.ROOT / "examples/v2/team-rules.json")
        second = copy.deepcopy(first)
        second["id"] = "second"
        second["gates"] = [{"id": "second-gate", "description": "Second obligation", "source": "fixture://second", "owner": "Fixture owner"}]
        record = ec.read_json(ec.ROOT / "examples/v2/docs-record.json")
        plan = ec.route(record["facts"], self.catalog, [first, second])
        record["rulesets"] = plan["rulesets"]
        record["gates"] = [{"id": gate, "result": "pass", "evidence": ["synthetic-review"], "reason": ""} for gate in plan["required_gates"]]
        self.assertTrue(ec.check_record(record, self.catalog, [second, first])["ready_to_close"])

    def test_duplicate_recorded_ruleset_identity_is_rejected(self):
        record = ec.read_json(ec.ROOT / "examples/v2/docs-record.json")
        identity = ec.rule_identity(ec.read_json(ec.ROOT / "examples/v2/team-rules.json"))
        record["rulesets"] = [identity, identity]
        with self.assertRaises(ec.Invalid):
            ec.check_record(record, self.catalog)

    def links(self, body, files=()):
        with tempfile.TemporaryDirectory(prefix="exec-ctrl-markdown-") as temp:
            root = Path(temp)
            (root / "README.md").write_text(body, encoding="utf-8")
            for name in files:
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("# Fixture\n", encoding="utf-8")
            return ec.check_links(root)

    def test_broken_full_reference_link_is_rejected(self):
        with self.assertRaises(ec.Invalid):
            self.links("[guide][ref]\n\n[ref]: missing.md\n")

    def test_reference_forms_and_case_whitespace_normalization(self):
        self.assertEqual(self.links("[Guide][doc name] [doc NAME][] [DOC name]\n\n[doc name]: exists.md\n", ["exists.md"]), 3)

    def test_reference_destination_can_be_on_next_line(self):
        self.assertEqual(self.links("[guide][ref]\n\n[ref]:\n  exists.md\n", ["exists.md"]), 1)

    def test_inline_code_and_comments_are_not_links(self):
        self.assertEqual(self.links("Use `[example](not-a-link.md)`.\n<!-- [x](missing.md) -->\n``[x](missing.md) ` literal``\n"), 0)

    def test_fenced_code_with_embedded_shorter_fence_is_not_links(self):
        self.assertEqual(self.links("````md\n```\n[x](missing.md)\n```\n````\n~~~\n[y](also-missing.md)\n~~~\n"), 0)

    def test_valid_inline_titles(self):
        for title in ['"A guide"', "'A guide'", "(A guide)"]:
            with self.subTest(title=title):
                self.assertEqual(self.links("[guide](exists.md " + title + ")", ["exists.md"]), 1)

    def test_angle_destinations_and_reference_titles(self):
        self.assertEqual(self.links('[guide](<with spaces.md> "title")\n[other][ref]\n\n[ref]: <with spaces.md> "title"\n', ["with spaces.md"]), 2)

    def test_balanced_and_escaped_parentheses_in_paths(self):
        self.assertEqual(self.links(r"[guide](exists(1).md) [other](exists\(1\).md)", ["exists(1).md"]), 2)

    def test_nested_labels_images_and_escaped_open_brackets(self):
        self.assertEqual(self.links(r"[a [nested] label](exists.md) ![image](exists.md) \[literal](missing.md)", ["exists.md"]), 2)

    def test_html_entities_and_percent_encoding_in_paths(self):
        self.assertEqual(self.links("[one](a&amp;b.md) [two](with%20spaces.md)", ["a&b.md", "with spaces.md"]), 2)

    def test_unused_reference_definition_is_not_a_link(self):
        self.assertEqual(self.links("ordinary prose\n\n[unused]: missing.md\n"), 0)

    def test_reference_path_escape_is_rejected(self):
        with self.assertRaises(ec.Invalid):
            self.links("[outside][ref]\n\n[ref]: ../outside.md\n")

    def test_first_reference_definition_wins(self):
        self.assertEqual(self.links("[ref]\n\n[ref]: exists.md\n[ref]: missing.md\n", ["exists.md"]), 1)

    def test_linked_image_checks_both_destinations(self):
        self.assertEqual(self.links("[![image](image.png)](exists.md)", ["image.png", "exists.md"]), 2)
        with self.assertRaises(ec.Invalid):
            self.links("[![image](missing.png)](exists.md)", ["exists.md"])

    def test_external_references_and_fragment_links_are_skipped(self):
        self.assertEqual(self.links("[external][ref] [local](#heading)\n\n[ref]: https://example.invalid/path\n"), 0)

    def test_json_exponent_overflow_is_rejected(self):
        with tempfile.TemporaryDirectory(prefix="exec-ctrl-json-") as temp:
            path = Path(temp) / "input.json"
            path.write_text('{"value": 1e10000}', encoding="utf-8")
            with self.assertRaises(ec.Invalid):
                ec.read_json(path)

    def test_oversized_json_is_rejected_before_parsing(self):
        with tempfile.TemporaryDirectory(prefix="exec-ctrl-json-") as temp:
            path = Path(temp) / "input.json"
            path.write_text(json.dumps({"value": "x" * (2 * 1024 * 1024)}), encoding="utf-8")
            with self.assertRaises(ec.Invalid):
                ec.read_json(path)

    def test_json_directory_is_rejected_as_input(self):
        with tempfile.TemporaryDirectory(prefix="exec-ctrl-json-") as temp:
            with self.assertRaises(ec.Invalid):
                ec.read_json(Path(temp))

    def test_json_exact_size_boundary_and_finite_numbers_are_accepted(self):
        with tempfile.TemporaryDirectory(prefix="exec-ctrl-json-") as temp:
            path = Path(temp) / "input.json"
            path.write_bytes(b"0" + b" " * (ec.MAX_JSON_BYTES - 1))
            self.assertEqual(ec.read_json(path), 0)
            path.write_text('[1.5, -1e-20, 1e300]', encoding="utf-8")
            self.assertEqual(ec.read_json(path), [1.5, -1e-20, 1e300])

    def test_cli_hostile_file_inputs_return_structured_errors(self):
        with tempfile.TemporaryDirectory(prefix="exec-ctrl-cli-") as temp:
            path = Path(temp) / "input.json"
            for payload in (b'\xff', b'{"v":1e10000}', b'[' * 2000 + b']' * 2000,
                            b'0' + b' ' * ec.MAX_JSON_BYTES):
                with self.subTest(size=len(payload), prefix=payload[:15]):
                    path.write_bytes(payload)
                    result = subprocess.run([sys.executable, "-B", str(ec.ROOT / "tools/exec_ctrl.py"),
                                             "check-record", str(path)], cwd=temp, capture_output=True,
                                            text=True, timeout=10)
                    self.assertEqual(result.returncode, 2)
                    self.assertFalse(json.loads(result.stderr)["valid"])
                    self.assertEqual(result.stdout, "")
                    self.assertNotIn("Traceback", result.stderr)

    def test_malformed_record_types_never_escape_as_unexpected_exceptions(self):
        base = ec.read_json(ec.ROOT / "examples/v2/docs-record.json")
        values = [None, True, False, 0, 1, 1.5, "", "unknown", [], {}, [None], {"id": "value"}]
        paths = [(key,) for key in base]
        paths += [("facts", key) for key in base["facts"]]
        paths += [("gates", 0, key) for key in base["gates"][0]]
        paths += [("evidence", 0, key) for key in base["evidence"][0]]
        for path in paths:
            for value in values:
                with self.subTest(path=path, value=value):
                    record = copy.deepcopy(base)
                    target = record
                    for segment in path[:-1]:
                        target = target[segment]
                    target[path[-1]] = value
                    try:
                        result = ec.check_record(record, self.catalog)
                        self.assertTrue(result["valid"])
                    except ec.Invalid:
                        pass


if __name__ == "__main__":
    unittest.main()
