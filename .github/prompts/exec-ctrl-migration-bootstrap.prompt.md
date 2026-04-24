---
description: "Use when governing migration-shaped work under exec-ctrl. Captures baseline inventory, sequencing, rollback expectations, and evidence before implementing the migration slice."
name: "Exec-Ctrl Migration Bootstrap"
argument-hint: "Migration goal, source and target state, and safety constraints"
agent: "agent"
---

Govern the current request as an exec-ctrl migration initiative.

Steps:

1. Inspect the repository and identify the migration source state, target state, dependencies, and rollback concerns.
2. Activate initiative-mode exec-ctrl unless the request clearly requires whole-repository governance.
3. Create or update the initiative control record, audit log, and decision log before substantive migration work begins.
4. Define the migration objective, scope in, scope out, deliverables, must-pass criteria, should-pass criteria, non-goals, sequencing, and rollback expectations.
5. Capture baseline evidence for the current state before implementing changes.
6. Execute the migration in bounded slices, validating each meaningful checkpoint and recording blockers or deferrals explicitly.
7. Close only when the must-pass criteria, migration evidence, and rollback or fallback posture are documented clearly.

In your response:

- state the chosen mode and why
- summarize the source state, target state, and migration boundary
- list the control files you created or updated
- summarize the must-pass criteria, sequencing, and rollback expectations
- identify any remaining blockers, risks, or deferred follow-up work