# First Session Bootstrap Guidance exec-ctrl

## Control Summary

| Field | Value |
| --- | --- |
| Initiative | `First Session Bootstrap Guidance` |
| Abbrev | `first-session-bootstrap-guidance` |
| Control system | `exec-ctrl` |
| Overall state | `complete` |
| Current phase | `Phase 5 Close complete` |
| Started | `2026-04-24` |
| Governs | adding a concrete first-session prompt example and a compact routing table so future users and agents can choose the correct entry behavior from a brand-new or lightly populated workspace |
| Primary inputs | active user direction, `README.md`, `docs/EXEC_CTRL_REPO_LINK_BOOTSTRAP.md`, `docs/EXEC_CTRL_AGENT_PROMPT_COOKBOOK.md`, `.github/prompts/bootstrap-exec-ctrl.prompt.md`, and the completed current-workspace intake refinement |

## Objective

Make the first-contact bootstrap path easier to invoke by adding one concrete example prompt and one compact routing table that distinguish current-workspace bootstrap, external repo bootstrap, and improving `exec-ctrl` itself.

## Scope In

- one compact routing table in the generic docs
- one concrete first-session example prompt for a brand-new or lightly populated workspace
- bootstrap prompt wording needed to stay aligned with the documented routing
- self-governing proof artifacts for this bounded refinement

## Scope Out

- new template packs or example-library expansion beyond the entry guidance
- runtime automation for importing or cloning repos
- broader redesign of the bootstrap method or self-hosting model

## Deliverables

1. a compact entry-routing table
2. a concrete first-session example prompt
3. aligned bootstrap prompt wording where needed
4. synchronized proof artifacts for the refinement

## Must-Pass Success Criteria

1. the docs show a quick comparison between current workspace bootstrap, external repo bootstrap, and improving `exec-ctrl` itself
2. a future user can copy a concrete first-session prompt from the repo without inventing the wording from scratch
3. the reusable bootstrap prompt does not contradict the documented routing behavior
4. the proof artifacts reflect the implemented clarification accurately

## Should-Pass Success Criteria

1. the new guidance stays compact and easy to scan
2. the first-session example is specific enough to be usable but generic enough to fit multiple repositories

## Non-Goals

- create a new standing backlog item from this one guidance refinement
- add a second onboarding system parallel to the existing bootstrap docs
- automate concept extraction from local documents

## Completion Conditions

- all must-pass criteria are satisfied
- the generic docs and reusable bootstrap prompt teach the same entry-routing distinction
- the refinement closes without reopening the exhausted planning backlog

## Workstreams

| Workstream | Purpose | Status | Evidence |
| --- | --- | --- | --- |
| `WS1` | Generic entry-guidance refinement | `complete` | `README.md`, `docs/EXEC_CTRL_REPO_LINK_BOOTSTRAP.md`, `docs/EXEC_CTRL_AGENT_PROMPT_COOKBOOK.md` |
| `WS2` | Reusable bootstrap-surface alignment | `complete` | `.github/prompts/bootstrap-exec-ctrl.prompt.md` |
| `WS3` | Self-governing records | `complete` | `docs/exec_ctrl/FIRST_SESSION_BOOTSTRAP_GUIDANCE_EXEC_CTRL.md`, audit log, decision log |

## Current Status

What is complete now:

- the repo now includes a compact three-way routing table covering current-workspace bootstrap, external repo bootstrap, and improving `exec-ctrl` itself
- the bootstrap guide now includes a concrete current-workspace first-session prompt that a future user can copy directly
- the prompt cookbook now explains why the current-workspace example is the copyable first-session prompt
- the reusable bootstrap prompt now distinguishes generic bootstrap from the self-hosting path when the governed target is `exec-ctrl` itself

What remains open:

- no defined follow-on work is required from this slice
- future first-session refinements, if needed, should come from repeated field use rather than a standing planning item

## Validation Evidence

- targeted reads of `docs/EXEC_CTRL_REPO_LINK_BOOTSTRAP.md`, `docs/EXEC_CTRL_AGENT_PROMPT_COOKBOOK.md`, `.github/prompts/bootstrap-exec-ctrl.prompt.md`, and the prior current-workspace intake proof artifacts
- `README.md`
- `docs/EXEC_CTRL_REPO_LINK_BOOTSTRAP.md`
- `docs/EXEC_CTRL_AGENT_PROMPT_COOKBOOK.md`
- `.github/prompts/bootstrap-exec-ctrl.prompt.md`
- targeted markdown diagnostics on the changed files after edits