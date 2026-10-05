> **v1 reference.** For new work use the [v2 activation contract](../START_HERE.md).
> Apply the workflow below only when explicitly maintaining a v1 adoption.

# Exec-Ctrl Workspace Guidance Validation Checklist

## Purpose

Use this checklist after copying [templates/workspace-guidance](../templates/workspace-guidance) into a target repository.

It is the validation step that turns copied prompt and instruction templates into repo-specific guidance that later agent sessions can trust.

Do not treat the copied `.github/` files as ready until this checklist passes.

## Pass Condition

The copied workspace-guidance layer is ready only when:

- placeholder text is gone
- build, test, and validation commands are repo-specific
- doc paths and authority references match the target repository
- only the prompt bundles the target repo actually needs remain active
- the result is recorded in the active exec-ctrl evidence surface

## Validation Checklist

### 1. Placeholder Sweep

- search the copied `.github/` files for `<replace with`, `Replace this section`, `placeholder`, and any source-repo wording that should not survive the copy
- confirm `.github/copilot-instructions.md` no longer contains template commands or generic reminder text that depends on manual follow-up
- if any placeholder remains, stop and finish customization before relying on the copied guidance

### 2. Build, Test, And Validation Commands

- replace the template build, test, and lint or typecheck commands with commands that exist in the target repo
- prefer the narrowest commands that produce evidence for the active bootstrap or initiative
- run those commands or explicitly verify the repo's equivalent validation path before closure

### 3. Doc Location And Authority Alignment

- confirm the copied guidance points to the real control-doc location such as `docs/exec_ctrl/` or the target repo's numbered exec-ctrl series
- if the repo uses a different path or naming model, update the copied instructions and prompts explicitly
- make sure the copied guidance does not claim authority over docs that the target repo does not actually use

### 4. Prompt Bundle Fit

- keep `bootstrap-exec-ctrl.prompt.md`
- keep only the task-shape prompt bundles that match recurring work in the target repo
- remove, defer, or document prompt bundles that would create noise or imply unsupported workflows
- if the repo already has equivalent prompts, reconcile them instead of leaving duplicate entry points behind

### 5. Guidance Surface Conflicts

- use `.github/copilot-instructions.md` or `AGENTS.md`, not both, unless the target repo already documents a safe coexistence rule
- remove or reconcile conflicting guidance that would make later sessions guess which file is authoritative
- confirm the copied guidance does not contradict repository-specific contribution, build, or operator docs

### 6. Repo-Specific Substitutions

- replace source-repo assumptions in prompt text, folder paths, command names, and examples
- confirm the target repo's package manager, test runner, and doc folders are named correctly
- if the target repo does not use exec-ctrl numbering, remove that assumption from the copied guidance

### 7. Evidence Capture

- record the completed validation in the active initiative audit log, decision log, or equivalent bootstrap evidence surface
- note any deferred prompt bundles or unresolved guidance gaps explicitly rather than implying they were handled
- close the bootstrap or refinement only when the copied guidance is both customized and checked

## Recommended Validation Sweep

1. copy the workspace-guidance pack
2. customize `.github/copilot-instructions.md` and any copied prompts
3. run a text search over `.github/` for placeholder markers and source-repo wording
4. verify or run the repo-specific build, test, and validation commands
5. record the result in the active exec-ctrl evidence surface

## Common Failure Modes

- leaving template commands untouched
- pointing to the wrong control-doc folder
- copying every prompt bundle even though the repo only needs one or two
- keeping duplicate or conflicting guidance files
- treating the copied guidance as done without evidence

This checklist is intentionally small.

It should be cheap enough to use on every repo-link bootstrap and strict enough to keep copied guidance from becoming stale template residue.