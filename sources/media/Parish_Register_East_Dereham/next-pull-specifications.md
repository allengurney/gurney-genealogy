# East Dereham — precise specifications for the next six image pulls

Written 2026-05-15 in support of the prior AI assistant's next-batch work. These specifications consolidate the high-value asks from `page-00725-second-opinion-verification.md`, `page-00725-second-opinion-verification-addendum.md`, and `broader-register-scan-findings.md`. The list has been reprioritized to reflect the recent finding that pages 00735/00736 carry an in-parchment "1620" heading — meaning the chronology anchor at 00736 must be re-validated before any line-level Marye-1618 sweep is meaningful.

## Common recipe for line sweeps and heading sweeps

Unless otherwise noted, every line-level or heading-level sweep should produce a single PNG contact sheet with the following six panels (per the established procedure §8):

1. `raw-resized` — extracted crop, resized to a uniform width and height for the panel
2. `existing-enhanced` — crop pulled from the existing `crop_NNNNN_enhanced.png` working file at the matching coordinates
3. `autocontrast` — PIL `ImageOps.autocontrast` over the raw crop
4. `contrast+sharp` — PIL `ImageEnhance.Contrast(1.9)` then `ImageEnhance.Sharpness(1.8)` then `ImageFilter.UnsharpMask(radius=2, percent=170, threshold=3)`
5. `background flatten` — local-contrast (CLAHE clipLimit 2.5, tileGridSize 8x8) then Gaussian blur sigma 0.6
6. `support threshold` — adaptive threshold block 41 / C 12, treated only as a support view, never as sole evidence

Each panel should be labelled with the panel name in the top-left. The panel grid should be 3 columns × 2 rows. Image header should include the page number, the target line description, and the crop box `(left, top, right, bottom)` in original-image coordinates.

All crops are taken from the **raw** `gbprs_norfolk_pd_86-41_NNNNN.jpg` file unless explicitly noted, with the `existing-enhanced` panel pulled from `crop_NNNNN_enhanced.png` at the equivalent coordinates.

Coordinate convention below: `(left, top, right, bottom)` in pixels of the source file specified. Original `gbprs_norfolk_pd_86-41_*.jpg` images are typically 5016 wide × 4272 tall grayscale. Existing `crop_*_enhanced.png` images use coordinates given in `crop-index.md`.

---

## Ask 1 — Heading-area sweep of pages 00735 and 00736 to confirm 1620 vs 1618

**Filename:** `page_00735_00736_heading_year_sweep.png`

**Purpose:** Confirm or refute that the in-parchment header on pages 00735 and 00736 reads "Christ[enings] Anno D[o]m[ini] 1620". If confirmed, the case-file's "Marye 1618" anchor (FS index VNN2-4VC) must be re-anchored to a different page; if refuted, the year remains a question to resolve. Upstream of every line-level chronology decision in the corridor 00715–00736.

**Source images:**
- `gbprs_norfolk_pd_86-41_00735.jpg`
- `gbprs_norfolk_pd_86-41_00736.jpg`

**Crop boxes:** The heading block (decorative title + indenture preamble + "Anno Domini" line) sits in the upper portion of the parchment region on each page. Approximate starting boxes:
- 00735: `(1500, 350, 3050, 1500)` in original-image coordinates
- 00736: `(350, 300, 1900, 1450)` in original-image coordinates

If the prior AI judges these starting boxes too tight or too loose, expand vertically until the entire "Anno Domini [year]" line is captured and shrink horizontally to just the inked region. Do not crop tighter than the decorative title at the top.

**Output format:** Two stacked rows, one per page, each row using the six-state sweep recipe above. Total grid 3 columns × 4 rows (6 panels per page, two pages stacked). Each row's header should give the page number and the crop box. Resize each panel so the "Anno Domini [year]" line text is ~80 px tall — this is the critical letterform region.

**Expected reading to verify or refute:**
- Decorative title line: "Billes Indented" or similar
- Indenture preamble: several lines of Latinate / English indenture wording
- Section heading line: "Christ[enings] Anno D[o]m[ini] [YEAR]"
- Target adjudication: the YEAR token at the end of that line

**Pass-fail criteria for the consumer:**
- If the YEAR token reads as `1620` across at least three enhancement states with consistent letterform, confirm the 1620 anchor.
- If the YEAR token reads as anything else (most importantly `1618`), report the alternate reading and re-open the chronology assumption.

---

## Ask 2 — Heading-area sweep of pages 00726 and 00727 to anchor the 00725 burial year

**Filename:** `page_00726_00727_heading_year_sweep.png`

**Purpose:** The 00726/00727 page pair (apparent duplicate scans) opens a new register section immediately after the 00725 burial list ends. If the heading carries an in-parchment year — comparable to the "Anno Domini 1620" header on 00735/00736 — that year minus one is a defensible anchor for the 00725 burial year (which currently has no legible heading). This is the cheapest path to converting the 00725 Marye/Agnes burial date estimates from interpretive to direct-evidence on year.

**Source images:**
- `gbprs_norfolk_pd_86-41_00726.jpg`
- `gbprs_norfolk_pd_86-41_00727.jpg`

**Crop boxes:** Same structural target as Ask 1 — decorative title block, indenture preamble, and any year-bearing heading line. Approximate starting boxes:
- 00726: `(1500, 250, 3050, 1450)` in original-image coordinates
- 00727: `(1500, 250, 3050, 1450)` in original-image coordinates

(If the parchment is positioned differently on these images, refine to capture the equivalent region.)

**Output format:** Same as Ask 1 — two stacked rows, one per page, each using the six-state sweep recipe. Resize each panel so any heading text is ~80 px tall.

**Expected reading to verify or refute:**
- Decorative title (probably "Billes Indented" or "His True Certificate or Roster")
- Indenture preamble
- Section heading line: should be "Christ[enings] Anno D[o]m[ini] [YEAR]" or similar

**Pass-fail criteria for the consumer:**
- If a YEAR is legible, record it directly as the year of the section opened on 00726/00727.
- If the heading is a christenings section, the year of the section opened immediately after the 00725 burials → the 00725 burial year is most likely `YEAR-1` (since 00725 ended its year in late January, and the next register section presumably starts with the new year's christenings).
- If the heading is **not** a christenings section (e.g., a separate marriages section, or a continuation of burials), record that fact — it changes the inference but is still useful.

---

## Ask 3 — Tight magnification of the 00725 Marye relationship token

**Filename:** `page_00725_line_marye_relationship_token_x4.png`

**Purpose:** Decide whether the damaged relationship token between "Marye" and "of ffrancis Gurny" on the 00725 Marye burial line resolves as "the daughter", "the neece"/"the niece", "the nephew", or some other relationship. This decides whether the page-00725 Marye is Francis Gurney's daughter (the natural baseline assumption used elsewhere in the case file) or a more distant relative — a meaningful change to the case-file family chart.

**Source image:** `gbprs_norfolk_pd_86-41_00725.jpg` (raw page) — also pull the equivalent region from `crop_00725_enhanced.png` for the `existing-enhanced` panel.

**Region in original-image coordinates:** The 00725 Marye line sits inside the existing crop box `(1605, 650, 3135, 3355)`. Inside that crop, the Marye-line sweep used the **crop-coordinate** box `(0, 2605, 2295, 2825)`. The relationship token is located in the left-of-centre portion of that line, immediately after "Marye" and before "of ffrancis". In crop-coordinate space, target box approximately:

- crop-coord: `(350, 2605, 800, 2825)`
- equivalent original-image coord: `(1955, 3255, 2405, 3475)`

If the actual word-break boundaries differ from these estimates, widen the left edge by up to 100 px and the right edge by up to 150 px to be sure the full token is inside the crop, but do not include "Marye" or "of ffrancis" themselves.

**Output format:** Six-state sweep at **4x resize** (this is the highest-zoom request — the token is only 4–5 character widths long, so it must be displayed large enough to count strokes). Panels still 3 columns × 2 rows. Each panel resized to approximately 1200 px wide × the proportional height.

**Expected adjudication targets — the consumer is looking for:**
- Letter count: 3 letters + space + 4-5 letters? Or one long word?
- Initial letter of the candidate relationship word: a "d"-shaped open loop (favors `daughter`) or an "n"-shaped two-stem opening (favors `niece` / `nephew`)?
- Mid-word ascenders: any h-shoulder consistent with `daughter`, or compressed mid-body consistent with `niece`?
- Terminal stroke: a long descending tail (favors `daughter`-style terminal r) or a clean drop (favors a shorter terminal)?

**Pass-fail criteria:**
- CONFIRM "daughter" if the initial-d shape, mid-body h-shoulder, and a recognizable `-ter` terminal all resolve consistently.
- CONFIRM "niece"/"neece" or "nephew" if the initial-n shape resolves and the word length is short (5–6 character widths).
- UNCERTAIN if neither pattern dominates after the six enhancement states — that is itself a useful answer.

---

## Ask 4 — Tight magnification of the 00725 Marye month token

**Filename:** `page_00725_line_marye_month_token_x4.png`

**Purpose:** Decide whether the month token preceding the numeral "25" on the 00725 Marye burial line reads as "January", "Iuly", "Iuny" / "June", or something else. The 00725 page is year-crossing if and only if the month is January (the prior AI's call); other months would force a different year-window inference for the page.

**Source image:** `gbprs_norfolk_pd_86-41_00725.jpg` — also pull the equivalent region from `crop_00725_enhanced.png` for the `existing-enhanced` panel.

**Region:** Inside the same Marye-line crop box `(0, 2605, 2295, 2825)` in crop-coordinate space. The month token sits to the right of "Gurny" and immediately before the numeral "25". Target box approximately:

- crop-coord: `(1700, 2605, 2100, 2825)`
- equivalent original-image coord: `(3305, 3255, 3705, 3475)`

If "25" is at the very right edge of the line, the month token may be narrower than 400 px; refine to just the month-word strokes.

**Output format:** Six-state sweep at **4x resize**. Panels 3 columns × 2 rows. Same resize convention as Ask 3.

**Expected adjudication targets:**
- Letter count of the month word: 7 letters (January), 4 letters (Iuly / Iune), or other?
- Initial letter: a capital "I" (favors `Iuly` / `Iuly`/ `Iuny`), a capital "J" with the long descender (favors `January`), or other?
- Mid-word features: a "-an-" cluster (favors `January`), a clean medial "l" (favors `Iuly`), or other?
- Terminal: `-ary`, `-ly`, `-ne`?

**Pass-fail criteria:**
- CONFIRM `January` if the initial-J descender, the mid-word `-an-` cluster, and a `-ary` terminal all resolve.
- CONFIRM an alternative month if its specific letterform pattern resolves consistently.
- UNCERTAIN if neither pattern dominates.

---

## Ask 5 — Marriages-section enhanced sweep over pages 00728, 00729, 00730

**Filename:** `pages_00728_00729_00730_marriages_section_sweep.png`

**Purpose:** Page 00729 carries a visible "Mariages" header at full-page resolution. The 00728 and 00730 pages flank it and may either be paired duplicate scans or continuation pages of the same marriages section. The case-file has an open Francis Gurney marriage question (specifically the marriage to Margaret, whose burial is the original lead) that has never been searched in this register's marriages section. A scanning sweep over this section is the cleanest independent validation path for the Francis-Margaret pairing.

**Source images:**
- `gbprs_norfolk_pd_86-41_00728.jpg`
- `gbprs_norfolk_pd_86-41_00729.jpg`
- `gbprs_norfolk_pd_86-41_00730.jpg`

**Crop boxes:** Use the existing `crop_00728_enhanced.png`, `crop_00729_enhanced.png`, `crop_00730_enhanced.png` images (per `crop-index.md`), and within each isolate the **marriages sub-section**. On 00729 specifically, the "Mariages" header is in the middle of the page (visible at full-page resolution); on 00728 and 00730, the marriages-section boundary depends on whether they are duplicate scans of 00729 (in which case the same vertical band applies) or continuation pages (in which case the marriages section may start at the top or continue to the bottom).

Approximate target band in **existing-enhanced-crop coordinate space** for each page:
- 00728: scan all of `crop_00728_enhanced.png` since I cannot confirm the marriages-section boundary at the available resolution. Bound the search by visible "Mariages" or similar heading.
- 00729: bound to a vertical strip immediately above and below the "Mariages" header. Approximate crop-coord box: `(0, 1400, 1165, 3250)` (i.e., from just above the header through the end of the marriages list to the next section break).
- 00730: same approach as 00728 — full crop, bounded by visible section headings.

**Output format:** This is **NOT** a single line-level six-state sweep. Produce a **scan-sheet** rather than a six-state contact sheet:
- One row per page (three rows total)
- Each row showing two panels: `raw-resized` (full crop or marriages-section sub-crop) and `contrast+sharp` (same crop with the contrast+sharp recipe applied)
- Resize so each row is approximately 1400 px tall — these images are scan targets, not stroke-level adjudication targets

**What the consumer looks for:**
- Any line where one of the two principals is a Gurney/Gurnie/Gurnoe/Gurny surname.
- Any line where one of the two principals is named `ffrancis` (regardless of surname legibility).
- Any line where one of the two principals is named `Margaret` (regardless of surname legibility) **and** the other principal has a Gurney-form surname.
- Apparent year markers within the marriages section.

**Output of the consumer pass:** a brief markdown summary listing each candidate line found (or "no candidates"), the page and approximate y-coordinate, and a short same-hand letterform note. If a candidate Gurney marriage is found, follow up with a dedicated six-state line sweep using the standard recipe.

---

## Ask 6 — Six-state line sweep of the 00715 John Entry E line (re-anchor)

**Filename:** `page_00715_line_05_john_entry_e_sweep.png`

**Purpose:** The case file's John Entry E reading is the linchpin of the broader Francis Gurney attribution. The original adjudication was completed in March 2026 (ChatGPT Thinking v5.4 per the procedure document) and uses comparator artifacts retained in `site/website/media/east-dereham/`. The retained line-level target crop is `line_05_enh_x3.png`. This pull re-runs the six-state sweep on that line using the same recipe applied to the 00725 line sweeps and the new 00732 line sweep, so John Entry E sits at the same evidence standard as the rest of the cluster.

**Source image:**
- `gbprs_norfolk_pd_86-41_00715.jpg` (raw)
- For the `existing-enhanced` panel, use `line_05_enh_x3.png` at its native size

**Region in original-image coordinates:** The original crop coordinates used in March 2026 are not recoverable from retained state (per procedure §6.3). Use `line_05_enh_x3.png` as the visual reference and identify the equivalent line on the raw page by matching the surrounding two-three lines above and below. Once identified, record the original-image bounding box in the output header so future passes can re-find it deterministically.

Target box geometry (relative reference, since absolute pixel coords need to be re-extracted): one full register-page line, approximately 1500 × 200 px in original-image scale.

**Output format:** Six-state sweep at **3x resize** (matches the original `line_05_enh_x3.png` retained naming). Panels 3 columns × 2 rows. Header line should include the recovered bounding box in original-image coords.

**Expected adjudication targets (these are the four tests from procedure §10–13 — re-run, do not assume the prior result):**

1. **Initial-stroke cluster test:** does the father-name opening behave like a capital `N` (Nicholas) or a fused / compact double-`f` opening (ffrancis)?
2. **Mid-body ascender / loop test:** is there a true `h` ascender (Nicholas) or compressed mid-body loops (ffrancis)?
3. **Segmentation / rhythm test:** does the word segment into `Ni-cho-las` or flow as `ffrancis`?
4. **Terminal formation test:** is the word ending `-las` (Nicholas) or compressed `-cis` (ffrancis)?

Additionally:
- The surname zone: does the surname resolve as `Gurnie` / `Gurny` / `Gurnoe` (consistent with the same-hand cluster) or as `Gorne` (the FS index reading and a singleton in the corpus)?

**Pass-fail criteria for the consumer:**
- Report each of the four father-name tests as `favors-Nicholas` / `favors-ffrancis` / `inconclusive`.
- Report the surname as `Gurnie`-cluster / `Gorne` / `inconclusive`.
- Report whether the original March-2026 conclusion of "ffrancis Gurnie" still holds under independent re-adjudication.

---

## Items moved off the top six (still valuable, retained as priority 7+)

These items remain valuable but were superseded in priority by the year-anchor work above. They should still be produced; they are simply not the next-six.

- **Page-00721 Edward full-line sweep** — six-state line sweep across the entire `Edward the sonne of ffranci[s] Gurnie/Gurny baptize may 27` line (not just the terminal). Filename: `page_00721_line_edward_full_sweep.png`. Recipe identical to Ask 6 with 3x resize.
- **The "Marye 1618" line sweep wherever it actually sits** — once Ask 1 resolves the 1620-vs-1618 year question, generate a six-state sweep of the Marye line that FS indexes as VNN2-4VC. If 00735/00736 are 1620, the Marye-1618 entry is likely on 00731–00734 and should be located via heading-area year crops on those pages first.
- **Duplicate-scan overlay-diff images** for the candidate pairs `(00720, 00721)`, `(00726, 00727)`, `(00733, 00734)`, `(00735, 00736)`. Each pair → one PNG produced by the procedure §19.4 `overlay` recipe (or equivalent absolute-difference image). A near-uniform mid-gray result confirms a duplicate scan; structural differences refute it.
- **Thin enhanced crops of the early section 00693–00714** — exploratory hunt for Francis Gurney's own baptism in the 1590s window. Same enhancement recipe used for the existing `crop_00725_enhanced.png` series. Lower priority because exploratory.

## Naming and storage

- All outputs should be placed in `sources/media/Parish_Register_East_Dereham/`.
- Adopt the prefix `page_NNNNN_` for line-level / heading-level sweeps and the prefix `pages_NNNNN_NNNNN_` for multi-page sweeps.
- Append a short descriptive suffix (`_sweep`, `_token_x4`, `_overlay`, etc.).
- All sweeps should retain the panel-label and the crop-box header inside the PNG itself, so the artifact is self-describing without referring back to this spec.
