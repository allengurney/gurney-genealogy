# East Dereham parish register — paleographic findings for Francis Gurney G14's household

Norfolk Record Office PD 86/41 covers the East Dereham parish register from 1593 onward. A 2026-05-15 paleographic pass over the available image set established the household-event picture for Francis Gurney G14 at East Dereham, anchored the register's date arithmetic via in-parchment year headings, and corrected several upstream-index attributions. Deep paleographic detail lives in `sources/media/Parish_Register_East_Dereham/east-dereham-paleographic-analysis-comprehensive-2026-05-15.md`; this topic file states the facts, confidence, and inferences that downstream research can rely on without re-doing the line-level work.

## Register structure

From image 00726 onward the register is laid out as **combined annual returns**. Each annual return opens with a decorative title block ("Bille Indented", "His True Certificate or Roster", or "Billes Indented"), an indenture preamble, and an "Anno Dom [YEAR]" section heading. Each annual return covers christenings, marriages, **and** burials for one Lady-Day-to-Lady-Day year (25 March year N → 25 March year N+1). Subsections within a single annual return appear in the order christenings → marriages → burials, with the marriages subsection signalled by an inline "Mariages" header.[^aer-2026]

This re-frames the earlier reading of the volume as separate "baptism pages" and "burial pages" — those are *subsections within annual returns*, not distinct register sections. The marriages subsection in particular was not surfaced in earlier passes; it sits in the middle of each annual return.

The image-numbered scans contain several **duplicate scans** of single register pages, not separate pages. The user has confirmed 00724/00725 as one such pair; image inspection at full-page resolution suggests the same pattern repeats at 00720/00721, 00726/00727, 00733/00734, and 00735/00736. A pixel-overlay-diff would convert these probable pairs to confirmed.

The pre-00726 pages use a different layout (not yet fully characterized) and the chronology lattice below does not extend back to them with the same confidence.

## Year anchors

Two direct-evidence year anchors lock the chronology after 00726:

- **00735 / 00736** carry the in-parchment heading "Billes Indented of all the Christnings, Marriages and Burialls in East Dereham 1620" followed by "Christings Anno Dom 1620". These pages are the **1620 register year** (25 March 1620 → 25 March 1621).[^anchor-1620]
- **00726 / 00727** carry a "His True Certificate or Roster" title with a date span line consistent with "25 of March 1616 unto the 25 of March 1617". These pages are the **1616 register year** (25 March 1616 → 25 March 1617).[^anchor-1616]

Modern marginal annotations (e.g., "PD 86/41/6", "1610", "1620") written outside the parchment edge are external-archivist annotations, not contemporaneous register-year headings. Year inferences should rely on in-parchment headings.[^marginal-annotations]

## Chronology lattice (post-00726)

Assuming one register page per annual return with paired duplicate scans:

| Image pair | Register year (OS) | Modern-year span | Confidence |
|---|---|---|---|
| 00726 / 00727 | 1616 | 25 Mar 1616 → 25 Mar 1617 | High (D) |
| 00728 / 00729 / 00730 | 1617 | 25 Mar 1617 → 25 Mar 1618 | Medium (I, interpolated) |
| 00731 / 00732 | 1618 | 25 Mar 1618 → 25 Mar 1619 | Medium (I, interpolated; consistent with the 00732 Marye Gurnoe May-25 entry) |
| 00733 / 00734 | 1619 | 25 Mar 1619 → 25 Mar 1620 | Medium (I, interpolated) |
| 00735 / 00736 | 1620 | 25 Mar 1620 → 25 Mar 1621 | High (D) |

Page **00725** (= 00724 duplicate) sits immediately before the 1616 annual return, so it is the burial subsection of the **1615 register year** (25 March 1615 → 25 March 1616 OS).

## Francis Gurney G14 household entries at East Dereham

Six entries in PD 86/41 are tied to Francis Gurney by visual reading and/or FS index attribution.

### 1. John (case-file Entry E)

- **Event:** baptism.
- **Date:** c.January 10, 1609–1610 (date day-and-month direct; year inferred — pre-00726 chronology, less constrained, case-file ±2-3 year margin applies).
- **Source:** PD 86/41 page 00715. FS index has the entry as "John the sonne of Nicholas Gorne"; the four-test letterform analysis (March 2026 ChatGPT analysis, re-built six-state in May 2026) reads it as **"John the sonne of ffrancis Gurnie"** — every test favored `ffrancis`, none favored `Nicholas`; same-hand recurrence and singleton analysis put `Nicholas Gorne` as an FS-index error.[^john-entry-e]
- **Confidence:** the father-name reading is the strongest single anchor for placing the colonial John Gurney's birth family at East Dereham. **Probable.**

### 2. Edward (case-file Entry A)

- **Event:** baptism.
- **Date:** May 27, year c.1610–1613 (date day-and-month direct from "may 27"; year inferred — the FS-indexed 1610 year derives from a modern marginal annotation, not from an in-parchment heading).
- **Source:** PD 86/41 page 00721 (FS index VNN2-SCF). Reading "Edward the sonne of ffranci[s] Gurnie/Gurny baptize may 27" — confirmed at six-state.[^edward-line]
- **Confidence:** **Confirmed.**

### 3. Marye — earlier burial (case-file Entry B, was-baptism, now-burial)

- **Event:** burial.
- **Date:** 25 of an ambiguous-month, register year 1615 OS. Day numeral direct (`25`); month token is 4 character widths and refutes spelled-out `January` — compatible with abbreviated `Iany`/`Jany` (late January 1616 modern) or with mid-summer `Iuny`/`Iuly` (June/July 1615 modern). Year inferred from chronology lattice.
- **Source:** PD 86/41 page 00725 (FS index VNN2-WR2). Reading "Marye [relationship token] of ffrancis Gurny [verb?] 25". Family-cluster context is confirmed; relationship-word stroke evidence **refutes `daughter`** and is class-consistent with niece/nephew family.[^marye-burial]
- **Confidence on Marye-as-Francis's-daughter:** **Refuted.** The relationship token does not support a daughter reading. The 00725 Marye is most likely a niece or other relative of Francis Gurney G14, not a daughter. This is one step firmer than the prior held-review framing and changes the case-file family chart.

### 4. Agnes — burial (case-file Entry C, was-baptism, now-burial; FS-indexed as "Susan")

- **Event:** burial.
- **Date:** 31 January, register year 1615 OS (= **31 January 1616 modern**). Day, month, and year-class direct from line + chronology lattice.
- **Source:** PD 86/41 page 00725 (FS index VNN2-WRG, indexed as "Susan"). Reading **"Agnes the daughter of ffrancis Gurny [buried] 31"**. The FS-indexed "Susan" is an indexer mis-read — the initial-letter architecture is capital "A", not capital "S", and the body matches `Agnes` not `Susan`/`Susanna`.[^agnes-burial]
- **Confidence:** **Confirmed.** The Round 2 working hypothesis of a previously-unrecorded daughter Susan is withdrawn (it is the same line as Agnes).

### 5. Marye — later baptism (case-file Entry D)

- **Event:** baptism.
- **Date:** **25 May 1618** (day, month, year all locked — day-and-month direct from line, year from chronology lattice with 00731/00732 = 1618 register year, fully consistent with the FS-indexed "Marye 1618" tradition).
- **Source:** PD 86/41 page 00732 (FS index VNN2-4VC). Reading **"Marye the daughter of ffrancis Gurnoe bapt may 25"**. The earlier case-file attribution of this entry to page 00736 is wrong — 00736 is a 1620 page. The correct page is 00732.[^marye-1618]
- **Confidence:** **Confirmed.** Naming pattern (subsequent daughter Marye after an earlier deceased Marye) is conventional 17th-century practice and consistent with §3 above.
- **Surname nuance:** the surname terminal reads paleographically as `Gurnoe` (open `-oe` form), distinct from the 00725 `Gurny` y-descender form. `Gurney` is a downstream-normalization candidate.

### 6. Francis (case-file Entry F, probable son)

- **Event:** burial.
- **Date:** 8 November 1633 (FS-indexed). Pre-V39 finding; not re-verified at line-level in the 2026-05-15 pass.
- **Source:** FS index VNN2-H8S. Parent not in the index; the probable-son-of-Francis-G14 attribution rests on geographic + chronological elimination of competing Francis Gurney identifications, and on the documented name-reuse pattern at the 1628 St Benet Fink Francis baptism (Bernau 1913).
- **Confidence:** **Probable son** (per V39 framing; not refined in this pass).

## Negative findings

- **No marriage of Francis Gurney to Margaret in the 1617 annual return** (pages 00728–00730). Scan-sheet level pass. The 1616, 1618, 1619, 1620 annual returns' marriages subsections have not yet been line-scanned for Gurney candidates, and a pre-00726 marriages section would also need separate scanning.[^marriages-1617]
- **No burial entry matching "Margaret wife of ffrancis Gurnie / Gurney / Gurny" or a Rybett / Ryvett variant** in the 00725 burial subsection. The Margaret-wife-of-ffrancis burial target remains unlocated in this register at the scope of the reviewed crops.[^margaret-burial-negative]
- **No missed Gurney/Gurnie/Gurny/Gurnoe entries** flagged in line-strip negative-passes over pages 00733, 00734, and 00735. Page 00735 contains some `ffrancis` entries but the visible surnames are non-Gurney forms.[^negative-pass]
- **No Gurney candidate** flagged on pages 00750–00768 (back-of-volume 1632–1633 register pages) at broad-pass resolution. Independent line-level verification not performed.

## Implications for the case file and fact sheet

- **Marye-1618 anchor** (case-file Entry D) cites the correct page now: PD 86/41 page **00732**, FS index VNN2-4VC.
- **00725 Marye relationship** (case-file Entry B) is **not** a daughter. The case file's family chart should reflect a niece/nephew-family relation; "daughter" should not be defaulted. If the case file held this entry as a confirmed daughter of Francis G14 in the children table, that should be downgraded.
- **Susan-Gurney candidate** (VNN2-WRG) is withdrawn — same line as Agnes; FS-index transcription error.
- **Margaret-daughter-of-ffrancis 00732 lead** (V39 held-review) is withdrawn — the 00732 line is Marye, not Margaret.
- **Edward (Entry A) year** remains ±2-3 — the FS-indexed 1610 derives from a modern marginal annotation, not an in-parchment heading. The chronology lattice does not extend back to 00721 with sufficient confidence to fix the year.
- **Margaret Rybett burial** is still unlocated in this register at the scope of the reviewed crops. The 1616, 1618, 1619, 1620 annual returns' burial subsections and a pre-00726 burial section have not yet been line-scanned for the burial target.

## Open research targets (priority order)

1. Marriages-subsection sweeps for the 1616, 1618, 1619, 1620 annual returns — locate a Francis Gurney + Margaret marriage if it took place at East Dereham.
2. Burial-subsection sweeps for the 1616–1620 annual returns and a pre-00726 burials section — locate Margaret Rybett's burial if it took place at East Dereham.
3. Duplicate-scan overlay-diff images for the candidate pairs (00720/00721, 00726/00727, 00733/00734, 00735/00736).
4. Early-section (00693–00714) thin enhanced crops — exploratory hunt for Francis G14's own baptism in the 1590s window.

## Tooling

The image-processing tooling lives in `tools/east_dereham_image_sweeps.py`. The script encodes the six-state recipe, the marriages scan-sheet recipe, and a `CROP_INDEX` constant matching `sources/media/Parish_Register_East_Dereham/crop-index.md`. CLI: `python tools/east_dereham_image_sweeps.py next-pulls`. Re-runs and new sweeps should use this tooling to preserve recipe parity with the existing artifacts.

[^aer-2026]: Combined annual return structure established by the in-parchment title on PD 86/41 page 00736: "Billes Indented of all the Christnings, Marriages and Burialls in East Dereham 1620" followed by churchwarden names. Confirmed at D-class in `sources/media/Parish_Register_East_Dereham/page_00736_marye_1618_source_mismatch_context.png`. The "Mariages" inline subsection header is visible on `pages_00728_00729_00730_marriages_section_sweep.png`.
[^anchor-1620]: PD 86/41 pages 00735 and 00736 — in-parchment heading "Christings Anno Dom 1620". Six-state sweeps in `sources/media/Parish_Register_East_Dereham/page_00735_heading_year_sweep.png` and `page_00736_marye_1618_source_mismatch_context.png`.
[^anchor-1616]: PD 86/41 pages 00726 and 00727 — in-parchment date span "25 of March 1616 unto the 25 of March 1617" per the heading sweep `sources/media/Parish_Register_East_Dereham/page_00726_00727_heading_year_sweep.png` and the reading summarized in `next-pull-results-2026-05-15.md`.
[^marginal-annotations]: Procedure §16.3 in `site/website/key-research/east-dereham-ai-assistant-procedure.md` already flagged the modern 1610 annotation on the 00721 page as external. The modern "1620" annotation on the 00732 page sits outside the parchment edge in the user's image set; the user has confirmed only the 00732 page carries a modern annotation outside the parchment in this corpus.
[^john-entry-e]: Four-test letterform analysis in `site/website/key-research/east-dereham-ai-assistant-procedure.md` §10–§14 (initial-stroke cluster, mid-body ascender/loop, segmentation/rhythm, terminal formation). Six-state rebuild in `sources/media/Parish_Register_East_Dereham/page_00715_entry_e_john_six_state_sweep.png`.
[^edward-line]: Full-line six-state sweep in `sources/media/Parish_Register_East_Dereham/page_00721_line_edward_ffrancis_gurnie_sweep.png`. Modern marginal "1610" annotation visible in `page_00721_edward_line_position_guide.png`. FS index `fs-vnn2-scf-edward-gurney-baptism-east-dereham` in `data/sources.json`.
[^marye-burial]: Line sweep `sources/media/Parish_Register_East_Dereham/page_00725_line_marye_ffrancis_gurny_sweep.png`. Relationship-token magnification `page_00725_marye_relationship_token_magnification_sweep.png`. Month-token magnification `page_00725_marye_month_token_magnification_sweep.png`. The relationship-token analysis is the second-opinion finding in `page-00725-second-opinion-verification-addendum.md` and `consolidation-note-2026-05-15.md`, where the stroke count and opening-letter shape refute `daughter`.
[^agnes-burial]: Line sweep `sources/media/Parish_Register_East_Dereham/page_00725_line_agnes_ffrancis_gurny_sweep.png`. The capital-A opening-architecture refutation of "Susan" is documented in `page-00725-second-opinion-verification.md`.
[^marye-1618]: Line sweep `sources/media/Parish_Register_East_Dereham/page_00732_line_margaret_ffrancis_gurnoe_sweep.png` (filename retains earlier target wording; line resolves to Marye, not Margaret). Surname-terminal comparison `page_00732_surname_terminal_comparison_00721_00725.png`. Year-context analysis in `page-00725-second-opinion-verification-addendum.md` and the 00736 mismatch context image.
[^marriages-1617]: Scan-sheet `sources/media/Parish_Register_East_Dereham/pages_00728_00729_00730_marriages_section_sweep.png`. Visual triage only; no Gurney/Gurnie/Gurny/Gurnoe candidate flagged.
[^margaret-burial-negative]: Image-walk negative finding documented in `sources/media/Parish_Register_East_Dereham/burial-analysis.md` and confirmed for the 00725 burial subsection in `page-00725-second-opinion-verification.md`.
[^negative-pass]: Line-strip negative-pass artifacts `sources/media/Parish_Register_East_Dereham/page_00733_gurney_negative_pass_line_strips.png`, `page_00734_gurney_negative_pass_line_strips.png`, `page_00735_gurney_negative_pass_line_strips.png`. Treated as "no candidate flagged in the line-strip pass," not as proof of absence under all imaging conditions.
