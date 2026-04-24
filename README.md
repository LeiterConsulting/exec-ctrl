# exec-ctrl

`exec-ctrl` is a reusable execution-control pattern for turning product-definition docs into an authoritative implementation system.

It is intended for projects where:
- the direction is mostly known
- phases should be explicit
- the next move should follow documented completion status
- testing and evidence should decide whether a phase is actually done
- the agent or team must keep the docs current while implementation evolves

It can be applied in two ways:
- as a full project execution layer on top of an existing concept pack
- as a bounded initiative control pack for a specific slice of work inside an active repository

## What this repo contains

- a generic method guide in [docs/EXEC_CTRL_METHOD.md](docs/EXEC_CTRL_METHOD.md)
- a bounded-work guide in [docs/EXEC_CTRL_INITIATIVE_MODE.md](docs/EXEC_CTRL_INITIATIVE_MODE.md)
- an agent prompt cookbook in [docs/EXEC_CTRL_AGENT_PROMPT_COOKBOOK.md](docs/EXEC_CTRL_AGENT_PROMPT_COOKBOOK.md)
- a repo-link bootstrap guide in [docs/EXEC_CTRL_REPO_LINK_BOOTSTRAP.md](docs/EXEC_CTRL_REPO_LINK_BOOTSTRAP.md)
- a self-hosting and method-evolution guide in [docs/EXEC_CTRL_SELF_HOSTING_AND_METHOD_EVOLUTION.md](docs/EXEC_CTRL_SELF_HOSTING_AND_METHOD_EVOLUTION.md)
- a self-hosting coherence checklist in [docs/EXEC_CTRL_SELF_HOSTING_COHERENCE_CHECKLIST.md](docs/EXEC_CTRL_SELF_HOSTING_COHERENCE_CHECKLIST.md)
- a bounded-vs-whole-system scoring rubric in [docs/EXEC_CTRL_BOUNDED_VS_WHOLE_SYSTEM_SCORING_RUBRIC.md](docs/EXEC_CTRL_BOUNDED_VS_WHOLE_SYSTEM_SCORING_RUBRIC.md)
- a non-operational planning area for future method enhancements in [docs/planning](docs/planning)
- a starter template pack in [templates/project-pack](templates/project-pack)
- a bounded-work starter pack in [templates/initiative-pack](templates/initiative-pack)
- a workspace-guidance template pack in [templates/workspace-guidance](templates/workspace-guidance)
- generic example initiative packs in [examples/initiative-examples](examples/initiative-examples)
- numbered template docs for the authoritative exec-ctrl layer:
  - `13_EXEC_CTRL_OVERVIEW.md`
  - `14_EXEC_CTRL_TARGET_PRODUCT.md`
  - `15_EXEC_CTRL_PAGES_AND_FUNCTIONS.md`
  - `16_EXEC_CTRL_PHASE_PLAN.md`
  - `17_EXEC_CTRL_TEST_AND_SUCCESS.md`
  - `18_EXEC_CTRL_STATUS.md`

## Intended usage

This repo supports both a full-project mode and a bounded-initiative mode.

Use full-project mode when the repository needs an authoritative execution layer for the whole product.

Use bounded-initiative mode when the user says something like:

- "use the exec-ctrl repo to do the following work"
- "govern this refactor under exec-ctrl"
- "run this audit/remediation effort under exec-ctrl"
- "define the work, success criteria, and evidence model before implementation"

Typical ordering:

1. product and architecture docs establish the concept
2. exec-ctrl docs become the authoritative execution layer
3. implementation work updates the status, phase, and evidence docs in the same cycle as code changes

For bounded initiatives, the ordering is lighter:

1. translate the request into a scoped initiative objective
2. activate a control record, audit log, and decision log
3. define success criteria and non-goals before implementation
4. execute and validate with evidence
5. close the initiative with explicit completion and deferrals

## Operating modes

### Project-pack mode

Use [templates/project-pack](templates/project-pack) when:

- the repository needs a full execution layer
- the work spans the whole product or delivery ladder
- the project already has concept, architecture, or product-definition docs

### Initiative-pack mode

Use [templates/initiative-pack](templates/initiative-pack) when:

- the work is a bounded slice inside an active codebase
- the user is asking for one initiative, audit, refactor, remediation effort, or subsystem slice
- the team needs explicit scope, success criteria, audit checkpoints, and decisions without rewriting the whole project pack
- the agent needs a default governance pattern for "do this work under exec-ctrl"

If the user request is bounded and does not require a whole-product execution layer, initiative-pack mode should be the default.

## Shared status vocabulary

Both operating modes should use the same core execution states unless a repository has a very strong reason not to:

- `not_started`
- `in_progress`
- `blocked`
- `complete`
- `deferred`

Phase names should carry the lifecycle nuance. Status words should stay compact and consistent.

## Core rule

The current phase is the earliest phase that is not `complete`.

That prevents work from drifting into later features while earlier gates remain unresolved.

For initiative-pack mode, the same discipline applies at the initiative level: work should not be declared closed until must-pass criteria are backed by evidence and documented in the control artifacts.

## Repo-link bootstrap

If the user brings a task idea plus a repository link and expects the agent to stand up exec-ctrl in the target repo, use [docs/EXEC_CTRL_REPO_LINK_BOOTSTRAP.md](docs/EXEC_CTRL_REPO_LINK_BOOTSTRAP.md).

That guide covers:

- mode selection from the request shape
- what control docs to create first
- how to add workspace guidance so later agent sessions stay aligned
- concrete prompt examples and failure modes

## Self-hosting and method evolution

If the work is to improve `exec-ctrl` itself, or to improve another governance, template, prompt, or method repository using the same discipline, use [docs/EXEC_CTRL_SELF_HOSTING_AND_METHOD_EVOLUTION.md](docs/EXEC_CTRL_SELF_HOSTING_AND_METHOD_EVOLUTION.md).

That guide covers:

- when self-hosting should still default to initiative mode
- how to treat docs, prompts, templates, and examples as governed product surfaces
- how to update the generic method first and repo-local evidence second
- how to close recursive method changes without hiding follow-on work

Use [docs/EXEC_CTRL_SELF_HOSTING_COHERENCE_CHECKLIST.md](docs/EXEC_CTRL_SELF_HOSTING_COHERENCE_CHECKLIST.md) during validation when you need to check whether the changed docs, prompts, templates, examples, and proof artifacts still teach one coherent workflow.

If the boundary between one bounded slice and a whole-system redesign is unclear, use [docs/EXEC_CTRL_BOUNDED_VS_WHOLE_SYSTEM_SCORING_RUBRIC.md](docs/EXEC_CTRL_BOUNDED_VS_WHOLE_SYSTEM_SCORING_RUBRIC.md) before choosing the control path.

If you need to capture likely next improvements without making them look active, use the non-operational planning area in [docs/planning](docs/planning). That area is for candidate enhancements and roadmap shaping, while [docs/exec_ctrl](docs/exec_ctrl) remains the operational evidence area for active or completed bounded refinements.

## Quick start

1. If the starting point is a repo link plus a task, follow [docs/EXEC_CTRL_REPO_LINK_BOOTSTRAP.md](docs/EXEC_CTRL_REPO_LINK_BOOTSTRAP.md) first.
2. If the starting point is to improve `exec-ctrl` itself or another method repository, follow [docs/EXEC_CTRL_SELF_HOSTING_AND_METHOD_EVOLUTION.md](docs/EXEC_CTRL_SELF_HOSTING_AND_METHOD_EVOLUTION.md) first.
3. Choose the operating mode.
4. For full-project control, copy the files from [templates/project-pack](templates/project-pack) into the target project's docs folder.
5. Keep the numbering so the exec-ctrl layer sits after the original concept pack.
6. Fill in the target product, page inventory, phase plan, tests, and live status for the project.
7. For bounded initiative control, copy the files from [templates/initiative-pack](templates/initiative-pack) into a folder such as `docs/exec_ctrl/` in the target repository and rename them to match the initiative.
8. If the repository lacks agent guidance, copy the files from [templates/workspace-guidance](templates/workspace-guidance) and customize them for the target repo.
9. During implementation, update the status, audit, and evidence docs whenever reality changes.

If you want a concrete starting point, use one of the generic example packs in [examples/initiative-examples](examples/initiative-examples) and adapt it to the target effort.

## Agent invocation pattern

When a future user says "use the exec-ctrl repo to do the following work: ...", the default agent behavior should be:

1. inspect the request and decide whether it is whole-project or bounded-initiative work
2. prefer initiative-pack mode unless the request clearly needs the full project pack
3. activate the required docs before implementation starts
4. install workspace guidance if the target repo does not already have an equivalent control surface
5. convert the request into explicit objective, scope, deliverables, must-pass criteria, should-pass criteria, and non-goals
6. keep the control docs current while implementation and validation happen
7. close only when evidence exists and any deferrals are recorded explicitly

When the target is the method repository itself, the same rule applies: activate the control docs first, then update the generic method surfaces before treating repo-local control records as the only evidence of change.

## Recommended repository convention

Use the exec-ctrl files as the authoritative execution surface.

When docs disagree, the usual order should be:

1. active user direction
2. `18_EXEC_CTRL_STATUS.md`
3. `16_EXEC_CTRL_PHASE_PLAN.md`
4. `17_EXEC_CTRL_TEST_AND_SUCCESS.md`
5. `14_EXEC_CTRL_TARGET_PRODUCT.md`
6. `15_EXEC_CTRL_PAGES_AND_FUNCTIONS.md`
7. earlier concept docs

## Extracted pattern scope

This repo is the generic pattern only.

It is not tied to one app, one framework, or one runtime. Project-specific examples belong in the target project or in a future examples directory if needed.