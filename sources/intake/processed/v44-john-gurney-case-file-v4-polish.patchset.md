# Intake patchset v44 — John Gurney case file v4 polish (REVISED)

**Prepared:** 2026-05-16 (revised 2026-05-16)
**Repo:** `allengurney/gurney-genealogy`
**Target branch:** `main`
**Target files:**
- `research/case-files/john-gurney-case-file-v4.md` (in-place edits — primary)
- `research/people/g13-john-gurney-fact-sheet.research.md` (receive five colonial-side supplemental blocks moved out of §10.7)

**Status:** APPLIED 2026-05-16.

**Application notes:**
- Candidate B probability anchored at ~60% (not ~65%) in both §8 and §11 per reviewer direction; other Unlikely probabilities left at their per-row 2-5% values.
- 8 strategic companion cross-links surfaced in case-file body (§2.1, §4.2, §5.1, §8.4, §8.5, §10.6, §10.7, §11 D-row).
- All five §10.7 supplemental h4 blocks deleted; companion already carries parallel content under existing sections (Find a Grave / Elm Street; Torrey marriage compendium; Mendon-Braintree-Weymouth land baseline; Cheny/Gurney conflict; American arms / Lysander). No companion-side additions were necessary.
- Case file: 720 → 706 lines after polish (net reduction; main savings from §10.7 h4 block relocations and §4.2 prose tightening, balanced by the new §8.5 Newgate subsection).
- One additional cleanup beyond patchset items: "G14" body-prose shorthand stripped from §2.4 ("Francis G14's child list") and §10.2 ("Francis G14's combined Norfolk-and-London profile") for plain-reader clarity. G14 / G13 internal shorthand retained inside §12 working-target lists and inside footnotes.

## Revision history

This is a corrected rewrite of the prior v44 draft. Key reviewer corrections folded in:
- Probabilities now match across §8 and §11.
- `Candidate D is held as Unlikely (~3-5%)` in §8.4 body and `ELIMINATED (probable)` on the Bury row are factual errors and are fixed.
- §3 timeline cells trimmed to event only; "household event; relationship class reads as niece, not daughter" replaced with "likely niece."
- "FS" and register page/image IDs removed from body text; they live in footnotes.
- All language describing the *history of the case file itself* removed (`previously read`, `earlier indexing`, `initially attributed`, `earlier children-search line of reasoning`, `case file does not currently fix`). The body presents current state only.
- §10.7 supplemental `<h4>` blocks relocated to the companion: their content sits in colonial-side / compiled-source territory and does not fit §10.7's For-and-Against table framing.

## Posture

Tighten in place, do not relocate substantive English-origin content. Topic sentence first. Plain English. Footnote-resident facts stay footnote-resident. The case file remains a single cohesive document, and is now structured so that the future #2 collapsible-disclosure UX layer can wrap individual subsections cleanly.

## UX implementation hooks for #2 and #5 (informational)

The following sections are sized and shaped to wrap cleanly in a default-collapsed `<details>` element once the disclosure UX lands:
- §4.2 prose-paragraph (single paragraph after the table)
- §5.1 letterform-evidence summary
- §5.2 limitations and next steps
- §6.2 Peter anomaly
- §8.3 Bucks same-county cluster (large bullet list)
- §8.5 1636 Newgate apprentice subsection
- §10.6 second paragraph (Bury 1653-1656 burials)
- §12 Round-6 highest-leverage targets

The §10.7 evidence-summary For/Against tables themselves stay always-open — they are the persuasion ledger.

No JS or template changes are made by this patchset; the structural shape only.

---

## 0. Section-anchor renumber

Renumber anchors so anchor ID matches section number: `s2..s13` → `s1..s13`. Update front-matter `caseNav` href list to match. Labels stay text-only.

| Section | Old | New |
|---|---|---|
| 1. PROBLEM STATEMENT | `s2` | `s1` |
| 2. THE CANDIDATE | `s3` | `s2` |
| 3. MASTER TIMELINE | `s4` | `s3` |
| 4. EAST DEREHAM REGISTER | `s5` | `s4` |
| 5. PROBABLE BAPTISM | `s6` | `s5` |
| 6. JOHN-1'S FAMILY | `s7` | `s6` |
| 7. ANN GURNEY / GILMAN | `s8` | `s7` |
| 8. PROCESS OF ELIMINATION | `s9` | `s8` |
| 9. TWO FRANCIS GURNEYS | `s10` | `s9` |
| 10. THE EVIDENCE | `s11` | `s10` |
| 11. PROBABILITY ASSESSMENT | `s12` | `s11` |
| 12. WHAT'S STILL NEEDED | `s13` | `s12` |
| 13. BIBLIOGRAPHY | `notes` | `s13` |

Pre-apply check: `grep -r "#s[0-9]\|#notes\b" .` to catch external linkbacks.

---

## 1. Textile-trade phrasing — three locations

Candidate D shares the textile trade. The absolute phrasing comes down. Argument stays distinctive on Norfolk corridor and continuing-London-residence grounds.

**1a — §2 candidate-table "Occupational match" row:**

Old: `Francis was a Merchant Taylor; John-1 was a tailor — no other candidate has any textile-trade connection`

New: `Francis was a Merchant Taylor; John-1 was a tailor. Only Candidate D shares any textile-trade link, and Candidate D stays in London (see §8.4).`

**1b — §10.1 first paragraph, second-to-last sentence:**

Old: `**No other identified candidate has any documented connection to the tailoring or textile trades.** The Stewkley Gurneys were landholders; the Kent and Sussex Johns were yeomen and shepherds.`

New: `**Only Candidate D shares a textile-trade link** — a London draper-tailor in the Old Change household of Robert Gurney — and Candidate D remains in London through at least 1638 (see §8.4). Most other eliminated candidates were landholders, yeomen, or shepherds.`

**1c — §10.7 For-table row 1, Explanation cell:**

Old: `Trades passed through family apprenticeship. No other candidate has any known textile-trade connection.`

New: `Trades passed through family apprenticeship. Only Candidate D shares a textile-trade link, and Candidate D's continuing London residence rules him out (see §8.4).`

---

## 2. §2.1 — drop the two-week MT freedom discrepancy from body

The Company binding book is the primary record. Use its date.

**§2.1 second paragraph (currently the long one with the two-week discrepancy) — replace:**

Old:
> Francis was bound apprentice in London on 14 May 1599, aged about seventeen, to Henry Tryme of the Merchant Taylors' Company "Near Ludgate," for a seven-year term beginning at Whitsun 1599. On 3 February 1605 the Company Court ordered him assigned over to William Smooth, Merchant Taylor of Lothbury, "with a report of good service from his first master on the grounds that he is due to take a journey into the north and not likely to return until Michaelmas" — a documented multi-month northward absence in 1605, six years before his September 1611 Norwich marriage to Margaret Rybett and the earliest concrete trace of his Norfolk re-engagement.<sup class="fn"><a href="#n13" id="ref-13">13</a></sup> Daniel Gurney's *Supplement* (Note 181) records his admission to the freedom of the Merchant Taylors' Company on 16 June 1606 — "Francis Gurnay son of Henry Gurnay of Great Ellinggam in the County of Norfolk was admitted and sworn to the Freedom of the Merchant Tailors' Company" — while the Company's own binding-book transcription (Scott 2024, UKDA-SN-9263) records the freedom on 30 June 1606. The two-week discrepancy is unresolved and most likely reflects a single-character transcription error in Daniel; reconciliation against the Guildhall MS register is pending.<sup class="fn"><a href="#n14" id="ref-14">14</a></sup>

New:
> Francis was bound apprentice in London on 14 May 1599, aged about seventeen, to Henry Tryme of the Merchant Taylors' Company "Near Ludgate," for a seven-year term beginning at Whitsun 1599. On 3 February 1605 the Company Court ordered him assigned over to William Smooth, Merchant Taylor of Lothbury, ahead of a documented multi-month journey into the north — the earliest concrete trace of his Norfolk re-engagement, six years before his September 1611 Norwich marriage to Margaret Rybett.<sup class="fn"><a href="#n13" id="ref-13">13</a></sup> The Merchant Taylors' Company binding book records his admission to the freedom of the Company on 30 June 1606.<sup class="fn"><a href="#n14" id="ref-14">14</a></sup>

(n14 already carries the Daniel-Gurney 16 June vs UKDA 30 June reconciliation. No footnote-text change.)

---

## 3. §3 Master Timeline — full table replacement

Fixes folded in: date order corrected; Francis-children dates corrected to match §4.2; "family relocates" expressed as date range; 1661 cells stripped to facts; trailing event-letter parens dropped; "likely niece" plain language; freedom-date conflict line collapsed to the primary date.

**Replace the entire §3 table with:**

```markdown
| Date | Francis Gurney (Father) | John Gurney-1 (Son) |
|---|---|---|
| 13 Sept 1581 | Born, West Barsham Hall, Norfolk (twin with Anthony) | — |
| **14 May 1599** | Bound apprentice to Henry Tryme, Merchant Taylor of Near Ludgate, 7 yrs (started Whitsun 1599) | — |
| **3 Feb 1605** | Transferred to William Smooth, Merchant Taylor of Lothbury, ahead of a six-month "journey into the north" — earliest documented Norfolk re-engagement | — |
| 30 June 1606 | Freed as Merchant Taylor | — |
| c.1606–1611 | Commercial career continues at Norwich; Lestrange agent | — |
| c.1609/10 | At East Dereham, Norfolk | Born at East Dereham (date ±1–2 yrs) |
| **23 Sept 1611** | **Marries Margaret Rybett, St Martin at Palace, Norwich ★** | Possibly infant; potentially born before marriage |
| c.1611/12 | Edward baptized, East Dereham | — |
| Jan 1612 | First documented Lestrange payment | — |
| c.1615 / Jan 1616 | Marye (likely niece) buried, East Dereham | — |
| 31 Jan 1616 | Agnes buried, East Dereham | Age c.6–7 |
| **22 April 1616** | Takes Francis Spelman as apprentice (£100 bond from Sir Henry Spelman of Middleton, Norfolk) | — |
| c.1616–1617 | **Margaret Rybett dies** (burial not found) | Age c.6–8 |
| c.1617 | Marries Anne Browning | — |
| 25 May 1618 | Marye baptized, East Dereham (Anne Browning's first child) | Age c.8–9 |
| **c.1618–1619** | **Family relocates from East Dereham to London** | Family moves with father |
| 2 March 1619 | Dorothy baptized, St Benet Fink, London | — |
| 1619–1637 | Six more children baptized at St Benet Fink | Growing up in or near London |
| c.1622–1625 | King's Lynn manufacturing venture fails | — |
| **1 Oct 1626** | — | **Sister Ann marries John Gilman, Hingham, Norfolk** |
| c.1628–1630 | — | **John marries Mary (surname unknown)** |
| c.1628–1635 | — | Children born in England (Sarah, Mary, Richard, John Jr.) |
| 1633 | Heralds' Visitation of London — Francis attests pedigree | — |
| **8 Nov 1633** | Francis (probable son) buried, East Dereham | — |
| **11 July 1634** | **Sells all Norfolk and Suffolk lands for £1,000** | No inheritance to expect |
| May 1636 | Last Lestrange payment | — |
| 1638 | Absent from 1638 Inhabitants of London survey | — |
| c.1638–1641 | — | **Emigrates to Massachusetts** |
| June 1641 | — | First Massachusetts record: fined at Weymouth |
| May 1645 | — | Signs petition for new plantation at Braintree |
| 3 July 1646 | Annuity record ("during his life") | Settled at Braintree |
| **9 Jan 1646/7** | **Dies, buried St Botolph Bishopsgate, London** | — |
| 1653 | — | Wilson v. Faxon deposition: "aged about 50 years" |
| 12 Feb 1661 | — | Sells Braintree land (deed witnessed by John Jr.) |
| 20 Sept 1661 | — | Wife Mary dies, Braintree |
| 12 Nov 1661 | — | Marries Grizzell Fletcher/Kidbee, Braintree |
| 1662/3 | — | **Dies, Braintree** |
```

---

## 4. §4.2 — heading rename, table cleanup, body-paragraph rewrite

**4a — Heading rename.**

Old: `### 4.2 Confirmed Francis Gurney/Gurnie Baptisms at East Dereham`

New: `### 4.2 Francis Gurney Events at East Dereham (Baptisms and Burials)`

**4b — Table replacement.** Drop the Page/Image column (image and FS-index identifiers live in n96 and n102). Clean the Entry B and Entry C cells to plain language. Replace certainty annotations with plain values.

```markdown
| Entry | Child | Event | Date | Certainty |
|---|---|---|---|---|
| **A** | Edward | Baptism | c.1611/12 | Confirmed<sup class="fn"><a href="#n96" id="ref-96a">96</a></sup> |
| **B** | Marye (likely niece) | Burial | late 1615 or January 1616 | Confirmed event<sup class="fn"><a href="#n96" id="ref-96b">96</a></sup><sup class="fn"><a href="#n102" id="ref-102a">102</a></sup> |
| **C** | Agnes, daughter of Francis Gurney | Burial | 31 January 1616 | Confirmed<sup class="fn"><a href="#n96" id="ref-96c">96</a></sup><sup class="fn"><a href="#n102" id="ref-102b">102</a></sup> |
| **D** | Marye, daughter of Francis Gurney | Baptism | 25 May 1618 | Confirmed<sup class="fn"><a href="#n102" id="ref-102c">102</a></sup> |
| **E** | **John** | **Baptism** | **c.1609/10** | **Probable** |
| **F** | Francis (probable son) | Burial | 8 November 1633 | Probable<sup class="fn"><a href="#n96" id="ref-96d">96</a></sup> |
```

**4c — Body prose after the table.** Replace the two long paragraphs (current lines 172 and 174) and the date-margin paragraph (line 176) with a single tight paragraph:

```markdown
Edward (c.1611/12), Agnes (31 January 1616 as "the daughter of ffrancis Gurny"), and the later Marye (25 May 1618, Anne Browning's first child) are confirmed children of Francis Gurney at East Dereham. The earlier Marye at Entry B is likely a niece — the relationship word in the register does not read as "daughter." Entry F (Francis, 8 November 1633) is a probable son: Francis Gurney was resident at East Dereham, no other documented Francis Gurney of the period fits the date, and Francis re-used the name when a second Francis was baptized at St Benet Fink in 1628. Entry E — John, c.1609/10 — is the central paleographic finding and is examined in §5. Most date estimates carry a ±2-3 year margin where the register's year was not visible at the page level.<sup class="fn"><a href="#n96" id="ref-96e">96</a></sup><sup class="fn"><a href="#n102" id="ref-102d">102</a></sup>
```

(No new footnotes. n96 and n102 already carry the image-walk, FS index IDs, page numbers, and paleographic refinement. The earlier bulleted refactor is dropped — it carried body-level page numbers, FS-index labels, and references to "previously read" and "earlier indexing," all of which were out of step with the case-file standard.)

---

## 5. §4.3 and §4.4 — wording tightens

**5a — §4.3 first sentence:**

Old: `Entry E (John, c.1609/10) potentially may predate the Margaret Rybett marriage (23 Sept 1611). Two explanations are possible: the estimated entry's date is wrong by 1–2 years (within the stated margin), or John was born before the marriage. Pre-marital conception was reasonably common in this period.<sup class="fn"><a href="#n45" id="ref-45">45</a></sup> Either scenario is consistent with John being Francis's son.`

New: `Entry E's estimated date (c.1609/10) may predate the Margaret Rybett marriage of 23 September 1611 by one to two years. Two readings fit Francis's paternity: the date estimate is off by one to two years (within the ±2-3 year register margin), or John was born before the marriage. Pre-marital conception was reasonably common in this period.<sup class="fn"><a href="#n45" id="ref-45">45</a></sup>`

**5b — §4.4 paragraph:**

Old: `Entry D (Marye, 25 May 1618) was initially attributed to Margaret Rybett as mother. However, Dorothy Gurnoy was baptized at St Benet Fink, London, on 2 March 1619 — only 9 months later. This is biologically near-impossible if Margaret was Marye's mother and Anne Browning was Dorothy's. Margaret Rybett most likely died c.1616–1617. The 1618 Marye is probably Anne Browning's first child, born before the family relocated to London.<sup class="fn"><a href="#n42" id="ref-42">42</a></sup>`

New: `Margaret Rybett most likely died c.1616-1617. The 1618 Marye baptism cannot be Margaret's child: Dorothy was baptized at St Benet Fink only nine months later, on 2 March 1619 — biologically near-impossible across two different mothers. The 1618 Marye is therefore Anne Browning's first child, born at East Dereham before the family relocated to London.<sup class="fn"><a href="#n42" id="ref-42">42</a></sup>`

---

## 6. §4.5 — delete; move Peter Woodcocke into n33

**Delete** §4.5 (the two lines about Ann Gurney / Peter Woodcocke at West Dereham 1618/19).

**Augment n33** by appending:

```
A separately documented Ann Gurney married Peter Woodcocke at West Dereham, Norfolk, on 8 February 1618/19 (NRO PD 192/2; FreeREG transcription). Whether this Ann is the same person as the Ann who married John Gilman in 1626 is unresolved; the case file treats them as potentially distinct.
```

No other §4 subsections renumber.

---

## 7. §5.1 — rewrite without chronology

**Replace §5.1 in full:**

Old:
> ### 5.1 Why the Original Indexing Was Likely Wrong
>
> The original indexing was performed under standard bulk-indexing conditions: a volunteer working through hundreds of entries on degraded microfilm, with no reason to suspect a Gurney entry. Our analysis had the advantage of targeted examination with image enhancement tools and direct cross-referencing against confirmed entries. Four independent letterform tests — initial stroke cluster, mid-body structure, word segmentation, and terminal formation — all favor "ffrancis" over "Nicholas." No test favors "Nicholas."
>
> > **A separate [AI Assistant Procedure for Parish Record Analysis](/key-research/east-dereham-ai-assistant-procedure.html) provides a detailed narrative of this analysis.**

New:
> ### 5.1 Letterform Evidence: ffrancis over Nicholas
>
> Four independent letterform tests favor "ffrancis" over "Nicholas": initial stroke cluster, mid-body structure, word segmentation, and terminal formation. No test favors "Nicholas." The Findmypast/FreeREG index reads "Nicholas Gorne" because the entry sits on degraded microfilm transcribed without targeted attention to the Gurney surname universe; magnified examination against confirmed Gurney entries in the same register and hand resolves to "ffrancis Gurnie."
>
> > A separate [AI Assistant Procedure for Parish Record Analysis](/key-research/east-dereham-ai-assistant-procedure.html) details the analysis.

§5.2 stays as written; it already reads cleanly.

---

## 8. §6.1 — "FS" → "FamilySearch"; rewrite chronology-bearing second paragraph

**8a — first paragraph, replace `FS, Findmypast, and Ancestry` with `FamilySearch, Findmypast, and Ancestry`.** Single token swap.

**8b — second paragraph (currently begins "The earlier children-search line of reasoning"):**

Old: `The earlier children-search line of reasoning — that all five colonial children should be findable in English parish baptisms — should therefore be read as a parish-register-coverage probe rather than a binary identification test. Over 20 baptism records in the names of John Gurney's children were identified in England across this search, but no parish cluster produces all five target children with a father named John Gurney and a mother named Mary (including variant spellings). The closest results are listed below but remain weak matches on dates, mother's name, or both.`

New: `No parish cluster produces all five target children with a father named John Gurney and a mother named Mary (or variant spellings), despite over twenty Gurney baptism records identified across the search. The closest results are listed below; each is a weak match on dates, mother's name, or both. The pattern most likely reflects parish-register coverage gaps in 17th-century East Anglian indexing rather than evidence against any specific origin.`

---

## 9. §6.2 — Peter Anomaly, topic-sentence-up-front

**Replace the §6.2 paragraph:**

Old: `An England-wide FamilySearch search found zero Peter Gurney baptisms 1620-1645. A subsequent Findmypast UK Parish Baptisms search 1632-1642 with surname variants returned twelve Peter Gurney baptism results, including a Peter G., father Peter G., christened 27 February 1641 at Smallburgh, Norfolk (FMP transcript R_880200102; "G." is a partial surname index). The Smallburgh entry is a Norfolk Gurney-variant household using the name Peter in the same decade the colonial John named his son Peter, so the case-file's earlier "Peter is completely foreign to the Gurney surname universe" framing is weakened. Peter as a child of the colonial John remains distinctive -- none of the twelve FMP results match a John-Gurney-father pattern -- but the name was not absolutely absent from Norfolk Gurney households. Mary's maiden family remains the most likely source of the colonial son Peter's name; identifying her maiden name and a Peter in her family would still provide independent confirmation of John-1's origin.<sup class="fn"><a href="#n55" id="ref-55">55</a></sup>`

New: `**Peter is distinctive among colonial John's family, but not absent from Norfolk Gurney households.** A 1641 Smallburgh, Norfolk baptism records a Peter Gurney whose father was also named Peter — a Norfolk Gurney-variant household using the name in the same decade the colonial John named his son Peter. None of the twelve indexed Peter-Gurney-variant baptisms 1632-1642 fathered a John-Gurney child, so Peter as the colonial son's name still calls for an explanation. The most likely source remains Mary's maiden family; identifying her surname and a Peter in her kin would be independent confirmation of John-1's origin.<sup class="fn"><a href="#n55" id="ref-55">55</a></sup>`

---

## 10. §2.3 — tighten the financial-collapse author's note

**Replace the §2.3 closing paragraph:**

Old: `**Author's note:** It is difficult to estimate in today's terms the extent or impact of Francis' financial collapse but it is plausible to estimate that Francis lost the equivalent of $10+ million USD (his entire net worth) over a few short decades. We do not know the cause(s) of such a collapse but one could envision Francis wanting to publicly hide or minimize his personal decline during the the Heralds' Visitation (see next section below).  With John Gurney being ~23 of age at the time, the strain on family during financial struggles, and unknown father-son dynamics could all be interconnected factors. However, with minimal genealogical evidence (either in support or against), this is framed as more anecdotal than a factual genealogical finding.`

New: `Francis's losses were substantial — plausibly equivalent to $10M+ USD in entire net worth over a few decades. The cause is unknown, but the financial strain, the 1633 Visitation, and the 1634 forced land sale all fall within John's late-teens-to-twenties window, and any father-son dynamics around John's emigration would have been shaped by that backdrop.<sup class="fn"><a href="#nA1" id="ref-A1">A1</a></sup>`

**Add new footnote nA1:**

```html
<li id="nA1">Authorial inference, not a sourced finding. The modern-dollar estimate is rough; £1,000 in 1634 has been variously equated to several million pounds sterling in 2020s purchasing-power terms, and Francis's losses across the King's Lynn venture, the Lestrange bond, and the 1634 land sale together suggest a substantially higher figure. Included as context for the emigration decision, not as a genealogical finding. <a class="backref" href="#ref-A1">↩</a></li>
```

---

## 11. §8 elimination table — three fixes

**11a — Candidate B status:** align with §11 (both at ~65%).

Old: `**PROBABLE (~55-60%)**`

New: `**PROBABLE (~65%)**`

**11b — Candidate D status:** drop the range.

Old: `**Unlikely (~3-5%)**`

New: `**Unlikely (~5%)**`

**11c — Bury St Edmunds row:** drop "(probable)" — eliminated is eliminated.

Old: `| Bury St Edmunds, Suffolk | Suffolk | Unknown (1656 widow burial) | **ELIMINATED (probable)** | National Burial Index records three Gurney burials at St Mary, Bury St Edmunds in close sequence: John Gurney 11 December 1653, unnamed Gurney 6 April 1655, unnamed Gurney 13 May 1656 ("Wife"). The household was settled at Bury through the colonial John's 1653 deposition window and beyond. Material to Banks's Bury attribution; see Section 10.6.<sup class="fn"><a href="#n93" id="ref-93b">93</a></sup> |`

New: `| Bury St Edmunds, Suffolk | Suffolk | Unknown (1656 widow burial) | **ELIMINATED** | Continuing Bury household: John buried 1653, Gurney burial 1655, widow buried 1656. The Bury head was not the colonial John. Bears on Banks's Bury attribution; see §10.6 and §8.5.<sup class="fn"><a href="#n93" id="ref-93b">93</a></sup> |`

**11d — Last row (1636 Newgate apprentice):** re-flag as ELIMINATED on chronology; tighten reason; full detail moves to new §8.5.

Old:
```
| **1636 Newgate apprentice (distinct second John)** | Suffolk (likely Bury area) → Boston | — | **Distinct second John; trail lost** | Implied birth c.29 September 1615 from the Winthrop/Savage 21 July 1636 court order setting service until age 24. Chronologically incompatible with the older Braintree John (deposed "aged 50 or thereabouts" 1652/3, born c.1602/3). John Newgate himself was from Horningsheath, Suffolk (~3 mi from Bury St Edmunds), residing later at Hessett, Bury, and Southwark before emigrating 1633; the apprentice was therefore most plausibly a young Suffolk man drawn from Newgate's own region. Banks's "Bury St Edmunds" attribution likely tracks this apprentice rather than the older Braintree John. No separate post-1639 colonial trail surfaces in indexed Massachusetts records for a John Gurney born c.1615; likeliest readings are early-Boston mortality, return to England, or absorption into a non-Gurney surname via marriage. The recurring American family-memory tradition of a 29 September 1615 birth and Southwark origin (Lysander F. Gurney sketch; *American Biography* vol. 26; Find a Grave memorial 252975617) sits cleanly in the apprentice's profile and was later conflated with the older Braintree John by 19th-century compilers.<sup class="fn"><a href="#n99" id="ref-99a">99</a></sup> |
```

New:
```
| **1636 Newgate apprentice (Winthrop/Savage)** | Suffolk → Boston | — | **ELIMINATED** | Implied birth c.1615 (1636 court order, service to age 24). Chronologically incompatible with the colonial John's c.1602/3 (1653 deposition). See §8.5.<sup class="fn"><a href="#n99" id="ref-99a">99</a></sup> |
```

---

## 12. New §8.5 — 1636 Newgate apprentice subsection

**Insert after §8.4:**

```markdown
### 8.5 The 1636 Newgate apprentice — a distinct second John, not the Braintree man

**The 1636 apprentice and the Braintree man are not the same person.** Winthrop/Savage's Addenda records that on 21 July 1636 John Newgate brought his apprentice John Gurney before the Boston governor; the court ordered service until age 24, three years from the following 29 September.<sup class="fn"><a href="#n75" id="ref-75b">75</a></sup> That sets the apprentice's birth at c.29 September 1615 — thirteen years too young to be the colonial John of Braintree, who deposed "aged 50 or thereabouts" in 1652/3 (born c.1602/3).

John Newgate himself was from Horningsheath, Suffolk, three miles from Bury St Edmunds, before emigrating in 1633. The apprentice was most plausibly drawn from Newgate's Suffolk network, which cleanly explains Banks's later Bury St Edmunds attribution: Banks's manuscript memo likely tracked the apprentice rather than the older Braintree John, and nineteenth-century compilers then merged the two Johns into a single biographical sketch.

The recurring American family-memory tradition of a 29 September 1615 birth and Southwark origin — repeated in compiled biographies and online memorials — fits this apprentice, not the colonial John, and should not be carried as a controlling chronology for Candidate B. The apprentice's own post-1639 Massachusetts trail does not surface in indexed records; likeliest readings are early-Boston mortality, return to England, or absorption into a non-Gurney surname via marriage.<sup class="fn"><a href="#n99" id="ref-99a">99</a></sup>
```

(n75 and n99 already carry the underlying source detail.)

---

## 13. §8.4 body — fix "is held as Unlikely"

**§8.4 first paragraph — replace:**

Old: `Candidate D is held as Unlikely (~3-5%) as the Massachusetts emigrant. John Gurney is a tailor born circa 1603 but post-1625 evidence keeps John Gurney in London through at least 1638 and probably 1661 and with no known wife and no matching child set.`

New: `**Candidate D is Unlikely (~5%).** John Gurney, son and executor of Robert Gurney, citizen and draper of Old Change, is a London tailor born about 1603 — but post-1625 evidence keeps him in London through at least 1638 and probably 1661, with no known wife and no matching child set.`

(The §8.4 paragraph following — `Candidate D is John Gurney, son and executor of Robert Gurney, citizen and draper (tailor) of Old Change, London. John was admitted to the Drapers' Company by redemption on 11 February 1623/4 and proved Robert's will on 23 September 1625.` — becomes redundant against the new topic sentence. Delete it and let the next paragraph start with the Robert Gurney apprenticeship-master detail.)

---

## 14. §10.1 — drop the two-MT-Johns sentence (already-stated user item)

**Replace the second paragraph of §10.1:**

Old:
> A first-hand scan of the Merchant Taylors' Company binding books and freedom registers 1583–1800 (Scott 2024, UKDA-SN-9263) qualifies but does not refute this occupational argument. The dataset records **no John Gurney son of Francis Gurney** at any binding in that 217-year window, and **no Gurney patrimony freedom anywhere in the 3,391-row Patrimony sheet**. The two John Gurneys who do appear are eliminable on parentage and date: John Gurney son of William, Glover deceased, of Moborne Worcestershire, bound 1602; and John Gurny son of John, Ironmonger of Aylesbury, bound 1655. If Candidate B holds, John G13's tailoring trade was therefore not transmitted through Francis G14's own livery — neither by formal apprenticeship to a fellow MT master nor by patrimony freedom after Francis's death. Three pathways remain consistent with Candidate B: apprenticeship in a different London livery (Drapers, Clothworkers, Worsted Weavers), apprenticeship at Norwich or to a country tailor, or informal household training. The trade-inheritance line of evidence is therefore weakened from "father MT, son trained as MT" to "father in the trade, son in the trade by some untraced pathway," which is still distinctive among the candidate set but not as tight as a documented MT patrimony freedom would have made it.<sup class="fn"><a href="#n95" id="ref-95">95</a></sup>

New:
> A first-hand scan of the Merchant Taylors' Company binding books and freedom registers 1583-1800 (Scott 2024, UKDA-SN-9263) records **no John Gurney son of Francis Gurney**, and **no Gurney patrimony freedom** anywhere in the 3,391-row Patrimony sheet. The two indexed John Gurneys in those records are not viable candidates on parentage and date. John's trade was therefore not transmitted through Francis's own livery; the likely routes are apprenticeship in a different London livery (Drapers, Clothworkers, Worsted Weavers), apprenticeship at Norwich or to a country tailor, or informal household training. The argument moves from "father MT, son trained as MT" to "father in the trade, son in the trade by an untraced pathway" — still distinctive among the candidate set.<sup class="fn"><a href="#n95" id="ref-95">95</a></sup>

---

## 15. §10.6 — Banks topic-sentence + Bury 1653-1656 rewrite

**15a — §10.6 first paragraph:**

Old: `Charles Edward Banks (1937) placed John at Bury St. Edmunds, Suffolk, within a documented cluster of BSE emigrants. The source was "Banks Mss." only — no primary citation. Anderson's 2025 "Unknown" implicitly rejects this under modern standards. But Banks was perceiving a real pattern: a Norwich-born son of Francis who served a Bury St. Edmunds apprenticeship would be exactly the person Banks described.<sup class="fn"><a href="#n64" id="ref-64">64</a></sup>`

New: `**Banks's Bury St Edmunds attribution is consistent with Candidate B, not against it.** Banks (1937) placed John inside a documented BSE emigrant cluster but sourced the attribution only to "Banks Mss." — no primary record. Anderson's 2025 "Unknown" rejects the attribution under modern standards. The cluster Banks perceived was real; the parish assignment was a working hypothesis. A Norwich-born son of Francis who trained at Bury would fit Banks's note precisely.<sup class="fn"><a href="#n64" id="ref-64">64</a></sup>`

**15b — §10.6 last paragraph (Bury 1653-1656 burials) — rewrite without chronology:**

Old: `The Bury St Edmunds register also carries an active Gurney household across the 1653-1656 window. The National Burial Index records a John Gurney buried at St Mary, Bury St Edmunds on 11 December 1653, an unnamed Gurney burial at the same parish on 6 April 1655, and an unnamed Gurney burial on 13 May 1656 explicitly noted "Wife." The trio reads most naturally as one continuing household: a male John buried 1653, a child or other family member in 1655, and the widow in 1656. This sharpens the Banks reading without overturning it. A Bury-resident John Gurney was buried at Bury exactly in the same calendar year the colonial John gave the Wilson v. Faxon deposition at Braintree, aged about 50. The case file does not currently fix the deposition's month, so the December 1653 Bury burial does not on its own eliminate Banks's Bury-Boston identification; but the household continuity through 1656 implies that the Bury Gurneys remained at Bury rather than emigrating, so Banks's attribution can only stand if the colonial John was an earlier-departing apprentice from this Bury household rather than its head. The Bury parish-register manuscript image is not yet pulled.<sup class="fn"><a href="#n93" id="ref-93c">93</a></sup>`

New: `The Bury Gurney household stayed at Bury rather than emigrating. The National Burial Index records a John Gurney buried at St Mary, Bury St Edmunds on 11 December 1653, a Gurney burial on 6 April 1655, and the widow ("Wife") on 13 May 1656 — three burials in one continuing household. Banks's attribution can therefore only stand if the colonial John was an earlier-departing apprentice from this household, not its head — which fits the §8.5 reading of the 1636 Newgate apprentice cleanly.<sup class="fn"><a href="#n93" id="ref-93c">93</a></sup>`

---

## 16. §10.7 — relocate five supplemental `<h4>` blocks to companion

These five blocks sit in colonial-side or compiled-source territory and do not fit §10.7's English-origin For-and-Against table framing. Move them to `research/people/g13-john-gurney-fact-sheet.research.md`. The relevant points are already represented in §10.7's For-table (rows 9, 16, 17, 18) and in n67, n68, n78–n81, so the persuasive ledger loses nothing.

**16a — Delete from the case file:**

- `<h4>Supplemental burial-place lead: Elm Street Cemetery, Braintree</h4>` and the following `<p>` (cites n68).
- `<h4>Supplemental heraldic family-memory lead: American Gurney arms</h4>` and the following `<p>` (cites n66), plus the Lysander Franklin Gurney `<p>` immediately after it (cites n76).
- `<h4>Torrey and History of Weymouth: cross-checks on the John1 family group</h4>` and the following `<p>` (cites n67).
- `<h4>Colonial land baseline: Weymouth, Braintree, and Mendon</h4>` and the following `<p>` (cites n78, n79, n80).
- `<h4>Braintree vital-record conflict: Cheny/Cheney vs. Gurney</h4>` and the following `<p>` (cites n81).

**16b — Insert one-line companion pointer** in their place at §10.7, immediately after the Against table:

```markdown
For colonial-side context — Braintree burial location, the Cheney/Gurney 1661 vital-record question, the Torrey and *History of Weymouth* family-group cross-checks, the Weymouth/Braintree/Mendon land record, the Lysander Franklin Gurney manuscript pointer, and the American Gurney arms family-memory lead — see the companion file at `research/people/g13-john-gurney-fact-sheet.research.md`.
```

**16c — Companion-side additions.** The companion already covers Find a Grave (n47/n49 of the companion), American Biography arms (n50), Lysander (n52), Newgate-Horningsheath (n79), and Newgate apprenticeship (n67–n75 region). The five blocks largely paraphrase content already there. The two pieces that may not have a clean companion home are:

1. **Torrey + *History of Weymouth* family-group cross-checks** (currently §10.7 `<p>` citing n67) — paste under a new heading `### Torrey and *History of Weymouth* family-group cross-checks` in the companion's "Working Notes" section.
2. **Mendon/Suffolk Deeds/Ballou colonial land baseline** (currently §10.7 `<p>` citing n78/n79/n80) — paste under a new heading `### Colonial land baseline: Weymouth, Braintree, and Mendon` in the companion's "Working Notes" section.

The other three (Elm Street, American arms, Cheney conflict) have parallel companion content already. Preserve the case-file footnote anchors (n66, n67, n68, n76, n78, n79, n80, n81) — they may still be referenced by other body text and by the For/Against tables. No footnote-text changes required.

---

## 17. §11 Probability Assessment — align with §8

**Replace §11 table cells:**

| Row | New |
|---|---|
| B — Son of Francis & Margaret Rybett | `**~65%**` (was `~65-70%`) |
| A — Stewkley / Bierton / Aylesbury → Northants | `**ELIMINATED**` (no change) |
| C — Berkhamsted, Herts | `**ELIMINATED**` (no change) |
| D — Son of Robert Gurney, draper of Old Change | `**Unlikely (~5%)**` (was `Unlikely (~3-5%)`) |
| Other named candidates | `**~5% combined**` (no change) |
| Unknown corridor (East Anglia / London) | `**~15%**` (was `~15-20%`) |
| Unknown other corridor (Kent, Lincs, West Country) | `**~10%**` (was `~5-10%`) |
| 1636 Newgate apprentice (distinct second John) | `**~5%**` (was `~3-5%`) |

**Newgate row Basis cell — align with §8.5:**

Old: `If Banks's BSE attribution genuinely tracks a separate apprentice whose post-1639 colonial trail is lost, this remains a residual reading. Treated independently of Candidate B because the apprentice is born c.1615 and chronologically incompatible with the older Braintree John (born c.1602/3 per the 1653 deposition).`

New: `Residual scenario in which Banks's BSE attribution tracks a separate apprentice (born c.1615) whose post-1639 Massachusetts trail is lost. Independent of Candidate B; eliminated as the colonial John on chronology grounds. See §8.5.`

Numbers sum to ~100% (B 65 + D 5 + Other 5 + Unknown corridor 15 + Unknown other 10 = 100). The Newgate-apprentice row sits outside that 100 as an independent residual scenario, as the basis cell notes.

---

## Errors and minor mis-statements found during full re-read

- **§2 candidate-introduction table footer** ends with `Candidate B strongly matches nearly all of the key criteria.` — fine; no change.
- **§4.1 first paragraph** mentions "69 microfilm images (pages 700–768)" — this is process detail. Recommend trimming to `A comprehensive review of the East Dereham parish register (NRO PD 86/41, 1593–1641) identifies six Gurney entries that bear on Francis Gurney's children. Approximately one-quarter of the register's entries are too degraded for confident reading.` — adds clarity without losing the methodological caveat. Apply if you agree.
- **§6.3 last sentence** has `Or John and his siblings may have been estranged from their father (Francis) which also could account for them not being included in the 1630's Herald's Visitation report.` — small grammar issue ("1630's" → "1633"). Recommend: `Or John and his siblings may have been estranged from their father, which could also account for their absence from the 1633 Heralds' Visitation.`
- **§8.1 fifth bullet** at line 316 — `**Tenancy, 1650.** John Gurney listed as tenant at Walgrave, Northamptonshire.` — fine.
- **§9 last paragraph** about the 1640 Francis Garney joiner — fine.
- **§10.3** paragraph 1 third sentence: `Braintree, Massachusetts itself was named after Braintree, Essex.` — fine but borderline trivia. Could trim. Leave as-is unless you want it tightened.
- **§12** Section heading reads "12. WHAT'S STILL NEEDED" — fine. The "Round 6+ targets" subsection numbering is consistent.

## Reviewer checklist (revised)

- [ ] Probability anchors at ~65% (Candidate B) and ~5% (Candidate D) in both §8 and §11
- [ ] §8 final-row Newgate apprentice flagged **ELIMINATED** with <30-word reason; full detail at new §8.5
- [ ] §8 Bury St Edmunds row reads **ELIMINATED** (not "ELIMINATED (probable)")
- [ ] §8.4 body sentence reads "Candidate D is Unlikely (~5%)" with topic-sentence-up-front
- [ ] §3 timeline cells contain event only — no entry-letter parens, no paleographic jargon, no register-year OS labels
- [ ] §4.2 table drops the Page/Image column; image and FS-index IDs live in n96/n102 only
- [ ] §4.2 prose after the table is a single tight paragraph with no register-page IDs or "FS" tokens in body
- [ ] §5.1 heading and prose carry no "original indexing" / "earlier" / "our analysis" chronology language
- [ ] §6.1 expands `FS` to `FamilySearch` and rewrites the "earlier children-search line of reasoning" paragraph
- [ ] §10.7 five supplemental `<h4>` blocks deleted from the case file; one-line companion pointer in their place; companion receives Torrey/Weymouth and colonial-land-baseline additions
- [ ] Anchor renumber `s2..s13` → `s1..s13` (and `notes` → `s13`) propagated through both section headings and the `caseNav` href list
- [ ] §6.3 1630's typo corrected
- [ ] §4.1 microfilm-page detail trimmed (optional — flag your preference)
- [ ] nA1 footnote inserted for the §2.3 author's-note tightening; renumber-safe placement in the citation index
