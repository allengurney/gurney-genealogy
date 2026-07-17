# Campaign 2026-07-16 incorporation — plan and wave prompts

**Scope.** Losslessly assimilate the six-round non-G13 online-discovery campaign
(`sources/intake/dump-files/dump-2026-07-16-round{1..6}.md` + sibling file folders) and
the outsourced paleography packets **41–51** (briefs + reports in
`sources/intake/paleography-staging/`, packet 51 returned 2026-07-17 after round 6
closed) into the repo's permanent layers. When this plan is done, the dumps must be
disposable: every finding, negative, extract, image, lead, and method lesson lives in its
long-term home.

**Sources of truth, in order:** (1) the packet **reports** (expert reads) override dump
working reads; (2) the dump text overrides this plan's summaries — quote primary text
from the dump/report, never from this plan; (3) round-6 **§13 per-lead disposition
table** is the lead hand-off; (4) the **evaluation deltas** below are corrections found
by post-campaign reverse-grounding and override the dumps where they conflict.

**Process shape.** Direct edits (not intake patchsets) for everything except fact
sheets, which go through one patchset (Wave 7, stub v126). Intake-layer discipline still
governs direct edits (`continual-improvement.md` "Direct edits still defer to
intake-layer thinking"). This is deliberately lighter than the G13-refactor 3-way-merge
process — one grounded editing pass per cluster, no merge scaffolding.

**Model.** Opus executes all waves. Two sub-analyses are flagged **[FABLE-GRADE]**
(Wave 1's three-witness will reconciliation; Wave 2's Norman generational
reconciliation) — run those waves on Fable if budget allows, otherwise Opus with extra
care and the delta notes below as guardrails.

---

## A. Evaluation deltas (apply on top of the dumps)

Reverse-grounding the dumps against the repo after the campaign surfaced these. Each is
binding on the wave that owns it.

- **E1 — G20 will: reconcile three witnesses; the "NEW son Edmund" claim is wrong.**
  The G20 companion already carries **Blomefield's full English summary of the 1471
  will** (West Barsham parish entry) which the campaign never consulted. Blomefield
  names: sons **John AND Edmund** (Depeden grants) — so Edmund is *not* new, and the
  dumps missed son John entirely; executors = wife Margaret, John Jerningham, **and
  Edmund Bokenham, Esq.**; supervisor **John Heydon** (converges with packet 51);
  Swathings bought of **Catherine Sturmer** (resolves the dump's "Skirmets(?)");
  confessor **John Bernard**, Friar Minor (resolves "Johannem [?]"); Swathings and the
  Norwich tenements **to be sold to William his son for 80 marks** (vs. the dump's
  "sold by executors" — a real conflict to expose, not silently pick); testator styled
  "senior" in Blomefield but **not in the manuscript rubric** (packet 51). Write the
  companion's will treatment as a reconciliation of register images (packet 51) ×
  DG-I pp. 280–282 × Blomefield — convergences stated, conflicts exposed.
- **E2 — Whinburgh = "Winburgh," a Bardolf caput manor, parcel of the barony of
  Gurnay.** CIPM vii.243 (already in
  `research/topics/anderson-yvery-harpetre-gournay-collateral.md`) lists Bardolf's
  caput manors Caister, Cantley, **Winburgh** held "as parcel of the barony of Gurnay."
  The Manor of Whinburgh-with-Members — the L-128 proof engine whose courts governed
  the Rivetts' Garveston copyhold — is that manor. The maternal-kin Rivetts were
  tenants of a manor that was once part of the senior Gournay barony. Connect this in
  the Rivett companion (one topic sentence + crosslink) and the senior-collateral
  topic; it may also help locate the manor's archival fonds (Bardolf-heir successor
  lords).
- **E3 — Swathings is an ancestral manor re-purchased, not just "footprint."** The repo
  documents Swathings (Hardingham) as G30 William de Gournay I's holding (1167,
  ancestors.json + hardingham.md) and the junior line holding it of the Bardolfs by
  knight's fee in 1313/14 (CIPM vii.243), with ex-Gurney "writings … of Gorney" in the
  Fastolf/Hellesdon muniments 1450. G20's will shows he **bought Swathings back from
  Catherine Sturmer late in life** and directed its sale. Assimilate the will's
  Swathings clause into that ~300-year thread (hardingham.md, G20 companion,
  senior-collateral topic) — this is fact-sheet-grade narrative.
- **E4 — The 1435 cleric's benefice is likely already answered in-repo: Rushmere.**
  DG-Supp Note 128 ("Thomas Gurnay presented to Rushmere living 1435") and the Suffolk
  Institute institutions list (Aslak presentation; "parish is the page's subject
  church, to be confirmed") both sit in the repo. If benefice = Rushmere (Suffolk),
  the cleric ≠ the 1454 Great Ellingham decedent, and he **stays live** as a
  clerk-convict candidate. Confirm the Suffolk Institute page's parish (cheap online
  check of the retained/linked volume) before treating the benefice test as gated on
  the Norwich episcopal register. Update L-200's residual routes accordingly.
- **E5 — New hypothesis: John Gurnay "the King's squire" (fl. 1455–63) ?= G20's son
  John.** Round 1 reasoned "no adult direct-line John existed in 1458" — contradicted
  by Blomefield's will summary (son John, Depeden grants, confirmed 1470). A Norfolk
  esquire's son in Henry VI's household, stripped by Yorkist regrants 1462–63, fits
  the CPR arc. Carry as a hypothesis + new lead (test: CPR Henry VI original grants;
  whether "Johanni filio meo" appears in the ultima voluntas — see E11 lead).
- **E6 — Podmer variant gap in the probate-index negative.** The round-2 62679 sweep
  used `podm*` and `p?dm*r` — neither catches the lived Norfolk variants Ancestry
  61045 itself surfaced (**Pitmer, Pytmer, Patmer**). The "no Podmer probate ever"
  negative is unproven for the variant family. New micro-lead: 62679 sweep on
  `p?tm*r`/`patm*`; also broadens the expected spelling of the 1584 bride.
- **E7 — The 1611 marriage venue is unused analysis.** Both Margaret-candidate
  arguments ignore that the wedding was at **Norwich St Martin at Palace**, not
  Garveston/Dereham. Add a short open-question note (service/residence in Norwich?
  bears on both candidates; the register image may carry residence/status styling).
- **E8 — Commission date-check.** Round 1 §2.6 flagged: locate the "T. Gurnay" proposed
  county-commission item's date in repo-held Gairdner vol. IV vs. Jan 1463 (a man in
  prison is an implausible commissioner). Do it during Wave 1 from
  `sources/corpus_supplement/paston-letters-gairdner-vol4-fulltext.txt`.
- **E9 — L-206 residual test from the repo side.** Before re-weighting Mary Gurney,
  check what the repo/Mendon records say about Mendon Mary's own later trail (any
  marriage/death by 1699 would cut against the identification). Note the result either
  way in the mendon-descendants thread.
- **E10 — AALT KB 9 is an online route.** The clerk-convict indictment hunt (KB 9
  Norfolk files 2–3 Edw IV) is free online image-browsing on AALT, not an
  archive-gated pull. L-200 should carry it as an online (laborious) route.
- **E11 — Packet-51 residuals become a HIGH-priority online-style lead** (user
  addendum): final Latin-edition pass on the held Jekkys images — ultima-voluntas
  day/regnal year; **is son John named** (E5); Jernegan/Jernyngham normalization;
  supervisor line recheck (Heydon); godson surname; Margaret's jewels/books clause
  verbatim; Depeden reading. Same treatment for the other open paleo re-stages:
  packet 41 (Whinburgh 1639 leaf tighter crops; "who is Robert Gurney" on the 1648
  leaf), packet 44 continuation (E. Dereham burial headers), packet 45 re-stage
  (adjacent leaves + Latin note). All use images already in hand or cheap pulls.

## B. Housekeeping decisions — committed paleo artifacts (user addendum)

Confirmed state: ~302 MB of packet-51 files are committed, ~294 MB of it the
regenerable `analysis/` enhancement crops; `snippets/packet-41-45-analysis/packet45-ladder/`
adds ~250 MB more of 25–34 MB PNGs. Decisions:

1. **Keep committed:** master das/v2 leaves, final contact sheets, `*-manifest.md`
   files, packet briefs and reports.
2. **Delete from the working tree** (they remain retrievable in git history; no history
   rewrite): the single-band enhancement crops and ladders — packet-51
   `analysis/img36*-{left,right}-*` band/line/ladder PNGs (keep the contact sheets and
   manifests), and the `packet45-ladder/` spread PNGs. These are regenerable from the
   kept masters via the paleography-analysis toolchain.
3. **Going forward:** derivative analysis crops are produced under the packet's
   `_local/` (gitignored) or deleted after the report; only masters + final contact
   sheets + manifests are committed. Wave 6 adds one line to
   `.claude/skills/paleography-analysis/SKILL.md` staging conventions recording this.
4. Returned packet briefs+reports move to `sources/intake/paleography-staging/done/`
   only **after** their findings are assimilated (packet-51 report's own instruction);
   Wave 6 does the move for 41–50, Wave 7 completion releases 51.

## C. Standing rules for every wave

1. **Ground before writing.** Read the destination file in full and run
   `tools/repo_search.py` (venv python) on the subject before adding anything. Read
   only the dump sections named for your wave — not the whole dump set.
2. **Assimilate, don't append.** Merge findings into the existing topical prose with
   several focused, atomic edits (Edit-tool `str_replace` granularity — the user
   reviews via GitHub Desktop diff; avoid whole-paragraph replacement unless the
   paragraph is genuinely superseded). Where a finding corrects an earlier statement,
   revise that statement; do not leave both.
3. **Plain language.** Define lingo on first use (admon = grant of administration;
   ultima voluntas = the "last will" disposing of lands, paired with the testament;
   copyhold, surrender-to-uses, benefit of clergy, mainpernor, etc.). Translate Latin
   quotes inline. Complex fact patterns get a one-sentence plain-English statement
   before the detail.
4. **Connect 1–2-degrees-removed content back to the ancestor** with a topic sentence
   ("X matters for G20 because…"). Position collateral material so it doesn't dilute
   direct-ancestor narrative — collateral clusters go to topic files with a crisp
   summary + crosslink in the companion.
5. **Corpus/corpus_supplement obligations** (sources.md): every extract gets (a) a
   registered `sourceId` in `data/sources.json` (2–4-sentence catalogue annotation, no
   evidence in notes; validation file by default), and (b) its findings promoted into
   the research layer **in full — humans read companions, not supplements, so the
   substance (verbatim key clauses, names, dates) must appear in the companion, not by
   reference**. Corpus files are timeless: no lead handles, no research-status framing.
6. **Citations** per `citations.md`: per-fact footnotes; show the full witness stack on
   multiply-attested facts; repo artifacts are never sources ("Cross-reference, not a
   source"); tertiary sources (Geni etc., in the Lloyd chain) traced or framed as
   collectors.
7. **Uncertainty quantified** ("~55/40/5"), negatives are first-class (carry the
   dumps' negative-ledger rows into the relevant companion/validation), conclusions
   don't outrun evidence, conflicts exposed not reconciled by fiat.
8. **Leads:** update the touched leads via `tools/research_leads.py update/close/add`
   (never rewrite the CSV wholesale); keep Status/Next-action within the CSV's field
   lengths (trim any field you touch to spec); mirror each lead change in the
   companion's lead tail. Lead handles stay out of visible prose (footnotes/HTML
   comments fine).
9. **File moves:** image masters → `sources/media/<sourceId>/` with descriptive names
   and a provenance note; regenerable crops per §B; retained text extracts →
   `sources/corpus_supplement/`. After a wave empties its dump-folder files, leave the
   dump .md in place (Wave 6 archives them).
10. **Disclose** everything done in the turn's summary; finish the wave in one turn.

---

## Wave 1 — Medieval Norfolk / G20 package  [FABLE-GRADE for the will reconciliation]

**Dump inputs:** r4 §2, §7 (NROCAT: Aleyn 19, Jekkys 211, probate census §7.3, deed
layer §7.4); r5 §1 (packets 46–48 triage), §3 (admon working read), §6.1 (NRS 7500);
r6 §1 (packet 49), §2 (Jekkys walk + working transcription), §6 (CCEd), §13 rows
L-30/L-122/L-164/167/L-200. Packet reports 46, 48-A, 49, **51**. Deltas
**E1, E3, E4, E5, E8, E10, E11**. Round-1 §2 (CPR sweeps, clerk-convict re-dating
§2.6–2.7) also lands here.

**Work:**
1. `sources/corpus_supplement/` — author the **Jekkys 211 will-complex extract**
   (testament + ultima voluntas + probate; packet-51 verified readings, uncertain
   readings bracketed; the Blomefield summary quoted as the parallel witness; DG-I
   extracts noted) and the **Aleyn act-book fo. 19v admon extract** (packet-49
   verbatim). Register sources: film-level entries for DGS 008470476 and 008076270
   under/linked to `nro-ncc-wills-registers`; PCC Calthorpe will (Ancestry dbid 5111,
   PROB 11/10 Vox); validations per default.
2. `research/people/g20-thomas-gournay-ii-fact-sheet.research.md` — assimilate the
   full will content per **E1** (three-witness reconciliation), the 1444/45 fine ×
   NRS 7500 corroboration, Margaret-executrix, William's conditional clause (packet
   51's "do not overstate rupture" caveat), sons John/Edmund, Bokenham/Jerningham/
   Heydon circle, Walsingham confraternity + turquoise-ring, Depeden, Swathings (E3),
   St Gregory's; the Wars-of-the-Roses section gains the probate date 27 July 1471
   (packet-51 corrected reading).
3. `research/topics/norwich-gurney-collateral-network.md` — **rewrite the
   clerk-convict section**: date → Christmastide 1462/Jan 1463 (Margaret Paston 19 Jan
   1463 + Playter lost-letter abstract, full quotes incl. the dagger-in-the-privy and
   "what they and other were purposed" conspiracy tail); murder-by-command; corrected
   benefit-of-clergy reasoning; candidate table (G20 / 1435 cleric via **E4 Rushmere**
   / "Thomas junior" senior-styling puzzle — noting the will names no Thomas junior /
   London yoman Thomas Garney); E8 commission date-check result; residual routes incl.
   AALT KB 9 (E10) and Lyhert act books. Extend the **King's-squire John Gurnay**
   entry with the three CPR acts + the **E5 hypothesis**. Add the 15th-c NCC probate
   census (r4 §7.3), freemen-calendar census + Gurnell-1551→1556 resolution (r1 §5.1),
   the NROCAT deed layer (r4 §7.4, as a catalogued-rows inventory), Thomas Gourney of
   Halton → `research/topics/john-gurney-candidate-aylesbury-buckinghamshire.md` or
   `research/places/buckinghamshire.md` (ground first, pick one).
4. Places: `great-ellingham.md` (Thomas + widow Alice 1454 deep anchor; NCC Lawson 151
   = G15 1623 probate row; RQG 180/181), `hardingham.md` (E3 Swathings arc),
   `harpley.md` / `west-barsham.md` (will's twin householder legacies + burial
   choice; Matthew de Gurnay 1202 Harpley fine from r5 §2.5 if not deferred to W2).
5. CPR full-text corpus files (`cpr-edward-iv-*.txt` ×2, `norwich-freemen-*.txt`) →
   `sources/corpus_supplement/` as curated extracts (the relevant entries + index
   negatives verbatim, not the whole 3 MB djvu text — register the printed calendars
   as sources; large raw .txt masters may go to `sources/media/_local/` or be dropped
   once extracts are cut, noting the archive.org identifiers).
6. Media: NCC/Jekkys/PCC-Calthorpe masters → `sources/media/<sourceId>/`.
7. Leads: **close L-30** (after companion+extract land; fact-sheet note deferred to
   W7), **close L-122**, update L-164/L-167 (NRS 7500), update L-200 (per above),
   **add** the E11 Jekkys final-edition lead (HIGH priority, online), the E5
   King's-squire lead, and the E4 Rushmere-confirm micro-lead if not settled in-wave.
   Mirror lead tails in the companions.

## Wave 2 — Norman charter / DEEDS package  [FABLE-GRADE for the generational reconciliation]

**Dump inputs:** r5 §2 (all), r6 §7; files
`deeds-utoronto-charter-extracts-round{5,6}.md`; §13 row L-232. No packet dependency.

**Work:**
1. Move both DEEDS extract files → `sources/corpus_supplement/` (cleaned to
   corpus-timeless standard); register a DEEDS/SCRIPTA source entry (note the
   DEEDS-mirrors-SCRIPTA dating finding: "Assigned" dates are SCRIPTA's editorial
   calls) alongside the existing `jenkins-missenden-cartulary-v1`.
2. **Generational reconciliation (the hard part):** the Bec 1112/13 confirmation
   (Hugh+Basilia → Gerard → Hugh) and the Jumièges 1040 family-group charter
   (Hugh + wife Basilia + son Gerard) must be reconciled against the repo's G34 Hugh
   II / G33 Hugh III / G32 Gerard ordering and against which Hugh Basilia is attached
   to. Expose the tension (charter chain vs. DG-derived interleaved Hugh III; the
   1040 assigned-date looseness) — **do not restructure `ancestors.json` or renumber
   generations in this wave**; write the analysis on the G32/G33/G34 companions (or a
   short topic section) with quantified weights, and raise a lead if a
   structure-changing conclusion looks likely. Basilia upgrades from compiled-pedigree
   to charter-attested either way.
3. Companions G31–G34: Lessingham manor given by Gerard (also `lessingham.md` — the
   charter is primary confirmation of the DG/Blomefield account), London holding of
   Hugh from William I, Fordham church (`fordham.md`), Milesent-wife + Broughton
   dower + double seals (1167, "apud Gornaium"), Hugh IV's sons Gerard & Hugh,
   attestation harvest (compact dated-act tables, verbatim key phrases: "Warnerio suo
   consanguineo," "Hugo senex"), the three pre-1204 King John acts, Matthew de
   Gurnay at Harpley 1202 + William de Gurnai 1198 (→ G30 companion/Harpley; new
   micro-lead "Matthew of Harpley 1202 fit to the G30/G29 household").
4. Leads: update/close-ish L-232 per §13; add the Matthew-1202 micro-lead; note the
   SCRIPTA cross-check as a cheap residual.

## Wave 3 — Rivett / Garveston / Whinburgh package

**Dump inputs:** r1 §3, §5.2–5.4, §6; r2 §1–§3, §5, §8; r3 §1–§3; r4 §5, §8.2; r5 §4;
r6 §1 (packet 50), §3; §13 rows L-128/129/130/131/140. Packet reports 41, 42, 44, 50.
Deltas **E2, E6, E7**.

**Work:**
1. `research/people/rivett-family-of-garveston.md` — the major update: competing
   Margaret candidate written as a live alternative (bp 1 Feb 1577/8 dau. of Robert,
   image+expert confirmed; brother-Richard naming argument; ~55/40/5 weights; E7
   venue note); Elizabeth (Podmer) Rivet burial 23 Oct 1626 + fostering-anchor
   analysis; "christened 1569" corrected (Pagnell, father Thomas — packet 50
   unresolved at image, index-mislocation caveat); Thomas Rivet household; Robert ×
   Agnes 1586 + prior-wife structure; matriarch burial 2 Sep 1584; Sarah 1652;
   Wymondham Francis **split off** (m. Matthy Gray 1620 — rewrite, don't append);
   Gressenhall child table (L-130) + Fay/Faithe 1609; Buxton block-baptism
   disambiguation note; register-survival map (61045 piece = full register images
   1538–1675; Grigson DGS 004115503 blocked-on-FS; three-source map); the
   **Whinburgh-with-Members unlock** as its own section — filmed rolls 1595–1663,
   unfilmed NRS surrenders 1564–1800, the 1639/1648 court leaves (packet-41 cautious
   readings, date-inversion warning, "Robert Gurney" question), the E2 Bardolf/
   barony-of-Gurnay connection, and the surrender-to-uses theory of Francis's missing
   will; Podmer section (Hingham household 1609–23, East Tuddenham Pitmer 1608,
   PCC Leaton 1615 clean negative, E6 variant-gap).
2. Extend `sources/corpus_supplement/rivett-garveston-maternal-family-2026-06.md`
   (or sibling) with the new verbatim register readings and the Mussett will
   transcript; move Garveston/Whinburgh/inventory images → media; register sources
   (Ancestry 61045 collection; Whinburgh rolls film; Grigson transcript catalog
   entry).
3. G13/G14 bearing: one-paragraph updates on the G13 companion/case-file *pointer*
   level only (full treatment stays on the Rivett companion; case files are
   user-initiated — flag, don't edit, the case file unless directed).
4. Leads: L-128 (open; Whinburgh routes + E2 context), L-129 (Podmer/1584-leaf state,
   Ancestry endpoint recipe pointer), L-130 (close per §13), L-131 (open/gated;
   packet-44 soft-negative + continuation-pull lead), L-140 (rewrite from "exhausted"
   to the mapped NRO/BL/CUL archive; spin WLS V/21 Great Ellingham court book into
   its own gated lead — paternal-line unlock); **add**: Whinburgh 1595–1663 image
   walk (P90, online), packet-41/44 re-stage leads (high priority per addendum), E6
   Pitmer/Patmer probate sweep, Grigson/1584-leaf pull, Mattishall
   register-coverage characterisation micro-task.

## Wave 4 — South-Norfolk collateral, Norwich, Maldon package

**Dump inputs:** r1 §4 (Stephen inventory); r2 §4 (Maldon arks); r3 §6.2 + packet 45;
r4 §3 (Maldon pulls), §5.2, §6 (Sion chain, Saxlingham, Ditchingham, Hempnall), §8.1
(CUL); r5 §1 (packet 47), §6.2–6.3; r6 §6 (CCEd census), §8; §13 rows
L-109/152/14/97/124. Packet reports 43, 45, 47.

**Work:**
1. Earsham/Sion chain → `research/people/john-gurney-earsham-will-1638.md`:
   Elizabeth-1663 mother = Sarah (image-confirm pending), the three-generation Sion
   chain [SPEC] with Saxlingham 1636 marriage, Ditchingham household, Esther = Norwich
   1728 wife; L-109 updated.
2. Hempnall enrichment + Saxlingham Thorpe/Nethergate node + Wymondham Gurnay brides
   (Wen/Leake 1617/1628) + Ditchingham → the collateral topic (or L-152 subject file
   if one exists — ground first). Every cluster opens with its
   connection-to-the-line topic sentence (candidate G15-orbit kin; Hempnall→Norwich
   bridge). CCEd census (24 Georgian clerics; post-1540 scope) as a coverage note;
   George-Gurnay-Tacolneston reroute on L-152.
3. Stephen Gurney inventory (packet 43): promote to the Norwich collateral topic
   (cautious wording per report; year unresolved residual); register source; image →
   media; L-124 update.
4. Maldon (packet 47): mark the 1677 ark REJECTED (Franny false positive) in
   `research/people/francis-gurney-of-maldon.md` working notes; promote the Francis
   Gurnay conveyance (Woodward/Pollard, witnesses); Jeffrey Gorney low-confidence
   note; 1676 election-return leaf context; images → media; L-14/L-97 updates.
5. CUL ArchiveSearch harvest (r4 §8.1): Feltwell 1382, Bintry 1393 Gurnay-Calthorp
   co-attestation → collateral/medieval topic; the 1609 VCCt "charges against Gurnay
   and Rush" → note on `research/people/edmund-gurney-divine.research.md` [SPEC] +
   gated lead.
6. Leads: cheap-online-check batch lead for L-84/L-119/L-171 tail; packet-45
   re-stage lead (addendum).

## Wave 5 — Colonial / L-206 Lloyd package (small)

**Dump inputs:** r5 §5, r6 §4; packet 48-C. Delta **E9**.

**Work:** update the `nevis-mary` thread in
`research/people/g13-john-gurney/topics/family/12-mendon-descendants.md` (note: this
file is inside the G13 graph-managed tree — check for graph markers and follow the
g13 revision path `apply-graph-edits.py` if markers govern the block; otherwise edit
directly with the marker preserved): Grisell Lloyd verified (dau. of James Lloyd of
Boston, b. Jamaica ~1685, m. Eastwick 1703), Bristol Henry distinct, image-confirmed
"Mary Gurney the daughter of John Gurney" verbatim (packet 48-C), working weight
~45–55%, E9 result; register PCC Lewis will images source + a Lloyd reference source
(collector-framed); Lewis will images → media; L-206 update (stays open).

## Wave 6 — Leads catalog, skills, validations, memory, cleanup

**Inputs:** every dump's [REC]/[GATED]/ledger sections; §13; §B above.

**Work:**
1. Leads audit: `research_leads.py validate` + `audit`; confirm every §13 disposition
   landed; add any stragglers from round-1 §11 / round-3 §10 / round-4 §11 not created
   in waves 1–5 (Podmer-Hingham census, Gressenhall manorial MDR, CUL Buxton fonds,
   E 179 subsidies / hearth tax / ML bonds ideas as a single "creative datasets"
   parked lead or topic note — judgment call, avoid catalog bloat); trim touched
   fields to spec.
2. Skills/validations updates (each 1–5 lines, targeted):
   `familysearch-fulltext-research` — sequential-awaited das ordering; Ancestry
   full-image endpoint recipe + renderer-freeze caveat; page-body-swap extraction
   trick. `findmypast-record-search` — ancestry.com-not-.co.uk; `page=` param
   non-binding (FMP + Ancestry). `online-discovery-strategy` — the
   **container-resolution lesson** (film-number/fonds lookups out-performed
   name-search all campaign) + MDR-first method for no-will problems.
   `paleography-analysis` — §B.3 derivative-crops _local rule.
   `sources/validations/familysearch-fulltext-search.md` — false positives: Almain
   rivets≠Rivett; Franny→Gurney; Horne→"Gorn"; Jekkys/Aleyn films have no name
   extraction (negatives meaningless). Venue notes: NROCAT = AtoM (URL pattern; can
   502), CCEd post-1540 only, DEEDS mirrors SCRIPTA.
3. Cleanup per §B: delete regenerable crops; move packets 41–50 to `done/`; move the
   six dump .mds + kickoff prompts into `Old dumps/`; delete emptied dump image
   folders; leave packet 51 in staging root until W7 completes.
4. Memory: update `non-g13-campaign-2026-07.md` (assimilation done, pointer to this
   plan) and `MEMORY.md` hook.

## Wave 7 — Fact-sheet patchset (v126)

After waves 1–5 settle, author one intake patchset (rename `stub-v126.md`, create
`stub-v127.md`) covering all fact-sheet edits, per `.claude/rules/fact-sheets.md`
(plain-English contract, story-led, dates-in-years) and `citations.md`:

- **G20** (major): the 1471 will — burial triangle, community legacies, turquoise
  ring/Walsingham confraternity, wife Margaret's textile clause, sons William/John/
  Edmund, the Swathings re-purchase story (E3), probate 27 July 1471; the 1454
  Great Ellingham namesake distinguished.
- **G32/G33/G34**: charter-attested Basilia; Lessingham/London/Fordham; Milesent;
  attestation highlights (subject to the W2 reconciliation's outcome — only
  non-structural facts).
- **G15** (touch): Great Ellingham 170-year Gurnay anchor. **G18** (touch): L-122
  William-forename close. **G13/G14** (touch): only if the Rivett updates change
  published statements (e.g., the "only Margaret of the right age" claim if echoed).
- User reviews the patchset; Phase 2 applies it; then close the L-30 fact-sheet note,
  move packet 51 + this campaign's residue to done/.

---

## Initial prompts

Copy-paste one per session. Each assumes a fresh session on `main`.

### Prompt — Wave 1

> Read AGENTS.md. Execute **Wave 1** of
> `tools/plans/campaign-2026-07-16-incorporation/incorporation-plan-and-prompts.md`
> (read the whole plan header, §A deltas E1/E3/E4/E5/E8/E10/E11, §C standing rules,
> and the Wave-1 block; then read only the dump sections and packet reports it
> names). This is the G20 Thomas Gournay II medieval-Norfolk package: Jekkys-211
> will complex + Aleyn-19 admon into corpus_supplement with sources registered;
> G20 companion assimilation as a three-witness reconciliation (packet-51 register
> read × DG-I × the Blomefield extract already in the companion — E1 controls where
> the dump conflicts); clerk-convict section rewrite; collateral-network additions;
> place-file updates; media moves; lead ops incl. closing L-30 and L-122 and adding
> the new leads specified. Direct edits, atomic str_replace-style, assimilate don't
> append, plain language, complete in this turn.

### Prompt — Wave 2

> Read AGENTS.md. Execute **Wave 2** of
> `tools/plans/campaign-2026-07-16-incorporation/incorporation-plan-and-prompts.md`
> (plan header, §C standing rules, Wave-2 block; dump round-5 §2 and round-6 §7 plus
> the two `deeds-utoronto-charter-extracts-round{5,6}.md` files). This is the Norman
> DEEDS charter package for G31–G34. The generational reconciliation (Bec 1112/13 +
> Jumièges 1040 vs. the repo's Hugh II/Hugh III/Gerard ordering) must be exposed as
> analysis with quantified weights — do NOT restructure ancestors.json or renumber
> generations. Corpus_supplement the extracts, register sources, assimilate into the
> G31–G34 companions and Lessingham/Fordham place files, update L-232, add the
> specified micro-leads. Complete in this turn.

### Prompt — Wave 3

> Read AGENTS.md. Execute **Wave 3** of
> `tools/plans/campaign-2026-07-16-incorporation/incorporation-plan-and-prompts.md`
> (plan header, §A deltas E2/E6/E7, §C standing rules, Wave-3 block; the named dump
> sections and packet reports 41/42/44/50). This is the Rivett/Garveston/Whinburgh
> package centred on `research/people/rivett-family-of-garveston.md` — the competing
> Margaret candidates must read as one current account with ~55/40/5 weights, the
> Wymondham Francis split off, and the Whinburgh-with-Members unlock (including the
> E2 Bardolf barony connection) written up with the manorial proof-architecture.
> Extend the Rivett corpus dossier, register sources, move media, and run the lead
> ops incl. the new Whinburgh-walk P90 lead and the high-priority paleo re-stage
> leads. Complete in this turn.

### Prompt — Wave 4

> Read AGENTS.md. Execute **Wave 4** of
> `tools/plans/campaign-2026-07-16-incorporation/incorporation-plan-and-prompts.md`
> (plan header, §C standing rules, Wave-4 block; the named dump sections and packet
> reports 43/45/47). This is the south-Norfolk collateral + Norwich + Maldon
> package: Earsham Sion chain, Hempnall/Saxlingham/Ditchingham/Wymondham collateral
> nodes (each with a topic sentence tying it back to the line), Stephen Gurney
> inventory, Maldon packet-47 fallout, CUL harvest. Every collateral cluster goes to
> the right topic/subject file with a crisp companion summary — don't let it dilute
> direct-ancestor files. Sources, media, leads per the wave block. Complete in this
> turn.

### Prompt — Wave 5

> Read AGENTS.md. Execute **Wave 5** of
> `tools/plans/campaign-2026-07-16-incorporation/incorporation-plan-and-prompts.md`
> (plan header, §A delta E9, §C standing rules, Wave-5 block; dump round-5 §5,
> round-6 §4, packet report 48-C). Small colonial package: the L-206 Lloyd/Boston
> verification into the mendon-descendants topic (respect the G13 graph-marker
> conventions in that file), source registrations, media, L-206 update. Complete in
> this turn.

### Prompt — Wave 6

> Read AGENTS.md. Execute **Wave 6** of
> `tools/plans/campaign-2026-07-16-incorporation/incorporation-plan-and-prompts.md`
> (plan header, §B housekeeping, §C standing rules, Wave-6 block; skim every dump's
> [REC]/[GATED]/negative-ledger sections and round-6 §13 to verify nothing was
> dropped by waves 1–5). Leads validate/audit + straggler adds + field trims; the
> targeted skill and validation updates; the §B cleanup (delete regenerable crops,
> archive dumps, move packets 41–50 to done/); memory updates. This wave is the
> lossless-completion gate: anything unassimilated gets fixed now or logged
> explicitly. Complete in this turn.

### Prompt — Wave 7

> Read AGENTS.md, `.claude/rules/fact-sheets.md`, `.claude/rules/sources.md`, and
> `.claude/skills/research-intake-prep/SKILL.md`. Execute **Wave 7** of
> `tools/plans/campaign-2026-07-16-incorporation/incorporation-plan-and-prompts.md`:
> author intake patchset v126 (rename the stub; create stub-v127) carrying all
> fact-sheet edits from the assimilated campaign — G20 major (the 1471 will story
> incl. the Swathings re-purchase), G32–G34 charter facts, G15/G18/G13/G14 touches
> as specified. Literal str_replace operations only; fact-sheet prose per the
> plain-English contract. Stop after the patchset is authored for review — do not
> apply Phase 2.
