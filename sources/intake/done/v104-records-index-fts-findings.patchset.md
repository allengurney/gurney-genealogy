**Done:** 2026-06-20 04:14 PT

# Patchset v104 — records-index & FTS findings (St Benet Fink children, Sarah Gurney's husband, Stephen Gurney inventory, medieval Gurney wills)

Four findings from the June 2026 authenticated FamilySearch pass (records-index search `/hr/v2/personas` + Full-Text Search, broad variant roots). All four assimilate into existing companion/place prose — no appended dated blocks. Leads L-109, L-149, L-124, L-68 are already updated directly in `research-leads.csv`; this patchset promotes the substance into the research layer.

**Source tracking:** all four use existing `sourceId`s already in `data/sources.json` — `fs-england-births-christenings` and `familysearch-fulltext-search`. No new `sourceId`, so no new `sources/validations/*.md` files. No rich (>150-word) primary extract here — the inventory transcript is garbled OCR and is cited at machine-transcript level, not promoted as corpus text — so no `sources/corpus_supplement/` writes.

---

## Item 1 — promote — Sarah Gurney's husband identified as Sion (Syon) Gurney of Earsham

**Destination:** `research/people/john-gurney-earsham-will-1638.md`

The Earsham file hypothesised Sarah Gurney's husband as the 1638 testator's son John. The FamilySearch index identifies him instead as a **Sion (Syon) Gurney of Earsham**: Sion Gurney christened 10 June 1677 at Earsham, parents Sion Gurney and Sarah. The Earsham Sion also appears with wife Ann (daughter Elizabeth 1663) and an Esther, so the household(s)/wife-sequence need the parish register.

### str_replace 1a — the reasoning clause

```
old_string:
and widow of an unidentified Gurney of this family (the 1638 testator's son John, b. after c. 1624, is chronologically exact and the natural candidate) — lived at Bungay
```

```
new_string:
and widow of **Sion (Syon) Gurney of Earsham**[^sarah-husband-sion-2026-06] — lived at Bungay
```

### str_replace 1b — add the footnote definition

```
old_string:
[^earsham-baptisms]: FindMyPast "Norfolk Baptisms," Earsham: John Gurney s. John (1635), John Gurney s. John (1636), Henry Gurney s. John (1638), and Susan Gurney dau. Sion (1638). Index level. Source ID: `findmypast-norfolk-baptisms-index`.
```

```
new_string:
[^earsham-baptisms]: FindMyPast "Norfolk Baptisms," Earsham: John Gurney s. John (1635), John Gurney s. John (1636), Henry Gurney s. John (1638), and Susan Gurney dau. Sion (1638). Index level. Source ID: `findmypast-norfolk-baptisms-index`.
[^sarah-husband-sion-2026-06]: FamilySearch, "England, Births and Christenings, 1538–1975": Sion Gurney christened 10 June 1677 at Earsham, Norfolk, parents Sion Gurney and Sarah — identifying Sarah Gurney's husband as Sion (Syon) Gurney of Earsham. The same Earsham Sion Gurney also appears with wife Ann (daughter Elizabeth christened 2 January 1663) and with an Esther, so the Earsham Sion household(s) and the wife sequence need the parish register to disentangle. The 1677 son Sion is the Lyon/Syon Gurney later of St Peter Parmentergate, Norwich (the Norwich Sion-Gurney family, baptisms 1706–1743). Index level. Source ID: `fs-england-births-christenings`.
```

### str_replace 1c — Open Question 2

```
old_string:
Remaining: which Gurney was Sarah's husband (the 1638 testator's son John, b. after c. 1624, is the natural candidate — test against Bungay/Earsham parish registers); James Adams's probate clause (the page after image 202); and a **full Latin transcription of the 1719 Syon Gurney admission**
```

```
new_string:
Remaining: disentangle the Earsham Sion-Gurney household(s) behind Sarah's now-identified husband **Sion (Syon) Gurney** (indexed with wives Ann, Sarah, and Esther — the parish register is needed for the wife sequence and to confirm which Sion married Sarah); James Adams's probate clause (the page after image 202); and a **full Latin transcription of the 1719 Syon Gurney admission**
```

---

## Item 2 — promote — FS index confirms Bernau's St Benet Fink children list; correct the erroneous Harleian citation

**Destination:** `research/people/g14-francis-gurney-fact-sheet.research.md`

The FamilySearch index independently confirms Bernau 1913's child list over the fact sheet's divergent one, resolving the open item in Bernau's favour at index level. Separately, the file's "Harleian Society transcript of St Benet Fink (vol. 44, Collins 1914)" citation is wrong — no Harleian transcript of St Benet Fink exists (Harleian Register vols 44–45 are St Mary le Bow / All Hallows Honey Lane / St Pancras Soper Lane).

### str_replace 2a — children-list analysis conclusion

```
old_string:
The cumulative pattern is that Bernau, working from the St Benet Fink register c. 1913, extracted a different and better-documented list than the one currently presented. Resolution requires fresh examination of the St Benet Fink register or of the Harleian Society / Guildhall transcripts that index it.
```

```
new_string:
The cumulative pattern is that Bernau, working from the St Benet Fink register c. 1913, extracted a different and better-documented list than the one currently presented. An independent examination of the FamilySearch index (England, Births and Christenings, 1538–1975) **confirms Bernau's list over the current fact sheet's**: the index returns to Francis Gurney and Anne, at St Peter le Poer with St Benet Fink, **Dorothy (1619), Roger (1621), Frances (1625), Francis (1628), Lucretia (1630), Thomas (1636), and Margaret (1637)** — Bernau's names, not the fact sheet's Deborah/Elizabeth/Mary/Anne — resolving the divergence in Bernau's favour at index level. Full register confirmation (LMA P69/BEN1) remains the gold standard.[^st-benet-fink-index-2026-06]
```

### str_replace 2b — add the footnote definition

```
old_string:
[^fs-non-bernau]: [`fact-sheets/g14-francis-gurney-fact-sheet.md`](https://github.com/allengurney/gurney-genealogy/blob/main/fact-sheets/g14-francis-gurney-fact-sheet.md), children table.
```

```
new_string:
[^fs-non-bernau]: [`fact-sheets/g14-francis-gurney-fact-sheet.md`](https://github.com/allengurney/gurney-genealogy/blob/main/fact-sheets/g14-francis-gurney-fact-sheet.md), children table.
[^st-benet-fink-index-2026-06]: FamilySearch, "England, Births and Christenings, 1538–1975," children of Francis (Frauncis/Frances) Gurney/Gurnay/Gurnoy and Anne (Ann/Ane) at St Peter le Poer with St Benet Fink, London: Dorothy (2 March 1619), Roger (20 December 1621), Frances (18 January 1625), Francis (13 November 1628), Lucretia (28 October 1630), Thomas (19 April 1636), Margaret (28 July 1637). Independent index confirmation of Bernau 1913's list over the fact sheet's divergent names; full register confirmation (LMA P69/BEN1) outstanding. Source ID: `fs-england-births-christenings`.
```

### str_replace 2c — fix Harleian citation in "Analysis" open item

```
old_string:
Open item: pull the St Benet Fink parish register (LMA P69/BEN1/A/001 and /002) for baptisms 1619–1638 and reconcile. Harleian Society transcripts of St Benet Fink registers (vol. 44, ed. Francis Collins 1914) are the most accessible published index.
```

```
new_string:
Open item: pull the St Benet Fink parish register (LMA P69/BEN1/A/001 and /002) for baptisms 1619–1638 and reconcile against the FamilySearch index confirmation above. **There is no Harleian Society transcript of St Benet Fink** — Harleian Register vols 44–45 cover St Mary le Bow, All Hallows Honey Lane, and St Pancras Soper Lane, not Fink; the earlier "Harleian vol. 44, Collins 1914" attribution was an error. The reachable index is the FamilySearch / Ancestry parish index plus the LMA register itself.
```

### str_replace 2d — fix Harleian citation in "Open items specific to this source"

```
old_string:
2. Examine the St Benet Fink baptism register (LMA P69/BEN1/A/001 and /002) for 1619–1638 and reconcile Bernau's Dorothy/Roger/Frances/Francis/Lucretia/Thomas/Margaret/Anne/John list against the current fact sheet's list. The Harleian Society published transcript of St Benet Fink (vol. 44, 1914) is the likely reachable index.
```

```
new_string:
2. Examine the St Benet Fink baptism register (LMA P69/BEN1/A/001 and /002) for 1619–1638 and reconcile Bernau's Dorothy/Roger/Frances/Francis/Lucretia/Thomas/Margaret/Anne/John list against the current fact sheet's list. The FamilySearch index confirms Bernau's 1619–1637 names (see the children-list analysis above); **no Harleian Society transcript of St Benet Fink exists** (Harleian vols 44–45 are St Mary le Bow etc., not Fink), so the LMA register and the FS/Ancestry parish index are the reachable sources.
```

---

## Item 3 — promote — Stephen Gurney probate inventory, Norwich c. 1613–1619 (new comparator)

**Destination:** `research/people/g13-john-gurney-fact-sheet.research.md`

A new in-window Gurney decedent surfaced by the authenticated broad FTS sweep — added as a comparator at the head of the "Wider Norfolk and same-name Gurney records" section.

### str_replace 3a — add comparator paragraph after the section intro

```
old_string:
Same-name Gurney households and Norfolk records that surfaced during the origin campaign. Each is a comparator or elimination aid for the John Gurney problem, not the emigrant himself; full treatment of those with their own subjects lives on the linked subject files.
```

```
new_string:
Same-name Gurney households and Norfolk records that surfaced during the origin campaign. Each is a comparator or elimination aid for the John Gurney problem, not the emigrant himself; full treatment of those with their own subjects lives on the linked subject files.

**A Gurney probate inventory at Norwich, c. 1613–1619 — a Gurney decedent inside the origin window.** A probate inventory indexed under the extracted name "Septeph Gurney" — almost certainly **Stephen Gurney** — survives for Norwich, dated 1613–1619.[^stephen-gurney-inventory-2026-06] The transcript is a heavily garbled room-by-room household inventory (buttery, pantry, cupboards, beds, "at the Grange," a long table and forms), so the parish, the exact year, and whether the named Gurney is the decedent or an appraiser are not legible and require an image read. If it is a Gurney decedent's own inventory it is the first probate of a Gurney *of the emigrant's father/grandfather generation* found inside Norfolk, and it nuances the "no Gurney testator in the window" bounding result below — which rests on the Norwich Consistory *registered-copy will* registers and would not capture an inventory or an Archdeaconry-court estate. Most plausibly a Norwich-city Gurney (cf. the St Peter Parmentergate plebeian line), not yet tied to West Barsham or to Francis G14's East Dereham household.

[^stephen-gurney-inventory-2026-06]: FamilySearch Full-Text Search, "Norwich, Norfolk, England Probate 1613–1619," record/ark `3:1:S3HT-624X-58`, extracted name entity "Septeph Gurney" (probable OCR rendering of Stephen Gurney); England, Norfolk, Legal collection. Machine-transcript level; full-resolution image read pending. Source ID: `familysearch-fulltext-search`.
```

---

## Item 4 — promote — medieval Norwich Consistory Gurney wills reachable in FTS

**Destination:** `research/places/great-ellingham.md`

The mid-15th-century NCC Gurney wills the file catalogues at register/folio level ("neither will text has been read yet") are now reachable as FTS images, and a possibly-new name (Antonette Gurnee) surfaced — added to the medieval-wills section.

### str_replace 4a — extend the medieval-collateral paragraph

```
old_string:
With the 1454 Thomas, the 1465 Joan of Deopham, and John of Filby, they sketch a Gurnay collateral presence threaded across south-central and eastern Norfolk — Loddon, Heigham, Great Ellingham, Deopham, Filby — from the 1370s onward, well before the West Barsham line acquired Great Ellingham.
```

```
new_string:
With the 1454 Thomas, the 1465 Joan of Deopham, and John of Filby, they sketch a Gurnay collateral presence threaded across south-central and eastern Norfolk — Loddon, Heigham, Great Ellingham, Deopham, Filby — from the 1370s onward, well before the West Barsham line acquired Great Ellingham. Several of these mid-fifteenth-century Norwich Consistory Gurney wills are now reachable as images in FamilySearch Full-Text — the image-read step previously outstanding: an authenticated broad-variant sweep surfaces a **John Gurnee** will (1444–54, ark `3:1:3Q9M-CSND-39LW-3`), an **Antonette Gurnee** will (1454–64, ark `3:1:3Q9M-CSND-NTYT`), and two further **Gurne/Gurnee** wills (1444–54, arks `3:1:3Q9M-CSND-39LF-F` and `3:1:3Q9M-CSND-39L6-P`). The transcripts are court-hand salad, so matching a given ark to a specific catalogued testator (Aleyn 19, Cobald 55, or John of Filby) needs the image reads. "Antonette Gurnee" is not among the catalogued testators above and may be an additional fifteenth-century Norfolk Gurney — verify against the Index to Wills, Consistory Court of Norwich 1370–1550.[^medieval-gurney-wills-fts-2026-06]
```

### str_replace 4b — add the footnote definition

```
old_string:
Surfaced June 2026 via a film-scoped full-text sweep. The exact published title/editor of the calendar is unconfirmed; held at catalogue level. Source ID: `familysearch-fulltext-search`.
```

```
new_string:
Surfaced June 2026 via a film-scoped full-text sweep. The exact published title/editor of the calendar is unconfirmed; held at catalogue level. Source ID: `familysearch-fulltext-search`.
[^medieval-gurney-wills-fts-2026-06]: FamilySearch Full-Text Search, Norwich Consistory registered-copy will registers (England, Norfolk, Legal collection), authenticated broad-variant (`gurn*`/`gourn*`/`gorn*`) sweep, June 2026: John Gurnee will 1444–54 (ark `3:1:3Q9M-CSND-39LW-3`), Antonette Gurnee will 1454–64 (ark `3:1:3Q9M-CSND-NTYT`), Gurne/Gurnee wills 1444–54 (arks `3:1:3Q9M-CSND-39LF-F`, `3:1:3Q9M-CSND-39L6-P`). Court-hand transcripts; testator-to-register matching pending image reads. Source ID: `familysearch-fulltext-search`.
```

---

## Leads (already updated directly — recorded here for traceability)

- **L-109** — Sarah's husband = Sion Gurney (Item 1).
- **L-149** — FS index confirms Bernau's children list; no Harleian St Benet Fink transcript (Item 2).
- **L-124** — Stephen Gurney inventory, Norwich 1613–19, image read pending (Item 3).
- **L-68** — medieval NCC Gurney wills reachable in FTS; possible new name Antonette Gurnee (Item 4).
