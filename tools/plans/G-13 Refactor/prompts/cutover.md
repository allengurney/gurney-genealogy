# Prompt — cutover (Opus) — GATED, this is the finish line

**Do not run this next.** Cutover promotes the staged package to canonical and
switches the site (Plan 02 §15, support/staging-cutover-and-rollback.md §6). It is
the *last* step, not something that follows 2a. It is **independent of and later
than** the G4 editor polish. Run it only when every gate below is green.

## Gate — all must hold before cutover
- The staged topic package is substantially complete (~15–20 units, Plan 02 §4),
  not the current 2 pilot topics.
- The root hub (`g13-john-gurney-fact-sheet.research.md` replacement) is authored
  (Plan 02 §6; 2,500–4,000 words, substantive current-state).
- The coverage checker reports **zero un-dispositioned items and zero untracked
  citation gaps** across all three ledgers (Plan 02 §7.4, §14).
- The difference reports (content / evidence / conclusion / website) are produced
  (support doc §5) and reviewed.
- Graph `validate` is 0-error; recovery export and latest snapshot match the live
  DB revision.
- Allen has explicitly approved the cutover.

Until then, keep authoring topics (g13-graph-authoring skill), building ledgers,
and leaving the live companion and public route untouched (Plan 02 non-destructive
invariant).

## Prompt (only when the gate is green)

```
Work in main. Execute the G13 cutover as one coherent reviewed change, per Plan 02
§15 and support/staging-cutover-and-rollback.md §6. Confirm every gate condition
first and stop if any is not met.

1. Verify the intended worktree scope is clean and bounded to this cutover.
2. Copy the exact legacy companion to research/people/_legacy/g13-pre-refactor/;
   store checksums + baseline metadata beside it.
3. Promote staged topics from research/people/_staging/g13-john-gurney/ to
   research/people/g13-john-gurney/.
4. Replace the root companion with the approved hub.
5. Migrate the staging graph DB content to the canonical location/config (export
   from staging → restore, or repoint config), refresh current.ndjson, and commit a
   versioned snapshot.
6. Switch the site default from legacy to package mode; update the few entry links;
   keep public inbound URLs stable.
7. Rebuild repo indexes; validate the canonical graph; refresh only its derived
   FTS/context/website exports.
8. Build and validate the site; run research-item / source / footnote / link
   validation.
9. Keep the legacy copy, the mode switch, the difference reports, and baseline
   hashes in place (rollback levels 1–3 must remain available) until Allen accepts.
10. Review the full Git diff before committing. Do not combine unrelated research
    promotions with this cutover.
```
