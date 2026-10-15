# Service desk

Small invoice-access and availabilty helpers. Python 3.10+; no dependencies.

`read_invoice(tenant, invoice)` returns the invoice amount for its owning tenant.
Missing or different tenants receive `PermissionError("access denied")`.
`coverage(samples)` returns `unknown` for empty/missing telemetry, `degraded`
when observed telemetry contains a failure, and otherwise `healthy`.
Missing coverage takes precedence over observed failures.

Run checks with `python -B -m unittest discover -s tests -v`.
