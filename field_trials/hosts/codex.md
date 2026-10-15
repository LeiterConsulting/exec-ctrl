# Codex operator checklist

Use `prepare --host codex` and the [shared run instructions](../README.md).
Select one generated target as the working directory/workspace. Start a fresh
Codex task/session per case and paste its prompt verbatim. Do not use this authoring
thread or preload evaluator instructions, method modules or the expected repair.

Record the actual surface (desktop, IDE extension or CLI), host/extension/CLI
version, model/reasoning settings, permissions/sandbox, retrieval tools and relevant
personalization/skills. Keep private configuration values out of returned evidence.
Different surfaces and local/remote execution need separate run labels.

Observe project instruction reads, any applicable parent or override instructions,
remote START_HERE/module retrieval, selected controls and actual commands/diffs.
Record whether local instruction loading is native, explicit or unobservable in
that surface. A source link is not evidence that its contents were retrieved.
Do not change sandbox or install a plugin to conceal a blocked baseline retrieval.

The auth case starts with existing dirty/untracked work; inspect its disposition.
The resume case has a stale checkpoint and changed source before the first prompt;
record actual freshness checks. It tests checkpoint reconciliation, not guaranteed
host context compaction. Use a separate observed run for real interruption/compaction.

Official OpenAI documentation checked 2026-10-15:
[Codex IDE settings](https://learn.chatgpt.com/docs/ide/settings) distinguishes
agent settings (model, reasoning, permissions and sandbox) from editor settings.
Record the settings actually available on the tested surface. This source informs
the checklist, not an observed Codex acceptance result.
