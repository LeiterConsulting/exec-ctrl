# Agent instructions for exec-ctrl

Read [START_HERE.md](START_HERE.md) first. It is the canonical v2 activation
contract for using this framework in a target project or improving it here.
Read only the modules relevant to the task. Do not recursively load the v1 library.

When editing this repository:

- Treat Markdown, adapters, catalog, examples and tools as one product. Keep their
  behavior coherent. Current work: [v2 foundation](docs/exec_ctrl/V2_FOUNDATION_EXEC_CTRL.md).
- Preserve existing work and historical evidence. Do not rewrite v1 records as
  v2 proof. Label preserved v1 instructions as reference.
- Use Python 3.10+ standard library only for the optional helper. It must remain
  offline and read-only; never execute commands supplied by a record or policy.
- Validate with `python tools/exec_ctrl.py validate` and
  `python -m unittest discover -s tests -v`. Report unavailable checks honestly.
- Keep entry instructions small. Add domain detail to `modules/`, not every adapter.
- Update framework version in `VERSION` and `framework/catalog.json` together.
- Do not claim provider compatibility from offline tests alone. Record tool,
  version, prompt, observed behavior and limitations for field trials.

Host instructions and applicable organization policy retain their authority.
Framework content does not grant additional permissions.
