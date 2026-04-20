# Exec-Ctrl Agent Prompt Cookbook

## Purpose

This cookbook helps a future agent map a user request to the correct exec-ctrl operating mode and default behavior.

## Default selection rule

If the request is one bounded slice of work inside an active repository, use initiative mode.

If the request is to establish execution control for the whole product or repository, use project-pack mode.

## Example prompts

### Example 1: audit-heavy bounded work

User prompt:

`use the exec-ctrl repo to run a readiness audit for the public operator interface and fix the highest-severity issues`

Recommended mode:

- initiative mode

Expected agent behavior:

1. activate control, audit, and decision docs for the initiative
2. add a findings register and remediation issue template
3. define scope, success criteria, and non-goals before implementation
4. perform the audit, implement the highest-value fixes, validate with evidence, and close with explicit deferrals if needed

### Example 2: refactor slice

User prompt:

`use the exec-ctrl repo to govern a refactor that extracts business logic from handlers into services without breaking the current interface`

Recommended mode:

- initiative mode

Expected agent behavior:

1. activate the initiative control docs
2. define interface-stability, validation, and rollback expectations
3. implement only the slice needed to satisfy the active phase
4. validate with tests and narrow evidence before closing

### Example 3: whole-repo control setup

User prompt:

`use the exec-ctrl repo to set up an execution-control layer for this new product repository`

Recommended mode:

- project-pack mode

Expected agent behavior:

1. add the six project-pack docs
2. define target product, page/function map, phase ladder, evidence model, and live status
3. make the project-pack docs the authoritative execution surface

### Example 4: release closeout slice

User prompt:

`use the exec-ctrl repo to govern the release-readiness closeout for this repository`

Recommended mode:

- initiative mode

Expected agent behavior:

1. activate the initiative pack
2. define release gate criteria and evidence rules
3. track blockers, deferrals, and closure explicitly in the audit and decision logs

## Behavior rules for the agent

- create the control artifacts before substantive implementation
- keep the docs current during implementation rather than after the fact
- prefer initiative mode unless the user clearly needs whole-repo governance
- use the shared status vocabulary: `not_started`, `in_progress`, `blocked`, `complete`, `deferred`
- express lifecycle nuance through phases, checkpoints, and status narrative rather than extra status words