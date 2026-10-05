# Preview 5 publication

Date: 2026-10-05. Baseline: merged `main` at
`32f1795a27fa3c55e7f79a260293c99ad0d51c48`, framework preview 4.
User scope: final tests, fixes, retests and public availability for project use.
Method and target: this repository. Publication branch: `codex/preview-5-publication`.

## What this release contains

Preview 5 packages the compact link-first activation, ten selectively loaded
modules, session controls, additive policy gates and optional offline/read-only
Python helper. It includes the merged
[Ping Monitor feedback](REAL_PROJECT_PING_MONITOR.md) and
[disposable release/policy acceptance](V2_POLICY_RELEASE_ACCEPTANCE.md).
Their original revisions/results remain historical evidence, not fresh proof
for this release. The Go application fix remains a separate local project change.

Final inspection found that repository validation accepted a stale public README
or newest changelog entry while catalog/entry versions matched. Two new negative
tests failed before the correction; a positive historical-changelog case passed.
Validation now requires the current README version marker and newest changelog
version. The three cases run in ordinary unittest discovery and CI. Link checking
is isolated in those fixtures and exercised separately by the existing suite.

VERSION, catalog, activation and active synthetic records advance together to
`2.0.0-preview.5`. Schema 1, CLI/snapshot formats, host authority and helper
side-effect limits stay unchanged. Review new controls and revalidate active
records; preserve historical records with their original helper/version.
The activation entry gains no mandatory reads. The README identifies `main` as
current and the older `v2` branch as historical instead of offering it for new work.
On 2026-10-05 the owner selected the [MIT license](../../LICENSE); its standard
text is included at the repository root. This resolves the roadmap's owner-choice
gate for reuse terms without closing the independent adoption gates.

## Verification and publication

Run from the repository root with Python 3.10+ and the standard library:

```sh
python tools/exec_ctrl.py validate
python -m unittest discover -s tests -v
git diff --check
```

- Release-metadata reproduction: three cases ran against the pre-fix helper;
  stale README and stale newest changelog were incorrectly accepted (two failures).
- Local Windows/Python 3.13.7 validation: version preview 5, ten modules and 307
  supported local links. Activation entry: 1,264 words (ceiling 1,700).
- Full local suite: 114 discovered tests, 112 passed and two symlink-creation
  skips. `git diff --check` passed. Release-metadata regressions pass after repair.
- A tracked-source ZIP extracted outside the checkout passed repository validation
  and all 114 tests, with the same two host-specific skips. No Git metadata,
  local test artifacts or external project work is required in the source archive.
- Hosted Windows/Linux Python 3.10/3.13 results must belong to the final PR head;
  exact job logs and disposition are recorded with the GitHub release below.
- Merge/tag publication requires the main tree to match that tested candidate.
  The tag target and final publication status are available in GitHub metadata.

Publication identity and hosted results belong to the release's PR and
[GitHub prerelease](https://github.com/LeiterConsulting/exec-ctrl/releases/tag/v2.0.0-preview.5).
Do not extend earlier passing runs to an untested revision. GitHub's source
archives contain the framework; no plugin, generated target documents or installer
is required for the Markdown workflow.

## Use and acceptance limits

For current updates, give your agent its task and the repository link:

> Fix the checkout retry bug. Use https://github.com/LeiterConsulting/exec-ctrl

For reproducibility, substitute
https://github.com/LeiterConsulting/exec-ctrl/tree/v2.0.0-preview.5 and retrieve the
entry/modules from that revision. If the agent cannot fetch them, it must disclose
that limit rather than claim activation. See [migration](../v2/MIGRATION.md).

This is a public preview for scoped project use. Offline helper acceptance and
controlled author-run cases do not establish independent task-plus-link adoption
across IDEs, real enterprise compliance, approved scanner integration, external
connector writes, independent review or production/customer acceptance. The
[field-trial protocol](../v2/FIELD_TRIALS.md) and
[stable-release gates](../v2/ROADMAP.md) remain applicable. Source identity and
evidence tags cannot establish semantic truth or authenticate an approver.
