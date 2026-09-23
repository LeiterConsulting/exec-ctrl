---
description: "Use when governing an audit, assessment, or audit-remediation slice under exec-ctrl. Creates findings-oriented control docs and keeps severity, remediation, and deferrals explicit."
name: "Exec-Ctrl Audit Initiative"
argument-hint: "Audit objective, target surfaces, and constraints"
agent: "agent"
---

> **v1 reference.** For new work use the [v2 activation contract](../../../../START_HERE.md).
> Apply the workflow below only when explicitly maintaining a v1 adoption.

Govern the current request as an exec-ctrl audit initiative.

Steps:

1. Inspect the repository and identify the bounded surfaces that the audit should cover.
2. Activate initiative-mode exec-ctrl unless the request clearly requires whole-repository governance.
3. Create or update the initiative control record, audit log, and decision log before substantive implementation.
4. Add optional findings and remediation artifacts when the initiative is audit-heavy.
5. Define the objective, scope in, scope out, deliverables, must-pass criteria, should-pass criteria, non-goals, and severity model before remediation starts.
6. Perform the audit, classify the findings, implement the highest-value fixes that fit the slice, and record lower-priority deferrals explicitly.
7. Close only when must-pass criteria are backed by evidence and the audit artifacts match reality.

In your response:

- state the chosen mode and why
- identify the audited surfaces
- list the control and findings files you created or updated
- summarize the must-pass criteria and severity approach
- distinguish fixed issues from explicit deferrals