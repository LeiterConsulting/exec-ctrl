# Controlled real-project revisit: Ping Monitor

Date: 2026-10-05. Scoped local acceptance: `complete`.
Method: merged preview 4, `bd343d405825f19c7a5b876ddea605083ecf7739`.
Target: public [Ping Monitor](https://github.com/LeiterConsulting/ping_tool_for_splunk),
released Go v5.1.0 code at `dc653fcca7208eb8158a18ed156d87b4f85b3cb5`.

## Task, authority and selected scope

Actual user prompt: "Merged - lets use a simple project we have already completed
most work on and try it again with exec-ctrl - a simple one without much effort
which can prove out the various aspects of exec-Ctrl and one we can use to improve
what we already have for the framework."

This is a controlled revisit in the framework's existing authoring session, not an
independent blind task-plus-link trial. The method was already in context. Codex
local task on Windows; exact desktop/model build is unavailable. Observed tools:
PowerShell 7.6.6, Python 3.13.7 and Go 1.25.5 windows/amd64. The Go module requires
1.24.0; dependency downloads were disabled and the existing local cache sufficed.

Select one narrow availability-reporting fix using task mode, low risk, behavior
and operations signals. Load policy/Git, quality, troubleshooting and documentation;
inspect the affected trust boundary without inventing company rules. No target
AGENTS/organization policy was supplied or found in the inspected target paths.
Use the user's task and host instructions. Team/enterprise connectors and release
governance are outside this local fix; there is no deployment or external message.

The original checkout has tracked endpoint-reload edits and untracked artifacts.
Use a separate worktree at the committed baseline; do not copy or test those
unfinished changes. Preserve original branch/status and both edited-file hashes.
The isolated branch is `codex/exec-ctrl-summary-trial`. Its reviewed local commit is
`2d2edade281c155263bf03cf59091e746c115c89`: three files, 159 insertions and two
deletions. The target branch is not pushed; no target PR, merge or release occurred.

Acceptance: reproduce the error-summary discrepancy, repair it without changing
successful/partial reporting, run the existing Go suite and added regression tests,
verify a local build when available, compare explicit current source before record
closure, and retain sanitized evidence. Use stub pingers and temporary files only.
Do not run the monitor, contact Splunk/monitored hosts, read real endpoint/config
files, install an application, or publish target changes as a release.

## Initial discrepancy

`runEndpoint` says "Treat as total failure" when its pinger returns an error, but
passes configured count, zero successful, **zero failed, 0% loss and zero average
latency** into its summary. Its ordinary all-failed path uses failed=count,
loss=100% and unknown latency=-1. The old PowerShell implementation also computes
failed=count-success. Metrics consume these fields, so the error branch can
misrepresent an unavailable target in downstream reports.

Reproduce with an injected error, no ICMP/HTTP calls. Check normal success,
partial/all failure and normalized count. This is a correctness finding; no
exploitation or universal vulnerability claim is inferred from it.

## Evidence and framework feedback

The regression supplies a stub pinger returning an error. Before repair,
`go test ./internal/engine -v` exited 1: all four error/count subcases and the
persisted-file test failed. Normal success, partial/all failure and empty-results
subcases passed. The repair changes the error branch from
`buildSummary(ep, sumID, sumTs, count, 0, 0, 0, 0)` to
`buildSummary(ep, sumID, sumTs, count, 0, count, 100, -1)`.

The README's original build command also failed: after `go -C .\go`, its package
argument `.\go\cmd\pingmonitor` resolved to a nonexistent `go/go/cmd/pingmonitor`.
Correct it to `go -C ./go build -o ../pingmonitor.exe ./cmd/pingmonitor`, and document
the failure contract and offline regression command. This is a documentation
execution defect, separate from the availability calculation.

| Check actually performed | Observed result and scope |
| --- | --- |
| Baseline `go test ./...` | Exit 0; three existing config tests, no engine tests; committed baseline only |
| Added regression against original implementation | Exit 1, wrong failed/loss/average values reproduced; no real pinger |
| Repaired `go test ./... -v` | Exit 0; six top-level functions including three new engine tests and eight engine subcases |
| Temporary NDJSON output | Correct failure summary persisted through the actual output manager; no extra record; HEC/metrics disabled |
| `go vet ./...` and `git diff --check` | Exit 0 |
| Exact corrected README build command | Exit 0; local binary built |
| Binary `--version` and `--help` | Exit 0 before configuration/engine startup; version still v5.1.0 |
| Old manifest against repaired source | Exit 2, `snapshot files changed or manifest is inconsistent` |
| Fresh scoped record/snapshot | Exit 0, valid and ready to close; behavior/verification require test evidence, separate local build gate requires build evidence |
| Original checkout preservation | Main/HEAD/status unchanged; both original modified-file SHA-256 values match intake; untracked status unchanged |

The target's three new engine functions cover backend errors with/without
individual output, zero/negative count normalization, success, partial/all
failure, empty replies and decoded persisted output. They assert the reporting
contract, including no fabricated individual replies, rather than the repaired
function call alone. Full tests and vet ran after the final source/README changes.

The local evidence bundle retains `before.json`, `pending-record.json`,
`stale-check.json`, `after.json`, `complete-record.json`, `closure-check.json`,
execution notes and the unreleased binary. Notes summarize observed tool output;
they are not verbatim transcripts or independent reports. Nothing relabels the
failing run as current passing evidence. The snapshot selects the same 20 Go
source/module/README files before and after repair, excluding real config,
endpoints, original unfinished edits, the binary and environment state.

- Before subject: `sha256:80aab2a9be8b5ad102bd0365e6ca0f36f0fc61e6b073b7463ceee227a3d37ab4`.
- After subject: `sha256:c9700ccf1bd77dc3e52930cd96e13f23e452282a3ce5993d51f8558e99fc1339`.
- Local binary SHA-256: `570a59137b9f6e14881119236d50d95cac99d26f035a111a8d58f7bf5917426f`.

The optional helper rehashed the source and checked record structure and evidence
kinds. It did not execute references or independently verify test truth, policy
completeness or reviewer independence. The author performed the local diff review.
The binary was retained outside the original checkout, not installed or operated.

## Observed axes and improvements

| Axis | Observation |
| --- | --- |
| Link retrieval / blind activation | Not exercised: method already in context; the actual prompt above contained no new method link |
| Selection | Task mode with low-risk behavior/operations; relevant modules and scoped gates, no full project inventory |
| Boundaries and Git | Local worktree isolated committed input; no reset/stash, instruction/settings installation, external message or production access |
| Correctness / troubleshooting | Actual reporting defect reproduced before repair; neighboring outcomes and persisted file checked |
| Evidence | Historical source rejected after change; fresh source/typed evidence used for closure; live acceptance not claimed |
| Overhead | No target control-document pack; one existing task/case record, optional caller-retained evidence and three target files; no comparative timing/token measurement |

Two protocol refinements follow from actual use:

1. Extend [field-trial guidance](../v2/FIELD_TRIALS.md) with an optional existing-project
   revisit recipe. Preserve dirty work, declare whether the worktree includes it,
   and distinguish a controlled revisit from independent task-plus-link adoption.
   Record which controls were actually exercised instead of forcing every module
   into a small task. This trial supports one bounded Go fix, not the entire product.
2. Clarify [CLI output handling](../v2/TOOLING.md): valid/pending JSON is on stdout;
   invalid-input JSON is on stderr with exit 2. An initial capture wrapper parsed
   only stdout and failed on the stale-input rejection. Correcting the wrapper
   captured the expected denial; this was not a helper defect.

No helper/catalog behavior or version changes are needed for these documentation
refinements. The compact activation entry and host adapters remain unchanged.

Framework follow-up validation on Windows/Python 3.13.7 passed: 10 modules and
289 supported local links; 108 discovered tests, 106 passed and two skipped
because symlink creation is unavailable on this host. `git diff --check` passed.
These checks cover the framework and its existing synthetic fixtures, separately
from the Go application's regression/build evidence above.

## Remaining acceptance

No real ICMP, Splunk/HEC/metrics delivery, installed service, customer workload,
security scanner, organization ruleset or team connector was exercised. The
unfinished endpoint-reload changes remain unqualified. Neither this case nor its
passing record establishes cross-IDE compatibility, compliance, an independent
review or production readiness. Those gates remain separate from this completed
local fix and from the merged framework preview.
