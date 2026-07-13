# G13 refactor — coverage ledgers (Plan 02 §7 + Plan 2b §6)

Losslessness for the G13 companion/dump refactor (Plan 02 §14) is controlled by
four ledgers and a mechanized checker (§7.4; expanded per Plan 2b §8). This
directory holds the ledgers. It is **tracking metadata, not research** — do not
put findings here.

## Frozen inventory (§8 step 1)

**Cutoff commit ref:** `e782703f` (`g13 graph initial release`, 2026-07-03).

The working tree is **not fully clean** at the cutoff. Exactly one inventory
input has uncommitted working-tree modifications, so the commit ref alone would
omit it; per §8 step 1 the frozen basis for every input is content-addressed by
SHA-256 below (whole-file), and the modified file is frozen at its **working-tree**
content, not its committed blob. Nothing in the current inputs is missed.

| Input | Lines | State at cutoff | Frozen SHA-256 (whole file) |
|---|---|---|---|
| `research/people/_legacy/g13-pre-refactor/g13-john-gurney-fact-sheet.research.md` (legacy companion) | 617 | exact pre-cutover copy; checksum recorded in `_legacy/g13-pre-refactor/BASELINE.md` | `41189a50f694ca749e40f3ae5cd870e8423949ad6d8de4bc50dabaf2fccef364` |
| `sources/intake/dump-files/dump-2026-07-01-g13-colonial-massbay-campaign.md` | 567 | **modified (uncommitted, +4/−3)** — frozen at working tree | `4ed9820e7684e6a58a27ccfcc6394e7c89d96abf13be0ba04b4ace74ff12b10d` |
| `sources/intake/dump-files/dump-2026-07-01-g13-colonial-round2-ward-county.md` | 466 | clean @ e782703f | `65e8ada86ad661adf2c38a8505eecbf2fd6dc1ada3eb9e4bd06aef2df120e481` |
| `sources/intake/dump-files/dump-2026-07-02-g13-colonial-round3-english-network.md` | 197 | clean @ e782703f | `1c5db3e2e16c19aa6a7731af2110189a97d901a5fb6813f657edce1812e56b57` |
| `sources/intake/dump-files/dump-2026-07-02-g13-colonial-round3-part2.md` | 264 | clean @ e782703f | `6a1810a25e29a3f4c2a182bb1dfb96afbdd6c4091ab8e42e72960b35b7d377d1` |
| `sources/intake/dump-files/dump-2026-07-02-g13-colonial-round4-arch45-and-network.md` | 681 | clean @ e782703f | `50c82ad7c00cdaa3670386b7f0b826aa2de95347e4a8646c078b70cb98744c80` |
| `sources/intake/dump-files/dump-2026-07-03-round5-G-14-to-G-37.md` | 322 | clean @ e782703f | `f5f8caa1aa02f224623c0da8c27900c9e97000957b31442f75c4f3093fc39408` |
| `sources/intake/dump-files/hobart-journal-pages-8-24-transcription.md` | 1173 | clean @ e782703f | `9afa515fd9e9723efed10586c210063f5835c5491aad48fe68f53b4eb1db3120` |

Dump image folders (`dump-2026-07-01-images/`, `dump-2026-07-02-images/`,
`dump-2026-07-03-images/`, `dump-2026-07-02-g13-colonial-round4-files/`) are
source-artifact candidates (§8, §9), not narrative findings; they are handled at
source-review time and are not enumerated as finding rows.

Material added to any input **after** this cutoff is queued for a later round,
not folded into this refactor (§8 step 1). If the modified massbay dump is later
committed, re-freeze that row against the new blob.

The live companion and dump are **not** touched by this work.

## Plan 2b frozen inventory — supplemental surfaces (§6.3, Thread 2, 2026-07-04)

**Plan 2b cutoff commit ref:** `c9006ce6` (`misc pdf`, 2026-07-04). This is a
**separate cutoff** from the original §8 step 1 freeze above; the supplemental
surfaces were not part of that freeze and are not back-dated into it. The
working tree was **clean** for every input below at this cutoff, so the commit
blob and the working-tree content coincide.

The seven G13/John topic files are the **explicit §3.3 enumeration** (the glob
`research/topics/g13-john-gurney-*.md` matches only one of them). Word-count
sanity check: the seven total 23,989 words by `wc -w` against Plan 02 §2's
"~24,269 words" — within counter tolerance, no missing file. The §3.3 scan of
`research/topics/` and its README found one additional file whose review showed
a G13-specific source relationship held nowhere else: the Bevis/Diligent/
Mary-Anne passenger-list topic carries the first-class negative *"no John
Gurney variant appears on any of these lists"* on its own source stack
(Banks's *Planters of the Commonwealth*, Drake). It is frozen as a tenth input
with minimal rows; the file itself remains a cross-cutting method/collection
topic, not a G13 subject file. No other `research/topics/` file has G13 John
Gurney as its subject.

| Input | Kind | Lines | State at cutoff | Frozen SHA-256 (whole file) |
|---|---|---|---|---|
| `fact-sheets/g13-john-gurney-fact-sheet.md` | fact_sheet | 176 | re-frozen at G13 cutover 2026-07-13; approved about-65% publication edit (prior c9006ce6 baseline retained in legacy baseline metadata) | `259606fdb742996cc3032d84140d33193c0d1070c71667c750f68d5f30c8133f` |
| `research/case-files/john-gurney-case-file-v4.md` | case_file | 1007 | clean @ c9006ce6 | `4b392b34ade271228d2da6e3dba292ca1f28cf6580b019da0d6bf9d7ee3c7e93` |
| `research/topics/g13-john-gurney-immigration-by-association.md` | existing_topic | 163 | clean @ c9006ce6 | `daf224d41e1b385202162f5a472f24dda17a367890c7e6d07141218e527ebaa5` |
| `research/topics/john-gurney-candidate-aylesbury-buckinghamshire.md` | existing_topic | 62 | clean @ c9006ce6 | `a57093b226c3be5b1a26aca4d253aad873251544270e0c913be42985be20a7a7` |
| `research/topics/john-gurney-candidate-berkhamsted-hertfordshire.md` | existing_topic | 21 | clean @ c9006ce6 | `48a4d4e36fc88f4aa097c6007982eaa11c598ea9999c4f6e874eeb9d2d41cdd2` |
| `research/topics/john-gurney-candidate-ackworth-yorkshire.md` | existing_topic | 28 | clean @ c9006ce6 | `88bbb4de83959d3bf0e3c17a65e4651ffeaf4d7f7f8893fee51f56c1587a93f0` |
| `research/topics/john-gurney-candidate-earsham-norfolk.md` | existing_topic | 57 | clean @ c9006ce6 | `1905273978b19bee38774544b1077078c24efd36f682e8ddb6679960047e1aa3` |
| `research/topics/john-gurney-candidate-london-draper.md` | existing_topic | 293 | clean @ c9006ce6 | `2a80a373358da920c66a5514efabbaad4591b77a2400a2c6d70ab0c60a1f3c87` |
| `research/topics/john-gurney-candidate-others.md` | existing_topic | 236 | clean @ c9006ce6 | `870960a6ca81f6de2ad4e22ef29ff691f821895b5218185f22d83cf25ff6e16c` |
| `research/topics/massachusetts-bay-passenger-lists-bevis-diligent-mary-anne.md` | existing_topic | 993 | clean @ c9006ce6 | `ec305d20d1fb84edc5a0eb34df0d35bfb42a81341f636b4c813507f390ff9c49` |

Material added to any of these files **after** this cutoff is queued for a
later round, not folded into this refactor. The map **never authorizes edits
to any origin surface** (Plan 2b §6.2).

Block-anchoring notes for the checker (§8.2 tiers): the fact sheet has **no
markdown headings** (pure HTML sections), so every fact-sheet row is
`extraction_unanchored` by construction — its `source_ids` were populated
mechanically at freeze (same parser, HTML footnote definitions resolved) and
are trusted from the ledger. The case file uses HTML `<h2 id="sN">` section
headings (also unanchorable) with markdown `###` subsections; rows are cut at
the h2-section level, so case-file rows are likewise `extraction_unanchored`.
Two mixed-scope case-file sections (s1, s10) are each split into two rows over
the same span — a staged-colonial-scope row and a family/identity-scope row —
whose `source_ids` partition the section's mechanically parsed set (asserted
lossless at generation). Topic-file rows anchor on real markdown headings and
gate normally; whole-file rows anchored on the `#` title deliberately carry
the file's complete parsed source set.

State at this freeze: **six topics staged** (arrival-chronology, weymouth,
braintree, frontier-rights, material-life, record-coverage; items
`G13-RI-000001..000042`), graph snapshot revision 17 — superseding the
three-topic coverage snapshot recorded above at the §8 freeze.

Thread 2 also mechanically completed `legacy-companion-map.csv` `source_ids`
against the frozen block parses (18 rows; three dispositioned rows had
genuinely missing cited ids, including the §4.2 `familysearch-fulltext-search`
omission on the full-text-campaign row) and audited the dump map (zero
mismatches; nine finding_ids are heading-unanchorable, non-gating). The
destination-by-destination handoff for Threads 3–5 is
[`plan2b-remediation-manifest.md`](plan2b-remediation-manifest.md). Checker
state at handoff: `input_inventory_gaps=0`, `input_source_set_gaps=0`,
`source_journey_gaps=12`, `topic_graph_source_gaps=7`,
`publication_mapping_gaps=0`, `friction_needs_decision=0` (+14 recorded,
non-gating), backlog 148.

**Plan 2b Thread 6 closeout (2026-07-05, Opus).** The five-topic remediation is
complete. Threads 3 (arrival + Weymouth, rev 21) and 5 (frontier, rev 23) had
landed; **Thread 4 (Braintree + material-life) had not been run** — the audit
found its 11 source-journey gaps and record-coverage's 6 prose↔graph parity gaps
still open. Thread 6 closed both: (a) retagged the six record-coverage
cross-links `context_for → cross_unit` so the §8.4 exemption applies (ledger
only); (b) executed Thread 4 — new canonical occupation finding
**G13-RI-000047** ("a tailor by trade, a husbandman by economy") + marker
**G13-PM-000029** in Braintree, and six source links to existing items
(familysearch-fulltext-search→RI-000013 Liber V registry copy; adams-history +
adams-genesis→RI-000011 non-resident Tyng proprietorship; sprague-braintree→
RI-000047; fs-suffolk-probate + suffolk-probate-index→RI-000033), plus the
l.107 destination extended to material-life + frontier. Live DB **rev 35**,
snapshot `g13-context-r000035.ndjson`, validate 0/0, all tiers aligned. **All
Plan 2b categories now zero** (`source_journey_gaps=0`,
`topic_graph_source_gaps=0`); backlog unchanged at 148 (the unauthored
family/origin/identity/research-state topics — the expected whole-refactor
`RESULT: FAIL`). All six colonial topics carry `coverageStatus:
increment-complete`. **GO** for resuming normal G3 authoring.

**G3 record-coverage revision (2026-07-10, Opus).** Revised the already-committed
`g13-colonial-record-coverage` unit to assimilate the colony-level negative
catalogue it had left in backlog. New items `G13-RI-000179..000183` (Boston-silence
synthesis + First Church, Boston civil/deed/vital, FamilySearch manuscript-sweep,
and Providence negatives) with marker `G13-PM-000111`; existing `G13-RI-000041`
gained the primary Massachusetts Bay Records witness for the never-freeman negative.
Dump rows F-R4.2 and F8 → assimilated; F6, F11, F-R4, F-R3.4, F-R4.11, F-R6 → partial
(sibling facets — the Samuel×Shapley descendant record, the Hingham Hobart-journal
lead, the Providence Garnet false-friend — routed to `g13-family-mendon-descendants`,
`g13-origin-migration-network`, and the unbuilt false-friends registry, and left in
backlog there). Two new sources registered (`boston-record-commissioners-ninth-report-1883`,
`early-records-town-of-providence`); `csm-39-boston-first-church` (Phase 1) is now
assimilated. Live DB **rev 167**, snapshot `g13-context-r000167.ndjson`, validate 0/0,
all tiers aligned. All Plan 2b per-increment categories zero for the touched topic;
whole-refactor backlog 77 (down from 148), the expected mid-refactor `RESULT: FAIL`.
The unit stays `increment-complete` (the partial rows' sibling facets remain backlog).

**G3 Braintree revision (2026-07-10, Opus).** Revised the already-committed
`g13-colonial-braintree-community` unit for two backlog rows. **F-R4.1 assimilated**:
the imaged 1646 Braintree meadows petition (Mass. Archives vol. 45 p. 11 + answer slip
p. 11a, DGS 007702989 imgs 1403/1402) is new source_evidence `G13-RI-000184` with marker
`G13-PM-000112`, SUPPORTS the residence finding RI-000008 (strong) and the community-standing
finding RI-000016 (moderate); cited at folio/image level. It is kept explicitly distinct from
the still-unlocated 1645 plantation petition (open_question RI-000017, L-191). The Phase-1
source `massachusetts-archives-vol-45-lands-1622-1726` is now assimilated; lead L-194 advanced
(append-status-note). **F-R4.6 re-routed** off `g13-colonial-braintree-community` to
`g13-origin-migration-network` and left backlog there: the Brackett-brothers→Sudbury→Gurdon
reading is a compiled-level network suggestion about origin, not a documented tie to John, and
the Gurdon-Winthrop material already lives in `g13-origin-wardship-network`; the documented
Braintree co-action with the Bracketts is carried in RI-000016 and the new RI-000184. Live DB
**rev 169**, snapshot `g13-context-r000169.ndjson`, validate 0/0, all tiers aligned. All Plan 2b
per-increment categories zero for the touched topic (source_journey_gaps=0, 0 deferred,
topic_graph_source_gaps=0); whole-refactor backlog **76** (down from 77 — F-R4.1 assimilated;
F-R4.6 stays backlog, re-homed from Braintree to migration-network, not closed). The unit stays
`increment-complete`.

**G4 out-of-scope dump routing (2026-07-11).** Routed the 35 dump-map rows that are not G13
John Gurney's and never belonged to this refactor: `F5` (G12 corroboration), `Input-1`
(county-framing methods guidance), `Input-3` (Hobart-journal transcript artifact), `F-R1`
(direct-ancestor Chancery IPMs, English-line), `F-R4.3` (Abel Gourney, London, resolved
same-name elimination), `F-R4.9` (Threnodia 1606 EEBO artifact), `HOB-Result`/`HOB-Nearby`
(Hobart-journal negative-context artifacts), and the 27 round-5 rows (`2.1`-`2.9`, `2.x`,
`3.1`-`3.9`, `4.1`-`4.8`) in `dump-2026-07-03-round5-G-14-to-G-37.md`, all G14-G37
English/collateral material with no G13 bearing on inspection. All 35 dispositioned `routed`
to their correct external subject/place files (extending S0's already-`routed` pattern), with
`source_ids` filled where a cited source is already registered and left empty (flagged
`source_registration_required=yes`) where it is not — no source registrations, graph writes,
or topic-prose edits were made in this pass. Nine existing leads updated (L-40, L-43, L-44,
L-54, L-151, L-174, L-175, L-178, L-179) and eight new leads added (L-195-L-202) for
genuinely actionable follow-ups with no prior tracker. Dump findings map now **83/83
dispositioned, 0 backlog**; checker gates hold (`input_source_set_gaps=0`,
`topic_graph_source_gaps=1` unchanged/pre-existing), whole-refactor backlog **27** (down from
62 — exactly the 35 routed rows). The frozen dump blocks retain the full text; nothing is
lost, only routed.

**FIRST ALL-GREEN RUN — coverage cutover gate met (2026-07-12, Opus).** The
legacy-companion and supplemental-surfaces ledgers were driven to **zero
un-dispositioned rows** and every §8 source-lossless category to zero.
`g13_coverage_check.py` now returns `RESULT: PASS` (0 gating) and
`SOURCE-LOSSLESS: PASS` — legacy 41/41, dump 83/83, supplemental 60/60
dispositioned; 0 citation gaps, 0 unregistered, 0 input-source-set gaps, 0
source-journey gaps, 0 prose↔graph parity gaps, 0 publication-mapping gaps, 0
friction-needing-decision. Live DB **rev 194**, snapshot `g13-context-r000194.ndjson`,
validate 0 errors. Work this session: (a) `sync-sources` cleared the stale
source_registry validate error; (b) the `alumni-cantabrigienses-venn` migration
parity gap retagged `cross_unit`, and the four `g13-colonial-record-coverage`
citation-map warns cleared by labelling the `[^land]` footnote's cross-unit ids;
(c) 20 legacy + supplemental backlog rows closed by disposition/routing (sources
already journeying, empty-set synthesized, external-canonical, or collectively-
carried context per the collective-set exception on case-file §8/§10); (d) five
authoring closures: the Newgate de-conflation's two residual witnesses linked to
g13-origin-traditions RI-000100; two new g13-research-source-coverage negatives
RI-000198 (Hotten/ROLLCO port-emigration & livery search) and RI-000199 (English
probate + Norfolk parish/marriage search) homing nine previously-unjourneyed
lead-search sources; and thompson→migration RI-000091, fs-england-marriages→other-
eliminations RI-000117. (e) **dump-ledger vocabulary + journey activation (2026-07-13, rev 194->214).**
The 17 dump rows carrying the non-vocabulary values 'synthesized'/'partial'/
'mentions' were retagged to `assimilated` — the correct dump-ledger word, which
(unlike those legacy-ledger values) the checker DOES journey-check. This was not
cosmetic: it activated source-journey verification on 17 rows that had been
skipping it. All 17 pass — every listed source was first confirmed item-linked in
its destination unit; three rows (F3-VERBATIM, F-R3, F-R6) had their
`destination_type` set to `topic` so the journey check would run on their graph
home; F11's destination was corrected to where its content actually landed
(record-coverage + migration, not arrival); and F-R4.5 (Jenner-in-Venn), the one
row that was a bare prose mention with its source unlinked, was homed by a
`mentions` source link of `alumni-cantabrigienses-venn` to the migration
weak-lever analysis RI-000079 it already elaborates. Dump ledger now 83/83
`assimilated`/`routed` with 0 vocabulary warnings and 0 journey gaps.

**The cutover gate's coverage conditions are now met** for all three ledgers.
CORRECTION (2026-07-13) to an earlier draft of this note: the ~40 `routed` dump
rows (non-G13 subjects — G12, G15-G34, medieval Gournay lines, place files, the
false-friends registry) are NOT merely "directed but unpromoted." Phase 5 routed
them ledger-only, but **Phase 8 (W1-W7, tools/plans/non-g13-assimilation/, all
marked DONE) subsequently ASSIMILATED that content into the destination
companions/places/topics and registered the sources** (spot-checked: g23-edmund
carries the Kings Lynn 1373-75 material; g19 the Townshend/Saxthorpe network). The
dump-map rows were deliberately left `routed` (not re-marked `assimilated`) per
Phase-8 rule #9 — re-marking is an explicit separate mechanical pass, not a silent
rewrite of this ledger from the non-G13 track. So `routed` here now means
routed-AND-homed-elsewhere.

Residual, genuinely-not-ingestable-now items are each tracked as a lead (per Allen's
directive): F-R4.9 Threnodia 1606 EEBO OCR unusable -> new lead **L-205**; F-R4.8
Rotuli Hundredorum scan-only -> **L-44**; Hobart journal pp.1652-1679 -> **L-188**.
Two "research-done-but-source-not-registered" chads are likewise lead-tracked:
Aspinwall Notarial Records + Lechford Note-Book (dump F6, swept-negative, cited at
IA-identifier level in record-coverage [^bostonclasses]) -> **L-193**; the John
Lewis of Nevis will Mary-Gurney identification (l.144 residual, graph open_question
RI-000135) -> new lead **L-206**.

## The four ledgers

All ledgers use `topicId`, never numbered shorthand (§5) — a file rename cannot
silently change a destination.

- **`legacy-companion-map.csv`** (§7.1) — one row per legacy heading or
  independently-meaningful block, with a per-block `content_hash` (16-hex SHA-256
  over the exact frozen line span). Two shared sections ("Land and property
  records", "Community and probate records") are split into sub-blocks because
  their material fans out to more than one destination plus backlog. `disposition`
  is one of the §7.1 set (`moved`, `synthesized`, `retained_in_hub`,
  `external-canonical`, `superseded-but-preserved`, `duplicate`, `needs-decision`);
  an **empty `disposition` is the backlog signal** the checker reports.
- **`dump-findings-map.csv`** (§7.2) — one row per dump finding / input / negative
  ledger across all frozen dump files. `destination_path` carries the provisional
  §9 routing where known; `disposition` is empty until a finding is actually
  assimilated per topic.
- **`source-and-citation-map.csv`** (§7.3) — one row per (staged unit × cited
  `sourceId`): registration status in `data/sources.json`, cited role, exact-locator
  availability, media/corpus artifact path, and the findings each source supports /
  contradicts / qualifies. No staged unit may be approved with an untracked citation
  gap (§7.3). A `cited_role` of `context_only` or `cross_unit` marks a reviewed
  prose citation deliberately carried without an item link in that unit — it
  exempts the pair from the Plan 2b §8.4 prose↔graph parity gate.
- **`supplemental-surfaces-map.csv`** (Plan 2b §6.2) — one row per independently
  meaningful assertion/block of the *supplemental* source-bearing inputs: the
  published fact sheet, the case file, and the seven pre-existing G13/John topic
  files (enumerated in Plan 2b §3.3). Each row carries the block's complete
  `source_ids` set, a Plan 2b disposition (`incorporated`, `summarized`,
  `publication_only`, `external_canonical`, `superseded_but_preserved`,
  `duplicate_but_preserved`, `routed_elsewhere`, `needs_decision`), and optional
  `friction` values (§6.2 controlled set). `origin_anchor` is the block's heading
  text — the checker uses it to locate and mechanically re-parse the block's
  cited sources. Header established by Plan 2b Thread 1 (2026-07-04); populated
  by Thread 2 (freeze + inventory, same day): 60 rows across the ten frozen
  surfaces, 26 dispositioned at freeze. The map never authorizes edits to any
  origin surface.

The dump map also carries a Plan 2b `source_ids` column (empty until a finding
is dispositioned): a dump finding cannot be dispositioned without recording its
complete source set (Plan 2b §6.1).

## What is dispositioned so far

Three topics are authored (Phase P and two Phase G3 increments), all colonial:
`g13-colonial-arrival-chronology` (items `G13-RI-000001..000007`),
`g13-colonial-braintree-community` (items `G13-RI-000008..000017`), and
`g13-colonial-weymouth-community` (items `G13-RI-000018..000023`). All were
synthesized from **legacy-companion** blocks; the July dump-campaign findings feed
topics not yet authored (wives/marriages, mendon-descendants, origin, identity,
record-coverage), so the dump rows remain backlog apart from the §0 county-scope
map, routed (not assimilated) to the Weymouth place file.

Ongoing rows are added per topic by the `g13-graph-authoring` skill (§11); this
pass establishes the structure and the first real rows only.

The `g13-colonial-braintree-community` topic carries five Plan 2a prose evidence
markers (`G13-PM-000001..000005`); the `g13-colonial-weymouth-community` topic was
authored with four more (`G13-PM-000006..000009`) in the same batch as its items.
Markers are a passage→item mapping held in SQLite (schema v3); they cite no new
sources and assimilate no new legacy/dump blocks, so they add no ledger rows and
leave the citation-gap count at zero.

## Coverage snapshot (computed at freeze)

| Ledger | Rows | Dispositioned | Coverage | Backlog |
|---|---|---|---|---|
| Legacy companion map | 41 | 8 | 19.5% | 33 |
| Dump findings map | 82 | 0 | 0.0% | 82 |
| Source & citation map | 14 (2 units) | — | 0 untracked citation gaps | — |

- **Legacy:** the 8 dispositioned rows are the colonial blocks the two authored
  topics assimilated (2 → arrival-chronology, 6 → braintree-community). The 33
  backlog rows are the family/origin/identity/research-state material and the
  Billerica/Mendon/estate remainders of the two split colonial sections.
- **Dump:** 82 findings frozen, none yet assimilated into the two authored topics.
- **Citation gaps:** all 14 cited `sourceId` values across both staged units are
  registered in `data/sources.json`; zero untracked gaps.

### One losslessness flag — RESOLVED (2026-07-04)

The legacy "Land and property records — Weymouth" block also cites the manuscript
`weymouth-land-grants-book-ms` (primary corroboration of the three original East/Mill
Field grants), which the `g13-colonial-arrival-chronology` unit carried only through
Nash (secondary). Deliberate decision taken with the Weymouth-community increment:
the manuscript is now carried into the graph as `source_evidence` **G13-RI-000019**
in `g13-colonial-weymouth-community` (its natural home — the manuscript primarily
evidences John's inhabitant standing), supporting the standing finding G13-RI-000018,
which in turn `DEPENDS_ON` the arrival finding G13-RI-000006. The aligned manuscript
source is preserved per §10; the legacy-map row is updated to RESOLVED.

### Pre-existing G13 topic files not in the frozen inventory (flag, 2026-07-04)

The frozen inventory (§8 step 1) covers the legacy companion and the dump files
only. It does **not** include the seven pre-existing `research/topics/g13-john-gurney-*.md`
topic files that Plan 02 §2 counts (~24,269 words) and §9 routes. One of them —
`research/topics/g13-john-gurney-immigration-by-association.md` — materially
**overlaps the authored colonial topics**: its Weymouth-reception section already
carries, in fuller form, the inhabitant-standing, Rev. Jenner credit-tie, and
Ludden/Porter/King associate-network findings now authored into
`g13-colonial-weymouth-community`, and its land-timing section overlaps
`g13-colonial-arrival-chronology`.

Per Plan 02 §9 this topic **subdivides**; it does not move as-is: Weymouth/Braintree
associate networks → `g13-colonial-weymouth-community` / `g13-colonial-braintree-community`;
migration/reception network classes → `g13-origin-migration-network` and the surviving
(rehomed) immigration/migration-network unit; the Candidate-B / Hingham-corridor /
Bucks-as-origin threads → `g13-identity-candidate-b` and the origin-network units. The
Weymouth-community increment reconciles its slice in prose (cross-referencing the
immigration topic as the fuller migration/reception home) but does not dissolve it.

**Follow-up before cutover:** add the seven G13 topic files to the frozen inventory as
a fourth input class (or an extension of the legacy-companion ledger) and disposition
each, so the checker tracks their assimilation like the companion and dumps. Until then
their content sits outside the checker's coverage denominator, and a topic authored from
the companion (as this one was) can silently duplicate a topic-file treatment — exactly
what happened here before the prose reconciliation.
