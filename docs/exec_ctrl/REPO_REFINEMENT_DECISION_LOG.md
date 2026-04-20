# Exec-Ctrl Repo Refinement Decision Log

| ID | Date | Decision | Rationale | Consequence |
| --- | --- | --- | --- | --- |
| `D-001` | `2026-04-20` | govern the repo refinement under initiative-mode exec-ctrl | the requested work is a bounded enhancement effort inside an already-active repo | the repo uses its own bounded-work process rather than pretending this update is a whole-project control exercise |
| `D-002` | `2026-04-20` | add two generic examples representing different initiative shapes | the repo needed examples that were reusable and not tied to a specific product history | one audit-heavy example and one refactor example are now included |
| `D-003` | `2026-04-20` | unify the core status vocabulary across both modes | future agents need predictable control language more than extra status labels | both modes now anchor on the same core execution states, while lifecycle nuance stays in phases and narrative |
| `D-004` | `2026-04-20` | add a dedicated prompt cookbook instead of burying invocation rules only in the README | future users are likely to reference the repo conversationally, not by reading every method doc first | the repo now has a short entry point specifically for agent invocation and behavior mapping |