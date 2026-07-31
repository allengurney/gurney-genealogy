# *The British Archivist* — Bernau (1913) — Validation

**Source:** `british-archivist-bernau-1913` (proposed entry; see `_CHANGES.md` at delivery root for proposed `data/sources.json` addition).

Audit trail for what has been examined from this source and where findings landed. Findings themselves live with the research subjects; this file is thin by design.

---

## Scope of examination

- 2026-04-23 — Full article examined by Claude (working session). Article runs pp. 49 ff. of *The British Archivist* vol. I, no. 7 (September 1913), authored by Charles A. Bernau, F.S.G. Corpus extract loaded at `sources/corpus_supplement/The_British_Archivist-Unrecorded-Biographies-Francis-Gurney.md`.

## What was examined

The entire article, all sections:

- "His Parentage" — paragraph on Francis G14 and Anne Browning
- "His Parents' Children" — Bernau's 11-item list of Francis G14's children (including speculative items 10–11)
- "His Marriage" — Francis-of-Maldon's marriage to Anne Browning of Maldon
- "His Children" — ten Maldon baptisms 1655–1667
- "His Official Position" — Maldon Alderman (1662) and Bailiff (1664)
- "His Business and Lawsuits" — two Chancery bills (TNA C6/Bridges 489/64 and 608/99)
- "His Death" — four caveats; Samuel Pepys's 21 August 1677 action
- "His Property" — Exchequer Special Commission No. 6222; estate schedule
- "Thomas Browning, D.D." — the brother-in-law hypothesis
- "The Problem" — Norwich cordwainer / St Gregory's identification

## Scope limitations

- Only this single article from *The British Archivist* has been examined. Other volumes of the periodical and the broader Bernau corpus have not been reviewed.
- None of Bernau's cited archival references have been pulled at first hand:
  - TNA C6/Bridges 489/64 and Hamilton 521/90 (1676 Chancery bill)
  - TNA C6/Bridges 608/99 (1677 Chancery bill)
  - S.P. Dom. Entry Book 45/42 (Treasurer's caveats)
  - S.P. Dom. Car. II. 396/21 fol. 34 (Pepys caveat entry)
  - Exchequer Special Commission No. 6222 (E178 or E134, Essex inquisition 11 October 1677)
  - Lay Subsidy 246/22 (1674 Hearth Tax, Maldon)
  - Lay Subsidy 246/12 (1663/4 Hearth Tax, Maldon)
  - PCC Caveats 13 and 25 August 1677
  - Commissary Court of London–Essex & Herts: Henry Jermyn will 1680 ("Heydon" 481); Michael Cooper will 1687 proved 1688 ("Hamor" 207); Thomas Browning will 1694 proved 1705
  - Foster's *Alumni Oxonienses* (verification of Thomas Browning Cambridge/Oxford record)
  - St Benet Fink parish registers (LMA P69/BEN1/A/001, /002) — source of the St Benet Fink baptisms 1619–1637
  - Maldon parish registers (St Mary's primarily; St Peter's for the 1660 George Gurney marriage and 1661 baptism)
- The 1634 Heralds' Visitation of London reference is quoted by Bernau but not cross-checked against Harleian Society vol. XV (1880), vol. XVII (1883), or the Fellows 1957 supplement.
- The Sir Henry Spelman manuscript-pedigree lead has not been pursued in any repository.

## Where findings landed

| Finding | Destination |
|---|---|
| All Francis G14 (elder) findings: parentage re-attestation; 1634 visitation date conflict; William Browning "later of Maldon" detail; Spelman pedigree lead; St Benet Fink children-list conflict with current fact sheet; the second John of Maldon (d. 1681 bachelor) and its implications for Candidate B; Thomas Browning brother-in-law hypothesis | `research/people/g14-francis-gurney-fact-sheet.research.md` |
| Full biography of Francis Gurney the younger of Maldon (b. 1628, d. 1677): marriage; Maldon civic career; ten Maldon children; two Chancery lawsuits; death by drowning; Pepys caveat; Exchequer inquisition and estate schedule; "The Problem" (Norwich cordwainer identification) | `research/people/francis-gurney-of-maldon.md` |
| Elimination row in the "Other John Gurneys" table for "John of Maldon, bachelor, d. 1681" | `research/case-files/john-gurney-case-file-v5.md` §8 |
| Source catalog entry | `data/sources.json` (proposed addition — see `_CHANGES.md`) |

## Known issues

- The Gurney/Gournay spelling alternates across the article, including within single PCC caveat transcriptions ("Fra: GURNEE", "Frances GURNEY", "Francis GOURNEY"). Bernau preserves the spelling of each archival source; Claude preserved the same convention in quoted matter and normalized to "Gurney" in narrative prose.
- The article is printed from 1913 typography; no OCR step was needed because the corpus extract was clean markdown.
