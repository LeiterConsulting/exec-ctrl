# v2 publication readiness

Started: 2026-10-05. Baseline: `2b9cfbd`, clean `main`, preview 3.
Method and target: this repository. Branch: `codex/publication-readiness`.
User scope: put tests in place, execute and improve the framework, iterate on
failures, and prepare a main-merge candidate before use in a real project.
Implementation/local acceptance: `complete`. Hosted verification/publication:
`complete` for the tested code below. Main merge: `not_performed`.

## Scope and acceptance

- Keep the link-first entry small and the optional helper Python 3.10+, stdlib,
  offline and read-only; add no adoption writes or production integrations.
- Put a complete synthetic project/evidence lifecycle in the repository's normal
  unittest/CI path, making it reproducible outside the author's separate local lab.
- Cover failure/repair, stale inputs, policy changes, user-work preservation and
  forbidden helper side effects. Prove discovered defects fail before the repair.
- Keep versions, catalog, examples and documentation coherent; preserve historical
  records and explicit limitations. Review the final diff and published revision.
- Run repository validation, all tests and diff checks locally and on the hosted
  Windows/Linux Python 3.10/3.13 matrix. Prepare a PR; main merge remains pending.

## Findings and repair evidence

| Finding | Reproduction and correction |
| --- | --- |
| Snapshot capture accepted files edited during hashing | Same-size edit and truncation tests both failed against preview 3 because no invalid result was raised. Compare opened-file identity/size/modification metadata before and after reading. |
| Capture accepted a replaced path after the read | Replacement at the close boundary also failed against preview 3. Re-resolve and compare path identity after close; deletion likewise returns invalid input. |
| Windows `stat`/`fstat` disagree on `ctime` for unchanged rewrites | The first repair caused false rejections in stable-file tests. A local repeated-rewrite probe isolated the timestamp difference. On Windows compare file ID, size and modification time; include `ctime` on other platforms. |
| Whole-project method acceptance depended on a separate lab | Add a checked-in test that creates an actual defective service, sees its regression fail, repairs it and closes only with fresh passing evidence. This is helper acceptance, not a blind agent-adoption trial. |
| Hosted Windows mutation fixtures used a temporary-directory alias | First hosted runs failed four mutation assertions because the fixture's short TEMP path differed from the helper's resolved path, so the mutation hook never ran. Resolve the fixture root and assert each mutation occurred; retain every matrix job with `fail-fast: false`. |

All three initial mutation regressions failed before the helper repair. The first
replacement fixture hit Windows file locking while trying to rename an open file;
moving that mutation to the close boundary made the regression portable. Preserve
that distinction: a fixture error was not counted as a product failure or pass.

The [test guide](../../tests/README.md) describes commands, scenario scope and audit
guard limits. Existing schema/CLI/snapshot formats remain unchanged. VERSION,
catalog, activation version and current synthetic examples advance to preview 4.

## Current evidence

- Baseline validation: 10 modules, 270 supported local links; 97 discovered tests,
  95 passed and two symlink skips on local Windows/Python 3.13.
- Repaired local suite: 108 discovered tests, 106 passed and the same two symlink
  skips. The project scenario runs two application tests before and after repair;
  these are nested acceptance assertions, not additional framework test counts.
- Routing acceptance: 72 kind/risk/project cases plus all 22 single signals, checking
  baseline gates, sensitive escalation, all four modes and all ten modules.
- All five CLI commands and invalid JSON run under a side-effect-denying audit hook;
  four negative probes check the guard itself. No network or production access.
- Local final validation: 10 modules, 284 supported local links; activation entry
  remains 1,264 words within its 1,700-word ceiling. `git diff --check` passed.
- Initial published candidate `b2be76e` failed its
  [PR matrix](https://github.com/LeiterConsulting/exec-ctrl/actions/runs/37351620006)
  and [push matrix](https://github.com/LeiterConsulting/exec-ctrl/actions/runs/37351611046)
  on the Windows fixture alias described above; cancelled jobs were not counted as
  passes. The fixture repair and complete-matrix setting require a new hosted run.
- Repaired code revision: `02e753a5983177126a837bff7bd298b022951805`.
  [PR validation](https://github.com/LeiterConsulting/exec-ctrl/actions/runs/37351837594)
  and [push validation](https://github.com/LeiterConsulting/exec-ctrl/actions/runs/37351830995)
  succeeded on all four Windows/Linux Python 3.10/3.13 jobs. Each job passed all
  108 tests with no skips, including both symlink checks and all mutation hooks.
- Publication candidate: [PR #3](https://github.com/LeiterConsulting/exec-ctrl/pull/3),
  `codex/publication-readiness` into `main`. This record's documentation update
  receives its own CI validation; the code identity above remains the repair evidence.

## Remaining acceptance

This increment prepares a preview for main merge and real-project trial. It does
not certify every agent/IDE, semantic module behavior, real organization rules,
scanner findings, external connector writes or production readiness. Independent
task-plus-link adoption remains a [field gate](../v2/FIELD_TRIALS.md). Stable-release
reuse/distribution terms remain an owner decision recorded in the
[roadmap](../v2/ROADMAP.md); no license terms are invented here.

The prior [session evolution](V2_SESSION_EVOLUTION.md) and lab records retain their
original revisions/results. Main merge and a stable v2 release are separate actions.
