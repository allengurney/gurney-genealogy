**Done:** 2026-06-23 07:12 PT

# Patchset v113 — thread wrap-up: fines regnal-year datings + Great Dunham/Bawdeswell register locations

Phase-1 patchset capturing the not-yet-promoted findings of the 2026-06-22 thread. The image-staging packets (32 Great Dunham, 33 Bawdeswell), the AALT-coverage note, the corpus-supplement datings, the Rye Part II local text, the new lead L-167, and all lead-CSV updates are **already in the repo** and are *not* repeated here. This patchset only lands the remaining promotions: the fines regnal-year datings into the subject companions, the Great Dunham/Bawdeswell register location + Bawdeswell marriage-gap finding into the G13 companion, and the supporting source/validation updates.

**Source basis (all already in repo):** regnal years recovered from Walter Rye's reign sub-headers in the Part II text now held at `sources/corpus/rye-feet-of-fines-norfolk-part2.txt`; datings transcribed in `sources/corpus_supplement/norfolk-feet-of-fines-gurnay-entries-rye.md`. Register findings from FamilySearch collection 1416598 (sourceId `fs-england-norfolk-parish-registers-1510-1997`, already in `data/sources.json`). No new sourceIds.

Datings recovered: #64 = 6 Hen IV (1405); #200 = 23 Hen VI (1444/45); #329 = 8 Edw III (1334/35); #432 = 9 Edw III (1335/36); #489 = 9 Edw II (1315/16).

---

## Item 1 — `data/sources.json`: update the Rye source entry (Part II text now local; regnal years recovered)

**Outcome: promote.** Two `str_replace` edits in `data/sources.json`, in the `rye-feet-of-fines-norfolk` entry. (corpusPath change does not alter any sourceId, so `data/indexes/source-ids.csv` needs no regeneration.)

### 1a. Point corpusStatus/corpusPath at the local Part II text

**str_replace — old_string:**
```
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/rye-feet-of-fines-norfolk.md",
```

**new_string:**
```
      "corpusStatus": "extract",
      "corpusPath": "sources/corpus/rye-feet-of-fines-norfolk-part2.txt",
      "mediaPath": null,
      "validationPath": "sources/validations/rye-feet-of-fines-norfolk.md",
```

### 1b. Append the local-text + regnal-year note to the entry's `notes`

**str_replace — old_string:**
```
consult AALT CP 25/1 scans for the manuscript image and exact file/number."
```

**new_string:**
```
consult AALT CP 25/1 scans for the manuscript image and exact file/number. The full Part II OCR text is now held locally at sources/corpus/rye-feet-of-fines-norfolk-part2.txt. Although the calendar is arranged by hundred/place, every entry sits under a regnal-year sub-header, so a fine's date is recoverable without the manuscript image; regnal years read 2026-06: entry 64 = 6 Hen IV (1405); 200 = 23 Hen VI (1444/45); 329 = 8 Edw III (1334/35); 432 = 9 Edw III (1335/36); 489 = 9 Edw II (1315/16)."
```

---

## Item 2 — `sources/validations/rye-feet-of-fines-norfolk.md`: record the recovered regnal years + local Part II text

**Outcome: promote.** One `str_replace`.

**old_string:**
```
**Scope and method.** Calendar abstracts only (not the Latin fine text or the foot itself); brief one-line entries with party names, lands, and an entry number per reign section. The exact TNA CP 25/1 file/number and the regnal date require Rye's section apparatus and/or the AALT image scans.
```

**new_string:**
```
**Scope and method.** Calendar abstracts only (not the Latin fine text or the foot itself); brief one-line entries with party names, lands, and an entry number per reign section. The full Part II OCR text is now held locally at [`sources/corpus/rye-feet-of-fines-norfolk-part2.txt`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus/rye-feet-of-fines-norfolk-part2.txt). The exact TNA CP 25/1 file/number still requires the AALT image scans, but each entry's **regnal date is recoverable from its nearest preceding reign sub-header** — so the AALT image is no longer required merely to date a fine. Regnal years read 2026-06: #64 = 6 Hen IV (1405); #200 = 23 Hen VI (1444/45); #329 = 8 Edw III (1334/35); #432 = 9 Edw III (1335/36); #489 = 9 Edw II (1315/16).
```

---

## Item 3 — G20 Thomas Gournay II companion: date fine #200 (1444/45) and place him in the Fastolf–Paston affinity (L-167)

**Outcome: promote.** Two `str_replace` edits in `research/people/g20-thomas-gournay-ii-fact-sheet.research.md`.

### 3a. Update the landholding row (replace the "regnal year unread" caveat with the dated reading)

**old_string:**
```
The rank "esquire," the named wife **Margaret**, and the West-Norfolk cluster on the West-Barsham/Harpley axis fit **Thomas II and Margaret Jerningham**; the fine's regnal year is unread, so the identification is provisional and a 14th-century Thomas namesake is not fully excluded (lead L-164).[^rye-thomas-margaret-2026] |
```

**new_string:**
```
The rank "esquire," the named wife **Margaret**, and the West-Norfolk cluster on the West-Barsham/Harpley axis fit **Thomas II and Margaret Jerningham**; the fine is now dated **23 Henry VI (1444/45)** from Rye's reign sub-header, which fits Thomas II's mid-15th-century floruit and effectively excludes a 14th-century namesake (Thomas Gournay I, G21, was militarily active in 1418 and so elderly or dead by 1444). The querents **Nicholas Bokkyng and John Aleyn of Castleacre** recur as professional feoffees throughout the surrounding 23 Henry VI Norfolk fines (the Oldhall, Fastolf, Yelverton, Heydon, Inglose and Calthorp circle), so the concord is an enfeoffment-to-use settling the Gurnay West-Norfolk manors — placing Thomas II squarely within the **Fastolf–Paston gentry affinity** already visible elsewhere in the line (the Harling-retinue and Heylesdon–Fastolf threads), lead L-167 (and L-164).[^rye-thomas-margaret-2026] |
```

### 3b. Extend the footnote to record the regnal-year source

**old_string:**
```
[^rye-thomas-margaret-2026]: Walter Rye, *A Short Calendar of the Feet of Fines for Norfolk*, Part II (Internet Archive [`ashortcalendarf00ryegoog`](https://archive.org/details/ashortcalendarf00ryegoog)), entry 200; harvest at [`sources/corpus_supplement/norfolk-feet-of-fines-gurnay-entries-rye.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/norfolk-feet-of-fines-gurnay-entries-rye.md). Underlying TNA CP 25/1 (Norfolk), AALT. Source ID: `rye-feet-of-fines-norfolk`.
```

**new_string:**
```
[^rye-thomas-margaret-2026]: Walter Rye, *A Short Calendar of the Feet of Fines for Norfolk*, Part II (Internet Archive [`ashortcalendarf00ryegoog`](https://archive.org/details/ashortcalendarf00ryegoog); full OCR text at [`sources/corpus/rye-feet-of-fines-norfolk-part2.txt`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus/rye-feet-of-fines-norfolk-part2.txt)), entry 200, under the reign sub-header **23 Henry VI (1444/45)**; the surrounding 22nd–24th Henry VI Norfolk fines supply the Bokkyng/Aleyn feoffee and Fastolf-circle context. Harvest and recovered regnal years at [`sources/corpus_supplement/norfolk-feet-of-fines-gurnay-entries-rye.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/norfolk-feet-of-fines-gurnay-entries-rye.md). Underlying TNA CP 25/1 (Norfolk), AALT. Source ID: `rye-feet-of-fines-norfolk`.
```

---

## Item 4 — G13 John companion: Great Dunham/Bawdeswell registers located; Bawdeswell marriage-gap finding

**Outcome: promote.** Assimilate into the existing Peter-Wales/Mary-Wales paragraph (replace the closing clause) and add the supporting footnote, in `research/people/g13-john-gurney-fact-sheet.research.md`.

### 4a. Replace the paragraph's closing clause with the register-location + gap finding

**old_string:**
```
so only the Great Dunham / Bawdeswell **parish-register image** can resolve it (lead L-161).
```

**new_string:**
```
so only the Great Dunham / Bawdeswell **parish-register image** can resolve it. Both registers have now been read where they survive, and neither yields the marriage. The **Great Dunham** composite register's continuous **1623–1633 marriage run contains no Mary Wales, no Wales-family, and no Gurney-form marriage** (high-confidence read of the core 1623–1632 pages and the surrounding buffer). The **Bawdeswell** register is a disordered composite whose surviving **marriage entries run 1562–1582 and then resume only in 1709** — so no Bawdeswell marriage survives for the 1620s–30s. The local-marriage route is therefore exhausted (a clean Great Dunham negative plus a genuine Bawdeswell record gap), and the candidacy now rests on a **disappearance test that is so far inconclusive**: a first read of the Bawdeswell baptisms ~1619–1631 found no secure Wales-family or Gurney-form entry and no post-1627 Mary-as-mother, but it did not image-confirm even the indexed Ann Wales (1618) and Peter Wales (1629) baptisms — faded 1617/18 pages and a film-waypoint/date-range mismatch leave the Wales household's Bawdeswell presence not yet manuscript-confirmed, and no 1627–1635 burial run has been read. Resolving the exact film waypoints for the indexed Ann (1618) and Peter (1629) baptisms, extending the baptism read to 1635, and staging the burials are the open steps (lead L-161).[^bawdeswell-register-gap-2026-06]
```

### 4b. Add the footnote (place immediately after the existing `[^peter-tracer-2026-06]` footnote definition)

**str_replace — old_string:** (the tail of the `[^peter-tracer-2026-06]` footnote)
```
so the emigrant's marriage (and any Mary Wales marriage there) simply is not indexed. Source IDs: `fs-england-births-christenings`; `findmypast-norfolk-banns-marriages-index`; `norfolk-wills-probate-index-1371-1858`. See lead L-161.
```

**new_string:**
```
so the emigrant's marriage (and any Mary Wales marriage there) simply is not indexed. Source IDs: `fs-england-births-christenings`; `findmypast-norfolk-banns-marriages-index`; `norfolk-wills-probate-index-1371-1858`. See lead L-161.

[^bawdeswell-register-gap-2026-06]: FamilySearch, "England, Norfolk, Parish Registers (County Record Office), 1510–1997" (collection 1416598; Norfolk Record Office originals). **Great Dunham** composite register "Baptisms, Marriages, Burials," 1538–1658: the continuous marriage section was read for 1623–1633 (decisive 1623–1632 window on images 48–49, with the pre- and post-window buffer); no bride or groom surnamed Wales/Wallis/Walys/Wayles and no Gurney/Gurnay/Gourney/Gournay/Gurnie-form surname appears — confidence ~95% (readable comparators include Hilary Bucknam × Alicia Bradnam 1627 and Robert Barker × Brigetta 1628). **Bawdeswell** composite register, 1557–1723: surviving marriage entries run 1562–1582 then resume only in 1709 — no marriages for the 1583–1708 window (the book is disordered: faded, tight-bound, sections interleaved out of chronological order). The Bawdeswell baptism read (~1619–1631) was partial: low-resolution, faded and gutter-damaged pages, with the date-window stopping near 1631; it did not securely image the indexed Ann (1618)/Peter (1629) Wales baptisms, so those need a film-waypoint-precise re-pull before the household's Bawdeswell presence is manuscript-confirmed. Both reads June 2026 (Packet-32 and Packet-33 reports under `sources/intake/paleography-staging/done/`). A parallel attempt to locate a will of Peter Wales — which might name daughter Mary's married surname — via TNA Discovery was blocked by an access restriction and deferred. Source ID: `fs-england-norfolk-parish-registers-1510-1997`. See lead L-161.
```

---

## Item 5 — G22 companion: fold the recovered regnal years and the #329 correction into the feet-of-fines harvest paragraph

**Outcome: promote.** One `str_replace` in `research/people/g22-robert-gournay-fact-sheet.research.md` (the "variant-spelling entries" sentence of the harvest paragraph). The dating that #329 = 1334/35 **excludes** the 15th-century Paston "William Gurney of Tharston," materially weakening lead L-162.

**old_string:**
```
Two variant-spelling entries are flagged for image verification as possible Gournays: **"Wm. Germye, Chivaler" of Tharston** (Pt II #329 — possibly the Paston "William Gurney esq. of Tharston," lead L-162) and **"Rad. Gereneye," parson, of the manors of Saxthorp and Swatthing** (Pt II #432, lead L-163); "Geney" of Gunton and "Gene" of Tilney were read and excluded as distinct surnames.[^rye-fines-harvest-2026-06]
```

**new_string:**
```
Two variant-spelling entries flagged as possible Gournays are now **dated from Rye's reign sub-headers**, which sharpens both: **"Wm. Germye, Chivaler" of Tharston** (Pt II #329) falls in **8 Edward III (1334/35)** — more than a century before the 15th-century Paston "William Gurney esq. of Tharston," so #329 cannot be that man; with the early date, knightly rank, and the "Germye" spelling, it most likely belongs to the distinct Norfolk **Germy(e)** family of Tharston rather than the Gournays, substantially weakening lead L-162. **"Rad. Gereneye," parson, of the manors of Saxthorp and Swatthing** (Pt II #432) falls in **9 Edward III (1335/36)**; the spelling does not map cleanly onto the Gournay head-forms, so the Saxthorpe tie is the only Gournay signal and the identification stays uncertain (lead L-163). The direct-line and clerical Gurnay fines are likewise now dated — Robert of Parva Cressingham (#64) to 6 Henry IV (1405), Thomas Gurnay Armiger & Margaret (#200) to 23 Henry VI (1444/45), and John Gurnay rector of Harpley (#489) to 9 Edward II (1315/16). "Geney" of Gunton and "Gene" of Tilney were read and excluded as distinct surnames.[^rye-fines-harvest-2026-06]
```

---

## Item 6 — Medieval-soldier-database topic: record the AALT coverage gap (collateral; low priority)

**Outcome: promote.** Two `str_replace` edits in `research/topics/gurney-medieval-soldier-database.md`, noting that the membrane reads cannot be done via AALT (a coverage gap, not connectivity). These are collateral same-name soldiers; the note prevents a future re-attempt assuming AALT holds the pieces.

### 6a. Richard Gurney esq. row (L-72)

**old_string:**
```
The membrane-neighbour read (L-72) is held at **low priority**. |
```

**new_string:**
```
The membrane-neighbour read (L-72) is held at **low priority** — and AALT does **not** digitise E101 pieces 40 or 41 (its E101 holdings are only nos. 79–83, 249–255, 349–355, 458–504, verified 2026-06-22), so E101/40/34 m1 (and the stray E101/41/5 m5) are image-only at TNA Kew, not an online pull. |
```

### 6b. John Gurnay archer row (L-154)

**old_string:**
```
so this is a same-name comparator, not a direct-line candidate (L-154, low priority). |
```

**new_string:**
```
so this is a same-name comparator, not a direct-line candidate (L-154, low priority). The membrane (E101/40/39 m2) is not on AALT — piece 40 is outside AALT's digitised E101 ranges — so it is image-only at TNA Kew. |
```

---

## Item 7 — media disposition: move the Packet 32/33 masters out of staging into `sources/media/_local/`

**Outcome: promote.** File operations (no prose). The FamilySearch register masters must not sit committed in the transient `images/` staging area; move them to the gitignored per-source `_local/` folder with a committed stub.

1. **Create** `sources/media/fs-england-norfolk-parish-registers-1510-1997/_local/` (the `_local/` bytes are gitignored; its `README.md` is committed).
2. **Move** all JPGs from `sources/intake/paleography-staging/images/packet-32-great-dunham-marriages/` (13 files, `gd-img-0NN.jpg`) and `sources/intake/paleography-staging/images/packet-33-bawdeswell-marriages/` (17 files, `bw-img-0NN.jpg`) into that `_local/` folder. Then remove the two now-empty `images/packet-3*/` folders.
3. **Move** the reader's regenerable enhancement sheets/crops from `sources/intake/paleography-staging/snippets/packets-32-33/` to `sources/media/_local/packets-32-33-working-crops/`.
4. **New file write** — `sources/media/fs-england-norfolk-parish-registers-1510-1997/_local/README.md` (committed stub):

```markdown
# Local masters — FamilySearch Norfolk parish-register images (Great Dunham, Bawdeswell)

Local-only (gitignored) masters: FamilySearch viewing-terms images, off GitHub. Source: FamilySearch "England, Norfolk, Parish Registers (County Record Office), 1510–1997" (collection 1416598; Norfolk Record Office originals). Source ID: `fs-england-norfolk-parish-registers-1510-1997`.

## Great Dunham — composite register "Baptisms, Marriages, Burials," 1538–1658 (77 images)
- Files `gd-img-0NN.jpg`, where NN = the image number within the volume.
- Staged for Packet 32 (marriage test): marriages run images ~44–52; the decisive 1623–1632 window is images 48–49. Baptism context images 1–2, 31, 39.
- Retrieval: viewer waypoint `4J8C-ZCP:29626501,29358102,29668501`; first-image ARK `3:1:S3HY-61VS-KM2`; das/v2 per-image (see `.claude/skills/familysearch-fulltext-research/SKILL.md`).

## Bawdeswell — composite register "Baptisms, Marriages, Burials," 1557–1723 (111 images)
- Files `bw-img-0NN.jpg`, NN = image number.
- Staged for Packet 33 (Wales-tracking): baptism run images ~20–27 (~1619–1631); marriage pages 45 (1562–82) and 46 (1709+); burial/structure samples 1, 48, 49, 50, 67, 89, 105.
- Retrieval: viewer waypoint `4JZS-H91:29359301,29358102,29426001`; first-image ARK `3:1:S3HY-6SL2-6Z`.

Reports (assimilated): `sources/intake/paleography-staging/done/packet-32-…md`, `packet-33-…md`. Findings promoted to the G13 companion via patchset v113.
```

---

## Source tracking

- No new sourceIds. `rye-feet-of-fines-norfolk` and `fs-england-norfolk-parish-registers-1510-1997` both pre-exist; this patchset updates the former's corpus pointer and validation (Items 1–2) and cites the latter in a new G13 footnote (Item 4).
- Validation files: the Rye validation is updated in Item 2. The `fs-england-norfolk-parish-registers-1510-1997` validation (if present) does not require a worksheet edit — the Bawdeswell-register examination and its gap finding live in the G13 companion (Item 4), with the source cited there; a thin pointer may optionally be added to that validation on application.
