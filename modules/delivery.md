# Delivery and operations

Use for releases, deployment, migration, production and CI changes.

## Actions

- Establish exactly what is being delivered, to which environment, by whose
  authority, with which required reviews, checks and change window.
- Trace source revision -> build -> immutable artifact -> deployed identity.
  Record version/digest where available. Do not infer the running version from
  source files or a successful upload.
- Review CI permission and secret boundaries, especially untrusted pull requests.
  Keep required checks and environment protection intact.
- Define preflight, rollout, health checks, abort conditions, rollback or forward
  recovery, data backup/restore needs and responsible owner before the change.
- Reuse the project's delivery tooling. Observe the actual result of an authorized
  deployment and the relevant smoke/health checks. Avoid unrelated environment edits.
- Distinguish rollback of code from reversal of persisted data. Define post-release
  observation and support handoff; do not create ongoing automation unless requested.

## Evidence and gate

`delivery-readiness`: artifact/source identity, required checks, rollout/recovery
plan and applicable authorization. This gate proves readiness only. If deployment
or live acceptance is in scope, add separate required gates for deployed identity
and observed runtime behavior; a successful build cannot satisfy those gates.
