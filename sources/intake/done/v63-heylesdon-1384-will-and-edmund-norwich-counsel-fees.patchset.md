**Done:** 2026-05-25 23:59 PT

# Intake patchset v63 — John Heylesdon's 1384 will (full Husting text) and Edmund Gurney's standing-counsel fees in Norwich

**Prepared:** 2026-05-25
**Phase:** 1. Ready for Phase 2.
**Sequencing:** Independent of v61/v62. Adds footnote handles `nNEW10`–`nNEW11` (no collision with v61/v62 ranges).

Two primary documents pulled from Internet Archive: (1) John Heylesdon's full 1384 Husting will at *Calendar of Wills proved and enrolled in the Court of Husting* vol. ii, pp. 241-243; (2) Norwich City Treasurers' fee-payment records to Edmund Gornay alongside Edmund de Clipesby at *Records of the City of Norwich* vol. ii, pp. 44 and 47.

## Action sequence

1. **Write file:** `sources/corpus_supplement/husting-wills-london-vol2-john-heylesdon-1384.md` — full content in §A1 below.
2. **Write file:** `sources/corpus_supplement/norwich-records-hudson-tingey-vol2-edmund-gornay-fees.md` — full content in §A2 below.
3. **Insert two source-JSON blocks** in `data/sources.json` — full JSON in §A3 below.
4. **Append block** to `research/people/g23-edmund-gurney-fact-sheet.research.md` — content in §A4 below.
5. **Append block** to `research/places/hellesdon.md` — content in §A5 below.
6. **`str_replace`** on `fact-sheets/g23-edmund-gurney-fact-sheet.md` footnote `n8` — old/new strings in §A6 below.
7. **`str_replace`** on `fact-sheets/g23-edmund-gurney-fact-sheet.md` Narrative paragraph 1 — old/new strings in §A7 below.
8. After all operations succeed, **move** this patchset to `sources/intake/done/` with `**Done:** YYYY-MM-DD HH:MM PT` stamp prepended.

---

## §A1 — New file: `sources/corpus_supplement/husting-wills-london-vol2-john-heylesdon-1384.md`

```md
# John de Heylesdon, mercer — will dated 14 April 1384, proved 20 July 1384

Source: Reginald R. Sharpe, ed., *Calendar of Wills proved and enrolled in the Court of Husting, London, A.D. 1258-A.D. 1688, preserved among the Archives of the Corporation of the City of London, at the Guildhall*, Part II (London: J. C. Francis, 1890), pp. 241-243. Husting Roll 113 (1). Internet Archive plain-text: <https://archive.org/stream/willshusting02sharuoft/willshusting02sharuoft_djvu.txt>. Source ID: `husting-wills-london-vol2-sharpe`.

Will dated London, 14 April 1384. Proved at the Court of Husting on Monday next before the Feast of S. Margaret, Virgin (20 July) 1384, 8 Richard II.

## Full calendar text

> Heylesdon (JOHN DE), mercer. — To be buried in the church of Heylesdon near the tomb of his father and mother. Bequests to the said church of vestments and ornaments, the parishioners being bound to give security to the rector of the church for the time being for the safe custody of the same; also to the poor of the vill of Heylesdon and other vills adjoining, to every mendicant friar in the cities of London and Norwich, to the old work of S. Paul's, to every rector in London for inserting his name in mortuary roll (*in suis memoralibus*), to the high altars of the churches of H. Trinity the Less and S. Michael de Paternostercherche, &c.; also to Robert his brother, Margaret his sister, Alice and Margaret his daughters, and others. To John Chircheman and Sir Richard Tasburgh, rector of the church of Heylesdon, he leaves twenty marks annual quitrent of lands and tenements in the parish of All Hallows de Graschirche, on condition that they maintain thereout two perpetual chantries in the church of Heylesdon for the good of his soul, the souls of Johanna his wife, Walter de Berneye, Edmund de Alderford, John Chircheman and Emma, wife of the same, Thomas de Aldeburgh, and others. Johanna his wife to enjoy a life interest in the above lands and tenements, subject to the said charge, by way of dower of all his other lands and tenements, and also to have the sum of two hundred pounds sterling by way of dower of all his movable goods, in addition to her entire chamber, ornaments, and personal clothing. His said wife to accept the above in the name of dower, or to have what the law adjudges her. After her decease the aforesaid lands and tenements to go to Margaret his daughter in tail; remainder in trust for sale for pious uses. To Alice his daughter lands and tenements in the city of Norwich in tail, with similar remainder; also, under certain conditions, she is to have his tenements in Westchepe, London, called the "Crowned Seld" (*la Selde coronata*). To Agnes, wife of Bartholomew Marche, rents in the parishes of S. Alban de Wodestrete and S. Giles without Crepulgate. Bequests also to poor lepers within three miles of London; for the redemption of poor prisoners in Ludgate and Neugate; to his poor kinsfolk in Heylesdon and elsewhere, co. Norfolk; for putting poor scholars to school; for sending two pilgrims to Rome, there to remain in prayer throughout one Lent (*per unam quadragesimam*); to the Carthusian monks near Westsmythfeld, the Nuns Minoresses without Algate, and the nuns of Shuldham; to William Reve, rector of the church of Drayton, John and Thomas Tasburgh, Margaret, wife of Thomas Mounteneye, and others. Forty pounds, more or less, to be expended on his funeral. Dated London, 14 April, A.D. 1384. — By a codicil annexed he varies former bequests made in the case of either of his daughters dying under age. Roll 113 (1).
>
> Note. — The above will was made an exhibit in Chancery, *re Attorney-General v. Fishmongers' Company*.

## Significance for the Gurney line

This is the foundation document for the entire Heylesdon settlement that came into the West Barsham Gurney portfolio through Sir John Gurney V (d. 1408)'s marriage to Alice Heylesdon. The will identifies:

- **Wife:** Johanna (Joan).
- **Daughters:** Alice (the future Lady Gurney) and Margaret (who died before majority — see History of Parliament biography of Sir John V). Both were under age at the will date; the codicil specifically addresses under-age death.
- **Brother:** Robert Heylesdon. **Sister:** Margaret Heylesdon.
- **Two perpetual chantries** at Hellesdon parish church, endowed by 20-marks-yearly quitrent from All Hallows de Graschirche, London. Trustees: John Chircheman and Sir Richard Tasburgh (then rector of Hellesdon). For the souls of John himself, Johanna, Walter de Berneye, Edmund de Alderford, John Chircheman and Emma wife of same, Thomas de Aldeburgh, and others.
- **"Crowned Seld" / la Selde coronata** in Westcheap, London — bequeathed specifically to Alice under conditions. (Identified in Stow's *Survey* as a building "Crownsild" granted by Henry IV to mercers in Westcheap, also known as "Tamersilde," possibly originally "Tanners' Seld.")
- **Norwich lands and tenements** — to Alice in tail.
- Norfolk-Hellesdon-kinsfolk bequests imply a wider Heylesdon family in Norfolk.
- Drayton (the other Heylesdon Norfolk manor) — William Reve as rector. John and Thomas Tasburgh as Hellesdon-connected clerics.

Burial directive "near the tomb of his father and mother" anchors at least two prior Heylesdon generations at Hellesdon parish church.

The Chancery note (*Attorney-General v. Fishmongers' Company*) indicates post-Reformation litigation over the chantry endowments, almost certainly after the Edward VI chantry dissolutions.
```

---

## §A2 — New file: `sources/corpus_supplement/norwich-records-hudson-tingey-vol2-edmund-gornay-fees.md`

```md
# Norwich City Treasurers' fee payments to Edmund Gornay

Source: William Hudson and John Cottingham Tingey, eds., *The Records of the City of Norwich* (Norwich and London: Jarrold, 1910), vol. ii, "Selected Records of the City of Norwich," City Treasurers' Accounts, pp. 44 and 47. Index of Names entry confirms: "Gornay, Edmund, 44, 7." Internet Archive plain-text: <https://archive.org/stream/recordsofcityofn02norwuoft/recordsofcityofn02norwuoft_djvu.txt>. Source ID: `norwich-records-hudson-tingey-vol2`.

## First payment paragraph (p. 44)

> Fees paid. First, paid to Edmund Gornay for his fee this year, 20s. To Edmund de Clipesby, 20s. To the said Treasurers for their fees this year, 40s. To Thomas de Worthsted etc. 13s. 4d. To William de Worthsted, clerk of the community etc. 40s. Sum £6 13s. 4d.

## Second payment paragraph (p. 47)

> Fees Paid. To Edmund Gornay for his fee this year, 20s. To Edmund de Clipesby etc. 20s. To John Drake etc. 13s. 4d. To John de Tasburgh, Common Sergeant, etc. £5 12s. To William de Worthstede, Common Clerk etc. 53s. 4d. Sum £8 18s. 8d.

## Significance for the Gurney line

These two fee-payment paragraphs are the direct primary record behind Blomefield's general standing-counsel reference and the History of Parliament biography of Sir John Gurney V which describes Edmund as "a successful lawyer whose counsel had been sought on occasion by the city of Norwich and the borough of Bishop's Lynn."

The key point Blomefield does not surface: Edmund was paid in the **same fee paragraph as Edmund de Clipesby**, also at 20 shillings. Clipesby is the lawyer the History of Parliament biography identifies as joint Duchy of Lancaster steward with Edmund Gurney's father and as the man murdered at his home in 1392 by servants of Bishop Despenser of Norwich, with Sir John Gurney V then threatened with death if he tried to open proceedings against the killers. The Norwich Treasurers' books show Gornay and Clipesby were a documented retainer pair to the city for years before the killing.

## A separate later "Gurnay, John" Norwich tenant

The same volume index also carries a separate entry: "Gurnay, John, 245, 7." This refers to a Norwich tenant John Gurnay holding small tenements in St Stephen parish (formerly Etheldreda Sparwe's) at low rents (2d). Identification with any named Gurney from the West Barsham pedigree is not warranted. Logged here only for completeness.
```

---

## §A3 — Source JSON additions in `data/sources.json`

Insert the following two entries into the top-level `sources` object:

```json
    "husting-wills-london-vol2-sharpe": {
      "shortTitle": "Sharpe -- Calendar of Wills Court of Husting London Part II (1890)",
      "citation": "Reginald R. Sharpe, ed., Calendar of Wills proved and enrolled in the Court of Husting, London, A.D. 1258-A.D. 1688, preserved among the Archives of the Corporation of the City of London, at the Guildhall, Part II (London: J. C. Francis, 1890).",
      "archive": "Internet Archive",
      "url": "https://archive.org/details/willshusting02sharuoft",
      "corpusStatus": "supplement",
      "corpusPath": "sources/corpus_supplement/husting-wills-london-vol2-john-heylesdon-1384.md",
      "mediaPath": null,
      "validationPath": null,
      "notes": "Part II covers A.D. 1358-1688. Used in v63 for the full Husting calendar text of John Heylesdon's 1384 will at pp. 241-243 (Roll 113 (1)), foundation document for the Heylesdon settlement that came into the Gurney line via Sir John V's marriage to Alice Heylesdon. Will dated 14 April 1384, proved 20 July 1384, 8 Richard II."
    },
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
```

---

## §A4 — Append to `research/people/g23-edmund-gurney-fact-sheet.research.md`

Append the following block at the end of the existing "Norwich civic counsel and North Barsham corroboration" sub-section (after the `[^blomefield-north-barsham-g23]` footnote definition):

```md
### Norwich Treasurers' fee payments to Edmund — primary record

The Norwich City Treasurers' accounts in *Records of the City of Norwich* vol. ii (Hudson and Tingey 1910), pp. 44 and 47, record two annual fee payments of 20 shillings each to "Edmund Gornay," paid in the same fee paragraph as the 20s paid to Edmund de Clipesby:

> "Fees paid. First, paid to Edmund Gornay for his fee this year, 20s. To Edmund de Clipesby, 20s. To the said Treasurers for their fees this year, 40s." (p. 44)

> "Fees Paid. To Edmund Gornay for his fee this year, 20s. To Edmund de Clipesby etc. 20s. To John Drake etc. 13s. 4d. To John de Tasburgh, Common Sergeant, etc. £5 12s." (p. 47)

This is the direct primary attestation behind Blomefield's standing-counsel reference and the History of Parliament biography's phrasing. The retainer-pair detail with Edmund de Clipesby is the new content: Clipesby is the lawyer the History of Parliament biography identifies as joint Duchy of Lancaster steward with Edmund Gurney's father and as the man murdered at his home in 1392 by servants of Bishop Despenser, with Sir John V then threatened with death if he opened proceedings against the killers. Gornay and Clipesby were a documented retainer pair to the city for years before the killing.

Full text of both paragraphs and the volume's later "Gurnay, John 245, 7" Norwich-tenant entry preserved at `sources/corpus_supplement/norwich-records-hudson-tingey-vol2-edmund-gornay-fees.md`.[^v63-norwich-records-edmund-gornay-fees]

[^v63-norwich-records-edmund-gornay-fees]: William Hudson and John Cottingham Tingey, eds., *The Records of the City of Norwich* (Norwich and London: Jarrold, 1910), vol. ii, "Selected Records of the City of Norwich," City Treasurers' Accounts, pp. 44 and 47. Internet Archive: [archive.org/stream/recordsofcityofn02norwuoft/recordsofcityofn02norwuoft_djvu.txt](https://archive.org/stream/recordsofcityofn02norwuoft/recordsofcityofn02norwuoft_djvu.txt). Index of Names entry: "Gornay, Edmund, 44, 7." Source ID: `norwich-records-hudson-tingey-vol2`.

### John Heylesdon's 1384 Husting will — foundation document for the Heylesdon settlement

Append also under the existing Sir John V sub-section: Reginald R. Sharpe, *Calendar of Wills proved and enrolled in the Court of Husting, London* Part II (1890), pp. 241-243, Roll 113 (1), preserves the full Husting calendar text of John Heylesdon's will, dated London 14 April 1384 and proved at the Husting on Monday next before St Margaret the Virgin (20 July) 1384.

Key provisions:

- Buried at Hellesdon parish church "near the tomb of his father and mother" — anchoring two prior Heylesdon generations at the parish.
- **Wife:** Johanna.
- **Daughters:** Alice (the future wife of Sir John Gurney V) and Margaret (who died before majority per the History of Parliament biography).
- **Brother:** Robert Heylesdon. **Sister:** Margaret Heylesdon.
- **Two perpetual chantries** at Hellesdon parish church, endowed by 20 marks yearly quitrent of lands in the London parish of All Hallows de Graschirche. Trustees: John Chircheman and Sir Richard Tasburgh (then rector of Hellesdon). For the souls of John, Johanna, Walter de Berneye, Edmund de Alderford, John Chircheman and Emma wife of same, Thomas de Aldeburgh, and others.
- Wife Johanna: life interest in the Hellesdon lands subject to the chantry charge; £200 sterling by way of dower of his movable goods; her entire chamber, ornaments, personal clothing.
- After Johanna's decease, the Hellesdon lands to Margaret his daughter in tail; remainder in trust for sale for pious uses.
- **To Alice his daughter** — lands and tenements in the city of Norwich in tail; and "under certain conditions," his tenements in Westcheap, London, called the "Crowned Seld" (*la Selde coronata*).
- Other bequests: Agnes wife of Bartholomew Marche; poor lepers within three miles of London; redemption of poor prisoners in Ludgate and Newgate; poor kinsfolk in Hellesdon and elsewhere in Norfolk; poor scholars at school; two pilgrims to Rome for one Lent; the Carthusian monks near West Smithfield; the Nuns Minoresses without Aldgate; the nuns of Shouldham; William Reve, rector of the church of Drayton; John and Thomas Tasburgh; Margaret wife of Thomas Mounteneye. £40 on his funeral. Codicil annexed.
- The Husting calendar notes the will was later made an exhibit in Chancery, *Attorney-General v. Fishmongers' Company* — almost certainly post-Reformation litigation over the chantry endowments after the Edward VI dissolutions.

This is the document from which the entire downstream Heylesdon-Gurney property settlement flows. When Margaret died before majority, Alice inherited everything (Crowned Seld, Norwich tenements, the Hellesdon and Drayton manors, the chantry advowsons, and the Norfolk kinsfolk network). On her marriage to Sir John Gurney V it all entered the West Barsham Gurney portfolio.

Full calendar text and the Stow / Crowned Seld identification preserved at `sources/corpus_supplement/husting-wills-london-vol2-john-heylesdon-1384.md`.[^v63-husting-heylesdon-1384]

[^v63-husting-heylesdon-1384]: Reginald R. Sharpe, ed., *Calendar of Wills proved and enrolled in the Court of Husting, London, A.D. 1258-A.D. 1688*, Part II (London: J. C. Francis, 1890), pp. 241-243, Roll 113 (1). Internet Archive: [archive.org/stream/willshusting02sharuoft/willshusting02sharuoft_djvu.txt](https://archive.org/stream/willshusting02sharuoft/willshusting02sharuoft_djvu.txt). Source ID: `husting-wills-london-vol2-sharpe`.
```

---

## §A5 — Append to `research/places/hellesdon.md`

Append the following block at the end of the file (after the existing closing content):

```md
## John Heylesdon's 1384 will and the two perpetual chantries

The Hellesdon manor and the two perpetual chantries founded in the parish church entered the West Barsham Gurney portfolio through the marriage of Alice Heylesdon (daughter of John Heylesdon, d. 1384) to Sir John Gurney V (d. 1408). The foundation document is John Heylesdon's will of 14 April 1384, proved at the Court of Husting in London on 20 July 1384.

The will directs burial at Hellesdon parish church "near the tomb of his father and mother," confirming at least two prior Heylesdon generations at the parish. Two perpetual chantries were endowed by 20 marks annual quitrent from London property in the parish of All Hallows de Graschirche, with John Chircheman and Sir Richard Tasburgh (then rector of Hellesdon) as the chantry trustees. The London Westcheap warehouse "Crowned Seld" (*la Selde coronata*) and lands and tenements in the city of Norwich were bequeathed specifically to Alice in tail.

Full Husting calendar text and discussion preserved at `sources/corpus_supplement/husting-wills-london-vol2-john-heylesdon-1384.md`.[^v63-husting-heylesdon-1384-place]

[^v63-husting-heylesdon-1384-place]: Reginald R. Sharpe, ed., *Calendar of Wills proved and enrolled in the Court of Husting, London, A.D. 1258-A.D. 1688*, Part II (London: J. C. Francis, 1890), pp. 241-243, Roll 113 (1). Internet Archive: [archive.org/stream/willshusting02sharuoft/willshusting02sharuoft_djvu.txt](https://archive.org/stream/willshusting02sharuoft/willshusting02sharuoft_djvu.txt). Source ID: `husting-wills-london-vol2-sharpe`.
```

---

## §A6 — `str_replace` on `fact-sheets/g23-edmund-gurney-fact-sheet.md` footnote `n8`

**`old_string`:**

```
  <li id="n8">Daniel Gurney, <em>Supplement</em> (1858), p. 359: "these two, Clipesby and Gurney, were the standing council for the city of Norwich, in the nature of recorder and steward." Bishop's Lynn: cited in project knowledge base and JSON from prior research. <a class="citation-back" href="#ref-8">↩</a></li>
```

**`new_string`:**

```
  <li id="n8">Daniel Gurney, <em>Supplement</em> (1858), p. 359: "these two, Clipesby and Gurney, were the standing council for the city of Norwich, in the nature of recorder and steward." The underlying primary record is in the City Treasurers' Accounts at William Hudson and John Cottingham Tingey, eds., <em>The Records of the City of Norwich</em> (Norwich and London: Jarrold, 1910), vol. ii, "Selected Records of the City of Norwich," pp. 44 and 47, recording payment of 20 shillings yearly to "Edmund Gornay for his fee this year" in the same fee paragraph as the 20 shillings paid to Edmund de Clipesby. Internet Archive: <a href="https://archive.org/stream/recordsofcityofn02norwuoft/recordsofcityofn02norwuoft_djvu.txt">archive.org/stream/recordsofcityofn02norwuoft/recordsofcityofn02norwuoft_djvu.txt</a>. Bishop's Lynn: cited in project knowledge base and JSON from prior research. <a class="citation-back" href="#ref-8">↩</a></li>
```

---

## §A7 — `str_replace` on `fact-sheets/g23-edmund-gurney-fact-sheet.md` Narrative paragraph 1

**`old_string`:**

```
Edmund Gournay is the ancestor who transformed the family's position in Norfolk society. His predecessors at Harpley had been respectable minor gentry — knights and esquires of moderate standing. Edmund became something considerably more: a lawyer of county-wide reputation, retained by the city of Norwich, by the borough of Bishop's Lynn, and — most impressively of all — by John of Gaunt himself, as steward of the Duke's East Anglian estates.
```

**`new_string`:**

```
Edmund Gournay is the ancestor who transformed the family's position in Norfolk society. His predecessors at Harpley had been respectable minor gentry — knights and esquires of moderate standing. Edmund became something considerably more: a lawyer of county-wide reputation, retained by the city of Norwich (the Norwich City Treasurers' accounts record him at 20 shillings a year, paid in the same paragraph as Edmund de Clipesby — the lawyer who would be murdered in 1392 by servants of the Bishop of Norwich, with Edmund's son Sir John then threatened with death for trying to open proceedings), by the borough of Bishop's Lynn, and — most impressively of all — by John of Gaunt himself, as steward of the Duke's East Anglian estates.
```

---

End of patchset.
