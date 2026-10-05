# Contributing

Read [AGENTS.md](AGENTS.md) and [START_HERE.md](START_HERE.md). Keep changes small
enough to review against a concrete user outcome. No mandatory dependency install
is needed for the optional Python helper.

Before submission:

```sh
python tools/exec_ctrl.py validate
python -m unittest discover -s tests -v
git diff --check
```

Change normative guidance before adapting examples and evidence records. Add tests
for behavioral changes to routing, parsing, policy composition or evidence checks;
do not add tests that only assert prose contains a preferred sentence. Check the
entry contract's reading budget and inspect version/migration boundaries.
Verify generated pending records and example policies as well as changed commands.
Test denial, stale identity, malformed input and read-only behavior for new helper
capabilities. Explicit-file snapshots must disclose their bounded scope; never
auto-read secrets or execute commands to infer project facts.

For provider-specific behavior, cite dated official documentation and distinguish
documentation support from observed field results. Update the field-trial record
only after running a real scenario. Do not mark the entire framework secure or
compliant from these checks.

Review the final diff for secrets, accidental generated files and changes outside
scope. Follow the repository's actual review and publishing authorization.
