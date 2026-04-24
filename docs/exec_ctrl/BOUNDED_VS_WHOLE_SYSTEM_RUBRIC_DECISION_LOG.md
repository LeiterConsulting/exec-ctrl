# Bounded-vs-Whole-System Scoring Rubric Enhancement Decision Log

| ID | Date | Decision | Rationale | Consequence |
| --- | --- | --- | --- | --- |
| `D-001` | `2026-04-24` | govern the rubric refinement under initiative-mode exec-ctrl | the request is a bounded improvement inside the already-active method repo | the refinement uses the same bounded control discipline it is clarifying |
| `D-002` | `2026-04-24` | add the rubric as a generic doc plus targeted workflow integration instead of as a standalone orphan surface | the scoring model is only useful if the main mode-selection paths actually invoke it | the method, bootstrap, self-hosting, prompt, and instruction surfaces now carry the rubric into ambiguous cases |
| `D-003` | `2026-04-24` | keep the rubric conservative and preserve the initiative-first default in ambiguous middle-band cases | exec-ctrl should not widen work by default just because multiple surfaces are affected | the rubric uses thresholds and overrides that still favor bounded control unless authority-model change or explicit user direction justifies escalation |