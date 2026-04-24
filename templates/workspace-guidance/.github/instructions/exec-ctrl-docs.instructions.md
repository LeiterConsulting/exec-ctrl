---
description: "Use when creating or updating exec-ctrl control records, audit logs, decision logs, or project-pack status docs. Covers authority order, phase honesty, evidence, and deferrals."
name: "Exec-Ctrl Docs Guidance"
applyTo:
  - "docs/exec_ctrl/**"
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
- When closure is not yet justified, say exactly what still blocks it.
- When work is closed, keep deferred items explicit rather than implied complete.