# Team systems and handoffs

Use for multiple owners, code review, issue systems and team handoffs.

## Actions

- Discover the existing system of record (GitHub/GitLab, Jira/Linear, Azure DevOps
  or another approved tool), repository ownership, review rules and delivery process.
  Use available authorized connectors/CLIs; none is required by this framework.
- Reuse the current issue or PR. Map outcome, acceptance, owner, dependencies,
  findings and evidence to its existing fields. Keep canonical links and IDs.
- Prepare concrete issue/PR/comment text before a write. Use existing authorization;
  check destination and sensitive content. A framework reference alone does not
  authorize posting, assigning people, changing shared status or sending messages.
- If the tool is unavailable, keep a local or response-based handoff and state
  "not synchronized." Never imply a draft was posted or a ticket was updated.
- If delegation is authorized by the user or host, give each agent a bounded scope,
  files/ownership, input revision, expected evidence and conflict protocol. Integrate
  and validate their combined result; multiple opinions do not replace tests.
- Respect required independent review and separation of duties. An agent cannot
  impersonate a reviewer or approve its own restricted change.

## Evidence and gate

`handoff`: canonical work item (or clearly unsent draft), acceptance/evidence links,
owner, dependencies and open decisions. Report synchronization and review status
separately from code completion. Reconcile fresh remote state before authorized edits
to avoid overwriting a teammate's changes.
