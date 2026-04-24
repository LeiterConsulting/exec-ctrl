---
description: "Use when updating exec-ctrl control records, audit logs, decision logs, or planning promotions in this repo. Covers authority, phase honesty, evidence, and planning-to-initiative transitions."
name: "Exec-Ctrl Docs Guidance"
applyTo:
  - "docs/exec_ctrl/**"
  - "docs/planning/**"
  - "**/*EXEC_CTRL*.md"
  - "**/*AUDIT_LOG*.md"
  - "**/*DECISION_LOG*.md"
---

# Exec-Ctrl Documentation Rules

- Keep the current phase aligned with reality. The active phase is the earliest phase that is not `complete`.
- Use only the shared execution states: `not_started`, `in_progress`, `blocked`, `complete`, `deferred`.
- Do not backfill optimistic completion language after validation fails or blockers appear.
- Record scope changes, sequencing changes, and deferrals in the decision log rather than hiding them in narrative summaries.
- Audit logs should use explicit verdicts such as `pass`, `pass_with_gaps`, or `fail`.
- Control records should keep objective, scope, success criteria, non-goals, workstreams, current status, and validation evidence current.
- Planning docs under `docs/planning/` are backlog inputs, not operational proof. When promoting an item, remove or restate it so it no longer looks untouched.
- For self-hosting slices, update generic docs first, then reusable operational surfaces, and only then repo-local proof artifacts.
- When closure is not yet justified, say exactly what still blocks it.
- When work is closed, keep deferred items explicit rather than implied complete.