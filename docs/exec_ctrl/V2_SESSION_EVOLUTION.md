# v2 project and session evolution

Started: 2026-10-05. State: `in_progress`. Baseline: `09d75e3`, clean `v2`.
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
- Publish on the already authorized v2 branch. Prepare the default-branch update
  as a reviewable pull request; broad repository work does not imply bypassing review.

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
Implementation and updated acceptance results are pending.

Local implementation checks: suite now discovers 97 tests; 95 passed and two
symlink cases skipped because this Windows host cannot create symlinks. Repository
validation checks 269 local links, catalog/entry coherence and both record examples.
The activation contract is 1,264 words, below its 1,700-word ceiling. Final diff
review preserves historical/v1 evidence and introduces no runtime dependency.
The symlink regression remains subject to actual execution on the hosted runners.

Review also found that canonicalizing a selected symlink could lose its original
meaning if later repointed. Snapshot input checks now reject symlinks, redirected
directories and parent traversal rather than masking that gap. Tests cover the
internal-repointing and external-escape cases where symlink creation is available.
