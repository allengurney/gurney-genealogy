**Done:** 2026-06-04 19:37 PT

# v86 patchset — Rigler (1994) Nathan-4 entry (p. 182): foster-father parentage correction

Prepared: 2026-06-04
Phase: 1 (preparation)

Scope: Promote Jean Gurney Rigler's NATHAN GURNEY-4 entry (*The Gurney Family from Aaron to Zuinglius*, rev. ed. 1994, p. 182) — supplied as a page image, not previously in the repo — into the collateral foster-father layer at G9. The entry corrects Nathan's parentage, supplies his vital dates, and adds a tenth child. The source already exists in `data/sources.json` (`rigler-gurney-family-aaron-zuinglius-1994`); this batch extends the existing corpus transcription with the Nathan-4 entry and propagates the correction into the Nathan fact sheet, the Nathan research companion, the Benjamin G9 companion, the Abington/Whitman place file, and the Rigler validation scope. No new `sourceId`. No `data/sources.json` change (the corpus path is unchanged; the existing extract file is extended in place).

## Intake summary

The repo's Nathan material was built from Hobart (1866) plus the mill-founder mention inside Rigler's *Benjamin* entries; Rigler's own *Nathan-4* entry (p. 182) was never captured. That entry contradicts the parentage the repo published and does so explicitly:

> "NATHAN GURNEY-4 (Zachariah-3, Richard-2)… s/o Zachariah & Mary (Benson) Gurney. (Weymouth VR) Hobart's 'History of Abington' indicates that he was the son of John, but that is incorrect. The error probably arose from confused wording on some transactions regarding the estate of John Gurney-3 of Little Comfort. However, Weymouth Vital Records, Cyrus Nash (G-III:87, G-IV:8), & the Anna Gurney papers conclusively prove that Nathan was the son of Zachariah Gurney."

Findings:

1. **Parentage corrected.** Nathan was a son of **Zachariah Gurney and Mary Benson**, not of John Gurney of Little Comfort. John Gurney-3 (the mill founder) was Nathan's **uncle**, not his father; Rigler diagnoses the Hobart error as a misreading of John-3's estate transactions — corroborated within the same entry, where Nathan in 1727 *buys* a 1/6 share of John-3's estate from his cousin David Gurney of Easton (John-3's son).
2. **The relationship conclusion is unchanged.** Both Zachariah-3 and John-3 are sons of Richard Gurney (G12), so Nathan remains a **grandson of Richard (G12)** and a **first cousin of Benjamin Gurney (G10)**. Only the named father and the "his father founded the sawmill" framing change.
3. **Vital dates resolved.** Born **15 October 1702 at Weymouth**; died **17 April 1786 at Abington**; Sarah (Harden) Gurney died **1788**. This closes the fact sheet's "Born: about 1700–1704" bracket and "Died: not established," and Nathan-companion open question #1.
4. **Marriage upgraded and humanized.** The 12 May 1725 Abington marriage, previously dated only to the compiled *Neverending Hobby* site, is confirmed by Rigler; the church called Nathan to answer for fornication because the eldest child, **Martha, was born 24 July 1725** — just over two months after the wedding.
5. **Tenth child added; child marriages and one correction.** Rigler's child set adds **Martha (b. 24 July 1725, m. Zachariah Shaw)** ahead of Hobart's nine, supplies marriages (Rebecca m. Joseph Tirrell; Noah m. Ruth Pool; son Nathan m. Mary "Molly" Palmer; Silas m. Ruth Palmer; Sarah m. John Tirrell Jr.; Jacob m. Elizabeth Keene; John m. Sarah Norton; Lemuel m. Rebecca Derby; Elijah m. 1. Mary Copeland, 2. Widow House), explicitly corrects Hobart's "Jacob married a Reese" to **Elizabeth Keene ("not Reese")**, and dates Lemuel to **11 July 1730** (Hobart: October).
6. **Nathan was a housewright** who, with his brother Joseph, bought Abington land in 1720 and built a sawmill (agreed 1730, sold 1748), and in 1733 bought the ~107-acre Stowell tract near Plymouth St. (now Whitman) where he settled. The Old Abington and Bridgewater Gurneys descend from Nathan and his brothers Zachariah and Joseph.

Per the user's direction, the parentage **conflict is kept out of the fact-sheet body** — the body states the corrected parentage cleanly, and the Hobart-vs-Rigler friction lives only in the fact-sheet footnotes and in full in the research companion (the friction layer). Fact-sheet prose is kept crisp and plain-spoken per `.claude/rules/fact-sheets.md` (Plain-English contract, Read-as-if-written-all-at-once, Story-led-not-source-led).

## Source tracking

- **Existing sourceId:** `rigler-gurney-family-aaron-zuinglius-1994`. No new sourceId; no `data/sources.json` edit. The corpus transcription file `sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md` (already the entry's `corpusPath`) is **extended** with the Nathan-4 entry — operation **A1**. Sub-authorities Rigler cites in-line (Weymouth/Abington VR, Cyrus Nash, Anna Gurney papers, Plymouth deeds) are cited *through Rigler*, not minted separately.
- **Validation:** `sources/validations/rigler-gurney-family-aaron-zuinglius-1994.md` already exists; operation **A2** widens its scope and findings to record the p. 182 Nathan-4 entry. No new validation file (default-on satisfied by the existing one).
- **Media (Phase-2 / user follow-up, not an operation here):** the p. 182 page was supplied as a chat image, not a file in `sources/intake/new/`. When the page scan is in hand it should land in `sources/media/rigler-gurney-family-aaron-zuinglius-1994/_local/` (gitignored, copyright), mirroring the v84 handling, with the `_local/README.md` stub updated to add `rigler-1994-p182-nathan-4-zachariah.png`. Flagged for the user; no bytes are in the repo yet, so no media operation is written.

---

# Operations (literal)

Phase 2 applies each `str_replace` against the verbatim `old_string`, and each `new file write` with the full body. Footnote numbers are final; no `NEW`-style placeholders.

## A1 — `sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md`: insert the Nathan-4 entry

`str_replace`

old_string:
```
## The "second Benjamin" (collateral) — for the two-Benjamin disambiguation
```
new_string:
```
## NATHAN GURNEY-4 (Zachariah-3, Richard-2) (p. 182) — collateral; foster father of Benjamin-5 (G9)

NATHAN GURNEY-4 (Zachariah-3, Richard-2) was b. 15 Oct. 1702 Weymouth, Norfolk Co. MA, s/o Zachariah & Mary (Benson) Gurney. (Weymouth VR) Hobart's "History of Abington" indicates that he was the son of John, but that is incorrect. The error probably arose from confused wording on some transactions regarding the estate of John Gurney-3 of Little Comfort. However, Weymouth Vital Records, Cyrus Nash (G-III:87, G-IV:8), & the Anna Gurney papers conclusively prove that Nathan was the son of Zachariah Gurney.

He moved from Weymouth to Abington, Plymouth Co. MA & apparently the church called Nathan to acknowledge the sin of fornication, subsequently he & Sarah Harden were m. 12 May 1725 in Abington & daughter Martha was born not quite 3 months later. Sarah was b. 9 Apr. 1707 in Abington, d/o John and Mary (Littlefield) Harden, & sister of Jane Harden. (Abington VR)

On 20 Jan. 1720 he & his brother Joseph were 2 of 6 men who bought land in Abington, agreed in 1730 to build a saw mill and dam, & sold it in 1748. (Plym. Deeds 39:92, 31:194, 39:262, 38:223) On 14 Feb. 1727 he bought for £25 from his cousin David Gurney of Easton MA, the 1/6 part of the land or inheritance formerly belonging to David's deceased father, John-3 Gurney of Little Comfort. (Plym. Deed 37:85) He may possibly have bought an additional 1/6 share from his cousin John Gurney of CT. On 25 June 1733 he purchased for £428 a tract of about 107 acres from John Stowell on which he eventually settled; the tract contained part woodland, part swamp, and part meadow. (Plym. Deed 52:90) This farm adjoined that of his brother Joseph, near Plymouth St., now Whitman MA. He was called a housewright. It was from Nathan and his brothers, Zachariah & Joseph, that the Gurneys of Old Abington and Bridgewater descend.

He died 17 Apr. 1786 and Sarah died 1788, both in Abington MA. (Abington VR)

Children: (b. Abington MA VR)
- Martha, b. 24 July 1725, m. 4 Sept. 1745 Second Church of Christ, Weymouth MA, Zachariah Shaw (1722–1791), s/o Zachariah & Phebe (Pratt) Shaw.
- Rebecca, b. 4 Oct. 1727, m. 9 Jan. 1745/6 Abington, Joseph Tirrell.
- + Lemuel, b. 11 July 1730, m. Rebecca Derby.
- + Elijah, b. 15 May 1732 (Weymouth VR), m. 1. Mary Copeland, 2. Widow House.
- + Noah, b. 4 May 1735, m. Ruth Pool.
- + Nathan, b. 22 Nov. 1739, m. Mary "Molly" Palmer, sister of Ruth.
- + Silas, b. 14 June 1743, m. Ruth Palmer, sister of Molly.
- Sarah, b. 14 Mar. 1745/6, m. 27 Oct. 1763 John Tirrell, Jr., d. 1816.
- + Jacob, b. 13 Mar. 1748, m. Elizabeth Keene (not Reese).
- + John, b. 23 May 1751, m. Sarah Norton.

## The "second Benjamin" (collateral) — for the two-Benjamin disambiguation
```

## A2 — `sources/validations/rigler-gurney-family-aaron-zuinglius-1994.md`: widen scope to the Nathan-4 entry

### A2-1 — Source examined

`str_replace`

old_string:
```
Eight page scans of the 1994 revised-and-expanded edition (author's signed gift copy), held local-only (copyright) at `sources/media/rigler-gurney-family-aaron-zuinglius-1994/_local/`. Pages cover the direct-line entries Richard-2 (G12), Benjamin-3 (G11), Benjamin-4 (G10), and Benjamin-5 (G9), the title page, and adjacent fragments of the John Gurney-1 children list and the collateral "second Benjamin."
```
new_string:
```
Page scans of the 1994 revised-and-expanded edition (author's signed gift copy), held local-only (copyright) at `sources/media/rigler-gurney-family-aaron-zuinglius-1994/_local/`. Pages cover the direct-line entries Richard-2 (G12), Benjamin-3 (G11), Benjamin-4 (G10), and Benjamin-5 (G9), the title page, and adjacent fragments of the John Gurney-1 children list and the collateral "second Benjamin." A later supply added p. 182, the collateral NATHAN GURNEY-4 entry (foster father of Benjamin-5/G9); its page image was supplied via chat and is pending capture into `_local/`.
```

### A2-2 — Scope examined

`str_replace`

old_string:
```
The four direct-line entries (G9–G12) and the immediately adjacent children lists. Not examined: the bulk of the dictionary (other branches, Aaron-to-Zuinglius alphabetical descendants).
```
new_string:
```
The four direct-line entries (G9–G12) and the immediately adjacent children lists, plus the collateral Nathan-4 entry (p. 182). Not examined: the bulk of the dictionary (other branches, Aaron-to-Zuinglius alphabetical descendants).
```

### A2-3 — Findings

`str_replace`

old_string:
```
Promote. The four entries were transcribed to `sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md` and the substantive findings recorded on the G9–G12 research companions and fact sheets. Key resolutions: Richard's 1691 (not 1719) death; Mendon-massacre death reattributed off Richard's son; Rebecca Taylor and Rebecca Staples parentage; the Granny Gurney's Swamp source (Cyrus Nash); independent confirmation of G10 as father of G9; the aunt-upbringing (Nathan & Sarah Harden Gurney); and the two-Benjamin resolution.
```
new_string:
```
Promote. The four direct-line entries and the collateral Nathan-4 entry were transcribed to `sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md` and the substantive findings recorded on the G9–G12 research companions and fact sheets and the Nathan-Gurney foster-father layer. Key resolutions: Richard's 1691 (not 1719) death; Mendon-massacre death reattributed off Richard's son; Rebecca Taylor and Rebecca Staples parentage; the Granny Gurney's Swamp source (Cyrus Nash); independent confirmation of G10 as father of G9; the aunt-upbringing (Nathan & Sarah Harden Gurney); the two-Benjamin resolution; and — from p. 182 — the correction of Nathan Gurney's parentage to Zachariah (not John) Gurney, with his 1702 birth and 1786 death and a tenth child, Martha.
```

---

## A3 — Nathan fact sheet — `fact-sheets/g09-nathan-gurney-related-fact-sheet.md`

### A3-1 — pageHeading dates

`str_replace`

old_string:
```
pageHeading: Nathan Gurney of Little Comfort (c.1700–after 1751)
```
new_string:
```
pageHeading: Nathan Gurney of Little Comfort (1702–1786)
```

### A3-2 — JSON-LD birthDate

`str_replace`

old_string:
```
    "birthDate": "1700",
```
new_string:
```
    "birthDate": "1702",
```

### A3-3 — Born vital cell

`str_replace`

old_string:
```
    <div class="fact-value">About 1700–1704, probably at Weymouth or the new Little Comfort settlement. No birth record survives; his 1725 marriage and his first child's 1727 birth place him in that bracket. He was a son of John Gurney, the Weymouth man who settled south Abington, and a grandson of Richard Gurney of Weymouth. <sup class="fn"><a href="#n1" id="ref-1">1</a></sup></div>
```
new_string:
```
    <div class="fact-value">15 October 1702, at Weymouth, Massachusetts. He was a son of Zachariah Gurney and Mary Benson, and a grandson of Richard Gurney of Weymouth (G12); he came to the Little Comfort settlement in south Abington as a young man. <sup class="fn"><a href="#n1" id="ref-1">1</a></sup></div>
```

### A3-4 — Died vital cell

`str_replace`

old_string:
```
    <div class="fact-value">Not established in surviving records. His youngest recorded child was born in 1751, and he headed a Little Comfort household through the middle of the century. <sup class="fn"><a href="#n2" id="ref-2">2</a></sup></div>
```
new_string:
```
    <div class="fact-value">17 April 1786, at Abington. His wife Sarah outlived him by two years, dying in 1788. <sup class="fn"><a href="#n2" id="ref-2">2</a></sup></div>
```

### A3-5 — Home vital cell

`str_replace`

old_string:
```
    <div class="fact-value">Little Comfort, the milling district of south Abington — then within the bounds of Bridgewater, later South Abington, today Whitman. His father had started the Little Comfort sawmill there. <sup class="fn"><a href="#n3" id="ref-3">3</a></sup></div>
```
new_string:
```
    <div class="fact-value">Little Comfort, the milling district of south Abington — then within the bounds of Bridgewater, later South Abington, today Whitman. The Gurneys had run its first sawmill since the 1690s; Nathan settled a 107-acre farm nearby, off what is now Plymouth Street. <sup class="fn"><a href="#n3" id="ref-3">3</a></sup></div>
```

### A3-6 — Highlights bullet 3 (Little Comfort Gurneys)

`str_replace`

old_string:
```
  <li><strong>Of the Little Comfort Gurneys.</strong> His father, John Gurney, came from Weymouth about 1690, settled the south part of old Abington, and started its first sawmill — the family seat for the next century. <sup class="fn"><a href="#n3" id="ref-3b">3</a></sup></li>
```
new_string:
```
  <li><strong>Of the Little Comfort Gurneys.</strong> Nathan's people had come from Weymouth a generation earlier and settled the south part of old Abington, running its first sawmill at the milling hamlet of Little Comfort — the family seat for the next century. <sup class="fn"><a href="#n3" id="ref-3b">3</a></sup></li>
```

### A3-7 — Highlights bullet 4 (large household)

`str_replace`

old_string:
```
  <li><strong>A large household.</strong> Nathan and Sarah had nine recorded children between 1727 and 1751 — Rebecca, Lemuel, Elijah, Noah, Nathan, Silas, Sarah, Jacob, and John — and Benjamin grew up among them. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></li>
```
new_string:
```
  <li><strong>A large household.</strong> Nathan and Sarah had ten children between 1725 and 1751 — Martha, Rebecca, Lemuel, Elijah, Noah, Nathan, Silas, Sarah, Jacob, and John — and Benjamin grew up among them. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></li>
```

### A3-8 — Narrative paragraph 1 (origins and the cousinship)

`str_replace`

old_string:
```
Nathan Gurney belongs to the Abington side of the family rather than the direct line, but he sits at one of its turning points: he and his wife raised the boy who carries the line forward. The Gurneys had reached old Abington a generation earlier, when Nathan's father, John Gurney, came over from Weymouth about 1690 and settled the south part of the town — then still within Bridgewater — at the milling hamlet called Little Comfort, where he built one of its first sawmills. John was a son of Richard Gurney of Weymouth (G12); his brother Benjamin (G11) is the direct ancestor, which makes Nathan and the direct-line Benjamin Gurney (G10) first cousins. <sup class="fn"><a href="#n3" id="ref-3c">3</a></sup><sup class="fn"><a href="#n5" id="ref-5d">5</a></sup>
```
new_string:
```
Nathan Gurney belongs to the Abington side of the family rather than the direct line, but he sits at one of its turning points: he and his wife raised the boy who carries the line forward. He was born at Weymouth in 1702, a son of Zachariah Gurney, and came down to the new south-Abington settlement at Little Comfort as a young man — the milling hamlet, then still within Bridgewater, where his uncle John Gurney had built one of the first sawmills. Through his grandfather, Richard Gurney of Weymouth (G12), Nathan was a first cousin of the direct-line Benjamin Gurney (G10): Richard's son Zachariah was Nathan's father, and Richard's son Benjamin (G11) was the direct ancestor. <sup class="fn"><a href="#n3" id="ref-3c">3</a></sup><sup class="fn"><a href="#n5" id="ref-5d">5</a></sup>
```

### A3-9 — Narrative paragraph 2 (marriage and the household)

`str_replace`

old_string:
```
In 1725 Nathan married Sarah Harden, a blacksmith's daughter from Little Comfort and a sister of Jane Harden. Five years later Jane gave birth to a son, Benjamin, baptized at the First Church of Abington on 30 May 1730 with only his mother named. The child was taken into Nathan and Sarah's household — a natural landing place, since Sarah was the baby's aunt and Nathan his father's cousin. Benjamin grew up there alongside the couple's own children: Rebecca, born in 1727; Lemuel, born the same year as Benjamin; and, in the years that followed, Elijah, Noah, Nathan, Silas, Sarah, Jacob, and John. <sup class="fn"><a href="#n4" id="ref-4b">4</a></sup><sup class="fn"><a href="#n6" id="ref-6b">6</a></sup>
```
new_string:
```
In May 1725 Nathan married Sarah Harden, a blacksmith's daughter from Little Comfort and a sister of Jane Harden; their first child, Martha, arrived that July. Five years on, Jane gave birth to a son, Benjamin, baptized at the First Church of Abington on 30 May 1730 with only his mother named. The child was taken into Nathan and Sarah's household — a natural landing place, since Sarah was the baby's aunt and Nathan his father's cousin. Benjamin grew up there alongside the couple's own children: Martha and Rebecca, then Lemuel, born the same year as Benjamin, and in the years that followed Elijah, Noah, Nathan, Silas, Sarah, Jacob, and John. <sup class="fn"><a href="#n4" id="ref-4b">4</a></sup><sup class="fn"><a href="#n6" id="ref-6b">6</a></sup>
```

### A3-10 — Narrative paragraph 3 (death and the Whitman line)

`str_replace`

old_string:
```
What became of Nathan himself is not recorded; no death date or estate has yet surfaced, and the last of his children was born in 1751. His line, however, did not leave. While the direct-line Benjamin moved on to Bridgewater and ultimately to Cummington in the western hills, Nathan's sons and grandsons stayed in south Abington, gave their name to houses still standing in Whitman, and produced — three generations on — another Nathan Gurney prominent enough in town affairs that the two are easily mistaken for one another. <sup class="fn"><a href="#n2" id="ref-2b">2</a></sup><sup class="fn"><a href="#n7" id="ref-7b">7</a></sup>
```
new_string:
```
Nathan died at Abington in 1786, and Sarah two years after him; the last of their children had been born in 1751. His line did not leave. While the direct-line Benjamin moved on to Bridgewater and ultimately to Cummington in the western hills, Nathan's sons and grandsons stayed in south Abington, gave their name to houses still standing in Whitman, and produced — three generations on — another Nathan Gurney prominent enough in town affairs that the two are easily mistaken for one another. <sup class="fn"><a href="#n2" id="ref-2b">2</a></sup><sup class="fn"><a href="#n7" id="ref-7b">7</a></sup>
```

### A3-11 — Citation n1 (birth and parentage; Hobart-error note lives here, not in body)

`str_replace`

old_string:
```
  <li id="n1">Birth bracket inferred from his 1725 marriage and first child's 1727 birth; parentage and grandparentage from Benjamin Hobart, <em>History of the Town of Abington, Plymouth County, Massachusetts, from its First Settlement</em> (Boston: T. H. Carter and Son, 1866), Appendix Gurney register, pp. 383–384, and Jean Gurney Rigler, <em>The Gurney Family from Aaron to Zuinglius</em>, rev. ed. (Honolulu: J. G. Rigler, 1994). Source IDs: <code>hobart-benjamin-history-abington-1866</code>, <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-1">return</a></li>
```
new_string:
```
  <li id="n1">Born 15 October 1702 at Weymouth (Weymouth vital records); parentage — son of Zachariah Gurney and Mary (Benson) Gurney, grandson of Richard Gurney of Weymouth — from Jean Gurney Rigler, <em>The Gurney Family from Aaron to Zuinglius</em>, rev. ed. (Honolulu: J. G. Rigler, 1994), Nathan-4 entry, p. 182. Benjamin Hobart's <em>History of the Town of Abington, Plymouth County, Massachusetts, from its First Settlement</em> (Boston: T. H. Carter and Son, 1866), Appendix Gurney register, pp. 383–384, made Nathan a son of John Gurney of Little Comfort; Rigler corrects this, noting the error arose from the wording of John Gurney-3's estate transactions and that the Weymouth vital records, Cyrus Nash, and the Anna Gurney papers establish Zachariah as his father. Source IDs: <code>rigler-gurney-family-aaron-zuinglius-1994</code>, <code>hobart-benjamin-history-abington-1866</code>. <a class="citation-back" href="#ref-1">return</a></li>
```

### A3-12 — Citation n2 (death)

`str_replace`

old_string:
```
  <li id="n2">Hobart, <em>History of the Town of Abington</em> (1866), Appendix Gurney register, p. 384 (youngest recorded child John, b. May 1751; no death recorded for Nathan). Source ID: <code>hobart-benjamin-history-abington-1866</code>. <a class="citation-back" href="#ref-2">return</a></li>
```
new_string:
```
  <li id="n2">Nathan Gurney died 17 April 1786, and Sarah (Harden) Gurney in 1788, both at Abington (Abington vital records), per Rigler, <em>Gurney Family from Aaron to Zuinglius</em> (1994), Nathan-4 entry, p. 182. Source ID: <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-2">return</a></li>
```

### A3-13 — Citation n3 (Little Comfort; John-3 as uncle and mill founder)

`str_replace`

old_string:
```
  <li id="n3">Hobart, <em>History of the Town of Abington</em> (1866), Appendix Gurney register, p. 383 ("John Gurney… came from Weymouth, and settled in the south part of this town… about the year 1690") and p. 3 (first Little Comfort sawmill, 1698); Rigler, <em>Gurney Family</em> (1994), identifying John Gurney as founder of the Little Comfort mill. Source IDs: <code>hobart-benjamin-history-abington-1866</code>, <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-3">return</a></li>
```
new_string:
```
  <li id="n3">The Little Comfort milling hamlet of south Abington (first sawmill, 1698): Hobart, <em>History of the Town of Abington</em> (1866), Appendix Gurney register, p. 383, and main text p. 3. Rigler, <em>Gurney Family</em> (1994), identifies the mill's founder as John Gurney-3 — Nathan's uncle, a son of Richard Gurney (G12) — and records Nathan's own 1733 purchase of a 107-acre Stowell tract near Plymouth Street where he settled (Nathan-4 entry, p. 182). Source IDs: <code>hobart-benjamin-history-abington-1866</code>, <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-3">return</a></li>
```

### A3-14 — Citation n4 (Sarah Harden and the marriage)

`str_replace`

old_string:
```
  <li id="n4">Sarah Harden's birth (9 April 1707) and parentage from <em>Vital Records of Abington, Massachusetts, to the Year 1850</em>, vol. 1, and John Harden's 1751 Plymouth County will (daughter Sarah Gurney); marriage of Nathan Gurney and Sarah Harden, 12 May 1725, from <em>The Neverending Hobby — John Gurney, US 1636</em>, corroborated by the October-1727 birth of their first child in Hobart's register. Source IDs: <code>abington-vr-1850-vol1</code>, <code>plymouth-probate-john-harden-1751-will</code>, <code>neverending-hobby-john-gurney-us-1636</code>, <code>hobart-benjamin-history-abington-1866</code>. <a class="citation-back" href="#ref-4">return</a></li>
```
new_string:
```
  <li id="n4">Sarah Harden's birth (9 April 1707) and parentage from <em>Vital Records of Abington, Massachusetts, to the Year 1850</em>, vol. 1, and John Harden's 1751 Plymouth County will (daughter Sarah Gurney). Marriage of Nathan Gurney and Sarah Harden, 12 May 1725 at Abington, from Rigler, <em>Gurney Family</em> (1994), Nathan-4 entry, p. 182, and <em>The Neverending Hobby — John Gurney, US 1636</em>; their eldest child Martha was born that July. Source IDs: <code>abington-vr-1850-vol1</code>, <code>plymouth-probate-john-harden-1751-will</code>, <code>rigler-gurney-family-aaron-zuinglius-1994</code>, <code>neverending-hobby-john-gurney-us-1636</code>. <a class="citation-back" href="#ref-4">return</a></li>
```

### A3-15 — Citation n5 (relationship; descent via Zachariah)

`str_replace`

old_string:
```
  <li id="n5">Relationship: Rigler, <em>Gurney Family</em> (1994), entry Benjamin Gurney-5, pp. 21–22 ("raised in Abington by Nathan-4 &amp; Sarah (Harden) Gurney, his mother's sister"); and the shared descent from Richard Gurney of Weymouth (G12) through John Gurney (Nathan's father) and Benjamin Gurney-3 (G11, the direct ancestor) in Hobart's register and Rigler. Source IDs: <code>rigler-gurney-family-aaron-zuinglius-1994</code>, <code>hobart-benjamin-history-abington-1866</code>. <a class="citation-back" href="#ref-5">return</a></li>
```
new_string:
```
  <li id="n5">Relationship: Rigler, <em>Gurney Family</em> (1994), entry Benjamin Gurney-5, pp. 21–22 ("raised in Abington by Nathan-4 &amp; Sarah (Harden) Gurney, his mother's sister"), with the shared descent from Richard Gurney of Weymouth (G12) — Nathan through Richard's son Zachariah (Nathan-4 entry, p. 182), the direct line through Richard's son Benjamin Gurney-3 (G11). Source ID: <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-5">return</a></li>
```

### A3-16 — Citation n6 (children)

`str_replace`

old_string:
```
  <li id="n6">Hobart, <em>History of the Town of Abington</em> (1866), Appendix Gurney register, p. 384 (children of Nathan: Rebecca 1727, Lemuel 1730, Elijah 1732, Noah 1735, Nathan 1739, Silas 1743, Sarah 1745, Jacob 1748, John 1751). Source ID: <code>hobart-benjamin-history-abington-1866</code>. <a class="citation-back" href="#ref-6">return</a></li>
```
new_string:
```
  <li id="n6">Children of Nathan and Sarah from Rigler, <em>Gurney Family</em> (1994), Nathan-4 entry, p. 182, with Hobart, <em>History of the Town of Abington</em> (1866), Appendix Gurney register, p. 384: Martha (b. 1725, m. Zachariah Shaw), Rebecca (1727, m. Joseph Tirrell), Lemuel (1730), Elijah (1732), Noah (1735, m. Ruth Pool), Nathan (1739, m. Mary "Molly" Palmer), Silas (1743, m. Ruth Palmer), Sarah (1745/6), Jacob (1748, m. Elizabeth Keene — Rigler correcting Hobart's "Reese"), and John (1751, m. Sarah Norton). Source IDs: <code>rigler-gurney-family-aaron-zuinglius-1994</code>, <code>hobart-benjamin-history-abington-1866</code>. <a class="citation-back" href="#ref-6">return</a></li>
```

### A3-17 — Relationship Path table: Father row

`str_replace`

old_string:
```
      <tr><td>Father</td><td>John Gurney, settler of Little Comfort</td></tr>
```
new_string:
```
      <tr><td>Father</td><td>Zachariah Gurney of Weymouth</td></tr>
```

### A3-18 — Timeline table

`str_replace`

old_string:
```
      <tr><td>c.1700–04</td><td>Born, a son of John Gurney of Little Comfort.</td></tr>
      <tr><td>1725</td><td>Married Sarah Harden, 12 May.</td></tr>
      <tr><td>1727</td><td>First child, Rebecca, born.</td></tr>
      <tr><td>1730</td><td>Took in his nephew Benjamin (G9), baptized 30 May; son Lemuel born the same year.</td></tr>
      <tr><td>1732–51</td><td>Seven more children: Elijah, Noah, Nathan, Silas, Sarah, Jacob, John.</td></tr>
      <tr><td>after 1751</td><td>Death not recorded; the Whitman Gurney line descends from him.</td></tr>
```
new_string:
```
      <tr><td>1702</td><td>Born at Weymouth, a son of Zachariah Gurney.</td></tr>
      <tr><td>1725</td><td>Married Sarah Harden, 12 May; daughter Martha born that July.</td></tr>
      <tr><td>1730</td><td>Took in his wife's nephew Benjamin (G9), baptized 30 May; son Lemuel born the same year.</td></tr>
      <tr><td>1733</td><td>Bought the 107-acre Stowell farm near Plymouth Street and settled there.</td></tr>
      <tr><td>1732–51</td><td>Seven more children: Elijah, Noah, Nathan, Silas, Sarah, Jacob, John.</td></tr>
      <tr><td>1786</td><td>Died at Abington; Sarah died 1788. The Whitman Gurney line descends from him.</td></tr>
```

---

## A4 — Nathan research companion — `research/people/nathan-gurney-abington.research.md`

### A4-1 — opening paragraph: corrected parentage + pointer to the friction section

`str_replace`

old_string:
```
Nathan Gurney lived at **Little Comfort** — the milling district of south Abington (within the old Bridgewater bounds, later South Abington, now **Whitman**). He was a son of **John Gurney**, the Weymouth man who settled there about 1690 and started the Little Comfort sawmill, and therefore a grandson of **Richard Gurney of Weymouth (G12)**. That makes Nathan a **first cousin of Benjamin Gurney-4 (G10)** — both were grandsons of Richard — and the cousin's household was where Benjamin (G10)'s out-of-wedlock son was raised.[^hobart-register][^rigler-g10]
```
new_string:
```
Nathan Gurney lived at **Little Comfort** — the milling district of south Abington (within the old Bridgewater bounds, later South Abington, now **Whitman**). He was born at Weymouth on 15 October 1702, a son of **Zachariah Gurney and Mary (Benson) Gurney**, and therefore a grandson of **Richard Gurney of Weymouth (G12)**. That makes Nathan a **first cousin of Benjamin Gurney-4 (G10)** — both were grandsons of Richard — and his household was where Benjamin (G10)'s out-of-wedlock son was raised. Nathan died at Abington 17 April 1786; Sarah died 1788. (On the older "son of John" reading, corrected by Rigler, see **Parentage** below.)[^rigler-nathan][^hobart-register]
```

### A4-2 — new Parentage section (the friction layer) before "The household Benjamin grew up in"

`str_replace`

old_string:
```
## The household Benjamin grew up in
```
new_string:
```
## Parentage — son of Zachariah, not John

Rigler's Nathan-4 entry corrects a long-standing error and states the case directly: Nathan was a son of **Zachariah Gurney and Mary (Benson) Gurney**, "Hobart's 'History of Abington' indicates that he was the son of John, but that is incorrect. The error probably arose from confused wording on some transactions regarding the estate of John Gurney-3 of Little Comfort. However, Weymouth Vital Records, Cyrus Nash… & the Anna Gurney papers conclusively prove that Nathan was the son of Zachariah Gurney."[^rigler-nathan]

Both Zachariah and John-3 were sons of Richard Gurney (G12), so the correction does **not** change Nathan's relationship to the direct line: he remains a grandson of Richard (G12) and a first cousin of Benjamin Gurney-4 (G10). What changes is the named father, and the narrative that "Nathan's father founded the Little Comfort mill." The mill was **John Gurney-3's**, and John-3 was Nathan's **uncle**. The same entry shows why the two were confused: on 14 February 1727 Nathan bought, for £25, a 1/6 share of John-3's Little Comfort estate from his cousin **David Gurney of Easton** — John-3's son. Hobart's register, dividing John-3's estate "among his children, among whom were Richard, David and Nathan," folded the cousin-buyer into the children. Nathan himself was a **housewright** who, with his brother Joseph, bought Abington land in 1720, agreed in 1730 to build a sawmill (sold 1748), and in 1733 bought the ~107-acre Stowell tract near Plymouth Street (now Whitman) where he settled. "It was from Nathan and his brothers, Zachariah & Joseph, that the Gurneys of Old Abington and Bridgewater descend."[^rigler-nathan]

## The household Benjamin grew up in
```

### A4-3 — children list: add Martha and the marriages

`str_replace`

old_string:
```
- Rebecca, b. October 1727
- Lemuel, b. October 1730
- Elijah, b. 1732
- Noah, b. May 1735
- Nathan, b. November 1739
- Silas, b. June 1743
- Sarah, b. March 1745
- Jacob, b. March 1748
- John, b. May 1751
```
new_string:
```
- Martha, b. 24 July 1725 (m. Zachariah Shaw, 1745)
- Rebecca, b. 4 October 1727 (m. Joseph Tirrell)
- Lemuel, b. 11 July 1730 (m. Rebecca Derby)
- Elijah, b. 15 May 1732 (m. 1. Mary Copeland, 2. Widow House)
- Noah, b. 4 May 1735 (m. Ruth Pool)
- Nathan, b. 22 November 1739 (m. Mary "Molly" Palmer)
- Silas, b. 14 June 1743 (m. Ruth Palmer)
- Sarah, b. 14 March 1745/6 (m. John Tirrell, Jr.)
- Jacob, b. 13 March 1748 (m. Elizabeth Keene — Rigler corrects Hobart's "Reese")
- John, b. 23 May 1751 (m. Sarah Norton)

Rigler (p. 182) supplies the eldest child Martha and the marriages; Hobart's register, which begins at Rebecca, is the source of the older nine-child list. The two compiled accounts otherwise agree on the sequence.[^rigler-nathan][^hobart-register]
```

### A4-4 — marriage-corroboration sentence: Martha, not Rebecca

`str_replace`

old_string:
```
Benjamin G9 (bpt. 30 May 1730) was almost exactly the age of Lemuel and slightly younger than Rebecca; he grew up among roughly nine Gurney foster-siblings at Little Comfort. Rebecca's October-1727 birth corroborates the **12 May 1725** marriage date that the compiled genealogies give for Nathan and Sarah Harden.[^hobart-register][^neverending-hobby]

No death date for Nathan is recorded in the examined sources; his youngest documented child was born in 1751.[^hobart-register]
```
new_string:
```
Benjamin G9 (bpt. 30 May 1730) was almost exactly the age of Lemuel and slightly younger than Rebecca; he grew up among ten Gurney foster-siblings at Little Comfort. The eldest, **Martha, born 24 July 1725** — just over two months after the **12 May 1725** marriage — both fixes the marriage date and explains the church's fornication citation that Rigler records.[^rigler-nathan]

Nathan died at Abington on 17 April 1786; Sarah died in 1788.[^rigler-nathan]
```

### A4-5 — "Little Comfort origin" section: John-3 is the uncle, not the father

`str_replace`

old_string:
```
## The Little Comfort origin — John Gurney, the Abington ancestor

Hobart: "**John Gurney**, the ancestor of most of the name in Abington, came from Weymouth, and settled in the south part of this town, then a part of Bridgewater, about the year 1690. He died about 1715; and, it seems, intestate… children, among whom were Richard, David and Nathan."[^hobart-register]

This John is, on convergent evidence, the **John Gurney-3 (son of Richard-2/G12)** whom Rigler names as the founder of the **Little Comfort mill**: same Weymouth origin, same south-Abington settlement, same intestacy, a son Nathan. The identification ties the foster-household directly back into the direct line — Nathan's father John and the direct-line Benjamin Gurney-3 (G11) were brothers, both sons of Richard Gurney (G12).[^hobart-register][^rigler-g10]
```
new_string:
```
## The Little Comfort origin — John Gurney-3, Nathan's uncle

Hobart: "**John Gurney**, the ancestor of most of the name in Abington, came from Weymouth, and settled in the south part of this town, then a part of Bridgewater, about the year 1690. He died about 1715; and, it seems, intestate… children, among whom were Richard, David and Nathan."[^hobart-register]

This John is the **John Gurney-3 (son of Richard-2/G12)** whom Rigler names as founder of the **Little Comfort mill**: same Weymouth origin, same south-Abington settlement, same intestacy. But Rigler's Nathan-4 entry shows that the "Nathan" in Hobart's list of John-3's heirs was **not** John-3's son — he was John-3's nephew, buying into the estate. John-3 was a brother of Nathan's father **Zachariah** and of the direct-line **Benjamin Gurney-3 (G11)**, all three sons of Richard Gurney (G12). So the foster-household still ties back into the direct line, but through Zachariah, not John: Nathan was Benjamin G10's first cousin, and John-3 the uncle whose mill and estate the family long associated — wrongly — with Nathan's paternity.[^hobart-register][^rigler-nathan][^rigler-g10]
```

### A4-6 — disambiguation header (now four Nathans worth separating cleanly — keep count honest)

`str_replace`

old_string:
```
1. **The foster-father Nathan** (this subject) — son of John, m. Sarah Harden ~1725, children 1727–1751.
```
new_string:
```
1. **The foster-father Nathan** (this subject) — son of Zachariah, b. 1702, m. Sarah Harden 1725, children 1725–1751, d. 1786.
```

### A4-7 — open question #1 resolved

`str_replace`

old_string:
```
1. **Nathan's vital dates.** Birth (implied c. 1700–1704), exact marriage record at Abington, and death/probate are not yet pinned to primary record images. (Unknown online.)
```
new_string:
```
1. **Nathan's vital dates — resolved from Rigler (Weymouth/Abington VR).** Born 15 October 1702 Weymouth; married Sarah Harden 12 May 1725 Abington; died 17 April 1786 Abington (Sarah 1788). The underlying town-record images and any Plymouth probate would still be worth pulling for primary confirmation. (Unknown online.)
```

### A4-8 — add the [^rigler-nathan] footnote definition

`str_replace`

old_string:
```
[^rigler-g9]: Jean Gurney Rigler, *The Gurney Family from Aaron to Zuinglius: Some Descendants of Richard Gurney Who Settled at Weymouth, MA before 1656*, rev. and expanded ed. (Honolulu: J. G. Rigler, 1994), entry BENJAMIN GURNEY-5, pp. 21–22 ("raised in Abington by Nathan-4 & Sarah (Harden) Gurney, his mother's sister"). Source ID: `rigler-gurney-family-aaron-zuinglius-1994`.
```
new_string:
```
[^rigler-g9]: Jean Gurney Rigler, *The Gurney Family from Aaron to Zuinglius: Some Descendants of Richard Gurney Who Settled at Weymouth, MA before 1656*, rev. and expanded ed. (Honolulu: J. G. Rigler, 1994), entry BENJAMIN GURNEY-5, pp. 21–22 ("raised in Abington by Nathan-4 & Sarah (Harden) Gurney, his mother's sister"). Source ID: `rigler-gurney-family-aaron-zuinglius-1994`.
[^rigler-nathan]: Rigler, *Gurney Family from Aaron to Zuinglius* (1994), entry NATHAN GURNEY-4 (Zachariah-3, Richard-2), p. 182 — Nathan's parentage (son of Zachariah & Mary Benson, correcting Hobart's "son of John"), birth 15 Oct. 1702 Weymouth, marriage 12 May 1725 and the fornication citation, the 1727 purchase of a 1/6 share of John-3's estate from cousin David Gurney of Easton, the 1733 Stowell-farm purchase, occupation (housewright), death 17 Apr. 1786 (Sarah 1788), and the full ten-child set. Transcribed at [`sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md). Source ID: `rigler-gurney-family-aaron-zuinglius-1994`.
```

---

## A5 — Benjamin G9 research companion — `research/people/g09-benjamin-gurney-fact-sheet.research.md`

### A5-1 — correct the "Hobart names the foster household" subsection

`str_replace`

old_string:
```
### Hobart (1866) names the foster household

Benjamin Hobart's *History of the Town of Abington* (1866) independently documents the household. Its Abington Gurney register makes Sarah Harden's husband **Nathan Gurney** a son of **John Gurney**, the Weymouth man who settled Little Comfort about 1690 and started its sawmill — i.e., the John Gurney-3 (son of Richard-2/G12) of Rigler's account, and a brother of the direct-line Benjamin Gurney-3 (G11). That makes Nathan a **first cousin of Benjamin's father, Benjamin Gurney G10**, as well as the husband of Benjamin's aunt: the boy was kept inside his Gurney kin and his Harden kin at once. Hobart gives Nathan and Sarah's children from town records — Rebecca (Oct. 1727), Lemuel (Oct. 1730), Elijah (1732), Noah (May 1735), Nathan (Nov. 1739), Silas (June 1743), Sarah (Mar. 1745), Jacob (Mar. 1748), John (May 1751) — so the household Benjamin grew up in can be reconstructed: he was the near-twin in age of Lemuel and grew up among roughly nine foster-siblings at Little Comfort. Rebecca's 1727 birth corroborates the 12 May 1725 marriage date the compiled genealogies give for Nathan and Sarah. The full collateral treatment is in `research/people/nathan-gurney-abington.research.md` and the related fact sheet `fact-sheets/g09-nathan-gurney-related-fact-sheet.md`.[^hobart-abington-1866]
```
new_string:
```
### The foster household

The household is documented by both Hobart (1866) and Rigler (1994). Nathan Gurney was a **son of Zachariah Gurney** and a grandson of Richard Gurney of Weymouth (G12), which makes him a **first cousin of Benjamin's father, Benjamin Gurney G10**, as well as the husband of Benjamin's aunt: the boy was kept inside his Gurney kin and his Harden kin at once. (Hobart's register calls Nathan a son of John Gurney, the Little Comfort mill founder; Rigler corrects this — John-3 was Nathan's uncle, and the error traces to John-3's estate transactions. Full treatment in `research/people/nathan-gurney-abington.research.md`.) Nathan and Sarah's ten children, born 1725–1751, were Martha (m. Zachariah Shaw), Rebecca, Lemuel, Elijah, Noah, Nathan, Silas, Sarah, Jacob, and John; Benjamin was the near-twin in age of Lemuel and grew up among them at Little Comfort. The eldest, Martha (b. 24 July 1725), corroborates the 12 May 1725 marriage. The full collateral treatment is in `research/people/nathan-gurney-abington.research.md` and the related fact sheet `fact-sheets/g09-nathan-gurney-related-fact-sheet.md`.[^hobart-abington-1866][^rigler-nathan-g9]
```

### A5-2 — add the [^rigler-nathan-g9] footnote definition

`str_replace`

old_string:
```
[^hobart-abington-1866]: Benjamin Hobart, *History of the Town of Abington, Plymouth County, Massachusetts, from its First Settlement* (Boston: T. H. Carter and Son, 1866), Appendix Gurney register, pp. 383–386; verbatim extract at `sources/corpus_supplement/hobart-1866-abington-gurney-register-extract.md`; [Internet Archive item historyoftownofa00hoba](https://archive.org/details/historyoftownofa00hoba/). Source ID: `hobart-benjamin-history-abington-1866`.
```
new_string:
```
[^hobart-abington-1866]: Benjamin Hobart, *History of the Town of Abington, Plymouth County, Massachusetts, from its First Settlement* (Boston: T. H. Carter and Son, 1866), Appendix Gurney register, pp. 383–386; verbatim extract at `sources/corpus_supplement/hobart-1866-abington-gurney-register-extract.md`; [Internet Archive item historyoftownofa00hoba](https://archive.org/details/historyoftownofa00hoba/). Source ID: `hobart-benjamin-history-abington-1866`.
[^rigler-nathan-g9]: Jean Gurney Rigler, *The Gurney Family from Aaron to Zuinglius* (1994), entry NATHAN GURNEY-4 (Zachariah-3), p. 182, establishing Nathan as a son of Zachariah (not John) Gurney and giving his vital dates and the full ten-child set. Transcribed at [`sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md). Source ID: `rigler-gurney-family-aaron-zuinglius-1994`.
```

---

## A6 — Abington/Whitman place file — `research/places/abington-whitman-line-ma.md`

`str_replace`

old_string:
```
John's son **Nathan Gurney** married **Sarah Harden** of Little Comfort (a blacksmith's daughter) about 1725 and raised here his wife's nephew **Benjamin Gurney (G9)**, baptized at Abington in 1730.
```
new_string:
```
John's nephew **Nathan Gurney** — a son of John's brother Zachariah, not of John himself, as the compiled genealogist Jean Gurney Rigler establishes against an older reading in Hobart — married **Sarah Harden** of Little Comfort (a blacksmith's daughter) about 1725 and raised here his wife's nephew **Benjamin Gurney (G9)**, baptized at Abington in 1730.
```
