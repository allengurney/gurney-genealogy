# Plan 2b Thread 2 — remediation manifest (destination-by-destination)

Handoff from Thread 2 (freeze + inventory), 2026-07-04. Input for Threads 3–5
(topic remediation) and Thread 6 (closeout). Basis: Plan 2b cutoff `c9006ce6`
(ten supplemental surfaces frozen; see the coverage README), graph snapshot
**revision 17** (six staged topics, items `G13-RI-000001..000042`), expanded
checker run 2026-07-04.

Checker state at handoff: `input_inventory_gaps=0`, `input_source_set_gaps=0`,
`source_journey_gaps=12`, `topic_graph_source_gaps=7`,
`publication_mapping_gaps=0`, `friction_needs_decision=0`, backlog=148
(32 legacy + 82 dump + 34 supplemental un-dispositioned rows — expected
mid-refactor). Every §4.2 audit example is now reproduced mechanically.

Row-level detail lives in `supplemental-surfaces-map.csv` (60 rows),
`legacy-companion-map.csv`, and `dump-findings-map.csv`; this manifest is the
work-order view. Nothing here authorizes edits to any origin surface.

## 1. g13-colonial-arrival-chronology (Thread 3)

Journey gaps (checker §8.3):
- `weymouth-land-grants-book-ms` — legacy l.44 row: resolved by design via
  `G13-RI-000019` in the Weymouth unit; the row's destination now includes
  the Weymouth unit, so this gap clears once Thread 3 re-runs the checker
  after confirming the cross-unit dependency prose is intact. No new link
  needed unless Thread 3 decides the arrival unit should carry its own
  representation.

Manual items (not mechanically flagged because a multi-destination row's
journey check unions its staged destinations):
- `anderson-gmd-2015` carries Anderson's published 1636-arrival/settlement
  assessment (fact sheet n8, case file n1/n7/n10). It is linked only in
  record-coverage (`G13-RI-000039/41/42`); the arrival unit has **no**
  Anderson representation. Plan 2b §10/R3 requires the published assessment
  and its cited-record relationship in the arrival graph.
- `familysearch-fulltext-search` — the 30 May 1641 petition-calendar
  full-resolution image read ("Richard Porter", film 007702977 image 947) is
  a second representation of the matter behind `G13-RI-000002/000003`
  (`massachusetts-state-archives-colonial`). Supplemental row "Finding"
  (immigration topic) carries `same_record_multiple_representations`
  friction; link the FTS representation to the same source_evidence with an
  alignment note, per Plan 2b §7.
- Hingham/arrival-vector dump findings `F11` (round 1) — reconcile with
  arrival or record-coverage (dump backlog row routes to both).
- Plan 2a markers: the Phase P arrival topic predates markers — backfill
  (`R3` explicit task).
- Arrival-envelope wording: the immigration topic sharpens the bound to
  "1638–early 1641, cannot be later" with the 1643 grant-record reasoning
  (rows "The 1640s gap…", "The Weymouth land system…"). Reconcile the staged
  arrival prose with that envelope; Plan 2b R3 says revisit the envelope
  separately from source preservation.

## 2. g13-colonial-weymouth-community (Thread 3)

No checker journey gaps of its own. Work items:
- Supplemental rows "The Weymouth land system and John's grant cohort" and
  "The 1640s gap…" journey mechanically, but the analytical depth (1636
  Fresh-Pond great-lot **absence** negative; the 1651/2 list as deferred
  laying-out with absentees and dead men; the John Read comparator) is not
  yet in the unit's prose — the coverage README flagged this overlap when the
  unit was authored. Assimilate or explicitly cross-reference.
- Backlog row "The Buckinghamshire (Aylesbury-Vale) cluster…" routes its
  Weymouth-reception slice here (Humphrey–Hunt–Randall–Brandon cluster,
  Mass. Archives 129:16 deposition). `source_id_missing` friction: the
  bucks-external footnote (weymouthhistoricalsociety.org) has no Source ID.
- Jenner/Venn reception datum (dump `F-R4.5`) — route without dropping its
  Weymouth bearing (destination also migration-network/record-coverage).

## 3. g13-colonial-braintree-community (Thread 4)

Journey gaps (checker §8.3):
- `sprague-braintree` — three rows demand it (fact-sheet Vitals-Occupation,
  case-file s1 colonial row, immigration-topic 1640s-gap row) and legacy
  rows echo it. Registered, zero item links. Carry Sprague's compiled
  occupation/Braintree statements as `published_source_statement` (Plan 2b §7).
- `familysearch-fulltext-search` — the Suffolk Deeds **Liber V** registry
  copy ("John Gurney of Braintry Taylor"): legacy l.184 row and case-file
  s10 colonial row both demand it here. Link the full deed representation to
  `G13-RI-000013` (or a new source_evidence) while retaining Bates and the
  printed Liber IV witnesses as separate representations.
- `fs-suffolk-probate-1636-1915` (case-file s1 row) — the FamilySearch
  probate-file-papers representation of Case #338 (case file n9) is a second
  representation of `spr-case-338-john-gurney-probate-1663`; link with a
  same-record alignment note rather than as a new witness.
- `adams-history-of-braintree-1891` and `adams-genesis-massachusetts-town-1892`
  (immigration-topic 1640s-gap row) — the forming-plantation/non-resident-
  proprietor context sources; registered, no links. Decide: link as
  context_for in braintree (and/or weymouth), or record a reviewed
  `context_only` role in the citation map.
- `mendon-proprietors-records-1899` (legacy l.107) — cited by the probate
  §338 block for the post-1667 proprietary correlation; linked in frontier
  only. Either extend l.107's destination to frontier (where it is linked)
  when Thread 4 confirms that is the intended home, or link in braintree.
- `suffolk-probate-index-v2-1895` (legacy l.107 + case-file s1) — see
  material-life below; the discovery/index trail's natural home.
- Dump backlog to assimilate: `F-R4.1` (1646 Braintree meadows petition,
  imaged, Mass Archives 45:11 — distinct from the 1645 petition already in
  `G13-RI-000009`; source registration + image intake required), `F1`
  (Pope 1646 petition record part), `F-R4.6` (Brackett brothers
  Sudbury-Suffolk association).
- The 1645-petition source: fact-sheet n10 and the unit cite it through
  `history-of-weymouth`/`anderson-great-migration-begins-v1-baxter`; lead
  L-191 (firm primary page) remains open — noted, not blocking.

## 4. g13-colonial-frontier-rights (Thread 5)

**Thread 5 done 2026-07-05 (Opus, uncommitted; live rev 21 → 23, snapshot
`g13-context-r000023.ndjson`, validate 0/0, all tiers aligned).** Both frontier
gaps closed by two `editor.commit_change add_source_link` transactions — no new
items (the frontier unit's `G13-RI-000024..000032` identities were all sound).
Frontier now has **zero** source-journey, parity, citation, source-set, and
publication gaps of its own; the 11 residual journey + 6 parity gaps the checker
still reports are all Braintree / material-life / record-coverage (Threads 4/6),
none frontier. Backlog unchanged at 148.

Journey gaps (checker §8.3) — RESOLVED:
- `braintree-records-1640-1793-1886` (legacy l.115 Billerica row) — cited via
  the Shed–Gurney bounding footnote (Daniel Shed answering "for his father
  John Gurney"). **Linked** `context_for` **G13-RI-000029** (the Billerica
  finding): Bates's *Records of the Town of Braintree* (1886) is the primary
  town-record witness to the 1647 Daniel Shed × Mary Gurney marriage and the
  seven Shed births 1647–1658 — the record that makes Daniel John's son-in-law.
  Carried as a second representation alongside the compiled
  `shedd-daniel-shed-genealogy-1920` (already linked), with truthful roles (§7):
  the town record registers the marriage/births, the genealogy compiles the
  descent. Frontier prose `[^shedd]` footnote expanded to cite both; new
  citation-map row added; the source was previously linked in record-coverage
  only.

Parity gaps (checker §8.4) — RESOLVED:
- `nash-historical-sketch-weymouth-1885` — cited in the frontier unit's prose
  (1651/2 Weymouth great lot) but linked to no frontier item (the known §4.1
  defect). **Linked** `context_for` **G13-RI-000031** (the "proprietary right,
  not residence" analysis): Nash Appendix C p.282, great lot no.16, is the
  earliest instance of the proprietary-right-without-residence pattern RI-000031
  synthesizes. The alignment note records it as a cross-unit comparator, not an
  independent frontier record — the great lot's landholding-context home is
  g13-colonial-arrival-chronology and its 1651-52 proprietary-right analysis is
  g13-colonial-weymouth-community (`G13-RI-000045`). Citation-map row updated
  (was prose-cross-link-only).

Manual items — DONE:
- **Boundary preserved.** John's-own-rights vs posthumous widow/descendant
  boundary is intact: the 1662 Mendon allotment acceptance is `G13-RI-000026`
  (ballou, supports) and the post-1667 print-stream chronology friction is the
  `open_question` `G13-RI-000032` (`mendon-proprietors-records-1899`,
  **qualifies** — the record postdates John's 1662/3 death). The post-1667
  "John Gurny + Grisel Gurney" proprietor/widow stream stays backlog for
  g13-family-mendon-descendants (legacy l.55 split row, un-dispositioned by
  design; its frontier sub-parts are assimilated via the more-specific l.115 /
  l.107 rows). No frontier prose or item claims the widow stream.
- **Probate-index coordination (with material-life / Thread 4).**
  `suffolk-probate-index-v2-1895` is the discovery/index trail for Suffolk
  probate Case #338, whose Quinapaug line is the frontier evidence
  `G13-RI-000027`. Its canonical home is **g13-colonial-material-life** (Plan 2b
  §5; §4.2 names material-life as its destination); it rides on legacy l.107
  (destination braintree) and is **not** a frontier-destination input.
  Deliberately **not** linked in frontier — Thread 4 links the index trail in
  material-life. Recorded here as a reviewed cross-unit disposition, not a
  frontier gap (the checker's residual l.107 `suffolk-probate-index-v2-1895`
  journey gap is Thread 4's, against g13-colonial-braintree-community).
- **Chronology / source-alignment friction recorded, not suppressed:** the
  Mendon post-death print-stream chronology (RI-000032 open_question); the
  Quinapaug manuscript-vs-printed-abstract alignment (the "wch we know not" line
  present in `spr-case-338` but absent from the `nehgr-12-suffolk-wills-1858`
  abstract — alignment note on RI-000027); and the Nash great-lot cross-unit
  representation (alignment note on the RI-000031 link).

## 5. g13-colonial-material-life (Thread 4)

Journey gaps routed here jointly with braintree (checker rows list both):
- `sprague-braintree` (occupation statement), `suffolk-probate-index-v2-1895`
  (probate discovery/index trail — the §4.2 example names material-life as
  its destination), `fs-suffolk-probate-1636-1915` (file-papers
  representation of the inventory).
- Create or identify the **canonical occupation finding** (Plan 2b R3):
  connect the direct deed evidence (`G13-RI-000013`), Sprague's published
  statement, the tailoring-tool negative (`G13-RI-000037`), and the husbandry
  interpretation without inflating derivative witnesses.
- Debt/net-estate conclusion and the "single most valuable possession"
  wording corrections — per R3, separately from source-lossless repair.

## 6. g13-colonial-record-coverage (Thread 4 or 6)

Parity gaps (checker §8.4) — the unit's prose cites six sources linked to no
item in the unit: `anderson-great-migration-begins-v1-baxter`,
`massachusetts-bay-records-v1-1853`, `nehgr-12-suffolk-wills-1858`,
`nehgr-62-94`, `spr-case-338-john-gurney-probate-1663`,
`suffolk-deeds-liber-iv-1888`. These read as the unit's six-record-basis
narrative (Anderson's documentary basis for John). Decide per pair: link to
the coverage items, or mark reviewed `cited_role=context_only`/`cross_unit`
in `source-and-citation-map.csv` (the §8.4 exemption designed for exactly
this). Do not leave unmarked.

Backlog routed here (not yet assimilated):
- Bevis/Diligent/Mary-Anne passenger-list negative (supplemental row 1.1 of
  the passenger-list topic; `source_id_missing` — its authorities carry no
  Source IDs; register before journey).
- Dump negatives `F6`, `F8`, `F-R4`, `F-R3.4`, `F-R4.2` (Boston First Church
  zero), `F-R4.10`, `F-R4.11`, `F-R6`; the enumerated fact-sheet-research
  "Negative Results" residue (legacy l.468 row notes).

## 7. Unstaged destinations (blocked until their increments)

Supplemental + legacy backlog now routed and source-complete, by destination:
- **g13-identity-assessment** — case-file s6/s8/s10-identity rows, candidate
  topic files (whole-file + section rows), s11 external_canonical anchor.
- **g13-identity-candidate-b** — case-file s2/s5/s9 rows; Bucks-cluster and
  Hingham-corridor threads (immigration topic).
- **g13-identity-candidate-a / g13-identity-london-candidate** — aylesbury and
  london-draper topic-file rows (note the unregistered
  `ancestry-pcc-wills-1384-1858` placeholder id, friction recorded).
- **g13-origin-age-baptism** — fact-sheet Vitals-Born remainder, case-file
  s4/s5 (s5 carries `nro-pd-86-41` manually; the section itself has no
  Source ID label — friction recorded).
- **g13-origin-migration-network** — case-file s7, immigration-topic
  reception-model and working-interpretation rows, passenger-list topic
  whole-file row.
- **g13-family-wives-marriages / -family-group / -mendon-descendants** —
  fact-sheet Marriage(s)/Children/King-Philip's-War rows, case-file s1 family
  row, dump F1/F2/F2-RESOLVED/F7; Isaac Gurney identification (external
  subject file exists: `research/people/isaac-gurney-scituate-boston.md`).
- **g13-origin-traditions** — Vitals-Buried / Find-a-Grave 1615-tradition rows.
- **g13-research-open-questions / g13-research-source-coverage** — immigration
  lead rows, dump 9.2/9.3, F-R4.7/F-R4.10, legacy Sources-Consulted /
  Negative-Results / leads rows.

## 8. Friction register (14 recorded, none gating)

- `confidence_mismatch;publication_wording` (×3 rows): the **fact sheet n8
  says "roughly a sixty percent probability"; case file v4.3 §11 says ~65%**
  (raised from ~60% in v4.2). The fact sheet lags the case file. Plan 2b does
  not authorize publication edits; this needs a later publication decision.
- `same_record_multiple_representations` (×1): MBCR 1:331 printed court order
  ("John Porter") vs the petition-calendar image read ("Richard Porter") —
  keep both representations with truthful roles (arrival, §1 above).
- `source_id_missing` (×7 rows): braintreema.gov + Britannica footnote
  (immigration topic, no ids); weymouthhistoricalsociety.org footnote (no
  id); case-file s5 in-line-only NRO PD 86/41; Margaret Rovett Ancestry lead
  (id deliberately unassigned pending review); `ancestry-pcc-wills-1384-1858`
  (cited but unregistered); Bevis/Diligent topic (no Source ID labels
  anywhere, ×2 rows).

## 9. Process findings from this pass (for Thread 6 and the record)

1. **Checker extractor fixes (tools/g13_coverage_check.py, tests extended,
   25 pass):** (a) the original regexes matched only singular
   `Source ID: \`x\`` labels — every plural `Source IDs: \`a\`; \`b\``
   citation (the dominant multi-source form on all surfaces) was silently
   missed; (b) colocated markdown footnote-definition blocks inside a span
   credited a block with its neighbors' citations (the Billerica legacy row
   appeared to cite 14 foreign sources). Both fixed; §8.2 results before the
   fix are not comparable.
2. **Legacy map completion (18 rows):** source_ids completed from the frozen
   block parses — 3 dispositioned rows (l.107 +mendon-proprietors,
   +suffolk-probate-index; l.115 +braintree-records, +familysearch-fulltext-
   search, +spr-case-338; l.184 +familysearch-fulltext-search — the §4.2
   bullet-5 omission) and 15 span-verified backlog rows filled from empty.
   All added ids are registered. The three split sub-block rows
   (l.44/55/56, spans unverifiable by design) were left untouched; l.44's
   destination was extended to include the Weymouth unit per its own
   recorded resolution.
3. **Dump map:** zero source_ids mismatches. `S0`'s empty set is correct (the
   scope-map block cites nothing). Nine finding_ids can never anchor under
   §8.2 because the headings differ from the ids (`Input-1..5` vs
   "Input 1 —", `HOB-*` vs "Result"/…, `S0` vs "0. Scope map") — non-gating
   (`extraction_unanchored`) but worth normalizing when those rows are
   dispositioned.
4. **Tenth frozen input:** the Bevis/Diligent/Mary-Anne passenger-list topic
   was added per the §3.3 review rule — it holds the G13 passenger-list
   negative on its own authorities, held nowhere else. It remains a
   cross-cutting reference topic, not a G13 subject file.
5. **Fact-sheet/case-file rows are `extraction_unanchored` by construction**
   (no markdown headings); their source sets were populated with the same
   parser at freeze and are ledger-trusted. Case-file s1 and s10 are split
   into staged-colonial vs family/identity partition rows over the same span
   (partition asserted lossless at generation).
