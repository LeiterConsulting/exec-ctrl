> **v1 reference.** For new work use the [v2 activation contract](../../START_HERE.md).
> Apply the workflow below only when explicitly maintaining a v1 adoption.

# Exec-Ctrl Phase Plan

## Phase control rule

The active phase is the earliest phase that is not `complete`.

Later work may be designed, but the next implementation move is controlled by the active phase.

## Phase ladder

| Phase | Name | Status | Exit control |
| --- | --- | --- | --- |
| 0 | Foundation baseline | `not_started` | Define the first technical gate |
| 1 | Control-plane completion | `not_started` | Define the next real gate |
| 2 | Core operator workflow | `not_started` | Define the next real gate |
| 3 | Main feature workflow | `not_started` | Define the next real gate |
| 4 | Safe approval and recovery | `not_started` | Define the next real gate |
| 5 | Strategic expansion | `not_started` | Define the next real gate |
| 6 | Hardening and handoff | `not_started` | Define the final gate |

## Phase detail

For each phase, define:
- objective
- required scope
- current status
- current blocker if any
- exit gate

## Current next phase

State the current active phase and why it is still the active one.

Do not describe the next phase aspirationally. Describe it according to real status.