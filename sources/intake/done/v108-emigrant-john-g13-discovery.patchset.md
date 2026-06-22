**Done:** 2026-06-21 19:08 PT

# Patchset v108 — Emigrant John Gurney (G13): origin-discovery findings

Phase-1 patchset. Promotes the G13 emigrant findings from the June 2026 discovery thread into the G13 companion, adds the one new source (the Commissary Court of London index), its validation, and its media. **Scope: G13 only.** The G22 (Robert) feet-of-fines / Bardolf / Joan-de-Norwich findings and the L-5 Spelman-pedigree promotion (→ G14 companion / case file) are deferred to **v109** (their raw extracts are already in `sources/corpus_supplement/`, and their lead dispositions are already in the leads CSV, so nothing is lost).

Raw source extracts written directly (not via this patchset, per session direction):
- `sources/corpus_supplement/commissary-court-london-gurney-testamentary-index-1626-1700.md`
- `sources/corpus_supplement/gurney-of-keswick-spelman-pedigree-hmc-1891.md` (used in v109)
- `sources/corpus_supplement/norfolk-feet-of-fines-gurnay-entries-rye.md` (used in v109)

Leads already updated directly via the leads tool: L-5 closed, L-156→merged into L-85, L-8/L-85/L-147 updated, L-157–L-161 added.

---

## Item 1 — new source: Commissary Court of London testamentary index (Marc Fitch / BRS)

**Outcome: promote.**

### 1a. `data/sources.json` — add entry under `sources`

Add this key/value to the `sources` object:

```json
"commissary-court-london-testamentary-index-marc-fitch": {
  "citation": "Marc Fitch, ed., Index to the Testamentary Records in the Commissary Court of London (London Division) now preserved in the Guildhall Library, London, vol. IV: 1626–1649 and 1661–1700 (British Record Society, vols. 102, 108, 111)",
  "archive": "Guildhall Library, London (printed index); Internet Archive digitisation",
  "url": "https://archive.org/details/indextotestament0004chur",
  "corpusStatus": "extract",
  "corpusPath": "sources/corpus_supplement/commissary-court-london-gurney-testamentary-index-1626-1700.md",
  "mediaPath": "sources/media/commissary-court-london-testamentary-index-marc-fitch/",
  "validationPath": "sources/validations/commissary-court-london-testamentary-index-marc-fitch.md",
  "notes": "Page 296 carries all five Gurney/Gourny entries for the volume's range (Daniel 1690, Miles 1636, Tho. Gourny 1676, Thomazine 1680, Wm. 1665); no Francis. Also searchable via FindMyPast 'England & Wales Published Wills & Probate Indexes 1300-1858' (record id OR/BRS/327/0310), whose transcription is incomplete vs the printed page."
}
```

### 1b. New file — `sources/validations/commissary-court-london-testamentary-index-marc-fitch.md`

```markdown
# Validation — Commissary Court of London testamentary index (Marc Fitch / BRS vols 102, 108, 111)

- **Source examined:** printed *Index to the Testamentary Records in the Commissary Court of London (London Division)*, vol. IV (1626–1649 & 1661–1700), surname Gurney/Gourny.
- **Portion examined:** page 296 (the complete Gurney/Gourny entries for the volume's date range), from a page image supplied by Allen Gurney, June 2026; cross-checked against the FindMyPast transcription of the same volume.
- **What it establishes:** the five Gurney/Gourny testamentary records in the Commissary Court of London 1626–1649 & 1661–1700 are Daniel (1690), Miles (1636), Tho. Gourny of Fulham (1676), Thomazine widow (1680), and Wm. (1665) — **no Francis Gurney**. The Commissary Court (London Division) held jurisdiction over City parishes incl. St Benet Fink, so this is a substantive negative for Francis Gurney G14's probate.
- **What remains:** the Archdeaconry of London court (a separate jurisdiction) is unchecked; and the Maldon-son Francis (d. 1677) belongs to the Essex courts, not this London Division.
- **Findings recorded in:** `research/people/g13-john-gurney-fact-sheet.research.md` (L-8 disposition).
- **Extract:** `sources/corpus_supplement/commissary-court-london-gurney-testamentary-index-1626-1700.md`.
```

### 1c. Media — move the supplied page image

Create `sources/media/commissary-court-london-testamentary-index-marc-fitch/` and move:
`sources/intake/new/Index to testamentary records in the Commissary Court of London page 296.png`
→ `sources/media/commissary-court-london-testamentary-index-marc-fitch/commissary-court-london-index-p296-gurney.png`

---

## Item 2 — G13 companion: L-8 disposition (Commissary negative; Francis G14 father resolved)

**Outcome: promote.** Assimilate into the existing L-8 disposition paragraph.

`str_replace` in `research/people/g13-john-gurney-fact-sheet.research.md`:

**old_string:**
`**L-8 — Francis Gurnay will: PCC negative; new Maldon Full-Text corroboration.** No PCC will or administration survives for Francis Gurney G14 (Merchant Taylor, d. 9 Jan 1646/7) under either the "Gurney" or "Gurnay" spelling — the 1640–1660 PROB 11 Gurney wills are all other men (closest: Sir Richard Gurney, Royalist Lord Mayor, 1647), and the "Gurnay" 1640–1660 returns are Chancery suits of the Norfolk gentry line. Remaining venues are the London Commissary/Archdeaconry (LMA) and Archdeaconry of Norwich (NRO), not in TNA Discovery. A FamilySearch Full-Text Search pass on "Francis Gurnay/Gurney," however, independently corroborated Francis Gurney **of Maldon** (G14's 1628 son) and surfaced three further restricted English records — detail recorded on [`research/people/francis-gurney-of-maldon.md`](https://github.com/allengurney/gurney-genealogy/blob/main/research/people/francis-gurney-of-maldon.md).`

**new_string:**
`**L-8 — Francis Gurnay will: no surviving probate (PCC, London Commissary, London Archdeaconry, and Norwich diocesan courts all negative).** No will or administration survives for Francis Gurney G14 (Merchant Taylor, d. 9 Jan 1646/7) in any court with jurisdiction over his affairs. The Prerogative Court of Canterbury is negative under both "Gurney" and "Gurnay": the 1640–1660 PROB 11 Gurney wills are all other men (closest: Sir Richard Gurney, Royalist Lord Mayor, 1647), and the "Gurnay" 1640–1660 returns are Chancery suits of the Norfolk gentry line. The **Commissary Court of London (London Division)** — which proved most City-parish wills, St Benet Fink included — is now also negative: the printed Marc Fitch index to that court (1626–1649 & 1661–1700) lists exactly five Gurney/Gourny testamentary records on p. 296 — Daniel (1690), Miles (1636), Tho. Gourny of Fulham (1676), Thomazine widow (1680), and Wm. (1665) — and **no Francis**.[^commissary-2026-06] The **Archdeaconry Court of London** — the other London diocesan court (British Record Society vol. 089, *London Archdeaconry Court Probate Index, 1363–1649*) — is likewise negative: a full variant net (Gurney/Gourney/Gorney, with leading-character tolerance) returns no Gurney testator, the only "Francis G\*rn\*" hits being Garner/Gerrard collisions. The **Norwich diocesan courts** (Norwich Consistory and Archdeaconry of Norwich) are also negative — the Norfolk probate index (*Norfolk Indexes to Wills, Probate, Administrations and Marriage Licence Bonds, 1371–1858*) holds 102 "Gurney" and 4 "Gourn-" testamentary records 1371–1858 with **no Francis** in the 1640s–50s (only Henry 1623 = G15, John 1639, Dorothy 1641), and no early-17th-century Gurney marriage-licence bond. All four courts silent matches Bernau's PRO finding of no will or death record for Francis G14 (only for the Maldon son), so he most plausibly **left no surviving probate** — Interregnum-era disruption the likely cause. The separate Maldon line — a FamilySearch Full-Text pass corroborating Francis Gurney **of Maldon** (G14's 1628 son, d. 1677) and the 1630/1636 Maldon borough-court Gournay entries — is recorded on [`research/people/francis-gurney-of-maldon.md`](https://github.com/allengurney/gurney-genealogy/blob/main/research/people/francis-gurney-of-maldon.md).

[^commissary-2026-06]: Marc Fitch, ed., *Index to the Testamentary Records in the Commissary Court of London (London Division)*, vol. IV, 1626–1649 and 1661–1700 (British Record Society, vols. 102, 108, 111), p. 296 (Gurney/Gourny entries); [Internet Archive](https://archive.org/details/indextotestament0004chur); page image supplied by Allen Gurney. Also searchable via FindMyPast "England & Wales Published Wills & Probate Indexes, 1300–1858" (record id `OR/BRS/327/0310`), whose transcription surfaces only one of the five entries. Extract: [`sources/corpus_supplement/commissary-court-london-gurney-testamentary-index-1626-1700.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/commissary-court-london-gurney-testamentary-index-1626-1700.md). Source ID: \`commissary-court-london-testamentary-index-marc-fitch\`.`

---

## Item 3 — G13 companion: the "Peter" reverse-tracer and the Peter Wales candidate for wife Mary

**Outcome: promote.** Append after the existing Peter paragraph.

`str_replace` in `research/people/g13-john-gurney-fact-sheet.research.md`:

**old_string:**
`The colonial John Gurney's son Peter remains distinctive because none of the FMP results match a John-Gurney-father pattern, but the name was not absolutely absent from Norfolk Gurney-variant households. Mary's maiden family remains the most likely source of the colonial son's name.[^fmp-peter-gurney-2026-05-09]`

**new_string:**
`The colonial John Gurney's son Peter remains distinctive because none of the FMP results match a John-Gurney-father pattern, but the name was not absolutely absent from Norfolk Gurney-variant households. Mary's maiden family remains the most likely source of the colonial son's name.[^fmp-peter-gurney-2026-05-09]

Reading the rare forename **Peter as a reverse tracer for Mary's birth family** — searching for a *Mary born to a father named Peter* in the Norfolk corridor c. 1605–1612 — produces, for the first time, a named candidate pool rather than the dead-end of the (coverage-gapped) John+Mary marriage search. The standout is **Peter Wales of Great Dunham**, ~6 miles from John's East Dereham birthplace and the maternal Rivett cluster: his daughter **Mary Wales was christened 1611 at Great Dunham** (mother Mary), and the household — also at Bawdeswell by 1618 — included Elizabeth (1614, d. 1616), Ann (1618), and a son **Peter** (1629).[^peter-tracer-2026-06] A daughter Mary of a *Peter* a few miles from where John was raised fits both the geography and the otherwise-unexplained grandson Peter Gurney. The reading is circumstantial, not proven: Mary b. 1611 is at the young edge for a pre-1628 marriage, the household carries no *Sarah* (the emigrant's other non-Gurney daughter-name), and Mary/Peter/Wales are common. It cannot be confirmed or refuted by the marriage indexes — **Great Dunham marriages are not in the indexed sets** (a coverage gap; a surname-agnostic Norfolk-wide John×Mary sweep 1622–1636 returns no Gurney-variant groom, and the index *does* catch "Gurney" cleanly, so the emigrant marriage is missing through register-coverage, not surname-munging), so only the Great Dunham / Bawdeswell **parish-register image** can resolve it (lead L-161). The same Peter-tracer surfaced lesser corridor candidates — a Mary daughter of Peter at Norwich (1611) and Mary Barker, daughter of Peter Barker, at Happisburgh (1612) — but the Norwich registers, which are well indexed, show no Gurney marriage for that Mary, leaving the unindexed Great Dunham candidate the one that cannot be ruled out.[^peter-tracer-2026-06]

[^peter-tracer-2026-06]: FamilySearch Historical Records (IGI-based "England, Births and Christenings, 1538–1975" and allied Norfolk parish sets), searched June 2026: children of Mary born to a father Peter in Norfolk c. 1598–1618, and the Peter Wales household at Great Dunham and Bawdeswell (Mary 1611, Elizabeth 1614 [bur. 1616], Ann 1618, Peter 1629). Surname-agnostic John×Mary marriage sweep, Norfolk 1622–1636, returned no Gurney-variant groom; Great Dunham marriages are absent from the indexed sets. Source ID: \`fs-england-births-christenings\`. See lead L-161.`

---

## Item 4 — G13 companion: Newgate's later record names no Gurney

**Outcome: promote.** Assimilate into the Newgate documentation sentence.

`str_replace` in `research/people/g13-john-gurney-fact-sheet.research.md`:

**old_string:**
`John Newgate himself is securely documented in Boston. A 1639 Winthrop deed identifies him as "John Newgate of Boston in New England Feltmaker," which fits the hatter/feltmaker form in later derivative accounts.[^mhs-newgate-feltmaker]`

**new_string:**
`John Newgate himself is securely documented in Boston. A 1639 Winthrop deed identifies him as "John Newgate of Boston in New England Feltmaker," which fits the hatter/feltmaker form in later derivative accounts.[^mhs-newgate-feltmaker] Newgate's later documentary footprint contains **no Gurney**: his 1638 will (children only), his 1638 Harvard deed of gift (witnesses Hezekiah Usher and Richard Russell), and his second will of 25 November 1664 with codicil 8 May 1665 (proved 11 September 1665) name only his Boston merchant-elite circle — wife Ann, son Nathaniel, sons-in-law Simon Lynde and Peter Oliver, the Jackson/Oliver/Lynde grandchildren, and brother-in-law Thomas Townsend. Twenty-eight years after the 1636 episode Newgate retained or remembered no Gurney apprentice — a soft negative consistent with the apprentice (indentured only to ~age 24, i.e. c. 1639) leaving Newgate's household, and with the two-Johns de-conflation.[^newgate-will-2026-06]

[^newgate-will-2026-06]: WikiTree profile [John Newgate (Newgate-14)](https://www.wikitree.com/wiki/Newgate-14), summarising his 1638 will, the 1638 Harvard deed of gift (Colonial Society of Massachusetts, [node 1206](https://www.colonialsociety.org/node/1206)), and the 1664 will + 1665 codicil (Suffolk Co., Mass. Probate); none names a Gurney. The primary will/codicil in Suffolk probate is the level above this compiled abstract (lead L-160). Source ID: \`wikitree-newgate-14-horningsheath\`.`

---

## Item 5 — G13 companion: Finchingfield/NW-Essex corridor test + Norfolk-port & Essex comparators

**Outcome: promote.** Append after the corridor conditional-probability sentence.

`str_replace` in `research/people/g13-john-gurney-fact-sheet.research.md`:

**old_string:**
`The conditional probability of an East Anglia / London origin for the colonial John, given his Essex colonial associations (Daniel Shed of Finchingfield as son-in-law, William Tyng of Stanford Rivers as landlord, Braintree-MA named after Braintree-Essex, Coleman Street adjacency), is materially higher than the unconditional ~60% corridor baseline.`

**new_string:**
`The conditional probability of an East Anglia / London origin for the colonial John, given his Essex colonial associations (Daniel Shed of Finchingfield as son-in-law, William Tyng of Stanford Rivers as landlord, Braintree-MA named after Braintree-Essex, Coleman Street adjacency), is materially higher than the unconditional ~60% corridor baseline.

The **Shed–Finchingfield tie is purely colonial, not an English-side origin clue.** A test of the tempting inference — that Daniel Shed's NW-Essex home (Finchingfield, ~16 miles south of Bury St Edmunds) points to a Gurney family near the Sheds — fails: the only Gurney baptism anywhere in the emigrant window (c. 1600–1645) in the whole of Essex is Marie Gurney at **Epping** (1625, parents **Robert & Sarah** — SW Essex / London fringe, a same-name comparator, not the corridor), with no Gurney at all in the Hinckford-hundred parishes (Finchingfield, Wethersfield, Bocking, Halstead, Castle Hedingham) despite good 17th-century Essex coverage in the index.[^finchingfield-corridor-2026-06] So the Shed alliance does not extend Banks's Bury attribution southward.

Two Norfolk-port and Essex same-name households surfaced as comparators (neither the emigrant's family). At **Great Yarmouth**, an **Edward & Anne Gurney** household baptised Christian (1629) and William (1631), followed after a gap by a William & Susan Gurney household (1657–62); this Edward cannot be securely identified with John's brother Edward (chr. 1610, East Dereham), since no Norfolk Edward-Gurney–Anne marriage is indexed and the only contemporary Edward Gurney × Ann marriage is at St Bride Fleet Street, London (1608/9), implying a man too old to be the 1610 brother.[^yarmouth-edward-2026-06] Separately, the **Ann Gurney × John Gilman** marriage (Hingham, 1626; Gilman a Deopham worsted-weaver) remains a geographically apt but **unverified** fostering/trade possibility — Ann's kinship to Francis G14 is undocumented and the compiled Gilman pedigrees are conflated (lead L-157). And the ROLLCO non-Drapers livery sweep confirmed that the only provincial *tailoring*-Gurney is in the eliminated Buckinghamshire Candidate-A region (Thomas, tailor of Weston Turville; son Francis bound Clothworkers 1622), with no East-Anglian Gurney livery apprentice — so John's tailoring was not company-transmitted (Merchant Taylors and Norwich both negative), pointing to informal/country training.[^rollco-disposition-2026-06]

[^finchingfield-corridor-2026-06]: FamilySearch / Ancestry IGI "England, Select Births and Christenings, 1538–1975" (collection 9841), Essex Gurney baptisms re-ranked, June 2026: only window-era Essex Gurney is Marie Gurney, Epping, 12 Feb 1625, parents Robert & Sarah; no Gurney in the Hinckford-hundred parishes. Shedd genealogy independently reports Daniel Shed's 1620 Finchingfield baptism as the family's sole entry to 1710. Source IDs: \`fs-england-births-christenings\`; \`shedd-daniel-shed-genealogy-1920\`.
[^yarmouth-edward-2026-06]: FamilySearch / Ancestry IGI, Great Yarmouth: Christian Gurney chr. 27 Jan 1629 and William Gurney chr. 17 Apr 1631, parents Edward & Anne; later William & Susan Gurney household 1657–62. England Select Marriages (collection 9852): no Norfolk Edward Gurney × Anne marriage; the only contemporary Edward Gurney × Ann marriage is St Bride Fleet Street, London, 1608/9. Source IDs: \`fs-england-births-christenings\`; \`fs-england-marriages-1538-1973\`. See lead L-159.
[^rollco-disposition-2026-06]: Records of London's Livery Companies Online, non-Drapers Gurney events 1573–1653; extract [`sources/corpus_supplement/rollco-other-companies-gurney-1573-1653.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/rollco-other-companies-gurney-1573-1653.md). The 1622 Clothworkers apprenticeship of Francis Gurney, son of Thomas Gurney, tailor (scissor) of Weston Turville, Bucks, is the only provincial tailoring-Gurney; none is East Anglian. Source ID: \`rollco-other-companies-gurney-1573-1653\`.`

---

## Item 6 — G13 companion: Sources Consulted table row

**Outcome: promote.** Add a row for the new Commissary source. `str_replace` the final existing row to append the new one.

`str_replace` in `research/people/g13-john-gurney-fact-sheet.research.md`:

**old_string:**
`| \`findmypast-england-marriages-gurney-mary-wildcard-sweep-2026-06\` | G\*rn\* + Mary 1620-1634 wildcard marriage negative; Robert Gvrney + Mary Norwich 1622 comparator | [\`sources/validations/findmypast-england-marriages-gurney-mary-wildcard-sweep-2026-06.md\`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/validations/findmypast-england-marriages-gurney-mary-wildcard-sweep-2026-06.md) |`

**new_string:**
`| \`findmypast-england-marriages-gurney-mary-wildcard-sweep-2026-06\` | G\*rn\* + Mary 1620-1634 wildcard marriage negative; Robert Gvrney + Mary Norwich 1622 comparator | [\`sources/validations/findmypast-england-marriages-gurney-mary-wildcard-sweep-2026-06.md\`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/validations/findmypast-england-marriages-gurney-mary-wildcard-sweep-2026-06.md) |
| \`commissary-court-london-testamentary-index-marc-fitch\` | Commissary Court of London index p. 296 — five Gurney/Gourny entries 1626–1700, no Francis (L-8) | [\`sources/validations/commissary-court-london-testamentary-index-marc-fitch.md\`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/validations/commissary-court-london-testamentary-index-marc-fitch.md) |
| \`london-archdeaconry-court-probate-index-brs-089\` | Archdeaconry Court of London index 1363–1649 — variant-net negative for Francis G14 (L-8) | [\`sources/validations/london-archdeaconry-court-probate-index-brs-089.md\`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/validations/london-archdeaconry-court-probate-index-brs-089.md) |
| \`norfolk-wills-probate-index-1371-1858\` | Norwich diocesan (NCC/ANW) + marriage-bond index — 102 Gurney + 4 Gourn-, no Francis 1640s–50s (L-8) | [\`sources/validations/norfolk-wills-probate-index-1371-1858.md\`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/validations/norfolk-wills-probate-index-1371-1858.md) |`

---

## Item 7 — new sources for the four-court L-8 finding

**Outcome: promote.**

### 7a. `data/sources.json` — add entry under `sources`

```json
"london-archdeaconry-court-probate-index-brs-089": {
  "citation": "Index to the Probate Records of the Archdeaconry Court of London, 1363–1649 (British Record Society, vol. 89)",
  "archive": "London Metropolitan Archives (originals); searched via FindMyPast 'England & Wales Published Wills & Probate Indexes, 1300–1858'",
  "url": "https://search.findmypast.co.uk/search-world-records/england-and-wales-published-wills-and-probate-indexes-1300-1858",
  "corpusStatus": "none",
  "validationPath": "sources/validations/london-archdeaconry-court-probate-index-brs-089.md",
  "notes": "June 2026: full variant net (gurn*/gourn*/gorn*, plus forename Francis) returns no Gurney/Gourney testator; the three 'Francis g*rn*' hits are Garner/Gerrard collisions. Negative for Francis Gurney G14."
}
```

### 7b. New file — `sources/validations/london-archdeaconry-court-probate-index-brs-089.md`

```markdown
# Validation — London Archdeaconry Court Probate Index, 1363–1649 (BRS vol. 89)

- **Source examined:** printed Archdeaconry Court of London probate index, 1363–1649, via the FindMyPast aggregator "England & Wales Published Wills & Probate Indexes, 1300–1858," surname Gurney and variants.
- **Portion examined:** all Gurney-variant entries; `gurn*` and `gourn*` and `gorn*` each returned no Gurney/Gourney; `francis g*rn*` returned 3, all read as Garner/Gerrard collisions (not Gurney).
- **What it establishes:** the third London court (after PCC and the Commissary Court, London Division) holds **no Francis Gurney probate** — completing the London-courts negative for Francis Gurney G14.
- **Findings recorded in:** `research/people/g13-john-gurney-fact-sheet.research.md` (L-8 disposition).
```

### 7c. Norwich diocesan / marriage-bond negative — reuses existing sourceId

The Norwich Consistory + Archdeaconry-of-Norwich + marriage-licence-bond negative cited in the L-8 disposition uses the **existing** sourceId `norfolk-wills-probate-index-1371-1858` (Ancestry collection 62679). If no `sources/validations/norfolk-wills-probate-index-1371-1858.md` exists yet, Phase 2 should add a thin one recording the June 2026 scope: 102 "Gurney" + 4 "Gourn-" testamentary records examined, **no Francis** in the 1640s–50s (only Henry 1623, John 1639, Dorothy 1641), and no early-17th-century Gurney marriage-licence bond.

---

## Deferred to v109 (scoped, not lost)
- **G22 Robert companion:** Rye feet-of-fines Gurnay entries (corpus written), the Bardolf–Gournay senior-line resolution (Julian de Gournay d. 1295 × Wm Lord Bardolf), and the de-Norwich-baronial-rejection note for Joan. New lead L-158 already filed.
- **L-5 Spelman pedigree → G14 companion / case file:** promote the located MS 122/16 (corpus `gurney-of-keswick-spelman-pedigree-hmc-1891.md`); new source `hmc-12th-report-appendix-ix-1891` + validation. Lead L-85 already updated; L-5 closed.
- **Mary Gurney × John Allen, 1622 Norwich** comparator → the Norwich same-name cluster note.
