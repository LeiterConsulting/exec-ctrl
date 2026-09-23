# Troubleshooting and incidents

Use for fixes, failures, incidents and unexplained behavior.

## Actions

1. State the symptom, expected behavior, affected revision/environment and impact.
   Capture the smallest useful reproduction and sanitized evidence.
2. Check recent changes and known-good behavior. Separate observation, hypothesis
   and proposed fix. Do not equate correlation with cause.
3. Rank plausible causes; choose the cheapest discriminating check. Change one
   relevant variable at a time and record why the result supports or rejects a cause.
4. If an attempt fails repeatedly, change the hypothesis or surface the dependency.
   Do not burn retries on unchanged credentials, unavailable services or missing
   user input. Continue independent diagnosis where useful.
5. Apply the smallest durable fix. For an incident, use the established containment
   and rollback process; production actions still require applicable authorization.
6. Verify both the reported symptom and nearby regression risks. Update the runbook
   or known-issue record if the diagnosis teaches something reusable.

## Evidence and gate

`diagnosis`: symptom, tested hypothesis, cause (or explicitly unresolved cause),
fix/containment, and reproduction outcome. A restart or retry restoring service is
recovery evidence, not automatically root-cause proof. If access prevents diagnosis,
record the exact blocked check, owner and next action; do not fabricate logs.
