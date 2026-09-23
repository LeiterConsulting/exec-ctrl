# Functional correctness and logic discrepancies

Use for behavior changes, audits, or uncertain/high risk.

## Actions

- Trace the affected requirement through entry point, state transitions, callers,
  persistence, side effects and visible result. Compare implementation with the
  contract, tests and docs. Record disagreements instead of silently picking one.
- For each important discrepancy, capture expected behavior, observed/source
  behavior, location, reproduction or reasoning, impact, confidence and owner.
  A suspicious pattern is a hypothesis until supported by evidence.
- Check relevant boundaries: empty/malformed input, authorization, errors and
  cancellation, retry/idempotency, concurrency, partial writes, resource cleanup,
  time/unit conversions, stale caches and compatibility with existing callers.
- Choose tests at the cheapest level that proves the contract. A regression test
  should fail for the original bug; avoid tests that merely repeat implementation.
- Run affected established checks. Separate pre-existing failures from regressions
  using a baseline when feasible without altering user work. Never suppress a test
  or weaken an assertion to obtain a green result.
- Review the completed diff for accidental scope, duplicated business rules,
  dead paths, changed defaults and error handling. Check changed public contracts
  against downstream consumers and migration needs.

## Evidence and gate

`behavior`: acceptance criterion -> code path -> test or inspection evidence.
Record command, environment, revision and result; state what the evidence cannot
prove. UI, performance or physical-device requirements may need separate acceptance.
Use the [finding template](../templates/v2/FINDING.md) for material discrepancies.
