# Cursor operator checklist

Use `prepare --host cursor` and the [shared run instructions](../README.md).
Open one generated target folder in Cursor and start a fresh Agent session for
each case. Paste its prompt verbatim. Keep evaluator material outside the session.

Record Cursor version, Agent mode, model, approval/tool permissions and any user,
team or project rules/skills that may influence behavior. Record their presence
without exporting private rule text. Distinguish native project instruction loading
from explicit retrieval of the remote exec-ctrl entry and selected modules.

Observe root and nested AGENTS handling in the auth/injection cases. Note any rules
diagnostics available in the installed version and retain sanitized tool receipts;
successful output alone does not prove discovery. Confirm that a bare method link
does not trigger adoption files/settings. Mark inaccessible retrieval as blocked;
do not silently add a local exec-ctrl rule to make the baseline pass.

For an optional persistent-rule trial, use a separate fresh run, label it assisted,
and record exactly what was added. Do not mix that result with task-plus-link runs.
No setting changes or global rule installation are required by this kit.

Official reference checked 2026-10-15: [Cursor rules](https://cursor.com/docs/rules)
documents root/nested AGENTS.md and scoped MDC project rules. This informs the
checklist; it is not a compatibility result for the installed host.
