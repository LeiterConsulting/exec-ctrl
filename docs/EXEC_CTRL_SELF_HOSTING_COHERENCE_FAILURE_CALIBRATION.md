> **v1 reference.** For new work use the [v2 activation contract](../START_HERE.md).
> Apply the workflow below only when explicitly maintaining a v1 adoption.

# Exec-Ctrl Self-Hosting Coherence Failure Calibration

## Purpose

Use this guide with [EXEC_CTRL_SELF_HOSTING_COHERENCE_CHECKLIST.md](EXEC_CTRL_SELF_HOSTING_COHERENCE_CHECKLIST.md) when a reviewer needs calibration for recurring self-hosting failure patterns.

It does not replace the checklist.

It helps reviewers decide whether the right verdict is `pass`, `pass_with_gaps`, or `fail` when the changed surfaces do not align cleanly.

## Case 1. README Routes Differently Than The Prompt Pack

Observed pattern:

- the README tells future users to start with one workflow
- the installed prompt or instruction surface points to a different starting point

Typical checklist sections:

- Generic teaching surfaces
- Reusable activation surfaces

Recommended verdict:

- `pass_with_gaps` if the contradiction is routing-only and the underlying authority model still matches
- `fail` if the routing contradiction would cause future sessions to activate the wrong control path repeatedly

Required fix:

- make the README and reusable activation surfaces point to the same entry path

## Case 2. Repo-Local Proof Artifacts Are Stronger Than The Generic Docs

Observed pattern:

- the control record, audit log, or decision log explains the refined behavior clearly
- the generic method docs still leave the behavior implied or unstated

Typical checklist sections:

- Generic teaching surfaces
- Examples and demonstrations

Recommended verdict:

- `fail`

Why:

- the repo-local proof artifacts are demonstrating a rule that the generic method still does not teach

Required fix:

- update the generic guide first, then reconcile prompts or examples, then resynchronize the proof artifacts

## Case 3. Examples Invent A Parallel Workflow

Observed pattern:

- new example packs use different phase names, status language, or authority assumptions than the generic method docs

Typical checklist sections:

- Examples and demonstrations
- Closure and deferrals

Recommended verdict:

- `fail`

Required fix:

- rewrite the example pack so it illustrates the generic method instead of becoming a competing explanation

## Case 4. Prompt Surface Lags One Small Generic Clarification

Observed pattern:

- the generic guide has been updated correctly
- one prompt or instruction file still uses older wording, but the implied workflow is materially the same

Typical checklist sections:

- Reusable activation surfaces

Recommended verdict:

- `pass_with_gaps`

Required fix:

- update the lagging prompt or instruction surface before closure

## Case 5. Planning Still Looks Active After Promotion

Observed pattern:

- the changed surfaces implement a planned item
- the planning doc still lists the item as untouched candidate work

Typical checklist sections:

- Closure and deferrals

Recommended verdict:

- `pass_with_gaps`

Why:

- the implementation may be real, but the repo still teaches the wrong backlog state

Required fix:

- update the planning surface so promoted work no longer looks open

## Case 6. Test-Ready Claims Outrun Evidence

Observed pattern:

- the repo claims it is ready for broader field use
- evidence still comes from only one or two narrow self-hosting slices

Typical checklist sections:

- Closure and deferrals
- Should-pass checklist

Recommended verdict:

- `pass_with_gaps` when the repo is directionally ready but missing one explicit review surface or broader trial evidence
- `fail` when broad readiness is claimed without any credible cross-surface review

Required fix:

- add or run the lightweight test-ready review and record the remaining evidence gaps explicitly

## Practical Review Rule

Choose `fail` when the changed surfaces would teach future agents the wrong workflow.

Choose `pass_with_gaps` when the workflow is still recognizable and recoverable, but one or more calibration or routing surfaces must be corrected before closure.