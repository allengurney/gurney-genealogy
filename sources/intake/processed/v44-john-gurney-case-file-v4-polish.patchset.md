# Intake patchset v44 — John Gurney case file v4 polish: persuasion, length discipline, and structural fixes

**Prepared:** 2026-05-16
**Repo:** `allengurney/gurney-genealogy`
**Target branch:** `main`
**Target files:**
- `research/case-files/john-gurney-case-file-v4.md` (in-place edits — primary)
- `research/people/g14-francis-gurney-fact-sheet.research.md` (one small surfacing note in companion)

**Status:** Draft patchset for review. **Do NOT apply until approved.** No content here is to be promoted into research or data files until the user signs off on the edits.

---

## Scope and posture

This is a content-polish patchset, not an intake from external sources. The case file's facts and citations are not being re-derived; the goal is persuasion, brevity, topic-sentence discipline, structural correctness, and a handful of factual corrections the user identified.

Posture: **tighten, do not relocate wholesale.** Substantive content stays in the case file. Detail moves to footnotes where it is mechanical or peripheral. Heading and table-cell text gets shortened. The §4.2 East Dereham analysis stays in the body but is tightened by table-leveraging and prose simplification.

The 8 user-specified items, plus the section-anchor renumber, plus six tightening passes the user invited me to identify, are itemized below. Each item gives an exact location, exact old text (where applicable), and exact new text.

## UX ideation appendix (non-binding — for separate conversation)

Per the user's invitation, lightweight UX ideas that would improve consumability without breaking the "single cohesive document" preference. None of these are implemented in this patchset.

1. **Sticky TL;DR card** at the very top, above §1: 3 bullets — the question, the candidate, the headline probability. Reader oriented in 15 seconds.
2. **Collapsible "Detail" disclosures** inside heavy subsections (§4.2 paleographic walk, §8.3 Bucks cluster, §10.6 Banks paragraph). Default-collapsed `<details>` blocks keep the cohesive document but let casual readers skim past depth without losing access.
3. **Evidence-ledger side panel** — render §10.7's For/Against tables as a sticky sidebar on wide screens so the reader sees the running ledger while reading the narrative. Falls back to inline tables on narrow screens.
4. **Inline candidate badges** — small colored chips inline ("Candidate B — Probable", "Candidate D — Unlikely") so any mid-paragraph mention of a candidate is self-anchoring without forcing a re-read of §8.
5. **"Jump to citation" affordance** — clicking a footnote opens a hover-card on desktop instead of jumping the page, so readers don't lose their place. Backrefs already exist; this is presentational.

These are seeds, not specs. Continue separately.

---

## Section anchor renumber (item 0)

Current anchors are off by one: §1 has `id="s2"`, §13 has `id="notes"`. Relabel so anchor and section number agree.

**File:** `research/case-files/john-gurney-case-file-v4.md`

| Section | Old anchor | New anchor |
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
| 13. BIBLIOGRAPHY | `notes` | `s13` (keep `notes` as a secondary anchor if needed for backrefs; primary becomes `s13`) |

Also update the `caseNav` front-matter `href` values to match the new anchors. The labels themselves stay text-only per user direction.

**Front-matter `caseNav` block — replace:**

```yaml
caseNav:
  - { label: "Problem Statement", href: "#s2" }
  - { label: "Candidate", href: "#s3" }
  - { label: "Timeline", href: "#s4" }
  - { label: "East Dereham", href: "#s5" }
  - { label: "Baptism", href: "#s6" }
  - { label: "Family", href: "#s7" }
  - { label: "Sister", href: "#s8" }
  - { label: "Other Johns", href: "#s9" }
  - { label: "Two Francises", href: "#s10" }
  - { label: "Evidence", href: "#s11" }
  - { label: "Probability", href: "#s12" }
  - { label: "Next Steps", href: "#s13" }
  - { label: "Bibliography", href: "#notes" }
  - { label: "Citations", href: "#citation-index" }
```

**With:**

```yaml
caseNav:
  - { label: "Problem Statement", href: "#s1" }
  - { label: "Candidate", href: "#s2" }
  - { label: "Timeline", href: "#s3" }
  - { label: "East Dereham", href: "#s4" }
  - { label: "Baptism", href: "#s5" }
  - { label: "Family", href: "#s6" }
  - { label: "Sister", href: "#s7" }
  - { label: "Other Johns", href: "#s8" }
  - { label: "Two Francises", href: "#s9" }
  - { label: "Evidence", href: "#s10" }
  - { label: "Probability", href: "#s11" }
  - { label: "Next Steps", href: "#s12" }
  - { label: "Bibliography", href: "#s13" }
  - { label: "Citations", href: "#citation-index" }
```

---

## Item 1 — "no other candidate has any textile-trade connection" no longer true

Candidate D (London Drapers' / Old Change tailor) shares the textile trade. The argument is still distinctive — B is a Norfolk-corridor son of a Merchant Taylor; D is a London draper who stays in London — but the absolute phrasing must come down. Three occurrences.

**Occurrence 1 — §2 "The Candidate" table (line 62), cell:**

Old:
> **Occupational match** | Francis was a Merchant Taylor; John-1 was a tailor — no other candidate has any textile-trade connection

New:
> **Occupational match** | Francis was a Merchant Taylor; John-1 was a tailor. Of the named candidates, only Candidate D shares any textile-trade link, and Candidate D stays in London (see §8.4).

**Occurrence 2 — §10.1 "The Occupational Connection" (line 410), second-to-last sentence of the first paragraph:**

Old:
> **No other identified candidate has any documented connection to the tailoring or textile trades.** The Stewkley Gurneys were landholders; the Kent and Sussex Johns were yeomen and shepherds.

New:
> **Among the named candidates, only Candidate D shares a textile-trade connection (London draper/tailor, son of Robert Gurney), and Candidate D remains in London through at least 1638. The Stewkley, Kent, and Sussex Johns were landholders, yeomen, and shepherds.**

**Occurrence 3 — §10.7 "Evidence Summary For" table, row 1 (line 452):**

Old:
> 1 | Occupation: Merchant Taylor father → tailor son | Strong | Trades passed through family apprenticeship. No other candidate has any known textile-trade connection.

New:
> 1 | Occupation: Merchant Taylor father → tailor son | Strong | Trades passed through family apprenticeship. Of the named candidates only Candidate D shares a textile-trade link, and D's continuing London residence rules him out as the colonial John (see §8.4).

---

## Item 2 — §2.1 two-week MT freedom discrepancy: drop from main body, keep in footnote

The discrepancy is between Daniel Gurney's 16 June 1606 transcription and the Company binding-book's 30 June 1606. The Company binding book is the primary record. Lead with it; keep the discrepancy in n14 (already covers it).

**§2.1 paragraph (line 73) — replace:**

Old:
> Francis was bound apprentice in London on 14 May 1599, aged about seventeen, to Henry Tryme of the Merchant Taylors' Company "Near Ludgate," for a seven-year term beginning at Whitsun 1599. On 3 February 1605 the Company Court ordered him assigned over to William Smooth, Merchant Taylor of Lothbury, "with a report of good service from his first master on the grounds that he is due to take a journey into the north and not likely to return until Michaelmas" — a documented multi-month northward absence in 1605, six years before his September 1611 Norwich marriage to Margaret Rybett and the earliest concrete trace of his Norfolk re-engagement.<sup class="fn"><a href="#n13" id="ref-13">13</a></sup> Daniel Gurney's *Supplement* (Note 181) records his admission to the freedom of the Merchant Taylors' Company on 16 June 1606 — "Francis Gurnay son of Henry Gurnay of Great Ellinggam in the County of Norfolk was admitted and sworn to the Freedom of the Merchant Tailors' Company" — while the Company's own binding-book transcription (Scott 2024, UKDA-SN-9263) records the freedom on 30 June 1606. The two-week discrepancy is unresolved and most likely reflects a single-character transcription error in Daniel; reconciliation against the Guildhall MS register is pending.<sup class="fn"><a href="#n14" id="ref-14">14</a></sup>

New:
> Francis was bound apprentice in London on 14 May 1599, aged about seventeen, to Henry Tryme of the Merchant Taylors' Company "Near Ludgate," for a seven-year term beginning at Whitsun 1599. On 3 February 1605 the Company Court ordered him assigned over to William Smooth, Merchant Taylor of Lothbury, ahead of a documented multi-month journey into the north — the earliest concrete trace of his Norfolk re-engagement, six years before his September 1611 Norwich marriage to Margaret Rybett.<sup class="fn"><a href="#n13" id="ref-13">13</a></sup> The Merchant Taylors' Company binding-book records his admission to the freedom of the Company on 30 June 1606.<sup class="fn"><a href="#n14" id="ref-14">14</a></sup>

n14 already carries the Daniel-Gurney-vs-UKDA two-week reconciliation discussion. No footnote text change needed; the body simply stops repeating it.

---

## Item 3 — §3 Master Timeline: out-of-order rows and verbose 1661 entries

Two structural issues plus the wordy 1661 entries.

**Issue A — out-of-order rows.** The current sequence after "16 June 1606 (DG) / 30 June 1606 (UKDA)" runs:
1. c.1606–1611
2. 22 April 1616 — Spelman apprentice  ← out of order
3. c.1609/10 — John born  ← out of order
4. 23 Sept 1611 — Margaret Rybett marriage
5. c.1611/12 — Edward
6. Jan 1612 — first Lestrange
7. c.1614 — Agnes (also factually wrong; see Item 4)

Move the 22 April 1616 Spelman row to its correct chronological slot (between Agnes 31 Jan 1616 and Margaret Rybett death c.1616–1617).

**Issue B — 1661 entries are wordy.** Drop the Cheny/Cheney transcription conflict from the timeline cell and just state the dates. The Cheny conflict already lives in §10.7 (the "Braintree vital-record conflict: Cheny/Cheney vs. Gurney" block) and in n81/n7.

**§3 Master Timeline — replace the full table.** Showing the corrected, reordered table with the Item-4 child-date corrections and Item-2 freedom date already baked in:

```markdown
| Date | Francis Gurney (Father) | John Gurney-1 (Son) |
|---|---|---|
| 13 Sept 1581 | Born, West Barsham Hall, Norfolk (twin with Anthony) | — |
| **14 May 1599** | Bound apprentice to Henry Tryme, Merchant Taylor of Near Ludgate, 7 yrs (started Whitsun 1599) | — |
| **3 Feb 1605** | Transferred to William Smooth (Merchant Taylor, Lothbury) ahead of a six-month "journey into the north" — earliest documented Norfolk re-engagement | — |
| 30 June 1606 | Freed as Merchant Taylor (MT binding-book, vol. 3a; see n14 for Daniel Gurney 16 June 1606 conflict) | — |
| c.1606–1611 | Commercial career continues at Norwich; Lestrange agent | — |
| c.1609/10 | At East Dereham, Norfolk | Born at East Dereham (date ±1–2 yrs) |
| **23 Sept 1611** | **Marries Margaret Rybett, St Martin at Palace, Norwich ★** | Possibly infant/toddler; soft date of birth, potentially before marriage |
| c.1611/12 | Edward baptized, East Dereham (Entry A) | — |
| Jan 1612 | First documented Lestrange payment | — |
| c.1615/16 | Marye buried, East Dereham (Entry B — household event; relationship class reads as niece, not daughter) | — |
| 31 Jan 1616 | Agnes (daughter) buried, East Dereham (Entry C) | Age c.6–7 |
| **22 April 1616** | Takes Francis Spelman, son of Sir Henry Spelman of Middleton, Norfolk, Knight, as his own apprentice (£100 bond) — Spelman–Gurney master-apprentice tie | — |
| c.1616–1617 | **Margaret Rybett dies** (burial not found) | Age c.6–8 |
| c.1617 | Marries Anne Browning | — |
| 25 May 1618 | Marye baptized, East Dereham (Entry D — Anne Browning's first child) | Age c.8–9 |
| **c.1618–1619** | **Family relocates from East Dereham to London (St Benet Fink)** | Family moves with father |
| 2 March 1619 | Dorothy baptized, St Benet Fink, London (first London child) | Growing up at St Benet Fink |
| 1619–1637 | Six more children baptized at St Benet Fink | Growing up in or near London |
| c.1622–1625 | King's Lynn manufacturing venture fails | — |
| **1 Oct 1626** | — | **Sister Ann marries John Gilman, Hingham, Norfolk** |
| c.1628–1630 | — | **John (age ~18) marries Mary [surname unknown]** |
| c.1628–1635 | — | Children born in England (Sarah, Mary, Richard, John Jr., possibly Peter) |
| 1633 | Heralds' Visitation of London — Francis attests his pedigree | — |
| **8 Nov 1633** | Francis (probable son) buried, East Dereham (Entry F) | — |
| **11 July 1634** | **Sells ALL Norfolk/Suffolk lands for £1,000** | No inheritance to expect |
| May 1636 | Last Lestrange payment | — |
| 1638 | Not in "1638 Inhabitants of London" survey | — |
| c.1638–1641 | — | **Emigrates to Massachusetts** |
| June 1641 | — | First MA record: fined at Weymouth, MA |
| May 1645 | — | Signs petition for new plantation at Braintree, MA |
| 3 July 1646 | Record showing annuity still claimed "during his life" | Settled at Braintree, MA |
| **9 Jan 1646/7** | **Dies, buried St Botolph Bishopsgate, London** | — |
| 1653 | — | Deposition: "aged about 50 years" |
| 12 Feb 1661 | — | Sells Braintree land (deed witnessed by John Jr.) |
| 20 Sept 1661 | — | Wife Mary dies, Braintree |
| 12 Nov 1661 | — | Marries Grizzell Fletcher/Kidbee, Braintree |
| 1662/3 | — | **Dies, Braintree, MA** |
```

Notes:
- Item-4 corrections folded in: Marye burial added at c.1615/16; Agnes corrected from "baptized c.1614" to "buried 31 Jan 1616"; Francis (probable son) burial added at 8 Nov 1633.
- Family-move row added as a range (c.1618–1619) per user instruction.
- 1661 wife-death and remarriage rows stripped to facts.
- 16 June / 30 June freedom-date conflict collapsed to the binding-book date with footnote pointer.

---

## Item 4 — §3 missing/incorrect Francis-family dates (covered by Item 3 above)

Item 3's replacement table is the operational change. Summary of factual corrections applied:

| Was | Now |
|---|---|
| `c.1614 Agnes baptized, East Dereham` | `31 Jan 1616 Agnes (daughter) buried, East Dereham (Entry C)` |
| (Marye burial absent) | `c.1615/16 Marye buried, East Dereham (Entry B — household event; relationship class reads as niece, not daughter)` |
| (8 Nov 1633 Francis burial absent) | `8 Nov 1633 Francis (probable son) buried, East Dereham (Entry F)` |
| `2 March 1619 ... Family relocates to London` (point) | `c.1618–1619 Family relocates from East Dereham to London (St Benet Fink)` (range) |

Source basis is the §4.2 table and the companion's image-walk refinement at `research/people/g14-francis-gurney-fact-sheet.research.md` (East Dereham children sections, 2026-05-15 image-walk and paleographic refinement).

---

## Item 5 — Probabilities as single ~number, both §8 and §11

Apply uniformly. Anchor at the midpoint of each existing range.

**§8 table — replace status cells:**

| Row | Old | New |
|---|---|---|
| Candidate B | `**PROBABLE (~55-60%)**` | `**PROBABLE (~60%)**` |
| Candidate D | `**Unlikely (~3-5%)**` | `**Unlikely (~5%)**` |

All other §8 status cells are already single-numbers (`~3%`, `~2%`) and stay as-is.

**§11 Probability Assessment — replace probability cells:**

| Row | Old | New |
|---|---|---|
| B — Son of Francis & Margaret Rybett | `**~65-70%**` | `**~65%**` |
| D — Son of Robert Gurney, draper of Old Change | `**Unlikely (~3-5%)**` | `**Unlikely (~5%)**` |
| Other named candidates (Unlikely / Lead) | `**~5% combined**` | `**~5% combined**` (no change) |
| Unknown corridor (East Anglia / London) | `**~15-20%**` | `**~15%**` |
| Unknown other corridor | `**~5-10%**` | `**~10%**` |
| 1636 Newgate apprentice as distinct second John | `**~3-5%**` | `**~5%**` |

Open question for reviewer: §11 probabilities now sum to ~100% with B at 65, D at 5, Other at 5, Unknown corridor at 15, Unknown other corridor at 10. The Newgate row should remain residual and is **not** an alternative parentage hypothesis for the colonial John — see Item 7 below. Confirm anchor numbers if you want different midpoints (e.g., B at 60 vs. 65).

---

## Item 6 + Item 7 — last §8 row (1636 Newgate apprentice): status, eliminate-reason length, placement

**Recommendation: re-flag as ELIMINATED.** Rationale, grounded only in case-file facts:
- Newgate apprentice's implied birth = c.29 Sept 1615 (Winthrop/Savage 21 July 1636 order, service to age 24, three years from following 29 Sept).
- Colonial John of Braintree's birth = c.1602/3 (Wilson v. Faxon 1653 deposition, "aged about 50 years").
- The 13-year gap is **chronologically incompatible**. The apprentice cannot be the colonial John.
- §11 already treats the apprentice as "treated independently of Candidate B because the apprentice is born c.1615 and chronologically incompatible with the older Braintree John."

The 3–5% in §11 represents a residual "two-Johns" scenario (the apprentice as a separate Massachusetts person whose trail is lost) — that is a different question from "is he the colonial John?" and stays in §11 as a residual bucket.

**Operational change — §8 table last row:**

Old (entire row, currently ~370 words in the eliminate-reason cell):
```
| **1636 Newgate apprentice (distinct second John)** | Suffolk (likely Bury area) → Boston | — | **Distinct second John; trail lost** | Implied birth c.29 September 1615 from the Winthrop/Savage 21 July 1636 court order setting service until age 24. Chronologically incompatible with the older Braintree John (deposed "aged 50 or thereabouts" 1652/3, born c.1602/3). John Newgate himself was from Horningsheath, Suffolk (~3 mi from Bury St Edmunds), residing later at Hessett, Bury, and Southwark before emigrating 1633; the apprentice was therefore most plausibly a young Suffolk man drawn from Newgate's own region. Banks's "Bury St Edmunds" attribution likely tracks this apprentice rather than the older Braintree John. No separate post-1639 colonial trail surfaces in indexed Massachusetts records for a John Gurney born c.1615; likeliest readings are early-Boston mortality, return to England, or absorption into a non-Gurney surname via marriage. The recurring American family-memory tradition of a 29 September 1615 birth and Southwark origin (Lysander F. Gurney sketch; *American Biography* vol. 26; Find a Grave memorial 252975617) sits cleanly in the apprentice's profile and was later conflated with the older Braintree John by 19th-century compilers.<sup class="fn"><a href="#n99" id="ref-99a">99</a></sup> |
```

New (≤30 words in the eliminate-reason cell; placement: keep adjacent to Banks/Bury attribution rows for narrative continuity — keep it as the final row of the elimination table):
```
| **1636 Newgate apprentice (Winthrop/Savage)** | Suffolk → Boston | — | **ELIMINATED** | Implied birth c.1615 (1636 court order, service to age 24). Chronologically incompatible with the colonial John's c.1602/3 (1653 deposition). See §8.5.<sup class="fn"><a href="#n99" id="ref-99a">99</a></sup> |
```

The displaced content moves to a new subsection §8.5 (so it stays in the body, not buried in a footnote — it is critical to deflating the Lysander/American-Biography/Find-a-Grave tradition that conflates this apprentice with the colonial John).

**New §8.5 — insert after §8.4 "Candidate D":**

```markdown
### 8.5 The 1636 Newgate apprentice — a distinct second John, not the Braintree man

Winthrop/Savage's Addenda records that on 21 July 1636 John Newgate brought his apprentice John Gurney before the Boston governor after Gurney had got away his indentures; the court ordered service until age 24, three years from the following 29 September.<sup class="fn"><a href="#n75" id="ref-75b">75</a></sup> That sets the apprentice's birth at c.29 September 1615 — thirteen years too young to be the colonial John of Braintree, who deposed "aged 50 or thereabouts" in 1652/3 (born c.1602/3).

John Newgate himself was from Horningsheath, Suffolk, three miles from Bury St Edmunds, before emigrating in 1633. The apprentice was most plausibly drawn from Newgate's own Suffolk network, which cleanly explains Banks's later Bury St Edmunds attribution: Banks's manuscript memo likely tracked the apprentice rather than the older Braintree John, and nineteenth-century compilers then merged the two Johns into a single biographical sketch.

This deflation matters for the recurring American family-memory tradition (Lysander F. Gurney sketch; *American Biography* vol. 26; Find a Grave memorial 252975617) of a 29 September 1615 birth and Southwark origin: that tradition fits the apprentice, not the colonial John, and should not be carried as a controlling chronology for Candidate B. The apprentice's own post-1639 colonial trail does not surface in indexed Massachusetts records; the likeliest readings are early-Boston mortality, return to England, or absorption into a non-Gurney surname via marriage.<sup class="fn"><a href="#n99" id="ref-99a">99</a></sup>
```

n75 and n99 already exist and carry the Winthrop/Savage Addenda citation, the Newgate Horningsheath origin, and the Lysander/American-Biography material. No footnote-content rewrite required. Re-use the existing `ref-75` anchor as `ref-75b` and keep the existing `ref-99a` reference, or renumber back-refs if the citation index tooling requires it.

**§11 last row (Newgate apprentice) — minor tightening to align with §8.5:**

Old:
> **1636 Newgate apprentice as distinct second John whose later trail is lost** | **~3-5%** | If Banks's BSE attribution genuinely tracks a separate apprentice whose post-1639 colonial trail is lost, this remains a residual reading. Treated independently of Candidate B because the apprentice is born c.1615 and chronologically incompatible with the older Braintree John (born c.1602/3 per the 1653 deposition).

New:
> **1636 Newgate apprentice as distinct second John** | **~5%** | Residual scenario in which Banks's BSE attribution tracks a separate apprentice (born c.1615) whose post-1639 Massachusetts trail is lost. Independent of Candidate B; eliminated as the colonial John on chronology grounds. See §8.5.

---

## Item 8 — §10.1 drop the two-MT-binding-Johns sentence

Per the user: state only that the indexed John Gurneys in the MT binding books are not viable candidates. Keep the bigger point (Francis G14's name does not appear as an MT-apprenticing or freed-by-patrimony father for any John Gurney).

**§10.1 second paragraph (line 412) — replace:**

Old:
> A first-hand scan of the Merchant Taylors' Company binding books and freedom registers 1583–1800 (Scott 2024, UKDA-SN-9263) qualifies but does not refute this occupational argument. The dataset records **no John Gurney son of Francis Gurney** at any binding in that 217-year window, and **no Gurney patrimony freedom anywhere in the 3,391-row Patrimony sheet**. The two John Gurneys who do appear are eliminable on parentage and date: John Gurney son of William, Glover deceased, of Moborne Worcestershire, bound 1602; and John Gurny son of John, Ironmonger of Aylesbury, bound 1655. If Candidate B holds, John G13's tailoring trade was therefore not transmitted through Francis G14's own livery — neither by formal apprenticeship to a fellow MT master nor by patrimony freedom after Francis's death. Three pathways remain consistent with Candidate B: apprenticeship in a different London livery (Drapers, Clothworkers, Worsted Weavers), apprenticeship at Norwich or to a country tailor, or informal household training. The trade-inheritance line of evidence is therefore weakened from "father MT, son trained as MT" to "father in the trade, son in the trade by some untraced pathway," which is still distinctive among the candidate set but not as tight as a documented MT patrimony freedom would have made it.<sup class="fn"><a href="#n95" id="ref-95">95</a></sup>

New:
> A first-hand scan of the Merchant Taylors' Company binding books and freedom registers 1583–1800 (Scott 2024, UKDA-SN-9263) records **no John Gurney son of Francis Gurney**, and **no Gurney patrimony freedom** anywhere in the 3,391-row Patrimony sheet. The two indexed John Gurneys in the MT records are not viable candidates on parentage and date. The trade-inheritance pathway for Candidate B was therefore not Francis's own livery; the likely routes are apprenticeship in a different London livery (Drapers, Clothworkers, Worsted Weavers), apprenticeship at Norwich or to a country tailor, or informal household training. The line of evidence is "father in the trade, son in the trade by some untraced pathway" — distinctive among the candidate set, but not a documented MT patrimony freedom.<sup class="fn"><a href="#n95" id="ref-95">95</a></sup>

n95 already documents the two indexed Johns (Moborne 1602, Aylesbury 1655); no footnote text change needed.

---

## Item 9 (user-invited tightening) — §2.3 author's note on financial collapse

Currently a 100-word anecdotal hedge. Tighten to a 1-sentence pointer and lift the modern-dollar estimate into a footnote.

**§2.3 last paragraph (line 102) — replace:**

Old:
> **Author's note:** It is difficult to estimate in today's terms the extent or impact of Francis' financial collapse but it is plausible to estimate that Francis lost the equivalent of $10+ million USD (his entire net worth) over a few short decades. We do not know the cause(s) of such a collapse but one could envision Francis wanting to publicly hide or minimize his personal decline during the the Heralds' Visitation (see next section below).  With John Gurney being ~23 of age at the time, the strain on family during financial struggles, and unknown father-son dynamics could all be interconnected factors. However, with minimal genealogical evidence (either in support or against), this is framed as more anecdotal than a factual genealogical finding.

New:
> Francis's loss was substantial — plausibly the equivalent of $10M+ USD in his entire net worth over a few decades. The cause is unknown, but the financial strain, the 1633 Visitation, and the 1634 forced land sale all fall within John's late-teens-to-twenties window, and any father-son dynamics around emigration would have been shaped by that backdrop.<sup class="fn"><a href="#nA1" id="ref-A1">A1</a></sup>

Footnote (new entry n-A1; renumber as the citation index dictates):

```html
<li id="nA1">Authorial inference, not a sourced finding. The modern-dollar estimate is rough; £1,000 in 1634 has been variously equated to several million pounds sterling in 2020s purchasing-power terms, and Francis's total losses across the King's Lynn venture, the Lestrange bond, and the 1634 land sale together suggest a substantially higher figure. Included as context for father-son dynamics around emigration, not as a genealogical finding. <a class="backref" href="#ref-A1">↩</a></li>
```

---

## Item 10 (user-invited tightening) — §4.2 heading and prose density

**Heading update.** Section currently reads "Confirmed Francis Gurney/Gurnie Baptisms at East Dereham" but the table now covers baptisms, burials, and a probable burial. Rename.

Old:
> ### 4.2 Confirmed Francis Gurney/Gurnie Baptisms at East Dereham

New:
> ### 4.2 Francis Gurney Events at East Dereham (Baptisms and Burials)

**Prose tightening.** The two paragraphs after the table (lines 172 and 174) currently total ~480 words of paleographic narration. Tighten to one focused paragraph that preserves the key takeaways — Entries B and C are burials not baptisms; Entry B's relationship word does not stroke-resolve to "daughter"; Entry D is on page 00732 not 00736; Susan is withdrawn; Entry F is a probable son. Push the page-by-page paleography into a bullet list for scannability.

**Replace** the two paragraphs (lines 172 and 174) **with:**

```markdown
**Takeaways from the 2026-05-15 image-walk and paleographic refinement (full record in the companion):**<sup class="fn"><a href="#n96" id="ref-96f">96</a></sup>

- **Entries B and C are burials, not baptisms.** Page 00725 sits in a burial sequence. Both lines previously read as baptisms in earlier indexing.
- **Entry B's relationship word does not stroke-resolve to "daughter."** Magnified comparison gives a 4–5 character-width token whose opening-letter shape is class-consistent with niece/nephew. Entry B records a Francis G14 household event at East Dereham — not a confirmed daughter.
- **Entry C (Agnes, "the daughter of ffrancis Gurny") locks to 31 January 1616 modern** via the in-parchment 1616 register-year heading on the same chronology lattice.
- **Entry D (Marye baptism) is on page 00732, not 00736.** Page 00732 is the 1618 christenings subsection under the register's combined annual-return layout; page 00736 is the 1620 christenings heading. The date locks to 25 May 1618.
- **Entry F (Francis, probable son, burial 8 November 1633)** carries no parent in the FS index. Identification as Francis G14's son rests on East Dereham residence, elimination of the other documented Francis Gurneys at that date, and Francis G14's documented name-reuse (1628 St Benet Fink Francis baptism).
- **"Susan Gurney" indexing is withdrawn.** FS index VNN2-WRG ("Susan Gurney burial 31 January") most plausibly mis-reads the Agnes burial line on the same page.

**Date-margin reminder.** Year dating was not consistently visible at the page level across the 1593–1641 register. The walk anchors confidently to in-parchment 1616 and 1620 register-year headings; Entry A (Edward, page 00721) sits in the pre-anchor portion of the register and carries a ±2–3 year margin.
```

n96 already carries the page-by-page citation chain (96a–96e) and the chronology lattice; add n96f as a single rolling pointer to the companion entry rather than introducing a new footnote chain in the body.

**Companion-side small additions** at `research/people/g14-francis-gurney-fact-sheet.research.md` are not needed — the case file already cross-links to the companion's existing East Dereham sections.

---

## Item 11 (user-invited tightening) — §6.2 Peter Anomaly, topic-sentence-up-front

Currently ~150 words leading with method and ending with the finding. Re-lead with the finding.

**§6.2 (line 233) — replace:**

Old:
> An England-wide FamilySearch search found zero Peter Gurney baptisms 1620-1645. A subsequent Findmypast UK Parish Baptisms search 1632-1642 with surname variants returned twelve Peter Gurney baptism results, including a Peter G., father Peter G., christened 27 February 1641 at Smallburgh, Norfolk (FMP transcript R_880200102; "G." is a partial surname index). The Smallburgh entry is a Norfolk Gurney-variant household using the name Peter in the same decade the colonial John named his son Peter, so the case-file's earlier "Peter is completely foreign to the Gurney surname universe" framing is weakened. Peter as a child of the colonial John remains distinctive -- none of the twelve FMP results match a John-Gurney-father pattern -- but the name was not absolutely absent from Norfolk Gurney households. Mary's maiden family remains the most likely source of the colonial son Peter's name; identifying her maiden name and a Peter in her family would still provide independent confirmation of John-1's origin.<sup class="fn"><a href="#n55" id="ref-55">55</a></sup>

New:
> **Peter is distinctive in the colonial John's family but is not absent from Norfolk Gurney households.** A 1641 Smallburgh, Norfolk baptism (Peter G., father Peter G.) sits in the same decade the colonial John named his son Peter. None of the twelve indexed Peter-Gurney-variant baptisms 1632–1642 fathered a John-Gurney child, so Peter as the colonial son's name still calls for explanation — most likely Mary's maiden family. Identifying Mary's surname and a Peter in her kin would remain independent confirmation of John-1's origin.<sup class="fn"><a href="#n55" id="ref-55">55</a></sup>

---

## Item 12 (user-invited tightening) — §10.6 Banks paragraph topic-sentence

The Banks subsection already carries the right facts but buries the lead. Re-lead with the takeaway.

**§10.6 first paragraph (line 438) — replace:**

Old:
> Charles Edward Banks (1937) placed John at Bury St. Edmunds, Suffolk, within a documented cluster of BSE emigrants. The source was "Banks Mss." only — no primary citation. Anderson's 2025 "Unknown" implicitly rejects this under modern standards. But Banks was perceiving a real pattern: a Norwich-born son of Francis who served a Bury St. Edmunds apprenticeship would be exactly the person Banks described.<sup class="fn"><a href="#n64" id="ref-64">64</a></sup>

New:
> **Banks's Bury St Edmunds attribution is consistent with Candidate B, not against it.** Banks (1937) placed John inside a documented BSE emigrant cluster but sourced the attribution only to "Banks Mss." — no primary record. Anderson's 2025 "Unknown" rejects the attribution under modern standards; but a Norwich-born son of Francis who trained at Bury would fit Banks's note precisely. The cluster Banks perceived was real; the parish assignment was a working hypothesis, not a citation.<sup class="fn"><a href="#n64" id="ref-64">64</a></sup>

---

## Item 13 (user-invited tightening) — §4.5 Peter Woodcocke marriage

This is a thin standalone subsection. The Ann/Peter Woodcocke marriage is more relevant as a sibling-disambiguation footnote on §7 (Ann Gurney / Gilman) than as its own §4 subsection.

**§4.5 (lines 187–188) — delete.** Move the content into n33 (or n43) so the Ann/Woodcocke ambiguity travels with §7's Ann/Gilman discussion.

**§7 first sentence (line 244) — append the disambiguation footnote pointer:**

Existing:
> Ann Gurney married John Gilman, a worsted weaver, at Hingham, Norfolk, on 1 October 1626.<sup class="fn"><a href="#n33" id="ref-33">33</a></sup>

Augment n33 with a sentence about the West Dereham 1618/19 Ann/Woodcocke marriage and whether identity overlap is possible. Old n33 stays focused on Hingham 1626; new prose to append:

```
A separately documented Ann Gurney married Peter Woodcocke at West Dereham, Norfolk, on 8 February 1618/19 (NRO PD 192/2; FreeREG transcription). Whether this Ann is the same person as the Ann who married John Gilman in 1626 is unresolved; the case file treats them as potentially distinct.
```

Renumber subsequent §4 subsections only if §4.5 deletion changes the count — §4.4 remains §4.4. The §4.5 anchor (if any inbound link exists) goes away.

---

## Companion surfacing (small)

Per the user's request to surface high-value companion content into the case study where it helps the argument, I have already pulled the **Entry B niece/nephew refinement** into §4.2 (Item 10 above) and the **Newgate Horningsheath–Bury bridge** into §8.5 (Item 6 above). No further companion-side content rises to the case study in this patchset. The companion file at `research/people/g14-francis-gurney-fact-sheet.research.md` is unchanged.

---

## Validation and unresolved items

- No new `data/sources.json` entries are introduced. Footnote n14, n55, n64, n75, n95, n96, n99 are reused as-is.
- The §8 final-row demotion to ELIMINATED is a category change. If the user disagrees and prefers the Unlikely placement with the other Unlikely Johns, swap status, move the row up into the Unlikely band, and update §8.5 accordingly.
- The single-number probability anchors (B at ~60–65%, D at ~5%, etc.) are midpoints of the previous ranges. Adjust before apply if the user wants different anchors.
- The Item-2 freedom-date change (30 June 1606) and Item-3 timeline reorder propagate into §2.1 and §3 cleanly with no other cross-reference breaks observed.
- The §3 master-timeline replacement strips the Item-2 freedom-date conflict line; the underlying n14 footnote already preserves the Daniel Gurney 16 June vs. UKDA 30 June reconciliation.
- Anchor renumber (s2..s13 → s1..s13) requires care if any other repo file links to the case-file's `#s2..#s13` anchors. A quick `grep -r "#s[0-9]" research/` and `grep -r "john-gurney-case-file-v4.html#s" .` should be run before apply to catch external linkbacks.

## Apply order

1. Apply anchor renumber (item 0) first so the site link tree is internally consistent.
2. Apply items 1–13 (mostly independent text replacements; can be applied in any order within the file).
3. Run a footnote-and-anchor pass: confirm n96f exists or is renamed; confirm nA1 is inserted into the citation index in the correct slot; confirm no orphaned back-refs.
4. Spot-check the rendered case-page locally via the site generation layer.

---

## Reviewer checklist (for user)

- [ ] Anchor renumber s2..s13 → s1..s13 is the right scope (not also nav labels)
- [ ] Single-number probability anchors (~60–65% / ~5% / ~15% / ~10%) are the right midpoints
- [ ] §8.5 Newgate subsection is the right home for the displaced detail (vs. footnote-only)
- [ ] §8 last row demoted to ELIMINATED (not Unlikely) is correct
- [ ] Author's-note tightening in §2.3 reads acceptably
- [ ] §4.2 heading rename + bullet-list refactor preserves the persuasive paleographic case
- [ ] §6.2 and §10.6 topic-sentence-up-front rewrites read as more persuasive, not flatter
- [ ] §4.5 Peter Woodcocke deletion-into-n33 is an acceptable structural move
- [ ] Textile-trade rephrasing in three places (§2 table, §10.1, §10.7 row 1) reads as tight enough
- [ ] UX ideation appendix is right-sized (continue separately vs. expand here)
