# Rubric-Review Prompt Enhancement Decision Log

| ID | Date | Decision | Rationale | Consequence |
| --- | --- | --- | --- | --- |
| `D-001` | `2026-04-24` | govern the rubric-review prompt addition under initiative-mode exec-ctrl | the request is a bounded improvement inside the already-active method repo | the prompt addition follows the same bounded-control discipline as the rubric it operationalizes |
| `D-002` | `2026-04-24` | add a dedicated review prompt instead of folding more rubric instructions into the bootstrap and method-evolution prompts | the scoring step is now generic enough to deserve its own one-command workflow | future users can invoke the rubric directly without overloading broader prompts |
| `D-003` | `2026-04-24` | route the prompt from the rubric and guidance surfaces immediately | a standalone prompt would remain easy to miss if only the prompt pack changed | the rubric doc and related guidance now expose the prompt as part of the normal ambiguity workflow |