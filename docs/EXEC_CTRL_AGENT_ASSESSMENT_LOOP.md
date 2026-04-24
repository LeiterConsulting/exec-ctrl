# Exec-Ctrl Agent Assessment Loop

## Purpose

Use this loop when an agentic IDE is pointed at the `exec-ctrl` repository itself and the user wants the repo to keep improving under its own method.

The loop is for bounded self-hosting refinements, not for whole-repository redesign.

It helps an agent move from workspace context to a defensible next slice without inventing a new workflow each time.

## When To Use It

Use this loop when requests sound like:

- continue refinement of this repo
- improve `exec-ctrl` itself
- keep enhancing the method, prompts, templates, or examples
- choose the next bounded self-hosting slice from the planning area

Do not use this loop when the user explicitly wants a whole-repository execution-model redesign.

If that boundary is unclear, apply the bounded-vs-whole-system scoring rubric first.

## Primary Inputs

Inspect these surfaces in roughly this order:

1. active user direction
2. `README.md`
3. `docs/EXEC_CTRL_METHOD.md`
4. `docs/EXEC_CTRL_SELF_HOSTING_AND_METHOD_EVOLUTION.md`
5. `docs/planning/FUTURE_ENHANCEMENTS.md`
6. related records under `docs/exec_ctrl/`
7. any installed workspace guidance under `.github/`

## Bounded Assessment Loop

### 1. Orient To The Workspace

- confirm whether the request is about using `exec-ctrl` in another repo or improving the `exec-ctrl` repo itself
- identify the most relevant active or recently completed refinement in `docs/exec_ctrl/`
- inspect the planning area to see whether a near-term candidate already matches the request

### 2. Choose One Bounded Slice

- prefer one candidate enhancement or one clearly bounded gap
- default to initiative mode unless the work clearly changes the whole repository execution model
- if multiple candidates look plausible, choose the one with the smallest coherent teaching-and-proof loop

### 3. Activate Control Before Substantive Edits

- create or update the initiative control record, audit log, and decision log under `docs/exec_ctrl/`
- state objective, scope in, scope out, deliverables, must-pass criteria, should-pass criteria, non-goals, and validation evidence
- make the active phase the earliest phase that is not `complete`

### 4. Update Generic Teaching Surfaces First

- update the generic method docs that should teach the refined behavior
- keep the normative rule in the generic docs rather than only in repo-local proof artifacts
- if the refinement promotes an item from planning, make that planning transition explicit

### 5. Update Reusable Operational Surfaces

- update prompts, instructions, templates, examples, or workspace-guidance files that make the refined behavior easy to invoke again
- keep repo-local guidance smaller than the method docs and aligned with the same authority order
- remove or avoid prompt clutter that would confuse the dominant workflows

### 6. Validate Coherence

- run markdown diagnostics or equivalent narrow checks on the changed surfaces
- check for placeholder drift, wrong paths, or routing contradictions
- for self-hosting changes, apply the self-hosting coherence checklist across generic docs, reusable activation surfaces, examples, planning, and repo-local proof artifacts

### 7. Close With Explicit Follow-On Work

- synchronize the control record, audit log, and decision log to the finished state
- update `docs/planning/FUTURE_ENHANCEMENTS.md` so promoted work no longer looks untouched
- record remaining candidates or deferrals explicitly instead of implying a complete roadmap

## Expected Outputs

A clean assessment-loop cycle should leave:

- one bounded initiative record under `docs/exec_ctrl/`
- generic docs that teach the new behavior directly
- reusable repo-local guidance or prompts that operationalize the new behavior
- a planning surface that accurately distinguishes promoted work from remaining candidates

## Common Failure Modes

- treating `docs/planning/` as operational proof instead of planning input
- updating only repo-local control records while leaving generic docs unchanged
- copying or adding prompt surfaces without deciding which ones this repo really needs
- widening one bounded refinement into unrelated repo cleanup
- closing the slice without updating the next-step recommendation

## Practical Rule

The next refinement should be the one that best improves how a future agent can understand, activate, and validate `exec-ctrl` from workspace context alone.