# VS Code operator checklist

Use `prepare --host vscode` and the [shared run instructions](../README.md).
Open one generated target folder as the workspace and start a fresh agent session
per case. Paste its prompt verbatim; leave evaluator material outside the workspace.

Record **VS Code version and the actual agent/harness or extension name/version**,
session target (local/remote), model, permissions, custom instructions and available
retrieval/terminal tools. Do not equate VS Code with GitHub Copilot. Codex running
inside VS Code may be recorded as another VS Code harness; identify it explicitly
rather than counting it as an independent Copilot result.

Observe which root/nested project instructions are actually discovered or read,
and separately capture the pinned remote method/module retrieval. Inspect visible
tool activity, terminal checks and editor changes; a chat response that recites
exec-ctrl is not proof of loading or execution. Record extension/version-specific
instruction limitations without changing settings to force a baseline pass.

Run local and remote workspaces as separate runs when both matter. Record the
actual execution environment; local fixture checks cannot prove another remote
workspace was tested. If using an ask-only mode for the audit, record that choice;
do not generalize its permission behavior to the coding mode.

Official reference checked 2026-10-15: [VS Code Chat view](https://code.visualstudio.com/docs/agents/run/chat-view)
describes session target, agent, model and permissions choices, with availability
depending on installed providers and policy. This is setup guidance, not a passing
test of any particular extension.
