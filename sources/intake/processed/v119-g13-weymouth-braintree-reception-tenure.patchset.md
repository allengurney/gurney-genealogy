# v119 — G13 John Gurney: Weymouth/Braintree reception, tenure, and the 1644 bill correction

**Arc:** Multi-turn critical review and extension of the Codex omnibus `sources/intake/new/g13-weymouth-land-tenure-cross-community-militia-omnibus-2026-06-28.md`, plus independent verification across the MHS *Genesis* land-system paper, the Tyng probate abstract (NEHGR 30:432), Adams's *History of Braintree*, and the Hingham histories. This patchset assimilates the verified findings into the G13 research companion and the immigration-by-association topic file. It does **not** touch the John Gurney case file (separate enumerated recommendation delivered in chat).

**Corpus added directly (not via this patchset), already written to the repo:**
- `sources/corpus_supplement/tyng-inventory-1653-nehgr-30-432-john-gurney.md`
- `sources/corpus_supplement/adams-genesis-massachusetts-town-1892-weymouth-land.md`
- `sources/corpus_supplement/hingham-massachusetts-norfolk-emigrant-cohort-1633-1639.md`

(The omnibus's Weymouth land-system detail — the 1636 great-lot roll, the small-strip comparables, the 1651/2 lists, the absentee comparators, and the Read profile — is **not** put in a supplement: those sources, Nash's *Historical Sketch* and the *History of Weymouth*, are already in the full-text corpus. The findings are assimilated into the topic file (item T6) and cited to the corpus by page/line.)

**Core findings promoted:**
1. The "1641/2 bill" is a misreading: the printed Massachusetts Bay records (session beginning 30 Oct 1644) accept John Gurny's bill of **£3 16s 4d** with Thomas Lake's note of **£1 3s 8d** as **£5** due from "Mr Ginner" = **Rev. Thomas Jenner**, Weymouth's minister 1636–40. Arithmetic (3·16·4 + 1·3·8 = 5·0·0) confirms.
2. The Tyng probate inventory (25 May 1653, NEHGR 30:432) lists **48 acres "in the possession of John Gurney,"** enumerated separately from "Salters Farme" — confirming 48 acres (not 45), confirming the parcel is distinct from John Read's/Gregory Belcher's Salter's (Mount Wollaston) farm, and that the lease was already in place by 1653. Tyng = Stanford Rivers, Essex (bp. 1602/3, d. 1653); Read = Salter's Farm tenant 1639–49, married Suffolk; Belcher (co-tenant) = Warwickshire.
3. Adams's *Genesis of the Massachusetts Town* supplies the land-system frame: Weymouth's property records are undated (the "1643" is inference), the town had no proprietor-body, the 6 April 1646 order restricted non-inhabitant landholding, and non-resident proprietors held rights but were excluded from inhabitant privileges — the doctrine under which John's 1651/2 great-lot entitlement persisted after he left.
4. Reception was into an **established** Weymouth: James Ludden = "Old Planter" (Wessagusset by 1632); "Goodman King" = John King of Weymouth (King's Cove seaman/planter, early settler). The 1651/2 cohort scattered to Rehoboth/Boston, not Braintree — John's Braintree move was individual.
5. The Hingham reception model for Candidate B is a **strong correlation**: 206 emigrants from Hingham, Norfolk and its vicinity settled adjacent Hingham, Massachusetts (1633–39; Diligent 1638 = 133), out of the same parishes as the direct-line Gurneys (Great Ellingham, Hingham, Wymondham, Attleborough, Deopham).
6. The Bucks-neighbour kin thread is weak: no Gurney is recorded in Wendover, Lee, or Ashton Clinton — the associate parishes.
7. The first Weymouth grants are undated: the defensible range is c. 1637–42 (best estimate c. 1640–41), and John is absent from the distinct 1636 Fresh Pond great-lot roll. The militia angle is a documented negative — no campaign, office, or Military-Company-roll entry. John's pattern is ordinary mixed tenure (small owned homestead + leased Tyng farm + residual Weymouth right), not a "sublet" (a word the repo never used).

**Codex omnibus coverage.** This patchset assimilates the substantive findings of `sources/intake/new/g13-weymouth-land-tenure-cross-community-militia-omnibus-2026-06-28.md` (the source thread reviewed and extended). Its corrected-bill, Tyng-tenure, possession-register, 1636-roll, absentee-cohort, Read-comparator, militia, and continuing-tie findings are all promoted above; the Hingham reading is carried as a strong correlation (not the omnibus's "weak"), per the direct-line-Gurney parish overlap. At Phase 2, after application, move the omnibus file to `sources/intake/archive/`.

---

## 1. Source registrations — `data/sources.json` (add to the `sources` object)

### 1.1 `nehgr-30-432`
```json
"nehgr-30-432": {
  "shortTitle": "NEHGR vol. 30 (1876), p. 432 — Capt. William Tyng inventory",
  "citation": "\"Abstracts of the Earliest Wills on Record in the County of Suffolk, Mass.\" New England Historical and Genealogical Register, vol. 30 (Boston: NEHGS, 1876), p. 432, inventory of Capt. William Tyng, made 25 May 1653 (abstracting Suffolk County, Mass., Probate Register vol. viii, p. 62).",
  "archive": "Internet Archive (item newenglandhistor30wate).",
  "url": "https://archive.org/details/newenglandhistor30wate",
  "corpusStatus": "extract",
  "validationPath": "sources/validations/nehgr-30-432.md",
  "notes": "Tyng probate inventory abstract. Lists \"48 Akers land at Brantree, and Marsh in the possession of John Gurney,\" separate from the Tyng \"Salters Farme.\" Verbatim extract at sources/corpus_supplement/tyng-inventory-1653-nehgr-30-432-john-gurney.md."
}
```

### 1.2 `adams-genesis-massachusetts-town-1892`
```json
"adams-genesis-massachusetts-town-1892": {
  "shortTitle": "C. F. Adams, Genesis of the Massachusetts Town (1892)",
  "citation": "Adams, Charles Francis. \"The Genesis of the Massachusetts Town, and the Development of Town-Meeting Government.\" Proceedings of the Massachusetts Historical Society, 2nd series, vol. 7 (1891–1892), pp. 172–263; Weymouth treatment pp. 190–192.",
  "archive": "Internet Archive (item proceedingsofmass2v7mass).",
  "url": "https://archive.org/details/proceedingsofmass2v7mass",
  "corpusStatus": "extract",
  "validationPath": "sources/validations/adams-genesis-massachusetts-town-1892.md",
  "notes": "Land-system context for Weymouth: undated property records, no proprietor-body, the 6 April 1646 anti-stranger order, and the non-resident-proprietor doctrine. No Gurney named. Verbatim extract at sources/corpus_supplement/adams-genesis-massachusetts-town-1892-weymouth-land.md."
}
```

### 1.3 `adams-history-of-braintree-1891`
```json
"adams-history-of-braintree-1891": {
  "shortTitle": "C. F. Adams, History of Braintree (1891)",
  "citation": "Adams, Charles Francis. History of Braintree, Massachusetts (1639–1708), the North Precinct of Braintree (1708–1792), and the Town of Quincy (1792–1889). Cambridge: Riverside Press, 1891.",
  "archive": "Internet Archive (item historyofbraintr00adam).",
  "url": "https://archive.org/details/historyofbraintr00adam",
  "corpusStatus": "extract",
  "validationPath": "sources/validations/adams-history-of-braintree-1891.md",
  "notes": "North-Precinct/Quincy-scoped town history. Records Tyng's 1639 purchase of Mount Wollaston and \"large allotments, indicative of a non-resident ownership\" post-1637 (p. 5). Names no Gurney; John Gurney's freehold was in the South Precinct on the Monatiquot. Extract folded into sources/corpus_supplement/adams-genesis-massachusetts-town-1892-weymouth-land.md."
}
```

### 1.4 `history-of-town-of-hingham-1893`
```json
"history-of-town-of-hingham-1893": {
  "shortTitle": "History of the Town of Hingham, Massachusetts (1893)",
  "citation": "History of the Town of Hingham, Massachusetts. 3 vols. Hingham: published by the town, 1893. Vol. 1 (history, incl. Daniel Cushing's settler list, pp. 201–203); vol. 2 (genealogies, English parishes of origin).",
  "archive": "Internet Archive (items historyoftownofh01hing, historyoftownofh02hing).",
  "url": "https://archive.org/details/historyoftownofh01hing",
  "corpusStatus": "extract",
  "validationPath": "sources/validations/history-of-town-of-hingham-1893.md",
  "notes": "Documents the Norfolk emigrant cohort (206 from Hingham, Norfolk and vicinity, 1633–39; Diligent 1638 = 133) that settled adjacent to Weymouth. No colonial Gurney at Hingham. Verbatim extract at sources/corpus_supplement/hingham-massachusetts-norfolk-emigrant-cohort-1633-1639.md."
}
```

### 1.5 `massachusetts-bay-records-v2-1853`
```json
"massachusetts-bay-records-v2-1853": {
  "shortTitle": "Mass. Bay Records, vol. 2 (1642–1649), Shurtleff ed.",
  "citation": "Shurtleff, Nathaniel B., ed. Records of the Governor and Company of the Massachusetts Bay in New England, vol. 2, 1642–1649. Boston: William White, 1853, p. 79.",
  "archive": "Internet Archive (item cu31924091024582).",
  "url": "https://archive.org/details/cu31924091024582",
  "corpusStatus": "extract",
  "validationPath": "sources/validations/massachusetts-bay-records-v2-1853.md",
  "notes": "Printed record of the General Court session beginning 30 Oct 1644: \"John Gurny his byl for 3. 16. 4d & Tho: Lake his note for 1. 3. 8d are accepted for £5 fro Mr Ginner.\" Corrects the earlier machine-transcript reading of a \"16 March 1641/2\" date. Index renders the counterparty \"Ginner, Mr.\" = Rev. Thomas Jenner."
}
```

Update `meta.lastUpdated` to `2026-06-28` if not already.

---

## 2. Validation files — `new file write`

### 2.1 `sources/validations/nehgr-30-432.md`
```markdown
# Validation — NEHGR vol. 30 (1876), p. 432 (Capt. William Tyng inventory)

- **Source:** `nehgr-30-432`. NEHGR vol. 30 (1876), p. 432, abstract of the probate inventory of Capt. William Tyng (made 25 May 1653), itself abstracting Suffolk County, Mass., Probate Register vol. viii, p. 62.
- **Examined:** the p. 432 Tyng inventory abstract (full text), via Internet Archive item `newenglandhistor30wate`.
- **Findings landed in:** `research/people/g13-john-gurney-fact-sheet.research.md` (land-and-property table, Tyng leasehold); verbatim extract at `sources/corpus_supplement/tyng-inventory-1653-nehgr-30-432-john-gurney.md`.
- **Open/uncertain:** the abstract gives no lease-start date or terms; the manuscript inventory (Suffolk Probate Reg. viii:62) and any underlying lease instrument remain the primary level. The NPS Adams CLR (1997) gives 45 acres and a 1647 lease start; the inventory abstract's 48 acres is the closer witness for the acreage.
```

### 2.2 `sources/validations/adams-genesis-massachusetts-town-1892.md`
```markdown
# Validation — C. F. Adams, "Genesis of the Massachusetts Town" (1892)

- **Source:** `adams-genesis-massachusetts-town-1892`. MHS Proceedings 2nd ser. vol. 7, pp. 172–263.
- **Examined:** the Weymouth treatment, pp. 190–192 (undated property records; no proprietor-body; the 6 April 1646 anti-stranger order; the non-resident-proprietor doctrine).
- **Findings landed in:** `research/topics/g13-john-gurney-immigration-by-association.md`; verbatim extract at `sources/corpus_supplement/adams-genesis-massachusetts-town-1892-weymouth-land.md`.
- **Open/uncertain:** no Gurney is named in the paper; it is general land-system context, not direct G13 evidence.
```

### 2.3 `sources/validations/adams-history-of-braintree-1891.md`
```markdown
# Validation — C. F. Adams, History of Braintree (1891)

- **Source:** `adams-history-of-braintree-1891`.
- **Examined:** the Tyng / Mount Wollaston passages (pp. 5, 109) and a full-text scan for "Gurney" (only a 19th-century "Sigourney" false hit — no colonial Gurney).
- **Findings landed in:** `research/topics/g13-john-gurney-immigration-by-association.md` (non-resident-ownership note); extract folded into the Adams *Genesis* corpus supplement.
- **Open/uncertain:** the volume is North-Precinct/Quincy-scoped; John Gurney's South-Precinct Monatiquot freehold and neighbours are better pursued via the Braintree town records, Sprague's *Genealogies of the Families of Braintree* (`sprague-braintree`, already used in this case), and the Suffolk Deeds abuttals. The family-specific Faxon and Brackett genealogies on Internet Archive were checked and contain no colonial Gurney.
```

### 2.4 `sources/validations/history-of-town-of-hingham-1893.md`
```markdown
# Validation — History of the Town of Hingham, Massachusetts (1893)

- **Source:** `history-of-town-of-hingham-1893`.
- **Examined:** vol. 1 Daniel Cushing settler list (pp. 201–203) and vol. 2 genealogies (English parishes of origin; calibrated that origins are recorded, e.g. Lincoln/Gates "from Wymondham, Norfolk").
- **Findings landed in:** `research/topics/g13-john-gurney-immigration-by-association.md` (Hingham corridor); verbatim extract at `sources/corpus_supplement/hingham-massachusetts-norfolk-emigrant-cohort-1633-1639.md`.
- **Open/uncertain:** no colonial Gurney settled at Hingham. The cohort heartland is south-central Norfolk (Hingham/Wymondham/Attleborough/Great Ellingham) — the direct-line Gurney parishes — supporting a strong regional reception correlation for a Norfolk-origin John.
```

### 2.5 `sources/validations/massachusetts-bay-records-v2-1853.md`
```markdown
# Validation — Mass. Bay Records, vol. 2 (1642–1649), p. 79

- **Source:** `massachusetts-bay-records-v2-1853`.
- **Examined:** p. 79, the General Court entry (session beginning 30 Oct 1644) accepting "John Gurny his byl for 3. 16. 4d & Tho: Lake his note for 1. 3. 8d ... for £5 fro Mr Ginner."
- **Findings landed in:** `research/people/g13-john-gurney-fact-sheet.research.md` (military-records discussion).
- **Open/uncertain:** the nature of Gurney's bill is unstated. The counterparty "Ginner" is identified as Rev. Thomas Jenner from the volume index and the Weymouth records ("Mr. Thom: Ginner (Jenner)"). A higher-resolution manuscript image of the entry would confirm the pence figures at source level.
```

---

## 3. Research assimilation — `research/people/g13-john-gurney-fact-sheet.research.md`

### C1 — correct the "1644 bill" paragraph (plain language)

`str_replace`:

**old_string:**
```
**Massachusetts military records (L-95) — the petition and the "bill" are a calendar entry and an account settlement, not autographs.** The Weymouth gunpowder-fines petition is item 67 of an inventory-calendar in "Massachusetts. Military Records 1643–1675": "Petition of John Gurny, Richard Porter, and James Ludden of Weymouth, for the remission of the fines laid upon them for not being supplied with powder" (undated; neighbouring items cluster c. 1645–51) — the calendar behind MBCR 1:331, not the petition itself. The "bill" reads "**John Gurny his byl for 3. 16. 42, & Tho: Lake his note for 1. 3. 84, are 1644 accepted for 5 fro Mr Ginn**" (Massachusetts Bay Colony Military Records 1642–1649, vol. p. 79) — a colony-accounts settlement of Gurny's £3 16s bill (dated 16 March 1641/2) through an intermediary, **not** demonstrably tailoring or supply work; the nature of the bill is unstated, so the earlier occupation-adjacent reading should be dropped.[^military-followup-2026-06]
```

**new_string:**
```
**Massachusetts military records — the petition is a calendar entry and the "bill" is a 1644 account settlement, not a 1641/2 record.** The Weymouth gunpowder-fines petition survives as item 67 of an inventory-calendar in "Massachusetts. Military Records 1643–1675": "Petition of John Gurny, Richard Porter, and James Ludden of Weymouth, for the remission of the fines laid upon them for not being supplied with powder" (undated; neighbouring items cluster c. 1645–51) — the calendar behind MBCR 1:331, not the petition itself. The separate "bill" entry, in the printed Massachusetts Bay records for the General Court session beginning 30 October 1644, reads: "John Gurny his byl for 3. 16. 4d & Tho: Lake his note for 1. 3. 8d are accepted for £5 fro Mr Ginner." The figures are pounds, shillings, and pence, and the arithmetic is exact — £3 16s 4d plus £1 3s 8d makes £5 — so the entry is a 1644 colony-accounts acceptance, not the "16 March 1641/2" date an earlier machine-transcript reading ("3. 16. 42") had produced. "Mr Ginner" is the volume index's form of **Rev. Thomas Jenner**, Weymouth's minister 1636–40 (the Weymouth records render him "Mr. Thom: Ginner (Jenner)"), who left for Saco soon after: Gurney's bill and Thomas Lake's note were accepted as the £5 due from Jenner. The nature of Gurney's bill is unstated — it is not evidence of tailoring, military supply, or a 1641/2 transaction — but it is a paper-and-credit tie between John and Weymouth's former minister. On the wider militia question the record is thin: the powder fine reflects only the ordinary readiness obligation every adult man carried — Weymouth and Hingham had belonged to the same regiment since December 1636, and Weymouth furnished five (unnamed) men for the 1636–37 Pequot War — but John appears on no campaign, officer, or volunteer record, and he is absent from the Military Company's 1637–52 roll, so no military service or land mechanism explains his arrival or movements.[^military-followup-2026-06][^ginner-jenner-2026-06]
```

### C1b — extend the existing footnote definition

`str_replace`:

**old_string:**
```
[^military-followup-2026-06]: Petition calendar: "Massachusetts. Military Records 1643–1675" (FamilySearch DGS 007702977), images 947–948 ([ark:/61903/3:1:3Q9M-C9Y5-F9M1-4](https://www.familysearch.org/ark:/61903/3:1:3Q9M-C9Y5-F9M1-4) and -F9M1-C). Bill: "Massachusetts Bay Colony. Military Records 1642–1649" (DGS 008713629), image 48 = volume p. 79 ([ark:/61903/3:1:3QHV-J3DW-8YB3](https://www.familysearch.org/ark:/61903/3:1:3QHV-J3DW-8YB3)); printed index "Gurny, John, 79" at image 169. Read 2026-06-13. Source ID: `familysearch-fulltext-search`.
```

**new_string:**
```
[^military-followup-2026-06]: Petition calendar: "Massachusetts. Military Records 1643–1675" (FamilySearch DGS 007702977), images 947–948 ([ark:/61903/3:1:3Q9M-C9Y5-F9M1-4](https://www.familysearch.org/ark:/61903/3:1:3Q9M-C9Y5-F9M1-4) and -F9M1-C). Bill: "Massachusetts Bay Colony. Military Records 1642–1649" (DGS 008713629), image 48 = volume p. 79 ([ark:/61903/3:1:3QHV-J3DW-8YB3](https://www.familysearch.org/ark:/61903/3:1:3QHV-J3DW-8YB3)); printed index "Gurny, John, 79" at image 169. Read 2026-06-13. Source ID: `familysearch-fulltext-search`.

[^ginner-jenner-2026-06]: Printed text of the 1644 bill: Nathaniel B. Shurtleff, ed., *Records of the Governor and Company of the Massachusetts Bay in New England*, vol. 2, 1642–1649 (Boston: William White, 1853), p. 79 ([Internet Archive `cu31924091024582`](https://archive.org/details/cu31924091024582)) — "John Gurny his byl for 3. 16. 4d & Tho: Lake his note for 1. 3. 8d are accepted for £5 fro Mr Ginner," session beginning 30 October 1644. Identification of "Mr Ginner" as Rev. Thomas Jenner: *History of Weymouth, Massachusetts* (1923), vol. 1, p. (deputy list) — "Mr. Thom: Ginner (Jenner)," chosen deputy 1640; Gilbert Nash, *Historical Sketch of Weymouth* (1885), p. 160 — Jenner at Roxbury 1634–5, called to Weymouth 1636, freeman Dec. 1636, deputy 13 May 1640, then removed to Saco. Source IDs: `massachusetts-bay-records-v2-1853`; `history-of-weymouth`; `nash-historical-sketch-weymouth-1885`.
```

### C2 — Tyng leasehold table row (NEHGR 30:432 primary; distinct from Salter's Farm)

`str_replace`:

**old_string:**
```
| Held 48 Braintree acres "by lease" (Tyng estate) | documented 25 May 1653; lease began earlier (inferred by the early 1650s) | The Tyng inventory records the 48 acres "in the possession of John Gurney"; *Suffolk Deeds, Liber IV* describes one of two Tyng-estate Braintree messuages as occupied "by lease" by John. Tenant, not owner; the lease predates the 1653 inventory (start unrecorded). | NEHGR 30:432; *Suffolk Deeds. Liber IV* |
```

**new_string:**
```
| Held 48 Braintree acres "by lease" (Tyng estate) | documented 25 May 1653; lease already in place before that date | The Tyng probate inventory (25 May 1653) lists "48 Akers land at Brantree, and Marsh in the possession of John Gurney," enumerated **separately** from the Tyng "Salters Farme" (the ~500-acre Mount Wollaston farm John Read carried under a ten-year agreement from 14 April 1639 and Gregory Belcher leased in 1657). John's 48 acres were therefore a distinct Tyng holding, and his tenancy was already running at Tyng's death — not begun afterward. *Suffolk Deeds, Liber IV* describes the messuage as "in the Occupation and by lease in the hands of John Gurney." Tenant, not owner. The figure is 48 acres at primary level (a later NPS cultural-landscape report's 45 acres is looser). | NEHGR 30:432; *Suffolk Deeds. Liber IV* |
```

### C3 — broaden the undated grant-date row (1636 great-lot-roll absence; possession-register bounds)

`str_replace`:

**old_string:**
```
| Original grant of East Field (2 ac) + Mill Field (4 ac) parcels, Weymouth | c. 1641–1642 (inferred) | After arrival, before the 1643 record (which already shows them held by others); the open-field division they sit in is the one whose Nathaniel Adams parcels were "granted between 1642 and 1644." No exact grant date survives. | Nash, App. C; *History of Weymouth* |
```

**new_string:**
```
| Original grant of East Field (2 ac) + Mill Field (4 ac) parcels, Weymouth | c. 1637–1642; best estimate c. 1640–41 | The grants are undated. The small open-field system was active before 1636, so an earlier start is not excluded, but John is absent from the distinct 1636 Fresh Pond great-lot roll of sixteen householders — evidence against a 1636 presence — while the narrower c. 1640–41 estimate fits Weymouth's substantial new-settler influx around 1640 and his first surviving Weymouth appearance. The parcels are recorded by the c. 1643 possession register, already held by other men; that register cannot predate William Fry's death on 26 October 1642 and carries recited instruments to at least 21 May 1644, so its conventional "1643" heading is an approximation, not a grant date. The same open-field division includes the Nathaniel Adams parcels "granted between 1642 and 1644." | Nash, App. C; *History of Weymouth* |
```

---

## 4. Research assimilation — `research/topics/g13-john-gurney-immigration-by-association.md`

### T1 — Braintree forming-plantation paragraph: fold in the land-system frame and the Adams-Braintree result

`str_replace`:

**old_string:**
```
**The Braintree move was into a forming plantation, not an established town.** Braintree was incorporated only in May 1640 — set off from Boston's Mount Wollaston grant of 1634 — and was actively drawing settlers through the early-to-mid 1640s, when the colony's first iron works went up there (1644-45). John's arrival c. 1642–1645 was therefore a *join into a new, still-forming town*, most plausibly drawn by land availability and his own network rather than any forced removal. Braintree took its name from **Braintree, Essex**, and carried a pronounced Essex-origin settler character — which dovetails with John's own Essex ties (his Tyng-estate landlord of Stanford Rivers, Essex; his son-in-law Daniel Shed of Finchingfield, Essex, in Braintree records by 1643). The early Braintree influx was multi-source (Boston, Weymouth, Hingham, and direct-from-England), so John was one of many forming the town rather than part of a single Weymouth contingent; whether specific Weymouth neighbours moved with him is testable against the Braintree settlement record (C. F. Adams, *History of Braintree, 1639–1708*; the *Genealogies of the Families of Braintree, 1640–1850*).[^braintree-founding]
```

**new_string:**
```
**The Braintree move was into a forming plantation, not an established town.** Braintree was incorporated only in May 1640 — set off from Boston's Mount Wollaston grant of 1634 — and was actively drawing settlers through the early-to-mid 1640s, when the colony's first iron works went up there (1644-45). Charles Francis Adams notes that even after 1637 the Mount Wollaston allotments were "large allotments, indicative of a non-resident ownership," and that William Tyng, the Boston merchant, bought the greater part of the Mount Wollaston land in 1639. John's arrival c. 1642–1645 was therefore a *join into a new, still-forming town*, most plausibly drawn by land availability and his own network rather than any forced removal. Braintree took its name from **Braintree, Essex**, and carried a pronounced Essex-origin settler character — which dovetails with John's own Essex ties (his Tyng-estate landlord of Stanford Rivers, Essex, confirmed baptised there 1602/3 and died 1653; his son-in-law Daniel Shed of Finchingfield, Essex, in Braintree records by 1643). The early Braintree influx was multi-source (Boston, Weymouth, Hingham, and direct-from-England), so John was one of many forming the town rather than part of a single Weymouth contingent. Adams's *History of Braintree* is North-Precinct/Quincy-scoped and names no Gurney — John's own freehold lay in the South Precinct on the Monatiquot — so his Braintree neighbours are better recovered from the Braintree town records, Sprague's *Genealogies of the Families of Braintree*, and the Suffolk Deeds abuttals than from that narrative.[^braintree-founding][^adams-braintree-genesis]
```

### T2 — resolve the L-182 neighbour/cohort test (1651/2 cohort scattered, not Braintree-bound)

`str_replace`:

**old_string:**
```
Resolving the texture is the work of lead L-182: confirm the original grant dates from the staged grant-book images, and profile whether the named East/Mill Field neighbours (Randoll, Adams, Hart, Cooke, Staple; Norton, Rawlings, Giles, Brandon) were Rehoboth-bound or Weymouth-stayers — testing whether John's land sat among an arriving cohort or among established proprietors.
```

**new_string:**
```
Profiling the neighbours and the later great-lot cohort answers part of this. John's East/Mill Field abutters were not a single arriving party but a mix of the two documented Weymouth streams — an Aylesbury-Vale Buckinghamshire group (Randall of Wendover, Brandon of Ashton Clinton) threaded with a West-Country/Dorchester group (Richards and Hart via the *Mary and John*; Norton via the Hull company) — set out in the cluster analysis below. And the men listed with John in the 2 February 1651/2 great-lot allotment did not move *with* him: the documented removals among them run to Rehoboth (Samuel Newman, John Allin) and Boston (Thomas Rider), with William Brandon already dead by 1647 — none to Braintree. John's move to Braintree was therefore an individual one, drawn by land and his own network, not part of a Weymouth-to-Braintree contingent. The 1651/2 list itself was a deferred laying-out of "formerly granted" rights that demonstrably included absentees and deceased men, so John's appearance on it reflects a surviving proprietary entitlement, not residence — exactly the non-resident-proprietor position Charles Francis Adams describes for early Massachusetts towns, where such men "were frequently of controlling influence ... yet, not having their residence with the actual settlers, were not entitled to certain exclusive privileges granted to inhabitants." Weymouth's own records fit this: the town "was not settled as a plantation by a definite body of proprietors," its property records are undated (the conventional "1643" is an inference), and a town order of 6 April 1646 forbade any inhabitant to "lett or sell any house, or land, to any person ... that is not an inhabitant amongst us" without first tendering it to the town — the climate a departed proprietor like John faced when his Weymouth right outlasted his residence.<!-- L-182, L-188: neighbour streams + 1651/2 cohort dispersal profiled 2026-06 -->[^adams-braintree-genesis]
```

### T3 — Tyng/Essex counterweight: add the Read comparator, Belcher, and the Bucks kin-link negative

`str_replace`:

**old_string:**
```
**The counterweight — associations are regionally mixed.** John's *Braintree* life points to a different English region entirely. He leased forty-eight acres within the estate of **William Tyng of Stanford Rivers, Essex**; his son-in-law **Daniel Shed came from Finchingfield, Essex** (in Braintree by 1643, married Mary Gurney 1647); and Braintree, Massachusetts took its name from Braintree, Essex. So John's documented colonial networks span three English regions — **Buckinghamshire** (his Weymouth land-neighbours), **Essex** (his Braintree estate and son-in-law), and **Norfolk** (the favoured Candidate-B origin) — with no single stream claiming him. That mixing is itself the lesson: in this case association is a *weak* origin signal, because John attached to whichever local network held land or kin. The Bucks neighbour-cluster is therefore best treated as a **reception context to test**, on a par with the Essex Braintree network — not an origin claim — and the direct evidence (the East Dereham baptism) remains the stronger basis for Candidate B.[^essex-braintree]
```

**new_string:**
```
**The counterweight — associations are regionally mixed.** John's *Braintree* life points to a different English region entirely. He leased forty-eight acres within the estate of **William Tyng of Stanford Rivers, Essex** (baptised there 16 January 1602/3, died 1653); his son-in-law **Daniel Shed came from Finchingfield, Essex** (in Braintree by 1643, married Mary Gurney 1647); and Braintree, Massachusetts took its name from Braintree, Essex. The closest structural parallel to John's own position is **John Read**, who likewise held early Weymouth land, took a Tyng farm at Mount Wollaston under a ten-year agreement (from 14 April 1639), received a Braintree grant, later removed to Rehoboth, and still drew an 18-acre Weymouth great lot in 1651/2 — the same pattern of a Weymouth proprietary right carried alongside a Tyng tenancy and a move elsewhere; Read had married into a Suffolk family (Lessie of Blyborough). John's *paired* Tyng co-tenant, Gregory Belcher, was from Warwickshire (Aston). By his last years John held three Braintree-area interests at once — the small five-acre Monatiquot freehold he sold in 1661/2, the larger leased Tyng farm, and a residual Weymouth proprietary right — an ordinary mixed tenure for a tradesman without the capital to buy a working farm, not an anomaly. So John's documented colonial networks span several English regions — **Buckinghamshire** (his Weymouth land-neighbours), **Essex** and **Warwickshire** and **Suffolk** (his Braintree estate, son-in-law, and Tyng-tenant peers), and **Norfolk** (the favoured Candidate-B origin) — with no single stream claiming him. That mixing is itself a lesson: John attached to whichever local network held land or kin, so association is a *weak* lever for most of these regions. It is weak specifically for the Buckinghamshire neighbour-cluster as a *kin source*: the Bucks Gurney households cluster in the Aylesbury–Stewkley–Chesham–Edlesborough arc, with **no Gurney recorded in Wendover, Lee, or Ashton Clinton** — the very parishes that supplied the Humphrey–Hunt–Randall–Brandon neighbours — so there is no Gurney kin behind that cluster. The Bucks neighbour-cluster is therefore best treated as a **reception context to test**, not an origin claim, and the direct evidence (the East Dereham baptism) remains the stronger basis for Candidate B.[^essex-braintree][^tyng-read-belcher]
```

### T4 — strengthen the Hingham paragraph with the quantified Cushing data

`str_replace`:

**old_string:**
```
A near-monolithic Weymouth would make a Norfolk John anomalous; the passenger-list and town-origin evidence in hand already shows Weymouth was *bi-regional* (West Country + Bucks) rather than single-source, so a Norfolk arrival by way of adjacent Hingham is not a strained hypothesis but a testable one. This is the more promising line than the Bucks-neighbour coincidence, because it connects John's reception directly to the documented Norfolk-Gurney–to–New-England corridor.[^hingham-corridor]
```

**new_string:**
```
Weymouth was not monolithic but it was firmly West-Country-led — Rev. Joseph Hull's 1635 company out of Somerset and Dorset — with the Aylesbury-Vale Buckinghamshire stream second; no Norfolk stream fed it, so a Norfolk John would indeed have been an outsider to Weymouth's own settlers. Adjacent Hingham is the opposite case, and the correlation is strong and quantified: Daniel Cushing's contemporary list records that "the whole number that came out of Norfolk (chiefly from Hingham, and its vicinity) from 1633 to 1639, and settled in this Hingham, was two hundred and six," the 1638 *Diligent* alone bringing 133. That cohort came out of the very parishes in which the direct-line Gurneys are documented — Hingham, Wymondham, Attleborough, Great Ellingham, Deopham — with named founders Stephen Payne of Great Ellingham, John Sutton of Attleborough, the Lincolns of Wymondham, and the Gilman, Peck, and Cushing families of Hingham, the same orbit as the Ann Gurney × John Gilman marriage at Hingham, Norfolk. A dense community from John's own family's Norfolk country thus sat under ten miles away, directly across the town line his Weymouth lots "but on." A Norfolk arrival received through that adjacent Norfolk colony is therefore not a strained hypothesis but the reception model that best fits Candidate B — connecting John's landing directly to the documented Norfolk-Gurney–to–New-England corridor.[^hingham-corridor][^hingham-cushing-list]
```

### T5 — add the reception synthesis (Ludden Old Planter; King; Jenner) to the Associate rings / Current evidence

`str_replace`:

**old_string:**
```
The first colonial anchor remains the June 1641 General Court record: John Gurney, James Ludden, and John Porter had fines remitted for want of gunpowder. The court line itself does not supply residence, age, origin, ship, or family structure. The Weymouth placement comes from supporting local-history context, especially the Porter genealogy's gloss that Ludden and Gurney were of Weymouth.[^mbcr-porter]
```

**new_string:**
```
The first colonial anchor remains the June 1641 General Court record: John Gurney, James Ludden, and John Porter had fines remitted for want of gunpowder. The court line itself does not supply residence, age, origin, ship, or family structure. The Weymouth placement comes from supporting local-history context, especially the Porter genealogy's gloss that Ludden and Gurney were of Weymouth.[^mbcr-porter] The two men John is grouped with are both established Weymouth settlers, not fellow newcomers: **James Ludden** was an "Old Planter," at Wessagusset/Weymouth by 1632 (Winthrop's guide across Luddam's Ford), and the Porter of the underlying petition is **Richard Porter**, a 1635 Rev. Hull–company settler. John's later Weymouth ties run the same way — his 1663 estate owed "Goodman King of Waymouth," who was **John King**, an early King's-Cove seaman and planter. The 1641 fine group, and these continuing debts, therefore read as the reception of a newcomer *into* an established Weymouth community rather than as evidence of a shared emigration. A separate 1644 colony-accounts entry adds a paper tie to **Rev. Thomas Jenner**, Weymouth's minister 1636–40: the General Court accepted "John Gurny his byl for 3. 16. 4d" with Thomas Lake's note of £1 3s 8d as the £5 due "fro Mr Ginner" (Jenner) — a credit relationship of unstated origin, not the "16 March 1641/2" transaction an earlier misreading of the figures had produced.[^ludden-king-jenner]
```

### T6 — new subsection surfacing the Weymouth allocation systems and John's cohort (insert before the Buckinghamshire-cluster heading)

`str_replace`:

**old_string:**
```
## The Buckinghamshire (Aylesbury-Vale) cluster around John's grants
```

**new_string:**
```
## The Weymouth land system and John's grant cohort

Weymouth ran several distinct land systems, and reading John's parcels against them is what dates and contextualizes them. The scattered open-field system — small one-to-eight-acre strips in named planting fields — was active before 1636: the East Field was already being granted by 1635 (Zachary Bicknell's East Field parcel was sold after his death by 9 March 1636/7). John's known package — two acres in the East Field, two more there, and four acres in the Mill Field — is ordinary settler accommodation in that system, and his parcels sit among roughly 176 "first granted" chain-of-title clauses spread over about 138 holders, with close analogues in the same record (Walter Harris's eight Mill Field acres, John Harding's six, John Barnard's eight, Matthew Pratt's composite twenty). They are normal, not exceptional.

A separate, household-scaled allocation — the 1636 Fresh Pond "great lots," six acres per adult and three per child under twelve — went to sixteen named men: Edward Bennett, Joseph Hull, Henry Kingman, Thomas Jenner Sr., Thomas White, William Fry, Robert Lovell, Edmund Hart, Thomas Rawling, Thomas Jenner Jr., William Read, Richard Sylvester, Richard Adams, William Smith, Stephen French, and John Upham. **John Gurney is absent from it** — evidence against his being at Weymouth as early as 1636 — though two of his later East Field abutters, Edmund Hart and Thomas Rawling, were already in that 1636 cohort.

John's other Weymouth land, great lot no. 16 of 2–3 February 1651/2, belongs to yet another exercise: the laying-out of rights "named in the old town Book and formerly granted." That list demonstrably carried absentees and the dead — Samuel Newman (no. 6) had gone to Rehoboth in 1643/44, John Allin (no. 17) to Rehoboth in 1643, Thomas Rider (no. 24) to Boston, James Britton to Woburn (and was executed in 1643), and William Brandon (no. 20) was dead by November 1647 — so John's place on it reflects a surviving proprietary entitlement, not residence, and none of these cohort-mates moved to Braintree with him. The closest parallel to John's whole pattern is **John Read**, who likewise held Weymouth land, took a Tyng Mount Wollaston farm under a ten-year agreement from 14 April 1639, received a 44-acre Braintree grant in 1640, removed to Rehoboth, and still drew an 18-acre Fresh Pond great lot in 1651/2 — a Weymouth right carried alongside a Tyng tenancy and a move elsewhere (Read had married into a Suffolk family, the Lessies of Blyborough). The later 1663 "First/Second Division" lots are different again — laid out 14 December 1663 westward toward the Braintree line — and should not be back-projected onto John's 1640s strips.[^weymouth-land-cohort]

## The Buckinghamshire (Aylesbury-Vale) cluster around John's grants
```

(The `[^weymouth-land-cohort]` footnote is defined in the §5 footnote-definitions block.)

---

## 5. New footnote definitions

### Topic file — add after the existing `[^hingham-corridor]` definition

`str_replace` (anchor on the end of the existing `[^braintree-founding]` footnote; append the new definitions):

**old_string:**
```
[^braintree-founding]: Braintree, Massachusetts was incorporated by the General Court on 13 May 1640, set off from Boston's 1634 Mount Wollaston grant, and was named for Braintree, Essex, England — "from which many settlers originated"; the colony's first iron works was built there 1644-45 (John Winthrop Jr.; tax exemption and 21-year monopoly granted 15 October 1645). Town of Braintree, "Historic Information," https://braintreema.gov/461/Historic-Information; *Encyclopædia Britannica*, "Braintree." For identifying specific Weymouth-to-Braintree movers and John Gurney's Braintree neighbours: Charles Francis Adams, *History of Braintree, Massachusetts (1639–1708)* (https://archive.org/details/historyofbraintr00adam) and the *Genealogies of the Families of Braintree, Mass., 1640–1850* — not yet mined.
```

**new_string:**
```
[^braintree-founding]: Braintree, Massachusetts was incorporated by the General Court on 13 May 1640, set off from Boston's 1634 Mount Wollaston grant, and was named for Braintree, Essex, England — "from which many settlers originated"; the colony's first iron works was built there 1644-45 (John Winthrop Jr.; tax exemption and 21-year monopoly granted 15 October 1645). Town of Braintree, "Historic Information," https://braintreema.gov/461/Historic-Information; *Encyclopædia Britannica*, "Braintree."

[^adams-braintree-genesis]: Charles Francis Adams, *History of Braintree, Massachusetts (1639–1708)* (Cambridge: Riverside Press, 1891), pp. 5, 109 ("large allotments, indicative of a non-resident ownership"; Tyng's 1639 Mount Wollaston purchase) — a full-text scan finds no colonial Gurney; and Adams, "The Genesis of the Massachusetts Town," *Proceedings of the Massachusetts Historical Society*, 2nd ser., vol. 7 (1892), pp. 190–192 (Weymouth's undated property records; no proprietor-body; the 6 April 1646 anti-stranger order; the non-resident-proprietor doctrine). Verbatim extracts at [`sources/corpus_supplement/adams-genesis-massachusetts-town-1892-weymouth-land.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/adams-genesis-massachusetts-town-1892-weymouth-land.md). The 1651/2 cohort dispersal (Newman and Allin to Rehoboth, Rider to Boston) is from the *History of Weymouth* (1923) family entries. Sprague's *Genealogies of the Families of Braintree* (the standard compiled Braintree genealogy, `sprague-braintree`) is the family-level source for John's Braintree household; the family-specific Faxon and Brackett genealogies on Internet Archive carry no colonial Gurney. Source IDs: `adams-history-of-braintree-1891`; `adams-genesis-massachusetts-town-1892`; `history-of-weymouth`; `sprague-braintree`.

[^tyng-read-belcher]: William Tyng baptised 16 January 1602/3 at Stanford Rivers, Essex, died 18 January 1653 (compiled genealogies; consistent with case file §10.3). John Read's Tyng tenancy, Braintree grant, removal to Rehoboth, and 1651/2 great lot: *History of Weymouth, Massachusetts* (1923), vol. 4, p. 151 (citing Lechford's Note-Book, 94–99). Gregory Belcher of Warwickshire (baptised Aston 1606): compiled genealogies. The 48-acre Tyng parcel "in the possession of John Gurney," distinct from "Salters Farme": NEHGR 30:432 (Tyng inventory, 25 May 1653), extract at [`sources/corpus_supplement/tyng-inventory-1653-nehgr-30-432-john-gurney.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/tyng-inventory-1653-nehgr-30-432-john-gurney.md). The Bucks Gurney distribution (no Gurney in Wendover/Lee/Ashton Clinton) is from the case-file §8.3 sweep. Source IDs: `nehgr-30-432`; `history-of-weymouth`.

[^hingham-cushing-list]: Daniel Cushing's settler list and the 206-from-Norfolk total: *History of the Town of Hingham, Massachusetts* (1893), vol. 1, pp. 201–203; English parishes of origin in vol. 2 (e.g. the Lincolns "from Wymondham, County of Norfolk"). No colonial Gurney settled at Hingham. Verbatim extract at [`sources/corpus_supplement/hingham-massachusetts-norfolk-emigrant-cohort-1633-1639.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/hingham-massachusetts-norfolk-emigrant-cohort-1633-1639.md). Source ID: `history-of-town-of-hingham-1893`.

[^ludden-king-jenner]: James Ludden the "Old Planter" at Wessagusset/Weymouth by 1632 (Luddam's/Ludden's Ford): Wallace Ludden, *James Ludden, the Old Planter, 1611–1692 and Descendants* ([Internet Archive `jamesluddenoldpl00ludd`](https://archive.org/details/jamesluddenoldpl00ludd)), and *History of Weymouth* (1923). John King of Weymouth (King's Cove seaman/planter, b. c. 1600): *History of Weymouth* (1923) and compiled accounts. Rev. Thomas Jenner at Weymouth 1636–40 then Saco: Gilbert Nash, *Historical Sketch of Weymouth* (1885), p. 160; *History of Weymouth* (1923), vol. 1 (deputy list, "Mr. Thom: Ginner (Jenner)"). The 1644 bill: Mass. Bay Records, vol. 2 (1853), p. 79. Source IDs: `history-of-weymouth`; `nash-historical-sketch-weymouth-1885`; `massachusetts-bay-records-v2-1853`.

[^weymouth-land-cohort]: Gilbert Nash, *Historical Sketch of the Town of Weymouth* (1885), Appendix C: the 1636 Fresh Pond great-lot roll of sixteen householders (pp. 280; corpus `nash-historical-sketch-weymouth-1885.txt:10753-10784`), the small-strip parcels and "first granted" clauses (pp. 258–280), and the 2–3 February 1651/2 great-lot lists naming John no. 16 (pp. 281–282; corpus `:10792-10811`); the "land divided from time to time" note (corpus `:1384-1390`). Absentee/deceased comparators in *History of Weymouth, Massachusetts* (1923): Samuel Newman (vol. 1 corpus `:4278-4289`), John Allin (vol. 3 `:416-420`), Thomas Rider (vol. 4 `:8727-8735`), James Britton (vol. 3 `:6042-6052`), William Brandon (vol. 3 `:5894-5903`); John Read's comparator profile (vol. 4 `:6920-6953`); the Pequot quota (vol. 1 `:4818-4823, 15792-15796`). Militia framework: Massachusetts Bay Colony Records, vol. 1, pp. 84–85, 186–87, 327–32. Source IDs: `nash-historical-sketch-weymouth-1885`; `history-of-weymouth`; `massachusetts-bay-records-v1-1853`.
```

---

## 6. Lead actions (applied directly via `research_leads.py`; listed here for traceability)

- **L-95** (military petition/bill) — core complete: bill re-read (£3 16s 4d + £1 3s 8d = £5, 30 Oct 1644), "Ginner" = Jenner identified, printed source registered. **Lower priority** (residual: higher-resolution manuscript image of the entry).
- **L-144** (Tyng leasehold origin) — acreage resolved (48, primary), parcel distinct from Salter's Farm, lease in place by 1653. **Lower priority** (residual: exact lease-start date from the manuscript inventory).
- **L-185** (Ludden / Weymouth reception) — Ludden resolved as Old Planter; reception-into-established-community established. **Close** (or low residual: Ludden's English origin via the Wallace Ludden genealogy).
- **L-188** (Weymouth regional composition + Hingham hop) — composition (West-Country-led + Bucks) and the strong Norfolk-Hingham correlation documented. **Lower priority.**
- **L-187** (Bucks Aylesbury-Vale kin link) — negative (no Gurney in Wendover/Lee/Ashton Clinton). **Keep open, low** (residual: direct register pull of those three parishes).
- **L-189** (Weymouth→Braintree movers + Braintree neighbours) — 1651/2 cohort scatter found; Braintree-genealogy sources mapped (Adams = N. Precinct; Faxon/Brackett negative). **Lower priority** (residual: Braintree town records / Suffolk Deeds abuttals for South-Precinct neighbours).
- **NEW lead** — Rev. Thomas Jenner paper trail: trace Jenner's Saco/probate and Thomas Lake records for any further Gurney/Lake account, to characterize the 1644 bill. Online: Part.

---

## 7. Source-tracking summary

| sourceId | New? | Validation | Corpus |
|---|---|---|---|
| `nehgr-30-432` | yes | create | `sources/corpus_supplement/tyng-inventory-1653-nehgr-30-432-john-gurney.md` (added directly) |
| `adams-genesis-massachusetts-town-1892` | yes | create | `sources/corpus_supplement/adams-genesis-massachusetts-town-1892-weymouth-land.md` (added directly) |
| `adams-history-of-braintree-1891` | yes | create | (folded into the Adams *Genesis* supplement) |
| `history-of-town-of-hingham-1893` | yes | create | `sources/corpus_supplement/hingham-massachusetts-norfolk-emigrant-cohort-1633-1639.md` (added directly) |
| `massachusetts-bay-records-v2-1853` | yes | create | (printed-text citation; extract in footnote) |
| `history-of-weymouth`, `nash-historical-sketch-weymouth-1885`, `familysearch-fulltext-search` | existing | — | reused in C1/C1b/T5 |
```
