# Exec-Ctrl Repo-Link Scorecards

## Purpose

Use these scorecards when a repo-link request is ambiguous enough that initiative mode and whole-project control both look plausible at first glance.

They are calibration examples for [EXEC_CTRL_BOUNDED_VS_WHOLE_SYSTEM_SCORING_RUBRIC.md](EXEC_CTRL_BOUNDED_VS_WHOLE_SYSTEM_SCORING_RUBRIC.md), not replacements for the rubric itself.

## How To Use These Examples

1. find the request shape closest to the current user request
2. compare the category scores and the factors that drove them
3. use the scorecard to calibrate judgment, then apply the real rubric to the live request
4. record any hard override, watchpoint, or explicit non-goal in the initiative decision log

## Scorecard 1. Cross-Surface Reliability Hardening

Request shape:

`Use exec-ctrl with https://github.com/example/team-console to harden the admin settings workflow across the UI, the settings API, and the operator diagnostics page. Keep it bounded to reliability and error recovery.`

| Category | Score | Why |
| --- | --- | --- |
| Surface breadth | `1` | several adjacent surfaces change together, but the work still stays within one operator flow |
| Authority impact | `0` | the core authority order and phase model stay intact |
| Dependency spread | `1` | UI, API, and diagnostics surfaces need coordinated updates |
| Validation breadth | `1` | several adjacent checks are needed, but not a repo-wide validation sweep |
| Reuse scope | `1` | the outcome improves one recurring reliability slice rather than the whole repo |
| User wording | `0` | the user names an explicit bounded slice and non-goal |

Total:

- `4`

Recommended path:

- initiative mode

Watchpoints:

- do not widen into platform-wide reliability governance
- keep non-goals explicit in the control record

## Scorecard 2. Multi-Service Bootstrap With Mixed Signals

Request shape:

`Use exec-ctrl with https://github.com/example/platform-monorepo to stand up a control layer for the shared docs, the deployment workflow, and the first delivery ladder for the platform services.`

| Category | Score | Why |
| --- | --- | --- |
| Surface breadth | `2` | many core surfaces across the repo change together |
| Authority impact | `2` | the request establishes baseline control for most future work |
| Dependency spread | `2` | docs, service inventory, and delivery workflow all need coordinated changes |
| Validation breadth | `2` | the claim requires broad repo-level validation |
| Reuse scope | `2` | the outcome becomes baseline guidance for the repository |
| User wording | `1` | the wording is broad and outcome-oriented even though it stops short of saying "whole repo redesign" explicitly |

Total:

- `11`

Recommended path:

- whole-project control

Why this is still useful:

- it shows how a repo-link request can sound operationally bounded but still require whole-repository governance because the authority layer itself is being established

## Scorecard 3. Audit Plus Limited Remediation

Request shape:

`Use exec-ctrl with https://github.com/example/customer-web to audit the account area for accessibility issues, fix the most severe findings, and keep explicit deferrals for lower-priority items.`

| Category | Score | Why |
| --- | --- | --- |
| Surface breadth | `1` | several adjacent screens may be involved, but the slice is still one audit area |
| Authority impact | `0` | the execution model does not change |
| Dependency spread | `1` | findings, remediation, and validation need coordination |
| Validation breadth | `1` | audit evidence plus targeted fixes must be validated together |
| Reuse scope | `0` | the improvement stays within one bounded audit effort |
| User wording | `0` | the request is explicit about scope and deferrals |

Total:

- `3`

Recommended path:

- initiative mode

Watchpoints:

- keep the severity model explicit
- do not let remediation widen into a general redesign of the account area

## Scorecard 4. Borderline Repo-Link Migration Request

Request shape:

`Use exec-ctrl with https://github.com/example/ops-portal to move the current spreadsheet-driven release checklist, remediation notes, and delivery status into repo-local execution control for the release program.`

| Category | Score | Why |
| --- | --- | --- |
| Surface breadth | `1` | several adjacent release-control surfaces are involved |
| Authority impact | `1` | the move clarifies where authority lives for one release program |
| Dependency spread | `1` | docs, checklists, and status signals need coordinated migration |
| Validation breadth | `1` | the migrated release-control surfaces need a coherent validation pass |
| Reuse scope | `1` | the outcome influences one recurring program workflow |
| User wording | `1` | the wording is broad but still plausibly bounded |

Total:

- `6`

Recommended path:

- initiative mode with explicit boundaries and escalation watchpoints

Suggested boundaries:

- govern one release program rather than the whole product
- avoid rewriting the repo-wide authority model unless the migration surfaces prove insufficient

## Practical Pattern

When ambiguity remains after repo inspection, use a scorecard like these to calibrate the live rubric pass.

When the request still lands in the middle band, stay bounded unless the authority model for most future work is actually being replaced.