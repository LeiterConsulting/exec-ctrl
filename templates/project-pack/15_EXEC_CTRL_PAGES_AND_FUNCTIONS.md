# Exec-Ctrl Pages And Functions

## Page inventory

This matrix defines the required operator surfaces.

| Surface | Purpose | Required actions | Current state | Release target |
| --- | --- | --- | --- | --- |
| Surface 1 | What the operator does here | Main actions | `not_started` | Release 1 |
| Surface 2 | What the operator does here | Main actions | `not_started` | Release 1 |

## Backend function inventory

| Function | Current owner | Current state | Notes |
| --- | --- | --- | --- |
| Function 1 | Service or module | `not_started` | Notes |
| Function 2 | Service or module | `not_started` | Notes |

## API or interface inventory

List the current interfaces the operator surfaces depend on.

Examples:
- REST endpoints
- message bus channels
- job interfaces
- queue consumers
- filesystem operations

## Required new function groups

List capability groups still required before the target product is complete.

## Operator flow ownership

The execution control rule is simple:

- every operator action must map to a page
- every page action must map to a backend function or interface
- every backend function must map to a phase gate in [16_EXEC_CTRL_PHASE_PLAN.md](16_EXEC_CTRL_PHASE_PLAN.md)