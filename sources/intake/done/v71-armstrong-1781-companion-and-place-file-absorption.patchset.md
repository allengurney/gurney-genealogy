**Done:** 2026-05-28 19:17 PT

# v71 patchset — Armstrong 1781 findings absorbed into research companions and place files

Prepared: 2026-05-28  
Phase: 1 preparation  
Scope: embed Armstrong 1781 findings (per v69) into the affected research companions (G19, G20, G21, G23, G29, G33) and place files (Harpley, West Barsham, North Barsham, Hingham, Great Ellingham, Hardingham, Norwich), so the new facts and corroborations live in the layer where research goes deeper than the published fact sheets.

Companion to v69 (source-tracking + corpus supplement) and v70 (fact-sheet absorption).

## Dependency on v69

This patchset assumes `armstrong-norfolk-1781` is in `data/sources.json` and the corpus supplement is at `sources/corpus_supplement/armstrong-norfolk-1781-selected-gurney-references.md`. Phase 2 application of v69 must run first.

## Findings absorbed in v71

Each target file receives an **appended new section** at the end (after any existing review-notes / generated-registry block), titled "Armstrong 1781 — [topic]". The append-at-end pattern is used because each existing file's prior structure is heterogeneous; new content as a clearly labeled trailing section preserves the existing prose while keeping the new material discoverable.

| Target | Content |
|---|---|
| `research/people/g19-william-gurney-iv-fact-sheet.research.md` | 1500 Thuxton advowson presentation; Cawston William Gurnay 1578 gravestone (for the Walter-of-Cley cadet branch). |
| `research/people/g20-thomas-gournay-ii-fact-sheet.research.md` | 1447-03-10 Berningham's attorney-delivery of seisin. |
| `research/people/g21-thomas-gournay-i-fact-sheet.research.md` | 1440-04-02 East Barsham Woolterton's confirmation (third dated East Barsham attestation alongside 1434-35 and 1445). |
| `research/people/g23-edmund-gurney-fact-sheet.research.md` | Sir John V + Alice attestations 1395-96 / 1398 / 1401 / 1401-02 at Heigham, Drayton, Hellesden, Taverham; Sir John Howard's silver-cup bequest to Sir John Gurney V; Saxthorpe c. 1411 attestation. |
| `research/people/g29-matthew-de-gournay-fact-sheet.research.md` | Armstrong as a third independent witness (alongside DG-I and Blomefield) to Matthew + Rose de Burnham. |
| `research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md` | Bastwick manor "granted to Hugh de Gourney by Henry I on the rebellion of lord Baynard" — c. 1110–1115 dated attestation for G33. |
| `research/places/harpley.md` | 1297 St James's Day fair grant; 1325 Uphall Manor deed with witness list; 1332 St Thomas the Apostle nephew-grant; Armstrong's 1781 observation that the rector's stone had its two shields and brass rim torn off; the "Folas" OCR-correction note pointing to the project's "Joh'is" reading. |
| `research/places/west-barsham.md` | Edward Gourney d. Aug 1641 chancel monument with Latin epitaph; eight-family impaled / quartered arms list (incl. probable Wentworth lead); 47 Edw. III (1373) Wauci → Gurney transfer date; 1641–1661 Calthorpe sale window. |
| `research/places/north-barsham.md` | Wauncy's Manor at Southall corroboration (with the "Edw. II." Armstrong-side dating-error flag); G17 Anthony's contemporaneous "of North Barsham" naming. |
| `research/places/hingham-norfolk.md` | Gurney's Manor 1572 lordship + post-1715 William Larwood of Norwich successor. |
| `research/places/great-ellingham.md` | 1525 Anthony Gurney inheritance via Margaret Lovell (Conyers / Lovell / Spelman kinship chain); post-1641 descent through Margaret Gurney → Henry Davy → Mary → Sir Roger Potts → Francis Colman of Norwich; rectory mediety Warners → Gurnays → Davys → Potts → Windhams. |
| `research/places/hardingham.md` | King-John-era Gurney lordship + 1316 free-warren plea by John de Gurney against William de Swathing + 1257 + 1268 John de Gurney tenures with Ravensholm mill detail; **undated Hugh de Gurney charter to Robert the Burgundian** for Swathing in Hardingham (20s. + horse, granted at "Ferretre" / La Ferté); **Saint-Hildevert-at-Gournay tithe-gift pattern extended to Hardingham church**. |
| `research/places/norwich.md` | Norwich Cathedral cloister Gournay arms (1382-1430 glazing); "Gournay's Place" capital messuage at Norwich (alienated to Gawdy by 1338, then Paston, then Cooke). |

## Phase 2 operations

Each operation appends a new trailing section. The anchor `old_string` is the file's current last meaningful line; the `new_string` repeats that line and adds the new section below it. If a target file has been further edited between this preparation and Phase 2 application, the operator should retarget to the new tail.

### 1. G19 William IV companion — Cawston 1578 gravestone + 1500 Thuxton advowson

File: `research/people/g19-william-gurney-iv-fact-sheet.research.md`.

```str_replace
old_string: [^v62-hop-drury]: L. M. Kirk, "DRURY, Sir Robert I (by 1456-1535), of Hawstead, Suff. and London," in S. T. Bindoff, ed., *The History of Parliament: The House of Commons 1509-1558* (London: Secker & Warburg, 1982). [historyofparliamentonline.org/volume/1509-1558/member/drury-sir-robert-i-1456-1535](https://www.historyofparliamentonline.org/volume/1509-1558/member/drury-sir-robert-i-1456-1535). Source ID: `hop-drury-robert-i-1456-1535`. Full text preserved at [`sources/corpus_supplement/hop-drury-robert-i-1456-1535.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/hop-drury-robert-i-1456-1535.md).
new_string: [^v62-hop-drury]: L. M. Kirk, "DRURY, Sir Robert I (by 1456-1535), of Hawstead, Suff. and London," in S. T. Bindoff, ed., *The History of Parliament: The House of Commons 1509-1558* (London: Secker & Warburg, 1982). [historyofparliamentonline.org/volume/1509-1558/member/drury-sir-robert-i-1456-1535](https://www.historyofparliamentonline.org/volume/1509-1558/member/drury-sir-robert-i-1456-1535). Source ID: `hop-drury-robert-i-1456-1535`. Full text preserved at [`sources/corpus_supplement/hop-drury-robert-i-1456-1535.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/hop-drury-robert-i-1456-1535.md).

---

## Armstrong 1781 — 1500 Thuxton advowson presentation and the Cawston cadet-branch monument

Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk* (1781), supplies two further data points for William Gurney IV (G19) and his cadet descendants.

**1500 Thuxton advowson presentation.** Armstrong vol. 8 (Mitford Hundred entry for Thuxton) records that "In 1381 Edmund Gurney presented to this church" — already covered for G23 — and that "In 1500 William Gurney presented to the church." The 1500 presenter is most parsimoniously G19 himself (d. 18 January 1508 per the Burnham Thorpe death attestation). This extends the documented advowson activity for G19 by one further parish.[^v71-armstrong-thuxton-1500]

**Cawston gravestone, William Gurnay d. 10 March 1578.** Armstrong vol. 3 (Cawston entry, North Erpingham Hundred) records: "A stone, having the effigies of a man and a woman, — For William Gurnay, gent. who died March 10, 1578; and Ann, his wife, January 19, 1595; they had one son and three daughters. — Gurnay impaling Waytes, of Norfolk." The arms in the windows include "Gurnay impaling Wayte" alongside the de la Pole and Boleyn families. This William Gurnay of Cawston is the Walter-of-Cley cadet-branch member already preserved on the Rye 1891 p. 132 Norfolk visitation captured in v67 — "William Gourney of Cawston in Norfolk = Ann, daughter to William Wayte of Tytleshall." Armstrong supplies the **exact death dates** (10 March 1578 for William; 19 January 1595 for Ann), the exact issue count (one son + three daughters), and an independent epigraphic confirmation of the marriage. The Walter-of-Cley cadet branch descended from G19's son Walter Gurney of Cley-by-the-Sea (granted lands 1495-96 by G19, per `fact-sheets/g19-william-gurney-iv-fact-sheet.md` n14).[^v71-armstrong-cawston-1578]

[^v71-armstrong-thuxton-1500]: Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 8 (Norwich, 1781), Mitford Hundred entry for Thuxton: "In 1381 Edmund Gurney presented to this church... In 1500 William Gurney presented to the church." Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_8`. Source ID: `armstrong-norfolk-1781`.

[^v71-armstrong-cawston-1578]: Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 3 (Norwich, 1781), North Erpingham Hundred entry for Cawston: Cawston church gravestone "For William Gurnay, gent. who died March 10, 1578; and Ann, his wife, January 19, 1595; they had one son and three daughters. — Gurnay impaling Waytes, of Norfolk"; arms in windows include "Gurnay impaling Wayte." Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_3`. Source ID: `armstrong-norfolk-1781`.
```

### 2. G20 Thomas II companion — 1447 Berningham's attorney role

File: `research/people/g20-thomas-gournay-ii-fact-sheet.research.md`.

The operator should locate the file's last meaningful line and append the section below. For brevity in this patchset, the section text is given here for direct append:

```markdown
---

## Armstrong 1781 — 1447 Berningham's attorney-delivery of seisin

Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 5 (Norwich, 1781), in the Gallow Hundred entry for East Barsham's Berningham's / Knold's / Waldgrave's Manor, records that on 10 March 25 Henry VI (1447) Robert Mompynson of Wisbich and Catherine his wife (widow of William Hunt of East Barsham) enfeoffed John Wode of Honingham, Margery his wife, and their son Robert in four messuages and four tofts at East Barsham and Snoring called Berningham's. "At the said time, a Thomas Gurney, esq. their attorney, to deliver seisin to John Wode and Margery, and to Robert, son of the said John and Margery."

Daniel Gurney's *Supplement* records that G21 Thomas Gournay I was probably dead before 1444; the 1447 attorney is therefore most parsimoniously G20 Thomas Gournay II, supplying a dated attestation that fills the gap between the 1445 Hunstanton seal (Daniel Gurney *Supplement* Note 126, p. 814) and the 1452 St George's Day Norwich petition to the Duke of Norfolk's deputy (already in the G20 fact-sheet narrative). The Berningham's transaction also confirms the persistence of the **Catherine, widow of William Hunt of East Barsham** through into a remarriage to Robert Mompynson of Wisbich — the same Catherine who released her right to John Wode in the 1440 Woolterton's confirmation Thomas Gournay also brokered (see G21 companion).[^v71-armstrong-1447-berninghams]

[^v71-armstrong-1447-berninghams]: Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 5 (Norwich, 1781), Gallow Hundred entry for East Barsham — Berningham's / Knold's / Waldgrave's Manor: "In the 25th of Henry VI. March 9, John Hines, of Swaffham in Norfolk, sells to John Wode the manor of Berningham for fifty marks; and on the 10th of the said month, Robert Mompynson, of Wisbich, and Catherine his wife, late wife of William Hunt, of East-Basham, enfeoffed John Wode, of Honingham, and Margery his wife, &c. in four messuages, four tofts, &c. called Berningham's, in this town, and Snoring... and, at the said time, a Thomas Gurney, esq. their attorney, to deliver seisin to John Wode and Margery, and to Robert, son of the said John and Margery." Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_5`. Source ID: `armstrong-norfolk-1781`.
```

Operator instruction: read the file, locate the current last paragraph, and append the section above (including the leading `---` separator). If the G20 companion file does not yet exist, create it with a one-line header `# Thomas Gournay II (G20) — Research Companion` plus the section above.

### 3. G21 Thomas I companion — 1440 East Barsham Woolterton's confirmation

File: `research/people/g21-thomas-gournay-i-fact-sheet.research.md`.

```str_replace
old_string: [^v61-blomefield-vol7-east-barsham-g21]: Francis Blomefield, *History of Norfolk*, vol. vii, "East-Barsham," pp. 53-65, [British History Online](https://www.british-history.ac.uk/topographical-hist-norfolk/vol7/pp53-65). Source ID: `blomefield-norfolk`. Full extract at [`sources/corpus_supplement/blomefield-norfolk-vol7-pp53-65-east-barsham.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/blomefield-norfolk-vol7-pp53-65-east-barsham.md).
new_string: [^v61-blomefield-vol7-east-barsham-g21]: Francis Blomefield, *History of Norfolk*, vol. vii, "East-Barsham," pp. 53-65, [British History Online](https://www.british-history.ac.uk/topographical-hist-norfolk/vol7/pp53-65). Source ID: `blomefield-norfolk`. Full extract at [`sources/corpus_supplement/blomefield-norfolk-vol7-pp53-65-east-barsham.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/blomefield-norfolk-vol7-pp53-65-east-barsham.md).

---

### 1440-04-02 East Barsham Woolterton's confirmation — fourth Norfolk attestation

Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 5 (Norwich, 1781), Gallow Hundred entry for East Barsham — Woolterton's Manor: "Thomas Gournay, esq. and John Hunt, son of William Hunt, of East Basham, confirmed to John Wode, of Briston, esq. and his heirs, &c. the manor of East Basham, formerly Roger de Woolterton's, and John de Bryston, of Bryston, esq. released to John Wode aforesaid, all his right in this manor, April 2, in the 18th of Henry VI. and Catherine, widow of William Hunt, released to him all her right."

The 2 April 1440 (18 Henry VI) confirmation is the **fourth** dated active-adult attestation for Thomas I, adding a year between the 1434-35 Blomefield East Barsham entry already in this companion and the 1441 retinue service under the 13th Earl of Oxford. The five-attestation span 1415 – 1418 – 1434-35 – **1440** – 1441 – 1445 (the post-1444 1445 Hunstanton seal probably belongs to Thomas II, per DG-Supp's "Thomas I probably dead before 1444"). The recurring counter-party in the 1440 and 1447 East Barsham conveyances is the Hunt family — William Hunt's widow Catherine and her later second husband Robert Mompynson of Wisbich.[^v71-armstrong-1440-woolterton]

[^v71-armstrong-1440-woolterton]: Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 5 (Norwich, 1781), Gallow Hundred, East Barsham — Woolterton's Manor (full text quoted above). Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_5`. Source ID: `armstrong-norfolk-1781`.
```

### 4. G23 Edmund companion — Sir John V Heigham/Drayton/Hellesden/Taverham cluster + Howard cup + Saxthorpe

File: `research/people/g23-edmund-gurney-fact-sheet.research.md`.

```str_replace
old_string: [^v63-husting-heylesdon-1384]: Reginald R. Sharpe, ed., *Calendar of Wills proved and enrolled in the Court of Husting, London, A.D. 1258-A.D. 1688*, Part II (London: J. C. Francis, 1890), pp. 241-243, Roll 113 (1). Internet Archive: [archive.org/stream/willshusting02sharuoft/willshusting02sharuoft_djvu.txt](https://archive.org/stream/willshusting02sharuoft/willshusting02sharuoft_djvu.txt). Source ID: `husting-wills-london-vol2-sharpe`.
new_string: [^v63-husting-heylesdon-1384]: Reginald R. Sharpe, ed., *Calendar of Wills proved and enrolled in the Court of Husting, London, A.D. 1258-A.D. 1688*, Part II (London: J. C. Francis, 1890), pp. 241-243, Roll 113 (1). Internet Archive: [archive.org/stream/willshusting02sharuoft/willshusting02sharuoft_djvu.txt](https://archive.org/stream/willshusting02sharuoft/willshusting02sharuoft_djvu.txt). Source ID: `husting-wills-london-vol2-sharpe`.

---

## Armstrong 1781 — Sir John V additional attestations (Heigham, Drayton, Hellesden, Taverham, Denver, Saxthorpe) + Sir John Howard's silver-cup bequest

Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk* (1781), substantially extends the documented economic footprint of Sir John Gurney V — the d. 1408 sheriff / MP / HoP-entered figure — outside the West Barsham / Harpley / North Barsham core.

### 1395-96 conveyance to John Winter

Armstrong vol. 9 (Freebridge entry for Heigham next Norwich): "John Gournay, and Alice his wife, were in possession of [the Hellesden mediety] in the 19th of Richard II [1395-96], when they passed it, with the manor of Drayton, and the advowson of the two chantries in this town, to John Winter, &c."

The same fine is recorded again at Drayton (vol. 9, Freebridge entry for Drayton): "But part of this lordship was alienated probably about the end of Edward III. by Sir John de la Pole, in the 19th of Richard II. John Gourney conveying it, with the advowson, to John Winter and his heirs, by fine."

And again at Taverham (vol. 9, Freebridge entry for Taverham): "In 1395, the advowson of one of these portions was settled by fine on John Winter, &c. by John Gournay and Alice his wife, with Drayton and Hellesden manors."

This is **John and Alice Gourney's coordinated 1395-96 alienation of the Norwich-adjacent Heigham / Hellesden / Drayton / Taverham cluster** — formerly the Hayleſdon family lands, now passing to John Winter (probably the same John Winter who was a major Norwich civic figure of the period). The named wife is Alice; the John Hayleſdon Husting will of 1384 (already in this companion) is the conveyance route by which these specific manors had come into Gurney hands. Armstrong's three-volume cross-attestation strongly supports the **Alice Heylesdon** identification over the Wansey-pedigree Alice Bavard variant.[^v71-armstrong-1395-heigham]

### 1398 + 1401 Heigham advowson presentations

Armstrong vol. 9 (continuation of the Heigham mediety entry): "yet in 1398, and 1401, John Gourney presented to this church as lord." Two further dated advowson presentations by Sir John V, between the 1395-96 conveyance to John Winter and the 1401-02 fee attestation below.[^v71-armstrong-1398-1401-heigham]

### 1401-02 Drayton + Taverham fee attestation

Armstrong vol. 9 (Drayton entry): "In the 3d of Henry IV. [1401-02] John Gournay held two fees here and in Drayton, sometime John Spring's, of the lord Morley, as part of the barony of Rye." Sir John V held two fees at Drayton + Taverham under the lord Morley as late as 1401-02 — six years before his 5 December 1408 death.[^v71-armstrong-1401-02-drayton]

### 1407-08 Denver lord-at-death

Armstrong vol. 1 (Loddon Hundred entry for Denver mediety): "In the 9th of Henry IV. John Gourney, esq. died lord, and of West Barsham." Independent corroboration of Sir John V's death year (9 Henry IV = 1407-08; DG-Supp Note 121 / HoP fix the date at 5 Dec 1408) and of his Denver tenure already in this companion's tenure table.[^v71-armstrong-1407-08-denver]

### Saxthorpe c. 1411 — post-IPM Gurney holding

Armstrong vol. 3 (North Erpingham Hundred entry for Saxthorpe): "[Saxthorpe manor descent:] ...In 1400 Henry, Alexander and Roger Groos held it, and about 1411 John Gurnay, of West Barsham; after this Sir John Fastolf, knight of the garter, was lord, and died seised of it." Sir John V died 5 Dec 1408. The c. 1411 actor is most parsimoniously **Edmund** (Sir John V's IPM-aged-10 son acting through guardians during minority) or the eventual nephew-successor **Thomas I** (G21). The 1411 attestation is distinct from the v62 Paston-Saxthorpe-1472 patchset's later Saxthorpe involvement.[^v71-armstrong-1411-saxthorpe]

### Sir John Howard's silver-cup bequest

Armstrong vol. 6 (South Erpingham Hundred entry for Walsingham priory area): Sir John Howard's will (late 14th / early 15th century — Howard's son John died on a journey to the Holy Land in 1410) leaves cups of plate to a named knightly circle: "to Sir William Beauchamp, and Sir John Marmion, knts. to each a silver cup with a cover, to be made new, weighing 10lb. in gross; to Sir Stephen Hales, John de Burgh, Richard de Sutton, knts. and [Sir John] Gurney, to each of them a new cup to be made of silver, with a cover, each of the weight of 10 marks in gross." This places **Sir John Gurney V in Sir John Howard's intimate gift circle** alongside Hales, Burgh, and Sutton — the same Howard / Plays / Heydon political network the project already documents at G18 / G19 / G20.[^v71-armstrong-howard-cup]

### 1373 Wauci → Edmund Gurney West Barsham transfer date

Armstrong vol. 5 (Gallow Hundred entry for West Barsham): "Hugo de Wauci held this manor of the Earl Warren, and it remained with his descendants till the **47th of Edw. III** [1373], when it came to Edmund Gurney by marriage." Sharpens the project's existing "after 1372" reading for the Wauncy → G23 West Barsham inheritance by one year.[^v71-armstrong-1373-west-barsham]

[^v71-armstrong-1395-heigham]: Mostyn John Armstrong, *History and Antiquities of the County of Norfolk*, vol. 9 (Norwich, 1781), Freebridge Hundred — Heigham next Norwich, Drayton, and Taverham parish entries. Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_9`. Source ID: `armstrong-norfolk-1781`.

[^v71-armstrong-1398-1401-heigham]: Armstrong, *Norfolk*, vol. 9, Heigham next Norwich. Source ID: `armstrong-norfolk-1781`.

[^v71-armstrong-1401-02-drayton]: Armstrong, *Norfolk*, vol. 9, Drayton. Source ID: `armstrong-norfolk-1781`.

[^v71-armstrong-1407-08-denver]: Armstrong, *Norfolk*, vol. 1, Loddon Hundred — Denver mediety. Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_1`. Source ID: `armstrong-norfolk-1781`.

[^v71-armstrong-1411-saxthorpe]: Armstrong, *Norfolk*, vol. 3, North Erpingham — Saxthorpe. Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_3`. Source ID: `armstrong-norfolk-1781`.

[^v71-armstrong-howard-cup]: Armstrong, *Norfolk*, vol. 6 (Norwich, 1781), South Erpingham Hundred — Walsingham priory area, Sir John Howard's will extract. Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_6`. Source ID: `armstrong-norfolk-1781`.

[^v71-armstrong-1373-west-barsham]: Armstrong, *Norfolk*, vol. 5, Gallow — West Barsham parish entry. Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_5`. Source ID: `armstrong-norfolk-1781`.
```

### 5. G29 Matthew companion — Armstrong as third witness to Matthew + Rose de Burnham

File: `research/people/g29-matthew-de-gournay-fact-sheet.research.md`.

Append the section below at end of file:

```markdown
---

## Armstrong 1781 — third independent witness

Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 5 (Norwich, 1781), Gallow Hundred entry for West Barsham, opens its Harpley-rooted Gurney pedigree skeleton with "Matthew de Gourney lived in the reign of Henry II. and married Rose, daughter and heir of Reginald de Burnham." This is Armstrong's eighteenth-century printed witness to the Matthew + Rose de Burnham marriage already independently attested by Daniel Gurney *Record* (1848) pedigree p. 286 and Blomefield's Harpley entry. Useful as a third corroborating citation; no new fact.[^v71-armstrong-matthew-rose]

[^v71-armstrong-matthew-rose]: Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 5 (Norwich, 1781), Gallow Hundred, West Barsham pedigree-skeleton paragraph. Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_5`. Source ID: `armstrong-norfolk-1781`.
```

### 6. G33 Hugh III companion — Bastwick Henry I grant on Baynard rebellion

File: `research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md`.

Append the section below at end of file:

```markdown
---

## Armstrong 1781 — Bastwick manor granted by Henry I on the Baynard rebellion

Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 7 (Norwich, 1781), Tunstead Hundred entry for the Bastwick / D'Aggs manor, records that the lordship "was granted to Hugh de Gourney by Henry I. on the rebellion of lord Baynard, and by Julian, daughter and heiress of that family, came to William lord Bardolph; her husband. Thomas de Ages, or D'aggs, was lord in the 3d of Edward III. held of Thomas lord Bardolph."

The William Baynard rebellion is the 1110 episode in which Baynard's English honour was forfeited to the Crown for treason and redistributed. The Henry I grant to "Hugh de Gourney" is therefore datable to c. 1110-1115. The recipient is most parsimoniously **G33 Hugh III** (b. c. 1075, fl. c. 1100-1135) — placing him in the Henry I tenant-in-chief grant circle in the years immediately after his minority court-fosterage (per the existing G33 companion's "raised at the king's court during minority" entry). The eventual transmission to William Bardolph via Julian de Gournay matches the existing Bardolph-as-Gournay-heir descent already in `research/topics/senior-gournay-baron-line-collateral.md`.[^v71-armstrong-bastwick]

[^v71-armstrong-bastwick]: Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 7 (Norwich, 1781), Tunstead Hundred — Bastwick / D'Aggs entry. Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_7`. Source ID: `armstrong-norfolk-1781`.
```

### 7. Harpley place file — 1297 fair, 1325 Uphall deed, 1332 nephew-grant, rector stone observation

File: `research/places/harpley.md`.

The file's current end is the `<!-- GENERATED:PLACE-REGISTRY:END -->` marker block. Append below it.

```str_replace
old_string: ### Review notes

- None in cleanup pass 3b.

<!-- GENERATED:PLACE-REGISTRY:END -->
new_string: ### Review notes

- None in cleanup pass 3b.

<!-- GENERATED:PLACE-REGISTRY:END -->

## Armstrong 1781 — Uphall Manor 1325 deed, 1332 nephew-grant, 1297 St James's Day fair, and the rector's stone in 1781

Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 5 (Norwich, 1781), Freebridge Hundred and Half entry for Harpley, supplies four specific Gurney-era details for the parish that complement the medieval-descent narrative already on this file.

**1297 (25 Edw. I) royal grant of an annual fair on St James's Day.** Armstrong records that the Harpley fair was "granted in the 25th of Edward I. to John de Gourney, lord, patron and rector of the town; and it belongs to the rector for the time being." The fair was held on 25 July — the feast of St James the Apostle (matching the parish church's St Lawrence dedication via the medieval Norfolk pilgrim-route economy). This is the earliest specific royal grant of an economic right at Harpley to a Gurney rector-patron.

**1325-11-26 Uphall Manor deed (verbatim witness list).** Armstrong reproduces a deed dated at Harpley on 26 November 18 Edward II (1325): "Walter son of Robert de Meleford, grants to his lord, sir John de Gourney, rector of the church of Harpley, his messuage called Uphall, with all the homages, and services of his free tenants, view of frank-pledge, free bull and boar, all perquisites of court, and all other liberties late Ralph's, son of Walter de Manors, with wards, reliefs, escheats, &c. with all the lands that Mariona, late wife of the said Walter, holds for life... the said John de Gourney paying one clove per ann."

The named witnesses are: Sir Henry de Walpole; Thomas de Feltham; Edmund Laurence; Oliver de Massingham; Ralph de Walsingham; William de Harplee. These are the working witnesses of the rector John's economic acquisitions in the late 1320s — a working Walpole / Feltham / Massingham / Walsingham / Harplee circle.

**1332-12-21 nephew-grant to John III + Jane.** Armstrong continues: "And the said manor, tenements, &c. were by deed of the said John de Gourney, dated on Monday the feast of St. Thomas the Apostle, in the 6th year of king Edward III. granted to his nephew, John de Gourney, and Jane his wife, and their heirs." This is the conveyance that transfers Uphall (with the rest of the Harpley estate) into the lay nephew's line — the same nephew-heir already preserved on this file as G25 John de Gournay III. The date (Monday, 21 December 1332) is the same year the rector died (6 Edw. III), so the grant was either a pre-death transfer or a deathbed arrangement.

**1297 + 1325 + 1332 dated chain.** The three Armstrong dates compress the Gurney-rector's economic-rights consolidation at Harpley into a 35-year window: 1297 fair grant; 1325 Uphall acquisition with full lord-tenant rights; 1332 transfer to the nephew.

**1781 observation on the rector's chancel stone.** Armstrong's eye-on-the-stone record from 1781 adds physical-monument detail to the rector John's chancel-floor grave-stone already noted on this file. Armstrong: "On the pavement of the chancel lies an old marble grave-stone, whereon was the portraiture or effigies of a priest, with **two shields and a rim of brass, now torn off**: by the incision of the stone made to let the letters in on the rim, it appears to be — 'Hic Jacet corpus Folas de Gournay, quonda' rectoris et patroni hujus ecclesie. cuj; a[ni]e p[ro]pitietur Deus, Amen.' — He died rector in the 6th of Edward III." The "Folas" reading is an Armstrong-side OCR or transcription error for the project's accepted "Joh'is" (Johannis = John) reading already preserved on this file; the substance — rector John, d. 6 Edw. III = 1332 — matches. The new observation is the **two shields and brass rim** that were already torn from the stone by 1781 (presumably during the Edwardian iconoclasm of the 1540s or the Civil War period).[^v71-armstrong-harpley]

[^v71-armstrong-harpley]: Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 5 (Norwich, 1781), Freebridge Hundred and Half — Harpley (Gourney's Manor, Uphall Manor, the church windows, the chancel grave-stone). Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_5`. Source ID: `armstrong-norfolk-1781`.
```

### 8. West Barsham place file — chancel monument, arms list, 1373 transfer, 1641–1661 sale window

File: `research/places/west-barsham.md`.

```str_replace
old_string: ### Review notes

- None in cleanup pass 3b.

<!-- GENERATED:PLACE-REGISTRY:END -->
new_string: ### Review notes

- None in cleanup pass 3b.

<!-- GENERATED:PLACE-REGISTRY:END -->

## Armstrong 1781 — West Barsham church arms, chancel monument, 1373 Wauci → Gurney transfer, 1641–1661 sale window

Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 5 (Norwich, 1781), Gallow Hundred entry for West Barsham, supplies four specific findings for the parish.

**1373 Wauci → Edmund Gurney transfer.** Armstrong: "Hugo de Wauci held this manor of the Earl Warren, and it remained with his descendants till the 47th of Edw. III, when it came to Edmund Gurney by marriage." The 47th of Edward III is 1373; the project's G23 Edmund Gurney fact-sheet establishes the marriage settlement of 100 marks p.a. by Catherine Wauncy's father in 1357 and the death of Sir Edmund de Wauncy (Catherine's brother) in 1372. Armstrong's 1373 transfer date is the seisin-conveyance date one year after Sir Edmund's death — sharpening the project's "after 1372" reading.

**Eight-family impaled / quartered arms list at West Barsham church.** Armstrong: "The arms of Gurney were argent, a cross ingrailed, gules, and impaled the arms of Wauci, gules, three dexter hands erect, argent; also Calthorpe, Lovell, Holdich, Blennerhasset and Lewknor; also they impaled Jernegan, and sable, a chevron between three leopards heads, &c. probably Wentworth." The eight families correspond to:

- **Wauci** — Catherine de Wauncy (wife of G23 Edmund Gourney).
- **Calthorpe** — Anne Calthorpe (wife of G19 William Gurney IV; mother of G18 William V).
- **Lovell** — Margaret Lovell (wife of G17 Anthony Gurney; brought Great Ellingham via the Lovell / Mortimer / Conyers / Spelman chain in 1525).
- **Holdich** — Ellen Holdich of Ranworth (wife of G16 Francis Gurney).
- **Blennerhasset** — Ellen Blennerhasset of Barsham (wife of G15 Henry Gurney).
- **Lewknor** — Martha Lewknor of Denham (wife of Thomas Gurney III, G15's eldest son; mother of Edward Gourney d. 1641).
- **Jernegan / Jerningham** — Margaret Jerningham of Somerleyton (wife of G20 Thomas II; the family was re-married to a generation later via Helen Holditch's c. 1560s second marriage).
- **Wentworth (probable)** — "sable, a chevron between three leopards' heads." **No currently recorded Gurney-Wentworth marriage in the West Barsham line.** Open lead.

The eight-family display gives an independent visual record of the family alliances preserved at the West Barsham church through to Armstrong's 1781 visit. Seven match already-known marriages; the eighth is a research lead carried forward to v72.

**Edward Gourney chancel monument, d. August 1641.** Armstrong reproduces the brass-plate Latin epitaph: "Caducum hoc aeternat Marmor Edwardus Gourney, filius et heres Tho. Gourney Armig. et Marthe filie Edu. Lewkenor de Denham, in Com. Suff, Militis, obiit Aug. 1641." Translation: *"This marble eternalises the perishable Edward Gourney, son and heir of Thomas Gourney Esq. and of Martha daughter of Edward Lewkenor of Denham in the county of Suffolk, Knight; died August 1641."*

Edward is the project's G15 Henry's grandson, the West Barsham heir who succeeded Henry G15 around 1615/16. His Aug 1641 death has not previously been in the project — the G15 Henry fact-sheet records his birth as 1608 and the eventual extinction of the line in 1661 in his son Henry II, but no date for Edward's own death. Armstrong supplies it.

**1641–1661 Calthorpe sale window.** Armstrong: "Edmund died seised of it in the year 1641, and his son Henry sold it to the family of Calthorpe." Armstrong's "Edmund" is an editorial slip for "Edward" (the chancel monument names Edward). Edward's son Henry II therefore held West Barsham from 1641 to 1661 (the line's extinction); the Calthorpe purchase falls within that window. Post-Gurney descent: Calthorpes → Dr. Charles Morley MD (lord 1720) → Charles Morley jr. of Basham → John Balders, esq.[^v71-armstrong-west-barsham]

[^v71-armstrong-west-barsham]: Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 5 (Norwich, 1781), Gallow Hundred — West Barsham parish entry. Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_5`. Source ID: `armstrong-norfolk-1781`.
```

### 9. North Barsham place file — Wauncy's Manor at Southall + G17 "of North Barsham"

File: `research/places/north-barsham.md`.

```str_replace
old_string: [^blomefield-north-barsham]: Francis Blomefield, ["Gallow and Brothercross Hundreds: North-Barsham,"](https://www.british-history.ac.uk/topographical-hist-norfolk/vol7/pp47-52) in *An Essay Towards A Topographical History of the County of Norfolk*, vol. 7 (London, 1807), pp. 47-52, British History Online. Source ID: `blomefield-norfolk`.
new_string: [^blomefield-north-barsham]: Francis Blomefield, ["Gallow and Brothercross Hundreds: North-Barsham,"](https://www.british-history.ac.uk/topographical-hist-norfolk/vol7/pp47-52) in *An Essay Towards A Topographical History of the County of Norfolk*, vol. 7 (London, 1807), pp. 47-52, British History Online. Source ID: `blomefield-norfolk`.

## Armstrong 1781 — Wauncy's Manor at Southall + G17 Anthony "of North Barsham"

Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 5 (Norwich, 1781), Gallow Hundred entry for North Barsham, records that "Wauncy's Manor, or Southall. Hugh, who was lord of West-Basham, was ancestor of the family of de Wauci, and held this lordship at the survey of the Earl Warren. The family of Suthale, or Southwell, had some interest herein under the Wauci. In the reign of Edw. II. it came to Edmund Gurney, by the marriage of Catherine, daughter of Sir William Wauch, and remained in that family."

The substance corroborates Blomefield's North Barsham entry (already on this file): the Wauncy → Edmund Gurney parallel inheritance at North Barsham accompanied the larger West Barsham acquisition. The Armstrong **dating "reign of Edw. II."** is editorial error — same volume gives "47 Edw. III" (1373) at West Barsham for the same Wauncy → Gurney transfer, agreeing with Blomefield and with the established G23 Edmund chronology. Do not adopt the "Edw. II." reading; the corpus extract preserves it as a documented Armstrong-side slip.

**G17 Anthony Gurney "of North Barsham."** Armstrong vol. 8 (Shropham Hundred entry for Great Ellingham) names the 1525 Great Ellingham inheritor as "Anthony Gurney, esq. of North Barsham, in right of Margaret his wife." The "of North Barsham" naming — alongside the more commonly published "of West Barsham" — indicates that by Anthony's lifetime (1499 – 4 Jan 1555/6) the North Barsham seat had become a working alternative residence. North Barsham is therefore not merely a tenurial appendage of the West Barsham estate; it carries enough working-residence weight to be the parish identifier in the Great Ellingham descent paragraph.[^v71-armstrong-north-barsham]

[^v71-armstrong-north-barsham]: Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 5 (Norwich, 1781), Gallow Hundred — North Barsham (Wauncy's Manor at Southall); and vol. 8, Shropham Hundred — Great Ellingham parish entry (G17 Anthony's "of North Barsham" naming at the 1525 inheritance). Internet Archive items `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_5` and `..._1781_8`. Source ID: `armstrong-norfolk-1781`.
```

### 10. Hingham place file — 1572 lordship + 1715 Larwood successor

File: `research/places/hingham-norfolk.md`.

```str_replace
old_string: ### Review notes

- None in cleanup pass 3b.

<!-- GENERATED:PLACE-REGISTRY:END -->
new_string: ### Review notes

- None in cleanup pass 3b.

<!-- GENERATED:PLACE-REGISTRY:END -->

## Armstrong 1781 — Gurney's Manor 1572 lordship + post-1715 William Larwood successor

Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 4 (Norwich, 1781), Forehoe Hundred entry for Hingham, records that "Gurney's Manor was part of the great manor, granted to a younger branch of the family before the forfeiture; it continued always in the family of that name, residing at Barsham and Great Ellingham, in this county; **Henry Gurney was lord in 1572**; how it passed afterwards we do not find; but in 1715 it was owned by Mr. Larwood, of Norwich, merchant."

Three points to record:

- The "younger branch ... before the forfeiture" reading aligns with project standing-fact #2 — the junior Norfolk branch through G31 Walter de Gournay, sub-enfeoffed before Hugh V's 1205 forfeiture.
- "Henry Gurney was lord in 1572" corroborates Blomefield's *History of Norfolk* vol. ii (1805), Forehoe entry for Hingham (already cited at G15 Henry's fact-sheet n3). G15 Henry held Hingham-Gurneys among his Norfolk tenures.
- The **post-Gurney successor at Hingham — Mr. William Larwood of Norwich, merchant, by 1715** — is new. Armstrong notes only the surname Larwood; the merchant's full identification, the date of his acquisition, and the chain by which Hingham left the Gurneys c. 1641–1715 would require further work in the Larwood family records or in 17th-century Norfolk court rolls. Worth a research lead.[^v71-armstrong-hingham]

[^v71-armstrong-hingham]: Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 4 (Norwich, 1781), Forehoe Hundred — Hingham parish entry, Gurney's Manor section. Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_4`. Source ID: `armstrong-norfolk-1781`.
```

### 11. Great Ellingham place file — 1525 Lovell-via-Margaret inheritance + post-1641 Davy descent + rectory mediety chain

File: `research/places/great-ellingham.md`.

```str_replace
old_string: [^historic-england-old-hall-1077566]: Historic England, ["Old Hall Farmhouse,"](https://historicengland.org.uk/listing/the-list/list-entry/1077566) *National Heritage List for England*, List Entry Number 1077566. Source ID: `historic-england-old-hall-farmhouse-1077566`.
new_string: [^historic-england-old-hall-1077566]: Historic England, ["Old Hall Farmhouse,"](https://historicengland.org.uk/listing/the-list/list-entry/1077566) *National Heritage List for England*, List Entry Number 1077566. Source ID: `historic-england-old-hall-farmhouse-1077566`.

## Armstrong 1781 — Great Ellingham 1525 inheritance + Conyers / Lovell / Spelman kinship + post-1641 Margaret Gurney → Henry Davy descent

Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 8 (Norwich, 1781), Shropham Hundred entry for Great Ellingham capital manor, supplies the most complete printed pre-Blomefield account of the manor's transit through the Gurney family.

**1525 inheritance via Margaret Lovell.** After Henry Spelman the elder of Mickle Ellingham died without issue in 1525, the capital manor "went to Anthony Gurney, esq. of North Barsham, in right of Margaret his wife, one of the daughters and co-heiresses of Sir Robert Lovell, by Ela Conyers his wife, who was sister to Ann Conyers, mother to Henry Spelman." The kinship chain is:

- **Ela Conyers** + Sir Robert Lovell → Margaret Lovell (m. G17 Anthony Gurney 1519).
- **Ann Conyers** (Ela's sister) + Thomas Spelman → Henry Spelman the elder of Mickle Ellingham (d. 1525, s.p.).

The two cousins — Margaret Lovell and Henry Spelman — were first cousins by Conyers; the Spelman lordship of Great Ellingham therefore passed to the surviving Conyers-blood line on Spelman's death s.p. This explanatory layer is in Armstrong but not in the present G17 fact-sheet narrative.

**Post-1641 descent to Margaret Gurney → Henry Davy.** Armstrong continues: "After 1641 it went to **Margaret Gurney, his aunt**, who married Mr. Henry Davy, of Great Ellingham, whose sole daughter and heiress, Mary, married Sir Roger Potts, bart. of Great Ellingham and Mannington, who sold it to Mr. Francis Colman, of Norwich, the present lord."

The "1641" trigger is Edward Gourney's August 1641 death (West Barsham chancel monument, see `research/places/west-barsham.md`). Edward's son Henry II inherited West Barsham (the senior seat); Great Ellingham, however, was diverted to **Margaret Gurney** — Edward's paternal aunt, daughter of G15 Henry Gurney, already named in the G15 fact-sheet child-table — who had married Henry Davy of Great Ellingham. Margaret's daughter Mary Davy married Sir Roger Potts, bart.; the Potts family sold the manor to Francis Colman of Norwich by Armstrong's 1781 visit.

**The Great Ellingham rectory mediety follows the same chain.** Armstrong (vol. 8 continuation, p. ~261): "After the division of the Mortimer's estate this advowson was allotted to John Fitz-Ralph, as part of the inheritance of Margery Mortimer, his wife; and from that time it passed with the manor of Ellingham-hall, from Fitz-Ralph to Conyers, from them to the **Warners, so to the Gurnays, and Davys**, and after to the Potts, who sold it to Mrs. Windham." The "Warners → Gurnays" linkage is new — the Gurneys received the rectory mediety from a Warner predecessor (whose precise relationship to the Conyers line would require further checking), then onward Davys → Potts → Windhams.

**Berryhall divergence in 1525.** Armstrong notes that at the 1525 division, "Berryhall went to the heirs of William De-Grey, of Merton, in right of Christian his wife, the daughter and co-heiress of Thomas Manning" — the Berryhall manor in Great Ellingham did not come to Anthony Gurney but went to the De-Grey of Merton line via a different Manning co-heiress, ending in 1474 with William De-Grey's death.[^v71-armstrong-great-ellingham]

[^v71-armstrong-great-ellingham]: Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 8 (Norwich, 1781), Shropham Hundred — Great Ellingham capital manor + rectory mediety entries. Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_8`. Source ID: `armstrong-norfolk-1781`.
```

### 12. Hardingham place file — King-John Gurney lordship + 1257/1268 + 1316 + Hugh charter + Saint-Hildevert extension

File: `research/places/hardingham.md`.

```str_replace
old_string: ### Review notes

- None in cleanup pass 3b.

<!-- GENERATED:PLACE-REGISTRY:END -->
new_string: ### Review notes

- None in cleanup pass 3b.

<!-- GENERATED:PLACE-REGISTRY:END -->

## Armstrong 1781 — King-John-era Gurney lordship + dated late-13th-century tenures + Hugh's undated charter + Saint-Hildevert at Hardingham church

Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 8 (Norwich, 1781), Mitford Hundred entry for the Hardingham / Swathing / Reymerston cluster, substantially extends the early Gurney lordship narrative for the junior-branch home parish.

**King-John-era Gurney lordship at Cranworth, Letton, and Swathing.** Armstrong: "The ancient family of de Gurney were [lords] of this town [Cranworth], Cranworth, and Letton, in the [reign] of king John." Aligns with project standing-fact #2 — the junior Norfolk branch through G31 Walter de Gournay, sub-enfeoffed before Hugh V's 1205 forfeiture.

**1316 (9 Edw. II) free-warren plea.** Armstrong: "John de Gurney in the 9th of Edward II. impleaded William de Swathing for chacing his hares without his licence, in his free-warren of Swathing." Dated 1316 enforcement of the John de Gurney free-warren right at Swathing — a working-lord attestation distinct from the bare tenurial record.

**1257 + 1268 John de Gurney tenures at Hardingham + Reymerston (with Ravensholm mill rights).** Armstrong: "In the 41st of Henry III. [1257] Ralph Redker conveyed lands to William de Swathing, and in the 52d of that king [1268], William de Swathing held of John de Gurney a messuage, fifty-four acres of land, and three of wood, in this town and Reymerston, with free grinding, without toll, at John's-mill, called Ravensholm, as he and his ancestors before had at Little-mill, whilst Little-mill was repairing... John likewise granted to William, and his heirs, a free bull, and ram, with a free fold-course, and common of pasture over all his lands for all his cattle (tempore aperto) in time of shack, as his ancestors had." Two dated tenures, with named mill (Ravensholm), free bull + ram, and fold-course rights.

**Undated Hugh de Gurney charter to Robert the Burgundian — granted at "Ferretre" in Normandy.** Armstrong: "Hugh de Gurney granted, by deed without date, to Robert, the Burgundian, the manor of Swathing, in Hardingham, with the manor and appurtenances in fee, for 20s. sterling per ann. and for the gift of one horse at the time of making this grant. It was granted at Ferretre, a town probably in Normandy, the Gurneys being [originally] of Gourney, a town in Normandy, from which they took their name, and came into England on the Norman invasion."

The grantor "Hugh de Gurney" is most parsimoniously **Hugh V de Gournay** (the senior-line baron forfeited 1205) — sub-infeudating the junior-branch Hardingham/Swathing manor to a Burgundian retainer in Normandy. The grant location "Ferretre" reads most plausibly as **La Ferté** (in Normandy, just south of Gournay-en-Bray), the same la-Ferté collateral branch identified in the project's senior-line topic file (Sigy priory founder Hugh I de la Ferté + son Hugh II monk at St Ouen Rouen). The undated charter is therefore plausibly late-12th / very-early-13th century — before the 1205 forfeiture broke the Norman / English baronial unity.

**Saint-Hildevert-at-Gournay tithe-gift extended to Hardingham church.** Armstrong: "And this Hugh gave to the chapter of the church of St. Ildebert, of Gourney, in Normandy, the said church [i.e. Hardingham church]." This extends the project's existing **Saint-Hildevert tithe-gift pattern** — already documented for Caister + Cantley via Potin 1842 and preserved in `research/places/collegiale-saint-hildevert-gournay.md` and the G33 companion — to a **third Norfolk church**. Hugh's pattern was systematic: take English manorial advowsons and assign them to the Gournay-en-Bray collegiate chapter. Hardingham church joins Caister and Cantley as a documented Saint-Hildevert tithe-recipient.[^v71-armstrong-hardingham]

[^v71-armstrong-hardingham]: Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 8 (Norwich, 1781), Mitford Hundred — Cranworth / Hardingham / Reymerston / Letton / Swathing cluster entries. Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_8`. Source ID: `armstrong-norfolk-1781`.
```

### 13. Norwich place file — Cathedral cloister Gournay arms + Gournay's Place capital messuage

File: `research/places/norwich.md`.

```str_replace
old_string: [^nro-doke-17-henry-gurnay-1443]: Norfolk Record Office, Norwich Consistory Court will register Doke, 17, administration of the goods and possessions of Henry Gurnay of Norwich, 1443. NRO online catalogue: http://nrocat.norfolk.gov.uk. Discovered via the girders.net Medieval Gurneys compilation. Source ID: `nro-ncc-wills-registers`.
new_string: [^nro-doke-17-henry-gurnay-1443]: Norfolk Record Office, Norwich Consistory Court will register Doke, 17, administration of the goods and possessions of Henry Gurnay of Norwich, 1443. NRO online catalogue: http://nrocat.norfolk.gov.uk. Discovered via the girders.net Medieval Gurneys compilation. Source ID: `nro-ncc-wills-registers`.

## Armstrong 1781 — Norwich Cathedral cloister Gournay arms + Gournay's Place capital messuage

Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 10 (Norwich, 1781), Hundred of Norwich entries, supplies two specific Norwich findings for the family.

**Norwich Cathedral cloister arms.** Armstrong: "In 1382, Walter de Berney, citizen of Norwich, gave 100l. towards the iron work and glazing of the cloister windows; which work was perfected at the charge of the several families of Morley, Shelton, Scales, Erpingham, **Gournay**, Mowbray, Thorpe, Savage, &c. whose arms were to be seen in the windows of the cloister, above the bars, before the glazing was demolished. This famous and elegant cloister was finished in 1430, in the hundred and thirty-third year from its being first undertaken."

The Gournay arms in the Norwich Cathedral cloister glazing place the family in the late-14th-century Norwich-civic heraldic display alongside the Morley, Scales, Erpingham, Mowbray, and Thorpe families. The 1382 gift (Walter de Berney) and 1430 completion date frame the contribution; it is contemporaneous with G23 Edmund Gurney's documented Norwich City Treasurers' standing-counsel fee (already in the G23 companion via v63). The cloister glazing was demolished at some later date (the "before the glazing was demolished" reading is post-Dissolution or 17th-century), so the arms survive only in Armstrong's printed record.

**Gournay's Place — a separate Norwich capital messuage.** Armstrong vol. 10 (Hundred of Norwich, p. ~204): "The capital messuage called Gournay's Place, was in 1338 the city house of Thomas Gawdy, esq. and afterward belonged to the Pastons, from whom it passed to the family of the Cookes. Adjoining to the north side of this house was the key anciently called Kyrmer-hoppe, with a messuage belonging to the Berneys. The messuage of Sir Miles Stapleton, knt. lay on the north of the former and joined to it, afterward the property of Edward Grey, esq. and to the north of that the house of Sir William Boleyn, knt. afterward of the lady Anna Boleyn."

This is a **distinct Norwich Gurney building** from the St Gregory's parish house named in G20 Thomas Gournay II's 1471 will (already on this file) and from the "Gurney's Place" in St Julian's parish recorded by Daniel Gurney for G17 Anthony's lifetime (in the G17 fact-sheet narrative). Three Norwich "Gurney's Place" / Gurney-named buildings are therefore documented:

- **Gournay's Place** (Armstrong vol. 10) — pre-1338 (Thomas Gawdy holding in 1338; therefore Gurney-owned earlier still), with Berney, Stapleton, and Boleyn houses adjacent. Parish unnamed.
- **St Gregory's parish house** (G20 Thomas II's 1471 will) — sold 1471 to William IV (G19) for 80 marks.
- **Gurney's Place in St Julian's parish** (G17 Anthony's lifetime per Daniel Gurney).

The Armstrong record is the earliest of the three and the only one whose adjacent-property neighbours (Berney, Stapleton, Boleyn) are named — useful for further work locating the building in modern Norwich.[^v71-armstrong-norwich]

[^v71-armstrong-norwich]: Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 10 (Norwich, 1781), Hundred of Norwich — Cathedral cloister glazing entry; capital-messuage entry naming Gournay's Place. Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_10`. Source ID: `armstrong-norfolk-1781`.
```

## Validation checklist

- [ ] `research/people/g19-william-gurney-iv-fact-sheet.research.md` — gains Cawston 1578 + Thuxton 1500 section.
- [ ] `research/people/g20-thomas-gournay-ii-fact-sheet.research.md` — gains 1447 Berningham's attorney section (file may need to be created if not present).
- [ ] `research/people/g21-thomas-gournay-i-fact-sheet.research.md` — gains 1440 East Barsham Woolterton's confirmation section.
- [ ] `research/people/g23-edmund-gurney-fact-sheet.research.md` — gains Sir John V Heigham/Drayton/Hellesden/Taverham + Howard cup + Saxthorpe c. 1411 + 1373 West Barsham section.
- [ ] `research/people/g29-matthew-de-gournay-fact-sheet.research.md` — gains Armstrong-third-witness section.
- [ ] `research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md` — gains Bastwick Henry I grant section.
- [ ] `research/places/harpley.md` — gains 1297 fair + 1325 Uphall deed + 1332 nephew-grant + rector-stone 1781 observation section.
- [ ] `research/places/west-barsham.md` — gains chancel monument + arms list + 1373 transfer + 1641-1661 sale window section.
- [ ] `research/places/north-barsham.md` — gains Wauncy's Manor at Southall corroboration + G17 "of North Barsham" section.
- [ ] `research/places/hingham-norfolk.md` — gains 1572 lordship + 1715 Larwood successor section.
- [ ] `research/places/great-ellingham.md` — gains 1525 Margaret Lovell inheritance + Conyers/Lovell/Spelman kinship + post-1641 Davy descent + rectory mediety chain section.
- [ ] `research/places/hardingham.md` — gains King-John lordship + 1316 + 1257/1268 + Hugh's undated charter + Saint-Hildevert at Hardingham church section.
- [ ] `research/places/norwich.md` — gains Cathedral cloister arms + Gournay's Place capital messuage section.

## Phase 2 completion step

After application:

```bash
python - <<'PY'
from pathlib import Path
src = Path("sources/intake/processed/v71-armstrong-1781-companion-and-place-file-absorption.patchset.md")
dst = Path("sources/intake/done/v71-armstrong-1781-companion-and-place-file-absorption.patchset.md")
body = src.read_text(encoding="utf-8")
dst.write_text("**Done:** 2026-05-28 HH:MM PT\n\n" + body, encoding="utf-8")
src.unlink()
PY
```

Replace `HH:MM` with the actual completion time.
