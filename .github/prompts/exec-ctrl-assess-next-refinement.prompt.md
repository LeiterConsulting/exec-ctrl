---
description: "Use when the user asks to continue refining the exec-ctrl repo itself. Inspects planning and recent proof artifacts, chooses one bounded slice, activates control docs, and closes with explicit follow-on work."
name: "Exec-Ctrl Assess Next Refinement"
argument-hint: "Current request, constraints, and any candidate areas to favor or avoid"
agent: "agent"
---

Assess the next bounded self-hosting refinement for the current `exec-ctrl` workspace and execute it under exec-ctrl.

Steps:

1. Inspect active user direction, `README.md`, `docs/EXEC_CTRL_METHOD.md`, `docs/EXEC_CTRL_SELF_HOSTING_AND_METHOD_EVOLUTION.md`, `docs/EXEC_CTRL_AGENT_ASSESSMENT_LOOP.md`, `docs/planning/FUTURE_ENHANCEMENTS.md`, and relevant records under `docs/exec_ctrl/`.
2. Decide whether the request is a bounded self-hosting slice or a whole-repository redesign. Default to initiative mode unless the whole execution model must change.
3. If ambiguity remains, apply the bounded-vs-whole-system scoring rubric.
4. Choose one bounded refinement based on repeated need, current planning signals, user direction, and the smallest coherent teaching-and-proof loop.
5. Before substantive edits, create or update the initiative control record, audit log, and decision log.
6. Define objective, scope in, scope out, deliverables, must-pass criteria, should-pass criteria, non-goals, workstreams, and validation evidence.
7. Update generic docs first, then reusable operational surfaces such as prompts, templates, instructions, or examples, and only then repo-local proof artifacts.
8. Validate coherence across the changed surfaces and keep the planning area accurate if a candidate was promoted.
9. Close only when evidence exists and the next follow-on work is explicit.

In your response:

- state the chosen slice and why it was selected
- state the chosen control path and rubric outcome when scoring was needed
- identify the governed surfaces
- list the files created or updated for generic docs, reusable operational surfaces, and repo-local proof artifacts
- summarize the must-pass criteria, validation outcome, and explicit follow-on work