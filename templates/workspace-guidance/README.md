> **v1 reference.** For new work use the [v2 activation contract](../../START_HERE.md).
> Apply the workflow below only when explicitly maintaining a v1 adoption.

# Workspace Guidance Template Pack

This template pack adds the agent-facing workspace guidance layer that pairs with exec-ctrl control docs.

Use it when a target repository needs more than the markdown control records alone.

It is especially useful when exec-ctrl is being activated from a repo link and later sessions need to keep following the same authority model.

## Included files

- `.github/copilot-instructions.md`
- `.github/instructions/exec-ctrl-docs.instructions.md`
- `.github/prompts/bootstrap-exec-ctrl.prompt.md`
- `.github/prompts/exec-ctrl-audit.prompt.md`
- `.github/prompts/exec-ctrl-checklist-review.prompt.md`
- `.github/prompts/exec-ctrl-method-evolution.prompt.md`
- `.github/prompts/exec-ctrl-rubric-review.prompt.md`
- `.github/prompts/exec-ctrl-refactor.prompt.md`
- `.github/prompts/exec-ctrl-release-closeout.prompt.md`
- `.github/prompts/exec-ctrl-migration-bootstrap.prompt.md`

## What each file does

### `.github/copilot-instructions.md`

Provides the always-on project guidance for mode selection, authority order, status vocabulary, and evidence discipline.

### `.github/instructions/exec-ctrl-docs.instructions.md`

Provides targeted rules for updating control records, audit logs, decision logs, and related exec-ctrl docs.

### `.github/prompts/bootstrap-exec-ctrl.prompt.md`

Provides a reusable chat prompt for activating exec-ctrl in the current workspace.

### `.github/prompts/exec-ctrl-audit.prompt.md`

Provides a reusable chat prompt for audit-heavy initiatives that should create findings, remediation, and explicit deferrals.

### `.github/prompts/exec-ctrl-checklist-review.prompt.md`

Provides a reusable chat prompt for applying the self-hosting coherence checklist as a one-command review during method-evolution validation.

### `.github/prompts/exec-ctrl-method-evolution.prompt.md`

Provides a reusable chat prompt for method, template, prompt, or governance-system improvements that should be governed under exec-ctrl while updating the method itself.

### `.github/prompts/exec-ctrl-rubric-review.prompt.md`

Provides a reusable chat prompt for ambiguous mode-selection cases that should apply the bounded-vs-whole-system scoring rubric in one command.

### `.github/prompts/exec-ctrl-refactor.prompt.md`

Provides a reusable chat prompt for bounded refactor work that must preserve the external contract while improving structure.

### `.github/prompts/exec-ctrl-release-closeout.prompt.md`

Provides a reusable chat prompt for release-readiness and closeout work where gates, blockers, and residual deferrals must stay explicit.

### `.github/prompts/exec-ctrl-migration-bootstrap.prompt.md`

Provides a reusable chat prompt for migration-shaped work that needs baseline inventory, sequencing, rollback awareness, and evidence before closure.

## Installation steps

1. Copy the `.github/` folder from this pack into the target repository.
2. Replace all placeholders in `.github/copilot-instructions.md` with the real repo commands and paths.
3. Run [../../docs/EXEC_CTRL_WORKSPACE_GUIDANCE_VALIDATION_CHECKLIST.md](../../docs/EXEC_CTRL_WORKSPACE_GUIDANCE_VALIDATION_CHECKLIST.md) before treating the copied guidance as authoritative.
4. Adjust the doc locations if the repo uses something other than `docs/exec_ctrl/` or the `13` through `18` numbering model.
5. Remove any duplicated or conflicting agent guidance already present in the target repo.

## Important constraints

- use `copilot-instructions.md` or `AGENTS.md`, not both
- do not leave placeholder build and test commands in the target repo
- do not skip the validation checklist after copying the template pack
- keep the copied guidance smaller than the control docs themselves; the control docs remain the authoritative execution surface

## Pairing recommendation

Copy this pack together with:

- [templates/initiative-pack](../initiative-pack) for bounded work
- [templates/project-pack](../project-pack) for whole-repository execution control

## Recommended usage pattern

Start with `bootstrap-exec-ctrl.prompt.md` when the workspace has no control docs yet.

Use `exec-ctrl-checklist-review.prompt.md` when a self-hosting or method-evolution slice needs a dedicated coherence review.

Use `exec-ctrl-rubric-review.prompt.md` when the boundary between one bounded slice and a whole-system control effort is unclear.

Then use the task-shape prompts when the work is clearly one of these patterns:

- audit and remediation
- method and process evolution
- bounded refactor
- release closeout
- migration bootstrap