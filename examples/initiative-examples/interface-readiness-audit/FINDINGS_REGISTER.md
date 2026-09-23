> **v1 reference.** For new work use the [v2 activation contract](../../../START_HERE.md).
> Apply the workflow below only when explicitly maintaining a v1 adoption.

# Interface Readiness Findings Register

| ID | Severity | Area | Surface | Finding | Evidence | Recommended Direction | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `IRA-F001` | `high` | semantics | primary action cluster | actions are visible but not exposed through clear structure or state | code review plus live interaction evidence | convert the action pattern to a semantic, state-exposing structure | `closed` |
| `IRA-F002` | `high` | clarity | operator status text | status language is ambiguous and leaves operator intent unclear | live review of labels and helper text | replace vague language with operator-facing descriptions | `closed` |
| `IRA-F003` | `medium` | readability | low-emphasis metadata | secondary information is hard to scan in common states | visual review and targeted checks | tune emphasis and keep it in the follow-up backlog if not blocking | `deferred` |