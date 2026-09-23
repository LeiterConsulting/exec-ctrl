# v2 operating model

Start with [the activation contract](../../START_HERE.md). That contract defines
the required behavior; modules specialize it. Templates and examples are aids.
Catalog/tooling implement a conservative subset of routing and record checks.
Historical v1 material is not the v2 default.

## One record, proportional detail

Keep the outcome, scope, relevant controls, acceptance, decisions, evidence and
handoff in the team's existing task/issue/PR when possible. A small task can keep
all of this in the response. Use [TASK_RECORD.md](../../templates/v2/TASK_RECORD.md)
when no adequate record exists. Separate findings/decisions only when they need
their own lifecycle. Do not write records into a read-only target.

Task states remain `not_started`, `in_progress`, `blocked`, `complete`, `deferred`.
`blocked` means a named dependency prevents the scoped next action; unaffected
work may continue. `deferred` means explicitly removed from the current delivery
scope with reason, owner and follow-up. It is not an alternative spelling of pass.

## Gates and evidence

All work has four baseline gates:

| Gate | Required claim |
| --- | --- |
| `scope` | Outcome, boundaries and acceptance are explicit |
| `policy` | Applicable instructions and action scope are reconciled |
| `verification` | The checks required for the scoped outcome have evidence |
| `review` | Final result/diff has been reviewed against acceptance |

Modules and organization rules add gates. Add product-specific acceptance gates;
the catalog cannot enumerate what an application needs. A baseline review may be
agent self-review, but never substitutes for required independent human review.

Gate results: `pass`, `fail`, `blocked`, `not_run`, `not_applicable`. Nonpassing
results need reasons. A non-applicable determination needs scope evidence and
cannot waive a mandatory rule. The optional helper is deliberately stricter:
only `git-review` can close as `not_applicable`; other selected gates must pass.
Resolve selection mistakes by correcting recorded facts with an explanation, not
by hiding failed acceptance criteria.

For each evidence item record kind, subject/revision, reference, check/environment,
result and limits. Protect secrets and sensitive findings. Keep evidence linked
to the final relevant inputs. For a dirty tree, use a diff/artifact digest or another
precise snapshot identifier, not HEAD alone. For multiple artifacts, identify a
manifest containing their revisions/digests and use that as the subject.

An automated test, code review, deployment receipt and observed runtime behavior
prove different things. A claimed pass with stale inputs requires revalidation.
The helper checks matching declared subjects and referenced results; it does not
read reports to verify truth or detect an author mislabeling a snapshot.

## Dependencies and continuation

The active milestone is the earliest unmet prerequisite on the current dependency
path. This preserves v1's gate discipline without serializing unrelated work.
Do not report a dependent milestone complete while its prerequisite is unresolved.

At a checkpoint or handoff, preserve current scope, target state, selected modules,
decisions, evidence, blockers/owners and next action. On resumption, inspect the
current instructions and Git state and compare them with the record. Reassess
controls if scope, data sensitivity, dependencies or production impact changed.

## Advisory versus enforced

Markdown guides behavior. The optional helper validates declared data. Neither
can guarantee agent obedience, policy completeness, security or compliance.
Branch protection, IAM, CI and environment approval must enforce mandatory
operations where the team requires them. A ruleset records those obligations and
evidence, rather than replacing those systems.
