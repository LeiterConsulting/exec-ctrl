# Documentation that matches behavior

Use for docs, features, planning, public contracts, onboarding and changed operations.

## Actions

- Identify who uses the changed behavior and which source is authoritative for it.
  Update the nearest existing API reference, README, runbook or architecture record.
- Verify commands, paths, defaults and examples against code/configuration. Check
  links and representative examples; never execute destructive example commands
  just to check their formatting.
- Separate proposed, implemented, verified, deployed and deprecated behavior.
  Keep release notes tied to changes actually present in the artifact.
- Put user outcomes and actionable instructions before internal implementation
  details. Include configuration, compatibility, recovery and limitations when needed.
- Preserve historical records. Supersede obsolete instructions with a clear version
  boundary and migration path rather than leaving two apparent defaults.
- Record meaningful decisions and evidence where the team will find them. Avoid
  duplicating full issue/PR content into several control documents.

## Evidence and gate

`documentation`: affected audience/contracts identified, docs reconciled with the
implementation, links/examples checked, and unresolved gaps stated. If documentation
does not change, record why existing material still describes the behavior.
