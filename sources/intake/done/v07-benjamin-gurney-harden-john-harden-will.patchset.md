# Intake patchset v07 — Benjamin Gurney, Jane/Jean Harden, and John Harden’s 1751 will

**Prepared:** 2026-04-28  
**Repo:** `allengurney/gurney-genealogy`  
**Target branch/ref inspected:** `main`  
**Patchset destination when applied:** `sources/intake/processed/v07-benjamin-gurney-harden-john-harden-will.patchset.md`

## Scope

Apply the attached research in:

- `benjamin_gurney_harden_research_tables_updated.md`
- `john_harden_1751_will_evidence_package.md`

to the canonical repo layers for Benjamin Gurney **G9**, Benjamin Gurney **G10**, and only as needed Benjamin Gurney **G11**.

This is a substantive evidence update. The key change is that the original Plymouth County probate record-book copy of **John Harden’s 1751 will** has now been located and transcribed. The will confirms that **Benjamin Gurney was John Harden’s grandson**, names John Harden’s daughter **Jane Spear**, names daughter **Sarah Gurney**, and shows **Elizabeth Harden as a witness rather than as a daughter/heir**.

## Governing evidentiary posture

Apply these conclusions exactly; do not re-expand or overstate them during Phase 2.

1. **Confirmed:** John Harden’s 1751 will names “my grandson Benjamin Gurney” and gives him twenty shillings.
2. **Confirmed:** John Harden’s daughter set in the will includes Mary Hobert/Hobart, Sarah Gurney, Jane Spear, deceased Rebecca Noyes’s children, and Lydia Dawes.
3. **Confirmed:** Elizabeth Harden appears in the will record as a witness, not as a daughter/heir.
4. **Primary-derived baptismal record:** Abington vital records list Benjamin under a Harden variant as “Benjamin, s. Jean, bp. May 30, 1730. C.R.1.” Use **baptized**, not **born**, for this record.
5. **Best-supported mother:** Jane/Jean Harden Spear is the likely mother of Benjamin Gurney G9. The will does not explicitly say “Benjamin Gurney, son of my daughter Jane,” so use **likely**, **best-supported**, or equivalent phrasing.
6. **Father link:** The Abington baptism does not name the father. Benjamin Gurney G10 as father is supported by secondary compiled genealogy and by the surrounding Harden/Gurney identity chain, not by the baptismal entry itself. Do not present the primary baptism as naming G10.
7. **Raised by aunt:** The will does not prove guardianship or upbringing. Treat the “raised by mother’s sister” claim as **family tradition / plausible reconstruction**. Sarah Harden Gurney is the strongest aunt-household candidate because she is a named Harden daughter, married into the Gurney family, and was old enough in 1730, but this is not proved.
8. **G11 impact:** No direct G11 fact change is required from this intake. G11 may be mentioned in G10 research only for the three-Benjamin chronology and secondary compiled genealogy context.

---

## File operation summary

### Files to update

- `data/sources.json`
- `data/ancestors v26.json`
- `research/people/g09-benjamin-gurney-fact-sheet.research.md`
- `research/people/g10-benjamin-gurney-fact-sheet.research.md`
- `fact-sheets/g09-benjamin-gurney-fact-sheet.md`
- `fact-sheets/g10-benjamin-gurney-fact-sheet.md`

### Files to create

- `sources/corpus_supplement/plymouth-probate-john-harden-1751-will.md`
- `sources/corpus_supplement/benjamin-gurney-harden-research-tables-2026-04.md`
- `sources/validations/plymouth-probate-john-harden-1751-will.md`
- `sources/validations/benjamin-gurney-harden-research-tables-2026-04.md`

### Files not to update

- Do **not** update `data/ancestors v25.json`; it is legacy.
- Do **not** hand-edit `site/website/_data/ancestors.json` or `site/website/_data/sourcesCatalog.json` unless the current build workflow explicitly treats them as non-generated mirrors. The repo rules identify `site/` as presentation/generated; canonical updates belong upstream in `data/`, `fact-sheets/`, and `research/`.
- Do **not** update G11 fact sheet or G11 data record for this intake unless Phase 2 finds the current branch has changed and now contains a directly conflicting G11 statement.

---

## 1. Update `data/sources.json`

### 1.1 Metadata

Set:

```json
"lastUpdated": "2026-04-28"
```

Do not change the existing schema version unless the current file has already advanced it.

### 1.2 Add source entry: John Harden 1751 will

Add this source entry under `"sources"` near other Plymouth County / Massachusetts probate or colonial New England sources.

```json
    "plymouth-probate-john-harden-1751-will": {
      "shortTitle": "Plymouth Probate — John Harden will (1751)",
      "citation": "Massachusetts. Probate Court (Plymouth County). Probate records, 1686–1903; with index and docket, 1685–1967. Plymouth County Probate Court record book, manuscript pp. 383–384, will of John Harden of Bridgewater, Plymouth County, Massachusetts, blacksmith, dated 17 September 1751, proved 7 October 1751.",
      "archive": "FamilySearch / microfilm of Plymouth County Probate Court records filmed by the Genealogical Society of Utah",
      "url": "https://www.familysearch.org/en/search/catalog/277512",
      "corpusStatus": "full",
      "corpusPath": "sources/corpus_supplement/plymouth-probate-john-harden-1751-will.md",
      "mediaPath": null,
      "validationPath": "sources/validations/plymouth-probate-john-harden-1751-will.md",
      "notes": "Primary probate record-book copy of John Harden's will. Key evidence for Benjamin Gurney G9: names John Harden's wife Mary, daughter Mary Hobert/Hobart, daughter Sarah Gurney, daughter Jane Spear, the children of deceased daughter Rebecca Noyes, daughter Lydia Dawes, son John Harden, and grandson Benjamin Gurney. Elizabeth Harden appears as a witness, not as a daughter or heir. Images: p. 383 https://www.familysearch.org/ark:/61903/3:1:3QSQ-G97D-F6PW; p. 384 https://www.familysearch.org/ark:/61903/3:1:3QS7-897D-FXDF."
    },
```

### 1.3 Add source entry: Abington vital records

Add this entry if it does not already exist. If a functionally equivalent sourceId already exists for Abington vital records, reuse the existing ID and update all references below accordingly.

```json
    "abington-vr-1850-vol1": {
      "shortTitle": "Abington Vital Records to 1850, vol. 1",
      "citation": "Vital Records of Abington, Massachusetts, to the Year 1850. Volume 1: Births. Boston: New England Historic Genealogical Society, 1912.",
      "archive": "Internet Archive / Wikimedia Commons PDF; MassachusettsGenealogy transcription used for abbreviation explanation",
      "url": "https://commons.wikimedia.org/wiki/File:Vital_records_of_Abington,_Massachusetts,_to_the_year_1850_.._(IA_vitalrecordsofab02abing).pdf",
      "corpusStatus": "partial",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/benjamin-gurney-harden-research-tables-2026-04.md",
      "notes": "Primary-derived town vital-record compilation. Important entries include Benjamin under Harden/Hardin variant as 'Benjamin, s. Jean, bp. May 30, 1730. C.R.1.' The abbreviation 'bp.' means baptized; C.R.1 identifies First Church of Abington. Also provides the John and Mary Harden child sequence including Mary, Sarah, Jean, Rebecca/Rebacka, Lydia, and John."
    },
```

### 1.4 Add source entry: Hobart, Historical Sketch of Abington

Add this entry if it does not already exist.

```json
    "hobart-abington-1839": {
      "shortTitle": "Hobart, Historical Sketch of Abington (1839)",
      "citation": "Hobart, Aaron. Historical Sketch of Abington, Plymouth County, Massachusetts; with an Appendix. Boston: Samuel N. Dickinson, 1839.",
      "archive": "LDSGenealogy online transcription",
      "url": "https://ldsgenealogy.com/MA/books/Historical-sketch-of-Abington-Plymouth-County-Massachusetts-With-an-appendix-part-2.htm",
      "corpusStatus": "partial",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/benjamin-gurney-harden-research-tables-2026-04.md",
      "notes": "Secondary local history for old Abington and Little Comfort. Useful for John Harden's Little Comfort context and the 22 February 1711 baptism of Jane Harden, daughter of John Harden of Little Comfort, as recorded by Mr. Niles of Braintree. Hobart-derived wording about an Elizabeth should be treated cautiously because the original John Harden will shows Elizabeth Harden as a witness, not as a daughter/heir."
    },
```

### 1.5 Add source entry: The Neverending Hobby compiled genealogy

Add this entry if it does not already exist.

```json
    "neverending-hobby-john-gurney-us-1636": {
      "shortTitle": "The Neverending Hobby — John Gurney, US 1636",
      "citation": "\"John Gurney, US 1636.\" The Neverending Hobby.",
      "archive": "Public compiled genealogy website",
      "url": "https://sites.google.com/site/theneverendinghobby/home/those-connected-to-more-than-one-family/john-gurney-us-1636",
      "corpusStatus": "partial",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/benjamin-gurney-harden-research-tables-2026-04.md",
      "notes": "Secondary compiled genealogy. Relevant for the Benjamin Gurney G10 / Jane Harden non-marital relationship, the identification of Benjamin Gurney G10 as father of Benjamin G9, Jane's reported return to Braintree with her parents, Sarah Harden's marriage to Nathan Gurney, and the later Sarah Morse child set including a second Benjamin. Use as corroborating secondary evidence, not as primary proof."
    },
```

### 1.6 Add source entry: Middleborough marriage index

Add this entry if it does not already exist.

```json
    "middleborough-marriages-by-mens-name": {
      "shortTitle": "Middleborough marriages by men's name",
      "citation": "Middleborough Public Library. \"Marriages by Men's Name.\" Middleborough, Massachusetts marriage index PDF.",
      "archive": "Middleborough Public Library online PDF",
      "url": "https://midlib.org/sites/midlib.org/files/images/marriages%20by%20mens%20name.pdf",
      "corpusStatus": "partial",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/benjamin-gurney-harden-research-tables-2026-04.md",
      "notes": "Marriage index source for Benjamin Gurney and Sarah Morse, 14 June 1731, and a later Benjamin Gurney and Thankfull Ellis, 23 August 1781. Use as an index until the original register image is obtained."
    },
```

### 1.7 Add source entry: Research table package

This entry tracks the supplied synthesized research table, not as a governing primary source but as a processing/crosswalk artifact.

```json
    "benjamin-gurney-harden-research-tables-2026-04": {
      "shortTitle": "Benjamin Gurney / Harden research tables (2026-04)",
      "citation": "Allen Gurney research intake. Benjamin Gurney, Jane/Jean Harden, and Related Harden–Gurney Research Tables. Updated April 2026.",
      "archive": "Project intake attachment",
      "url": null,
      "corpusStatus": "captured",
      "corpusPath": "sources/corpus_supplement/benjamin-gurney-harden-research-tables-2026-04.md",
      "mediaPath": null,
      "validationPath": "sources/validations/benjamin-gurney-harden-research-tables-2026-04.md",
      "notes": "Synthesis table prepared from public-source research and the located John Harden probate-record images. Use as a research crosswalk and not as a substitute for citing the underlying primary or secondary sources."
    },
```

---

## 2. Create corpus-supplement files

### 2.1 Create `sources/corpus_supplement/plymouth-probate-john-harden-1751-will.md`

Create this file exactly.

```markdown
# Plymouth Probate — John Harden will (1751)

**Source ID:** `plymouth-probate-john-harden-1751-will`

## Full citation

Massachusetts. Probate Court (Plymouth County). *Probate records, 1686–1903; with index and docket, 1685–1967*. Plymouth County Probate Court record book, manuscript pages 383–384, will of **John Harden of Bridgewater, Plymouth County, Massachusetts, blacksmith**, dated **17 September 1751**, proved **7 October 1751**. Microfilm of originals at Plymouth, Massachusetts; filmed by the Genealogical Society of Utah. FamilySearch catalog: https://www.familysearch.org/en/search/catalog/277512. FamilySearch collection: https://www.familysearch.org/en/search/collection/2018320. Images consulted: page 383 image https://www.familysearch.org/ark:/61903/3:1:3QSQ-G97D-F6PW; page 384 image https://www.familysearch.org/ark:/61903/3:1:3QS7-897D-FXDF. Related index image showing the record-book target: https://www.familysearch.org/ark:/61903/3:1:3QS7-897D-FXB1.

## Transcription conventions

- This is a working full-text transcription from the record-book copy of the will.
- Spelling, capitalization, and punctuation are lightly normalized only where needed for readability.
- Relationship terms and names are preserved.
- Uncertain readings are placed in square brackets.
- The will begins on page 383 and continues on page 384.

## Full text of the will

> In the Name of God Amen. I John Harden of Bridgewater in the County of Plimouth in New England, Blacksmith, being of perfect mind and memory, blessed be God, being indisposed of body, doe make this my last will & testament in manner & form following, that is to say, after recommending my Soule into ye hands of God that gave it and my body to the dust to be decently buried at the discretion of my executors hereafter named; as for the estate which God hath given me to dispose of as followeth —
>
> Imprimis, I do give unto Mary my well beloved wife the improvement of all my estate and the income of the same, both real and personal, except what I have hereafter disposed of, during her life; and after my wife’s decease I do give the estate both real and personal unto my five daughters and unto the heirs of my Daughter Rebecca Noyes deceased, the above said estate to be equally divided amongst them, that is to say, one fifth part to my Daughter Mary Hobert, one fifth to my Daughter Sarah Gurney, one fifth part to my Daughter Jane Spear, and one fifth part to the children of my Daughter Rebecca Noyes deceased, and the other fifth part which makes the whole of my estate to my Daughter Lydia Dawes, to them, their heirs & assigns forever.
>
> Item, I do give unto my son John Harden all my blacksmith tools [and iron chains] to him, his heirs & assigns forever.
>
> Item, I also give unto my grandson Benjamin Gurney twenty shillings to be paid by my executors.
>
> Lastly, I do constitute, ordain, and appoint my dear wife Mary and my son-in-law Robert Bates to be the sole executors of this my last will and testament, as witness my hand and seal on this seventeenth day of September Anno Domini one thousand seven hundred and fifty one, and in the twenty fifth year of his Majesty’s reign &c.
>
> Signed, sealed, published & declared to be my last will & testament in the presence of —
>
> Samuel Reade  
> Elizabeth [her mark] Harden  
> Woodbridge [his mark] Brown
>
> John Harden [seal]

## Probate attestation

> Plimouth ss. October the Seventh, 1751. This will being exhibited for probate by the executors therein named, Elizabeth Harden, Woodbridge Brown, made oath that they saw the said John Harden sign, seal, and heard him declare this instrument to be his last will and testament, and that they together with Samuel Reed in the testator’s presence subscribed as witnesses, and that according to the best of their judgments he was then of sound mind.
>
> Before me, John Cushing, Judge of Probate.

## Research value

The will confirms that Benjamin Gurney was John Harden’s grandson. It also confirms the relevant Harden daughter-lines: Mary Hobert/Hobart, Sarah Gurney, Jane Spear, deceased Rebecca Noyes’s children, and Lydia Dawes. This substantially improves the Benjamin Gurney / Harden evidence chain because the grandson relationship is no longer dependent on Hobart’s local-history abstract.

The will does not explicitly identify Benjamin Gurney as the son of Jane Spear. Its importance is strongest when combined with the Abington baptismal entry for Benjamin, son of Jean, baptized 30 May 1730. The combined record chain supports Jane/Jean Harden Spear as the best-supported maternal candidate, but the fact sheet should still avoid saying the will alone proves Jane’s maternity.

Elizabeth Harden appears as a witness, not as a daughter or heir. That resolves the prior Elizabeth problem in favor of treating any “daughter Elizabeth” language as a derivative abstracting or conflation issue unless a separate primary record is later found.

The will does not state that Benjamin Gurney was raised by an aunt. That tradition remains plausible but unproved.
```

### 2.2 Create `sources/corpus_supplement/benjamin-gurney-harden-research-tables-2026-04.md`

Create this file as a concise captured reference to the supplied table package.

```markdown
# Benjamin Gurney / Harden research tables (2026-04)

**Source ID:** `benjamin-gurney-harden-research-tables-2026-04`

## Citation

Allen Gurney research intake. *Benjamin Gurney, Jane/Jean Harden, and Related Harden–Gurney Research Tables*. Updated April 2026.

## Scope

This corpus-supplement file records the existence and research value of the supplied table package. The table package synthesizes public-source research and the newly located John Harden probate-record images. It is a crosswalk into the underlying sources, not a substitute for citing the underlying primary or secondary records.

## Key retained conclusions

- The original Plymouth County probate record-book copy of John Harden’s 1751 will has been located on manuscript pages 383–384.
- The will names “my grandson Benjamin Gurney.”
- The will names daughter-lines Mary Hobert/Hobart, Sarah Gurney, Jane Spear, the children of deceased Rebecca Noyes, and Lydia Dawes.
- Elizabeth Harden appears as a witness, not as a daughter or heir.
- Abington vital records list Benjamin under a Harden/Hardin variant as “Benjamin, s. Jean, bp. May 30, 1730. C.R.1.”
- “bp.” should be read as baptized, and “C.R.1” as First Church of Abington.
- Jane/Jean Harden Spear is the best-supported maternal candidate for Benjamin Gurney G9.
- The Abington baptism does not name Benjamin Gurney G10 as father; the G10 father link remains supported by secondary compiled genealogy and by the broader Harden/Gurney evidence chain.
- The “raised by mother’s sister” tradition is plausible but unproved; Sarah Harden Gurney is the strongest aunt-household candidate, but no direct guardianship or household record has been located in this intake.
```

---

## 3. Create validation files

### 3.1 Create `sources/validations/plymouth-probate-john-harden-1751-will.md`

Keep this validation thin.

```markdown
# Source validation: Plymouth Probate — John Harden will (1751)

**Source ID:** `plymouth-probate-john-harden-1751-will`

**Source examined:** Plymouth County Probate Court record book, manuscript pages 383–384, will of John Harden of Bridgewater, Plymouth County, Massachusetts, blacksmith, dated 17 September 1751, proved 7 October 1751.

**Images checked:**  
- Page 383: https://www.familysearch.org/ark:/61903/3:1:3QSQ-G97D-F6PW  
- Page 384: https://www.familysearch.org/ark:/61903/3:1:3QS7-897D-FXDF  
- Related index image: https://www.familysearch.org/ark:/61903/3:1:3QS7-897D-FXB1

**Finding destinations:**  
- `research/people/g09-benjamin-gurney-fact-sheet.research.md`  
- `research/people/g10-benjamin-gurney-fact-sheet.research.md`  
- `fact-sheets/g09-benjamin-gurney-fact-sheet.md`  
- `fact-sheets/g10-benjamin-gurney-fact-sheet.md`  
- `data/ancestors v26.json`

**Validation result:** Strong primary-source evidence for John Harden’s family structure and for Benjamin Gurney’s status as John Harden’s grandson.

**Limitations:** The will does not explicitly identify Benjamin Gurney’s mother and does not describe his upbringing, guardianship, or household placement. Those points must be stated from the combined evidence chain or as tradition, not as direct will evidence.

**Detailed execution trail:** `sources/intake/processed/v07-benjamin-gurney-harden-john-harden-will.patchset.md`
```

### 3.2 Create `sources/validations/benjamin-gurney-harden-research-tables-2026-04.md`

```markdown
# Source validation: Benjamin Gurney / Harden research tables (2026-04)

**Source ID:** `benjamin-gurney-harden-research-tables-2026-04`

**Source examined:** Supplied research table package: `benjamin_gurney_harden_research_tables_updated.md`.

**Scope checked:** John Harden will implications; Abington baptism entry; Jane/Jean Harden identification; Elizabeth Harden witness issue; Harden daughter set; aunt-household candidates; Benjamin Gurney G10 father-link evidence; Sarah Morse chronology; later second Benjamin disambiguation.

**Finding destinations:**  
- `research/people/g09-benjamin-gurney-fact-sheet.research.md`  
- `research/people/g10-benjamin-gurney-fact-sheet.research.md`  
- `fact-sheets/g09-benjamin-gurney-fact-sheet.md`  
- `fact-sheets/g10-benjamin-gurney-fact-sheet.md`  
- `data/ancestors v26.json`

**Validation result:** Useful synthesis and source crosswalk. The table package should not be cited as the sole authority for primary facts when the underlying source is available.

**Limitations:** Treat the table as an intake synthesis. Cite the underlying John Harden will, Abington vital records, Hobart local history, Middleborough marriage index, and secondary compiled genealogy directly in fact sheets and research companions.

**Detailed execution trail:** `sources/intake/processed/v07-benjamin-gurney-harden-john-harden-will.patchset.md`
```

---

## 4. Update `data/ancestors v26.json`

Make narrowly scoped edits only.

### 4.1 G9 record: `ancestor-g9-benjamin-gurney`

Within the object with:

```json
"recordId": "ancestor-g9-benjamin-gurney"
```

replace only the following fields.

#### Replace `summary`

```json
"summary": "Plymouth County farmer baptized at Abington as Benjamin, son of Jean/Jane Harden, and confirmed in John Harden's 1751 will as his grandson; in 1770 he sold his Abington land and bought into the frontier town of Cummington with Silas Reed, opening the family's western Massachusetts chapter.",
```

#### Replace `notables`

```json
"notables": "Baptized at Abington 30 May 1730 in the Harden/Hardin entries as Benjamin, son of Jean; C.R.1 identifies the church source as First Church of Abington. John Harden's 1751 Plymouth County will names daughter Jane Spear and separately gives twenty shillings to \"my grandson Benjamin Gurney,\" confirming Benjamin's Harden-side kinship. Elizabeth Harden appears in the will as a witness, not as a daughter or heir, resolving the older Elizabeth-conflict in favor of Jane/Jean Harden Spear as the best-supported maternal candidate. The tradition that Benjamin was raised by his mother's sister remains plausible but unproved; Sarah Harden Gurney is the strongest aunt-household candidate, not a confirmed caregiver. Sold Abington land June 1770; on 5 Nov. 1770 purchased land in Town No. 5 (Cummington) with Silas Reed. 1787 farm exchange with Philip Shaw at Cummington (Foster & Streeter, *\"Only One Cummington,\"* 1974, p. 390). 1790 census: head of a six-person Cummington household (3-0-3). Two marriages — Elizabeth Harden, then Mercy Noyes. Buried Dawes Cemetery, Cummington.",
```

Leave `dates`, `geography`, `landHoldings`, `spouses`, `children`, `buttons`, `recordId`, and `placeRefs` unchanged unless the current branch has an obvious syntax drift that requires correction.

### 4.2 G10 record: `ancestor-g10-benjamin-gurney`

Within the object with:

```json
"recordId": "ancestor-g10-benjamin-gurney"
```

replace only the following fields.

#### Replace `summary`

```json
"summary": "Plymouth County farmer identified by secondary compiled genealogy as the father of Benjamin Gurney G9 through a likely non-marital relationship with Jane/Jean Harden before his 1731 marriage to Sarah Morse; the new John Harden will evidence confirms the Harden grandson relationship but does not itself name G10 as father.",
```

#### Replace `notables`

```json
"notables": "The Abington baptismal record for Benjamin G9 names only the mother, Jean, and records a baptism on 30 May 1730; it does not name the father. The identification of this Benjamin as son of Benjamin Gurney G10 and Jane/Jean Harden is supported by secondary compiled genealogy and strengthened indirectly by John Harden's 1751 will, which names \"my grandson Benjamin Gurney\" and daughter Jane Spear. G10 married Sarah Morse at Middleborough on 14 June 1731, about a year after the Abington baptism. Three traceable Plymouth County land transactions: with his father (G11) bought from Samuel Tinkham, Middleboro, 28 Oct. 1730 (Plym. Reg. 39:79), 3 lots upland + ~2 acres meadow, sold 3 May 1749; bought 8 acres at Middleboro from Sam Eddy Jr., 7 Nov. 1731 (Plym. Reg.); held a Rochester homestead farm later divided among sons Lemuel, Benjamin, and Levi by deed 1 Jan. 1800 (Plym. Co. 95:139, GS film 559,140). The 1800 division and secondary genealogy preserve the two-Benjamin problem: G9, baptized in 1730 as son of Jean/Jane Harden, is distinct from the later Benjamin in the Sarah Morse child set. Died at Rochester before December 1772.",
```

#### Replace `spouses`

```json
"spouses": [
  {
    "name": "Jane / Jean Harden",
    "notes": "Likely non-marital partner; best-supported mother of Benjamin G9. Abington baptism names Benjamin as son of Jean; John Harden's will confirms grandson Benjamin Gurney and daughter Jane Spear."
  },
  {
    "name": "Sarah Morse",
    "dates": "m. 14 June 1731, Middleborough",
    "notes": "Marriage date from Middleborough marriage index; original register still preferred."
  }
],
```

#### Replace `children`

```json
"children": [
  {
    "name": "Benjamin Gurney",
    "dates": "bpt. 30 May 1730",
    "mother": "Jane / Jean Harden",
    "notes": "G9 in direct line; baptism names mother Jean but not father; father identification supported by secondary compiled genealogy and broader Harden/Gurney evidence chain."
  },
  {
    "name": "Lemuel Gurney",
    "mother": "Sarah Morse",
    "notes": "With brothers divided Rochester farm 1 Jan. 1800"
  },
  {
    "name": "Benjamin Gurney",
    "dates": "b. c. 1743",
    "mother": "Sarah Morse",
    "notes": "Later same-name half-brother; likely distinct from G9 and relevant to the two-Benjamin disambiguation problem."
  },
  {
    "name": "Levi Gurney",
    "mother": "Sarah Morse",
    "notes": "With brothers divided Rochester farm 1 Jan. 1800"
  }
],
```

Leave all other G10 fields unchanged unless the current branch has an obvious syntax drift that requires correction.

### 4.3 G11 record: `ancestor-g11-benjamin-gurney`

No JSON change. Add no new assertions to G11 based on this intake.

Rationale: the attached materials provide useful secondary chronology for G11 and G10, but the new primary evidence is John Harden’s will, which affects G9’s Harden-side kinship and G10’s fatherhood discussion. It does not change G11’s vitals, landholding facts, wife, or child list.

---

## 5. Replace G9 research companion

Replace the entire file `research/people/g09-benjamin-gurney-fact-sheet.research.md` with the following synthesized narrative. This is intentionally a clean replacement, not an appended note pile.

```markdown
# Benjamin Gurney (G09) — Research Companion

Research companion for `g09-benjamin-gurney-fact-sheet.md`.

---

## Current evidence summary

Benjamin Gurney G9 is now anchored by two strong, independent record points: the Abington church-derived baptismal entry for **Benjamin, son of Jean**, baptized 30 May 1730, and John Harden's 1751 Plymouth County probate will, which names **"my grandson Benjamin Gurney"** and gives him twenty shillings.[^abington-baptism][^john-harden-will]

This combination materially improves the older narrative. The baptismal entry gives the mother-name as Jean but does not name a father. John Harden's will confirms that the later Benjamin Gurney belonged in the Harden grandson set. The will also names daughter **Jane Spear**, making Jane/Jean Harden Spear the best-supported maternal candidate when the will is read with the baptismal entry.[^abington-baptism][^john-harden-will]

The will does not explicitly state that Benjamin Gurney was the son of Jane Spear. The most accurate present wording is therefore: **Benjamin Gurney G9 was baptized at Abington on 30 May 1730 as Benjamin, son of Jean; John Harden's 1751 will confirms him as John Harden's grandson; Jane/Jean Harden Spear is the likely mother.**[^abington-baptism][^john-harden-will]

## Abington baptism: Benjamin, son of Jean

The Abington vital-record compilation places Benjamin under a Harden/Hardin variant entry:

> HARDENG (see Harden, Hardin), Benjamin, s. Jean, bp; May 30, 1730. C.R.1.[^abington-baptism]

This should be cited and described as a baptism, not as a birth. The abbreviation **bp.** means baptized, and **C.R.1** identifies the First Church of Abington record source.[^abington-abbrev]

The entry is unusually important because it names the mother rather than a father. That is consistent with, but does not by itself prove, the later tradition of a non-marital Gurney/Harden birth. It does establish that the key 30 May 1730 record is a Harden-side church entry and that the mother-name was Jean.[^abington-baptism]

## John Harden's 1751 will

John Harden's will is the strongest new document in this cluster. The record-book copy identifies him as **John Harden of Bridgewater, Plymouth County, Massachusetts, blacksmith**. The will was dated 17 September 1751 and proved 7 October 1751.[^john-harden-will]

The will gives Mary, his wife, the use and income of the estate during her life. After Mary's death, the estate was to be divided among five daughter-lines: daughter Mary Hobert/Hobart, daughter Sarah Gurney, daughter Jane Spear, the children of deceased daughter Rebecca Noyes, and daughter Lydia Dawes. Son John Harden received the blacksmith tools. Benjamin appears in a separate clause:

> Item, I also give unto my grandson Benjamin Gurney twenty shillings to be paid by my executors.[^john-harden-will]

The will confirms Benjamin Gurney's Harden-side kinship without relying on the later Hobart abstract. It also resolves the older Elizabeth problem: Elizabeth Harden appears in the will as a witness, not as a daughter or heir.[^john-harden-will]

## Jane / Jean Harden Spear as likely mother

The identification of Jane/Jean Harden Spear as Benjamin's likely mother rests on a combined chain:

1. Abington records identify Benjamin as **son of Jean**, baptized 30 May 1730.[^abington-baptism]
2. John Harden's will names a daughter **Jane Spear**.[^john-harden-will]
3. The same will names **my grandson Benjamin Gurney**.[^john-harden-will]
4. Elizabeth Harden appears as a witness, not as a daughter/heir, removing the strongest competing reading in the older abstract tradition.[^john-harden-will]
5. Abington records independently place Jean/Jane in the John and Mary Harden child set, with Jean Harden/Hardin, daughter of John and Mary, born 19 November 1709.[^abington-jean-birth]

The Jane/Jean name variation should be preserved rather than silently flattened. The Abington vital records use Jean in the birth and baptismal material; Hobart and the will use Jane. The records are best treated as variant forms for the same Harden daughter unless a later conflicting record is found.[^abington-jean-birth][^hobart-jane-baptism][^john-harden-will]

## The "Elizabeth" problem

Older or derivative accounts introduced an Elizabeth reading into the Benjamin Gurney / John Harden story. The original will materially changes that reading. Elizabeth Harden is present in the will record, but as a witness:

> Samuel Reade  
> Elizabeth [her mark] Harden  
> Woodbridge [his mark] Brown[^john-harden-will]

She is not one of the five daughter-lines receiving John Harden's estate. The daughter-lines are Mary Hobert/Hobart, Sarah Gurney, Jane Spear, deceased Rebecca Noyes's children, and Lydia Dawes.[^john-harden-will]

Until a separate primary record proves otherwise, the Elizabeth wording should be treated as an abstracting or derivative conflation with Elizabeth Harden the witness. It should not be used to identify Benjamin's mother.

## Was Benjamin raised by a maternal aunt?

The will does not prove the "raised by his mother's sister" claim. It confirms Benjamin's Harden kinship, but it says nothing about guardianship, upbringing, household placement, or who cared for Benjamin after the baptism.[^john-harden-will]

The aunt tradition remains plausible because John and Mary Harden's daughter set included several possible maternal aunts. The strongest candidate is **Sarah Harden Gurney**. She was born 9 April 1707, was about twenty-three at Benjamin's baptism, is named in John Harden's will as daughter Sarah Gurney, and secondary compiled genealogy reports that Nathan Gurney married Sarah Harden on 12 May 1725.[^abington-sarah-birth][^john-harden-will][^neverending-hobby]

Sarah is stronger than Mary, Rebecca, or Lydia as a reconstruction because she was both chronologically plausible and already married into the Gurney network. Mary Harden Hobart was old enough and remains possible. Rebecca Harden Noyes was about fourteen in 1730, and Lydia Harden Dawes was about nine, making them weaker candidates for an infancy-caregiver role.[^abington-siblings]

The fact sheet should not say Benjamin was raised by his aunt as a proved fact. A durable phrasing is: **Family tradition says Benjamin was raised by a maternal aunt; Sarah Harden Gurney is the strongest candidate, but no guardianship or household record has yet been found.**

## Father identification: Benjamin Gurney G10

The Abington baptism does not name Benjamin Gurney G10 as father. The father identification currently rests on secondary compiled genealogy plus the broader record chain. The public compiled genealogy at *The Neverending Hobby* states that Benjamin Gurney G10 had a non-marital relationship with Jane Harden and fathered Benjamin in Abington; it also says Jane returned to Braintree with her parents while Benjamin moved to Middleborough with his parents.[^neverending-hobby]

That secondary account aligns well with the primary-derived chronology: Benjamin, son of Jean, was baptized at Abington on 30 May 1730; Benjamin Gurney G10 married Sarah Morse at Middleborough on 14 June 1731; and the later Sarah Morse family produced a second Benjamin in the child set, creating a known two-Benjamin disambiguation problem.[^abington-baptism][^middleborough-marriage][^neverending-hobby]

The father link is therefore credible but should be carefully phrased. Do not cite the baptismal record as if it names G10.

## Harden sibling set

The John and Mary Harden child set matters because it frames both the maternal identification and the aunt-household question. The Abington vital records and John Harden's will together support this core set:

- Mary Harden, born 25 July 1705; later Mary Hobert/Hobart in the will.[^abington-siblings][^john-harden-will]
- Sarah Harden, born 9 April 1707; later Sarah Gurney in the will.[^abington-siblings][^john-harden-will]
- Jean/Jane Harden, born 19 November 1709; later Jane Spear in the will.[^abington-jean-birth][^john-harden-will]
- Rebecca/Rebacka Harden, born 27 January 1715/16; deceased Rebecca Noyes by the will, with her children receiving her share.[^abington-siblings][^john-harden-will]
- Lydia Harden, born 4 August 1720; later Lydia Dawes in the will.[^abington-siblings][^john-harden-will]
- John Harden, born 3 September 1723; son John Harden in the will, receiving the blacksmith tools.[^abington-siblings][^john-harden-will]

This set also confirms that no daughter Elizabeth is needed to explain Benjamin's Harden kinship.

## Later-life anchors

The Harden evidence does not change the later Cummington arc. Benjamin Gurney G9 remains the man who sold Abington land in June 1770 and bought into Town No. 5, later Cummington, with Silas Reed on 5 November 1770. Foster and Streeter preserve the later 1787 farm exchange with Philip Shaw at Cummington.[^foster-cummington]

The 1790 federal census summary for Cummington still requires image-level rechecking. The currently carried 3-0-3 household structure is consistent with a later-life farm household but may not include son Amos in the expected older male category. Treat this as a check item rather than a resolved household reconstruction.

## Open questions

1. **Direct aunt-household proof.** Search guardianship, church, deed, probate-distribution, and loose estate-file records for evidence that Sarah Harden Gurney, Mary Harden Hobart, or another aunt raised Benjamin.
2. **Loose John Harden estate file.** The record-book will has been located; the loose Plymouth County estate file may contain bonds, receipts, or distributions that further clarify relationships.
3. **Original Abington church record.** The NEHGS town vital-record compilation is strong, but the original First Church of Abington register entry would be preferable for the exact wording around "Benjamin, son of Jean."
4. **Original Middleborough marriage record.** The current 14 June 1731 Gurney/Morse date comes from a marriage index; obtain the original register page if possible.
5. **G9 marriage records.** Elizabeth Harden and Mercy Noyes remain underdocumented in this companion.
6. **Cummington deeds and probate.** Direct deed citations for the 1770 sale/purchase and any 1805 estate settlement would strengthen the later-life section.

---

## Sources consulted

- Plymouth County Probate Court record-book copy of John Harden's 1751 will.[^john-harden-will]
- *Vital Records of Abington, Massachusetts, to the Year 1850*, volume 1.[^abington-baptism]
- Aaron Hobart, *Historical Sketch of Abington*.[^hobart-jane-baptism]
- Middleborough marriage index.[^middleborough-marriage]
- *The Neverending Hobby — John Gurney, US 1636*.[^neverending-hobby]
- Foster and Streeter, *Only One Cummington*.[^foster-cummington]

[^john-harden-will]: Massachusetts. Probate Court (Plymouth County), *Probate records, 1686–1903; with index and docket, 1685–1967*, Plymouth County Probate Court record book, manuscript pp. 383–384, will of John Harden of Bridgewater, Plymouth County, Massachusetts, blacksmith, dated 17 September 1751, proved 7 October 1751; FamilySearch catalog https://www.familysearch.org/en/search/catalog/277512; p. 383 image https://www.familysearch.org/ark:/61903/3:1:3QSQ-G97D-F6PW; p. 384 image https://www.familysearch.org/ark:/61903/3:1:3QS7-897D-FXDF. Source ID: `plymouth-probate-john-harden-1751-will`.
[^abington-baptism]: *Vital Records of Abington, Massachusetts, to the Year 1850*, vol. 1, Births (Boston: New England Historic Genealogical Society, 1912), Harden/Hardin/Hardeng entry for Benjamin, son of Jean, baptized 30 May 1730, C.R.1; PDF at https://commons.wikimedia.org/wiki/File:Vital_records_of_Abington,_Massachusetts,_to_the_year_1850_.._(IA_vitalrecordsofab02abing).pdf. Source ID: `abington-vr-1850-vol1`.
[^abington-abbrev]: MassachusettsGenealogy transcription/explanation for *Vital Records of Abington, Massachusetts, to the Year 1850*, vol. 1, noting the abbreviation structure and church-record notation; https://massachusettsgenealogy.net/plymouth/vital-records-of-abington-massachusetts-to-the-year-1850-vol-1.htm. Source ID: `abington-vr-1850-vol1`.
[^abington-jean-birth]: *Vital Records of Abington, Massachusetts, to the Year 1850*, vol. 1, entry for Jean Harden/Hardin, daughter of John and Mary, born 19 November 1709. Source ID: `abington-vr-1850-vol1`.
[^hobart-jane-baptism]: Aaron Hobart, *Historical Sketch of Abington, Plymouth County, Massachusetts; with an Appendix* (Boston: Samuel N. Dickinson, 1839), online transcription at LDSGenealogy, recording Mr. Niles of Braintree's baptism of Jane Harden, daughter of John Harden of Little Comfort, 22 February 1711; https://ldsgenealogy.com/MA/books/Historical-sketch-of-Abington-Plymouth-County-Massachusetts-With-an-appendix-part-2.htm. Source ID: `hobart-abington-1839`.
[^abington-sarah-birth]: *Vital Records of Abington, Massachusetts, to the Year 1850*, vol. 1, entry for Sarah Harden, daughter of John and Mary, born 9 April 1707. Source ID: `abington-vr-1850-vol1`.
[^abington-siblings]: *Vital Records of Abington, Massachusetts, to the Year 1850*, vol. 1, John and Mary Harden/Hardin family entries for Mary, Sarah, Jean, Rebecca/Rebacka, Lydia, and John. Source ID: `abington-vr-1850-vol1`.
[^neverending-hobby]: "John Gurney, US 1636," *The Neverending Hobby*, public compiled genealogy, https://sites.google.com/site/theneverendinghobby/home/those-connected-to-more-than-one-family/john-gurney-us-1636. Use as secondary compiled genealogy. Source ID: `neverending-hobby-john-gurney-us-1636`.
[^middleborough-marriage]: Middleborough Public Library, "Marriages by Men's Name," marriage index PDF, entry for Benjamin Gurney and Sarah Morse, 14 June 1731; https://midlib.org/sites/midlib.org/files/images/marriages%20by%20mens%20name.pdf. Source ID: `middleborough-marriages-by-mens-name`.
[^foster-cummington]: Foster and Streeter, *Only One Cummington* (1974), p. 390, Benjamin Gurney / Cummington land and farm-exchange context. Existing sourceId in repo may be `foster-streeter-cummington`; if absent, add a separate `data/sources.json` entry before citing.
```

---

## 6. Replace G10 research companion

Replace the entire file `research/people/g10-benjamin-gurney-fact-sheet.research.md` with the following synthesized narrative.

```markdown
# Benjamin Gurney (G10) — Research Companion

Research companion for `g10-benjamin-gurney-fact-sheet.md`.

---

## Current evidence summary

Benjamin Gurney G10 remains the best-supported father of Benjamin Gurney G9, but the evidence must be described carefully. The new John Harden will evidence confirms that Benjamin Gurney G9 was John Harden's grandson, and the Abington baptismal entry identifies G9 as Benjamin, son of Jean, baptized 30 May 1730.[^john-harden-will][^abington-baptism]

The baptismal entry does **not** name G10 as father. The father identification comes from secondary compiled genealogy and from the coherence of the surrounding Harden/Gurney evidence chain: Jane/Jean Harden as likely mother, John Harden as confirmed grandfather, a 1730 baptism before G10's 1731 marriage to Sarah Morse, and the later two-Benjamin problem created by the Sarah Morse child set.[^neverending-hobby][^middleborough-marriage]

The fact sheet should therefore say that G10 is **identified by secondary compiled genealogy** as the father of G9 through a likely non-marital relationship with Jane/Jean Harden. It should not imply that the Abington baptism or the John Harden will directly names G10 as father.

## The 1730 / 1731 sequence

The chronology is now sharper:

- **30 May 1730:** Benjamin, son of Jean, baptized at Abington, C.R.1 / First Church of Abington.[^abington-baptism]
- **28 October 1730:** Benjamin Gurney G10 and his father G11 are reported in secondary genealogy as buying Samuel Tinkham's Middleborough land.[^neverending-hobby]
- **14 June 1731:** Benjamin Gurney married Sarah Morse at Middleborough, according to the located Middleborough marriage index.[^middleborough-marriage]
- **7 November 1731:** G10 is reported in existing project data as buying eight acres at Middleborough from Sam Eddy Jr.

This sequence supports a pre-marital chronology if G10 is the father. Benjamin G9 was baptized about a year before the Sarah Morse marriage. The Middleborough land context belongs to G10's transition into his married household, not to proof of the Jane Harden relationship.

## Jane / Jean Harden relationship

The secondary compiled genealogy at *The Neverending Hobby* is the clearest current source saying that Benjamin Gurney G10 had a non-marital relationship with Jane Harden and fathered Benjamin in Abington. It also states that Jane returned to Braintree with her parents while Benjamin moved to Middleborough with his parents.[^neverending-hobby]

This source should be used as corroborating secondary genealogy, not as a primary record. The primary-derived records now available are stronger on the Harden side than on the Gurney-father side:

- Abington baptism: Benjamin, son of Jean.[^abington-baptism]
- John Harden will: grandson Benjamin Gurney; daughter Jane Spear; daughter Sarah Gurney; Elizabeth Harden as witness.[^john-harden-will]

Those records make Jane/Jean Harden Spear the best-supported maternal candidate, but they do not independently name G10.

## Sarah Morse marriage and later household

Benjamin Gurney married Sarah Morse at Middleborough on 14 June 1731, per the Middleborough marriage index.[^middleborough-marriage] The original marriage register should still be obtained before treating the index as final.

The Sarah Morse household is genealogically important because it apparently included a later son also named Benjamin. The secondary compiled genealogy lists a later Benjamin, born about 1743, in the Benjamin Gurney / Sarah Morse child set.[^neverending-hobby] Existing project data also records a Rochester homestead division dated 1 January 1800 among sons Lemuel, Benjamin, and Levi, which fits the Sarah Morse child set rather than G9.[^rochester-deed]

## The two-Benjamins problem

The direct line includes Benjamin G9, baptized in 1730 as son of Jean/Jane Harden, and a later Benjamin in the Sarah Morse child set. The two should be kept explicitly distinct in all data and narrative:

- **Benjamin Gurney G9** — baptized 30 May 1730, son of Jean/Jane Harden; John Harden's grandson; direct line; later Cummington.[^abington-baptism][^john-harden-will]
- **Benjamin Gurney, son of Sarah Morse** — later same-name half-brother, probably the Benjamin in the Rochester homestead division and likely the better fit for later Middleborough/Rochester same-name records.[^neverending-hobby][^rochester-deed]

This is the most important G10 disambiguation issue. Any mid-eighteenth-century record simply naming Benjamin Gurney in Abington, Middleborough, Rochester, or Plymouth County could refer to either man depending on date, location, and kinship context.

## Rochester homestead and Sarah Morse sons

Existing project data cites a 1 January 1800 Plymouth County deed, 95:139, GS film 559,140, by which Lemuel, Benjamin, and Levi divided the Rochester homestead farm.[^rochester-deed] The new Harden evidence does not change that deed's importance. It does, however, sharpen the interpretation: the Benjamin in that division should be treated as the Sarah Morse son unless direct deed language proves otherwise.

Because G9 was already established in Cummington by 1800 and descended through the Harden/Jean line, he should not be casually folded into the Rochester homestead inheritance narrative.

## G11 context

The secondary compiled genealogy also supports the three-Benjamin sequence: G11 Benjamin Gurney, G10 Benjamin Gurney, and G9 Benjamin Gurney.[^neverending-hobby] This intake does not require a G11 fact-sheet update. G11's existing companion should still obtain his original Plymouth probate image and deed records as a separate task.

## Open questions

1. **Primary proof of G10 as father.** Search Abington church discipline records, court records, bastardy/support proceedings, guardianships, or town records for a direct father identification.
2. **Original Middleborough marriage register.** Confirm the G10/Sarah Morse marriage date from the register, not only the index.
3. **G10 probate or administration.** A Rochester/Plymouth County estate file could clarify all Sarah Morse children and whether G9 was excluded or treated separately.
4. **Rochester homestead deed image.** Directly examine Plymouth County 95:139 to confirm the identities and relationships of Lemuel, Benjamin, and Levi.
5. **Second Benjamin's life course.** The later Benjamin likely fits some later Middleborough/Rochester records, possibly including the 1781 Thankfull Ellis marriage, but this requires direct disambiguation.

---

## Sources consulted

- John Harden 1751 will.[^john-harden-will]
- Abington vital-record entry for Benjamin, son of Jean.[^abington-baptism]
- Middleborough marriage index for Benjamin Gurney and Sarah Morse.[^middleborough-marriage]
- *The Neverending Hobby — John Gurney, US 1636*.[^neverending-hobby]
- Existing project-cited Plymouth County deed references for G10.

[^john-harden-will]: Massachusetts. Probate Court (Plymouth County), *Probate records, 1686–1903; with index and docket, 1685–1967*, Plymouth County Probate Court record book, manuscript pp. 383–384, will of John Harden of Bridgewater, Plymouth County, Massachusetts, blacksmith, dated 17 September 1751, proved 7 October 1751; FamilySearch catalog https://www.familysearch.org/en/search/catalog/277512; p. 383 image https://www.familysearch.org/ark:/61903/3:1:3QSQ-G97D-F6PW; p. 384 image https://www.familysearch.org/ark:/61903/3:1:3QS7-897D-FXDF. Source ID: `plymouth-probate-john-harden-1751-will`.
[^abington-baptism]: *Vital Records of Abington, Massachusetts, to the Year 1850*, vol. 1, Births (Boston: New England Historic Genealogical Society, 1912), Harden/Hardin/Hardeng entry for Benjamin, son of Jean, baptized 30 May 1730, C.R.1; PDF at https://commons.wikimedia.org/wiki/File:Vital_records_of_Abington,_Massachusetts,_to_the_year_1850_.._(IA_vitalrecordsofab02abing).pdf. Source ID: `abington-vr-1850-vol1`.
[^middleborough-marriage]: Middleborough Public Library, "Marriages by Men's Name," marriage index PDF, entry for Benjamin Gurney and Sarah Morse, 14 June 1731; https://midlib.org/sites/midlib.org/files/images/marriages%20by%20mens%20name.pdf. Source ID: `middleborough-marriages-by-mens-name`.
[^neverending-hobby]: "John Gurney, US 1636," *The Neverending Hobby*, public compiled genealogy, https://sites.google.com/site/theneverendinghobby/home/those-connected-to-more-than-one-family/john-gurney-us-1636. Use as secondary compiled genealogy. Source ID: `neverending-hobby-john-gurney-us-1636`.
[^rochester-deed]: Plymouth County land deed 95:139, GS film 559,140, Rochester homestead farm divided among Lemuel, Benjamin, and Levi Gurney, 1 January 1800; currently cited through `data/ancestors v26.json`, G10 entry. Direct image still needed before finalizing all relationship language.
```

---

## 7. Update G9 fact sheet

Update `fact-sheets/g09-benjamin-gurney-fact-sheet.md` with targeted edits.

### 7.1 Front matter

Set:

```yaml
updated: 28 April 2026
```

Revise `subtitle` to:

```yaml
subtitle: "Ancestor fact sheet for G09 in the direct Gurney line. Abington-baptized Massachusetts farmer, now directly confirmed as John Harden's grandson by the 1751 Harden will; sold Plymouth County land in 1770 and bought into Cummington with Silas Reed."
```

### 7.2 Vital "Born" field

Replace the current Born value with:

```html
<div class="fact-value">Baptized 30 May 1730, Abington, Plymouth County, Massachusetts, as Benjamin, son of Jean, in the First Church of Abington-derived Harden/Hardin entries; later confirmed by John Harden's 1751 will as John Harden's grandson. <sup class="fn"><a href="#n1" id="ref-1">1</a></sup><sup class="fn"><a href="#n5" id="ref-5born">5</a></sup></div>
```

### 7.3 Highlight: born of liaison / raised by aunt

Replace the first highlight bullet with:

```html
<li><strong>Confirmed as John Harden's grandson.</strong> The original Plymouth County record-book copy of John Harden's 1751 will gives "my grandson Benjamin Gurney" twenty shillings. Read with the Abington baptism of Benjamin, son of Jean, this makes Jane/Jean Harden Spear the best-supported maternal candidate; the older "Elizabeth" reading is substantially weakened because Elizabeth Harden appears in the will as a witness, not as a daughter or heir. <sup class="fn"><a href="#n1" id="ref-1b">1</a></sup><sup class="fn"><a href="#n5" id="ref-5">5</a></sup></li>
```

Add this new highlight bullet immediately after it:

```html
<li><strong>The aunt-upbringing tradition is plausible but not proved.</strong> Family tradition says Benjamin was raised by his mother's sister. The will confirms the Harden kinship but does not name a guardian or caregiver. Sarah Harden Gurney, a Harden daughter who married into the Gurney family, is the strongest aunt-household candidate, but no direct guardianship or household record has yet been found. <sup class="fn"><a href="#n9" id="ref-9">9</a></sup></li>
```

### 7.4 Narrative paragraph 1

Replace the current first narrative paragraph with:

```html
<p>Benjamin Gurney is the man who moved the family from old Plymouth County into the Massachusetts hill country. The newly located John Harden will materially strengthens the opening chapter of his life: he was baptized at Abington on 30 May 1730 as Benjamin, son of Jean, and John Harden's 1751 Plymouth County will later named "my grandson Benjamin Gurney." The combined record chain points to Jane/Jean Harden Spear as his likely mother, while Benjamin Gurney G10 remains the father identified by secondary compiled genealogy rather than by the baptismal entry itself. The older Elizabeth-Harden reading should be set aside unless new evidence appears, because Elizabeth Harden is a witness in the will, not a daughter or heir. <sup class="fn"><a href="#n1" id="ref-1c">1</a></sup><sup class="fn"><a href="#n5" id="ref-5b">5</a></sup><sup class="fn"><a href="#n10" id="ref-10">10</a></sup></p>
```

### 7.5 Citations list

Replace existing citations `n1`, `n4`, and `n5`; add `n9` and `n10`.

Use these exact citation bodies.

```html
<li id="n1"><em>Vital Records of Abington, Massachusetts, to the Year 1850</em>, vol. 1, Births (Boston: New England Historic Genealogical Society, 1912), Harden/Hardin/Hardeng entry for Benjamin, son of Jean, baptized 30 May 1730, C.R.1; PDF at https://commons.wikimedia.org/wiki/File:Vital_records_of_Abington,_Massachusetts,_to_the_year_1850_.._(IA_vitalrecordsofab02abing).pdf. The abbreviation "bp." means baptized, and C.R.1 identifies the First Church of Abington record source. Source ID: <code>abington-vr-1850-vol1</code>. <a class="citation-back" href="#ref-1">↩</a></li>
```

```html
<li id="n4">Two marriages — to Elizabeth Harden and to Mercy Noyes — recorded in <code>data/ancestors v26.json</code>, G9 entry; specific dates and marriage records not yet captured here. <a class="citation-back" href="#ref-4">↩</a></li>
```

```html
<li id="n5">Massachusetts. Probate Court (Plymouth County), <em>Probate records, 1686–1903; with index and docket, 1685–1967</em>, Plymouth County Probate Court record book, manuscript pp. 383–384, will of John Harden of Bridgewater, Plymouth County, Massachusetts, blacksmith, dated 17 September 1751, proved 7 October 1751; FamilySearch catalog https://www.familysearch.org/en/search/catalog/277512; p. 383 image https://www.familysearch.org/ark:/61903/3:1:3QSQ-G97D-F6PW; p. 384 image https://www.familysearch.org/ark:/61903/3:1:3QS7-897D-FXDF. The will names daughter Jane Spear and gives "my grandson Benjamin Gurney" twenty shillings; Elizabeth Harden appears as a witness. Source ID: <code>plymouth-probate-john-harden-1751-will</code>. <a class="citation-back" href="#ref-5">↩</a></li>
```

Add before the closing `</ol>`:

```html
<li id="n9"><em>Vital Records of Abington, Massachusetts, to the Year 1850</em>, vol. 1, John and Mary Harden/Hardin family entries for Mary, Sarah, Jean, Rebecca/Rebacka, Lydia, and John; John Harden will, pp. 383–384, naming daughter Sarah Gurney. Sarah Harden Gurney is a plausible aunt-household candidate, but the current evidence does not prove guardianship or upbringing. Source IDs: <code>abington-vr-1850-vol1</code>; <code>plymouth-probate-john-harden-1751-will</code>. <a class="citation-back" href="#ref-9">↩</a></li>
<li id="n10">"John Gurney, US 1636," <em>The Neverending Hobby</em>, public compiled genealogy, https://sites.google.com/site/theneverendinghobby/home/those-connected-to-more-than-one-family/john-gurney-us-1636. Use as secondary compiled genealogy for the identification of Benjamin Gurney G10 as father through Jane/Jean Harden; the Abington baptism itself does not name the father. Source ID: <code>neverending-hobby-john-gurney-us-1636</code>. <a class="citation-back" href="#ref-10">↩</a></li>
```

### 7.6 Ensure all new footnote references resolve

After edit, ensure:

- every `href="#n9"` has `id="n9"` in the citation list
- every `href="#n10"` has `id="n10"` in the citation list
- no duplicate `id="ref-5"` values are introduced; if duplicates occur, append suffixes such as `ref-5c`

---

## 8. Update G10 fact sheet

Update `fact-sheets/g10-benjamin-gurney-fact-sheet.md` with targeted edits.

### 8.1 Front matter

Set:

```yaml
updated: 28 April 2026
```

Revise `subtitle` to:

```yaml
subtitle: "Ancestor fact sheet for G10 in the direct Gurney line. Plymouth County farmer identified by secondary genealogy as father of Benjamin (G9) through Jane/Jean Harden before his 1731 marriage to Sarah Morse; later associated with Middleboro and Rochester."
```

### 8.2 Vital "Marriage / Liaisons" field

Replace the Jane Harden line with:

```html
<div><strong>Jane / Jean Harden</strong> — likely non-marital liaison prior to marriage; best-supported mother of Benjamin (G9). The Abington baptism names Benjamin as son of Jean but does not name the father; John Harden's will confirms Benjamin as Harden grandson. <sup class="fn"><a href="#n4" id="ref-4">4</a></sup><sup class="fn"><a href="#n8" id="ref-8">8</a></sup></div>
```

Replace the Sarah Morse line with:

```html
<div><strong>Sarah Morse</strong> — married 14 June 1731, Middleborough, Massachusetts, per marriage index. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></div>
```

### 8.3 Highlight: fathered Benjamin outside marriage

Replace the current second highlight bullet with:

```html
<li><strong>Likely father of Benjamin (G9) through Jane/Jean Harden.</strong> Secondary compiled genealogy identifies G10 as the father of Benjamin (G9), baptized at Abington in 1730 as Benjamin, son of Jean. The primary baptism does not name the father, so this should be treated as a strong compiled-genealogy identification supported by the Harden-side record chain, not as a direct baptismal statement. <sup class="fn"><a href="#n4" id="ref-4b">4</a></sup><sup class="fn"><a href="#n8" id="ref-8b">8</a></sup></li>
```

### 8.4 Narrative paragraph 1

Replace the current first narrative paragraph with:

```html
<p>Benjamin Gurney G10 lived his entire life within the working farms and small towns of eastern Plymouth County, Massachusetts. He was born around 1704 at Weymouth, into the household of his father Benjamin G11 and Rebecca Staples; he reached adulthood in the Abington–Whitman line area, where the family had held land since the previous generation. The difficult opening event of his adult life should now be stated with sharper evidence discipline: secondary compiled genealogy identifies him as the father of Benjamin (G9), who was baptized at Abington on 30 May 1730 as Benjamin, son of Jean. The newly located John Harden will confirms that the child later known as Benjamin Gurney was John Harden's grandson and makes Jane/Jean Harden Spear the best-supported mother, but neither the baptism nor the will directly names G10 as father. <sup class="fn"><a href="#n1" id="ref-1b">1</a></sup><sup class="fn"><a href="#n4" id="ref-4c">4</a></sup><sup class="fn"><a href="#n8" id="ref-8c">8</a></sup></p>
```

### 8.5 Children table

Replace the first Benjamin row with:

```html
<tr><td>Benjamin Gurney</td><td>bpt. 30 May 1730 – d. 28 Sept. 1805</td><td>Jane / Jean Harden</td><td>G9 in direct line; baptized as Benjamin, son of Jean; later confirmed as John Harden's grandson. Father identification rests on secondary compiled genealogy and the broader evidence chain. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup><sup class="fn"><a href="#n8" id="ref-8d">8</a></sup></td></tr>
```

Add a later Benjamin row after Lemuel and before Levi if the table does not already include him:

```html
<tr><td>Benjamin Gurney</td><td>b. c. 1743</td><td>Sarah Morse</td><td>Later same-name half-brother; likely distinct from G9 and relevant to the Rochester homestead / two-Benjamin disambiguation problem. <sup class="fn"><a href="#n4" id="ref-4d">4</a></sup></td></tr>
```

### 8.6 Paragraph below children table

Replace with:

```html
<p><em>The family has a two-Benjamin problem. Benjamin G9, baptized in 1730 as son of Jean/Jane Harden, is distinct from the later Benjamin in the Sarah Morse child set who appears to fit the Rochester homestead division and later Middleborough/Rochester records. <sup class="fn"><a href="#n4" id="ref-4e">4</a></sup><sup class="fn"><a href="#n6" id="ref-6d">6</a></sup><sup class="fn"><a href="#n8" id="ref-8e">8</a></sup></em></p>
```

### 8.7 Citations list

Replace citations `n4`, `n5`, and `n7`; add `n8`.

```html
<li id="n4">"John Gurney, US 1636," <em>The Neverending Hobby</em>, public compiled genealogy, https://sites.google.com/site/theneverendinghobby/home/those-connected-to-more-than-one-family/john-gurney-us-1636. Use as secondary compiled genealogy for the G10 / Jane Harden relationship, G10's identification as father of Benjamin G9, the Sarah Morse child set, and the later same-name Benjamin. Source ID: <code>neverending-hobby-john-gurney-us-1636</code>. <a class="citation-back" href="#ref-4">↩</a></li>
```

```html
<li id="n5">Middleborough Public Library, "Marriages by Men's Name," marriage index PDF, entry for Benjamin Gurney and Sarah Morse, 14 June 1731; https://midlib.org/sites/midlib.org/files/images/marriages%20by%20mens%20name.pdf. Source ID: <code>middleborough-marriages-by-mens-name</code>. <a class="citation-back" href="#ref-5">↩</a></li>
```

```html
<li id="n7">See <a href="/fact-sheets/g09-benjamin-gurney-fact-sheet.html">Benjamin Gurney (G9) fact sheet</a>; G9's baptism is recorded in <em>Vital Records of Abington, Massachusetts, to the Year 1850</em>, vol. 1, as Benjamin, son of Jean, baptized 30 May 1730, C.R.1. Source ID: <code>abington-vr-1850-vol1</code>. <a class="citation-back" href="#ref-7">↩</a></li>
```

Add before `</ol>`:

```html
<li id="n8">Massachusetts. Probate Court (Plymouth County), <em>Probate records, 1686–1903; with index and docket, 1685–1967</em>, Plymouth County Probate Court record book, manuscript pp. 383–384, will of John Harden of Bridgewater, Plymouth County, Massachusetts, blacksmith, dated 17 September 1751, proved 7 October 1751; FamilySearch catalog https://www.familysearch.org/en/search/catalog/277512; p. 383 image https://www.familysearch.org/ark:/61903/3:1:3QSQ-G97D-F6PW; p. 384 image https://www.familysearch.org/ark:/61903/3:1:3QS7-897D-FXDF. The will confirms Benjamin Gurney as John Harden's grandson and names daughter Jane Spear; it does not name Benjamin Gurney G10 as father. Source ID: <code>plymouth-probate-john-harden-1751-will</code>. <a class="citation-back" href="#ref-8">↩</a></li>
```

---

## 9. G11 fact sheet and companion

No G11 fact-sheet or companion replacement is required in this patchset.

If Phase 2 elects to add a note, keep it only in `research/people/g11-benjamin-gurney-fact-sheet.research.md` under a short heading such as `### Relation to the Harden/Gurney update`, and use this exact text:

```markdown
### Relation to the Harden/Gurney update

The John Harden 1751 will update does not materially change G11's own profile. Its value for the G11/G10/G9 sequence is indirect: it strengthens the Harden-side identification of G9 and sharpens the need to distinguish G9 from the later Benjamin in G10's Sarah Morse household. G11 still needs direct examination of his own Plymouth probate and deed records as a separate task.
```

Do not add this optional note if the G11 companion is otherwise stable and Phase 2 is trying to minimize churn.

---

## 10. Validation commands

After applying the patchset, run:

```bash
python -m json.tool "data/sources.json" > /tmp/sources.json.validated
python -m json.tool "data/ancestors v26.json" > /tmp/ancestors-v26.json.validated
```

Then search for dangling source IDs introduced by this patchset:

```bash
grep -R "plymouth-probate-john-harden-1751-will\|abington-vr-1850-vol1\|hobart-abington-1839\|neverending-hobby-john-gurney-us-1636\|middleborough-marriages-by-mens-name\|benjamin-gurney-harden-research-tables-2026-04" -n data fact-sheets research sources | cat
```

Expected: all introduced source IDs should appear in `data/sources.json`; citations should appear in the relevant fact sheets/research companions; validation and corpus supplement paths should exist.

If the repo has the usual validation/build commands available, also run:

```bash
npm run validate
npm run package
```

If those commands are unavailable on the local machine, record that they were not run.

---

## 11. Commit message suggestion

```text
Update Benjamin Gurney Harden evidence chain
```

Longer commit body:

```text
Promote John Harden 1751 will evidence and related Harden/Gurney research into canonical data, fact sheets, and research companions.

- Add John Harden will and related Harden/Gurney source entries
- Confirm Benjamin Gurney as John Harden grandson
- Reframe Jane/Jean Harden Spear as likely mother, not overproved
- Downgrade aunt-upbringing tradition to plausible but unproved
- Clarify that G10 fatherhood is secondary-genealogy supported, not named in baptism
- Preserve two-Benjamin disambiguation in G10 household
```
