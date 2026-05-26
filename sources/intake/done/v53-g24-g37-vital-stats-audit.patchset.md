# Intake patchset v53 — G24–G37 vital-stats audit (Norman & junior Norfolk branch)

**Prepared:** 2026-05-23
**Repo:** `allengurney/gurney-genealogy`
**Target branch:** `main`
**Phase:** 1 (preparation). **Status:** Draft patchset for review. **Do NOT apply until approved.**
**Origin:** In-session audit, not from `sources/intake/new/`. No raw intake to archive.

## Scope

Audit of the vital-stats blocks (Born / Died / Occupation / Buried / Marriage(s)) on the fourteen direct-line fact sheets G24 through G37, prepared as input to a FamilySearch.org alignment pass. For each ancestor the audit:

1. Verifies the fact-sheet vitals against the paired research companion, the `data/ancestors v26.json` entry, and `data/familysearch-ids.csv`.
2. Checks the surname variant in the fact-sheet title against contemporary documentary spelling and DG's own pedigree usage.
3. Flags internal inconsistencies between fact sheet, research companion, and JSON.
4. Proposes a targeted edit when warranted.

Out of scope: website mirrors under `site/website/fact-sheets/` (per the requesting task), collateral ancestors, narrative prose unless it touches vitals or surname, and FS structured-table edits (handled in a Phase-2 FS-alignment pass — see Section 13).

## Sources / data referenced

Existing `data/sources.json` entries are used wherever a finding is anchored — no new `data/sources.json` entries are required. The key sourceIds in play:

- `dg-rec-pt1`, `dg-rec-pt2`, `dg-rec-supp` — Daniel Gurney 1845/1848 and Supplement 1858. Anchors for almost every vital-stat claim in this generation range.
- `three-hundred-years-norman-house` — Hannay 1867.
- `pettigrew-collectanea-house-gournay-1871` — Pettigrew 1871.
- `planche-conqueror-companions-1874` — Planché 1874.
- `anderson-yvery-1742-vol-i`, `anderson-yvery-1742` — Anderson 1742, vols I and II.
- `chronicon-beccensis` — *Chronicon Beccensis Abbatiæ*.
- `regesta-rano` — Bates ed., *Regesta Regum Anglo-Normannorum*, 1998.
- `loyd-origins` — Loyd 1951.
- `dudo-historia` — Dudo of Saint-Quentin.
- `liber-niger` — *Liber Niger Scaccarii*.
- `histoire-chronique-normandie-1610`, `dumoulin-histoire-generale-normandie-1631`, `histoire-de-lorraine-calmet`, `wace-roman-de-rou`, `potin-recherches-ville-gournay-1842`, `nrp-recherches-possessions-1852`, `painchault-gaillefontaine-2012`, `delisle-critique-of-dg`.
- `blomefield-norfolk` — Blomefield's *Norfolk*.
- `domesday-1086` — Domesday Book.
- `hop-gurney` — History of Parliament Online.
- `farrer-honors-knights-fees-v3-gurnay-extracts` — Farrer's *Honors and Knights' Fees* vol. 3.

No `sourceId` proposed here. The patchset proposes one open question per ancestor where the available cited material is enough to support the edit but the FS-side update would benefit from one further primary-source check (see Section 14).

## How to read each ancestor section

Each block is structured the same way:

- **Title surname variant** — verdict on the fact-sheet H1 / title's surname form.
- **Vitals current state** — what the fact-sheet vitals block currently says, summarised.
- **Audit findings** — vital-stat issues found, ordered by severity.
- **Proposed edits** — exact find/replace pairs against `fact-sheets/{slug}.md`, with line-number hints.
- **JSON alignment** — corresponding edit to the `data/ancestors v26.json` record where the fact-sheet edit creates a structured-data divergence.
- **Out-of-scope notes** — narrative-side improvements the auditor noticed but is not patching in this pass.

---

## 1. G24 — John de Gournay IV (`fact-sheets/g24-john-de-gournay-iv-fact-sheet.md`)

**Title surname variant — verdict: KEEP.** "John de Gournay IV." Pedigree p. 286 uses "JOHN GURNAY, Junior, IV." in the same entry where the senior is "JOHN DE GURNEY, III." Both *Gurnay* and *Gournay* coexist in DG. The repo's project-wide standardisation on *de Gournay* for the medieval junior-Norfolk generations (G23–G30) is consistent and defensible.

**Vitals current state.** Born c. 1330, Norfolk, son of John III (G25) and Jane de Lexham. Died c. 1370 or later. Lord of Harpley and Hardingham. Buried unknown. Marriage: unknown wife.

**Audit findings.**

1. **No FS PID in `data/familysearch-ids.csv`.** The CSV note for G24 reads "NOT FOUND on FS — FS tree skips this generation between Edmund G23 and John III G25." This is the most consequential audit finding for the FS-alignment outcome: FS believes Edmund G23 is the direct son of John III G25, collapsing G24 out of the line. Resolving this requires submitting a new FS person for John IV, not editing the fact sheet.
2. **First-attestation language is slightly soft.** Vitals say "First attested in a deed of his great-uncle John (Rector of Harpley), 1331." DG-II p. 356 specifies the deed is dated 6 Edward III and names John IV as "Son and heir of John de Gurney and Joan his wife." The current text is correct but adds nothing about Joan/Jane the mother (covered at G25). No edit needed beyond strengthening citation precision.
3. **1354 court entry citation could pin the BL manuscript.** The Highlights section names the source (BL Add. MSS. 8841, fol. 112). The Vitals "Occupation/Status" cell does not. This is acceptable — vitals stay compact — but the Phase-2 FS update for John IV should cite the manuscript identifier in the FS person event note so the FS reviewer sees the primary-source anchor.
4. **Death date is implicit but unstated.** Vitals say "c. 1370 or later. Active as lord of Harpley in 1354 (28 Edw. III). Son Edmund Gournay (G23) died 1387." No primary attestation for a post-1370 act survives. The "c. 1370 or later" framing is correct.

**No edits to the fact sheet proposed.** The Vitals block is internally consistent and consistent with the JSON `G24` record. Findings 1–3 are FS-side or Phase-2 tasks (see Section 13).

**JSON alignment.** None required.

**Out-of-scope notes.** Research companion notes that the Walsingham 1385 charter naming Edmund (G23) falls inside John IV's likely death window; mentioning the c. 1385 *terminus* in a narrative footnote would be a fact-sheet enhancement, not a vitals edit.

---

## 2. G25 — John de Gournay III (`fact-sheets/g25-john-de-gournay-iii-fact-sheet.md`)

**Title surname variant — verdict: KEEP.** "John de Gournay III." DG pedigree p. 286 uses "JOHN DE GURNEY, III." (Gurney spelling) but DG narrative also writes "John de Gournay" interchangeably. Norfolk feodary (BM Add. MSS. 5522, fol. 171) records contemporary 14th-century spelling as "Johannes Gurney" — i.e., *Gurney*. Repo standardisation on *de Gournay* for medieval generations is retained for consistency.

**Vitals current state.** Born c. 1300, Norfolk, son of Sir William III (G26) and Katherine Baconsthorpe. Died c. 1353 or later. Lord of Harpley and associated Norfolk manors. Patron of Harpley living (presented 1332). Buried unknown. Marriage: Jane de Lexham, daughter of Edmund de Lexham, married before 1324 or in that year.

**Audit findings.**

1. **Wife's name carries a documented Jane/Joan variant the vitals do not flag.** DG pedigree p. 286 calls her "JANE, dau. of Edmund de Lexham"; DG-Supp p. 356 refers to "John de Gurney and Joan his wife" — referring to the same woman. Jane and Joan were interchangeable in medieval English usage; the variation is captured in citation n4 but not in the vitals box itself. Recommended: a single-clause parenthetical, no edit to the vitals proper. **No edit proposed.**
2. **JSON ancestor record gives "Jane de Lexham" without surfacing the Joan variant.** This is acceptable in structured data — variants belong in narrative/footnote — but the FS-side update for G25 should record the alternate first-name form on the FS person.
3. **DG-Supp Note 115 connects John III to the Bardolf baronial network (Norfolk feodary, BM Add. MSS. 5522).** The research companion flags this as a finding, observing the 1314 Escheat Roll feoffee role was more probably the Rector John (collateral) than John III. The vitals block correctly stays out of this; the narrative could absorb it but it does not bear on the vital-stats audit.

**No edits to the fact sheet proposed.**

**JSON alignment.** None required.

**Out-of-scope notes.** None affecting vitals.

---

## 3. G26 — Sir William de Gournay III, Knt. (`fact-sheets/g26-sir-william-de-gournay-iii-fact-sheet.md`)

**Title surname variant — verdict: KEEP.** "Sir William de Gournay III." DG pedigree p. 286: "Sir WILLIAM DE GOURNAY, Knt. III." Direct match.

**Vitals current state.** Born c. 1260, Harpley, son of Sir John I (G27). Died c. 1300 or after. Knight; lord of Gurney's manor in Harpley, Hardingham, and Hingham-Gurneys. Buried unknown. Marriage: Katherine, daughter of Edmund Baconsthorpe.

**Audit findings.**

1. **CRITICAL — Children table includes "John de Gurnay II (Rector of Harpley)" as William III's child. This is wrong. The Rector is William III's *brother*, not his son.** DG pedigree p. 286 places Rector John and William III as siblings (both sons of Sir John I, G27). The G27 fact sheet's own children table lists the Rector correctly as John I's son. The G26 children table's own Notes cell even contradicts the row itself ("Wait — correction: the Rector John is William III's brother (son of Sir John I), not his son. See Research Appendix."). The row should be removed entirely; "Wait — correction" prose has no business in a published children table.
2. **JSON `ancestor-g26-sir-william-de-gournay-iii-knt` mirrors the same error.** The `children` array includes a "John de Gournay II" entry whose own notes field reads "Received brother William's estates 1294" — the same internal contradiction (called "brother" inside a "child" row). The JSON entry must be cleaned in the same patch as the fact-sheet edit.
3. **JSON `children` lacks Edmund and William who appear on the fact-sheet table.** Pedigree p. 286 names William III's children as John III, Edmund, and William (the latter two as collaterals). The fact-sheet table includes Edmund and William; the JSON has only the malformed Rector entry. After removing the Rector row, the JSON should add Edmund and William as collateral child entries to match the fact sheet.
4. **Marriage(s) — Katherine identification.** The vitals state Katherine was "daughter of Edmund Baconsthorpe." DG pedigree p. 286 says so. DG-Supp Note 113 (1858, DG's later, more considered view, p. 786) proposes that the same Katherine was actually "daughter or sister of Thomas de Ingoldesthorpe" based on the fine at DG-I p. 325. This finding pertains to W II's wife (G28), but the G26 companion notes that "The G26 companion assigns Katherine Baconsthorpe as the wife of William III (G26), not William II (G28). This may be a different Katherine, or the Baconsthorpe identification may have been displaced from G28 to G26." The G26 fact-sheet should retain the Baconsthorpe identification as DG pedigree's explicit statement, with a citation note acknowledging DG-Supp Note 113 may relocate the Ingoldesthorpe identification to G28's wife. **See G28 Section 5 below for the paired edit.**
5. **Death range.** Vitals: "c. 1300 or after." Roll of Arms entry "John de Gurney — 1245 to 1277" (DG-Supp Note 113) and the 1294 conveyance set William III's last documented act at 1294. Roll-of-Arms dates do not constrain William III's death. No edit.

**Proposed edits.**

**3.1 Fact-sheet children-table cleanup.** Find (lines ~99–115):

```
    <tr>
      <td>John de Gurnay II (Rector of Harpley)</td>
      <td>d. 1332</td>
      <td>Katherine Baconsthorpe</td>
      <td>Wait — correction: the Rector John is William III's brother (son of Sir John I), not his son. See Research Appendix. COLLATERAL relative. <sup class="fn"><a href="#n9" id="ref-9">9</a></sup></td>
    </tr>
    <tr>
      <td>Edmund</td>
      <td>fl. c. 1290s–1320s</td>
      <td>Katherine Baconsthorpe</td>
      <td>Named in DG pedigree. Further details not documented in sources consulted. COLLATERAL. <sup class="fn"><a href="#n10" id="ref-10">10</a></sup></td>
    </tr>
    <tr>
      <td>William</td>
      <td>fl. c. 1290s–1320s</td>
      <td>Katherine Baconsthorpe</td>
      <td>Named in DG pedigree. Further details not documented. COLLATERAL. <sup class="fn"><a href="#n10" id="ref-10b">10</a></sup></td>
    </tr>
```

Replace with:

```
    <tr>
      <td>Edmund de Gurnay</td>
      <td>fl. c. 1290s–1320s</td>
      <td>Katherine Baconsthorpe</td>
      <td>Named in DG pedigree p. 286 alongside John III. Further details not documented in sources consulted. COLLATERAL. <sup class="fn"><a href="#n10" id="ref-10">10</a></sup></td>
    </tr>
    <tr>
      <td>William de Gurnay</td>
      <td>fl. c. 1290s–1320s</td>
      <td>Katherine Baconsthorpe</td>
      <td>Named in DG pedigree p. 286 alongside John III. Further details not documented in sources consulted. COLLATERAL. <sup class="fn"><a href="#n10" id="ref-10b">10</a></sup></td>
    </tr>
```

**3.2 Fact-sheet citation cleanup.** Citation n9 currently footnotes a row that no longer exists. Remove it and renumber if and only if other notes reference it; otherwise leave n9 dormant — the file already has gaps in numbering (e.g., G34 n9b) and an unused n9 will not render as a broken reference because no `<sup>` calls it. **Preferred: leave n9 in place, retitle to "(unused after v53 audit)" or remove the `<li id="n9">` outright; choose at apply time based on validator behaviour.**

**3.3 JSON children-array cleanup.** Find in `data/ancestors v26.json`, in the G26 record (lines 1555–1565 approx.):

```json
    "children": [
      {
        "name": "John de Gournay III",
        "dates": "fl. c. 1300–1353",
        "notes": "G25 in direct line"
      },
      {
        "name": "John de Gournay II",
        "notes": "Priest, Rector and Patron of Harpley; d. 1332. Received brother William's estates 1294. Buried Harpley chancel. COLLATERAL."
      }
    ],
```

Replace with:

```json
    "children": [
      {
        "name": "John de Gournay III",
        "dates": "fl. c. 1300–1353",
        "notes": "G25 in direct line"
      },
      {
        "name": "Edmund de Gurnay",
        "dates": "fl. c. 1290s–1320s",
        "notes": "Named in DG pedigree p. 286 alongside John III. COLLATERAL."
      },
      {
        "name": "William de Gurnay",
        "dates": "fl. c. 1290s–1320s",
        "notes": "Named in DG pedigree p. 286 alongside John III. COLLATERAL."
      }
    ],
```

**3.4 JSON G27 children-array verification.** Confirm `data/ancestors v26.json` G27 record (line 1599 approx.) lists *both* William III (G26 in direct line) and the Rector John as William III's siblings (i.e., both as children of John I). Current state: G27 record's `children` array contains only Sir William III. Recommended addition to the G27 children array:

```json
      {
        "name": "John de Gurnay II",
        "notes": "Priest, Rector and Patron of Harpley; d. 1332. Received brother William III's estates 1294 in exchange for a lifetime annuity; estates descended to nephew John III on Rector's death without heirs. Buried Harpley chancel. COLLATERAL."
      }
```

**JSON alignment.** Sections 3.3 and 3.4 together fix the structural error: Rector John moves from W III's children list to John I's (his correct father).

**Out-of-scope notes.** Narrative paragraphs 3 and 4 already describe the 1294 transfer correctly. No narrative edits needed.

---

## 4. G27 — Sir John de Gournay I, Knt. (`fact-sheets/g27-sir-john-de-gournay-i-fact-sheet.md`)

**Title surname variant — verdict: KEEP.** "Sir John de Gournay I." DG pedigree p. 286: "Sir JOHN GOURNAY, Knt. I." Direct match.

**Vitals current state.** Born c. 1240, Harpley, son of William de Gournay II (G28) and Katherine (prob. Baconsthorpe). Died c. 1280 or later. Knight, lord of Harpley/Hardingham/Hingham. Rebel baron; Crusader. Buried unknown. Marriage: unknown wife.

**Audit findings.**

1. **Children table is correct.** Lists William III (G26) and Rector John (collateral). Matches DG pedigree p. 286.
2. **JSON G27 children-array is incomplete.** Currently lists only William III. Should include Rector John per Section 3.4 above. This is the partner edit to the G26 cleanup.
3. **Roll of Arms date range "1245 to 1277" (DG-Supp Note 113) supports the vitals "fl. c. 1240–1280" range.** No edit needed.
4. **Anderson 1742 vol. II p. 478 — Harpley advowson trial-by-battle in 3 Edw. I (1274/5).** Research companion entry under "Anderson 1742 — Harpley advowson resolved by trial by battle." This is independent 1742 corroboration of John I's Harpley landholding *and* his ecclesiastical-patronage right. The fact sheet's existing Highlights bullets do not mention the advowson resolution. **Recommended: add a sixth highlights bullet, in scope for vitals only as a strengthening of the "Lord of Harpley" status claim.** Proposed text below; apply-time decision whether to insert.

**Proposed edits.**

**4.1 Insert advowson-trial highlights bullet (Section 4 Highlights, after the existing 1257 jury-presentment bullet).** Find the closing `</ul>` of the Highlights list (after line ~75) and insert before it:

```
  <li><strong>Won the Harpley advowson by trial by battle, 3 Edw. I (1274/5).</strong> Anderson, <em>House of Yvery</em> Vol. II (1742), p. 478, records that John "had a Suit with the Prior of Lewes, for the Right of Presentation to the Church of Harpeli ... whereupon a Trial by Battle was appointed, and the said John de Gournay and the Prior came armed into the Field, where the Prior yielded full Seizin of the said Advowson, to the said John de Gournay, for himself and his Successors for ever." The trial-by-battle resolution is striking — judicial combat for advowson disputes was already archaic by 1274/5 — and gave John and his successors the right of presentation to Harpley church that transmitted through G26, G25, G24, G23 Edmund and beyond. <sup class="fn"><a href="#n12" id="ref-12">12</a></sup></li>
```

**4.2 Add citation n12.** At the close of the existing citation list, after the `<li id="n10">` entry (line ~134), insert:

```
  <li id="n12">Anderson, James, <em>Genealogical History of the House of Yvery</em>, Vol. II (London, 1742), p. 478, citing <em>Placita de Banco</em>, Norfolk, 3 Edw. I, "de Ecclesia de Harpeli." Predates Daniel Gurney by 106 years. Source ID: <code>anderson-yvery-1742</code>. <a class="citation-back" href="#ref-12">↩</a></li>
```

**4.3 JSON G27 children-array additions** — see Section 3.4 above.

**4.4 JSON G27 notables field — soften ambiguity about "South Wootton" forfeiture if needed.** Current text reads correctly. No edit.

**JSON alignment.** Section 3.4 is the only JSON change. No vitals JSON change.

**Out-of-scope notes.** The narrative could integrate the trial-by-battle anecdote between paragraphs 2 and 3 (it sits naturally between Lewes/Evesham and the Crusade). Apply-time choice.

---

## 5. G28 — Sir William de Gournay II, Knt. (`fact-sheets/g28-william-de-gournay-ii-fact-sheet.md`)

**Title surname variant — verdict: KEEP.** "William de Gournay II." DG pedigree p. 286: "Sir WILLIAM DE GOURNAY, Knt. II." Direct match.

**Vitals current state.** Born c. 1210, Harpley, son of Matthew de Gournay (G29) and Rose de Burnham. Died c. 1250 or later, attested 1234 and 1243. Knight; lord of Harpley. Buried unknown. Marriage: Katherine ("probably a Baconsthorpe" per DG pedigree).

**Audit findings.**

1. **Marriage(s) — Katherine's identity carries a DG-Supp Note 113 alternative that the fact sheet should surface in the vitals cell.** DG-I pedigree p. 286 says "probably a Baconsthorpe." DG-Supp Note 113 (1858, the later, more considered DG opinion, p. 786) proposes Katherine was "the daughter or sister of Thomas de Ingoldesthorpe" based on the fine at DG-I p. 325. The current Vitals text gives only the Baconsthorpe identification. The Highlights bullet does mention the Ingoldesthorpe alternative briefly, but the Vitals marriage cell — the part FS reviewers will compare against — currently reads as a single-identification claim.

**Proposed edit.** Find (lines ~57–65):

```
  <div class="fact-item fact-item-span-2">
    <div class="fact-label">Marriage(s)</div>
    <div class="fact-value">
      <div class="stacked-records">
        <div><strong>Katherine</strong> — surname uncertain; DG pedigree notes she was "probably a Baconsthorpe." No further details. By Katherine, William was father of Sir John de Gournay I (G27). <sup class="fn"><a href="#n4" id="ref-4">4</a></sup></div>
      </div>
    </div>
  </div>
```

Replace with:

```
  <div class="fact-item fact-item-span-2">
    <div class="fact-label">Marriage(s)</div>
    <div class="fact-value">
      <div class="stacked-records">
        <div><strong>Katherine</strong> — surname unresolved. DG pedigree p. 286 calls her "probably a Baconsthorpe"; DG-Supp Note 113 (1858) — DG's later, more considered view — proposes she was a daughter or sister of Thomas de Ingoldesthorpe, based on the fine at DG-I p. 325. The two identifications are not yet reconciled. By Katherine, William was father of Sir John de Gournay I (G27). <sup class="fn"><a href="#n4" id="ref-4">4</a></sup></div>
      </div>
    </div>
  </div>
```

2. **Vitals "Died" range is consistent.** "c. 1250 or later. Attested living 1234 and 1243 (Norfolk records)." DG-Supp Note 111 places William II as charter witness at Dore Abbey in 1220. This is *earlier* than the 1234/1243 dates already cited and does not change the "Died" estimate but does broaden his documented active span. **Recommended optional secondary edit:** update "Attested living 1234 and 1243 (Norfolk records)" to "Attested living 1220 (Herefordshire), 1234, and 1243 (Norfolk records)." Apply-time choice.

3. **Children table:** John I (G27) + Edmund (Houghton fee 1303) + Thomas (Norfolk fine). Consistent with DG pedigree p. 286 and JSON. No edit needed.

**JSON alignment.** JSON G28 record's `spouses[0].notes` field already captures both candidates correctly: "DG-I pedigree calls her 'probably a Baconsthorpe.' DG-Supp Note 113 (1858) proposes she was an Ingoldesthorpe, based on a fine at DG-I p. 325. The two identifications are unresolved — they may represent the same woman (with the Supplement being DG's later, more considered opinion) or two different Katherines in successive generations (G28 and G26)." The proposed fact-sheet edit brings the fact-sheet vitals in line with the JSON. **No JSON edit required.**

**Out-of-scope notes.** Existing Highlights bullet 3 already covers the Baconsthorpe/Ingoldesthorpe puzzle. The fact-sheet edit above tightens the vitals cell only.

---

## 6. G29 — Sir Matthew de Gournay, Knt. (`fact-sheets/g29-matthew-de-gournay-fact-sheet.md`)

**Title surname variant — verdict: KEEP.** "Matthew de Gournay" / page-heading "Sir Matthew de Gournay." DG pedigree p. 286: "Sir MATTHEW DE GOURNAY, Knight." Direct match.

**Vitals current state.** Born c. 1180, Norfolk. Died "c. 1220 or later. Attested living 1206 (Norfolk fines)." Knight. Lord of Runhall, Swathings, and Harpley. Buried unknown. Marriage: Rose de Burnham (c. 1183, arranged by Hameline Earl Warren).

**Audit findings.**

1. **CRITICAL — Vitals "Died" cell does not reflect DG-Supp Note 109's correction.** DG-Supp Note 109 (p. 780) explicitly corrects DG-I: "I have said that Matthew de Gournay probably did not long survive the year 1206, but this appears to be a mistake; he was living 2nd Henry III (1217), as is shewn by the following extract: Fines 2. Regis Henrici III. Norff. — Mattheus de Gurney dat Domino Regi XX. pro habendo brevi de attingendo, &c., &c., in comitatu Norfolcie de tenemento in Swathing in comitatu Norfolcie." The JSON G29 record already captures the correction: `"dates": "fl. c. 1180 — living 1217"`. The fact-sheet vitals box, the timeline, and Highlights bullet 4 still cite "1206" as the last attestation. The fact sheet must be updated to match the JSON and the cited research-companion correction.

**Proposed edits.**

**6.1 Vitals → Died.** Find (lines ~46–48):

```
  <div class="fact-item">
    <div class="fact-label">Died</div>
    <div class="fact-value">c. 1220 or later. Attested living 1206 (Norfolk fines). <sup class="fn"><a href="#n2" id="ref-2">2</a></sup></div>
  </div>
```

Replace with:

```
  <div class="fact-item">
    <div class="fact-label">Died</div>
    <div class="fact-value">c. 1220 or later. Last attested living 2 Henry III (1217), paying 20 marks to the Crown for a writ of attaint concerning his tenement of Swathings (Fine Roll 2 Henry III, Norfolk), per DG-Supp Note 109 (p. 780) correcting the earlier 1206 estimate. <sup class="fn"><a href="#n2" id="ref-2">2</a></sup></div>
  </div>
```

**6.2 Highlights bullet 4 ("Living 1206…").** Find (lines ~75–76 area):

```
  <li><strong>Living 1206 — survived to see the loss of Normandy.</strong> Matthew was active in the period when King John lost Normandy to Philip Augustus (1204). The Montigny-sur-Andelle Norman holding that his grandfather William I had held in parage presumably passed out of the family's hands at this point, as most Anglo-Norman lords who remained in England forfeited their Norman estates. <sup class="fn"><a href="#n8" id="ref-8">8</a></sup></li>
```

Replace with:

```
  <li><strong>Living 1217 — survived to see the loss of Normandy and beyond.</strong> Matthew was active in the period when King John lost Normandy to Philip Augustus (1204). The Montigny-sur-Andelle Norman holding that his grandfather William I had held in parage presumably passed out of the family's hands at this point, as most Anglo-Norman lords who remained in England forfeited their Norman estates. He outlived King John (d. 1216) and is still found paying the Crown 20 marks for a writ of attaint concerning his Swathings tenement in 2 Henry III (1217). <sup class="fn"><a href="#n8" id="ref-8">8</a></sup></li>
```

**6.3 Citation n2.** Find:

```
  <li id="n2">Living 1206: DG-I pedigree p. 286. Norfolk fines of 27 Hen. III (c. 1243) name his daughter Katherine, suggesting Matthew was by then deceased or elderly. <a class="citation-back" href="#ref-2">↩</a></li>
```

Replace with:

```
  <li id="n2">Last attested 2 Henry III (1217): DG-Supp Note 109 (p. 780), correcting the earlier DG-I "did not long survive 1206" estimate, citing the Fine Roll 2 Henry III, Norfolk: "Mattheus de Gurney dat Domino Regi XX. pro habendo brevi de attingendo, &c., &c., in comitatu Norfolcie de tenemento in Swathing in comitatu Norfolcie." Norfolk fines of 27 Hen. III (c. 1243) name his daughter Katherine, suggesting Matthew was by then deceased. <a class="citation-back" href="#ref-2">↩</a></li>
```

**6.4 Citation n8.** Find:

```
  <li id="n8">Loss of Normandy 1204: DG-I, Introduction, p. ii. Matthew living 1206 per pedigree p. 286. <a class="citation-back" href="#ref-8">↩</a></li>
```

Replace with:

```
  <li id="n8">Loss of Normandy 1204: DG-I, Introduction, p. ii. Matthew last attested 2 Henry III (1217) per DG-Supp Note 109 (p. 780). <a class="citation-back" href="#ref-8">↩</a></li>
```

**6.5 Timeline.** Find:

```
      <tr><td>1206</td><td>Last attested date for Matthew (Norfolk fine record).</td></tr>
      <tr><td>c. 1210–1220</td><td>Probable death. Son William II succeeds.</td></tr>
```

Replace with:

```
      <tr><td>1206</td><td>Living per DG-I pedigree p. 286.</td></tr>
      <tr><td>1217</td><td>Last attested. Pays 20 marks for a writ of attaint concerning his Swathings tenement (Fine Roll 2 Henry III, Norfolk) — DG-Supp Note 109 (p. 780).</td></tr>
      <tr><td>c. 1217–1220</td><td>Probable death. Son William II succeeds.</td></tr>
```

2. **Schema.org block birthDate is "c. 1180."** Consistent. No edit.

3. **No FS PID in `data/familysearch-ids.csv` for G29.** CSV note: "NOT FOUND on FS — FS tree skips Matthew between William II G28 and William I G30." Same FS-side gap as G24. Phase-2 task — see Section 13.

4. **Children table is consistent with DG pedigree p. 286** (William II, Matilda, Katherine, Thomas, Matthew the younger). Rose de Burnham listed as mother for all. No edit needed.

**JSON alignment.** JSON G29 record already carries `"fl. c. 1180 — living 1217"`. The fact-sheet edits above bring the fact sheet into alignment with the JSON — no JSON edits required.

**Out-of-scope notes.** Narrative paragraph 4 references "Matthew lived to see King John lose Normandy to Philip Augustus in 1204" — this remains accurate. Updating the narrative to mention 1217 specifically is optional and falls outside the vitals audit.

---

## 7. G30 — Sir William de Gournay I, Knt. (`fact-sheets/g30-william-de-gournay-i-fact-sheet.md`)

**Title surname variant — verdict: KEEP.** "William de Gournay I" / page-heading "Sir William de Gournay I." DG pedigree p. 286 carries the Knight title for this man.

**Vitals current state.** Born c. 1150, Norfolk. Died c. 1180 or later; living 1167. Knight ("Dominus Willelmus de Gurney"). Lord of Runhall and Swathings; holder of Montigny-sur-Andelle in parage. Buried unknown. Marriage: unknown wife.

**Audit findings.**

1. **Vitals are internally consistent.** Matches DG pedigree p. 286 and the JSON.
2. **DG-Supp Note 105 places a "William de Gournay" as witness to a Henry II charter at Notre Dame du Pré, Rouen.** DG himself flags this "in all probability" as G30. This is mentioned in Highlights bullet 3 ("Probable witness to a charter of Henry II at Rouen") and is appropriately hedged. No edit.
3. **No spouse named in any source.** Vitals cell is correct.
4. **Children table lists Matthew (G29) only.** Consistent with JSON. DG pedigree p. 286 names only Matthew. No edit.

**No edits to the fact sheet proposed.** Vitals are clean.

**JSON alignment.** None required.

**Out-of-scope notes.** Narrative paragraph 4 about the contemporary "Provost of Paris" namesake is appropriately handled per the research companion. The fact sheet correctly distinguishes the two Williams.

---

## 8. G31 — Walter de Gournay (`fact-sheets/g31-walter-de-gournay-fact-sheet.md`)

**Title surname variant — verdict: KEEP.** "Walter de Gournay." DG-I p. 277, p. 286 — direct match. Walter is not a knight in DG's pedigree; no "Sir" prefix in the page heading is correct.

**Vitals current state.** Born c. 1108, England or Normandy; youngest son of Gerard de Gournay (G32) and Edith de Warenne. Died c. 1150–1165 (no record). Lord of manors in Norfolk and Suffolk. Mesne tenant under senior Lords of Gournay and under Manasser de Dampmartin. Buried unknown. Marriage: unknown wife.

**Audit findings.**

1. **Vitals are internally consistent.** Matches the JSON G31 record (`"fl. c. 1108–1154"`) and DG-Supp Note 104's generational arithmetic.
2. **The Walter-as-son-of-Gerard identification is editorial.** Research companion case file at `research/case-files/walter-de-gournay-as-son-of-gerard.md` documents three competing positions: son (DG, Pettigrew, NRP-I, Geni); grandson (Pattou's "possible petit-fils"); unrelated (Richardson SGM 2002, with English-side Suffolk/Essex/Kent feudal evidence). The repo follows DG. Fact-sheet vitals do not need to surface this scholarly dispute, but the Phase-2 FS update for Walter should include the case-file URL as a private note to anticipate FS-reviewer pushback.
3. **Children table lists William I (G30) only.** Consistent.
4. **Schema.org birthDate "c. 1108," birthPlace "Normandy or England" — both consistent with the research companion.**

**No edits to the fact sheet proposed.** Vitals are clean.

**JSON alignment.** None required.

**Out-of-scope notes.** None affecting vitals.

---

## 9. G32 — Gerard de Gournay (`fact-sheets/g32-gerard-de-gournay-fact-sheet.md`)

**Title surname variant — verdict: KEEP.** "Gerard de Gournay." DG-I p. 27, p. 67 — direct match. Orderic Vitalis preserves "*Gornacensis Girardus*"; the Wikipedia article carries "Gerard de Gournay."

**Vitals current state.** Born c. 1040, Gournay-en-Bray. Died before 1104, Palestine. Lord of Gournay-en-Bray; baron; Anglo-Norman landholder (Norfolk); Crusader. Buried unknown. Marriage: Edith de Warenne, daughter of William de Warenne, 1st Earl of Surrey.

**Audit findings.**

1. **Vitals are clean.** Birth, death, marriage, occupation all match the JSON G32 record and the research-companion v2 synthesis.
2. **Children table includes "Gerard (eldest son) — Died *vitae patris*."** JSON G32 record's `children` array does NOT include this Gerard the elder son — it includes only Hugh IV, Walter (G31), and Gundred. **Internal inconsistency between fact sheet and JSON.** DG-I p. 277 pedigree explicitly names "Gerard, eldest son, died vit. pat. in 1104." FMG is silent on this figure. Research companion §3.3 explicitly retains this Gerard in the fact-sheet children table to "resolve the otherwise irreconcilable death-date discrepancy in the secondary literature" (the "1097 Nicaea" date some databases assign to the father).

**Recommended resolution:** the fact sheet's listing is correct per DG's own pedigree; the JSON should be updated to match by adding the elder Gerard as a collateral child entry. This is the safest of two options (the other being to remove Gerard the elder from the fact sheet, which would dissolve the death-date-discrepancy explanation in the narrative).

**Proposed JSON edit.** Add to `data/ancestors v26.json` G32 record's `children` array (after the Walter entry, before Gundred):

```json
      {
        "name": "Gerard (eldest son)",
        "notes": "Died vitae patris in 1104 per DG-I pedigree p. 277. Possibly at the siege of Nicaea (1097) — DG's reading reconciles the conflicting '1097 Nicaea' death dates some secondary sources assign to the father. Not in FMG MedLands. COLLATERAL."
      }
```

3. **JSON G32 record's `notables` field references "Bohemond, who inspected their heraldic badges" — correctly framed as "one of the earliest documented discussions of nascent armorial heraldry," consistent with research-companion language.** No edit.

4. **Edith's second marriage to Dreux de Monceaux is captured in both fact-sheet vitals (Marriage cell) and JSON (`spouses[0].notes`). No edit.**

5. **Amicie de Gournay (Talbot parentage) is intentionally omitted from the fact-sheet children table** per research companion §3.2 — repo position is option (b), first-wife daughter, with the case file at `research/case-files/amicie-de-gournay-talbot-parentage.md` to be created. **No vitals edit; flag the case-file gap below.**

**Proposed edits.**

**9.1 JSON children-array addition** — see above.

**JSON alignment.** Section 9.1.

**Out-of-scope notes.** The Amicie case file is not yet present in `research/case-files/`. Creation of that case file is out of scope for the vitals audit.

---

## 10. G33 — Hugh de Gournay III (`fact-sheets/g33-hugh-de-gournay-iii-fact-sheet.md`)

**Title surname variant — verdict: KEEP.** "Hugh de Gournay III." DG-I p. 25; FMG; Pattou — direct match.

**Vitals current state.** Born c. 1020, Gournay-en-Bray. Died 1110, Abbey of Bec. Lord of Gournay-en-Bray; Norman knight; Domesday landholder; charter witness. Buried Abbey of Bec, Le Bec-Hellouin, Eure. Marriage: Basilia Flaitel.

**Audit findings.**

1. **Vitals reflect the v2 research-companion reconciliation: entered Bec 1080, Prior of Saint-Nicaise de Meulan 1092, died 1110.** Consistent.
2. **CSV `familysearch-ids.csv` still records "G33 ... c. 1020 -- d. c. 1093" — the older DG death year.** The CSV summary needs to be brought in line with the fact sheet and FS PID `MZ68-VKD` updated when the FS-alignment pass runs (Phase 2). Repo-side: edit the CSV row.

**Proposed edits.**

**10.1 `data/familysearch-ids.csv` G33 row.** Find:

```
G33,ancestor,Hugh de Gournay III,c. 1020 -- d. c. 1093,ancestor-g33-hugh-de-gournay-iii,MZ68-VKD,https://www.familysearch.org/tree/person/details/MZ68-VKD,,clean match
```

Replace with:

```
G33,ancestor,Hugh de Gournay III,c. 1020 -- d. 1110,ancestor-g33-hugh-de-gournay-iii,MZ68-VKD,https://www.familysearch.org/tree/person/details/MZ68-VKD,,death year revised from c. 1093 (DG-I) to 1110 (Potin 1842 p. 110; Richardson Royal Ancestry III) per research companion v2 reconciliation: entered Bec 1080, Prior of Saint-Nicaise de Meulan 1092, died Bec 1110. FS still shows c. 1093 pending Phase-2 FS update.
```

3. **Children table lists Gerard (G32) only.** Research-companion §8 entertains Guillaume de Gournay (likely Gerard's brother, not son), Hawise (likely Somerset-cadet line, not Hugh III's daughter), and Adélaïde / Yves II de Beaumont (Depoin's hypothesis, FMG rejects). Fact-sheet correctness: only Gerard belongs. No edit.

4. **Basilea's death — 16 January 1099/1100, *Chronicon Beccensis Abbatiæ*.** Captured in Marriage cell and Timeline. No edit.

**JSON alignment.** JSON G33 record's `dates` field reads "c. 1020 — d. 1110" — consistent with the fact sheet and the proposed CSV update. **No JSON edit required.**

**Out-of-scope notes.** Narrative is fine.

---

## 11. G34 — Hugh de Gournay II (`fact-sheets/g34-hugh-de-gournay-ii-fact-sheet.md`)

**Title surname variant — verdict: KEEP.** "Hugh de Gournay II." DG-I p. 24; Pattou; Wace's *Roman de Rou* "*Hue de Gornai*" — direct match.

**Vitals current state.** Born c. 985, Gournay-en-Bray. Died c. 1074 (Cardiff tradition disputed; most likely a 1074–75 East Anglian engagement during the Earls' Revolt). Lord of Gournay-en-Bray and the Pays de Bray; military commander; ducal charter witness. Buried unknown. Marriage: unknown.

**Audit findings.**

1. **Vitals correctly relocate the "Senex / L'Ancien / Le Vieux / Le Vieil Huon" epithet stack to this generation,** consistent with research-companion §4 and Wace's *Roman de Rou* T. 2.
2. **The "Cardiff" death tradition is appropriately framed as legendary in the Died cell.** Consistent with FMG [892]'s "historical basis of the account is uncertain" verdict.
3. **Children table lists Hugh III (G33) and Néel (Nigel) de Gournay (collateral, Somerset cadet line founder).** Consistent with the research-companion §9 synthesis. **The fact-sheet children table includes Néel even though the JSON G34 record's `children` array lists only Hugh III.** Internal inconsistency between fact sheet and JSON.

**Recommended resolution:** JSON should add Néel as a collateral child entry to match the fact sheet. Néel is independently attested at Domesday 1086 (Barrow-Gurney and Inglishcombe in Somerset, held of the Bishop of Coutances; per Pattou pp. 12–14).

**Proposed JSON edit.** Add to `data/ancestors v26.json` G34 record's `children` array (after Hugh III):

```json
      {
        "name": "Néel (Nigel) de Gournay",
        "dates": "fl. 1066 – after 1086",
        "notes": "Founder of the Somerset cadet line. Held Barrow-Gurney and Inglishcombe (Somerset) of the Bishop of Coutances at Domesday 1086 (Exon registry). Progenitor of Sir Thomas de Gournay (jailer of Edward II, 1327) and Sir Matthew of Crécy/Poitiers/Stoke-sub-Hamdon (b. 1310, d. 26 Sep 1406). Per Pattou Racines Histoire pp. 12-14. COLLATERAL."
      }
```

4. **The "Manassès of Reims as son" question remains open per research-companion §8.** Not adopted into the fact sheet or JSON. No edit.

5. **Vitals "Marriage(s)" cell correctly says unknown.** The FS-tree's "Berthilde de Gerberoy" attribution at PID `LVSH-KBM` is misplaced (per research companion §7); the corresponding FS update should remove that attribution. Phase-2 task.

**Proposed edits.** JSON 11.1 only.

**JSON alignment.** Section 11.1.

**Out-of-scope notes.** None affecting vitals.

---

## 12. G35 — Renaud de Gournay (`fact-sheets/g35-renaud-de-gournay-fact-sheet.md`)

**Title surname variant — verdict: KEEP.** "Renaud de Gournay." DG-I p. 25; FMG `[884]`/`[885]`; NRP-I 1852 p. 77 — direct match.

**Vitals current state.** Born c. 970, Gournay-en-Bray (date estimated). Died dates uncertain; active 989–996 charter. Lord of Gournay-en-Bray and the Pays de Bray. Buried unknown. Marriage: Alberade.

**Audit findings.**

1. **Vitals are clean and consistent with FMG [884]/[885] and NRP-I 1852.**
2. **Children table lists Hugh I (G36), Gautier de la Ferté (collateral, founded La Ferté priory), and Raoul (Radulphus, mort sans postérité per Potin 1842 p. 65 / NRP-I 1852 p. 77).** The JSON G35 record's `children` array lists only Hugh II — wait, this is wrong; **JSON G35 says son is "Hugh de Gournay II" (i.e., G34), not Hugh I (G36).** Re-checking: JSON G35 record's children array (line 2042–2046):

```json
    "children": [
      {
        "name": "Hugh de Gournay II",
        "dates": "c. 985",
        "notes": "G34 in direct line"
      }
    ],
```

But the fact-sheet (line 94) and research-companion §2.1 (FMG [884]) say Renaud's son is **Hugh I** (the fortifier, G36 in repo numbering), and **G36 Hugh I is then father of G34 Hugh II.** No wait — the repo numbering is reversed-chronological: G36 is the *earlier* Hugh (Hugh I, the fortifier); G34 is the *later* Hugh (Hugh II, the Mortemer commander); G35 is Renaud, father of Hugh I. Therefore:

- G37 Eudes → G36 Hugh I → **G35 Renaud** → G34 Hugh II → G33 Hugh III

Wait, that's wrong. Let me re-check the lineage. In the fact-sheet sequence, the higher GNN is the older ancestor:
- G37 Eudes (c. 860)
- G36 Hugh I (c. 920–940)
- G35 Renaud (c. 970)
- G34 Hugh II (c. 985)
- G33 Hugh III (c. 1020)

So Renaud (G35) is *son* of Hugh I (G36) and *father* of Hugh II (G34). That matches the JSON G35 → child "Hugh de Gournay II" (= G34, the *next-younger* ancestor).

It also matches the fact-sheet G35 children table row 1, which reads "Hugh de Gournay I" — but lists "G36 in direct line." **That's the bug.** Renaud's son in the direct line is G34 (Hugh II), not G36 (Hugh I). G36 is Renaud's *father*. The fact-sheet children-table row 1 mislabels the direct-line son.

Re-reading the fact-sheet G35 children-table row 1 (line 93–98):

```
    <tr>
      <td>Hugh de Gournay I</td>
      <td>fl. c. 990s; died perhaps c. 1040</td>
      <td>Alberade</td>
      <td>G36 in direct line. The "fratre Hugone" of the la Ferté foundation charter — confirmed elder brother. The standard repo numbering (G36 = Hugh I, the fortifier) follows DG, FMG, and Potin 1842. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></td>
    </tr>
```

**This is incorrect on the page.** "Hugh I" with "G36 in direct line" places G35's child as his own grandfather. The la Ferté charter's "fratre Hugone" *is* the brother of Gautier de la Ferté, the senior Lord of Gournay at that date — which the repo numbers as G34 (Hugh II), not G36 (Hugh I). The naming convention in DG/FMG is confusing because both Gautier and the brother-Hugues fall under "Hugh-the-fortifier" in some older readings, but the repo's chosen numbering puts Hugh I at G36 (a generation back) and Hugh II at G34 (Renaud's son and the "fratre Hugone").

**Wait — let me cross-check against the research companion explicitly.** G35 research companion §1: "Father: Eudes (G37), per local tradition. (No documented son-of-Eudes attestation; the Hugues I → Renaud chain is partial editorial inference per Potin 1842 p. 89.)" So Renaud's *father* is Hugh I (G36) — i.e., G37 → G36 → G35 → G34 → G33.

G35 research companion §2.1 (FMG MedLands extract): "**HUGUES [I] de Gournay** (-after 989). Gauthier de la Ferté founded the priory of La Ferté en Brai, at the command of 'fratre Hugone', by charter dated to [989/96], which names his father Renaud and his mother Alberade." — i.e., FMG itself uses "HUGUES [I]" for **the son of Renaud who was Gautier's brother.** This is FMG's "Hugues I." But the repo numbers this *same person* as **Hugh II (G34)**, the Mortemer commander.

This is a long-standing FMG-vs-repo numbering offset that the repo has chosen to live with. The fact-sheet children-table row for G35's son uses FMG's "Hugh I" label *plus* the repo's "G36 in direct line" cross-reference — and these two labels point to **different people**. The "Hugh I" name is from FMG; the "G36" tag is from the repo numbering. But G35 → G34 (next younger), not G35 → G36 (next older).

**Resolution:** the row's son must be re-labelled with the repo-numbering identity (Hugh II, G34), not with FMG's "Hugues I." The FMG-vs-repo offset can be flagged in a footnote.

**Proposed edit.**

**12.1 Fact-sheet G35 children-table row 1.** Find (lines 92–98):

```
    <tr>
      <td>Hugh de Gournay I</td>
      <td>fl. c. 990s; died perhaps c. 1040</td>
      <td>Alberade</td>
      <td>G36 in direct line. The "fratre Hugone" of the la Ferté foundation charter — confirmed elder brother. The standard repo numbering (G36 = Hugh I, the fortifier) follows DG, FMG, and Potin 1842. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></td>
    </tr>
```

Replace with:

```
    <tr>
      <td>Hugh de Gournay II</td>
      <td>c. 985 – d. c. 1074</td>
      <td>Alberade</td>
      <td><strong>G34 in direct line.</strong> The "fratre Hugone" of the la Ferté foundation charter [989/96]. In FMG MedLands's separate numbering, this person is labelled "HUGUES [I] de Gournay" — but the repo's project-wide numbering places him as G34 Hugh II, the Mortemer 1054 commander and Hastings 1066 figure. The repo's Hugh I (G36) is a generation earlier. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></td>
    </tr>
```

**12.2 Schema.org / Timeline / Highlights bullet 2 ("Two sons, two legacies") references "Hugh II" already.** Re-check:

- Highlights bullet 2 (line ~73): "Son Hugh II (Renaud's heir as lord of Gournay) became one of the principal Norman commanders at the Battle of Mortemer in 1054…" — correct.
- Narrative paragraph 1 (line ~118–119): "two sons, one of whom inherited the lordship and one of whom directed his energies toward the church" + paragraph 4 (line ~123): "Renaud's lasting contribution to the family story was a son — Hugh II — who would become…" — correct.
- Timeline (line ~168): `<tr><td>c. 985</td><td>Son Hugh II (G34) born.</td></tr>` — correct.

So the only place the misnumbered "Hugh I / G36 in direct line" appears in the G35 fact sheet is the children-table row 1. The rest of the document is consistent. The proposed edit fixes the single bug.

**12.3 JSON G35 children-array.** Already correct (`"name": "Hugh de Gournay II", "dates": "c. 985", "notes": "G34 in direct line"`). No edit.

3. **Vitals are clean.** Birth, marriage to Alberade, La Ferté charter dating window 989–996, all consistent. No vitals-block edit.

**JSON alignment.** None required (JSON already correct).

**Out-of-scope notes.** None affecting vitals.

---

## 13. G36 — Hugh de Gournay I (`fact-sheets/g36-hugh-de-gournay-i-fact-sheet.md`)

**Title surname variant — verdict: KEEP.** "Hugh de Gournay I." DG-I p. 24; Pattou; Potin 1842 — direct match.

**Vitals current state.** Born c. 920–940. Died dates uncertain; active generation c. 960–1000. Lord of Gournay-en-Bray and the Pays de Bray; frontier military lord. Buried unknown. Marriage: unknown.

**Audit findings.**

1. **Vitals are clean.** Internally consistent with the research companion §1.
2. **JSON `lineageStatus` field reads "Limited Historical Record"; fact-sheet narrative paragraph 5 says "classified as **Uncertain** rather than Confirmed"; Highlights bullet 3 says "Uncertain, not Tradition."** Three slightly different labels for the same status. Project convention should standardise. Reading the JSON for sibling generations: G37 is "Minimal historical record" (lowercase) and G36 is "Limited Historical Record" (title case). The JSON casing inconsistency is itself a minor bug but cross-cuts other ancestors and is out of scope for this vitals audit. **No edit proposed in v53.**
3. **Children table lists Renaud (G35) only.** Consistent with JSON and DG/FMG. No edit.
4. **Pattou tentatively names "? Bathilde de Gerberoy (+1059)" at this generation level.** Vitals correctly say "Unknown" — Pattou's `?` markers signal a research-tier candidate, not an adopted fact. No edit.

**No edits to the fact sheet proposed.**

**JSON alignment.** None required.

**Out-of-scope notes.** The Limited / Uncertain / Tradition status-label inconsistency across G35/G36/G37 deserves a future cross-ancestor normalisation pass.

---

## 14. G37 — Eudes (Odon) de Gournay (`fact-sheets/g37-eudes-de-gournay-fact-sheet.md`)

**Title surname variant — verdict: KEEP.** "Eudes (Odon) de Gournay." DG-I p. 23–24; Hannay; Potin 1842 — direct match. The parenthetical "(Odon)" is the standard Frankish rendering of the Norse name.

**Vitals current state.** Born c. 860, Scandinavia (region and parentage unknown). Died after 911, before c. 932. Viking warrior; probable Christian convert after 911. Buried unknown. Marriage: unknown.

**Audit findings.**

1. **Vitals are clean.** The "before c. 932" Rollo-died-after-Eudes constraint from Potin 1842 p. 65 is correctly applied.
2. **JSON `lineageStatus` "Minimal historical record"; fact-sheet narrative paragraph 5 says "classified as **Tradition** rather than Confirmed."** Same label-inconsistency cross-cut as G36. **No edit in v53.**
3. **Children table lists Hugh I (G36) only.** Consistent.
4. **TNG-via-FS attribution of "Marthe de Foucarmont" as Eudes's wife is correctly NOT adopted** per research-companion §1; vitals say "Unknown." No edit.

**No edits to the fact sheet proposed.**

**JSON alignment.** None required.

**Out-of-scope notes.** Same cross-ancestor lineage-status normalisation needed as for G36.

---

## 15. FamilySearch PID gaps and Phase-2 alignment plan

The audit confirms two `data/familysearch-ids.csv` rows that lack FS PIDs:

- **G24 John de Gournay IV** — "NOT FOUND on FS — FS tree skips this generation between Edmund G23 and John III G25."
- **G29 Sir Matthew de Gournay** — "NOT FOUND on FS — FS tree skips Matthew between William II G28 and William I G30."

Both gaps are *substantive* — they mean the global FS tree is currently *missing* two real ancestors, collapsing two-generation gaps into one. Resolving each requires a Phase-2 FS-side action:

1. **Create FS person for John de Gournay IV.** Parents: John III (`9ZH8-98D`, G25) and Jane de Lexham. Vitals: born c. 1330 Norfolk; died c. 1370 or later. Children: Edmund Gournay (`K8MR-TT8`, G23). Primary sources for the FS Sources tab:
   - DG-I p. 279, p. 286 (pedigree)
   - DG-II p. 356 (1331 deed and 1354 manorial court)
   - BL Add. MSS. 8841 fol. 112 (1354 court roll)
2. **Create FS person for Sir Matthew de Gournay, Knt.** Parents: William I (`M4SW-X7R`, G30). Vitals: born c. 1180 Norfolk; living 1217 (Fine Roll 2 Henry III). Spouse: Rose de Burnham (daughter of Reginald de Burnham; given in marriage by Hameline Earl Warren c. 1183). Children: William II (`MVTV-YP3`, G28) + Matilda + Katherine + Thomas + Matthew the younger. Primary sources:
   - DG-I p. 278, p. 286 (pedigree)
   - DG-I Appendix XLIX (p. 308) — c. 1160 deed witness
   - DG-I Appendix LIII — Matthew v. Gilbert de Runhall plea
   - DG-Supp Note 109 (p. 780) — Fine Roll 2 Henry III, Norfolk
   - Harleian MS 970 — Hardingham tithes

A separate set of FS-side cleanups is implied by the audit but should be staged as a Phase-2 patchset, not bundled here:

- **G33 Hugh III** — update FS PID `MZ68-VKD` death year from c. 1093 to 1110.
- **G34 Hugh II** — remove the misplaced "Berthilde de Gerberoy" spouse attribution (the attribution belongs at the G36 level with `?` markers per Pattou, but is not adopted as fact).
- **G36 Hugh I** — verify FS PID `PWPZ-VK1` is *not* conflating Eudes (G37) with Hugh I (G36). The CSV note already flags "FS labels 'Eudes ou Hugues de Gournay en Bray' abt 930-995; FS conflates names; matches repo G36 by descent position." This conflation should be untangled FS-side.
- **G37 Eudes** — FS PID `P8MV-L5C` carries date "abt 890"; repo gives c. 860. The FS date is FS's own estimate and is loose; the repo's "c. 860" is also an estimate. The CSV note flags this. Phase-2 FS edit should align FS to c. 860 (Hannay; Pattou companion p. 1).

The FS-side updates are documented here for the apply session's reference but are **not** the patchset's primary subject — the patchset's primary subject is the fact-sheet and JSON cleanup. The FS-alignment session should be opened as a separate piece of work after this patchset is applied.

---

## 16. Phase-2 application checklist

When applying this patchset:

1. Apply Section 3.1 — G26 children-table cleanup (fact sheet).
2. Apply Section 3.2 — G26 citation n9 cleanup decision (at applier discretion).
3. Apply Section 3.3 — G26 JSON children-array cleanup.
4. Apply Section 3.4 — G27 JSON children-array addition of the Rector John collateral entry.
5. Apply Section 4.1–4.2 — G27 fact-sheet Highlights bullet 4 + citation n12 (Anderson 1742 trial-by-battle).
6. Apply Section 5 — G28 Vitals marriage cell clarification.
7. Apply Section 6.1–6.5 — G29 vitals + Highlights + citations + timeline (DG-Supp Note 109 correction, "Living 1217").
8. Apply Section 9.1 — G32 JSON children-array addition of Gerard the elder son.
9. Apply Section 10.1 — `data/familysearch-ids.csv` G33 death year update.
10. Apply Section 11.1 — G34 JSON children-array addition of Néel.
11. Apply Section 12.1 — G35 fact-sheet children-table row 1 (re-label as Hugh II / G34, with FMG numbering footnote).
12. Re-validate JSON syntax (G26, G27, G32, G34 records mutated).
13. Re-validate fact-sheet HTML (G26, G27, G28, G29, G35 mutated).
14. Confirm no `<sup>`/`<a href="#nN">` references are left dangling after the G26 n9 disposition.
15. Site mirrors under `site/website/fact-sheets/` are out of scope per the requesting task and should NOT be edited in this patch.
16. No `sources/media/` files to move.
17. No `sources/validations/` notes to create — every finding is already supported by an existing cited source.
18. No archive of `sources/intake/new/` — this patchset originates from an in-session audit.

## 17. Unresolved / out-of-scope notes

- The Anselm-letter dating uncertainty (G33 §2 reading (a) vs (b)) is a research-companion-level open question, not a vitals issue.
- The Walter-as-son-of-Gerard (G31) editorial choice remains a conscious adoption of the DG position; the Richardson SGM 2002 alternative position is documented in the research case file and not adopted.
- The Amicie-de-Gournay (Talbot wife) parentage case file (G32 §3.2) has not yet been created in `research/case-files/`. Creation is recommended in a separate pass.
- The G35/G36/G37 lineage-status label inconsistency (`Limited Historical Record` / `Uncertain` / `Tradition` / `Minimal historical record`) should be addressed by a future cross-ancestor normalisation patchset.
- The FMG-vs-repo numbering offset at Renaud-Hugh — FMG calls Renaud's son "Hugues [I]," the repo calls the same person G34 Hugh II — is a long-standing convention and not changed by this patchset. The G35 children-table footnote (Section 12.1) flags the offset for any reader who consults FMG.
- The Manassès-of-Reims-as-son-of-Hugh-II question (G34 §8) remains open and is not adopted.
- The "three Gournays at Hastings" third figure remains open; Néel/Nigel is the strongest candidate per Pattou pp. 12–14 but is documented as a Domesday Somerset lord, not specifically as a Hastings combatant. Out of scope.
