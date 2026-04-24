# Rubric-Review Prompt Enhancement exec-ctrl

## Control Summary

| Field | Value |
| --- | --- |
| Initiative | `Rubric-Review Prompt Enhancement` |
| Abbrev | `rubric-review-prompt` |
| Control system | `exec-ctrl` |
| Overall state | `complete` |
| Current phase | `Phase 5 Close complete` |
| Started | `2026-04-24` |
| Governs | adding a reusable one-command prompt for applying the bounded-vs-whole-system scoring rubric in ambiguous exec-ctrl mode-selection work |
| Primary inputs | `docs/EXEC_CTRL_BOUNDED_VS_WHOLE_SYSTEM_SCORING_RUBRIC.md`, workspace-guidance prompts, `README.md`, active user direction, and existing exec-ctrl refinement records |

## Objective

Add a reusable rubric-review prompt so future users and agents can run the bounded-vs-whole-system scoring step as a single explicit workflow instead of reconstructing it manually inside other prompts.

## Requirement Definitions

| ID | Requirement | Definition | Success Signal |
| --- | --- | --- | --- |
| `RRP-1` | Reusable prompt surface | The repo should provide a dedicated prompt for rubric-based mode review. | A prompt file exists in the workspace-guidance prompt pack and applies the rubric in one flow. |
| `RRP-2` | Workflow integration | The rubric and related docs should point to the reusable review prompt rather than leaving it as an isolated file. | The rubric doc and relevant guidance surfaces reference the new prompt explicitly. |
| `RRP-3` | Self-governing refinement | The prompt addition itself should be governed under initiative-mode exec-ctrl. | This enhancement has control, audit, and decision records that close with evidence. |

## Scope In

- a reusable rubric-review prompt
- targeted doc updates that route users to the prompt
- self-governing exec-ctrl records for this refinement

## Scope Out

- redesign the scoring rubric itself
- add runtime automation or hooks that enforce prompt usage
- revise every existing prompt to embed the rubric-review flow internally

## Deliverables

1. a reusable rubric-review prompt
2. targeted doc updates that expose the prompt
3. self-governing initiative records for this refinement

## Must-Pass Success Criteria

1. the repo contains a dedicated rubric-review prompt file
2. the rubric doc or related entry surfaces reference that prompt explicitly
3. the prompt makes the scoring outcome and chosen control path explicit
4. this refinement is governed under initiative-mode exec-ctrl within the repo

## Should-Pass Success Criteria

1. the prompt stays focused on one task rather than becoming a second bootstrap workflow
2. the prompt is generic enough to use in both product and method-repo ambiguity cases
3. the refinement leaves any broader prompt-pack redesign as explicit future work

## Non-Goals

- change the rubric thresholds in the same slice
- replace the bootstrap or method-evolution prompts
- create a full prompt bundle for every possible scoring scenario

## Completion Conditions

- all must-pass criteria are satisfied
- the prompt and linked doc surfaces are coherent
- any follow-on work remains explicit rather than implied complete

## Execution Process

### Phase 0. Activate

Outputs:

- refinement activated
- prompt gap confirmed

Status:

- `complete`

### Phase 1. Define

Outputs:

- objective, scope, and success criteria made explicit

Status:

- `complete`

### Phase 2. Design

Outputs:

- prompt shape and linked workflow surfaces chosen

Status:

- `complete`

### Phase 3. Build

Outputs:

- rubric-review prompt added
- linked docs refined

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
| `WS1` | Prompt surface addition | `complete` | `templates/workspace-guidance/.github/prompts/exec-ctrl-rubric-review.prompt.md` |
| `WS2` | Workflow integration | `complete` | `docs/EXEC_CTRL_BOUNDED_VS_WHOLE_SYSTEM_SCORING_RUBRIC.md`, `docs/EXEC_CTRL_REPO_LINK_BOOTSTRAP.md`, `docs/EXEC_CTRL_SELF_HOSTING_AND_METHOD_EVOLUTION.md`, `templates/workspace-guidance/README.md` |
| `WS3` | Self-governing records | `complete` | `docs/exec_ctrl/RUBRIC_REVIEW_PROMPT_EXEC_CTRL.md`, audit log, decision log |

## Baseline Evidence

- the repo already contains a reusable scoring rubric
- the workspace prompt pack does not yet contain a dedicated rubric-review prompt
- the rubric refinement record explicitly left this prompt as future work

## Risks and Dependencies

1. the new prompt could duplicate too much of bootstrap or method-evolution behavior
2. the prompt could become too narrow for method-repo use or too broad for bounded review use
3. the docs must reference the prompt clearly enough that it becomes part of the actual workflow

## Current Status

What is complete now:

- the repo now contains a dedicated one-command rubric-review prompt
- the rubric and related guidance surfaces now point to that prompt explicitly
- this bounded refinement was governed and closed under initiative-mode exec-ctrl

What remains open:

- future prompt-pack refinements can add dedicated review prompts for other generic checklist or rubric surfaces, but they are not required for this slice to close

## Validation Evidence

- `templates/workspace-guidance/.github/prompts/exec-ctrl-rubric-review.prompt.md`
- `templates/workspace-guidance/README.md`
- `docs/EXEC_CTRL_BOUNDED_VS_WHOLE_SYSTEM_SCORING_RUBRIC.md`
- `docs/EXEC_CTRL_REPO_LINK_BOOTSTRAP.md`
- `docs/EXEC_CTRL_SELF_HOSTING_AND_METHOD_EVOLUTION.md`
- `docs/exec_ctrl/RUBRIC_REVIEW_PROMPT_AUDIT_LOG.md`
- `docs/exec_ctrl/RUBRIC_REVIEW_PROMPT_DECISION_LOG.md`