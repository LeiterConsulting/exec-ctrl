# Portable IDE field tests

Run targeted exec-ctrl trials on separate systems without access from the author's
machine. Use Python 3.10+ and Git; no package install, lab account, scanner, server
or credential is needed by this kit. The agent still needs its usual account/tools.

This is an **operator test kit**, separate from the optional offline/read-only
framework helper. `prepare` creates synthetic Git repositories in a new directory.
The kit does not launch an IDE, change its settings or claim that a host passed.

## Get the branch on each system

```sh
git clone --branch codex/portable-ide-field-tests --single-branch https://github.com/LeiterConsulting/exec-ctrl.git
cd exec-ctrl
```

Alternatively download the branch's GitHub source ZIP and extract it. The kit
works without a `.git` directory in its own checkout. Git is still needed to
create the disposable targets. Record the branch commit or ZIP digest you used.

## Prepare one host run

From this checkout, choose the host you will actually use:

```sh
python -B field_trials/run.py prepare --host cursor --output ../trial-cursor-system-a --label system-a
python -B field_trials/run.py prepare --host vscode --output ../trial-vscode-system-b --label system-b
python -B field_trials/run.py prepare --host codex --output ../trial-codex-system-c --label system-c
```

Run only the applicable command on each machine. Use fresh anonymous labels and
destinations for repeats. Existing destinations are never reset or overwritten.
Paths with spaces work when quoted. The output parent must already exist and the
destination must be outside this checkout.

All default prompts pin the method to commit
`19b3e1b3fcb11bdff9857ce6364f640c586cdaa8`, the current v2 method before this kit.
The kit digest is recorded separately. To compare another revision, supply its
full lowercase commit SHA with `--method-ref`; use the same SHA on every system.
Method content must actually be retrieved from that revision. A moving branch or
an unavailable URL is not proof of consistent instructions.

## Run in the IDE

1. Read the appropriate operator checklist: [Cursor](hosts/cursor.md),
   [VS Code](hosts/vscode.md), or [Codex](hosts/codex.md).
2. Open **one** `targets/<case>` folder as the workspace. Do not open the kit or
   the whole run directory in the agent session. Start a fresh session per case.
3. Paste only the corresponding `prompts/<case>.txt`. Do not attach evaluator
   notes, the expected repair, or other case transcripts. The bare-link prompt
   intentionally contains only the pinned method URL.
4. Capture the agent's retrieval/tool activity, changes and final response. Record
   actual versions, model, permissions, customizations, assistance and timing in
   `results.json`. Avoid changing normal settings to manufacture success.
5. Review the target diff, then run the evaluator from the **kit** checkout.

Start with `typo` and `auth` to confirm the setup, then run the remaining cases.
Leave unrun cases marked `not_run`; partial results can be returned without
pretending that the whole host suite passed.

If a tool, source URL or command is inaccessible, record `blocked`/`not_run` for
the affected axis. Continue independent work. For an assisted/offline repeat,
use a fresh run, record `assisted: true` and the actual prompt/local source with
its provenance; do not score it as blind URL retrieval. The kit itself needs no
network after download; hosted agents or method retrieval may still need network.

## Check and return results

After reviewing the synthetic target edits:

```sh
python -B field_trials/run.py verify --run ../trial-cursor-system-a --allow-execution > ../trial-cursor-system-a/fixture-checks.json
python -B field_trials/run.py summarize --run ../trial-cursor-system-a --checks ../trial-cursor-system-a/fixture-checks.json
python -B field_trials/run.py bundle --run ../trial-cursor-system-a --checks ../trial-cursor-system-a/fixture-checks.json --output ../cursor-system-a-results.zip
```

Substitute your run path. `--allow-execution` runs reviewed target Python in a
local subprocess with a 15-second timeout. It is not a sandbox. Without that
flag, behavioral checks stay `not_run`; file/Git preservation checks still run.
Neither mode executes commands from records, issue text or policies.

Exit codes: `0` means preparation/bundling succeeded, fixtures passed, or a result
record is ready for review, depending on the command; `1` means a valid pending or
failed evaluation; `2` means invalid input/tool failure. **Fixture checks initially
fail by design**: the agent has not repaired the defects or completed the tasks.
Passing the visible baseline tests does not repair the seeded defects.

Fill the six scoring axes in `results.json` from actual observations. Put only
operator-redacted receipts in `evidence/` and reference them from the axis entries.
`pass`/`fail` requires notes and a real referenced evidence file; retrieval passes
also need the actual method revision and files. `not_applicable` needs a reason.
The [evaluator](EVALUATOR.md) defines the expected outcomes. Keep it out of agent
context. Host versions or unknown details must be recorded honestly.

`summarize` rejects checks from another run or changed target inputs. A complete
record is **ready for human review**, never automatic compatibility or release
approval. These records are operator declarations, not authenticated proof.
Keep prior checks/transcripts when rechecking a changed target; use a new output
filename rather than relabeling an earlier result.

`bundle` includes structured reports and **only explicitly referenced evidence**.
It excludes target workspaces, Git history, evaluator notes and unreferenced files.
It does not automatically redact evidence; review the included receipts before
sharing. Keep receipts small: at most 1 MiB per file, 128 referenced files and
16 MiB total. Preserve the ZIP locally and transfer it however appropriate. The kit
does not send, upload or publish anything, and partial results can be bundled.

## Scope and validation

Eight shared cases make results comparable across hosts. Host checklists target
their particular discovery, settings and agent identity. This kit does not cover
every scenario in the [full protocol](../docs/v2/FIELD_TRIALS.md), actual enterprise
compliance, real deployment/rollback, unavailable commercial scanners, cloud
agents or reliable compaction in every host. Add separately recorded trials for
those acceptance claims. Small synthetic tasks do not establish general reliability.

The repository tests exercise preparation, failure/repair, scope preservation,
freshness, result validation and portable collection. They do not drive Cursor,
VS Code or Codex. Run them with the [normal test command](../tests/README.md).
