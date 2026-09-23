# Git hygiene

Always inspect applicability. A non-Git workspace requires no Git initialization.

## Actions

- Record current branch, HEAD, upstream if available, and tracked/untracked changes
  before edits. Review affected diffs to distinguish user work from agent work.
- Respect local branching and commit conventions. Use an isolated branch/worktree
  when useful, but remember uncommitted files may not be copied into a worktree.
- Do not reset, clean, stash, revert, amend or rewrite others' work as preparation.
  If overlap is unsafe, isolate your edits or ask about that specific conflict.
- Stage explicit files or hunks. Inspect staged diff, generated artifacts, binary
  payloads and accidental credentials before committing. Avoid broad `git add .`.
- Keep commits coherent and explain the behavior change. Recheck tests affected by
  merge/conflict resolution. Never resolve conflicts by blindly taking one side.
- Before an authorized push/PR, confirm target remote, base branch and final diff.
  Before authorized merge/release, inspect required checks and review state. Do not
  disable branch protection or force-push around a rejection.
- Report final Git state, including intentionally uncommitted files. Do not say
  "clean" merely because your own files were committed.

## Evidence and gate

`git-review`: baseline state, final diff review and disposition of changes.
Use `not_applicable` with reason for a non-Git task. Local validation does not prove
remote checks passed. Branch protection and server permissions enforce team gates;
this document guides the agent's behavior.
