**Done:** 2026-06-23 07:12 PT

# Patchset v114 — Bokkyng/Fastolf affinity, Maldon heir & the Quaker "Problem", emigration-list negative, Braintree Y-DNA

Phase-1 patchset for the 2026-06-22/23 research thread's net-new findings (the round *after* v113). Leads, the lead-CSV updates, and the paleography packet briefs (34–36) are **already in the repo** and are not repeated here. This patchset lands the source additions, validations, and research-companion promotions.

**Apply order — depends on v113.** v113 is drafted but intentionally held un-applied (to keep the repo stable across the thread). **Apply v113 first, then v114.** v114's G20 and G13 edits are written to target the repo *after* v113 is applied; the two patchsets touch different anchors (v113: the G20 #200 table row + its footnote, the G13 Peter-Wales paragraph + a new footnote; v114: a new G20 subsection appended at end-of-file, and two G13 inserts in different sections), so applied in order they do not collide.

**Source basis.** DNB "Bocking" family note (Nicholas Bocking in Fastolf's service; Bockings of Longham); Hotten *Original Lists* full-text search (emigrant negative + the "Gummy" lookalike); FamilyTreeDNA Gurney project + public Discover (Braintree Y-line); Burke's *Landed Gentry* "Gurney of Maldon" pedigree (tertiary, the "Problem" corroboration); the existing `familysearch-fulltext-search` catch-all (Maldon court-book Gournay entries). Four new sourceIds: `dnb-bocking`, `hotten-original-lists-1874`, `ftdna-gurney-ydna`, `burke-landed-gentry-gurney`.

---

## Item 1 — `data/sources.json`: add four new source entries

**Outcome: promote.** One `str_replace` inserting four entries at the boundary after the `dnb-edmund-gurney-1890` entry.

**old_string:**
```
      "notes": "Core public-domain biographical source for Edmund Gurney/Gurnay, d.1648: parentage, Cambridge chronology, Edgefield and Harpley livings, Puritan inclination, surplice anecdote, burial at St Peter Mancroft Norwich on 14 May 1648, wife Ellen, apparent son Protestant, works list, and Gurnay/Gurney spelling note."
    },
    "ggm-benefice-harpley-rectors": {
```

**new_string:**
```
      "notes": "Core public-domain biographical source for Edmund Gurney/Gurnay, d.1648: parentage, Cambridge chronology, Edgefield and Harpley livings, Puritan inclination, surplice anecdote, burial at St Peter Mancroft Norwich on 14 May 1648, wife Ellen, apparent son Protestant, works list, and Gurnay/Gurney spelling note."
    },
    "dnb-bocking": {
      "shortTitle": "DNB - Bocking (Nicholas Bocking / Fastolf service note)",
      "citation": "\"Bocking, Edward (d. 1534).\" In Leslie Stephen, ed., Dictionary of National Biography, vol. 5. London: Smith, Elder & Co., 1886.",
      "archive": "Wikisource transcription of Dictionary of National Biography, 1885-1900, vol. 5",
      "url": "https://en.wikisource.org/wiki/Dictionary_of_National_Biography,_1885-1900/Bocking,_Edward",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/dnb-bocking.md",
      "notes": "Dictionary of National Biography (1885-1900), vol. 5, 'Bocking, Edward' entry. Used only for its appended family note naming a Nicholas Bocking in Sir John Fastolf's service and the Bocking family's Longham (Norfolk) / Ash Bocking (Suffolk) holdings; the entry's main subject (Edward Bocking, the Canterbury monk) is unrelated. The one relevant sentence is quoted in the G20 companion footnote."
    },
    "hotten-original-lists-1874": {
      "shortTitle": "Hotten, Original Lists of Persons of Quality (1874)",
      "citation": "Hotten, John Camden, ed. The Original Lists of Persons of Quality; Emigrants; Religious Exiles ... Who Went from Great Britain to the American Plantations, 1600-1700. London: Chatto and Windus, 1874.",
      "archive": "Internet Archive (originallistsofp00hottuoft)",
      "url": "https://archive.org/details/originallistsofp00hottuoft",
      "corpusStatus": "extract",
      "corpusPath": "sources/corpus_supplement/hotten-original-lists-gurney-search-2026.md",
      "mediaPath": null,
      "validationPath": "sources/validations/hotten-original-lists-1874.md",
      "notes": "Standard published transcription of the surviving 1600-1700 London port emigration / examination registers (TNA E157 and allied State Papers); records emigrants' names, ages, ships, destinations, and conformity certificates. Searched for the Gurney surname; the relied-on extracts (the 1635 America/Virginia list and the 1634 Dartmouth oath list) are captured in the corpus supplement."
    },
    "ftdna-gurney-ydna": {
      "shortTitle": "FTDNA Gurney Y-DNA project + Discover (public)",
      "citation": "FamilyTreeDNA, Gurney surname Y-DNA project (administrator Caroline Gurney) and public Discover Y-DNA haplogroup reports, familytreedna.com / discover.familytreedna.com. Consulted June 2026.",
      "archive": "FamilyTreeDNA (public project results and Discover haplotree reports)",
      "url": "https://discover.familytreedna.com/y-dna/R-FTD83678/tree",
      "corpusStatus": "extract",
      "corpusPath": "sources/corpus_supplement/ftdna-gurney-ydna-braintree-line-2026.md",
      "mediaPath": null,
      "validationPath": "sources/validations/ftdna-gurney-ydna.md",
      "notes": "Public FamilyTreeDNA Gurney surname Y-DNA project and Discover haplotree reports; direct-paternal-line (Y-DNA) data for the Braintree Gurney line (project kit 576097, earliest known ancestor 'John Gurney b.1603 d.1663', terminal SNP R-FTD83678). The relied-on project and Discover data are captured in the corpus supplement."
    },
    "burke-landed-gentry-gurney": {
      "shortTitle": "Burke's Landed Gentry - Gurney of Maldon pedigree (tertiary)",
      "citation": "Burke, John, and John Bernard Burke. A Genealogical and Heraldic Dictionary of the Landed Gentry of Great Britain and Ireland. London: Henry Colburn / Harrison, editions 1850s-1870s. 'Gurney' pedigree, 'Gurney of Maldon' branch.",
      "archive": "Consulted via FamilySearch Full-Text Search (digitised editions), June 2026",
      "url": "",
      "corpusStatus": "extract",
      "corpusPath": "sources/corpus_supplement/burke-landed-gentry-gurney-of-maldon.md",
      "mediaPath": null,
      "validationPath": null,
      "notes": "Tertiary compiled pedigree (a collector, not a primary authority - trace to primary before citing for any genealogical fact): Burke's Landed Gentry 'Gurney' pedigree, including the 'Gurney of Maldon' branch. The relied-on extract is captured in the corpus supplement."
    },
    "ggm-benefice-harpley-rectors": {
```

---

## Item 2 — new validation worksheets (thin)

**Outcome: promote.** Three new-file writes. (No validation for `burke-landed-gentry-gurney`: a single tertiary discovery-trail citation, consistent with the existing `burke-ancient-family` entry which carries none.)

### 2a. New file write — `sources/validations/dnb-bocking.md`
```markdown
# Validation — DNB, "Bocking" (Nicholas Bocking / Fastolf-service note)

**Source.** Dictionary of National Biography (1885-1900), vol. 5, "Bocking, Edward (d.1534)"; Wikisource transcription. Source ID: `dnb-bocking`.

**What was examined.** The appended Bocking-family note within the Edward Bocking entry, June 2026.

**Portion / scope.** Only the family note: "A Nicholas Bocking was also in Sir John Fastolf's service," and the Bockings of Ash Bocking, Suffolk, holding property at Longham, Norfolk, 15th-16th c. The entry's main subject (Edward Bocking, Canterbury monk) is not used.

**Findings landed.** `research/people/g20-thomas-gournay-ii-fact-sheet.research.md` (the #200-feoffee Nicholas Bokkyng = a Fastolf-service man, tightening the Fastolf-affinity reading).

**Caveats.** A short tertiary biographical note; corroborates, does not prove, the identification of the fine's Bokkyng with Fastolf's servant.
```

### 2b. New file write — `sources/validations/hotten-original-lists-1874.md`
```markdown
# Validation — Hotten, Original Lists of Persons of Quality (1874)

**Source.** John Camden Hotten, ed., *The Original Lists of Persons of Quality ... 1600-1700* (London: Chatto and Windus, 1874). Source ID: `hotten-original-lists-1874`.

**What was examined.** Full OCR text (Internet Archive `originallistsofp00hottuoft`), searched June 2026 for the emigrant John Gurney.

**Portion / scope.** Whole-text search across the Modern Gurney variant registry plus OCR-mangle patterns (rn->m, G->C, u->n) and the printed index; coverage confirmed (tailor/Weymouth/Braintree present).

**Findings landed.** `research/people/g13-john-gurney-fact-sheet.research.md` (no John Gurney in the published emigration lists = reliable negative; the 'Richard Gum[m]y' America/Virginia 1635 hit resolves to surname Gummy, not Gurney).

**Caveats.** Hotten's list survival is partial (not every ship/year survives); all readings here trace to Hotten - the independent arbiters are Coldham and TNA E157/20 (lead L-170).
```

### 2c. New file write — `sources/validations/ftdna-gurney-ydna.md`
```markdown
# Validation — FTDNA Gurney Y-DNA project + Discover (public)

**Source.** FamilyTreeDNA Gurney surname Y-DNA project and public Discover haplotree reports. Source ID: `ftdna-gurney-ydna`.

**What was examined.** Public Discover pages for R-FTD83678 and its upstream SNPs (tree, country-frequency, ancestral-path, suggested-projects) and the public project summary, June 2026. No login; no kit-owner contact.

**Portion / scope.** Braintree-line kit 576097 (EKA 'John Gurney b.1603 d.1663'), Big Y-700 terminal R-FTD83678 within R1b > P312 > DF19 > R-Z27053. Parent-branch country frequencies and project affiliations read from the public table view.

**Findings landed.** `research/people/g13-john-gurney-fact-sheet.research.md` (paternal Y-line; continental NW-European nearest-cousin signal).

**Caveats.** Terminal/parent branches have very few testers (small-sample, deep, pre-surname); self-reported origins. The decisive comparison (project kit 365744 vs a documented English Gurney) needs the project chart or the kit owner (lead L-145).
```

---

## Item 3 — `research/people/g20-thomas-gournay-ii-fact-sheet.research.md`: Bokkyng = a Fastolf-service man

**Outcome: promote.** One `str_replace` appending a new subsection at end-of-file (after the Armstrong 1447 footnote). Builds on v113's #200/Fastolf-affinity edit (Item 3 of v113).

**old_string:**
```
[^v71-armstrong-1447-berninghams]: Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 5 (Norwich, 1781), Gallow Hundred entry for East Barsham — Berningham's / Knold's / Waldgrave's Manor: "In the 25th of Henry VI. March 9, John Hines, of Swaffham in Norfolk, sells to John Wode the manor of Berningham for fifty marks; and on the 10th of the said month, Robert Mompynson, of Wisbich, and Catherine his wife, late wife of William Hunt, of East-Basham, enfeoffed John Wode, of Honingham, and Margery his wife, &c. in four messuages, four tofts, &c. called Berningham's, in this town, and Snoring... and, at the said time, a Thomas Gurney, esq. their attorney, to deliver seisin to John Wode and Margery, and to Robert, son of the said John and Margery." Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_5`. Source ID: `armstrong-norfolk-1781`.
```

**new_string:**
```
[^v71-armstrong-1447-berninghams]: Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 5 (Norwich, 1781), Gallow Hundred entry for East Barsham — Berningham's / Knold's / Waldgrave's Manor: "In the 25th of Henry VI. March 9, John Hines, of Swaffham in Norfolk, sells to John Wode the manor of Berningham for fifty marks; and on the 10th of the said month, Robert Mompynson, of Wisbich, and Catherine his wife, late wife of William Hunt, of East-Basham, enfeoffed John Wode, of Honingham, and Margery his wife, &c. in four messuages, four tofts, &c. called Berningham's, in this town, and Snoring... and, at the said time, a Thomas Gurney, esq. their attorney, to deliver seisin to John Wode and Margery, and to Robert, son of the said John and Margery." Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_5`. Source ID: `armstrong-norfolk-1781`.

---

## Nicholas Bokkyng, the #200 feoffee — a man of Fastolf's service

The querent on the 1444/45 fine that settled the Gurnay West-Norfolk manors (Rye Part II #200), **Nicholas Bokkyng**, was not merely a feoffee who happened to recur in the surrounding Fastolf-circle fines. The *Dictionary of National Biography* records that "a Nicholas Bocking was also in Sir John Fastolf's service," the family being seated at Ash Bocking, Suffolk, and holding property at **Longham, Norfolk** — a parish in the same West-Norfolk orbit as the Lexham / Castleacre / Newton / Great Dunham lands of the fine.[^dnb-bokking-2026] Reading the #200 feoffee as a member of Fastolf's own service circle tightens Thomas Gournay II's placement within the Fastolf–Paston affinity: the enfeoffment-to-use of the Gurney manors was drawn up through Fastolf's man, of a piece with the 1452 St George's Day petition on the Paston side and with the Heylesdon–Fastolf and Harling-retinue threads documented above. Bokkyng recurs across the 22nd–24th Henry VI Norfolk fines beside Yelverton, Paston and Sir Henry Inglose, and is styled "Armiger" at Rye Part II #185.[^dnb-bokking-2026]

[^dnb-bokking-2026]: "Bocking, Edward (d.1534)," *Dictionary of National Biography*, vol. 5 (London: Smith, Elder & Co., 1886), appended family note: "A Nicholas Bocking was also in Sir John Fastolf's service," the Bockings of Ash Bocking, Suffolk, holding property at Longham, Norfolk, in the 15th–16th centuries. The Bokkyng/Aleyn feoffee context of the surrounding 23 Henry VI Norfolk fines (Yelverton, Paston, Sir Henry Inglose at Rye Part II ##185, 196 ff.) is preserved in [`sources/corpus/rye-feet-of-fines-norfolk-part2.txt`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus/rye-feet-of-fines-norfolk-part2.txt). Source ID: `dnb-bocking`.
```

---

## Item 4 — `research/people/g13-john-gurney-fact-sheet.research.md`: published emigration lists carry no John Gurney (Hotten)

**Outcome: promote.** One `str_replace` inserting a paragraph after the Diligent-of-Ipswich paragraph in the "Great Migration corridor" section. (v113 does not edit this section.)

**old_string:**
```
The Edward Gilman cohort emigration on the Diligent of Ipswich (departed 26 April 1638 Gravesend, arrived Boston 10 August 1638, primarily Norfolk Hingham passengers bound for Hingham, Massachusetts — fewer than 10 miles from Braintree/Weymouth) is the corridor event nearest in time and place to John Gurney's 1641 Weymouth appearance. Ann Gurney's husband John Gilman was apprenticed in 1609 in Deopham, Norfolk as a worsted weaver to John Bubbyn; Ann Gurney + John Gilman themselves did not emigrate (Ann buried Hingham, Norfolk, 23 November 1651), but at least two of their sons emigrated to Exeter, New Hampshire (John Gilman Jr born 1638, emigrated by 1658; Charles Gilman born 1642, emigrated 1664 "with his brother John and cousins"). The Diligent passenger list itself contains no Gurney passenger (Banks/Cushing transcription), so John Gurney travelled on a different vessel within the same multi-year corridor.[^gilman-diligent-2026]
```

**new_string:**
```
The Edward Gilman cohort emigration on the Diligent of Ipswich (departed 26 April 1638 Gravesend, arrived Boston 10 August 1638, primarily Norfolk Hingham passengers bound for Hingham, Massachusetts — fewer than 10 miles from Braintree/Weymouth) is the corridor event nearest in time and place to John Gurney's 1641 Weymouth appearance. Ann Gurney's husband John Gilman was apprenticed in 1609 in Deopham, Norfolk as a worsted weaver to John Bubbyn; Ann Gurney + John Gilman themselves did not emigrate (Ann buried Hingham, Norfolk, 23 November 1651), but at least two of their sons emigrated to Exeter, New Hampshire (John Gilman Jr born 1638, emigrated by 1658; Charles Gilman born 1642, emigrated 1664 "with his brother John and cousins"). The Diligent passenger list itself contains no Gurney passenger (Banks/Cushing transcription), so John Gurney travelled on a different vessel within the same multi-year corridor.[^gilman-diligent-2026]

The published London port-emigration registers add a clean negative on the passage itself. John Camden Hotten's *Original Lists* — the surviving 1630s examination lists from which Banks worked — carry **no John Gurney in any spelling**, on a full-text search across the Gurney variant set and OCR-mangle forms with coverage confirmed; this complements Banks's "[no ship]." The single Gurney-adjacent entry, a "Richard Gum[m]y" aged 21 aboard the *America* (William Barker, master) bound for **Virginia**, examined at Gravesend 23 June 1635, resolves to the surname **Gummy** (so read in Hotten's text and index and in the standard transcriptions) and to Virginia, not New England — a lookalike, not a colonial Gurney; a William Gourney in the same volume is the Mayor of Dartmouth (1634), a port official. The independent arbiters of the "Gummy" reading are Coldham and the original register (TNA E157/20).[^hotten-emigration-2026]

[^hotten-emigration-2026]: John Camden Hotten, ed., *The Original Lists of Persons of Quality ... 1600-1700* (London: Chatto and Windus, 1874), full OCR text ([Internet Archive `originallistsofp00hottuoft`](https://archive.org/details/originallistsofp00hottuoft)); searched June 2026 across the Modern Gurney variant registry and OCR-mangle patterns plus the printed index (coverage confirmed: tailor/Weymouth/Braintree present). The "Richard Gum[m]y" entry is at p.95, ship *America* to Virginia, examined 23 June 1635; the surname is read "Gummy" in Hotten's text and index and in the Olive Tree Genealogy transcription. Relied-on extracts at [`sources/corpus_supplement/hotten-original-lists-gurney-search-2026.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/hotten-original-lists-gurney-search-2026.md). Source ID: `hotten-original-lists-1874`.
```

---

## Item 5 — `research/people/g13-john-gurney-fact-sheet.research.md`: Y-DNA paternal line

**Outcome: promote.** One `str_replace` inserting a new subsection after the candidate-table assessment paragraph and before the Newgate subsection. (v113 does not edit this section.)

**old_string:**
```
The compiler discussion remains useful as provenance, but later primary-index work now controls the probabilities.
```

**new_string:**
```
The compiler discussion remains useful as provenance, but later primary-index work now controls the probabilities.

### Y-DNA — the Braintree paternal line (R1b-DF19)

A direct-paternal-line (Y-DNA) comparison is the one evidence class that could test deep Gurney paternity independently of record survival. The FamilyTreeDNA Gurney surname project includes a Big Y-700 tester (kit 576097) whose earliest known ancestor is given as "John Gurney b.1603 d.1663" — the Braintree emigrant's own dates — placing the Braintree line at terminal SNP **R-FTD83678**, within **R1b-M269 > P312 > DF19 > R-Z27053**. On the public Discover data, R-FTD83678 is a very recent terminal twig (only ~2 tested descendants — essentially the family's own branch), and its parent **R-Z27053** is small and **continental-leaning**: its handful of testers self-report UK, Belgium and Canada origins and affiliate with the Viking-Germanic, Benelux, Flanders-Flemish and Belgium-Walloon projects. That is a continental NW-European signal rather than a distinctively English one — compatible with, but far too sparse and too deep (pre-surname) to prove, a Norman/continental deep origin of the kind the de Gournay tradition would predict. The discriminating comparison — whether a *documented English* Gurney shares the DF19/R-Z27053 branch — turns on the project's other R-M269 Gurney tester (kit 365744).[^ydna-2026]

[^ydna-2026]: FamilyTreeDNA Gurney surname Y-DNA project (administrator Caroline Gurney) and public Discover haplotree reports for R-FTD83678 and its upstream SNPs, consulted June 2026 (no login). Kit 576097 = Big Y-700, terminal R-FTD83678; parent R-Z27053 country-frequency and suggested-projects read from the public table view. Data captured at [`sources/corpus_supplement/ftdna-gurney-ydna-braintree-line-2026.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/ftdna-gurney-ydna-braintree-line-2026.md). Source ID: `ftdna-gurney-ydna`. See lead L-145.
```

---

## Item 6 — `research/people/francis-gurney-of-maldon.md`: the Maldon courts after 1677 — a John Gournay reclaiming Francis's property

**Outcome: promote.** One `str_replace` extending the Maldon-court-books paragraph with the 2026 "Gournay"-spelling full-text findings.

**old_string:**
```
The Maldon borough court books themselves are now full-text searchable and carry Francis throughout his Maldon years: entries naming Francis Gurney appear in the court records of 1662, 1669, 1672, and 1675–77 (his litigation and offices), and — most usefully for the children list — a record of 1689/1697 concerns "the children of the said Francis Gurney," a post-death administration or guardianship matter a decade after his 1677 drowning. Image pulls are lead L-97 in the project lead register.[^maldon-court-books-fts]
```

**new_string:**
```
The Maldon borough court books themselves are now full-text searchable and carry Francis throughout his Maldon years: entries naming Francis Gurney appear in the court records of 1662, 1669, 1672, and 1675–77 (his litigation and offices), and — most usefully for the children list — a record of 1689/1697 concerns "the children of the said Francis Gurney," a post-death administration or guardianship matter a decade after his 1677 drowning. Image pulls are lead L-97 in the project lead register.[^maldon-court-books-fts] A 2026 full-text pass on the rarer **"Gournay"** spelling sharpens the picture: the borough records confirm **"Francis Gournay gent" as one of the Bailiffs in 1675** (named again in 1678), and — after his 1677 death — show a **John Gournay buying from the Maldon Corporation a lot "heretofore of Francis Gournay" and dealing with goods at Goldhanger**, the salt-works parish of the 1677 estate schedule. A John Gournay acquiring or reclaiming Francis's former property is most economically his **son and heir John (born 1655)** rather than the bachelor uncle who died in 1681; the borough series is the right instrument for the family's civic life but does not hold the 1681 ecclesiastical administration (a Commissary of London, Essex & Herts matter). The relevant court leaves are staged for image reading as paleography Packet 36.[^maldon-gournay-fts-2026]

[^maldon-gournay-fts-2026]: Maldon, Essex borough court records, FamilySearch Full-Text Search (machine-transcribed manuscript images), "Gournay" spelling, June 2026: "Francis Gournay gent" as Bailiff 1675 (named again 1678); a post-1677 John Gournay buying a Corporation lot "heretofore of Francis Gournay" and possessed of / disposing goods at Goldhanger. Machine-transcript level (court-hand OCR) — names and relationships require image reads, staged as paleography Packet 36 (arks 3:1:9Q97-YSLK-24M; 3:1:9Q97-YSL8-SXF; 3:1:9Q97-YSLK-2CC; 3:1:9Q97-YSL8-SXM; 3:1:9Q97-YSL8-SDZ). The 1681 bachelor-John administration is not in the borough series (Commissary of London, Essex & Herts). Source ID: `familysearch-fulltext-search`. Leads L-97, L-14.
```

---

## Item 7 — `research/people/francis-gurney-of-maldon.md`: Burke corroboration of "The Problem"

**Outcome: promote.** One `str_replace` inserting a paragraph after the closing line of "The Problem" section.

**old_string:**
```
Bernau emphasizes that the Maldon bachelor John who died in 1681 was the wrong John — that was an uncle of the 1655 John, not the 1655 John himself. The identification of the 1655 John with the Norwich cordwainer remains an open problem. Family tradition supports it; "certainly their ages tally"; no contemporary primary document ties them together.[^the-problem-summary]
```

**new_string:**
```
Bernau emphasizes that the Maldon bachelor John who died in 1681 was the wrong John — that was an uncle of the 1655 John, not the 1655 John himself. The identification of the 1655 John with the Norwich cordwainer remains an open problem. Family tradition supports it; "certainly their ages tally"; no contemporary primary document ties them together.[^the-problem-summary]

A tertiary pedigree now corroborates the identification without proving it. Burke's *Landed Gentry* "Gurney of Maldon" pedigree (read 2026 via full-text search) gives Francis of Maldon (b.1628, son of Francis Gurney and Anne Browning, "a merchant ... and one of the bailiffs" of Maldon) and names his eldest son **"John Gourney ... b. 1655, who joined the Society of Friends [and] established himself as a merchant"** — i.e. Burke asserts that the 1655 Maldon John became the Quaker merchant, the very identification Bernau left open. Burke is a collector rather than an authority, and the same pedigree conflates the Maldon line into the famous Norwich-Quaker / Keswick (Barclay–Hoare–Buxton–Fry) descent, so it is a discovery-trail pointer to be tested against the Quaker registers — the 1687 Woodbridge marriage to Elizabeth Swanton and the 1721 death — not a settled fact. Independently, a full-text search of the period records returns no Gournay/Gurney co-occurring with "New England" before the nineteenth century, consistent with the 1655 John having gone to Norwich rather than the colonies.[^burke-maldon-problem]

[^burke-maldon-problem]: Burke's *Landed Gentry*, "Gurney" / "Gurney of Maldon" pedigree, consulted via FamilySearch Full-Text Search, June 2026 (the 1856 entry and a later edition): Francis Gurney of Maldon (b.1628, son of Francis Gurney and Anne Browning, merchant and a bailiff of Maldon) and son "John Gourney ... b. 1655, who joined the Society of Friends." Tertiary compiled pedigree; the Maldon-into-Norwich-Quaker descent is Burke's conflation, untraced to primary record here. The no-Gournay-with-New-England result is from the same FTS pass. Extract at [`sources/corpus_supplement/burke-landed-gentry-gurney-of-maldon.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/burke-landed-gentry-gurney-of-maldon.md). Source IDs: `burke-landed-gentry-gurney`; `familysearch-fulltext-search`. See lead L-171.
```

---

## Item 8 — regenerate the generated ID indexes

**Outcome: promote.** After Item 1 adds four sourceIds, regenerate the locator indexes (do not hand-edit them):

```
.\.venv\Scripts\python.exe tools\generate_id_indexes.py --write
```

This refreshes `data/indexes/source-ids.csv` and `data/indexes/all-ids.csv` with `dnb-bocking`, `hotten-original-lists-1874`, `ftdna-gurney-ydna`, and `burke-landed-gentry-gurney`.

---

## Source tracking

- **New sourceIds (4):** `dnb-bocking`, `hotten-original-lists-1874`, `ftdna-gurney-ydna`, `burke-landed-gentry-gurney` — added in Item 1. The `notes` fields are short source-descriptions only; the findings live in the research companions (Items 3–7).
- **Relied-on source material is referenceable.** Three corpus supplements were created **directly** (per the corpus-direct rule) and already exist in the repo; Item 1 only adds the `corpusPath` pointers to them — Phase 2 must **not** recreate them:
  - `sources/corpus_supplement/hotten-original-lists-gurney-search-2026.md` (the 1635 America/Virginia list + 1634 Dartmouth oath list);
  - `sources/corpus_supplement/ftdna-gurney-ydna-braintree-line-2026.md` (project + Discover data);
  - `sources/corpus_supplement/burke-landed-gentry-gurney-of-maldon.md` (the Maldon pedigree extract).
  The DNB-Bocking material is a single sentence, carried as a quotation in the G20 companion footnote (Item 3) — no corpus file (`corpusStatus: none`).
- **Validations:** new worksheets for `dnb-bocking`, `hotten-original-lists-1874`, `ftdna-gurney-ydna` (Item 2). `burke-landed-gentry-gurney` skips a worksheet — a single tertiary discovery-trail citation (consistent with the existing `burke-ancient-family` source, which carries none).
- **Existing source reused:** `familysearch-fulltext-search` (catch-all) for the Maldon court-book Gournay entries (Item 6) and the no-New-England result (Item 7).
- **Traceability:** Bokkyng/Fastolf → G20 companion (Item 3); emigration negative + Y-DNA → G13 companion (Items 4–5); Maldon heir + Burke "Problem" → Maldon companion (Items 6–7). Leads L-14, L-97, L-145, L-170, L-171 (open/partial) and the closed L-168 carry the discovery trail in the lead CSV. Underlying machine-transcript reads (Maldon courts) are staged as Packet 36.
