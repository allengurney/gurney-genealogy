# East Dereham PD 86/41 register structure and chronology

Examined: 2026-05-15. Image set under `sources/media/Parish_Register_East_Dereham/` (raw `gbprs_norfolk_pd_86-41_00693.jpg` through `gbprs_norfolk_pd_86-41_00768.jpg`; enhanced crops per `sources/media/Parish_Register_East_Dereham/crop-index.md`). Tooling at `tools/east_dereham_image_sweeps.py`.

Findings landed in:
- `research/topics/east-dereham-parish-register-paleography.md` (fact-and-confidence narrative).
- `sources/media/Parish_Register_East_Dereham/east-dereham-paleographic-analysis-comprehensive-2026-05-15.md` (deep-reference comprehensive analysis).
- `research/case-files/john-gurney-case-file-v4.md` §4.2 children-table refinement (Entry B relationship; Entry D page attribution).
- `research/people/g14-francis-gurney-fact-sheet.research.md` East Dereham subsection (paleographic refinement).

Source IDs touched:
- `fs-vnn2-4vc-marye-gurney-baptism-east-dereham` (new in v40; baptism on page 00732, not 00736)
- `fs-vnn2-wr2-marye-gurney-burial-east-dereham` (notes-field appendix in v40; relationship and month refinements)
- `fs-vnn2-wrg-agnes-gurney-burial-east-dereham` (notes-field appendix in v40; date anchor 31 January 1616 modern)
- `fs-vnn2-scf-edward-gurney-baptism-east-dereham` (notes-field appendix in v40; year remains ±2-3)

Key structural findings:

1. **Combined annual returns.** From image 00726 onward the register is laid out as combined annual returns. Each return opens with a decorative title block ("Bille Indented", "His True Certificate or Roster", or "Billes Indented") + indenture preamble + "Anno Dom [YEAR]" section heading. Each annual return covers christenings, marriages, and burials for one Lady-Day-to-Lady-Day year (25 March year N - 25 March year N+1). Inline "Mariages" header separates the marriages subsection from the surrounding christenings + burials subsections. Confirmed at D-class resolution on the 00736 page title ("Billes Indented of all the Christnings, Marriages and Burialls in East Dereham 1620") in `sources/media/Parish_Register_East_Dereham/page_00736_marye_1618_source_mismatch_context.png`.

2. **Year anchors.**
   - 00735 / 00736 = **1620 register year** (25 March 1620 - 25 March 1621). In-parchment "Christings Anno Dom 1620" heading; D-class. Confirmed in `sources/media/Parish_Register_East_Dereham/page_00735_heading_year_sweep.png` and `page_00736_marye_1618_source_mismatch_context.png`.
   - 00726 / 00727 = **1616 register year** (25 March 1616 - 25 March 1617). In-parchment date span "25 of March 1616 unto the 25 of March 1617"; D-class. Confirmed in `sources/media/Parish_Register_East_Dereham/page_00726_00727_heading_year_sweep.png`.

3. **Chronology lattice (post-00726).** Assuming one register page per annual return with paired duplicate scans:

   | Image pair | Register year (OS) | Modern-year span | Evidence class |
   |---|---|---|---|
   | 00726 / 00727 | 1616 | 25 Mar 1616 - 25 Mar 1617 | D |
   | 00728 / 00729 / 00730 | 1617 | 25 Mar 1617 - 25 Mar 1618 | I (interpolated) |
   | 00731 / 00732 | 1618 | 25 Mar 1618 - 25 Mar 1619 | I (interpolated; consistent with the 00732 Marye Gurnoe May-25 entry, locked at 25 May 1618 modern) |
   | 00733 / 00734 | 1619 | 25 Mar 1619 - 25 Mar 1620 | I (interpolated) |
   | 00735 / 00736 | 1620 | 25 Mar 1620 - 25 Mar 1621 | D |

   Page 00725 (= 00724 duplicate per user confirmation) sits immediately before the 1616 annual return and is therefore the burial subsection of the **1615 register year** (25 March 1615 - 25 March 1616 OS).

4. **Duplicate-scan pattern.** Confirmed and probable duplicate pairs:
   - 00720 / 00721 (probable; identical "Eppingam" / indenture-header layout)
   - 00724 / 00725 (confirmed by user; scanning artifact)
   - 00726 / 00727 (probable; identical decorative title + preamble + heading + entry column)
   - 00733 / 00734 (probable; visually near-identical)
   - 00735 / 00736 (probable; identical "Billes Indented" title + 1620 heading + entry list)

   Pixel overlay-diff confirmation is queued as a low-cost follow-up.

5. **Pre-00726 layout.** Pages 00715, 00721, and similar early pages do not appear to use the combined-annual-return layout; the chronology lattice does not extend back to them with the same confidence. The case file's ±2-3 year margin for East Dereham dates remains appropriate for pre-00726 entries.

6. **Modern marginal annotations.** Modern annotations ("PD 86/41/6", "1610", "1620") sit outside the parchment edge and are external-archivist annotations, not contemporaneous register-year headings. Year inferences rely on in-parchment headings only.

7. **Elizabethan section divider.** Page 00697 is a mostly-blank parchment with a small handwritten label "1593-1594" / "38 Eliz". Places the early section in the 1590s. If Francis G14 was baptized in this register, his own baptism plausibly sits in the unindexed 00693-00714 range.

Negative findings carried over from earlier work:

- No Gurney marriage candidate flagged in the 1617 annual return marriages subsection (pages 00728-00730). Other annual returns' marriages subsections remain unscanned.
- No Margaret-wife-of-ffrancis or Rybett/Ryvett variant burial flagged in the 00725 burial subsection. Other annual returns' burial subsections remain unscanned for the burial target.
- No missed Gurney/Gurnie/Gurny/Gurnoe entries flagged in line-strip negative passes over pages 00733, 00734, and 00735.

Open research targets (priority order) are listed in `research/topics/east-dereham-parish-register-paleography.md`.

Tooling: `tools/east_dereham_image_sweeps.py` encodes the six-state recipe, the marriages scan-sheet recipe, and the per-page heading-year sweep. CLI: `python tools/east_dereham_image_sweeps.py next-pulls`.
