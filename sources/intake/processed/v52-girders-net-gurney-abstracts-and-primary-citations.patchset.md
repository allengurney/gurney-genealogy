# Intake patchset v52 — girders.net Gurney abstracts and adjacent primary citations

**Prepared:** 2026-05-22
**Repo:** `allengurney/gurney-genealogy`
**Target branch:** `main`
**Intake source:** `sources/intake/processed/Ready/V52-next-stepsv5.md`

**Status:** DRAFT — awaiting Phase 2 application.

## Posture

The intake batch is a single markdown file pasting eleven short abstracts. The first eight (Henry GURNAY d.1443; John GURNAY d.1409; Thomas GURNAY d.1454 of Great Ellingham; Thomas GURNAY fl.1471 of Harpley; John GURNEY fl.1423 of Little Walsingham; Richard GURNEY fl.1404; Richard GOURNEY fl.1483 of Aylesbury; Matthew GOURNAY fl.1399) come from the same compilation site, **girders.net** (https://www.girders.net/). Each entry reproduces a primary-source citation (NRO will register, C.F.R., C.P.R., TNA A2A, or medievalgenealogy.org.uk fine abstract). Three additional records follow: a TNA Discovery entry (DL 42/2/33/5) for a Richard I grant witnessed by Hugh de Gurnai; an extract from Bardsley's surname dictionary; and a Calendar of Inquisitions Post Mortem vol. 12 entry for Thomas de Sancto Omero naming Robert Gurnay among the Mulbarton/Keteringham tenants.

girders.net is treated as a tertiary index, not a citable source on its own. The primary citation it reproduces is used in each footnote, with girders.net acknowledged in the new source entry as the discovery vector and abstract host.

## Triage summary

| # | Item | Outcome | Destination |
|---|---|---|---|
| 1 | Henry GURNAY (d.1443), Norwich, NRO Doke 17 | PROMOTE | `research/places/norwich.md` (collateral note) |
| 2 | John GURNAY (d.1409), C.F.R. 1405-13 p.123 | PROMOTE | `research/people/g21-thomas-gournay-i-fact-sheet.research.md` (Sir John d.1408 escheat corroboration) |
| 3 | Thomas GURNAY (d.1454), Great Ellingham, NRO Aleyn 19 | PROMOTE | `research/places/great-ellingham.md` (pre-Lovell Gurney flag) |
| 4 | Thomas GURNAY (fl.1471), Harpley, NCC Jekkys 211 | PROMOTE | `research/people/g20-thomas-gournay-ii-fact-sheet.research.md` (NCC register citation for the 1471 will) |
| 5 | John GURNEY (fl.1423), Little Walsingham, Goldsmith, C.P.R. 1422-29 p.26 | PROMOTE | `research/places/norfolk.md` (collateral note) |
| 6 | Richard GURNEY (fl.1404), Stone/Hartwell, Bucks, CP 25/1/21/112 | PROMOTE | `research/places/buckinghamshire.md` (later-Bucks Gurney record) |
| 7 | Richard GOURNEY (fl.1483), Aylesbury, TNA A2A 705:349/12946/495200 | PROMOTE | `research/places/buckinghamshire.md` (later-Bucks Gurney record) |
| 8 | Matthew GOURNAY (fl.1399), Somerset, C.P.R./C.F.R. | PROMOTE | `research/places/somerset-gournay-collateral.md` (extends Sir Matthew section) |
| 9 | Hugh de Gurnai, Richard I grant, TNA DL 42/2/33/5 | PROMOTE | `research/topics/senior-gournay-baron-line-collateral.md` (Hugues V) |
| 10 | Bardsley, *Dictionary of English & Welsh Surnames*, p. 344 | PARTIAL PROMOTE | `research/places/norfolk.md` (only the 1438 Hethel rector item); etymology/Hastings tradition REJECT (already covered) |
| 11 | IPM Thomas de Sancto Omero 1366 (Robert Gurnay tenants) | PROMOTE | `research/people/g22-robert-gournay-fact-sheet.research.md` (contextual note: contemporary non-gentry Robert Gurnays) |

## New `data/sources.json` entries

Add the following ten entries. Insertion is alphabetic by sourceId only where existing convention already does so; otherwise append at the end of the `sources` object.

```json
"girders-net-medieval-gurney-abstracts": {
  "shortTitle": "girders.net Medieval Gurney Abstracts",
  "citation": "\"Medieval Gurneys,\" girders.net, accessed 22 May 2026, https://www.girders.net/.",
  "archive": "girders.net (private compilation site)",
  "url": "https://www.girders.net/",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": null,
  "notes": "Compilation site of short Gurney/Gurnay/Gournay abstracts each citing an underlying primary source (NRO will register, Calendar of Fine Rolls, Calendar of Patent Rolls, TNA A2A, medievalgenealogy.org.uk fine abstract). Used here as the discovery vector for a v52 batch of eight Norfolk/Bucks/Somerset abstracts. Cite the underlying primary source in footnotes; cite girders.net only when the underlying record has not been re-examined."
},
"cfr-henry-iv-1405-13": {
  "shortTitle": "Calendar of Fine Rolls, Henry IV, 1405-13",
  "citation": "Calendar of the Fine Rolls Preserved in the Public Record Office, Henry IV, A.D. 1405-1413, vol. 13 (London: HMSO, 1934).",
  "archive": "TNA / HMSO printed calendar; widely available in research libraries and via HathiTrust",
  "url": null,
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": null,
  "notes": "Henry IV Fine Rolls calendar volume. Used in v52 for the 16 Feb 1409 escheator order on the lands of John Gurnay (= collateral Sir John Gurney d. 4 Dec 1408), p. 123."
},
"cpr-henry-iv-1399-1401": {
  "shortTitle": "Calendar of Patent Rolls, Henry IV, 1399-1401",
  "citation": "Calendar of the Patent Rolls Preserved in the Public Record Office, Henry IV, A.D. 1399-1401, vol. 1 (London: HMSO, 1903).",
  "archive": "TNA / HMSO printed calendar; HathiTrust and Internet Archive copies",
  "url": null,
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": null,
  "notes": "Henry IV Patent Rolls calendar volume. Used in v52 for Sir Matthew de Gournay's Somerset commissions of array (18 Dec 1399 p. 210, 25 Feb 1400 p. 267, 5 Jul 1400 p. 564) and his 300 marks/year Exchequer grant (12 Mar 1400 p. 208)."
},
"cpr-henry-vi-1422-29": {
  "shortTitle": "Calendar of Patent Rolls, Henry VI, 1422-29",
  "citation": "Calendar of the Patent Rolls Preserved in the Public Record Office, Henry VI, A.D. 1422-1429, vol. 1 (London: HMSO, 1901).",
  "archive": "TNA / HMSO printed calendar; HathiTrust and Internet Archive copies",
  "url": null,
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": null,
  "notes": "Henry VI Patent Rolls calendar volume. Used in v52 for the 1 Feb 1423 pardon of John Gurney, goldsmith of Little Walsingham, for non-appearance touching a plea of debt of 100s. by John Langholm (p. 26)."
},
"nro-ncc-wills-registers": {
  "shortTitle": "Norfolk Record Office, NCC Will Registers",
  "citation": "Norfolk Record Office, Norwich Consistory Court (NCC) will registers, including registers Doke (mid-15th c.), Aleyn (mid-15th c.), and Jekkys (later 15th c.).",
  "archive": "Norfolk Record Office, The Archive Centre, Martineau Lane, Norwich",
  "url": "http://nrocat.norfolk.gov.uk",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": null,
  "notes": "Umbrella entry for the NCC will and administration registers held at the Norfolk Record Office. v52 uses three entries discovered via girders.net: NCC will register Doke, 17 (administration of Henry Gurnay of Norwich, 1443); NCC will register Aleyn, 19 (administration of Thomas Gurnay of Great Ellingham, 1454); NCC will register Jekkys, 211 (will of Thomas Gurnay of Harpley, 1471 = G20 Thomas Gournay II). The Jekkys 211 will is the primary register copy of the will whose contents DG-I pp. 280-282 already extracts."
},
"tna-dl-42-2-33-5-richard-i-canville-nicholaa-de-la-haye": {
  "shortTitle": "TNA DL 42/2/33/5 — Richard I grant to Gerard de Canville and Nicholaa de la Haye",
  "citation": "The National Archives (UK), Duchy of Lancaster: Cartularies, Enrolments, Surveys and other Miscellaneous Books, DL 42/2/33/5, folio 476, 1189-1199.",
  "archive": "The National Archives, Kew",
  "url": "https://discovery.nationalarchives.gov.uk/details/r/C19720752",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": null,
  "notes": "Richard I grant to Gerard de Canville and his wife Nicholaa de la Haye of her right and inheritance in England and Normandy, with the custody and constableship of Lincoln castle and the manors of Puppeville and Warreville. Hugh de Gurnai [Gournay] is named in the witness list alongside John the king's brother count of Mortain, William de Hommet constable, Henry de Newburgh, Walkelin de Ferrers, Ralph Taissun, William de St John, Robert de Harcourt, William de Diva, and Hugh Bard the king's marshal. Dated by William the king's chancellor at Barfleur; undated, 1189-1199. Latin. The Discovery catalogue note reproduces a substantial English summary of the grant."
},
"tna-a2a-705-349-aylesbury-1483-grant": {
  "shortTitle": "TNA A2A 705:349/12946/495200 — Aylesbury grant, 4 April 1483",
  "citation": "The National Archives, Access to Archives (A2A), reference 705:349/12946/495200, grant of lands, tenements and appurtenances in Aylesbury and Walton-near-Aylesbury by John Ingram of Aylesbury and his wife Agnes to Richard Gourney and John Ingram of North Marston, 4 April 1483.",
  "archive": "The National Archives (UK) — collection now searchable through Discovery; original held at a county record office (per A2A description, the depositing repository line should be re-verified at Phase-2 application).",
  "url": "https://www.nationalarchives.gov.uk/a2a/",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": null,
  "notes": "A2A descriptive index entry only. The deed names John Goodman and Henry Crowlond as attorneys for delivery of possession. Used in v52 as a Buckinghamshire collateral Gurney record (Richard Gourney of Aylesbury, fl.1483). The A2A descriptive system is being progressively folded into TNA Discovery; the exact Discovery URL for this reference should be resolved when the patchset is applied."
},
"medievalgenealogy-cp25-1-21-112-stone-hartwell": {
  "shortTitle": "medievalgenealogy.org.uk — CP 25/1/21/112 fine, Stone and Hartwell, Bucks",
  "citation": "Abstract of a Feet of Fines entry, CP 25/1/21/112, c.1404, Richard Gurney and William Gurney v. Robert Porter and his wife Christian, settlement of an action concerning a messuage, 4 tofts, 86 acres of land, 10 acres of meadow, 2 acres of pasture, and 12s. of rent in Stone and Hartwell, Buckinghamshire; published online by Chris Phillips, www.medievalgenealogy.org.uk.",
  "archive": "TNA CP 25/1/21/112 (original); medievalgenealogy.org.uk transcript/abstract",
  "url": "https://www.medievalgenealogy.org.uk/fines/abstracts/CP_25_1_21_112.shtml",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": null,
  "notes": "Used in v52 as a Buckinghamshire collateral Gurney record (Richard Gurney + William Gurney v. Robert and Christian Porter, c.1404). Re-verification of the abstract against the original TNA CP 25/1 series is the natural next step before any heavier interpretation is built on this fine."
},
"bho-ipm-edward-iii-vol12-sancto-omero-mulbarton-1366": {
  "shortTitle": "BHO Calendar of IPM, Edward III, vol. 12 — Thomas de Sancto Omero (1366)",
  "citation": "\"Inquisitions Post Mortem, Edward III, File 188,\" Calendar of Inquisitions Post Mortem, vol. 12 (London: HMSO; published online at British History Online), entry 79, Thomas de Sancto Omero, 40 Edward III (1366).",
  "archive": "TNA E. Inq. P.M. File 25 (13) and C. Edw. III File 188 (10); printed calendar published HMSO; available online via British History Online.",
  "url": "https://www.british-history.ac.uk/inquis-post-mortem/vol12/pp51-65",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": null,
  "notes": "Assignment of dower and partition of the lands of Thomas de Sancto Omero, made at Mulkebertone (Mulbarton), Norfolk, 23-25 May 1366. The Mulbarton partition lists 'the services of Robert Gurnay, John Pigot and William Stalon' among the free tenants, and separately 'bondmen named Nicholas Elvard, Henry Isabel, Robert Gurnay, John Dobyn, Henry Short and Walter Smyht.' Two distinct Roberts named Gurnay are named in the same partition — one free tenant, one bondman. Neither is G22 Robert Gournay (gentry, fl. c.1370-1420)."
},
"bardsley-english-welsh-surnames-1901": {
  "shortTitle": "Bardsley, Dictionary of English & Welsh Surnames",
  "citation": "Charles Wareing Bardsley, A Dictionary of English & Welsh Surnames with Special American Instances (London: Henry Frowde; Oxford University Press, 1901), p. 344, s.v. \"Gurney, Gurnay, Gurnee.\"",
  "archive": "Internet Archive (bwb_P9-CDP-537 copy)",
  "url": "https://archive.org/details/bwb_P9-CDP-537/page/344/mode/2up",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": null,
  "notes": "Standard turn-of-the-20th-century surname etymology reference. The Gurney entry repeats the Norman-origin tradition (Gournai-en-Brai, two Hugh de Gournays at Hastings per Roman de Rou) and lists specimen medieval bearers from Rotuli Hundredorum 1273 (Milesenta fil. Hugh de Gorney co. Bedf.; John de Gurnay co. Norf.; Anselm de Gurney co. Glouc.; Robert de Gurnay co. Wilts., Hen. III - Edw. I), Kirby's Quest 1327 (John de Gorney co. Soms.), and one Norfolk clerical entry (Robert Gournay, rector of Hethel, co. Norf., 1438; abbreviation 'FF. v. 109' in Bardsley still to be resolved). Used in v52 only for the 1438 Hethel rector lead. Surname-etymology and Hastings-tradition material is already documented in the senior-line companion files (G33, G34) and the senior-baron-line topic file; no new prose is added for those."
}
```

---

## 1. Sir John Gurney (d.1408) — CFR escheat 16 Feb 1409 corroboration

**File:** `research/people/g21-thomas-gournay-i-fact-sheet.research.md`

**Location:** Inside `### Collateral succession mechanics`, append the following paragraph immediately after the existing "Thomas 'the nephew' succeeded" line and before the existing 2026-05-22 military-service update.

```markdown
The 1409 Fine Rolls preserve the post-death administrative trace of Sir John's death directly. On 16 February 1409 the Escheator of Norfolk was ordered to take Sir John's lands into the King's hands following his death, the standard escheat-order step opening the inheritance process that the IPM (DG-Supp Note 121) then resolved.[^cfr-1409-sir-john-escheat]

[^cfr-1409-sir-john-escheat]: *Calendar of the Fine Rolls Preserved in the Public Record Office, Henry IV, A.D. 1405-1413*, vol. 13 (London: HMSO, 1934), p. 123, entry of 16 February 1409 ordering the Escheator of Norfolk to take into the king's hands the lands of John Gurnay, deceased. Discovered via the girders.net Medieval Gurneys compilation. Source ID: `cfr-henry-iv-1405-13`.
```

---

## 2. Thomas Gournay II (d.1471) — NCC will register Jekkys 211 citation

**File:** `research/people/g20-thomas-gournay-ii-fact-sheet.research.md`

**Location:** Inside `### The 1471 will — textile bequest (DG-I p. 282)`, append the following paragraph at the end of that entry (before the next `### Wars of the Roses context` heading).

```markdown
The will itself survives as a register copy at the Norfolk Record Office in the Norwich Consistory Court will register Jekkys, folio 211 — the primary-register text that lies behind DG-I's English extracts (pp. 280-282) of the three-residence and Margaret-textile-bequest clauses.[^nro-jekkys-211-thomas-ii-will]

[^nro-jekkys-211-thomas-ii-will]: Norfolk Record Office, Norwich Consistory Court will register Jekkys, folio 211, will of Thomas Gurnay of Harpley, 1471. NRO online catalogue: http://nrocat.norfolk.gov.uk. Source ID: `nro-ncc-wills-registers`.
```

---

## 3. Sir Matthew de Gournay (Somerset) — CPR/CFR primary citations

**File:** `research/places/somerset-gournay-collateral.md`

**Location:** Inside `## Sir Matthew de Gournay`, append the following paragraph after the existing Pettigrew-cited "26 September 1406" sentence.

```markdown
The Patent and Fine Rolls of Henry IV preserve four primary-source moments from the same Somerset career. On 18 December 1399 Matthew sat on a commission of array for Somerset; on 25 February 1400 he was placed on a commission to inquire into all treasons and insurrections at Frome, Somerset; on 12 March 1400 he was granted 300 marks a year at the Exchequer; and on 5 July 1400 he sat on a commission of the peace for Somerset.[^cpr-1399-1400-matthew-gournay-commissions] The Fine Rolls then record him as already dead by 5 November 1406, confirming Pettigrew's Leland-derived 26 September 1406 death date with an independent administrative terminus ante quem.[^cfr-1406-matthew-gournay-dead-by]

[^cpr-1399-1400-matthew-gournay-commissions]: *Calendar of the Patent Rolls Preserved in the Public Record Office, Henry IV, A.D. 1399-1401*, vol. 1 (London: HMSO, 1903), pp. 210 (commission of array, Somerset, 18 December 1399), 267 (Frome treasons/insurrections inquiry, 25 February 1400), 208 (300 marks/year Exchequer grant, 12 March 1400), 564 (commission of the peace, Somerset, 5 July 1400). Discovered via the girders.net Medieval Gurneys compilation. Source ID: `cpr-henry-iv-1399-1401`.
[^cfr-1406-matthew-gournay-dead-by]: *Calendar of the Fine Rolls Preserved in the Public Record Office, Henry IV, A.D. 1405-1413*, vol. 13 (London: HMSO, 1934), p. 78, recording that Sir Matthew de Gournay had died by 5 November 1406. Source ID: `cfr-henry-iv-1405-13`.
```

---

## 4. Hugh de Gurnai — Richard I grant, TNA DL 42/2/33/5 (1189-1199)

**File:** `research/topics/senior-gournay-baron-line-collateral.md`

**Location:** Inside `## Hugues V de Gournay (c. 1140 – 1214)`, append the following bullet after the existing **1190 Third Crusade** bullet and before **1198 Bellosanne foundation**.

```markdown
- **1189-1199 Richard I court.** Hugh de Gurnai (Gournay) appears in the witness list of a Richard I grant of Gerard de Canville and his wife Nicholaa de la Haye's right and inheritance in England and Normandy, including the custody and constableship of Lincoln castle and the manors of Puppeville and Warreville. The witness list places Hugh alongside John the king's brother count of Mortain, William de Hommet constable, Henry de Newburgh, Walkelin de Ferrers, Ralph Taissun, William de St John, Robert de Harcourt, William de Diva, and Hugh Bard the king's marshal, with the grant dated by William the king's chancellor at Barfleur. This is direct Plantagenet-court attestation for Hugues V in the decade before Bellosanne and the Capetian conquest.[^tna-dl-42-richard-i-hugh-de-gurnai]

[^tna-dl-42-richard-i-hugh-de-gurnai]: The National Archives (UK), Duchy of Lancaster, DL 42/2/33/5, folio 476, [grant of Richard I to Gerard de Canville and Nicholaa de la Haye](https://discovery.nationalarchives.gov.uk/details/r/C19720752), 1189-1199, Honor of Bolingbroke. Latin original; the Discovery catalogue reproduces a substantial English summary including the witness list. Source ID: `tna-dl-42-2-33-5-richard-i-canville-nicholaa-de-la-haye`.
```

---

## 5. Thomas Gurnay of Great Ellingham (d.1454) — pre-Lovell record flag

**File:** `research/places/great-ellingham.md`

**Location:** After the closing paragraph of `## Why this place matters structurally` (i.e. immediately before the existing `## The Manor (current site)` heading), insert the following short note.

```markdown
A 1454 Norwich Consistory Court administration grant names a Thomas Gurnay "of Great Ellingham," more than a century before the documented Lovell inheritance through Margaret Lovell brings the manor into Anthony Gurney's (G17) household.[^nro-aleyn-19-thomas-gurnay-great-ellingham-1454] The Thomas concerned does not match G20 Thomas Gournay II (d.1471, Harpley/West Barsham seat) or G21 Thomas Gournay I (dead before 1444). The record is held here as an open lead for a pre-Lovell Gurney presence in the parish; identity, descent, and possible relationship to the later Lovell-inherited manor are not yet established.

[^nro-aleyn-19-thomas-gurnay-great-ellingham-1454]: Norfolk Record Office, Norwich Consistory Court will register Aleyn, 19, administration of the goods and possessions of Thomas Gurnay of Great Ellingham, 1454. NRO online catalogue: http://nrocat.norfolk.gov.uk. Discovered via the girders.net Medieval Gurneys compilation. Source ID: `nro-ncc-wills-registers`.
```

---

## 6. Henry Gurnay of Norwich (d.1443) — NRO Doke 17 administration

**File:** `research/places/norwich.md`

**Location:** Append a new H2 section at the end of the file, after the existing `## Cathedral precinct memorial evidence` block and its footnotes.

```markdown
## Mid-15th-century Norwich collateral

A 1443 Norwich Consistory Court administration grant records the estate of a Henry Gurnay "of Norwich."[^nro-doke-17-henry-gurnay-1443] The record is contemporary with G21 Thomas Gournay I's tenure of the senior Norfolk seat (West Barsham / Harpley) and with the 1443 Harpley advowson presentation by a Thomas Gurnay (Blomefield, Harpley descent). No direct relationship to the senior line is established; the entry is preserved here as evidence that the Gurney surname was distributed across the city of Norwich itself, not only across the manorial portfolio.

[^nro-doke-17-henry-gurnay-1443]: Norfolk Record Office, Norwich Consistory Court will register Doke, 17, administration of the goods and possessions of Henry Gurnay of Norwich, 1443. NRO online catalogue: http://nrocat.norfolk.gov.uk. Discovered via the girders.net Medieval Gurneys compilation. Source ID: `nro-ncc-wills-registers`.
```

---

## 7. John Gurney goldsmith of Little Walsingham (fl.1423) and Bardsley 1438 Hethel rector

**File:** `research/places/norfolk.md`

**Location:** Append a new H2 section at the end of the file (after the closing interpretive note section). The section consolidates two unrelated collateral Norfolk Gurneys discovered in v52 so that the regional-umbrella file gains two short distributed-record entries without claiming new analytical structure.

```markdown
## Distributed medieval collateral records

Two fifteenth-century Norfolk Gurney records sit outside the manorial chain of the junior line and the cathedral-precinct cluster at Norwich, but belong to the county's distributed Gurney presence in the period.

A John Gurney, goldsmith of Little Walsingham, was pardoned on 1 February 1423 for failing to appear to answer John Langholm touching a plea of a debt of 100s.[^cpr-1423-john-gurney-walsingham-goldsmith] The record is the only known fifteenth-century Norfolk Gurney explicitly named with a goldsmith occupation and an urban Walsingham address; no relationship to the West Barsham seat is established.

A Robert Gournay served as rector of Hethel, Norfolk, in 1438 according to Bardsley's surname dictionary, citing "FF. v. 109."[^bardsley-1438-robert-gournay-hethel] The Bardsley abbreviation requires resolution at the primary-source layer (the citation form is consistent with a Feet of Fines or county-history volume), but the entry is preserved as a Norfolk clerical lead contemporary with G21 Thomas Gournay I.

[^cpr-1423-john-gurney-walsingham-goldsmith]: *Calendar of the Patent Rolls Preserved in the Public Record Office, Henry VI, A.D. 1422-1429*, vol. 1 (London: HMSO, 1901), p. 26, pardon of 1 February 1423 to John Gurney, goldsmith of Little Walsingham, Norfolk, for non-appearance to answer John Langholm touching a plea of a debt of 100s. Discovered via the girders.net Medieval Gurneys compilation. Source ID: `cpr-henry-vi-1422-29`.
[^bardsley-1438-robert-gournay-hethel]: Charles Wareing Bardsley, *A Dictionary of English & Welsh Surnames with Special American Instances* (London: Henry Frowde; Oxford University Press, 1901), p. 344, s.v. "Gurney, Gurnay, Gurnee," reproducing the entry "Robert Gournay, rector of Hethel, co. Norf., 1438: FF. v. 109." The "FF. v. 109" abbreviation should be resolved against the primary record at Phase-2 application. Source ID: `bardsley-english-welsh-surnames-1901`.
```

---

## 8. Richard Gurney (fl.1404) and Richard Gourney of Aylesbury (fl.1483) — Bucks collateral

**File:** `research/places/buckinghamshire.md`

**Location:** Append a new H2 section after the existing `### Farrer on Wendover and Bledlow` block and before the `## Open items` heading.

```markdown
## Later Buckinghamshire Gurney records (15th c.)

Two later Buckinghamshire Gurney records carry forward from the senior-baron Wendover/Bledlow cluster into the fifteenth century, well after Hugh V's line ceased to hold the Bray seat. These are county-level collateral records, not extensions of the senior baron line, and they are preserved here as part of Buckinghamshire's distributed Gurney record-presence.

Around 1404 a Feet of Fines entry records the settlement of an action by Richard Gurney and William Gurney against Robert Porter and his wife Christian, deforciants of a messuage, four tofts, eighty-six acres of land, ten acres of meadow, two acres of pasture, and twelve shillings of rent in Stone and Hartwell, Buckinghamshire.[^cp25-1-21-112-richard-william-gurney-stone-hartwell-1404]

On 4 April 1483 John Ingram of Aylesbury and his wife Agnes granted lands, tenements and appurtenances in Aylesbury and Walton, near Aylesbury, to Richard Gourney and John Ingram of North Marston, with John Goodman and Henry Crowlond named as attorneys to deliver possession.[^tna-a2a-705-349-1483-richard-gourney-aylesbury] The Aylesbury connection is suggestive in light of the seventeenth-century Aylesbury Gurney cluster documented in the John Gurney case file (early-Stuart Aylesbury baptisms, marriages, and burials), but no direct descent has been established between the 1483 Richard Gourney and the 1640s-1660s Aylesbury Gurneys; the record is preserved as a continuity flag rather than as proven descent.

[^cp25-1-21-112-richard-william-gurney-stone-hartwell-1404]: Abstract of Feet of Fines entry CP 25/1/21/112, c.1404, Richard Gurney and William Gurney v. Robert Porter and his wife Christian, settlement of an action concerning a messuage, four tofts, eighty-six acres of land, ten acres of meadow, two acres of pasture, and twelve shillings of rent in Stone and Hartwell, Buckinghamshire; published online by Chris Phillips at [www.medievalgenealogy.org.uk](https://www.medievalgenealogy.org.uk/fines/abstracts/CP_25_1_21_112.shtml). Discovered via the girders.net Medieval Gurneys compilation. Source ID: `medievalgenealogy-cp25-1-21-112-stone-hartwell`.
[^tna-a2a-705-349-1483-richard-gourney-aylesbury]: The National Archives, Access to Archives (A2A) descriptive entry, reference 705:349/12946/495200, grant of 4 April 1483 by John Ingram of Aylesbury and his wife Agnes to Richard Gourney and John Ingram of North Marston, of lands, tenements and appurtenances in Aylesbury and Walton, near Aylesbury; [www.nationalarchives.gov.uk/a2a](https://www.nationalarchives.gov.uk/a2a/). Discovered via the girders.net Medieval Gurneys compilation. Source ID: `tna-a2a-705-349-aylesbury-1483-grant`.
```

---

## 9. Robert Gurnay tenants in the 1366 Sancto Omero IPM — G22 context

**File:** `research/people/g22-robert-gournay-fact-sheet.research.md`

**Location:** Inside `### External research sweep, 22 May 2026`, append the following paragraph at the end of that section, immediately before the existing `### Remaining open primary-source leads` heading.

```markdown
**1366 Mulbarton IPM — two contemporary Robert Gurnays at lower social levels.** The 1366 partition of the Norfolk lands of Thomas de Sancto Omero, made at Mulkebertone (Mulbarton) on 23-25 May 1366, lists "the services of Robert Gurnay, John Pigot and William Stalon" among the free tenants delivered to William de Hoo and his wife Alice, and separately names "bondmen named Nicholas Elvard, Henry Isabel, Robert Gurnay, John Dobyn, Henry Short and Walter Smyht" among the manor's villein tenants.[^bho-ipm-vol12-mulbarton-sancto-omero-1366] Two distinct men named Robert Gurnay are therefore visible in a single Norfolk partition four years before G22's traditional flourishing window (fl. c.1370-1420). Neither matches G22 — one is a free tenant of Mulbarton, the other a bondman of the same manor — but the entry sharpens DG-II p. 363's hedge on the name itself by confirming that the spelling "Robert Gurnay" was carried in 1360s Norfolk at multiple social levels, not only in the gentry line.

[^bho-ipm-vol12-mulbarton-sancto-omero-1366]: "Inquisitions Post Mortem, Edward III, File 188," *Calendar of Inquisitions Post Mortem*, vol. 12 (London: HMSO; British History Online), entry 79, Thomas de Sancto Omero, partition of Norfolk lands, 23-25 May 1366; [www.british-history.ac.uk/inquis-post-mortem/vol12/pp51-65](https://www.british-history.ac.uk/inquis-post-mortem/vol12/pp51-65). Source ID: `bho-ipm-edward-iii-vol12-sancto-omero-mulbarton-1366`.
```

---

## 10. File operations

The intake file currently lives at `sources/intake/processed/Ready/V52-next-stepsv5.md`. Phase-2 application should:

1. **Rename and relocate** the intake file to `sources/intake/archive/v52-girders-net-gurney-abstracts.md` (canonical archive name aligned with the patchset slug), preserving the file content verbatim. The interim `processed/Ready/` subdirectory is non-canonical per `.claude/rules/sources-intake.md` (the canonical lifecycle is `new/` → `processed/` → `archive/`); the file should not remain there after application.
2. **Add the ten new `data/sources.json` entries** listed in the "New `data/sources.json` entries" block above. Append at the end of the `sources` object in `data/sources.json`. Bump `meta.lastUpdated` to the application date.
3. **Apply the eight research-content insertions** listed in §1-§9 above, in the order given. Each insertion is local and does not touch surrounding paragraphs.
4. **No `sources/validations/*.md` notes are required** for this patchset. All eight retained items are short documentary abstracts whose handling is fully captured by the new sourceId block and the inserted research-prose footnote; the validation layer would duplicate the patchset.

## 11. Unresolved items (do not block application)

- The Bardsley "FF. v. 109" abbreviation should be resolved at Phase-2 application or at the next Bardsley pass (most plausibly Norfolk Feet of Fines or a Blomefield volume reference; verification required).
- The TNA A2A 705:349 reference's depositing repository line should be re-verified through TNA Discovery, since A2A descriptive content has been progressively migrated into Discovery and the holding-repository field is the most likely to have shifted.
- The 1404 medievalgenealogy.org.uk Stone/Hartwell fine should at some point be re-verified against the TNA CP 25/1/21 original before any heavier interpretation is built on it.
- The 1454 NRO Aleyn, 19 Thomas Gurnay of Great Ellingham administration warrants a deeper pull at the next Great Ellingham pass — the pre-Lovell Gurney presence is a genuinely interesting flag and deserves direct register-level examination.
