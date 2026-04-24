---
description: "Use when governing improvements to a method, prompt library, template library, or governance repository under exec-ctrl. Keeps generic method changes ahead of repo-local proof artifacts."
name: "Exec-Ctrl Method Evolution"
argument-hint: "Method change objective, governed surfaces, and constraints"
agent: "agent"
---

Govern the current request as an exec-ctrl method-evolution initiative.

Steps:

1. Inspect the repository and identify which surfaces define the method now, such as docs, prompts, templates, examples, or instructions.
2. Activate initiative-mode exec-ctrl unless the request clearly requires a whole-repository execution redesign.
3. If that distinction remains unclear, apply a bounded-vs-whole-system scoring pass across surface breadth, authority impact, dependency spread, validation breadth, reuse scope, and user wording.
4. Create or update the initiative control record, audit log, and decision log before substantive changes begin.
5. Audit the gap between what the method teaches generically and what the repository currently demonstrates in practice.
6. Define the objective, scope in, scope out, deliverables, must-pass criteria, should-pass criteria, non-goals, and validation evidence for the method change.
7. Update the generic method surfaces first, then update reusable prompts, templates, and examples, and only then update the repo-local self-governing records.
8. During validation, run a self-hosting coherence checklist across generic docs, reusable activation surfaces, examples, and repo-local proof artifacts.
9. Close only when the changed surfaces agree and the remaining follow-on work is explicit.

In your response:

- state the chosen mode and why
- include the rubric outcome when ambiguity required scoring
- identify the governed method surfaces
- describe the gap between the current teaching surface and the demonstrated behavior
- list the files created or updated for the generic method, reusable activation surfaces, and repo-local proof artifacts
- summarize the must-pass criteria, the checklist outcome, and any explicit follow-on work