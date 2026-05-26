# Intake patchset v50 — §1 facts table and §8 elimination table styling

**Prepared:** 2026-05-18
**Repo:** `allengurney/gurney-genealogy`
**Target branch:** `main`
**Target files:**
- `site/website/assets/site.css` — new `.facts-baseline` and `.candidates-table` CSS classes
- `research/case-files/john-gurney-case-file-v4.md` — §1 facts table converted from markdown pipe-table to HTML with the `.facts-baseline` class; §8 elimination table converted from markdown pipe-table to HTML with the `.candidates-table` class and per-row status classes

**Status:** DRAFT — awaiting application.

## Posture

Pure presentation change. No body prose, no footnote text, and no §8 row content changes. The pipe-table → HTML conversion preserves all existing cell content, all footnote references, and all row order. The CSS additions are scoped under the existing `.case-page` selector so that only the case-file page is affected.

The §1 facts table gets fixed column widths weighting the Detail column at roughly twice the Source column. The §8 elimination table gets row-level background highlighting for non-eliminated candidates (PROBABLE row darker, Unlikely rows lighter), plus colored Status badges that distinguish active candidates from eliminated ones at a glance.

Markdown pipe-tables cannot carry row-level `class=` attributes; HTML conversion is required.

---

## 1. CSS additions to `site/website/assets/site.css`

Insert under the existing `.case-page table { ... }` block (around line 79 of `site/website/assets/site.css`).

```css
/* §1 facts table — Detail column weighted ~2x Source column */
.case-page table.facts-baseline { table-layout: fixed; }
.case-page table.facts-baseline th:nth-child(1),
.case-page table.facts-baseline td:nth-child(1) { width: 16%; }
.case-page table.facts-baseline th:nth-child(2),
.case-page table.facts-baseline td:nth-child(2) { width: 56%; }
.case-page table.facts-baseline th:nth-child(3),
.case-page table.facts-baseline td:nth-child(3) { width: 28%; }

/* §8 elimination table — row highlighting for non-eliminated candidates */
.case-page table.candidates-table tr.status-probable { background: #e8f1fa; }
.case-page table.candidates-table tr.status-unlikely { background: #f3f7fb; }

/* §8 elimination table — status badges */
.case-page table.candidates-table .badge-probable {
  color: #1e5b8f;
  font-weight: 700;
}
.case-page table.candidates-table .badge-unlikely {
  color: #2f6fa6;
  font-weight: 700;
}
.case-page table.candidates-table .badge-eliminated {
  color: #6b6358;
  font-weight: 600;
}
```

Color rationale:
- `#e8f1fa` is a soft pale blue (about 95% lightness, slight cool tint) — visually announces the PROBABLE row without aggressive emphasis.
- `#f3f7fb` is one shade lighter for Unlikely rows so the visual hierarchy reads PROBABLE > Unlikely > ELIMINATED.
- Badge color `#1e5b8f` (deep slate-blue) for PROBABLE and `#2f6fa6` (medium slate-blue) for Unlikely contrast clearly with the page's brown accent (`var(--accent)`) without clashing.
- Eliminated badge color `#6b6358` (warm gray, matches the existing `.case-subtitle` color) recedes visually.

The `_site` parallel file at `site/website/_site/assets/site.css` is the built copy and will pick up the change at the next site build.

---

## 2. §1 facts table — pipe-table → HTML conversion

Locate the §1 table currently rendered as:

```markdown
| Fact | Detail | Genealogy Source |
|---|---|---|
| **Occupation** | Tailor | Sprague, p. 695<sup class="fn">...</sup>; Bates, p. 10<sup class="fn">...</sup> |
...
```

Replace with this HTML block (preserving every cell's content verbatim from the current markdown source, including all `<sup class="fn">…</sup>` footnote references):

```html
<table class="facts-baseline">
<thead>
<tr><th>Fact</th><th>Detail</th><th>Genealogy Source</th></tr>
</thead>
<tbody>
<tr>
  <td><strong>Occupation</strong></td>
  <td>Tailor</td>
  <td>Sprague, p. 695<sup class="fn"><a href="#n2" id="ref-2">2</a></sup>; Bates, p. 10<sup class="fn"><a href="#n72" id="ref-72">72</a></sup></td>
</tr>
<tr>
  <td><strong>First recorded in <br>Colonial America</strong></td>
  <td>June 1641 General Court fine-remission record</td>
  <td>MBCR 1:331; Porter, <em>Genealogy of the Descendants of Richard Porter</em> (1878), p. 225<sup class="fn"><a href="#n73" id="ref-73">73</a></sup> <sup class="fn"><a href="#n109" id="ref-109">109</a></sup></td>
</tr>
<tr>
  <td><strong>Settlement</strong></td>
  <td>Braintree, Massachusetts</td>
  <td>Sprague; Anderson GMD<sup class="fn"><a href="#n4" id="ref-4">4</a></sup></td>
</tr>
<tr>
  <td><strong>Birth estimate</strong></td>
  <td>c.1603 (stated "aged about 50" in 1653 deposition)</td>
  <td>Wilson v. Faxon, 1653<sup class="fn"><a href="#n5" id="ref-5">5</a></sup></td>
</tr>
<tr>
  <td><strong>Wife</strong></td>
  <td>Mary (maiden name unknown), d. 20 Sept 1661</td>
  <td>Bates, <em>Records of the Town of Braintree</em> (1886), p. 638; Sprague p. 695<sup class="fn"><a href="#n6" id="ref-6">6</a></sup></td>
</tr>
<tr>
  <td><strong>Second wife</strong></td>
  <td>Grizzell Fletcher/Kidbee, traditionally m. 12 Nov 1661; Braintree printed-record surname conflict</td>
  <td>Bates, <em>Records of the Town of Braintree</em> (1886), p. 717; Holman, "Grissell of the Many Marriages," <em>The American Genealogist</em> 10 (1933), pp. 70-73<sup class="fn"><a href="#n7" id="ref-7">7</a></sup></td>
</tr>
<tr>
  <td><strong>Children</strong> <br>(born in England)</td>
  <td>Sarah (b unknown), Mary (bc.1628), Richard (bc.1630), John Jr. (bc.1633), Peter (bc.1635-40) + potentially Isaac (uncertain)</td>
  <td>Sprague, <em>Genealogies of the Families of Braintree</em> (2001), p. 695; <em>History of Weymouth, Massachusetts</em> (1923), vol. 3, p. 251<sup class="fn"><a href="#n8" id="ref-8">8</a></sup></td>
</tr>
<tr>
  <td><strong>Estate / Death</strong></td>
  <td>Inventory dated 16 Mar 1662/63; died intestate</td>
  <td>SPR Case #338<sup class="fn"><a href="#n9" id="ref-9">9</a></sup>; Suffolk probate index<sup class="fn"><a href="#n74" id="ref-74">74</a></sup></td>
</tr>
<tr>
  <td><strong>Religion</strong></td>
  <td>Settled in Puritan community</td>
  <td>Context<sup class="fn"><a href="#n10" id="ref-10">10</a></sup></td>
</tr>
</tbody>
</table>
```

(Whitespace and indentation inside `<td>` cells are tolerated by all browsers; the eleventy markdown processor passes raw HTML through unchanged.)

---

## 3. §8 elimination table — pipe-table → HTML conversion with row classes

Locate the §8 table currently rendered as:

```markdown
| John Gurney | Location | Wife | Status | Primary Elimination Reason |
|---|---|---|---|---|
| **Candidate B** <br />(this case file) | East Dereham, Norfolk | Unknown | **PROBABLE (~60%)** | Son of London Merchant Taylor; occupational, geographic, and financial match (see §10). |
| **Candidate A** | Stewkley to Bierton to Aylesbury to Northamptonshire | **Alice** Oliffe | **ELIMINATED** | Alive in 1653 England; wife Alice Oliffe, not Mary (see section 8.1 below). |
...
```

Replace with this HTML block. **Important:** this conversion is a 1:1 transcription of the current §8 table contents — every row, every footnote reference, every cell preserved verbatim. The patchset adds only the `<table class="candidates-table">` wrapper, the `<tr class="status-…">` row-level class on rows where Status is not ELIMINATED, and the `<span class="badge-…">` wrapper around the Status cell content. **No row is removed and no cell content is altered in v50.** Row removal, cell-text simplification, and the Maldon-row merge happen in v51.

```html
<table class="candidates-table">
<thead>
<tr><th>John Gurney</th><th>Location</th><th>Wife</th><th>Status</th><th>Primary Elimination Reason</th></tr>
</thead>
<tbody>
<tr class="status-probable">
  <td><strong>Candidate B</strong> <br>(this case file)</td>
  <td>East Dereham, Norfolk</td>
  <td>Unknown</td>
  <td><span class="badge-probable">PROBABLE (~60%)</span></td>
  <td>Son of London Merchant Taylor; occupational, geographic, and financial match (see §10).</td>
</tr>
<tr>
  <td><strong>Candidate A</strong></td>
  <td>Stewkley to Bierton to Aylesbury to Northamptonshire</td>
  <td><strong>Alice</strong> Oliffe</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Alive in 1653 England; wife Alice Oliffe, not Mary (see section 8.1 below).</td>
</tr>
<tr>
  <td><strong>Candidate C</strong></td>
  <td>Berkhamsted, Hertfordshire</td>
  <td>Unknown</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Wrong age. Eight-child family; five children mismatch with colonial John Gurney (see section 8.2 below).</td>
</tr>
<tr>
  <td><strong>Candidate D</strong></td>
  <td>St Augustine Watling Street and Old Change, London</td>
  <td>Unknown</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Continuing London presence: 1638 T.C. Dale return at £10 rent and 1662 hearth tax at 1 hearth "poore" (TNA E 179/252/27 rot 21) at the same St Augustine precinct.<sup class="fn"><a href="#n92" id="ref-92a">92</a></sup> <sup class="fn"><a href="#n110" id="ref-110">110</a></sup></td>
</tr>
<tr class="status-unlikely">
  <td>Aylesbury, Bucks (John + Anne Cowheard)</td>
  <td>Buckinghamshire</td>
  <td><strong>Anne</strong> Cowheard</td>
  <td><span class="badge-unlikely">Unlikely (~3%)</span></td>
  <td>Single indexed event: marriage 1638 at Saint Mary, Aylesbury; no continuation of household indexed and no emigration evidence.<sup class="fn"><a href="#n105" id="ref-105">105</a></sup></td>
</tr>
<tr class="status-unlikely">
  <td>Amersham, Bucks (John + Avis Garter)</td>
  <td>Buckinghamshire</td>
  <td><strong>Avis</strong> Garter</td>
  <td><span class="badge-unlikely">Unlikely (~3%)</span></td>
  <td>Marriage 7 February 1638 Amersham; single indexed event; no continuation of this couple's household and no emigration evidence.<sup class="fn"><a href="#n94" id="ref-94p">94</a></sup></td>
</tr>
<tr>
  <td>Cheddington, Bucks</td>
  <td>Buckinghamshire</td>
  <td><strong>Rebecka</strong> Coker (Ivinghoe 1640)</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Continuing Bucks household: Johannes Gurney b.1608, m. Rebecka Coker Ivinghoe 1640, buried Edlesborough 1688 (residence Northall).<sup class="fn"><a href="#n103" id="ref-103">103</a></sup></td>
</tr>
<tr class="status-unlikely">
  <td>Hitcham, Bucks (John)</td>
  <td>Buckinghamshire</td>
  <td>Unknown</td>
  <td><span class="badge-unlikely">Unlikely (~2%)</span></td>
  <td>Single indexed event: Mary Gurny bapt 1631 at Hitcham, father John Gurny; mother and siblings unindexed; no further Hitcham Gurney activity surfaces 1620–1665.<sup class="fn"><a href="#n88" id="ref-88c">88</a></sup> <sup class="fn"><a href="#n107" id="ref-107">107</a></sup></td>
</tr>
<tr class="status-unlikely">
  <td>Norwich (m. 1639)</td>
  <td>Norfolk</td>
  <td><strong>Jane</strong> Wright</td>
  <td><span class="badge-unlikely">Unlikely (~3%)</span></td>
  <td>Single indexed event: marriage 1639 at Saint Benedict, Norwich; no continuation of a John + Jane Norwich household and no emigration evidence indexed.<sup class="fn"><a href="#n104" id="ref-104">104</a></sup></td>
</tr>
<tr class="status-unlikely">
  <td>Ackworth, Yorkshire</td>
  <td>Yorkshire</td>
  <td><strong>Mary</strong> Burton</td>
  <td><span class="badge-unlikely">Unlikely (~2%)</span></td>
  <td>John Gurnoe + Mary Burton m. Ackworth 6 June 1636; son John Thomas bapt Ackworth 1637; first child is John Thomas not Sarah; no further indexed Yorkshire Gurnoe activity surfaces.<sup class="fn"><a href="#n93" id="ref-93a">93</a></sup> <sup class="fn"><a href="#n106" id="ref-106">106</a></sup></td>
</tr>
<tr>
  <td>Toddington, Beds</td>
  <td>Bedfordshire</td>
  <td><strong>Elizabeth</strong> Moreton</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Died in England (buried Toddington September 1641); wife Elizabeth, not Mary; non-matching children.<sup class="fn"><a href="#n90" id="ref-90">90</a></sup></td>
</tr>
<tr>
  <td>Winkfield, Berkshire</td>
  <td>Berkshire</td>
  <td><strong>Alice / Ellice</strong></td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Died in England (will proved 1682, PROB 11/372/123); yeoman.<sup class="fn"><a href="#n60" id="ref-60c">60</a></sup></td>
</tr>
<tr>
  <td>Aylesbury, Bucks (probate)</td>
  <td>Buckinghamshire</td>
  <td><strong>Sarah</strong> (probable)</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Died in England (probate sentence PROB 11/337/37).<sup class="fn"><a href="#n60" id="ref-60d">60</a></sup></td>
</tr>
<tr>
  <td>Chesham, Bucks (John + Elizabeth)</td>
  <td>Buckinghamshire</td>
  <td><strong>Elizabeth</strong></td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Died in England (buried Chesham July 1672 and 11 June 1678); wife Elizabeth (see 8.3).</td>
</tr>
<tr>
  <td>Cublington, Bucks (John + Mary)</td>
  <td>Buckinghamshire</td>
  <td><strong>Mary</strong></td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Alive in 1664 England (son Isaac baptized Cublington); held Stewkley manor by 1687 (see 8.3).</td>
</tr>
<tr>
  <td>East Claydon, Bucks (John + Elizabeth)</td>
  <td>Buckinghamshire</td>
  <td><strong>Elizabeth</strong></td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Died in England (buried East Claydon 17 April 1654); wife Elizabeth (see 8.3).</td>
</tr>
<tr>
  <td>Haddenham, Bucks (John)</td>
  <td>Buckinghamshire</td>
  <td>Unknown</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Alive in 1620-1622 England (Haddenham parish baptisms); fathering in 1620 requires a birth by about 1600, while the colonial John was born about 1603 (aged about 50 in 1653), making him only about 17 in 1620 and biologically incompatible with fathering (see 8.3).</td>
</tr>
<tr>
  <td>Wing, Bucks (John + Anne)</td>
  <td>Buckinghamshire</td>
  <td><strong>Anne</strong></td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Alive in 1650-1652 England (Wing parish baptisms); wife Anne (see 8.3).</td>
</tr>
<tr>
  <td>Maldon, Essex (bachelor)</td>
  <td>Essex</td>
  <td>(unmarried)</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Alive in 1674 England (Essex hearth tax); bachelor; died in England 1681.<sup class="fn"><a href="#n65" id="ref-65">65</a></sup></td>
</tr>
<tr>
  <td>Albury, Herts</td>
  <td>Hertfordshire</td>
  <td><strong>Jane</strong></td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Died in England (will proved 1676, PROB 11/335/425); husbandman.<sup class="fn"><a href="#n60" id="ref-60f">60</a></sup></td>
</tr>
<tr>
  <td>Eythorne, Kent</td>
  <td>Kent</td>
  <td><strong>Mary</strong> Marsh</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Died in England (buried Eythorne 1648); married Eythorne 6 November 1632.</td>
</tr>
<tr>
  <td>St Botolph Aldgate, London</td>
  <td>London</td>
  <td><strong>Mary</strong></td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Died in England (will proved 1666, PROB 11/382/271); merchant.<sup class="fn"><a href="#n60" id="ref-60b">60</a></sup></td>
</tr>
<tr>
  <td>St Giles Cripplegate, London (Francis B)</td>
  <td>London</td>
  <td>-</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Died in England (buried St Giles Cripplegate as an infant aged 2 days, son of Francis B the laceweaver).</td>
</tr>
<tr>
  <td>St Ann Blackfriars, London (John bapt 1615)</td>
  <td>London</td>
  <td>-</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>FS index reads father as Wm. (William), not P or F. Resolves the case file's earlier "P Gurney" lead. Most plausibly the London William Gurney cluster (Coleman Street area; PROB 11/252/152 barber-chirurgion William, sons John, Abel, Walter). The 1615 baptism date for this John (son of William) is also consistent with the 1636 Newgate apprentice's implied birth year under the two-Johns reading.<sup class="fn"><a href="#n98" id="ref-98a">98</a></sup></td>
</tr>
<tr>
  <td>St Giles Cripplegate (Francis Garney joiner)</td>
  <td>London</td>
  <td>-</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Died in England (buried St Giles Cripplegate December 1640, son of Francis Garney joiner).<sup class="fn"><a href="#n70" id="ref-70">70</a></sup></td>
</tr>
<tr>
  <td>Harrow on the Hill / Okington</td>
  <td>Middlesex</td>
  <td><strong>Mary</strong></td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Alive in 1669 England (Saint Mary Harrow parish burials of children); wife Mary.<sup class="fn"><a href="#n69" id="ref-69">69</a></sup></td>
</tr>
<tr>
  <td>Denton, Norfolk</td>
  <td>Norfolk</td>
  <td><strong>Rachell / Rachelle</strong></td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Continuing Denton, Norfolk household 1638–1644: children Mary 1638, Thomas 1639, Sarah 1644.<sup class="fn"><a href="#n87" id="ref-87a">87</a></sup> <sup class="fn"><a href="#n89" id="ref-89a">89</a></sup></td>
</tr>
<tr>
  <td>Earsham, Norfolk</td>
  <td>Norfolk</td>
  <td><strong>Elizabeth</strong> Singler</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Died in England (will proved 1639).<sup class="fn"><a href="#n60" id="ref-60a">60</a></sup></td>
</tr>
<tr>
  <td>Hempnall, Norfolk</td>
  <td>Norfolk</td>
  <td>Unknown</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Alive in 1640-1641 England (Hempnall parish baptisms of Anna 1640 and Elizabeth 1641; earlier Anna buried Hempnall 6 April 1639).<sup class="fn"><a href="#n87" id="ref-87b">87</a></sup></td>
</tr>
<tr>
  <td>Norwich, Saint Peter Mancroft</td>
  <td>Norfolk</td>
  <td>-</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Died in England (buried Saint Peter Mancroft, Norwich 10 February 1639).<sup class="fn"><a href="#n91" id="ref-91">91</a></sup></td>
</tr>
<tr>
  <td>Bury St Edmunds, Suffolk</td>
  <td>Suffolk</td>
  <td>Unknown (1656 widow burial)</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Continuing Bury household across 1653-1656: John buried 1653, Gurney burial 1655, widow buried 1656. The Bury head was not the colonial John. Bears on Banks's Bury attribution; see §10.2 and §8.5.<sup class="fn"><a href="#n93" id="ref-93b">93</a></sup></td>
</tr>
<tr>
  <td>Maldon, Essex (John, bachelor s/o Francis G14)</td>
  <td>Essex</td>
  <td>(unmarried)</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Bachelor of St Mary's Maldon: 1674 hearth tax on nine hearths; letters of administration granted to brother Thomas Gurney 1681; second son named John in Francis G14's Anne Browning marriage.<sup class="fn"><a href="#n108" id="ref-108a">108</a></sup></td>
</tr>
<tr>
  <td>East Chiltington, Sussex</td>
  <td>Sussex</td>
  <td>Unknown</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Died in England (probate PROB 11/241/246 and PROB 11/242/723); shepherd.<sup class="fn"><a href="#n60" id="ref-60g">60</a></sup></td>
</tr>
<tr>
  <td>East Grinstead, Sussex</td>
  <td>Sussex</td>
  <td><strong>Dorothy</strong></td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Died in England (will proved 1654, PROB 11/252/319); yeoman.<sup class="fn"><a href="#n60" id="ref-60e">60</a></sup></td>
</tr>
<tr>
  <td>Stepney / Wapping, London (Mariner)</td>
  <td>Middlesex</td>
  <td><strong>Elizabeth</strong></td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Alive in 1633 England (John Garnes, mariner of "Nere Ye Hermitage," Wapping; son John baptized St John, Wapping, 6 January 1633, mother Elizabeth). Wife Elizabeth, not Mary; mariner trade.<sup class="fn"><a href="#n94" id="ref-94a">94</a></sup></td>
</tr>
<tr>
  <td>Stepney, St Dunstan (John + Rose)</td>
  <td>Middlesex</td>
  <td><strong>Rose</strong></td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Alive in 1654 England (son John buried St Dunstan, Stepney, 21 January 1654, parents John and Rose Gurney). Wife Rose, not Mary.<sup class="fn"><a href="#n94" id="ref-94b">94</a></sup></td>
</tr>
<tr>
  <td>St Gregory by St Paul's, London (licence)</td>
  <td>London</td>
  <td><strong>Jane</strong> Underwood</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Trade mismatch (yeoman of St Clement Danes, London) with the colonial tailor; 1626 marriage to Jane Underwood of St Andrew, Holborn.<sup class="fn"><a href="#n94" id="ref-94c">94</a></sup></td>
</tr>
<tr>
  <td>St Dunstan in the West, London (Henry's son)</td>
  <td>Middlesex</td>
  <td>-</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Died in England (infant son of Henry Gurney, buried St Dunstan in the West 26 March 1648). Father Henry Gurney is a separately documented London household; see held-review notes.<sup class="fn"><a href="#n94" id="ref-94d">94</a></sup></td>
</tr>
<tr>
  <td>St Olave Old Jewry, London</td>
  <td>London</td>
  <td>Unknown</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Died in England (Jn Gourny, buried St Olave Old Jewry 1665).<sup class="fn"><a href="#n94" id="ref-94e">94</a></sup></td>
</tr>
<tr>
  <td>St Margaret, Westminster</td>
  <td>Middlesex</td>
  <td>Unknown</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Died in England (John Gurney, buried St Margaret Westminster 11 September 1675).<sup class="fn"><a href="#n94" id="ref-94f">94</a></sup></td>
</tr>
<tr>
  <td>Vintry 6th precinct, London (Edward)</td>
  <td>London</td>
  <td>Unknown</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Edward Gurney, Vintry 6th precinct, 9 hearths, 1662 (TNA E 179/367/8 Part 1, m 16); substantial London merchant household continuing in England.<sup class="fn"><a href="#n110" id="ref-110a">110</a></sup></td>
</tr>
<tr>
  <td>All Hallows Staining, London (Richard, wine cooper)</td>
  <td>London</td>
  <td>Unknown</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Richard Gurney, wine cooper, All Hallows Staining, Elme Chapell Court, 3 hearths, 1666; continuing London residence.<sup class="fn"><a href="#n110" id="ref-110b">110</a></sup></td>
</tr>
<tr>
  <td>St Alban Wood Street, London (Christopher)</td>
  <td>London</td>
  <td>Unknown</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Christopher Gurney, St Alban Wood Street, Hobs Alley, 5 hearths, 1666; forename Christopher; continuing London residence.<sup class="fn"><a href="#n110" id="ref-110c">110</a></sup></td>
</tr>
<tr>
  <td>St Bride Fleet Street, London (William, 7 hearths)</td>
  <td>London</td>
  <td>Unknown</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>William Gurny, St Bride Fleet Street, Southside Fleet Street, 7 hearths, 1666, "empty"; continuing London residence household within the London William Gurney cluster (see also Cock & Key Alley William and PROB 11/252/152).<sup class="fn"><a href="#n98" id="ref-98b">98</a></sup> <sup class="fn"><a href="#n110" id="ref-110d">110</a></sup></td>
</tr>
<tr>
  <td>Stepney, Shadwell, Middlesex (Edward)</td>
  <td>Middlesex</td>
  <td>Unknown</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Edward Gurney, Stepney, Hamlet of Shadwell, Cutthroat Lane, 2 hearths, 1666, "Em" (empty); continuing English residence. May be the same person as Vintry 1662 Edward in a downshifted household.<sup class="fn"><a href="#n110" id="ref-110e">110</a></sup></td>
</tr>
<tr>
  <td>St Margaret's Westminster (Walter)</td>
  <td>Middlesex</td>
  <td>Unknown</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Walter Gurney, St Margaret's Westminster, Greene Dragon Court, 1 hearth, 1664; most plausibly the Walter Gurney son of William Gurney in PROB 11/252/152 (see also n98).<sup class="fn"><a href="#n98" id="ref-98c">98</a></sup> <sup class="fn"><a href="#n110" id="ref-110f">110</a></sup></td>
</tr>
<tr>
  <td>Lidlington, Beds</td>
  <td>Bedfordshire</td>
  <td>Unknown</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Died in England (John Gurney "Senr.," buried Lidlington St Margaret 28 February 1674).<sup class="fn"><a href="#n94" id="ref-94g">94</a></sup></td>
</tr>
<tr>
  <td>Houghton Regis, Beds</td>
  <td>Bedfordshire</td>
  <td><strong>Elizabeth</strong></td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Wife Elizabeth, not Mary. Marriage in c.1640 (Houghton Regis All Saints, 23 June 1640/41).<sup class="fn"><a href="#n94" id="ref-94h">94</a></sup></td>
</tr>
<tr>
  <td>Norwich, St Michael At Thorn (clergyman)</td>
  <td>Norfolk</td>
  <td>-</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Died in England (Mr John Girny, occupation Clerke, monumental inscription 17 December 1640, Norwich St Michael At Thorn). Clergyman.<sup class="fn"><a href="#n94" id="ref-94i">94</a></sup></td>
</tr>
<tr>
  <td>Norwich, St Lawrence</td>
  <td>Norfolk</td>
  <td>Unknown</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Died in England (John Garrne, buried Norwich St Lawrence 27 November 1641).<sup class="fn"><a href="#n94" id="ref-94j">94</a></sup></td>
</tr>
<tr>
  <td>Mickfield / Morningthorpe, Suffolk-Norfolk (Garneys gentry)</td>
  <td>Suffolk</td>
  <td>-</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Died in England. Garneys gentry: John Garneys gentleman of Mickfield, Suffolk, will 1675 (NCC Wiseman 196); buried Morningthorpe with Fritton, Norfolk, 17 December 1661.<sup class="fn"><a href="#n94" id="ref-94k">94</a></sup></td>
</tr>
<tr>
  <td>Warfield, Berks</td>
  <td>Berkshire</td>
  <td>-</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Died in England (John Guerne, buried Warfield 1674, son of Francis Guerne). Father Francis, not the colonial John's profile.<sup class="fn"><a href="#n94" id="ref-94l">94</a></sup></td>
</tr>
<tr>
  <td>Sulhamstead Bannister, Berks</td>
  <td>Berkshire</td>
  <td>Unknown</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Alive in 1658 England (John Gurney baptized Sulhamstead Bannister 1658, father John Gurney). Father John of this household was still resident at Sulhamstead in 1658, after the colonial John's June 1641 Weymouth appearance.<sup class="fn"><a href="#n94" id="ref-94m">94</a></sup></td>
</tr>
<tr>
  <td>Upton on Severn, Worcs</td>
  <td>Worcestershire</td>
  <td>Unknown</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Died in England (John Gurney, buried Upton on Severn St Peter & St Paul 19 January 1666). Out of the Norfolk-to-Massachusetts emigration corridor.<sup class="fn"><a href="#n94" id="ref-94n">94</a></sup></td>
</tr>
<tr>
  <td>Abthorpe, Northants (labourer)</td>
  <td>Northamptonshire</td>
  <td>Unknown</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Died in England (John Gurney, labourer, will 1664, Archdeaconry Court of Northampton, Series 4TH, Book 6, fol. 260). Labourer trade; distinct from the Candidate A Northants tenancy at Walgrave.<sup class="fn"><a href="#n94" id="ref-94o">94</a></sup></td>
</tr>
<tr>
  <td>London Merchant Taylor apprentice (Moborne, Worcestershire 1602)</td>
  <td>London</td>
  <td>—</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>John Gurney son of William, Glover deceased, of "Moborne," Worcestershire, bound 13 September 1602 to James Briggs of Shoe Lane (Merchant Taylor binding-book vol. 3b, no. 852, p. 114). Bound 1602 → would be too old by 1641 Weymouth; father William not Francis; not the Norfolk corridor.<sup class="fn"><a href="#n95" id="ref-95a">95</a></sup></td>
</tr>
<tr>
  <td>London Merchant Taylor apprentice (Aylesbury, Bucks 1655)</td>
  <td>London / Bucks</td>
  <td>—</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>John Gurny son of John, Ironmonger of Aylesbury, Bucks, bound 30 May 1655 to Alexander Harbin of Gracechurch Street (Merchant Taylor binding-book vol. 14, no. 514, p. 67). Date too late for a 1641 Massachusetts emigrant; same Aylesbury Vale cluster as §8.1 / §8.3.<sup class="fn"><a href="#n95" id="ref-95b">95</a></sup></td>
</tr>
<tr>
  <td><strong>1636 Newgate apprentice (Winthrop/Savage)</strong></td>
  <td>Suffolk → Boston</td>
  <td>—</td>
  <td><span class="badge-eliminated">ELIMINATED</span></td>
  <td>Implied birth c.1615 (1636 court order, service to age 24). Chronologically incompatible with the colonial John's c.1602/3 (1653 deposition). See §8.5.<sup class="fn"><a href="#n99" id="ref-99a">99</a></sup></td>
</tr>
</tbody>
</table>
```

Five rows tagged `class="status-probable"` (Candidate B) or `class="status-unlikely"` (Aylesbury Cowheard, Amersham, Hitcham, Norwich Jane Wright, Ackworth) get colored backgrounds. The remaining 40+ rows are ELIMINATED and stay default.

---

## 4. Pre-apply integrity checks

- `grep -n '<table class="facts-baseline">' research/case-files/john-gurney-case-file-v4.md` → exactly 1 match.
- `grep -n '<table class="candidates-table">' research/case-files/john-gurney-case-file-v4.md` → exactly 1 match.
- `grep -cE 'class="status-(probable|unlikely)"' research/case-files/john-gurney-case-file-v4.md` → exactly 6 (Candidate B + Aylesbury Cowheard + Amersham + Hitcham + Norwich Jane Wright + Ackworth).
- `grep -cE 'class="badge-(probable|unlikely|eliminated)"' research/case-files/john-gurney-case-file-v4.md` → should equal the §8 row count plus any §11 status references (the §11 probability table stays markdown for v50; adapt later if desired).
- Build the site and visually confirm: §1 table Detail column is roughly 2× the Source column width; §8 row 1 (Candidate B) is pale blue; rows for Aylesbury Cowheard, Amersham, Hitcham, Norwich Jane Wright, Ackworth are a slightly lighter pale blue; all other rows default white.

## Reviewer checklist

- [ ] CSS additions inserted in `site/website/assets/site.css` under the `.case-page` selector
- [ ] §1 facts table converted from markdown pipe-table to `<table class="facts-baseline">` HTML; all nine rows preserved verbatim with footnote refs intact
- [ ] §8 elimination table converted from markdown pipe-table to `<table class="candidates-table">` HTML; all current rows preserved verbatim; row count unchanged
- [ ] `class="status-probable"` set on the Candidate B row only
- [ ] `class="status-unlikely"` set on the four Unlikely rows (Aylesbury Cowheard, Amersham, Hitcham, Norwich Jane Wright, Ackworth)
- [ ] Status cell content wrapped in `<span class="badge-probable|unlikely|eliminated">` on every row
- [ ] Built site renders the expected coloring on the published case-file page
- [ ] No body prose, no footnote text, and no §8 row content changes in v50 (all row simplification work happens in v51)
