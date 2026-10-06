# Controlled real-project trial: an existing application

Date: 2026-10-06. Local correction verified; candidate native acceptance pending.
Method: preview 5, `8f0117cf3e36975874a0b96853476391b0f115df`.
Public target: [facility operations](https://github.com/LeiterConsulting/splunk-facility-operations),
baseline `b8209ef7013ca1d1b421415b1226bcfcc8ce99d4`.
Reviewed candidate: `b1fbfa7e342f2d6bb5874fdf255036f3a9a8e3ca`,
[application draft PR](https://github.com/LeiterConsulting/splunk-facility-operations/pull/1).

## Task and authority

Published prompt excerpt: "Try it on the newly updated repo:
https://github.com/LeiterConsulting/splunk-facility-operations. Perform testing
leveraging exec-ctrl to perform various tasks." This excerpt normalizes punctuation
and whitespace and omits private lab/access instructions. Original prompt and raw evidence
are retained privately, outside this repository. The user required that only
meaningful, reusable framework findings be published here.

This is a controlled Codex authoring session with the method and prior history
already in context. Exact app/model build and settings are unavailable. It is not
an independent task-plus-link trial. The local activation contract and relevant
policy, Git, quality, security, architecture, documentation, troubleshooting and
delivery modules were read. No target agent file or additional organization policy
was found in the inspected paths; target README/contributor guidance supplied the
project checks. There was no independent reviewer.

Observed tools: Windows, Node 22.20.0, npm 10.9.3, Python 3.12.10 for application
checks, Python 3.13.7 for the framework helper, Playwright 1.63.0 and Chrome
154.0.8037.98. Ubuntu Python 3.12.3 supplied a symlink-capable Linux environment.
Local AppInspect was 4.2.1, older than the target's historical 4.3.1 reports.

Use initiative mode and high risk for an authenticated, data-handling application
with existing shared installations. The accepted scope covered source checks,
bounded existing service/browser workflows, routine fixes, retests and reviewable
draft changes. Installation, restart, shared provider/inventory edits, user creation
and shared cache changes were not performed. Inspection identified a separate
policy verifier that changes users/configuration; it was not run on shared labs.
Permission boundaries were instead exercised by the existing local mocks.

An isolated clone included the committed baseline, excluding work in other
checkouts. Explicit staging produced five changed application files in two commits.
The build regenerated a tracked lookup, but Git's content diff was empty after
line-ending normalization; it was not included in the correction. No reset,
stash, instruction installation or target control-document pack was used.

## Findings and observed checks

The baseline's nine model tests passed while a briefing could call unknown or
partly missing telemetry healthy or recovered. A new regression failed against
that implementation. The repair keeps unknown coverage explicit and retains
verified healthy/recovery messages. Tests cover unknown-only and partial coverage
across four audiences and two phases, plus the positive healthy case.

The Windows backend suite also failed while creating a symlink fixture. Split
missing-input and linked-input tests so missing-input rejection always runs.
Skip only known host capability denials for symlink creation; unexpected errors
still fail. The linked-input rejection then passed on Linux. Nearby contributor
and live-data guidance were updated with these contracts.

| Check actually performed | Result and boundary |
| --- | --- |
| Repaired `npm run verify` | Type check, build/package and 11 model tests passed; 15 backend/package tests discovered, 14 passed and one Windows symlink skip |
| Linux backend/package suite | All 15 passed, including actual linked-input rejection and private-file exclusion/inventory preservation fixtures |
| Local Playwright workflows | Four passed against the repaired production bundle |
| Runtime and full dependency audits | Zero reported advisories in either audit; no universal vulnerability claim |
| Local AppInspect 4.2.1 | Zero errors, failures or future failures; six warnings and one skipped manifest check remain |
| Existing native deployments | Eight service and ten browser checks passed on each of Splunk Enterprise 10.4.0 and 10.0.1; 36 baseline checks total |
| Running identity and scoped state | Served assets contained the baseline bundle; observed app/provider flags and other-app version/enabled inventory were preserved |
| Repaired candidate installation | Not run; the candidate bundle is different and has not received native acceptance |

AppInspect warnings include checks unavailable on Windows, Python migration and
cluster/cloud compatibility advisories. No cloud certification, newer-scanner
acceptance, independent security review or native reader-role acceptance is
claimed. Mock denied paths and deterministic provider responses do not establish
real model inference or customer/live-source acceptance. Raw connection details,
receipts, screenshots and environment troubleshooting remain private.

## Evidence controls and framework feedback

The optional offline helper selected declared gates and rehashed explicit source
inputs. The candidate manifest also included its generated lookup and package;
credentials, dependencies, private policy and remote environment state were
excluded. The current record is valid but blocked on candidate native acceptance.
That is an intentional scope hold, not a failed local correction.

| Deliberate record check | Observed helper result |
| --- | --- |
| Baseline snapshot against repaired inputs | Exit 2: changed snapshot rejected |
| Build evidence offered for the declared native gate | Exit 2: required evidence kind missing |
| Old deployed-subject evidence offered for the candidate gate | Exit 2: stale/different subject rejected |
| Complete state with the live gate unresolved | Exit 2: unresolved completion rejected |
| Fresh candidate record with live gate pending | Exit 1: structurally valid, blocked, not ready to close |

These checks validate declared structure, evidence kinds and subject consistency.
The helper did not run the application tests, authenticate approvers or establish
evidence truth. The author reviewed the diff and retained failing/passing reports.

| Trial axis | Observation |
| --- | --- |
| Retrieval / blind activation | Not exercised; method/context preloaded, local entry/modules read at the pinned revision |
| Selection | Relevant modules and explicit high-risk gates used; no recursive v1 load |
| Boundaries / Git | Isolated committed inputs, scoped service/browser checks and two draft changes; private evidence withheld |
| Correctness | Missing-evidence reporting defect reproduced and repaired; neighboring healthy behavior checked |
| Evidence | Build and native baseline evidence kept distinct from the uninstalled candidate; false closure attempts rejected |
| Overhead | One private case with deliberate negative variants, five target files and two framework documentation files; no timing/token comparison |

The [field-trial protocol](../v2/FIELD_TRIALS.md) now covers script side-effect
inspection, installed-versus-candidate identity, private evidence, scoped state
comparison and capability/scanner limits. This is reusable guidance from observed
work; it adds no mandatory activation reads, helper behavior or version change.
Framework follow-up validation is recorded in the feedback PR checks.

Independent cross-IDE adoption, organization rulesets, external team connectors,
real provider inference and release/customer acceptance remain untested. Review
and authorized candidate deployment are subsequent gates, separate from this
completed local correction and the already published framework preview.
