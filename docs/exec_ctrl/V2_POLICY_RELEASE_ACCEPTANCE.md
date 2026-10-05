# Controlled policy and release acceptance

Date: 2026-10-05. Baseline method: preview 4 at
`eda5bccdbf783876980f8c535ab8c78946d31eec`.
Preceding [PR #4](https://github.com/LeiterConsulting/exec-ctrl/pull/4) merged at
20:12:17 UTC, bringing the [Ping Monitor revisit](REAL_PROJECT_PING_MONITOR.md)
and protocol refinements into main. Preserve that case's original results.

Actual continuation prompt: "Merged. Let’s continue". This is a controlled
authoring-session extension, not an independent task-plus-link adoption trial.
Host: local Codex on Windows; exact desktop/model build unavailable. Execution uses
PowerShell 7.6.6 and Python 3.13.7; no other agent or real organization/production
system is involved.

## Scope and acceptance

The Go revisit covered a narrow fix. This increment covers a different boundary:
source -> built artifact -> isolated stage -> executed identity/behavior -> rollback
and release approval. The tests use stdlib zipapps, disposable files and fixed
subprocess input, with no network access or installed application changes.
The optional helper remains offline/read-only; the trusted test harness performs
the build and staging operations, never commands obtained from policy or evidence.

Declared release facts select initiative mode with policy/Git, quality, security,
documentation, delivery, team and enterprise controls. The existing fictional
[release ruleset](../../examples/v2/release-rules.json) supplies review and
deployment/live evidence requirements. Its owner and sources are fixture labels,
not proof of an actual organization's policy or an authorized approver.

Acceptance:

- Observe an actual wrong staged artifact despite exit 0 and a correct computation.
- Hold the failed identity gate; a build or failed report cannot satisfy runtime
  policy, even when record-local `requires` is removed.
- Restore the prior artifact, compare its SHA-256 and execute its expected behavior.
- Stage the correct built candidate, compare its SHA-256 and observe version/result.
- Keep independent approval blocked; reject a complete record with that open gate.
- Hold unavailable policy for dependent release while allowing local fixture work.
- Reject removal of a policy gate and unsupported executable policy fields.
- Keep executable metadata inert under the side-effect audit and deny opening one
  fictional private canary; verify that read guard itself with a negative probe.
- Preserve fixture instructions/unfinished notes; include only explicit application
  source in the artifact. The handoff is an unsent draft, with no system update.

## What actually ran

[Three new unittest scenarios](../../tests/test_release_acceptance.py) execute
the helper as a real CLI outside its checkout, under the test audit wrapper, with
a target path containing spaces. They build and execute the following artifacts:

| Stage | Actual observation | Disposition |
| --- | --- | --- |
| Candidate build | Explicit source packaged as a runnable `.pyz`; only `__main__.py` included; expected version `fixture-v2`, input `[2,3,5]`, total 10/count 3 | Candidate test passes; no release approval inferred |
| Previous stage | `fixture-v1`, total 10/count 3 | Save exact bytes/digest for bounded rollback |
| Wrong stage | Exit 0 and total 10, but `fixture-unexpected` and a different artifact digest | Failed identity evidence retained; runtime gate unresolved |
| False pass | Runtime gate references that failed deployment evidence | Helper exits 2 |
| Recovery | Prior bytes restored; digest and `fixture-v1` result verified | Artifact rollback passes; no persisted-data recovery claimed |
| Correct stage | Staged digest equals candidate; executed `fixture-v2`, total 10/count 3 | Local fixture deployment/runtime evidence passes |
| Required review | Author source inspection cannot meet the required review kind; independent reviewer unavailable | Final record stays blocked, exit 1; falsely declaring complete exits 2 |
| Changed policy | Same policy revision label, additional test requirement | Historical record rejected by normalized policy identity, exit 2 |

The harness checks that deleting record-local runtime requirements cannot remove
supplied-policy requirements. A separate unavailable-policy case retains a blocked
policy gate and still builds/runs a local candidate; an absent explicit ruleset
returns exit 2 rather than being treated as no policy.

The untrusted-metadata case places fake directions to bypass approval, read a
private fixture and execute a marker write in issue text/reference metadata.
The helper is a structural reader: it does not execute those references. A
test-only named-path read guard is independently triggered, then remains enabled
for helper calls. Unsupported `command` policy fields and removing the required
approval gate are rejected. No marker/publication file appears in the fixture.

The executable fixture deliberately demonstrates a limit of generic smoke tests:
exit success and correct business output can coexist with incorrect deployed
identity. The helper cannot discover that discrepancy from kind tags; the harness
measures it and reports failure. It also cannot authenticate reviewer independence:
even a `review` tag would remain an externally verifiable claim. These tests do
not strengthen it into a scanner, approver, permission enforcer or semantic inspector.

## Changes from the observations

- Add the release lifecycle and denial cases to ordinary unittest/CI discovery.
  Earlier project acceptance tested source repair; this checks actual artifact and
  executed fixture identity, recovery and a deliberately unclosed approval gate.
- Extend the test audit wrapper with an optional, named fictional read canary.
  It is never installed as a project control or claimed as a general sandbox.
- Clarify the delivery module/playbook: check artifact identity despite a healthy
  response, and verify restored identity/behavior after an abort.
- Keep the compact activation entry, helper, adapters, catalog and version unchanged.
  There is no new mandatory entry read, connector, package dependency or deployment.

## Validation and limits

Focused release suite: three tests passed. Local repository validation passed:
10 modules and 294 supported local links. Full suite: 111 discovered tests,
109 passed and two skips because symlink creation is unavailable on this host.
`git diff --check` passed. Hosted matrix results belong to the exact publication
candidate's PR. Fixtures and artifacts are disposable; assertions and a sanitized
test log are repeatable evidence, not retained release packages or real approvals.

The local fixture's `live` tag means a real, observed disposable subprocess, not
Splunk/game/device/production acceptance. All policy/reviewer identities are
fictional. No real company policy, approved vulnerability scanner, independent
review, team connector write, customer workload or cross-IDE adoption was exercised.
The automated suite succeeds by proving the release hold, not by granting it.
