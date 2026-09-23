> **v1 reference.** For new work use the [v2 activation contract](../../../START_HERE.md).
> Apply the workflow below only when explicitly maintaining a v1 adoption.

# Method Evolution exec-ctrl

## Control Summary

| Field | Value |
| --- | --- |
| Initiative | `Method Evolution` |
| Abbrev | `method-evolution` |
| Control system | `exec-ctrl` |
| Overall state | `complete` |
| Current phase | `Phase 5 Close complete` |
| Started | `YYYY-MM-DD` |
| Governs | bounded improvement of a method, template library, prompt pack, or governance repository using the same control system it defines |
| Primary inputs | current method docs, templates, prompts, examples, and repo-local control artifacts |

## Objective

Improve a method repository so the generic guidance, reusable activation surfaces, and local demonstration records all describe the same workflow clearly.

## Requirement Definitions

| ID | Requirement | Definition | Success Signal |
| --- | --- | --- | --- |
| `ME-1` | Generic guidance clarity | the refined behavior should be taught in a generic method surface, not only implied by local records | a generic guide or updated method doc makes the change explicit |
| `ME-2` | Operational reuse | the refined behavior should be easy to invoke again | at least one prompt, template, or instruction surface operationalizes the change |
| `ME-3` | Cross-surface coherence | docs, prompts, templates, examples, and local control records should agree | the changed surfaces reinforce one authority model and one bounded workflow |

## Scope In

- method-guide refinement
- prompt, template, or instruction changes that operationalize the method delta
- example and proof-artifact alignment

## Scope Out

- whole-repository redesign of the entire method system
- unrelated cleanup in other parts of the repo
- runtime automation before the behavior is stable enough to deserve it

## Deliverables

1. updated generic method guidance
2. reusable activation surface for the refined behavior
3. aligned example or proof artifacts
4. explicit closeout records

## Must-Pass Success Criteria

1. the method change is taught generically rather than only demonstrated locally
2. at least one reusable activation surface exists
3. the changed prompts, templates, examples, and local records do not contradict the new guidance
4. follow-on work is explicit rather than hidden inside completion language

## Should-Pass Success Criteria

1. the method change remains small and bounded
2. the updated repo is easier for future agents to use than before the refinement

## Non-Goals

- broad redesign of the entire system
- product-specific case study writing
- automation that outruns the clarity of the method itself

## Completion Conditions

- all must-pass criteria are satisfied
- changed surfaces are coherent
- deferred follow-on work is explicit

## Workstreams

| Workstream | Purpose | Status | Evidence |
| --- | --- | --- | --- |
| `WS1` | generic method update | `complete` | refined method docs |
| `WS2` | reusable activation surface | `complete` | prompt or template changes |
| `WS3` | example and proof alignment | `complete` | example pack and control records |

## Current Status

What is complete now:

- the generic method change is documented
- reusable activation surfaces exist
- examples and proof artifacts were aligned with the method change

What remains open:

- future refinements can build on the updated method, but they are not required for this initiative to close