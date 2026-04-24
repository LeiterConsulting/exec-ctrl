# Exec-Ctrl Bounded-vs-Whole-System Scoring Rubric

## Purpose

Use this rubric when it is not obvious whether a requested change should be governed as:

- one bounded initiative under initiative mode
- or a whole-system or whole-repository control effort that needs a broader execution layer

This rubric does not replace user direction.

It helps structure the decision when the request sits between those two shapes.

For worked examples, use [EXEC_CTRL_REPO_LINK_SCORECARDS.md](EXEC_CTRL_REPO_LINK_SCORECARDS.md) for repo-link requests and [EXEC_CTRL_METHOD_REPO_REFINEMENT_SCORECARDS.md](EXEC_CTRL_METHOD_REPO_REFINEMENT_SCORECARDS.md) for self-hosting method-repo refinements.

If the workspace-guidance prompt pack is installed, you can run the scoring step as a one-command workflow with `.github/prompts/exec-ctrl-rubric-review.prompt.md`.

## When to use it

Use the rubric when:

- the request touches multiple method or product surfaces
- the request sounds larger than one narrow slice but smaller than a total redesign
- the repo already has an execution model, but the requested change might alter how most future work is governed
- initiative mode and whole-system control both look initially plausible

If the request is already clearly bounded or clearly whole-system, do not force a scoring pass.

## Hard overrides

Choose the whole-system path without scoring if any of these are explicitly true:

- the user asks to redesign the whole repository execution model
- the change replaces the authority order, status vocabulary, phase model, or evidence model for most future work
- the change requires repo-wide control docs for the full product rather than one bounded slice

Choose initiative mode without scoring if any of these are explicitly true:

- the user calls out one bounded slice and explicit non-goals
- the request targets one guide, one prompt family, one template family, one subsystem, or one closeout slice
- the current repository execution model stays intact and only one bounded improvement is needed

## Scoring method

Score each category from `0` to `2`.

- `0` means the signal is clearly bounded
- `1` means the signal is mixed or unclear
- `2` means the signal points strongly to a whole-system effort

Add the scores to get the total whole-system score.

## Scoring categories

### 1. Surface breadth

- `0`: one guide, one prompt family, one template family, one example pack, or one subsystem slice
- `1`: several adjacent surfaces change together, but the rest of the repo remains stable
- `2`: many core surfaces across the repo change together

### 2. Authority impact

- `0`: authority order, status vocabulary, phase model, and evidence rules stay intact
- `1`: the change clarifies or tightens those rules in one bounded area
- `2`: the change redefines those rules for most future work

### 3. Dependency spread

- `0`: only narrow dependent surfaces need updating
- `1`: several prompts, templates, docs, or examples need coordinated updates
- `2`: the change cascades across most execution surfaces in the repo

### 4. Validation breadth

- `0`: narrow validation or one focused coherence pass is enough
- `1`: multiple adjacent surfaces need validation together
- `2`: broad repo-wide validation is required before the claim is credible

### 5. Reuse scope

- `0`: the outcome primarily improves one recurring task shape or one bounded capability
- `1`: the outcome will influence several workflows
- `2`: the outcome becomes baseline guidance for most future work in the repo

### 6. User wording and expected outcome

- `0`: the user asks for one slice, one refinement, one task shape, or explicit non-goals
- `1`: the wording is broad but still plausibly bounded
- `2`: the user asks for redesign of the whole repo, whole system, or default control model

## Interpreting the total

- `0-4`: treat the work as a bounded initiative
- `5-7`: still default to initiative mode, but record explicit boundaries, non-goals, and watchpoints in the decision log
- `8-12`: treat the work as a whole-system effort unless the user explicitly constrains it to a bounded slice and the authority model remains intact

If the score lands in the middle band, default to initiative mode unless:

- the user explicitly wants whole-system governance
- or the change rewrites the core authority, phase, or evidence model for the repository

## Required recordkeeping

When you use this rubric, record:

- the total score
- the categories that drove the outcome
- the final chosen control path
- any explicit non-goals or escalation watchpoints

Typical places to record this:

- decision log
- control record current status
- bootstrap notes when the repo is being activated from a link

## Method-repo examples

### Clearly bounded

Example:

- add a self-hosting coherence checklist and wire it into the method-evolution prompt

Typical score:

- surface breadth `0`
- authority impact `0`
- dependency spread `1`
- validation breadth `0`
- reuse scope `1`
- user wording `0`

Total:

- `2`

Recommended path:

- initiative mode

### Borderline but still bounded

Example:

- tighten mode-selection guidance across the self-hosting guide, bootstrap guide, prompts, and workspace instructions without changing the core authority model

Typical score:

- surface breadth `1`
- authority impact `1`
- dependency spread `1`
- validation breadth `1`
- reuse scope `2`
- user wording `1`

Total:

- `7`

Recommended path:

- initiative mode with explicit boundaries and decision-log watchpoints

### Whole-system

Example:

- redesign exec-ctrl so the default numbering model, authority order, status vocabulary, and phase advancement rules all change across the repo

Typical score:

- surface breadth `2`
- authority impact `2`
- dependency spread `2`
- validation breadth `2`
- reuse scope `2`
- user wording `2`

Total:

- `12`

Recommended path:

- whole-system control path

## Failure modes to avoid

- using the rubric to override explicit user direction
- treating the score as more important than authority-model impact
- scoring a request as whole-system just because it is important
- skipping the decision-log record after using the rubric
- widening a bounded initiative because several surfaces need coordinated updates

This rubric is intentionally conservative.

When in doubt, stay bounded and document the boundary explicitly unless the request or the authority-model impact truly requires a whole-system path.