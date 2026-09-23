# v2 publication and test project

Started: 2026-09-23. State: `in_progress`.

## Authorization and scope

The user requested publishing the preview to a `v2` branch on the existing
LeiterConsulting/exec-ctrl repository and using a test project in this task to
exercise its functions. Publish only that branch; the default branch stays on v1.
Create an isolated local test project with synthetic data and local-only services.
No new public application repository, team messages or production deployment.

## Acceptance

- Remote `v2` matches the reviewed local commit; default `main` is unchanged.
- The branch-specific entry and selected files can be retrieved from GitHub.
- Inspect hosted CI results for the published revision.
- A separate repeatable lab exercises routing, all ten modules, all helper commands,
  policy composition, evidence failures and realistic development scenarios.
- Fix in-scope defects found by testing and rerun relevant checks.
- Report automated assertions and controlled agent observations separately from
  blind cross-IDE trials. This agent authored the method and has prior context.

## Planned lab

Local path: `E:/exec-ctrl-v2-lab`. Method input: the published `v2` URL pinned to
its commit. Use a small Python service with tenant isolation and idempotent job
submission, a data migration, existing project instructions, simulated dirty work,
fictional policy and an unsent team handoff. No third-party runtime dependencies.

Exercise successful and denied requests, logic regressions, documented behavior,
deployment identity on loopback, rollback/failed migration, missing tools/policy,
stale evidence and hostile text treated as data. Keep deliberately flawed baseline
fixtures out of the deployed service and identify them as test-only.

## State

| Work | State | Evidence |
| --- | --- | --- |
| Publish preview branch | in_progress | Local checks and reviewed diff |
| Retrieve pinned source | not_started | Pending push |
| Exercise isolated project | not_started | Pending lab |
| Report results and remaining gates | not_started | Pending tests |

Hosted CI and all scenario results must be observed before they are marked passed.
