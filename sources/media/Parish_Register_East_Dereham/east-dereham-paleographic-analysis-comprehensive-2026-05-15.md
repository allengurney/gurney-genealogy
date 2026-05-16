# East Dereham parish register — comprehensive paleographic analysis

Compiled 2026-05-15. Consolidates the full body of paleographic, structural, and chronology analysis performed on the East Dereham PD 86/41 parish-register image set under `sources/media/Parish_Register_East_Dereham/`. This file is a deep-reference artifact — long-form, raw, and intentionally exhaustive. Frequent-access research summaries live in `research/topics/`. The repo-update artifact lives in the V40 intake patchset.

## 1. Provenance and method

### 1.1 Image corpus

Source images in `sources/media/Parish_Register_East_Dereham/`:

- Raw register pages: `gbprs_norfolk_pd_86-41_00693.jpg` through `gbprs_norfolk_pd_86-41_00768.jpg` (76 images, grayscale, typically 5016 × 4272 pixels).
- Enhanced crops: `crop_00725_enhanced.png`, `crop_00728_enhanced.png` through `crop_00736_enhanced.png`, `crop_00750_enhanced.png` through `crop_00768_enhanced.png` (29 images, PIL `ImageEnhance.Contrast(1.6)` + autocontrast + 1.5x upscale; coordinates in `crop-index.md`).
- Line-level sweeps and magnifications listed under §5 below.

### 1.2 Methodology

- No OCR, no HTR. Same-hand comparator paleography only.
- Six-state enhancement sweeps following procedure §8: raw-resized, existing-enhanced, autocontrast, contrast+sharp (PIL `ImageEnhance.Contrast(1.9)` → `ImageEnhance.Sharpness(1.8)` → `ImageFilter.UnsharpMask(radius=2, percent=170, threshold=3)`), background-flatten (OpenCV CLAHE clipLimit 2.5 tileGridSize 8x8 → Gaussian blur sigma 0.6), and support-threshold (OpenCV adaptive threshold block 41 / C 12). The threshold view is treated only as a support, never as sole evidence.
- Evidence class legend per procedure §0.1: **D** direct (recoverable from current artifacts or safe workflow notes), **R** reconstructed (consistent with surviving outputs and retained code), **I** interpretive (qualitative paleographic judgment after enhancement and comparison).
- Reusable tooling: `tools/east_dereham_image_sweeps.py` (Python + PIL + OpenCV; generates the six-state sheets, the marriages scan-sheet, and the per-page heading/year sweep).

### 1.3 Working files this artifact synthesizes

In order of analytical depth:

- `burial-analysis.md` — prior AI broad-pass burial survey (2026-05-15)
- `crop-index.md` — enhanced-crop catalogue with crop boxes
- `page-00725-deep-analysis.md` — prior AI deeper page-00725 line-level work
- `page-00732-marye-ffrancis-gurnoe-terminal-analysis.md` — prior AI focused 00732 follow-up
- `followup-burial-image-analysis-2026-05-15.md` — prior AI follow-up batch from the v1 ask list
- `next-pull-results-2026-05-15.md` — prior AI follow-up batch from the v2 ask list
- `page-00725-second-opinion-verification.md` — my independent verification pass (C1–C6, Q1–Q4)
- `page-00725-second-opinion-verification-addendum.md` — my second-pass addendum (post-00732 confirmation, date-estimate work)
- `broader-register-scan-findings.md` — my structural scan of pages outside the prior AI's crop range
- `consolidation-note-2026-05-15.md` — my consolidation note on the followup batch
- `next-pull-specifications.md` — my detailed specifications for the second-batch asks
- This file — comprehensive consolidation

## 2. Register structure findings

### 2.1 Combined annual returns

**Finding.** From image 00726 onward, this register is laid out as combined annual returns. Each annual return is opened by a decorative title block — variants include "Bille Indented", "His True Certificate or Roster", "Billes Indented" — followed by an indenture preamble paragraph and a "Christings Anno Dom [YEAR]" section heading. Each annual return covers **christenings, marriages, and burials** for a single Lady-Day-to-Lady-Day year (25 March year N → 25 March year N+1).

**Evidence.**
- 00736 page title reads in full: *"Billes Indented of all the Christnings, Marriages and Burialls in East Dereham 1620"*, followed by churchwarden names, then "Christings Anno Dom 1620". Confirmed at D-class resolution in `page_00736_marye_1618_source_mismatch_context.png`.
- 00735 carries the same decorative title and the same "Christings ... 1620" section heading. Confirmed in `page_00735_heading_year_sweep.png`.
- 00726/00727 page title reads "His True Certificate or Roster" with a date span line consistent with **"25 of March 1616 unto the 25 of March 1617"** per `page_00726_00727_heading_year_sweep.png` and `next-pull-results-2026-05-15.md`.
- The 00729 page carries a visible "Mariages" subsection header midway down the page — confirming that christenings/marriages/burials are subsections within a single annual-return page rather than separate-section starts in the register volume.

**Implications.** The earlier interpretation of "burial pages" vs "baptism pages" should be re-read as **subsections within annual returns**. A "burial page" appearance is the lower (burials) subsection of a year's annual return; a "baptism page" appearance is the upper (christenings) subsection. The 25-March year-boundary anchors the register's date arithmetic and locks the chronology lattice in §4.

### 2.2 Duplicate-scan pattern

**Finding.** Several adjacent image pairs are duplicate scans of single register pages, not separate register pages. The duplicate-scan pattern was identified at full-page resolution from visual layout identity.

Confirmed and probable pairs:

| Pair | Status | Basis |
|---|---|---|
| 00720 / 00721 | Probable | Both show identical "Eppingam" / indenture-header layout |
| 00724 / 00725 | Confirmed (user) | User-confirmed scanning artifact |
| 00726 / 00727 | Probable | Both show identical decorative title + indenture preamble + section heading + entry column |
| 00733 / 00734 | Probable | Visually near-identical layout with the same section breaks and column rhythm |
| 00735 / 00736 | Probable | Both carry the identical "Billes Indented" title + 1620 heading + entry list |

**Evidence class.** I (visual-layout pattern). A cheap pixel-overlay-diff (`overlay` recipe in procedure §19.4 or equivalent absolute-difference) would convert probable pairs to confirmed.

**Implications.** The effective unique-register-page count between known anchors is roughly half the image-number count in regions where the duplicate-scan pattern operates. This is essential for the chronology mapping in §4.

### 2.3 Pre-1626 layout (probable; pages before ~00726)

**Finding.** Pages 00715, 00721, and similar early pages do not appear to use the "Billes Indented" combined-annual-return layout. The 00721 Eppingam page carries a modern "1610" annotation but a different in-parchment structure than the post-1626 annual returns. The transition to the combined-annual-return format appears to begin around image 00726.

**Evidence class.** I.

**Implications.** Chronology mapping for pages before ~00726 is less tightly constrained than for the 00726-onward range. The case-file's "±2-3 year margin" for East Dereham dates remains appropriate for pre-00726 entries.

### 2.4 Modern marginal annotations

**Finding.** Modern (post-foliation) annotations such as "PD 86/41/6", "1610", and "1620" appear in the upper corners of some images outside the parchment edge. These are external-archivist annotations and **not** contemporaneous register-year headings. Procedure §16.3 already flagged the modern 1610 annotation; the user has confirmed that the modern 1620 annotation on 00732 is similarly outside the parchment.

**Evidence class.** D for the annotation positions and hand style.

**Implications.** Year inferences should rely on in-parchment headings (e.g., the "25 of March 1616 unto the 25 of March 1617" line on 00726/00727 or the "Christings Anno Dom 1620" on 00735/00736), not on modern marginal numerals.

### 2.5 Elizabethan section divider on page 00697

**Finding.** Page 00697 is a mostly-blank parchment with a small handwritten label reading "1593–1594" and below it "38 Eliz" (38th regnal year of Elizabeth I).

**Evidence class.** D for the label content.

**Implications.** The early section of the register (00693 onward) sits in the 1590s. If Francis G14 was baptized in this register (he is documented from c.1611 as a father; estimated birth window ~1585–1595), his own baptism may sit in the unindexed 00693–00714 page range.

## 3. Line-level paleographic findings

### 3.1 Page 00725 — Marye burial line (FS index VNN2-WR2)

**Reading.** "Marye [relationship-token] of ffrancis Gurny [verb-token?] [date-token]"

**Direct-class tokens.**
- Given name: **Marye** — opening "M" two-peak secretary-hand form, body "a-r-y-e" with terminal-e. Firm across six enhancement states in `page_00725_line_marye_ffrancis_gurny_sweep.png`. D.
- Father name: **ffrancis Gurny** — double-f opening matches same-hand exemplars on `candidate_721_edward_francis_gurnie_wide.png` and the immediately-following Agnes line on `page_00725_line_agnes_ffrancis_gurny_sweep.png`. The "G" of Gurny has the closed-loop form matching the Agnes-line Gurny one register-line below. The terminal "-y" carries a long descending tail in both same-page Gurny instances. D.
- Date numeral: **25** — clear in raw-resized and existing-enhanced views. D.

**Interpretive tokens.**
- **Relationship token (Marye [TOKEN] of ffrancis Gurny):** the token is short — 4–5 character widths. The opening letter is not "d" (no closed lower loop with an ascender), and the body does not fill the 8 character widths required for `daughter`. Across the six enhancement states in `page_00725_marye_relationship_token_magnification_sweep.png` the strokes are class-consistent with `niece` / `neece` / `nephew`. **Refutes** `daughter`; the relationship is most likely a niece/nephew-family relation. I, supported by D-class magnification artifact.
- **Date verb / burial-verb token:** there is a short token before the numeral "25" that on the magnified sweep `page_00725_marye_month_token_magnification_sweep.png` could be either an abbreviated month name (Iuny, Iuly, Iany, Jany) or, less likely, a burial-verb form (buryd / bury'd). Width 4 character widths. **Refutes** the full-spelled `January`. Compatible with abbreviated `Iany`/`Jany` (January) or with mid-summer `Iuny`/`Iuly` (June/July). I, supported by D-class magnification artifact.

**Aggregate reading.** "Marye [the niece?] of ffrancis Gurny [buried/abbreviated-month] 25". Relationship class probable niece/nephew. Month either abbreviated January or mid-summer.

### 3.2 Page 00725 — Agnes burial line (FS index VNN2-WRG; FS-indexed "Susan")

**Reading.** "Agnes the daughter of ffrancis Gurny [Buryd?] 31"

**Direct-class tokens.**
- Given-name body "g-n-e-s" rhythm — a low-loop "g", a short connected mid-body, and a terminal "s" with the secretary-hand drop. Consistent with `Agnes`. D.
- Given-name opening: a leftward-opening triangular cap with a horizontal cross-stroke — capital "A" architecture, not the round-curving opening of capital "S". Refutes the FS index "Susan" reading. D.
- Word length: 5 character widths, consistent with `Agnes`, incompatible with `Susan` (5 chars but different stroke pattern) or `Susanna` (7 chars).
- "the daughter of ffrancis Gurny" — firm across all six enhancement states in `page_00725_line_agnes_ffrancis_gurny_sweep.png`. The "daughter" token shows a clean opening "d" with descending shoulder into "augh"; the surname matches the immediately-preceding Marye-line "Gurny". D.
- Numeral: **31** — firm. D.

**Interpretive tokens.**
- A short token between "Gurny" and "31" (visible in raw and contrast+sharp views) reads as "buryd"/"Bury'd"; supports the burial classification of the page. I.

**Aggregate reading.** "Agnes the daughter of ffrancis Gurny [buried] 31". The FS index's "Susan" reading is an indexer mis-read.

### 3.3 Page 00725 — section-classification evidence (burial vs baptism)

**Finding.** Page 00725 sits in a burial subsection (later understood as the burial portion of an annual return).

**Evidence.**
- `page_00725_line_robert_mary_leadin_sweep.png` shows two adjacent entries where the verb "Buried" is legible in raw, autocontrast, and contrast+sharp views: a "Robart [name] was Buried November 21" line and a following "Mary [name]" line with a November date. The "B-u-r-i-e-d" letter sequence with the long descender on the "B" is consistent across enhancement states. D.
- `page_00725_line_margaret_richard_cooke_sweep.png` shows a standalone "[Name] the wife of Richard Cooke [date]" form. Standalone wife-of-husband as the subject of a dated single-line entry is the canonical burial-register form for an adult woman; baptism registers record the wife only as the mother in the context of a named child's baptism. I.
- Comparator: 00721 (the confirmed-baptism Edward page) carries the verb "baptize[d]" before each date ("Edward ... baptize[d] may 27"; "Agnes ... baptize[d] may 28"). No "baptize[d]" verb appears in the 00725 entries reviewed. I.

### 3.4 Page 00732 — Marye Gurnoe baptism line (FS index VNN2-4VC)

**Reading.** "Marye the daughter of ffrancis Gurnoe bapt may 25"

**Direct-class tokens.**
- Given name: **Marye** — 5 character widths, terminal-e loop. The line immediately above is also a "Marye" (the daughter of John Park[er?]) baptized May 3, with matching length, rhythm, and terminal. Two adjacent "Marye" entries on the same May date cluster make the "Marye" reading effectively self-consistent. D.
- The given name **refutes** `Margaret` — 8 character widths and a terminal cross-stroke "t" are absent.
- "the daughter of ffrancis" — firm in raw and contrast+sharp views. D.
- Verb: **bapt** — legible in raw, autocontrast, and contrast+sharp. Confirms christening classification. D.
- Date: **may 25** — firm. D.

**Interpretive tokens.**
- Surname terminal: the open rounded "-oe" form lacks the descending y-tail seen on both 00725 Gurny surnames. `page_00732_surname_terminal_comparison_00721_00725.png` documents the contrast. Best paleographic reading is `Gurnoe`; `Gurney` is a downstream-normalization candidate. I.

**Implications.** The case-file's "Marye 1618" anchor (FS VNN2-4VC) is on page 00732, not 00736. The 00732 page is the 1618 register-year christenings subsection; see §4 chronology lattice.

### 3.5 Page 00715 — John Entry E (case-file Entry E)

**Reading (carried from the March 2026 ChatGPT analysis, re-verified at six-state in the 2026-05-15 follow-up).** "John the sonne of ffrancis Gurnie bapt Jan 10"

**Status.** Not independently re-adjudicated by me in the May 2026 verification pass — UNCERTAIN at the verification scope. The March 2026 four-test letterform analysis (procedure §10–§14) recorded:

| Test | Direction | Weight |
|---|---|---|
| Initial-stroke cluster | favors `ffrancis` | strong |
| Mid-body ascender / loops | favors `ffrancis` | moderate-strong |
| Segmentation / rhythm | favors `ffrancis` | moderate |
| Terminal formation | weakly favors `ffrancis` | weak-moderate |

No individual test favored `Nicholas`. The 2026-05-15 follow-up re-built the six-state sweep at `page_00715_entry_e_john_six_state_sweep.png` using the retained `line_05_enh_x3.png` target crop, bringing the evidence standard for Entry E to parity with the 00725 and 00732 line-level work. The surname-side anomaly analysis (procedure §15) found `Nicholas` and `Gorne` to be singletons in the reviewed corpus, while `ffrancis` + `Gurnie/Gurny/Gurnoe` recurs as a cluster. The aggregate reading remains `John the sonne of ffrancis Gurnie`.

### 3.6 Page 00721 — Edward baptism line (FS index VNN2-SCF)

**Reading.** "Edward the sonne of ffranci[s] Gurnie/Gurny baptize[d] may 27"

**Status.** Full six-state line sweep was completed in `page_00721_line_edward_ffrancis_gurnie_sweep.png` (prior AI follow-up). The line is a same-hand comparator for `ffrancis`, the `Gurn-` surname body, and the terminal variation between `Gurnie` and `Gurny`. The terminal differs from the 00732 `Gurnoe` open-o form; the 00721 terminal is more compact and supports the broader Gurney/Gurnie surname cluster.

**Date.** The FS-indexed date "27 May 1610" inherits its year from a modern marginal annotation on the parish-register page (the same modern hand also wrote "PD 86/41/6"), not from a contemporaneous register-year heading. The case file's ±2-3 year margin on East Dereham dates remains the correct posture for the Edward entry's year. The chronology lattice in §4 (which is anchored from 00726 onward) does not extend back to 00721 with the same confidence; the year remains plausibly anywhere in c.1610–1613.

### 3.7 Pages 00733/00734/00735 negative-pass for missed Gurney entries

The line-strip negative pass artifacts `page_00733_gurney_negative_pass_line_strips.png`, `page_00734_gurney_negative_pass_line_strips.png`, and `page_00735_gurney_negative_pass_line_strips.png` did not flag any missed Gurney/Gurnie/Gurny/Gurnoe entries. Page 00735 contains some `ffrancis` entries but the visible surnames are non-Gurney forms. Treat as "no candidate flagged in the line-strip pass," not as proof of absence under all imaging conditions.

### 3.8 Pages 00728–00730 marriages-section scan

The scan-sheet `pages_00728_00729_00730_marriages_section_sweep.png` did not flag any Gurney/Gurnie/Gurny/Gurnoe marriage candidate for the 1617 register year. Two candidate-name hits noted (`next-pull-results-2026-05-15.md`):

- 00728/00729 marriages subsection — a line reads visually as "Richard Barritt & ffrancis Crosse were married June 9" — `ffrancis` given-name hit but surname is `Crosse`, not a Gurney form.
- 00729 above the `Mariages` header — a "Margret the daughter of Edmund [...]" line — not a marriage entry and not paired with a Gurney-form surname.

**Implication.** No Gurney marriage in the 1617 register year. Other annual returns' marriages subsections (1616 on 00726/00727, 1618 on 00731/00732, 1619 on 00733/00734, 1620 on 00735/00736, plus pre-00726 marriages) remain not-yet-scanned and could plausibly contain Francis Gurney's marriage to Margaret if the marriage took place at East Dereham.

## 4. Chronology lattice

### 4.1 Direct-class anchors

- **00736 / 00735 = 1620 register year** (25 March 1620 → 25 March 1621). In-parchment "Christings Anno Dom 1620" heading, D-class.
- **00726 / 00727 = 1616 register year** (25 March 1616 → 25 March 1617). In-parchment date-span line per `next-pull-results-2026-05-15.md`, D-class on date span.

### 4.2 Interpolated mapping (post-00726)

Assuming approximately one register page per annual return, with paired duplicate scans accounting for image-number padding:

| Image pair | Register year (Old Style) | Modern-year span | Basis |
|---|---|---|---|
| 00726 / 00727 | 1616 | 25 March 1616 → 25 March 1617 | D — in-parchment date span |
| 00728 / 00729 / 00730 | 1617 | 25 March 1617 → 25 March 1618 | I — one annual return after 1616 |
| 00731 / 00732 | 1618 | 25 March 1618 → 25 March 1619 | I — two annual returns after 1616; consistent with the 00732 Marye Gurnoe May-25 baptism dating to **25 May 1618** (modern), matching the case file's FS-indexed Marye-1618 anchor (VNN2-4VC) |
| 00733 / 00734 | 1619 | 25 March 1619 → 25 March 1620 | I — three annual returns after 1616 |
| 00735 / 00736 | 1620 | 25 March 1620 → 25 March 1621 | D — in-parchment "Anno Dom 1620" heading |

### 4.3 00725 burial entries date

- The 00725 page sits immediately before the 1616 annual return on 00726/00727. It is therefore the burial subsection of the **1615 register year** (25 March 1615 → 25 March 1616 OS).
- The Agnes burial on 31 January reads as the late-winter tail of the 1615 register year — in modern dating, **31 January 1616**.
- The Marye burial token magnification leaves the month ambiguous between abbreviated January and mid-summer (Iuny/Iuly). If January, the Marye burial is **~25 January 1616** (modern). If mid-summer, the Marye burial is **~June or July 1615** (modern). The Agnes-line month is more confidently late-January and the two burials sit close together on the page, so the natural reading is two late-January 1616 burials — but the month token on the Marye line remains formally interpretive.

### 4.4 Pre-00726 chronology (less constrained)

Pages 00715 and 00721 sit in the pre-00726 portion of the register. The combined-annual-return format may not be in use here, so the one-register-page-per-year interpolation may not strictly apply. Working estimates:

| Image | Estimate | Basis |
|---|---|---|
| 00715 | c.1609–1610 (Jan 10 baptism for John Entry E) | I — case-file working estimate; consistent with the chronology lattice extrapolating backward |
| 00721 | c.1610–1613 (May 27 baptism for Edward) | I — modern marginal annotation says 1610; chronology lattice extrapolating backward gives ~1613; case-file ±2-3 year margin spans both |

### 4.5 Pre-1609 chronology

- 00697 carries a "1593–1594, 38 Eliz" section-divider label. The early-section (00693–00714) sits in the 1590s. Francis G14's own baptism, if in this register, plausibly sits in this range. Not yet line-level scanned.

## 5. Artifact manifest

### 5.1 Working analysis files

| File | Role |
|---|---|
| `burial-analysis.md` | Prior AI broad-pass burial survey |
| `crop-index.md` | Enhanced-crop catalogue with boxes |
| `page-00725-deep-analysis.md` | Prior AI deeper 00725 line-level work |
| `page-00732-marye-ffrancis-gurnoe-terminal-analysis.md` | Prior AI 00732 follow-up |
| `followup-burial-image-analysis-2026-05-15.md` | Prior AI follow-up batch 1 |
| `next-pull-results-2026-05-15.md` | Prior AI follow-up batch 2 |
| `page-00725-second-opinion-verification.md` | My independent verification pass |
| `page-00725-second-opinion-verification-addendum.md` | My second-pass addendum |
| `broader-register-scan-findings.md` | My structural-scan findings |
| `consolidation-note-2026-05-15.md` | My post-followup consolidation |
| `next-pull-specifications.md` | My second-batch ask specs |
| `east-dereham-paleographic-analysis-comprehensive-2026-05-15.md` | This file |

### 5.2 Line-level and heading-level sweep artifacts

Page 00725 sweeps:

- `page_00725_line_position_guide.png`
- `page_00725_upper_burials_x2.png` / `page_00725_upper_burials_enhancement_sweep.png`
- `page_00725_middle_family_cluster_x2.png` / `page_00725_middle_family_cluster_enhancement_sweep.png`
- `page_00725_lower_susan_mary_cluster_x2.png` / `page_00725_lower_susan_mary_cluster_enhancement_sweep.png`
- `page_00725_line_margaret_richard_cooke_sweep.png`
- `page_00725_line_robert_mary_leadin_sweep.png`
- `page_00725_line_marye_ffrancis_gurny_sweep.png`
- `page_00725_line_agnes_ffrancis_gurny_sweep.png`
- `page_00725_line_lower_continuation_sweep.png`
- `page_00725_marye_relationship_token_magnification_sweep.png`
- `page_00725_marye_month_token_magnification_sweep.png`

Page 00732 sweeps:

- `page_00732_line_margaret_ffrancis_gurnoe_sweep.png` (filename retains earlier target wording; resolves to Marye, not Margaret)
- `page_00732_surname_terminal_comparison_00721_00725.png`
- `page_00732_target_line_position_guide.png`
- `page_00732_target_line_grid.png`
- `page_00732_upper_christnings_position_guide.png`

Page 00715 / 00721 sweeps:

- `page_00715_entry_e_john_six_state_sweep.png` (six-state rebuild of John Entry E)
- `page_00721_line_edward_ffrancis_gurnie_sweep.png` (six-state Edward full line)
- `page_00721_line_edward_ffrancis_gurnie_terminal_crop.png` (terminal-only earlier crop)
- `page_00721_edward_line_position_guide.png`
- `page_00721_candidate_grid.png`

Page 00736 context / heading sweeps:

- `page_00736_marye_1618_source_mismatch_context.png` (full title legible — "Billes Indented of all the Christnings, Marriages and Burialls in East Dereham 1620")
- `page_00735_heading_year_sweep.png` (heading sweep, six-state)
- `page_00726_00727_heading_year_sweep.png` (heading sweep, both pages)

Marriages-section and negative-pass sweeps:

- `pages_00728_00729_00730_marriages_section_sweep.png` (scan-sheet; no Gurney candidates flagged for 1617)
- `page_00733_gurney_negative_pass_line_strips.png`
- `page_00734_gurney_negative_pass_line_strips.png`
- `page_00735_gurney_negative_pass_line_strips.png`

Same-register retained comparators (from `site/website/media/east-dereham/`):

- `candidate_721_edward_francis_gurnie_wide.png`
- `candidate_724_725_mary_agnes_francis_gurny.png`
- `line_05_enh_x3.png`
- `john_gurney_715_enhancement_sweep_v1.png` (earlier-format)
- `john_gurney_fathername_composite_v3.png` (earlier-format)

### 5.3 Tooling

- `tools/east_dereham_image_sweeps.py` — generates the six-state sheets, marriages scan-sheet, and per-page heading-year sweeps. Crop registry in `CROP_INDEX` constant; recipe constants for contrast+sharp, CLAHE+blur, and adaptive threshold. CLI: `python tools/east_dereham_image_sweeps.py next-pulls`.

## 6. Open items and recommended next pulls (priority order)

Carry-over priorities. Items 1–6 from `next-pull-specifications.md` have all been completed (see `next-pull-results-2026-05-15.md` and `followup-burial-image-analysis-2026-05-15.md`). The remaining open work:

1. **Marriages-section sweeps for the 1616, 1618, 1619, 1620 annual returns.** The 1617 sweep on 00728–00730 returned no Gurney marriage. Other annual returns' marriages subsections have not been scanned. If Francis Gurney's marriage to Margaret took place at East Dereham, it would sit in one of these subsections (1616 on 00726/00727, 1618 on 00731/00732, 1619 on 00733/00734, 1620 on 00735/00736) — or in a pre-00726 marriages section.
2. **Burials-subsection sweeps for the 1616–1620 annual returns.** The Margaret-wife-of-ffrancis burial target (still open) could sit in any of these annual-return burial subsections.
3. **Duplicate-scan overlay-diff images** for the candidate pairs (00720/00721, 00726/00727, 00733/00734, 00735/00736). Cheap to produce, cleans the chronology mapping if a probable pair turns out to be two separate register pages.
4. **00697 area / early-section thin enhanced crops** for the 1590s window — exploratory hunt for Francis G14's own baptism. Lower priority because exploratory.
5. **A primary-source pull of the 00725 burial entries' year heading**, if it exists on an adjacent register page outside the current crop boxes. The 00725 burial year is currently inferred from sequence (1615 OS); a direct in-parchment year would convert this from I to D.

## 7. Differences from the initial broad-pass interpretation

Where my analysis or the follow-up sweeps refined the prior AI's initial broad-pass:

- **Page 00725 burial classification.** Initial broad pass inferred burial classification from page rhythm and form. The Robert/Mary lead-in sweep adds the direct legible verb "Buried", anchoring the burial classification at D-class.
- **00725 Marye relationship word.** Initial pass: "relationship word is damaged". Magnification: refutes `daughter`; the relationship is most likely a niece/nephew-family relation.
- **00725 Marye month.** Initial pass: "January 25" treated as established. Magnification: the month token is 4 character widths, too short for spelled-out `January`; either abbreviated Iany/Jany or mid-summer Iuny/Iuly.
- **00725 Agnes vs FS-indexed Susan.** Initial pass: "Agnes" reading inferred. Magnification + comparator: Agnes is the visual reading; "Susan" is an indexer mis-read. Refuted the Susan hypothesis with capital-A architecture and word-length mismatch.
- **00732 candidate Margaret-baptism lead.** Initial pass: probable "Margaret daughter of ffrancis Gurnoe May 25". Focused sweep: refutes `Margaret`; the line reads `Marye the daughter of ffrancis Gurnoe`. The held-review Margaret lead should be withdrawn from any case-file context that retained it.
- **Marye-1618 anchor page attribution.** Initial pass and case-file: Marye-1618 entry attributed to page 00736. Heading sweeps: 00735/00736 are 1620 christenings; the Marye-1618 entry is on page 00732.
- **Register structure.** Initial pass treated separate "burial pages" and "baptism pages". Confirmed: the register from ~00726 onward is combined annual returns (christenings + marriages + burials per page).
- **Marriages section.** Initial pass did not call out a marriages subsection. Confirmed: 00729 carries a "Mariages" subsection header.
- **Duplicate-scan pattern.** Initial pass did not call out duplicate scans beyond 00724/00725. Probable pairs also include 00720/00721, 00726/00727, 00733/00734, 00735/00736.

## 8. Aggregate evidence-confidence table

| Finding | Verdict | Evidence class | Source artifact |
|---|---|---|---|
| Page 00725 is a burial subsection | CONFIRM | D | `page_00725_line_robert_mary_leadin_sweep.png` |
| Page 00725 Marye line reads "Marye [token] of ffrancis Gurny ... 25" | CONFIRM (name + father + numeral) | D | `page_00725_line_marye_ffrancis_gurny_sweep.png` |
| Page 00725 Marye relationship token = `daughter` | REFUTE | I (supported by D magnification) | `page_00725_marye_relationship_token_magnification_sweep.png` |
| Page 00725 Marye relationship token = niece/nephew family | Likely | I | same |
| Page 00725 Marye month token = full-spelled `January` | REFUTE | I (supported by D magnification) | `page_00725_marye_month_token_magnification_sweep.png` |
| Page 00725 Agnes line reads "Agnes the daughter of ffrancis Gurny ... 31" | CONFIRM | D | `page_00725_line_agnes_ffrancis_gurny_sweep.png` |
| FS index VNN2-WRG "Susan" is correct | REFUTE | I | same |
| Page 00732 line reads "Marye the daughter of ffrancis Gurnoe bapt may 25" | CONFIRM | D (line) + I (surname terminal) | `page_00732_line_margaret_ffrancis_gurnoe_sweep.png` |
| Case-file held-review "Margaret daughter of ffrancis Gurnoe" lead | REFUTE | I | same |
| Pages 00735 and 00736 = 1620 register year | CONFIRM | D | `page_00735_heading_year_sweep.png`, `page_00736_marye_1618_source_mismatch_context.png` |
| FS Marye-1618 (VNN2-4VC) anchor is on page 00736 | REFUTE; correct page is 00732 | D + I | same |
| Pages 00726/00727 open the 1616 register year (25 March 1616 → 25 March 1617) | CONFIRM | D | `page_00726_00727_heading_year_sweep.png` |
| Register layout = combined annual returns | CONFIRM | D | `page_00736_marye_1618_source_mismatch_context.png` |
| Duplicate-scan pattern beyond 00724/00725 | Probable | I | broader-scan visual layout identity |
| No Gurney marriage in 1617 register year | CONFIRM | I (scan-sheet level) | `pages_00728_00729_00730_marriages_section_sweep.png` |
| Page 00697 is "1593–1594, 38 Eliz" section divider | CONFIRM | D | raw page 00697 inspection |
| Page 00715 John Entry E reads `John the sonne of ffrancis Gurnie` | CONFIRM (March 2026 four-test analysis + May 2026 six-state rebuild) | I | `page_00715_entry_e_john_six_state_sweep.png` + procedure §10–§14 |
| Page 00721 Edward line reads `Edward the sonne of ffranci[s] Gurnie/Gurny baptize may 27` | CONFIRM | D | `page_00721_line_edward_ffrancis_gurnie_sweep.png` |
