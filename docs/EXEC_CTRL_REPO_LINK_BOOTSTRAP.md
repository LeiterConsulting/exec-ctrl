# Exec-Ctrl Repo-Link Bootstrap

## Purpose

This guide turns `exec-ctrl` from a reference repo into a bootstrap pattern for agentic IDE workflows.

Use it when the user provides:

- a repository link
- a task, initiative, or outcome idea
- optional constraints such as deadlines, non-goals, or validation expectations

and expects the agent to stand up the control docs and workspace guidance in the target repository.

If the target repository is itself a method, template, prompt, or governance repository, also use [EXEC_CTRL_SELF_HOSTING_AND_METHOD_EVOLUTION.md](EXEC_CTRL_SELF_HOSTING_AND_METHOD_EVOLUTION.md) so the work treats those surfaces as the governed product.

## Default rule

If the request is bounded, use initiative mode.

If the request clearly asks for whole-product or whole-repository governance, use project-pack mode.

When the request is ambiguous, prefer initiative mode and state the boundary explicitly.

If ambiguity remains after repo inspection, use [EXEC_CTRL_BOUNDED_VS_WHOLE_SYSTEM_SCORING_RUBRIC.md](EXEC_CTRL_BOUNDED_VS_WHOLE_SYSTEM_SCORING_RUBRIC.md) before choosing the control path.

If the workspace-guidance prompt pack is installed, you can also invoke `.github/prompts/exec-ctrl-rubric-review.prompt.md` to run that scoring pass directly.

## Required intake inputs

The agent should collect or infer:

- the target repository or current workspace
- the requested outcome
- scope constraints and non-goals when they are already known
- the likely validation surface
- any existing authoritative docs the new control layer must respect

Do not stop for extra clarification unless missing information would block an accurate bootstrap.

## Bootstrap workflow

### 1. Inspect the target repository

- open or clone the target repo
- identify current concept docs, runbooks, architectural docs, and operator surfaces
- look for any existing authoritative status or planning docs
- check whether `.github/copilot-instructions.md`, `.github/instructions/`, or `.github/prompts/` already exist

### 2. Choose the operating mode

Use initiative mode when:

- the request is one slice of work
- the task is an audit, remediation effort, refactor, hardening effort, release closeout, or subsystem addition
- the repository already has its own product direction and only needs governance for one bounded effort

Use project-pack mode when:

- the request is to establish whole-repository execution control
- the repository is early enough that the execution layer should cover the full product
- the user explicitly wants the phase ladder and live status for the whole project

### 3. Create the control artifacts before substantive implementation

For initiative mode, create:

- `docs/exec_ctrl/<INITIATIVE>_EXEC_CTRL.md`
- `docs/exec_ctrl/<INITIATIVE>_AUDIT_LOG.md`
- `docs/exec_ctrl/<INITIATIVE>_DECISION_LOG.md`

Add optional findings or remediation docs when the initiative is audit-heavy.

For project-pack mode, create or adapt:

- `13_EXEC_CTRL_OVERVIEW.md`
- `14_EXEC_CTRL_TARGET_PRODUCT.md`
- `15_EXEC_CTRL_PAGES_AND_FUNCTIONS.md`
- `16_EXEC_CTRL_PHASE_PLAN.md`
- `17_EXEC_CTRL_TEST_AND_SUCCESS.md`
- `18_EXEC_CTRL_STATUS.md`

### 4. Install workspace guidance

If the target repo lacks equivalent agent guidance, copy and adapt the files from [templates/workspace-guidance](../templates/workspace-guidance):

- `.github/copilot-instructions.md`
- `.github/instructions/exec-ctrl-docs.instructions.md`
- `.github/prompts/bootstrap-exec-ctrl.prompt.md`
- any task-shape prompt bundles that match the initiative, such as audit, refactor, release closeout, or migration bootstrap

Customize the placeholders immediately.

The goal is to make later agent sessions keep using the same authority model rather than treating the bootstrap as a one-off event.

When the target repo has a recurring task shape, copy the matching prompt bundle as well so future sessions can invoke the same pattern directly.

### 5. Translate the task into control language

Before building, convert the request into explicit:

- objective
- scope in
- scope out
- deliverables
- must-pass success criteria
- should-pass success criteria
- non-goals
- workstreams
- baseline evidence
- validation evidence expectations

### 6. Execute and validate under the active phase

- the active phase is the earliest phase that is not `complete`
- later work can be designed early but should not be claimed complete first
- use the closed status vocabulary: `not_started`, `in_progress`, `blocked`, `complete`, `deferred`
- keep the control docs current in the same cycle as code or documentation changes

### 7. Close explicitly

Do not mark the work complete because the implementation appears close.

Close only when:

- must-pass criteria are satisfied
- evidence exists for the completion claim
- the audit and decision records match reality
- deferred items remain explicit rather than implied complete

## Recommended outputs by mode

### Initiative mode

Minimum outputs:

- initiative control record
- audit log
- decision log
- updated workspace guidance if needed

Common optional outputs:

- findings register
- remediation issue template
- follow-up backlog or deferral list

### Project-pack mode

Minimum outputs:

- six project-pack docs
- updated workspace guidance if needed

Common optional outputs:

- additional test annexes
- release-gate or risk registers
- mode-specific supporting runbooks

## Prompt shapes that should work well

### Repo link plus bounded initiative

`Use the exec-ctrl repo with https://github.com/example/team-service to govern a diagnostics hardening effort for the admin API. Keep it bounded to operator-visible reliability and do not widen into a broader platform rewrite.`

### Repo link plus audit and remediation

`Use the exec-ctrl repo with https://github.com/example/frontend-app to run an accessibility audit for the settings area, fix the highest-severity issues, and keep explicit deferrals for lower-priority findings.`

### Repo link plus whole-project setup

`Use the exec-ctrl repo with https://github.com/example/new-product to create the initial execution-control layer for the repository and define the first authoritative phase ladder.`

## Failure modes to avoid

- choosing project-pack mode for a bounded request that only needs initiative control
- writing substantive code before the control artifacts exist
- assuming the repo already has authoritative guidance without inspecting it
- leaving build and test placeholders uncustomized in copied workspace-guidance files
- closing the initiative without explicit evidence and deferrals

## Suggestions for future refinement

Track future repo-link and bootstrap enhancements in [planning/FUTURE_ENHANCEMENTS.md](planning/FUTURE_ENHANCEMENTS.md) instead of treating them as live operational work.

Current candidates already captured there include:

1. a validation checklist for copied workspace-guidance templates so placeholders are not left behind
2. more example prompts for data migrations, release readiness, and incident remediation
3. example scorecards for recurring ambiguous repo-link requests so the rubric is easier to calibrate over time

This guide intentionally stops short of automation.

It defines the repeatable bootstrap behavior that a future prompt, skill, or agent can automate later.