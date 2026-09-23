> **v1 reference.** For new work use the [v2 activation contract](../../../START_HERE.md).
> Apply the workflow below only when explicitly maintaining a v1 adoption.

# Service Refactor Decision Log

| ID | Date | Decision | Rationale | Consequence |
| --- | --- | --- | --- | --- |
| `D-001` | `YYYY-MM-DD` | govern the refactor under initiative-mode exec-ctrl | the work is bounded but still needs explicit safety and closure rules | the refactor is tracked through control, audit, and decision artifacts |
| `D-002` | `YYYY-MM-DD` | preserve the existing contract unless explicit change is approved | the refactor should reduce risk, not create accidental external breakage | interface stability becomes a must-pass criterion |
| `D-003` | `YYYY-MM-DD` | defer additional opportunistic cleanup outside the chosen boundary | broad cleanup would dilute the initiative and blur validation | follow-on refactor opportunities are recorded separately |