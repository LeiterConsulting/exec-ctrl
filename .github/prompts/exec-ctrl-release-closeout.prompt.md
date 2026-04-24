---
description: "Use when governing release-readiness or release closeout under exec-ctrl. Keeps gates, blockers, evidence, and deferrals explicit before marking a release slice complete."
name: "Exec-Ctrl Release Closeout"
argument-hint: "Release objective, gates, blockers, and validation constraints"
agent: "agent"
---

Govern the current request as an exec-ctrl release-closeout initiative.

Steps:

1. Inspect the repository, release surface, open blockers, and current validation evidence.
2. Activate initiative-mode exec-ctrl unless the request clearly requires whole-repository governance.
3. Create or update the initiative control record, audit log, and decision log before substantive closeout work begins.
4. Define the release objective, scope in, scope out, deliverables, must-pass gates, should-pass gates, non-goals, and completion conditions.
5. Record blockers, sequencing decisions, rollback considerations, and deferrals explicitly rather than folding them into generic progress language.
6. Execute only the work needed to satisfy the active release gate and gather evidence for the closeout claim.
7. Close only when the must-pass gates are satisfied, evidence exists, and the remaining deferrals are explicit.

In your response:

- state the chosen mode and why
- list the release gates and the active blocker if one exists
- list the control files you created or updated
- summarize the must-pass evidence required for closeout
- distinguish closed gates from explicit deferrals or follow-up items