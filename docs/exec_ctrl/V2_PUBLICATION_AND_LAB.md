# v2 publication and test project

Started: 2026-09-23. State: `complete` for preview publication and the controlled local lab.

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
| Publish preview branch | complete | `v2` published at `58d3cf7`; `main` unchanged; hosted CI passed |
| Retrieve pinned source | complete | Fresh remote source cache matched `58d3cf7a76b218850410a716637629b66b3b722e` |
| Exercise isolated project | complete | 50 lab checks; 91 routing cases; 13 product tests; 14 live HTTP checks |
| Report results and remaining gates | complete | [Controlled results](V2_CONTROLLED_LAB_RESULTS.md); independent trials remain open |

The local project is committed at `5051bcc` with its simulated user edit intentionally
unstaged. The lab has no remote. The service was stopped after testing. Framework
documentation now includes the evidence summary; the tested helper itself did not
require changes. Stable release and independent cross-IDE acceptance are separate.
