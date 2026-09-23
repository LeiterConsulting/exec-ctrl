# v2 review and delivery roadmap

Baseline reviewed: `68f5c4a`, 2026-09-23. This roadmap is planning; current evidence
lives in the [foundation record](../exec_ctrl/V2_FOUNDATION_EXEC_CTRL.md).

## Existing version: retain and change

| Baseline evidence | Assessment | v2 response |
| --- | --- | --- |
| v1 method: phases, must-pass criteria, audit and decision history | Strong evidence discipline | Retain explicit gates, honest state and traceability |
| v1 minimum of six project / three initiative docs | Too much overhead for everyday agent tasks | Inline/task/initiative/project scale |
| README and interlinked manuals | Entry requires too much routing before action | One short START_HERE contract with selective modules |
| v1 bootstrap default versus current-workspace routing table | Conflicting initiative/project advice | Risk and explicit scope choose mode |
| Workspace templates center on Copilot; root AGENTS absent | Weak portable discovery | Canonical AGENTS with thin host adapters |
| v1 status-first document precedence | Can be misread as overriding policy or evidence | Explicit authority and trust boundaries |
| No executable validation at baseline | No repeatable routing/closure checks | Offline catalog, helper, tests and CI |
| Security/team/enterprise details largely absent | Broad request needs operational guidance | Ten modules with actions and evidence gates |

## Preview 1: foundation

Implemented scope: link-first entry, adaptive workflow, modules, compact templates,
versioned migration, official-documentation-based adapters, additive rulesets,
offline routing/record checks, regression tests and CI configuration.

Acceptance: coherent local entry paths, meaningful negative tests, validated local
links, transparent evidence limits. No provider is called field-validated yet.

## Next: field acceptance

The [first controlled local lab](../exec_ctrl/V2_CONTROLLED_LAB_RESULTS.md) and
hosted Windows/Linux CI passed after publishing `v2`. Independent blind adoption
trials remain the next gate; the controlled run does not substitute for them.

Run the [trial protocol](FIELD_TRIALS.md) in actual Codex, Claude Code, Cursor and
Copilot surfaces available to testers. Start from the same pinned source revision
and a task plus repository link; no hand-loaded module prompts. Include small fixes,
dirty repositories, unavailable tools, conflicting policy and adversarial issue text.

Measure actual instruction retrieval, relevant-module selection, unnecessary writes
and questions, regression detection, completion accuracy and context overhead.
Store sanitized transcripts and reproducible cases. Change defaults based on
failures rather than adding more prose for every hypothetical edge case.

## Later increments, not implemented claims

- Policy conformance fixtures against real approved organization rulesets, including
  exception lifecycle and expiry validation without bypassing enforcement.
- Optional adoption tooling with idempotent merge, dry-run, rollback and provenance
  once repeated field use establishes the needed behavior.
- Team connector adapters for specific systems with explicit write scopes,
  deduplication and conflict handling. Current team support is a workflow and record
  mapping, not shipped connector code.
- Reproducible artifact bundles/provenance and CI report adapters; scanner integrations
  should consume trusted results without leaking source or sensitive findings.
- Broader language/ecosystem examples, accessibility and performance acceptance
  fixtures, and outcome comparisons against the v1 baseline.

## Stable v2 gate

Require recorded field results for each advertised host, resolved critical workflow
failures, migration checks, reviewed release identity and documentation, and known
limits. Publication and release are separate from local implementation. A passing
offline suite does not satisfy the cross-agent gate.

No repository license file existed in the reviewed baseline. Record the owner's
chosen reuse/distribution terms before presenting a stable release for broad
adoption; this increment does not invent those terms.
