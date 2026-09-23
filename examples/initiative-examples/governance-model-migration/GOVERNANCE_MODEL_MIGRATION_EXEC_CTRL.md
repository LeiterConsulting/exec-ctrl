> **v1 reference.** For new work use the [v2 activation contract](../../../START_HERE.md).
> Apply the workflow below only when explicitly maintaining a v1 adoption.

# Governance Model Migration exec-ctrl

## Control Summary

| Field | Value |
| --- | --- |
| Initiative | `Governance Model Migration` |
| Abbrev | `governance-model-migration` |
| Control system | `exec-ctrl` |
| Overall state | `complete` |
| Current phase | `Phase 5 Close complete` |
| Started | `YYYY-MM-DD` |
| Governs | bounded migration from one governance or status-tracking surface into repo-local exec-ctrl without widening into a total system redesign |
| Primary inputs | prior governance surface, target exec-ctrl surface, migration constraints, and generic method docs |

## Objective

Move one bounded governance workflow into exec-ctrl while keeping sequencing, rollback posture, and authority boundaries explicit.

## Scope In

- migration planning and baseline evidence
- bounded transfer of one governance workflow into exec-ctrl surfaces
- proof artifacts that show the migration slice in use

## Scope Out

- redesign of the whole repository execution model
- simultaneous migration of unrelated governance surfaces
- automation beyond what the bounded migration requires

## Deliverables

1. a bounded governance-model migration plan
2. evidence of the migrated target state
3. synchronized proof artifacts

## Must-Pass Success Criteria

1. the migration boundary is explicit
2. sequencing and fallback posture are recorded clearly
3. the migration remains bounded rather than turning into whole-system redesign

## Current Status

What is complete now:

- the example shows how to govern a migration-shaped self-hosting slice under initiative mode
- sequencing and fallback posture remain explicit rather than implied

What remains open:

- future migrations can reuse the pattern, but none are required for this example to close