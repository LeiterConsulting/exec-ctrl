# v2 foundation audit

## 2026-09-23 baseline

Baseline `68f5c4a`; clean worktree before changes; 116 tracked files. Reviewed
README, method, bootstrap, self-hosting, assessment, workspace guidance, templates,
planning and readiness surfaces. No executable checks or root AGENTS.md existed.

Findings: document-heavy minimum; Copilot-specific onboarding; inconsistent
bootstrap mode defaults; incomplete policy/trust model; no repeatable security,
functional-discrepancy or enterprise-policy workflow. Evidence-driven completion,
explicit deferrals and scoped initiatives are worth retaining.

Verdict: v1 is useful reference material, but does not yet meet the v2 objective.

## Foundation validation

2026-09-23, Windows, Python 3.13.7. Local branch `codex/exec-ctrl-v2`, uncommitted
working tree. Verdict: `pass` for the foundation increment's offline criteria.

| Check | Result | Scope and limit |
| --- | --- | --- |
| `python -m unittest discover -s tests -q` | 50 passed | Routing, policy composition, malformed data, evidence gates and CLI behavior |
| `python tools/exec_ctrl.py validate` | Pass; ten modules, 223 links | Catalog, entry/adapters, version, local file destinations; not external URLs or anchors |
| `python tools/exec_ctrl.py check-record examples/v2/docs-record.json` | Structurally valid/ready | Synthetic example only; not actual product evidence |
| Production release routing with example team rules | High-risk initiative; baseline, security, delivery and organization gates retained | Declared facts and fictional rules, not actual enterprise compliance |
| Python 3.10 grammar check | Pass | AST syntax compatibility only; local execution used 3.13.7 |
| `git diff --check` | Pass | Tracked diff whitespace; additional new-file whitespace reviewed separately |
| Entry reading budget | 1,072 words | Under the 1,700-word enforced ceiling; modules load selectively |
| Coherence review | Pass | README, contract, modules, adapters, templates, examples and version boundaries inspected |

## Review corrections

- Unknown policy now prevents a passing policy gate, including contradictory
  complete records. Unaffected work can still be recorded in progress.
- Ruleset identity includes normalized-content SHA-256, so a changed obligation
  cannot reuse a saved record merely by retaining its revision label.
- Local link checks reject source paths resolving outside the repository.
- Active Copilot prompts now use v2 rather than silently activating v1 packs.

## Checked implementation identities

SHA-256 of the tested local files (not a release artifact or whole-tree digest):

| File | SHA-256 |
| --- | --- |
| tools/exec_ctrl.py | `561fc5b1c3a7a962174a57884b2f89ec2a3c9c91a5a08ab1da2234f429ea3842` |
| tests/test_exec_ctrl.py | `bd99441b40ac9516975123202d583e1f9062cf8e09c6ca91e097100b0cb04d46` |
| framework/catalog.json | `1b1d469a1d399e01863f52420bfd99e3a16a593fd7de88f7fc168698ef7014b4` |
| START_HERE.md | `fe582538e0a65d1a3efd7321ae20ac2fc58ae0cf6ae792f078022569e74a5b62` |

## Outstanding acceptance

At the original foundation checkpoint, hosted CI was configured for Windows/Linux
and Python 3.10/3.13 but had not run. Subsequent publication, successful hosted CI
and controlled local trials are recorded in [the lab results](V2_CONTROLLED_LAB_RESULTS.md).
The official [checkout](https://github.com/actions/checkout) and
[setup-python](https://github.com/actions/setup-python) actions are pinned to v7
commit hashes resolved from their official remotes on 2026-09-23; credentials are
not persisted and the workflow has read-only repository permissions.

Vendor documentation research is design evidence, not proof that agents in each
IDE follow the workflow. Cross-agent trials, hosted CI, real organization-policy
acceptance, connector implementations and stable release remain open as recorded
in the roadmap. No commit, push, external team-system write or release was made
at that original checkpoint; later preview publication is tracked separately.
