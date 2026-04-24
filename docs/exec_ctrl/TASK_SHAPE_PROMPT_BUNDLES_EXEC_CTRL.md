# Task-Shape Prompt Bundles exec-ctrl

## Control Summary

| Field | Value |
| --- | --- |
| Initiative | `Task-Shape Prompt Bundles` |
| Abbrev | `task-shape-prompts` |
| Control system | `exec-ctrl` |
| Overall state | `complete` |
| Current phase | `Phase 5 Close complete` |
| Started | `2026-04-24` |
| Governs | installing the next high-value live task-shape prompt bundles for the `exec-ctrl` repo so an agent pointed at this workspace can invoke recurring repo-link workflows directly |
| Primary inputs | active user direction, `docs/planning/FUTURE_ENHANCEMENTS.md`, repo-local `.github/` guidance, `templates/workspace-guidance/.github/prompts/`, and existing self-hosting records |

## Objective

Make the repo-local workspace guidance more directly usable by installing the next recurring task-shape prompt bundles for audit-remediation, release closeout, and migration-shaped repo-link work.

## Requirement Definitions

| ID | Requirement | Definition | Success Signal |
| --- | --- | --- | --- |
| `TSP-1` | Live task-shape prompts | The repo should contain live repo-local task-shape prompts for the next recurring bootstrap patterns it already teaches generically. | Repo-root `.github/prompts/` includes prompt bundles for audit-remediation, release closeout, and migration bootstrap with repo-local wording and no placeholders. |
| `TSP-2` | Discoverability | The repo-local guidance should point agents to the new task-shape prompts when those request shapes appear. | `.github/copilot-instructions.md` and any necessary routing docs mention the new prompt surfaces explicitly. |
| `TSP-3` | Planning promotion | `FE-002` should no longer look like untouched planning backlog once this slice is active and complete. | The planning doc records the promotion and advances the next recommendation explicitly. |
| `TSP-4` | Self-governing evidence | This refinement should remain governed under initiative-mode exec-ctrl. | Control, audit, and decision records stay synchronized through implementation and validation. |

## Scope In

- repo-local prompt bundles for audit-remediation, release closeout, and migration bootstrap
- targeted repo-local guidance updates for prompt discoverability
- planning-surface updates to reflect promotion of `FE-002`
- self-governing exec-ctrl records for this bounded refinement

## Scope Out

- new generic method examples unrelated to prompt bundles
- broad redesign of the workspace-guidance template pack
- installing every optional prompt bundle from the template pack if it does not match the current bounded slice
- CI or runtime automation for prompt discovery

## Deliverables

1. three live repo-local task-shape prompts under `.github/prompts/`
2. repo-local guidance updates that route agents to those prompts
3. a planning update that promotes `FE-002`
4. synchronized control, audit, and decision records for this refinement

## Must-Pass Success Criteria

1. the repo contains live prompt bundles for audit-remediation, release closeout, and migration bootstrap
2. the repo-local guidance points to those prompts clearly enough for agent discovery from workspace context
3. `FE-002` no longer appears in planning as untouched candidate work after implementation
4. the repo-local proof artifacts reflect the final refinement state accurately

## Should-Pass Success Criteria

1. the new prompts stay aligned with the generic workspace-guidance template surfaces
2. the added prompt set stays bounded and avoids unnecessary prompt clutter
3. the planning doc advances the next most useful bounded refinement explicitly

## Non-Goals

- install the refactor prompt in the same slice unless the bounded need changes
- add new task-shape prompts beyond the three covered here
- redesign the generic repo-link bootstrap method docs beyond routing needed for discovery

## Completion Conditions

- all must-pass criteria are satisfied
- any remaining prompt-surface follow-on work is explicit rather than implied complete
- the installed guidance, planning surface, and proof artifacts agree on the finished prompt set

## Execution Process

### Phase 0. Activate

Outputs:

- bounded prompt-bundle refinement activated
- baseline gap confirmed between template prompt availability and live repo-local prompt availability

Status:

- `complete`

### Phase 1. Define

Outputs:

- objective, scope, success criteria, and non-goals made explicit

Status:

- `complete`

### Phase 2. Design

Outputs:

- exact repo-local prompt set chosen for the bounded slice
- minimal routing surfaces chosen for prompt discoverability

Status:

- `complete`

### Phase 3. Build

Outputs:

- prompt bundles installed
- routing and planning docs updated

Status:

- `complete`

### Phase 4. Validate

Outputs:

- markdown diagnostics clean
- placeholder and coherence checks pass on the added prompt surfaces

Status:

- `complete`

### Phase 5. Close

Outputs:

- completion and remaining follow-on work recorded explicitly

Status:

- `complete`

## Workstreams

| Workstream | Purpose | Status | Evidence |
| --- | --- | --- | --- |
| `WS1` | Prompt bundle installation | `complete` | `.github/prompts/exec-ctrl-audit.prompt.md`, `.github/prompts/exec-ctrl-release-closeout.prompt.md`, `.github/prompts/exec-ctrl-migration-bootstrap.prompt.md` |
| `WS2` | Prompt discoverability and planning | `complete` | `.github/copilot-instructions.md`, `docs/planning/FUTURE_ENHANCEMENTS.md` |
| `WS3` | Self-governing records | `complete` | `docs/exec_ctrl/TASK_SHAPE_PROMPT_BUNDLES_EXEC_CTRL.md`, audit log, decision log |

## Baseline Evidence

- the template workspace-guidance pack already contains prompt bundles for audit-remediation, release closeout, and migration bootstrap
- the repo-local `.github/prompts/` folder currently contains only the bootstrap, method-evolution, rubric-review, checklist-review, and next-refinement prompts
- the planning area names `FE-002` as the next strongest bounded refinement after the agent assessment loop
- the repo is now self-orienting, but recurring repo-link task shapes still require agents to infer or reach into template surfaces instead of using live repo prompts

## Risks And Dependencies

1. copying too many prompts into the live guidance layer would create unnecessary prompt clutter
2. repo-local prompt wording must stay aligned with the generic template surfaces rather than drifting into a separate workflow
3. the planning surface must reflect promotion cleanly so future sessions do not reopen the same slice by mistake

## Current Status

What is complete now:

- the repo now exposes live task-shape prompts for audit-remediation, release closeout, and migration bootstrap under `.github/prompts/`
- the live workspace guidance points agents to those prompt surfaces directly
- `FE-002` was promoted out of planning during this slice, and later follow-on refinements were completed afterward
- this bounded self-hosting prompt refinement is documented under initiative-mode exec-ctrl

What remains open:

- later follow-on refinements were completed after this slice closed
- no defined backlog items remain in `docs/planning/FUTURE_ENHANCEMENTS.md`

## Validation Evidence

- file search confirming the current repo-local prompt set before activation
- `.github/prompts/exec-ctrl-audit.prompt.md`
- `.github/prompts/exec-ctrl-release-closeout.prompt.md`
- `.github/prompts/exec-ctrl-migration-bootstrap.prompt.md`
- `.github/copilot-instructions.md`
- `docs/planning/FUTURE_ENHANCEMENTS.md`
- final markdown diagnostics for changed prompt and routing surfaces
- final placeholder and coherence checks across the added prompt bundles and updated guidance