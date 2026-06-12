**Done:** 2026-06-11 20:43 PT

# Patchset v90 â€” Henry G15's last will (1 May 1621, proved 23 Oct 1623); the NCC register map; the Waveney network resolved (James Adams will)

**Session:** chat-first FTS campaign session 2026-06-11, plus expert paleography packets 10â€“11 (reports in `sources/intake/paleography-staging/`). This patchset is the promotion vehicle; no `sources/intake/new/` session file exists.

**What this promotes.**
1. **Henry Gurnay G15's last will** â€” made 1 May 1621 (19 James I), proved Norwich 23 October 1623, administration to his son Anthony. Expert-read (packet 10). Revises Henry's death from "1615/16" to **between May 1621 and October 1623**, and exposes two child-level conflicts (Thomas, Anthony). Destinations: G15 companion (full treatment), G15 fact sheet (death/burial/children/timeline), `data/ancestors.json`.
2. **The NCC will-register â†’ DGS map** (new topic file) â€” the registered-copy-wills series mapped year-by-year from the FamilySearch catalog, with the 2026-06-11 sweep results, including the coverage-confirmed negative for Edmund the Divine's will (1643â€“51 registers).
3. **The Waveney/Earsham Gurney network** â€” the 1638 Earsham will's probate clause (proved Norwich 26 Dec 1639); Sarah Gurney of Bungay's 1710 nuncupative will read in full; and the packet-11 correction that the "sister Sarah Gurney" legacies belong to the will of **James Adams of Bungay, merchant (31 Jan 1692/3)** â€” Sarah Gurney was his sister â€” while the adjacent Mary Scamler will is unrelated. Destinations: Earsham subject file, corpus supplement.
4. **Paleography batch disposition** â€” packets 10â€“11 reports and master images to their durable homes.

**Already done directly in-session (allowed classes, disclosed in chat):** leads CSV updates (L-6, L-106, L-109, L-110, L-111); skill method update; removal of the G17-will paragraph from the G13 companion (Allen-approved correction); rule update to `research-files.md` (companion scope + synthesis-over-log).

**Source tracking:** every item cites the existing sourceId `familysearch-fulltext-search` (validation file exists). No new sourceId; no new validation file.

---

## Item 01 (promote) â€” new topic file: the Norwich Consistory Court will registers in Full-Text Search

**Why a topic file:** the register series serves every English generation (G13â€“G17 probates so far), so the inventory lives here, not on any one companion.

**Target (new file write):** `research/topics/norwich-consistory-wills-register-map.md`

```
# The Norwich Consistory Court will registers in FamilySearch Full-Text Search â€” film map and sweep log

The Norwich Consistory Court (NCC) was the bishop's probate court for Norfolk, Suffolk, and part of Cambridgeshire â€” the court that proved the wills of Anthony Gurney G17 (1557), John Gurney of Earsham (1639), Henry Gurnay G15 (1623), and the Waveney-family wills around the Earsham Gurneys. Its registered-copy-will volumes (1370â€“1858) are digitised and machine-transcribed in FamilySearch Full-Text Search as year-labelled films ("Norwich. Wills 1638â€“1639," etc.). This file maps register years to film (DGS) numbers so any probate year is a two-step pull: take the DGS from the table, film-scope the query (`q.groupName=<DGS>`).[^ncc-register-map]

## Register â†’ DGS map (registered copy wills; volumes verified in use)

| Vols. | Years | DGS | Notes |
|---|---|---|---|
| â€” | 1556â€“1557 | 008076312 | Anthony Gurney G17's will at image 145 |
| 96â€“109 | 1600â€“1614 | 008076500â€“008076507 (with 008452447 = 1602, 008452448 = 1609, 008398214 = 1611) | one to two years per volume |
| 110â€“111 | 1615â€“1616 | 008076508 | swept clean (below) |
| 112â€“113 | 1617â€“1618 | 008076509 | swept clean |
| 114â€“115 | 1619â€“1620 | 008076510 | swept clean |
| 116â€“118 | 1621â€“1623 | 008470484 | **Henry Gurnay G15's will, images 594â€“596** |
| 119â€“120 | 1624â€“1625 | 008470970 | |
| 121 | 1626 | 008219670 | |
| 122â€“123 | 1627â€“1628 | 008076511 | |
| 127 | 1634 | 008076861 | |
| 128 | 1635 | 008472223 | |
| 129 | 1636 | 008076860 | |
| 130 | 1637 | 008076859 | |
| 131 | 1638â€“1639 | 008076858 | John Gurney of Earsham's will, images 454â€“456 |
| 132 | 1640â€“1642 | 008472224 | |
| 133 | 1643â€“1646 | 008402405 | swept clean (Edmund target) |
| 134 | 1647â€“1651 | 007904832 | swept clean (Edmund target) |
| 135 | 1660â€“1661 | 008472225 | **Interregnum gap before this volume** â€” no NCC registers 1652â€“1659 (probate centralized in London; use PCC PROB 11) |
| 136â€“141 | 1664â€“1686 | 008076857, 008472229, 008076862, 008076921, 008472230 | |
| 142â€“143 | 1691â€“1698 | 008472233 | Mary Scamler and James Adams wills, images 199â€“202 |
| 147 | 1709â€“1711 | 008076925 | Sarah Gurney of Bungay's nuncupative will, image 450 |

Source for the map: the catalog record's Film/Digital Notes table (289 reels), which also lists original-will bundles, calendars/indexes (e.g., calendars to wills 1592â€“1649 = DGS 008076232), and administration volumes not reproduced here â€” return to the catalog record for anything outside the registered-copy series.[^ncc-register-map]

## Gurney sweep log (2026-06-11)

- **1615â€“16, 1617â€“18, 1619â€“20** (`Gurn* Gourn*`): no Gurney testator. Coverage confirmed per film by `+wife` probes; the only cards are garble ("Gurnance" â‰ˆ *governance*; a "do bene Gurne" token inside a Latin probate formula, [ark:/61903/3:1:3Q9M-CSN8-T942-7](https://www.familysearch.org/ark:/61903/3:1:3Q9M-CSN8-T942-7?view=fullText), image 528). Consequence: **the 1621â€“23 will of Henry Gurnay of Great Ellingham is the only Gurney will registered at Norwich in 1615â€“1623** â€” there is no 1615/16 Henry Gurney probate.
- **1621â€“23**: two cards â€” Henry Gurnay G15's will (see the [G15 companion](https://github.com/allengurney/gurney-genealogy/blob/main/research/people/g15-henry-gurney-fact-sheet.research.md)), and an unrelated will at image 365 with legatee token "the said Gourne my [sonne?]" and a "Henry Porter of Barton" ([ark:/61903/3:1:3Q9M-C39Z-C3SQ-X](https://www.familysearch.org/ark:/61903/3:1:3Q9M-C39Z-C3SQ-X?view=fullText)) â€” unexamined minor card.
- **1643â€“46 and 1647â€“51** (`Gurn*`, `Gourn*`, `+Harpley`): zero. Coverage confirmed. **Edmund Gurney the Divine's will (d. 1648, rector of Harpley) is not findable at machine level in the NCC registers**; given the Interregnum gap after 1651, the next stop is the Prerogative Court of Canterbury (PROB 11, TNA) for a 1648â€“1659 probate. (Lead L-6.)

[^ncc-register-map]: FamilySearch catalog record koha:278818, "Probate records for the Episcopal Consistory Court, Archdeaconry of Norwich, 1370â€“1858" (Church of England, Diocese of Norwich, Consistory Court; 289 microfilm reels), Film/Digital Notes table read 2026-06-11. Film-scoped sweeps and coverage probes per `.claude/skills/familysearch-fulltext-research/SKILL.md`. Source ID: `familysearch-fulltext-search`.
```

## Item 02 (promote) â€” G15 companion: the last will, the death-date revision, and the child conflicts

**Target:** `research/people/g15-henry-gurney-fact-sheet.research.md`

**Operation 02a â€” str_replace.** Replace:

```
## Working Notes

### 2026-05-29 â€” Visitation of Norfolk pedigree (a fifth source for Henry â†’ Francis "of London")
```

with:

```
## Working Notes

### 2026-06-11 â€” Henry's last will: made 1 May 1621, proved 23 October 1623 â€” the death date moves to 1621Ã—1623

**The question.** Henry's death has been published as 1615 or early 1616 (Pease gives 23 February 1615; the Catalogue of English Literary Manuscripts and Steven May give 1616), with the unexplained oddity that his will â€” known to Daniel Gurney only as a text "dated 1614" â€” was "proved 1623," eight or nine years after the supposed death. Lead L-111 sought the registered will itself in the digitised Norwich Consistory Court registers.

**The finding.** The NCC registered-copy-wills volume for 1621â€“1623 carries Henry's **last** will: "In the name of God Amen. I H[enrie] Gurnay of Greate Elingham in the Countie of Norff[olk], Esquier â€¦ all former wills being revoked or to be abolished â€¦ the first daie of May in the xixth yeare of the Raigne of our Soveraigne Lorde Kinge James, and in the yeare of our Lord God 1621." It was proved at Norwich **23 October 1623**, before Nathaniel Yednam [Yedham?], doctor of laws, and administration was committed to "**Anthonii Gurnay filii naturalis et legitimi dicti defuncti**" â€” Anthony Gurnay, his natural and lawful son. Henry was therefore alive on 1 May 1621 and dead by 23 October 1623 â€” the "d. 1615/16" tradition is superseded by the primary record, on the same pattern as Anthony G17's Blomefield death date (corrected by his 1557 register will). The 1614 will Daniel Gurney extracted (burial "next to my wife there"; the "fantasticall or erroneous opinions" warning) was an **earlier will, revoked** by the 1621 text â€” which instead leaves burial "in Christian buriall at the discretion of my executor." Identification with G15 is effectively certain: testator style (Great Ellingham, Esquire), the probate-1623 match, and the child-set below; the only residual alternative (Henry the second son, b. 1576, with an identically named child-set) is dismissably improbable. Corroborating negative: the NCC registers for 1615â€“16, 1617â€“18, and 1619â€“20 â€” all confirmed in Full-Text coverage â€” contain **no Gurney testator**, so there is no competing 1615/16 probate (see the [register map](https://github.com/allengurney/gurney-genealogy/blob/main/research/topics/norwich-consistory-wills-register-map.md)).[^henry-will-1621]

**The children in the will.** Bequests and the already-portioned recital name: eldest son **Thomas** (the silver-and-gilt basin and ewer); sons **Henry**, **Edward**, and **Francis** among children "heretofore" given their portions; **Francis** separately receives "all my bookes in Latyne" â€” the commonplace-book poet's Latin library passing to the Merchant Taylor sixth son (G14); daughters **Elizabeth** (portioned) and the unmarried **Anne** and **Abigayle** (Â£200 portions at marriage, Â£20 yearly maintenance, payable on demand after two years even if unmarried, cross-remainder to the survivor, Â£200 to younger sons if both die unmarried); the executor must bond for the daughters' portions before taking his benefit; Â£10 to the poor of Great Ellingham as a continuing churchwardens' loan-stock (sums of 20s or under, on pawn or bill obligatory, the minister as "moderator" in disputes). **No wife is named or provided for** â€” consistent with Ellen Blennerhasset's death before May 1621 and the 1614 will's burial directive beside her. **No grandchild and no New England kin is named.** Anthony, not named in the legacy clauses as read, is established by the probate clause and was very likely the executor.[^henry-will-children]

**Two conflicts exposed (not resolved).** (1) **Thomas:** the family genealogies say the eldest son Thomas III died in 1614, *vita patris*; the 1621 will bequeaths to "my eldest sonne Thomas." Either Thomas was alive in May 1621 (and died 1621Ã—1623, still before his father) and the 1614 date is wrong â€” possibly a confusion with the 1614 *will* â€” or the registered text carries a recital from the earlier will. The will is primary and the bequest reading is high-confidence; the 1614 tradition should be traced to its root (Daniel Gurney p. 287 / Pease) before the fact sheets pick a Thomas death year. (2) **Anthony:** the fact sheet carried Anthony (Francis's twin, b. 1581) as died *vita patris*; the probate clause shows him alive, administering, on 23 October 1623. The *vita-patris* claim is superseded.[^henry-will-conflicts]

[^henry-will-1621]: Norwich Consistory Court registered copy wills, vols. 116â€“118 (1621â€“1623), FamilySearch DGS 008470484 (British Film 94937), images 594â€“596: [ark:/61903/3:1:3Q9M-C39Z-C39M-3](https://www.familysearch.org/ark:/61903/3:1:3Q9M-C39Z-C39M-3?view=fullText), [ark:/61903/3:1:3Q9M-C39Z-C3MP-N](https://www.familysearch.org/ark:/61903/3:1:3Q9M-C39Z-C3MP-N?view=fullText), [ark:/61903/3:1:3Q9M-C39Z-C3MJ-W](https://www.familysearch.org/ark:/61903/3:1:3Q9M-C39Z-C3MJ-W?view=fullText). Expert paleographic transcription 2026-06-11: `sources/corpus_supplement/paleo-2026-06-packet-10-henry-gurnay-great-ellingham-will.md` (date line and probate clause high-confidence; surfaced by the film-scoped query `Gurn* Gourn*`). The 1614 will: Daniel Gurney, *Supplement* (1858), pp. 875 ff., and the fuller extract in *A Hundred Years at Northrepps* (see fact-sheet citation 6). Pease 23 Feb 1615: Pease/Pennyghael Gurney genealogy (2016). CELM/May 1616: *Spenser Studies* 20 (2005), 183â€“223. Source ID: `familysearch-fulltext-search`.
[^henry-will-children]: Packet-10 transcription (citation above), confidence levels per its report: Thomas-eldest, Anne/Abigail portions, poor-stock, probate/administration high; the already-portioned list (Henry, Edward, Francis, Elizabeth) and "bookes in Latyne" medium â€” "in Latyne" preferred over "in London" on letter forms. Visitation child-set control: Walter Rye, ed., *The Visitations of Norfolk, 1563, 1589 and 1613* (Harleian Society vol. 32, 1891), p. 141. Source ID: `familysearch-fulltext-search`.
[^henry-will-conflicts]: Thomas d. 1614: Daniel Gurney, *Record* (1848), pedigree p. 287, and Pease/Pennyghael (the fact sheet's citations 12 and 2). Anthony *vita patris*: same pedigree sources (fact-sheet citation 15). Against both: packet-10 readings of the bequest to "my eldest sonne Thomas" and the probate commission to Anthony, 23 Oct. 1623. Source ID: `familysearch-fulltext-search`.

### 2026-05-29 â€” Visitation of Norfolk pedigree (a fifth source for Henry â†’ Francis "of London")
```

**Operation 02b â€” str_replace** (retire the stale friction recommendation). Replace:

```
1. **Death date.** The project `ancestors_v3.json` gives "21 Jan. 1548 â€” d. 1623." The 1623 date is "will proved 1623," not a death date. Recommend updating to "21 Jan. 1548 â€” d. 1615/16 (will proved 1623)."
```

with:

```
1. **Death date.** ~~Recommend updating to "d. 1615/16 (will proved 1623)."~~ Superseded 2026-06-11: Henry's last will (1 May 1621, proved 23 Oct. 1623) places his death between those dates â€” see the 2026-06-11 working note above. The structured data now reads "d. 1621Ã—1623."
```

## Item 03 (promote) â€” G15 fact sheet: death window, burial wording, children rows, timeline

**Target:** `fact-sheets/g15-henry-gurney-fact-sheet.md` (all operations are surgical str_replace)

**Operation 03a.** Replace:

```
pageHeading: Henry Gurnay, Esq. (1548/49 â€“ 1615/16)
```

with:

```
pageHeading: Henry Gurnay, Esq. (1548/49 â€“ 1623)
```

**Operation 03b.** Replace:

```
    "deathDate": "1615",
```

with:

```
    "deathDate": "1623",
```

**Operation 03c.** Replace:

```
    <div class="fact-value">1615 or early 1616. Date contested between sources; will proved 1623. See Research Appendix. <sup class="fn"><a href="#n2" id="ref-2">2</a></sup></div>
```

with:

```
    <div class="fact-value">Between May 1621 and October 1623. He made his last will on 1 May 1621 and it was proved at Norwich on 23 October 1623; older accounts gave 1615 or 1616. <sup class="fn"><a href="#n2" id="ref-2">2</a></sup></div>
```

**Operation 03d.** Replace:

```
    <div class="fact-value">All Saints, West Barsham, Norfolk â€” next to his wife Ellen Blennerhasset, per the language of his own 1614 will: "my body to rest till the joyfull resurrectio in the parish Church next to my wife there." The Pease/Pennyghael genealogy independently records Ellen's burial at West Barsham. The epitaph verse to "Henry Gournay squire" preserved by Verily Anderson is associated with Great Ellingham (Henry's principal late-life residence), but the formal burial â€” by Henry's own direction â€” was at the West Barsham seat. <sup class="fn"><a href="#n4" id="ref-4">4</a></sup></div>
```

with:

```
    <div class="fact-value">Probably All Saints, West Barsham, Norfolk â€” next to his wife Ellen Blennerhasset, the wish he set down in an earlier will of 1614: "my body to rest till the joyfull resurrectio in the parish Church next to my wife there." His final will of 1621 left the burial to his executor's discretion, so the West Barsham resting place is his recorded wish rather than a documented interment. The epitaph verse to "Henry Gournay squire" preserved by Verily Anderson is associated with Great Ellingham, his principal late-life residence. <sup class="fn"><a href="#n4" id="ref-4">4</a></sup></div>
```

**Operation 03e.** Replace:

```
  <li id="n2">Daniel Gurney, <em>Record</em> (1848), pedigree p. 287, gives "will proved 1623." Pease/Pennyghael Gurney genealogy (Charles E. G. Pease, 2016, <a href="http://www.pennyghael.org.uk/Gurney.pdf">Gurney.pdf</a>) gives "died 23 Feb 1615 in West Barsham, Norfolk." The Catalogue of English Literary Manuscripts (Folger Shakespeare Library) and Steven W. May, "Henry Gurney, A Norfolk Farmer, Reads Spenser and Others," <em>Spenser Studies</em> 20 (2005), 183â€“223 (DOI 10.1086/SPSv20p183), both give life dates as 1549â€“1616. Most likely reconciliation: died 1615 or early 1616, will proved 1623 due to the disrupted succession (his eldest son Thomas III having died in 1614). <a class="citation-back" href="#ref-2">â†©</a></li>
```

with:

```
  <li id="n2">Henry's last will, made 1 May 1621 ("the first daie of May in the xixth yeare of the Raigne of our Soveraigne Lorde Kinge James, and in the yeare of our Lord God 1621"), registered copy in the Norwich Consistory Court will register for 1621â€“1623, FamilySearch image group 008470484, images 594â€“596 (<a href="https://www.familysearch.org/ark:/61903/3:1:3Q9M-C39Z-C39M-3">ark:/61903/3:1:3Q9M-C39Z-C39M-3</a> and following); proved at Norwich 23 October 1623, administration committed to "Anthonii Gurnay filii naturalis et legitimi dicti defuncti" â€” his son Anthony. Expert transcription at <code>sources/corpus_supplement/paleo-2026-06-packet-10-henry-gurnay-great-ellingham-will.md</code>. Source ID: <code>familysearch-fulltext-search</code>. Older accounts: Daniel Gurney, <em>Record</em> (1848), pedigree p. 287, "will proved 1623"; Pease/Pennyghael Gurney genealogy (Charles E. G. Pease, 2016, <a href="http://www.pennyghael.org.uk/Gurney.pdf">Gurney.pdf</a>), "died 23 Feb 1615"; the Catalogue of English Literary Manuscripts and Steven W. May, <em>Spenser Studies</em> 20 (2005), 183â€“223 (DOI 10.1086/SPSv20p183), life dates 1549â€“1616. The registered will supersedes these: Henry was alive on 1 May 1621, and the Norwich registers for 1615â€“1620 contain no Gurney will. <a class="citation-back" href="#ref-2">â†©</a></li>
```

**Operation 03f.** Replace:

```
He was, the family record insists, the last member of the Gurney family to be born a Roman Catholic. He grew up amid the religious convulsions of the late 1550s â€” Mary I's return to Rome, then Elizabeth's restoration of the reformed church in 1559 â€” and as an adult conformed to the Church of England, though his eventual will (dated 1614) would warn his sons against holding "fantastical opinions," a phrase aimed in both directions.
```

with:

```
He was, the family record insists, the last member of the Gurney family to be born a Roman Catholic. He grew up amid the religious convulsions of the late 1550s â€” Mary I's return to Rome, then Elizabeth's restoration of the reformed church in 1559 â€” and as an adult conformed to the Church of England, though a will he made in 1614 warned his sons against holding "fantastical opinions," a phrase aimed in both directions.
```

**Operation 03g.** Replace:

```
His eldest son Thomas (sometimes called Thomas III) married Martha Lewknor of Denham, Suffolk, but died in 1614 â€” a year before his father â€” leaving Henry's eventual succession to fall on Henry's grandson Edward Gournay (b. 1608).
```

with:

```
His eldest son Thomas (sometimes called Thomas III) married Martha Lewknor of Denham, Suffolk, but died in his father's lifetime â€” the family genealogies say in 1614, though Henry's last will still named him in 1621 â€” leaving Henry's eventual succession to fall on Henry's grandson Edward Gournay (b. 1608).
```

**Operation 03h.** Replace:

```
Henry died in 1615 or early 1616. The Pease/Pennyghael genealogy gives 23 February 1615; modern catalogue records (the Catalogue of English Literary Manuscripts at the Folger, and Steven May 2005) give 1616; his will was not proved until 1623.
```

with:

```
Henry died between May 1621 and October 1623, in his mid-seventies. On 1 May 1621 he made his last will â€” revoking an earlier one of 1614 â€” providing Â£200 marriage portions for his two still-unmarried daughters, a Â£10 loan-stock for the poor of Great Ellingham to be lent out by the churchwardens in small sums, his silver-and-gilt basin and ewer to his eldest son, and all his Latin books to his sixth son Francis, the London Merchant Taylor. The will was proved at Norwich on 23 October 1623, his son Anthony administering. Older accounts placed his death in 1615 or 1616, an error the surviving will corrects.
```

**Operation 03i** (Thomas row). Replace:

```
      <td>Thomas Gurney III</td>
      <td>b. 1572 â€“ d. 1614</td>
      <td>Eldest son. Baptised 15 May 1572 at West Barsham. Married Martha Lewknor of Denham, Suffolk. Died <em>vita patris</em>. His son Edward Gournay (b. 1608) eventually succeeded Henry as heir of West Barsham and Great Ellingham; Edward died in August 1641 and is commemorated by a Latin chancel monument at West Barsham church. <sup class="fn"><a href="#n12" id="ref-12">12</a></sup><sup class="fn"><a href="#n19" id="ref-19">19</a></sup></td>    </tr>
```

with:

```
      <td>Thomas Gurney III</td>
      <td>b. 1572 â€“ d. before October 1623</td>
      <td>Eldest son. Baptised 15 May 1572 at West Barsham. Married Martha Lewknor of Denham, Suffolk. Died <em>vita patris</em>; the family genealogies date his death 1614, but his father's last will of May 1621 still names him eldest son, so the records conflict. His son Edward Gournay (b. 1608) eventually succeeded Henry as heir of West Barsham and Great Ellingham; Edward died in August 1641 and is commemorated by a Latin chancel monument at West Barsham church. <sup class="fn"><a href="#n12" id="ref-12">12</a></sup><sup class="fn"><a href="#n19" id="ref-19">19</a></sup><sup class="fn"><a href="#n2" id="ref-2b">2</a></sup></td>    </tr>
```

**Operation 03j** (Anthony row). Replace:

```
      <td>Anthony Gurney</td>
      <td>b. 18 September 1581</td>
      <td>Twin with Francis. Died <em>vita patris</em>. <sup class="fn"><a href="#n15" id="ref-15b">15</a></sup></td>
```

with:

```
      <td>Anthony Gurney</td>
      <td>b. 18 September 1581</td>
      <td>Twin with Francis. Outlived his father: the Norwich court committed administration of Henry's estate to "Anthony Gurnay, natural and lawful son" in October 1623, correcting an older account that he died in his father's lifetime. <sup class="fn"><a href="#n15" id="ref-15b">15</a></sup><sup class="fn"><a href="#n2" id="ref-2c">2</a></sup></td>
```

**Operation 03k** (further-children row â€” Anne and Abigail). Replace:

```
      <td>The Pease/Pennyghael genealogy lists Leonard, Margaret (later wife of Henry Davy of Great Ellingham, in whose female line Great Ellingham eventually descended), Abigail, Anne, Amy, and Mary. Total reaches 12 surviving children consistent with the epitaph verse. <sup class="fn"><a href="#n17" id="ref-17">17</a></sup></td>
```

with:

```
      <td>The Pease/Pennyghael genealogy lists Leonard, Margaret (later wife of Henry Davy of Great Ellingham, in whose female line Great Ellingham eventually descended), Abigail, Anne, Amy, and Mary. Anne and Abigail were still unmarried in May 1621, when their father's will gave each a Â£200 marriage portion and Â£20 a year until then. Total reaches 12 surviving children consistent with the epitaph verse. <sup class="fn"><a href="#n17" id="ref-17">17</a></sup><sup class="fn"><a href="#n2" id="ref-2d">2</a></sup></td>
```

**Operation 03l** (timeline). Replace:

```
      <tr><td>1614</td><td>Eldest son Thomas III dies <em>vita patris</em>. Henry's will dated this year.</td></tr>
      <tr><td>1615 / 1616</td><td>Dies, aged ~67.</td></tr>
      <tr><td>1623</td><td>Will proved.</td></tr>
```

with:

```
      <tr><td>1614</td><td>Makes a will directing burial beside Ellen at West Barsham (later revoked). The family genealogies also place eldest son Thomas III's death this year.</td></tr>
      <tr><td>1 May 1621</td><td>Makes his last will, revoking all former wills.</td></tr>
      <tr><td>by 23 Oct 1623</td><td>Dies, aged ~72â€“74; will proved at Norwich, son Anthony administering.</td></tr>
```

## Item 04 (promote) â€” `data/ancestors.json`: G15 record

**Target:** `data/ancestors.json`, record `ancestor-g15-henry-gurney`

**Operation 04a â€” str_replace.** Replace:

```
    "dates": "21 Jan. 1548/9 (OS) â€” d. 1615/16 (will proved 1623)",
```

with:

```
    "dates": "21 Jan. 1548/9 (OS) â€” d. 1621Ã—1623 (will 1 May 1621, proved Norwich 23 Oct. 1623)",
```

**Operation 04b â€” str_replace** (within the `notables` string; verbatim including escapes). Replace:

```
Three of his twelve surviving children shaped onward history: Thomas III (heir, d. 1614 vita patris); Edmund (Cambridge-educated Puritan divine, Rector of Edgefield 1614 then Harpley 1620â€“1648, with his own *Dictionary of National Biography* entry); and Francis (G14), apprenticed to a London Merchant Taylor and the bridge to the family's American descent. Will of 1614 directed burial \"next to my wife there\" at All Saints, West Barsham (corroborating Pease/Pennyghael's record of Ellen Blennerhasset's burial there) and warned his sons against holding \"fantasticall or erroneous opinions, so adjudged by our Bishop or civill Lawes.\"
```

with:

```
Three of his twelve surviving children shaped onward history: Thomas III (heir, d. vita patris â€” the genealogies say 1614, though Henry's 1621 will still names him); Edmund (Cambridge-educated Puritan divine, Rector of Edgefield 1614 then Harpley 1620â€“1648, with his own *Dictionary of National Biography* entry); and Francis (G14), apprenticed to a London Merchant Taylor and the bridge to the family's American descent â€” to whom Henry's last will left \"all my bookes in Latyne.\" An earlier will of 1614 directed burial \"next to my wife there\" at All Saints, West Barsham (corroborating Pease/Pennyghael's record of Ellen Blennerhasset's burial there) and warned his sons against holding \"fantasticall or erroneous opinions, so adjudged by our Bishop or civill Lawes.\" His last will (1 May 1621, proved Norwich 23 Oct. 1623, administration to son Anthony) left burial to his executor's discretion and endowed a Â£10 poor-stock for Great Ellingham.
```

*Phase-2 check:* JSON validity after edit (`python -c "import json;json.load(open('data/ancestors.json',encoding='utf-8'))"`), then regenerate indexes per `data-json.md` if the tooling flags drift.

## Item 05 (promote) â€” G13 companion: the G13 bearing only

**Target:** `research/people/g13-john-gurney-fact-sheet.research.md`

**Operation â€” str_replace.** Replace:

```
### 2026-06-11 session â€” seventh pass: expert image reads land, Tyng indenture dated, Quinapaug chain, Providence resolved, the Waveney network
```

with:

```
### The grandfather and great-uncle wills (L-111/L-6) â€” searched for New England kin; none named

The two English wills most likely to name the emigrant or his children were Henry Gurney G15's (d. by 1623) and Edmund the Divine's (d. 1648). Henry's will is now found and expert-read (made 1 May 1621, proved Norwich 23 October 1623 â€” full treatment on the [G15 companion](https://github.com/allengurney/gurney-genealogy/blob/main/research/people/g15-henry-gurney-fact-sheet.research.md)): it names Francis G14 among the portioned children and leaves him "all my bookes in Latyne," but **names no grandchild and no New England kin** â€” a clean negative for direct G13 evidence, while independently confirming Francis's standing in the armigerous family. Edmund's will is not in the Norwich Consistory registers for 1643â€“1651 (coverage-confirmed sweeps; the registers then gap until 1660), so the remaining target is a Prerogative Court of Canterbury probate 1648â€“1659. Register-to-film map and sweep log: [`research/topics/norwich-consistory-wills-register-map.md`](https://github.com/allengurney/gurney-genealogy/blob/main/research/topics/norwich-consistory-wills-register-map.md).[^l111-outcome-2026-06]

[^l111-outcome-2026-06]: Henry's will: NCC registered copy wills 1621â€“1623 (DGS 008470484), images 594â€“596; expert transcription `sources/corpus_supplement/paleo-2026-06-packet-10-henry-gurnay-great-ellingham-will.md`. Edmund negatives: film-scoped `Gurn*`/`Gourn*`/`+Harpley` queries against DGS 008402405 and 007904832, 2026-06-11, zero results, coverage confirmed by `+wife` probes. Source ID: `familysearch-fulltext-search`.

### 2026-06-11 session â€” seventh pass: expert image reads land, Tyng indenture dated, Quinapaug chain, Providence resolved, the Waveney network
```

## Item 06 (promote) â€” Earsham subject file: probate clause; the Adams kin map; Bungay read; court-book sweep

**Target:** `research/people/john-gurney-earsham-will-1638.md`

**Operation 06a â€” str_replace.** Replace:

```
The witness list and probate clause sit at the top of the next register image (456), not yet pulled â€” the probate date and court (presumably Norwich Consistory) are an open one-image pull.
```

with:

```
The will was **proved at Norwich 26 December 1639**, before Mr. R. Gamon, clerk, surrogate of Clement Corbett, doctor of laws (chancellor of Norwich diocese), administration committed to the executors named in the will â€” so the testator died between August 1638 and late 1639. It was sealed, subscribed, and published in the presence of Edw[ard] Calvert, Christopher Jay (by mark), and Jacob Bland (by mark).[^earsham-probate-1639]

[^earsham-probate-1639]: Probate clause and witness list at the top of image 456 of film 008076858, [ark:/61903/3:1:3Q9M-CSN6-3W3D](https://www.familysearch.org/ark:/61903/3:1:3Q9M-CSN6-3W3D); full-resolution image read 2026-06-11 ("Probatum fuit â€¦ apud Norwicum â€¦ xxvj die Decembris Anno Domini 1639"); working transcription appended to the corpus-supplement file. Source ID: `familysearch-fulltext-search`.
```

**Operation 06b â€” str_replace.** Replace:

```
- **Sarah Gurney of Bungay â€” nuncupative will, June 1710.** A memorandum in the Norwich wills register: "on Sunday the fourth day of June â€¦ 1710, we whose names are hereunder subscribed being at the house of **Lyon Gurney of the parish of St Peter [Parmentergate] in the City of Norwich**, where was **Sarah Gurney his mother**, who had been at his house about a month before, to look after her said Son in the time of his wifes sickness, but her habitation or dwelling was at **Bungay in the County of Suff[olk]** â€¦ the said Sarah Gurney complaining at the same time that she was sickâ€¦" â€” Sarah of Bungay (directly across the Waveney from Earsham) made her deathbed will at her son Lyon's Norwich house.[^sarah-bungay-1710]
```

with:

```
- **Sarah Gurney of Bungay â€” nuncupative will, June 1710 (image-read in full).** On Sunday 4 June 1710, at the house of **Lyon Gurney of the parish of St Peter per Mountergate [Parmentergate] in the City of Norwich**, his mother **Sarah Gurney** â€” "her habitation or dwelling was att Bungay in the County of Suffolk" â€” declared her will before witnesses. She had been at Lyon's house about a month, nursing her son **and his wife** through a sickness, intended to return to Bungay shortly, and died of that same sickness about fifteen days later (â‰ˆ 19 June 1710), "of perfect mind & memory." Her declared will: her son Lyon to have all her moveable goods and what money was due to her, "for to bury her"; "as for her daughter **Mary**, she had had enough already, So that her son Syon [Lyon] should have what she left at her death." Witnesses subscribed 22 June 1710: Thomas Loades, a second Loades by mark, Rachel Kingston; **proved at Norwich the same day, 22 June 1710**, before Peter Burgess, surrogate of Thomas Tanner, S.T.P. [the antiquary, then chancellor of the diocese]. Full working transcription in [`sources/corpus_supplement/ncc-will-1710-sarah-gurney-bungay-nuncupative-transcription.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/ncc-will-1710-sarah-gurney-bungay-nuncupative-transcription.md).[^sarah-bungay-1710]
```

**Operation 06c â€” str_replace.** Replace:

```
- **A 1690s Waveney-Suffolk will names "my Sister Sarah Gurney['s] children."** A testator with son-in-law Richard Nelson and lands in "Bar[s]ham, Ship Meadow and [Mettingham?] in the County of Suff" (the Suffolk Barsham by Beccles, six miles from Earsham) leaves "to **John Gurney, Thomas [& L?i]on Gurney and to Mary Farrow, my Sister Sarah Gurney['s] children**, five pounds a piece," among Woolnough kin. Most plausibly the same Sarah â€” her children John, Thomas, L[yo]n(?) Gurney, and Mary (married Farrow).[^barsham-will-1690s]
```

with:

```
- **Sarah Gurney was a sister of James Adams of Bungay, merchant â€” his will (31 January 1692/3) maps her family.** Expert reading of the register pages resolved the 1690s will naming "my Sister Sarah Gurney['s] children": the testator is **James Adams of Bungay in the County of Suffolk, merchant**, will dated "the one and thirtieth day of January in the fourth yeare of the raigne of â€¦ William and Mary â€¦ Anno Domini 1692" [1692/3]. He gives "unto **John Gurney, Thomas Gurney, Lyon Gurney, and Mary Farrow, my sister Sarah Gurney's children**, five pounds apiece"; and "unto **my sister Sarah Gurney** the summe of six pounds by the yeare during her naturall life," charged on his estate at **Mettingham** with a right of entry if unpaid. His lands at **Barsham, Shipmeadow, and Mettingham** (occupiers John Deveson and John Cole) go to his son-in-law **Richard Nelson** and daughter **Margaret** his wife and the heirs of her body, remainder to John Adams son of his brother Thomas Adams; Nelson (sole executor) collects the rents for a term to pay the legacies, which include Â£5 apiece to **James Woolnough's children** (Robert, Mary, Elizabeth, Lawrence) and small sums to his brother Henry Adams's children; Â£5 to the poor of Bungay; gold, plate, and linen between daughters Margaret Nelson and Elizabeth Baker. Sarah Gurney was therefore â€” if "sister" is blood usage â€” **nÃ©e Adams of Bungay**, with an annuity from her brother from 1693 and a deathbed estate of moveables only in 1710; her children John, Thomas, Lyon, and Mary (married Farrow) match the 1710 memorandum's son Lyon and portioned daughter Mary. (The will registered immediately before Adams's, Mary Scamler/Scambler of Norwich, widow, 22 January 1688/9 â€” initially conflated with this one â€” proves unrelated: her will concerns Smith and Scambler kin and sons "beyond the seas.")[^adams-will-1692]
```

**Operation 06d â€” str_replace.** Replace:

```
- **Earsham court records 1710â€“1818 are digitised and carry Lyon Gurney entries** (two result cards under the exact-name probe; the film also has an 1841â€“83 successor volume) â€” the family's manorial trail at Earsham itself continues a century beyond the 1638 will. Unswept; lead.[^earsham-court-cards]
```

with:

```
- **The Earsham court book 1710â€“1818 is swept (DGS 004389278): Lyon Gurney held Earsham copyhold from c. 1719, and the family's land memory runs to 1811.** Latin court entries of 1719â€“1734 carry Lyon Gurney's active tenure (machine transcripts garble the rare forename as "my son"/"Sion"/"Simon"/"Leon"), including a close called **Broadland** and land on the way toward Ditchingham; "Lands late of Lyon Gurney" abuttal recitals run 1744â€“1811; a "Land late of **Susan Gurney**" recital appears in 1748; and several entries recite "one Acre of Copyhold Land of the **Tenement Gurneys** heretofore of John Plough [Clough?] called Hallsty" with recited years reaching back to 1642â€“1654 â€” a possible documentary chain from the eighteenth-century holdings to the 1638 testator's messuages. (The same physical film carries Docking and Diss court records, whose Gurney cards are the nineteenthâ€“twentieth-century Norwich banking family as estate parties â€” not this family.) Image-read targets: the 1719â€“24 Lyon admissions and the Tenement-Gurneys recital.[^earsham-court-cards]
```

**Operation 06e â€” str_replace.** Replace:

```
Reading: the 1638 testator's brother **Lyon** gave the family a recurring name; two generations later a Sarah Gurney (widow, evidently of a John or Thomas of this family) lived at Bungay with children John, Thomas, Lyon(?), and Mary, and her son **Lyon Gurney lived in St Peter Parmentergate, Norwich** â€” the laceweaver Francis B's own parish (AGENTS.md Â§6 standing fact #4).
```

with:

```
Reading: the 1638 testator's brother **Lyon** gave the family a recurring name; two generations later Sarah Gurney â€” sister of James Adams of Bungay, merchant, so most plausibly **nÃ©e Adams**, and widow of an unidentified Gurney of this family (the 1638 testator's son John, b. after c. 1624, is chronologically exact and the natural candidate) â€” lived at Bungay with children John, Thomas, Lyon, and Mary (Farrow), and her son **Lyon Gurney lived in St Peter Parmentergate, Norwich** â€” the laceweaver Francis B's own parish (AGENTS.md Â§6 standing fact #4).
```

**Operation 06f â€” str_replace** (footnotes). Replace:

```
[^sarah-bungay-1710]: Nuncupative-will memorandum of Sarah Gurney of Bungay, Suffolk, made at the house of her son Lyon Gurney, St Peter Parmentergate, Norwich, Sunday 4 June 1710; "Norwich, Norfolk, England. Wills 1709â€“1711" (FamilySearch), image 450, [ark:/61903/3:1:3Q9M-CSND-1SKS-C](https://www.familysearch.org/ark:/61903/3:1:3Q9M-CSND-1SKS-C?view=fullText). Machine transcript; image read pending. Source ID: `familysearch-fulltext-search`.
[^barsham-will-1690s]: Will register "Cambridgeshire. Wills 1691â€“1698 | Suffolk. Wills 1691â€“1698 | Norfolk. Wills 1691â€“1698" (FamilySearch), image 202, [ark:/61903/3:1:3Q9M-C39Z-BJML](https://www.familysearch.org/ark:/61903/3:1:3Q9M-C39Z-BJML?view=fullText): "â€¦to pay â€¦ unto Thomas & John Adams Sons of my Bro Adams five Pounds a peice and to John Gurney Thomas [& L?i]on Gurney and to Mary Farrow my Sister Sarah Gurney['s] children five pounds a pice and to my Brother in Law James Woolnough's Childrenâ€¦" Machine transcript; the testator's name is on a neighbouring image â€” identification pending. Source ID: `familysearch-fulltext-search`.
[^earsham-court-cards]: "Earsham, Norfolk, England. Court Records 1710â€“1818" (FamilySearch), result cards at [ark:/61903/3:1:S3HY-6XP3-C89](https://www.familysearch.org/ark:/61903/3:1:S3HY-6XP3-C89?view=fullText) and [ark:/61903/3:1:S3HY-6XP3-HMJ](https://www.familysearch.org/ark:/61903/3:1:S3HY-6XP3-HMJ?view=fullText), surfaced by the exact-phrase probe "Lyon Gurney" 2026-06-11; film not yet swept. Source ID: `familysearch-fulltext-search`.
```

with:

```
[^sarah-bungay-1710]: Nuncupative-will memorandum of Sarah Gurney of Bungay, Suffolk, "Norwich. Wills 1709â€“1711" (NCC registered copy wills vol. 147, FamilySearch DGS 008076925), image 450, fo. 420, margin "Sara Gurney | 97," [ark:/61903/3:1:3Q9M-CSND-1SKS-C](https://www.familysearch.org/ark:/61903/3:1:3Q9M-CSND-1SKS-C?view=fullText); full-resolution image read 2026-06-11; working transcription in the corpus supplement linked in the body. Source ID: `familysearch-fulltext-search`.
[^adams-will-1692]: Will of James Adams of Bungay, Suffolk, merchant, 31 Jan. 1692/3, NCC registered copy wills vols. 142â€“143 (1691â€“1698, FamilySearch DGS 008472233), beginning image 201 ([ark:/61903/3:1:3Q9M-C39Z-BJQV](https://www.familysearch.org/ark:/61903/3:1:3Q9M-C39Z-BJQV?view=fullText)) and continuing on image 202 ([ark:/61903/3:1:3Q9M-C39Z-BJML](https://www.familysearch.org/ark:/61903/3:1:3Q9M-C39Z-BJML?view=fullText)); expert paleographic reading 2026-06-11, `sources/corpus_supplement/paleo-2026-06-packet-11-mary-scamler-and-james-adams-waveney-wills.md` (which also establishes the page boundary against the adjacent Mary Scamler/Scambler will, images 199â€“201, and notes Adams's probate clause lies beyond the staged images â€” one remaining pull). Source ID: `familysearch-fulltext-search`.
[^earsham-court-cards]: "Earsham, Norfolk, England. Court Records 1710â€“1818" (FamilySearch DGS 004389278, item 17 of 18 on the film), `Gurn* Gourn*` film-scoped sweep of 48 cards 2026-06-11 (Earsham subset ~20 cards; the Docking and Diss cards on the same film are the banking Gurneys). Key arks: 1719 Lyon entries [ark:/61903/3:1:S3HY-6XP3-H4R](https://www.familysearch.org/ark:/61903/3:1:S3HY-6XP3-H4R?view=fullText); 1720â€“24 Latin entries [ark:/61903/3:1:S3HY-6XP3-ZS6](https://www.familysearch.org/ark:/61903/3:1:S3HY-6XP3-ZS6?view=fullText) and [ark:/61903/3:1:S3HY-6XPS-TY6](https://www.familysearch.org/ark:/61903/3:1:S3HY-6XPS-TY6?view=fullText); "Tenement Gurneys â€¦ Hallsty" recitals [ark:/61903/3:1:S3HY-6XPS-TZT](https://www.familysearch.org/ark:/61903/3:1:S3HY-6XPS-TZT?view=fullText); "late of Susan Gurney" 1748 [ark:/61903/3:1:S3HY-6XPS-YVW](https://www.familysearch.org/ark:/61903/3:1:S3HY-6XPS-YVW?view=fullText); abuttal recitals to 1811 [ark:/61903/3:1:S3HY-6XP3-C89](https://www.familysearch.org/ark:/61903/3:1:S3HY-6XP3-C89?view=fullText). Source ID: `familysearch-fulltext-search`.
```

**Operation 06g â€” str_replace** (open questions). Replace:

```
1. Probate clause and witnesses â€” image 456 of film 008076858, one pull. (Available online.)
2. **Lyon Gurney trace â€” substantially advanced** (see the Waveney-network section above): Sarah Gurney of Bungay's 1710 nuncupative will at her son Lyon's Norwich (Parmentergate) house; a 1690s Suffolk-Barsham will naming sister Sarah Gurney's children; Earsham court records 1710â€“1818 with Lyon Gurney entries. Remaining: image-read the 1710 memorandum, identify the 1690s testator, sweep the Earsham court film. (All available online â€” arks in the footnotes.)
```

with:

```
1. Probate clause and witnesses â€” done: proved Norwich 26 December 1639 (see the family section above).
2. **Lyon Gurney trace** â€” the 1710 memorandum is read, the 1690s testator is identified (James Adams of Bungay; Sarah Gurney his sister), and the Earsham court book is swept. Remaining: which Gurney was Sarah's husband (the 1638 testator's son John, b. after c. 1624, is the natural candidate â€” test against Bungay/Earsham parish registers); James Adams's probate clause (the page after image 202); image reads of the 1719â€“24 Earsham Lyon admissions and the Tenement-Gurneys/Hallsty recital. (All available online â€” arks in the footnotes.)
```

## Item 07 (promote) â€” new corpus-supplement file: Sarah Gurney of Bungay nuncupative will (1710), working transcription

**Target (new file write):** `sources/corpus_supplement/ncc-will-1710-sarah-gurney-bungay-nuncupative-transcription.md`

```
# Nuncupative will of Sarah Gurney of Bungay, Suffolk â€” declared 4 June 1710, proved Norwich 22 June 1710 (working transcription)

Registered copy in "Norwich. Wills 1709â€“1711" (Norwich Consistory Court registered copy wills vol. 147, FamilySearch DGS 008076925), image 450, register folio 420, margin "Sara Gurney | 97" ([ark:/61903/3:1:3Q9M-CSND-1SKS-C](https://www.familysearch.org/ark:/61903/3:1:3Q9M-CSND-1SKS-C?view=fullText)). Working transcription from the full-resolution image, read 2026-06-11. Square brackets mark uncertain readings or supplied letters. Source ID: `familysearch-fulltext-search`.

---

## Working transcription

> **Memorand[um]** That on Sunday the fourth day of June in the year of our Lord Christ one thousand seven hundred & tenn, wee whose Names are hereunder Subscribed being att the house of **Syon [Lyon] Gurney of the parish of St Peter per Mountergate in the City of Norwich** where was **Sara Gurney his Mother** who had been at his house about a Month before, to look after her said Son in the time of his & wife's Sickness but her habitation or dwelling was att **Bungay in the County of Suffolk** to w[hi]ch place she did speak of returning shortly after, the s[ai]d Sara Gurney complaining at the same time that she was sick (of w[hi]ch sickness she dyed about fifteen dayes after but was of p[er]fect mind & memory & well knew what she said or did) did voluntarily of her own accord declare her will & mind to be in these words following or in words tending to the same sense & effect, that her son **Syon Gurney** should have all her moveable goods & what money was due to her, for to bury her, as for her daughter **Mary**, she had had enough already, So that her son Syon should have what she left at her death. In Witness whereof we have hereunto set our hands the two & twentieth day of June in the year of our Lord one thousand seven hundred & ten aforesaid. **Thomas Loades**. the marke of [Persa?] **Loades**. [the marke of] **Rachel R Kingston**.
>
> Probatum fuit h[uius]mo[d]i Test[amentu]m nuncupativ[um] ap[u]d Norvic[um] vicesimo s[e]c[un]do die mens[is] Junij A[nn]o D[omi]ni 1710, jurat[is] Thoma Loades, [Persa?] Loades et Rachel Kingston testium â€¦ subscript[is], coram discreto viro **Petro Burgess** â€¦ Surrogato â€¦ venerabilis viri **ThomÃ¦ Tanner S.T.P.** â€¦ Offic[ialis] pr[incipa]lis â€¦ constitut[o]. At â€¦ [administra]tio â€¦ bonor[um] â€¦ [final lines partly unread].

## Reading notes

- **Date of death.** Sarah declared the will 4 June 1710 and "dyed about fifteen dayes after" â€” â‰ˆ 19 June 1710; the witnesses subscribed and probate passed on 22 June 1710. Burial place untraced (Bungay or Norwich).
- **"Syon" = Lyon.** The forename is written Syon/Sion in this register; the family's recurring rare forename (the 1638 Earsham testator's brother) makes Lyon the secure normalization. Machine transcripts garble it as "my son"/"Simon"/"Leon."
- **The parish.** "St Peter per Mountergate" â€” the register's spelling of St Peter Parmentergate, Norwich.
- **Daughter Mary** "had had enough already" â€” consistent with Mary Farrow, married with a settled portion; James Adams's 1692/3 will groups "Mary Farrow" with "my sister Sarah Gurney's children."
- The second witness's forename (machine "Persa"; a Loades household member) remains an open glance for any future expert pass.
```

## Item 08 (promote) â€” Earsham working transcription: append the probate clause

**Target:** `sources/corpus_supplement/ncc-will-1638-john-gurney-earsham-working-transcription.md`

**Operation 08a â€” str_replace.** Replace:

```
Working transcription from the full-resolution page images (downloaded 2026-06-10; held at `sources/media/ncc-will-1638-john-gurney-earsham/_local/`), read at crop-and-enhance level. Square brackets mark uncertain readings or supplied letters; the register hand is a clear secretary hand but the second leaf is faintly photographed. The witness list and probate clause fall at the top of image 456, not yet pulled. Source ID: `familysearch-fulltext-search`.
```

with:

```
Working transcription from the full-resolution page images (downloaded 2026-06-10; held at `sources/media/ncc-will-1638-john-gurney-earsham/_local/`), read at crop-and-enhance level. Square brackets mark uncertain readings or supplied letters; the register hand is a clear secretary hand but the second leaf is faintly photographed. The witness list and probate clause (top of image 456, [ark:/61903/3:1:3Q9M-CSN6-3W3D](https://www.familysearch.org/ark:/61903/3:1:3Q9M-CSN6-3W3D)) were pulled and read 2026-06-11 â€” transcribed below. Source ID: `familysearch-fulltext-search`.
```

**Operation 08b â€” str_replace.** Replace:

```
> Item I doe [constitute] ordaine & make & [a]ppoint my well beloved **Broth[er] Lyon Gurney & my Broth[er] in Law John Youngman of S[ain]t Andrews** Executors of this my last will & testam[ent]. I doe give... [text continues at the top of image 456 â€” witness list and probate clause not yet pulled].
```

with:

```
> Item I doe [constitute] ordaine & make & [a]ppoint my well beloved **Broth[er] Lyon Gurney & my Broth[er] in Law John Youngman of S[ain]t Andrews** Executors of this my last will & testam[ent]. I doe give... [residue clause continues at the top of image 456]
>
> Sealed Subscribed & published in [the] p[rese]nce of **Edw: Calvert**; Sign[um] **Christopher Jay**; Sign[um] **Jacobi Bland**.
>
> **Probatum** fuit h[uius]mo[di] Testamentu[m] apud Norwicu[m] cora[m] ven[era]b[i]li viro m[agist]ro R[ichardo?] **Gamon** Cl[er]ico Surro[gato] venerabilis viri **Clementis Corbett leg[um] d[o]ctoris** â€¦ Offic[ialis] principalis â€¦ **xxvjÂ° die Decembris An[no] Dom[ini] 1639**; Comissa[que] fuit ad[ministra]tio bonor[um] et[c] Executoribus in [huius]mo[di] Testamento no[m]i[n]at[is] â€¦ jurat[is] â€¦ salvo [jure cujuscunque].
```

**Operation 08c â€” str_replace.** Replace:

```
- **The register.** The film bundles Cambridgeshire, Suffolk, and Norfolk wills 1638â€“1639 â€” consistent with a Norwich Consistory Court register volume (NCC jurisdiction spanned Norfolk, Suffolk, and part of Cambridgeshire). The probate clause (image 456) will identify the court and probate date.
```

with:

```
- **The register.** The film bundles Cambridgeshire, Suffolk, and Norfolk wills 1638â€“1639 â€” a Norwich Consistory Court register volume (NCC registered copy wills vol. 131 per the FamilySearch catalog film list; NCC jurisdiction spanned Norfolk, Suffolk, and part of Cambridgeshire). The probate clause confirms the court: proved at Norwich, 26 December 1639, before the chancellor's surrogate â€” sixteen months after the will's making, so the testator died between August 1638 and late 1639.
```

## Item 09 (promote) â€” paleography batch 2 disposition (file operations)

Per the disposition convention in `.claude/skills/familysearch-fulltext-research/SKILL.md` Â§4. Execute as literal file operations:

1. Copy `sources/intake/paleography-staging/packet-10-henry-gurnay-great-ellingham-will.md` â†’ `sources/corpus_supplement/paleo-2026-06-packet-10-henry-gurnay-great-ellingham-will.md` (verbatim).
2. Copy `sources/intake/paleography-staging/packet-11-mary-scamler-and-james-adams-waveney-wills.md` â†’ `sources/corpus_supplement/paleo-2026-06-packet-11-mary-scamler-and-james-adams-waveney-wills.md` (verbatim).
3. Create directory `sources/media/ncc-wills-registers/_local/` and move into it the seven master images from `sources/intake/paleography-staging/images/`: `ncc-wills-vol116-118-1621-1623-img594.jpg`, `â€¦img595.jpg`, `â€¦img596.jpg`, `ncc-wills-1691-1698-img199-mary-widow-norwich.jpg`, `â€¦img200-mary-scamler-will.jpg`, `â€¦img201-mary-scamler-will.jpg`, `â€¦img202-gurney-legacies.jpg`. Also move `ncc-wills-1709-1711-img450-sarah-gurney-bungay-nuncupative.jpg` into the same `_local/`. Move `ncc-wills-1638-1639-img456-earsham-probate-clause.jpg` â†’ `sources/media/ncc-will-1638-john-gurney-earsham/_local/` (alongside the existing masters for that will).
4. **New file write:** `sources/media/ncc-wills-registers/README.md` with content:

```
# Norwich Consistory Court will registers â€” working-reference images

Full-resolution register-page images retrieved from FamilySearch (das/v2 downloads). Masters live in `_local/` (kept off GitHub per the media `_local` convention â€” FamilySearch terms; retrievable at the arks below).

| File (_local/) | Register | Image | Ark | Content |
|---|---|---|---|---|
| ncc-wills-vol116-118-1621-1623-img594.jpg | NCC regd. wills 1621â€“23 (DGS 008470484) | 594 | 3:1:3Q9M-C39Z-C39M-3 | Henry Gurnay G15 will, opening |
| ncc-wills-vol116-118-1621-1623-img595.jpg | same | 595 | 3:1:3Q9M-C39Z-C3MP-N | will body |
| ncc-wills-vol116-118-1621-1623-img596.jpg | same | 596 | 3:1:3Q9M-C39Z-C3MJ-W | probate clause, 23 Oct 1623 |
| ncc-wills-1691-1698-img199-mary-widow-norwich.jpg | NCC regd. wills 1691â€“98 (DGS 008472233) | 199 | 3:1:3Q9M-C39Z-BJWR | Mary Scamler will, opening |
| ncc-wills-1691-1698-img200-mary-scamler-will.jpg | same | 200 | 3:1:3Q9M-C39Z-BN13 | Scamler will body |
| ncc-wills-1691-1698-img201-mary-scamler-will.jpg | same | 201 | 3:1:3Q9M-C39Z-BJQV | Scamler end/probate; James Adams will opening |
| ncc-wills-1691-1698-img202-gurney-legacies.jpg | same | 202 | 3:1:3Q9M-C39Z-BJML | Adams will: Gurney legacies, Sarah Gurney annuity |
| ncc-wills-1709-1711-img450-sarah-gurney-bungay-nuncupative.jpg | NCC regd. wills 1709â€“11 (DGS 008076925) | 450 | 3:1:3Q9M-CSND-1SKS-C | Sarah Gurney of Bungay nuncupative will |

Transcriptions: `sources/corpus_supplement/paleo-2026-06-packet-10-â€¦` and `â€¦packet-11-â€¦`, plus `ncc-will-1710-sarah-gurney-bungay-nuncupative-transcription.md`. Register-series map: `research/topics/norwich-consistory-wills-register-map.md`.
```

5. Move the working-crop files (`_crop*.jpg` in `sources/intake/paleography-staging/images/` and the expert's `working-snippets/` folders) â†’ `sources/media/_local/paleo-2026-06-batch2-working-crops/` (derivative, regenerable).
6. Move `sources/intake/paleography-staging/README.md` â†’ `sources/intake/done/paleography-2026-06-batch2/README.md`.
7. Grep `paleography-staging` across the repo afterward and fix any remaining references to the moved files.

---

## Phase-2 sequencing note

Apply in order 01 â†’ 09 (Item 09's file moves last, after every reference that mentions the staging paths is in its final form). After application: validate `data/ancestors.json` parses; prepend the Done stamp; move this patchset to `sources/intake/done/`.

