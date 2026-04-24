# Checklist-Review Prompt Enhancement exec-ctrl

## Control Summary

| Field | Value |
| --- | --- |
| Initiative | `Checklist-Review Prompt Enhancement` |
| Abbrev | `checklist-review-prompt` |
| Control system | `exec-ctrl` |
| Overall state | `complete` |
| Current phase | `Phase 5 Close complete` |
| Started | `2026-04-24` |
| Governs | adding a reusable one-command prompt for applying the self-hosting coherence checklist in method-evolution validation work |
| Primary inputs | `docs/EXEC_CTRL_SELF_HOSTING_COHERENCE_CHECKLIST.md`, `docs/EXEC_CTRL_SELF_HOSTING_AND_METHOD_EVOLUTION.md`, workspace-guidance prompt pack, active user direction, and existing exec-ctrl refinement records |

## Objective

Add a reusable checklist-review prompt so future users and agents can run the self-hosting coherence review as one explicit workflow instead of reconstructing it manually inside broader prompts.

## Requirement Definitions

| ID | Requirement | Definition | Success Signal |
| --- | --- | --- | --- |
| `CRP-1` | Reusable prompt surface | The repo should provide a dedicated prompt for checklist-based self-hosting review. | A prompt file exists in the workspace-guidance prompt pack and applies the coherence checklist in one flow. |
| `CRP-2` | Workflow integration | The checklist and self-hosting guidance should point to the prompt instead of leaving it as an isolated file. | The checklist doc, self-hosting guide, or prompt-pack README reference the new prompt explicitly. |
| `CRP-3` | Self-governing refinement | The prompt addition itself should be governed under initiative-mode exec-ctrl. | This enhancement has control, audit, and decision records that close with evidence. |

## Scope In

- a reusable checklist-review prompt
- targeted doc updates that route users to the prompt
- self-governing exec-ctrl records for this refinement

## Scope Out

- redesign the checklist itself
- add runtime automation or hooks that enforce the review prompt
- revise every existing method-evolution prompt to embed the whole review outcome inline

## Deliverables

1. a reusable checklist-review prompt
2. targeted doc updates that expose the prompt
3. self-governing initiative records for this refinement

## Must-Pass Success Criteria

1. the repo contains a dedicated checklist-review prompt file
2. the checklist or self-hosting guidance references that prompt explicitly
3. the prompt makes the review verdict and main gaps explicit
4. this refinement is governed under initiative-mode exec-ctrl within the repo

## Should-Pass Success Criteria

1. the prompt stays focused on one review task rather than becoming a second method-evolution workflow
2. the prompt is generic enough to use across self-hosting and method-repo validation slices
3. the refinement leaves broader checklist-review automation as explicit future work

## Non-Goals

- change the checklist sections in the same slice
- replace the method-evolution prompt
- add multiple review prompts for every checklist variant

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

- checklist-review prompt added
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
| `WS1` | Prompt surface addition | `complete` | `templates/workspace-guidance/.github/prompts/exec-ctrl-checklist-review.prompt.md` |
| `WS2` | Workflow integration | `complete` | `docs/EXEC_CTRL_SELF_HOSTING_COHERENCE_CHECKLIST.md`, `docs/EXEC_CTRL_SELF_HOSTING_AND_METHOD_EVOLUTION.md`, `templates/workspace-guidance/README.md` |
| `WS3` | Self-governing records | `complete` | `docs/exec_ctrl/CHECKLIST_REVIEW_PROMPT_EXEC_CTRL.md`, audit log, decision log |

## Baseline Evidence

- the repo already contains a reusable self-hosting coherence checklist
- the workspace prompt pack does not yet contain a dedicated checklist-review prompt
- the self-hosting guide still lists this prompt as a future extension

## Risks and Dependencies

1. the new prompt could duplicate too much of the method-evolution prompt
2. the prompt could become too narrow for general self-hosting validation or too broad for one review task
3. the docs must reference the prompt clearly enough that it becomes part of the actual workflow

## Current Status

What is complete now:

- the repo now contains a dedicated one-command checklist-review prompt
- the checklist and self-hosting guide now point to that prompt explicitly
- this bounded refinement was governed and closed under initiative-mode exec-ctrl

What remains open:

- broader prompt-pack refinements can still add review prompts for other specialized validation surfaces, but they are not required for this slice to close

## Validation Evidence

- `templates/workspace-guidance/.github/prompts/exec-ctrl-checklist-review.prompt.md`
- `templates/workspace-guidance/README.md`
- `docs/EXEC_CTRL_SELF_HOSTING_COHERENCE_CHECKLIST.md`
- `docs/EXEC_CTRL_SELF_HOSTING_AND_METHOD_EVOLUTION.md`
- `docs/exec_ctrl/CHECKLIST_REVIEW_PROMPT_AUDIT_LOG.md`
- `docs/exec_ctrl/CHECKLIST_REVIEW_PROMPT_DECISION_LOG.md`