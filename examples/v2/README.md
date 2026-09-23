# v2 worked examples

These are illustrative scenarios, not recorded agent trials.

| Task | Selection and record | Required evidence / boundary |
| --- | --- | --- |
| Fix a spelling error in a README | `docs`, low risk; policy, Git, documentation; inline | Review intended text, diff and relevant links; no document pack |
| Fix tenant access check | `fix` + `auth`; high risk; initiative with quality/security/diagnosis | Denied cross-tenant path, allowed path, policy and final diff; no production claim |
| Refactor public API with another team | `refactor` + `api` + `team`; initiative | Contract/consumer tests, compatibility decision, docs and handoff status |
| Migrate production schema | `migration` + `production` + `data`; initiative | Backfill/partial failure, recovery, policy and release gates; deployment needs separate evidence |
| Read-only vulnerability review | `audit`; response/external record | Source/scan scope, exposure/confidence, sanitized findings; no target writes |
| Fix agent tool permissions | `fix` + `agent-tools`; task or higher by impact | Input trust, permission boundary, denied-path test; never self-expand permissions |
| Plan an entire new product | `planning` + whole-project | Requirements, dependencies and lifecycle gates; planning is not implementation |
| Enterprise release with inaccessible policy | `release` + `policy-unknown` | Prepare allowed work; hold affected release until mandatory source is resolved |

For the README typo, an inline record can be four sentences: desired correction
and scope; applicable instructions and selected controls; the edit; diff/link
checks and their results. No JSON file is needed in the target.

The [synthetic docs record](docs-record.json) demonstrates the helper's structure.
Its `example://` references deliberately do not represent real validation.
The [fictional team rules](team-rules.json) show additive policy gates, not an
organization's actual obligations. Replace sources and owners with verified ones
before operational use.
