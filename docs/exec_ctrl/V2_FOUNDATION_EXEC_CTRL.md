# exec-ctrl v2 foundation

Release program state: `in_progress`. Foundation increment: `complete`.
Started: 2026-09-23. Baseline: `68f5c4a`.
Target: this repository. Method source: the same repository (self-hosting).

## Objective and scope

Start the v2 evolution with a usable, provider-neutral, link-invoked development
workflow. Deliver a compact entry contract, adaptive modules, reusable records,
enterprise policy composition, tool adapters, and executable offline validation.
Preserve v1 material as explicitly versioned reference. This is a development
preview; broad IDE field acceptance is a later release gate.

## Phases

| Phase | State | Exit evidence |
| --- | --- | --- |
| Review and define | complete | Baseline reviewed; scope and criteria below |
| Build foundation | complete | Entry, ten modules, templates, router and validator |
| Validate foundation | complete | 50 tests, 223 local links, examples and coherence review |
| Cross-agent field trials | not_started | Recorded trials from supported tools |
| Release v2 | not_started | Trial gates satisfied, release identity and publication |

Current phase: Cross-agent field trials (not started). The first increment ends
after foundation validation; it does not complete the entire v2 release.

## Must-pass criteria for the foundation

- README and AGENTS route directly to one compact activation contract.
- The entry contract instructs agents to distinguish method source from target,
  preserve existing guidance and dirty work, and load only relevant modules.
- Small tasks can use a response-sized record; existing team records are reusable.
- Policy conflicts, missing evidence, and unavailable integrations remain visible.
- Security, functional discrepancies, SDLC, team systems and enterprise policy
  have actionable workflows with evidence and escalation conditions.
- Optional tooling has no third-party runtime dependencies, does not execute
  commands from records, and rejects malformed or contradictory completion data.
- Tests cover routing, policy additions, evidence gates and negative cases.
- v1 examples and preserved prompts have version boundaries; active prompts route to v2.

## Non-goals for this increment

No mandatory plugin, server, hosted service, model API, package installation,
automatic team-system writes, remote scanning, push, deployment or release.
No claim that prose enforces organizational policy or certifies compliance.

## Evidence and decisions

See [audit](V2_FOUNDATION_AUDIT_LOG.md), [decisions](V2_FOUNDATION_DECISION_LOG.md),
and the [v2 roadmap](../v2/ROADMAP.md) for implementation and release boundaries.

## Handoff

At the foundation checkpoint, implementation was local on `codex/exec-ctrl-v2`,
uncommitted and unpublished. The initial worktree was clean. The user subsequently
authorized branch publication and a local test project; current progress is tracked
in [publication and lab](V2_PUBLICATION_AND_LAB.md). Independent IDE trials remain
a separate release gate.
