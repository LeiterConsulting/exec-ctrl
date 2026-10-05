# Agent adapters and source retrieval

The portable entry is [START_HERE.md](../../START_HERE.md), reached from the README
or [AGENTS.md](../../AGENTS.md). A task plus the repository URL is sufficient input
for a capable agent with repository retrieval access. No host is assumed to follow
a bare link automatically. Native instruction discovery usually concerns files in
the **target workspace**, not files at an arbitrary remote URL.

## First session

1. Retrieve README and START_HERE from the method source.
2. Resolve a commit/ref when possible and fetch selected modules from that same
   revision. For GitHub this can be a commit-specific blob or raw URL.
3. Inspect the user's target and apply the contract there. Do not clone the method
   into the target or execute a remote installer just to read instructions.
4. If only browser retrieval exists, use session-only adoption. If retrieval is
   unavailable, say exactly which content is missing; do not simulate ingestion.

A moving branch is convenient for discovery; reviewed, pinned content is preferable
for reproducible ongoing adoption. Never silently refresh an enterprise installation
to a new upstream revision.

## Future sessions

When persistent adoption is in scope, merge a short pointer into existing target
guidance. The [adapter snippet](../../templates/v2/ADOPTION.md) records source,
revision and local adaptations. Read existing files first; preserve unrelated rules.
Multiple native files may coexist as thin adapters to one canonical contract.
They should not carry divergent copies of the workflow.

| Host | Native entry / integration approach | Evidence boundary |
| --- | --- | --- |
| Codex | Root/path `AGENTS.md`; account for `AGENTS.override.md` and configured fallbacks | Discovery follows root-to-working-directory scope and a configured size cap; remote content still needs retrieval |
| Claude Code | `CLAUDE.md` importing `@AGENTS.md` remains a supported bridge | Native AGENTS loading depends on version/settings and the presence of CLAUDE files; verify the actual session |
| Cursor | Root/nested `AGENTS.md`, or scoped `.cursor/rules/*.mdc` when needed | Agent rule scope and mode matter; plain `.md` files under `.cursor/rules` are not MDC rules |
| GitHub Copilot | `.github/copilot-instructions.md`, path instructions or supported agent instruction files | Support differs by Copilot surface; verify the one being used |
| Other agents | Fetch/read START_HERE explicitly and retain a short task record | Capability-based workflow, not a claim of tested native integration |

This repo uses AGENTS.md as the canonical native entry, a small Claude import and
a Copilot pointer. These are instructions for working on this framework. Do not
copy their repository-maintenance commands wholesale into an application.

## Verification

Record the actual host/version, source revision, invocation and files retrieved.
Observe whether the agent selects the right controls and completes a task with
evidence. Asking it to recite rules is useful diagnostics, but does not prove
behavioral adherence. See [field trials](FIELD_TRIALS.md).

Record applicable nested guidance for the affected paths even if the current host
does not preload it. Native discovery is not the same as following a Markdown link.
Use the host's supported diagnostics to verify loaded files; do not install global
hooks or change settings to make a trial appear successful. Review instructions for
redundant mandatory reads/tests as agents improve; keep task-specific facts and
boundaries useful instead of accumulating scaffolding.

## Official references checked 2026-10-05

- [OpenAI: AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
  documents local instruction discovery, directory scope and size limits.
- [Anthropic: project memory](https://code.claude.com/docs/en/memory) documents
  CLAUDE.md imports and conditional AGENTS.md loading. It currently describes direct
  support from v2.1.277, with version/session exceptions. By default existing CLAUDE
  project files can take precedence; the local import is still a practical bridge.
- [Cursor: rules](https://cursor.com/docs/rules) documents AGENTS.md and scoped rules.
- [GitHub: repository instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions)
  documents Copilot instruction surfaces.
- [OpenAI: revisiting instructions](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)
  recommends contextual reads and reviewing redundant scaffolding as models change.

These references informed adapters. They are not cross-agent acceptance results.
