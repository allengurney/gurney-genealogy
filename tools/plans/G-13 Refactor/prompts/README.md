# G-13 refactor — prompt reference

Short, reusable session-start prompts. Substance lives in the plan docs, the
`g13-graph-authoring` skill, and `tools/g13_graph/README.md`; these prompts point
there and fill the blanks (keeps prompts short by design).

## Recommended sequence

Cutover is the **finish line**, not the next step — it is gated on a complete
authored package + green coverage ledgers + an authored hub, which is many Opus
authoring sessions away. 2a and the G4 polish are independent of cutover and come
first. Rough order (several tracks run in parallel):

| # | Work | Owner | Prompt | Depends on |
|---|---|---|---|---|
| 1 | Marker plumbing (Plan 2a M0/M1/M3) | Codex | `codex-2a-markers.md` | — |
| 2 | Coverage ledgers + checker | Opus (ledgers) → Fable (checker) | `coverage-ledgers.md` | — |
| 3 | Author G13 topics one at a time (markers as you go, once #1 lands) | Opus | `g3-topic-increment.md` | #1 for markers |
| 4 | G4 editor UI polish (contract fixed) | Fable | `g4-editor-polish.md` | — (any time) |
| 5 | 2a Braintree marker pilot (M2) + reader JS (M4/M5) | Opus / Plan 03 | — (folded into skill / Plan 03) | #1 |
| 5b | Source registrations + five revision increments | Sonnet, then Opus | `phase-1-and-2-prompts.md` | #3 complete |
| 6 | **Cutover** — promote package, switch site | Opus | `cutover.md` | package complete + #2 green + hub |

#1, #2, #4 can start now and run concurrently. #3 was the long pole and is **done** —
all 25 topic units are authored and `increment-complete`, so the current recurring loop
is #5b, not #3. #6 waits for the gate in `cutover.md`.

## Files
- `phase-1-and-2-prompts.md` — the current loop: one Sonnet prompt registering the three
  gating sources, then five Opus prompts for revision increments on already-committed
  units (the skill's revision path, `apply-graph-edits.py`, never `author-batch`).
- `g3-topic-increment.md` + `example-batch.json` — author one bounded topic (the creation
  loop; every planned unit now exists, so this is kept for a future new unit).
- `codex-2a-markers.md` — Codex builds the narrative-marker plumbing.
- `coverage-ledgers.md` — Opus scaffolds the ledgers; Fable builds the §7.4 checker.
- `g4-editor-polish.md` — Fable polishes the editor UI (no behavior change).
- `cutover.md` — the gated finish-line promotion (do not run early).
