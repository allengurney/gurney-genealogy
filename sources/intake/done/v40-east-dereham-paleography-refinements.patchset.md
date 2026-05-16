# Intake patchset v40 — East Dereham paleography refinements

```yaml
patchset_id: v40
created: 2026-05-15
repo_scope: gurney-genealogy
phase: phase_2_paleographic_refinements_on_top_of_v39
depends_on: v39-john-gurney-rounds-1-6-research-deep-dive
input_packet: sources/media/Parish_Register_East_Dereham/east-dereham-paleographic-analysis-comprehensive-2026-05-15.md
phase_2_rule: This patchset refines the V39 East Dereham child-cluster findings using a second-opinion paleographic pass and follow-up image sweeps. V40 corrects three V39 specifics (Marye-1618 page attribution from 00736 to 00732; Margaret-daughter-of-ffrancis-Gurnoe held-review lead withdrawn; 00725 Marye relationship word disambiguated from "daughter" to family-relation-class), adds new findings (register chronology lattice, combined-annual-return register structure, duplicate-scan pattern, 1617 marriages negative scan, tooling), and applies on top of an already-applied V39.
```

## 0. Scope

Six refinements confirmed for application after a 2026-05-15 second-opinion paleographic pass and follow-up image sweeps on top of V39:

1. **§4 children table refinement.** Entry B (Marye, 00725 burial) — the relationship word does not stroke-resolve to "daughter"; it is class-consistent with niece/nephew family. Re-frame from "earlier daughter" to "household-relation; not stroke-resolved to daughter". Entry D (Marye, 1618 baptism) — page attribution corrected from **00736** to **00732**. Entry B month — the magnified month token is 4 character widths and refutes spelled-out `January`; it is compatible with abbreviated `Iany`/`Jany` (January) **or** mid-summer `Iuny`/`Iuly`. Year — anchored by the 00726/00727 in-parchment heading "25 of March 1616 unto the 25 of March 1617" → 00725 burials = 1615 register year (Old Style), making the Agnes burial **31 January 1616** (modern) and the Marye burial either January 1616 or mid-summer 1615 (modern), month-token-dependent.
2. **Held-review withdrawal.** The V39 §7 held-review lead for a possible "Margaret daughter of ffrancis Gurnoe/Gurney bapt may 25" on `crop_00732_enhanced.png` is **withdrawn**. The focused six-state sweep refutes `Margaret` and the line resolves to `Marye the daughter of ffrancis Gurnoe`. Promoted to the case-file body as Entry D (replacing the prior 00736 attribution).
3. **`data/sources.json` addition.** New source ID `fs-vnn2-4vc-marye-gurney-baptism-east-dereham` for the 25 May 1618 Marye baptism on page 00732. The V39-applied set lacks this entry.
4. **New validation note.** `sources/validations/east-dereham-pd-86-41-register-structure-and-chronology.md` capturing the combined-annual-return register layout, the year anchors at 00735/00736 (1620) and 00726/00727 (1616), the chronology lattice for 00726-onward, and the duplicate-scan pattern.
5. **Companion file updates.** `research/people/g14-francis-gurney-fact-sheet.research.md` gets a compact paleographic-refinement subsection. The V39-inserted subsection text is amended in place (Marye relationship phrasing; Entry D page citation; held-review withdrawal).
6. **Research-topics addition.** `research/topics/east-dereham-parish-register-paleography.md` is the fact-and-confidence narrative; already created. This patchset only records its existence and primary cross-references.

Reusable tooling — `tools/east_dereham_image_sweeps.py` — was added during the 2026-05-15 work and is referenced by this patchset for re-runs and new sweeps.

## 1. `data/sources.json` source registry operations

Insert this new entry near the existing `fs-vnn2-h8s-francis-gurney-burial-east-dereham-1633` block (added in V39 §1.3), maintaining the FS-VNN2 cluster grouping for the East Dereham FS-index entries.

### 1.1 Add `fs-vnn2-4vc-marye-gurney-baptism-east-dereham`

```json
"fs-vnn2-4vc-marye-gurney-baptism-east-dereham": {
  "shortTitle": "FS index VNN2-4VC — Marye Gurney baptism 25 May 1618, East Dereham, father Francis",
  "citation": "England, Norfolk, Parish Registers (County Record Office), 1510-1997, FamilySearch entry for Mary Gurney, christening 25 May 1618, Dereham (East Dereham), Norfolk, father Francis Gurney. FS index identifier VNN2-4VC. The underlying register entry reads 'Marye the daughter of ffrancis Gurnoe bapt may 25' on PD 86/41 page 00732; the surname terminal is paleographically Gurnoe with downstream-normalized Gurney.",
  "archive": "FamilySearch — Norfolk Record Office partnership collection",
  "url": "https://www.familysearch.org/ark:/61903/1:1:VNN2-4VC",
  "corpusStatus": "transcript",
  "corpusPath": null,
  "mediaPath": "sources/media/Parish_Register_East_Dereham/page_00732_line_margaret_ffrancis_gurnoe_sweep.png",
  "validationPath": "sources/validations/fs-east-dereham-francis-gurney-indexed-children.md",
  "notes": "Baptism entry for Marye daughter of ffrancis Gurnoe at East Dereham, 25 May 1618. Visual reading from the enhanced register page (gbprs_norfolk_pd_86-41_00732.jpg, line-level six-state sweep). Anchors case-file Entry D. Year is locked by the chronology lattice in sources/validations/east-dereham-pd-86-41-register-structure-and-chronology.md: pages 00731/00732 are the 1618 register year (25 March 1618 - 25 March 1619) under the combined-annual-return layout, two annual returns before the directly-anchored 1620 register year on 00735/00736. The earlier case-file attribution of this entry to page 00736 reflects a pre-2026-05-15 working assumption; the actual 00736 page is a 1620 christenings page (page title 'Billes Indented of all the Christnings, Marriages and Burialls in East Dereham 1620'). The 25 May 1618 Marye baptism is a separate, later child of the same name as the 25 January (year-unindexed) Marye burial on page 00725 — a name-reuse pattern consistent with the earlier Marye having died in infancy."
}
```

## 2. `data/sources.json` source registry corrections

These entries were added in V39 and need a minor update on the back of the chronology-lattice work in this patchset.

### 2.1 Update `fs-vnn2-scf-edward-gurney-baptism-east-dereham` (V39 §1.4)

Append to the existing `notes` field (do not replace), preserving V39's note text:

```
Year is post-2026-05-15 understood as not directly anchored by an in-parchment heading on page 00721; the chronology lattice in sources/validations/east-dereham-pd-86-41-register-structure-and-chronology.md applies only from page 00726 onward (where the combined-annual-return layout begins). The case file's ±2-3 year margin therefore continues to apply to the Edward year specifically; the indexed 1610 date inherits from a modern marginal annotation. Plausible year range remains c.1610-1613.
```

### 2.2 Update `fs-vnn2-wr2-marye-gurney-burial-east-dereham` (V39 §1.2)

Append to the existing `notes` field:

```
Post-2026-05-15 paleographic refinement: the relationship token between 'Marye' and 'of ffrancis Gurny' was magnified at 4x in sources/media/Parish_Register_East_Dereham/page_00725_marye_relationship_token_magnification_sweep.png. The token is 4-5 character widths with an opening-letter shape that refutes 'daughter' and is class-consistent with niece/nephew family. The default 'daughter of' framing in this notes field should be read as the V39 working assumption; the case-file Entry B framing in v4.1 carries the refined family-relation-class wording. The month token before '25' was magnified in sources/media/Parish_Register_East_Dereham/page_00725_marye_month_token_magnification_sweep.png and is 4 character widths, refuting spelled-out 'January'; compatible with abbreviated Iany/Jany (late January 1616 modern) or with mid-summer Iuny/Iuly (June/July 1615 modern). The chronology lattice in sources/validations/east-dereham-pd-86-41-register-structure-and-chronology.md anchors the 00725 burial year to 1615 (Old Style); the Agnes burial on 31 January is therefore 31 January 1616 modern; the Marye burial day-month is 25 of an ambiguous month in the same register year.
```

### 2.3 Update `fs-vnn2-wrg-agnes-gurney-burial-east-dereham` (V39 §1.1)

Append to the existing `notes` field:

```
Post-2026-05-15 chronology-lattice work anchors this burial date to 31 January 1616 modern (25 March 1615 - 25 March 1616 register year on page 00725, immediately preceding the directly-anchored 25 March 1616 - 25 March 1617 annual return on pages 00726/00727; in-parchment date span at sources/media/Parish_Register_East_Dereham/page_00726_00727_heading_year_sweep.png).
```

## 3. New validation note

### 3.1 Create `sources/validations/east-dereham-pd-86-41-register-structure-and-chronology.md`

```markdown
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
```

## 4. `research/people/g14-francis-gurney-fact-sheet.research.md` updates

V39 §3 inserted a new "East Dereham children — primary index expansion and Entries B/C reclassification (FS + image-walk, 2026-05-15)" subsection. v40 adds a follow-on subsection immediately AFTER that V39-inserted block and BEFORE the existing "Pettigrew on Francis Gurnay of London and the Keswick commercial line" subsection.

```markdown
### East Dereham children — paleographic refinement (image sweeps, 2026-05-15)

Three refinements to the V39 East Dereham child-cluster framing, all grounded in focused image sweeps under `sources/media/Parish_Register_East_Dereham/` and the chronology lattice in `sources/validations/east-dereham-pd-86-41-register-structure-and-chronology.md`:

1. **Entry B (Marye, 00725 burial) — relationship class, not "daughter".** A 4x magnification of the relationship token between 'Marye' and 'of ffrancis Gurny' on the 00725 Marye burial line (`page_00725_marye_relationship_token_magnification_sweep.png`) shows a 4-5 character-width token whose opening-letter shape refutes 'daughter' and is class-consistent with niece/nephew family. The case-file Entry B should be read as a Francis G14 household-event entry (likely niece), not as a confirmed daughter. The Agnes line (Entry C) immediately below reads cleanly as "the daughter of ffrancis Gurny" and is unaffected by this refinement.[^east-dereham-paleographic-2026]

2. **Entry D (Marye, 1618 baptism) — page attribution corrected to 00732.** Focused six-state sweep `page_00732_line_margaret_ffrancis_gurnoe_sweep.png` resolves the candidate line as "Marye the daughter of ffrancis Gurnoe bapt may 25". The case file's earlier 00736 page attribution reflects a pre-2026-05-15 working assumption; the actual 00736 page is the 1620 christenings page ("Billes Indented of all the Christnings, Marriages and Burialls in East Dereham 1620"). Page 00732 sits in the 1618 register year under the chronology lattice and the date locks to **25 May 1618** modern. Surname terminal is paleographically `Gurnoe` (open `-oe` form); `Gurney` is a downstream-normalization candidate. Source ID `fs-vnn2-4vc-marye-gurney-baptism-east-dereham` added.[^east-dereham-paleographic-2026]

3. **Margaret-daughter-of-ffrancis-Gurnoe 00732 baptism lead — withdrawn.** The V39 held-review lead for a possible "Margaret daughter of ffrancis Gurnoe/Gurney bapt may 25" on `crop_00732_enhanced.png` is withdrawn. The focused sweep refutes 'Margaret' (word length and terminal incompatible) and replaces with the 'Marye' reading promoted to Entry D above. There is therefore no previously-undocumented daughter Margaret arising from the 00732 image; the original Margaret Rybett burial question remains open and unresolved by the East Dereham image set reviewed to date.

Chronology context (all I-class except where noted):

- Pages 00735 / 00736 = 1620 register year (D, in-parchment heading).
- Pages 00726 / 00727 = 1616 register year (D, in-parchment "25 of March 1616 unto the 25 of March 1617" date span).
- Page 00725 = 1615 register year burial subsection (I, derived by sequence from the 1616 anchor).
- Entry B and Entry C (00725 burials) therefore sit in the 25 March 1615 - 25 March 1616 OS register year; the Agnes burial 31 January is **31 January 1616** modern. The Marye burial month token is 4 character widths and refutes spelled-out 'January'; compatible with abbreviated Iany/Jany (late January 1616 modern) or with mid-summer Iuny/Iuly (June/July 1615 modern).
- Entry A (Edward, 00721 baptism) sits in the pre-00726 portion of the register and the lattice does not extend back with the same confidence; case-file ±2-3 year margin applies. The FS-indexed 1610 derives from a modern marginal annotation.

Register layout note: from page 00726 the register is laid out as combined annual returns (christenings + marriages + burials per page), with an inline "Mariages" subsection header. The 1617 annual return marriages subsection (pages 00728-00730) does not contain a Gurney candidate; other annual returns' marriages subsections (1616, 1618, 1619, 1620, and any pre-00726 marriages) remain unscanned and are the most direct path for testing whether Francis G14 + Margaret Rybett married at East Dereham.[^east-dereham-paleographic-2026]

[^east-dereham-paleographic-2026]: Paleographic analysis under `sources/media/Parish_Register_East_Dereham/`. Comprehensive deep-reference at `east-dereham-paleographic-analysis-comprehensive-2026-05-15.md`. Topic narrative at `research/topics/east-dereham-parish-register-paleography.md`. Validation note `sources/validations/east-dereham-pd-86-41-register-structure-and-chronology.md`. Tooling at `tools/east_dereham_image_sweeps.py`. Source IDs `fs-vnn2-4vc-marye-gurney-baptism-east-dereham`, `fs-vnn2-wr2-marye-gurney-burial-east-dereham`, `fs-vnn2-wrg-agnes-gurney-burial-east-dereham`, `fs-vnn2-scf-edward-gurney-baptism-east-dereham`.
```

## 5. Case-file edits in `research/case-files/john-gurney-case-file-v4.md`

### 5.1 Section 4.2 children table — refine Entry B and re-attribute Entry D

V39 §5.1 replaced the children table to add the Event column and reclassify B and C. v40 refines two rows in the V39-applied table.

Find the V39-applied row:

```markdown
| **B** | Marye (earlier daughter) | Burial | 25 January, year not in register | 00725 (FS index VNN2-WR2) | Confirmed<sup class="fn"><a href="#n96" id="ref-96b">96</a></sup> |
```

Replace with:

```markdown
| **B** | Marye (household relation; relationship word not stroke-resolved to *daughter*) | Burial | 25 of an ambiguous month (abbreviated Iany/Jany or Iuny/Iuly), register year 1615 OS | 00725 (FS index VNN2-WR2) | Confirmed event; relationship class<sup class="fn"><a href="#n96" id="ref-96b">96</a></sup><sup class="fn"><a href="#n102" id="ref-102a">102</a></sup> |
```

Find the V39-applied row:

```markdown
| **C** | Agnes | Burial | 31 January, year not in register | 00725 (FS index VNN2-WRG; indexed "Susan") | Confirmed<sup class="fn"><a href="#n96" id="ref-96c">96</a></sup> |
```

Replace with:

```markdown
| **C** | Agnes | Burial | 31 January 1616 (modern; register year 1615 OS) | 00725 (FS index VNN2-WRG; indexed "Susan") | Confirmed<sup class="fn"><a href="#n96" id="ref-96c">96</a></sup><sup class="fn"><a href="#n102" id="ref-102b">102</a></sup> |
```

Find the V39-applied row:

```markdown
| **D** | Marye (later daughter) | Baptism | 25 May 1618 | 00736 (FS index VNN2-4VC) | Confirmed |
```

Replace with:

```markdown
| **D** | Marye (later daughter) | Baptism | 25 May 1618 | 00732 (FS index VNN2-4VC)<sup class="fn"><a href="#n102" id="ref-102c">102</a></sup> | Confirmed |
```

### 5.2 Section 4.2 — short prose addition after the V39-inserted reclassification paragraph

V39 §5.2 inserted a paragraph beginning "The reclassification of Entries B and C from baptisms to burials reflects a 2026-05-15 image-walk of page 00725..." Insert this new paragraph immediately AFTER that V39 paragraph and BEFORE the existing "**These dates should be understood as estimates with a margin of approximately ±2–3 years.**" line.

```markdown
A focused 2026-05-15 paleographic refinement on the same page-00725 line tightened the Marye relationship reading and the chronology of the burial cluster. The relationship token on the Marye burial line, magnified at 4x, does not stroke-resolve to "daughter"; it is 4-5 character widths with an opening-letter shape class-consistent with niece/nephew family. Entry B therefore records a household-event for Francis G14 at East Dereham rather than a confirmed daughter, and the case-file family chart should not default to "daughter" for this Marye. The Marye month token is also short (4 character widths), refuting spelled-out "January"; the modern-date year locks to 1615/1616 via the chronology lattice, and the month is either late January 1616 (abbreviated Iany/Jany) or mid-summer 1615 (Iuny/Iuly). The Agnes burial date locks more confidently to 31 January 1616 modern. Entry D (Marye, baptism 25 May 1618) is on page 00732, not 00736 as earlier working notes had assumed: the 00736 page carries an in-parchment "Christings Anno Dom 1620" heading and is the 1620 register-year christenings subsection, while page 00732 is the 1618 register-year christenings subsection under the combined-annual-return register layout established for pages 00726 onward.<sup class="fn"><a href="#n102" id="ref-102d">102</a></sup>
```

### 5.3 Footnote n102 (new)

Add this new footnote immediately AFTER the existing V39-inserted footnote `n101`:

```html
<li id="n102" value="102">East Dereham paleographic refinement, 2026-05-15. Comprehensive deep-reference at <code>sources/media/Parish_Register_East_Dereham/east-dereham-paleographic-analysis-comprehensive-2026-05-15.md</code>. Topic narrative at <code>research/topics/east-dereham-parish-register-paleography.md</code>. Validation note <code>sources/validations/east-dereham-pd-86-41-register-structure-and-chronology.md</code>. Marye relationship token magnification at <code>sources/media/Parish_Register_East_Dereham/page_00725_marye_relationship_token_magnification_sweep.png</code>; Marye month token magnification at <code>page_00725_marye_month_token_magnification_sweep.png</code>; 00732 Marye Gurnoe line sweep at <code>page_00732_line_margaret_ffrancis_gurnoe_sweep.png</code> (filename retains earlier target wording; line resolves to Marye, not Margaret); 00735/00736 1620 heading sweeps at <code>page_00735_heading_year_sweep.png</code> and <code>page_00736_marye_1618_source_mismatch_context.png</code>; 00726/00727 1616 heading sweep at <code>page_00726_00727_heading_year_sweep.png</code>. Source IDs <code>fs-vnn2-4vc-marye-gurney-baptism-east-dereham</code> (new in v40), <code>fs-vnn2-wr2-marye-gurney-burial-east-dereham</code> (v39 base; v40 notes-field appendix), <code>fs-vnn2-wrg-agnes-gurney-burial-east-dereham</code> (v39 base; v40 notes-field appendix), <code>fs-vnn2-scf-edward-gurney-baptism-east-dereham</code> (v39 base; v40 notes-field appendix). <a class="backref" href="#ref-102a">back</a> <a class="backref" href="#ref-102b">back</a> <a class="backref" href="#ref-102c">back</a> <a class="backref" href="#ref-102d">back</a></li>
```

### 5.4 Case-file header version bump

V39 §5.10 set the case-file header to `updated: 15 May 2026` and `Version: 4.1`. v40 bumps the version to 4.2 to reflect the paleographic refinements.

Find:

```markdown
caseMeta: "<strong>Prepared by:</strong> Allen Lawrence Gurney, Portland, Oregon &nbsp;&nbsp; <strong>Date:</strong> May 2026 &nbsp;&nbsp; <strong>Version:</strong> 4.1"
```

Replace with:

```markdown
caseMeta: "<strong>Prepared by:</strong> Allen Lawrence Gurney, Portland, Oregon &nbsp;&nbsp; <strong>Date:</strong> May 2026 &nbsp;&nbsp; <strong>Version:</strong> 4.2"
```

Leave the `updated: 15 May 2026` line as is.

## 6. V39 held-review block — withdraw the Margaret-daughter lead

V39 §7 carries the held-review item:

> "Probable baptism reading 'Margaret the daughter of ffrancis Gurnoe/Gurney bapt may 25' on `crop_00732_enhanced.png` (East Dereham parish-register page 00732)..."

This item is withdrawn in v40 and should not be carried forward as an open held-review lead. The 00732 line is `Marye the daughter of ffrancis Gurnoe` and is promoted to the case-file body as Entry D (via §5.1 above). The Margaret Rybett burial question itself remains open and is **not** affected by this withdrawal — the original Margaret-wife-of-ffrancis burial target remains unlocated.

No action required in v40 if v39 §7 has already been treated as descriptive; if the held-review list is maintained as a separate tracking document, remove the Margaret-daughter-of-ffrancis-Gurnoe-bapt-may-25 row and add a single line: "Margaret Rybett burial target — still unlocated as of 2026-05-15; 1617 annual return marriages and burial subsections scanned negative; other annual returns' subsections remain unscanned."

## 7. Held-review and deferred items added in v40

These targets are tracked for future intake. None are blockers for v40 application.

- **Marriages-subsection sweeps for the 1616, 1618, 1619, 1620 annual returns** (pages 00726/00727, 00731/00732, 00733/00734, 00735/00736) to locate any Francis Gurney + Margaret marriage if it took place at East Dereham. The 1617 sweep is the only marriages sweep performed to date.
- **Burials-subsection sweeps for the 1616-1620 annual returns and a pre-00726 burials section** to test whether Margaret Rybett's burial sits in this register.
- **Duplicate-scan overlay-diff images** for the probable pairs (00720/00721, 00726/00727, 00733/00734, 00735/00736). Cheap to produce; would confirm or refute the duplicate-scan pattern at pixel level.
- **Early-section (00693-00714) thin enhanced crops** for the 1590s window; exploratory hunt for Francis G14's own baptism.
- **In-parchment year heading on page 00725 (or adjacent register pages)**, if it exists outside the current crop boxes. The 00725 burial year is currently inferred from sequence (1615 OS); a direct in-parchment year would convert this from I-class to D-class on the year specifically.

## 8. Audit checklist

Before declaring this patchset applied, confirm each item:

- [ ] `data/sources.json` has one new source ID: `fs-vnn2-4vc-marye-gurney-baptism-east-dereham`.
- [ ] `data/sources.json` `notes` field appended (not replaced) for `fs-vnn2-scf-edward-gurney-baptism-east-dereham`, `fs-vnn2-wr2-marye-gurney-burial-east-dereham`, `fs-vnn2-wrg-agnes-gurney-burial-east-dereham`.
- [ ] New validation file created at `sources/validations/east-dereham-pd-86-41-register-structure-and-chronology.md`.
- [ ] `research/people/g14-francis-gurney-fact-sheet.research.md` has one new subsection inserted immediately after the V39-inserted "East Dereham children — primary index expansion and Entries B/C reclassification" block.
- [ ] Case-file §4.2 children table rows for Entries B, C, and D refined as specified.
- [ ] Case-file §4.2 has the new prose paragraph inserted immediately after the V39-inserted reclassification paragraph.
- [ ] Case-file footnote `n102` inserted after the V39-inserted `n101`.
- [ ] Case-file header `caseMeta` Version field bumped to 4.2.
- [ ] V39 §7 held-review Margaret-daughter-of-ffrancis-Gurnoe row removed from any active tracking; Margaret Rybett burial target carried forward as still unlocated.
- [ ] `research/topics/east-dereham-parish-register-paleography.md` exists and is the primary cross-reference for downstream research.

## 9. Session traceability

Input packets and working artifacts (all under `sources/media/Parish_Register_East_Dereham/`):

- `burial-analysis.md`
- `crop-index.md`
- `page-00725-deep-analysis.md`
- `page-00732-marye-ffrancis-gurnoe-terminal-analysis.md`
- `followup-burial-image-analysis-2026-05-15.md`
- `next-pull-results-2026-05-15.md`
- `page-00725-second-opinion-verification.md`
- `page-00725-second-opinion-verification-addendum.md`
- `broader-register-scan-findings.md`
- `consolidation-note-2026-05-15.md`
- `next-pull-specifications.md`
- `east-dereham-paleographic-analysis-comprehensive-2026-05-15.md`

Generated image artifacts (selection; full list in §5 of the comprehensive analysis file):

- Page-00725: `page_00725_line_*.png`, `page_00725_marye_*_magnification_sweep.png`
- Page-00732: `page_00732_line_margaret_ffrancis_gurnoe_sweep.png`, `page_00732_surname_terminal_comparison_00721_00725.png`
- Page-00715: `page_00715_entry_e_john_six_state_sweep.png`
- Page-00721: `page_00721_line_edward_ffrancis_gurnie_sweep.png`
- Heading sweeps: `page_00735_heading_year_sweep.png`, `page_00736_marye_1618_source_mismatch_context.png`, `page_00726_00727_heading_year_sweep.png`
- Marriages scan: `pages_00728_00729_00730_marriages_section_sweep.png`
- Negative passes: `page_00733_gurney_negative_pass_line_strips.png`, `page_00734_*`, `page_00735_*`

Tooling: `tools/east_dereham_image_sweeps.py`.

These artifacts are working analysis files and remain in `sources/media/Parish_Register_East_Dereham/`. The comprehensive analysis file is the deep-reference document; the topic narrative at `research/topics/east-dereham-parish-register-paleography.md` is the frequently-accessed summary; the validation note at `sources/validations/east-dereham-pd-86-41-register-structure-and-chronology.md` is the source-traceability layer.
