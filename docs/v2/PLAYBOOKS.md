# Task playbooks

Choose the row matching the user's outcome, then inspect the actual affected
contracts. These recipes are starting points, not a requirement to load every
module or run every possible check. A record can stay in the response or an
existing issue/PR. Use [the session loop](SESSION_LOOP.md) for continued work.

| Work | Inspect and define | Evidence that advances the task |
| --- | --- | --- |
| Small docs/config correction | Intended text/default, affected links or consumers | Focused diff and relevant syntax/link check; keep the record short |
| Bug fix | Reproduction, entry point, state and caller assumptions | Original failure, supported cause, regression and nearby boundary check |
| Feature | User outcome, affected components, error and denied paths | Acceptance traced to implementation and meaningful contract checks |
| Refactor | Observable behavior and compatibility constraints | Before/after contract coverage and affected consumer checks |
| Auth or tenant boundary | Principal, resource, access decision and side effect | Allowed path, denied path, failed mutation leaves state unchanged |
| Retry/concurrency | Idempotency scope, conflict semantics, atomic commit | Duplicate retries, conflicting writers, partial failure and cleanup |
| Schema migration | Source/target format, ordering, consumers and recovery | Failure at intermediate points, data preservation, rerun and rollout gates |
| Dependency or CI update | Provenance, supported versions, permissions and install behavior | Affected build/tests, current advisory review and artifact boundary |
| Performance | Workload, bottleneck hypothesis, resource and latency budget | Comparable baseline, relevant measurement and correctness under load |
| UI/accessibility | Task flow, input methods, focus, errors and assistive needs | Actual interaction checks; record manual or device-dependent acceptance |
| Security audit | Authorized assets, versions, entry points and exposure | Sanitized finding with reachability, impact, confidence, owner and disposition |
| Release | Source, artifact, target environment and required approvals | Build identity, deployed identity and runtime acceptance as separate gates |
| Team handoff | Canonical issue/PR, owner, dependencies and current status | Concrete draft or verified update; synchronization status explicit |
| Whole-product planning | Requirements, dependencies, lifecycle and exclusions | Bounded roadmap with owners and measurable milestones; no implementation claim |

## Example: a tiny change with a large trust boundary

"Fix the missing tenant check" may change one line. Trace the principal through
the endpoint and storage operation. Check another tenant cannot read or mutate the
resource; check the owner still can. Include retries or background jobs if they use
the same access decision. Link the failure and corrected result to the final inputs.
Diff size alone does not reduce the risk.

## Example: reconcile a function discrepancy

Suppose documentation promises one job per tenant/key, code keys globally, and a
test only checks one tenant. Record the three claims and source locations. Establish
the intended contract from the authorized requirement and consumers. Reproduce the
cross-tenant conflict, correct the implementation, add a failing-before/fixed-after
check, and update the public contract if needed. An assertion that repeats the
implementation would preserve the discrepancy.

Use [CONTRACT_REVIEW.md](../../templates/v2/CONTRACT_REVIEW.md) for material
disagreements across entry points, callers, persisted data or docs. It can be a
section in the current record rather than a new file.

## Example: release evidence without collapsing stages

A test run proves its tested behavior. A build proves that artifact was produced.
An upload receipt identifies a transfer. A deployed-identity check identifies the
running artifact. A live task check observes behavior in that environment.
Declare product-specific gates for the required stages. Typed `requires` lists in
the optional helper prevent a declared build result satisfying a live-evidence
requirement, but still rely on honest tags, actual reports and environment review.

## Example: handle a missing integration

Inspect approved local policy and prepare the change. If a required independent
review or scanner is unavailable, leave that gate blocked with source, owner and
next action. Prepare a sanitized handoff in the existing task. Follow
[integration mappings](INTEGRATIONS.md) when an authorized connector becomes
available. A successful local check does not supply the missing approval.
