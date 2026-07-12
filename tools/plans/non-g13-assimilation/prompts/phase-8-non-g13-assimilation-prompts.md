# Phase 8 — non-G13 dump assimilation (round-5 G14–G37 + colonial non-G13 residue)

**Why this exists.** The G13 refactor (Phases 1–7) assimilates only G13 John
Gurney. The non-G13 research — chiefly
`sources/intake/dump-files/dump-2026-07-03-round5-G-14-to-G-37.md` plus the eight
non-G13 rows in the colonial dumps — was handled by **Phase 5 as ledger-only
`routed`**: the dump-findings-map now points each finding at a destination file,
but "no source registrations, graph writes, or topic-prose edits were made"
(coverage README, 2026-07-11 entry). The frozen dump retains the text; the
findings are **not** in the fact-sheet / research / sources / corpus / data
layers. This phase closes that gap — it *assimilates* what Phase 5 only *routed*.

**Relationship to G13 cutover.** Independent. This work touches none of the G13
graph, the frozen fact sheet, or the case file, so it neither blocks nor is
blocked by the Phase-7 cutover gate (`g13_coverage_check.py` zero-backlog, which
`routed` already satisfies). Run it as its own track — ideally before final
"migration complete" sign-off, since Allen's top-line requirement is that all
findings land in their proper sections. It can run in parallel with, or after,
G13 cutover.

**Source of truth.** The frozen dump
`dump-2026-07-03-round5-G-14-to-G-37.md` (§-numbered) is the content authority;
the `dump-findings-map.csv` `routed` rows carry the agreed destinations. Read the
dump §block before writing each finding — quote its verbatim primary text; do not
work from this plan's summaries.

---

## Standing rules — apply to every cluster below

These are direct edits, not an intake patchset, but the intake-layer discipline
still governs (continual-improvement rule, "Direct edits still defer to
intake-layer thinking"). Before editing a destination, read the matching
path-scoped rule (`research-files.md` for people/places/topics; `citations.md`;
`sources.md`; `data-json.md`).

1. **Ground before writing.** Read the destination companion/place/topic **in
   full** and run `repo_search.py` on the subject before adding anything —
   several of these findings may already be partly present from earlier work, and
   the file tells you where a new fact belongs. **Promotions assimilate, they do
   not append**: merge each finding into the relevant existing paragraph so the
   file reads as one current account; where a finding sharpens or corrects an
   existing sentence, revise that sentence rather than bolting on a dated block.
2. **Two obligations per corpus extract** (sources.md): (a) **register** the
   source in `data/sources.json` at the verification level actually examined
   (printed edition / calendar abstract / catalogue), with a 2–4-sentence
   catalogue annotation only — never evidence in the notes; (b) **promote** the
   finding into the research layer. A corpus_supplement file is never committed
   without a registered `sourceId`. Rich primary text (Kings Lynn accounts,
   Paston letters, CIPM/CCR abstracts, Recueil/Rigord Latin) belongs in
   `sources/corpus_supplement/`; the companion cites it.
3. **The repo is never a source.** Every evidence footnote leads with the
   third-party record and a registered `Source ID`. Cross-references to case
   files / fact sheets / other companions open with "Cross-reference, not a
   source."
4. **Citations** (citations.md): every discrete fact carries an explicit source;
   show the full source stack when 3+ witnesses agree; quote to exact
   page/entry/image.
5. **Uncertainty is quantified, not hedged**, and attached to the specific claim.
   Several dump items are explicitly `[SPEC]` — carry them at the weight the dump
   assigns (e.g. "a cadet branch, not a documented tie to the direct line"), and
   never let a network/association datum imply a proven descent.
6. **Confidence-conservation on identity-open items.** Where the dump flags an
   identification as open (the Thomas "clerk convict"; which John holds Swathings
   in 1313/14; which Gurnay married Clemency de Chesney), preserve the open
   question — do not resolve by fiat.
7. **Per-source validation** (sources.md, default-on): each new `sourceId` gets a
   thin `sources/validations/*.md` worksheet unless already covered or a
   single-footnote quotation.
8. **Close-out gates for every session:** bump `data/sources.json`
   `meta.version`; `python tools/lint_source_notes.py` (PASS);
   `python tools/generate_id_indexes.py --write`; confirm no orphaned citations.
   Report per session: files touched, findings assimilated, sources registered,
   corpus extracts written, and anything left un-assimilated with the reason
   (**escalation valve**: a finding whose source will not support the claim, or
   that is already homed, is reported and left — never force-written).
9. **Do not re-open the ledger unless asked.** The dump-findings-map rows are
   already `routed`; this phase writes the *content*. If Allen wants the rows
   re-marked `assimilated` afterward, that is a separate mechanical pass — flag
   it, don't silently rewrite the G13 coverage ledger from this non-G13 track.
10. **Leads are largely done.** Phase 5 updated L-40/43/44/54/151/174/175/178/179
    and added L-195–L-202. When a cluster's finding closes or advances a lead,
    update it with `tools/research_leads.py` — but read the subject companion
    before trusting a lead's Status (leads-csv-status-lags-companions).

Run the clusters **sequentially, one session each** (they share
`data/sources.json`, the source-index files, and `search-variants.json`; parallel
sessions collide). Suggested order W1 → W7; W1/W6 are the cleanest first sessions.

---

## W1 — G23 Edmund Gournay (medieval justice & borough counsel) — Model: Sonnet - DONE

*Self-contained, high narrative value, cleanest starting cluster. Destinations:
`research/people/g23-edmund-gurney-fact-sheet.research.md`,
`research/people/g23-sir-john-gurney-v-related-fact-sheet.research.md`,
`research/places/kings-lynn.md`.*

Assimilate the Edmund G23 dossier from the round-5 dump:
- **§2.3** — Kings Lynn Chamberlains' accounts (HMC 11th Report, App. pt III,
  pp.213–231): 1373–75 civic hospitality + "for his counsel respecting the
  persons imprisoned for the disturbance of the peace." Corpus extract already
  saved: `dump-2026-07-03-images/bho-hmc-vol11-pt3-pp213-231-kings-lynn-chamberlains.txt`.
- **§3.4** — four feoffee/legatee acts: Plaiz will 1385 (10-mark silver cup
  legacy, ranked with knights; Blomefield vol 2 pp159–173); Garboldisham 1375
  (co-feoffee with the Earl of Suffolk; Blomefield vol 1 pp255–274); Oxburgh
  advowson trust for West Dereham abbey (Blomefield vol 6 pp168–197); Egmere fine
  c.1351 (Blomefield vol 9 pp223–226).
- **§4.4** — CCR Edward III crown commissions 1367–77 (vols 12/13/14; index
  styles him "Gourneye, Edmund, justice"): wreck-inquiry, riot/oyer commissions
  alongside CJ Cavendish and Wychingham.
- **§6.3** — the synthesis arc (young conveyancer 1351 → crown commissioner
  1367–74 → Lynn borough counsel 1374–75 → Plaiz legatee 1385 → advowson
  trustee), plus the existing Morley feoffeeship (L-166) already in the companion.
- **§3.5** (residual, → the Sir-John-d.1408 related companion): 1401 Holm Hale
  first court, John Gurnay co-feoffee with the Harpley rector and a Lynn burgess
  (Blomefield vol 6 pp7–14).

Register: HMC 11th Report App. III (Kings Lynn); CCR Edward III vols 12–14 (one
sourceId per printed volume, or a shared calendar sourceId — check what the medieval
companions already cite). Blomefield is almost certainly already registered — verify
the sourceId and reuse it. Corpus_supplement extracts: the Kings Lynn page (move the
saved file in) and the CCR Edmund-commission passages. Update L-174 (Close-Rolls
Edmund test done) per its companion.

---

## W2 — William Gurney IV & V and the Tudor legal-gentry network — Model: Opus - DONE

*The richest single narrative gain. Destinations:
`research/people/g19-william-gurney-iv-fact-sheet.research.md`,
`research/people/g18-william-gurney-v-fact-sheet.research.md`,
`research/places/saxthorpe.md`, `research/topics/norwich-gurney-collateral-network.md`.*

- **§4.1 (MAJOR)** — Paston Letters (Gairdner ed.), the 1472/3 Saxthorpe
  confrontation: William Gurney IV (G19) seizing the Fastolf manor of Saxthorpe
  as Waynflete's/Heydon's man, backed by "young Heydon … in barneys," with Roger
  Townshend proposed as mediator (letters 796, 801 + Gairdner intro pp.272–273).
  This is fact-sheet-grade narrative for G19. Corpus_supplement extract of the two
  letters + the intro passage; the retained texts are
  `dump-2026-07-03-images/pastonlettersad10{1..6}gairuoft.txt`.
- **§2.5** — the CIPM Henry VII feoffee webs: "William Gurnay the younger"
  (proves G18 and G19 acted contemporaneously — the elder/younger dating tool),
  plus the Wynter, Geddyng/Drury, Tendale/Townshend, and Fortescue/Calthorpe
  feoffments (~15 dated acts c.1488–1502). Register CIPM Henry VII (series 2 vols
  1–2). Extend the existing supplement
  `bho-ipm-henry-vii-townshend-gurnay-feoffee.md` (verify its name/path) with the
  saved pages.
- **§5.2** — Ancient Deeds A.7857: Henry Heydon enfeoffing William Gurney of the
  Ormesby/Flegg Heydon estates — primary-deed corroboration of the Gurney–Heydon
  bond that L-122 built from Blomefield (→ G18 companion + the heraldry/collateral
  topic).
- **§6.2** — the Gurney–Heydon–Townshend–Calthorpe quadrangle synthesis
  (1470s–1500s), tying Saxthorpe 1472/3 forward to the 1493 feoffeeships.

Register: Paston Letters (Gairdner, New Complete Library ed., 6 vols — corpus
retention candidate); CIPM Henry VII; Ancient Deeds (TNA C-series descriptive
catalogue). Update L-175 (promote + close), L-122 context, L-163 (Saxthorpe).

---

## W3 — the medieval junior line & the Bardolf key (G25–G28) — Model: Opus

*The heaviest analytically — the tenurial spine. Destinations:
`research/places/hardingham.md` (Swathings), `research/places/harpley.md`,
`research/people/g25-...`, `g26-...`, `g27-...`, `g28-...`,
`research/topics/anderson-yvery-harpetre-gournay-collateral.md`,
`research/places/runhall.md`.*

- **§3.1 (MAJOR — resolves L-178, reframes L-151)** — CIPM vol 7 entry 243
  (Thomas Bardolf IPM): the junior John de Gurnay held Swathings **of** Bardolf by
  knight service, and Bardolf's Caister/Cantley/Winburgh manors are "parcel of the
  barony of Gurnay." The architecture: senior barony forfeited 1204 → Juliana →
  Bardolf; junior line held fragments *of* that barony. This is the primary
  calendar anchor for DG-Supp Note 115. Keep the John-identity (Rector John d.1332
  vs G25 John III) **open** per L-43. → hardingham (Swathings section), g25
  companion, anderson-yvery topic.
- **§3.2** — Ancient Deeds A.2972: "Hugh de Gurnay of Letton" grant to Lewes
  priory (+ Blomefield Letton vol 10 pp231–233). A senior-line forename in
  junior-line Mitford-hundred territory; carry as the cadet-enfeoffment datapoint
  (§6.1), not a resolved descent.
- **§3.8** — Farrer *Honors and Knights' Fees* v3: the Harpley tenure chain
  (1242–3 William II G28; 1275 Hundred Rolls John I G27, Gurney→Calthorpe→Warenne;
  1302–3 John III/Rector John G25) → harpley place + g25/g26/g27/g28; **Olive de
  Gurnay** (Sussex 1291, unplaced); **Clemency de Chesney** marriage (c.1170–1200,
  keep the "which Gurnay?" open — feeds the junior-origin question); **Hawise de
  Gurnai** (†1201 Englishcombe dower → the Somerset collateral, cross-ref W5).
  The full Farrer v3 text is retained
  (`dump-2026-07-03-images/farrer-hkf-v3-fulltext-hathitrust.txt`) — a
  corpus-retention candidate that supersedes the existing
  `sources/corpus_supplement/farrer-honors-knights-fees-v3-gurnay-extracts.txt`;
  decide whether to replace or complement.
- **§6.1** — the synthesis: reframe L-151 from "reconcile two accounts" to
  "identify the cadet enfeoffment." Image-checks (Harpley fee fractions; the p.297
  Warenne-table row) stay flagged as `[GATED]`, not asserted.

Register: CIPM vol 7; Ancient Deeds A-series; Farrer v3 (verify the existing
sourceId; extend for the full text). Update L-178 (CONFIRMED for Swathings),
L-43 (route RESOLVED — record is CIPM vii.243, John-identity open), L-151
(reframed), L-40 (Farrer captured).

---

## W4 — the senior Gournay line & the Norman charters (G32–G37) — Model: Opus

*Destinations: `research/topics/senior-gournay-baron-line-collateral.md`,
`research/people/g32-gerard-...`, `g33-hugh-iii-...`, `g34-hugh-ii-...`,
`research/topics/gournay-tower-la-tour-hue.md`.*

- **§4.6** — Delisle-Berger, *Recueil des actes de Henri II*: the two Hugh de
  Gournay charters NOT in Daniel Gurney (Anchin abbey, 1176 & 1177; the 1177 one
  styles Hugh "by God's permission lord of Gournay" and calls Ralph de Coucy "our
  lord and kinsman" — a primary Gournay–Coucy kinship statement); the Henry II
  confirmation naming Gerard de Gournay + Basilia his mother as joint donors of
  Longueil; the Sigy priory protection naming Hugh twice; the Osbert de Gornai
  "deceased usurer" exchequer entry. Retained: `recueildesactesd0{0,1,2}grea.txt`.
- **§4.7** — Rigord / Guillaume le Breton (Delaborde ed.), the 1202 fall of
  Gournay (Philip Augustus breaching the mill-pond dam to flood the walls;
  Arthur's knighting at Gournay) + the Philippide book-VI locators for L-54.
  Retained: `uvresderigordetd02rigouoft.txt`.

Register: Recueil des actes de Henri II (Delisle-Berger); Œuvres de Rigord et de
Guillaume le Breton (Delaborde, SHF). Both are corpus-retention candidates (full
Latin/French text) — extract the cited passages into corpus_supplement. Update
L-54 (Philippide locators found), and the Anchin-charter follow-up is L-196 (verify).

---

## W5 — the Norfolk collateral map & G17 Anthony — Model: Opus

*Destinations: `research/people/g17-anthony-gurney-fact-sheet.research.md`,
`research/topics/norwich-gurney-collateral-network.md`,
`research/places/somerset-gournay-collateral.md`,
`research/topics/gurney-medieval-soldier-database.md`,
`research/people/gurney-family-cawston-manorial.md`, and possibly new small place
files.*

- **§2.6** — G17 Anthony Gurnay's 1532 Larling settlement (Blomefield vol 1
  pp428–432) → g17 companion. (Larling has no place file; fold into the companion
  or create `research/places/larling.md` — decide by weight.)
- **§2.7 / §3.6.3** — William Gurney gent. of Cawston d.1578 (monument,
  crescent-differenced arms, wife Anne Wayte) + Ancient Deeds B.991 (Wm Gurnay of
  Booton) → the Cawston manorial file + norwich-collateral topic. Feeds L-198.
- **§3.6** — new named Gurneys for the Tudor/Stuart map: George Gurnay rector of
  Tacolneston 1577–c.1618; Thomas Gurnay instituted 1435 (Aslak patronage);
  → norwich-collateral topic.
- **§3.7 / §4.4.5 / §4.5 / §5** — the Somerset/Harptree collateral packet: Sir
  John de Gournay of Harptree (CCR charters, staple release); Matthew de Gournay's
  full CIPM-vol-18 footprint; Anselm/Thomas (CIPM v5); Joan Catecote heiress
  (CIPM vol 16); Richard of Curry Mallet (1509 pardon roll); Hawise †1201
  (cross-ref W3) → somerset-gournay-collateral place + gurney-medieval-soldier
  topic (Matthew). Register the Ancient Deeds abstracts (A.1554 "Master John
  Gurnay, King's squire, of Westminster" 1458; A.7911/A.7196/A.8939 etc.).
- **§3.7 (false-friend)** — Sir Richard Gurney, Lord Mayor of London (the
  dominant 1640s London "Gurney"; systematic false-positive). Phase 4 built the
  false-friends registry; **verify** whether he is already an entry there and add
  if not — do not duplicate.

Update L-76 (Somerset packet), L-198 (Cawston/Booton), L-200/L-201 (Westminster
squire, verify).

---

## W6 — the London Gurneys & the G14/G15 household — Model: Sonnet - DONE

*Cleanest of the late clusters. Destinations:
`research/topics/london-gurney-comparators-1595-1670.md`,
`research/people/g14-francis-gurney-fact-sheet.research.md`,
`research/people/g15-henry-gurney-fact-sheet.research.md`.*

- **§2.1 / §3.6.4 / §6.5** — the Fleet-Street corridor Gurney household:
  Henry Gurney, householder of St Dunstan-in-the-West, 1638, rated 20 marks (Dale,
  *Inhabitants of London in 1638*, pp230–235); William Gurny, St Bride's, 7
  hearths, 1666, and Rich. Gurny, Clerkenwell, 1 hearth, 1666 (London Hearth Tax
  1666) — a distinct middling household in the legal quarter across the G13/G14
  window, none of them Sir Richard the Lord Mayor. → london-gurney-comparators
  topic; cross-reference from g14/g15 (Henry is the lead G14-family forename;
  flag the open question against Francis G14's children by Margaret Rivett).
- **§2.2 (NEG)** — the L-179 negative: Henry the antiquary (G15) does not surface
  by name in BHO's Cecil Papers / CSPD; log the negative on the g15 companion
  (negative results are first-class), not on a source.

Register: Dale, *Inhabitants of London in 1638* (BHO / London Record Society);
London Hearth Tax 1666 (BHO). Update L-179 (BHO-Cecil exhausted for Henry),
L-197/L-199 (Fleet-Street Gurneys — verify).

---

## W7 — corpus / source / data-spine reconciliation — Model: Sonnet

*The closing mechanical session. Destinations: `data/sources.json`,
`sources/corpus_supplement/`, `sources/validations/`, `data/search-variants.json`,
`data/places*.json`, and the eight colonial-dump non-G13 residue rows.*

- **Corpus retention.** Move the retained full-text volumes that W1–W6 relied on
  from `sources/intake/dump-files/dump-2026-07-03-images/` into
  `sources/corpus_supplement/` where multiple sections were used (Farrer v3 full
  text; Paston vols 1–6; CCR Edw III 12–14; Recueil 0/1/2; Rigord vol 2), each
  with its registered sourceId. Single-section BHO page texts already extracted by
  the earlier clusters need no move. Confirm each committed corpus file ties to a
  registered source (sources.md obligation 1).
- **Source-registration audit.** Confirm every sourceId W1–W6 introduced is
  registered with a 2–4-sentence catalogue annotation (no evidence in notes —
  lint_source_notes must PASS), has a thin validation worksheet where required,
  and appears in the id-indexes.
- **search-variants.json** — add the Surney/Garney colonial spelling variants
  (round-5 §F2-RESOLVED residual / Phase-3 carryover — verify they were not
  already added), matching the file's existing shape.
- **places data** — decide whether Swathings, Letton, Larling, Booton, Cawston
  warrant `places.json` / `places_detail.json` entries or stay narrative-only in
  the companions/topics (per data-json.md and the places README).
- **Colonial-dump non-G13 residue** (the 8 rows Phase 5 routed from the colonial
  dumps): F5 → g12 companion corroboration; Input-1 → already substantially in
  `research/places/weymouth-ma.md` (verify, cross-ref); F-R1 → English-line direct
  IPMs (mostly already homed in the wardship material — verify, assimilate any
  gap); F-R4.3 → candidate-others (resolved elimination, likely already homed);
  F-R4.9 / Input-3 / HOB-Result / HOB-Nearby → artifact-retention in the sources
  corpus, no promotion needed. Assimilate only the genuine gaps; report the rest
  as artifact-retention.

Close-out gates as above. Final report: confirm every W1–W6 finding is now
visible in the research layer with a registered source, and state whether any
round-5 §block remains un-assimilated (with the reason).

---

## Coverage checklist (round-5 dump §blocks → cluster)

| §  | Finding | Cluster |
|----|---------|---------|
| 2.1 | Henry Gurney, St Dunstan 1638 | W6 |
| 2.2 | L-179 Cecil/CSPD negative | W6 |
| 2.3 | Edmund G23 — Kings Lynn counsel 1373–75 | W1 |
| 2.5 | CIPM Hen VII feoffee webs; "William the younger" | W2 |
| 2.6 | G17 Anthony — Larling 1532 | W5 |
| 2.7 | Cawston monument 1578 (cadet arms) | W5 |
| 2.8 / 5 | Ancient Deeds index + abstracts | W3 (medieval) / W5 (collateral) |
| 3.1 | CIPM vii.243 — Bardolf/Swathings key | W3 |
| 3.2 | A.2972 Hugh of Letton | W3 |
| 3.3 | Edmund-the-divine Corpus fellowship dossier 1607–8 | *(→ `edmund-gurney-divine.research.md`; fold into W1 or run standalone)* |
| 3.4 | Edmund G23 — four feoffee/legatee acts | W1 |
| 3.5 | 1401 Holm Hale — Sir John d.1408 | W1 |
| 3.6 | new named Gurneys (George, Thomas 1435, London) | W5 / W6 |
| 3.7 | Somerset collaterals; Lord Mayor false-friend | W5 |
| 3.8 | Farrer v3 — Harpley chain, Olive, Clemency, Hawise | W3 |
| 4.1 | Paston Saxthorpe 1472/3 | W2 |
| 4.2 | Thomas "clerk convict" c.1461 (identity open) | W2 *(caution)* |
| 4.3 | smaller Paston Gurney items | W2 |
| 4.4 | CCR Edw III — Edmund commissions; minor Gurnays | W1 / W5 |
| 4.5 | CIPM v5 Somerset (L-43 closure) | W3 / W5 |
| 4.6 | Recueil Henri II — Norman charters | W4 |
| 4.7 | Rigord/Philippide — 1202 fall of Gournay | W4 |

The §3.3 Edmund-the-divine 1607–8 Corpus dossier routes to the collateral
`edmund-gurney-divine.research.md` (the divine is G14 Francis's brother, not G23);
run it inside W1 if convenient or as a short standalone — it is self-contained.
