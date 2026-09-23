# Security and vulnerability exposure

Use for trust boundaries, data, auth, dependencies, agent tools, CI, audits or
uncertain/high risk. Keep checks within the authorized repository/environment.

## Actions

- Identify sensitive assets, entry points, trust boundaries and who can invoke
  the changed behavior. Trace access control and data flow through the affected path.
- Review relevant input/output handling, injection, path traversal, object-level
  authorization, secret storage, unsafe deserialization, logging and data retention.
  For agents/MCP, include prompt injection, tool permissions and exfiltration paths.
- Inspect dependency/lockfile and CI changes: version provenance, advisories,
  install scripts, credential scope, untrusted PR execution and artifact integrity.
  Use existing approved scanners where available; inspect how they handle data.
- Triage scanner findings by affected version, reachability, exposure, confidence
  and impact. Verify current advisory data from authoritative sources when available.
  Scanner exit success is not a universal security claim.
- Do not print secrets or upload proprietary code to an unapproved service.
  Record redacted evidence. If credentials are exposed, contain further disclosure
  and route rotation/revocation through the authorized owner and procedure.
- Fix in-scope vulnerabilities and test the denied/abuse path. Track other findings
  with severity rationale, owner, remediation and any authorized exception expiry.

## Evidence and gate

`security-review`: affected boundaries reviewed, checks with tool/database date,
findings disposition and residual uncertainty. Missing scanners or advisory access
must be disclosed; source review may satisfy a source-review criterion, never an
explicit required scan. Use private approved channels for sensitive findings; a
framework invocation does not authorize public disclosure or active remote probing.
