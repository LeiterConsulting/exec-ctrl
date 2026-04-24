# Exec-Ctrl Future Enhancements

This document collects non-operational future enhancements for the `exec-ctrl` method repo.

It is a planning surface, not an execution-control surface.

Use it to keep likely next improvements visible without making them look active, validated, or complete.

## Planning states

- `near_term`: worth considering in the next bounded refinement or two
- `candidate`: useful, but not yet the best next slice
- `later`: directional idea that should wait for more repeated use

## Promotion rule

When one of these items becomes active work:

1. create the initiative control record, audit log, and decision log in `docs/exec_ctrl/`
2. treat this planning doc as one input to the refinement
3. remove or update the planning entry so it no longer looks unstarted by accident

## Near-term planning themes

Recently promoted from planning:

- `FE-001` added the workspace-guidance validation checklist in [../EXEC_CTRL_WORKSPACE_GUIDANCE_VALIDATION_CHECKLIST.md](../EXEC_CTRL_WORKSPACE_GUIDANCE_VALIDATION_CHECKLIST.md)
- `FE-007` added the agent assessment loop in [../EXEC_CTRL_AGENT_ASSESSMENT_LOOP.md](../EXEC_CTRL_AGENT_ASSESSMENT_LOOP.md) and installed repo-local guidance under `.github/`
- `FE-002` installed live task-shape prompt bundles for audit-remediation, release closeout, and migration bootstrap under `.github/prompts/`
- `FE-003` added repo-link ambiguity scorecards in [../EXEC_CTRL_REPO_LINK_SCORECARDS.md](../EXEC_CTRL_REPO_LINK_SCORECARDS.md)
- `FE-004` added generic self-hosting example packs for prompt-library evolution, template-library hardening, and governance-model migration under [../../examples/initiative-examples](../../examples/initiative-examples)
- `FE-005` added self-hosting coherence-failure calibration in [../EXEC_CTRL_SELF_HOSTING_COHERENCE_FAILURE_CALIBRATION.md](../EXEC_CTRL_SELF_HOSTING_COHERENCE_FAILURE_CALIBRATION.md)
- `FE-006` added method-repo refinement scorecards in [../EXEC_CTRL_METHOD_REPO_REFINEMENT_SCORECARDS.md](../EXEC_CTRL_METHOD_REPO_REFINEMENT_SCORECARDS.md)
- `FE-008` added the lightweight test-ready review in [../EXEC_CTRL_METHOD_REPO_TEST_READY_REVIEW.md](../EXEC_CTRL_METHOD_REPO_TEST_READY_REVIEW.md)

No defined planning items remain.

Future additions should be created only when repeated field use exposes a new recurring need that is not already covered by the current docs, prompts, examples, or calibration surfaces.

## Planning guidance for agents

An agent using this planning area should:

1. treat these entries as backlog signals rather than active work
2. prefer one bounded refinement at a time
3. choose the next slice based on repeated need, not novelty
4. promote the chosen item into `docs/exec_ctrl/` before substantive edits
5. close the initiative with explicit evidence and update this planning doc afterward

## Current recommendation

The repo appears ready for real-world testing now.

No defined backlog items remain. The next work, if any, should come from real field use rather than from this planning surface.