---
description: "Use when the boundary between a bounded initiative and a whole-system control path is unclear. Applies the bounded-vs-whole-system scoring rubric and makes the chosen control path explicit."
name: "Exec-Ctrl Rubric Review"
argument-hint: "Request, repo context, and ambiguity to score"
agent: "agent"
---

Review the current request with the bounded-vs-whole-system scoring rubric.

Steps:

1. Inspect the request and the current repository context.
2. Apply any hard overrides first. Do not let scoring overrule explicit user direction.
3. If no hard override resolves the path, score these categories from `0` to `2`: surface breadth, authority impact, dependency spread, validation breadth, reuse scope, and user wording.
4. Add the total score and interpret it against the rubric thresholds.
5. Choose the control path: bounded initiative or whole-system effort.
6. Record the categories that drove the outcome, plus any non-goals, watchpoints, or escalation conditions that should be explicit.

In your response:

- state whether a hard override applied
- show the category scores and total score when scoring was needed
- name the chosen control path and explain why
- list the main factors that drove the decision
- list any boundaries, non-goals, or watchpoints that should be recorded if the work proceeds