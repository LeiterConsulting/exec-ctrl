# Exec-Ctrl Future Enhancements

This document collects non-operational future enhancements for the `exec-ctrl` method repo.

It is a planning surface, not an execution-control surface.

Use it to keep likely next improvements visible without making them look active, validated, or complete.

## Planning states

- `near_term`: worth considering in the next bounded refinement or two
- `candidate`: useful, but not yet the best next slice
- `later`: directional idea that should wait for more repeated use

## Promotion rule

When one of these items becomes active work:

1. create the initiative control record, audit log, and decision log in `docs/exec_ctrl/`
2. treat this planning doc as one input to the refinement
3. remove or update the planning entry so it no longer looks unstarted by accident

## Near-term planning themes

### 1. Bootstrap hardening

| ID | State | Enhancement | Why it matters | Suggested next slice |
| --- | --- | --- | --- | --- |
| `FE-001` | `near_term` | add a validation checklist for copied workspace-guidance templates | copied prompt and instruction packs can drift when placeholders are left behind | create a bounded guide or checklist that validates placeholders, target-repo substitutions, and repo-specific build/test guidance |
| `FE-002` | `candidate` | add more task-shape prompt bundles for data migrations, release readiness, and incident remediation | repo-link bootstrap becomes more reusable when recurring task shapes already have prompt surfaces | add one prompt at a time under initiative mode and link it from the workspace-guidance README |
| `FE-003` | `candidate` | add example scorecards for recurring ambiguous repo-link requests | rubric outcomes become easier to calibrate when common mixed-signal requests have comparison examples | create a small example pack or annex with scored request patterns |

### 2. Self-hosting calibration

| ID | State | Enhancement | Why it matters | Suggested next slice |
| --- | --- | --- | --- | --- |
| `FE-004` | `candidate` | add more generic examples for prompt-library evolution, template-library hardening, and governance-model migrations | self-hosting is stronger when the repo demonstrates more than one method-evolution shape | add one bounded example pack at a time and keep the generic guide ahead of the examples |
| `FE-005` | `candidate` | add example review cases for recurring self-hosting coherence failures | checklist outcomes become easier to interpret when reviewers can compare common failure patterns | add a compact calibration annex tied to the coherence checklist |
| `FE-006` | `candidate` | add example scorecards for ambiguous method-repo refinements | method-evolution mode selection becomes easier to compare over time | add a scorecard appendix or example doc that pairs the rubric with self-hosting scenarios |

### 3. Agent-assisted method evolution

| ID | State | Enhancement | Why it matters | Suggested next slice |
| --- | --- | --- | --- | --- |
| `FE-007` | `near_term` | define an agent-assisted assessment loop for iterative `exec-ctrl` improvement | the repo is close to the point where agents can repeatedly inspect gaps, choose bounded refinements, and improve the method without inventing the workflow each time | add a guide or prompt that tells an agent how to inspect the planning area, choose one bounded slice, create control records, and close with explicit follow-on work |
| `FE-008` | `later` | define a lightweight test-ready review for the method repo itself | repeated self-hosting cycles need a clear checkpoint for when the repo is ready for broader field testing | add a bounded review guide only after several real repo-link trials produce repeatable evaluation criteria |

## Planning guidance for agents

An agent using this planning area should:

1. treat these entries as backlog signals rather than active work
2. prefer one bounded refinement at a time
3. choose the next slice based on repeated need, not novelty
4. promote the chosen item into `docs/exec_ctrl/` before substantive edits
5. close the initiative with explicit evidence and update this planning doc afterward

## Current recommendation

The repo appears ready for real-world testing now.

The most defensible next bounded refinement, if one is wanted before more field use, is `FE-001` because copied workspace-guidance placeholders are a practical failure mode during repo-link bootstrap.