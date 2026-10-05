> **v1 reference.** For new work use the [v2 activation contract](../../START_HERE.md).
> Apply the workflow below only when explicitly maintaining a v1 adoption.

# Exec-Ctrl Initiative Pack

This template pack is the default bounded-work exec-ctrl pattern.

Use it when the user wants a specific effort governed under exec-ctrl without converting the entire repository to the full project-pack model.

## Recommended placement

Copy these files into a folder such as:

- `docs/exec_ctrl/`

Then rename them to match the initiative.

Examples:

- `CHAT_UX_EXEC_CTRL.md`
- `CHAT_UX_AUDIT_LOG.md`
- `CHAT_UX_DECISION_LOG.md`

## Required files

- `INITIATIVE_EXEC_CTRL.md`
- `INITIATIVE_AUDIT_LOG.md`
- `INITIATIVE_DECISION_LOG.md`

## Optional files

- `OPTIONAL_FINDINGS_REGISTER.md`
- `OPTIONAL_REMEDIATION_ISSUE_TEMPLATE.md`

Use the optional files when the initiative is audit-heavy or will produce a remediation backlog.

## Repo-link bootstrap pairing

When initiative mode is activated from a repo link rather than by manual template copying alone, also copy the workspace-guidance files from `templates/workspace-guidance/.github/` into the target repository.

That keeps later agent sessions aligned with the control docs after the initial bootstrap work is complete.

## Activation rule

Before substantive implementation:

1. rename the files for the initiative
2. fill in the control summary, objective, scope, and success criteria
3. create the first baseline audit entry
4. log any initial scope or sequencing decision that materially shapes the work

## Shared status vocabulary

Use the same core execution states as project-pack mode:

- `not_started`
- `in_progress`
- `blocked`
- `complete`
- `deferred`

Use phase names and narrative sections for extra lifecycle detail.

## Update rule

During implementation:

- update the control record when scope, status, workstreams, or evidence state changes
- update the audit log when a checkpoint or validation step becomes authoritative
- update the decision log when a meaningful scope, sequencing, or deferral choice is made

## Closure rule

The initiative is not complete because the work feels done.

It is complete when:

- must-pass criteria are satisfied
- evidence exists
- deferred items are explicit
- the control artifacts match reality