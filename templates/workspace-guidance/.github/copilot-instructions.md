> **v1 reference.** For new work use the [v2 activation contract](../../../START_HERE.md).
> Apply the workflow below only when explicitly maintaining a v1 adoption.

# Project Guidelines

## Exec-Ctrl Mode Selection

- Use initiative mode for bounded work such as an audit, remediation effort, refactor, hardening slice, release closeout, or subsystem addition.
- Use project-pack mode only when the request is to govern the whole product or repository.
- If the request is ambiguous, prefer initiative mode and state the boundary explicitly.
- If ambiguity remains after inspection, score surface breadth, authority impact, dependency spread, validation breadth, reuse scope, and user wording before escalating to whole-repository governance.

## Exec-Ctrl Authority

- Active user direction is authoritative over any standing documentation.
- For initiative mode, authority usually flows from the current initiative control record, then the audit log, then the decision log, then any dependent project docs.
- For project-pack mode, authority usually flows from `18_EXEC_CTRL_STATUS.md`, then `16_EXEC_CTRL_PHASE_PLAN.md`, then `17_EXEC_CTRL_TEST_AND_SUCCESS.md`, then `14_EXEC_CTRL_TARGET_PRODUCT.md`, then `15_EXEC_CTRL_PAGES_AND_FUNCTIONS.md`, then earlier concept docs.

## Execution Rules

- Create the exec-ctrl artifacts before substantive implementation.
- The active phase is the earliest phase that is not `complete`.
- Use only the shared execution states: `not_started`, `in_progress`, `blocked`, `complete`, `deferred`.
- Do not mark work complete without evidence and explicit deferrals.
- Update the control docs in the same work cycle as code, test, or operator-surface changes.

## Workspace Convention

- Initiative docs normally live under `docs/exec_ctrl/`.
- Whole-repository control docs normally use the `13` through `18` exec-ctrl series after the concept pack.
- If this repository already uses a different authoritative location or numbering model, document the adaptation explicitly in the control artifacts.

## Build And Test

Replace this section with repository-specific commands before relying on this file.

- Build: `<replace with build command>`
- Test: `<replace with test command>`
- Lint or typecheck: `<replace with validation command>`