> **v1 reference.** For new work use the [v2 activation contract](../../START_HERE.md).
> Apply the workflow below only when explicitly maintaining a v1 adoption.

# Exec-Ctrl Test And Success

## Test policy

A phase cannot move to `complete` without evidence.

Accepted evidence types:
- automated test output
- narrow compile, syntax, or type validation when appropriate
- live API verification
- live browser or operator verification
- explicit blocker evidence when completion is not yet possible

## System-level success definition

Define the operator-visible end state for the product.

Use numbered outcomes if that makes success easier to verify.

## Phase test matrix

For each phase, define:
- named tests
- what counts as passing evidence
- what evidence already exists

Recommended pattern:

### Phase 0 tests

- `P0-T1`: first foundational test
- `P0-T2`: second foundational test

Current evidence:
- none yet

### Phase 1 tests

- `P1-T1`: first control-plane test
- `P1-T2`: second control-plane test

Current evidence:
- none yet

Repeat as needed for each phase.

## Evidence already established in this workspace

Use this section to record the live facts that should not be rediscovered repeatedly.

## Known evidence gap

Record the most important evidence gap that still keeps the active phase open.