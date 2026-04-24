# Agent Workspace Orientation exec-ctrl

## Control Summary

| Field | Value |
| --- | --- |
| Initiative | `Agent Workspace Orientation` |
| Abbrev | `agent-workspace-orientation` |
| Control system | `exec-ctrl` |
| Overall state | `complete` |
| Current phase | `Phase 5 Close complete` |
| Started | `2026-04-24` |
| Governs | making the `exec-ctrl` repo self-orienting for agentic IDE use so an agent pointed at the workspace can identify the right docs, prompts, and next bounded refinement path from repo context |
| Primary inputs | active user direction, `README.md`, `docs/EXEC_CTRL_METHOD.md`, `docs/planning/FUTURE_ENHANCEMENTS.md`, the workspace-guidance template pack, and existing repo-local exec-ctrl records |

## Objective

Make this repository easier for an agentic IDE to use directly by installing repo-specific workspace guidance, adding a repeatable assessment loop for self-hosted refinements, and routing entry docs toward those surfaces.

## Requirement Definitions

| ID | Requirement | Definition | Success Signal |
| --- | --- | --- | --- |
| `AWO-1` | Installed workspace guidance | The repo should contain live `.github/` guidance customized for this workspace rather than only template copies under `templates/`. | Repo-local agent guidance exists with no unresolved placeholders and points to the real docs and workflows in this repo. |
| `AWO-2` | Assessment loop | The repo should teach an agent how to inspect the planning area, choose one bounded refinement, activate control docs, and close with explicit follow-on work. | A reusable prompt or guide exists for iterative self-hosted repo refinement. |
| `AWO-3` | Entry routing | The main entry docs should route users and agents to the installed guidance and assessment loop. | README and any related planning or method docs point to the new orientation surfaces where relevant. |
| `AWO-4` | Self-governing evidence | This refinement should be governed under initiative-mode exec-ctrl. | Control, audit, and decision records remain current through implementation and validation. |

## Scope In

- repo-local `.github/` guidance for this workspace
- one reusable assessment-loop prompt or guide for self-hosted refinements
- targeted routing updates in entry docs and planning surfaces
- self-governing exec-ctrl records for this bounded refinement

## Scope Out

- redesign of the entire method repository structure
- broad rewrites of example packs unrelated to agent orientation
- runtime automation, CI enforcement, or extension development
- non-doc feature work outside repo guidance, prompts, and control surfaces

## Deliverables

1. repo-local workspace guidance customized for `exec-ctrl`
2. a reusable assessment-loop surface for choosing the next bounded refinement
3. entry-doc updates that make those surfaces discoverable
4. synchronized control, audit, and decision records for this refinement

## Must-Pass Success Criteria

1. the repo contains live workspace guidance under `.github/` with repo-specific paths and validation guidance
2. an agent can find a clear, reusable workflow for inspecting planning, activating a bounded slice, and updating control records
3. the main entry docs point to the installed guidance or assessment surface where an agent would reasonably look first
4. the repo-local exec-ctrl artifacts reflect the final state of the refinement accurately

## Should-Pass Success Criteria

1. the installed guidance stays smaller than the method docs and defers to them correctly
2. the assessment loop aligns with the planning-area promotion rules already documented in the repo
3. the refinement promotes or clarifies the next planning candidate if that becomes necessary during implementation

## Non-Goals

- replace the generic template pack with repo-specific guidance only
- create new framework-specific examples
- automate refinement selection without an explicit user request

## Completion Conditions

- all must-pass criteria are satisfied
- any remaining follow-on work is recorded explicitly rather than implied complete
- the repo guidance and repo-local control records agree on how self-hosted refinements should proceed

## Execution Process

### Phase 0. Activate

Outputs:

- bounded self-hosting refinement activated
- baseline gap identified around missing live workspace guidance for the repo itself

Status:

- `complete`

### Phase 1. Define

Outputs:

- objective, scope, success criteria, and non-goals made explicit

Status:

- `complete`

### Phase 2. Design

Outputs:

- minimal installed guidance set chosen for this repo
- assessment-loop surface selected for iterative self-hosted refinement

Status:

- `complete`

### Phase 3. Build

Outputs:

- repo-local guidance and assessment surfaces added
- entry docs updated

Status:

- `complete`

### Phase 4. Validate

Outputs:

- markdown diagnostics clean
- placeholder and routing checks pass on the installed guidance

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
| `WS1` | Repo-local guidance installation | `complete` | `.github/copilot-instructions.md`, `.github/instructions/exec-ctrl-docs.instructions.md`, `.github/prompts/` |
| `WS2` | Assessment-loop definition | `complete` | `docs/EXEC_CTRL_AGENT_ASSESSMENT_LOOP.md`, `README.md`, `docs/EXEC_CTRL_SELF_HOSTING_AND_METHOD_EVOLUTION.md`, `docs/planning/FUTURE_ENHANCEMENTS.md` |
| `WS3` | Self-governing records | `complete` | `docs/exec_ctrl/AGENT_WORKSPACE_ORIENTATION_EXEC_CTRL.md`, audit log, decision log |

## Baseline Evidence

- the repo currently contains workspace-guidance files only under `templates/workspace-guidance/.github/`
- the repo root does not yet contain live `.github/` guidance for agent sessions in this workspace
- the planning area already identifies `FE-007` as the next strongest candidate for an agent-assisted assessment loop
- the repo already documents self-hosting method evolution, but an agent pointed at the workspace still has to infer how to operate without repo-local guidance

## Risks And Dependencies

1. installed guidance could become redundant if it merely copies the templates without repo-specific adaptation
2. the assessment loop could become too broad if it tries to automate whole-repo redesign instead of bounded refinement selection
3. routing updates must stay aligned with the authority order already taught in the generic method docs

## Current Status

What is complete now:

- repo-local workspace guidance is installed and customized under `.github/`
- the repo now contains a generic agent assessment loop plus a repo-local next-refinement prompt
- the README, self-hosting guide, and planning surface route agents toward the new orientation flow
- `FE-007` was promoted out of the planning backlog during this slice, and later follow-on refinements were completed afterward

What remains open:

- later follow-on refinements were completed after this slice closed
- no defined backlog items remain in `docs/planning/FUTURE_ENHANCEMENTS.md`

## Validation Evidence

- targeted file search confirming no live repo-root `.github/` guidance before activation
- `docs/EXEC_CTRL_AGENT_ASSESSMENT_LOOP.md`
- `.github/copilot-instructions.md`
- `.github/instructions/exec-ctrl-docs.instructions.md`
- `.github/prompts/bootstrap-exec-ctrl.prompt.md`
- `.github/prompts/exec-ctrl-method-evolution.prompt.md`
- `.github/prompts/exec-ctrl-checklist-review.prompt.md`
- `.github/prompts/exec-ctrl-rubric-review.prompt.md`
- `.github/prompts/exec-ctrl-assess-next-refinement.prompt.md`
- `README.md`
- `docs/EXEC_CTRL_SELF_HOSTING_AND_METHOD_EVOLUTION.md`
- `docs/planning/FUTURE_ENHANCEMENTS.md`
- final markdown diagnostics for the added and updated docs
- final placeholder and routing checks across the installed guidance surfaces
- self-hosting coherence review across generic docs, reusable activation surfaces, planning, and repo-local proof artifacts