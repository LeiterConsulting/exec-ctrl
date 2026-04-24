# Self-Hosting Coherence Checklist Enhancement exec-ctrl

## Control Summary

| Field | Value |
| --- | --- |
| Initiative | `Self-Hosting Coherence Checklist Enhancement` |
| Abbrev | `self-hosting-checklist` |
| Control system | `exec-ctrl` |
| Overall state | `complete` |
| Current phase | `Phase 5 Close complete` |
| Started | `2026-04-24` |
| Governs | adding a reusable checklist for validating coherence across self-hosting method surfaces in the exec-ctrl repo |
| Primary inputs | `docs/EXEC_CTRL_SELF_HOSTING_AND_METHOD_EVOLUTION.md`, `templates/workspace-guidance/.github/prompts/exec-ctrl-method-evolution.prompt.md`, `README.md`, active user direction, and existing repo-local exec-ctrl records |

## Objective

Add a generic self-hosting coherence checklist so method-evolution work can validate agreement across docs, prompts, templates, examples, and repo-local proof artifacts before closure.

## Requirement Definitions

| ID | Requirement | Definition | Success Signal |
| --- | --- | --- | --- |
| `SHC-1` | Generic checklist surface | The repo should contain a generic checklist for self-hosting coherence validation. | A dedicated checklist doc exists under `docs/` and explains how to use it during validation. |
| `SHC-2` | Workflow integration | The self-hosting workflow should route users to the checklist rather than leaving it as an orphan doc. | The self-hosting guide, entry docs, or prompt surfaces reference the checklist explicitly. |
| `SHC-3` | Self-governing refinement | The checklist addition itself should be governed under initiative-mode exec-ctrl. | This enhancement has control, audit, and decision records that close with evidence. |

## Scope In

- a generic self-hosting coherence checklist
- targeted doc and prompt updates that route users to the checklist
- self-governing exec-ctrl records for this refinement

## Scope Out

- a full bounded-versus-whole-system scoring rubric
- broad redesign of the method-evolution prompt pack
- unrelated cleanup outside the self-hosting validation path

## Deliverables

1. a generic self-hosting coherence checklist
2. targeted self-hosting workflow updates that use the checklist
3. self-governing initiative records for this refinement

## Must-Pass Success Criteria

1. the repo contains a dedicated self-hosting coherence checklist doc
2. the self-hosting guide or related entry surfaces reference the checklist explicitly
3. the method-evolution prompt uses the checklist during validation
4. this refinement is governed under initiative-mode exec-ctrl within the repo

## Should-Pass Success Criteria

1. the checklist stays narrow and reusable rather than becoming a second method guide
2. the checklist makes the validation step more concrete for future method-evolution work
3. the refinement leaves the bounded-versus-whole-system rubric as explicit future work rather than widening into both enhancements at once

## Non-Goals

- add the scoring rubric in the same slice
- create runtime automation for checklist enforcement
- rewrite all examples to include a filled-out checklist

## Completion Conditions

- all must-pass criteria are satisfied
- the checklist and linked workflow surfaces are coherent
- any follow-on work remains explicit rather than implied complete

## Execution Process

### Phase 0. Activate

Outputs:

- refinement activated
- checklist gap confirmed

Status:

- `complete`

### Phase 1. Define

Outputs:

- objective, scope, and success criteria made explicit

Status:

- `complete`

### Phase 2. Design

Outputs:

- decision to land the checklist before the scoring rubric
- workflow surfaces chosen for checklist integration

Status:

- `complete`

### Phase 3. Build

Outputs:

- checklist doc added
- self-hosting guide, README, and method-evolution prompt updated

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
| `WS1` | Generic checklist guidance | `complete` | `docs/EXEC_CTRL_SELF_HOSTING_COHERENCE_CHECKLIST.md` |
| `WS2` | Workflow integration | `complete` | `docs/EXEC_CTRL_SELF_HOSTING_AND_METHOD_EVOLUTION.md`, `README.md`, `templates/workspace-guidance/.github/prompts/exec-ctrl-method-evolution.prompt.md` |
| `WS3` | Self-governing records | `complete` | `docs/exec_ctrl/SELF_HOSTING_COHERENCE_CHECKLIST_EXEC_CTRL.md`, audit log, decision log |

## Baseline Evidence

- the self-hosting guide explicitly listed a coherence checklist as a future extension
- no generic checklist surface yet existed in the repo
- the method-evolution prompt described coherence validation but did not name a reusable checklist

## Risks and Dependencies

1. the checklist could become too broad and duplicate the self-hosting guide
2. the refinement could widen into the scoring rubric instead of staying bounded
3. the checklist must reinforce the existing authority order rather than invent a separate review system

## Current Status

What is complete now:

- the repo now contains a dedicated self-hosting coherence checklist
- the self-hosting workflow now routes users to the checklist explicitly
- the method-evolution prompt now uses the checklist during validation
- this bounded refinement was governed and closed under initiative-mode exec-ctrl

What remains open:

- a bounded-versus-whole-system scoring rubric remains open as a separate future refinement, but it is not required for this checklist slice to close

## Validation Evidence

- `README.md`
- `docs/EXEC_CTRL_SELF_HOSTING_AND_METHOD_EVOLUTION.md`
- `docs/EXEC_CTRL_SELF_HOSTING_COHERENCE_CHECKLIST.md`
- `templates/workspace-guidance/.github/prompts/exec-ctrl-method-evolution.prompt.md`
- `docs/exec_ctrl/SELF_HOSTING_COHERENCE_CHECKLIST_AUDIT_LOG.md`
- `docs/exec_ctrl/SELF_HOSTING_COHERENCE_CHECKLIST_DECISION_LOG.md`