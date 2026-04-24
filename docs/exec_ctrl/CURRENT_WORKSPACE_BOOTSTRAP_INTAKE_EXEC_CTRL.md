# Current Workspace Bootstrap Intake exec-ctrl

## Control Summary

| Field | Value |
| --- | --- |
| Initiative | `Current Workspace Bootstrap Intake` |
| Abbrev | `current-workspace-bootstrap-intake` |
| Control system | `exec-ctrl` |
| Overall state | `complete` |
| Current phase | `Phase 5 Close complete` |
| Started | `2026-04-24` |
| Governs | clarifying what an agent should do when a user starts in a new workspace with local documents and ideas and references `exec-ctrl` only by repo URL inside prompt text |
| Primary inputs | active user direction, `README.md`, `docs/EXEC_CTRL_METHOD.md`, `docs/EXEC_CTRL_REPO_LINK_BOOTSTRAP.md`, `docs/EXEC_CTRL_AGENT_PROMPT_COOKBOOK.md`, and `.github/prompts/bootstrap-exec-ctrl.prompt.md` |

## Objective

Make the method explicit about the first-contact case where the current workspace is the target repo and the `exec-ctrl` URL is only a method reference inside the user's prompt.

## Scope In

- generic intake guidance for current-workspace bootstrap from prompt text
- one prompt-cookbook example for the scenario
- bootstrap prompt wording so it fits this intake path
- self-governing proof artifacts for this bounded refinement

## Scope Out

- runtime automation for fetching or cloning the `exec-ctrl` repo
- expansion into a new template pack or example-library slice
- product-specific instructions for one target workspace

## Deliverables

1. generic method guidance for prompt-only current-workspace bootstrap
2. a cookbook example that shows expected agent behavior
3. a bootstrap prompt that handles the current-workspace case explicitly
4. synchronized proof artifacts for this refinement

## Must-Pass Success Criteria

1. the docs distinguish the `exec-ctrl` repo link as method source rather than the target workspace when no other repo link is provided
2. the intake path tells the agent to inspect the current workspace docs and ideas before choosing mode and creating control artifacts
3. the bootstrap prompt can be used from the current workspace without requiring a separate target repo link
4. the proof artifacts reflect the scenario and the implemented clarification accurately

## Should-Pass Success Criteria

1. the clarification stays small and folds into existing bootstrap guidance rather than creating a parallel onboarding system
2. the example reduces the risk that an agent will shift focus to the `exec-ctrl` repo itself instead of the user's workspace

## Non-Goals

- make the method fetch external repos automatically
- define a new standing backlog from a single field-use scenario
- widen the slice into full bootstrap automation or editor integration

## Completion Conditions

- all must-pass criteria are satisfied
- the generic docs and bootstrap prompt teach the same intake distinction
- the field-use clarification is recorded without reopening a standing defined backlog

## Workstreams

| Workstream | Purpose | Status | Evidence |
| --- | --- | --- | --- |
| `WS1` | Generic intake clarification | `complete` | `README.md`, `docs/EXEC_CTRL_METHOD.md`, `docs/EXEC_CTRL_REPO_LINK_BOOTSTRAP.md`, `docs/EXEC_CTRL_AGENT_PROMPT_COOKBOOK.md` |
| `WS2` | Reusable bootstrap surface alignment | `complete` | `.github/prompts/bootstrap-exec-ctrl.prompt.md` |
| `WS3` | Self-governing records | `complete` | `docs/exec_ctrl/CURRENT_WORKSPACE_BOOTSTRAP_INTAKE_EXEC_CTRL.md`, audit log, decision log |

## Current Status

What is complete now:

- the method now states that a lone `exec-ctrl` repo URL in prompt text is a method reference rather than the governed target repo
- the bootstrap guide now tells the agent to inspect the current workspace docs, notes, and idea fragments before mode selection when no other target repo link is present
- the prompt cookbook now shows the scenario and the expected first steps explicitly
- the repo-local bootstrap prompt now asks the agent to state whether the governed target is the current workspace or an external repo

What remains open:

- no defined follow-on work is required from this slice
- future additions, if needed, should come from repeated field use rather than from a standing backlog item
- one open-ended watchpoint remains: if repeated field use shows agents struggle to turn loose local docs and idea fragments into first-pass concept inputs, add a lightweight concept-intake example or prompt later

## Validation Evidence

- targeted reads of `README.md`, `docs/EXEC_CTRL_METHOD.md`, `docs/EXEC_CTRL_REPO_LINK_BOOTSTRAP.md`, `docs/EXEC_CTRL_AGENT_PROMPT_COOKBOOK.md`, and `.github/prompts/bootstrap-exec-ctrl.prompt.md`
- `README.md`
- `docs/EXEC_CTRL_METHOD.md`
- `docs/EXEC_CTRL_REPO_LINK_BOOTSTRAP.md`
- `docs/EXEC_CTRL_AGENT_PROMPT_COOKBOOK.md`
- `.github/prompts/bootstrap-exec-ctrl.prompt.md`
- targeted markdown diagnostics on the changed files after edits