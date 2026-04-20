# Exec-Ctrl Method

## Definition

Exec-ctrl means execution control.

It is a documentation-driven implementation discipline where:
- the product direction is defined in advance
- the current phase is explicit
- each phase has an exit gate
- tests and evidence determine completion
- the next phase is chosen by status, not by preference
- the docs are updated as implementation changes

## Why use it

Exec-ctrl is useful when a project is larger than a quick prototype but still evolving during implementation.

It prevents several common failures:
- skipping unresolved dependencies
- claiming progress without evidence
- building later features while earlier gates are still broken
- losing track of what is authoritative
- letting docs drift away from real implementation status

It is also useful for bounded initiatives inside an already-active repository when the user wants one slice of work to be governed explicitly before implementation starts.

## Minimum document set

The minimum authoritative layer is six docs:

1. overview
2. target product
3. pages and functions
4. phase plan
5. test and success
6. status

For bounded initiative mode, the minimum set is three docs:

1. control record
2. audit log
3. decision log

Optional supporting docs such as findings registers or remediation templates can be added when the initiative is audit-heavy.

## Operating modes

Exec-ctrl supports two operating modes:

### Full project mode

Use the full six-document project pack when the repository needs an authoritative execution layer for the product as a whole.

### Initiative mode

Use initiative mode when the work is a bounded slice inside an active repository.

Typical triggers:

- refactor effort
- audit and remediation effort
- UX or accessibility slice
- subsystem or integration slice
- release-readiness closeout
- any request phrased as "use the exec-ctrl repo to do this work"

If the request is bounded and does not require whole-project control, initiative mode should be the default.

## Authority model

When the project uses exec-ctrl, the authority usually flows like this:

1. active user direction
2. live status doc
3. phase plan doc
4. test and success doc
5. target product doc
6. pages and functions doc
7. earlier concept pack

For initiative mode, the same idea applies in lighter form:

1. active user direction
2. initiative control record
3. initiative audit log
4. initiative decision log
5. any underlying project docs the initiative depends on

## Shared core status vocabulary

Use a small closed set:

- `not_started`
- `in_progress`
- `blocked`
- `complete`
- `deferred`

Do not create ad hoc status words unless the project has a very strong reason.

This shared vocabulary should be used in both project mode and initiative mode.

Use phase names, checkpoints, and narrative status sections to express lifecycle nuance such as activation, definition, validation, or closeout.

## Phase advancement rule

The active phase is the earliest phase that is not `complete`.

Implications:
- later phases can be designed early
- later phases should not be declared complete before dependent earlier phases
- a blocked phase stays active until the blocker is removed or direction changes

## Evidence rule

A phase is not complete because the team believes it is complete.

A phase is complete when evidence exists.

Accepted evidence may include:
- automated tests
- narrow compile or syntax validation
- live API verification
- live browser verification
- explicit blocker evidence when completion is not yet possible

In initiative mode, evidence should also be tied to the must-pass criteria that the initiative defined before implementation started.

## Update rule

Implementation and exec-ctrl docs must move together.

At minimum:
- update the status doc when real completion status changes
- update the phase plan when a blocker or exit gate changes
- update the test doc when new evidence appears or a new test becomes required
- update the pages/functions doc when the operator surface or capability map changes

For initiative mode:

- update the control record when scope, phase, workstreams, or evidence state changes
- update the audit log whenever a checkpoint becomes authoritative
- update the decision log whenever a material scope, sequencing, or deferral choice is made

## Recommended workflow

1. create the concept pack
2. add the exec-ctrl layer
3. identify the active phase
4. implement only the next meaningful slice that advances the active phase
5. validate with evidence
6. update the exec-ctrl docs
7. move to the next phase only when the gate is actually met

For initiative mode, the workflow is:

1. inspect the user request and current repo state
2. activate the initiative control record, audit log, and decision log
3. define objective, scope, deliverables, must-pass criteria, should-pass criteria, and non-goals
4. implement only the slices that advance the current initiative phase
5. validate against the initiative criteria with evidence
6. close only when completion and deferrals are explicit

## Agent activation rule

When a future user says "use the exec-ctrl repo to do the following work", the agent should:

1. decide whether the request needs full project mode or initiative mode
2. default to initiative mode unless the request clearly demands whole-project governance
3. create the control artifacts before substantive implementation
4. keep those artifacts current while the work is executed and validated

## Cookbook rule

If the future agent needs examples of how a request should map to exec-ctrl behavior, it should consult:

- [docs/EXEC_CTRL_AGENT_PROMPT_COOKBOOK.md](EXEC_CTRL_AGENT_PROMPT_COOKBOOK.md)
- [examples/initiative-examples](../examples/initiative-examples)

## Practical guidance

- keep the status doc brutally honest
- do not hide blockers inside progress language
- do not mark later phases complete while the active gate is still open
- make operator-visible surfaces map cleanly to backend functions and tests
- prefer concrete evidence over broad narrative summaries
- define non-goals early so bounded work does not sprawl
- separate must-pass criteria from should-pass criteria when using initiative mode
- record deferrals explicitly instead of leaving them implied in completion language

## Template placement

The template pack keeps numbering `13` through `18` so it can sit after a typical `01` through `12` concept pack.

If a project uses a different numbering model, adapt the numbers while preserving the six-document structure.

For bounded-work use, the initiative pack is intended to live in a folder such as `docs/exec_ctrl/` with initiative-specific filenames.