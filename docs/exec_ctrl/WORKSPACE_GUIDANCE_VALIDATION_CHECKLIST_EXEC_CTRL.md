# Workspace Guidance Validation Checklist exec-ctrl

## Control Summary

| Field | Value |
| --- | --- |
| Initiative | `Workspace Guidance Validation Checklist` |
| Abbrev | `workspace-guidance-validation` |
| Control system | `exec-ctrl` |
| Overall state | `complete` |
| Current phase | `Phase 5 Close complete` |
| Started | `2026-04-24` |
| Governs | adding a reusable validation checklist for copied workspace-guidance templates and routing the existing repo docs to that validation step |
| Primary inputs | `docs/planning/FUTURE_ENHANCEMENTS.md`, `README.md`, `docs/EXEC_CTRL_METHOD.md`, `docs/EXEC_CTRL_REPO_LINK_BOOTSTRAP.md`, `templates/workspace-guidance/README.md`, and active user direction |

## Objective

Add a reusable validation checklist that keeps copied workspace-guidance templates from retaining placeholders, wrong doc paths, or misleading repo-specific assumptions after bootstrap.

## Requirement Definitions

| ID | Requirement | Definition | Success Signal |
| --- | --- | --- | --- |
| `WGV-1` | Reusable checklist | The repo should contain one generic checklist for validating copied workspace guidance. | A dedicated checklist doc exists under `docs/` and defines the validation pass condition and concrete checks. |
| `WGV-2` | Routing updates | The docs that tell users to copy workspace guidance should route them to the checklist. | The README, method docs, bootstrap guide, and workspace-guidance README all point to the checklist at the moment of use. |
| `WGV-3` | Planning promotion | `FE-001` should no longer look like untouched planning backlog once the work is active and complete. | The planning doc records the promotion and no longer lists `FE-001` as an unstarted candidate. |
| `WGV-4` | Self-governing evidence | The refinement should be governed under initiative-mode exec-ctrl. | This repo contains synchronized control, audit, and decision records for the checklist refinement. |

## Scope In

- one reusable workspace-guidance validation checklist under `docs/`
- targeted routing updates in the existing README and method/bootstrap/template guidance docs
- promotion of `FE-001` out of the planning backlog
- self-governing initiative records for this bounded refinement

## Scope Out

- adding new task-shape prompt bundles
- automating checklist enforcement in tooling or CI
- installing the workspace-guidance pack into unrelated target repositories as part of this slice
- broad repo cleanup outside the copied-guidance validation gap

## Deliverables

1. a standalone workspace-guidance validation checklist
2. entry-doc routing to the checklist at the bootstrap and template-installation points
3. a planning-surface update that promotes `FE-001`
4. self-governing control, audit, and decision records for this refinement

## Must-Pass Success Criteria

1. a generic checklist exists and clearly states how copied workspace-guidance templates should be validated
2. the README, method bootstrap guidance, repo-link bootstrap guide, and workspace-guidance README all route users to that checklist
3. `FE-001` no longer appears in planning as if it were untouched future work
4. the repo-local control artifacts reflect the completed refinement accurately

## Should-Pass Success Criteria

1. the checklist stays short enough for repeated repo-link use
2. the checklist covers placeholders, repo-specific substitutions, authority alignment, and evidence capture
3. the planning doc advances to the next strongest candidate rather than stopping at a stale recommendation

## Non-Goals

- create automation that scans copied workspace guidance automatically
- expand the same slice into additional prompt bundles or rubric examples
- redesign the workspace-guidance template pack itself beyond adding validation routing

## Completion Conditions

- all must-pass criteria are satisfied
- the generic checklist and routing docs agree with one another
- the planning surface reflects that `FE-001` has been promoted and completed
- any remaining follow-on work remains explicit rather than implied complete

## Execution Process

### Phase 0. Activate

Outputs:

- self-hosting refinement activated from `FE-001`
- baseline gap confirmed across the bootstrap and template guidance surfaces

Status:

- `complete`

### Phase 1. Define

Outputs:

- objective, scope, and success criteria made explicit

Status:

- `complete`

### Phase 2. Design

Outputs:

- decision to add one reusable checklist doc instead of scattering ad hoc reminders
- decision to update routing surfaces where copied guidance is installed and customized

Status:

- `complete`

### Phase 3. Build

Outputs:

- checklist doc added
- targeted README, method, bootstrap, template, and planning updates applied

Status:

- `complete`

### Phase 4. Validate

Outputs:

- edited markdown files checked for errors
- final routing and planning surfaces reviewed against the must-pass criteria

Status:

- `complete`

### Phase 5. Close

Outputs:

- completion recorded in the self-governing artifacts
- next follow-on work left explicit in planning rather than mixed into this slice

Status:

- `complete`

## Workstreams

| Workstream | Purpose | Status | Evidence |
| --- | --- | --- | --- |
| `WS1` | Generic checklist definition | `complete` | `docs/EXEC_CTRL_WORKSPACE_GUIDANCE_VALIDATION_CHECKLIST.md` |
| `WS2` | Routing and planning updates | `complete` | `README.md`, `docs/EXEC_CTRL_METHOD.md`, `docs/EXEC_CTRL_REPO_LINK_BOOTSTRAP.md`, `templates/workspace-guidance/README.md`, `docs/planning/FUTURE_ENHANCEMENTS.md` |
| `WS3` | Self-governing records | `complete` | `docs/exec_ctrl/WORKSPACE_GUIDANCE_VALIDATION_CHECKLIST_EXEC_CTRL.md`, audit log, decision log |

## Baseline Evidence

- `FE-001` already identified the copied-guidance validation gap in `docs/planning/FUTURE_ENHANCEMENTS.md`
- the repo-link bootstrap guide warned about placeholder drift but did not yet route users to a concrete validation checklist
- the workspace-guidance README required placeholder replacement but did not yet include a dedicated validation pass
- the repo did not yet contain a reusable checklist doc for copied workspace-guidance validation

## Risks And Dependencies

1. the checklist could become too large to use routinely if it expands beyond the copied-guidance failure mode
2. planning updates must keep the boundary between completed work and future candidates explicit
3. routing changes must stay limited to the guidance surfaces that actually instruct users to copy the template pack

## Current Status

What is complete now:

- the repo now includes a reusable workspace-guidance validation checklist
- the main bootstrap and template docs route users to that checklist at the right point in the workflow
- `FE-001` was promoted out of the planning backlog during this slice, and later follow-on refinements were completed afterward
- this bounded self-hosting refinement is documented under initiative-mode exec-ctrl

What remains open:

- later follow-on refinements were completed after this slice closed
- no defined backlog items remain in `docs/planning/FUTURE_ENHANCEMENTS.md`

## Validation Evidence

- `docs/EXEC_CTRL_WORKSPACE_GUIDANCE_VALIDATION_CHECKLIST.md`
- `README.md`
- `docs/EXEC_CTRL_METHOD.md`
- `docs/EXEC_CTRL_REPO_LINK_BOOTSTRAP.md`
- `templates/workspace-guidance/README.md`
- `docs/planning/FUTURE_ENHANCEMENTS.md`
- targeted VS Code error check on the edited markdown files