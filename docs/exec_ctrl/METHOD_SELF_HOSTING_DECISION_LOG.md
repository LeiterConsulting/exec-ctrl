# Method Self-Hosting Enhancement Decision Log

| ID | Date | Decision | Rationale | Consequence |
| --- | --- | --- | --- | --- |
| `D-001` | `2026-04-24` | govern this refinement under initiative-mode exec-ctrl | the request is a bounded enhancement inside the already-active exec-ctrl repo | the repo improves the method by using the same bounded control pattern it recommends elsewhere |
| `D-002` | `2026-04-24` | treat self-hosting as a generic method concern rather than a repo-local anecdote | the repo already shows recursive use, but future users need the pattern taught explicitly | the enhancement should produce method guidance and reusable activation surfaces, not only more local control records |
| `D-003` | `2026-04-24` | add a dedicated self-hosting guide instead of folding the whole pattern into one paragraph of the method doc | recursive method evolution is a distinct enough workflow to deserve its own entry point | future users can route method-improvement work through a dedicated guide while the core method doc stays compact |
| `D-004` | `2026-04-24` | add a method-evolution prompt and a generic example pack | self-hosting should be operational, not only descriptive | future agents and users get a ready-to-copy activation surface plus a concrete example of recursive governance |