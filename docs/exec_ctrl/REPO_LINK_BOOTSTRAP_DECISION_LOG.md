# Repo-Link Bootstrap Enhancement Decision Log

| ID | Date | Decision | Rationale | Consequence |
| --- | --- | --- | --- | --- |
| `D-001` | `2026-04-24` | govern the repo-link enhancement under initiative-mode exec-ctrl | the requested work is a bounded improvement effort inside an already-active repo | the repo demonstrates the same bounded control model it recommends for similar enhancements |
| `D-002` | `2026-04-24` | add a dedicated bootstrap guide instead of burying repo-link behavior inside the existing method doc | repo-link activation is important enough to deserve its own entry point | future users can find the bootstrap workflow quickly from the README and method guide |
| `D-003` | `2026-04-24` | add a reusable workspace-guidance template pack based on `.github` files | target repositories need agent-facing guidance in addition to markdown control docs | future agents have copyable templates for always-on instructions, doc guidance, and bootstrap prompts |
| `D-004` | `2026-04-24` | keep the new templates generic and avoid runtime automation | the repo should define the repeatable pattern before trying to automate it | the result is reusable across multiple repos and editor workflows without hidden product assumptions |
| `D-005` | `2026-04-24` | add ready-to-copy prompt bundles for recurring initiative shapes | future users need faster activation paths once the workspace-guidance layer already exists | the template pack now includes prompts for audit, refactor, release closeout, and migration bootstrap work |