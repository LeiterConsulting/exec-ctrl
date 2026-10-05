# Project and session loop

Use this for sustained work, changing scope, resumption or context pressure.
The [entry contract](../../START_HERE.md) remains the portable default. No session
file is required; an existing issue, task history or compact response may suffice.

## Establish a useful working agreement

Inspect the affected implementation and applicable instructions, then state the
intended result, target/snapshot, significant controls and acceptance. Record
unresolved scope or policy only when it affects a decision. Infer routine choices
from the project. Continue authorized work without asking the user to choose the
framework's mode, modules or bookkeeping format.

For a small fix, this can be one paragraph. For a migration, include prerequisite
gates, data compatibility, recovery and owners. The [playbooks](PLAYBOOKS.md) help
select the checks; they do not create additional scope.

## Execute and reassess at meaningful boundaries

| Trigger | Reassessment | Useful next action |
| --- | --- | --- |
| New trust boundary or sensitive data | Risk, policy and denied paths | Add the affected controls and acceptance before proceeding |
| Changed API, schema or dependency | Consumers, compatibility and recovery | Inspect affected callers and update contract checks |
| Failed check | Observation versus hypothesis; baseline versus regression | Run the cheapest discriminating check, then fix the supported cause |
| Repeated unchanged failure | Missing dependency, access or wrong hypothesis | Change the approach; identify the exact blocker and owner |
| New user message | Correction, status question or new objective | Answer briefly and incorporate steering into the active task |
| Combined branch or delegated result | Changed inputs, overlapping work and aggregate behavior | Review the integrated diff and run affected checks |
| Release or external write | Existing authorization, destination, current remote state | Finish concrete preparation, then perform the authorized action |

Keep unrelated work moving while a dependent operation is blocked. A missing
scanner blocks a required scan; it does not automatically prevent source fixes,
tests or preparation. Defer obligations only through an explicit scoped decision.

Delegation requires the user or host to authorize it. Define ownership and input
revision, and inspect the combined result. An agent's summary does not establish
that its edits, claimed tests or approvals are correct.

## Checkpoint without creating a second bureaucracy

Before a handoff, interruption or loss of useful context, preserve:

- Objective, accepted changes in scope and current authorization.
- Target/branch and relevant content identity, including dirty work to preserve.
- Instruction/method/policy sources and selected controls.
- Acceptance gates, current evidence and the inputs each result covers.
- Findings and material decisions, including failed attempts and excluded causes.
- Exact blocker, owner and next useful action; external synchronization status.

Use [CHECKPOINT.md](../../templates/v2/CHECKPOINT.md) only if it fills a gap in the
existing record. Store private data in its approved location; keep pointers and
sanitized conclusions in the checkpoint. Do not put secrets in instructions.

## Resume from current state

Read the latest user steering, applicable instructions and checkpoint. Inspect the
current branch, dirty files and affected content. Compare with the checkpoint's
inputs before trusting evidence. Reconcile external issue/PR state if a write is
in scope. Reroute after changes to risk, ownership, policy or acceptance.

Preserve the original report when an input changes. Mark its coverage historical;
collect fresh evidence rather than changing its subject label. The helper's
explicit-file snapshots can detect selected content changes. Omitted files,
environment changes and fabricated evidence still need separate review.

Carry forward completed work that remains valid. Rerun checks after relevant
changes, failures or unresolved concerns; repeated successful checks without new
information add overhead. A final handoff states the scoped result, its evidence
and remaining acceptance. Do not claim independent review, deployment, team updates
or ongoing monitoring from preparation alone.
