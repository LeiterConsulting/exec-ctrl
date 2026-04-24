# Future Enhancements Planning Surface exec-ctrl

## Control Summary

| Field | Value |
| --- | --- |
| Initiative | `Future Enhancements Planning Surface` |
| Abbrev | `future-enhancements-planning` |
| Control system | `exec-ctrl` |
| Overall state | `complete` |
| Current phase | `Phase 5 Close complete` |
| Started | `2026-04-24` |
| Governs | adding a non-operational planning area for future `exec-ctrl` enhancements and routing existing follow-on ideas into that area |
| Primary inputs | `README.md`, `docs/EXEC_CTRL_REPO_LINK_BOOTSTRAP.md`, `docs/EXEC_CTRL_SELF_HOSTING_AND_METHOD_EVOLUTION.md`, active user direction, and existing repo-local refinement records |

## Objective

Create a non-operational planning area where future `exec-ctrl` enhancements can be documented and shaped without looking like active execution-control work.

## Requirement Definitions

| ID | Requirement | Definition | Success Signal |
| --- | --- | --- | --- |
| `FEP-1` | Dedicated planning area | The repo should contain a planning-only doc area outside `docs/exec_ctrl/`. | A planning folder exists under `docs/` and clearly distinguishes planning from operational control. |
| `FEP-2` | Centralized future backlog | Existing follow-on ideas should route into one planning surface instead of remaining scattered only in inline future sections. | A future-enhancements planning doc exists and captures the current main candidate refinements. |
| `FEP-3` | Self-governing refinement | The planning-area addition itself should be governed under initiative-mode exec-ctrl. | This enhancement has control, audit, and decision records that close with evidence. |

## Scope In

- a non-operational planning folder under `docs/`
- a future-enhancements planning doc with the current backlog themes
- targeted entry-doc updates that route follow-on ideas into the planning area
- self-governing exec-ctrl records for this refinement

## Scope Out

- activating any planned enhancement as live work
- converting the planning area into a second operational control system
- redesigning the existing method or bootstrap guidance beyond routing follow-on work

## Deliverables

1. a planning-only documentation area outside `docs/exec_ctrl/`
2. a centralized future-enhancements planning doc
3. targeted routing updates from generic docs into the planning area
4. self-governing initiative records for this refinement

## Must-Pass Success Criteria

1. the repo contains a non-operational planning area that is clearly separate from `docs/exec_ctrl/`
2. the current future enhancement ideas are captured in a dedicated planning doc
3. entry docs route future follow-on work to that planning area explicitly
4. this refinement is governed under initiative-mode exec-ctrl within the repo

## Should-Pass Success Criteria

1. the planning surface is explicit enough that future agents can use it without mistaking it for active work
2. the planning doc captures the emerging agent-assisted method-evolution direction
3. the refinement stays bounded to planning-surface creation rather than activating more enhancements immediately

## Non-Goals

- implement one of the future enhancements in the same slice
- replace the existing operational evidence model
- add automation that promotes planning items automatically

## Completion Conditions

- all must-pass criteria are satisfied
- the planning and operational areas are clearly distinguished
- any remaining planned work remains explicit rather than implied active

## Execution Process

### Phase 0. Activate

Outputs:

- refinement activated
- planning gap confirmed

Status:

- `complete`

### Phase 1. Define

Outputs:

- objective, scope, and success criteria made explicit

Status:

- `complete`

### Phase 2. Design

Outputs:

- planning-area structure and routing surfaces chosen

Status:

- `complete`

### Phase 3. Build

Outputs:

- planning docs added
- entry docs routed to the planning area

Status:

- `complete`

### Phase 4. Validate

Outputs:

- changed surfaces reviewed
- self-governing records synchronized to the final outcome

Status:

- `complete`

### Phase 5. Close

Outputs:

- completion or deferral recorded explicitly

Status:

- `not_started`

## Workstreams

| Workstream | Purpose | Status | Evidence |
| --- | --- | --- | --- |
| `WS1` | Planning-area definition | `complete` | `docs/planning/README.md`, `docs/planning/FUTURE_ENHANCEMENTS.md` |
| `WS2` | Routing and backlog centralization | `complete` | `README.md`, `docs/EXEC_CTRL_REPO_LINK_BOOTSTRAP.md`, `docs/EXEC_CTRL_SELF_HOSTING_AND_METHOD_EVOLUTION.md` |
| `WS3` | Self-governing records | `complete` | `docs/exec_ctrl/FUTURE_ENHANCEMENTS_PLANNING_EXEC_CTRL.md`, audit log, decision log |

## Baseline Evidence

- `docs/exec_ctrl/` already serves as the operational evidence area for active or completed refinements
- future enhancement ideas currently live mainly in inline sections of generic method docs
- the repo does not yet expose a dedicated non-operational planning area for those future ideas

## Risks and Dependencies

1. the planning area could be mistaken for active work if the boundary is not explicit
2. the backlog could become a vague wish list unless entries stay bounded and promotable
3. routing updates must not imply that inline future sections are themselves execution control

## Current Status

What is complete now:

- the repo now contains a dedicated non-operational planning area under `docs/planning/`
- the current future enhancement backlog is centralized in one planning doc
- entry docs now route follow-on ideas into the planning area explicitly
- this bounded refinement was governed and closed under initiative-mode exec-ctrl

What remains open:

- the planned enhancements remain candidates until they are promoted into separate initiative records under `docs/exec_ctrl/`

## Validation Evidence

- `docs/planning/README.md`
- `docs/planning/FUTURE_ENHANCEMENTS.md`
- `README.md`
- `docs/EXEC_CTRL_REPO_LINK_BOOTSTRAP.md`
- `docs/EXEC_CTRL_SELF_HOSTING_AND_METHOD_EVOLUTION.md`
- `docs/exec_ctrl/FUTURE_ENHANCEMENTS_PLANNING_AUDIT_LOG.md`
- `docs/exec_ctrl/FUTURE_ENHANCEMENTS_PLANNING_DECISION_LOG.md`