**Done:** 2026-06-21 19:44 PT

# Patchset v111 — multi-source enrichment of the G13 findings + G22 harvest correction

**Premise: the repo as it now stands (v108 and v109 applied/done) plus v110 pending.** This patchset (1) adds the *additional witnesses* the multi-source principle requires to findings already in the live G13 companion (a corroborating source is added, not skipped), and (2) corrects the now-applied G22 harvest paragraph so it holds only its own subject — v110 routes the per-ancestor fines to G20/G23/G29, so the G22 paragraph's other-ancestor enumeration is trimmed to a pointer here. No new sourceIds (all reused).

All `str_replace` targets are the current live files.

---

## Item 1 — Newgate: add Savage as a corroborating witness (G13 companion)

`str_replace` in `research/people/g13-john-gurney-fact-sheet.research.md`:

**old_string:**
`The primary will/codicil in Suffolk probate is the level above this compiled abstract (lead L-160). Source ID: \`wikitree-newgate-14-horningsheath\`.`

**new_string:**
`The primary will/codicil in Suffolk probate is the level above this compiled abstract (lead L-160). Savage's *Genealogical Dictionary of the First Settlers of New England* (Newgate entry) independently lists the same Newgate family, marriages, and legatees with **no Gurney** among them — a second compiled witness to the same negative. Source IDs: \`wikitree-newgate-14-horningsheath\`; \`savage-dictionary\`.`

---

## Item 2 — Marriage-negative: add the second/third indexed witnesses + coverage proof (G13 companion)

`str_replace` in `research/people/g13-john-gurney-fact-sheet.research.md`:

**old_string:**
`returned no Gurney-variant groom; Great Dunham marriages are absent from the indexed sets. Source ID: \`fs-england-births-christenings\`. See lead L-161.`

**new_string:**
`returned no Gurney-variant groom. The indexed absence is corroborated across additional independent sources: the Norfolk FHS "Banns & Marriages" set shows John Gurn\*/Gourn\* marriages at 1591 then none until 1663 (no 1620s John × Mary), and the Norfolk marriage-licence-bond index (Ancestry collection 62679) holds no early-17th-century Gurney bond. The gap is shown to be a coverage limitation, not surname-munging: a 783-record "Wales" / 69-record "Mary Wales" test confirms Great Dunham and Bawdeswell marriages are absent from these sets entirely, so the emigrant's marriage (and any Mary Wales marriage there) simply is not indexed. Source IDs: \`fs-england-births-christenings\`; \`findmypast-norfolk-banns-marriages-index\`; \`norfolk-wills-probate-index-1371-1858\`. See lead L-161.`

---

## Item 3 — Yarmouth Edward: add the Norfolk-FHS and Aldgate witnesses (G13 companion)

`str_replace` in `research/people/g13-john-gurney-fact-sheet.research.md`:

**old_string:**
`the only contemporary Edward Gurney × Ann marriage is St Bride Fleet Street, London, 1608/9. Source IDs: \`fs-england-births-christenings\`; \`fs-england-marriages-1538-1973\`. See lead L-159.`

**new_string:**
`the only contemporary Edward Gurney × Ann marriage is St Bride Fleet Street, London, 1608/9. The Norfolk FHS "Banns & Marriages" set independently confirms no Edward Gurney × Anne marriage in Norfolk, and a St Botolph without Aldgate (London) baptism of 1622 to an **Edward & Anne Gourney** points the same way — to a London-derived Edward, not the 1610-born brother. Source IDs: \`fs-england-births-christenings\`; \`fs-england-marriages-1538-1973\`; \`findmypast-norfolk-banns-marriages-index\`. See lead L-159.`

---

## Item 4 — Gilman: record the genealogies actually read (G13 companion)

`str_replace` in `research/people/g13-john-gurney-fact-sheet.research.md`:

**old_string:**
`Ann's kinship to Francis G14 is undocumented and the compiled Gilman pedigrees are conflated (lead L-157).`

**new_string:**
`Ann's kinship to Francis G14 is undocumented and the compiled Gilman pedigrees are conflated; the three archive.org Gilman family histories were read for her parentage and give none — only the Hingham manor named "Gurneys", not Ann's kin — leaving Davis (1963), offline, as the residual authority (lead L-157).[^gilman-genealogies-2026-06]

[^gilman-genealogies-2026-06]: Three compiled Gilman genealogies read June 2026 for Ann Gurney's parentage, all negative (none names her father): A. W. Gillman, *Searches into the History of the Gillman or Gilman Family* (1895), [Internet Archive \`searchesintohist01gill\`](https://archive.org/details/searchesintohist01gill); *The Story of the Gilmans and a Gilman Genealogy of the Descendants of Edward Gilman of Hingham, England, 1550–1950*, [\`storyofgilmansan00ames\`](https://archive.org/details/storyofgilmansan00ames); and the Gilman family tract [\`gilmanfamilytrac00gilm\`](https://archive.org/details/gilmanfamilytrac00gilm) — the latter two carry only the Hingham manor named "Gurneys." The standing authority, G. C. Davis, *The Gilman Family* (1963), is not freely online. Source ID: \`fs-england-births-christenings\` (for the underlying Hingham/Deopham IGI records).`

---

## Item 5 — Mary Gurney × John Allen 1622 Norwich comparator (G13 companion)

`str_replace` in `research/people/g13-john-gurney-fact-sheet.research.md` — append to the existing Norwich-comparator footnote.

**old_string:**
`A SW-Norwich household; not a candidate. Source IDs: \`fs-england-marriages-1538-1973\`; \`findmypast-norfolk-baptisms-index\`.`

**new_string:**
`A SW-Norwich household; not a candidate. A second 1622 Norwich Gurney datum from the surname-agnostic sweep is **Mary Gurney m. John Allen, 12 February 1622, Norwich** — a Gurney daughter marrying *out* of the same Norwich same-name orbit (the index renders "Gurney" cleanly here, confirming the emigrant-marriage gap is coverage, not transcription); likewise not the emigrant's family. Source IDs: \`fs-england-marriages-1538-1973\`; \`findmypast-norfolk-baptisms-index\`.`

---

## Item 6 — correction: trim the (applied) G22 harvest to its own subject

The G22 companion's applied feet-of-fines paragraph enumerates records about other ancestors; v110 routes those to their subject companions (G20/G23/G29). Trim the G22 enumeration to a pointer so G22 holds only Robert's own fine and the Tharston/Saxthorpe candidate leads.

`str_replace` in `research/people/g22-robert-gournay-fact-sheet.research.md`:

**old_string:**
`The wider Gurnay landholding harvest (full list and entry numbers in [\`sources/corpus_supplement/norfolk-feet-of-fines-gurnay-entries-rye.md\`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/norfolk-feet-of-fines-gurnay-entries-rye.md)) adds several **direct-line** records previously unseen: **Thomas Gurnay, Esq. ("Armiger"), and Margaret his wife** in Westlexham, Eastlexham, Castleacre, Newton, and Great Dunham (Pt II #200 — a primary attestation of a gentry Thomas of the G20/G21 generation *and his wife's name*, lead L-164); **John Gurnay, rector of Harpley**, holding the manor of Harpley and land in Gaywood (Pt II #489, lead L-165); **John Gournay and Alicia his wife**, manors of Heylesdon and Drayton (Pt II #262 — Sir John Gurney V × Alice Heylesdon, the fine behind the Heylesdon settlement); **Edmund Gournay**, manor of Hingham (Pt II #1526); and the earlier-line Harpley/Saxthorpe/Hardingham/Hillington Gurnays in Part I (Matthew de Gurnay at Harpley #236; John de Gurney of Saxthorpe #837; John de Gurney in Hardingham #1593; Hillington #1059).`

**new_string:**
`The wider Gurnay harvest names records about other generations, each routed to its own subject companion (Thomas Gurnay, Esq. & Margaret → **G20** #200; Matthew at Harpley → **G29** #236; Edmund Gournay's Hingham trusteeship, the John-&-Alicia Heylesdon fine, and the Rector-John Saxthorpe/Harpley fines → **G23** #1526/#262/#837/#489; via patchset v110), with the full list and the unattributed same-name fines kept in [\`sources/corpus_supplement/norfolk-feet-of-fines-gurnay-entries-rye.md\`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/norfolk-feet-of-fines-gurnay-entries-rye.md).`
