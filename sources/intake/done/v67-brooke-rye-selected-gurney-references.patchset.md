**Done:** 2026-05-28 19:17 PT

# v67 patchset — Brooke and Rye selected Gurney references

Prepared: 2026-05-28  
Phase: 1 preparation  
Scope: corrected Phase-1 intake patchset for seven already-captured page images under `sources/intake/processed/`.

## Correction to prior passes

The earlier work was wrong in three material ways:

1. **Brooke page 200/201 was misread.** Page 201 explicitly contains **Hugh Gurney**: Brooke quotes Doctor Powell's Welsh-description tradition that Walter de Eureux, Earl of Salisbury, and Hugh Gurney were hurt near Cardiff and later died in Normandy. Page 200 is retained because it supplies the immediately preceding Salisbury/Patrick de Eureux setup for the page-201 passage.
2. **Brooke page 92 was misclassified.** The supplied transcription contains a separate **Hugh Gurney** reference: Millicent, daughter of Hugh Gurney and Julian his wife (sister to Reginald Earl Bullen), married Almeric/Amaury Mountfort, Earl of Évreux/Gloucester by right of his mother Mabel, and later William Cantelupe. This is the **senior-line Hugh V de Gournay** (forfeited 1205) with his wife Juliana de Dammartin and her brother Renaud de Dammartin, Count of Boulogne — already a recognized senior-collateral figure cluster in the project.
3. **Rye page transcriptions must preserve pedigree structure.** The selected Rye pages are not prose. They are tree diagrams. The durable transcription therefore uses nested pedigree form to preserve parent-child and spouse relationships.

## Correction to this preparation pass

A second-AI review (2026-05-28) identified two transcription errors and one research-routing miss that this patchset now reflects:

- **Rye p. 141 nesting was wrong.** The original draft nested Henry's later sons (`5. Anthony`, `6. Francis`, `7. Leonard`) and the unnumbered daughters (Elizabeth Salford, Mary s.p., Anne Osburne, Abigail) as children of Henry's eldest son Thomas Gurney + Martha Lewknor. The visitation numbering, picking up at 5/6/7 after Bassingborne (4), shows these are Henry's continuing children, matching the project's standing fact that Francis G14 is Henry G15's sixth son. The transcription block below is corrected.
- **Rye p. 141 names Henry's third son as "Edward."** The project (DG-I pedigree p. 287; G15 fact-sheet) identifies that son as **Edmund Gurney the divine** (Cambridge, DNB entry, Rector of Harpley 1620–1648). The visitation's "Edward" is an early-modern variant or scribal error for Edmund. Worth flagging in research, not silently reconciled.
- **Rye p. 40 also carries Blennerhasset material.** The top half of p. 40 is the tail of a Blennerhasset/Bleverhassett pedigree, which is directly relevant to G15 Henry's wife Ellen Blennerhasset of Barsham. The transcription now captures the visible Blennerhasset content as well as the Blundeville pedigree.

## Source tracking

Two new source IDs are proposed:

- `brooke-catalogue-succession-1619` — Ralph Brooke, *A Catalogue and Succession of the Kings, Princes, Dukes, Marquesses, Earles, and Viscounts of this Realme of England, since the Norman Conquest, to this Present Yeare, 1619* (London: William Jaggard, 1619), Internet Archive item `cataloguesuccess00broo`.
- `rye-visitacion-norffolk-1891` — William Hervey, Robert Cooke, and John Raven, *The Visitacion of Norffolk...*, ed. Walter Rye (London: Harleian Society, 1891), Internet Archive item `visitacionnorff00ravegoog`.

Existing repo search did not surface either proposed source ID in `data/sources.json`, `sources/corpus_supplement/`, or `sources/media/`.

## Research-value assessment

### Brooke, *Catalogue and Succession* (1619)

1. **Page 92 — Hugh Gurney as father of Millicent — senior-collateral content.** Brooke's Gloucester/Évreux/Mountfort passage names Millicent as daughter of Hugh Gurney and Julian his wife, sister to Reginald Earl Bullen; her first husband Almeric Mountfort, Earl of Évreux (later briefly Earl of Gloucester in right of his mother Mabel, eldest daughter of William Earl of Gloucester) brought her the manor of Hanston but they had no issue; Almeric was buried at the Monastery of Keynsham. Millicent then married William Cantelupe and had Thomas Cantelupe (later Bishop of Hereford, canonized in 1320) and Julian Cantelupe (m. Robert Tregoz, Lord of Ewias Harold). This is the **senior Gournay baron line** — "Hugh Gurney" here is Hugues V de Gournay (the lord forfeited in 1205), "Julian/Iulian" is Juliana de Dammartin, and "Reginald Earl Bullen" is Renaud de Dammartin, Count of Boulogne (the loser at Bouvines, 1214). Modern reference scholarship (FMG MedLands) records two daughters of Hugues V: Juliana de Gournay (m. William Bardolf of Wormegay) and Millicent (m. Amaury de Montfort then William de Cantilupe). Brooke is an early-modern printed witness to Millicent's marital line not yet present in `research/topics/senior-gournay-baron-line-collateral.md`, which currently covers Hugues V's career, foundations, and death in 1214 English exile but does not name Millicent or the Cantelupe / Tregoz descent. Destination: senior-collateral topic file (additive paragraph, with the Cantelupe / Tregoz human-interest detail — Thomas Cantelupe is the only canonized saint reachable by marriage from the Gournay senior line).
2. **Pages 200-201 — Hugh Gurney in the Cardiff/Powell death tradition.** Page 201 quotes Doctor Powell's *Historie of Cambria* (1584) for the claim that, about 1094, Roger Montgomery, William Fitz-Eustace, and Arnold Harecourt were slain near Cardiff, while Walter de Eureux, Earl of Salisbury, and Hugh Gurney were hurt and later died in Normandy. This is a Welsh-marcher antiquarian transmission of the Cardiff death tradition already attached to **Hugh II de Gournay (G34)** in the project (Pattou companion places G34's Cardiff death at 1074). Brooke's 1094 dating is twenty years late; pairing Hugh Gurney with Walter d'Évreux Earl of Salisbury is also chronologically problematic (the first Walter d'Évreux of Salisbury is the mid-12th-century figure, not the 1090s). The Powell tradition therefore looks like a conflation. Destination: G34 (`research/people/g34-hugh-de-gournay-ii-fact-sheet.research.md`) and the existing Cardiff/death-tradition material across G33–G34 and `research/topics/dg-reception-delisle-critique.md`. Cite as Brooke transmitting Powell, not as independent evidence; record the chronological conflict.

### Rye, *Visitacion of Norffolk* (1891)

1. **Page 40 (lower) — Blundevill / Gorney of Barsham alliance.** The Blundevill pedigree makes Constance, wife of Rafe Blundevill of Newton Flotman (d. 1514), a daughter of William Gorney of Bassam/Barsham. This corroborates the Constance Gurney marriage **already published** in `fact-sheets/g19-william-gurney-iv-fact-sheet.md` (child table n12; "Married (1) Ralf Blundeville, (2) William Bokenham"). Destination: add Rye p. 40 as an additional independent witness in the G19 fact sheet n12 footnote and the G19 research companion. Preserves the visitation spelling form `Gorney`.
2. **Page 40 (upper) — Blennerhassett pedigree tail — relevant to G15 Henry's wife.** The top half of p. 40 carries the close of a Blennerhassett of Norfolk pedigree (Sir Edward Blever[hassett] of Horsford by Norwich; Rafe Blennerhassett with descendants in Ireland; daughter of Death of Gimingham). G15 Henry Gurney's wife is Ellen Blennerhasset of Barsham; the Blennerhassett family is already in the G15 research apparatus. Destination: record the visible Blennerhassett text in the corpus extract; flag for `research/people/g15-henry-gurney-fact-sheet.research.md` and any future Blennerhassett-family research note. This patchset does not promote a specific Blennerhassett claim — it only captures the source content.
3. **Page 132 — West Barsham / Cawston / Aylsham cadet branch.** The Gourney pedigree starts from Thomas `[William ?]` Gurney of West Bassant `[Barsham]`, then traces Walter Gurney of Cley/Elay and his Cawston/Aylsham descendants. This corroborates the **already-published** cadet branch in `fact-sheets/g19-william-gurney-iv-fact-sheet.md` (child table: "Walter Gurney of Cley-by-the-Sea ... ancestor of the Gurneys of Cawston and Aylsham"). The visitation's `Thomas [William ?]` apex is a notable wrinkle — the printed source itself flags ambiguity between Thomas and William as the pedigree head, which is consistent with the project's reading of William G19 as Walter's father (with Walter's 1495-96 land grant per G19 fact sheet, n14). Destination: add Rye p. 132 to G19 fact sheet n13 footnote and G19 research companion; preserve the arms detail (*Argent, a cross engrailed gules, a crescent for difference*) and Walter's wife (Margaret Moore of Wolterton). Note that this Walter is **not** the G31 Walter de Gournay of the junior Norfolk-branch founding (standing-fact #2 in `AGENTS.md` §6); these are two different Walters separated by ~300 years.
4. **Pages 140-141 — direct-line Gurney pedigree.** The Gurney pedigree gives Anthony Gurney → Francis Gurney of West Barsham and Ellen Holdich of Ranworth → Henry Gurney of Great Ellingham and Ellen Blennerhasset of Barsham → Thomas Gurney of West Barsham (m. Martha Lewknor of Denham) plus Henry's continuing children numbered `5. Anthony` / `6. Francis` / `7. Leonard` with daughters Elizabeth (m. Salford of London), Mary (s.p.), Anne (m. Thomas Osburne of Mundham), and Abigail. This is a compact visitation witness for the **already-published** G17 → G16 → G15 → G14 direct line, particularly:
   - G17 Anthony Gurney: pedigree apex, named by the visitation.
   - G16 Francis Gurney and Ellen Holdich of Ranworth: corroborates the Holdich marriage already in `fact-sheets/g16-francis-gurney-fact-sheet.md` and `research/people/g16-francis-gurney-fact-sheet.research.md`.
   - G15 Henry Gurney of Great Ellingham and Ellen Blennerhasset of Barsham: corroborates `fact-sheets/g15-henry-gurney-fact-sheet.md`, the children-table order Thomas/Henry/Edward[Edmund]/Bassingborne, and the placement of Anthony+Francis as twins at 5/6.
   - G14 Francis Gurney as Henry's sixth son: corroborates the project's standing fact #4 and the G14 fact sheet vital ("13 September 1581 ... sixth son of Henry Gurnay, Esq."). Note: the visitation's `3. Edward.` is an early-modern variant or scribal error for **Edmund** the divine (Cambridge B.D., Rector of Harpley 1620–1648, DNB entry); not to be silently reconciled.
   Destination: add Rye pp. 140-141 as an additional citation across the G14, G15, G16, and G17 research companions (and optionally as a supporting footnote in each fact sheet). This patchset records the routing but does **not** modify the fact sheets — fact-sheet-side citation insertion is a separate user-directed task.

## Outcomes

| Item | Files | Outcome | Destination |
|---|---|---|---|
| 1 | `page92.png`, `page200.png`, `page201.png` | promote | `sources/media/brooke-catalogue-succession-1619/`, `sources/corpus_supplement/`, `sources/validations/`, `research/topics/brooke-rye-selected-gurney-references.md`; downstream routing (deferred) to senior-collateral topic file (Hugues V / Millicent / Cantelupe) and G34 companion (Cardiff/Powell) |
| 2 | `Visitation-page40.png`, `Visitation-page132.png`, `Visitation-page140.png`, `Visitation-page141.png` | promote | `sources/media/rye-visitacion-norffolk-1891/`, `sources/corpus_supplement/`, `sources/validations/`, `research/topics/brooke-rye-selected-gurney-references.md`; downstream routing (deferred) to G14, G15, G16, G17, G19 research companions for direct-line corroboration |

No item is rejected.

## Phase 2 operations

### 1. Promote Brooke page images to media

Run these file moves:

```bash
mkdir -p sources/media/brooke-catalogue-succession-1619
git mv sources/intake/processed/page92.png sources/media/brooke-catalogue-succession-1619/page092-gloucester-mountfort-hugh-gurney-millicent.png
git mv sources/intake/processed/page200.png sources/media/brooke-catalogue-succession-1619/page200-salisbury-patricke-de-eureux-context.png
git mv sources/intake/processed/page201.png sources/media/brooke-catalogue-succession-1619/page201-salisbury-hugh-gurney-cardiff-powell.png
```

### 2. Promote Rye page images to media

Run these file moves:

```bash
mkdir -p sources/media/rye-visitacion-norffolk-1891
git mv sources/intake/processed/Visitation-page40.png sources/media/rye-visitacion-norffolk-1891/page040-blennerhassett-tail-and-blundevill-constance-gorney-barsham.png
git mv sources/intake/processed/Visitation-page132.png sources/media/rye-visitacion-norffolk-1891/page132-gourney-west-barsham-cawston-aylsham.png
git mv sources/intake/processed/Visitation-page140.png sources/media/rye-visitacion-norffolk-1891/page140-gurney-anthony-francis-west-barsham.png
git mv sources/intake/processed/Visitation-page141.png sources/media/rye-visitacion-norffolk-1891/page141-gurney-henry-great-ellingham-francis-sixth-son.png
```

### 3. Update `data/sources.json` lastUpdated

File: `data/sources.json`

```str_replace
old_string:
    "lastUpdated": "2026-05-25",
new_string:
    "lastUpdated": "2026-05-28",
```

### 4. Add source entries to `data/sources.json`

File: `data/sources.json`

```str_replace
old_string:
    "norwich-records-hudson-tingey-vol2": {
      "shortTitle": "Hudson and Tingey -- Records of the City of Norwich, vol. ii (1910)",
      "citation": "William Hudson and John Cottingham Tingey, eds., The Records of the City of Norwich (Norwich and London: Jarrold, 1910), vol. ii.",
      "archive": "Internet Archive",
      "url": "https://archive.org/details/recordsofcityofn02norwuoft",
      "corpusStatus": "supplement",
      "corpusPath": "sources/corpus_supplement/norwich-records-hudson-tingey-vol2-edmund-gornay-fees.md",
      "mediaPath": null,
      "validationPath": null,
      "notes": "Vol. ii of the Hudson-Tingey edition. Used in v63 for the City Treasurers' Accounts entries at pp. 44 and 47 recording two annual fee payments of 20 shillings each to 'Edmund Gornay', paid in the same fee paragraph as the 20s paid to Edmund de Clipesby. Direct primary attestation behind Blomefield's general standing-counsel reference and the History of Parliament biography of Sir John Gurney V."
    }
  }
}
new_string:
    "norwich-records-hudson-tingey-vol2": {
      "shortTitle": "Hudson and Tingey -- Records of the City of Norwich, vol. ii (1910)",
      "citation": "William Hudson and John Cottingham Tingey, eds., The Records of the City of Norwich (Norwich and London: Jarrold, 1910), vol. ii.",
      "archive": "Internet Archive",
      "url": "https://archive.org/details/recordsofcityofn02norwuoft",
      "corpusStatus": "supplement",
      "corpusPath": "sources/corpus_supplement/norwich-records-hudson-tingey-vol2-edmund-gornay-fees.md",
      "mediaPath": null,
      "validationPath": null,
      "notes": "Vol. ii of the Hudson-Tingey edition. Used in v63 for the City Treasurers' Accounts entries at pp. 44 and 47 recording two annual fee payments of 20 shillings each to 'Edmund Gornay', paid in the same fee paragraph as the 20s paid to Edmund de Clipesby. Direct primary attestation behind Blomefield's general standing-counsel reference and the History of Parliament biography of Sir John Gurney V."
    },
    "brooke-catalogue-succession-1619": {
      "shortTitle": "Brooke, Catalogue and Succession (1619)",
      "citation": "Brooke, Ralph. A Catalogue and Succession of the Kings, Princes, Dukes, Marquesses, Earles, and Viscounts of this Realme of England, since the Norman Conquest, to this Present Yeare, 1619. London: William Jaggard, 1619.",
      "archive": "Internet Archive",
      "url": "https://archive.org/details/cataloguesuccess00broo",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/brooke-catalogue-succession-1619-selected-gurney-pages.md",
      "mediaPath": "sources/media/brooke-catalogue-succession-1619/",
      "validationPath": "sources/validations/brooke-catalogue-succession-1619.md",
      "notes": "Public-domain early printed heraldic/genealogical catalogue. Selected page images transcribed in v67: page 92 naming Millicent as daughter of Hugh Gurney and Julian his wife; page 200 as setup for Patrick de Eureux / Salisbury; page 201 quoting Doctor Powell for Hugh Gurney wounded near Cardiff and later dying in Normandy. Use as early printed derivative evidence for senior Gournay-line traditions, not as primary proof."
    },
    "rye-visitacion-norffolk-1891": {
      "shortTitle": "Rye, Visitacion of Norffolk (1891)",
      "citation": "Hervey, William; Cooke, Robert; and Raven, John. The Visitacion of Norffolk, Made and Taken by William Hervey, Clarencieux King of Arms, Anno 1563; Enlarged with Another Visitacion Made by Clarenceux Cooke, with Many Other Descents; and also the Vissitation Made by John Raven, Richmond, Anno 1613. Edited by Walter Rye. London: Harleian Society, 1891.",
      "archive": "Internet Archive",
      "url": "https://archive.org/details/visitacionnorff00ravegoog",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/rye-visitacion-norffolk-1891-gurney-selected-pages.md",
      "mediaPath": "sources/media/rye-visitacion-norffolk-1891/",
      "validationPath": "sources/validations/rye-visitacion-norffolk-1891.md",
      "notes": "Harleian Society edition of the Norfolk visitations of 1563, 1589, and 1613. Selected Gurney/Gorney/Gourney pages transcribed in v67: printed pp. 40, 132, 140, and 141. High value for direct-line Francis G16, Henry G15, and Francis G14 parentage/sibling ordering; also useful for collateral Barsham/Cawston/Aylsham and Blundevill-alliance Gorney variants."
    }
  }
}
```

### 5. Write Brooke corpus supplement

New file write: `sources/corpus_supplement/brooke-catalogue-succession-1619-selected-gurney-pages.md`

```markdown
# Brooke, Catalogue and Succession (1619) — selected Gurney page transcriptions

Source ID: `brooke-catalogue-succession-1619`

Source: Ralph Brooke, *A Catalogue and Succession of the Kings, Princes, Dukes, Marquesses, Earles, and Viscounts of this Realme of England, since the Norman Conquest, to this Present Yeare, 1619* (London: William Jaggard, 1619), Internet Archive item `cataloguesuccess00broo`.

Images transcribed:

- `sources/media/brooke-catalogue-succession-1619/page092-gloucester-mountfort-hugh-gurney-millicent.png`
- `sources/media/brooke-catalogue-succession-1619/page200-salisbury-patricke-de-eureux-context.png`
- `sources/media/brooke-catalogue-succession-1619/page201-salisbury-hugh-gurney-cardiff-powell.png`

Transcription note: semi-diplomatic transcription from page images and user-corrected page text. Long-s is normalized to modern `s`; original spelling, capitalization, and punctuation are otherwise preserved where practical. The supplied page 92 transcription is retained as the controlling correction for this patchset because the prior local render used in the first pass did not match the user's intended Brooke p. 92 capture.

## Research value

Brooke supplies two Hugh Gurney references, both bearing on the senior Norman line rather than the direct West Barsham descent:

1. **Page 92 — Hugues V de Gournay and the Mountfort / Cantelupe daughter-line.** Brooke names Millicent (Millescent) as daughter of Hugh Gurney and Julian his wife (sister to Reginald Earl Bullen), wife first of Almeric/Amaury Mountfort, Earl of Évreux (briefly Earl of Gloucester in right of his mother Mabel), then of William Cantelupe — with downstream children Thomas Cantelupe Bishop of Hereford (canonized 1320) and Julian Cantelupe (m. Robert Tregoz, Lord of Ewias Harold). The "Hugh Gurney + Julian" couple is identifiable as Hugues V de Gournay (forfeited 1205) and Juliana de Dammartin; Reginald is Renaud de Dammartin, Count of Boulogne. This is a printed-source witness to the Millicent half of the two-daughter cluster recorded by Cawley (FMG MedLands), corroborating an already-recognized senior-collateral pattern not yet narrated in the project's senior-line topic file.
2. **Pages 200-201 — Doctor Powell's Cardiff death tradition.** Brooke transmits David Powell's *Historie of Cambria* (1584) for a c. 1094 Cardiff wounding of "Hugh Gurney" and Walter d'Évreux of Salisbury. This intersects the project's existing Cardiff death tradition for G34 Hugh II de Gournay, but with chronological problems (Brooke's 1094 dating is twenty years late on the project's reading; the paired Walter d'Évreux of Salisbury identification is a mid-12th-century figure, not a 1090s one). Use as a late, derivative witness to the Cardiff tradition; record the chronological discrepancy when routing to G34.

Both pages are derivative early-modern printed witnesses. They are useful for the senior Gournay line and for the Cardiff/death-tradition problem, but they do not substitute for primary charter, chronicle, or IPM evidence.

## Page 92 — Almeric Mountfort / Millicent daughter of Hugh Gurney

Working heading: Gloucester / Earls of Gloucester context.

> Almerick Mountfort, Earle of Eureux in Normandy, after the diuorce of King Iohn, from his wife Isabell, yongest daughter & co-heire of Will: Earle of Glocefter, was the next Earle of Glocefter, in right of his mother Mabell, eldest daughter and heire of the fore-said William Earle of Glocefter, in the second yeare of king Iohn. He maried Millescent, daughter of Hugh Gurney and of Iulian his wife, sister to Reginald Earle Bullen, and had with her in marriage, the Mannor of Hanston, but by her had no issue. She was after married to William Cantelape, and had issue, Thomas Bishop of Hereford, and Iulian married to Robert Tregoz, Lord of Ewias Herald.
>
> Almerick dyed, and was buried in the Monastery of Kenisham.
>
> Et portoit, de gueulles party & endente d'argent de six pieces.

### Structured relationship extraction

- Hugh Gurney = Julian, sister to Reginald Earl Bullen.
  - *Identifications (per Cawley, Medieval Lands, SEIGNEURS de GOURNAY):* Hugh Gurney = **Hugues V de Gournay** (the lord forfeited in 1205); Julian = **Juliana de Dammartin**; Reginald Earl Bullen = **Renaud de Dammartin, Count of Boulogne** (defeated at Bouvines, 1214). Brooke is a late printed witness to a family cluster already documented in modern reference scholarship.
  - Millicent / Millescent, daughter of Hugh Gurney and Julian. *Second daughter of Hugues V; her sister Juliana de Gournay married William Bardolf of Wormegay (by whom the senior English lands passed to the Bardolfs).*
    - married Almeric / Almerick Mountfort, Earl of Évreux in Normandy (Amaury de Montfort, d. 1213); briefly Earl of Gloucester in right of his mother Mabel; by Millicent he had the manor of Hanston; no issue. Buried at the monastery of Keynsham (Somerset).
    - later married William Cantelupe (William de Cantilupe, d. 1239).
      - Thomas Cantelupe, Bishop of Hereford — **canonized in 1320**; the only saint reachable by marriage from the Gournay senior line.
      - Julian Cantelupe, married Robert Tregoz, Lord of Ewias Harold.

## Page 200 — Earls of Salisbury setup for page 201

Heading: `A CATALOGVE OF THE Earles of Salisbury, their Armes, Wiues, and Children.`

> Patricke de Eureux, (sonne of Walter de Eureux, Earle of Rosmer, and Sibill his wife, Founders of the Monastery of Bradenstoke, 1093.) was Steward of the house to Mauld the Empresse, by whose meanes the Earledome of Salisbury was confirmed vnto him, in the 28. yeare of king Henry the second. He married Ela, the widdow of William, the third Earle Warren and Surrey, daughter of William Taluase, Earle of Pontine, grand-childe to Roger Mountgomery, by his sonne Robert de Mountgomery Earle of Shrewsbury, by who he had issue, William Fitz-Patricke Earle of Salisbury and Rosemer,

## Page 201 — Hugh Gurney in the Cardiff / Doctor Powell tradition

Continuation from page 200:

> Rosemer, Patricke and Philip, Cannons at Bradenstock. This Patricke was a Witnesse to the Charter of pacification of the troubles betweene King Stephen, and Henry Duke of Normandy, 1152, and after was slaine in Aquitaine, by Guy de Lusignan, in comming as a Pilgrim from S. Iames de Compostella, and as the Priory Booke of Lacok hath, the 6. Kalend of Aprill, 1168, and was buried at S. Hillaries, the 15. of king Henry the second; (Doctor Powell in his description of Wales, Fol.154, saith, that about the yeare, 1094. Roger Montgomery, William Fitz-Eustace, and Arnold Harecourt, were slaine neere Caer diffe in Wales; and Walter de Eureux Earle of Salisbury, and Hugh Gurney were hurt, and after dyed in Normandy) Which Walter was Father of this Patricke, which M. Camden denyeth to be Earle.
>
> Et portoit, d'azur six lyons rampant d'or, 3, 2, 1. arme & lampasse de gueulle.

### Structured relationship / event extraction

- Walter de Eureux, Earl of Salisbury / Rosmar.
  - Patrick de Eureux, son of Walter and Sibill; later Earl of Salisbury.
- Doctor Powell tradition as quoted by Brooke:
  - c. 1094, near Cardiff in Wales:
    - slain: Roger Montgomery; William Fitz-Eustace; Arnold Harecourt.
    - hurt and later died in Normandy: Walter de Eureux, Earl of Salisbury; Hugh Gurney.

### Chronological notes on the Powell tradition

The project (Pattou companion) attaches a Cardiff death tradition to **G34 Hugh II de Gournay** at c. 1074, twenty years earlier than Brooke / Powell's c. 1094. The c. 1094 dating is also chronologically incompatible with the standard biography of Walter d'Évreux, first Earl of Salisbury, who flourished in the mid-12th century rather than the 1090s — the named Walter is too early on Powell's dating for the Earl of Salisbury attribution to hold. The Powell version therefore reads as a marcher-tradition conflation. Use as a late, derivative witness; record the chronological discrepancy on the G34 companion.
```

### 6. Write Rye corpus supplement

New file write: `sources/corpus_supplement/rye-visitacion-norffolk-1891-gurney-selected-pages.md`

```markdown
# Rye, Visitacion of Norffolk (1891) — selected Gurney/Gorney/Gourney pedigree pages

Source ID: `rye-visitacion-norffolk-1891`

Source: William Hervey, Robert Cooke, and John Raven, *The Visitacion of Norffolk, Made and Taken by William Hervey, Clarencieux King of Arms, Anno 1563; Enlarged with Another Visitacion Made by Clarenceux Cooke, with Many Other Descents; and also the Vissitation Made by John Raven, Richmond, Anno 1613*, ed. Walter Rye (London: Harleian Society, 1891), Internet Archive item `visitacionnorff00ravegoog`.

Images transcribed:

- `sources/media/rye-visitacion-norffolk-1891/page040-blennerhassett-tail-and-blundevill-constance-gorney-barsham.png`
- `sources/media/rye-visitacion-norffolk-1891/page132-gourney-west-barsham-cawston-aylsham.png`
- `sources/media/rye-visitacion-norffolk-1891/page140-gurney-anthony-francis-west-barsham.png`
- `sources/media/rye-visitacion-norffolk-1891/page141-gurney-henry-great-ellingham-francis-sixth-son.png`

Transcription note: the printed pages are pedigree diagrams. The transcription below preserves relationship structure using nested bullets. Square brackets reproduce Rye's editorial bracketed corrections or expansions when visible. A question mark in brackets is retained where Rye printed one. `ux.` means wife of; `ob. s.p.` means died without issue.

## Page 40 — upper: Blennerhassett pedigree tail (relevant to G15 Henry's wife)

The top half of page 40 is the close of a Blennerhassett of Norfolk pedigree continued from page 39. Captured here for the Blennerhassett-family context of G15 Henry Gurney's wife Ellen Blennerhasset of Barsham, even though the page itself does not name Ellen directly.

### Structured transcription (upper)

- (continued from p. 39) Sir Edward Blever[hassett] of Norfolk, of Layes [Lowes/Loyes ?] by Norwich.
  - 4. Jeremy Bleverhassett of Wilton in co. Norfolk = Margaret daughter of John Lee of Toddenham in co. Norfolk.
    - Children: Rebecca (wife of Rob[ert] Bishop of Norwich); Mary; Ursula (ob. s.p.); Margaret; Susan; 2. Daniel or 5. Samuel; 3. Thomas; 4. Edward; Joane; Susan (ob. s.p.).
- 1. Rafe Blennerhassett = ... daughter & coheir of ... Death of Gimingham in Norfolk.
  - 2. Edward.
  - 3. Francis, in Ireland.
  - 4. Edward.

This block does not name Ellen Blennerhasset of Barsham specifically but anchors the visitation Blennerhassett surname in the same Norfolk milieu (Wilton; Loyes near Norwich; Gimingham; an Irish branch). Cross-reference to G15 research companion as standing context for the Blennerhassett alliance.

## Page 40 — lower: Blundevill pedigree, Constance daughter of William Gorney of Barsham

Heading: `Blundevile.`  
Manuscript reference: `Harl. 1552, ink fo. 135, pencil 129.`  
Arms: quarterly, including Blundevile and Ingloyse/Ynglose quarters; crescent for difference.

### Structured transcription (lower)

- Sir William Blundevill.
  - William Blundevill = Elizabeth daughter of ... Boswell.
    - Richard Blundevill of Newton Flockman `[Flotman]` in Norfolk, ob. 1409 = Catherine daughter and heir of Rob. Ynglose, esq.
      - 1. Rafe Blundevill of Newton Flockman in Norfolk, ob. 1514 = Constance daughter of William Gorney of Bassam in Norfolk `[Gurney of Barsham]`.
        - Later descendants continue on the lower part of the page, including Edward Blundevill, ob. 1568.
      - 2. Richard.
      - Catherine, wife of Henry Apliard.
      - Mary.

### Gurney-relevant extraction

- Constance Gorney / Gurney, daughter of William Gorney of Bassam / Barsham, married Rafe Blundevill of Newton Flotman, Norfolk, who died in 1514.
- This is a visitation witness for the Constance Gurney marriage already carried in the G19 William Gurney IV child table.

## Page 132 — Gourney pedigree: West Barsham, Cley, Cawston, Aylsham

Heading: `Gourney.`  
Manuscript reference: `Harl. 1552, ink fo. 48b, pencil 44b.`  
Arms: `Argent, a cross engrailed gules, a crescent for difference.`

### Structured transcription

- Thomas `[William ?]` Gurney of West Bassant `[Barsham]` in Norfolk, esq.
  - 1. William Gurney, eldest son.
  - 2. Walter Gurney of Elay `[Cley ?]` in Norfolk, 2 son = Margaret daughter to Edmund Moore of Wolterton in Norfolk, esq.
    - William Gourney of Cawston in Norfolk, eldest son = Ann daughter to William Wayte of Tytleshall in Norfolk, gent.
      - William Gourney of Cawston, eldest son = ... daughter of ... Browne of Tacleston in Norfolk.
        - 1. Wolston, ob. s.p.
        - 2. Robert Gorney of Aylesham = Dorothy, widow of John Thompson of Aylesham.
        - Elizabeth, wife of Robert Cooke of Walcott.
        - Lucy, wife of Richard Johnson of Cawston.
      - Prudence, wife of Gilbert Parker of Honing in Norfolk.
      - Anne, wife of Edward Haman of Cawston in Norfolk, clerk.
  - 3. Thomas Gourney, 3 son.
  - 4. Christopher Gourney, a priest, 4 son.

### Gurney-relevant extraction

- Rye prints a collateral Gurney/Gourney/Gorney branch at West Barsham, Cley, Cawston, and Aylsham.
- The arms use the same base Gurney arms as the direct pedigree but with a crescent for difference, consistent with a cadet branch.
- Walter Gurney of Cley is the key branching figure; this aligns with the project fact-sheet note that Walter founded the Cley/Cawston/Aylsham cadet branch.

## Page 140 — Gurney pedigree, beginning: Anthony and Francis of West Barsham

Heading: `Gurney.`  
Manuscript reference: `Harl. 1552, ink fo. 53, pencil 49.`  
Arms: `Argent, a cross engrailed gules, in dexter chief point a cinquefoil azure.`

### Structured transcription

- Anthony Gurney.
  - Francis Gurney of West Bassam `[Barsham]` in Norfolk = Ellen daughter of ... Holdich of Ranworth in co. Norfolk.
    - Continued at page 141.

### Gurney-relevant extraction

- The pedigree begins the direct West Barsham line at Anthony Gurney, then gives Francis Gurney of West Barsham as Anthony's son and Ellen Holdich of Ranworth as Francis's wife.
- This is directly relevant to G17 Anthony, G16 Francis, and the Holdich connection.

## Page 141 — Gurney pedigree, continuation: Henry of Great Ellingham and children

Heading continues from p. 140: `Gurney.`

### Structured transcription

Reading note: the printed tree shows Henry's children in two visual rows. The top row gives the four numbered eldest sons (1 Thomas, 2 Henry, 3 Edward, 4 Bassingborne). The bottom row continues the same parental line — Henry's sons 5/6/7 (Anthony, Francis, Leonard) and four unnumbered daughters — visually positioned below Thomas's own children but numerically continuing Henry's son list. The transcription below reflects that numerical continuation.

- Francis Gurney of West Barsham in Norfolk = Ellen daughter of ... Holdich of Ranworth in co. Norfolk.
  - 1. Henry Gurney of Great Ellingham in Norfolk = Ellen daughter of John Blenerhasset of Barsham.
    - 1. Thomas Gurney of West Barsam in Norfolk = Martha daughter of Sir Edward Lewknor of Denham in co. Suffolk, near Newmarket.
      - 1. Edward.
      - 2. Thomas.
      - Susan.
      - Martha.
      - Ellen.
      - Margaret.
    - 2. Henry.
    - 3. Edward. *(printed `Edward`; this is the project's Edmund Gurney the divine — early-modern Edmund/Edward variant or scribal error. The DNB-entered Cambridge B.D. and Rector of Harpley 1620–1648 is identified as Edmund elsewhere; the visitation is the only known witness printing the name as Edward.)*
    - 4. Bassingborne, ob. s.p.
    - 5. Anthony.
    - 6. Francis.
    - 7. Leonard.
    - Elizabeth, wife of ... Salford of London.
    - Mary, s.p.
    - Anne, wife of Thomas Osburne of Mundham in Norfolk.
    - Abigail.
  - 2. Anthony.
  - 3. Thomas.
  - Elizabeth, wife of Thomas Golding of Fornham in Suffolk.

### Gurney-relevant extraction

- Henry Gurney of Great Ellingham is printed as the first child of Francis Gurney of West Barsham and Ellen Holdich.
- Henry's wife is Ellen, daughter of John Blennerhasset of Barsham.
- Thomas Gurney of West Barsham is printed as Henry's first son and married Martha Lewknor; Thomas's children are Edward, Thomas, Susan, Martha, Ellen, and Margaret.
- Henry's continuing children, picking up the son numbering at 5 after Bassingborne (4), are: 5. Anthony, 6. Francis, 7. Leonard, plus daughters Elizabeth (wife of ... Salford of London), Mary (s.p.), Anne (wife of Thomas Osburne of Mundham), and Abigail.
- The page is a compact independent visitation witness for **Francis G14 as Henry G15's sixth son** (matching project standing-fact #4 and the G14 fact-sheet vital "13 September 1581 ... sixth son of Henry Gurnay, Esq."), and for **Anthony G14a as twin / fifth son**. It also supplies the Norfolk gentry-marriage destinations for Henry's daughters: Salford of London, Osburne of Mundham.
- The `3. Edward` reading is the visitation's variant for **Edmund** the divine. The fact-sheet G15 / DG-I pedigree p. 287 / DNB entry are independent on the name; the visitation reading should be recorded but not treated as overriding.
```

### 7. Write cross-cutting research topic

New file write: `research/topics/brooke-rye-selected-gurney-references.md`

```markdown
# Brooke 1619 and Rye 1891 — selected Gurney references

This topic captures the research value of seven selected page images promoted in v67: Brooke 1619 pp. 92, 200, 201; and Rye 1891 printed pp. 40, 132, 140, 141. Full page transcriptions live in `sources/corpus_supplement/brooke-catalogue-succession-1619-selected-gurney-pages.md` and `sources/corpus_supplement/rye-visitacion-norffolk-1891-gurney-selected-pages.md`. The two sources hit very different parts of the line and are treated separately below.

## Brooke 1619 — Hugh Gurney in senior-line traditions (G33–G34 and Hugues V collateral)

### Page 92 — Millicent de Gournay, Mountfort, and the Cantelupe / Tregoz descent

Brooke makes Millicent (Millescent) the daughter of Hugh Gurney and Julian his wife, sister to Reginald Earl Bullen. Her first husband Almeric Mountfort, Earl of Évreux in Normandy, became Earl of Gloucester in right of his mother Mabel (eldest daughter of William Earl of Gloucester) in the second year of King John; he received the manor of Hanston with Millicent but had no issue by her, and was buried at the monastery of Keynsham. Millicent then married William Cantelupe and bore Thomas Cantelupe, Bishop of Hereford — canonized in 1320, the only saint reachable by marriage from the Gournay senior line — and Julian Cantelupe, who married Robert Tregoz, Lord of Ewias Harold.[^brooke-p92]

Identifications: "Hugh Gurney" here is **Hugues V de Gournay** (the lord forfeited in 1205); "Julian/Iulian his wife" is **Juliana de Dammartin**; "Reginald Earl Bullen" is **Renaud de Dammartin, Count of Boulogne** (defeated at Bouvines, 1214). Modern reference scholarship (Charles Cawley, *Medieval Lands*) records two daughters of Hugues V: Juliana de Gournay (m. William Bardolf of Wormegay — the line by which the senior English lands passed to the Bardolfs) and Millicent (m. Amaury de Montfort, then William de Cantilupe). Brooke is a useful early-modern printed witness for the Millicent half of that pair, which the project's existing senior-collateral coverage does not yet name. The page also preserves the Mountfort burial at Keynsham (Somerset) — a useful place anchor for any future senior-collateral place work.[^brooke-p92]

### Pages 200-201 — Doctor Powell's Cardiff death tradition

Page 201, continued from page 200, quotes David Powell's *Historie of Cambria* (1584) in the course of a Salisbury / Patrick de Eureux entry. Powell, as Brooke transmits him, says that about 1094 Roger Montgomery, William Fitz-Eustace, and Arnold Harecourt were slain near Cardiff, while Walter de Eureux Earl of Salisbury and Hugh Gurney were wounded there and later died in Normandy.[^brooke-p201]

This is another antiquarian witness to the long-running Cardiff death tradition for Hugh de Gournay, already attached to **G34 Hugh II de Gournay** in the project (Pattou companion places G34's Cardiff death at 1074). Brooke's c. 1094 dating is twenty years late against the project reading and is chronologically incompatible with the standard biography of Walter d'Évreux, first Earl of Salisbury, who flourished in the mid-12th century rather than the 1090s. The Powell version therefore looks like a marcher-tradition conflation. Use Brooke as a late, derivative witness to the Cardiff problem, not as independent evidence; record the chronological discrepancy in the G34 companion.[^brooke-p201]

## Rye 1891 — Norfolk visitation corroboration for G14 – G19

The Rye visitation pages all corroborate published Norfolk-branch facts; none introduces a new identification. The patchset routes each finding to the relevant fact-sheet or research companion.

### Page 40 (lower) — Constance Gurney / Blundevill (G19 corroboration)

The Blundevill pedigree on Rye p. 40 makes Constance, wife of Rafe Blundevill of Newton Flotman (d. 1514), a daughter of William Gorney of Bassam/Barsham. This is a third independent witness for the marriage already published in `fact-sheets/g19-william-gurney-iv-fact-sheet.md` (child table n12). The visitation preserves the `Gorney` spelling form. The Gurney arms borne by Constance's line bear a crescent for difference, consistent with cadet treatment of the daughters' lines.[^rye-p40]

### Page 40 (upper) — Blennerhassett pedigree tail (G15 standing context)

The top half of p. 40 carries the tail of a Norfolk Blennerhassett pedigree (Sir Edward Blever[hassett] of Norfolk; Jeremy Bleverhassett of Wilton; Rafe Blennerhassett with descendants including Francis in Ireland). G15 Henry Gurney's wife Ellen Blennerhasset of Barsham is in the same Norfolk surname-cluster, although the page does not name Ellen directly. Recorded as standing context for the G15 Blennerhassett alliance.[^rye-p40]

### Page 132 — Walter Gurney of Cley and the Cawston / Aylsham cadet branch (G19 corroboration)

Rye p. 132 gives a Gourney pedigree headed `Thomas [William ?] Gurney of West Bassant [Barsham] in Norfolk, esq.`, with arms `Argent, a cross engrailed gules, a crescent for difference`. The named children are 1 William (eldest), 2 Walter Gurney of Elay [Cley ?] (m. Margaret daughter of Edmund Moore of Wolterton), 3 Thomas, and 4 Christopher (a priest). Walter's line proceeds through William Gourney of Cawston (m. Ann Wayte of Tytleshall), and then to Robert Gorney of Aylsham (m. Dorothy, widow of John Thompson). This corroborates the cadet branch already published in `fact-sheets/g19-william-gurney-iv-fact-sheet.md` (child table: "Walter Gurney of Cley-by-the-Sea ... ancestor of the Gurneys of Cawston and Aylsham" — Daniel Gurney 1848 pedigree p. 287). The visitation's `Thomas [William ?]` apex is the printed source itself flagging ambiguity between a Thomas and a William as the pedigree head — consistent with the project's reading of William G19 as Walter's father. The arms-with-crescent on this cadet pedigree match the cadet-branch convention.[^rye-p132]

Note: this Walter Gurney of Cley/Elay (fl. late 15th / early 16th century) is **not** the G31 Walter de Gournay who founded the junior Norfolk branch in the early 13th century (standing-fact #2 in `AGENTS.md` §6). Two different Walters separated by roughly three centuries.

### Pages 140-141 — direct line G17 → G16 → G15 → G14 (corroboration)

Pages 140 and 141 give a direct West Barsham / Great Ellingham pedigree headed `Gurney.` with arms `Argent, a cross engrailed gules, in dexter chief point a cinquefoil azure`. The line runs Anthony Gurney → Francis Gurney of West Barsham (m. Ellen daughter of ... Holdich of Ranworth) → Henry Gurney of Great Ellingham (m. Ellen daughter of John Blenerhasset of Barsham) → Henry's children: 1 Thomas (of West Barsham, m. Martha Lewknor of Denham, with children Edward, Thomas, Susan, Martha, Ellen, Margaret); 2 Henry; 3 Edward; 4 Bassingborne (ob. s.p.); 5 Anthony; 6 Francis; 7 Leonard; plus daughters Elizabeth (m. ... Salford of London), Mary (s.p.), Anne (m. Thomas Osburne of Mundham), and Abigail.[^rye-p141]

Corroborated facts:
- G17 Anthony Gurney as pedigree apex.
- G16 Francis Gurney + Ellen Holdich of Ranworth (matches G16 fact sheet and companion).
- G15 Henry Gurney of Great Ellingham + Ellen Blennerhasset of Barsham, and the children-table order (matches G15 fact sheet and DG-I pedigree p. 287).
- G14 Francis Gurney as Henry's **sixth son**, twin with Anthony — matches project standing-fact #4 and the G14 fact sheet vital "13 September 1581 ... sixth son of Henry Gurnay, Esq."

One reading wrinkle: the visitation prints Henry's third son as `3. Edward`, but the project (DG-I; G15 fact sheet; DNB) identifies that son as **Edmund Gurney the divine** (Cambridge B.D., Rector of Harpley 1620–1648, separate DNB entry). Record the visitation's `Edward` reading in research; do not silently reconcile.[^rye-p141]

[^brooke-p92]: Ralph Brooke, *A Catalogue and Succession of the Kings, Princes, Dukes, Marquesses, Earles, and Viscounts of this Realme of England, since the Norman Conquest, to this Present Yeare, 1619* (London: William Jaggard, 1619), p. 92 (Gloucester / Earls of Gloucester entry on Almeric Mountfort, his marriage to Millicent daughter of Hugh Gurney, his earldom of Évreux/Gloucester, and Millicent's second marriage to William Cantelupe). Internet Archive item `cataloguesuccess00broo`. Source ID: `brooke-catalogue-succession-1619`. Identification of Hugh Gurney as Hugues V de Gournay and Julian as Juliana de Dammartin per Charles Cawley, *Medieval Lands*, SEIGNEURS de GOURNAY section.

[^brooke-p201]: Brooke, *Catalogue and Succession* (1619), pp. 200–201 (Earls of Salisbury entry, with the Doctor Powell c. 1094 Cardiff tradition embedded in the Patrick de Eureux paragraph). Source ID: `brooke-catalogue-succession-1619`. Powell text: David Powell, *The Historie of Cambria* (London, 1584), fo. 154, as quoted by Brooke. Project's Cardiff death tradition for G34 Hugh II de Gournay at c. 1074: see Pattou companion p. 2 ("Hue ... +X 1074 (Cardiff)").

[^rye-p40]: William Hervey, Robert Cooke, and John Raven, *The Visitacion of Norffolk, Made and Taken by William Hervey, Clarencieux King of Arms, Anno 1563; Enlarged with Another Visitacion Made by Clarenceux Cooke, with Many Other Descents; and also the Vissitation Made by John Raven, Richmond, Anno 1613*, ed. Walter Rye (London: Harleian Society, 1891), p. 40 (Blundevile pedigree on the lower half; Blennerhassett pedigree tail on the upper half). Internet Archive item `visitacionnorff00ravegoog`. Source ID: `rye-visitacion-norffolk-1891`.

[^rye-p132]: Rye, *Visitacion of Norffolk* (1891), p. 132 (Gourney pedigree). Source ID: `rye-visitacion-norffolk-1891`. Project cross-reference: `fact-sheets/g19-william-gurney-iv-fact-sheet.md` child-table entry for Walter Gurney of Cley-by-the-Sea (Daniel Gurney 1848 pedigree p. 287).

[^rye-p141]: Rye, *Visitacion of Norffolk* (1891), pp. 140–141 (Gurney pedigree, beginning at Anthony Gurney; continued through Henry of Great Ellingham and his children). Source ID: `rye-visitacion-norffolk-1891`. Project cross-references: `fact-sheets/g17-anthony-gurney-fact-sheet.md`, `fact-sheets/g16-francis-gurney-fact-sheet.md`, `fact-sheets/g15-henry-gurney-fact-sheet.md`, `fact-sheets/g14-francis-gurney-fact-sheet.md` (standing-fact #4 — Francis G14 as sixth son of Henry G15).
```

### 8. Write Brooke validation file

New file write: `sources/validations/brooke-catalogue-succession-1619.md`

```markdown
# Validation — Brooke, Catalogue and Succession (1619)

Source ID: `brooke-catalogue-succession-1619`

## Source examined

Ralph Brooke, *A Catalogue and Succession of the Kings, Princes, Dukes, Marquesses, Earles, and Viscounts of this Realme of England, since the Norman Conquest, to this Present Yeare, 1619* (London: William Jaggard, 1619), Internet Archive item `cataloguesuccess00broo`.

## Portion examined

Selected page images:

- page 92 — Millicent / Millescent, daughter of Hugh Gurney and Julian his wife.
- page 200 — preceding Salisbury / Patrick de Eureux context.
- page 201 — Doctor Powell tradition naming Hugh Gurney wounded near Cardiff and later dying in Normandy.

## Method and limitations

Transcription from user-supplied page images and corrected user text. Long-s normalized to modern `s`. Brooke is an early-modern printed heraldic/genealogical source and should be used as derivative evidence unless the underlying Powell, priory-book, charter, or other cited authority is separately examined.

## Substantive findings recorded

- `sources/corpus_supplement/brooke-catalogue-succession-1619-selected-gurney-pages.md`
- `research/topics/brooke-rye-selected-gurney-references.md`

## Patchset trail

Prepared in `sources/intake/processed/v67-brooke-rye-selected-gurney-references.patchset.md`; after application, archived to `sources/intake/done/`.
```

### 9. Write Rye validation file

New file write: `sources/validations/rye-visitacion-norffolk-1891.md`

```markdown
# Validation — Rye, Visitacion of Norffolk (1891)

Source ID: `rye-visitacion-norffolk-1891`

## Source examined

William Hervey, Robert Cooke, and John Raven, *The Visitacion of Norffolk, Made and Taken by William Hervey, Clarencieux King of Arms, Anno 1563; Enlarged with Another Visitacion Made by Clarenceux Cooke, with Many Other Descents; and also the Vissitation Made by John Raven, Richmond, Anno 1613*, ed. Walter Rye (London: Harleian Society, 1891), Internet Archive item `visitacionnorff00ravegoog`.

## Portion examined

Selected printed pages:

- p. 40 — Blundevill pedigree naming Constance daughter of William Gorney of Barsham.
- p. 132 — Gourney/Gorney collateral branch: West Barsham, Cley, Cawston, Aylsham.
- pp. 140-141 — Gurney direct-line pedigree: Anthony, Francis of West Barsham, Henry of Great Ellingham, and Henry's children including Francis.

## Method and limitations

Transcription from page images. Because the source pages are pedigree diagrams, the durable corpus transcription preserves relationship structure with nested bullets rather than flattening the text into prose. Rye's bracketed editorial expansions and question marks are retained where visible.

## Substantive findings recorded

- `sources/corpus_supplement/rye-visitacion-norffolk-1891-gurney-selected-pages.md`
- `research/topics/brooke-rye-selected-gurney-references.md`

## Patchset trail

Prepared in `sources/intake/processed/v67-brooke-rye-selected-gurney-references.patchset.md`; after application, archived to `sources/intake/done/`.
```

### 10. Write media README files

New file write: `sources/media/brooke-catalogue-succession-1619/README.md`

```markdown
# Brooke, Catalogue and Succession (1619) — selected Gurney pages

Source ID: `brooke-catalogue-succession-1619`

Working-reference page images from Ralph Brooke, *A Catalogue and Succession...* (London: William Jaggard, 1619), Internet Archive item `cataloguesuccess00broo`.

## Files

- `page092-gloucester-mountfort-hugh-gurney-millicent.png` — Millicent, daughter of Hugh Gurney and Julian his wife.
- `page200-salisbury-patricke-de-eureux-context.png` — preceding Salisbury / Patrick de Eureux context.
- `page201-salisbury-hugh-gurney-cardiff-powell.png` — Doctor Powell tradition naming Hugh Gurney wounded near Cardiff and later dying in Normandy.

## Transcript

See `sources/corpus_supplement/brooke-catalogue-succession-1619-selected-gurney-pages.md`.
```

New file write: `sources/media/rye-visitacion-norffolk-1891/README.md`

```markdown
# Rye, Visitacion of Norffolk (1891) — selected Gurney pages

Source ID: `rye-visitacion-norffolk-1891`

Working-reference page images from William Hervey, Robert Cooke, and John Raven, *The Visitacion of Norffolk...*, ed. Walter Rye (London: Harleian Society, 1891), Internet Archive item `visitacionnorff00ravegoog`.

## Files

- `page040-blennerhassett-tail-and-blundevill-constance-gorney-barsham.png` — page 40: Blennerhassett pedigree tail (upper) and Blundevill pedigree (lower) naming Constance daughter of William Gorney of Barsham.
- `page132-gourney-west-barsham-cawston-aylsham.png` — Gourney/Gorney collateral branch.
- `page140-gurney-anthony-francis-west-barsham.png` — direct Gurney pedigree beginning with Anthony and Francis of West Barsham.
- `page141-gurney-henry-great-ellingham-francis-sixth-son.png` — continuation through Henry of Great Ellingham and Henry's children, including Francis.

## Transcript

See `sources/corpus_supplement/rye-visitacion-norffolk-1891-gurney-selected-pages.md`.
```

### 11. Downstream routing — for a follow-up patchset

The page-by-page research-value section above identifies specific downstream destinations for the visitation findings. Because the existing fact sheets and research companions each have their own footnote structure, those targeted insertions are **deferred to a follow-up patchset** rather than scripted here. The intended insertions are:

- `research/people/g14-francis-gurney-fact-sheet.research.md` — Rye pp. 140-141 as additional witness to G14 as Henry G15's sixth son (twin with Anthony).
- `research/people/g15-henry-gurney-fact-sheet.research.md` — Rye pp. 140-141 as additional witness to Henry's children-table order; flag the visitation's `3. Edward` reading as a variant for Edmund the divine. Rye p. 40 upper as Blennerhassett standing context (no specific Ellen claim).
- `research/people/g16-francis-gurney-fact-sheet.research.md` — Rye pp. 140-141 as additional witness to the Holdich of Ranworth marriage.
- `research/people/g17-anthony-gurney-fact-sheet.research.md` — Rye pp. 140-141 as additional witness to Anthony as pedigree apex.
- `research/people/g19-william-gurney-iv-fact-sheet.research.md` — Rye p. 40 lower as additional witness to Constance Gurney / Blundeville marriage; Rye p. 132 as additional witness to Walter Gurney of Cley and the Cawston/Aylsham cadet branch.
- `research/people/g34-hugh-de-gournay-ii-fact-sheet.research.md` — Brooke pp. 200-201 as a late antiquarian witness to the Cardiff death tradition, with chronological-discrepancy note (c. 1094 vs. project's c. 1074).
- `research/topics/senior-gournay-baron-line-collateral.md` — additive paragraph for the Hugues V → Millicent → Mountfort / Cantelupe / Tregoz line from Brooke p. 92, with the Renaud de Dammartin (Earl of Boulogne) identification for "Julian's brother Reginald Earl Bullen" and the Thomas Cantelupe (Bishop of Hereford, canonized 1320) human-interest detail.

Optional fact-sheet citation additions (less urgent than the companion updates) would add the Rye visitation as a corroborating footnote on the existing Constance Gurney, Walter Gurney, Anthony / Francis / Henry / Francis, and Holdich rows. These should be a single coordinated fact-sheet edit, not scattered one-offs.

### 12. Finalize intake patchset lifecycle

This patchset file already exists at `sources/intake/processed/v67-brooke-rye-selected-gurney-references.patchset.md`. The original `stub-v67.md` was renamed during Phase 1; `stub-v68.md` and `stub-v69.md` are already in place (v68 has since been promoted to a sibling patchset). No additional lifecycle moves are needed before Phase 2 runs.

## Phase 2 completion step

After Phase 2 application is complete, prepend the done stamp to the patchset and move it:

```bash
python - <<'PY'
from pathlib import Path
from datetime import datetime
src = Path("sources/intake/processed/v67-brooke-rye-selected-gurney-references.patchset.md")
dst = Path("sources/intake/done/v67-brooke-rye-selected-gurney-references.patchset.md")
body = src.read_text(encoding="utf-8")
stamp = "**Done:** 2026-05-28 HH:MM PT\n\n"
dst.write_text(stamp + body, encoding="utf-8")
src.unlink()
PY
```

Replace `HH:MM` with the actual completion time.
