**Done:** 2026-06-20 20:29 PT

# Patchset v107 — Emigrant John & G14 family (Rivett/burial negatives, Hempnall expansion, Marsham, St Benet Fink citation, Browning, Francis G14 at Maldon, Spelman pedigree provenance, Tyng, ROLLCO Weston Turville)

Second half of the 2026-06-18→20 discovery arc (companion to v106). Net-new raw extracts already written directly to `sources/corpus_supplement/`: `rye-norwich-free-library-calendar-gurnay-extracts.md`, `rollco-other-companies-gurney-1573-1653.md`, `maldon-borough-court-gournay-fts-1630-1706.md`. Lead-CSV updates (L-5, L-8, L-85, L-87, L-93, L-97, L-128, L-131, L-135, L-136, L-139, L-144, L-149, L-152, L-155, L-6, L-127) were applied via `tools/research_leads.py` during the arc; L-154 and L-155 were added.

---

## Item 1 — promote: Rivett-of-Garveston probate fully exhausted (no PCC/national-court will); 1611 marriage is a register marriage, not a licence

**Destination:** `research/people/rivett-family-of-garveston.md` (leads L-128, L-131).

**Finding.** The probate routes to proving Margaret Rivet = Francis Gurney's wife are now comprehensively closed: a TNA Discovery (PROB 11 / national) search for Rivet/Rivett/Revett of Garveston, Dereham, or Norfolk, 1580–1640, returns **nil** — so no Prerogative Court of Canterbury will exists either, beyond the already-recorded Norfolk-index negative. And the 1611 Gurney × Rybett marriage is indexed (FindMyPast Norfolk Banns and Marriages) as event type **"Marriage" — a parish-register marriage, not a licence** — so there is no marriage allegation/bond that would have named Margaret's father. For Margaret's burial (L-131), the FMP Norfolk Burials set (Gurn*, 1608–1628) returns no East Dereham or West Barsham burial and, on a place-column read, **omits East Dereham and West Barsham entirely** — confirming that set's parish-selectivity, so the indexed route cannot resolve her burial; the East Dereham register image (NRO PD 86/41) remains the only route.

**Action 1a — str_replace (extend the exhaustion statement with the PCC/national negative):**

old_string:
```
rests on chronology, geography, and the absence of any competing Margaret — strong
circumstantial alignment, but no document yet names Margaret as Francis Gurney's wife or ties
Francis Rivet's household to the older Rivett testators.
```

new_string:
```
rests on chronology, geography, and the absence of any competing Margaret — strong
circumstantial alignment, but no document yet names Margaret as Francis Gurney's wife or ties
Francis Rivet's household to the older Rivett testators. The probate routes are now closed at
national level too: a Prerogative Court of Canterbury / TNA Discovery search for any Rivet,
Rivett, or Revett of Garveston, Dereham, or Norfolk in 1580–1640 returns nothing, so no PCC will
supplements the Norfolk-index negative.[^pcc-rivett-negative] And the 1611 Gurney × Rybett
marriage is indexed as a parish-register *marriage*, not a licence, so no marriage allegation
survives that could have named Margaret's father.[^fmpm]
```

**Action 1b — str_replace (add the PCC-negative footnote to the file's footnote block):**

new footnote text (place adjacent to `[^probate-francis]`):
```
[^pcc-rivett-negative]: The National Archives, Discovery online catalogue (https://discovery.nationalarchives.gov.uk), search of surnames Rivet/Rivett/Revett with Garveston, Dereham, and Norfolk, record series PROB 11 and unrestricted, 1580–1640: no results (2026-06-20). Confirms that no Prerogative Court of Canterbury will or national-court probate exists for Francis Rivet or the Garveston Rivetts in the window, complementing the Norfolk diocesan-index negative recorded at `[^probate-francis]`. Source ID: `tna-pcc-probate` (the PCC record series searched; Discovery is the access route).
```

**Action 1c — str_replace (sharpen the L-131 burial open-question with the FMP coverage finding).** In the open-questions list, the L-131 bullet currently ends noting East Dereham as the remaining test; append:

old_string (note: the continuation lines carry the bullet's 2-space indent — preserve it verbatim):
```
  John's removal to maternal kin. (Garveston now read; East Dereham the remaining test —
  available online.)
```

new_string:
```
  John's removal to maternal kin. The indexed route is now closed: the FindMyPast Norfolk Burials
  set (Gurn*, 1608–1628) shows no Gurney/Rivet burial at East Dereham or West Barsham and, on a
  place-column read, omits both parishes — so it cannot resolve her burial, and only the East
  Dereham register image can.[^fmp-burials-coverage] (Garveston read; East Dereham the remaining
  image test.)
```

new footnote text (place in the footnote block):
```
[^fmp-burials-coverage]: FindMyPast "Norfolk Burials," surname `Gurn*`, year-of-death 1608–1628 (2026-06-20): 20 results, none at East Dereham or West Barsham; the place column across the result set carries neither parish, confirming the set's parish-selectivity (the same selectivity that omits East Dereham from the FMP "Norfolk Baptisms" set). A blank here is therefore not a true negative for Margaret's burial. Source ID: `findmypast-norfolk-burials-index`.
```

---

## Item 2 — promote: Hempnall John-Gurnie household expanded; the Syon forename rooted by 1576

**Destination:** `research/people/john-gurney-earsham-will-1638.md` (lead L-152).

**Finding.** A FindMyPast "Norfolk Baptisms" sweep on the Hempnall index spelling *Gurnie* resolves the south-Norfolk John-Gurnie household well beyond the two prior entries: **John Gurnie of Hempnall had children Henricus (1576, mother Margaret), Elizabeth (1585), John (1587), Susana (1590), Syon (1593), and Margaret (1596)** — a coherent 1576–1596 set that roots the rare Syon forename in the household by 1576/1593. A separate **Robert Gurnie** household at Hempnall (Jana 1570, mother Anna; James 1578) and a **John Gurnie at Redenhall** (Marie 1598) sit alongside it; Redenhall edges toward the Waveney/Earsham area.

**Action 2a — str_replace (expand the Hempnall sentence in the parish-register-traces section):**

old_string:
```
The earliest instance of the forename is **Syon Gurnie, christened 1593 at Hempnall** (south Norfolk, ~10 miles from Earsham), son of a **John** Gurney — rooting the rare name in a south-Norfolk John-Gurney household by 1593; the same Hempnall family recurs with father-John children (Anna 1640, Elizabeth 1641).[^hempnall-syon-1593]
```

new_string:
```
The earliest instance of the forename is **Syon Gurnie, christened 1593 at Hempnall** (south Norfolk, ~10 miles from Earsham), son of a **John** Gurney. On the Hempnall index spelling *Gurnie*, that household resolves more fully: **John Gurnie of Hempnall had children Henricus (1576, mother Margaret), Elizabeth (1585), John (1587), Susana (1590), Syon (1593), and Margaret (1596)** — a coherent 1576–1596 set that roots the rare Syon name in the household by 1576/1593, a generation before the Earsham testator. A separate **Robert Gurnie** household at Hempnall (Jana 1570, mother Anna; James 1578) and a **John Gurnie at Redenhall** (Marie 1598, edging toward the Waveney) sit alongside it; the same Hempnall John-Gurney line recurs with later father-John children (Anna 1640, Elizabeth 1641).[^hempnall-syon-1593][^hempnall-gurnie-household-1576-1596]
```

**Action 2b — str_replace (add the supporting footnote):**

new footnote text (place adjacent to `[^hempnall-syon-1593]`):
```
[^hempnall-gurnie-household-1576-1596]: FindMyPast "Norfolk Baptisms," surname `Gurnie`, year-of-birth 1610 ±40 (2026-06-20): Hempnall ("Hempnall and the Hempnall Group of Parishes") children of John Gurnie — Henricus (1576, mother Margr[aret]), Elisa[beth] (1585), Johs/John (1587), Susana (1590), Syon (1593), Margaret (1596); plus a Robert Gurnie household (Jana 1570, mother Anna; Jacobus/James 1578) and Marie Gurnie (1598) at Redenhall, father John. Index level. Note also (capture mechanics): the FMP baptisms results URL does not bind a `fathersfirstname` or `mothersfirstname` filter — isolate a household by the exact index spelling of the surname. Source ID: `findmypast-norfolk-baptisms-index`.
```

---

## Item 3 — promote: the April-1659 Costessey court of "Anthony Dobbs of Marsham" is not Marsham manor

**Destination:** `research/people/gurney-family-costessey-manorial.md` (lead L-93).

**Finding.** Blomefield's account of Marsham (vol. 6) traces the manor through the seventeenth century as Boleyn → Sir Henry Hobart → the Freemans → the Pastons — with **no Dobbs as lord of Marsham manor**. So Anthony Dobbs of Marsham, esquire, who held the bundled April-1659 court, was a Marsham *resident* holding a manor **elsewhere**; the 1659 court does not belong to Marsham manor, and the manor-name question still turns on the image read of the 1659 court opening.

**Action 3a — str_replace (extend open-question 3):**

old_string:
```
so the manor name needs an **image read** of the 1659 court opening, not full-text. If not Costessey (Jernegan lords), the 1659 John Gurney senior may belong to a neighbouring manor bundled on the film.
```

new_string:
```
so the manor name needs an **image read** of the 1659 court opening, not full-text. If not Costessey (Jernegan lords), the 1659 John Gurney senior may belong to a neighbouring manor bundled on the film. Blomefield's Marsham descends Boleyn → Sir Henry Hobart → the Freemans → the Pastons, with no Dobbs as lord — so Anthony Dobbs of Marsham was a Marsham *resident* holding a manor elsewhere, and the 1659 court is not Marsham manor itself.[^marsham-dobbs-blomefield]
```

new footnote text:
```
[^marsham-dobbs-blomefield]: Francis Blomefield, "Hundred of South Erpingham: Marsham," *An Essay Towards a Topographical History of the County of Norfolk*, vol. 6, pp. 286–289, British History Online — the manor of Marsham passes Boleyn → Sir Henry Hobart → the Freemans → the Pastons through the seventeenth century; the Dobbs family is not named as lord of Marsham. Source ID: `blomefield-norfolk`.
```

---

## Item 4 — promote: G14 companion — St Benet Fink citation, Browning-probate negative, Francis G14 at the Maldon courts, and the Spelman pedigree's provenance

**Destination:** `research/people/g14-francis-gurney-fact-sheet.research.md` (leads L-149, L-135, L-8, L-97, L-5; with L-85/L-87 provenance context).

### 4a — Spelman pedigree provenance traced (L-5)

**Finding.** The Spelman-pedigree "open item" is resolved. Daniel Gurney's *Record*, Appendix LV (p. 317) states the pedigree "was transcribed by Sir Henry Spelman, from one given him by Francis Gurnay in 1639… it is amongst the Spelman manuscripts collected by Dr. Macro, and which are now in the possession of Hudson Gurney, Esq." The chain, each link sourced: Francis G14 → Spelman (1639, from now-lost family deeds) → the Spelman MSS in **Cox Macro**'s collection → the **1820 Christie sale** (Dawson Turner bought 41 lots, Hudson Gurney the rest, £700) → **Hudson Gurney of Keswick Hall** (where DG saw it, 1848) → catalogued in the **HMC 12th Report, Appendix IX (1891), p. 161** (J. H. Gurney of Keswick). It was **not** in the 1936 Sotheby's sale of the Bawdeswell-branch Gurney library (that sent Spelman *miscellanea* — chartularies, Cavendish, Dugdale, heraldry — to the Bodleian, but no family pedigree), so the pedigree most plausibly remains in the Keswick-line family archive (check the Norfolk Record Office Gurney-of-Keswick deposit). This unifies L-5 with L-85 (the Keswick MSS) and touches L-87 (Dawson Turner's share of the same 1820 dispersal).

**Action 4a — str_replace:**

old_string:
```
Open item: locate a manuscript Gurney/Gournay pedigree among the Spelman papers. Candidate repositories: CUL MS Add. (Spelman), Bodleian MS Eng. hist., BL Add. MSS (Spelman transcripts), College of Arms.
```

new_string:
```
The pedigree's provenance is now traced. Daniel Gurney's *Record*, Appendix LV (p. 317), records that it "was transcribed by Sir Henry Spelman, from one given him by Francis Gurnay in 1639… it is amongst the Spelman manuscripts collected by Dr. Macro, and which are now in the possession of Hudson Gurney, Esq."[^spelman-pedigree-provenance] The chain runs: Francis G14 → Spelman (1639, from family deeds now lost) → the Spelman MSS owned by **Cox Macro** (1683–1767) → the **1820 Christie sale**, at which Dawson Turner bought 41 lots and **Hudson Gurney** the rest (£700) → Hudson Gurney of **Keswick Hall** (where DG saw it in 1848) → catalogued in the **HMC 12th Report, Appendix IX (1891), p. 161** (J. H. Gurney of Keswick). It was **not** in the 1936 Sotheby's sale of the Bawdeswell-branch Gurney library (that dispersed Spelman *miscellanea* to the Bodleian but no family pedigree), so the pedigree most plausibly remains in the Keswick-line family archive — the Norfolk Record Office Gurney-of-Keswick deposit being the first place to check. This unifies the lead with the Keswick-MSS lead (L-85) and with Dawson Turner's share of the same 1820 dispersal (L-87). The pedigree's text and medieval content are already transcribed in DG Appendix LV (corpus: `sources/corpus/daniel-gurney-part-2.md`), so locating the original is a verification-and-detail step, not a recovery of unknown content.
```

new footnote text:
```
[^spelman-pedigree-provenance]: Daniel Gurney, *Record of the House of Gournay* (1848), Appendix LV, p. 317 ("The Pedigree of Gurney, from Spelman MSS."): transcribed by Sir Henry Spelman from one given him by Francis Gurnay in 1639, "amongst the Spelman manuscripts collected by Dr. Macro [Cox Macro, 1683–1767], and which are now in the possession of Hudson Gurney, Esq." (corpus: `sources/corpus/daniel-gurney-part-2.md`, p. 317). Dispersal of the Macro/Spelman MSS: the 1820 Christie of Pall Mall sale (Dawson Turner 41 lots; Hudson Gurney the rest, £700) — Wikipedia, "Cox Macro" (https://en.wikipedia.org/wiki/Cox_Macro) and "Hudson Gurney" (https://en.wikipedia.org/wiki/Hudson_Gurney). Keswick holding catalogued in HMC, *12th Report, Appendix IX* (1891), p. 161 (MSS of J. H. Gurney of Keswick). The 1936 Sotheby's "Gurney of Bawdeswell Hall" sale (catalogue digitised at the Internet Archive, https://archive.org/details/b31661531) contained Spelman miscellanea later acquired by the Bodleian (Eng. hist. MSS, per CELM) but no Gurney family pedigree. Source ID: `dg-rec-pt2` (the primary, carrying the pedigree's substantive content). The dispersal/holding references (Cox Macro / Hudson Gurney / the HMC 12th Report / the 1936 Sotheby's catalogue) are cited inline by title and URL as contextual provenance per the citations rule's contextual-colour band — none has been examined at first hand, so no separate sourceIds are minted; if the original is located at the NRO the holding reference is then promoted to a real sourceId.
```

### 4b — Francis G14's later life: the Maldon courts and the unlocated death (L-8, L-97); Browning-probate negative (L-135)

**Action 4b — str_replace (insert a new subsection before the St Benet Fink children section):**

old_string:
```
### Children at St Benet Fink — Bernau's list vs. current fact sheet
```

new_string:
```
### Francis G14's later life — the Maldon courts, the Essex probate gap, and the Browning wills

Three strands bear on where Francis G14 went after his St Benet Fink children's baptisms end in 1637 and where his death record should be sought. (1) **Maldon borough court "Gournay" entries.** A FamilySearch Full-Text sweep finds 26 pre-1700 "Gournay" entries in the Maldon (Essex) borough court records; an image read of the two earliest (paleography packet 31) places **Francis Gournay, gentleman, as a sworn juror at the Maldon court of 1 December 1630** — an adult gentleman at Maldon a decade before the London baptisms end, **chronologically consistent with Francis G14** (and not his son Francis, then about two). The court the machine transcript dated "1636" proved on the image to be a **1676** court naming the *younger* Francis Gournay, gentleman, as a borough **bailiff** (alongside Sir William Wiseman) — so it belongs to the son (b. 1628, d. 1677), as does the later 1669–1676 cluster. The 1630 sighting is the G14-relevant one, though the entry records only office, not parentage; masters at `sources/media/maldon-borough-court-gournay-fts/_local/`.[^maldon-court-gournay] (2) **The probate jurisdiction.** PCC is negative for a Francis Gurney/Gournay will in the window, and Bernau's thorough PRO-based study reports no will or death for Francis G14 (only the son's 1677 suicide caveats). The family's documented Maldon settlement points the search at the **Commissary Court of London (Essex & Herts division) / Archdeaconry of Essex** (Essex Record Office "Seax"; Ancestry), not the Norwich Archdeaconry.[^francis-g14-essex-probate] (3) **The Browning wills (L-135).** Bernau already worked the Browning-probate route: Henry Jermyn's 1680 will names "Dr. Thomas Browning and Anne his wife," but **Dr. Thomas Browning's own 1694 will makes no mention of the Gurneys** — so the hoped-for Anne-Gurney × Thomas-Browning sister-pair remains an unproven speculation and the Browning probate yields no Gurney kin.[^browning-wills-no-gurney]

### Children at St Benet Fink — Bernau's list vs. current fact sheet
```

new footnote texts (place in the footnote block):
```
[^maldon-court-gournay]: Maldon, Essex borough court records, FamilySearch Full-Text Search (`+Gournay +Maldon`, 2026-06-20; https://www.familysearch.org/search/full-text): 92 Maldon entries, 26 before 1700. Image read (paleography packet 31, 2026-06-20): the court of 1 December 1630 (ark `3:1:9Q97-YSLK-YTV`) lists "Franciscus Gournay, gent." as a sworn juror (an adult gentleman, chronologically consistent with Francis G14); the court the machine transcript dated 1636 (ark `3:1:9Q97-YSLZ-BQG`) is in fact a 1676 court naming Francis Gournay, gent., as a borough bailiff with Sir William Wiseman — the younger Francis (d. 1677) — FamilySearch Full-Text collapses this hand's "1676" to "1636." Full account: `sources/corpus_supplement/maldon-borough-court-gournay-fts-1630-1706.md`; masters at `sources/media/maldon-borough-court-gournay-fts/_local/`. Source ID: `familysearch-fulltext-search`.
[^francis-g14-essex-probate]: The National Archives Discovery online catalogue (https://discovery.nationalarchives.gov.uk), search PROB 11 / Gourney / Maldon / Essex, 1637–1665: nil. With the family's documented Maldon, Essex settlement, the relevant probate courts are the Commissary Court of London (Essex & Herts division) and the Archdeaconry of Essex (Essex Record Office "Seax", https://www.essexarchivesonline.co.uk; Ancestry London/Essex probate), not the Norwich Archdeaconry. Bernau (*British Archivist* I.7) reports no will or death for Francis G14, only the 1677 caveats for the son. Source IDs: `tna-pcc-probate`; `british-archivist-bernau-1913`.
[^browning-wills-no-gurney]: C. A. Bernau, "Francis Gournay (or Gurney), of Maldon, Essex," *The British Archivist* I.7 (1913): the will of Henry Jermyn of Wickham Bishop (1680, Comm. London Essex & Herts, "Heydon" 481) names "Dr. Thomas Browning and Anne his wife"; Dr. Thomas Browning's own will (16 June 1694, proved 3 May 1705) "makes no mention of the Gurneys." The suggested Anne-Gurney × Thomas-Browning sibling-pair marriage is Bernau's conjecture, unproven. Corpus: `sources/corpus_supplement/The_British_Archivist-Unrecorded-Biographies-Francis-Gurney.md`. Source ID: `british-archivist-bernau-1913`.
```

### 4c — St Benet Fink children list confirmed; the Harleian citation corrected (L-149)

**Action 4c — str_replace (add the reconciliation/citation note to the St Benet Fink section intro):**

old_string:
```
His numbered list nevertheless differs substantially from the children table in [`fact-sheets/g14-francis-gurney-fact-sheet.md`](https://github.com/allengurney/gurney-genealogy/blob/main/fact-sheets/g14-francis-gurney-fact-sheet.md). The conflict is documented below; it is not reconciled here. Primary-register examination is the resolution path.
```

new_string:
```
His numbered list nevertheless differs substantially from the children table in [`fact-sheets/g14-francis-gurney-fact-sheet.md`](https://github.com/allengurney/gurney-genealogy/blob/main/fact-sheets/g14-francis-gurney-fact-sheet.md). A FamilySearch records-index check independently confirms **Bernau's** list over the fact sheet's divergent one (Dorothy 1619, Roger 1621, Frances 1625/6, Francis 1628, Lucretia 1630, Thomas 1636, Margaret 1637, all of Francis & Anne at St Benet Fink), so the reconciliation should follow Bernau. The citation must also be corrected: any reference to a Harleian Society "vol. 44, Collins/Bannerman 1914" transcript of St Benet Fink is a **misattribution** — that Harleian register volume is **St Mary le Bow / St Benet *Sherehog***, a different church; there is no Harleian printed transcript of St Benet *Fink*. Cite the St Benet Fink baptisms to Bernau (1913) and the original LMA register, P69/BEN1/A.[^st-benet-fink-citation]
```

new footnote text:
```
[^st-benet-fink-citation]: The St Benet Fink baptisms of Francis G14's children are recorded in C. A. Bernau, "Francis Gournay (or Gurney), of Maldon, Essex," *The British Archivist* I.7 (1913), and are confirmed at index level by FamilySearch records (England births & christenings). The original register is London Metropolitan Archives, P69/BEN1/A/001–002 (St Benet Fink, City of London). The Harleian Society Register Series vol. 44 (W. Bruce Bannerman, ed., 1914) is the registers of St Mary le Bow, St Pancras Soper Lane, and St Benet *Sherehog* — not St Benet Fink; there is no Harleian transcript of St Benet Fink, so that citation, where it appears, is to be removed as a misattribution. Source IDs: `british-archivist-bernau-1913`; `st-benet-fink-register`.
```

---

## Item 5 — promote: G13 companion — Tyng/Braintree leasehold dating, ROLLCO Weston Turville tailoring family, and three negatives

**Destination:** `research/people/g13-john-gurney-fact-sheet.research.md` (leads L-144, L-155, L-6, L-136, L-127).

### 5a — ROLLCO Weston Turville (Bucks) tailoring Gurney + Tyng leasehold dating

**Finding.** (i) A complete ROLLCO sweep across all eleven partner companies (the repo previously held only the Drapers and Stationers) surfaces, in the **Clothworkers' Company**, a 1622 apprenticeship of **Francis Gurney, son of Thomas Gurney, "scissor" (tailor), of Weston Turville, Buckinghamshire** — a tailor-Gurney household in Aylesbury hundred (≈4 miles from Aylesbury, the Candidate-A region), surfaced through a London livery record, a source type the repo's Bucks work (FS baptisms + PCC wills) had not reached. The same sweep adds a London **Edward Gurney, citizen and haberdasher** (1641 Clothworkers), Clothworkers/Tallow Chandlers/Mercers Gurney households (full list: `sources/corpus_supplement/rollco-other-companies-gurney-1573-1653.md`); it does **not** resolve the older-notes "Haberdashers' Company 1632 John Gurney apprentice" (the Haberdashers are not a ROLLCO partner). (ii) For the Braintree leasehold: Capt. William Tyng of Boston (d. 1653) owned the Braintree "Salter's Farm," which his estate **leased to Gregory Belcher on 6 January 1657**; John Gurney's adjacent Tyng-tenement lease most plausibly began in the same post-1653 estate-leasing window, with William Tyng's 1653 probate inventory (Suffolk Co. MA Probate Liber 1, AmericanAncestors) the decisive next pull.

**Action 5a — str_replace (expand the comparator-leads pointer to carry these findings).** In the "Live catalog leads bearing on the G13 origin question" section:

old_string:
```
- **Colonial:** L-11 (Braintree manuscript vitals — 1661 Cheny/Gurney conflict), L-20 (SPR #338 full transcription), L-147 (Wilson v. Faxon 1653 deposition file), L-94 (Isaac Gurney court records), L-142 (Mendon proprietors' manuscript), L-144 (Tyng Braintree leasehold origin).
- **Same-name / comparator:** L-138 (Clement Gurney, Gent), L-127 (1608 Norwich depositions), L-143 (Ellingham poor-charity 1630), L-109 (Earsham court records), L-148 (Robert Gvrney + Mary, Norwich 1622), L-146 (Henry Gurney in Star Chamber 1620 — probably Midlands).
```

new_string:
```
- **Colonial:** L-11 (Braintree manuscript vitals — 1661 Cheny/Gurney conflict), L-20 (SPR #338 full transcription), L-147 (Wilson v. Faxon 1653 deposition file), L-94 (Isaac Gurney court records), L-142 (Mendon proprietors' manuscript), L-144 (Tyng Braintree leasehold origin — *2026-06-20:* Capt. William Tyng of Boston, d. 1653, owned the Braintree "Salter's Farm," leased to Gregory Belcher 6 Jan 1657; John Gurney's adjacent Tyng-tenement lease most plausibly began in the same post-1653 estate-leasing window; Tyng's 1653 inventory, Suffolk Co. MA Probate Liber 1, is the decisive pull).
- **Same-name / comparator:** L-138 (Clement Gurney, Gent), L-127 (1608 Norwich depositions — *2026-06-20:* the FTS deposition transcripts are court-hand salad, ages/origins not OCR-extractable; resolution needs the staged packet-14 image reads), L-143 (Ellingham poor-charity 1630), L-109 (Earsham court records), L-148 (Robert Gvrney + Mary, Norwich 1622), L-146 (Henry Gurney in Star Chamber 1620 — probably Midlands), **L-155 (ROLLCO non-Drapers livery Gurneys — *2026-06-20:* a 1622 Clothworkers' apprenticeship of Francis Gurney, son of Thomas Gurney, tailor of Weston Turville, Bucks ≈4 mi from Aylesbury; plus Edward Gurney citizen & haberdasher 1641 and Clothworkers/Tallow Chandlers/Mercers households — `sources/corpus_supplement/rollco-other-companies-gurney-1573-1653.md`)**.
```

### 5b — Negatives (L-6, L-136); Haberdashers open question (L-155)

**Action 5b — str_replace (add the ROLLCO result to the standing Haberdashers open question):**

old_string:
```
- Can the reported **Haberdashers' Company 1632 John Gurney apprentice** be re-sourced? The claim is carried in older notes, but the Findmypast London Apprenticeship Abstracts returned zero Gurney results; the original source needs re-identification before the lead can be tested.
```

new_string:
```
- Can the reported **Haberdashers' Company 1632 John Gurney apprentice** be re-sourced? The claim is carried in older notes, but the Findmypast London Apprenticeship Abstracts returned zero Gurney results; the original source needs re-identification before the lead can be tested. (The 2026-06-20 ROLLCO all-company sweep does not resolve it — the Haberdashers are not a ROLLCO partner company — but it does record a London **Edward Gurney, citizen and haberdasher**, as father of a 1641 Clothworkers' apprentice, the nearest haberdasher-Gurney datum found.)
```

**Action 5c — str_replace (record the L-6 and L-136 negatives in the Negative Results and Exclusions section).** Phase 2: append these two bullets within the existing "Negative Results and Exclusions" section (research/people/g13-john-gurney-fact-sheet.research.md, the section beginning "## Negative Results and Exclusions"):

bullets to append:
```
- **Edmund Gurney the Divine (d. 1648) probate (L-6):** a FamilySearch Full-Text search for "Edmund/Edmond Gurney" surfaces no probate of the Norfolk divine c. 1648 (consistent with the standing NCC and PCC catalogue negatives); the only early-modern hit is a 1638 Norwich will carrying an Edmund Gurney as a witness/party, not testator. The online route is exhausted; the residual is the auth-gated PCC admon / NRO session-file check.
- **Francis G14's brothers' fostering probate (L-136):** a FamilySearch Full-Text search for "Anthony Gurney"/"Anthony Gurnay" and "Edward Gurney" in Norfolk probate, 1610–1660, returns nothing — so the redirected manorial/probate route surfaces no will of the uncles naming a fostered nephew John or Edward; with indexed parish searches already exhausted, no documentary fostering link is currently visible.
```

(The L-139 first-wife-Mary indexed-exhaustion is already recorded in this companion's "Mary Gurney's English birth" section and needs no new entry.)

---

## Structured data — `data/sources.json` operations

Reuse analysis (checked against `data/indexes/source-ids.csv`): the only **new** sourceId needed is `rollco-other-companies-gurney-1573-1653`. Everything else **reuses an existing entry** — `british-archivist-bernau-1913`, `st-benet-fink-register`, `findmypast-norfolk-burials-index`, `tna-pcc-probate`, `dg-rec-pt2`, `familysearch-fulltext-search`, `blomefield-norfolk`, `findmypast-norfolk-baptisms-index`, `findmypast-norfolk-banns-marriages-index`, `edmund-divine-pcc-probate-negative` — with three small revisions below. No `tna-discovery-catalogue`, `lma-st-benet-fink-register`, `hmc-12th-report-keswick-gurney`, or `wikipedia-*` sourceIds are minted (the provenance sources are cited inline as contextual colour per Item 4a).

### S1 — new file insert: add `rollco-other-companies-gurney-1573-1653` (alphabetically after `rollco-drapers…`)

**Action S1 — str_replace in `data/sources.json`:**

old_string:
```
      "notes": "Full ROLLCO Drapers' Gurney event corpus 1581-1654. Earliest Robert event is freedom by servitude 16 Dec 1581 (DREW4826) under master Robert Furnes, with Robert already styled 'Tailor, Old Change' at admission. Robert is recorded as Drapers' apprenticeship or freedom master in roughly 14 events between 1597 and 1622, with explicit 'tailor, Old Change' identifications in 1604, 1617, and 1622. John Gurney's 1623/4 freedom by redemption (DREW5638) names Robert Gurney as father in the same event row. The 1629 Marten Backhurst freedom-by-servitude event (DREB1311) names Robert as master without a deceased flag; given Robert's confirmed 1625 death this is a posthumous master-name record, not a second living Robert. John Gurney's 1630 apprenticeship-master event (DRLL2060) bound Henry Smith, son of late Thomas Smith yeoman of Kilton, Suffolk, for 7 years on 3 November 1630."
    },
```

new_string:
```
      "notes": "Full ROLLCO Drapers' Gurney event corpus 1581-1654. Earliest Robert event is freedom by servitude 16 Dec 1581 (DREW4826) under master Robert Furnes, with Robert already styled 'Tailor, Old Change' at admission. Robert is recorded as Drapers' apprenticeship or freedom master in roughly 14 events between 1597 and 1622, with explicit 'tailor, Old Change' identifications in 1604, 1617, and 1622. John Gurney's 1623/4 freedom by redemption (DREW5638) names Robert Gurney as father in the same event row. The 1629 Marten Backhurst freedom-by-servitude event (DREB1311) names Robert as master without a deceased flag; given Robert's confirmed 1625 death this is a posthumous master-name record, not a second living Robert. John Gurney's 1630 apprenticeship-master event (DRLL2060) bound Henry Smith, son of late Thomas Smith yeoman of Kilton, Suffolk, for 7 years on 3 November 1630."
    },
    "rollco-other-companies-gurney-1573-1653": {
      "shortTitle": "ROLLCO - Gurney events in Clothworkers, Tallow Chandlers, Mercers (1573-1653)",
      "citation": "Records of London's Livery Companies Online (ROLLCO), Gurney event records in the Clothworkers', Tallow Chandlers', and Mercers' companies; surname Gurney all-company sweep, captured 2026-06-20.",
      "archive": "ROLLCO (Records of London's Livery Companies Online)",
      "url": "https://www.londonroll.org/search",
      "corpusStatus": "full",
      "corpusPath": "sources/corpus_supplement/rollco-other-companies-gurney-1573-1653.md",
      "mediaPath": null,
      "validationPath": "sources/validations/rollco-other-companies-gurney-1573-1653.md",
      "notes": "Complements rollco-drapers-gurney-old-change-cluster and rollco-stationers-gurney-1613-1626 (the previously-held ROLLCO companies). Key finding: a 1622 Clothworkers' apprenticeship of Francis Gurney, son of Thomas Gurney, 'scissor' (tailor) of Weston Turville, Buckinghamshire (Aylesbury hundred, the Candidate-A region for the emigrant John G13). Also a London Edward Gurney, citizen and haberdasher (1641 Clothworkers); Richard Gurney (Clothworkers freeman 1635-36); a William/Ws (Clothworkers freeman 1573); a Tallow Chandlers Ralph/William/Christopher household (1650); Thomas/Francis Gurney bound to the Mercers (1653). ROLLCO event IDs not captured (the browser privacy guard strips the result-link query strings); rows identified by year/name/company/role. ROLLCO does not include the Merchant Taylors' Company (see ukda-9263-mt-apprentices-scott-2024)."
    },
```

### S2 — revise `findmypast-norfolk-burials-index` (add the now-created validation path; append the 2026-06-20 coverage finding)

**Action S2 — str_replace in `data/sources.json`:**

old_string:
```
      "validationPath": null,
      "notes": "Used in negative-result mode for Margaret Rybett's burial 1614-1620: zero Margaret Gurney/Ryvett burials surface across Norfolk surname variants, including at East Dereham specifically. Burial therefore not in indexed Norfolk burials; future targets are Suffolk burials (Ryvett family geography) and the East Dereham parish-register burial-section image walk."
    },
```

new_string:
```
      "validationPath": "sources/validations/findmypast-norfolk-burials-index.md",
      "notes": "Used in negative-result mode for Margaret Rybett's burial 1614-1620: zero Margaret Gurney/Ryvett burials surface across Norfolk surname variants. Re-confirmed 2026-06-20 with a Gurn* 1608-1628 sweep (20 results, none at East Dereham or West Barsham; the place column across the result set carries neither parish) - the set is parish-selective and omits both, so a blank is not a true negative. Future targets: Suffolk burials (Ryvett geography) and the East Dereham parish-register burial-section image walk."
    },
```

### S3 — revise `st-benet-fink-register` (add LMA shelfmark + URL + validation + the Harleian-misattribution note)

**Action S3 — str_replace in `data/sources.json`:**

old_string:
```
      "archive": "London Metropolitan Archives (presumed)",
      "url": null,
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Children of Francis G14 + Anne Browning. Transcribed DG-III-525."
    },
```

new_string:
```
      "archive": "London Metropolitan Archives, P69/BEN1/A/001-002 (St Benet Fink, City of London)",
      "url": "https://search.lma.gov.uk/",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/st-benet-fink-register.md",
      "notes": "Baptisms of Francis G14 + Anne Browning's children 1619-1637, transcribed by Bernau (British Archivist I.7, 1913; sourceId british-archivist-bernau-1913) and confirmed at FS-index level; the original register has not been examined at first hand. There is NO Harleian Society printed transcript of St Benet Fink - Harleian Register Series vol. 44 (Bannerman 1914) is St Mary le Bow / St Benet Sherehog, a different church - so any 'Harleian St Benet Fink' citation is a misattribution. Cite Bernau + this register."
    },
```

### S4 — revise `tna-pcc-probate` (append the 2026-06-20 Rivett/Francis-G14 Discovery negatives)

**Action S4 — str_replace in `data/sources.json`:**

old_string:
```
      "notes": "13 probate items examined for John Gurney emigrant elimination. 7 John Gurneys confirmed in England post-1637 (St Botolph Aldgate, Winkfield, Aylesbury, East Grinstead, Albury, East Chiltington x2). 6 contextual records (Anne Gurney Eythorne, Daniel Gurney Aylesbury, William Gurney London, Richard Gurney London, Sir Richard Gurney, Tobias/Edward Gurney). Full analysis in research/case-files/john-gurney-case-file-v4.md."
    },
```

new_string:
```
      "notes": "13 probate items examined for John Gurney emigrant elimination. 7 John Gurneys confirmed in England post-1637 (St Botolph Aldgate, Winkfield, Aylesbury, East Grinstead, Albury, East Chiltington x2). 6 contextual records (Anne Gurney Eythorne, Daniel Gurney Aylesbury, William Gurney London, Richard Gurney London, Sir Richard Gurney, Tobias/Edward Gurney). Full analysis in research/case-files/john-gurney-case-file-v4.md. 2026-06-20 (TNA Discovery online catalogue, https://discovery.nationalarchives.gov.uk): PROB 11 search for Rivet/Rivett/Revett of Garveston/Dereham/Norfolk 1580-1640 = nil (no PCC will for Francis Rivet or the Garveston Rivetts); Gourney/Maldon/Essex 1637-1665 = nil (no PCC will for Francis G14)."
    },
```

## Validation worksheets — file writes (full bodies)

### V1 — new file write: `sources/validations/rollco-other-companies-gurney-1573-1653.md`

```
# ROLLCO - Gurney events in companies beyond Drapers and Stationers - Validation

**Source:** `rollco-other-companies-gurney-1573-1653`. Thin audit trail; findings live on the subject files.

## Scope of examination
- 2026-06-20: ROLLCO (londonroll.org) all-company surname sweep `Gurney` (172 events). The Drapers' and Stationers' Gurney events are held separately (`rollco-drapers-gurney-old-change-cluster`, `rollco-stationers-gurney-1613-1626`) and are not repeated. This source covers the Gurney events in the Clothworkers', Tallow Chandlers', and Mercers' companies. Corpus extract: `sources/corpus_supplement/rollco-other-companies-gurney-1573-1653.md`.

## What was examined / limitations
- Index level (ROLLCO transcribed event records). ROLLCO numeric event IDs were not captured (the browser privacy guard strips the result-link query strings); rows are identified by year, name, company, and role.
- The underlying registers (Clothworkers'/Tallow Chandlers'/Mercers' apprenticeship and freedom books) have not been examined at first hand.
- ROLLCO does not include the Merchant Taylors' Company (covered separately by `ukda-9263-mt-apprentices-scott-2024`).

## Where findings landed
- The Weston Turville (Bucks) tailor Thomas Gurney + son Francis (1622 Clothworkers) and the wider London livery-Gurney presence: `research/people/g13-john-gurney-fact-sheet.research.md` (lead L-155).
```

### V2 — new file write: `sources/validations/findmypast-norfolk-burials-index.md`

```
# Findmypast Norfolk Burials index - Validation

**Source:** `findmypast-norfolk-burials-index`. Thin audit trail.

## Scope of examination
- Used in negative-result mode for Margaret (Rivett) Gurney's burial c. 1614-1620; re-confirmed 2026-06-20 with a `Gurn*` year-of-death 1608-1628 sweep.

## What was examined / limitations
- Index level (Norfolk FHS / NRO partnership transcription). The set is parish-selective: the 2026-06-20 sweep returned 20 `Gurn*` burials, none at East Dereham or West Barsham, and the place column across the result set carries neither parish - so the set omits both, and a blank there is not a true negative.

## Where findings landed
- `research/people/rivett-family-of-garveston.md` (leads L-128, L-131).
```

### V3 — new file write: `sources/validations/st-benet-fink-register.md`

```
# St Benet Fink register, London - Validation

**Source:** `st-benet-fink-register` (London Metropolitan Archives, P69/BEN1/A/001-002). Thin audit trail.

## Scope of examination
- The original register has NOT been examined at first hand. The baptisms of Francis G14 + Anne Browning's children (1619-1637) are known via C. A. Bernau's transcription (`british-archivist-bernau-1913`) and confirmed at FamilySearch-index level.

## What was examined / limitations
- Citation level only. NB: there is no Harleian Society printed transcript of St Benet Fink; the Harleian Register Series vol. 44 (Bannerman 1914) is St Mary le Bow / St Benet Sherehog, a different church - so any "Harleian St Benet Fink" citation is a misattribution.

## Where findings landed
- `research/people/g14-francis-gurney-fact-sheet.research.md` (lead L-149: children-list reconciliation + citation correction).
```

(No new validation for `tna-pcc-probate` — it is a pre-existing general record-series source being annotated, not a new sourceId; the Rivett/Francis negatives are recorded in its `notes` and in the rivett companion. The provenance sources in Item 4a are contextual-colour, not minted.)

## File operations

### F1 — media move: Maldon court masters

Move the two downloaded masters from staging into the gitignored media `_local`, then record them in a committed README stub:

- `move sources/intake/paleography-staging/images/packet-31-maldon-gournay-courts/maldon-court-1630-YTV.jpg` → `sources/media/maldon-borough-court-gournay-fts/_local/maldon-court-1630-juror-francis-gournay-YTV.jpg`
- `move sources/intake/paleography-staging/images/packet-31-maldon-gournay-courts/maldon-court-1636-BQG.jpg` → `sources/media/maldon-borough-court-gournay-fts/_local/maldon-court-1676-bailiff-francis-gournay-BQG.jpg` (note the corrected date: the machine "1636" is a 1676 court)

### F2 — new file write: `sources/media/maldon-borough-court-gournay-fts/README.md`

```
# Media - Maldon (Essex) borough court records, Gournay entries (FamilySearch Full-Text)

Full-resolution court-page masters behind the Maldon Gournay analysis in `research/people/g14-francis-gurney-fact-sheet.research.md` and the corpus extract `sources/corpus_supplement/maldon-borough-court-gournay-fts-1630-1706.md`. Image reading: paleography packet 31 (2026-06-20).

## `_local/` (not committed - FamilySearch terms restrict redistribution)

| File | Content | Retrieve from |
|---|---|---|
| `maldon-court-1630-juror-francis-gournay-YTV.jpg` | Court of 1 December 1630 (6 Chas I) - "Franciscus Gournay, gent." a sworn juror | [ark:/61903/3:1:9Q97-YSLK-YTV](https://www.familysearch.org/ark:/61903/3:1:9Q97-YSLK-YTV) |
| `maldon-court-1676-bailiff-francis-gournay-BQG.jpg` | Court of 1676 (machine-transcript mis-dated "1636") - Francis Gournay, gent., a borough bailiff with Sir William Wiseman (the younger Francis, d. 1677) | [ark:/61903/3:1:9Q97-YSLZ-BQG](https://www.familysearch.org/ark:/61903/3:1:9Q97-YSLZ-BQG) |

Downloaded 2026-06-20 (signed-in session). Source ID: `familysearch-fulltext-search`.
```

### F3 — staging disposition

Move the packet-31 report `sources/intake/paleography-staging/done/packet-31-maldon-gournay-courts.md` into the dated done-folder per the FTS-skill disposition convention, and update `sources/intake/paleography-staging/README.md` Packet 31 to "incorporated" (its findings now live in the corpus + g14 companion). The working-snippets under `sources/intake/paleography-staging/working-snippets/packet31-*` are derivative/regenerable and may be deleted.

## Lead-catalog state (already applied via `tools/research_leads.py`, recorded here for the audit trail)

These lead edits were made directly with the CLI during this correction pass (the catalog is maintained outside the patchset workflow), and are listed so the trail is complete:
- **Closed:** L-16 (St Ann Blackfriars 1615 baptism) — resolved by the existing `fs-jw7y-c3b-john-gurney-baptism-st-ann-blackfriars` index entry: the father is "Wm." (William), not F or P; a William Gurney's child, not the Francis/Peter line. (Staging Packet 30 is therefore moot.)
- **Demoted to `Online=N` (online routes exhausted; see the new "Exhausted-online" rule in `research/future-research/README.md`):** L-6 (Edmund the Divine probate — reuses `edmund-divine-pcc-probate-negative`), L-136 (brothers' fostering probate), L-139 (first-wife-Mary marriage).
- **Deprioritised to low (DB trusted; membrane reads marginal):** L-72 (14), L-73 (12), L-74 (12), L-154 (10).
- **Status-trimmed to index size** with narrative moved here / to the companions: L-97 (Maldon, corrected per packet 31), and the leads above.

## Citation-rule tension flag (per maintainer request)

The tightened `citations.md` adds "show every aligned source" and the "contextual colour vs. substantive claim" band. One residual judgement call: Item 4a's Spelman-dispersal provenance is cited inline by title+URL to tertiary sources (Wikipedia "Cox Macro"/"Hudson Gurney"; the 1936 Sotheby's catalogue on archive.org; the HMC 12th Report) and handled under the contextual-colour band — the *substantive* pedigree content is cited to the primary `dg-rec-pt2`. If you'd prefer a scholarly secondary for the dispersal, the standard authority is A. N. L. Munby's studies of the Phillipps/Macro sale history. Item 1's marriage-not-licence point reuses the pre-existing `[^fmpm]` register-marriage footnote.

## Citation-rule tension flag (per maintainer request)

The recently-tightened `citations.md` adds "show every aligned source" and the "contextual colour vs. substantive claim" band. Two places to watch at Phase 2: (1) Item 4a's Spelman provenance leans on Wikipedia for the 1820-sale dispersal — handled under the contextual-colour band (the *substantive* pedigree content is cited to DG/the primary; the dispersal is provenance colour), but flag if you'd prefer a non-tertiary source for the dispersal (the standard authority is A. N. L. Munby's studies of the Phillipps/Macro dispersals, and the 1936 Sotheby's catalogue itself). (2) Item 1's marriage-not-licence point reuses the existing `[^fmpm]` footnote; confirm that footnote still reads as a register-marriage citation after the edit.
