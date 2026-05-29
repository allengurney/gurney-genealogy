**Done:** 2026-05-28 19:17 PT

# v69 patchset — Armstrong, *History and Antiquities of the County of Norfolk* (1781) — selected Gurney references across vols 1–10

Prepared: 2026-05-28  
Revised: 2026-05-28 (extended from vol-5-only to full ten-volume sweep)  
Phase: 1 preparation  
Scope: capture Mostyn John Armstrong's 1781 ten-volume *History and Antiquities of the County of Norfolk* as a new project source; transcribe selected Gurney-variant content across all ten volumes (118 hits total); and route the substantively new findings — including a hitherto unrecorded death date for **Edward Gourney** (G15 Henry's grandson; West Barsham heir), a previously unknown **list of impaled / quartered arms at West Barsham church**, a **1637 attestation of Edward Gourney as Norfolk Justice of the Peace**, the **Hingham Gurney's Manor 1572 lordship** confirmation for G15 Henry, the **G17 Anthony Gurney 4 January 1555/6 death as lord of Irstead** with the 1541-42 Southwell purchase, the **William Gurnay of Cawston 1578 gravestone**, the **Sir John V + Alice attestations 1395-96 / 1398 / 1401** at Hellesden + Drayton + Taverham, and the **Norwich Cathedral cloister Gournay arms** — to the affected research files for a follow-up patchset.

## Scope revision

A first-pass review of the patchset covered only vol. 5 of Armstrong (Freebridge and Gallow hundreds — 21 hits). A second-AI review on the same day expanded scope to all ten volumes after the user's prompt to "consider checking out the other volumes." Hit counts across the full work:

| Volume | Hundreds covered | Gurney-variant hits |
|---|---|---|
| 1 | Earsham, Guiltcross, Loddon, etc. | 9 |
| 2 | Clavering, etc. | 0 |
| 3 | North Erpingham, Humbleyard, etc. | 11 |
| 4 | East Flegg, Clackclose, Lothingland, Forehoe (Hingham), etc. | 11 |
| 5 | Freebridge and Half, Gallow | 21 |
| 6 | South Erpingham, Grimshoe, Happing, Brothercross | 4 |
| 7 | Happing, Humbleyard, Heath, Lessingham, Tunstead | 11 |
| 8 | Eynsford, Mitford (Cranworth + Swathing), Shropham (Great Ellingham), South Greenhoe, etc. | 20 |
| 9 | Gallow, Smithdon (Hunstanton), Freebridge (Heigham, Drayton, Hellesden, Taverham, Irstead) | 12 |
| 10 | Blofield, Hundred of Norwich (Cathedral cloister, Sir Richard Gurney biographies, etc.) | 19 |
| **Total** | | **118** |

Per the patchset standard ("typically several turns of research → one patchset"), the cleanest architecture for one work in ten bound volumes is one source ID and one consolidated corpus supplement with per-volume sections — not ten separate per-volume patchsets. This patchset uses that architecture.

## Incoming source

URL-supplied. No images placed in `sources/intake/`; the OCR plaintext was pulled from each volume's Internet Archive djvu derivative and transcribed below by parish + theme. Master collection URL:

```
https://archive.org/details/bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_5/
```

Per-volume Internet Archive item identifiers (all of form `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_N` for N in 1..10):

- vol. 1 — `..._1781_1`
- vol. 2 — `..._1781_2`
- vol. 3 — `..._1781_3`
- vol. 4 — `..._1781_4`
- vol. 5 — `..._1781_5`  (Freebridge + Gallow — was the entry point of this patchset)
- vol. 6 — `..._1781_6`
- vol. 7 — `..._1781_7`
- vol. 8 — `..._1781_8`
- vol. 9 — `..._1781_9`
- vol. 10 — `..._1781_10`

Repo search confirmed Armstrong is **not** currently in `data/sources.json` or referenced from `research/`, `fact-sheets/`, or `sources/`. New source.

## Stub repair

The intake stub state was stale on entry to this patchset: `sources/intake/processed/stub-v67.md` was still present, even though v67 and v68 have both been promoted to live patchsets in the same directory. Per `sources.md` ("If the stub is missing or stale, repair it with a one-time shallow scan and take the highest `vNN` found across processed/, processed/Ready/, processed/on-hold/, and done/"), the highest live `vNN` is v68; this patchset is therefore v69, and Phase 2 creates a fresh `stub-v70.md` while removing the stale `stub-v67.md`.

## Source tracking

Proposed new source ID:

- **`armstrong-norfolk-1781`** — Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, 10 vols. (Norwich, 1781). One bibliographic work in ten volumes; the IA hosts each volume as a separate item under the `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_N` identifier pattern. Useful as an **independent pre-Blomefield-completion (1781) witness** to Norfolk parish descents — Armstrong's Norfolk volumes were issued one generation **after** Blomefield's first edition (vols. i–iii, 1739–1745) and three to four decades **before** Blomefield's posthumous completion was reissued (1805–1810). Armstrong draws on private-hand antiquarian collections of the 1770s as well as on Blomefield, so his text is partly synthetic; pedigree summaries occasionally collapse generations (see per-volume caveats below).

## Research-value assessment — substantively new findings (across all ten volumes)

Listed in order of weight; routing destinations in the dedicated routing section.

1. **Edward Gourney's death date — August 1641** (vol. 5 p. ~19, West Barsham chancel monument). The G15 Henry Gurney fact-sheet records the succession line Henry → Thomas (d. 1614 vita patris, m. Martha Lewknor) → grandson Edward Gournay (b. 1608) → Henry II (d. 1661 s.p.), but has no death date for Edward. Armstrong supplies Aug 1641, fixing Henry II's tenure as 1641–1661.
2. **Edward Gourney as Norfolk Justice of the Peace, 12 Oct 1637** (vol. 9 p. ~16, Sessions order at Walsingham Parva). Edward sat as a JP on a Hunstanton rates dispute alongside Sir Hamon L'Estrange and Robert Baron — Latin "Hammone L'Estrange milite, Roberto Baron, et Edwardo Gournay armigeris justiciariis dicti domini regis ad pacem" — four years before his Aug 1641 death. This is the first known administrative office attestation for Edward.
3. **Latin chancel epitaph of Edward Gourney (verbatim)** (vol. 5 p. ~19). Names "Edwardus Gourney, filius et heres Tho. Gourney Armig. et Marthe filie Edu. Lewkenor de Denham, in Com. Suff, Militis, obiit Aug. 1641." Independent epigraphic confirmation of Thomas G15-son's marriage to Martha Lewknor and of Edward's parentage.
4. **List of arms impaled / quartered by the Gurneys at West Barsham church** (vol. 5 p. ~18): Wauci, Calthorpe, Lovell, Holdich, Blennerhasset, Lewknor, Jernegan, and a probable Wentworth (sable, a chevron between three leopards' heads). Seven match already-known marriages; the probable Wentworth is a **new research lead** — no Gurney-Wentworth marriage is currently recorded in the West Barsham line.
5. **Gurney arms in Norwich Cathedral cloister** (vol. 10 p. ~149). "Gournay" listed alongside Morley, Shelton, Scales, Erpingham, Mowbray, Thorpe, Savage among the families whose arms appeared in the cloister windows above the bars — those arms commemorated 1382 (Walter de Berney's gift) glazing work completed 1430. Independent late-medieval heraldic attestation of the Gurney family's standing in Norwich civic-cathedral context.
6. **Hingham — Gurney's Manor lordship 1572** (vol. 4 p. ~266). "Gurney's Manor was part of the great manor, granted to a younger branch of the family before the forfeiture; it continued always in the family of that name, residing at Barsham and Great Ellingham, in this county; **Henry Gurney was lord in 1572**; how it passed afterwards we do not find; but in 1715 it was owned by Mr. Larwood, of Norwich, merchant." Confirms project standing fact #6 (Hingham Gurney's Manor held to extinction) + supplies the post-1611 / extinction successor as William Larwood by 1715.
7. **Great Ellingham — Anthony Gurney's 1525 inheritance and the post-1641 Margaret Gurney/Davy descent** (vol. 8 pp. ~254–255 in the Shropham hundred). Anthony Gurney of North Barsham (G17) got Great Ellingham capital manor in right of his wife **Margaret Lovell, one of the daughters and co-heiresses of Sir Robert Lovell by Ela Conyers**, after Henry Spelman (Anthony's wife's first-cousin-once-removed) died s.p. in 1525. "After 1641 it went to **Margaret Gurney, his aunt**, who married Mr. Henry Davy of Great Ellingham, whose sole daughter and heiress, Mary, married Sir Roger Potts, bart." Identifies the 1641 transition as **Edward's death** → Great Ellingham to **Margaret (Gurney) Davy** (G15 Henry's daughter, Edward's paternal aunt), while West Barsham went to Edward's son Henry II. Major chain-of-descent gap fill. Adds Ela Conyers as the kinship link between the Lovell and Spelman lines (Ela was sister to Ann Conyers, mother of Henry Spelman) — the explanation for why the Lovell-Mortimer-Conyers-Spelman estate came to G17 Anthony via marriage.
8. **Anthony Gurnay of Great Ellingham buried 1557** (vol. 8 p. ~256). G17 Anthony was already known to have died 4 Jan 1555/6 (Blomefield West Barsham entry, G15 fact-sheet n1). Armstrong's "buried in this church in 1557" date is slightly later than the project's death date — calendar slip or Armstrong-side editorial error. Worth flagging as a documented variant.
9. **G17 Anthony Gurney's 1541-42 purchase of Irstead manor from Sir Richard Southwell + 4 January 1555/6 death** (vol. 9 p. ~17 area, Irstead parish). Armstrong: "In the 33rd of Henry VIII, Sir Richard Southwell, knt. conveyed by fine to Anthony Gourney, esq. the manor of Irstead, with lands in Barton, Neatishead, Smalburgh, &c. and the said Anthony died lord on January 4, in the 2d and 3d of Philip and Mary [= 4 Jan 1555/6], whose grandson, Henry, is said... to hold his manor of the bishop of Norwich." Corroborates G17's death date (matches Blomefield West Barsham) + supplies the 1541-42 Southwell-purchase as the route by which the Gurneys acquired Irstead (already listed as a tenure in G15 fact-sheet n3 via Blomefield).
10. **G17 Anthony Gurney's c. 1540 sale of Merton manor to Sir Richard Southwell** (vol. 9 p. ~25, Merton parish in South Greenhoe). "In 1402, on the division of the Mortimer estate, this manor fell to the share of Sir John Fitz-Ralph, knt. in right of his wife; and from that time it went with Ellingham-hall manor till 1540, and then was **sold by Anthony Gurnay, esq. to sir Richard Southwell**." The Merton-by-Watton manor came to the Gurneys through the same Lovell/Mortimer line as Great Ellingham and was alienated by G17 Anthony in 1540 — a counter-direction transaction with Sir Richard Southwell from whom Anthony also bought Irstead in 1541-42 (item 9). New manor history; specific 1540 alienation not currently in G17 fact-sheet companion.
11. **William Gurnay of Cawston gravestone, d. 10 March 1578** (vol. 3 p. ~133 in Cawston entry, South Erpingham). "For W[ill]iam Gurnay, gent. w[ho] died March 10, 1578; and Ann, his wife, January 19, 1595; they had one son and three daughters — Gurnay impaling Waytes, of Norfolk." Plus arms in the windows of Cawston church include "Gurnay impaling Wayte." Corroborates the Rye 1891 p. 132 visitation pedigree captured in v67 (William Gourney of Cawston + Ann Wayte of Tytleshall, in the Walter-of-Cley cadet branch from G19 William IV's son). Brand-new exact death dates (10 March 1578 and 19 Jan 1595) and exact child count (one son + three daughters).
12. **Sir John Gurney V + Alice his wife — 1395-96, 1398, 1401, 1401-02 attestations at Hellesden, Drayton, Taverham** (vol. 9 pp. ~13–16, Heigham + Drayton + Hellesden + Taverham). Armstrong: "John Gournay, and Alice his wife, were in possession of [Hellesden] in the 19th of Richard II [1395-96], when they passed it, with the manor of Drayton, and the advowson of the two chantries in this town, to John Winter, etc." Plus: "in 1398, and 1401, John Gourney presented to this church as lord." Plus "in the 3d of Henry IV [1401-02] John Gournay held two fees here, and in Taverham, late John Spring's, of the barony of Rye." Plus the same conveyance to John Winter is recorded again at Drayton (vol. 9 p. ~21). These are four new dated attestations for Sir John V across the Norwich-adjacent Hellesden / Drayton / Taverham cluster. Alice is the wife — the HoP / DG-Supp identification with Alice Heylesdon is most parsimonious (the same manors had been in the Hayleſdon family, with John de Hayleſdon's 1384 Husting will already captured in v63).
13. **Cantley, Bedingham, Kimberley, Lessingham, Bastwick, etc. — senior-line corroboration cluster** (across vols 1, 4, 7). Armstrong corroborates many already-documented senior-line items (Hugh de Gournay → Nicholas de Stuteville with Gunnora marriage; Julian de Gournay → William Bardolph; Gerard de Gournay's Lessingham donation to Bec; the 1205 disseizure of Norman lands by King John). Adds two specific new attestations: (a) **Kimberley parallel to Bedingham** — the Stuteville/Gunnora marriage carried Kimberley as well as Bedingham (vol. 4 pp. ~272–273); (b) **Bastwick manor granted to Hugh de Gourney by Henry I on Baynard rebellion** (vol. 7 p. ~278) — a specific Henry-I-era grant attestation for either G33 or G34 Hugh, useful for the Hugh-III / Hugh-IV career-attestation chain in the senior-line topic file.
14. **Harpley parish cluster** (already captured in original vol-5-only v69 — preserved unchanged below). Includes the 1297 fair grant, 1325 Uphall deed with witness list, 1332 nephew-grant, rector-stone observation, and Sir John V 1400-01 release to Hugh Bavent + 9 Henry IV (1407-08) death year.
15. **East Barsham conveyance cluster** (already captured in original vol-5-only v69 — preserved unchanged below). 1440 Thomas Gournay + John Hunt confirmation; 1447 Thomas Gurney attorney-delivery of seisin.
16. **Norwich — Gournay's Place capital messuage** (vol. 10 p. ~204). "The capital messuage called Gournay's Place, was in 1338 the city house of Thomas Gawdy, esq. and afterward belonged to the Pastons, from whom it passed to the family of the Cookes." A Norwich townhouse named after a former Gurney owner; by 1338 already in the Gawdy family. Useful for the G20 / G21 Norwich-civic-presence picture (the G20 1471 will already names a Norwich house in St Gregory's parish — Gournay's Place is a separate, earlier Norwich Gurney building).
17. **Cranworth + Swathing + Letton cluster — King-John-era Gurney lordships** (vol. 8 pp. ~125–126 and pp. ~152–153 and pp. ~157, Mitford Hundred). "The ancient family of de Gurney were lords of this town [Cranworth], Cranworth, and Letton, in the [reign] of king John." Plus 1316 (9 Edw. II) John de Gurney impleaded William de Swathing for chasing his hares without his licence in his free-warren of Swathing. Plus 1257 + 1268 John de Gurney tenure at Hardingham/Reymerston with William de Swathing holding mill rights at Ravensholm. Plus the **undated Hugh de Gurney charter to Robert the Burgundian** for the manor of Swathing in Hardingham (20s. + horse rent, granted at "Ferretre" in Normandy — read La Ferté), with the further note that "this Hugh gave to the chapter of the church of St. Ildebert, of Gourney, in Normandy, the said church" — extends the project's existing Saint-Hildevert-at-Gournay pattern (Caister + Cantley tithes per Potin 1842) to Hardingham church as well. **Major new junior-branch-founding period content.**
18. **John Gourney 1395-96 conveyance pattern at Heigham, Drayton, Hellesden, Taverham, Merton** — see item 12 above. Adds substantive specifics for Sir John V's economic-administrative footprint outside the West Barsham / Harpley / North Barsham core.
19. **Houghton — Gaunts and Gurneys manors** (vol. 6 p. ~100). Two named manors "Gaunts and Gurneys in Houghton" purchased in 1756 by Henry Lee-Warner. New post-Gurney descent context for the Houghton (next Harpley) Gurney holdings.
20. **Sir John Howard's will — silver cup to Sir John Gurney** (vol. 6 p. ~116). Howard's will (late 14th / early 15th century) leaves "to Sir Stephen Hales, John de Burgh, Richard de Sutton, knts. and [Sir John] Gurney, to each of them a new cup to be made of silver, with a cover, each of the weight of 10 marks in gross." This places **Sir John V in Howard's intimate gift circle** alongside Hales, Burgh, and Sutton — significant social-network detail. New.
21. **William Gurney's 1500 advowson presentation at Thuxton** (vol. 8 p. ~265, Mitford Hundred). Likely **G19 William Gurney IV** (d. 18 Jan 1508) — extends his documented advowson activity beyond the existing project list.
22. **Edmund Gurney's 1381 advowson presentation at Thuxton** (vol. 8 p. ~265). Corroborates G23 Edmund's advowson activity in the Thuxton / Mitford cluster.
23. **Saxthorpe — John Gurnay of West Barsham c. 1411** (vol. 3 p. ~277). "About 1411 John Gurnay, of West Barsham" held Saxthorpe manor; later passed to Sir John Fastolf. Sir John V died 5 Dec 1408, so the c. 1411 actor is most parsimoniously **Edmund** (Sir John V's IPM-aged-10 son, acting through guardians) or his nephew-and-eventual-successor **Thomas I** (G21). Project's v62 Paston-Saxthorpe-1472 patchset covers a different (later) Saxthorpe-Gurney involvement; the 1411 attestation is new.
24. **DG-Reception note — Edmund Gourney the divine biographical sketch** (vol. 1 pp. ~64–65, in the "Eminent Norfolk Men" prefatory matter). Armstrong's biographical sketch of Edmund Gurney the divine (the project's G15 Henry's third son) is an independent 1781 printed witness to the same Edmund-the-divine narrative already captured in the project from DNB + DG-Supp + Fuller's *Worthies of England*. Useful citation; no new fact.
25. **Honingham — burial of Ann (Gurney) Richardson 1697** (vol. 4 p. ~270). Ann, daughter of Sir Richard Gurney, lord mayor of London, was buried at Honingham in 1697. Collateral cadet (the post-G19 London/Essex Gurney line through G19's son Thomas of Dartmouth → eventually Sir Richard the Lord Mayor of 1642).
26. **Sir Richard Gurney, Lord Mayor of London — full biographical entry** (vol. 10 pp. ~270 ff., in the "Eminent Norfolk Men" prefatory matter). Substantial biographical entry of the collateral Sir Richard (lord mayor 1641-42, royalist, imprisoned by Parliament). Already in the project via G19 fact-sheet n13 ("his grandson, Richard Gurney, was Sheriff of London"). Useful corroborating-citation source for any later biography work.

### Corroboration of already-published facts (across all volumes)

- **Matthew de Gourney = Rose de Burnham** (vol. 5 pedigree paragraph; agrees with G29 fact-sheet + DG-I p. 286).
- **Sir John I in arms against Henry III** (Barons' War 1264-65; G27 fact-sheet companion).
- **John de Gournay rector of Harpley d. 1332** (vol. 5; Harpley place file; chancel monument).
- **Gerard de Gournay donation to Bec (Lessingham specifically)** (vol. 7; already in Gerard companion).
- **Hugh-Gournay-with-Gunnora-to-Stuteville marriage** (vols. 4 and 7; already in Cantley/Bedingham research).
- **Julian de Gournay → William Bardolph of Wormegay** (vols. 1, 4; already in senior-collateral topic).
- **G18 William V married Anne Heydon** (vol. 3 sibling-marriage list; already in G18 fact-sheet).
- **Henry G15 lord of Hingham in 1572** (vol. 4; already in G15 fact-sheet via Blomefield).
- **G17 Anthony Gurney d. 4 January 1555/6** (vol. 9; already in G15 fact-sheet n1 via Blomefield).

### Volume-specific OCR / editorial caveats

- **vol. 4, Honingham — "Sir Richard Gorney, lord mayor of London"** is the same person as the **Sir Richard Gurney** of vols 6 and 10 — the "Gorney" spelling is an Armstrong-side variant within the same volume.
- **vol. 5 — "Folas de Gournay"** rector inscription is an Armstrong-transcription error for **"Joh'is de Gurnay"** (Johannis = John); confirmed against the parallel transcription in `research/places/harpley.md`.
- **vol. 5 — "in the reign of Edw. II."** for the North Barsham Wauncy transfer is contradicted by the same volume's "47 Edw. III. (1373)" at West Barsham; Armstrong-side error for "Edw. III."
- **vol. 5 — "Edmund died seised in 1641"** at West Barsham is contradicted by the chancel monument naming Edward Gourney; Armstrong-side error or OCR slip for "Edward."
- **vol. 8 — "Anthony Gurney, esq. was lord in the 26th of Henry III"** (at Hardingham/Swathing): 26 Henry III = 1242 is anachronistic for an Anthony Gurney (Anthonys are 15th-16th century in this family); read as Armstrong-side error, possibly for 26 Henry VIII (1534/35).
- **vol. 5 (pedigree skeleton) — collapses 1316 brother-Edmund and 1373 West Barsham acquirer-Edmund into one figure.** Project's G24 / G23 generational chain preserves the correct intervening generations.

## Outcomes

| Item | Files | Outcome | Destination |
|---|---|---|---|
| 1 | URL-supplied source (10 IA volumes; no local file) | promote as new source ID | `data/sources.json`, `sources/corpus_supplement/`, `sources/validations/`; downstream routing (deferred) to G15 fact-sheet (Edward d. 1641 + JP 1637), G17 fact-sheet / companion (Irstead purchase 1541-42, Merton sale 1540, Great Ellingham via Lovell), G18 / G19 / G20 / G21 / G23 / G27 / G29 research companions, Harpley + West Barsham + North Barsham + Hingham + Great Ellingham + Cranworth + Norwich place files, senior-collateral topic file (Hugh-Henry-I-grant; Saint-Hildevert at Hardingham; Kimberley parallel to Bedingham) |

No item rejected.

## Phase 2 operations

### 1. Update `data/sources.json` — add Armstrong (full ten-volume work)

File: `data/sources.json`.

```str_replace
old_string:
    "lastUpdated": "2026-05-25",
new_string:
    "lastUpdated": "2026-05-28",
```

Then append the new entry inside `sources`:

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
    "armstrong-norfolk-1781": {
      "shortTitle": "Armstrong, History and Antiquities of the County of Norfolk (1781)",
      "citation": "Mostyn John Armstrong, The History and Antiquities of the County of Norfolk, 10 vols. (Norwich, 1781).",
      "archive": "Internet Archive",
      "url": "https://archive.org/details/bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_5/",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/armstrong-norfolk-1781-selected-gurney-references.md",
      "mediaPath": null,
      "validationPath": "sources/validations/armstrong-norfolk-1781.md",
      "notes": "Pre-Blomefield-completion 10-volume antiquarian county history, issued one generation after Blomefield's first edition and three to four decades before the posthumous completion was reissued. 118 Gurney-variant hits across all ten volumes, transcribed in v69 by parish and theme. Per-volume IA item identifiers follow the pattern bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_N for N in 1..10; vol. 2 alone has no Gurney content. Substantively new findings include Edward Gourney's Aug 1641 death (West Barsham chancel monument); Edward's 1637 Justice-of-the-Peace attestation at Walsingham Parva; the full impaled/quartered arms list at West Barsham church including a probable Wentworth shield; Henry G15's lord-of-Hingham confirmation for 1572 and the 1715 post-Gurney successor at Hingham; G17 Anthony's 1541-42 Irstead purchase from Southwell + 1540 Merton sale to Southwell; the William Gurnay of Cawston 1578 gravestone; Sir John V's Hellesden/Drayton/Taverham/Heigham 1395-96 to 1401-02 attestations with his wife Alice; the Norwich Cathedral cloister Gournay-arms attestation; and the Cranworth/Swathing/Letton King-John-era junior-branch cluster including an undated Hugh de Gourney charter to Robert the Burgundian and a Saint-Hildevert-at-Gournay-tithes pattern extending to Hardingham. Volume-specific OCR / editorial caveats are documented in the corpus supplement."
    }
  }
}
```

### 2. Write Armstrong corpus supplement (selected Gurney pages across all ten volumes)

New file write: `sources/corpus_supplement/armstrong-norfolk-1781-selected-gurney-references.md`.

```markdown
# Armstrong, History and Antiquities of the County of Norfolk (1781) — selected Gurney references across vols 1–10

Source ID: `armstrong-norfolk-1781`

Source: Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, 10 vols. (Norwich, 1781). Per-volume Internet Archive items at `https://archive.org/details/bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_N/` for N in 1..10.

Page numbers below are to the printed page numbers preserved in the Internet Archive djvu derivative; pagination resets at the start of each hundred, so "vol. 5 p. 138 (Freebridge)" and "vol. 5 p. 18 (Gallow)" refer to different physical pages in the same printed volume. Long-s is normalized to modern `s`; OCR slips that touch Gurney readings are flagged inline.

Volume hit counts: vol. 1 = 9; vol. 2 = 0; vol. 3 = 11; vol. 4 = 11; vol. 5 = 21; vol. 6 = 4; vol. 7 = 11; vol. 8 = 20; vol. 9 = 12; vol. 10 = 19. **Total: 118.**

---

## Vol. 1 — Earsham, Guiltcross, Loddon (and Eminent Norfolk Men prefatory matter)

### Eminent Norfolk Men — Edmund Gurney the divine (p. ~64)

> Edmund Gourney was born and beneficed in this county, but the place is not known. He was bred in Queen's and Bennet's Colleges, Cambridge, where he commenced Bachelor of Divinity. He was an excellent scholar, and could be merry or serious as he pleased, but never was prophane towards God, or injurious to his neighbour, in his jests, and so might be allowed to please himself, if he gave no one else cause of displeasure. He was a sound Anti-papist, as his books against Transubstantiation, and upon the second Commandment, both of them learnedly and judiciously written, do testify. He died in the beginning of the civil wars.

Extraction: Independent 1781 biographical witness to the project's Edmund Gurney the divine — G15 Henry's third son (Cambridge B.D.; Rector of Edgefield then Harpley 1620–1648; DNB entry). Echoes the Fuller / Anderson tradition. No new fact; useful as one more contemporary printed citation.

### Cantley / Caister / Bedingham complex — Hugh de Gournay senior line (pp. ~120–124)

> [Cantley/Caister/Bedingham descent]... soon after the survey it was granted from the crown to the noble family of de Gournay. Hugh de Gournay, a Norman baron, was a witness to the foundation deed of the abbey of Caen in Normandy, in 1084, founded by the Conqueror; and Hugh de Gournay was lord in this town in the 7th of Richard I. Julian daughter and heir of the lord Hugh de Gournay, brought it by marriage to William lord Bardolph, of Wormegay, who in her right was lord in the 38th of Henry III. and had then a grant of free warren.

Extraction: Corroborates the existing project narrative (Hugh II at Caen 1084; Hugh V seizure 1205; Julian de Gournay → William Bardolph carrying the English lands to Wormegay). Already in `research/topics/anderson-yvery-harpetre-gournay-collateral.md` and the senior-line topic file. No new fact.

### Cantley — Uphall Manor granted by Hugh de Gournay to Roger Botetourt 1229 (p. ~124)

> Uphall Manor took its rise from the grant of Hugh de Gournay, (capital lord of the town) to Roger Botetourt; which he held of Hugh in the 13th of Henry III. anno 1229.

Extraction: A second "Uphall" in the Gurney record — Cantley's Uphall, distinct from Harpley's Uphall (vol. 5 p. ~139). Hugh de Gournay → Roger Botetourt 1229; the 13th Henry III dating places this in the Hugh-de-Gournay-V-or-just-after window. Useful for the senior-line lordship-fragment-distribution pattern.

### Denver — John Gourney died lord 9 Henry IV (p. ~36)

> In the 47th of Edward III the convent of West Dereham had a patent for this moiety, but we do not find them possessed of it. In 1395 Walter Gaddard presented to the aforesaid mediety as lord. ... In the 9th of Henry IV, John Gourney, esq. died lord, and of West Barsham.

Extraction: Independent corroboration of Sir John V's death year (9 Henry IV = 1407-08) and his Denver tenure (already in G23 companion as "Denver, Norfolk | 1357 (attested) onward").

---

## Vol. 2 — no Gurney content

(Clavering hundred; no Gurney-variant hits in the volume's djvu text.)

---

## Vol. 3 — North Erpingham, Humbleyard

### Cawston — William Gurnay gravestone d. 10 March 1578 (p. ~133)

> A stone, having the effigies of a man and a woman, — For W[ill]iam Gurnay, gent. w[ho] died March 10, 1578; and Ann, his wife, January 19, 1595; they had one son and three daughters. — Gurnay impaling Waytes, of Norfolk.

> [Arms in Cawston church windows include] ... lord Hoo, quarterly sab. and arg.; Gurnay impaling Wayte; Waterton...

Extraction: William Gurnay of Cawston d. 10 March 1578, m. Ann (Wayte) d. 19 Jan 1595, one son + three daughters. Cawston is the eldest-son seat of the Cley/Cawston/Aylsham cadet branch descending from Walter Gurney G19's son (per `fact-sheets/g19-william-gurney-iv-fact-sheet.md` n13). The Rye 1891 p. 132 visitation captured in v67 names this William as the cadet line's "William Gourney of Cawston in Norfolk = Ann, daughter to William Wayte of Tytleshall." Armstrong supplies the **exact death dates** and **gravestone-and-arms confirmation** that the visitation pedigree alone lacks. New precise dates.

### South Erpingham — Herward impaling Gourney arms (p. ~32 area)

> Arms in the church: Brotherton, earl of Norfolk, impaling ... — Morley impaling ditto. — Herward impaling Reymes. — Herward impaling Gourney.

Extraction: A Herward–Gourney marriage attested in heraldic display in a South Erpingham parish church. Likely collateral; the project does not currently record a Hereward / Herward marriage with a Gurney in the main pedigree. New collateral lead; availability tag: Unknown online.

### Heydon family — Ann Heydon married William Gurney G18 (p. ~120)

> ... he had three sons, John, Henry, and William, and five daughters; Amy, married to Sir Roger Townshend of Hunstanton, knt.; Dorothy, to Sir Thomas Brook, son and heir of John Lord Cobham; Elizabeth, to Walter Hobart, of Hales-hall, esq.; Ann, to William Gurney, esq.; and Bridget, to Sir William Paston, knt.

Extraction: Ann Heydon's marriage to **G18 William Gurney V** — already in G18 fact-sheet. Armstrong supplies the four sister-marriages in one paragraph: Amy → Townshend, Dorothy → Brook (Cobham), Elizabeth → Hobart of Hales-hall, Bridget → Paston. Useful family-network context (the Brook, Hobart, and Paston names recur in the G18 / G19 / G20 generations of Gurney marriages).

### Reepham/Wickmere area — Mr. John Gurnay of Norwich 1733 (p. ~141)

> [Manor descent]... in 1704 [it] belonged to Mr. John Gurnay, of Norwich, in 1733, and at his death came to his son, Mr. John Gurnay.

Extraction: 18th-century Norwich Gurneys — the collateral cadet via G14 Francis → John Gurney-1 of Braintree → Norwich Quaker line. Two generations of John Gurnay of Norwich, 1704 and 1733+. Useful descent context.

### Saxthorpe — c. 1411 John Gurnay of West Barsham (p. ~277)

> Simon de Creping, (who occurs lord of it in 1315) was the founder of it ... and sold it to John de Gurney; but in 1337 John de Mereworth was in possession of it. In 1400 Henry, Alexander and Roger Groos held it, and about 1411 John Gurnay, of West Barsham; after this Sir John Fastolf, knight of the garter, was lord, and died seised of it.

Extraction: Saxthorpe held c. 1411 by a "John Gurnay of West Barsham." Sir John V died 5 Dec 1408 (DG-Supp Note 121 IPM); the c. 1411 actor is most parsimoniously **Edmund** (Sir John V's IPM-aged-10 son acting through guardians) or the nephew-successor **Thomas I** (G21). The 1411 attestation is new to the project; not the same Saxthorpe involvement covered in v62 (Paston-Saxthorpe-1472 patchset).

### Scottow — "Gurnay's, or Berney's" alias (p. ~454)

> In 1[6?]52 Robert Balle sold the whole to Robert Giblon, who bought Gurnay's, or Berney's, of Mr. Lowerdow, and Stubbe's at Sir Thomas Knevet.

Extraction: A Scottow manor named "Gurnay's, or Berney's" — likely a Gurney-then-Berney alias. Collateral; no further detail.

---

## Vol. 4 — East Flegg, Clackclose, Forehoe (Hingham + Kimberley)

### Hingham — Gurney's Manor: Henry Gurney lord 1572 + post-1715 successor (p. ~266)

> Gurney's Manor was part of the great manor, granted to a younger branch of the family before the forfeiture; it continued always in the family of that name, residing at Barsham and Great Ellingham, in this county; **Henry Gurney was lord in 1572**; how it passed afterwards we do not find; but in 1715 it was owned by Mr. Larwood, of Norwich, merchant.

Extraction: 
- **Henry Gurney lord of Hingham's Gurney's Manor in 1572** — corroborates project standing-fact #6 + Blomefield + G15 fact-sheet narrative.
- **Post-Gurney successor**: Mr. [William] Larwood of Norwich, merchant, lord by 1715. The G15 fact-sheet does not currently track the post-extinction Hingham manor; this fills the gap. Useful for Hingham place file.
- The "granted to a younger branch of the family before the forfeiture" reading aligns with standing-fact #2 (junior Norfolk branch through Walter G31; "before the forfeiture" = before Hugh V's 1205 loss).

### Honingham — Ann (Gurney) Richardson buried 1697 (p. ~270)

> He married Ann, daughter of Sir Richard Gorney, lord mayor of London, buried at Honingham in 1697. Their eldest son, Henry, died without issue, and was succeeded by his brother, William lord Richardson...

Extraction: Ann Gurney, daughter of Sir Richard Gurney (lord mayor 1641-42, the project's collateral via G19), married into the Richardson family and was buried at Honingham, Norfolk, 1697. Collateral cadet line context. The "Sir Richard Gorney" spelling is an Armstrong-side variant.

### Kimberley — Hugh de Gurnaco → Stuteville marriage parallel to Bedingham (pp. ~272–274)

> In the beginning of the reign of king John Hugh de Gurnaco, or Gournay, a Norman, was possessed of it, and gave it to Nicholas de Stutevile with Gunnora, his daughter, in marriage; he was disseized of it at the time of the disseizing all the Normans from their lands, for their rebellion, which was in 1205, in the 7th of king John, who the next year directed his writ to the sheriff, to restore Nicholas de Stutevile to all his lands that Nicholas, his father, was disseized of. At the seizure the manor and stock was assigned to Walter de Cantelupe during the king's pleasure; this Nicholas died in 1232; and in 1237 Simon de Greynvill, or Greyvill, then husband of Alice, relict of Nicholas, and John de Stutevile, son and heir of Nicholas, released all their right to Wido, or Guy de Boutetort, in 10l. a year, rents and lands, which Nicholas de Stutevile had granted him in Kimberley, which ever after was called Boutetort's manor.
>
> In 1284 Nicholas de Stutevile had the assize of bread, ale, and beer, of all his tenants here, and held this town of the barony of Gournay. After this we find no mention of it till 1313, when Margery, relict of Roger Colyn, of Norwich, granted it to Sir Walter de Norwich, and Catherine, his wife, and their heirs.
>
> In 1345 William de Holtford, who presented in 1342, Robert de Yarmouth, and Roger de Norwich, held it at half a fee of Sir John Bardolph's honor of Wormegay, but more rightly of Gournay, which came to the Bardolphs by William Bardolph's marriage with Julian, daughter and heiress of Gournay.

Extraction:
- **Kimberley parallel to Bedingham** — same Hugh de Gournay → Gunnora → Stuteville marriage carried Kimberley as well as Bedingham. The project's existing senior-collateral topic file records the Bedingham strand only; Kimberley extends the pattern.
- The 1206 King John writ restoring Nicholas de Stuteville (son) to his disseized father's lands is dated context for the Capetian-era English-lands restoration narrative.
- The 1237 Simon de Greynvill / John de Stuteville release to Guy de Botetourt at 10l. p.a. preserves how Kimberley fragmented after Nicholas's 1232 death.
- The 1284 attestation that Nicholas's heir "held this town of the barony of Gournay" + the 1345 attestation that the Bardolph honour was "more rightly of Gournay" carry the inherited-Gurney-barony identification forward into the late-medieval Bardolph era.

### Eminent Norfolk Men — Sir Richard Gorney (lord mayor) again (p. ~250 area, by reference)

Cross-reference to the full Sir Richard Gurney biography in vol. 10. The vol. 4 mentions are incidental to the Honingham descent (above) and other Norfolk-Stuart references.

---

## Vol. 5 — Freebridge + Gallow (the original vol-5-only patchset content, preserved unchanged)

### Harpley — Gourney's Manor (pp. ~138–139)

> Gourney's Manor. This manor in the reign of Henry II. came into the family of the Gourneys.
>
> Sir John de Gourney was lord in the reign of Henry II.
>
> John Gourney, esq. of Harpley, released in the 2d of Henry IV. to Hugh Bavent, all his right in a messuage, and forty-four acres of land in this township, formerly Alice Bevant's, wife of Richard Bevant, and died in the 9th of the said King.
>
> The Gourneys remained in possession till the reign of Henry VII.
>
> The Cursons enjoyed it in the reign of queen Elizabeth; from the Cursons it came to the Yelvertons, until Sir William Yelverton, bart. sold it about 1642, to John Walpole, esq. of Bromesthorpe.

Extraction: Sir John I (G27) or near-collateral lord in Henry II's reign; Sir John V (the d. 1408 sheriff/MP) released 44 acres to Hugh Bavent 1400-01 + died 1407-08; Gurney tenure to Henry VII's reign, then Cursons (Elizabethan), Yelvertons, Walpoles from 1642.

### Harpley — Uphall Manor (pp. ~139–140)

> [Earlier history: Laurence de Manors, William de Manors with Margaret his wife, 3 and 31 Edw. I.]
>
> After this, by a deed dated November 26, in the 18th of Edward II. at Harpley, Walter son of Robert de Meleford, grants to his lord, Sir John de Gourney, rector of the church of Harpley, his messuage called Uphall, with all the homages, and services of his free tenants, view of frank-pledge, free bull and boar, all perquisites of court, and all other liberties late Ralph's, son of Walter de Manors, with wards, reliefs, escheats, &c. with all the lands that Mariona, late wife of the said Walter, holds for life, being of his right and inheritance; and all the tenements which Sir Henry de Walpole, knt. Godfrey son of Acelina de Harplee, and Thomas Elvyn, of Houghton, hold of the said Mariona, during her life, and which, after her decease, ought to descend to the said Walter and his heirs, the said John de Gourney paying one clove per ann. — Witnesses, Sir Henry de Walpole, Thomas de Feltham, Edmund Laurence, Oliver de Massingham, Ralph de Walsingham, William de Harplee.
>
> And the said manor, tenements, &c. were by deed of the said John de Gourney, dated on Monday the feast of St. Thomas the Apostle, in the 6th year of king Edward III. granted to his nephew, John de Gourney, and Jane his wife, and their heirs.
>
> Here is an annual fair kept on the 25th of July, granted in the 25th of Edward I. to John de Gourney, lord, patron and rector of the town; and it belongs to the rector for the time being.

Extraction:
- **26 Nov 1325 Uphall deed**: Walter son of Robert de Meleford grants Uphall to Sir John de Gourney rector with full lord-tenant rights, free bull/boar, view of frankpledge, court perquisites, plus the reversionary lands held for life by Mariona (Walter's late wife), Sir Henry de Walpole, Godfrey son of Acelina de Harplee, and Thomas Elvyn of Houghton. Rent: one clove p.a.
- **Witnesses** to the 1325 deed: Sir Henry de Walpole; Thomas de Feltham; Edmund Laurence; Oliver de Massingham; Ralph de Walsingham; William de Harplee.
- **21 Dec 1332 (Monday, feast of St Thomas the Apostle, 6 Edw. III) onward grant** by Sir John de Gourney rector to his nephew **John de Gourney + Jane his wife and their heirs.** This is the transfer to G25 John III (the nephew-heir) already in the Harpley place file.
- **25 Edw. I (1297) royal grant** of an annual fair on 25 July (St James's Day) to John de Gourney as lord, patron, and rector, the fair belonging to the rector for the time being. New economic-history detail for Harpley.

### Harpley — St Lawrence church arms in windows (p. ~141)

> In the windows of the church were the arms of Gourney, argent, a cross, ingrailed, gules; — of Balsingbourne, gyrony of eight, or, and azure; of Noiers, vairy, argent and gules; of Calthorpe, checque, or, and azure, a fess, ermine.

Extraction: Confirms the Gourney engrailed-cross arms at Harpley. Balsingbourne, Noiers, and Calthorpe arms in adjacent panels.

### Harpley — Chancel grave-stone of the rector (p. ~141)

> On the pavement of the chancel lies an old marble grave-stone, whereon was the portraiture or effigies of a priest, with two shields and a rim of brass, now torn off: by the incision of the stone made to let the letters in on the rim, it appears to be —
>
> "Hic Jacet corpus Folas de Gournay, quonda' recioris et patroni hujus ecclesie. cuj; a[ni]e p[ro]pitietur Deus, Amen."
>
> — He died rector in the 6th of Edward III.

**OCR / reading correction.** Armstrong's printed reading "Folas de Gournay" is a transcription error or mediaeval-script artefact for **"Joh'is de Gurnay"** (Johannis = John). The parallel transcription preserved on the church monument and recorded in `research/places/harpley.md` reads "Joh'is" / Johannis correctly. The rector is **John, Rector of Harpley**, d. 6 Edw. III = 1332. New physical-monument context: Armstrong observed in 1781 that the **two shields and brass rim had been torn off** but the lettered incision survived.

### East Barsham — 1440 Woolterton's Manor confirmation (Gallow hundred, pp. ~7–9)

> Thomas Gournay, esq. and John Hunt, son of William Hunt, of East Basham, confirmed to John Wode, of Briston, esq. and his heirs, &c. the manor of East Basham, formerly Roger de Woolterton's, and John de Bryston, of Bryston, esq. released to John Wode aforesaid, all his right in this manor, April 2, in the 18th of Henry VI. and Catherine, widow of William Hunt, released to him all her right.

Extraction: 2 April 1440 East Barsham (Woolterton's) confirmation; Thomas Gournay esq. (most parsimoniously G21 Thomas I, active to 1441 per project) + John Hunt + Catherine widow of William Hunt + John de Bryston + John Wode of Briston. Distinct from the 1434-35 and 1445 East Barsham conveyances already in the G20/G21 fact-sheets.

### East Barsham — Berningham's 1447 attorney-delivery of seisin (Gallow hundred, p. ~11)

> In the 25th of Henry VI. March 9, John Hines, of Swaffham in Norfolk, sells to John Wode the manor of Berningham for fifty marks; and on the 10th of the said month, Robert Mompynson, of Wisbich, and Catherine his wife, late wife of William Hunt, of East-Basham, enfeoffed John Wode, of Honingham, and Margery his wife, &c. in four messuages, four tofts, &c. called Berningham's, in this town, and Snoring, with the homages of other messuages, held by John Lynge for life; and, at the said time, a Thomas Gurney, esq. their attorney, to deliver seisin to John Wode and Margery, and to Robert, son of the said John and Margery.

Extraction: 10 March 1447 Berningham's enfeoffment; Thomas Gurney esq. (most parsimoniously G20 Thomas II, since G21 Thomas I was probably dead before 1444 per DG-Supp) as attorney delivering seisin to John Wode + Margery + their son Robert.

### North Barsham — Wauncy's Manor at Southall (Gallow hundred, p. ~15)

> Wauncy's Manor, or Southall. Hugh, who was lord of West-Basham, was ancestor of the family of de Wauci, and held this lordship at the survey of the Earl Warren.
>
> The family of Suthale, or Southwell, had some interest herein under the Wauci. In the reign of Edw. II. it came to Edmund Gurney, by the marriage of Catherine, daughter of Sir William Wauch, and remained in that family.

Extraction: Corroborates G23's North Barsham parallel inheritance. The **"reign of Edw. II."** dating is Armstrong-side error; same volume gives 47 Edw. III (1373) for the same Wauci → Gurney transfer at West Barsham. Do not adopt.

### West Barsham — descent + chancel monument + arms list (Gallow hundred, pp. ~17–19)

> BASHAM, WEST. Hugo de Wauci held this manor of the Earl Warren, and it remained with his descendants till the 47th of Edw. III, when it came to Edmund Gurney by marriage.
>
> This estate was long in the family of the Gurneys. Edmund died seised of it in the year 1641, and his son Henry sold it to the family of Calthorpe. From the Calthorpes it came to Dr. Charles Morley, M. D. who was lord in 1720...
>
> This family of de Gourney was of great antiquity, and lords of Harpley. Matthew de Gourney lived in the reign of Henry II. and married Rose, daughter and heir of Reginald de Burnham. William de Gourney was his son and heir, and had Sir John de Gourney, who was in arms against king Henry III. and one of the same name was lord in the beginning, and 8th of Edw. I. and John de Gourney was rector, patron, and lord also, of Harpley, in the 31st of the said king; and in the 9th of Edw. II. settled on John de Gourney, his nephew, (son of Catherine) and Jane his wife, the manor of Harpley, remainder to William and Edmund, brothers of John. This Edmund was he, who by the marriage of Catherine, daughter of Sir William, and sister and heir of Sir Edmund de Wauci, brought this lordship of West-Basham into the Gurney family.
>
> The arms of Gurney were argent, a cross ingrailed, gules, and impaled the arms of Wauci, gules, three dexter hands erect, argent; also Calthorpe, Lovell, Holdich, Blennerhasset and Lewknor; also they impaled Jernegan, and sable, a chevron between three leopards heads, &c. probably Wentworth.
>
> [Chancel monument:] Caducum hoc aeternat Marmor Edwardus Gourney, filius et heres Tho. Gourney Armig. et Marthe filie Edu. Lewkenor de Denham, in Com. Suff, Militis, obiit Aug. 1641.

Extraction:
- **47 Edw. III (1373)** Wauci → Edmund Gurney West Barsham transfer (sharpens project's "after 1372").
- **"Edmund died seised in 1641"** body-text reading is an Armstrong-side error or OCR slip for **"Edward"** (the chancel monument names Edward Gourney as the decedent).
- **Edward Gourney d. Aug 1641** (chancel monument), son of Thomas Gourney + Martha Lewknor of Denham; project G15 Henry's grandson, the West Barsham heir.
- **Sale window 1641–1661** for the West Barsham alienation to the Calthorpes via Henry II.
- **Eight-family impaled / quartered arms list at West Barsham church**: Wauci, Calthorpe, Lovell, Holdich, Blennerhasset, Lewknor, Jernegan, probable Wentworth (the unidentified "sable, a chevron between three leopards' heads"). Seven match known marriages; the probable **Wentworth** is a new research lead.
- **Harpley-rooted pedigree skeleton**: Matthew + Rose de Burnham → William → Sir John (vs. Henry III) → rector John (1303 onwards) → 1316 nephew-John + remainders to brothers William and Edmund. Armstrong **collapses two Edmunds across generations** (1316 brother-Edmund vs. 1373 West Barsham acquirer); project's G24 / G23 chain preserves the intervening generation.

---

## Vol. 6 — South Erpingham, Grimshoe, Happing, Brothercross

### Houghton — Gaunts and Gurneys manors (p. ~100)

> The manors of Walsingham, and mills, were separated from the abbey, and remained so till 1756, when they were purchased, with divers lands, from Norbone Berkley, lord Bottetourt, by Henry Lee-Warner, esq. who also purchased divers other lands in Walsingham and Houghton, and the manors of Gaunts and Gurneys in Houghton; and died, as before mentioned, in 1760.

Extraction: Two named manors "Gaunts and Gurneys in Houghton" purchased in 1756 by Henry Lee-Warner from Lord Botetourt. Houghton (next Harpley) was within the Gurney landed footprint; the manor names suggest former Gurney ownership of one or both. Post-Gurney descent.

### Burnham — 1406 Walsingham trust license (p. ~115)

> Licence was granted in the 7th of Henry IV. John Gourney and John Drew, parson of B[urnham?], to amortize twenty acres of land in Burnham, to celebrate the obit of Sir Edmund de Reynham and Christian his wife; and in the said year to Sir Thomas Erpingham, &c. to sell the manor of Swanton-Nowers, with that of Branches, in Wiveton, to this Priory.

Extraction: Independent witness to the **1406 Burnham Walsingham trust** already in the G23 companion (Patent Roll Henry IV, p. 2, m. 29 (1406): "Johanni Gournay, Johanni Drew persona ecclesie de Harplee..."). Armstrong abbreviates the parson's parish to "B" (likely either Burnham, where the land lay, or Harplee per the original Patent Roll); the date 7 Henry IV (= 1405-06) matches.

### South Erpingham parish — Edmund Gournay + Hugh de Holland trustees (p. ~301)

> Edmund Gournay and Hugh de Holland, as trustees, gave the advowson of this church to the abbey of West Dereham, who presented in 1410.

Extraction: G23 Edmund Gourney trust activity; Hugh de Holland as co-trustee. The advowson went to West Dereham abbey (presentation 1410). Additional Edmund / West Dereham datum.

### Sir John Howard's will — silver cup to Sir John Gurney (p. ~116)

> [Sir John Howard's bequests:]... to Sir William Beauchamp, and Sir John Marmion, knts. to each a silver cup with a cover, to be made new, weighing 10lb. in gross; to Sir Stephen Hales, John de Burgh, Richard de Sutton, knts. and [Sir John] Gurney, to each of them a new cup to be made of silver, with a cover, each of the weight of 10 marks in gross.

Extraction: **Sir John Gurney V in Sir John Howard's intimate gift circle.** Howard's will (late 14th / early 15th century — Howard's son John died on a journey to the Holy Land in 1410) leaves a 10-mark silver-with-cover cup to "Gurney" (= Sir John V) alongside Hales, Burgh, and Sutton. The same Howard / Plays / Heydon network the project already documents at G18 / G19 / G20. New social-network detail for Sir John V.

---

## Vol. 7 — Happing, Humbleyard, Heath (Lessingham, Bedingham, Bastwick, Langley priory)

### Lessingham — Gerard de Gournay donation to Bec (p. ~67)

> Afterwards this lordship was granted from the crown, and given by Gerard de Gournay, lord of it, to the abbey of Benedictine monks, at Bec, in Normandy, which abbey subjected to their cell, at Okebourne, in Wiltshire, as appears from a charter of Henry II. exemplified among the rolls of the Tower though not mentioned in Neustria Pia.

Extraction: **Gerard G32's donation of Lessingham to Bec** — already extensively covered in project research (G32 Gerard companion). Armstrong corroborates Lessingham specifically as one of the granted manors; the Bec cell at Okebourne (Wiltshire) reception is an additional downstream-house detail not currently in the Gerard companion.

### Bedingham — Hugh de Gournay → Stuteville with Gunnora (p. ~278)

> In the reign of Henry II. Hugh de Gournay was lord; and in the beginning of king John's reign Hugh de Gournay, a Norman baron, gave it Nicholas de Stutevile, with Gunnora, his daughter, in marriage: Nicholas was soon after disseised of it, as land of the Normans, for their rebellion in 1203, by king John, who in the next year restored to Nicholas, the son, all that his father Nicholas had been deprived of.
>
> At the seizure of the manor, and stock, it was assigned to Walter de Cantelupe, during the king's pleasure.

Extraction: Already in project research (Bedingham descent in `research/topics/anderson-yvery-harpetre-gournay-collateral.md`); Armstrong's 1203 disseizure dating is two years earlier than the standard 1205 reading carried elsewhere in the volume and in the project — likely Armstrong-side error or compressed-narrative shorthand.

### Bedingham — Stuteville heirs (p. ~278 continuation)

> Sir Nicholas de Stutevile granted in the 16th of Edward I. this lordship to Nicholas de Castello, and his heirs, to be held by one knight's fee... In the 3d of Edward II. Gregory de Castello, of Raveningham, had a charter of free-warren, this manor being held of the lord Bardolph, as heir to the Gournays.

Extraction: Bardolph "as heir to the Gournays" — independent printed corroboration of the Bardolph senior-line inheritance.

### Bastwick (or adjacent manor) — granted to Hugh de Gourney by Henry I on Baynard rebellion (p. ~278 area)

> It was granted to Hugh de Gourney by Henry I. on the rebellion of lord Baynard, and by Julian, daughter and heiress of that family, came to William lord Bardolph; her husband. Thomas de Ages, or D'aggs, was lord in the 3d of Edward III. held of Thomas lord Bardolph.

Extraction: **New specific dated grant** — Henry I (1100–1135) granted a manor to Hugh de Gournay on Baynard's rebellion (the William Baynard rebellion, 1110). This is **G33 Hugh III** (b. c. 1075, died c. 1130s) — direct attestation of his receiving a Baynard-forfeited manor in the c. 1110-1115 window. Useful for the Hugh-III career-attestation chain in the senior-line topic file and G33 companion.

### Langley priory — Sir Hugh Gourney burial (p. ~310 area)

> In the priory church were buried — Sir Robert Thurkelby, Sir Thomas Roscelyn, Sir Peter Roscelyn, **Sir Hugh Gourney**, Sir Jeffrey Say, Sir Henry [Wodehouse?], Sir Fulk Kerdeston, Sir William Kerdeston, and Margaret, his wife, who died in 1328...

Extraction: A "Sir Hugh Gourney" buried at Langley Priory (Norfolk), in a witness list dating to the late 13th / early 14th century. Likely collateral — not in the project's senior or junior direct lines. Worth flagging as a new lead.

### Honingham + cross-volume Lord Mayor reference (Sir Richard Gorney) — see vol. 4

---

## Vol. 8 — Eynsford, Mitford (Cranworth + Swathing + Letton), Shropham (Great Ellingham), South Greenhoe

### Mitford — Cranworth + Swathing + Letton — King-John-era Gurney lordships (pp. ~125–126)

> The ancient family of de Gurney were [lords] of this town, Cranworth, and Letton, in the [reign] of king John.

Extraction: Cranworth, Letton, and the unnamed parish in which this paragraph sits (Swathing or its parent) were held by the Gurneys in King John's reign. This aligns with project standing-fact #2 (junior Norfolk branch through Walter G31) and the existing G31 Walter companion ("The Gournays of Swathings... were that younger branch... subenfeoffed as mesne lords of the manors of Hingham Gurney's, and Swathings in Hardingham, before the forfeiture of his Norman and English estates, by Hugh de Gournay V. in 1205.").

### Mitford — 1316 (9 Edw. II) John de Gurney's free-warren plea against William de Swathing (p. ~126)

> Edmund de Swathing, as lord, presented to the church of Cranworth in the reign of Edward I. and John de Gurney in the 9th of Edward II. impleaded William de Swathing for chacing his hares without his licence, in his free-warren of Swathing.

Extraction: **1316 (9 Edw. II) John de Gurney impleaded William de Swathing for chasing hares without licence in his free-warren of Swathing.** Dated lordship attestation. New.

### Mitford — Hugh de Gurney charter to Robert the Burgundian + Saint-Hildevert at Hardingham (pp. ~152–153)

> Hugh de Gurney granted, by deed without date, to Robert, the Burgundian, the manor of Swathing, in Hardingham, with the manor and appurtenances in fee, for 20s. sterling per ann. and for the gift of one horse at the time of making this grant. It was granted at Ferretre, a town probably in Normandy, the Gurneys being [originally] of Gourney, a town in Normandy, from which they took their name, and came into England on the Norman invasion, and this Hugh gave to the chapter of the church of St. Ildebert, of Gourney, in Normandy, the said church.

Extraction:
- **Undated Hugh de Gurney charter** to Robert the Burgundian — manor of Swathing in Hardingham, 20s. annual rent + horse gift, granted at "Ferretre" (probably La Ferté). The "Hugh de Gurney" here is most likely Hugh V (forfeited 1205), the senior-line Norman baron giving a Norfolk manor in fee to a Burgundian retainer in Normandy; an alternative reading is Hugh IV (c. 1098–c. 1180). Either way, **a new undated primary charter mention** for the senior-line Hugh.
- **Saint-Hildevert at Gournay donation extended to Hardingham church** — Hugh gave the church of Hardingham to the chapter of St-Hildevert at Gournay. Extends the existing project pattern (Caister + Cantley tithes per Potin 1842; senior-line Saint-Hildevert relationship in G33 companion + Gournay-en-Bray place file) to a **third Norfolk church**.

### Mitford — 1257 + 1268 John de Gurney tenure at Hardingham/Reymerston (p. ~153)

> In the 41st of Henry III. [1257] Ralph Redker conveyed lands to William de Swathing, and in the 52d of that king [1268], William de Swathing held of John de Gurney a messuage, fifty-four acres of land, and three of wood, in this town and Reymerston, with free grinding, without toll, at John's-mill, called Ravensholm, as he and his ancestors before had at Little-mill, whilst Little-mill was repairing; and if they should be both out of repair, that they could grind at neither, then John to pay 6s. 5d. per ann. till they could grind.
>
> John likewise granted to William, and his heirs, a free bull, and ram, with a free fold-course, and common of pasture over all his lands for all his cattle (tempore aperto) in time of shack, as his ancestors had.

Extraction: Substantive dated late-13th-century lordship attestations for John de Gurney at Hardingham (1257 + 1268), with named mill (Ravensholm) and a free bull + ram + fold-course grant. **New dated tenure detail** for the Swathing-line Gurneys in the late Henry III window.

### Mitford — "Anthony Gurney lord 26 Henry III" — error caveat (p. ~153)

> Anthony Gurney, esq. was lord in the 26th of Henry III. and soon after it was in the family of Thwayte.

Caveat: 26 Henry III = 1242 is anachronistic for an Anthony Gurney; Anthonys are 15th–16th-century in the family. Read as Armstrong-side error, possibly for 26 Henry VIII (1534/35).

### Letton — Hugh de Gurnay tenement grant to Lewes priory (p. ~157)

> Hugh de Gurnay, of Leiton, granted them [Lewes Priory] a tenement, &c. without date.

Extraction: Undated grant to Lewes Priory by Hugh de Gurnay "of Leiton" (= Letton, Norfolk). Pattern matches the senior-line foundation-gift habit; useful for senior-collateral topic file.

### Mitford — Thuxton — 1381 Edmund Gurney + 1500 William Gurney advowson presentations (p. ~265)

> The Gurneys were early enfeoffed of the manor that Godric held, and the Thurstons held it of them.
>
> John and Richard de Thurston were lords in the 9th of king John, and the patronage belonged to it.
>
> In 1381 Edmund Gurney presented to this church. In 1387 William de Thurston was lord; and in the year 1472 John Ovy, of Worstead, was lord of the manor of Thuxton; and Thomas, his son, who died in 1473, ordered it to be sold to pay his debts. In 1500 William Gurney presented to the church.

Extraction:
- **1381 Edmund Gurney advowson presentation at Thuxton** — G23 Edmund's advowson activity; corroboration.
- **1500 William Gurney advowson presentation at Thuxton** — most parsimoniously G19 William IV (d. 1508 per G19 fact-sheet). New attested advowson presentation for G19.

### Shropham — Great Ellingham capital manor + Anthony Gurney + Margaret Gurney 1641 (pp. ~254–256)

> [Manor descent through Spelman line:] Anne, one of the two daughters and co-heiresses of Thomas Conyers, esq. his brother [married Thomas Spelman]; he died in 1483, and in 1499 Thomas Spelman, gentleman, of [Great] Ellingham, held it of Shropham hundred. who died seised, and by his will, dated this year, ordered to be buried in the church... Henry his brother inherited; he died without issue in 1525, and was buried here; upon which this manor went to Anthony Gurney, esq. of North Barsham, in right of Margaret his wife, one of the daughters and co-heiresses of Sir Robert Lovell, by Ela Conyers, his wife, who was sister to Ann Conyers, mother to Henry Spelman; but Berryhall went to the heirs of William De-Grey, of Merton, in right of Christian his wife, the daughter and co-heiress of Thomas Manning. After 1641 it went to Margaret Gurney, his aunt, who married Mr. Henry Davy, of Great Ellingham, whose sole daughter and heiress, Mary, married Sir Roger Potts, bart. of Great Ellingham and Mannington, who sold it to Mr. Francis Colman, of Norwich, the present lord.

Extraction:
- **G17 Anthony Gurney of North Barsham inherited Great Ellingham 1525** through his wife **Margaret Lovell**, one of the daughters and co-heiresses of **Sir Robert Lovell by Ela Conyers**. Ela Conyers was sister to Ann Conyers (mother of Henry Spelman) — Lovell + Spelman were first cousins by Conyers. New kinship-explanation detail.
- **1525 (Henry Spelman d. s.p.)** is the date the manor came to Anthony Gurney + Margaret Lovell. New precise date.
- **"After 1641 it went to Margaret Gurney, his aunt, who married Mr. Henry Davy of Great Ellingham"** — Edward Gourney's death Aug 1641 (vol. 5) triggered the manor transfer to Edward's paternal aunt **Margaret Gurney** (G15 Henry's daughter, already in the G15 children-table). Margaret + Henry Davy → daughter Mary → Sir Roger Potts, bart. → sold to Francis Colman of Norwich. Brand-new precise descent chain post-1641 for Great Ellingham, distinct from the West Barsham (Henry II) line.

### Shropham — Great Ellingham rectory mediety: Warners → Gurnays → Davys → Potts (p. ~261)

> After the division of the Mortimer's estate this advowson was allotted to John Fitz-Ralph, as part of the inheritance of Margery Mortimer, his wife; and from that time it passed with the manor of Ellingham-hall, from Fitz-Ralph to Conyers, from them to the Warners, so to the Gurnays, and Davys, and after to the Potts, who sold it to Mrs. Windham.

Extraction: The Great Ellingham church's larger rectory mediety descended through the same chain. **Warners → Gurnays** is a new linkage — the Gurneys received the rectory mediety **from a Warner predecessor** (presumably between 1525 Anthony Gurney's inheritance and the same Warner family who later held nearby Walsingham manors per vol. 6). Then Gurnays → Davys (Margaret Davy 1641) → Potts → Windhams.

### Shropham — Anthony Gurnay of Great Ellingham buried 1557 (p. ~256)

> Anthony Gurnay, of Great Ellingham, esq. was buried in this church in 1557.

Extraction: G17 Anthony was already known to have died 4 Jan 1555/6 per Blomefield West Barsham (G15 fact-sheet n1). Armstrong's "buried in this church in 1557" is **a year later than the project's death date**. Possible explanations: (a) Armstrong-side editorial error; (b) calendar slip (Old vs New Style); (c) a delayed burial for some reason. Worth flagging.

### Shropham — Rockland St Peter — Kirkhall Moynes and Gurney's manor (p. ~129)

> Kirkhall Moynes, and Gurney's, were distinct manors at first, though they have been long united...
>
> In 1546 John Berney settled his manor, called Barrie's, alias Gurney's, on Ralph Chaumberlain, esq.

Extraction: A "Gurney's manor" at Rockland St Peter (Shropham hundred), united with Kirkhall Moynes; later "Barrie's alias Gurney's" settled by John Berney on Ralph Chaumberlain 1546. Collateral; no further detail.

---

## Vol. 9 — Gallow, Smithdon (Hunstanton), Freebridge (Heigham, Drayton, Hellesden, Taverham, Irstead, Merton)

### Smithdon — Walsingham Parva Sessions 12 Oct 1637 — Edward Gourney as Justice of the Peace (p. ~16)

> SESSIO GENERALIS Pacis Domini Regis tent. apud Walsingham Parvam ibid. in com. praed. die jovis videlicet duodecimo die Octobris anno regni domini Caroli nunc regis Angliae &c. tertio decimo coram **Hammone L'Estrange milite, Roberto Baron, et Edwardo Gournay armigeris justiciariis dicti domini regis ad pacem** nec non &c. assign.

Extraction: **12 Oct 1637 (13 Charles I) Sessions order at Little Walsingham**. Edward Gourney sat as a Norfolk Justice of the Peace alongside Sir Hamon L'Estrange of Hunstanton and Robert Baron. The case concerned a parish-rates dispute at Hunstanton. **First known administrative office attestation for Edward Gourney**, four years before his Aug 1641 death. Brand-new.

### Heigham — John Gournay + Alice his wife (Sir John V) — 19 Richard II conveyance (p. ~34)

> John Gournay, and Alice his wife, were in possession of [Hellesden mediety] in the 19th of Richard II [1395-96], when they passed it, with the manor of Drayton, and the advowson of the two chantries in this town, to John Winter, &c. and in the 4th of the said Richard II. John Hokere conveyed this lordship to John Churchman and Bartholomew Marsh, citizens of London, feoffees of John de Hayleſdon.

Extraction: **Sir John Gurney V + Alice his wife** in possession of Hellesden + Drayton + chantry advowsons, 19 Richard II (1395-96). Conveyed to John Winter (already in the existing G23 companion's Sir John V narrative). Alice is the wife — the John-de-Hayleſdon connection in the next sentence (the same Hayleſdon whose 1384 Husting will is in v63) strongly supports the **Alice Heylesdon** identification over the Wansey-pedigree Alice Bavard variant.

### Heigham (continued) — 1398 + 1401 John Gourney presented to this church as lord (p. ~34)

> yet in 1398, and 1491 [read: 1401], John Gourney presented to this church as lord.

Extraction: **1398 and 1401** dated Heigham advowson presentations as lord by Sir John V. Two new attestations.

### Drayton — 3 Henry IV John Gournay holds two fees (p. ~21)

> In the 3d of Henry IV. John Gournay held two fees here and in Drayton, sometime John Spring's, of the lord Morley, as part of the barony of Rye.

Extraction: **3 Henry IV (1401-02)** Sir John V held two fees at Heigham + Drayton, formerly John Spring's, of lord Morley's barony of Rye. New fee-attestation for Sir John V.

### Hellesden — same conveyance recorded again (p. ~21)

> But part of this lordship was alienated probably about the end of Edward III. by Sir John de la Pole, in the 19th of Richard II. John Gourney conveying it, with the advowson, to John Winter and his heirs, by fine, which Joan, wife of Sir John de Seaton, held for life; yet in 1398, and 1401, John Gourney presented to this church as lord.

Extraction: Duplicate of the Heigham entry; the 1395-96 fine to John Winter affected both the Hellesden and Drayton properties.

### Taverham — John Gournay + Alice his wife — 1395 advowson settled (p. ~45)

> In 1395, the advowson of one of these portions was settled by fine on John Winter, &c. by John Gournay and Alice his wife, with Drayton and Helleſden manors.

Extraction: 1395 advowson-settling fine — third dated attestation in the John-Gournay-and-Alice cluster.

### Irstead — Anthony Gourney purchases from Sir Richard Southwell 1541-42 + dies lord 4 Jan 1555/6 (p. ~17 area)

> In the 33rd of Henry VIII [1541-42], Sir Richard Southwell, knt. conveyed by fine to Anthony Gourney, esq. the manor of Irstead, with lands in Barton, Neatishead, Smalburgh, &c. and the said Anthony died lord on January 4, in the 2d and 3d of Philip and Mary, whose grandson, Henry, is said, by Mr. Parkin, to hold his manor of the bishop of Norwich.

Extraction:
- **1541-42 purchase**: Sir Richard Southwell sold Irstead manor (with lands in Barton, Neatishead, Smalburgh) to G17 Anthony Gourney by fine.
- **4 Jan 1555/6 (2 & 3 Philip and Mary)** G17 Anthony died as lord of Irstead — matches Blomefield-via-G15-fact-sheet death-date exactly.
- **Henry** (G17's grandson — i.e., G15 Henry) later held it of the bishop of Norwich, consistent with G15 fact-sheet's "Irstead manor of the Bishop Norwich" tenure note.

### Merton — Anthony Gurnay sold to Sir Richard Southwell c. 1540 (p. ~25)

> In 1402, on the division of the Mortimer estate, this manor fell to the share of Sir John Fitz-Ralph, knt. in right of his wife; and from that time it went with Ellingham-hall manor till 1540, and then was sold by Anthony Gurnay, esq. to Sir Richard Southwell, with the advowson of Trinity church here, and Sir Edward Chamberlain released his right in it. It extended then into Riling, Cranworth, Hingham, Carbrooke, and little Ellingham.

Extraction: **c. 1540 sale of Merton manor by G17 Anthony Gurnay to Sir Richard Southwell**. Same Southwell who sold Irstead to Anthony in 1541-42 (item above) — a **counter-direction estate-rationalisation pair** between Anthony and Southwell in 1540-42. New 1540 alienation detail for G17 Anthony.

### South Greenhoe — Merton — early Gurney tenure (p. ~25)

> [Sir Fulk Baynard:] in the time of Henry III. he held in Merton one fee, of which John de Gurney held one quarter of him.

Extraction: 13th-century 1/4-fee tenure of Merton by John de Gurney under Sir Fulk Baynard. Early junior-branch lordship attestation.

---

## Vol. 10 — Blofield, Hundred of Norwich (Cathedral cloister, Eminent Norfolk Men prefatory matter)

### Norwich Cathedral cloister — Gournay arms (p. ~149)

> In 1382, Walter de Berney, citizen of Norwich, gave 100l. towards the iron work and glazing of the cloister windows; which work was perfected at the charge of the several families of Morley, Shelton, Scales, Erpingham, Gournay, Mowbray, Thorpe, Savage, &c. whose arms were to be seen in the windows of the cloister, above the bars, before the glazing was demolished. This famous and elegant cloister was finished in 1430, in the hundred and thirty-third year from its being first undertaken.

Extraction: **Gournay arms displayed in Norwich Cathedral cloister windows** alongside Morley, Shelton, Scales, Erpingham, Mowbray, Thorpe, Savage etc. — the cloister glazing was a 1382-1430 work co-funded by these families. Significant late-14th-century civic-heraldic standing for the Gurneys, complementing the Norwich-counsel attestation of G23 Edmund (Norwich City Treasurers' fee in v63).

### Norwich — Gournay's Place capital messuage (p. ~204)

> The capital messuage called Gournay's Place, was in 1338 the city house of Thomas Gawdy, esq. and afterward belonged to the Pastons, from whom it passed to the family of the Cookes. Adjoining to the north side of this house was the key anciently called Kyrmer-hoppe, with a messuage belonging to the Berneys. The messuage of Sir Miles Stapleton, knt. lay on the north of the former and joined to it, afterward the property of Edward Grey, esq. and to the north of that the house of Sir William Boleyn, knt. afterward of the lady Anna Boleyn.

Extraction: **A Norwich capital messuage named "Gournay's Place"** — by 1338 already owned by Thomas Gawdy esq. (so already alienated by the Gurneys by 1338). Later Pastons, then Cookes. Adjacent properties: Berneys (Kyrmer-hoppe key), Sir Miles Stapleton (then Edward Grey), Sir William Boleyn (then Anna Boleyn). This is a **distinct Norwich Gurney building** from the St Gregory's parish house named in G20 Thomas II's 1471 will. Useful for the wider Norwich-civic footprint of the family.

### Eminent Norfolk Men — Sir Richard Gurney, Lord Mayor of London (pp. ~270 ff.)

> RICHARD GOURNEY, or GURNEY, says Lord Clarendon, was a man of wisdom, and courage, and being lord mayor of London on the King's return from Scotland, 25 Nov. 1642, gave him a great entertainment, at which the Queen, Prince, and the whole court of lords and ladies, were present; and on their return to Whitehall, they were attended by the whole city. When the outcry against the bishops was at the height, Sir Richard, with great courage, opposed the fanatic humours of the courts of aldermen and common council...

Extraction: **Sir Richard Gurney biographical entry** — the collateral cadet from G19's son Thomas of Dartmouth → Essex → London Gurney line, lord mayor 1641-42, royalist, opposed Parliament, imprisoned, defied the Commons through to his 1647 death. Already in the project via G19 fact-sheet n13. Useful corroborating citation source.

Cross-references to Sir Richard in vol. 10: numerous patron-list and charity-trustee references (e.g., pp. ~570, ~590, ~616, etc.). Each is a single-mention corroboration with no further genealogical detail.

### Other vol. 10 references

Sir Richard Gurney's daughter / co-heiress applied to Christ's Hospital (p. ~575); Sir Richard's involvement with the Lumley / Earl of Essex / Whitmore / Nevill / Croydon-and-Deptford-property circle (multiple pages); the Deptford / Croydon property bought from Sir Richard in 1641 by London trustees for £40 p.a. (p. ~571). Useful for any future expansion of the Sir Richard biography but contains no new Norfolk-Gurney genealogical content.
```

### 3. Write Armstrong validation file

New file write: `sources/validations/armstrong-norfolk-1781.md`.

```markdown
# Validation — Armstrong, History and Antiquities of the County of Norfolk (1781)

Source ID: `armstrong-norfolk-1781`

## Source examined

Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, 10 vols. (Norwich, 1781). Per-volume Internet Archive items at `https://archive.org/details/bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_N/` for N in 1..10.

## Portion examined

Full ten-volume text search for surname variants `Gurney`, `Gourney`, `Gournay`, `Gorney`, `Gurnay`, `Gurnoy`, `Gurnie` against each volume's Internet Archive djvu OCR derivative. 118 hits identified across vols 1, 3, 4, 5, 6, 7, 8, 9, 10 (vol. 2 has no Gurney content). Hits are transcribed in `sources/corpus_supplement/armstrong-norfolk-1781-selected-gurney-references.md`, organised by volume → parish → theme.

Coverage map: vol. 1 = Earsham + Guiltcross + Loddon hundreds (plus Eminent Norfolk Men prefatory matter); vol. 2 = Clavering (no hits); vol. 3 = North Erpingham + Humbleyard; vol. 4 = East Flegg + Clackclose + Forehoe (Hingham, Kimberley); vol. 5 = Freebridge and Half + Gallow; vol. 6 = South Erpingham + Grimshoe + Happing + Brothercross; vol. 7 = Happing + Humbleyard + Heath (Lessingham, Bedingham, Bastwick, Langley priory); vol. 8 = Eynsford + Mitford (Cranworth + Swathing + Letton) + Shropham (Great Ellingham); vol. 9 = Gallow + Smithdon (Hunstanton 1637 Sessions) + Freebridge (Heigham, Drayton, Hellesden, Taverham, Irstead, Merton); vol. 10 = Blofield + Hundred of Norwich (Cathedral cloister; Gournay's Place; Sir Richard Gurney biography).

## Method and limitations

Working from each volume's Internet Archive djvu OCR derivative. Long-s normalized to modern `s`. The OCR carries scattered character errors (e.g., "Govnnty" for "Gourney"; "Folas" for "Joh'is"; "Gurnoy" appearing where "Gourney" was intended). Each Gurney-touching slip is flagged inline in the corpus supplement. No page images were captured into `sources/media/`; if a specific page becomes important for downstream citation work (e.g., the West Barsham chancel monument plate, the Walsingham Parva Sessions order, or the Norwich Cathedral cloister arms list), it can be re-photographed in a future patchset.

Volume-specific OCR / editorial caveats documented in the corpus supplement: vol. 5 "Folas de Gournay" → "Joh'is de Gurnay"; vol. 5 North Barsham "Edw. II." → "Edw. III." (Wauncy transfer); vol. 5 West Barsham "Edmund died seised in 1641" → "Edward" (per chancel monument); vol. 5 pedigree skeleton collapses 1316 brother-Edmund and 1373 West Barsham acquirer-Edmund into one figure; vol. 7 Bedingham "rebellion in 1203" is two years earlier than the standard 1205 reading and is most parsimoniously an Armstrong-side editorial shorthand; vol. 8 Hardingham "Anthony Gurney, esq. was lord in the 26th of Henry III" is anachronistic for an Anthony Gurney and should be read as an Armstrong-side regnal-year error; vol. 8 Great Ellingham "Anthony Gurnay buried in this church in 1557" is one year later than the Blomefield-attested 4 Jan 1555/6 death and is most parsimoniously an Armstrong-side editorial slip or a calendar artefact.

## Substantive findings recorded

- `sources/corpus_supplement/armstrong-norfolk-1781-selected-gurney-references.md` — full transcriptions of all 118 hits with parish + theme context, organized by volume.

Downstream routing to the affected research files is documented in the patchset and deferred to a follow-up patchset because each destination file has its own footnote structure.

## Patchset trail

Prepared in `sources/intake/processed/v69-armstrong-norfolk-1781-vol5-selected-gurney-references.patchset.md`; after application, archived to `sources/intake/done/`. (The file name retains the historical "vol5" suffix from the original single-volume scope; the patchset content covers all ten volumes.)
```

### 4. Downstream routing — for a follow-up patchset

Deferred to a follow-up patchset because the existing fact sheets, research companions, and place files each have their own footnote structure that warrants targeted insertion rather than scripted str_replace. The routing list, by file:

- **`fact-sheets/g15-henry-gurney-fact-sheet.md`** — update child-table row 1 (Thomas III) or add a new line under the narrative paragraph (line 157) to record:
  - **Edward Gourney's death Aug 1641** (vol. 5 chancel monument).
  - **Edward Gourney as Norfolk JP, 12 Oct 1637, at Walsingham Parva** (vol. 9 Sessions order).
  - **Hingham — Henry G15's lordship 1572 + post-Gurney 1715 William Larwood successor** (vol. 4).
  - **Great Ellingham post-1641 descent to Margaret (Gurney) Davy** (vol. 8 Shropham Great Ellingham capital manor + the related rectory mediety: Warners → Gurnays → Davys → Potts).
- **`fact-sheets/g17-anthony-gurney-fact-sheet.md`** and **`research/people/g17-anthony-gurney-fact-sheet.research.md`** — add:
  - **1541-42 Irstead purchase from Sir Richard Southwell** (vol. 9).
  - **c. 1540 Merton sale to Sir Richard Southwell** (vol. 9).
  - **1525 Great Ellingham inheritance via Margaret Lovell** with Ela Conyers / Ann Conyers kinship link (vol. 8).
  - **4 Jan 1555/6 death as lord of Irstead** (vol. 9 — matches existing Blomefield citation).
  - **Armstrong-side "1557 burial" variant** flagged (vol. 8 Great Ellingham).
- **`fact-sheets/g18-william-gurney-v-fact-sheet.md`** — supplementary citation: vol. 3 Heydon sibling-marriage list places Ann Heydon's marriage to William G18 in the network of her sisters Amy/Townshend, Dorothy/Brook (Cobham), Elizabeth/Hobart, Bridget/Paston.
- **`research/people/g19-william-gurney-iv-fact-sheet.research.md`** — add **1500 Thuxton advowson presentation** (vol. 8) and the **Cawston William Gurnay gravestone d. 10 March 1578 + wife Ann (Wayte) d. 19 Jan 1595, one son three daughters** (vol. 3, the cadet branch from G19's son Walter — corroborates Rye 1891 p. 132 visitation captured in v67).
- **`research/people/g20-thomas-gournay-ii-fact-sheet.research.md`** — 1447 Berningham's attorney-delivery of seisin (vol. 5).
- **`research/people/g21-thomas-gournay-i-fact-sheet.research.md`** — 1440 East Barsham confirmation with John Hunt (vol. 5).
- **`research/people/g23-edmund-gurney-fact-sheet.research.md`** —
  - **Sir John V + Alice his wife — 1395-96 / 1398 / 1401 / 1401-02 Hellesden / Drayton / Heigham / Taverham attestations** (vol. 9).
  - **Sir John Howard's bequest of a 10-mark silver cup to Sir John Gurney V** (vol. 6).
  - **1406 Walsingham trust license** corroboration (vol. 6) and **Edmund-and-Hugh-de-Holland trustees** advowson grant to West Dereham 1410 (vol. 6).
  - **1373 (47 Edw. III) Wauci → Edmund Gurney West Barsham transfer** (vol. 5).
  - **9 Henry IV (1407-08) Denver lord-at-death attestation for Sir John V** (vol. 1).
  - **1381 + 1500 Thuxton advowson presentations** (Edmund 1381 and William 1500 — vol. 8).
  - **Sir John V Saxthorpe c. 1411 attestation** (vol. 3) for the post-1408 Saxthorpe holding via Edmund / Thomas I.
- **`research/people/g24-john-de-gournay-iv-fact-sheet.research.md`** and **`research/people/g25-john-de-gournay-iii-fact-sheet.research.md`** — Armstrong vol. 5 pedigree skeleton corroborates the rector-uncle / nephew-John III / Edmund-brother 1316 remainder structure (with the generational caveat); 1257 + 1268 + 1316 Mitford-cluster attestations (vol. 8) supply additional John de Gurney datapoints for the 13th–early-14th-century junior-branch chain.
- **`research/people/g27-sir-john-de-gournay-i-fact-sheet.research.md`** — vol. 5 corroborates Sir John I "in arms against king Henry III" (Barons' War).
- **`research/people/g29-matthew-de-gournay-fact-sheet.research.md`** — Armstrong vol. 5 is a third independent witness to the Matthew + Rose de Burnham marriage.
- **`research/people/g31-walter-de-gournay-fact-sheet.research.md`** — vol. 8 Cranworth + Letton + Swathing King-John-era Gurney lordship paragraph corroborates the existing junior-branch-founding context.
- **`research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md`** — vol. 7 Bastwick / D'Aggs manor "granted to Hugh de Gourney by Henry I on the rebellion of lord Baynard" supplies a c. 1110-1115 Hugh-III grant attestation.
- **`research/places/harpley.md`** — extensive updates from vol. 5 (1297 fair, 1325 Uphall deed, 1332 nephew-grant, rector-stone two-shield observation, Sir John V 1400-01 release to Hugh Bavent). Reading correction for the "Folas" OCR.
- **`research/places/west-barsham.md`** — vol. 5 arms-list at the church (including probable Wentworth lead); 47 Edw. III (1373) precise transfer date; chancel monument Latin epitaph; 1641-1661 Calthorpe sale window.
- **`research/places/north-barsham.md`** — vol. 5 Wauncy's Manor at Southall corroboration (with the "Edw. II." vs "Edw. III." caveat) and **vol. 8 Great Ellingham reference to Anthony Gurney "of North Barsham" 1525 inheritance** (linking the North Barsham seat to G17 Anthony as well as the West Barsham seat).
- **`research/places/hingham.md`** (or create if missing) — vol. 4 Hingham Gurney's Manor 1572 lordship + 1715 Larwood successor.
- **`research/places/great-ellingham.md`** (or create if missing) — vol. 8 1525 Anthony Gurney inheritance via Margaret Lovell, the Conyers / Lovell / Spelman kinship chain, the post-1641 Margaret (Gurney) Davy descent → Mary → Sir Roger Potts → Francis Colman of Norwich. Also the rectory-mediety Warners → Gurnays → Davys → Potts chain.
- **`research/places/cranworth.md`** (or topic equivalent — create if missing) — vol. 8 King-John-era Gurney lordship; 1316 free-warren plea; 1257 + 1268 John de Gurney tenures with the Ravensholm mill detail.
- **`research/places/hardingham.md`** (or junior-branch sub-folder; create if missing) — vol. 8 undated Hugh de Gurney charter to Robert the Burgundian for the manor of Swathing in Hardingham; Saint-Hildevert at Gournay gift extended to Hardingham church; mill / fold-course tenure.
- **`research/topics/senior-gournay-baron-line-collateral.md`** — vol. 7 Bastwick c. 1110-1115 Henry-I grant on Baynard rebellion (Hugh III); vol. 7 Langley priory burial of Sir Hugh Gourney (collateral knight); vol. 4 Kimberley parallel-to-Bedingham Stuteville / Gunnora marriage; vol. 1 Cantley Uphall 1229 grant to Roger Botetourt; the "Bardolph holding of Gournay" attestations.
- **`research/topics/anderson-yvery-harpetre-gournay-collateral.md`** — vol. 4 Kimberley extension; vol. 7 Lessingham Bec donation (Gerard); vol. 1 Cantley/Caister general descent corroboration.
- **`research/places/gournay-en-bray.md`** and Saint-Hildevert place file — vol. 8 extends the Saint-Hildevert tithe-gift pattern to Hardingham church (a third Norfolk church alongside Caister and Cantley).
- **`research/places/norwich-cathedral.md`** (or topic equivalent — create if missing) — vol. 10 Gournay arms in cloister windows (1382-1430 glazing); vol. 10 Gournay's Place capital messuage at Norwich (alienated to Gawdy by 1338, then Paston, then Cooke).
- **`research/topics/london-gurney-comparators-1595-1670.md`** or a Sir-Richard-Gurney biographical note — vol. 10 Sir Richard Gurney lord-mayor biography (corroborating citation; collateral cadet).
- **Research leads (availability tag: Unknown online):**
  - The probable **Wentworth shield** at West Barsham church — does an attested Gurney-Wentworth marriage exist in the West Barsham line? Cross-check Visitation of Suffolk + History of Parliament for the Wentworths of Nettlestead.
  - The **Herward impaling Gourney** arms in a South Erpingham parish church (vol. 3) — does the project record a Gurney-Hereward / Gurney-Herward marriage?
  - The **Langley priory Sir Hugh Gourney burial** (vol. 7) — which Hugh, and where in the senior or collateral line?

No `data/sources.json` updates beyond the Armstrong source-entry addition above; no `fact-sheets/` direct changes in this patchset; no media-directory creation.

### 5. Repair stub state

The intake processed-folder stub state was stale on entry to this patchset (`stub-v67.md` still present, with v67 and v68 already promoted to live patchset files). Repair as part of Phase 2 lifecycle:

```bash
git rm sources/intake/processed/stub-v67.md
cat > sources/intake/processed/stub-v70.md <<'EOF'
Next patchset stub.

Rename this file to `v70-topic.patchset.md` when creating the next patchset, then immediately create `stub-v71.md`.
EOF
```

### 6. Finalize intake patchset lifecycle

This patchset file is being written directly at `sources/intake/processed/v69-armstrong-norfolk-1781-vol5-selected-gurney-references.patchset.md`. The filename retains the historical "vol5" suffix from the original single-volume scope; the patchset content now covers all ten volumes. No stub rename was needed because the stub was stale (see step 5).

## Phase 2 completion step

After Phase 2 application is complete, prepend a top-line `**Done:** YYYY-MM-DD HH:MM PT` stamp and move this patchset to `sources/intake/done/`:

```bash
python - <<'PY'
from pathlib import Path
src = Path("sources/intake/processed/v69-armstrong-norfolk-1781-vol5-selected-gurney-references.patchset.md")
dst = Path("sources/intake/done/v69-armstrong-norfolk-1781-vol5-selected-gurney-references.patchset.md")
body = src.read_text(encoding="utf-8")
dst.write_text("**Done:** 2026-05-28 HH:MM PT\n\n" + body, encoding="utf-8")
src.unlink()
PY
```

Replace `HH:MM` with the actual completion time.

## Validation checklist

- [ ] `data/sources.json` parses after update; `armstrong-norfolk-1781` entry exists with correct corpusPath and validationPath.
- [ ] `sources/corpus_supplement/armstrong-norfolk-1781-selected-gurney-references.md` exists with all 118 hits transcribed organized by volume.
- [ ] `sources/validations/armstrong-norfolk-1781.md` exists.
- [ ] `sources/intake/processed/stub-v67.md` removed; `stub-v70.md` created.
- [ ] No `fact-sheets/`, `research/people/`, `research/places/` files modified — those targeted updates are deferred to a follow-up patchset.
- [ ] `meta.lastUpdated` in `data/sources.json` advanced to 2026-05-28.
