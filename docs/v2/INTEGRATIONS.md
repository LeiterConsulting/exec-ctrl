# Mapping exec-ctrl into existing team systems

Use the project's approved connector, CLI or existing task record. The framework
does not require a new account, plugin, server or competing system of record.
Read-only discovery can proceed within the task's scope; external messages and
shared changes need the user's authorization or an explicitly invoked workflow.

| exec-ctrl information | GitHub/GitLab | Jira/Linear/Azure DevOps | Existing document or local task |
| --- | --- | --- | --- |
| Outcome and scope | Issue/PR description | Work-item description and acceptance | Task objective |
| Contract and evidence | Required checks, test report links, diff | Acceptance/checklist plus evidence links | Acceptance table |
| Owners and dependencies | Code owners, reviewer rules, linked issues | Assignee and dependency relationships | Named owner and prerequisites |
| Security finding | Approved private finding/advisory location | Restricted security work item | Approved private register |
| Decision | Existing ADR or linked discussion | Decision note linked to work item | Short decision section |
| Release | Required CI, artifact and environment approvals | Release/change work item | Rollout and recovery record |
| Handoff | PR state and unresolved review items | Work-item state and next owner | Checkpoint and next action |

## Before an authorized write

Prepare the exact description, comment or transition against the current result.
Check destination, canonical ID, current state, applicable ownership and sensitive
content. Reuse the existing item; search its recent discussion before creating
another record. If retrying an uncertain write, fetch the destination and verify
whether it happened before retrying. Use the tool's idempotency mechanism when
available; a local identifier alone does not establish remote deduplication.

Preserve teammates' newer content. Update only the intended fields and reconcile
conflicts. A reviewable PR contains the problem/result, scope, real checks and
remaining limitations. Do not assign people, approve a change or broaden notification
recipients merely because a template mentions those fields.

## Required checks and approvals

Record enforcing systems separately from declared obligations. For example, a
ruleset may require an independent review, while branch protection enforces it.
Inspect the actual review state and source revision. A changed diff may invalidate
an earlier approval according to the project's rules. Do not substitute agent
self-review for separation of duties.

Security findings may require a private channel and approved scanner. Record tool,
version/database date, scope, disposition and actual report location. Do not post
secrets, exploit payloads or proprietary code in a public PR for convenience.

## After a write or when tools are unavailable

Verify the returned item/link and intended fields. Distinguish `draft`, `posted`,
`not synchronized`, `blocked` and `outcome unconfirmed`. A timeout is an unknown
outcome; a prepared message is a draft. Report code completion, external status,
review approval and release acceptance separately.

Use [CHECKPOINT.md](../../templates/v2/CHECKPOINT.md) or the existing task for a
handoff that remains unsent. Current support is this mapping and policy/evidence
checks, not shipped connector clients or automatic team writes.
