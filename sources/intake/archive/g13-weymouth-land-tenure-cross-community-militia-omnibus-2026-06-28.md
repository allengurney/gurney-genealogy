# G13 John Gurney — Weymouth land, cross-community tenure, and militia omnibus

**Status:** Research-session handoff; not yet promoted into canonical research files.  
**Date:** 2026-06-28  
**Scope:** Lossless continuation of the G13 immigration-by-association investigation, focused on Weymouth land grants from 1636 to 1652, comparison with Hingham, John Gurney's later Braintree tenure, and the lower-probability militia hypothesis.

## Executive findings

1. **The current `c.1641–42` dating for John Gurney's first Weymouth parcels is too narrow.** No surviving entry dates the original grants. A defensible broad range is **c.1637–42**, with **c.1640–41 as the narrower best contextual estimate**. The parcels' small, scattered open-field form does not itself distinguish the earlier from the later end of that range.
2. **The 1641 gunpowder case is not a post-arrival terminus for the grants.** It proves John was associated with Weymouth by the General Court action, but the grants could predate it.
3. **A supposed second 1641/2 anchor disappears entirely.** The entry formerly read as a bill dated `3.16.42` actually records a monetary amount, **£3 16s 4d**, accepted with Thomas Lake's £1 3s 8d as £5 in the General Court session beginning 30 October 1644.
4. **The 1651/2 Weymouth great-lot entry was not a fresh grant to a newly favored resident.** The town was laying out lots “formerly granted” and recognizing older entitlements. Multiple men in John's cohort had already removed from Weymouth.
5. **John Read is the closest comparator yet found.** Read held Weymouth rights, operated a Tyng farm at Braintree under a ten-year agreement, received a Braintree grant, removed again, and still received an 18-acre Weymouth great lot in 1651/2.
6. **John Gurney's pattern is coherent mixed tenure, not an odd “sublet.”** He retained a Weymouth proprietary entitlement, owned a small Braintree homestead, and leased a much larger Tyng farm. The lease likely supplied a working farm without requiring the capital to purchase it.
7. **The 1651/2 entry proves continuing legal/proprietary recognition, not exceptional personal favor.** John's other Weymouth ties were real, but they are corroborating context rather than the necessary explanation for the grant.
8. **The militia hypothesis remains low-yield.** Adult men were ordinarily subject to training, and the powder case concerns readiness obligations, but no surviving record found in this pass names John as an officer, campaign soldier, or militia volunteer.
9. **Isaac's inferred c.1643 birth cannot locate the household.** The date and parentage are indirect reconstructions; no record establishes Weymouth or Braintree as his birthplace.
10. **Hingham remains a possible entry corridor but a weak specific hypothesis.** Its organized lot-making and proximity show how advance reception could work, but no Gurney variant or strong person-level overlap places John there.

## 1. Source ingestion and search

The downloaded full-text Nash source was incorporated during this session:

- Full OCR text: `sources/corpus/nash-historical-sketch-weymouth-1885.txt`
- PDF: `sources/media/nash-historical-sketch-weymouth-1885/nash-historical-sketch-weymouth-1885.pdf`
- Existing focused extract retained: `sources/corpus_supplement/nash-historical-sketch-weymouth-1885-gurney-extracts.md`
- Validation: `sources/validations/nash-historical-sketch-weymouth-1885.md`
- Source registry ID: `nash-historical-sketch-weymouth-1885`
- Internet Archive item: https://archive.org/details/historicalsketch00nash_0

The PDF copied byte-for-byte into its media destination, SHA-256:

`6DD24ACBA4797CE4205B1309B941099DB964A6FB4114842A2C121828D0F31643`

The original intake PDF remained locked by another Windows process after two removal attempts. It therefore still exists at `sources/intake/new/pdfs/historicalsketch00nash_0.pdf` and should be deleted after the external file handle is closed. The corpus text was moved successfully.

The full OCR was searched with the updated `repo_search.py infile` workflow using conservative and broad Gurney variants, followed by exact/non-fuzzy review to remove false positives. Genuine Gurney-family hits were:

- John Gurny/Gurnie on printed pp. 258, 270, 278, and 282;
- Zachariah Gurney in 1675;
- later Leander P. Gurney;
- Revolutionary-era David and Jonathan Gurney.

No additional colonial John Gurney occurrence emerged beyond the already known Weymouth land entries. The broad fuzzy pass produced many unrelated OCR similarities; the exact variant ledger is the reliable negative.

## 2. What kind of record is the “1643” Weymouth land book?

Nash expressly says the time of Weymouth's first land grant is unknown and that land was divided “from time to time, as the needs of the settlers appeared.” See full OCR at `sources/corpus/nash-historical-sketch-weymouth-1885.txt:1384-1390` and Internet Archive p. 31:

https://archive.org/details/historicalsketch00nash_0/page/31/mode/1up

The printed “owners of land about the year 1643” material is therefore not a single clean grant batch. It is a possession/title compilation containing:

- current holders;
- parcels “first granted” to earlier people;
- transferred parcels;
- entries accumulated after the conventional heading date.

It cannot have been finalized before William Fry's death on 26 October 1642, and at least one recited Dyer instrument is dated 21 May 1644. The safest label is therefore **a possession register begun or representing c.1643, with material through at least May 1644**.

This distinction matters. The book establishes that John had entered the title chain by its compilation, but it does not date the day the town first granted his parcels.

## 3. Reconstructing the Weymouth allocation systems

### 3.1 Small/open-field parcels existed before 1636

The East Field was already an active grant area by 1635. Zachary Bicknell's original East Field parcel was sold after his death by 9 March 1636/7. See:

- `sources/corpus/history-of-weymouth-1923-vol3.txt:3544-3554`
- `sources/corpus/nash-historical-sketch-weymouth-1885.txt:10700-10705`

John's known early package—two acres in the East Field, two more acres there, and four acres in the Mill Field—belongs to this ordinary scattered open-field system.

### 3.2 The 1636 Fresh Pond “great lots” were a distinct allocation

The 1636 list assigned six acres per “complete” person or householder and three acres per child under twelve. Sixteen named men received calculated family allotments:

- Edward Bennett
- Joseph Hull
- Henry Kingman
- Thomas Jenner Sr.
- Thomas White
- William Fry
- Robert Lovell
- Edmund Hart
- Thomas Rawling
- Thomas Jenner Jr.
- William Read
- Richard Sylvester
- Richard Adams
- William Smith
- Stephen French
- John Upham

See `sources/corpus/nash-historical-sketch-weymouth-1885.txt:10753-10784` and Internet Archive p. 280:

https://archive.org/details/historicalsketch00nash_0/page/280/mode/1up

John is absent. That weakens any claim that he received a **1636 great lot**, but it does not exclude residence after 1636 or a later small-field grant. Edmund Hart and Thomas Rawling, later abutters in John's title descriptions, were already in this 1636 cohort.

### 3.3 Small strips continued to be assigned and transferred

The c.1643/44 possession register contains many one- to eight-acre ordinary parcels. Comparable examples include:

- Walter Harris: eight acres in the Mill Field;
- Nicholas White: three acres plus two acres on the Plain;
- Thomas Rawling: three acres in the Mill Field;
- John Harding: six acres in the Mill Field;
- John Barnard: eight acres in the Mill Field;
- Matthew Pratt: a larger composite twenty-acre Mill Field holding.

The record contains roughly 176 “first granted” or equivalent chain-of-title clauses among about 138 holders. John's transferred and re-described parcels are normal for this record, not an exceptional pattern.

### 3.4 The 1651/2 great lots executed older rights

Nash's transcription begins:

> The great lots named in the old town Book and formerly granted to be laid out on the East side of Fresh Pond ...

See `sources/corpus/nash-historical-sketch-weymouth-1885.txt:10792-10811` and printed pp. 281–82:

- https://archive.org/details/historicalsketch00nash_0/page/281/mode/1up
- https://archive.org/details/historicalsketch00nash_0/page/282/mode/1up

The 2 February 1651/2 list contains 32 entries. On 3 February the town found another 27 men “entitled” to lots, requiring each claimant to bear his own measuring cost. John is number 16 in the supplemental list:

5. Nicholas Norton  
6. Samuel Newman  
7. Jeffrey Staple  
...  
15. John Staple  
16. **John Gurney**  
17. John Allin  
18. John Harding  
19. James Smith  
20. William Brandon

This wording and the absentee examples below show a deferred survey/recognition of old proprietary rights, not a batch of new homesteads for current residents.

### 3.5 The 1663 divisions are later and geographically different

The “First Division” and “Second Division” lists belong to 14 December 1663, not 1636. The first lay westward toward the Braintree line and contained numbered lots. These later divisions should not be back-projected onto John's early East Field and Mill Field strips.

## 4. Revised date range for John's first Weymouth grants

### Broad documentary/plausible range

**c.1637–42**, while allowing that the surviving title compilation contains entries through 1644.

Why not begin in 1636? John is absent from the distinct 1636 great-lot roll, and no current evidence places him in Weymouth that early. Why not begin only in 1641? The small-field system was active years earlier, and the town's surviving title record does not say his grants followed his first recorded court appearance.

### Narrower best estimate

**c.1640–41** is the best contextual estimate, with **c.1640–early 1642** a more conservative expression.

Reasons:

- Weymouth experienced a substantial new-settler influx around 1640.
- John is demonstrably associated with the town by the first surviving court matter.
- His small scattered parcels resemble ordinary settler accommodation rather than the 1636 household-scaled great-lot allocation.
- Nathaniel Adams's separate 1642–44 title/acquisition window supplies only a weak later boundary; it does not date John's original grants.

Recommended future wording:

> The grants could have been made at any point from about 1637 to 1642; their small, scattered open-field form does not date them. The best contextual estimate is about 1640–41, before or around John's first surviving Weymouth appearance. The later end rests mainly on the 1642–44 Adams title window rather than on a dated Gurney grant.

The canonical G13 companion's wording that John received the parcels “after arrival” around 1641–42 should be corrected later. The topic file's phrase “1642–44 East/Mill Field division” is likewise unsupported: no such single division has been established.

## 5. Why a Braintree resident still appeared in Weymouth in 1651/2

The answer is proprietary continuity. The town was executing previously recorded entitlements, and nonresidence did not extinguish them automatically.

### Direct absentee/nonresident comparators

**Samuel Newman**, number 6 in John's same supplemental cohort, had removed to Rehoboth in 1643/44 and remained there. See `sources/corpus/history-of-weymouth-1923-vol1.txt:4278-4289`.

**John Allin/Allen**, number 17 immediately after John, had land on the Plain and removed to Rehoboth in 1643. See `sources/corpus/history-of-weymouth-1923-vol3.txt:416-420`.

**Thomas Rider**, number 24 in the same list, removed to Boston yet was still “entitled to a lot” on 3 February 1651/2. See `sources/corpus/history-of-weymouth-1923-vol4.txt:8727-8735`.

**James Britton** had removed to Woburn in 1640 and was executed in 1643, but a lot still stood in his name in the 1651/2 process. See `sources/corpus/history-of-weymouth-1923-vol3.txt:6042-6052`.

**William Brandon** was dead by November 1647, yet a 1651/2 entitlement was still carried in his name. See `sources/corpus/history-of-weymouth-1923-vol3.txt:5894-5903`.

These are decisive against reading the list as a census of residents or a set of fresh personal favors.

### The strongest comparator: John Read

John Read:

- held earlier Weymouth land;
- agreed on 14 April 1639 to operate William Tyng's Mount Wollaston farm for ten years;
- moved to Braintree and received a 44-acre Braintree grant in 1640;
- later removed to Rehoboth;
- nevertheless received 18 acres east of Fresh Pond on 2 February 1651/2.

See `sources/corpus/history-of-weymouth-1923-vol4.txt:6920-6953`.

Read's path is nearly the same institutional pattern proposed for Gurney: **Weymouth proprietary right + Braintree Tyng tenancy + continued recognition of the Weymouth right despite residence elsewhere**.

## 6. John Gurney's Braintree tenure

### Not a “sublet”

The known instruments say the Tyng property was “in the Occupation and by lease in the hands of John Gurney.” The lease was a direct recognized interest under the Tyng estate and its coheirs, paired in the division instruments with Gregory Belcher's tenancy of the other Braintree farm.

Primary transcript:

`sources/corpus_supplement/suffolk-deeds-liber-iv-1888-gurney-extracts.md:23-73,82-149`

Calling this a sublet adds an unsupported intermediary relationship. **Tenant farmer or leaseholder of a Tyng farm** is the accurate description.

### Dual tenure

John also owned a separate Braintree house, orchard, five-acre parcel, and adjoining half-acre parcel, which he could sell in 1661/2. The best reconstruction is therefore:

- a small owned homestead/freehold;
- a much larger leased Tyng working farm;
- a residual Weymouth proprietary entitlement.

Leasing was rational, not anomalous. It supplied access to an established, capital-intensive farm while preserving flexibility and requiring less purchase capital. A tailor could combine a trade, a small owned homestead, and agricultural production on leased acreage.

### Tyng chronology and acreage conflict

The National Park Service cultural-landscape report says William Tyng leased John a **45-acre** section in 1647 for ten years; Tyng's 1653 inventory still called it land “in the possession of John Gurney”; and John continued under Tyng's daughters Bethia and Mercy after the nominal 1657 term.

https://npshistory.com/publications/adam/clr-1997.pdf

The repo currently says **48 acres** in several places. Before promotion, inspect the primary source behind the NPS citation, apparently NEHGR 30:432 or the probate inventory image, and reconcile 45 versus 48. Do not silently choose one number.

### What the 1651/2 right does and does not show

It shows:

- John had a legally recognized Weymouth proprietary entitlement after moving to Braintree;
- the town still admitted the title/right into its survey process;
- cross-town landholding and tenancy were ordinary enough to have a close parallel.

It does not alone show:

- that John was living in Weymouth in 1651/2;
- that the town bestowed a new favor because of unusually warm relations;
- that John occupied or improved the lot;
- that the entitlement was economically valuable after survey costs.

John's lot was later granted to others. The right may have been transferred, monetized, abandoned, or allowed to lapse.

## 7. Genuine continuing Weymouth ties

The entitlement needs no special social explanation, but other records show real continuing ties:

- John's 1663 estate still owed “Goodman King of Waymouth.”
- Son Richard established the lasting Weymouth branch.
- Peter Gurney mustered under Weymouth in 1675.
- A 1690 Weymouth abuttal still referred to “John Gurney['s] land.”
- The Porter–Ludden association begins in the powder-fine matter, and Ludden/Gurney land proximity persisted into the next generation.

These facts support a cross-community household network. They should be presented as independent continuity, not used to transform the 1651/2 entitlement into evidence of special favoritism.

## 8. Isaac Gurney and the transition

Isaac is not in the core child lists, no record names John as his father, and no birth record has been found. The c.1643 date is an age-fit reconstruction from his later court career, not a recorded birth.

Relevant files:

- `research/people/isaac-gurney-scituate-boston.md`
- `research/topics/john-gurney-candidate-others.md`
- `fact-sheets/g13-john-gurney-fact-sheet.md`

The uncommon name, lack of a competing colonial Isaac, age fit, and later Blue Hill/Ponkapoag geography make identification with this family probable, but not proven. His inferred birth falls neatly inside the Weymouth-to-Braintree transition, yet it cannot establish where the household was physically living in 1643.

## 9. Militia hypothesis

### What can be said

Massachusetts Bay required ordinary adult men to train and maintain arms and ammunition, subject to exemptions. Weymouth used training days as convenient public-notice and meeting days. The powder-fine case is consistent with that civic-militia system.

By 1641 the colony required town companies to train eight days yearly, military officers to inspect equipment, and arms surveyors to levy fines for deficiencies. Weymouth and Hingham had belonged to the same regiment, with Boston, Roxbury, and Dorchester, since December 1636. That created a regional institutional corridor, but not evidence of a special Gurney unit or personal service relationship.

Massachusetts Bay Colony Records, volume I:

- general arms requirements, pp. 84–85: https://archive.org/stream/recordsofgoverno01mass/recordsofgoverno01mass_djvu.txt
- regimental organization, pp. 186–87: same OCR, lines 12930–12959
- 1641 training, inspection, and powder provisions, pp. 327–32: same OCR, lines 22752–22810 and 23024–23025

John, Richard Porter, and James Ludden petitioned for remission of fines for not being supplied with powder. This shows:

- the town/court treated them as men subject to ammunition-readiness rules;
- John was embedded enough in Weymouth's civic administration to be fined and to petition with two neighbors;
- Porter and Ludden are useful social/proximity associates.

It does **not** prove prior English military service, colonial campaigning, officeholding, or recruitment through militia service.

The General Court's same 2 June 1641 session recognized the scarcity of money and allowed men deficient in powder to tender corn or other commodities for it. Richard Porter, an established 1635 settler, shared the petition. The grouped matter is therefore better read as a local inspection/supply problem than as a marker of newly arrived men who lacked equipment.

### The corrected 1644 bill

The official printed Massachusetts Bay Colony records for the session beginning 30 October 1644 read:

> John Gurny his byl for 3. 16. 4d & Tho: Lake his note for 1. 3. 8d are accepted for £5 fro Mr Ginner.

The arithmetic is exact:

- £3 16s 4d
- £1 3s 8d
- total £5

Official printed text, volume II, p. 79:

https://archive.org/stream/cu31924091024582/cu31924091024582_djvu.txt

The OCR/machine-transcript superscript pence marks were previously misread as final digits in `3.16.42` and `1.3.84`, leading to the false interpretation of a 16 March 1641/2 date. The entry is a **1644 financial acceptance**, and the nature of John's bill is unstated.

The immediately preceding order concerns purchase of powder and lead, but it is a separate order. Page proximity does not establish that John's bill was for military supplies.

### Mr. Ginner probably connects the bill back to Weymouth

The printed volume's index identifies the counterparty as **Ginner, Mr.** Weymouth records render Rev. Thomas Jenner as “Mr. Thom: Ginner (Jenner).” Jenner:

- came from Roxbury to minister at Weymouth in 1636;
- was a 1636 Weymouth great-lot grantee;
- served as Weymouth deputy in May 1640;
- left for Saco soon afterward.

See:

- `sources/corpus/history-of-weymouth-1923-vol1.txt:9855-9857`
- `sources/corpus/nash-historical-sketch-weymouth-1885.txt:6102-6119`

The likely reading is therefore that Gurny's £3 16s 4d bill and Lake's £1 3s 8d note were accepted as £5 from Thomas Jenner/Ginner. This is a plausible paper/credit connection between John and an earlier Weymouth minister and proprietor. The direction and underlying consideration of the debt remain unknown; it should not be called military evidence.

### Militia assessment

- Answerability to the ordinary Weymouth company/readiness system: **high probability, about 85–95%**
- Participation in a specific campaign: **not shown**
- Militia office: **not shown**
- Militia service as explanation for immigration, land, or Braintree movement: **low probability and unsupported**
- Financial/personal connection to Thomas Jenner via the 1644 bill: **plausible, worth targeted follow-up**

Weymouth furnished five unnamed men for the 1636–37 Pequot War, but their names are lost. John could have been one only if he was already present, which remains unproved; keep that possibility below roughly 10–15%. See `sources/corpus/history-of-weymouth-1923-vol1.txt:4818-4823,15792-15796`.

No service-linked land mechanism was found. The 1636 Weymouth division was household-scaled, not a soldier bounty. The Military/Artillery Company's 1,000-acre corporate grant was an exceptional institutional endowment for training expenses, and John Gurney is absent from its 1637–52 roll. The 1643 “John Gurnell” is the distinct Dorchester Gurnell surname already separated in `research/topics/john-gurney-candidate-others.md:7-11`.

Potential next checks:

1. Weymouth company officer/training lists and county militia returns before 1650.
2. Pequot War quota/payroll lists, recognizing that absence may reflect incomplete survival.
3. Original manuscript or higher-resolution image of the 1644 General Court entry.
4. Jenner/Ginner probate, account, and Saco records for John Gurny or Thomas Lake paper.

## 10. Hingham as an entry point

Prior work in this thread found:

- Hingham organized town lots in 1635, expanded in 1636, and received the large *Diligent* cohort in 1638.
- Matthew Cushing received lots before the *Diligent* arrived, proving that advance reception/allocation was possible.
- The 1638 cohort was concentrated around Hingham's central settlement.
- No Gurney variant appeared in the printed Hingham histories.
- No strong John-specific neighbor or associate overlap emerged.
- Weymouth's eastern land geography and Hingham's proximity make movement between the towns physically easy.

Sources:

- https://archive.org/details/historyoftownofh01hing
- https://archive.org/details/historyoftownofh02hing
- https://www.hingham-ma.gov/436/Historical-Timeline

Conclusion: Hingham is a geographically sensible but evidentially weak possible entry corridor. It should not displace the stronger Weymouth-centered reconstruction without a person-level record.

## 11. Integrated timeline

| Date | Best current reading |
|---|---|
| 1635 | East Field small-grant system already active. |
| 1636 | Fresh Pond household-scaled great-lot list; John absent. Thomas Jenner and several later Gurney abutters present. |
| c.1637–42 | Broad plausible range for John's first small East/Mill Field grants. |
| c.1640–41 | Narrower best contextual estimate for those grants. |
| 1640 | Jenner serves as deputy and leaves Weymouth soon afterward. |
| By first court matter | John associated with Weymouth; powder-fine petition concerns readiness, not campaign service. |
| c.1643 | Isaac probably born somewhere in Massachusetts, if the later Isaac is John's son; place unknown. |
| c.1643–May 1644+ | Weymouth possession/title compilation records John's parcels and later title material. |
| 30 Oct. 1644 | General Court accepts Gurny's £3 16s 4d bill plus Lake's £1 3s 8d note as £5 from Mr. Ginner, probably Thomas Jenner. |
| By 1645 | John established in Braintree. |
| 1647 | NPS reports start of ten-year Tyng lease; acreage needs 45/48 reconciliation. |
| 1651/2 | Weymouth lays out formerly granted great-lot entitlements; John appears among numerous absentees/nonresidents. |
| 1653 | Tyng inventory confirms John in possession of the leased farm. |
| 1657 onward | John apparently continues under Tyng's daughters after nominal lease term. |
| 1661/2 | John sells his distinct small Braintree freehold. |
| 1662/3 | John dies; later family and debt evidence preserves Weymouth ties. |

## 12. Corrections recommended for a later intake/apply phase

Do not apply these mechanically without reviewing the primary citations:

1. Replace `c.1641–42` for the first Weymouth grants with a broad `c.1637–42` range and a best estimate of `c.1640–41`.
2. Remove wording that the grants necessarily came “after” the first surviving court appearance.
3. Replace “1642–44 East/Mill Field division” with language recognizing an undated small-field grant system and a c.1643/44 possession compilation.
4. Describe the 1651/2 great lot as a carried entitlement “formerly granted,” not proof of renewed residence.
5. Use John Read as the primary cross-town comparator.
6. Replace “sublet” with direct Tyng leasehold/tenant-farm language.
7. Reconcile 45 versus 48 Tyng acres from the primary inventory/source.
8. Correct every repo interpretation of the bill as dated 16 March 1641/2. It is £3 16s 4d in an October 1644 entry.
9. Treat the bill's connection to Mr. Ginner/Jenner as plausible but not yet fully resolved.
10. Keep Isaac's c.1643 birth and parentage explicitly inferential; do not use them to assign a 1643 residence.

Likely canonical destinations after review:

- Main sustained argument: `research/people/g13-john-gurney-fact-sheet.research.md`
- Immigration/association interpretation: `research/topics/g13-john-gurney-immigration-by-association.md`
- Published concise correction, only after research promotion: `fact-sheets/g13-john-gurney-fact-sheet.md`
- Source-specific corrections: the existing military intake/patchset and related corpus-supplement interpretation

## 13. Source and artifact ledger

### Local sources

- `research/people/g13-john-gurney-fact-sheet.research.md`
- `research/topics/g13-john-gurney-immigration-by-association.md`
- `research/people/isaac-gurney-scituate-boston.md`
- `research/topics/john-gurney-candidate-others.md`
- `sources/corpus/nash-historical-sketch-weymouth-1885.txt`
- `sources/corpus_supplement/nash-historical-sketch-weymouth-1885-gurney-extracts.md`
- `sources/corpus/history-of-weymouth-1923-vol1.txt`
- `sources/corpus/history-of-weymouth-1923-vol3.txt`
- `sources/corpus/history-of-weymouth-1923-vol4.txt`
- `sources/corpus_supplement/suffolk-deeds-liber-iv-1888-gurney-extracts.md`
- `sources/corpus_supplement/bodge-soldiers-king-philips-war-1891-gurney-extracts.md`
- `sources/intake/archive/g13-immigration-association-thread-omnibus-2026-06-25.md`
- `sources/intake/archive/g13-gilman-diligent-immigration-by-association-discovery-2026-06-25.md`
- `sources/intake/done/colonial-followups-2026-06/fts-2026-06-13-military-bury-l95-l96.md`
- `sources/intake/done/v93-colonial-john-gurney-followups.patchset.md`

### External access points

- Nash, *Historical Sketch of Weymouth*: https://archive.org/details/historicalsketch00nash_0
- *History of Weymouth*, volume 1: https://archive.org/details/historyofweymout01cham
- *History of Hingham*, volume 1: https://archive.org/details/historyoftownofh01hing
- *History of Hingham*, volume 2: https://archive.org/details/historyoftownofh02hing
- Massachusetts Bay Colony Records, volume II: https://archive.org/details/cu31924091024582
- Volume II OCR with the 1644 Gurny entry: https://archive.org/stream/cu31924091024582/cu31924091024582_djvu.txt
- NPS Adams National Historic Site Cultural Landscape Report: https://npshistory.com/publications/adam/clr-1997.pdf
- FamilySearch image formerly used for the Gurny bill: https://www.familysearch.org/ark:/61903/3:1:3QHV-J3DW-8YB3
- FamilySearch petition-calendar images: https://www.familysearch.org/ark:/61903/3:1:3Q9M-C9Y5-F9M1-4 and https://www.familysearch.org/ark:/61903/3:1:3Q9M-C9Y5-F9M1-C

## 14. Remaining research delta

Highest-value next work:

1. Read the primary Tyng probate/inventory or NEHGR source to settle 45 versus 48 acres and confirm the 1647 lease date and terms.
2. Inspect the original Weymouth town-book images behind pp. 258–82, especially whether wording or layout distinguishes original grant, later possession, and transfer.
3. Trace Mr. Ginner/Jenner's 1644 financial paper and Thomas Lake's role.
4. Search original Suffolk land and probate instruments for disposition of John's 1651/2 entitlement.
5. Test whether other members of the 1651/2 supplemental cohort also had Braintree or Tyng ties.
6. Search surviving Weymouth militia-company records once, with a firm stop rule; do not treat ordinary powder liability as campaign service.
7. Preserve Hingham as a low-priority route hypothesis unless a person-level bridge appears.

### Evidentiary stop rules

- Do not infer a grant date from the conventional date of the possession book.
- Do not infer residence from an entitlement list that demonstrably includes absentees and deceased men.
- Do not infer military service from ammunition liability or from the 1644 bill.
- Do not infer Isaac's birthplace from an estimated birth year.
- Do not infer special Weymouth favor where ordinary property-law continuity is sufficient.
- Do not call the Tyng tenure a sublease without a document identifying an intermediate lessor.
