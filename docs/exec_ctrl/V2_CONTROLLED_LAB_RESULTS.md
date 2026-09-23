# v2 controlled local lab results

Date: 2026-09-23. Method tested: published commit
`58d3cf7a76b218850410a716637629b66b3b722e` on `v2`.
Target: separate local-only Python queue lab, commit
`5051bccea1dd5d9ce9e98807f6d07ccb46dd28ba` (not a public repository).
Environment: this Codex desktop task, Windows, Python 3.13.7.

## Observed results

| Check | Result |
| --- | --- |
| Remote publication | `v2` matched local commit; `main` remained `68f5c4a4d45cf1531816b6f173332089d1bd8f08` |
| Fresh source retrieval | Separate remote clone matched the published pin; entry and helper validated |
| Hosted CI | Four jobs passed: Windows/Linux, Python 3.10/3.13 |
| Published helper unit tests | 50 passed |
| Controlled lab checks | 50 passed, zero failed in final run |
| Routing cases | 91: 72 kind/risk/project combinations plus all 19 signals; all ten modules reached |
| Helper entry points | route, check-record and validate, including all four workflow modes |
| Product regression tests | 13 passed; deliberately flawed v0 triggered 10 failures including subtests |
| Packaged service | 14 real HTTP checks passed against an extracted artifact on loopback |
| Git/instruction preservation | Simulated user edit and existing AGENTS.md retained byte-for-byte; user edit left unstaged |
| Read-only target | Content inventory unchanged; records stored outside target |
| Enterprise/team boundaries | Missing scanner and independent review remained blocked; handoff explicitly unsent |

The [GitHub CI run](https://github.com/LeiterConsulting/exec-ctrl/actions/runs/35923519145)
is evidence for the published source revision, not for other IDE behavior.

## What the scenarios exercised

- Policy/Git: existing instruction preservation, inert untrusted text/reference,
  explicit authorization boundaries, dirty-file preservation and precise staging.
- Quality/security/troubleshooting: tenant-access denial, atomic idempotency,
  invalid inputs, baseline failure reproduction and narrow corrections.
- Architecture/SDLC: migration preparation and commit only after success;
  injected failure preserved original state.
- Documentation: explicit contract, findings, diagnosis, limitations and handoff.
- Delivery: source -> ZIP -> extracted files -> running identity -> observed HTTP
  behavior, followed by shutdown of the owned test process.
- Team/enterprise: additive policy gates, hashed policy identity, blocked scanner
  and reviewer requirements, and a draft that was never represented as posted.

Negative record checks rejected missing gates, unsupported fields, absent/failed/
stale evidence, policy omission/content changes, unknown-policy passes, malformed
JSON and fabricated completion through an unresolved gate. Positive synthetic
records only prove format acceptance and are labeled synthetic in the lab.

## Live check found a real test-application defect

The first HTTP facade used `request` as a helper method name. Python's server base
class sets `request` to a socket, so the first health request failed despite passing
domain tests. The traceback identified the collision. Renaming the helper to
`dispatch`, rebuilding and rerunning produced the passing live results above.
The failed run was retained; it was not relabeled a pass. This was a lab application
bug, not a discovered defect in exec-ctrl's helper.

## Evidence identity and availability

The local lab retains timestamped command logs, routing matrix, JSON records,
HTTP observations, source snapshots and failed/successful reports. The successful
run is `20260923T214555889409Z`; the earlier failed run is `20260923T214520665025Z`.
They are local artifacts for this task, not publicly reproducible evidence bundles.

Packaged ZIP SHA-256:
`003a3f92eb036d9e48b67da2b21caa9fdcf8f780a21277ab31df2325e49eeeda`.
Packaged/extracted/running source SHA-256:
`fb5a987ae8371cd662b6558773e8af7b446bc09ea2871728e7fd43b81d22917c`.

## Interpretation and remaining gates

This is a controlled trial by the agent that authored the framework, in a task
with prior context. It is not a blind task-plus-link evaluation. Deterministic
tests and observed local actions do not establish universal prompt adherence or
prompt-injection resistance. Other IDEs, real organization-policy acceptance,
approved scanners, independent review and actual team connectors remain untested.

The local test exercise is complete. A stable v2 release remains pending the
independent trials in [the protocol](../v2/FIELD_TRIALS.md). This report does not
waive the deliberately blocked organization release gates in the fixture.
