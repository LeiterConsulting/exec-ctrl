---
description: "Use when governing a bounded refactor under exec-ctrl. Preserves external behavior while creating initiative control docs, validation evidence, and explicit cleanup deferrals."
name: "Exec-Ctrl Refactor Initiative"
argument-hint: "Refactor goal, target boundary, and compatibility constraints"
agent: "agent"
---

> **v1 reference.** For new work use the [v2 activation contract](../../../../START_HERE.md).
> Apply the workflow below only when explicitly maintaining a v1 adoption.

Govern the current request as an exec-ctrl refactor initiative.

Steps:

1. Inspect the current implementation boundary, public contract, and existing validation surface.
2. Activate initiative-mode exec-ctrl unless the request clearly needs whole-repository governance.
3. Create or update the initiative control record, audit log, and decision log before substantive refactor work begins.
4. Define the objective, scope in, scope out, deliverables, must-pass criteria, should-pass criteria, non-goals, and compatibility expectations.
5. Identify the smallest refactor slices that advance the active phase without widening into unrelated cleanup.
6. Implement the refactor, gather narrow validation evidence, and record any residual cleanup as explicit deferrals.
7. Close only when the must-pass criteria are satisfied and the evidence supports the claimed compatibility and boundary improvement.

In your response:

- state the chosen mode and why
- name the target boundary and the contract that must remain stable
- list the files you created or updated for control and implementation
- summarize the must-pass criteria and validation surface
- list any explicit deferrals that remain out of scope for this slice