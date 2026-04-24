# Exec-Ctrl Self-Hosting Coherence Checklist

## Purpose

Use this checklist during `Phase 4 Validate` for bounded method-evolution or self-hosting initiatives.

Its job is to test whether the changed surfaces still teach one coherent workflow rather than a mixture of generic guidance, prompt behavior, and repo-local proof artifacts that disagree with each other.

For recurring failure-pattern calibration, use [EXEC_CTRL_SELF_HOSTING_COHERENCE_FAILURE_CALIBRATION.md](EXEC_CTRL_SELF_HOSTING_COHERENCE_FAILURE_CALIBRATION.md) alongside this checklist.

If the workspace-guidance prompt pack is installed, you can run this review as a one-command workflow with `.github/prompts/exec-ctrl-checklist-review.prompt.md`.

## How to use it

1. Review each checklist section against the changed surfaces in the initiative.
2. Record the outcome in the initiative audit log using `pass`, `pass_with_gaps`, or `fail`.
3. Treat every must-pass item as required for closure unless the user explicitly approves a deferral.
4. If an item fails, update the generic method first, then reusable activation surfaces, then repo-local proof artifacts.

## Must-pass checklist

### 1. Generic teaching surfaces

- [ ] The generic method docs explicitly describe the refined behavior rather than leaving it implied only in local records.
- [ ] Authority order, evidence rules, and phase logic still match the rest of exec-ctrl.
- [ ] Entry docs route future users to the correct method path.

Typical evidence:

- `README.md`
- generic guides under `docs/`
- any entry-point cookbook or bootstrap docs affected by the change

### 2. Reusable activation surfaces

- [ ] Prompts, templates, or instructions operationalize the refined behavior.
- [ ] Reusable surfaces do not contradict the generic method sequence.
- [ ] Any new reusable surface is generic enough to copy into another repository without hidden repo-specific assumptions.

Typical evidence:

- prompt bundles
- template packs
- instruction files
- bootstrap guidance

### 3. Examples and demonstrations

- [ ] Examples reflect the refined generic guidance instead of inventing a parallel rule set.
- [ ] Example packs remain illustrative rather than silently becoming the only authoritative explanation.
- [ ] Repo-local control records prove the change in use without substituting for the generic method docs.

Typical evidence:

- `examples/initiative-examples/`
- repo-local exec-ctrl records in `docs/exec_ctrl/`

### 4. Closure and deferrals

- [ ] The audit log records what was reviewed and whether any gaps remain.
- [ ] The decision log captures material sequencing, scope, or deferral choices.
- [ ] The validation evidence in the control record points to the changed generic, reusable, and proof surfaces.
- [ ] Any remaining follow-on work is explicit instead of implied complete.

## Should-pass checklist

- [ ] The refined method is easier for a future agent to invoke than before the change.
- [ ] The changed surfaces are still concise enough to scan quickly.
- [ ] The refinement does not widen into unrelated cleanup outside the chosen method delta.

## Common failure patterns

- the repo-local initiative records are stronger than the generic docs
- the prompts or templates imply a different workflow than the method guide
- the README routes users differently than the self-hosting guide
- examples demonstrate a pattern that the generic method never defines
- the change closes with a narrative summary but no explicit evidence across surfaces

## Recommended audit outcome cues

- use `pass` when the must-pass items are satisfied and only minor follow-on work remains
- use `pass_with_gaps` when the refinement can continue but important coherence issues remain open
- use `fail` when the changed surfaces materially contradict each other or closure is being claimed without evidence

This checklist is intentionally narrow.

It is for self-hosting and method-evolution coherence, not for every general exec-ctrl initiative.