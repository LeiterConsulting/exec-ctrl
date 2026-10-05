# v2 project and session evolution

Started: 2026-10-05. Implementation/test increment: `complete`.
Default-branch rollout: `in_progress`. Baseline: `09d75e3`, clean `v2`.
Method and target: this repository. User request: re-review the updates and improve
the complete framework for projects and agentic sessions.

## Review and selected work

The previous preview passed its documented controlled checks. That evidence remains
historical. Current review found practical gaps rather than a need for more mandatory
documents:

| Gap | Impact | Selected correction |
| --- | --- | --- |
| Records require manual assembly | More bookkeeping and inconsistent pending gates | Generate an honest pending record from declared facts and policies |
| Subject freshness is only a label | A passing report can be attached to changed files under an unchanged label | Explicit-file content snapshots and optional current-target comparison |
| Evidence kinds are descriptive only | A build can accidentally be cited for a declared live acceptance requirement | Typed gate requirements, including additive policy obligations |
| Session continuation is lightly specified | Scope changes and compaction can lose acceptance or repeat failed work | Small working agreement, checkpoint and resume protocol |
| Broad modules lack concrete task recipes | Harder to turn controls into useful daily actions | Bounded playbooks, contract-discrepancy and integration mappings |
| Adapter guidance ages quickly | Native discovery may differ from actual configuration | Dated official documentation refresh, retaining observed-trial limits |
| Nonfunctional signals are missing | Performance, accessibility and compatibility work lacks explicit routing | Add those facts without automatic claims of validation |

## Acceptance and scope

- Keep one compact link-invoked entry, no required install or document pack.
- Preserve v1 references, prior reports, target instructions and unrelated work.
- Keep the helper Python 3.10+, standard-library-only, offline and read-only.
- Generate no passing evidence or approvals; policy requirements compose additively.
- Reject changed snapshot content, path escapes, malformed manifests and wrong
  evidence kinds. Snapshot scope must be explicit and bounded.
- Verify CLI behavior from an unrelated directory and preserve target bytes.
- Run repository validation, regression suite, controlled lab and hosted CI for
  the published preview. Independent IDE trials remain a separate gate.
- Publish on v2 and roll the labeled preview into the default branch through a
  reviewable pull request, after inspecting actual required review/check state.
  Preserve v1 reference and review history; do not bypass repository controls.

No new agent sessions, external team messages, production deployment, automatic
scanner execution, credentials discovery or invented licensing terms are needed.

## Decisions

Use `2.0.0-preview.3`; retain record schema 1 with documented optional gate
requirements. Historical records still require their original pinned helper.
Snapshots cover only explicitly named files and cannot prove omitted dependencies,
an atomic repository state, environment identity or evidence truth. No helper command
executes record content or writes adoption files.

## Evidence and next action

Baseline: 73 tests and repository validation passed on 2026-10-05. Remote/default
branch inspected; main remains v1, v2 matches the local baseline, no open PR exists.
Implementation and published-source acceptance completed; default rollout follows.

Local implementation checks: suite now discovers 97 tests; 95 passed and two
symlink cases skipped because this Windows host cannot create symlinks. Repository
validation checks 269 local links, catalog/entry coherence and both record examples.
The activation contract is 1,264 words, below its 1,700-word ceiling. Final diff
review preserves historical/v1 evidence and introduces no runtime dependency.
Both symlink regressions subsequently executed successfully on all hosted runners.

Review also found that canonicalizing a selected symlink could lose its original
meaning if later repointed. Snapshot input checks now reject symlinks, redirected
directories and parent traversal rather than masking that gap. Tests cover the
internal-repointing and external-escape cases where symlink creation is available.

## Published-source acceptance

Method commit: `ed0ba8e9ef89e5ce5fc0b4e43a6b46b153f5ed68`, retrieved from GitHub
into a separate clean cache. Lab harness/results commit:
`bf8949da8b693c253231d4374f79e83ce5c5d61c` in the local-only lab.

| Check | Observed result |
| --- | --- |
| Hosted unit suite | All 97 tests passed on Windows/Linux, Python 3.10/3.13; symlink cases executed |
| Controlled lab | 63 checks passed, zero failed |
| Routing | 94 cases; all ten modules and four modes |
| Application regression suite | 19 passed; deliberately flawed baseline still fails as expected |
| Extracted artifact/runtime | 68 real HTTP checks passed on loopback; owned process stopped, stderr empty |
| New CLI flows | Pending records, current snapshots, same-size change rejection and typed-policy requirements exercised |
| Target preservation | User note and AGENTS bytes unchanged; user note remains modified/unstaged |
| Review | Final affected diff, source/record/example coherence and authorization boundaries inspected |

[Hosted CI for the tested commit](https://github.com/LeiterConsulting/exec-ctrl/actions/runs/37345950458)
passed all four jobs. Detailed local evidence remains in
`exec-ctrl-v2-lab/reports/20261005T170807502860Z/`; it is not a public evidence bundle.
Positive kind-tag tests are synthetic format checks; actual runtime checks are
reported separately. Missing independent-review/scanner policy gates remain blocked.

Artifact SHA-256:
`003a3f92eb036d9e48b67da2b21caa9fdcf8f780a21277ab31df2325e49eeeda`.
Unchanged extracted/running application source SHA-256:
`fb5a987ae8371cd662b6558773e8af7b446bc09ea2871728e7fd43b81d22917c`.

## Rollout and remaining program gates

Promote the labeled preview through a PR after checks pass. Repository branch
protection and ruleset metadata were inspected: no mandatory protection/review rule
was returned for main. No review or enforcement control is being disabled.
The complete repo-link entry becomes v2 while historical v1 references are retained.

This iteration is still a controlled author-session exercise. Fresh independent
task-plus-link trials across advertised hosts, real policy/scanner/connector
acceptance, and the owner's reuse terms remain program gates for stable broad
adoption. Native-adapter documentation support is not an observed host trial.
