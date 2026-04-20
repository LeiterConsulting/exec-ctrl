# Exec-Ctrl Overview

## Purpose

This exec-ctrl series turns the existing product pack into an authoritative execution system.

It exists to:
- define the target product from the current real project state
- define the required pages, functions, and operator flows
- define the phase ladder and the gate for each phase
- define what evidence is required before a phase can be marked complete
- define what the next phase is based on actual completion status

## What this series controls

Docs `13` through `18` control live implementation work.

They do not replace the original concept pack. They sit on top of it and convert it into an execution discipline.

## Authority order

Use this order whenever docs disagree:

1. Explicit user direction in the active conversation
2. [18_EXEC_CTRL_STATUS.md](18_EXEC_CTRL_STATUS.md)
3. [16_EXEC_CTRL_PHASE_PLAN.md](16_EXEC_CTRL_PHASE_PLAN.md)
4. [17_EXEC_CTRL_TEST_AND_SUCCESS.md](17_EXEC_CTRL_TEST_AND_SUCCESS.md)
5. [14_EXEC_CTRL_TARGET_PRODUCT.md](14_EXEC_CTRL_TARGET_PRODUCT.md)
6. [15_EXEC_CTRL_PAGES_AND_FUNCTIONS.md](15_EXEC_CTRL_PAGES_AND_FUNCTIONS.md)
7. Original concept pack docs `01` through `12`

## Required update behavior

When implementation changes, the agent or team must update the authoritative docs in the same work cycle.

Minimum rule set:
- update [18_EXEC_CTRL_STATUS.md](18_EXEC_CTRL_STATUS.md) whenever completion status changes
- update [15_EXEC_CTRL_PAGES_AND_FUNCTIONS.md](15_EXEC_CTRL_PAGES_AND_FUNCTIONS.md) whenever a new page, endpoint, or major service responsibility changes
- update [16_EXEC_CTRL_PHASE_PLAN.md](16_EXEC_CTRL_PHASE_PLAN.md) whenever a phase gate changes or a blocker is added or cleared
- update [17_EXEC_CTRL_TEST_AND_SUCCESS.md](17_EXEC_CTRL_TEST_AND_SUCCESS.md) whenever a new test is required or a new test result becomes authoritative evidence

## Status vocabulary

Use only these execution states:

- `not_started`
- `in_progress`
- `blocked`
- `complete`
- `deferred`

## Advancement rule

The current phase is the earliest phase that is not `complete`.

Rules:
- a later phase may be designed while an earlier phase is open
- a later phase may not be claimed complete while an earlier dependent phase is incomplete
- a blocked phase remains the active phase until the blocker is removed or the user explicitly changes direction
- evidence is required before any phase changes to `complete`

## Document roles

- [14_EXEC_CTRL_TARGET_PRODUCT.md](14_EXEC_CTRL_TARGET_PRODUCT.md): the finished product definition
- [15_EXEC_CTRL_PAGES_AND_FUNCTIONS.md](15_EXEC_CTRL_PAGES_AND_FUNCTIONS.md): the required operator surfaces and backend capability map
- [16_EXEC_CTRL_PHASE_PLAN.md](16_EXEC_CTRL_PHASE_PLAN.md): the gated delivery ladder
- [17_EXEC_CTRL_TEST_AND_SUCCESS.md](17_EXEC_CTRL_TEST_AND_SUCCESS.md): the authoritative test and evidence model
- [18_EXEC_CTRL_STATUS.md](18_EXEC_CTRL_STATUS.md): the live snapshot and next-phase controller

## Current control point

Replace this section with a short, reality-based statement about:
- what is already real
- what the active phase is
- why that phase is still active