# Exec-Ctrl Workspace Guidance

## Repository Purpose

- This repository is the generic `exec-ctrl` method repo, not an application runtime.
- Its main governed surfaces are method docs under `docs/`, reusable template packs under `templates/`, generic examples under `examples/`, installed workspace guidance under `.github/`, and repo-local proof artifacts under `docs/exec_ctrl/`.
- When the user asks to improve this repo itself, treat the work as self-hosting method evolution by default.

## First Reading Order

- Start with `README.md` for repo purpose and entry routing.
- Read `docs/EXEC_CTRL_METHOD.md` for the base method rules.
- Read `docs/EXEC_CTRL_SELF_HOSTING_AND_METHOD_EVOLUTION.md` for self-hosted repo changes.
- Read `docs/EXEC_CTRL_AGENT_ASSESSMENT_LOOP.md` when the user asks to continue refining or enhancing this repo.
- Read `docs/EXEC_CTRL_REPO_LINK_SCORECARDS.md` or `docs/EXEC_CTRL_METHOD_REPO_REFINEMENT_SCORECARDS.md` when the request shape is ambiguous.
- Read `docs/EXEC_CTRL_SELF_HOSTING_COHERENCE_FAILURE_CALIBRATION.md` when a checklist review needs verdict calibration.
- Read `docs/EXEC_CTRL_METHOD_REPO_TEST_READY_REVIEW.md` when the question is whether the repo is ready for broader field use.
- Inspect `docs/planning/FUTURE_ENHANCEMENTS.md` for planning-only candidates and `docs/exec_ctrl/` for active or completed bounded refinements.

## Mode Selection In This Repo

- Default to initiative mode for bounded changes to docs, prompts, templates, examples, or workspace guidance.
- Use project-pack mode only when the request clearly redesigns the whole repository execution model.
- If the boundary is unclear, apply the bounded-vs-whole-system scoring rubric before choosing the control path.

## Self-Hosting Execution Rules

- Create or update the initiative control record, audit log, and decision log before substantive edits.
- The active phase is the earliest phase that is not `complete`.
- Update generic docs first, then reusable operational surfaces such as `.github/`, templates, or examples, and only then update repo-local proof artifacts.
- Keep planning under `docs/planning/` non-operational. When a candidate is promoted, make that explicit so it no longer looks untouched.

## Workspace Conventions

- Generic method docs live under `docs/`.
- Planning-only backlog lives under `docs/planning/`.
- Operational proof for active and completed bounded refinements lives under `docs/exec_ctrl/`.
- This repo uses `.github/copilot-instructions.md` as the live always-on guidance surface.

## Validation In This Repo

- Build: none. This is a documentation, prompt, and template repository.
- Test: use narrow evidence tied to the active refinement, such as markdown diagnostics, placeholder searches, routing checks, or coherence reviews.
- Validation: when self-hosting surfaces change, compare the README, generic docs, `.github/` guidance, templates, examples, planning docs, and repo-local proof artifacts for coherence.

## Useful Prompt Surfaces

- Use `.github/prompts/exec-ctrl-assess-next-refinement.prompt.md` when the user asks to keep improving this repo and the next bounded slice must be chosen from workspace context.
- Use `.github/prompts/exec-ctrl-method-evolution.prompt.md` for bounded method, prompt, template, or governance changes.
- Use `.github/prompts/bootstrap-exec-ctrl.prompt.md` when the repo is being used to bootstrap exec-ctrl in another workspace.
- Use `.github/prompts/exec-ctrl-audit.prompt.md` for audit-remediation or findings-heavy bounded work.
- Use `.github/prompts/exec-ctrl-release-closeout.prompt.md` for release-readiness and closeout slices.
- Use `.github/prompts/exec-ctrl-migration-bootstrap.prompt.md` for migration-shaped work that needs sequencing and rollback awareness.
- Use `.github/prompts/exec-ctrl-checklist-review.prompt.md` for self-hosting coherence review.
- Use `.github/prompts/exec-ctrl-rubric-review.prompt.md` when bounded versus whole-system choice remains ambiguous.

## Useful Calibration Surfaces

- Use `docs/EXEC_CTRL_REPO_LINK_SCORECARDS.md` to calibrate ambiguous repo-link requests before or during rubric scoring.
- Use `docs/EXEC_CTRL_METHOD_REPO_REFINEMENT_SCORECARDS.md` to calibrate ambiguous self-hosting or method-repo refinements.
- Use `docs/EXEC_CTRL_SELF_HOSTING_COHERENCE_FAILURE_CALIBRATION.md` to interpret recurring checklist failure patterns.
- Use `docs/EXEC_CTRL_METHOD_REPO_TEST_READY_REVIEW.md` when deciding whether broader field testing is justified after the defined backlog is exhausted.