---
description: "Resume an exec-ctrl task from current inputs and its existing checkpoint."
name: "Exec-Ctrl Resume"
argument-hint: "Task or checkpoint reference, latest steering, and affected target"
agent: "agent"
---

Read [START_HERE.md](../../START_HERE.md) and the relevant
[session loop](../../docs/v2/SESSION_LOOP.md). Inspect current instructions,
branch/dirty state and affected inputs before trusting prior evidence. Incorporate
the latest user steering, preserve completed work that remains valid, and continue
the next authorized action. Reuse existing records; do not create a second task
or write adoption files solely to resume. Report exact blockers and evidence gaps.
