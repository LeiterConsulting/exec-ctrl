# Bounded-vs-Whole-System Scoring Rubric Enhancement exec-ctrl

## Control Summary

| Field | Value |
| --- | --- |
| Initiative | `Bounded-vs-Whole-System Scoring Rubric Enhancement` |
| Abbrev | `mode-selection-rubric` |
| Control system | `exec-ctrl` |
| Overall state | `complete` |
| Current phase | `Phase 5 Close complete` |
| Started | `2026-04-24` |
| Governs | adding a reusable scoring rubric for deciding between bounded initiative control and whole-system control in ambiguous exec-ctrl work |
| Primary inputs | `docs/EXEC_CTRL_METHOD.md`, `docs/EXEC_CTRL_INITIATIVE_MODE.md`, `docs/EXEC_CTRL_REPO_LINK_BOOTSTRAP.md`, `docs/EXEC_CTRL_SELF_HOSTING_AND_METHOD_EVOLUTION.md`, workspace-guidance prompts and instructions, active user direction, and existing repo-local exec-ctrl records |

## Objective

Add a generic scoring rubric so ambiguous mode-selection cases can be resolved more consistently without widening every mixed-signal request into a whole-system effort.

## Requirement Definitions

| ID | Requirement | Definition | Success Signal |
| --- | --- | --- | --- |
| `BWR-1` | Generic rubric surface | The repo should contain a reusable rubric for bounded-vs-whole-system decisions. | A dedicated rubric doc exists under `docs/` and explains categories, thresholds, overrides, and recordkeeping. |
| `BWR-2` | Workflow integration | The generic method and activation surfaces should route users to the rubric when ambiguity remains. | The relevant docs, prompts, or instructions reference the rubric explicitly. |
| `BWR-3` | Self-governing refinement | The rubric addition itself should be governed under initiative-mode exec-ctrl. | This enhancement has control, audit, and decision records that close with evidence. |

## Scope In

- a generic bounded-vs-whole-system scoring rubric
- targeted doc, prompt, and instruction updates that use the rubric during ambiguous mode selection
- self-governing exec-ctrl records for this refinement

## Scope Out

- redesign the whole execution model
- replace the default initiative-first rule in clearly bounded cases
- create runtime automation for rubric enforcement

## Deliverables

1. a generic bounded-vs-whole-system scoring rubric
2. targeted workflow updates that use the rubric where ambiguity remains
3. self-governing initiative records for this refinement

## Must-Pass Success Criteria

1. the repo contains a dedicated bounded-vs-whole-system scoring rubric doc
2. generic method-selection surfaces reference the rubric explicitly
3. reusable prompt or instruction surfaces apply the rubric during ambiguous mode selection
4. this refinement is governed under initiative-mode exec-ctrl within the repo

## Should-Pass Success Criteria

1. the rubric remains conservative and does not turn bounded work into broad redesign by default
2. the rubric is concrete enough for future agents to record the outcome consistently
3. the refinement leaves dedicated review-prompt automation as explicit future work instead of widening into it now

## Non-Goals

- remove the initiative-first default in clearly bounded cases
- add a dedicated rubric-review prompt in the same slice
- revise all historical examples to include scored mode-selection tables

## Completion Conditions

- all must-pass criteria are satisfied
- the rubric and linked workflow surfaces are coherent
- any follow-on work remains explicit rather than implied complete

## Execution Process

### Phase 0. Activate

Outputs:

- refinement activated
- rubric gap confirmed

Status:

- `complete`

### Phase 1. Define

Outputs:

- objective, scope, and success criteria made explicit

Status:

- `complete`

### Phase 2. Design

Outputs:

- rubric categories and thresholds chosen
- workflow surfaces selected for integration

Status:

- `complete`

### Phase 3. Build

Outputs:

- rubric doc added
- method docs, prompts, and instructions updated

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

- `complete`

## Workstreams

| Workstream | Purpose | Status | Evidence |
| --- | --- | --- | --- |
| `WS1` | Generic rubric guidance | `complete` | `docs/EXEC_CTRL_BOUNDED_VS_WHOLE_SYSTEM_SCORING_RUBRIC.md` |
| `WS2` | Workflow integration | `complete` | `docs/EXEC_CTRL_METHOD.md`, `docs/EXEC_CTRL_INITIATIVE_MODE.md`, `docs/EXEC_CTRL_AGENT_PROMPT_COOKBOOK.md`, `docs/EXEC_CTRL_REPO_LINK_BOOTSTRAP.md`, `docs/EXEC_CTRL_SELF_HOSTING_AND_METHOD_EVOLUTION.md`, `README.md`, workspace-guidance prompts and instructions |
| `WS3` | Self-governing records | `complete` | `docs/exec_ctrl/BOUNDED_VS_WHOLE_SYSTEM_RUBRIC_EXEC_CTRL.md`, audit log, decision log |

## Baseline Evidence

- the repo named the rubric as a future self-hosting extension but did not yet define it
- generic method-selection surfaces still relied mainly on default initiative-first language in ambiguous cases
- reusable prompts and instructions did not yet record a concrete scoring pass for mixed-signal requests

## Risks and Dependencies

1. the rubric could encourage unnecessary escalation to whole-system control
2. the rubric could be treated as more authoritative than explicit user direction
3. too much scoring detail could overcomplicate straightforward bounded work

## Current Status

What is complete now:

- the repo now contains a dedicated bounded-vs-whole-system scoring rubric
- the generic method-selection surfaces now reference the rubric in ambiguous cases
- the reusable bootstrap and method-evolution prompts now apply the rubric when ambiguity remains
- this bounded refinement was governed and closed under initiative-mode exec-ctrl

What remains open:

- a reusable rubric-review prompt remains a possible future refinement, but it is not required for this slice to close

## Validation Evidence

- `README.md`
- `docs/EXEC_CTRL_METHOD.md`
- `docs/EXEC_CTRL_INITIATIVE_MODE.md`
- `docs/EXEC_CTRL_AGENT_PROMPT_COOKBOOK.md`
- `docs/EXEC_CTRL_REPO_LINK_BOOTSTRAP.md`
- `docs/EXEC_CTRL_SELF_HOSTING_AND_METHOD_EVOLUTION.md`
- `docs/EXEC_CTRL_BOUNDED_VS_WHOLE_SYSTEM_SCORING_RUBRIC.md`
- `templates/workspace-guidance/.github/copilot-instructions.md`
- `templates/workspace-guidance/.github/prompts/bootstrap-exec-ctrl.prompt.md`
- `templates/workspace-guidance/.github/prompts/exec-ctrl-method-evolution.prompt.md`
- `docs/exec_ctrl/BOUNDED_VS_WHOLE_SYSTEM_RUBRIC_AUDIT_LOG.md`
- `docs/exec_ctrl/BOUNDED_VS_WHOLE_SYSTEM_RUBRIC_DECISION_LOG.md`