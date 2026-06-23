# Packet 34 — Bawdeswell: close the Mary Wales test (indexed Ann 1618 / Peter 1629 + post-1627 mother/burial)

**Status:** Open brief, 2026-06-22. Successor to Packet 33, which confirmed the Bawdeswell marriage gap but did **not** image-confirm the indexed Ann Wales (1618) or Peter Wales (1629) baptisms and reached only ~1631. Lead L-161 (G13 emigrant wife Mary).

## The question (carried from Packets 32–33)
The emigrant **John Gurney (G13)** married a **Mary** of unknown family c.1627; their grandson bore the rare forename **Peter**, traced as a reverse tracer to a *Mary born to a father Peter*. The standout candidate is **Mary Wales, chr. 1611 Great Dunham, dau. Peter Wales** — a household ~6 miles from John's East Dereham birthplace that moved to **Bawdeswell** by 1618. Indexed children of Peter Wales: Mary (1611, Gt Dunham), Elizabeth (1614, bur. 1616), **Ann (1618, Bawdeswell)**, **Peter (1629, Bawdeswell)**.

Packets 32–33 established two things: (1) the marriage indexes do not cover these parishes, and Bawdeswell's surviving marriages jump **1562–1582 → 1709+** — so Mary's marriage cannot be tested here (a true register gap). (2) The test therefore shifts entirely to the **baptism and burial sections**: does Mary Wales reappear after ~1627 as a **mother** or in a **burial** (which would *eliminate* her as the emigrant's wife who died in New England), or does she vanish from the record after ~1627 (consistent with the candidacy)?

## Why Packet 33 fell short — and what changes here
Packet 33 discovered the Bawdeswell composite register is **NOT chronologically ordered**: faded, tight-bound, with baptism / marriage / burial entries interleaved and out of date-sequence. The img20–27 baptism window staged on a chronological assumption was therefore unreliable, which is most likely why the indexed Ann (1618) and Peter (1629) entries were not found where expected. **Packet 34 abandons the chronological-image assumption** and instead (a) reads the baptism portion comprehensively, and (b) uses the FamilySearch *index* entries for Ann and Peter to pin the exact film/image where possible.

## Two decisive tasks

### Task A — Resolve and pull the indexed Ann Wales (1618) and Peter Wales (1629) baptisms
The two entries are indexed in **FamilySearch "England, Births and Christenings, 1538–1975"** (IGI-derived). Search FamilySearch indexed records (not full-text):
- `Ann Wales`, christening **1618**, **Bawdeswell, Norfolk**, father **Peter Wales**.
- `Peter Wales`, christening **1629**, **Bawdeswell, Norfolk**, father **Peter Wales**.
- Spelling net: **Wales / Wallis / Walys / Wayles / Wale**; forename **Ann/Anne/Anna**, **Peter/Petrus**.

For each index hit, open the record detail and capture **every** source-locator field it carries — the **Digital Film / DGS number**, **batch number**, **image number / film reference**, and the collection it sits in. IGI entries are frequently index-only (no linked image); if so, record the batch/film so the underlying register can be matched, and fall through to Task B. If an index entry *does* carry an image link, pull that master and its two neighbouring openings.

### Task B — Comprehensive read of the Bawdeswell baptism section, 1610–1635
Because the book is disordered, read the **whole baptism portion** rather than a chronological slice. Stage the contiguous run that contains the baptisms (sampling in Packet 33 found baptisms scattered across img20–27 and img67, with "Anno 1617" at img23 and "Anno 1635" at img27 but other baptisms elsewhere). Harvest:
1. **Every Wales-family entry** (any spelling) anywhere in the baptism pages — confirm Mary (1611, if present), Ann (1618), Peter (1629); find **any other children of Peter Wales**; and record the **mother's forename** in each (test whether Peter Wales's wife was herself a "Mary").
2. **The decisive post-1627 test:** does a **Mary Wales** — or a Mary of any married surname, or simply any Mary whose husband could be a Gurney-variant — appear as a **mother** in a baptism dated **1627–1635**? Any such entry weakens the candidacy.
3. **Any Gurney/Gournay/Gurnay/Gurnie-variant entry** anywhere (baptism, marriage, burial).

### Task C — Bawdeswell burials, 1627–1640 (death-elimination)
Stage the Bawdeswell **burial** section covering **1627–1640** (Packet 33 found burials at img48–50, 67, also disordered). Test: is there a **burial of a Mary Wales** (or Mary [married-surname]) in this window? A local burial would eliminate her as the emigrant's wife. Record every Wales and every Gurney-variant burial.

## Source & provenance — Bawdeswell
FamilySearch **"England, Norfolk, Parish Registers (County Record Office), 1510–1997"** (collection `1416598`; NRO originals). Bawdeswell, **"Baptisms, Marriages, Burials," 1557–1723** (composite register; **111 images**). Waypoint `4JZS-H91:29359301,29358102,29426001`; first-image ARK `3:1:S3HY-6SL2-6Z`. Alternate parish waypoint `4JZS-4D3:29359301`. Browse images, unindexed.

## Image staging instructions (`images/packet-34-bawdeswell-wales/`)
Re-authenticate to FamilySearch, then download full-resolution masters via the das/v2 route (see `familysearch-fulltext-research` skill for the presigned-S3 image API). Stage:
- **Baptism section, comprehensive:** the contiguous block spanning the baptisms — at minimum **img18–img35** plus **img67** (the known out-of-sequence baptism leaf), to catch the disordered Wales entries 1610–1635. If the baptism run proves to extend further, follow it to its bounds.
- **Burial section 1627–1640:** **img46–img52** and any further burial leaves the read reveals (the burials are interleaved; img48 = burials 1646–48 / 1682–84, so the 1627–1640 burials sit on nearby but not strictly adjacent leaves — follow the dates).
- **Orientation:** img1 (opening), plus any leaf an index hit from Task A points to.
- Do **not** re-stage img20–27 alone on the chronological assumption — that was Packet 33's miss. Stage the wider contiguous block.

Masters are full-resolution JPGs (archival width). On incorporation, move to `sources/media/<sourceId>/_local/` per the staging README.

## Reading aids / terminology
- Entries are **English**: "[name] the son/daughter of [father] ([and mother]) baptised the [N] day of [month] 16NN"; burials "[name] [relationship] buried the [N] day of …".
- **Wales** = *Wales / Wallis / Walys / Wayles / Wale*; **Peter** = *Peter/Petrus*; watch **Mary/Maria/Marie** as a mother's or decedent's forename.
- Gurney-variant head-forms: *Gurney / Gurnay / Gournay / Gurnie / Gurnee*; first-letter corruption (G→C/J) common in these hands.
- Whole book flagged **"Faded Document / Tight Binding"** — expect gutter loss and light ink; outer columns read better than the gutter.

## Negative results are findings
Record explicit negatives: a confirmed **absence** of any post-1627 Mary Wales mother/burial entry is the result that *keeps the candidacy alive* and must be reported as a positive finding, with the page range actually read. Likewise a confirmed image-read of Ann (1618) and Peter (1629) — even if it only reproduces the index — closes the Packet 33 gap.

## Follow-up (not staged here)
- Great Dunham burials 1627–1660 are staged separately as **Packet 35** (the Great Dunham death-elimination + Gurney/Wales sweep).
- If a Wales×[groom] marriage or a post-1627 Mary entry is found, pull the surrounding leaves for witnesses, abode, and family reconstruction.
