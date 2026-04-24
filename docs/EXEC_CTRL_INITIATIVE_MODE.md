# Exec-Ctrl Initiative Mode

## Purpose

Initiative mode is the lightweight exec-ctrl pattern for bounded work inside an active repository.

Use it when the user is not asking for a full product execution system, but still wants the work to be governed, auditable, and completion-driven.

Typical examples:

- a subsystem slice
- an audit and remediation effort
- a refactor with explicit quality gates
- a UX or accessibility initiative
- a release-readiness closeout
- a capability, integration, or service addition that should be tracked as one initiative
- a method, prompt, template, or governance-system refinement inside the repository that defines that method

## Default rule for future agent use

If a future user says:

- "use the exec-ctrl repo to do the following work"
- "run this under exec-ctrl"
- "define the work and success criteria before implementation"

the agent should default to initiative mode unless the request clearly requires a whole-project execution layer.

If that boundary is still unclear after inspecting the repo and request, use [EXEC_CTRL_BOUNDED_VS_WHOLE_SYSTEM_SCORING_RUBRIC.md](EXEC_CTRL_BOUNDED_VS_WHOLE_SYSTEM_SCORING_RUBRIC.md) before escalating to a whole-system control path.

## Minimum artifact set

Initiative mode uses three required artifacts:

1. control record
2. audit log
3. decision log

Recommended naming:

- `<INITIATIVE>_EXEC_CTRL.md`
- `<INITIATIVE>_AUDIT_LOG.md`
- `<INITIATIVE>_DECISION_LOG.md`

Recommended placement:

- `docs/exec_ctrl/`

## Optional supporting artifacts

Add optional artifacts when the initiative needs them:

- findings register
- remediation issue template
- implementation plan pack
- backlog or follow-up register

These are especially useful for audit, remediation, readiness, and public-surface efforts.

## Lifecycle

Initiative mode uses six phases:

### 0. Activate

Outputs:

- initiative name
- objective
- initial scope in and scope out
- baseline evidence
- initial risks and dependencies

### 1. Define

Outputs:

- requirement definitions
- deliverables
- must-pass success criteria
- should-pass success criteria
- non-goals
- completion conditions

### 2. Design

Outputs:

- execution approach
- architecture or implementation direction if relevant
- validation strategy
- rollout or sequencing decisions if relevant

### 3. Build

Outputs:

- implementation progress under workstreams or slices
- evidence references to changed code, docs, or interfaces
- logged scope or sequencing changes

### 4. Validate

Outputs:

- tests and evidence
- unresolved issues list
- explicit statement of what still blocks closure

### 5. Close

Outputs:

- completion verdict
- explicit complete versus deferred statement
- follow-on backlog if needed

## Control record structure

The control record should include:

- control summary
- objective
- requirement definitions
- scope in
- scope out
- deliverables
- must-pass success criteria
- should-pass success criteria
- non-goals
- completion conditions
- execution process
- workstreams
- baseline evidence
- risks and dependencies
- current status
- validation evidence

## Audit model

Each audit entry should capture:

- date
- checkpoint
- evidence reviewed
- verdict
- gaps
- next action

Recommended verdicts:

- `pass`
- `pass_with_gaps`
- `fail`

`pass_with_gaps` is useful when the initiative can continue but real issues remain open.

## Decision model

Each decision entry should capture:

- ID
- date
- decision
- rationale
- consequence

Log any material change in:

- scope
- sequencing
- success criteria interpretation
- validation strategy
- deferral choice

## Shared status vocabulary

Initiative mode should use the same core execution states as project-pack mode:

- `not_started`
- `in_progress`
- `blocked`
- `complete`
- `deferred`

Lifecycle detail should be carried by the current phase, checkpoint names, and current-status narrative rather than extra status words.

## Completion rule

An initiative should be marked `complete` only when:

- must-pass criteria are satisfied
- evidence exists for the claimed completion state
- audit and decision records are current
- deferred items are explicit rather than implied complete

## Agent activation workflow

When using initiative mode, the agent should:

1. inspect the request and current repo state
2. activate the control record, audit log, and decision log before substantive implementation
3. define the initiative in concrete terms before building
4. keep the docs current as implementation and validation progress
5. close only when evidence and deferrals are explicit

## Relationship to project-pack mode

Initiative mode does not replace the full project-pack pattern.

Use project-pack mode when the repository needs a whole-product execution layer.

Use initiative mode when the work is one bounded effort inside an already-running project.

Method and process refinement usually fit this rule as well.

If the repository defines a method and the requested change is one bounded improvement to that method, govern it as an initiative and keep the generic method surfaces ahead of repo-local proof artifacts.