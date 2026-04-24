# Exec-Ctrl Method Repo Test-Ready Review

## Purpose

Use this review when the `exec-ctrl` repo has completed its currently defined backlog and you need a lightweight way to judge whether the method is ready for broader field testing.

This is a readiness review, not a second operational control system.

## When To Run It

Run this review when:

- the defined planning backlog is exhausted
- the repo has completed several self-hosting refinements
- you want an explicit checkpoint before relying on the repo for wider real-world trials

Do not use this review as a gate for every small method change.

## Review Questions

### 1. Core method clarity

- does the README route users into the right starting surfaces quickly
- do the core method guides explain initiative mode, repo-link bootstrap, self-hosting, and planning boundaries clearly
- does the live `.github/` guidance match the generic docs

### 2. Reusable activation coverage

- are the main recurring prompt shapes installed and discoverable
- can a future agent identify when to use bootstrap, rubric review, checklist review, method evolution, next-refinement assessment, audit, release closeout, and migration bootstrap
- does the workspace-guidance template pack still align with the live repo guidance

### 3. Example and calibration coverage

- do the examples cover more than one kind of bounded initiative
- are there scorecards or calibration surfaces for ambiguous repo-link and method-repo requests
- is there guidance for interpreting recurring coherence failures

### 4. Evidence honesty

- do the repo-local exec-ctrl records match the current method state
- has promoted planning work stopped looking untouched
- are there explicit follow-on gaps rather than hidden assumptions that the method is final

## Suggested Verdicts

- `ready_for_field_test`: the repo teaches one coherent workflow, recurring prompt shapes are discoverable, calibration surfaces exist, and remaining future work is open-ended rather than missing from the method
- `ready_with_gaps`: the repo is directionally ready, but one or two explicit guidance or calibration surfaces still need tightening before broader use
- `not_ready`: major routing, calibration, or evidence gaps still make broader use likely to produce confused agent behavior

## Minimum Evidence For `ready_for_field_test`

- core method docs and live workspace guidance align
- the prompt pack covers the main recurring task shapes
- multiple generic example packs exist for materially different initiative shapes
- scorecards or calibration surfaces exist for ambiguous control-path decisions and coherence review outcomes
- the planning surface either has no defined backlog items or records only clearly open-ended future ideas

## Non-Goals

- replace initiative-level validation with one repo-level status claim
- imply that no further refinements will ever be useful
- create a permanent release gate process for every documentation change

## Recommended Output

Record:

- the verdict
- the evidence reviewed
- the remaining explicit gaps, if any
- whether the repo is ready for broader field testing now or should wait for one more bounded slice