# Test coverage and publication checks

Use Python 3.10+ and the standard library. From the repository root:

```sh
python tools/exec_ctrl.py validate
python -m unittest discover -s tests -v
git diff --check
```

The existing [CI workflow](../.github/workflows/validate.yml) runs these checks on
Windows/Linux with Python 3.10 and 3.13, for pushes and pull requests. No package
installation, account, network service or production target is needed by the suite.
The test harness creates disposable local inputs and runs local Python processes;
the optional helper itself remains offline and read-only.

| Coverage | Behavior exercised |
| --- | --- |
| `test_exec_ctrl.py` | Routing, authority/risk facts, additive policy identity, evidence gates, closure denials, CLI exit codes |
| `test_adversarial.py` | Malformed JSON/type mutations, size limits, policy order and supported local Markdown links |
| `test_session_tools.py` | Pending records, typed evidence requirements, current-file snapshots, containment and resource bounds |
| `test_publication_readiness.py` | Complete disposable project workflow, all modes/modules through 94 routing cases, audited CLI behavior, history preservation and unstable capture |

## Reproducible project acceptance

The publication test creates a small Python service with a deliberate tenant-access
bug and two actual application tests. It records a pending auth fix with a fictional
policy requiring test evidence, observes the denial test fail, and checks that failed
evidence cannot pass the gate. The harness repairs only its disposable service, runs
the same application tests successfully, captures a new identity and supplies current
evidence. Old snapshots/subjects and changed policy content are rejected.

The helper is called as a real CLI from outside its own checkout, including a target
path with spaces. Existing project instructions and unfinished user notes retain their
bytes; no helper-generated files appear in the target. Passing fixture evidence is
explicitly synthetic acceptance, with no production approval or independent reviewer.
The deliberate application failure is an expected assertion inside a passing framework
test; it is not hidden by skipping a failed test.

## Offline/read-only execution and capture consistency

`audit_cli.py` is a test-only subprocess wrapper. It installs a Python audit hook
before running the helper and denies file mutations, process creation and socket
operations. All five helper commands and an invalid-input path run under it.
Separate probes verify that the guard rejects actual writes, directory creation,
process attempts and sockets. Executable-looking and URL evidence references remain
data. This is a regression guard for exercised paths, not a general host sandbox.

Deterministic capture tests edit the same-size content, truncate a file, and replace
or delete the selected path at read/close boundaries. They require an invalid result
and separately accept stable files immediately after repeated rewrites. Metadata
checks cannot establish an atomic multi-file snapshot or defeat every concurrent
writer; immutable inputs and closure comparison remain necessary.

Two symlink tests skip only when the host cannot create symlinks. Report skips
separately from passes and inspect hosted job logs before claiming those paths passed.
Capture mutation tests use controlled read boundaries, not timing-dependent sleeps.

## What remains a field gate

These tests validate the helper, catalog and supported links. The behavioral modules
also require an agent to inspect the real target and carry out their guidance. Offline
results cannot prove instruction retrieval, semantic defect detection, actual enterprise
policy compliance, connector authorization, independent approval or customer acceptance.
Use the [field-trial protocol](../docs/v2/FIELD_TRIALS.md) for task-plus-link adoption
and the [publication record](../docs/exec_ctrl/V2_PUBLICATION_READINESS.md) for this
increment's evidence. Keep earlier runs/versioned records unchanged.
