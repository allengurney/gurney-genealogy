# Prompts — Phases 3–7 (backlog burn-down to cutover)

Session-start prompts for the remaining post-authoring G13 work, continuing
`phase-1-and-2-prompts.md`. All 25 topic units are authored and
`increment-complete`; Phases 1 and 2.1–2.3 are done and 2.4/2.5 are the current
loop. Everything below is ledger burn-down: the goal is all three input ledgers
at **zero un-dispositioned rows** so the cutover gate can go green.

Backlog at the time of writing (2026-07-10, mid-Phase-2): 72 gating rows —
18 legacy, 43 dump, ~11 supplemental. Phase 2.4/2.5 will trim a few more.
Always re-run `g13_coverage_check.py` at session start for the live worklist;
the enumerations below are the plan, the ledger annotations are the authority.

## Decisions taken (Allen, 2026-07-10) — the two standing cutover questions

1. **Fact-sheet probability: update to ~65%.** The fact sheet's "roughly a
   sixty percent probability" (n8 + parentage highlight + narrative para 2)
   WILL be updated to match the case file's and topic files' ~65%. This
   resolves the standing `confidence_mismatch` friction. Execute it **inside
   the cutover change (Phase 7)**, not earlier: the fact sheet is a frozen
   Plan 2b input, and editing it sooner breaks the §8.1 frozen-hash gate.
   The edit carries four follow-ons (see `cutover.md` → Resolved decisions):
   re-freeze note, three friction-annotation resolutions, and a graph revision
   to `G13-RI-000178`, whose statement currently asserts the lag.
2. **Identity units stay `public`.** Confirmed. All 25 units already carry
   `publicationStatus: public` in the staging `manifest.json`, so this is a
   no-change decision — recorded here so cutover does not re-ask.

## Sequence and ownership

| # | Work | Model | Depends on |
|---|---|---|---|
| Phase 3 | Small-rows sweep — 4 gating dump rows + 2 partial-row residuals | Sonnet | Phase 2 complete |
| Phase 4 | False-friends registry — build the artifact, close 4 dump rows | Sonnet | — (unblocked today) |
| Phase 5 | Out-of-scope routing — 35 dump rows to `routed`, ledger-only | Sonnet | — (unblocked today) |
| Phase 6.1 | Root hub authoring (Plan 02 §6) | Opus | Phases 3–5 |
| Phase 6.2 | Legacy + supplemental ledger closeout | Opus | Phase 6.1 |
| Phase 7 | Cutover — prompt already drafted in `cutover.md` | Opus | Everything + the gate |

Phases 4 and 5 are unblocked now; Phase 3 waits for 2.4/2.5 (it revises the
same units). Run all phases **sequentially**, one session at a time — they
share the canonical SQLite DB and the same ledger CSVs, and parallel sessions
will collide on both.

## Standing rules that apply to every prompt below

Same as `phase-1-and-2-prompts.md`; the load-bearing ones restated:

- **The case file is not a source.** No repo artifact ever occupies the source
  slot; cross-references open with "Cross-reference, not a source." Every
  evidence footnote leads with a third-party record and a registered `Source ID`.
- **Revision path, not creation.** `author-batch` only *creates*. Edits to
  existing items go through
  `.\.venv\Scripts\python.exe .claude/skills/g13-graph-authoring/apply-graph-edits.py <ops.json>`.
  Each op is its own transaction (no dry-run) — order ops so an earlier one
  cannot strand a later one. Derive all new RI/PM ids from the live DB, never
  from memory or this file.
- **Close out every graph-writing session:** `hash-sources` (if new local
  sources) → `export --snapshot` → `validate` (**0/0**) → `status` (tiers
  aligned) → ledger rows → `g13_coverage_check.py`. Per-increment gates must
  all read 0 for the touched topics; the whole-refactor `RESULT: FAIL` shrinks
  with every phase and is only fully cleared by Phase 6.2.
- **A dispositioned dump row needs its `source_ids`.** Plan 2b §6.1: fill the
  column from the frozen block (and its footnote definitions) whenever you set
  a disposition — the checker's §8.2 extraction verifies dispositioned rows.
- **Escalation valve:** if a row cannot be dispositioned truthfully — the
  source will not support the claim, the destination is wrong, the finding is
  already homed elsewhere — **report it and leave it in backlog**. Do not
  false-close and do not invent a citation.

---

## Phase 3 — small-rows sweep: the last topic-destination dump rows - DONE

*Model: Sonnet. Four gating rows + two non-gating residuals, spread across
four units. Depends on Phase 2 complete (2.4 owns `g13-origin-migration-network`,
which two of these rows touch).*

```
Work in main. Task: one bounded REVISION sweep closing the last topic-destination
dump rows, per the /g13-graph-authoring skill's "Revising an already-committed
increment" section. Verify Phases 2.4 and 2.5 landed (migration-network Ann Gurney
items RI-000189..000191 and the identity §6/§10 items exist in the live DB) and
stop if they did not.

Read each row's ledger annotation in
research/people/_staging/g13-john-gurney/coverage/dump-findings-map.csv before
acting — the annotations are authoritative over this list.

Four gating rows:

1. F-R4.6 — the Brackett brothers (Sudbury, Suffolk) → g13-origin-migration-network.
   A compiled-level network suggestion: John's tightest Braintree associates came
   from Brampton Gurdon's parliamentary borough, putting them inside the
   Gurdon-Winthrop Stour-valley patronage geography. Author it at exactly that
   weight — a research_finding at low-to-moderate confidence or an analysis, tied
   to the reception-network items (RI-000090/000091) and cross-referencing the
   wardship unit's Gurdon material (RI-000080/000083). It is NOT a documented tie
   to John; no item may imply one. The compiled witness (the NEHGS Early New
   England Families Richard Brackett sketch) is not registered — register it at
   the level actually examined, or leave the row in backlog and report.

2. F-R4.5 — Rev. Thomas Jenner in Venn → the same unit. Take ONLY the
   eastern-counties corridor texture: Venn pins Jenner as an Essex (Fordham) man
   who ended at Coltishall, Norfolk. alumni-cantabrigienses-venn is registered.
   Jenner's Weymouth bearing stays in RI-000020/000021 — one home per conclusion.
   Two earlier increments declined this row as identity-flavored; if on reading
   the unit you judge the datum adds nothing beyond what RI-000091 carries, close
   the row with a mentions-level link and an honest annotation instead of
   authoring a redundant finding — or leave it in backlog and say why.

3. F-R3.2 — Martha Heigham's 1591 will, the Candidate-B facet →
   g13-identity-candidate-b. Pre-made judgment: the identity-side question this
   row was held for is very likely already answered by open_question RI-000175
   (no record connects John to the senior branch's network). Read RI-000175 and
   the unit; if the will's Candidate-B reading is genuinely subsumed, close the
   row by annotation (with source_ids: muskett-suffolk-manorial-families-v1-1900
   prints the will) and author nothing. Only create an item if you find a
   distinct unhomed bearing.

4. 9.3 — speculations and loose threads. Verify each facet's stated home: the
   Mary-church-membership thread (RI-000055), the Quinapaug thread (frontier
   RI-000030), the Henry Adams co-petitioner note (already in braintree), the
   apprentice-John thread (RI-000075 / g13-identity-london-candidate), and the
   false-friend table (routes to the false-friends registry — leave that facet
   pointed there if Phase 4 has not run). Close the row once every facet is
   verified-homed or explicitly re-routed.

Two non-gating residuals in the same session:

- F-R4 / F-R3.4 residual — the Samuel Gurney × Sarah Shapley marriage (Boston,
  26 Oct 1693) → g13-family-mendon-descendants. Check whether the unit's Samuel
  (son of John Jr. and Ruth, RI-000128) can carry the identification truthfully;
  if not supportable, carry it as its own small source_evidence + open_question
  at low confidence. boston-record-commissioners-ninth-report-1883 is registered.
- F2-RESOLVED residual — add the Surney/Garney colonial spelling variants to
  data/search-variants.json, matching the file's existing shape. Update the
  row's annotation.

Close out per the skill. Report items, revisions, snapshot, rows closed, and
anything left in backlog with the reason.
```

---

## Phase 4 — the false-friends registry - DONE

*Model: Sonnet. Creates the long-promised cross-cutting artifact, then closes
the four dump rows routed to it. Unblocked today.*

```
Work in main. Task: build the cross-cutting Gurney false-friends registry as a
real repo artifact, then disposition the dump rows that have been routed to it
since 2026-07-01. No staged-topic prose edits; graph writes only if a new
source registration needs sync-sources.

Create research/topics/gurney-false-friends-registry.md — a cross-cutting
method/reference topic (same class as
research/topics/massachusetts-bay-passenger-lists-bevis-diligent-mary-anne.md,
not a G13 subject file). One entry per false friend: the name-form, the records
it appears in, the resolution, and the sources. Follow
.claude/rules/research-writing-style.md and .claude/rules/citations.md. Where a
graph item already carries the resolution (RI-000144 Dorchester Gurnell;
RI-000183 Providence Garnet; RI-000116 Gurnell elimination), cite the
third-party records and add the item as "Cross-reference, not a source."

Seed entries — verify each against the frozen dump text before writing:

- Hingham GARDNER/GARNET: Hobart's "John Garnet maried at Boston" (10 Apr 1651)
  is the Hingham Gardner/Garnet family, not a Gurney [F-R2].
- Dorchester GURNELL: "Goodman Gurney of Dorchester" = the Gurnell family,
  including the Dedham "Goodman Gurney of Dorchester, a Tanner" (2 Jan 1670/1)
  occupation sighting and "Jane Gurnet" = Jane Gornell [F-R3 facet, F-R3.5].
- Providence GARNET: the distinct Providence Garnet family [F-R6 facet].
- Muskett's GARNEYS rendered as "Gurneys" (Mirabel) [F-R3.12].
- The Hobart-journal distant-candidate / false-positive watch item [HOB-FP].
- The Wymondham "John Braintree" surname curio [noted on F-R4.11].
- The "Old Norfolk" county false-friend [noted on the routed S0 place row].
- The immigration topic's name-variant search table (Ludden/Porter/Randoll/...)
  — the supplemental "Search strategy" row is already routed_elsewhere to this
  registry; carry or cross-reference its substance.

Registration: the Hobart journal itself and the Dedham town-record witness for
F-R3.5 have no sourceIds. Register what an entry actually rests on, at the
verification level actually examined (transcript / printed edition / catalogue),
per the sources.json notes discipline (2–4 sentence catalogue annotation, never
evidence). Then bump meta.version, run
.\.venv\Scripts\python.exe tools\lint_source_notes.py (PASS),
tools\generate_id_indexes.py --write, and tools\g13_graph.py sync-sources +
validate (0/0). If an entry cannot be truthfully sourced, write what can be
sourced and leave the rest in backlog with a report.

Then the ledgers: disposition F-R2, F-R3.5, F-R3.12, and HOB-FP as routed to
the registry, filling each row's source_ids from its frozen block; update the
false-friend facet annotations on F-R3, F-R6, and 9.3, and the supplemental
Search-strategy row, to point at the real artifact path instead of "not yet
built".

Do NOT edit any frozen origin surface. Run g13_coverage_check.py before and
after: backlog drops by exactly the rows you closed and no other category
regresses. Report the registry path, entries, registrations, and rows closed.
```

---

## Phase 5 — out-of-scope routing: 35 dump rows to `routed` - WIP

*Model: Sonnet. The cheapest large win. Ledger-only — no graph writes, no topic
prose, no source registrations. Unblocked today.*

```
Work in main. Task: route the 35 out-of-scope dump rows in
research/people/_staging/g13-john-gurney/coverage/dump-findings-map.csv — the
material that is not G13 John Gurney's and never belonged to this refactor.
Ledger and leads updates only: no graph writes, no topic prose, no source
registrations, no file moves.

The 35 rows: F5; Input-1; Input-3; F-R1; F-R4.3; F-R4.9; HOB-Result;
HOB-Nearby; and the 27 round-5 rows (2.1–2.9, 2.x, 3.1–3.9, 4.1–4.8) in
dump-2026-07-03-round5-G-14-to-G-37.md. Verify the list against the live
ledger first.

For each row, following the pattern of the already-routed S0 row:
- Read the frozen dump block. If it shows any genuine G13 bearing after all
  ("Flag only any G13 bearing"), do NOT route it — leave it in backlog and
  report it.
- Set disposition `routed`. Verify the provisional destination_path and correct
  it if wrong (F5 → the G12 companion; F-R1's direct-ancestor IPMs → the
  English-line/place files, its wardship-relevant part is already in RI-000081;
  F-R4.3 → the G14/London-candidate orbit, lead already closed; round-5 rows →
  their G14–G37 subject/place files; Input-3, F-R4.9, HOB-Result, HOB-Nearby →
  the sources corpus, artifacts retained in place; Input-1's county-framing
  methods guidance is already substantially carried by the S0 place note in
  research/places/weymouth-ma.md — verify and route with a cross-reference).
- Fill source_ids from the frozen block and its footnote definitions (Plan 2b
  §6.1 — the checker's §8.2 extraction gates dispositioned rows).
- Write a note stating where the content canonically lives or will land, and
  why nothing is lost (the frozen dump retains the text; leads track the
  follow-ups).

Leads: several rows reference existing leads (L-175, L-179, L-174, L-43, L-44,
L-54, ...). Confirm with
.\.venv\Scripts\python.exe tools\research_leads.py search — and read the
subject companion before trusting a lead's Status. Where a row carries a
genuinely actionable follow-up with no lead, add one; NEG-ledger and
artifact-retention rows need none.

Run g13_coverage_check.py before and after. Gates: the un-dispositioned count
drops by exactly the rows you routed; input_source_set_gaps stays 0; no other
category regresses. Report rows routed, destinations corrected, leads added or
matched, and any row held back with its G13 bearing.
```

---

## Phase 6.1 — the root hub

*Model: Opus. The Plan 02 §6 hub is a cutover gate requirement, and several
legacy rows can only be dispositioned once it exists. After Phases 3–5.*

```
Work in main. Task: author the G13 root hub per Plan 02 §6 — the 2,500–4,000
word substantive current-state document that replaces
research/people/g13-john-gurney-fact-sheet.research.md at cutover. Author it
inside the staging package (location and manifest wiring per Plan 02 §6 and the
staging README's conventions).

Read first: Plan 02 §6, the staging README, manifest.json, and the six legacy
rows whose destination is the hub — the intro/lineage banner, the Known Facts
table, the two section containers, the Crosslinks block, and any row whose
annotation says "provisional destination: root hub".

Design the hub to carry what those blocks carried: a compact known-facts table,
the topic index by group (colonial / family / origin / identity / research),
a crosslink map, and a current identity-status statement that cross-references
the case file's ~65% model (s11) without restating it as a project fact — the
probability model stays external-canonical to the case file. Note: per Allen's
2026-07-10 decision the FACT SHEET's published figure moves to ~65% at cutover;
write the hub so it will read correctly after that edit (do not describe the
fact sheet as lagging).

The hub is a publication/working surface, not a source: every factual sentence
footnotes a third-party record with its Source ID; links to topic units and the
case file are cross-references and labeled as such where they sit in footnotes.

In the same session, disposition the hub-destined legacy rows
(retained_in_hub / synthesized, per the §7.1 vocabulary) with honest notes.
The live companion itself is untouched — the hub replaces it only at cutover.

No graph items are expected (the hub synthesizes; the units own the research),
but if you do link markers or need graph ops, follow the revision path and
close out per the skill. Run g13_coverage_check.py; report the hub path, word
count, the legacy rows closed, and anything Plan 02 §6 requires that you could
not satisfy.
```

---

## Phase 6.2 — legacy + supplemental ledger closeout

*Model: Opus. The last content work before cutover: every remaining legacy and
supplemental row to a truthful disposition. Likely 2–3 bounded sessions; keep
each session to one coherent destination group.*

```
Work in main. Task: take the legacy-companion and supplemental-surfaces ledgers
to ZERO un-dispositioned rows, per the /g13-graph-authoring skill's revision
path. Run g13_coverage_check.py first for the live worklist; read every row's
annotation before acting — several rows' facets have been closed piecemeal and
the annotations say exactly what remains.

Legacy rows (the content rows; the hub rows closed in Phase 6.1):

- "Item 4 - Boston / Book of Possessions negative - PROMOTE" →
  g13-colonial-record-coverage. Check RI-000179/000181 first: if the Book of
  Possessions class is not yet explicitly carried, author the negative (with a
  structured negative_result_scope); otherwise close by annotation + any
  missing source link.
- "Negative Results and Exclusions" → most of its enumerated negatives now
  exist (RI-000180 First Church, RI-000182 colony FTS, RI-000183 Providence,
  RI-000048..000053 dataset negatives). Verify each bullet against the graph,
  add whatever is genuinely unhomed, and close.
- "Richard Gurney (G12) - land records" → external-canonical (G12 companion).
- "External compiler assessments" residual → the tag-10-70 Grissell facet to
  g13-identity-assessment / g13-origin-age-baptism.
- "The Newgate apprenticeship / 1636 record" residual → the fuller two-Johns
  de-conflation (mhs-winthrop-papers-newgate-deed-1639, savage-dictionary,
  wikitree-newgate-14-horningsheath) to g13-identity-london-candidate.
- "Great Migration corridor - empirical priors" residuals → check what Phase
  2.4 landed first (RI-000189..000191 may now home the Gilman/Diligent corridor
  event). Route the Hotten passenger-list negative and ROLLCO livery sweep to
  g13-research-source-coverage; the Yarmouth-Edward and Epping/Finchingfield
  same-name comparators and the Shed-Finchingfield disproof to
  g13-identity-other-eliminations.
- "The grandfather and great-uncle wills" negative → g13-research-source-coverage.
- "Online and full-text lead dispositions" → the seven remaining lead-search
  sources to their identity/origin/source-coverage homes.
- "Sources Consulted", "Target source pulls" container, "Anderson cited
  sources - research outcomes", "Live catalog leads" → source-coverage /
  identity-assessment / leads-catalogue reconciliation per their annotations
  (reconcile the leads block against research-leads.csv; read companions before
  trusting Status).
- "Open Questions" residual facets per the annotation.
- Fix the two rows using the unrecognized value 'partial' (Mary Gurney/Nevis
  lead l.144; American Biography/arms l.262): resolve the remaining facet or
  restate the disposition inside the §7.1 vocabulary — do not lose the facet
  notes.

Supplemental rows (whatever remains after Phase 2.5; verify live):

- s1 family/religion partition; s8's reserved per-candidate archival sourceIds
  (most candidate units are now staged — verify which ids now journey and close
  or re-route the remainder); s10 identity facets (trade/corridor/motive/
  network recap, Coleman Street adjacency, John-of-Maldon) — check what Phase
  2.5 closed first.
- The LT9Z-KQ1 tree-profile caution / Medmenham lead / Richards non-lead row →
  a small discovery-trail carry in g13-identity-candidate-a or an honest
  routed/external disposition.
- The Earsham family-trace part → external_canonical
  (research/people/john-gurney-earsham-will-1638.md holds it).
- The candidate-others banner residuals: ancestry-norfolk-1535-1812 (Norfolk
  household-density context) → a Candidate-B increment or an explicit
  external/routed disposition; the Costessey/Cawston/Providence/Isaac/Maldon
  external subject files; the Margaret Rovett/Rybett no-source-id lead stays a
  recorded friction, not a citation.
- The "Wider Norfolk and same-name Gurney records" comparator row per its
  annotation.

Also clear the four stale citation-map warn rows on g13-colonial-record-coverage
(ballou-history-of-milford-1882, billerica-town-records-ms, hazen-billerica-1883,
nash-historical-sketch-weymouth-1885 are listed but not cited by the unit):
retag cited_role (context_only/cross_unit) or remove per the ledger's own rules.

Escalation valve as always: a row that cannot close truthfully is reported, not
forced. Close out each session per the skill. After the final session,
g13_coverage_check.py must read zero un-dispositioned rows across all three
ledgers and zero gaps in every source-lossless category — the first all-green
run of the refactor. Report per session; in the last report state explicitly
whether the cutover gate's coverage conditions are now met.
```

---

## Phase 7 — cutover

The prompt is already drafted in [`cutover.md`](cutover.md) — do not run it
until every gate condition there is green. Both of the standing decisions the
gate was waiting on were taken by Allen on 2026-07-10 and are recorded at the
top of this file and in `cutover.md` → Resolved decisions:

1. The fact sheet's "roughly a sixty percent probability" is updated to the
   case file's / topic files' ~65% **as part of the cutover change** (step 4b
   there), with the frozen-inventory re-freeze note, the friction-annotation
   resolutions, and the RI-000178 graph revision that follow from it.
2. The identity units stay `public` — already true in `manifest.json`; no
   change required.
