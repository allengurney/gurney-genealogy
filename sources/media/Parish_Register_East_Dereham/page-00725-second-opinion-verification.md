# East Dereham page 00725 second-opinion paleographic verification

Reviewed 2026-05-15. Independent verification pass over the prior AI assistant's reading of `gbprs_norfolk_pd_86-41_00725.jpg` and related page-00732 lead. No OCR or HTR used. Same-hand comparator paleography only. Evidence classes follow the procedure document's legend (D direct, R reconstructed, I interpretive).

## Overall assessment

The prior AI's burial-classification of page 00725 is supported by direct in-page evidence I did not see called out as crisply in the deep-analysis file: the same hand uses the explicit word "Buried" on at least two adjacent lines (Robert/Mary lead-in zone), and the page carries standalone "[Name] the wife of [Husband] [date]" forms (Cooke line) that are characteristic of burial registers and absent on the confirmed-baptism comparator page 00721. The prior reading of the Marye and Agnes lines as a Gurny family-cluster burial pair is largely confirmed, with the Agnes reading firm and the Marye reading carrying a real but bounded uncertainty in the relationship token and month. The FS index "Susan" for the Agnes line is not supported by the visible letterforms. The Margaret-wife-of-ffrancis burial target is not visible on 00725 within the reviewed crops. The 00732 Margaret-baptism lead was UNCERTAIN at the resolutions available to this pass; a later focused crop resolves that line as Marye, not Margaret.

## Claim-by-claim verdicts

### C1 — Page 00725 is a BURIAL page, not a baptism page

- **Verdict:** CONFIRM
- **Evidence class:** D (the word "Buried" is directly visible on the page) + I (form-level inference)
- **Reasoning:**
  - The `page_00725_line_robert_mary_leadin_sweep.png` shows two adjacent entries where the verb "Buried" is legible in raw, autocontrast, and contrast+sharp views: a "Robart ... was Buried November 21" line and a following "Mary ..." line with a November date. The "B-u-r-i-e-d" letter sequence with the long descender on the "B" is consistent across enhancement states and matches secretary-hand "Buried" terminal-d formation.
  - The `page_00725_line_margaret_richard_cooke_sweep.png` shows a standalone "[Name] the wife of Richard Cooke [Aprill?] [date]" form. Standalone wife-of-husband as the subject of a dated single-line entry is the canonical burial-register form for an adult woman; baptism registers record the wife only as the mother in the context of a named child's baptism.
  - Comparator contrast: the confirmed-baptism page 00721 (`candidate_721_edward_francis_gurnie_wide.png`) shows the verb "baptized" before the date on each entry ("Edward ... baptize[d] may 27"; "Agnes ... baptize[d] may 28"). No such "baptize[d]" token appears in the 00725 entries reviewed.
- **Source images / positions:** `page_00725_line_robert_mary_leadin_sweep.png` (upper-middle of page, lines immediately above the Gurny cluster); `page_00725_line_margaret_richard_cooke_sweep.png` (upper page); `candidate_721_edward_francis_gurnie_wide.png` (negative-comparator).

### C2 — Marye line reads "Marye ... of ffrancis Gurny", date January 25, relationship word damaged

- **Verdict:** CONFIRM (with bounded uncertainty as the prior AI flagged)
- **Evidence class:** D for "Marye", "ffrancis Gurny", and the numeral "25"; I for the month being "January" and for the relationship word being damaged rather than absent
- **Reasoning:**
  - "Marye" at line-start is firm across all six enhancement states in `page_00725_line_marye_ffrancis_gurny_sweep.png`: the opening "M" has the expected two-peak secretary-hand form, followed by short "a-r-y-e".
  - "ffrancis Gurny" is firm in the comparator-rich middle of the line; the double-f opening matches the same-hand `ffrancis` exemplar on `candidate_724_725_mary_agnes_francis_gurny.png` and on `candidate_721_edward_francis_gurnie_wide.png`. The "G" of Gurny has the same closed-loop form as the Agnes-line Gurny immediately below it.
  - The numeral "25" at the right end of the line is clear in raw-resized and existing-enhanced views.
  - The relationship token between "Marye" and "of ffrancis" is short (4–5 character widths), partially obscured by bleed-through staining. It does not resolve to "the daughter" (too short) or "the sonne" (initial stroke does not match secretary-hand "s"). The token reads more like "the n[?]ce" / "the ne[?]" — possibly "the neece" / "the n[ie]ce" / "the nephew" — but I would not extract any specific relationship from this line without further work.
  - The month preceding "25" is not as crisp as the prior AI's "January" call. Stroke rhythm is compatible with "January" but also with "Iuly" / "Iuny" depending on enhancement state. Marking the month as I-class.
- **What I see instead, where I diverge from the prior AI:** I would not write the relationship word as merely "damaged"; the visible stroke count and shape positively disfavor "daughter" and "sonne" and lean toward a shorter relationship token (niece/nephew or similar). The month should be tagged as inferred rather than directly read.
- **Source images / positions:** `page_00725_line_marye_ffrancis_gurny_sweep.png` (lower-third of page); `candidate_724_725_mary_agnes_francis_gurny.png` (same-hand comparator).

### C3 — Agnes line reads "Agnes the daughter of ffrancis Gurny", date January 31; FS "Susan" (VNN2-WRG) is an indexer mis-read

- **Verdict:** CONFIRM "Agnes the daughter of ffrancis Gurny"; REFUTE "Susan"
- **Evidence class:** D for "the daughter of ffrancis Gurny" and "31"; I for "Agnes" vs "Susan" adjudication
- **Reasoning:**
  - "the daughter of ffrancis Gurny" is firm across all six enhancement states in `page_00725_line_agnes_ffrancis_gurny_sweep.png`. The "daughter" token shows a clean opening "d" with descending shoulder into "augh"; "ffrancis" matches the same-hand double-f exemplar pattern; "Gurny" matches the Marye-line Gurny on the previous register line.
  - The given-name opening is short (5 character widths), with an initial stroke that resolves as a leftward-opening triangular cap with a horizontal cross-stroke — that is, a capital "A" architecture, not the round-curving opening of a capital "S".
  - The body of the word after the opening reads as "g-n-e-s" rhythm: a low-loop "g", a short connected mid-body, and a terminal "s" with the typical secretary-hand drop. This is consistent with "Agnes".
  - "Susan" / "Susanna" is implausible: it would require an opening "S" (round-curve) and a longer body (5 letters for "Susan", 7 for "Susanna"); neither the opening shape nor the body length matches.
  - The numeral "31" is clear in raw-resized and existing-enhanced views.
  - There is a short word between "Gurny" and "31" (visible in raw and contrast+sharp views) that I would read as "buryd" / "Bury'd" — this directly reinforces C1.
- **What I see instead of "Susan":** "Agnes" is the correct visual reading. The FS index "Susan" appears to be a transcription error.
- **Source images / positions:** `page_00725_line_agnes_ffrancis_gurny_sweep.png` (lower-third of page, line immediately below the Marye line).

### C4 — No visible burial for "Margaret wife of ffrancis Gurnie/Gurney/Gurny" or Rybett/Ryvett variant on page 00725

- **Verdict:** CONFIRM
- **Evidence class:** I (page-scan negative finding)
- **Reasoning:**
  - I scanned `crop_00725_enhanced.png` plus the upper, middle, and lower enhancement sweeps and each line-level sweep listed in the deep-analysis file.
  - The only Margaret-form entry I find on the page is the "[Name] the wife of Richard Cooke" line, where the husband is Cooke, not Gurney. The given name in that line is consistent with "Margaret" but the family is not the target.
  - The two Gurny-family entries on the page (Marye and Agnes) read as relative-of-ffrancis, not wife-of-ffrancis.
  - No "Rybett" / "Ryvett" letterform appears in any line I reviewed. Initial-letter scan for "R" + medial double-stroke confirms no candidate.
- **Source images / positions:** `crop_00725_enhanced.png` (whole page); `page_00725_line_margaret_richard_cooke_sweep.png` (Cooke disambiguation).

### C5 — No visible burial for Margaret wife of ffrancis Gurney anywhere in 00725, 00728–00736, 00750–00768

- **Verdict:** UNCERTAIN (independent confirmation deferred)
- **Evidence class:** I
- **Reasoning:**
  - My pass independently verified absence on 00725 only (see C4).
  - I did not perform a line-level re-scan of 00728–00736 or 00750–00768 in this verification pass; doing so would replicate, not verify, the prior AI's broad-pass survey.
  - The prior AI's broad-pass survey (`burial-analysis.md`) is internally consistent and I have no evidence pointing the other way, but it remains a broad-pass result. UNCERTAIN is the correct verification verdict at this scope.
- **Recommendation:** if the patchset hinges on a hard "no Margaret-wife-of-Francis burial entry anywhere", commission a separate line-level negative-pass review with focused line crops of each candidate page before promoting C5 from "no entry seen" to "no entry exists".

### C6 — 00732 line formerly tentatively read as "Margaret"; focused follow-up resolves it as Marye

- **Verdict:** UNCERTAIN
- **Evidence class:** D for the year heading; I for the line-level reading itself
- **Reasoning:**
  - The raw `gbprs_norfolk_pd_86-41_00732.jpg` shows a year notation in the upper-right corner of the page above the parchment that reads as **"1618-1[9]"**. This is the strongest year anchor I observed in this pass and is consistent with the prior AI's 1618–19 christenings characterization.
  - The page opens with a preamble paragraph ("Hees ffolios Indented..." or similar), followed by a christenings list. Entry format on this page is the bare "[Name] the [son/daughter] of [Parent] [month] [date]" form, without an explicit "baptized" verb, which is acceptable register style for a section under a "Christenings" heading.
  - At the resolutions and crops available in this verification pass, I could not independently locate and stroke-verify a specific "Margaret the daughter of ffrancis Gurnoe/Gurney" line on this page. This point is superseded by the follow-up crop, which resolves the target line as Marye, not Margaret.
  - The proposed reading is plausible (right page type, right era, same-hand register), but UNCERTAIN until a focused line crop is generated.
- **What is needed:** a `page_00732_line_margaret_ffrancis_gurnoe_sweep.png`-style focused crop with the six-state enhancement panel used on 00725, plus an explicit comparison of the surname terminal ("-oe" vs "-ey") against the same-hand Gurny/Gurnie forms on 00721 and 00725.
- **Source images / positions:** `gbprs_norfolk_pd_86-41_00732.jpg` (page header and overall layout); `crop_00732_enhanced.png` (page-level enhanced).
- **Follow-up result, 2026-05-15:** `page_00732_line_margaret_ffrancis_gurnoe_sweep.png` was created and resolves this item against the tentative Margaret reading. The focused line reads `Marye the daughter of ffrancis Gurnoe bapt may 25`; see `page-00732-marye-ffrancis-gurnoe-terminal-analysis.md` and `page_00732_surname_terminal_comparison_00721_00725.png`.

## Open-question answers

### Q1 — Year heading or year context on or near page 00725?

- **Answer:** No explicit year heading is visible within the supplied `crop_00725_enhanced.png` bounds `(1605, 650, 3135, 3355)` or in the corresponding region of the raw image. The page is a year-crossing burial sequence running from April through late January (the Marye/Agnes "25" / "31" datelines fall at the tail). Inference: this is one calendar year of burials. Year value remains inferential and should not be hardcoded without an external anchor (an adjacent-page heading, FS waypoint metadata, or a section title on the verso/recto of 00724/00725).
- **Evidence class:** I

### Q2 — Other Gurney/ffrancis lines on 00725 not called out, especially any "wife"-relationship line?

- **Answer:** I see no additional Gurney/ffrancis line on 00725 beyond the Marye and Agnes pair that the prior AI already called out. The middle-family-cluster sweep is dominated by bleed-through stain in the contrast 2.0 view; under autocontrast and contrast 1.6 the readable entries appear to involve other surnames (Lenny, Cooke, William/Mullian-like forms), not additional Gurney entries. No "wife of ffrancis" form was found in any reviewed crop.
- **Evidence class:** I

### Q3 — Does 00715 Entry E support "John the sonne of ffrancis Gurnie" at first glance, vs FS index "John the sonne of Nicholas Gorne"?

- **Answer:** UNCERTAIN at this verification scope. I did not re-run the four-test letterform adjudication, and I was not supplied with the canonical `line_05_enh_x3.png` target crop in the active workspace. The procedure document (the methodology file read at task start) records four discrete tests, each independently favoring `ffrancis` over `Nicholas`, with no test favoring `Nicholas` — that is the prior evaluation's bottom line. A first-glance same-hand comparison against the same-hand `ffrancis` exemplars on 00721 and 00725 is consistent with `ffrancis Gurnie` being a viable reading, but I will not promote that observation to a CONFIRM without re-running the line-05 crop sweep. UNCERTAIN.
- **Evidence class:** I

### Q4 — Anything else material to the family research file?

- **Answer:** Two items worth flagging.
  1. The word "Buried" on the page 00725 Robert/Mary lead-in line (`page_00725_line_robert_mary_leadin_sweep.png`) is the cleanest direct-class evidence of the page's burial classification. The current `page-00725-deep-analysis.md` characterizes the page as a burial list but does not appear to anchor that classification on a specific in-page legible "Buried" token. Anchoring on this concrete token strengthens the case-file rewrite and shortens the audit trail.
  2. The 00732 page header carries a legible **"1618-1[9]"** year notation in the upper-right corner of the parchment. This is the strongest year anchor I encountered in this pass. It is worth recording in the source-validation note for 00732 alongside the follow-up reading of the line as Marye daughter of ffrancis Gurnoe.

## Differences from the prior AI reading

- **Stronger anchor for C1 (burial classification):** I rely on the directly legible "Buried" token on the Robert/Mary lead-in line plus the standalone "wife of Richard Cooke" form. The prior deep-analysis file frames the burial classification more interpretively and notes the Cooke line as a non-target rather than as positive evidence for the page being a burial register. My read promotes the Cooke line from non-target to genre-evidence.
- **Tighter framing on C2 (Marye line):** I would not record the damaged relationship word as merely "damaged"; the visible stroke shape positively disfavors "daughter" and "sonne" and is more compatible with a shorter relationship token (niece/nephew family). The prior AI's flag is sound but undersells what the strokes can rule out. Also, the month should be flagged as inferred rather than treated as a confirmed "January".
- **Same conclusion, different confidence on C3 (Agnes/Susan):** I agree the indexer's "Susan" is a mis-read. My adjudication leans on the capital-A architecture of the initial letter and on word-length mismatch with "Susan/Susanna", which I would record as the primary refutation reasons.
- **More cautious on C5:** the prior AI's broad-pass survey is the correct first-pass result, but I would not promote it to a confident "no such entry exists anywhere" without a line-level negative-pass on 00728–00736 and 00750–00768. The patchset should preserve this distinction.
- **More cautious on C6:** the prior AI calls the 00732 Margaret line "probable"; my read held at UNCERTAIN pending a focused line crop. The follow-up crop now resolves the line as Marye, not Margaret.

## Recommended next image pulls

In priority order:

1. **Completed: `page_00732_line_margaret_ffrancis_gurnoe_sweep.png`** — focused 6-state enhancement panel of the formerly suspected Margaret-daughter-of-ffrancis line on 00732. The follow-up refutes the Margaret reading and resolves the entry as Marye daughter of ffrancis Gurnoe.
2. **Year-anchor crop for 00725** — the parchment heading area on the verso/recto of `gbprs_norfolk_pd_86-41_00724.jpg` or the very top of `00725.jpg` outside the current crop box `(1605, 650, ...)`. The current crop excludes the upper margin; a fresh crop including the page heading would settle Q1.
3. **Marye-line relationship-token magnification** — a tighter sub-crop of just the 5-character-width token between "Marye" and "of ffrancis" on `page_00725_line_marye_ffrancis_gurny_sweep.png`, at 3x or 4x resize. If this resolves to "the neece" / "the nephew" rather than "the daughter", that materially changes the case file (Marye becomes a Gurney niece/nephew of Francis, not a daughter).
4. **`page_00725_line_marye_ffrancis_gurny_sweep.png` month-token magnification** — a tighter sub-crop of just the month token before "25" to disambiguate January vs Iuly vs Iuny.
5. **00728–00736 and 00750–00768 line-level negative-pass crops** — a thin pass cropping each page's wife-of-husband zone candidates if/when C5 must move from UNCERTAIN to CONFIRM. Lower priority than items 1–4 because the patchset can proceed on a "no entry seen" basis without promoting to "no entry exists".
