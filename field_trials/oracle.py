"""Evaluator-only behavioral checks. Invoke only after reviewing target edits."""

import argparse
import importlib.util
import json
from pathlib import Path


def check(target, kind):
    spec = importlib.util.spec_from_file_location("trial_candidate", target / "src/service.py")
    candidate = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(candidate)
    checks = {}
    if kind in {"auth", "coverage"}:
        for name, tenant, invoice, allowed in [
            ("own_invoice", "alpha", {"tenant": "alpha", "amount": 42}, True),
            ("other_tenant", "beta", {"tenant": "alpha", "amount": 42}, False),
            ("anonymous", None, {"tenant": "alpha", "amount": 42}, False),
            ("empty_tenant", "", {"tenant": "alpha", "amount": 42}, False),
            ("missing_owner", "alpha", {"amount": 42}, False),
        ]:
            before = dict(invoice)
            try:
                value = candidate.read_invoice(tenant, invoice)
                checks[name] = allowed and value == 42
            except PermissionError as exc:
                checks[name] = not allowed and str(exc) == "access denied"
            checks[name + "_input_preserved"] = invoice == before
    if kind in {"auth", "coverage"}:
        for name, values, expected in [
            ("healthy", [True, True], "healthy"),
            ("degraded", [True, False], "degraded"),
            ("empty", [], "unknown"),
            ("unknown", [None], "unknown"),
            ("partial_healthy", [True, None], "unknown"),
            ("partial_failure", [False, None], "unknown"),
        ]:
            before = list(values)
            checks[name] = candidate.coverage(values) == expected
            checks[name + "_input_preserved"] = values == before
    return {"checks": checks, "passed": all(checks.values())}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path, required=True)
    parser.add_argument("--kind", choices=["auth", "coverage"], required=True)
    args = parser.parse_args()
    try:
        result = check(args.target, args.kind)
    except Exception as exc:
        result = {"passed": False, "error": type(exc).__name__ + ": " + str(exc)}
    print(json.dumps(result))
    raise SystemExit(0 if result["passed"] else 1)
