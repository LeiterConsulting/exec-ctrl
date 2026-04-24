# Exec-Ctrl Self-Hosting And Method Evolution

## Purpose

This guide defines how exec-ctrl can govern its own improvement work.

Use it when the target repository is not only implementing product features, but is itself defining a method, governance model, template library, prompt pack, or instruction surface.

## Default rule

Treat self-hosting work as initiative mode unless the request is to redesign the whole repository execution system.

Most method changes are bounded:

- add or refine a guide
- clarify authority rules
- add templates or prompt bundles
- improve example packs
- tighten the relationship between documentation and reusable activation surfaces

Use project-pack mode only when the method repository itself needs whole-repository execution control across the full product surface.

If the distinction between one bounded method slice and a whole-system redesign is unclear, use [EXEC_CTRL_BOUNDED_VS_WHOLE_SYSTEM_SCORING_RUBRIC.md](EXEC_CTRL_BOUNDED_VS_WHOLE_SYSTEM_SCORING_RUBRIC.md).

If the workspace-guidance prompt pack is installed, `.github/prompts/exec-ctrl-rubric-review.prompt.md` can run that scoring step as a one-command review.

## What counts as the governed product

In self-hosting work, the governed product is usually a combination of:

- method docs
- templates
- prompts and instructions
- example packs
- bootstrap or onboarding guidance
- repo-local control records that demonstrate the method in use

Do not reduce the effort to repo-local control records alone.

Those records are evidence of the method at work, but they are not the only teaching surface.

## Core self-hosting rule

Update the generic method first.

Then update the reusable operational surfaces.

Then update the repo-local control records so they reflect the finished method change accurately.

That ordering matters because:

- generic docs define the norm
- prompts, templates, and examples operationalize the norm
- repo-local records prove the norm was used in one bounded case


For recurring bounded refinement inside the `exec-ctrl` repo itself, use [EXEC_CTRL_AGENT_ASSESSMENT_LOOP.md](EXEC_CTRL_AGENT_ASSESSMENT_LOOP.md) to inspect planning, choose the next slice, and activate control before substantive edits begin.

For recurring ambiguous self-hosting refinements, use [EXEC_CTRL_METHOD_REPO_REFINEMENT_SCORECARDS.md](EXEC_CTRL_METHOD_REPO_REFINEMENT_SCORECARDS.md) to calibrate the rubric outcome against worked examples.

## Recommended workflow

### 1. Baseline the gap

Audit the difference between:

- what the method claims to support
- what the repo actually demonstrates
- what reusable prompts, templates, and examples make easy to do

Look for mismatches such as:

- the repo demonstrates a pattern but never teaches it generically
- the docs teach a pattern but no prompt or template makes it easy to invoke
- examples imply behaviors that the method docs never define

### 2. Activate a bounded initiative

Create the initiative control record, audit log, and decision log before substantive edits.

Typical scope language:

- improve self-hosting clarity for bounded method evolution
- add a reusable activation surface for method-improvement work
- align prompts, examples, templates, and method docs around one authority model

### 3. Define the method delta explicitly

Before editing, define:

- what part of the method is being improved
- what remains unchanged
- which surfaces are normative versus illustrative
- what evidence will prove the improvement is real

Useful must-pass criteria often include:

- a generic guide exists
- at least one reusable activation surface exists
- entry docs route users to the new pattern
- examples or templates do not contradict the updated method

### 4. Build from generic to specific

Recommended order:

1. update the generic method guide
2. update entry docs that route users into the correct path
3. update prompts, templates, and examples
4. update repo-local self-governing records

This prevents repo-local evidence from becoming the only place the refined behavior is actually visible.

### 5. Validate coherence across surfaces

Use [EXEC_CTRL_SELF_HOSTING_COHERENCE_CHECKLIST.md](EXEC_CTRL_SELF_HOSTING_COHERENCE_CHECKLIST.md) as the default validation aid for this step.

Use [EXEC_CTRL_SELF_HOSTING_COHERENCE_FAILURE_CALIBRATION.md](EXEC_CTRL_SELF_HOSTING_COHERENCE_FAILURE_CALIBRATION.md) when reviewers need examples of the failure patterns that usually drive `pass_with_gaps` versus `fail` outcomes.

If the workspace-guidance prompt pack is installed, `.github/prompts/exec-ctrl-checklist-review.prompt.md` can run that review as a one-command workflow.

Check that:

- the README and method docs point to the same workflow
- prompts do not contradict the docs
- examples reflect the generic guidance rather than replacing it
- the self-governing records match the final method state

### 6. Close with explicit follow-on work

If further automation, examples, or task-shape bundles would help later, record them explicitly.

For repo-level method planning that is not yet active work, place those items in [planning/FUTURE_ENHANCEMENTS.md](planning/FUTURE_ENHANCEMENTS.md) rather than mixing them into `docs/exec_ctrl/` records.

Do not imply that the method is final just because one bounded refinement closed successfully.

## Typical self-hosting workstreams

### Method guidance refinement

Used for:

- new guides
- authority-order clarifications
- lifecycle or evidence rule clarifications

### Reusable activation surfaces

Used for:

- new prompt bundles
- template improvements
- instruction or bootstrap refinements

### Examples and demonstrations

Used for:

- generic example packs
- self-governing initiative records
- updated case patterns that show the refined method in use

## Failure modes to avoid

- treating repo-local initiative records as the entire self-hosting story
- changing prompts or templates without updating the generic method docs
- changing docs without updating reusable activation surfaces
- over-automating the method before the repeated behavior is actually clear
- using method evolution as cover for broad unrelated repo cleanup

## Good prompts for this pattern

- `Use exec-ctrl to improve exec-ctrl itself so self-hosting is a first-class pattern.`
- `Govern this prompt-library refinement under exec-ctrl and keep the generic method ahead of the local example records.`
- `Use exec-ctrl to tighten the relationship between this governance repo's docs, templates, and prompt bundles.`
- `Continue refining this repo. Inspect the planning area, choose one bounded slice, and keep the control records current while you implement it.`

## Suggested future extensions

Track self-hosting and method-evolution follow-on ideas in [planning/FUTURE_ENHANCEMENTS.md](planning/FUTURE_ENHANCEMENTS.md).

When the planning backlog is exhausted, treat future self-hosting work as open-ended field-use follow-on work rather than as a standing list of defined candidates.

When the defined planning backlog is exhausted and broader field use is the next question, use [EXEC_CTRL_METHOD_REPO_TEST_READY_REVIEW.md](EXEC_CTRL_METHOD_REPO_TEST_READY_REVIEW.md) as the lightweight readiness checkpoint.

This guide keeps self-hosting grounded in the same evidence, authority, and bounded-scope rules as any other exec-ctrl initiative.