# Exec-Ctrl Agent Prompt Cookbook

## Purpose

This cookbook helps a future agent map a user request to the correct exec-ctrl operating mode and default behavior.

When the request includes a repository link, the agent should also use [EXEC_CTRL_REPO_LINK_BOOTSTRAP.md](EXEC_CTRL_REPO_LINK_BOOTSTRAP.md) to stand up the target docs and workspace guidance.

## Default selection rule

If the request is one bounded slice of work inside an active repository, use initiative mode.

If the request is to establish execution control for the whole product or repository, use project-pack mode.

If the request falls between those two shapes, use [EXEC_CTRL_BOUNDED_VS_WHOLE_SYSTEM_SCORING_RUBRIC.md](EXEC_CTRL_BOUNDED_VS_WHOLE_SYSTEM_SCORING_RUBRIC.md) and record the outcome explicitly in the decision log.

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

### Example 5: repo link plus bounded initiative

User prompt:

`use the exec-ctrl repo with https://github.com/example/team-service to govern a diagnostics hardening effort for the admin API without widening into a full platform rewrite`

Recommended mode:

- initiative mode

Expected agent behavior:

1. inspect the target repo before choosing the control path
2. activate the initiative control docs under `docs/exec_ctrl/`
3. add workspace guidance if the target repo lacks equivalent `.github` instructions and prompts
4. define objective, scope, must-pass criteria, should-pass criteria, and non-goals before implementation
5. execute only the bounded slice and keep the control docs current while evidence is gathered

### Example 6: repo link plus whole-product control setup

User prompt:

`use the exec-ctrl repo with https://github.com/example/new-product to create the initial execution-control layer for the whole repository`

Recommended mode:

- project-pack mode

Expected agent behavior:

1. inspect the target repo and any existing concept docs
2. add the six project-pack docs after the existing concept pack or adapt the numbering model explicitly
3. add workspace guidance so later agent sessions treat the exec-ctrl docs as authoritative
4. define the target product, phase ladder, test model, and live status before implementation expands

### Example 7: improve the method using the method

User prompt:

`use exec-ctrl to improve exec-ctrl itself so the method teaches self-hosting explicitly rather than only demonstrating it in repo-local records`

Recommended mode:

- initiative mode

Expected agent behavior:

1. activate a bounded initiative for the method refinement before changing the docs
2. audit the gap between generic method guidance and repo-local demonstrations
3. add or update the generic self-hosting guidance first
4. update reusable prompts, templates, and examples that operationalize the change
5. only then update the repo-local control records so they reflect the completed refinement accurately

## Behavior rules for the agent

- create the control artifacts before substantive implementation
- inspect the target repository before choosing the mode when the prompt includes a repo link
- install workspace guidance when the target repo lacks an equivalent always-on instruction surface
- keep the docs current during implementation rather than after the fact
- prefer initiative mode unless the user clearly needs whole-repo governance
- use the shared status vocabulary: `not_started`, `in_progress`, `blocked`, `complete`, `deferred`
- express lifecycle nuance through phases, checkpoints, and status narrative rather than extra status words
- when improving the method itself, update generic teaching surfaces before relying on repo-local proof artifacts alone