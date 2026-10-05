# Architecture and SDLC

Use for features, refactors, migrations, public interfaces and multiple services.

## Actions

- Translate the request into user-visible behavior and nonfunctional constraints:
  reliability, accessibility, performance, privacy, operability and support as relevant.
- Map affected components, contracts, data ownership and dependencies. Inspect
  existing patterns before adding a framework or abstraction.
- Compare practical alternatives only for material decisions. Record tradeoffs,
  reversibility and the simplest design meeting the requirements in an existing ADR
  or a short decision section. Avoid speculative platform construction.
- Define compatibility and evolution strategy for APIs, schemas and persisted data.
  Migrations need ordering, partial-failure handling, rollback/forward recovery and
  consumer coordination. A rollback may be impossible after destructive conversion;
  say so before execution and establish the approved recovery plan.
- Sequence discovery, design, implementation, verification, release and operation
  according to dependencies. Independent work can proceed concurrently; dependent
  milestones cannot pass before prerequisites do.
- Include observability, support ownership, deprecation and eventual retirement
  where relevant. Do not stop the lifecycle at "code compiles."

Keep a trace from each material requirement to its affected contract and acceptance.
Choose measurable performance/reliability constraints and concrete accessibility
or compatibility checks when relevant. Reassess after newly discovered consumers,
data ownership or operational dependencies. An exploratory prototype proves its
bounded hypothesis; identify the remaining production lifecycle before reuse.

## Evidence and gate

`design`: affected contracts and dependencies, acceptance constraints and rationale
for significant choices. Scale the record to risk; a small refactor may need only
one paragraph. Delivery and live operational evidence have separate gates.
