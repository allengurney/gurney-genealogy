# Intake patchset v51 — §8 row cleanup, factual fixes, and footnote pass

**Prepared:** 2026-05-18
**Repo:** `allengurney/gurney-genealogy`
**Target branch:** `main`
**Target files:**
- `research/case-files/john-gurney-case-file-v4.md` — §2 candidate-table birth-age direction fix; §2 financial-motive wording softening; §8 elimination table six non-John rows removed; §8 Haddenham, St Ann Blackfriars, Maldon-bachelor rows simplified; §8 PROB/MS shelfmarks moved out of body cells; §10.1 For-table row 9 phrasing tightened to distinguish Francis G14 from his son John of Maldon; n3 missing backref added; n88 absorbs Haddenham detail; n92 split into n92a/n92b/n92c; n98 absorbs St Ann Blackfriars detail; n101 rewritten in plain English aligned to ~60%; n83 internal-pointer paths stripped; n94 dated language stripped; n61 action-item phrase stripped; orphan-footnote integrity check
- `research/people/g13-john-gurney-fact-sheet.research.md` — receive a stub "Daniel Shed / Braintree-Essex page-level citations" target-pull entry migrated from n61

**Status:** DRAFT — awaiting application. Depends on v50 (§1 and §8 HTML conversion) being in place; v51 edits the HTML `<td>` cell content and the citation index.

## Posture

Content cleanup pass. No styling changes (those are v50). All probabilities for Candidate B are normalized to **~60%** across §2, §8, §10, §11, and n101; the Bayesian-decomposition prose in n101 is replaced with plain-English reasoning that lists the supporting evidence and the offsetting concerns without multiplying multipliers.

Six non-John rows added to the §8 table in v48 are removed (the §8 table heading is "OTHER JOHN GURNEYS"; William, Walter, Christopher, Edward, Richard etc. do not belong there). The wider 1662-1666 London Gurney cluster remains catalogued in n110 and in `sources/corpus_supplement/london-hearth-tax-1662-1666-gurney-cluster.md`; no in-body acknowledgement of the wider cluster is added (the user's direction is to keep §8 focused on Johns only).

PROB / TNA / archive shelfmarks are stripped from §8 body cells and held in the corresponding footnotes only. Two body rows that carried elaborate elimination logic (Haddenham, St Ann Blackfriars) are reduced to the simple eliminative claim ("Not the correct age") with the chronological argument absorbed into the relevant footnote.

The Maldon-bachelor double-row (one citing n65, one citing n108a — both describing Bernau's "item 9" John, Francis G14's son from the Anne Browning marriage) is merged into a single row. The Maldon "Maldon, Essex (bachelor)" row name is preserved as the parish-ID half of the merged row title; both n65 and n108a are kept on the merged row so existing back-references continue to resolve.

The §2 candidate-table "Birth/age" row direction error is fixed (the case file currently says "slightly older than 'aged about 50' testimony would suggest" — the candidate is actually slightly **younger** than the deposition implies). The §2 candidate-table "Financial motive" cell is softened from "leaving sons with nothing to inherit" to "leaving elder sons with no land to expect" per the agreed wording.

---

## 1. §2 candidate-introduction table — two cell fixes

### 1a. Birth/age row — fix direction error

Locate the §2 candidate-introduction table (the markdown pipe-table near the top of §2 that summarizes the case). The "Birth/age" row currently reads:

```
| **Birth/age** | Born c.1607-1611 which is slightly older than "aged about 50" testimony would suggest (c.1603) but within plausibility. |
```

Replace with:

```
| **Birth/age** | Born c.1607-1611, slightly **younger** than the 1653 "aged about 50" deposition would imply (c.1603), but within plausibility for a self-reported age estimate. |
```

(A person born c.1607-1611 would be c.42-46 in 1653, not 50. The deposition's "about 50" therefore overstates the candidate's true age by 4-8 years, not understates it.)

### 1b. Financial motive row — soften wording

Same table, "Financial motive" row currently reads:

```
| **Financial motive** | John's father Francis sold ALL his lands in 1634, leaving sons with nothing to inherit |
```

Replace with:

```
| **Financial motive** | John's father Francis sold ALL his lands in 1634, leaving elder sons with no land to expect |
```

(Per the user's direction. The "lost everything" rhetoric is overstated — Francis G14 retained London standing through his 1646/7 burial at St Botolph Bishopsgate, and his sons by Anne Browning ended up in respectable Essex/Maldon households. The 1634 sale removed inheritable land, not all wealth.)

### 1c. §2.3 narrative — parallel softening

§2.3 currently closes:

```
This financial strain falls during John's late-teens-to-twenties, and any father-son dynamics around emigration would have been shaped by that backdrop of no inheritance.
```

Replace the closing clause:

```
This financial strain falls during John's late-teens-to-twenties, and any father-son dynamics around emigration would have been shaped by that backdrop of no land to expect.
```

---

## 2. §8 elimination table — remove six non-John rows

In the v50 HTML table, delete the following six `<tr>` blocks in full. Each is contextual London-cluster data, not a John candidate; the §8 table heading is "OTHER JOHN GURNEYS."

```
DELETE: <tr> ... Vintry 6th precinct, London (Edward) ... </tr>
DELETE: <tr> ... All Hallows Staining, London (Richard, wine cooper) ... </tr>
DELETE: <tr> ... St Alban Wood Street, London (Christopher) ... </tr>
DELETE: <tr> ... St Bride Fleet Street, London (William, 7 hearths) ... </tr>
DELETE: <tr> ... Stepney, Shadwell, Middlesex (Edward) ... </tr>
DELETE: <tr> ... St Margaret's Westminster (Walter) ... </tr>
```

These continue to be catalogued in:
- footnote n110 (full Merry 2010 hearth-tax cluster)
- `sources/corpus_supplement/london-hearth-tax-1662-1666-gurney-cluster.md`

n110 back-references for the removed rows (ref-110a, ref-110b, ref-110c, ref-110d, ref-110e, ref-110f) become orphan. The footnote text itself stays intact; only the back-reference letter chain at the end of n110 should drop the now-unused letters. The remaining back-refs (ref-110 on the Candidate D §8 row, ref-110g and ref-110h on the §8.4 body) stay in place.

**n110 backref-chain cleanup (last line of n110):**

Old:
```
<a class="backref" href="#ref-110">↩</a> <a class="backref" href="#ref-110a">back</a> <a class="backref" href="#ref-110b">back</a> <a class="backref" href="#ref-110c">back</a> <a class="backref" href="#ref-110d">back</a> <a class="backref" href="#ref-110e">back</a> <a class="backref" href="#ref-110f">back</a> <a class="backref" href="#ref-110g">back</a> <a class="backref" href="#ref-110h">back</a>
```

New:
```
<a class="backref" href="#ref-110">↩</a> <a class="backref" href="#ref-110g">back</a> <a class="backref" href="#ref-110h">back</a>
```

Similarly for n98 (referenced by St Ann Blackfriars row only after v51), the back-refs ref-98b and ref-98c (which were on the St Bride Fleet Street and St Margaret's Westminster Walter rows respectively) are orphan after row removal. Update the last line of n98:

Old:
```
<a class="backref" href="#ref-98a">back</a> <a class="backref" href="#ref-98b">back</a> <a class="backref" href="#ref-98c">back</a>
```

New:
```
<a class="backref" href="#ref-98a">back</a>
```

---

## 3. §8 elimination table — simplify Haddenham and St Ann Blackfriars rows

### 3a. Haddenham row — body cell

Locate the v50 HTML row for "Haddenham, Bucks (John)". The current elimination-reason `<td>` reads:

```html
<td>Alive in 1620-1622 England (Haddenham parish baptisms); fathering in 1620 requires a birth by about 1600, while the colonial John was born about 1603 (aged about 50 in 1653), making him only about 17 in 1620 and biologically incompatible with fathering (see 8.3).</td>
```

Replace the `<td>` content with:

```html
<td>Not the correct age (see §8.3).<sup class="fn"><a href="#n88" id="ref-88b">88</a></sup></td>
```

(The chronological argument is preserved in the expanded n88 — see §6 below.)

### 3b. St Ann Blackfriars row — body cell

Locate the v50 HTML row for "St Ann Blackfriars, London (John bapt 1615)". The current elimination-reason `<td>` reads:

```html
<td>FS index reads father as Wm. (William), not P or F. Resolves the case file's earlier "P Gurney" lead. Most plausibly the London William Gurney cluster (Coleman Street area; PROB 11/252/152 barber-chirurgion William, sons John, Abel, Walter). The 1615 baptism date for this John (son of William) is also consistent with the 1636 Newgate apprentice's implied birth year under the two-Johns reading.<sup class="fn"><a href="#n98" id="ref-98a">98</a></sup></td>
```

Replace the `<td>` content with:

```html
<td>Not the correct age (born 1615 vs. 1603).<sup class="fn"><a href="#n98" id="ref-98a">98</a></sup></td>
```

(The father-name resolution and William-cluster context are preserved in n98 — already there, no rewrite required. The body row no longer claims that the father-name reading is itself the eliminator; the row eliminates on age only, consistent with the corrected discriminator rule.)

---

## 4. §8 elimination table — strip PROB / MS shelfmarks from body cells

Each row below has an inline PROB / MS / archive shelfmark in its body cell. The reference already lives in the footnote that the row cites; remove it from the body for readability while keeping the substantive elimination claim.

### 4a. Candidate D row

Old `<td>` content:
```
Continuing London presence: 1638 T.C. Dale return at £10 rent and 1662 hearth tax at 1 hearth "poore" (TNA E 179/252/27 rot 21) at the same St Augustine precinct.<sup class="fn"><a href="#n92" id="ref-92a">92</a></sup> <sup class="fn"><a href="#n110" id="ref-110">110</a></sup>
```

New:
```
Continuing London presence: 1638 T.C. Dale return at £10 rent and 1662 hearth tax at 1 hearth "poore" at the same St Augustine precinct.<sup class="fn"><a href="#n92" id="ref-92a">92</a></sup> <sup class="fn"><a href="#n110" id="ref-110">110</a></sup>
```

### 4b. Winkfield, Berkshire

Old: `Died in England (will proved 1682, PROB 11/372/123); yeoman.`
New: `Died in England (will 1682); yeoman.`

### 4c. Aylesbury, Bucks (probate)

Old: `Died in England (probate sentence PROB 11/337/37).`
New: `Died in England (probate sentence).`

### 4d. Albury, Herts

Old: `Died in England (will proved 1676, PROB 11/335/425); husbandman.`
New: `Died in England (will 1676); husbandman.`

### 4e. St Botolph Aldgate, London

Old: `Died in England (will proved 1666, PROB 11/382/271); merchant.`
New: `Died in England (will 1666); merchant.`

### 4f. East Chiltington, Sussex

Old: `Died in England (probate PROB 11/241/246 and PROB 11/242/723); shepherd.`
New: `Died in England (probate); shepherd.`

### 4g. East Grinstead, Sussex

Old: `Died in England (will proved 1654, PROB 11/252/319); yeoman.`
New: `Died in England (will 1654); yeoman.`

### 4h. Abthorpe, Northants (labourer)

Old: `Died in England (John Gurney, labourer, will 1664, Archdeaconry Court of Northampton, Series 4TH, Book 6, fol. 260). Labourer trade; distinct from the Candidate A Northants tenancy at Walgrave.`
New: `Died in England (will 1664). Labourer trade; distinct from the Candidate A Northants tenancy at Walgrave.`

### 4i. Mickfield / Morningthorpe

Old: `Died in England. Garneys gentry: John Garneys gentleman of Mickfield, Suffolk, will 1675 (NCC Wiseman 196); buried Morningthorpe with Fritton, Norfolk, 17 December 1661.`
New: `Died in England. Garneys gentry (distinct surname): will 1675; buried Morningthorpe with Fritton, Norfolk, 17 December 1661.`

### 4j. London Merchant Taylor apprentice (Moborne, Worcestershire 1602)

Old: `John Gurney son of William, Glover deceased, of "Moborne," Worcestershire, bound 13 September 1602 to James Briggs of Shoe Lane (Merchant Taylor binding-book vol. 3b, no. 852, p. 114). Bound 1602 → would be too old by 1641 Weymouth; father William not Francis; not the Norfolk corridor.`
New: `John Gurney son of William, glover (deceased), of Moborne, Worcestershire, bound 13 September 1602 to James Briggs of Shoe Lane. Bound 1602 → would be too old by 1641 Weymouth; not the Norfolk corridor.`

### 4k. London Merchant Taylor apprentice (Aylesbury, Bucks 1655)

Old: `John Gurny son of John, Ironmonger of Aylesbury, Bucks, bound 30 May 1655 to Alexander Harbin of Gracechurch Street (Merchant Taylor binding-book vol. 14, no. 514, p. 67). Date too late for a 1641 Massachusetts emigrant; same Aylesbury Vale cluster as §8.1 / §8.3.`
New: `John Gurny son of John, ironmonger of Aylesbury, Bucks, bound 30 May 1655 to Alexander Harbin of Gracechurch Street. Date too late for a 1641 Massachusetts emigrant; same Aylesbury Vale cluster as §8.1 / §8.3.`

(The "father William not Francis" rationale in 4j was removed per the corrected discriminator rule — father-name is not an eliminator under the v46 logic correction. The Worcestershire-origin and 1602 binding-date elements remain.)

---

## 5. §8 elimination table — merge duplicate Maldon-bachelor rows

The current §8 table has two rows describing the same person (Francis G14's son John, the Maldon bachelor who died 1681):

```html
<tr>
  <td>Maldon, Essex (bachelor)</td>
  ... Alive in 1674 England (Essex hearth tax); bachelor; died in England 1681.<sup>n65</sup>
</tr>
<tr>
  <td>Maldon, Essex (John, bachelor s/o Francis G14)</td>
  ... Bachelor of St Mary's Maldon: 1674 hearth tax on nine hearths; letters of administration granted to brother Thomas Gurney 1681; second son named John in Francis G14's Anne Browning marriage.<sup>n108a</sup>
</tr>
```

**Delete the first row** (the `(bachelor)` row, cites n65). **Update the second row** to carry both citations:

```html
<tr>
  <td>Maldon, Essex (John, bachelor s/o Francis G14)</td>
  <td>Essex</td>
  <td>(unmarried)</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Bachelor of St Mary's Maldon: 1674 hearth tax on nine hearths; letters of administration granted to brother Thomas Gurney 1681. Bernau documents this as Francis G14's son John from the Anne Browning marriage.<sup class="fn"><a href="#n65" id="ref-65">65</a></sup> <sup class="fn"><a href="#n108" id="ref-108a">108</a></sup></td>
</tr>
```

(Both n65 and n108 cite the same Bernau "His Parents' Children" item 9 — n65 was the older citation, n108 the v46 citation. Keeping both back-references preserves any external links that resolve to either anchor.)

---

## 6. Footnote pass

### 6a. n3 — add missing back-reference

Old:
```html
<li id="n3" value="3">Nathaniel B. Shurtleff, ed., <em>Records of the Governor and Company of the Massachusetts Bay in New England</em>, vol. 1, 1628–1641 (Boston: William White, 1853), p. 331, June 1641 General Court record; cited for John Gurney by Anderson, <em>Great Migration Directory</em>, p. 158. Source ID: <code>anderson-gmd-2015</code>.</li>
```

New:
```html
<li id="n3" value="3">Nathaniel B. Shurtleff, ed., <em>Records of the Governor and Company of the Massachusetts Bay in New England</em>, vol. 1, 1628–1641 (Boston: William White, 1853), p. 331, June 1641 General Court record; cited for John Gurney by Anderson, <em>Great Migration Directory</em>, p. 158. Source ID: <code>anderson-gmd-2015</code>. <a class="backref" href="#ref-3">↩</a></li>
```

### 6b. n88 — absorb Haddenham age-incompatibility detail

Append to the existing n88 text (after the Hitcham line):

```
The 1620 Haddenham fathering is biologically incompatible with the colonial John, who was about 17 then under the 1602/3 birth implied by the 1653 Wilson v. Faxon "aged about 50" deposition; this Haddenham household is generationally earlier than Candidate A's 1628 marriage.
```

### 6c. n92 — split into n92a, n92b, n92c

Delete the existing n92 (the 600+ word omnibus footnote). Replace with three separate footnotes covering Robert's family, John's path into the Drapers' Company, and John's 1638-1662 London continuation. The footnote IDs remain `n92` (renumbered to `n92a`) for back-reference compatibility, with two new footnotes `n92b` and `n92c` added.

**Replacement block:**

```html
<li id="n92a" value="92">Robert Gurney, citizen and draper of London (St Augustine Watling Street and Old Change), the father of Candidate D John. Robert's will written 18 January 1621/2 and proved 23 September 1625, Archdeaconry Court of London; user-supplied image <code>31787_A002570-00422.jpg</code>; Source ID <code>acl-robert-gurney-will-1625</code>. Robert's Drapers' Company freedom 16 December 1581 (ROLLCO Drapers' event corpus including DREW4826, DREB5398, DRLL837, DRHT1669, DREW7982); described as a tailor at Old Change from his admission; Source ID <code>rollco-drapers-gurney-old-change-cluster</code>. Robert's St Magnus the Martyr marriage to Anne Morris by licence on 4 April 1611 (Source ID <code>lma-st-magnus-martyr-register-candidate-d-images</code>), after an earlier wife produced three children at St Augustine in the 1590s (Source ID <code>lma-st-augustine-watling-register-candidate-d-images</code>). Robert's will preamble uses the phrase "elect children of God" — Reformed-Protestant vocabulary, too weak to prove nonconformity. <a class="backref" href="#ref-92a">↩</a> <a class="backref" href="#ref-92b">back</a> <a class="backref" href="#ref-92c">back</a></li>
<li id="n92b" value="92b">Candidate D John Gurney's path into the Drapers' Company. ROLLCO Stationers' Company event STMM8981 (25 March 1613, John Gurney apprentice to James Boler, no later Stationers' freedom under Boler); Source ID <code>rollco-stationers-gurney-1613-1626</code>. ROLLCO Drapers' Company event DREW5638 (11 February 1623/4, John Gurney new freeman by redemption, Robert Gurney father of freeman); proved Robert's will 23 September 1625; John Gurney master event DRLL2060 (3 November 1630, Henry Smith of Kilton, Suffolk, bound seven years); Henry Smith does not surface as a freed Drapers' Smith 1635-1645, and no Drapers' turnover events involving any Gurney 1620-1670. Source ID <code>rollco-drapers-gurney-old-change-cluster</code>. The apprenticeship-via-Stationers-then-Drapers'-redemption reading is consistent with Joseph Hunscott (the Stationer named as overseer in Robert's 1625 will, and the case file's "will-network" bridge) — see also n92c. <a class="backref" href="#ref-92d">back</a> <a class="backref" href="#ref-92e">back</a></li>
<li id="n92c" value="92c">Candidate D John Gurney's continuation in London 1638–1662. T.C. Dale, "Inhabitants of London in 1638: St. Augustine," British History Online (Source ID <code>bho-london-inhabitants-st-augustine-1638</code>) — the return is a rents / tithe assessment in three manuscript sections, with John Gurney in MS. 67a at £10 and Joseph Huntscott (the Stationer Joseph Hunscott, 1612-1646 apprentice master, father of John Hunscott Stationer 1641, author of 1646 royalist petition Wing H3728) at £12 in MS. p. 68. The Robert Gurney will-network is still in the same parish thirteen years after Robert's death. Source IDs <code>rollco-stationers-hunscott-cluster</code>, <code>arber-stationers-bsoc-petition-1646-hunscott</code>. Boyd's Inhabitants of London card <code>GBOR/BIL/SOG59/0240</code> (John Gurny of S Augustine) reads "1661 poll tax [unclear] Old Change   1638 rent £10"; Source ID <code>findmypast-boyds-inhabitants-london-candidate-d-gurney-cards</code>. The 1661 poll-tax cue is now corroborated by the 1662 Lady Day hearth-tax entry at the same parish (see n110). No London-parish marriage of John Gurney to a wife named Mary, and no baptisms of Sarah, Mary, Richard, John, or Peter to a John Gurney + Mary household 1620-1641, have been located; the closest John Gurney + Mary marriage in window (Eythorne, Kent, 6 November 1632 to Mary Marsh) belongs to a Kent couple who stayed in Kent. Source ID <code>fs-england-births-christenings</code>. Depth-of-detail file: <code>research/people/john-gurney-candidate-d.md</code>; cross-link summary: <code>research/people/g13-john-gurney-fact-sheet.research.md</code>. <a class="backref" href="#ref-92f">back</a> <a class="backref" href="#ref-92g">back</a></li>
```

**Back-reference reassignment in §8.4 body:**

- `ref-92a` (Candidate D §8 row) → n92a (Robert Gurney's family) — unchanged
- `ref-92b` (§8.4 opener paragraph) → n92a (Robert Gurney's family context for the opener) — points to n92a now
- `ref-92c` (§8.4 paragraph "He was admitted to the Drapers' Company by redemption…") → n92a (Robert + Drapers' freedom + St Magnus marriage detail) — unchanged
- `ref-92d` (§8.4 paragraph "John was admitted to the Drapers' by redemption rather than patrimony…") → n92b (John's path into Drapers') — points to n92b now
- `ref-92e` (§8.4 paragraph "On 3 November 1630 John bound Henry Smith…") → n92b for the Henry Smith binding; n92c for the 1638 St Augustine return + 1662 hearth tax tie — split as `<sup>92b</sup> <sup>92c</sup>` adjacent
- `ref-92f` (§8.4 final paragraph "Robert's will preamble…") → n92c (the no-Mary-marriage / Hunscott / 1638 / 1661 cluster) — points to n92c now
- `ref-92g` (any remaining body ref) → n92c — unchanged

Update the body `href="#n92"` and `id="ref-92X"` attributes to the new target footnote IDs where they differ. The body text itself doesn't change; only the footnote anchor letters and the target IDs.

### 6d. n98 — confirm content covers the Haddenham/St Ann simplification

n98 already says:

```
FamilySearch England, Births and Christenings, 1538-1975 index entry for John Gurney, christening 13 March 1615, Saint Ann Blackfriars, London, father Wm. (William) Gurney. FS identifier JW7Y-C3B. Image unavailable in FS at index level. Source ID fs-jw7y-c3b-john-gurney-baptism-st-ann-blackfriars. The 1615 baptism date for this John (son of William) is also consistent with the 1636 Newgate apprentice's implied birth year (29 September 1615) under the case file's two-Johns reading.
```

This is sufficient to back the new "Not the correct age (born 1615 vs. 1603)" body row. No n98 text change required; only the backref-chain at the end is shortened (see §2 of this patchset).

### 6e. n101 — plain-English rewrite aligned to ~60%

Delete the existing n101 text in full. Replace with:

```html
<li id="n101" value="101">The ~60% point estimate for Candidate B reflects the combined weight of the supporting evidence in §10.1 against the offsetting concerns in §10.1. Supporting weight: the primary-record-confirmed Margaret Rybett marriage at Norwich in 1611 (NRO PD 12/1, fitting the chronological window for a son born c.1609/10); a tailor-from-Merchant-Taylor trade match consistent with the 17th-century pattern of sons following father into the same trade; placement in the dominant East Anglia → London emigration corridor that produced roughly sixty percent of Massachusetts Bay emigrants in the 1630s; a documented financial motive (the 1634 Court of Wards land sale liquidating Francis's Norfolk and Suffolk holdings); a substantial Essex colonial network on John's Massachusetts side (Daniel Shed of Finchingfield as son-in-law, the William Tyng leasehold in Braintree, the Braintree-Massachusetts/Braintree-Essex name carry-over, Coleman Street parish adjacency to Francis's St Benet Fink); the Ann Gurney / Gilman Norfolk-Hingham → Massachusetts-Hingham emigration corridor; Francis G14's East Dereham child cluster reinforced by primary-record-confirmed burials for Marye and Agnes and a probable 1633 burial for a younger Francis; and Mary Shed's 1647 Braintree marriage bounding her English birth before 1628. Offsetting concerns: the age mismatch between Entry E (c.1609/10) and the 1653 deposition's "aged about 50" (implying birth c.1602/3) — 6 to 8 years that survive only under a wide reading of "about"; the absence of a son named Francis in the colonial John's family — the strongest single naming-pattern concern; the absence of any indexed John+Mary marriage in eastern-England parish-marriage collections 1620-1635 outside the eliminated Eythorne Kent / Mary Marsh event; and common-name density across English parishes 1600-1670, with parish-coverage gaps leaving room for unidentified candidates in the corridor. The 60% estimate is a working summary, not a calculated probability — it is rounded to the nearest 5% and should be read with that precision. <a class="backref" href="#ref-101a">↩</a></li>
```

(No Bayesian decomposition jargon; no "raised by ~10 percentage points" historical-narrative framing; aligned to the ~60% in the §11 table.)

### 6f. n83 — strip internal-pointer paths

Old:
```html
<li id="n83" value="83">The National Archives, Kew, E 115/180/113, certificate of residence for John Gurney moving from Aylesbury half-hundred to Northamptonshire, 1641; John Gurney recorded as tenant at Walgrave, Northamptonshire, 1650. The originating Aylesbury parish register, Buckinghamshire, baptism entry for Jonathan Gurney son of John Gurney, 22 November 1647 is recorded in the same foundation research notes. <a class="backref" href="#ref-83">↩</a><a class="backref" href="#ref-83b">back</a></li>
```

New:
```html
<li id="n83" value="83">The National Archives, Kew, E 115/180/113, certificate of residence for John Gurney moving from Aylesbury half-hundred to Northamptonshire, 1641. John Gurney also recorded as tenant at Walgrave, Northamptonshire, 1650. The Aylesbury parish register baptism entry for Jonathan Gurney son of John Gurney, 22 November 1647 is part of the same Candidate A household sequence (see also n85 and n88). <a class="backref" href="#ref-83">↩</a> <a class="backref" href="#ref-83b">back</a></li>
```

### 6g. n94 — strip dated session language

Old opening:
```
Findmypast supplementary same-name sweep, 12 May 2026 raw research batch (`sources/intake/john-gurney-2026May/12May2026-John-Gurney-research-raw.md`). Surname variants Gurney, Gurny, Gourney, Garney, Garnes, Garneys, Garrne, Gernne, Girney, Girny, Guerne, Gourny across England Births & Baptisms 1538-1975; ...
```

New opening:
```
Findmypast supplementary same-name sweep across surname variants Gurney, Gurny, Gourney, Garney, Garnes, Garneys, Garrne, Gernne, Girney, Girny, Guerne, Gourny across England Births & Baptisms 1538-1975; ...
```

Also strip the "Aylesbury area screenshots retained at `sources/intake/john-gurney-2026May/image-2026051208*.png`" mid-footnote reference. The remaining footnote content (collections enumerated, source ID, out-of-corridor cluster note) stays.

### 6h. n61 — strip action-item phrase

Old closing:
```
The Daniel Shed/Finchingfield and Braintree-Essex place-name elements still need dedicated page-level citations. Source IDs: <code>sprague-braintree</code>; <code>nps-adams-nhp</code>; <code>british-archivist-bernau-1913</code>.
```

New closing:
```
Source IDs: <code>sprague-braintree</code>; <code>nps-adams-nhp</code>; <code>british-archivist-bernau-1913</code>.
```

The "still need dedicated page-level citations" action item migrates to the G13 companion's "Target Source Pulls" list:

```markdown
- **Daniel Shed / Finchingfield and Braintree-Essex place-name page-level citations.** §10.1 row 7 "Essex social network" rests on the Shed (Finchingfield, Essex) son-in-law connection, William Tyng (Stanford Rivers, Essex) leasehold, and the Braintree-Massachusetts naming-from-Braintree-Essex transfer. Each currently cites Sprague p. 695 (Shed marriage) and the NPS Adams NHP Cultural Landscape Report (Tyng leasehold) generally; targeted page-level citations from Bates, *Records of the Town of Braintree* (1886), the Tyng probate (Suffolk County MA Probate Liber 1, deferred pull), and the Finchingfield, Essex parish register (Daniel Shed's June 1620 baptism) would tighten the row.
```

### 6i. Orphan footnote integrity check

Run after applying §6a-§6h:

- `grep -nE "#ref-(66|67|68)" research/case-files/john-gurney-case-file-v4.md` — confirm that:
  - n66 (American Gurney arms) is still referenced from §10.1 For-table row 18.
  - n67 (Torrey + History of Weymouth) is referenced — confirm location; if no body reference remains, mark n67 for deletion in a follow-up.
  - n68 (Find a Grave Elm Street Cemetery) — if the v49 deletion of the §10.7 orphan "For colonial-side context …" paragraph removed the only body reference, n68 is now orphan; mark for deletion in a follow-up.

(Do not delete n66/n67/n68 in v51 unless the grep confirms zero body references. Orphan footnotes are visually inert; flagging them for a follow-up patchset is safer than deleting and finding an unexpected back-reference somewhere.)

### 6j. §10.1 For-table row 9 — tighten phrasing to distinguish Francis G14 from his son John of Maldon

Locate §10.1 For-table row 9. Current cell content:

```markdown
| 9 | Francis named a second son John in the Anne Browning marriage (Maldon bachelor, d. 1681) | Moderate | Bernau documents a second John Gurney son of Francis G14, paying 1674 hearth tax on nine hearths at St Mary's Maldon and dying a bachelor 1681. Demonstrates that Francis used the name John for a son in his second marriage; rebuts the inverse of the "no son named Francis" naming-pattern concern.<sup class="fn"><a href="#n108" id="ref-108">108</a></sup> |
```

Replace:

```markdown
| 9 | Francis named a second son John in the Anne Browning marriage | Moderate | Bernau documents that Francis G14 (d. 1646/7) named a son John in his second marriage to Anne Browning. This son — John of Maldon, distinct from Francis G14 himself — lived continuously at St Mary's Maldon, Essex through 1681 and died a bachelor (1674 hearth tax on nine hearths; letters of administration granted to brother Thomas Gurney 1681). Demonstrates that Francis used the name John for a son in his second marriage; rebuts the inverse of the "no son named Francis" naming-pattern concern.<sup class="fn"><a href="#n108" id="ref-108">108</a></sup> |
```

(The "(Maldon bachelor, d. 1681)" parenthetical is removed from the Evidence column heading because the row label itself is now framed around naming, not around the bachelor's biography. The subject of the explanation sentence is now unambiguous — "Francis G14 named a son John" — and the John-of-Maldon detail follows as the *evidence for* that claim, clearly attributed to the son not the father.)

---

## 7. Pre-apply integrity checks

- `grep -n "slightly older" research/case-files/john-gurney-case-file-v4.md` — should return zero matches in the §2 candidate table after application.
- `grep -nE "leaving sons with nothing to inherit|backdrop of no inheritance" research/case-files/john-gurney-case-file-v4.md` — should return zero matches.
- `grep -c '<tr>' research/case-files/john-gurney-case-file-v4.md` (or equivalent count over the v50 HTML §8 table) — should decrease by 6 (six non-John rows removed) and additionally decrease by 1 (Maldon-bachelor merge) → net −7 from the v50 baseline.
- `grep -nE "PROB 11/372/123|PROB 11/337/37|PROB 11/335/425|PROB 11/382/271|PROB 11/241/246|PROB 11/242/723|PROB 11/252/319|NCC Wiseman 196|TNA E 179/252/27|TNA E 179/367" research/case-files/john-gurney-case-file-v4.md | grep -v 'id="n' | grep -v 'id="ref-'` — should return only the citation-index footnote text (no `<td>` cell occurrences).
- `grep -n '<li id="n92a\|<li id="n92b\|<li id="n92c' research/case-files/john-gurney-case-file-v4.md` — exactly three matches.
- `grep -n '<li id="n92"' research/case-files/john-gurney-case-file-v4.md` — exactly zero matches (the old single n92 is replaced).
- `grep -nE "65-70%|65 to 70%|raised by ~10 percentage points" research/case-files/john-gurney-case-file-v4.md` — should return zero matches.
- `grep -nE "n3.*backref|#ref-3" research/case-files/john-gurney-case-file-v4.md` — confirm both the body anchor (in §1 table) and the citation-index back-ref are present.
- `grep -n "12 May 2026 raw research batch" research/case-files/john-gurney-case-file-v4.md` — should return zero matches.

## Reviewer checklist

- [ ] §2 candidate table birth/age row says "slightly **younger**"
- [ ] §2 candidate table financial-motive row says "leaving elder sons with no land to expect"
- [ ] §2.3 closing clause says "backdrop of no land to expect"
- [ ] §8 table — six non-John rows removed (Vintry Edward, All Hallows Staining Richard, St Alban Wood Street Christopher, St Bride Fleet Street William, Stepney Shadwell Edward, Westminster Walter)
- [ ] §8 table — Haddenham body cell now reads "Not the correct age (see §8.3)."
- [ ] §8 table — St Ann Blackfriars body cell now reads "Not the correct age (born 1615 vs. 1603)."
- [ ] §8 table — Maldon-bachelor merged into single row citing both n65 and n108; old "Maldon, Essex (bachelor)" row deleted
- [ ] §8 table — PROB / NCC / TNA / MS shelfmarks stripped from 10 body cells (Candidate D, Winkfield, Aylesbury probate, Albury, St Botolph Aldgate, East Chiltington, East Grinstead, Abthorpe, Mickfield, both MT apprentice rows)
- [ ] §10.1 For-table row 9 — Evidence column simplified; Explanation column clearly attributes John of Maldon as Francis G14's *son*, distinct from Francis G14 himself
- [ ] §11 Probability table: Candidate B remains at ~60% (no number change required in v51)
- [ ] n3 — back-reference link added
- [ ] n88 — Haddenham age-incompatibility detail appended
- [ ] n92 — replaced with n92a, n92b, n92c
- [ ] n98 — content unchanged; back-ref chain trimmed to ref-98a only
- [ ] n101 — rewritten in plain English aligned to ~60% point estimate; no Bayesian-decomposition jargon
- [ ] n83 — internal-pointer paths to foundation files stripped
- [ ] n94 — opening "12 May 2026 raw research batch" and mid-footnote screenshot path stripped
- [ ] n61 — closing action-item sentence stripped; pull-target migrated to G13 companion
- [ ] n110 — back-reference chain trimmed to ref-110, ref-110g, ref-110h
- [ ] G13 companion — Daniel Shed / Finchingfield / Braintree-Essex page-level-citation target-pull entry added
- [ ] Orphan footnote check on n66, n67, n68 (grep + flag for follow-up if no body reference remains; no deletion in v51)
- [ ] Integrity-check greps all pass

## Notes for follow-up

- **n26 substantiation gap.** Body §2.3 says "By 1638 he had left St Benet Fink" and cites n26; n26 admits the specific St Benet Fink absence still needs a direct check. Not addressed in v51. A future patchset could either soften the body claim to "Francis's St Benet Fink baptism sequence runs 1619-1637; subsequent residence is not directly attested" or pull the actual Dale St Benet Fink page reference into n26.
- **n7 Anderson / Winthrop long aside.** The second sentence of n7 is a long discursive note about Anderson's 1636 date possibly deriving from Winthrop's *Journal* 2:422. Acceptable as-is but could trim in a future pass.
- **n66, n67, n68 orphan status.** Resolved by the integrity-check grep in v51, not by a deletion. Follow up in v52+ if any are confirmed orphan.
- **§10 row 18 "American Gurney arms".** Currently labeled "Weak" with the saving clause "if an early American object or manuscript witness can be found." A future pass could either drop this row entirely (it doesn't currently move the probability) or upgrade with a specific early-witness pull from the G13 companion's American-arms target.
- **Adversarial review items #3-15** are intentionally not addressed in v51 per the user direction to leave them alone.
