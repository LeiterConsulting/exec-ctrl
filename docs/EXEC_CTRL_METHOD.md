# Exec-Ctrl Method

## Definition

Exec-ctrl means execution control.

It is a documentation-driven implementation discipline where:
- the product direction is defined in advance
- the current phase is explicit
- each phase has an exit gate
- tests and evidence determine completion
- the next phase is chosen by status, not by preference
- the docs are updated as implementation changes

## Why use it

Exec-ctrl is useful when a project is larger than a quick prototype but still evolving during implementation.

It prevents several common failures:
- skipping unresolved dependencies
- claiming progress without evidence
- building later features while earlier gates are still broken
- losing track of what is authoritative
- letting docs drift away from real implementation status

## Minimum document set

The minimum authoritative layer is six docs:

1. overview
2. target product
3. pages and functions
4. phase plan
5. test and success
6. status

## Authority model

When the project uses exec-ctrl, the authority usually flows like this:

1. active user direction
2. live status doc
3. phase plan doc
4. test and success doc
5. target product doc
6. pages and functions doc
7. earlier concept pack

## Required status vocabulary

Use a small closed set:

- `not_started`
- `in_progress`
- `blocked`
- `complete`
- `deferred`

Do not create ad hoc status words unless the project has a very strong reason.

## Phase advancement rule

The active phase is the earliest phase that is not `complete`.

Implications:
- later phases can be designed early
- later phases should not be declared complete before dependent earlier phases
- a blocked phase stays active until the blocker is removed or direction changes

## Evidence rule

A phase is not complete because the team believes it is complete.

A phase is complete when evidence exists.

Accepted evidence may include:
- automated tests
- narrow compile or syntax validation
- live API verification
- live browser verification
- explicit blocker evidence when completion is not yet possible

## Update rule

Implementation and exec-ctrl docs must move together.

At minimum:
- update the status doc when real completion status changes
- update the phase plan when a blocker or exit gate changes
- update the test doc when new evidence appears or a new test becomes required
- update the pages/functions doc when the operator surface or capability map changes

## Recommended workflow

1. create the concept pack
2. add the exec-ctrl layer
3. identify the active phase
4. implement only the next meaningful slice that advances the active phase
5. validate with evidence
6. update the exec-ctrl docs
7. move to the next phase only when the gate is actually met

## Practical guidance

- keep the status doc brutally honest
- do not hide blockers inside progress language
- do not mark later phases complete while the active gate is still open
- make operator-visible surfaces map cleanly to backend functions and tests
- prefer concrete evidence over broad narrative summaries

## Template placement

The template pack keeps numbering `13` through `18` so it can sit after a typical `01` through `12` concept pack.

If a project uses a different numbering model, adapt the numbers while preserving the six-document structure.