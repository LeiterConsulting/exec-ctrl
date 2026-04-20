# exec-ctrl

`exec-ctrl` is a reusable execution-control pattern for turning product-definition docs into an authoritative implementation system.

It is intended for projects where:
- the direction is mostly known
- phases should be explicit
- the next move should follow documented completion status
- testing and evidence should decide whether a phase is actually done
- the agent or team must keep the docs current while implementation evolves

## What this repo contains

- a generic method guide in [docs/EXEC_CTRL_METHOD.md](docs/EXEC_CTRL_METHOD.md)
- a starter template pack in [templates/project-pack](templates/project-pack)
- numbered template docs for the authoritative exec-ctrl layer:
  - `13_EXEC_CTRL_OVERVIEW.md`
  - `14_EXEC_CTRL_TARGET_PRODUCT.md`
  - `15_EXEC_CTRL_PAGES_AND_FUNCTIONS.md`
  - `16_EXEC_CTRL_PHASE_PLAN.md`
  - `17_EXEC_CTRL_TEST_AND_SUCCESS.md`
  - `18_EXEC_CTRL_STATUS.md`

## Intended usage

This pattern assumes the project already has an earlier concept or product pack.

Typical ordering:

1. product and architecture docs establish the concept
2. exec-ctrl docs become the authoritative execution layer
3. implementation work updates the status, phase, and evidence docs in the same cycle as code changes

## Core rule

The current phase is the earliest phase that is not `complete`.

That prevents work from drifting into later features while earlier gates remain unresolved.

## Quick start

1. Copy the files from [templates/project-pack](templates/project-pack) into the target project's docs folder.
2. Keep the numbering so the exec-ctrl layer sits after the original concept pack.
3. Fill in the target product, page inventory, phase plan, tests, and live status for the project.
4. During implementation, update the status and evidence docs whenever reality changes.

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