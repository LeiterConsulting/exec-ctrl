---
description: "Use when bootstrapping exec-ctrl for the current repository from a new task request. Chooses the mode, creates control docs, and installs workspace guidance."
name: "Bootstrap Exec-Ctrl"
argument-hint: "Task, scope, and constraints"
agent: "agent"
---

Bootstrap exec-ctrl for the current repository using the prompt argument as the task request.

Steps:

1. Inspect the repository and the current request.
2. Decide whether the work is whole-project or bounded-initiative. Default to initiative mode unless whole-repository governance is clearly required.
3. If ambiguity remains, apply a bounded-vs-whole-system scoring pass across surface breadth, authority impact, dependency spread, validation breadth, reuse scope, and user wording.
4. Before substantive implementation, create the required control artifacts.
5. If the repository does not already have equivalent guidance, add the workspace-guidance files under `.github/`.
6. Convert the request into objective, scope in, scope out, deliverables, must-pass criteria, should-pass criteria, non-goals, workstreams, and validation evidence expectations.
7. Keep the control docs current while implementation and validation proceed.
8. Close only when evidence exists and deferred items are explicit.

In your response:

- state the chosen mode and why
- include the rubric outcome when ambiguity required scoring
- list the files you created or updated
- name the active phase
- list the must-pass criteria
- note any missing information that still blocks accurate activation