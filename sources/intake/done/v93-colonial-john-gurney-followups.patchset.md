**Done:** 2026-06-13 15:55 PT

# Patchset v93 — colonial emigrant John Gurney (G13): Billerica re-grant (L-104), military calendar entries (L-95), Bury St Edmunds cleared (L-96), PCC negative for Edmund the Divine (L-6) + the Gurnay v Cocke lead (L-115)

**Arc:** the colonial-emigrant half of the 2026-06-12/13 sessions (the English-ancestral half is v92). All findings are corroborating, clarifying, or negative — no structured-data facts change.

**What v93 promotes** (all to the G13 emigrant companion):
1. **L-104 Billerica** — the surrendered lot's re-grant to John Hall; the real Billerica footprint; the "Gurney Tanner" garble debunked.
2. **L-95 military** — the petition and the "bill" identified as a calendar entry and an account settlement (not autographs; the occupation-adjacent reading dropped).
3. **L-96 Bury St Edmunds** — no 1630s John Gurney household; Bury cleared as the emigrant's natal origin (the Thomas × Lydia Broddish household is a generation too late).
4. **L-6 / L-115** — the Prerogative Court of Canterbury search for Edmund the Divine's will returned negative; two incidental West-Barsham-line records logged (a 1630 Harpley grant; the 1648 *Gurnay v Cocke* Chancery suit).

**No `data/ancestors.json` change is warranted** — these are negative/corroborating findings; "Bury cleared" reinforces the existing "origin unknown" posture rather than altering a structured fact.

**Source tracking — three new sources registered (written directly 2026-06-13; Phase 2 must NOT re-create them).** Per Allen's 2026-06-13 guidance that significant-effort sweeps and high-value negative findings become durable sources, three sourceIds were added with full apparatus, all already in the repo:
- `billerica-town-records-ms` → `sources/corpus_supplement/billerica-town-records-gurney-1659-1660.md` + `sources/validations/billerica-town-records-ms.md`
- `bury-st-james-registers` → `sources/corpus_supplement/bury-st-edmunds-gurney-registers-1561-1800.md` + `sources/validations/bury-st-james-registers.md`
- `edmund-divine-pcc-probate-negative` → `sources/corpus_supplement/edmund-gurney-divine-pcc-probate-negative.md` + `sources/validations/edmund-divine-pcc-probate-negative.md`

Each has a `data/sources.json` entry. The military records (L-95) are two targeted pulls, not a sweep — kept under `familysearch-fulltext-search`, no corpus file (per the "smaller individual queries do not get corpus treatment" boundary). The TNA records (L-6/L-115) are cited inline as leads.

**Leads CSV:** L-104, L-95, L-96, L-6, L-115 status updates applied directly (allowed class), marked "promoted in v93."

---

## Item 01 (promote) — G13 companion: colonial document follow-ups

**Target:** `research/people/g13-john-gurney-fact-sheet.research.md`

**Operation — str_replace.** Replace:

```
## Working Notes

### The grandfather and great-uncle wills (L-111/L-6) — searched for New England kin; none named
```

with:

```
## Working Notes

### Colonial document follow-ups (2026-06-12/13) — Billerica re-grant, the Massachusetts "bill" and petition, Bury St Edmunds cleared

Three colonial leads were run to ground at machine-transcript level; the full card tables and verbatim extracts are preserved durably in the corpus-supplement extracts cited below.

**Billerica (L-104) — the surrendered lot was re-granted, and John Gurney's footprint was larger than "explored and abandoned" implies.** After John Gurney surrendered his ten-acre Billerica house-lot (26 December 1659; Daniel Shead "in answer for his father John Gurney"), the town **re-granted one half of it to John Hall on 19 March 1659/60** ("the Towne Doe grant to John Hall one halfe of the Lot yt was granted to John Gurney"); no second-half recipient is recorded. But Gurney was not a mere transient applicant: the town book carries him in the proprietors' lot-draw list ("John Gurney I"), a house valuation of £3, a rate of £2 5s 10d and town charges of 10s 7d (autumn 1659), the 56-acre layout named in the surrender entry, and **two great-meadow lots** — 4¼ acres "beging at the bonds of James Paterson" and 4½ acres at "the mouth of Horse Brook bounded with John Rogers South." The "Gurney Tanner" reading previously flagged is a **dead OCR garble of "Towne Charges"** — image 13 reads the same list cleanly, "John Gurney : Towne Charges of -10-7"; there is no tanner occupation for any Billerica Gurney. The Shead tie recurs (Daniel Shed sequential with Gurney in the proprietors list; "Sheads corner" a survey landmark; a Nathan Shead still an assessor in 1707).[^billerica-followup-2026-06]

**Massachusetts military records (L-95) — the petition and the "bill" are a calendar entry and an account settlement, not autographs.** The Weymouth gunpowder-fines petition is item 67 of an inventory-calendar in "Massachusetts. Military Records 1643–1675": "Petition of John Gurny, Richard Porter, and James Ludden of Weymouth, for the remission of the fines laid upon them for not being supplied with powder" (undated; neighbouring items cluster c. 1645–51) — the calendar behind MBCR 1:331, not the petition itself. The "bill" reads "**John Gurny his byl for 3. 16. 42, & Tho: Lake his note for 1. 3. 84, are 1644 accepted for 5 fro Mr Ginn**" (Massachusetts Bay Colony Military Records 1642–1649, vol. p. 79) — a colony-accounts settlement of Gurny's £3 16s bill (dated 16 March 1641/2) through an intermediary, **not** demonstrably tailoring or supply work; the nature of the bill is unstated, so the earlier occupation-adjacent reading should be dropped.[^military-followup-2026-06]

**Bury St Edmunds (L-96) — no 1630s John Gurney household; Bury is cleared as the emigrant's natal origin.** A full sweep of the Bury St James parish registers shows the Bury Gurney presence was a **Thomas Gurney × Lidda (Lydia) Broddish** household, married c. 1633–35 — far too late to have fathered John Gurney-1 (b. c. 1607–12). Their children were Juda (bap. c. 1633/4), a John "son to Thomas" (registered c. 1653/4, after the 1653 Act reopened the register), and a Thomas (c. 1661/2); a separate John Gurney × Elizabeth baptised a William in 1665. Earlier Bury Gurneys are unconnected (a William Gurney's daughter Bridgett, 1588; a Mary Gurny in a 1620–24 communicant list). Banks's Bury St Edmunds attribution therefore finds **no supporting natal household** in these registers — consistent with the long-standing reading that Banks tracked an apprenticeship at Bury, not a birth (see the Newgate/Horningsheath note and case file §8.5 below).[^bury-followup-2026-06]

[^billerica-followup-2026-06]: Billerica, Massachusetts town records 1653–1727 (FamilySearch image group DGS 007466228), film-scoped `Gurn*` sweep of 17 cards, 2026-06-12: re-grant at image 15 ([ark:/61903/3:1:3QS7-89Z8-TV2C](https://www.familysearch.org/ark:/61903/3:1:3QS7-89Z8-TV2C)); grant/surrender at image 173 ([ark:/61903/3:1:3QS7-89Z8-T2GH](https://www.familysearch.org/ark:/61903/3:1:3QS7-89Z8-T2GH)); great-meadow lots at images 179–180; "Towne Charges" at image 13 ([ark:/61903/3:1:3QS7-89Z8-TV6F](https://www.familysearch.org/ark:/61903/3:1:3QS7-89Z8-TV6F)) vs the "Tanne" OCR garble at image 214. Full record: [`sources/corpus_supplement/billerica-town-records-gurney-1659-1660.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/billerica-town-records-gurney-1659-1660.md). Source ID: `billerica-town-records-ms`.
[^military-followup-2026-06]: Petition calendar: "Massachusetts. Military Records 1643–1675" (FamilySearch DGS 007702977), images 947–948 ([ark:/61903/3:1:3Q9M-C9Y5-F9M1-4](https://www.familysearch.org/ark:/61903/3:1:3Q9M-C9Y5-F9M1-4) and -F9M1-C). Bill: "Massachusetts Bay Colony. Military Records 1642–1649" (DGS 008713629), image 48 = volume p. 79 ([ark:/61903/3:1:3QHV-J3DW-8YB3](https://www.familysearch.org/ark:/61903/3:1:3QHV-J3DW-8YB3)); printed index "Gurny, John, 79" at image 169. Read 2026-06-13. Source ID: `familysearch-fulltext-search`.
[^bury-followup-2026-06]: Bury St Edmunds, St James parish registers (FamilySearch DGS 007413310), `Gurn*` sweep of 20 cards, 2026-06-13: Thomas Gurney × Lidda Broddish marriage (image 297); Juda fil. Thomas bap. (image 60); John "son to Thomas" (image 77); Thomas fil. Thomas (image 83); William fil. Johannis et Elizabeth bap. 1665 (image 86); Bridgett fil. William bap. 1588 (image 23); Mary Gurny in a 1620–24 communicant list (image 294). Full record: [`sources/corpus_supplement/bury-st-edmunds-gurney-registers-1561-1800.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/bury-st-edmunds-gurney-registers-1561-1800.md). Source ID: `bury-st-james-registers`.

### The grandfather and great-uncle wills (L-111/L-6) — searched for New England kin; none named
```

## Item 02 (promote) — G13 companion: record the PCC-negative outcome and the two incidental records (L-6 / L-115)

**Target:** `research/people/g13-john-gurney-fact-sheet.research.md`

**Operation — str_replace.** Replace:

```
Edmund's will is not in the Norwich Consistory registers for 1643–1651 (coverage-confirmed sweeps; the registers then gap until 1660), so the remaining target is a Prerogative Court of Canterbury probate 1648–1659.
```

with:

```
Edmund's will is not in the Norwich Consistory registers for 1643–1651 (coverage-confirmed sweeps; the registers then gap until 1660), and a Prerogative Court of Canterbury search (TNA Discovery and beta catalogue, all spellings, 1648–1660) is also negative — no PCC will or administration for Edmund — so his probate most likely does not survive (full search record: [`sources/corpus_supplement/edmund-gurney-divine-pcc-probate-negative.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/edmund-gurney-divine-pcc-probate-negative.md); Source ID `edmund-divine-pcc-probate-negative`). The search incidentally surfaced two West-Barsham-line records, logged as leads rather than emigrant evidence: a 27 April 1630 grant by "Edmond Gurnay of Harpley, clerk" to Edward Gurnay of West Barsham, esq. (Norfolk Record Office BL/O/G/1), confirming the rector's own spelling and a property tie to the West Barsham heir; and the 1648 Chancery suit *Gurnay v Cocke* over Great Ellingham, plaintiffs Frances Gurnay widow and Henry Gurnay — plausibly Edward Gournay's widow and his heir Henry II, which would name Edward's otherwise-unrecorded wife (TNA C 5/609/120, lead L-115).
```

## Item 03 (promote) — intake disposition

The durable substance of these three sweeps now lives in `sources/corpus_supplement/` + `data/sources.json` + `sources/validations/` (written directly 2026-06-13), so the raw intake files are pure working-capture audit and nothing in the repo depends on them. Execute as literal file operations:

1. **Move** the colonial campaign intake records into a dated done-folder `sources/intake/done/colonial-followups-2026-06/` (working-capture audit only):
   - `sources/intake/new/fts-2026-06-12-billerica-l104.md`
   - `sources/intake/new/fts-2026-06-12-edmund-pcc-l6.md`
   - `sources/intake/new/fts-2026-06-13-military-bury-l95-l96.md`
2. **Move** the two L-112/L-34 analysis inputs (consumed by patchset v92) into `sources/intake/done/english-wills-2026-06/`:
   - `sources/intake/new/analysis-2026-06-12-l112-anthony-g17-will-reconciliation.md`
   - `sources/intake/new/analysis-2026-06-13-l34-edmund-g23-will-resolution.md`
3. **Drop** the three Massachusetts military calendar images from `sources/intake/paleography-staging/images/` — they are calendar/account pages, not autographs needing paleography: `ma-military-1642-1649-bill-gurny.jpg`, `ma-military-1643-1675-petition-img948.jpg`, `ma-military-1643-1675-second-match-img947.jpg`.

---

## Phase-2 sequencing note

Apply items 01 → 02 (both G13 companion str_replace), then Item 03 (file moves). The three new sources (corpus_supplement extracts, validation worksheets, and `data/sources.json` entries) were already written directly 2026-06-13 — do NOT re-create them; just confirm they exist and that `data/sources.json` parses. No `data/ancestors.json` change. After application, prepend the Done stamp and move this patchset to `sources/intake/done/`.
