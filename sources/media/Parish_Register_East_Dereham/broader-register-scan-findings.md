# East Dereham broader-register independent scan — findings

Reviewed 2026-05-15. Independent scan of pages outside the prior AI's broad-pass crop range, prompted by user request to validate that other Gurney/ffrancis entries were not missed. No OCR/HTR. Raw-page visual inspection of `gbprs_norfolk_pd_86-41_*.jpg` images at full-page resolution; not line-level scanning. Evidence-class legend D/R/I retained.

## Scope and method

- Reviewed pages outside the prior AI's enhanced-crop coverage (`crop_00725` through `crop_00736` and `crop_00750` through `crop_00768`). The raw-image inventory covers 00693–00768 (76 images) — the prior AI's enhanced crops cover roughly 38 of these.
- Inspected raw images at full-page resolution to identify: section-break structure, year headings, page type (christening / marriage / burial), apparent duplicate scans, and any unexamined ranges where Gurney material could have been missed.
- At raw-page resolution, I cannot reliably stroke-resolve specific given-name / surname tokens (e.g., "ffrancis Gurney"); identifying Gurney mentions inside dense entries requires focused line crops similar to those created for 00725 and 00732. This pass therefore identifies **structural** findings and **next-pull priorities**, not new line-level Gurney readings.

## Findings affecting the case-file chronology

### F1 — Duplicate-scan pattern is widespread, not isolated to 00724/00725

The user has already flagged that `00724` is a duplicate scan of `00725`. Visual inspection at the raw-image level suggests this pattern repeats elsewhere in the register's scan sequence:

| Image pair | Apparent relationship | Basis |
|---|---|---|
| 00720 / 00721 | Probable duplicate | Both show identical "Eppingam" / indenture-header layout, similar entry layout below |
| 00724 / 00725 | Confirmed duplicate (user) | User-confirmed scanning artifact |
| 00726 / 00727 | Probable duplicate | Both show identical "Bille Indented / True Certificate or Roster" decorative title, identical indenture preamble, identical "ffor Marye[?]" section heading, identical column of entries below |
| 00733 / 00734 | Probable duplicate | Visually near-identical layout with the same section breaks and column rhythm |
| 00735 / 00736 | Probable duplicate | Both carry the identical "Billes Indented" decorative title + "Christ[enings] Anno D[o]m[ini] 1620" in-parchment heading + an April-onwards entry list |

- **Evidence class:** I (visual-layout pattern at full-page resolution, not stroke-confirmed line equivalence)
- **Why this matters:** the prior chronology work treated image numbers as 1-to-1 with register pages. If five of the listed pairs collapse to single register pages, the effective register-page count between known anchors halves in those regions and the case-file's year interpolation across the 00715–00736 corridor needs to be recompressed.
- **Recommended verification:** for each apparent pair, generate a small overlay-difference image (the `overlay` recipe in procedure §19.4). If the resulting overlay is near-uniform mid-gray, the pair is a duplicate; if structural differences emerge, they are separate register pages.

### F2 — Pages 00735 and 00736 are 1620 christenings, not 1618

The case-file currently treats `gbprs_norfolk_pd_86-41_00736.jpg` as the "Marye 1618" anchor (FS index VNN2-4VC). The raw image of 00736 (and its apparent duplicate 00735) shows a clear in-parchment section heading that reads as **"Christ[enings] Anno D[o]m[ini] 1620"** — written in the same early-modern hand as the entries, not in modern annotation. A modern "1620" annotation also appears in the upper-right corner outside the parchment.

- **Evidence class:** D (parchment heading legible at raw-page resolution) for the year 1620 anchoring of 00735/00736.
- **Implication:** either (a) the FS index has the year wrong on VNN2-4VC and the entry is actually a 1620 baptism; or (b) the case-file is pointing at the wrong image number for the "Marye 1618" entry and that entry is on an earlier page in the 1618 christenings section. The case-file's 1618 chronology anchor should be re-verified before any patchset relies on it.
- **Recommended next pull:** a six-state focused sweep of the heading area on 00735 and 00736 (the parchment block reading "Christ[enings] Anno D[o]m[ini] 1620"), plus a line-level search for the Marye-1618 entry on pages 00733/00734 (which would be approximately one register page earlier if duplicates are accounted for) and possibly 00731–00732.

### F3 — Pages 00726 and 00727 are the start of a new register section after the 00725 burials end

- **Evidence class:** D for the section break (decorative title and indenture preamble visible at raw-page resolution); I for the page-type identification.
- The 00726/00727 layout is structurally identical to 00735/00736: a decorative title block ("Bille Indented" / "His True Certificate or Roster"), an indenture preamble paragraph, a section heading, then a list of entries. This is the canonical East Dereham section-start layout.
- **Implication:** the 00725 burial list ends ~late January, and 00726/00727 begins what is likely a christenings section for the **following** year. This supports treating the 00725 Marye/Agnes burials as the **tail** of one calendar year of burials, with the section that follows starting a new year of christenings.
- **Recommended next pull:** focused heading-area crop of 00726/00727 to read the section title and any in-parchment year. This is the cleanest path to anchoring the 00725 burial year, since the burial page itself has no legible year heading.

### F4 — Register contains a Marriages section the prior AI did not call out

- **Evidence class:** D for the presence of a "Mariages" header at full-page resolution on 00729.
- The middle of page 00729 shows a clear secondary-heading word that reads as **"Mariages"** (early-modern spelling of Marriages), with entries continuing below it that follow a different format than the surrounding christenings/burials entries.
- **Why this matters for the case file:** Francis Gurney's marriage to Margaret (the wife whose burial is the case file's outstanding question) should appear in this register's marriages section if it took place at East Dereham. The case-file's "no burial entry for Margaret" finding does not foreclose locating the **marriage** entry, which would independently constrain the family chronology and could be a strong validation of the Francis Gurney identification.
- **Recommended next pull:** a full-page enhanced crop of 00729 plus 00728 and 00730 (apparent paired duplicates likely sit nearby), focused on the marriages section. Scan for "Gurney" / "Gurnie" / "Gurnoe" / "Gurny" forms with the same six-state sweep recipe used on 00732.

### F5 — Page 00697 is an Elizabethan section-divider showing "1593–1594, 38 Eliz" — the early register section is in the 1590s

- **Evidence class:** D for the label content.
- 00697 is a mostly-blank parchment page with a small handwritten label reading **"1593 – 1594"** and below it **"38 Eliz"** (38th regnal year of Elizabeth I).
- **Implication for Gurney research:** if Francis Gurney was baptized in this register, he would likely appear in the early baptism section in the 1590s window. A Francis born c.1585–1595 would be 14–24 years old by 1609 (the John Entry E baseline), consistent with being a father of a 1609 child. The early section (00693–00714) is therefore high-value for locating **Francis's own baptism** as well as any sibling baptisms.
- **Recommended next pull:** the early-section is currently entirely uncropped. A first-pass thin enhanced-crop of 00693–00714 (the same recipe used for the 00725–00736 corridor) would let the next AI/research pass scan for Gurney family-cluster entries in the 1590s window.

## Areas where my pass adds nothing new

- Line-level reading of Gurney mentions on the unexamined pages was not feasible at raw-page resolution. The prior AI's "no Gurney mention seen on 00728–00731 and 00733–00734" broad-pass result is not contradicted by my pass; it is also not independently validated. A line-level negative-pass over these pages is the next defensible step.
- The 00750–00768 range was not re-scanned; the prior AI's broad-pass note that this range is back-of-volume 1632–1633 register pages is consistent with my full-page inspection of two representative pages in that range, but I did not validate every page.
- No Gurney burial / baptism entry I would call out on my own appeared in the raw-page inspection. This is a resolution-limited result, not a confirmed absence.

## Consolidated priority list of next pulls

In priority order — combining this pass with the previous addendum's recommendations:

1. **Heading-area crop of 00735 and 00736**: parchment-block sweep of the "Christ[enings] Anno D[o]m[ini] 1620" line to confirm year. This single artifact decides whether the case-file's Marye-1618 anchor needs to move pages, and is upstream of everything else in the chronology.
2. **Heading-area crop of 00726 / 00727**: locks down the year of the section that immediately follows the 00725 burials, which in turn anchors the 00725 burial year.
3. **Tight magnification of the 00725 Marye relationship token** (carried over from the addendum): decides daughter vs niece/nephew for the Marye burial.
4. **Tight magnification of the 00725 Marye month token** (carried over): decides January vs other month.
5. **Marriages-section enhanced crops of 00728–00730**: scan for any "Gurney"-form marriage entry, including Francis Gurney's own marriage to Margaret. This is the cleanest validation path for the Francis-Margaret pairing.
6. **Six-state sweep of the candidate Marye-1618 line wherever it actually sits** — likely 00731–00734 if not 00735/00736. Depends on (1).
7. **Six-state sweep of the 00715 John Entry E (carried over from the addendum)**.
8. **Full-line sweep of the 00721 Edward entry (carried over)**.
9. **Thin enhanced crops of the 00693–00714 early section** — to scan the 1590s window for Francis Gurney's own baptism and any sibling baptisms. Lower priority than 1–6 because it is exploratory; promote if (1)–(6) confirm a Francis Gurney father identity, since that strengthens the case for searching for his own baptism here.
10. **Duplicate-scan verification overlays** for the candidate pairs (00720/00721, 00726/00727, 00733/00734, 00735/00736) — small overlay-diff images. Cheap to produce and useful for cleaning the chronology mapping.

## Recommended adjustments to the planned intake patchset

These do not change the C1–C6 / Q1–Q4 verdicts from the parent verification file but they widen the patchset's scope:

- Add a held-review flag: "Marye 1618 anchor on 00736 may be 1620; needs heading-area sweep before normalization."
- Add a held-review flag: "00729 contains an unexamined Marriages section; potential Francis Gurney marriage entry has not been ruled in or out."
- Add a duplicate-scan note to any source-validation entry that cites 00724/00725, 00720/00721, 00726/00727, 00733/00734, or 00735/00736 — to avoid double-counting register events.
- Do not promote any new Gurney readings from my pass; this scan produced **structural** findings only. Line-level promotion remains contingent on the focused crops in the priority list.
