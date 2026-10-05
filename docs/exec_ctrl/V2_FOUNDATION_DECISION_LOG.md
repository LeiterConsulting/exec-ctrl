# v2 foundation decisions

## 2026-09-23

- D1: Make plain Markdown the portable runtime. Optional tools assist agents;
  users do not need to install them to invoke exec-ctrl.
- D2: Use a short activation contract and selective modules; choose record size
  by risk and coordination needs, not by a mandatory document count.
- D3: Preserve host instruction precedence and applicable organization controls.
  Status is a claim checked against evidence, never permission to ignore policy.
- D4: Keep machine assistance advisory and offline. No inferred permission to
  publish, execute arbitrary scripts, install integrations or contact teammates.
- D5: Identify this increment as 2.0.0-preview.1. Offline validation and live
  cross-agent field trials are separate gates before a stable v2 release.
- D6: Keep v1 paths intact with explicit version boundaries; provide a migration
  route rather than converting historical evidence into new claims.
- D7: Bind optional policy records to normalized ruleset content hashes, as well
  as declared provenance, and reject an unresolved-policy/pass contradiction.
- D8: The initial increment is locally validated. Keep hosted CI and cross-agent
  field trials pending; no publication or stable-release claim follows from it.
