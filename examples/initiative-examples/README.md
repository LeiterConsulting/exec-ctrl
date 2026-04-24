# Initiative Example Packs

These examples show how initiative-mode exec-ctrl can be applied without relying on product-specific history.

## Included examples

### Interface Readiness Audit

Use this pattern when the initiative is audit-heavy and will likely produce findings, remediation issues, and severity-based decisions.

Files included:

- control record
- audit log
- decision log
- findings register
- remediation issue template

### Service Refactor

Use this pattern when the initiative is implementation-heavy and needs explicit interface-preservation, validation, and rollback discipline.

Files included:

- control record
- audit log
- decision log

### Method Evolution

Use this pattern when the initiative is improving a method, template library, prompt pack, or governance repository using the same control system it defines.

Files included:

- control record
- audit log
- decision log

### Prompt Library Evolution

Use this pattern when the initiative expands or hardens recurring prompt surfaces so the method becomes easier to invoke from workspace context.

Files included:

- control record
- audit log
- decision log

### Template Library Hardening

Use this pattern when the initiative tightens reusable templates and their validation path to reduce copy drift without changing the core method.

Files included:

- control record
- audit log
- decision log

### Governance Model Migration

Use this pattern when one bounded governance workflow must move into exec-ctrl with explicit sequencing and fallback posture.

Files included:

- control record
- audit log
- decision log

## How to use these examples

1. choose the example closest to the requested initiative shape
2. copy the structure into the target repository
3. rename the files for the real initiative
4. replace the example content with the actual scope, evidence, and decisions for the live work