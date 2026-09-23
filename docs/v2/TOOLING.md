# Optional offline helper

The agent can use the whole Markdown workflow without Python. For repeatable
local assistance, run the reviewed helper from an exec-ctrl checkout with Python
3.10+; it uses only the standard library. It reads explicitly supplied files,
prints JSON and never runs commands from records, writes the target or uses network.

```sh
python tools/exec_ctrl.py route --kind fix --risk low
python tools/exec_ctrl.py route --kind feature --signal auth --signal team
python tools/exec_ctrl.py route --kind release --signal production --rules examples/v2/team-rules.json
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

JSON output lists modules with selection reasons, effective risk, mode, required
gate IDs and policy provenance. It grants no execution permission.

## Rulesets

Use [team-rules.json](../../examples/v2/team-rules.json) as a fictional format example.
Each explicitly supplied ruleset has schema version, ID, source, revision, owner,
required module IDs and gates (`id`, `description`, `source`, `owner`). All its
gates apply to the invocation; there are no hidden path predicates. Select applicable
rulesets after policy inspection. Multiple files compose additively.

Duplicate IDs, unknown fields/modules and gate collisions are errors. Rulesets
cannot lower risk or remove gates. Supplying a ruleset also loads enterprise
guidance. No file is auto-discovered from the user's home or a secret store.
The helper does not validate policy authorship or support waivers.

## Records

[docs-record.json](../../examples/v2/docs-record.json) illustrates the complete
machine format, with synthetic evidence explicitly labeled as such. The Markdown
task template remains the usual user-facing record.

A record contains schema/framework versions, ID, objective, subject snapshot,
state, facts, ruleset identities, gates and evidence. Gates contain ID, result,
evidence IDs and a reason. Evidence contains ID, kind, subject, result, reference
and summary. Supported evidence kinds: inspection, test, build, deployment, live,
review. All extra fields are rejected to catch typos and unsupported expectations.

Every routed gate must be present, even if `not_run`. Additional acceptance gates
are allowed and also block closure unless passed. Passing gates require evidence
with passing results and matching declared subject. Only `git-review` can close
as `not_applicable`, with a reason for non-Git work. A complete record with unresolved
gates is invalid. A `policy-unknown` signal requires an unresolved policy gate;
update the facts only after the source is resolved. Ruleset identity, source,
revision, owner and normalized-content SHA-256 must match the explicitly supplied
rules, preventing an accidental check without a recorded policy file or against
silently changed policy content. Copy the `rulesets` list from the route output.

Exit codes: `0` = valid route/framework, or record ready to close; `1` = structurally
valid record with unresolved gates; `2` = invalid input or inconsistent claim.
Read `state` as well as `ready_to_close`; readiness does not change task state.

## Limits

This is a structural checker, not a security scanner, policy engine or proof of
completion. It cannot detect omitted risk facts, undisclosed policies, fabricated
reports or a stale snapshot given a new label. Review those claims separately.
It does not fetch evidence references. `validate` checks catalog/entry coherence
and local Markdown file destinations; it does not check external URLs or anchors.
