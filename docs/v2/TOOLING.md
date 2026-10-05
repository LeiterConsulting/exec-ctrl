# Optional offline helper

The agent can use the whole Markdown workflow without Python. For repeatable
local assistance, run the reviewed helper from an exec-ctrl checkout with Python
3.10+; it uses only the standard library. It reads explicitly supplied files,
prints JSON and never runs commands from records, writes the target or uses network.
JSON inputs must be regular files of at most 2 MiB, encoded as UTF-8 (an optional
BOM is accepted). Duplicate keys, non-finite numbers including exponent overflow,
malformed JSON and unsupported fields are rejected. Input errors produce exit 2.

```sh
python tools/exec_ctrl.py route --kind fix --risk low
python tools/exec_ctrl.py route --kind feature --signal auth --signal team
python tools/exec_ctrl.py route --kind release --signal production --rules examples/v2/team-rules.json
python tools/exec_ctrl.py record-template --kind fix --signal auth --id access-fix --objective "Correct tenant access" --subject "current-input-identity"
python tools/exec_ctrl.py snapshot --target /path/to/project --path src/service.py --path tests/test_service.py
python tools/exec_ctrl.py check-record examples/v2/docs-record.json
python tools/exec_ctrl.py validate
python -m unittest discover -s tests -v
```

## Routing

`--kind` is required. `--risk` defaults to `unknown`; `--signal` and `--rules`
can repeat. `--whole-project` represents an explicit request for whole-product
governance. Supported values and module triggers are in
[catalog.json](../../framework/catalog.json).

The helper does not infer facts from source code. The agent inspects the project
and supplies facts; it must add relevant signals and product-specific gates.
Auth, data, payments, production and destructive signals raise risk to high;
incidents and migrations also receive high-risk handling. High risk, team ownership
or multiple services choose initiative mode. Only low-risk docs/fixes with no
additional signals/rules can select inline mode. Whole-project scope selects project
mode. Unknown risk loads quality and security as a conservative starting point.
Performance, accessibility and compatibility signals select appropriate quality,
design and documentation controls; they do not claim those properties are verified.

JSON output lists modules with selection reasons, effective risk, mode, required
gate IDs and policy provenance. It grants no execution permission.

## Rulesets

Use [team-rules.json](../../examples/v2/team-rules.json) as a fictional format example.
Each explicitly supplied ruleset has schema version, ID, source, revision, owner,
required module IDs and gates (`id`, `description`, `source`, `owner`). All its
gates apply to the invocation; there are no hidden path predicates. Select applicable
rulesets after policy inspection. Multiple files compose additively.
Their command-line order does not change record validity; each ruleset must still
have a unique ID and unchanged identity/content. Array order within an individual
ruleset is part of its content hash.

Duplicate IDs, unknown fields/modules and gate collisions are errors. Rulesets
cannot lower risk or remove gates. Supplying a ruleset also loads enterprise
guidance. No file is auto-discovered from the user's home or a secret store.
The helper does not validate policy authorship or support waivers.
An optional gate `requires` list adds required evidence kinds. These remain binding
when checking a record even if its author omits the list from the saved gate.

## Pending records

`record-template` accepts the same routing flags plus required `--id`, `--objective`
and `--subject`. It prints a schema-1 record with every routed gate `not_run`, reasons
populated, no evidence and state `not_started`. The supplied ID is retained.
It never creates a passing claim. A generated record is valid pending work;
`check-record` returns 1 until its obligations are resolved.

Capture stdout in the existing task or an authorized file if useful. The helper
does not write that file. Use UTF-8 when saving JSON; older PowerShell redirection
may use another encoding. Markdown-only and response-only workflows remain valid.

## Content snapshots and freshness

`snapshot --target <root> --path <file>` hashes only explicit repository-relative
POSIX file paths; repeat `--path` for all selected inputs. Output includes each
canonical relative path, SHA-256 and byte count, plus a portable aggregate `subject`.
Input order and absolute checkout location do not change the aggregate. Content,
path or selected-file membership changes do. No file contents appear in output.

Select the affected implementation, relevant tests, dependency/configuration files
and instructions rather than relying on HEAD for a dirty tree. No files, secrets
or home-directory rules are auto-discovered. Path escapes, nonexistent files,
directories, parent traversal, symbolic links/redirected directories,
duplicate/aliased inputs and oversized inputs are rejected. Refusing redirected
paths avoids losing the selected path's meaning when a link is repointed. Limits:
256 files, 16 MiB per file and 64 MiB total. Select a bounded slice or use an approved
artifact/provenance system for larger inputs; do not silently truncate coverage.

After capturing the manifest and using its subject in a record, compare against
the current target before closure:

```sh
python tools/exec_ctrl.py check-record /approved/record.json --snapshot /approved/snapshot.json --target /path/to/project
```

`--snapshot` and `--target` must be supplied together. The helper rehashes listed
files, checks manifest identity, then requires the record subject to match. Changed,
missing or renamed selected files, tampered metadata or a different record subject
produce exit 2. Keep old manifests/reports historical and collect new evidence.

Snapshots exclude unlisted files, permissions, runtime/tool versions and environment
state. Reads are per file, not an atomic repository capture. During concurrent edits,
use an isolated immutable input or repeat comparison at the appropriate checkpoint.

## Records

[docs-record.json](../../examples/v2/docs-record.json) illustrates the complete
machine format, with synthetic evidence explicitly labeled as such. The Markdown
task template remains the usual user-facing record.

A record contains schema/framework versions, ID, objective, subject snapshot,
state, facts, ruleset identities, gates and evidence. Gates contain ID, result,
evidence IDs and a reason. Evidence contains ID, kind, subject, result, reference
and summary. Supported evidence kinds: inspection, test, build, deployment, live,
review. All extra fields are rejected to catch typos and unsupported expectations.
The one gate extension is optional `requires`, a unique list of those kinds.

Every routed gate must be present, even if `not_run`. Additional acceptance gates
are allowed and also block closure unless passed. Passing gates require evidence
with passing results and matching declared subject. Only `git-review` can close
as `not_applicable`, with a reason for non-Git work. A complete record with unresolved
gates is invalid. A `policy-unknown` signal requires an unresolved policy gate;
update the facts only after the source is resolved. Ruleset identity, source,
revision, owner and normalized-content SHA-256 must match the explicitly supplied
rules, preventing an accidental check without a recorded policy file or against
silently changed policy content. Copy the `rulesets` list from the route output.

A passing gate with `requires: ["deployment", "live"]` needs referenced passing
evidence of both kinds for the current subject. A build cannot satisfy either kind.
Local and supplied-policy requirements are unioned. Additional unrequired evidence
is allowed but must still pass and match the subject. Kind tags do not verify the
report's truth, environment identity or an actor's independence. See the
[pending release example](../../examples/v2/pending-release-record.json) and its
[fictional rules](../../examples/v2/release-rules.json).

Exit codes: `0` = valid route/framework, or record ready to close; `1` = structurally
valid record with unresolved gates; `2` = invalid input or inconsistent claim.
Read `state` as well as `ready_to_close`; readiness does not change task state.

## Limits

This is a structural checker, not a security scanner, policy engine or proof of
completion. It cannot detect omitted risk facts, undisclosed policies, fabricated
reports or a stale snapshot given a new label. Review those claims separately.
It does not fetch evidence references. `validate` checks catalog/entry coherence
and local Markdown file destinations. Supported link syntax includes inline links
and images, titles, angle destinations, balanced/escaped parentheses, and full,
collapsed or shortcut references. Fenced code, inline code and HTML comments are
ignored. First reference definitions win; unused definitions are not checked.
This is not a full CommonMark renderer: HTML links, indented code, block-container
syntax, external URLs and anchors are outside its validation scope.
