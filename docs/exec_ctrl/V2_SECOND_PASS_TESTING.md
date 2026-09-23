# v2 second test pass

Started/completed: 2026-09-23. State: `complete` for this controlled test pass.
Baseline: framework `a31bc4b`, lab `5051bcc`; lab USER_NOTES.md intentionally dirty.

## Scope and acceptance

Continue the user's authorized local testing and v2 branch work. Extend coverage
for malformed inputs, policy composition/resumption, evidence edges, documentation
links and concurrent/failed application operations. Reproduce defects before fixing
them, preserve old reports, and add regression coverage. Keep source checks,
controlled local observations and independent IDE trials distinct.

No remote application deployment, external team writes, new agent sessions or
changes to main. Preserve the lab's simulated user edit and native instructions.
Publish tested in-scope framework corrections to v2 and verify remote identity/CI.

## Evidence

The pre-fix probes reproduced two user-visible defects: supplying unchanged policy
files in a different order rejected a saved record, and the Markdown checker missed
broken reference links while rejecting valid titles/parentheses and literal code.
The first 19 added tests reported seven failures and eleven errors (including
subtests). JSON exponent overflow and inputs over 2 MiB were also accepted before
hardening; directory input errors now have a consistent validation message.

Corrections in `2.0.0-preview.2`:

- Compare unique policy identities by ID, retaining exact content/revision matching.
- Parse the documented local Markdown link forms and ignore code/comments; this
  remains a limited link checker, not a CommonMark renderer.
- Read at most 2 MiB plus one byte from an explicitly supplied regular JSON file;
  reject oversized files and non-finite floating-point results.
- Preserve the previous schema and read-only/offline helper behavior. Historical
  preview.1 records retain their original version and pinned helper.

Local framework suite: 73 tests passed, up from 50. Coverage includes 300 field/type
mutations, malformed UTF-8, deep nesting, overflow and file-size boundaries. The CLI
returns structured errors with exit 2 for these invalid inputs without tracebacks.

Local application suite: 19 tests passed, up from 13. Added scenarios cover 480
tenant-scoped retries, 12 conflicting writers, 280 creates racing migration,
80 denied operations, rollback at each of eight migration prefixes, and copy
isolation. These are bounded concurrency tests, not throughput benchmarks.

## Published-source acceptance

Framework commit: `498e67f77922fa279ee26993693f3482073fc555`, fetched from GitHub
into the separate clean method cache and checked out at that pin. The local lab
harness and results are committed as `cf9f884ab3047f71830ff98a2403ea38b10e5960` in
the local-only test project. Its application source is unchanged from the first pass.

| Check | Observed result |
| --- | --- |
| Expanded lab | 55 passed, zero failed |
| Framework suite in retrieved checkout | 73 passed |
| Application suite | 19 passed; original baseline still produces ten expected failures |
| Routing | 91 cases; all ten modules and four modes reached |
| Extracted artifact on loopback | 68 HTTP checks passed, including concurrent retries and tenant-scoped keys |
| Service lifecycle | No server stderr; owned process stopped after acceptance |
| Preservation | Simulated user edit and native instructions byte-identical; user edit remains unstaged |
| Enterprise/team | Reviewer and scanner requirements still blocked; local handoff still unsent |
| Hosted CI | All four Windows/Linux, Python 3.10/3.13 jobs passed |
| Publication | Published v2 matched the tested commit; main stayed at its original SHA |

Hosted evidence: [CI run for the tested commit](https://github.com/LeiterConsulting/exec-ctrl/actions/runs/35926501260).
Local detailed evidence: `exec-ctrl-v2-lab/reports/20260923T220713393793Z/`, including
command logs, JSON records, routing matrix, HTTP observations and artifact identity.
The lab is not a public repository; these files are local evidence for this task.

Artifact SHA-256:
`003a3f92eb036d9e48b67da2b21caa9fdcf8f780a21277ab31df2325e49eeeda`.
Extracted/running application source SHA-256:
`fb5a987ae8371cd662b6558773e8af7b446bc09ea2871728e7fd43b81d22917c`.
Unchanged main: `68f5c4a4d45cf1531816b6f173332089d1bd8f08`.

## Remaining acceptance

These results support preview.2 evaluation. They do not establish blind link-only
retrieval, adherence in another IDE, real policy approval, scanner coverage or
external team integration. Independent field trials and the stable v2 release
gate remain open. Synthetic evidence accepted by a format test is not an actual
approval. The original evidence remains in [the first controlled report](V2_CONTROLLED_LAB_RESULTS.md).
