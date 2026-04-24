# Repo-Link Bootstrap Enhancement exec-ctrl

## Control Summary

| Field | Value |
| --- | --- |
| Initiative | `Repo-Link Bootstrap Enhancement` |
| Abbrev | `repo-link-bootstrap` |
| Control system | `exec-ctrl` |
| Overall state | `complete` |
| Current phase | `Phase 5 Close complete` |
| Started | `2026-04-24` |
| Governs | making the standalone `exec-ctrl` repo operational for repo-link driven activation in agentic IDE workflows |
| Primary inputs | `README.md`, `docs/EXEC_CTRL_METHOD.md`, `docs/EXEC_CTRL_AGENT_PROMPT_COOKBOOK.md`, template packs, and active user direction |

## Objective

Make the standalone `exec-ctrl` repo able to bootstrap a target repository from a prompt that includes a repo link and a task idea, not just describe the method after the fact.

## Requirement Definitions

| ID | Requirement | Definition | Success Signal |
| --- | --- | --- | --- |
| `RLB-1` | Bootstrap workflow | The repo should explain how an agent turns a repo link plus a task request into exec-ctrl activation steps. | A dedicated repo-link bootstrap guide exists with inputs, workflow, outputs, and examples. |
| `RLB-2` | Workspace guidance pack | The repo should provide reusable `.github` guidance files that can be copied into a target repo. | A template pack exists with `copilot-instructions.md`, an exec-ctrl docs instruction file, a bootstrap prompt file, and task-shape prompt bundles for common initiative types. |
| `RLB-3` | Discoverable entry points | Future users should find the repo-link workflow from the main entry docs rather than only from deep template reading. | The README, method guide, cookbook, and initiative-pack readme all point to the bootstrap path. |

## Scope In

- repo-link bootstrap documentation
- reusable workspace-guidance templates
- task-shape prompt bundles for common initiative patterns
- entry-doc refinements that surface the new path
- self-governing exec-ctrl records for this enhancement

## Scope Out

- runtime automation for cloning or copying templates
- editor-specific features beyond generic `.github` guidance files
- product-specific case studies from other repositories

## Deliverables

1. a repo-link bootstrap guide
2. a workspace-guidance template pack with task-shape prompt bundles
3. updated entry docs that route users to the new flow
4. a self-governing initiative pack for the enhancement

## Must-Pass Success Criteria

1. the repo contains a dedicated repo-link bootstrap guide
2. the repo contains reusable workspace-guidance templates for target repos
3. the README and other entry docs expose the repo-link bootstrap path clearly
4. the enhancement is governed under initiative-mode exec-ctrl within this repo

## Should-Pass Success Criteria

1. the new guidance stays generic rather than tied to one product history
2. the prompt examples are specific enough to reduce ambiguity for future users
3. the workspace-guidance pack is small enough to copy without becoming a second control system

## Non-Goals

- automate repository cloning or template installation
- replace the existing project-pack or initiative-pack templates
- introduce runtime enforcement of the method

## Completion Conditions

- all must-pass criteria are satisfied
- the added docs and templates are linked coherently
- deferred future ideas remain explicit rather than implied complete

## Execution Process

### Phase 0. Activate

Outputs:

- bounded enhancement initiative defined
- baseline repo gap reviewed

Status:

- `complete`

### Phase 1. Define

Outputs:

- objective, scope, and success criteria made explicit

Status:

- `complete`

### Phase 2. Design

Outputs:

- decision to add a dedicated bootstrap guide and workspace-guidance template pack
- decision to route users from the README, method guide, and cookbook into that new path

Status:

- `complete`

### Phase 3. Build

Outputs:

- bootstrap guide added
- template pack added
- task-shape prompt bundles added for audit, refactor, release closeout, and migration bootstrap
- entry docs refined

Status:

- `complete`

### Phase 4. Validate

Outputs:

- repo structure reviewed
- links and file placement checked

Status:

- `complete`

### Phase 5. Close

Outputs:

- completion recorded in control, audit, and decision artifacts

Status:

- `complete`

## Workstreams

| Workstream | Purpose | Status | Evidence |
| --- | --- | --- | --- |
| `WS1` | Bootstrap method refinement | `complete` | `README.md`, `docs/EXEC_CTRL_METHOD.md`, `docs/EXEC_CTRL_REPO_LINK_BOOTSTRAP.md`, `docs/EXEC_CTRL_AGENT_PROMPT_COOKBOOK.md` |
| `WS2` | Workspace guidance templates and prompt bundles | `complete` | `templates/workspace-guidance/` |
| `WS3` | Self-governing records | `complete` | `docs/exec_ctrl/REPO_LINK_BOOTSTRAP_EXEC_CTRL.md`, `docs/exec_ctrl/REPO_LINK_BOOTSTRAP_AUDIT_LOG.md`, `docs/exec_ctrl/REPO_LINK_BOOTSTRAP_DECISION_LOG.md` |

## Baseline Evidence

- the repo already described full-project and initiative-mode control
- the repo already contained templates and a prompt cookbook
- the repo did not yet define a repo-link bootstrap workflow
- the repo did not yet provide reusable `.github` workspace-guidance templates
- the repo did not yet provide ready-to-copy task-shape prompt bundles for common initiative patterns

## Risks and Dependencies

1. adding too much guidance could make the repo harder to scan quickly
2. workspace-guidance templates must stay generic enough to fit multiple repos
3. copied templates can become misleading if placeholders are not customized

## Current Status

What is complete now:

- the repo contains a dedicated repo-link bootstrap guide
- the repo contains a workspace-guidance template pack for target repositories
- the workspace-guidance pack includes ready-to-copy prompt bundles for audit, refactor, release closeout, and migration bootstrap
- the main entry docs route users to the bootstrap path
- this enhancement is itself governed under initiative-mode exec-ctrl

What remains open:

- future automation or richer prompt libraries can be added later, but they are not required for this enhancement to close

## Validation Evidence

- `README.md`
- `docs/EXEC_CTRL_METHOD.md`
- `docs/EXEC_CTRL_REPO_LINK_BOOTSTRAP.md`
- `docs/EXEC_CTRL_AGENT_PROMPT_COOKBOOK.md`
- `templates/workspace-guidance/`
- `templates/workspace-guidance/.github/prompts/`
- `docs/exec_ctrl/REPO_LINK_BOOTSTRAP_AUDIT_LOG.md`
- `docs/exec_ctrl/REPO_LINK_BOOTSTRAP_DECISION_LOG.md`