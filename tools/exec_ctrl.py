#!/usr/bin/env python3
"""Offline, read-only assistance for exec-ctrl. Never executes record content."""

import argparse
import hashlib
import html
import json
import math
import os
import re
import stat
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MAX_JSON_BYTES = 2 * 1024 * 1024
MAX_SNAPSHOT_FILES = 256
MAX_SNAPSHOT_FILE_BYTES = 16 * 1024 * 1024
MAX_SNAPSHOT_TOTAL_BYTES = 64 * 1024 * 1024
STATES = {"not_started", "in_progress", "blocked", "complete", "deferred"}
RESULTS = {"pass", "fail", "blocked", "not_run", "not_applicable"}
EVIDENCE_KINDS = {"inspection", "test", "build", "deployment", "live", "review"}
SNAPSHOT_LIMITS = "Explicit files only; excludes unlisted inputs and environment state. Per-file reads, not an atomic repository snapshot."


class Invalid(ValueError):
    """Invalid input, including ambiguous or unsupported fields."""


def require(condition, message):
    if not condition:
        raise Invalid(message)


def object_fields(value, required, optional=()):
    require(isinstance(value, dict), "expected an object")
    require(set(required) <= value.keys(), "missing required fields: " + ", ".join(sorted(set(required) - value.keys())))
    require(value.keys() <= set(required) | set(optional), "unsupported fields: " + ", ".join(sorted(value.keys() - set(required) - set(optional))))


def nonempty(value, label):
    require(isinstance(value, str) and bool(value.strip()), label + " must be a nonempty string")
    return value


def strings(value, label):
    require(isinstance(value, list), label + " must be a list")
    for item in value:
        nonempty(item, label)
    require(len(set(value)) == len(value), label + " contains duplicates")
    return value


def choice(value, choices, label):
    nonempty(value, label)
    require(value in choices, label + " has an unsupported value")


def unique_objects(items, label):
    require(isinstance(items, list), label + " must be a list")
    ids = []
    for item in items:
        require(isinstance(item, dict), label + " must contain objects")
        ids.append(nonempty(item.get("id"), label + " id"))
    require(len(ids) == len(set(ids)), label + " contains duplicate IDs")


def read_json(path):
    def no_duplicates(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, "duplicate JSON key")
            result[key] = value
        return result

    def no_constant(value):
        raise Invalid("non-finite JSON number")

    def finite_float(value):
        number = float(value)
        require(math.isfinite(number), "non-finite JSON number")
        return number

    source = Path(path)
    require(source.is_file(), "JSON input must be a regular file")
    with source.open("rb") as stream:
        payload = stream.read(MAX_JSON_BYTES + 1)
    require(len(payload) <= MAX_JSON_BYTES, "JSON input exceeds 2 MiB limit")
    return json.loads(payload.decode("utf-8-sig"), object_pairs_hook=no_duplicates,
                      parse_constant=no_constant, parse_float=finite_float)


def local_file(root, name):
    nonempty(name, "local path")
    require(not Path(name).is_absolute() and "\\" not in name, "expected repository-relative POSIX path")
    path = (root / name).resolve()
    require(path.is_relative_to(root.resolve()), "path escapes repository")
    require(path.is_file(), "referenced file does not exist: " + name)
    return path


def snapshot(target, names):
    """Hash only explicitly selected local files, never discover or execute inputs."""
    def metadata_key(metadata):
        result = (metadata.st_dev, metadata.st_ino, metadata.st_size, metadata.st_mtime_ns)
        # Windows path stat and descriptor stat can report different ctime values
        # for the same unchanged file. Compare modification time and file ID there.
        return result if os.name == "nt" else result + (metadata.st_ctime_ns,)

    root = Path(target).resolve()
    require(root.is_dir(), "snapshot target must be a directory")
    strings(names, "snapshot paths")
    require(0 < len(names) <= MAX_SNAPSHOT_FILES, "snapshot requires 1 to 256 files")
    files = []
    seen = set()
    total = 0
    for name in names:
        path = local_file(root, name)
        candidate = root / name
        require(".." not in Path(name).parts and candidate.absolute() == path,
                "snapshot paths cannot contain parent traversal, symbolic links or redirected directories")
        require(path not in seen, "snapshot contains aliases of the same file")
        seen.add(path)
        before = path.stat()
        require(before.st_size <= MAX_SNAPSHOT_FILE_BYTES, "snapshot file exceeds 16 MiB limit")
        require(total + before.st_size <= MAX_SNAPSHOT_TOTAL_BYTES, "snapshot exceeds 64 MiB total limit")
        changed = "snapshot input changed during capture: " + name
        digest = hashlib.sha256()
        size = 0
        with path.open("rb") as stream:
            opened = os.fstat(stream.fileno())
            require(stat.S_ISREG(opened.st_mode) and metadata_key(before) == metadata_key(opened), changed)
            while True:
                chunk = stream.read(1024 * 1024)
                if not chunk:
                    break
                size += len(chunk)
                total += len(chunk)
                require(size <= MAX_SNAPSHOT_FILE_BYTES, "snapshot file exceeds 16 MiB limit")
                require(total <= MAX_SNAPSHOT_TOTAL_BYTES, "snapshot exceeds 64 MiB total limit")
                digest.update(chunk)
            require(size == before.st_size and metadata_key(before) == metadata_key(os.fstat(stream.fileno())), changed)
        try:
            require(candidate.resolve(strict=True) == path and metadata_key(before) == metadata_key(path.stat()), changed)
        except OSError as exc:
            raise Invalid(changed) from exc
        files.append({"path": path.relative_to(root).as_posix(), "sha256": digest.hexdigest(), "bytes": size})
    files.sort(key=lambda item: item["path"])
    identity = json.dumps(files, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return {"schema_version": 1, "subject": "sha256:" + hashlib.sha256(identity.encode("utf-8")).hexdigest(),
            "files": files, "limits": SNAPSHOT_LIMITS}


def check_snapshot(manifest, target):
    object_fields(manifest, {"schema_version", "subject", "files", "limits"})
    require(type(manifest["schema_version"]) is int and manifest["schema_version"] == 1, "unsupported snapshot schema")
    nonempty(manifest["subject"], "snapshot subject")
    require(manifest["limits"] == SNAPSHOT_LIMITS, "snapshot scope limits changed")
    require(isinstance(manifest["files"], list), "snapshot files must be a list")
    require(0 < len(manifest["files"]) <= MAX_SNAPSHOT_FILES, "snapshot requires 1 to 256 files")
    paths = []
    for item in manifest["files"]:
        object_fields(item, {"path", "sha256", "bytes"})
        paths.append(nonempty(item["path"], "snapshot path"))
        require(isinstance(item["sha256"], str) and re.fullmatch(r"[0-9a-f]{64}", item["sha256"]), "invalid file digest")
        require(type(item["bytes"]) is int and 0 <= item["bytes"] <= MAX_SNAPSHOT_FILE_BYTES, "invalid snapshot file size")
    current = snapshot(target, paths)
    require(sorted(manifest["files"], key=lambda item: item["path"]) == current["files"], "snapshot files changed or manifest is inconsistent")
    require(manifest["subject"] == current["subject"], "snapshot subject does not match current files")
    return current["subject"]


def validate_catalog(catalog, root=ROOT):
    object_fields(catalog, {"schema_version", "framework_version", "entry", "kinds", "risks", "signals", "high_risk_signals", "base_gates", "modules"})
    require(type(catalog["schema_version"]) is int and catalog["schema_version"] == 1, "unsupported catalog schema")
    nonempty(catalog["framework_version"], "framework version")
    for key in ("kinds", "risks", "signals", "high_risk_signals", "base_gates"):
        strings(catalog[key], key)
    require(set(catalog["risks"]) == {"low", "medium", "high", "unknown"}, "risk vocabulary drift")
    require(set(catalog["high_risk_signals"]) <= set(catalog["signals"]), "unknown high-risk signal")
    require(set(catalog["base_gates"]) == {"scope", "policy", "verification", "review"}, "baseline gate drift")
    local_file(root, catalog["entry"])
    unique_objects(catalog["modules"], "modules")
    module_ids = {m["id"] for m in catalog["modules"]}
    require({"policy", "git", "enterprise"} <= module_ids, "missing baseline modules")
    gates = list(catalog["base_gates"])
    for module in catalog["modules"]:
        object_fields(module, {"id", "path", "always", "kinds", "signals", "risks", "gates"})
        require(type(module["always"]) is bool, "always must be boolean")
        if module["id"] in {"policy", "git"}:
            require(module["always"], "baseline modules must always apply")
        for field in ("kinds", "signals", "risks"):
            require(set(strings(module[field], field)) <= set(catalog[field]), "unknown module trigger")
        gates.extend(strings(module["gates"], "gates"))
        local_file(root, module["path"])
    require(len(gates) == len(set(gates)), "duplicate catalog gate")
    return catalog


def load_catalog(root=ROOT):
    return validate_catalog(read_json(root / "framework/catalog.json"), root)


def validate_facts(facts, catalog):
    object_fields(facts, {"kind", "risk", "signals", "whole_project"})
    choice(facts["kind"], catalog["kinds"], "kind")
    choice(facts["risk"], catalog["risks"], "risk")
    require(set(strings(facts["signals"], "signals")) <= set(catalog["signals"]), "unknown signal")
    require(type(facts["whole_project"]) is bool, "whole_project must be boolean")


def validate_rules(rules, catalog):
    unique_objects(rules, "rulesets")
    module_ids = {m["id"] for m in catalog["modules"]}
    gate_ids = set(catalog["base_gates"])
    gate_ids.update(g for m in catalog["modules"] for g in m["gates"])
    for rule in rules:
        object_fields(rule, {"schema_version", "id", "source", "revision", "owner", "required_modules", "gates"})
        require(type(rule["schema_version"]) is int and rule["schema_version"] == 1, "unsupported ruleset schema")
        for key in ("id", "source", "revision", "owner"):
            nonempty(rule[key], "ruleset " + key)
        require(set(strings(rule["required_modules"], "required_modules")) <= module_ids, "unknown required module")
        unique_objects(rule["gates"], "policy gates")
        for gate in rule["gates"]:
            object_fields(gate, {"id", "description", "source", "owner"}, {"requires"})
            for key in ("id", "description", "source", "owner"):
                nonempty(gate[key], "policy gate " + key)
            require(set(strings(gate.get("requires", []), "policy evidence requirements")) <= EVIDENCE_KINDS, "unknown policy evidence kind")
            require(gate["id"] not in gate_ids, "policy gate collides with another gate")
            gate_ids.add(gate["id"])


def rule_identity(rule):
    """Bind the declared source/revision to normalized content, not just a label."""
    identity = {key: rule[key] for key in ("id", "source", "revision", "owner")}
    payload = json.dumps(rule, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    identity["sha256"] = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    return identity


def route(facts, catalog, rules=()):
    validate_facts(facts, catalog)
    rules = list(rules)
    validate_rules(rules, catalog)
    signals = set(facts["signals"])
    high = signals & set(catalog["high_risk_signals"])
    risk = "high" if high or facts["kind"] in {"incident", "migration"} else facts["risk"]
    forced = {m for rule in rules for m in rule["required_modules"]}
    if rules:
        forced.add("enterprise")
    selected = []
    gates = list(catalog["base_gates"])
    for module in catalog["modules"]:
        reasons = []
        if module["always"]:
            reasons.append("baseline")
        if facts["kind"] in module["kinds"]:
            reasons.append("task:" + facts["kind"])
        reasons.extend("signal:" + s for s in sorted(signals & set(module["signals"])))
        if risk in module["risks"]:
            reasons.append("risk:" + risk)
        if module["id"] in forced:
            reasons.append("ruleset")
        if reasons:
            selected.append({"id": module["id"], "path": module["path"], "reasons": reasons})
            gates.extend(module["gates"])
    gates.extend(gate["id"] for rule in rules for gate in rule["gates"])
    if facts["whole_project"]:
        mode = "project"
    elif risk == "high" or signals & {"team", "multi-service"}:
        mode = "initiative"
    elif risk == "low" and facts["kind"] in {"docs", "fix"} and not rules and not signals:
        mode = "inline"
    else:
        mode = "task"
    return {"framework_version": catalog["framework_version"], "mode": mode,
            "effective_risk": risk, "modules": selected, "required_gates": gates,
            "gate_requirements": {g["id"]: g["requires"] for r in rules for g in r["gates"] if g.get("requires")},
            "rulesets": [rule_identity(r) for r in rules],
            "limits": "Declared facts only; no repository inspection, enforcement, or evidence truth verification."}


def record_template(facts, catalog, identifier, objective, subject, rules=()):
    """Generate pending obligations, never synthetic passes or execution commands."""
    for value, label in ((identifier, "id"), (objective, "objective"), (subject, "subject")):
        nonempty(value, label)
    plan = route(facts, catalog, rules)
    gates = []
    for gate_id in plan["required_gates"]:
        gate = {"id": gate_id, "result": "not_run", "evidence": [], "reason": "Pending scoped verification"}
        if gate_id in plan["gate_requirements"]:
            gate["requires"] = list(plan["gate_requirements"][gate_id])
        gates.append(gate)
    return {"schema_version": 1, "framework_version": catalog["framework_version"],
            "id": identifier, "objective": objective, "subject": subject, "state": "not_started",
            "facts": {**facts, "signals": list(facts["signals"])},
            "rulesets": plan["rulesets"], "gates": gates, "evidence": []}


def check_record(record, catalog, rules=(), expected_subject=None):
    object_fields(record, {"schema_version", "framework_version", "id", "objective", "subject", "state", "facts", "rulesets", "gates", "evidence"})
    require(type(record["schema_version"]) is int and record["schema_version"] == 1, "unsupported record schema")
    require(record["framework_version"] == catalog["framework_version"], "framework version mismatch")
    for key in ("id", "objective", "subject"):
        nonempty(record[key], key)
    if expected_subject is not None:
        require(record["subject"] == nonempty(expected_subject, "expected subject"), "record subject does not match current snapshot")
    choice(record["state"], STATES, "state")
    plan = route(record["facts"], catalog, rules)
    unique_objects(record["rulesets"], "record rulesets")
    require({r["id"]: r for r in record["rulesets"]} == {r["id"]: r for r in plan["rulesets"]},
            "record rulesets do not match supplied ruleset identities/revisions/content")
    unique_objects(record["evidence"], "evidence")
    evidence = {}
    for item in record["evidence"]:
        object_fields(item, {"id", "kind", "subject", "result", "reference", "summary"})
        choice(item["kind"], EVIDENCE_KINDS, "evidence kind")
        choice(item["result"], {"pass", "fail"}, "evidence result")
        for key in ("subject", "reference", "summary"):
            nonempty(item[key], "evidence " + key)
        evidence[item["id"]] = item
    unique_objects(record["gates"], "gates")
    present = {g["id"] for g in record["gates"]}
    require(set(plan["required_gates"]) <= present, "record is missing required gates")
    unresolved = []
    for gate in record["gates"]:
        object_fields(gate, {"id", "result", "evidence", "reason"}, {"requires"})
        kinds = set(strings(gate.get("requires", []), "gate evidence requirements"))
        require(kinds <= EVIDENCE_KINDS, "unknown gate evidence kind")
        kinds.update(plan["gate_requirements"].get(gate["id"], []))
        choice(gate["result"], RESULTS, "gate result")
        refs = strings(gate["evidence"], "gate evidence")
        require(set(refs) <= evidence.keys(), "gate refers to missing evidence")
        require(isinstance(gate["reason"], str), "gate reason must be a string")
        if gate["id"] == "policy" and "policy-unknown" in record["facts"]["signals"]:
            require(gate["result"] in {"fail", "blocked", "not_run"}, "unknown policy cannot have a passing policy gate")
        if gate["result"] == "pass":
            require(bool(refs), "passing gate requires evidence")
            require(all(evidence[e]["result"] == "pass" for e in refs), "passing gate cites failed evidence")
            require(all(evidence[e]["subject"] == record["subject"] for e in refs), "passing gate cites stale/different subject evidence")
            require(kinds <= {evidence[e]["kind"] for e in refs}, "passing gate is missing required evidence kinds: " + gate["id"])
        else:
            nonempty(gate["reason"], "nonpassing gate reason")
            if gate["result"] != "not_applicable" or gate["id"] != "git-review":
                unresolved.append(gate["id"])
    require(record["state"] != "complete" or not unresolved, "complete record has unresolved gates")
    return {"valid": True, "state": record["state"], "ready_to_close": not unresolved,
            "unresolved_gates": unresolved, "route": plan,
            "limits": "Structure and declared subject consistency only; evidence content, policy authority and actual risk require review."}


def markdown_text(value):
    """Decode Markdown punctuation escapes and HTML entities in destinations."""
    return html.unescape(re.sub(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\]\\^_`{|}~])", r"\1", value))


def prose_only(body):
    """Mask fenced code, inline code and comments while preserving line positions."""
    def blank(value):
        return re.sub(r"[^\n]", " ", value)

    lines = []
    fence = None
    for line in body.splitlines(keepends=True):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line.rstrip("\r\n"))
        if fence:
            lines.append(blank(line))
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
                fence = None
        elif marker and not (marker[1][0] == "`" and "`" in marker[2]):
            fence = marker[1]
            lines.append(blank(line))
        else:
            lines.append(line)
    body = re.sub(r"<!--.*?(?:-->|\Z)", lambda m: blank(m[0]), "".join(lines), flags=re.S)
    parts = []
    start = 0
    cursor = 0
    while cursor < len(body):
        if body[cursor] == "\\":
            cursor += 2
            continue
        if body[cursor] != "`":
            cursor += 1
            continue
        end = cursor
        while end < len(body) and body[end] == "`":
            end += 1
        close = re.search(r"(?<!`)" + re.escape(body[cursor:end]) + r"(?!`)", body[end:])
        if close:
            stop = end + close.end()
            parts.extend((body[start:cursor], blank(body[cursor:stop])))
            start = cursor = stop
        else:
            cursor = end
    return "".join(parts) + body[start:]


def markdown_destination(body, start):
    """Return a destination and its end, or None for malformed syntax."""
    cursor = start
    angle = body[start:start + 1] == "<"
    if angle:
        cursor += 1
        start = cursor
    depth = 0
    while cursor < len(body):
        char = body[cursor]
        if char == "\\" and cursor + 1 < len(body):
            cursor += 2
            continue
        if angle:
            if char == ">":
                return body[start:cursor], cursor + 1
            if char in "\n<":
                return None
        else:
            if char.isspace():
                break
            if char == "(":
                depth += 1
            elif char == ")":
                if not depth:
                    break
                depth -= 1
        cursor += 1
    if angle or depth:
        return None
    return body[start:cursor], cursor


def markdown_tail(body, cursor):
    """Skip whitespace and an optional quoted or parenthesized link title."""
    start = cursor
    while cursor < len(body) and body[cursor].isspace():
        cursor += 1
    if cursor > start and body[cursor:cursor + 1] in {'"', "'", "("}:
        closing = ")" if body[cursor] == "(" else body[cursor]
        cursor += 1
        while cursor < len(body):
            if body[cursor] == "\\":
                cursor += 2
            elif body[cursor] == closing:
                cursor += 1
                while cursor < len(body) and body[cursor].isspace():
                    cursor += 1
                return cursor
            else:
                cursor += 1
        return None
    return cursor


def bracket_end(body, start):
    depth = 1
    cursor = start + 1
    while cursor < len(body):
        if body[cursor] == "\\":
            cursor += 2
            continue
        if body[cursor] == "[":
            depth += 1
        elif body[cursor] == "]":
            depth -= 1
            if not depth:
                return cursor
        cursor += 1
    return None


def markdown_destinations(body):
    """Extract supported inline/image and full/collapsed/shortcut reference links.

    This is a repository link checker, not a full CommonMark renderer. HTML links,
    indented code and block-container parsing are outside its supported syntax.
    """
    body = prose_only(body)
    references = {}

    def label(value):
        return " ".join(markdown_text(value).split()).casefold()

    def definition(match):
        parsed = markdown_destination(match[2], 0)
        if parsed:
            target, end = parsed
            tail = markdown_tail(match[2], end)
            if target and tail == len(match[2]):
                references.setdefault(label(match[1]), target)
                return "\n" * match[0].count("\n")
        return match[0]

    body = re.sub(r"^ {0,3}\[([^\]\n]+)\]:[ \t]*(?:\n[ \t]*)?([^\n]+)$", definition, body, flags=re.M)

    def scan(text):
        cursor = 0
        while cursor < len(text):
            if text[cursor] == "\\":
                cursor += 2
                continue
            if text[cursor] != "[":
                cursor += 1
                continue
            end = bracket_end(text, cursor)
            if end is None:
                cursor += 1
                continue
            caption = text[cursor + 1:end]
            stop = end + 1
            target = None
            if text[stop:stop + 1] == "(":
                start = stop + 1
                while start < len(text) and text[start].isspace():
                    start += 1
                parsed = markdown_destination(text, start)
                if parsed:
                    candidate, pos = parsed
                    tail = markdown_tail(text, pos)
                    if tail is not None and text[tail:tail + 1] == ")":
                        target, stop = candidate, tail + 1
            elif text[stop:stop + 1] == "[":
                ref_end = bracket_end(text, stop)
                if ref_end is not None:
                    key = text[stop + 1:ref_end] or caption
                    target = references.get(label(key))
                    stop = ref_end + 1
            else:
                target = references.get(label(caption))
            if target is not None:
                yield markdown_text(target)
            # Images inside a linked label have their own destinations.
            if "[" in caption:
                yield from scan(caption)
            cursor = stop

    yield from scan(body)


def check_links(root):
    """Check supported local Markdown destinations, excluding external URLs."""
    checked = 0
    for path in root.rglob("*.md"):
        if any(part in {".git", "__pycache__", ".venv"} for part in path.relative_to(root).parts):
            continue
        require(path.resolve().is_relative_to(root.resolve()), "Markdown source escapes repository: " + str(path.relative_to(root)))
        for target in markdown_destinations(path.read_text(encoding="utf-8-sig")):
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            name = unquote(url.path)
            dest = (path.parent / name).resolve()
            require(dest.is_relative_to(root.resolve()), "Markdown link escapes repository: " + str(path.relative_to(root)))
            require(dest.exists(), "broken Markdown link in " + str(path.relative_to(root)) + ": " + name)
            checked += 1
    return checked


def validate_repository(root=ROOT):
    catalog = load_catalog(root)
    version = (root / "VERSION").read_text(encoding="utf-8").strip()
    require(version == catalog["framework_version"], "VERSION/catalog mismatch")
    readme = (root / "README.md").read_text(encoding="utf-8")
    require("**" + version + "**" in readme, "README version mismatch")
    changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8")
    latest = re.search(r"^## ([^\s]+)(?:[ \t].*)?$", changelog, flags=re.M)
    require(latest is not None and latest[1] == version, "latest changelog version mismatch")
    entry = (root / catalog["entry"]).read_text(encoding="utf-8")
    require(version in entry, "entry version mismatch")
    require(len(entry.split()) <= 1700, "activation contract exceeds 1700-word budget")
    for module in catalog["modules"]:
        require(module["path"] in entry, "entry does not link module: " + module["id"])
    for name in ("README.md", "AGENTS.md", ".github/copilot-instructions.md"):
        require("START_HERE.md" in local_file(root, name).read_text(encoding="utf-8"), "entry route missing: " + name)
    require((root / "CLAUDE.md").read_text(encoding="utf-8").strip() == "@AGENTS.md", "Claude adapter drift")
    require({p.relative_to(root).as_posix() for p in (root / "modules").glob("*.md")} == {m["path"] for m in catalog["modules"]}, "uncatalogued or missing module")
    example_rules = [read_json(root / "examples/v2/team-rules.json"), read_json(root / "examples/v2/release-rules.json")]
    validate_rules(example_rules, catalog)
    check_record(read_json(root / "examples/v2/docs-record.json"), catalog)
    check_record(read_json(root / "examples/v2/pending-release-record.json"), catalog, [example_rules[1]])
    checked = check_links(root)
    return {"valid": True, "version": version, "modules": len(catalog["modules"]), "local_links_checked": checked,
            "limits": "Catalog, release metadata, examples and supported local links only; external URLs, anchors and actual agent behavior are not verified."}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("validate", help="check framework catalog, entry coherence and local links")
    for name, help_text in [("route", "route explicit facts; does not inspect a target repository"),
                            ("record-template", "generate a pending record on stdout from explicit facts")]:
        routing = commands.add_parser(name, help=help_text)
        routing.add_argument("--kind", required=True)
        routing.add_argument("--risk", default="unknown")
        routing.add_argument("--signal", action="append", default=[])
        routing.add_argument("--whole-project", action="store_true")
        routing.add_argument("--rules", action="append", default=[])
        if name == "record-template":
            routing.add_argument("--id", required=True)
            routing.add_argument("--objective", required=True)
            routing.add_argument("--subject", required=True)
    hashing = commands.add_parser("snapshot", help="hash explicitly selected files; prints a manifest without writing files")
    hashing.add_argument("--target", required=True)
    hashing.add_argument("--path", action="append", required=True)
    checking = commands.add_parser("check-record", help="validate declared completion evidence")
    checking.add_argument("record")
    checking.add_argument("--rules", action="append", default=[])
    checking.add_argument("--snapshot", help="explicit manifest to compare with current target files")
    checking.add_argument("--target", help="target root used together with --snapshot")
    args = parser.parse_args(argv)
    try:
        if args.command == "validate":
            result = validate_repository()
        elif args.command == "snapshot":
            result = snapshot(args.target, args.path)
        else:
            catalog = load_catalog()
            rules = [read_json(p) for p in args.rules]
            if args.command in {"route", "record-template"}:
                facts = {"kind": args.kind, "risk": args.risk,
                         "signals": args.signal, "whole_project": args.whole_project}
                result = route(facts, catalog, rules) if args.command == "route" else record_template(
                    facts, catalog, args.id, args.objective, args.subject, rules)
            else:
                require(bool(args.snapshot) == bool(args.target), "--snapshot and --target must be supplied together")
                subject = check_snapshot(read_json(args.snapshot), args.target) if args.snapshot else None
                result = check_record(read_json(args.record), catalog, rules, expected_subject=subject)
        print(json.dumps(result, indent=2))
        if args.command == "check-record" and not result["ready_to_close"]:
            return 1
        return 0
    except (Invalid, OSError, ValueError, RecursionError) as exc:
        print(json.dumps({"valid": False, "error": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
