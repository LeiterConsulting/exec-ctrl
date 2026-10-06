# Controlled real-project trial: an existing application

Date: 2026-10-06. Initial local correction verified; native acceptance subsequently
passed in the authorized follow-up below.
Method: preview 5, `8f0117cf3e36975874a0b96853476391b0f115df`.
Public target: [facility operations](https://github.com/LeiterConsulting/splunk-facility-operations),
baseline `b8209ef7013ca1d1b421415b1226bcfcc8ce99d4`.
Reviewed candidate: `b1fbfa7e342f2d6bb5874fdf255036f3a9a8e3ca`,
[application correction](https://github.com/LeiterConsulting/splunk-facility-operations/pull/1).

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

| Initial check actually performed | Result and boundary |
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
excluded. The initial record was valid but blocked on candidate native acceptance.
That was an intentional scope hold, not a failed local correction.

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

| Initial trial axis | Observation |
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
real provider inference and customer acceptance remain untested. The initial trial
left review and authorized candidate deployment as subsequent gates. The follow-up
below closes the bounded native gate with new evidence, preserving the earlier
results and their original scope.

## Authorized post-merge native follow-up

After both corrections merged, the owner requested deployment and native checks.
Method: merged framework `3a1d26cb32aaecb3d1df117be2f73690da544175`.
Application: merged `b7c89e6418fe2ba84404d837d3cd6b3882f21d79`, with the same Git
tree as the tested application candidate. This remains a controlled authoring run.

Back up scoped operator files, permissions and effective settings before rollout.
Reconstruct the original installer and verify it against its retained digest;
retain it for rollback. No rollback was needed or executed. Upgrade the first
environment, restore approved operator state and verify it before the second.
Both updates rewrote operator metadata and the empty inventory file. Restore the
original bytes and permissions from the protected backups, then repeat affected
native checks. This is meaningful upgrade behavior, not evidence that a sanitized
release package automatically preserves installed state.

A new browser in one environment received an older frontend after an earlier
browser had passed candidate identity. Retain that failure. A project-supported
Web asset-cache refresh followed by new normal and regression browsers yielded
the correct candidate. Exact internal cache/worker causality was not established.
No service restart, provider change or server-side synthetic inventory write was
performed. Connection values, backups, receipts and screenshots remain private.

| Follow-up check actually performed | Result and boundary |
| --- | --- |
| Deployed identity | Raw installed bundle and fresh served assets match the repaired candidate on both supported versions |
| Normal native workflows | Eight service and ten browser checks per environment; 36 passed against the repaired candidate, with no page errors |
| Briefing regressions | Six cases per environment, 12 passed using browser-only synthetic search responses against the installed frontend; no live-source ingestion claim |
| Scoped preservation and identity | Nine checks per environment passed: protected file bytes/permissions, effective settings, inventory, other-app version/enabled flags, app flags, unchanged startup time and raw bundle identity |
| Fresh merged-source verification | 11 model tests, all 15 backend/package tests on Linux and four local browser workflows passed; Windows retains one explicit symlink skip |
| Fresh dependency audits | Runtime and full audits report zero advisories |
| Scanner artifact binding | Rebuild is byte-identical to the earlier inspected/deployed installer; the retained AppInspect 4.2.1 report applies to those bytes, with its original warnings/skips and certification limits |
| Fresh record and source comparison | Exit 0, structurally valid and ready to close; current deployment and live evidence satisfy the declared native gate |

Git checkout normalized line endings in five selected source/test/doc files after
merge reconciliation. The old raw-byte manifest was correctly rejected even
though the canonical Git tree matched the candidate. Fresh verification and a new
20-input manifest identified current inputs; the rebuild matched the deployed
artifact. Historical records and failures were retained, not relabeled as passes
for a different source subject. The helper remained offline and read-only; project
tools performed the network, upgrade and browser operations.

The twelve briefing cases check unknown-only and partial coverage in normal and
recovery phases, and positive verified healthy/recovered behavior. Their synthetic
responses exist only in isolated browsers. Normal native workflows separately
exercise actual lab searches and the deterministic investigation service.

The [delivery module](../../modules/delivery.md) now makes operator-state restoration
and fresh-client asset identity explicit. This adds relevant rollout guidance,
with no activation-entry, adapter, helper, catalog or version change. Independent
adoption, organization policy, native reader-role, real model, cloud certification
and customer acceptance remain outside this completed deployment qualification.
