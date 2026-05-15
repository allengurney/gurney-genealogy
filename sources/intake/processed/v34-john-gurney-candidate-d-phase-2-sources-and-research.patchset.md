# Intake patchset v34 - Candidate D Phase 2 research, sources, and validations

```yaml
patchset_id: v34
created: 2026-05-14
repo_scope: gurney-genealogy
phase: phase_2_research_and_sources
input_packet: sources/intake/john-gurney-2026May/john-gurney-candidate-d-working-packet-audited-v13.md
companion_packet: sources/intake/john-gurney-2026May/john-gurney-candidate-d-working-packet-ai-ready-v15.md
depends_on:
  - v32-john-gurney-candidate-d-source-foundation.patchset.md
  - v33-john-gurney-candidate-d-register-and-comparator-sources.patchset.md
sibling_patchset: v35-john-gurney-case-file-candidate-d-section-8.patchset.md
phase_2_rule: Apply Round 1-3 deep-research findings into sources, validations, and research files. The Candidate D entry in the case file is handled separately in v35.
```

## 0. Scope

This patchset records the substantive Phase 2 output of the Candidate D research pass:

- Round 1: BHO 1638 St Augustine row capture and neighbour context; full ROLLCO Drapers' Gurney corpus 1581-1654 including event IDs.
- Round 2: 1581 freedom-by-servitude detail (Robert Furnes as master, "Tailor, Old Change" already stated); 1597 Drapers' master event; Joseph Hunscott verified as a documented Stationer 1612-1646; "second Robert" puzzle resolved (Stationer-Robert 1616-1626 = separate man); 1613 John Gurney Stationer apprenticeship to James Boler surfaced as a possible Candidate D bridge.
- Round 3: PCC Wills 1625-1670 Anne Gurney null result; Hanging Houghton John Gourney (gent) confirmed as separate Northants family; Arber Stationers' Registers deferred as image-pull target; redemption-pathway hypothesis (H-D1) raised but not confirmed.

Sibling patchset v35 handles the case-file Section 8 Candidate D subsection and the related Section 9, 11, and 12 updates. Keep this patchset's research/topic-file output authoritative for depth and detail; the case file should remain tight.

## 1. Source registry operations on `data/sources.json`

Preserve existing ordering style. Do not reformat the full file.

### 1.1 Update `bho-london-inhabitants-st-augustine-1638`

Replace the existing record body with this version. Keep the JSON object key unchanged.

```json
"bho-london-inhabitants-st-augustine-1638": {
  "shortTitle": "BHO - Inhabitants of London 1638, St Augustine",
  "citation": "Dale, T. C. \"Inhabitants of London in 1638: St. Augustine.\" In The Inhabitants of London in 1638. Society of Genealogists, 1931. British History Online.",
  "archive": "British History Online",
  "url": "https://www.british-history.ac.uk/no-series/london-inhabitants/1638/pp34-35",
  "corpusStatus": "full",
  "corpusPath": "sources/corpus_supplement/bho-london-inhabitants-st-augustine-1638.md",
  "mediaPath": null,
  "validationPath": "sources/validations/bho-london-inhabitants-st-augustine-1638.md",
  "notes": "St Augustine 1638 rents return, three manuscript pages (MS. 67, MS. 67a, MS. 68), £1,700 total assessed value yielding £233 5s tithe at 2/9 per £. John Gurney is in MS. 67a at £10, between Christopher Hunlock £2 and George Browne £10. Joseph Huntscott (= Joseph Henscott, will overseer of Robert Gurney 1625, and the well-documented Stationer) appears on MS. p. 68 at £12, anchoring parish-network continuity from Robert's death (1625) into 1638. Candidate D context now stronger than a generic same-name London lead."
}
```

### 1.2 Update `rollco-drapers-gurney-old-change-cluster`

Replace the existing record body. Keep the JSON object key unchanged.

```json
"rollco-drapers-gurney-old-change-cluster": {
  "shortTitle": "ROLLCO Drapers - Robert and John Gurney Old Change cluster",
  "citation": "Records of London's Livery Companies Online (ROLLCO), Drapers' Company event records for Robert Gourney/Gurney (1581-1629) and John Gurney (1623/4-1630), captured by surname Gurney and surname Gourney variant sweeps 1580-1665.",
  "archive": "ROLLCO; underlying data from P. Boyd, Roll of the Drapers' Company of London (1934)",
  "url": "https://www.londonroll.org/",
  "corpusStatus": "full",
  "corpusPath": "sources/corpus_supplement/rollco-drapers-gurney-old-change-cluster.md",
  "mediaPath": null,
  "validationPath": "sources/validations/rollco-drapers-gurney-old-change-cluster.md",
  "notes": "Full ROLLCO Drapers' Gurney event corpus 1581-1654. Earliest Robert event is freedom by servitude 16 Dec 1581 (DREW4826) under master Robert Furnes, with Robert already styled 'Tailor, Old Change' at admission. Robert is recorded as Drapers' apprenticeship or freedom master in roughly 14 events between 1597 and 1622, with explicit 'tailor, Old Change' identifications in 1604, 1617, and 1622. John Gurney's 1623/4 freedom by redemption (DREW5638) names Robert Gurney as father in the same event row. The 1629 Marten Backhurst freedom-by-servitude event (DREB1311) names Robert as master without a deceased flag; given Robert's confirmed 1625 death this is a posthumous master-name record, not a second living Robert. John Gurney's 1630 apprenticeship-master event (DRLL2060) bound Henry Smith, son of late Thomas Smith yeoman of Kilton, Suffolk, for 7 years on 3 November 1630."
}
```

### 1.3 Add `rollco-stationers-hunscott-cluster`

```json
"rollco-stationers-hunscott-cluster": {
  "shortTitle": "ROLLCO Stationers - Joseph Hunscott cluster",
  "citation": "Records of London's Livery Companies Online (ROLLCO), Stationers' Company event records for Joseph Hunscott (1612-1646) and John Hunscott (1641), captured by surname Hunscott sweep 1600-1660.",
  "archive": "ROLLCO; underlying data from Stationers' Company records",
  "url": "https://www.londonroll.org/search?company=STN&surname=Hunscott",
  "corpusStatus": "partial",
  "corpusPath": "sources/corpus_supplement/rollco-stationers-hunscott-cluster.md",
  "mediaPath": null,
  "validationPath": "sources/validations/rollco-stationers-hunscott-cluster.md",
  "notes": "Joseph Hunscott appears as Stationers' apprenticeship master in events dated 1612, 1614, 1619, 1626, 1632 (turnover master), 1635, 1636, 1638 (×2), 1642, and 1646 (×2). His son John Hunscott was admitted Stationer by servitude in 1641 with Joseph as 'father of freeman'. The variant spellings Henscott (Robert Gurney's 1625 will), Huntscott (BHO 1638 St Augustine return), and Hunscott (ROLLCO and Wing H3728 1646 petition) are the same person."
}
```

### 1.4 Add `rollco-stationers-gurney-1613-1626`

```json
"rollco-stationers-gurney-1613-1626": {
  "shortTitle": "ROLLCO Stationers - John Gurney 1613 binding and Robert Gurney 1616-1626 apprenticeship sequence",
  "citation": "Records of London's Livery Companies Online (ROLLCO), Stationers' Company event records: John Gurney, new apprentice to master James Boler, 25 March 1613 (STMM8981); Robert Gurney, new apprentice to master William Wrench, 2 September 1616 (STMM10464); Robert Gurney, new freeman by servitude, 15 June 1626 (STMM24305).",
  "archive": "ROLLCO; underlying data from Stationers' Company records",
  "url": "https://www.londonroll.org/search?company=STN&surname=Gurney",
  "corpusStatus": "partial",
  "corpusPath": "sources/corpus_supplement/rollco-stationers-gurney-1613-1626.md",
  "mediaPath": null,
  "validationPath": "sources/validations/rollco-stationers-gurney-1613-1626.md",
  "notes": "Two Stationers' Gurney threads relevant to Candidate D. (1) The 1613 John Gurney apprentice to James Boler has no recorded Stationers' freedom; he is a candidate for being the future Candidate D John, whose 1623/4 Drapers' freedom-by-redemption pathway would be explained by an earlier non-Drapers apprenticeship. (2) The 1616 Robert Gurney apprentice and 1626 Robert Gurney new freeman by servitude form one consistent ten-year apprenticeship under William Wrench; this Robert is a separate man from Robert of Old Change (d. 1625), resolving the so-called 'second Robert' puzzle."
}
```

### 1.5 Add `tna-e179-1661-london-poll-tax-deferred`

```json
"tna-e179-1661-london-poll-tax-deferred": {
  "shortTitle": "TNA E179 - 1661 Free and Voluntary Present, City of London (deferred image-pull target)",
  "citation": "England, Free and Voluntary Present, 1661 (13 Car. II), City of London ward/parish assessments. The National Archives, Kew, E179 series, especially E179/253 sequence for the City.",
  "archive": "The National Archives, Kew",
  "url": "https://www.nationalarchives.gov.uk/e179/",
  "corpusStatus": "deferred",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/tna-e179-1661-london-poll-tax-deferred.md",
  "notes": "Boyd's Inhabitants card for John Gurny of S Augustine carries a free-note '1661 poll tax... Old Change', which points to the 1660-1661 Free and Voluntary Present collection rather than the 1641 Poll Tax. If a Gurney entry can be confirmed at Old Change in 1661, Candidate D is effectively eliminated as the colonial John of Braintree, who died in Boston about March 1662/3. Online image access not currently established."
}
```

### 1.6 Add `bho-1640-principal-inhabitants-london-deferred`

```json
"bho-1640-principal-inhabitants-london-deferred": {
  "shortTitle": "Harvey - List of the Principal Inhabitants of the City of London, 1640 (deferred)",
  "citation": "Harvey, W. J., editor. List of the Principal Inhabitants of the City of London, 1640, from Returns Made by the Aldermen of the Several Wards. London: 1886; reprinted British Library Historical Print Editions, 2011. Original manuscript Lambeth Palace Library MS. 272.",
  "archive": "Lambeth Palace Library MS. 272; printed reprint widely available",
  "url": null,
  "corpusStatus": "deferred",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/bho-1640-principal-inhabitants-london-deferred.md",
  "notes": "1640 alderman-return inhabitants list covering 93 of 107 City parishes. A Gurney entry at St Augustine in 1640 would be a clean midpoint between the 1638 Dale return and the 1661 poll tax cue, strengthening the case for continued London residence. Full text not yet retrieved online; copy held at British Library, Bodleian, and major research libraries."
}
```

### 1.7 Add `arber-stationers-registers-1554-1640-deferred`

```json
"arber-stationers-registers-1554-1640-deferred": {
  "shortTitle": "Arber - Transcript of the Registers of the Stationers' Company 1554-1640 (deferred)",
  "citation": "Arber, Edward, editor. A Transcript of the Registers of the Company of Stationers of London, 1554-1640. 5 vols. London: privately printed, 1875-1894.",
  "archive": "Various; full-text scans intermittently available on Internet Archive and HathiTrust",
  "url": "https://archive.org/details/transcriptofregi01statuoft",
  "corpusStatus": "deferred",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/arber-stationers-registers-1554-1640-deferred.md",
  "notes": "Underlying transcription used by ROLLCO for Stationers' apprenticeships and freedoms. ROLLCO shows the 25 March 1613 John Gurney binding to James Boler (STMM8981) without a father name; the Arber transcript volume 3 raw entry may preserve the father, place of origin, or bond detail that would prove or kill the H-D1 redemption-pathway hypothesis."
}
```

### 1.8 Add `arber-stationers-bsoc-petition-1646-hunscott`

```json
"arber-stationers-bsoc-petition-1646-hunscott": {
  "shortTitle": "Hunscott - Humble Petition and Information, 1646 (Wing H3728)",
  "citation": "Hunscot, Joseph. The Humble Petition and Information of Joseph Hunscot Stationer, To the Honourable Houses of Parliament Assembled. London, 1646. Wing H3728.",
  "archive": "Early English Books Online; Wing Short Title Catalogue",
  "url": null,
  "corpusStatus": "partial",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/arber-stationers-bsoc-petition-1646-hunscott.md",
  "notes": "Identifies Joseph Hunscott as an active Stationer petitioner in 1646. Used here to anchor the identity bridge from Robert Gurney's will overseer 'Joseph Henscott Stationer' (1625) through the BHO 1638 St Augustine 'Joseph Huntscott' (£12) to the named ROLLCO Stationer Joseph Hunscott (1612-1646)."
}
```

## 2. Validation file operations

### 2.1 Replace `sources/validations/bho-london-inhabitants-st-augustine-1638.md`

```markdown
# BHO - Inhabitants of London 1638, St Augustine validation

- Examined: https://www.british-history.ac.uk/no-series/london-inhabitants/1638/pp34-35, accessed 2026-05-01 and re-examined 2026-05-14.
- Scope: full St Augustine parish/rents return — MS. 67, MS. 67a (which contains the John Gurney row), MS. 68; preamble; total £1,700 at 2/9 per £ yielding £233 5s tithe.
- John Gurney entry surfaced in MS. 67a at £10, between Christopher Hunlock £2 and George Browne £10.
- Joseph Huntscott (= Joseph Henscott / Hunscott of will and ROLLCO) surfaced at £12 on MS. p. 68.
- Findings recorded in: `research/people/john-gurney-candidate-d.md`, `research/people/g13-john-gurney-fact-sheet.research.md`, `research/places/city-of-london.md`.
- Detailed phase 1 setup: `sources/intake/processed/v06.patchset.md`.
- Phase 2 deep-research extraction: `sources/intake/processed/v34-john-gurney-candidate-d-phase-2-sources-and-research.patchset.md`.
```

### 2.2 Replace `sources/validations/rollco-drapers-gurney-old-change-cluster.md`

```markdown
# ROLLCO Drapers - Robert and John Gurney Old Change cluster validation

- Source ID: `rollco-drapers-gurney-old-change-cluster`.
- Examined: ROLLCO advanced-search results and event-detail pages for surname Gurney and surname Gourney within the Drapers' Company, year range 1580-1665, accessed 2026-05-14.
- Scope: full Drapers' Gurney/Gourney event corpus for the Old Change cluster, including event IDs DREW4826 (1581 Robert freedom), DREB5398 (1597 Robert master), DREB972, DRHT2178, DREB6664, DRLL837, DREB6662, DREB3081, DREW68, DREB6663, DRLL2652, DREB2377, DRHT1660, DRHT1669, DREW7982, DREW5638 (1623/4 John freedom by redemption), DREB1311 (1629 Marten Backhurst freedom; Robert as master, posthumous), and DRLL2060 (1630 John as master binding Henry Smith of Kilton, Suffolk).
- Method note: the 1629 event names Robert as master without a 'deceased' flag; cross-checked against the 1625 probate of Robert (will source `acl-robert-gurney-will-1625`), this is a posthumous master-name record, not a second living Robert.
- Findings recorded in: `research/people/john-gurney-candidate-d.md` and `sources/corpus_supplement/rollco-drapers-gurney-old-change-cluster.md`.
- Detailed phase 1 setup: `sources/intake/processed/v32-john-gurney-candidate-d-source-foundation.patchset.md`.
- Phase 2 deep-research extraction: `sources/intake/processed/v34-john-gurney-candidate-d-phase-2-sources-and-research.patchset.md`.
```

### 2.3 Create `sources/validations/rollco-stationers-hunscott-cluster.md`

```markdown
# ROLLCO Stationers - Joseph Hunscott cluster validation

- Source ID: `rollco-stationers-hunscott-cluster`.
- Examined: ROLLCO advanced-search results for surname Hunscott within the Stationers' Company, year range 1600-1660, accessed 2026-05-14.
- Scope: 14 Joseph Hunscott Stationers' events 1612-1646 and one 1641 freedom event admitting his son John Hunscott by servitude.
- Findings recorded in: `research/people/john-gurney-candidate-d.md`.
- Phase 2 deep-research extraction: `sources/intake/processed/v34-john-gurney-candidate-d-phase-2-sources-and-research.patchset.md`.
```

### 2.4 Create `sources/validations/rollco-stationers-gurney-1613-1626.md`

```markdown
# ROLLCO Stationers - Gurney 1613-1626 sequence validation

- Source ID: `rollco-stationers-gurney-1613-1626`.
- Examined: ROLLCO advanced-search results for surname Gurney within the Stationers' Company, year range 1605-1640, plus event-detail pages STMM8981 (1613 John binding), STMM10464 (1616 Robert binding), and STMM24305 (1626 Robert freedom).
- Method note: ROLLCO STMM24305 does not carry a master-name field; STMM10464 names William Wrench as master and gives no father; STMM8981 names James Boler as master and gives no father. The Arber underlying transcription should be consulted to test whether the original Stationers' Court Book preserved more detail.
- Findings recorded in: `research/people/john-gurney-candidate-d.md`.
- Phase 2 deep-research extraction: `sources/intake/processed/v34-john-gurney-candidate-d-phase-2-sources-and-research.patchset.md`.
```

### 2.5 Create `sources/validations/tna-e179-1661-london-poll-tax-deferred.md`

```markdown
# TNA E179 - 1661 Free and Voluntary Present, City of London (deferred)

- Source ID: `tna-e179-1661-london-poll-tax-deferred`.
- Examined: not yet examined at image level; only the existence of the City of London E179 fragments and the 8 July 1661 royal assent date confirmed via The National Archives E179 finding aid and Wikipedia poll-tax overview.
- Scope (target): Castle Baynard ward and adjacent wards covering St Augustine Watling Street / Old Change, 1660-1661.
- Reason kept: Boyd's Inhabitants card for John Gurny of S Augustine carries a free-note '1661 poll tax... Old Change'; if confirmed at image level, this would be an essentially decisive datum against Candidate D as the Massachusetts John.
- Findings recorded in: `research/people/john-gurney-candidate-d.md` next-steps section.
- Phase 2 deep-research extraction: `sources/intake/processed/v34-john-gurney-candidate-d-phase-2-sources-and-research.patchset.md`.
```

### 2.6 Create `sources/validations/bho-1640-principal-inhabitants-london-deferred.md`

```markdown
# Harvey - 1640 Principal Inhabitants of the City of London (deferred)

- Source ID: `bho-1640-principal-inhabitants-london-deferred`.
- Examined: not yet examined; existence confirmed via WorldCat, Powell's, AbeBooks, and Amazon listings of the 2011 British Library Historical Print Editions reprint of the 1886 Harvey edition.
- Scope (target): St Augustine Watling Street and adjacent parishes in the 1640 aldermen's returns.
- Reason kept: a 1640 entry would be a clean midpoint between the 1638 Dale return and the Boyd-card 1661 poll-tax cue, strengthening or weakening the continued-residence reading.
- Findings recorded in: `research/people/john-gurney-candidate-d.md` next-steps section.
- Phase 2 deep-research extraction: `sources/intake/processed/v34-john-gurney-candidate-d-phase-2-sources-and-research.patchset.md`.
```

### 2.7 Create `sources/validations/arber-stationers-registers-1554-1640-deferred.md`

```markdown
# Arber - Stationers' Registers Transcript (deferred)

- Source ID: `arber-stationers-registers-1554-1640-deferred`.
- Examined: not yet examined at image/text level; existence confirmed via Internet Archive catalog entries and Hathi Trust catalog records 001168984 and related IDs. Multiple Archive instances either unavailable for direct fetch in this pass or borrow-only.
- Scope (target): Volume 3 covering 1595-1620, especially the 25 March 1613 apprentice-binding line for John Gurney to master James Boler.
- Findings recorded in: `research/people/john-gurney-candidate-d.md` next-steps section.
- Phase 2 deep-research extraction: `sources/intake/processed/v34-john-gurney-candidate-d-phase-2-sources-and-research.patchset.md`.
```

### 2.8 Create `sources/validations/arber-stationers-bsoc-petition-1646-hunscott.md`

```markdown
# Hunscott petition 1646 (Wing H3728) validation

- Source ID: `arber-stationers-bsoc-petition-1646-hunscott`.
- Examined: existence and ascription of the 1646 Joseph Hunscott petition confirmed via the Taylor & Francis chapter republishing the text in Geoff Kemp and Jason McElligott, eds., *Censorship and the Press, 1580-1720*, citing Wing H3728.
- Scope: identity confirmation for the will overseer 'Joseph Henscott Stationer' named in Robert Gurney's 1625 will, supporting the BHO 1638 'Joseph Huntscott' reading.
- Findings recorded in: `research/people/john-gurney-candidate-d.md`.
- Phase 2 deep-research extraction: `sources/intake/processed/v34-john-gurney-candidate-d-phase-2-sources-and-research.patchset.md`.
```

## 3. Corpus supplement files

### 3.1 Replace `sources/corpus_supplement/bho-london-inhabitants-st-augustine-1638.md`

```markdown
# BHO - Inhabitants of London 1638, St Augustine

- Source ID: `bho-london-inhabitants-st-augustine-1638`
- Citation: Dale, T. C. "Inhabitants of London in 1638: St. Augustine." In The Inhabitants of London in 1638. Society of Genealogists, 1931. British History Online.
- Archive: British History Online
- URL: https://www.british-history.ac.uk/no-series/london-inhabitants/1638/pp34-35
- Intake patchsets: `sources/intake/processed/v06.patchset.md`, `sources/intake/processed/v34-john-gurney-candidate-d-phase-2-sources-and-research.patchset.md`

## Structure of the return

The St Augustine 1638 return is a rents/tithe assessment, not a head-count census. The preamble describes a £1,700 total assessed value producing £233 5s tithe at 2/9 in the pound (about 2s 9d per £). The return is divided into three manuscript sections, transcribed under the headings:

- **St Augustine. Rents. MS. p. 67** — first section, 42 entries, values £6-£80.
- **MS. 67a** — second section, 41 entries, values £2-£40. The label and physical separation from MS. 67 suggest this list captures a separate categorical group of premises (likely shops or non-resident lessees).
- **MS. p. 68** — third section, 24 entries, values £1 10s-£20.

## John Gurney row

John Gurney appears once in the entire return, in MS. 67a at £10. The local context is:

```
Christopher Hunlock      £2
John Gurney             £10
George Browne           £10
Henry Mason             £16
George Gill             £10
Edmord Gregory          £10
William Norrice         £10
Hugh Jones              £10
```

£10 places John in the middle of the assessment band. Top of MS. 67: Daniel Hollingworth £80, Stephen Offley £46. Bottom of MS. p. 68: Anne Beale £1 10s. £10 is the most common single value in MS. 67a, consistent with a working ratepayer occupying a standard shop or tenement.

## Joseph Huntscott row

MS. p. 68 includes Joseph Huntscott at £12, immediately preceding Thomas Flower £10. Joseph Huntscott is best read as Joseph Hunscott (alias Henscott), the Stationer who served as overseer of Robert Gurney's 1625 will. Independent ROLLCO evidence shows Joseph Hunscott as an active Stationers' Company apprenticeship master from 1612 to 1646 and the father of John Hunscott (Stationer freeman 1641). The 1646 petition Wing H3728, "The Humble Petition and Information of Joseph Hunscot Stationer," confirms his continued London activity.

## Interpretive note

The 1638 return places one John Gurney and Joseph Huntscott in the same parish. Given the demonstrated 1625 will-network relationship between the Old Change Robert Gurney's executor John and the Stationer Joseph Henscott, the most economical reading is that the 1638 John Gurney is the same John Gurney who took Drapers' Company freedom by redemption in 1623/4 and who took on the apprentice Henry Smith at Old Change in 1630. This is not proof, because no occupation, residence street, or kinship is stated in the return.
```

### 3.2 Create `sources/corpus_supplement/rollco-drapers-gurney-old-change-cluster.md`

```markdown
# ROLLCO Drapers - Robert and John Gurney Old Change cluster

- Source ID: `rollco-drapers-gurney-old-change-cluster`
- Search base: https://www.londonroll.org/search?company=drp&surname=Gurney and the surname=Gourney variant search.
- Captured: 2026-05-14

## Full Drapers' Gurney event corpus 1581-1654

| Year | Person | Role | Occupation / Location | Event ID | Counterparty / Notes |
|------|--------|------|----------------------|----------|-----|
| 1581 Dec 16 | Robert Gourney | New freeman by servitude | Tailor, Old Change | DREW4826 | Master: Robert Furnes. Already styled 'Tailor, Old Change' at admission. |
| 1597 | Robert Gourney | Freedom Master | Not stated | DREB5398 | First Drapers' master appearance after admission. |
| 1603 | Robert Gurney | Apprenticeship Master | Not stated | DREB972 | |
| 1603 | Robert Gurney | Apprenticeship Master | Not stated | DRHT2178 | |
| 1604 | Robert Gurney | Apprenticeship Master | Not stated | DREB6664 | |
| 1604 Aug 1 | Robert Gurney | Freedom Witness | Tailor, Old Change | DRLL837 | New freeman: Richard Sebrineke (servitude). Earliest explicit 'Tailor, Old Change' identification in the post-1581 events. |
| 1605 | Robert Gurney | Freedom Master | Not stated | DREB6662 | |
| 1605 | Robert Gurney | Apprenticeship Master | Not stated | DREB3081 | |
| 1609 | Robert Gurney | Apprenticeship Master | Not stated | DREW68 | |
| 1611 | Robert Gurney | Freedom Master | Not stated | DREB6663 | |
| 1612 | Robert Gurney | Apprenticeship Master | Not stated | DRLL2652 | |
| 1614 | Robert Gurney | Freedom Master | Not stated | DREB2377 | |
| 1614 | Robert Gurney | Apprenticeship Master | Not stated | DRHT1660 | |
| 1617 | Robert Gurney | Apprenticeship Master | tailor, Old Change | DRHT1669 | New apprentice: John Lee, son of Edward Lee yeoman of Shenley, Bucks. 7-year bond. |
| 1622 May 30 | Robert Gurney | Apprenticeship Master | tailor | DREW7982 | New apprentice: William Holdsworth, son of William Holdsworth tailor of Sowerby Bridge, Yorkshire. 7-year bond. |
| 1623/4 Feb 11 | John Gurney | New freeman by redemption | Not stated | DREW5638 | Father (same event): Robert Gurney. |
| 1623/4 Feb 11 | Robert Gurney | Father of freeman | Not stated | DREW5638 | Same event row as John's freedom; freedom method redemption (not patrimony). |
| 1629 Feb 14 | Robert Gurney | Master (in someone else's freedom) | Not stated | DREB1311 | New freeman by servitude: Marten Backhurst. Robert had died 23 Sept 1625; this is a posthumous master-name record. ROLLCO does not flag Robert as deceased here. |
| 1630 Nov 3 | John Gurney | Apprenticeship Master | Not stated | DRLL2060 | New apprentice: Henry Smith, son of late Thomas Smith yeoman of Kilton, Suffolk. 7-year bond. |
| 1654 | John Gourney | Father of apprentice, Sponsor | gent, Hanging Holton, Northants | DREW4827 | New apprentice: Charles Gourney. Separate Northants gentry family; not the Old Change cluster. |

## Cross-references

- Robert's 1581 master Robert Furnes corrects the Boyd card 5 reading 'Robert Mason[?]' for the same event.
- Robert's death 23 Sept 1625 is documented in `acl-robert-gurney-will-1625` (will image `31787_A002570-00422.jpg`).
- John's 1630 apprentice Henry Smith does not appear as a freed Drapers' Smith 1635-1645 under John Gurney as master, and no Drapers' Turnover event for any Gurney exists 1620-1670, so Henry Smith's apprenticeship trail terminates in the records without a clean completion or turnover.
- The 1604 William Gurney freedom (DREW5637, master Robert Warner) is a separate William, not apprenticed to Robert Gurney.
```

### 3.3 Create `sources/corpus_supplement/rollco-stationers-hunscott-cluster.md`

```markdown
# ROLLCO Stationers - Joseph Hunscott cluster

- Source ID: `rollco-stationers-hunscott-cluster`
- Search base: https://www.londonroll.org/search?company=STN&surname=Hunscott
- Captured: 2026-05-14

## Joseph Hunscott events in Stationers' Company

14 events 1612-1646:

- 1612 Apprenticeship Master (Co Stationer)
- 1614 Apprenticeship Master
- 1619 Apprenticeship Master
- 1626 Apprenticeship Master
- 1632 App/Turnover Turnover master
- 1635 Apprenticeship Master
- 1636 Apprenticeship Master
- 1638 Apprenticeship Master (×2)
- 1641 Freedom Father of freeman (his son John Hunscott admitted by servitude)
- 1642 Apprenticeship Master
- 1646 Apprenticeship Master (×2)

## Joseph Hunscott elsewhere

- 1625: Joseph Henscott named as overseer in Robert Gurney's will (will source `acl-robert-gurney-will-1625`).
- 1638: Joseph Huntscott at £12 in MS. p. 68 of the St Augustine return (source `bho-london-inhabitants-st-augustine-1638`).
- 1646: Joseph Hunscot publishes *The Humble Petition and Information of Joseph Hunscot Stationer*, Wing H3728. Royalist anti-libel petition to Parliament. Source `arber-stationers-bsoc-petition-1646-hunscott`.

## Identity bridge

The spelling variants Henscott (1625 will), Huntscott (1638 BHO), Hunscott (ROLLCO and 1646 petition) refer to the same Stationer. He lived in St Augustine parish at least 1625-1638 and remained an active Stationer until at least 1646. This anchors the parish-network continuity argument across the 1625-1638 window of greatest interest for Candidate D.
```

### 3.4 Create `sources/corpus_supplement/rollco-stationers-gurney-1613-1626.md`

```markdown
# ROLLCO Stationers - Gurney 1613-1626 sequence

- Source ID: `rollco-stationers-gurney-1613-1626`
- Search base: https://www.londonroll.org/search?company=STN&surname=Gurney
- Captured: 2026-05-14

## Events

### 1613 - John Gurney apprentice to James Boler (STMM8981)

| Field | Value |
|---|---|
| Event Date | 25 March 1613 (Lady Day) |
| Event | Apprenticeship |
| Apprentice | John Gurney (Male), location unknown |
| Master | James Boler (Male), Co Stationer, location unknown |
| Father | not recorded |
| Bond length | not recorded |
| Reference | ST/1:0812 |

No subsequent Stationers' freedom record under James Boler or any other Stationer master is recorded for this John Gurney.

### 1616 - Robert Gurney apprentice to William Wrench (STMM10464)

| Field | Value |
|---|---|
| Event Date | 2 September 1616 |
| Event | Apprenticeship |
| Apprentice | Robert Gurney (Male), location unknown |
| Master | William Wrench (Male), location unknown |
| Father | not recorded |
| Reference | ST/1:2791 |

### 1626 - Robert Gurney new freeman (STMM24305)

| Field | Value |
|---|---|
| Event Date | 15 June 1626 |
| Event | Freedom |
| Freedom method | Servitude |
| New freeman | Robert Gurney (Male), Co Stationer |
| Master | not recorded in summary |

The 1616 binding and the 1626 freedom together describe one ten-year apprenticeship by Robert Gurney in the Stationers' Company. This Robert is a separate person from Robert Gourney of Old Change (Drapers' freeman 1581, d. 1625). The Old Change Robert was already a Drapers' freeman of 35 years' standing in 1616 and could not have been bound as a fresh Stationers' apprentice. The Stationer Robert is therefore generationally and trade-wise distinct.

## Working hypothesis (H-D1)

The 1613 John Gurney binding to James Boler is open to interpretation. If this John is the future Candidate D John (born about 1599-1600 as the replacement son of Robert of Old Change after the first John's 1599/1600 burial), then a Stationers' apprenticeship started in 1613 would normally end in freedom around 1620-1621. The absence of a Stationers' freedom record, plus the 1623/4 Drapers' freedom by redemption (not patrimony, despite Robert's 1581 freedom), is consistent with Candidate D having served apprenticeship in a different company, abandoning Stationer freedom in favour of taking up his father's Drapers'/tailoring business via the redemption route.

This hypothesis is consistent with the Robert Gurney 1625 will choice of Joseph Henscott Stationer as an overseer alongside Thomas Dunnell brother-in-law: a senior Stationer would be a natural overseer choice for the executor son if that son had a personal Stationer-Company history. The hypothesis is not yet proven; the Arber transcript volume 3 raw entry for 25 March 1613 may preserve a father name that would confirm or refute it.
```

## 4. Research file operations

### 4.1 Create `research/people/john-gurney-candidate-d.md` (Candidate D topic file)

```markdown
# John Gurney - Candidate D - London draper of Old Change

This research file holds the depth and detail of the Candidate D investigation, kept out of the main John Gurney case file so that the case file's Section 8 stays tight. Candidate D is John Gurney, adult son and executor of Robert Gurney, citizen and draper of London / tailor of Old Change, with John made free of the Drapers' Company by redemption on 11 February 1623/4.

The companion summary lives in `research/case-files/john-gurney-case-file-v4.md` Section 8.4. Working extracts and transcriptions are in `sources/intake/john-gurney-2026May/john-gurney-candidate-d-working-packet-audited-v13.md`.

## Identity anchor

Robert Gurney died in late September 1625 leaving a will written 18 January 1621/2 and proved at the Archdeaconry Court of London on 23 September 1625 by the oath of John Gurney, son and executor. Robert styled himself "Robert Gurney Citizen and Draper of London" and gave his dwelling in Old Change. Robert left wife Anne use of the two uppermost rooms of his Old Change house while she continued his widow, and gave his son John Gurney the shop, cellar, and hall under the same house plus the residue. Thomas Dunnell, brother-in-law, and Joseph Henscott, stationer and citizen of London, were overseers.[^acl-will]

Independent ROLLCO evidence places John Gurney as a new freeman of the Drapers' Company by redemption on 11 February 1623/4, in the same event row that names Robert Gurney as father of the freeman.[^rollco-drapers-1624]

## Robert of Old Change: confirmed career 1581-1625

Robert Gourney was admitted to the Drapers' Company by servitude on 16 December 1581 under master Robert Furnes, already described as "Tailor, Old Change" at his admission.[^rollco-1581] The Boyd's Inhabitants card for Robert had read the 1581 master as "Robert Mason[?]"; the ROLLCO event detail (DREW4826) corrects the master to Robert Furnes.[^rollco-1581]

ROLLCO records about 14 Drapers' apprenticeship- or freedom-master events for Robert Gurney between 1597 and 1622. The "Tailor, Old Change" occupation/location appears in DRLL837 (1604), DRHT1669 (1617), and DREW7982 (1622). Two of those events name the apprentice and place of origin:

- 1617 (DRHT1669): apprentice John Lee, son of Edward Lee yeoman of Shenley, Buckinghamshire; 7-year bond.[^rollco-1617]
- 1622 (DREW7982): apprentice William Holdsworth, son of William Holdsworth tailor of Sowerby Bridge, Yorkshire; 7-year bond.[^rollco-1622]

The 1604 freedom event DRLL837 records Robert Gurney as Witness at the admission of Richard Sebrineke by servitude; the witness role typically marks Robert as Sebrineke's earlier master.[^rollco-1604]

A 1611 Drapers' freedom-master event predates Robert's own 1611 St Magnus marriage to Anne Morris by months and shows the established master functioning continuously across the marriage year.[^rollco-1611]

A 1629 Drapers' freedom-by-servitude event admitting Marten Backhurst (DREB1311) names Robert Gurney as master without any deceased flag. Cross-checked against the 1625 probate, this is a posthumous master-name record: Backhurst had been bound to Robert before September 1625 and completed servitude in 1629. ROLLCO data conventions do not retrofit a deceased flag onto a master who died during the apprentice's term, so the 1629 event does not point to a second living Robert Gurney.[^rollco-1629]

## John as freeman and master 1623/4 - 1630

The 11 February 1623/4 Drapers' freedom event (DREW5638) is a single integrated transaction recording John Gurney as new freeman by redemption and Robert Gurney as father of freeman. Neither party has an occupation or location stated in the event record.[^rollco-1624]

On 3 November 1630, John Gurney appeared as a Drapers' apprenticeship master in event DRLL2060, binding Henry Smith, son of late Thomas Smith yeoman of Kilton, Suffolk, for a 7-year term. John still has no occupation or location stated, but the active master role implies a London tailoring or draper's business, almost certainly the Old Change premises John inherited under Robert's 1625 will.[^rollco-1630]

Henry Smith does not appear as a freed Drapers' Smith between 1635 and 1645 under John Gurney as master or under any other Drapers' master, and no Turnover event involving any Gurney is recorded in the Drapers' Company between 1620 and 1670. The apprenticeship trail therefore terminates inconclusively: Smith may have died during apprenticeship, defaulted, completed without paying the freedom fine, or been turned over informally without a recorded event. The silence is not strong enough to prove either continued London residence or emigration by John Gurney.[^rollco-1630]

## Freedom by redemption: why not patrimony

The Drapers' freedom-by-redemption route was the standard pathway for an adult man who had not served a Drapers' apprenticeship. Robert Gurney had been a Drapers' freeman since 16 December 1581, so a son born after that date would have been entitled to free patrimony admission. John's choice of redemption is an anomaly that needs explanation.

Three live readings:

1. **John served an apprenticeship in a different company.** A man admitted to one company's freedom by completing apprenticeship elsewhere typically had to pay redemption to enter the Drapers'. ROLLCO records a John Gurney apprentice bound to the stationer James Boler on 25 March 1613 (STMM8981) with no recorded Stationers' freedom; if this is the future Candidate D John, the 1623/4 Drapers' redemption would be the natural consequence of an aborted or completed Stationers' apprenticeship. This is hypothesis H-D1; it is internally consistent with the choice of Joseph Henscott Stationer as a will overseer in 1625, but the Arber Stationers' transcript volume 3 raw entry has not yet been checked for a father name that would confirm or kill the link.[^rollco-stationers-1613]
2. **John was born before Robert's December 1581 freedom and was therefore not eligible for patrimony.** This would require Candidate D John to be born about 1574-1580 and to be roughly 44-50 in 1623/4, 58-64 in 1638, and 81-87 in 1661 if Boyd's 1661 poll-tax cue is real. It is biologically possible but does not fit the colonial John's c.1603 birth deposition.
3. **Procedural choice.** Some adult sons paid redemption for speed, formality, or because their patrimony claim was unclear. This is the default reading absent more evidence.

The most economical of these is H-D1; the strongest neutral fallback is reading 3.

## 1638 St Augustine: parish continuity and Hunscott

The T. C. Dale 1931 transcription of the 1638 London Inhabitants return places one John Gurney at £10 in MS. 67a of the St Augustine parish/rents return, between Christopher Hunlock £2 and George Browne £10. The return is a rents/tithe assessment, not a head-count, with £1,700 total assessed at 2/9 in the pound yielding £233 5s tithe.[^bho-1638]

On MS. p. 68 of the same return, **Joseph Huntscott** appears at £12. This is the same Joseph Hunscott who was a documented Stationers' Company apprenticeship master from 1612 to 1646 and the father of John Hunscott (Stationer freeman 1641), and the same Joseph Hunscot who in 1646 published *The Humble Petition and Information of Joseph Hunscot Stationer* (Wing H3728). The 1625 will of Robert Gurney named "Joseph Henscott, stationer and citizen of London," as one of two overseers; the Henscott / Huntscott / Hunscott spellings denote a single person who lived in St Augustine parish at least 1625-1638 and remained an active Stationer until at least 1646.[^rollco-hunscott][^hunscott-petition]

Two corollaries:

- **Parish-network continuity.** The Robert Gurney will-overseer network was still in St Augustine in 1638. The most economical reading of the 1638 John Gurney entry is that he was a continuing member of the same parish circle, occupying the Old Change shop premises Robert had left him; the alternative reading (a coincidentally same-named separate John Gurney resident in St Augustine alongside the Hunscott household for the 13 years between probate and the BHO return) is uneconomical.
- **The 1638 John is unlikely to be the Massachusetts John.** The colonial John of Braintree is in Weymouth, Massachusetts by June 1641 (General Court fine), with a New England family already including a daughter Mary born about 1628 in England, son Richard about 1630 in England, son John about 1633 in England, and son Peter about 1635 in England. A 1636 arrival window is the conventional reading. A John Gurney still being assessed at £10 rent in St Augustine in 1638 is incompatible with that profile.

## 1661 poll-tax cue (deferred)

The Boyd's Inhabitants card for John Gurny of S Augustine carries a partly-legible free-note reading "1661 poll tax [unclear] Old Change". The most likely underlying record is the 1661 Free and Voluntary Present collection (13 Car. II, royal assent 8 July 1661), with City of London assessments in TNA E179 (especially the E179/253 sequence). If a Gurney entry at Old Change in 1661 can be confirmed at image level, Candidate D is effectively eliminated as the Massachusetts John, who died in Boston about March 1662/3. No online image has yet been located.[^tna-e179]

A second potentially useful midpoint is the 1640 W. J. Harvey list of Principal Inhabitants of the City of London (Lambeth MS 272), reprinted by the British Library Historical Print Editions in 2011. Full text has not been retrieved online in this pass.[^harvey-1640]

## Family reconstruction at St Augustine

The St Augustine Watling Street parish register (LMA P69/AUG) confirms an earlier child sequence to Robert Gurny before his 1611 St Magnus marriage to Anne Morris:[^st-augustine-register]

- John Gurny, son of Robert, baptized 18 February 1595/6, buried 4 February 1599/1600.
- Marye Gurny / Gorney, daughter of Robert, baptized 12 March 1597/8, buried 25 January 1600/1.
- Unnamed stillborn son of Robert, buried 8 April 1601.

No replacement-John baptism was found in the supplied St Augustine christening images from 1601 through 1610, and no first-wife burial was found in the supplied St Augustine burial images from 1601 through 1612.[^st-augustine-register]

Robert married Anne Morris of St Michael in the Querne by licence at St Magnus the Martyr on 4 April 1611. The original parish entry confirms the marriage but does not state marital status, so does not formally identify Robert as a widower at remarriage.[^st-magnus-1611]

The earlier-child sequence weakens any assumption that Anne Morris was Candidate D John's biological mother. Anne was confirmed as Robert's wife and widow-beneficiary in 1625, but the earliest documented Robert child at St Augustine baptized 1595/6 sits 15 years before the Anne Morris marriage.

## Religious-language assessment

Robert's will preamble commits his soul to Almighty God his creator and to Jesus Christ his only Saviour and Redeemer, by whose mercy and merits the testator believes he has obtained "full and free remission pardon" for all sins, and looks to enjoy "eternal life with others the elect children of god in the kingdom of heaven." The phrase "elect children of God" is Reformed / Calvinist-compatible vocabulary; the formula is consistent with a godly-Protestant milieu but does not by itself prove Puritan identity, nonconformity, or emigration intent.[^acl-will]

No identified Puritan minister, lecturer, named nonconforming associate, Coleman Street-network member, or known New England-connected name appears in Robert's will or in the Drapers'/Stationers' records around the Old Change household. The St Stephen Coleman Street parish (the main London emigration hub) does contain a William Gurney + Tamazin family with children Fotheza 1626, Adeall 1628, Susanna 1630, Marke 1636 - none of those names match the colonial John family pattern of Sarah, Mary, Richard, John, Peter, and the family has no demonstrated link to Robert's household.[^st-stephen-coleman-street]

Old Change as a textile-trade geography remains a context clue rather than a migration-corridor clue.

## Wife and children test

No marriage of Candidate D John to a wife named Mary, and no baptisms of Sarah, Mary, Richard, John, or Peter to a John Gurney + Mary household, have been located in any London parish register, City of London Drapers' / Stationers' / Haberdashers' material, or FamilySearch indexes for the 1620-1641 window. The nearest John Gurney + Mary marriage in the time window is the Eythorne, Kent, marriage of John Gurney + Mary Marsh on 6 November 1632, with a son John baptized at the same Kent parish on 13 May 1638 - a Kent couple who stayed in Kent and whose child-naming sequence (first known child John 1638) is incompatible with the colonial John family (first child Mary about 1628, son John not until about 1633).[^fs-john-mary-london]

No PCC will or administration for Anne Gurney widow has been located in the 1625-1670 window; one potentially relevant Anne-Gurney marriage in the supplied FamilySearch sweep is "An Gurney + George Bucher, 27 April 1640, Essex," but the indexed entry gives only the bare event with no parish specification and is treated as a low-confidence lead pending image review.[^anne-gurney-search]

## Comparator: Hanging Houghton John Gourney (1647-1654)

A separate John Gourney "gent" of Hanging Houghton, Northamptonshire, appears in ROLLCO records placing his son Charles Gourney as a Drapers' apprentice in 1654 (DREW4827), and earlier placing a son in a Clothworkers' apprenticeship in 1647 with the same residence reading. Hanging Houghton was a Montague family seat; this gentry family is geographically and socially distinct from Robert of Old Change. Keep visible as a comparator only.[^rollco-hanging-houghton]

## Working assessment

Candidate D is substantially weakened (not eliminated) as a candidate for John Gurney of Braintree, primarily by post-1625 London continuity evidence:

- 1630 Drapers' apprenticeship-master role (binding Henry Smith, 7-year term).
- 1638 St Augustine £10 rent return, with documented will-network associate Joseph Hunscott still in the same parish.
- Boyd's card cue to a 1661 Old Change poll-tax entry (deferred image verification).
- Absence of any matching wife Mary, child set, Puritan-corridor associate, or Massachusetts bridge record.

The 1604 push-back of Robert's "Tailor, Old Change" identification to (at the latest) his 1604 Drapers' witness event, plus the 1581 admission already styled "Tailor, Old Change," locks the household to Old Change for 44 years (1581-1625). Robert of Old Change was a long-tenured London draper-tailor, not a recent arrival, with documented apprentices drawn from Buckinghamshire (Shenley) and Yorkshire (Sowerby Bridge) - a typical Drapers' master profile, not a profile suggestive of a migration network.

Strengths of Candidate D as a comparator remain real:

- Father in textile trade (Drapers' Company / Old Change / tailor).
- Adult son of a textile-trade household admitted to the Drapers' Company in the early 1620s.
- Plausible c.1600-1604 birth window if the replacement-John reading is correct.
- Reformed-vocabulary will preamble compatible with godly-Protestant milieu.

But the case for Candidate D being the colonial John depends on (a) wife Mary appearing somewhere in the London record, (b) a 1633-1638 child set matching Sarah, Mary, Richard, John, Peter, and (c) a clean disappearance of the London John before about 1641. None of those three have been found, and the 1638 BHO and the deferred 1661 cue actively point the other way.

## Next steps, ranked by tractability and value

1. **Pull the 1661 Old Change poll-tax record.** TNA E179 series, particularly E179/253 fragments for the City. If Ancestry's London E179 collection covers the relevant ward at image level, this is the cleanest single discriminator. Source `tna-e179-1661-london-poll-tax-deferred`.
2. **Pull the 1640 W. J. Harvey list of Principal Inhabitants of the City of London** for St Augustine entries. The 2011 BL reprint is widely available; check whether Internet Archive or HathiTrust unlocks full text. Source `bho-1640-principal-inhabitants-london-deferred`.
3. **Pull the Arber Stationers' Registers volume 3 raw entry** for the 25 March 1613 binding of John Gurney to James Boler. A father name would confirm or kill the H-D1 hypothesis. Source `arber-stationers-registers-1554-1640-deferred`.
4. **Walk the St Augustine Watling Street parish-administrative records (vestry, churchwardens' accounts, poor and tithe rate books) 1625-1665.** LMA P69/AUG. The original `lma-st-augustine-watling-register-candidate-d-images` source covered baptisms and burials only; the administrative books would directly test post-1625 household continuity.
5. **Walk the Archdeaconry Court of London and Commissary Court of London admon/will indexes 1625-1670** for Anne Gurney widow and any London John Gurney draper/tailor. PCC search came back empty; lesser-court coverage is needed.
6. **Verify the Hanging Houghton John Gourney 1647 and 1654 events** in detail to keep the Northamptonshire gentry comparator separated from any Northamptonshire activity associated with Candidate A (Walgrave) and from any later Massachusetts conflation.
7. **Search Stationers' Court Books for John Gurney 1613-1625** beyond what ROLLCO surfaces (turnover events, registers of testimony, freedom-by-redemption parallel entries). Useful if H-D1 is to be pursued seriously.
8. **Confirm the 27 April 1640 An Gurney + George Bucher Essex marriage** at parish-image level - the only plausibly Anne-Morris-aged Anne Gurney marriage indexed in the supplied FS sweep.
9. **Identify James Boler's parish of business in 1613.** Even brief context on Boler (then a young Stationer probably operating at or near Cornhill / St Paul's) would strengthen or weaken the H-D1 link.

[^acl-will]: Robert Gurney, citizen and draper of London, will written 18 January 1621/2, proved 23 September 1625, Archdeaconry Court of London; user-supplied image `31787_A002570-00422.jpg`; full transcription in `sources/intake/john-gurney-2026May/john-gurney-candidate-d-working-packet-audited-v13.md` section 8. Source ID: `acl-robert-gurney-will-1625`.
[^rollco-drapers-1624]: ROLLCO Drapers' Company event DREW5638, freedom by redemption, 11 February 1623/4, new freeman John Gurney, father of freeman Robert Gurney. https://www.londonroll.org/event/?company=drp&event_id=DREW5638. Source ID: `rollco-drapers-gurney-old-change-cluster`.
[^rollco-1581]: ROLLCO Drapers' Company event DREW4826, freedom by servitude, 16 December 1581, new freeman Robert Gourney "Tailor, Old Change", master Robert Furnes. https://www.londonroll.org/event/?company=drp&event_id=DREW4826. Source ID: `rollco-drapers-gurney-old-change-cluster`.
[^rollco-1617]: ROLLCO Drapers' Company event DRHT1669, 1617 apprenticeship, master Robert Gurney "tailor, Old Change", new apprentice John Lee of Shenley Bucks, father Edward Lee yeoman, 7-year bond. Source ID: `rollco-drapers-gurney-old-change-cluster`.
[^rollco-1622]: ROLLCO Drapers' Company event DREW7982, 30 May 1622 apprenticeship, master Robert Gurney tailor, new apprentice William Holdsworth, father William Holdsworth tailor of Sowerby Bridge Yorkshire, 7-year bond. Source ID: `rollco-drapers-gurney-old-change-cluster`.
[^rollco-1604]: ROLLCO Drapers' Company event DRLL837, 1 August 1604 freedom by servitude, new freeman Richard Sebrineke, witness Robert Gurney "Tailor, Old Change". Source ID: `rollco-drapers-gurney-old-change-cluster`.
[^rollco-1611]: ROLLCO Drapers' Company event DREB6663, 1611 freedom event with Robert Gurney as master. Source ID: `rollco-drapers-gurney-old-change-cluster`.
[^rollco-1629]: ROLLCO Drapers' Company event DREB1311, 14 February 1629 freedom by servitude, new freeman Marten Backhurst, master Robert Gurney (no deceased flag in record; cross-checked against 1625 probate). Source ID: `rollco-drapers-gurney-old-change-cluster`.
[^rollco-1630]: ROLLCO Drapers' Company event DRLL2060, 3 November 1630 apprenticeship, master John Gurney, new apprentice Henry Smith, father Thomas Smith yeoman (deceased) of Kilton Suffolk, 7-year bond. Source ID: `rollco-drapers-gurney-old-change-cluster`.
[^rollco-stationers-1613]: ROLLCO Stationers' Company event STMM8981, 25 March 1613 apprenticeship, master James Boler Co Stationer, new apprentice John Gurney, reference ST/1:0812; no father recorded; no subsequent freedom under Boler. Source ID: `rollco-stationers-gurney-1613-1626`.
[^bho-1638]: T. C. Dale, "Inhabitants of London in 1638: St. Augustine," in *The Inhabitants of London in 1638* (Society of Genealogists, 1931), British History Online, https://www.british-history.ac.uk/no-series/london-inhabitants/1638/pp34-35; John Gurney in MS. 67a at £10 between Christopher Hunlock £2 and George Browne £10; Joseph Huntscott on MS. p. 68 at £12. Source ID: `bho-london-inhabitants-st-augustine-1638`.
[^rollco-hunscott]: ROLLCO Stationers' Company event corpus for Joseph Hunscott 1612-1646; 14 apprenticeship/freedom events; son John Hunscott admitted Stationer by servitude 1641 with Joseph as father of freeman. Source ID: `rollco-stationers-hunscott-cluster`.
[^hunscott-petition]: Joseph Hunscot, *The Humble Petition and Information of Joseph Hunscot Stationer, To the Honourable Houses of Parliament Assembled* (London, 1646); Wing H3728. Source ID: `arber-stationers-bsoc-petition-1646-hunscott`.
[^tna-e179]: The National Archives, Kew, E179 series, City of London assessments under the 1660-1661 Free and Voluntary Present (13 Car. II, royal assent 8 July 1661); specific roll for Castle Baynard ward and St Augustine Watling Street not yet retrieved at image level. Source ID: `tna-e179-1661-london-poll-tax-deferred`.
[^harvey-1640]: W. J. Harvey, ed., *List of the Principal Inhabitants of the City of London, 1640, from Returns Made by the Aldermen of the Several Wards* (London, 1886; reprinted British Library Historical Print Editions, 2011); original Lambeth Palace Library MS. 272. Full text not yet retrieved online. Source ID: `bho-1640-principal-inhabitants-london-deferred`.
[^st-augustine-register]: Parish register, St Augustine Watling Street, City of London, London Metropolitan Archives P69/AUG; christening images 31281_a101009-00022 through 31281_a101009-00030 (1595-1610) and burial images 31281_a101009-00121 through 31281_a101009-00130 (1599-1612); user-supplied transcriptions in working packet v13 sections 14-17. Source ID: `lma-st-augustine-watling-register-candidate-d-images`.
[^st-magnus-1611]: Parish register, St Magnus the Martyr, City of London, marriage register; user-supplied image 31281_a101911-00014; Robert Gourney of St Augustine in Watling Street married Anne Morris of St Michael in the Querne by licence, 4 April 1611. Source ID: `lma-st-magnus-martyr-register-candidate-d-images`.
[^st-stephen-coleman-street]: FamilySearch indexed entries, England Births and Christenings 1538-1975, William Gurney + Tamazin christenings at St Stephen Coleman Street, London: Fotheza 19 January 1626, Adeall 2 April 1628, Susanna 23 July 1630, Marke 17 January 1636; no Sarah/Mary/Richard/John/Peter set; no demonstrated link to Robert of Old Change. Source ID: `fs-england-births-christenings`.
[^fs-john-mary-london]: FamilySearch records search, surname Gurney, given name John, spouse given name Mary, marriage 1620-1640, place London/England, returned 211 hits; no London-parish John Gurney + Mary marriage in window; closest John Gurney + Mary Marsh marriage 6 November 1632 at Eythorne, Kent, with son John baptized Eythorne 13 May 1638. Source ID: `fs-england-births-christenings`.
[^anne-gurney-search]: FamilySearch records search, Anne Gurney 1625-1645 London-area marriages and burials; no clear Anne-of-Robert candidate; weak lead An Gurney + George Bucher marriage 27 April 1640, Essex; PCC Wills 1625-1670 search returned no Anne Gurney match. Source IDs: `fs-england-births-christenings`, `ancestry-pcc-wills-1384-1858` (existing source if applicable).
[^rollco-hanging-houghton]: ROLLCO Drapers' Company event DREW4827, 1654 apprenticeship, new apprentice Charles Gourney, father of apprentice John Gourney "gen, Hanging Holton N'hants"; parallel Clothworkers' event 1647 with same residence reading. Source ID: `rollco-drapers-gurney-old-change-cluster`.

## Cross-references

- Case-file summary: `research/case-files/john-gurney-case-file-v4.md` Section 8.4 (added by patchset v35).
- Research companion: `research/people/g13-john-gurney-fact-sheet.research.md` (London Drapers' Old Change discriminator).
- Place note: `research/places/city-of-london.md` (St Augustine Watling Street).
- Validation notes: `sources/validations/bho-london-inhabitants-st-augustine-1638.md`, `sources/validations/rollco-drapers-gurney-old-change-cluster.md`, `sources/validations/rollco-stationers-hunscott-cluster.md`, `sources/validations/rollco-stationers-gurney-1613-1626.md`.
```

### 4.2 Replace `research/places/city-of-london.md` St Augustine narrative block

Replace the existing "St Augustine John Gurney and Haberdashers' Gournay charity" section (lines 3-9 plus footnotes 11) with this expanded version. Preserve all subsequent content including the `GENERATED:PLACE-REGISTRY` block.

```markdown
# City of London, England

### St Augustine Watling Street and Old Change - Robert and John Gurney

St Augustine Watling Street stood at the corner of Watling Street and Old Change in the City of London. Old Change ran from Cheapside to Knightrider Street; the parish was destroyed in the Great Fire 1666 and rebuilt by Wren, then united with St Faith under St Paul's in 1670 and ultimately united with St Mary le Bow in 1954. The 1638 T. C. Dale return surveyed by British History Online lists the parish's rents and tithe assessment in three sections (MS. 67, MS. 67a, MS. 68) totalling £1,700 yielding £233 5s tithe at 2/9 in the pound.[^bho-1638-place]

Robert Gourney was admitted to the Drapers' Company by servitude on 16 December 1581 under master Robert Furnes, already styled "Tailor, Old Change" at admission, and worked as a Drapers' master in roughly 14 apprenticeship- and freedom-master events between 1597 and 1622 at Old Change. He married Anne Morris of St Michael in the Querne by licence at St Magnus the Martyr on 4 April 1611, after having three children of an earlier marriage baptized at St Augustine in the 1590s (John 1595/6, Mary 1597/8, and a stillborn son 1601). His 1625 Archdeaconry of London will places his dwelling and shop in Old Change and gives the lower commercial portion to his son John Gurney.[^rollco-1581-place][^acl-1625-place]

John Gurney, son of Robert, was admitted to the Drapers' Company by redemption on 11 February 1623/4 (a non-patrimony path that requires explanation since Robert was a Drapers' freeman since 1581) and appears as a Drapers' apprenticeship master on 3 November 1630, binding Henry Smith of Kilton, Suffolk, for seven years. In 1638 the St Augustine rents return lists one John Gurney at £10 in MS. 67a; on MS. p. 68 of the same return Joseph Huntscott (= Joseph Henscott, the Stationer named in Robert's will as overseer) appears at £12, confirming continued parish-network presence of the same circle 13 years after Robert's death. Boyd's Inhabitants of London card for John Gurny of S Augustine also carries an unverified 1661 Old Change poll-tax reading, which if confirmed at image level would extend the household's London presence well past the colonial-emigration horizon.[^rollco-1630-place][^bho-1638-place][^boyd-card-place]

This Old Change household is the Candidate D cluster of the John Gurney case. Depth-of-detail analysis is held in `research/people/john-gurney-candidate-d.md`; the case-file summary is at `research/case-files/john-gurney-case-file-v4.md` Section 8.4.

### Haberdashers' Gournay charity

A later Charity Commission report on the Haberdashers' Company describes "Gournay's Charity," a loan charity arising from Richard Gournay's gift of 300 pounds, with annual interest intended for the poor of the Company, Christ's Hospital, and a poor scholar studying divinity at Oxford or Cambridge. The report says the money was no longer lent at interest and had been represented by a nominal stock appropriation producing 15 pounds per year. The Richard Gournay charity is not yet tied to the direct line, but it is useful London mercantile/civic context for the broader surname network and should remain visible as a lead.[^haberdashers-gournay-charity]

[^bho-1638-place]: T. C. Dale, "Inhabitants of London in 1638: St. Augustine," in *The Inhabitants of London in 1638* (Society of Genealogists, 1931), British History Online, https://www.british-history.ac.uk/no-series/london-inhabitants/1638/pp34-35; £1,700 total assessed yielding £233 5s tithe at 2/9 per £; three sections MS. 67, MS. 67a, MS. 68; John Gurney in MS. 67a at £10; Joseph Huntscott in MS. p. 68 at £12. Source ID: `bho-london-inhabitants-st-augustine-1638`.
[^rollco-1581-place]: ROLLCO Drapers' Company event DREW4826, freedom by servitude, 16 December 1581, new freeman Robert Gourney "Tailor, Old Change", master Robert Furnes. Source ID: `rollco-drapers-gurney-old-change-cluster`.
[^acl-1625-place]: Robert Gurney, citizen and draper of London, will written 18 January 1621/2, proved 23 September 1625, Archdeaconry Court of London. Source ID: `acl-robert-gurney-will-1625`.
[^rollco-1630-place]: ROLLCO Drapers' Company event DREW5638 (1623/4 freedom by redemption, John Gurney new freeman with Robert Gurney as father) and DRLL2060 (3 November 1630 apprenticeship of Henry Smith of Kilton Suffolk to John Gurney, 7-year bond). Source ID: `rollco-drapers-gurney-old-change-cluster`.
[^boyd-card-place]: Findmypast Boyd's Inhabitants of London card `GBOR/BIL/SOG59/0240`, John Gurny of S Augustine, free-note line reading "1661 poll tax [unclear] Old Change    1638 rent £10". Source ID: `findmypast-boyds-inhabitants-london-candidate-d-gurney-cards`.
[^haberdashers-gournay-charity]: "Report on the Charities of the Haberdashers' Company: Part I," *City of London Livery Companies Commission*, vol. 4, British History Online, https://www.british-history.ac.uk/livery-companies-commission/vol4/pp420-456#h3-s47. Source ID: `bho-livery-haberdashers-gournay-charity`.

<!-- GENERATED:PLACE-REGISTRY:START -->
## Place registry

- `placeId`: `place-city-of-london-england`
- Short description: Historic commercial site
- Place type: locality
- Aliases: City of London
- Coordinate: 51.51389, -0.08611 (exact)
- Roles: landholding / property reference, individual geography
- Site name: St Benet Fink
- Detail: City of London commercial context linked to St Benet Fink parish and the La Selde Coronata warehouse tradition.
- Current-site status: site only — St Benet Fink church is lost; the historic site lies within the modern Bank of England east-wing area.
- Links: [Reference page](https://en.wikipedia.org/wiki/St_Benet_Fink) · [St Benet Fink (historic image)](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Benet_fink_godwin.jpg/250px-Benet_fink_godwin.jpg)

### Linked ancestors

- G14 Francis Gurney — landholding / property reference, individual geography
- G23 Sir John Gurney, Knt. (d.1408) — Collateral — landholding / property reference, individual geography

### Review notes

- City-level record aggregates more than one London sub-site; keep the narrative file for separation.

<!-- GENERATED:PLACE-REGISTRY:END -->
```

### 4.3 Update `research/people/g13-john-gurney-fact-sheet.research.md`

Replace the existing "London St Augustine same-name lead, 1638" subsection (lines 403-407 inclusive, including the heading) with this expanded section. Keep all surrounding content and footnotes intact, and keep the `[^london-st-augustine-1638]` definition where it lives now (line 427).

```markdown
### London Drapers' Old Change discriminator (Candidate D)

The Old Change cluster surfaced from a 2026-05 working pass through Boyd's Inhabitants cards, the ROLLCO Drapers' Company event corpus, and Robert Gurney's 1625 Archdeaconry of London will. It is held as Candidate D of the John Gurney case and is documented in depth in `research/people/john-gurney-candidate-d.md`.

The cluster's anchor is Robert Gurney, citizen and draper of London, tailor at Old Change, freed of the Drapers' Company by servitude on 16 December 1581 under master Robert Furnes (ROLLCO DREW4826), and active as Drapers' master across roughly 14 events 1597-1622. His will of 1621/2 was proved 23 September 1625 by his son John Gurney as sole executor; the will placed Robert's dwelling and shop in Old Change and named Anne (Morris) as wife/widow-beneficiary and Joseph Henscott Stationer and Thomas Dunnell brother-in-law as overseers.[^candidate-d-acl-will][^candidate-d-rollco-1581]

John Gurney, son of Robert, was admitted to the Drapers' Company by redemption on 11 February 1623/4 (ROLLCO DREW5638, with Robert as father of freeman in the same event row), and appears as a Drapers' apprenticeship master on 3 November 1630 (ROLLCO DRLL2060) binding Henry Smith of Kilton, Suffolk, for seven years. Henry Smith does not surface as a freed Drapers' Smith 1635-1645 under John Gurney or any other master, and no Drapers' Turnover event for any Gurney 1620-1670 has been recorded. The Drapers' freedom-by-redemption pathway (rather than patrimony) is anomalous since Robert was a Drapers' freeman from 1581; the working hypothesis (H-D1) is that John had earlier been bound to a different company, possibly the Stationers' apprentice "John Gurney" bound to master James Boler on 25 March 1613 (ROLLCO STMM8981) for whom no Stationers' freedom is recorded.[^candidate-d-rollco-1624][^candidate-d-rollco-1630][^candidate-d-stationers-1613]

The 1638 London Inhabitants return for St Augustine lists one John Gurney at £10 in MS. 67a (rents/tithe assessment, £1,700 total at 2/9 per £). On MS. p. 68 of the same return, Joseph Huntscott appears at £12. Joseph Huntscott is the same Joseph Hunscott who was an active Stationers' apprenticeship master 1612-1646 with a son John admitted Stationer 1641, and the same Joseph Hunscot who published the 1646 royalist Wing H3728 petition; he was the Henscott named in Robert Gurney's 1625 will. The 1638 entry therefore points to continuation of the Old Change Gurney - Hunscott will-network across the 13 years after Robert's death.[^candidate-d-bho-1638][^candidate-d-hunscott]

The case-file Section 8.4 summary holds the tight version. The substantive next moves are: (1) the 1661 City of London poll-tax record at TNA E179 that Boyd's card cues as "1661 poll tax... Old Change", which if confirmed at image level would essentially eliminate Candidate D as the colonial John; (2) the 1640 Harvey Principal Inhabitants list at Lambeth MS. 272; (3) the Arber Stationers' Registers volume 3 raw entry for the 25 March 1613 binding to James Boler, which may name John's father; (4) walks through the LMA P69/AUG St Augustine vestry, churchwardens', and rate books 1625-1665; (5) Archdeaconry and Commissary of London admon/will indexes 1625-1670 for Anne Gurney widow and any London John Gurney draper/tailor.

[^candidate-d-acl-will]: Robert Gurney, citizen and draper of London, will written 18 January 1621/2, proved 23 September 1625, Archdeaconry Court of London. Source ID: `acl-robert-gurney-will-1625`.
[^candidate-d-rollco-1581]: ROLLCO Drapers' Company event DREW4826, 16 December 1581 freedom by servitude, new freeman Robert Gourney "Tailor, Old Change", master Robert Furnes. Source ID: `rollco-drapers-gurney-old-change-cluster`.
[^candidate-d-rollco-1624]: ROLLCO Drapers' Company event DREW5638, 11 February 1623/4 freedom by redemption, new freeman John Gurney, father of freeman Robert Gurney. Source ID: `rollco-drapers-gurney-old-change-cluster`.
[^candidate-d-rollco-1630]: ROLLCO Drapers' Company event DRLL2060, 3 November 1630 apprenticeship, master John Gurney, new apprentice Henry Smith, father Thomas Smith yeoman (deceased) of Kilton Suffolk, 7-year bond. Source ID: `rollco-drapers-gurney-old-change-cluster`.
[^candidate-d-stationers-1613]: ROLLCO Stationers' Company event STMM8981, 25 March 1613 apprenticeship, master James Boler Co Stationer, new apprentice John Gurney, reference ST/1:0812; no father recorded; no subsequent Stationers' freedom record. Source ID: `rollco-stationers-gurney-1613-1626`.
[^candidate-d-bho-1638]: T. C. Dale, "Inhabitants of London in 1638: St. Augustine," British History Online; John Gurney £10 in MS. 67a between Christopher Hunlock £2 and George Browne £10; Joseph Huntscott £12 on MS. p. 68. Source ID: `bho-london-inhabitants-st-augustine-1638`.
[^candidate-d-hunscott]: ROLLCO Stationers' Company event corpus for Joseph Hunscott 1612-1646; and Joseph Hunscot, *The Humble Petition and Information of Joseph Hunscot Stationer* (London, 1646), Wing H3728. Source IDs: `rollco-stationers-hunscott-cluster`, `arber-stationers-bsoc-petition-1646-hunscott`.
```

Also append the following row to the existing Research Companion "Sources Consulted" table (right before the Negative Results section):

```markdown
| `rollco-drapers-gurney-old-change-cluster` | Full Drapers' Gurney event corpus 1581-1654 | `sources/validations/rollco-drapers-gurney-old-change-cluster.md` |
| `rollco-stationers-hunscott-cluster` | Joseph Hunscott Stationers' apprenticeship master 1612-1646 and son John 1641 | `sources/validations/rollco-stationers-hunscott-cluster.md` |
| `rollco-stationers-gurney-1613-1626` | 1613 John Gurney binding to James Boler; 1616-1626 separate Robert Gurney apprenticeship | `sources/validations/rollco-stationers-gurney-1613-1626.md` |
| `arber-stationers-bsoc-petition-1646-hunscott` | Wing H3728 1646 Joseph Hunscot petition - identity bridge for the will overseer | `sources/validations/arber-stationers-bsoc-petition-1646-hunscott.md` |
| `tna-e179-1661-london-poll-tax-deferred` | Deferred image-pull target for the 1661 Old Change poll-tax cue | `sources/validations/tna-e179-1661-london-poll-tax-deferred.md` |
| `bho-1640-principal-inhabitants-london-deferred` | Deferred image-pull target for the 1640 W. J. Harvey Principal Inhabitants list | `sources/validations/bho-1640-principal-inhabitants-london-deferred.md` |
| `arber-stationers-registers-1554-1640-deferred` | Deferred image-pull target for the 1613 John Gurney binding raw entry | `sources/validations/arber-stationers-registers-1554-1640-deferred.md` |
```

## 5. Audit checklist

Before declaring this patchset applied, confirm each of the following findings has been recorded into research or sources (not lost):

- BHO 1638 St Augustine John Gurney £10 in MS. 67a between Christopher Hunlock £2 and George Browne £10. ✅ `bho-london-inhabitants-st-augustine-1638` corpus + `research/people/john-gurney-candidate-d.md`.
- BHO 1638 St Augustine Joseph Huntscott £12 on MS. p. 68 (= Henscott of 1625 will). ✅ corpus + Candidate D topic file + place file.
- BHO 1638 St Augustine total £1,700 at 2/9 per £ yielding £233 5s tithe. ✅ corpus.
- ROLLCO 1581 Robert Gourney freedom by servitude under master Robert Furnes, already "Tailor, Old Change". ✅ corpus + topic file + place file + research companion.
- ROLLCO 1597 Robert Gurney Freedom Master. ✅ corpus.
- ROLLCO 1604 Robert Gurney Witness with "Tailor, Old Change" explicit; Richard Sebrineke new freeman. ✅ corpus + topic file.
- ROLLCO 1617 Robert Gurney master, John Lee of Shenley Bucks 7-yr apprentice. ✅ corpus + topic file.
- ROLLCO 1622 Robert Gurney master, William Holdsworth of Sowerby Bridge Yorks 7-yr apprentice. ✅ corpus + topic file.
- ROLLCO 1624 John freedom by redemption + Robert father same event. ✅ corpus + topic file + research companion.
- ROLLCO 1629 Marten Backhurst freedom by servitude under Robert (posthumous record). ✅ corpus + topic file.
- ROLLCO 1630 John Gurney master, Henry Smith of Kilton Suffolk 7-yr apprentice. ✅ corpus + topic file + research companion.
- ROLLCO 1654 John Gourney "gen, Hanging Holton Northants" - separate gentry comparator. ✅ corpus + topic file.
- ROLLCO Stationers' 1613 John Gurney apprentice to James Boler (no later freedom). ✅ new corpus + topic file + research companion + new validation.
- ROLLCO Stationers' 1616-1626 Robert Gurney apprentice/freedom under William Wrench (separate Robert). ✅ new corpus + topic file + new validation.
- Joseph Hunscott identity bridge Henscott = Huntscott = Hunscott; Wing H3728 petition. ✅ new corpus + new sources + topic file + research companion.
- Henry Smith 1637-1640 Drapers' freedom not found under John Gurney; no Drapers' Turnover events for Gurney 1620-1670. ✅ topic file.
- PCC Wills 1625-1670 Anne Gurney null result. ✅ topic file next-steps + research companion footnotes.
- An Gurney + George Bucher 27 April 1640 Essex weak Anne remarriage lead. ✅ topic file footnote.
- H-D1 redemption-via-Stationers hypothesis articulated. ✅ topic file dedicated section.
- 1604 Old Change identification pushes back from 1617 (already known) to 1604 and 1581. ✅ topic file + place file.
- "Second Robert" puzzle resolved. ✅ Stationers' corpus + Candidate D topic file.
- 1661 Old Change poll-tax cue captured as deferred target. ✅ new source + new validation + topic file next-steps.
- 1640 Harvey Principal Inhabitants captured as deferred target. ✅ new source + new validation + topic file next-steps.
- Arber Stationers' Registers captured as deferred target. ✅ new source + new validation + topic file next-steps.

## 6. Sibling patchset hand-off

This patchset stops at the topic file, research companion, place file, sources, validations, and deferred targets. The case-file Section 8.4 Candidate D subsection plus the Section 9 candidate-table row, Section 11 probability row, and Section 12 next-steps additions are handled in sibling patchset `v35-john-gurney-case-file-candidate-d-section-8.patchset.md`.
