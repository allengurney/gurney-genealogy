# Intake patchset v20 - John Gurney TAG 10:70-73 obtained text and Mendon Proprietors corroboration

```yaml
patchset_id: v20
created: 2026-05-09
repo_scope: gurney-genealogy
phase: phase_1_patchset_only
primary_case_file: research/case-files/john-gurney-case-file-v4.md
primary_research_file: research/people/g13-john-gurney-fact-sheet.research.md
working_memo: sources/intake/working/john-gurney-audit-state.md
phase_2_rule: Apply only after review. Do not create corpus-supplement files for the short Holman extract or the short Mendon proprietors extract; both are short enough to live in research with citation.
```

## 0. Audit report

### 0.1 Scope

Two online-accessible primary/print sources were obtained in the 2026-05-09 lead-work pass:

1. Mary Lovering Holman, "Grissell of the Many Marriages," *The American Genealogist* vol. 10 (1933-34), pp. 70-73 — full article text via Internet Archive issue `sim_american-genealogist_1933-10_10_2`.
2. *The Proprietors' Records of the Town of Mendon, Massachusetts* (1899) — full text via Internet Archive item `proprietorsrecor00mend`.

These two pulls produce three case-file-relevant updates:

- A small new specific detail for the Grizzell marriage line (officiant Peter Brackett).
- A negative finding that controls Anderson's 1636 date: TAG 10:70-73 does NOT contain a 1636 arrival or birth date for John Gurney. Anderson's 1636 must derive from a different citation in his bracketed source list, almost certainly the Newgate-apprentice tradition behind WJ 2:422.
- A direct print citation that names BOTH "John Gurny" and "Grisel Gurney" as twenty-acre Mendon proprietors. This complicates the existing G13 phrasing that John "appears to have died with no land" and that Grizzell merely "applied for John's Mendon lot."

### 0.2 Lead triage outcome

| Lead | Work done | Outcome | Incorporation decision |
|---|---|---|---|
| TAG 10:70-73 (Holman, "Grissell of the Many Marriages") | Located issue 1933-10 vol. 10 iss. 2 on archive.org; full text confirmed; opening line and Gurney section read | Obtained and usable. Article gives marriage at Braintree by Peter Brackett 12 Nov 1661, John Gurney died 1662-63, no children with Grizzell, no 1636 arrival or birth claim for John. | Update existing footnote n7 to cite the obtained article directly with the new Peter Brackett officiant detail; add a footnote/footnote update explicitly noting that Holman gives no 1636 date for John, redirecting Anderson's 1636 cite trail to WJ 2:422 / Newgate. |
| Mendon Proprietors' Records online | Located archive.org item `proprietorsrecor00mend`; full text confirmed; Gurney mentions extracted | Obtained and usable. First-proprietors block lists "John Gurny, a twenty acre lot" and separately "Grisel Gurney, a twenty acre lot." | Add new source record for the printed Mendon proprietors volume; add thin validation note; refine existing G13 land-and-property paragraph to reflect the printed-record statement that John (not only Grizzell) appears in the proprietor list. Preserve the chronological tension (Mendon incorporation 1667, John d. 1662/3) as a documented qualifier rather than smoothing it over. |
| Anderson's 1636 arrival source-trail | Cross-checked TAG 10:70-73 obtained text against Anderson's bracketed source list at GMD p. 158 | Negative result: TAG is eliminated as the 1636 source. Most likely 1636 source remaining in the bracketed list is Winthrop's *Journal* 2:422, the 21 Jul 1636 entry already in the audit-state about Newgate's apprentice. | Use as a footnote refinement and as a research-file note in G13 strengthening the two-Johns interpretation. Do not change the case-file probability table for v20. |
| Pease pennyghael.org.uk Gurney.pdf retry | Attempted; ECONNREFUSED in this pass | Inaccessible in this pass; prior Margaret Ryvett finding from this PDF already in case file | No change in v20. Carry forward as future re-pull. |
| Daniel Shed genealogy (Frank Shedd, 1921) for Mary Gurney parentage | Read opening section of full text on archive.org; checked WikiTree Mary (Gurney) Shed sources | Negative for primary citation. Shedd 1921 is cited by WikiTree but the parentage is not sourced to a primary record. | No change. Mary's parentage continues to rest on the existing History of Weymouth "called John Gurney father" relationship statement plus the Sprague family-group summary. |
| Haberdashers 1632 John Gurney apprentice | Checked ROLLCO (londonroll.org) | ROLLCO does not currently index Haberdashers' or Merchant Taylors' Companies. Free online index path does not exist. | No change. Keep as Tier-1B target via Findmypast London Apprenticeship Abstracts or Guildhall Library, not as a 2026-05-09 v20 pull. |
| St Ann Blackfriars 1615 baptism (P/F Gurney) | Checked Harleian Society publication lists, FamilySearch wiki, and a parish overview PDF | No printed-register transcription of St Ann Blackfriars baptisms found freely online. Original is at LMA; Ancestry/Findmypast access is paywalled. | No change. Keep as paleography target requiring LMA/paywall access. |
| SPR Case #338 (John Gurney probate) | No new public-domain image surfaced; the Suffolk Probate index entry already accepted in audit-state remains the controlling secondary trail | Inaccessible in this pass without AmericanAncestors / FamilySearch image rights | No change. Keep as Tier-1 target. |
| Wilson v. Faxon 1653 deposition full case | No public online stream located beyond the printed NEHGR 62:94 abstract already in the case file | Inaccessible in this pass | No change. Keep as targeted Massachusetts Archives pull. |

### 0.3 Candidate implications

- The 2026-05-09 pulls do not change the Candidate B/A/C probability table.
- The TAG negative result on 1636 strengthens the existing two-Johns/Newgate framing already in the audit-state and case file. Anderson's "1636" should be read as inheriting the Newgate-apprentice record, not as independent evidence of John Gurney-1's arrival year.
- The Mendon proprietors print citation does not exclude any candidate but tightens the Mendon context for both John and Grizzell. It should be incorporated as a small refinement to the John1 land-and-property paragraph, not as a candidate-altering datum.

## 1. Source registry operation

Before applying, verify the proposed source ID is still absent:

```powershell
Select-String -Path data\sources.json -Pattern "mendon-proprietors-records-1899"
```

Add this object near the existing colonial Massachusetts John Gurney sources in `data/sources.json`:

```json
    "mendon-proprietors-records-1899": {
      "shortTitle": "Mendon proprietors' records, 1899 print",
      "fullTitle": "The Proprietors' Records of the Town of Mendon, Massachusetts: Incorporated May 15, 1667",
      "publisher": "Town of Mendon, Massachusetts (with Uxbridge, Northbridge, Milford, Blackstone, and Hopedale)",
      "year": 1899,
      "type": "town record (printed)",
      "url": "https://archive.org/details/proprietorsrecor00mend",
      "notes": "Printed transcription of the manuscript proprietors' records. First-proprietors roster names both 'John Gurny' and 'Grisel Gurney' as twenty-acre proprietors."
    }
```

No new source record is needed for TAG 10:70-73 because the existing `tag-10-70` source already covers it; this patchset only updates the footnote text and adds the Holman extract reference URL.

## 2. Validation note (proposed thin file)

Create `sources/validations/mendon-proprietors-records-1899.md` with the following content. Keep it thin per the validation rules — substantive findings live in `g13-john-gurney-fact-sheet.research.md` and the case file.

```markdown
# Validation - Mendon proprietors' records, 1899 print

- Source ID: `mendon-proprietors-records-1899`
- Title: *The Proprietors' Records of the Town of Mendon, Massachusetts: Incorporated May 15, 1667* (1899 print of the manuscript records).
- Online: https://archive.org/details/proprietorsrecor00mend
- Method: Internet Archive full-text search of the OCR derivative for `Gurney`, `Gourney`, `Gurny`, and `Grisel`.
- Use in Gurney research: cited in `research/people/g13-john-gurney-fact-sheet.research.md` and `research/case-files/john-gurney-case-file-v4.md` as the printed first-proprietors source naming both John Gurny and Grisel Gurney as twenty-acre Mendon proprietors. Page-image verification of the proprietor block recommended before quoting.
```

## 3. Proposed case-file edits (research/case-files/john-gurney-case-file-v4.md)

### 3.1 Update endnote n7 to cite the obtained Holman article and the Peter Brackett officiant detail

Old:

```html
<li id="n7" value="7">Braintree, Massachusetts, town vital records, marriage entry for John Gurney and Grizzell Fletcher, 12 Nov. 1661; Mary Lovering Holman, "Grissell of the Many Marriages," <em>The American Genealogist</em>, vol. 10 (1933), pp. 70–73, for Grizzell's sequence of marriages and John as her fourth husband. Source ID: <code>tag-10-70</code>. <a class="backref" href="#ref-7">↩</a></li>
```

New:

```html
<li id="n7" value="7">Braintree, Massachusetts, town vital records, marriage entry for John Gurney and Grizzell Fletcher, 12 Nov. 1661; Mary Lovering Holman, "Grissell of the Many Marriages," <em>The American Genealogist</em>, vol. 10, no. 2 (October 1933), pp. 70-73, Internet Archive, <a href="https://archive.org/details/sim_american-genealogist_1933-10_10_2">https://archive.org/details/sim_american-genealogist_1933-10_10_2</a>, giving the marriage at Braintree by Peter Brackett, 12 Nov. 1661, John Gurney Sr.'s death in 1662-63, and Grissell's full marriage sequence Jewell - Griggs - Kibby - Gurney - Burge. Holman supplies no 1636 arrival or birth date for John Gurney; Anderson's 1636 in <em>Great Migration Directory</em> p. 158 must derive instead from his other bracketed citations, almost certainly Winthrop's <em>Journal</em> 2:422 / the 1636 Newgate apprentice tradition. Source ID: <code>tag-10-70</code>. <a class="backref" href="#ref-7">↩</a></li>
```

### 3.2 Refine §13.2 Primary Sources table row for SPR Case #338 — no change

(Listed only to confirm no change in v20.)

### 3.3 Optional new endnote and case-file paragraph for Mendon proprietors

If accepted, add a sentence to the existing land/property discussion of John1 (currently in the bibliography section, but the substance lives in G13). Suggested case-file additional sentence inside the supplemental burial-place paragraph or its neighbor:

```html
<p>The 1899 printed transcription of the Mendon proprietors' records lists "John Gurny, a twenty acre lot" and separately "Grisel Gurney, a twenty acre lot" within the first-proprietors roster, providing direct print evidence that both John and his widow appear as Mendon proprietors. Mendon was not incorporated until 15 May 1667, after John1's 1662-63 death, so John's name in the printed roster reflects either an early grant carried into the post-incorporation list or a retrospective allottee record; the chronology should be preserved as a qualifier rather than smoothed over.<sup class="fn"><a href="#nXX" id="ref-XX">XX</a></sup></p>
```

Add new endnote (number to assign on application; current endnotes run through `n71`):

```html
<li id="nXX" value="XX"><em>The Proprietors' Records of the Town of Mendon, Massachusetts: Incorporated May 15, 1667</em> (Mendon, Mass., 1899), first-proprietors roster, listing "John Gurny, a twenty acre lot" and "Grisel Gurney, a twenty acre lot"; Internet Archive, <a href="https://archive.org/details/proprietorsrecor00mend">https://archive.org/details/proprietorsrecor00mend</a>. Source ID: <code>mendon-proprietors-records-1899</code>. <a class="backref" href="#ref-XX">↩</a></li>
```

## 4. Proposed G13 research-file edits (research/people/g13-john-gurney-fact-sheet.research.md)

### 4.1 Refine the existing land-and-property paragraph

Current G13 phrasing:
> "John appears to have died with no land. The NPS Cultural Landscape Report for Adams National Historical Park identifies him among early Braintree tenants occupying land within the future park boundaries."

And later:
> "Grizzell became a Mendon proprietor and received a 20-acre allotment in December 1663. After John's death, she applied for his Mendon lot (NEHGR 22:44)."

Suggested adjustment:
> "John appears to have held no Braintree freehold at death; the NPS Cultural Landscape Report for Adams National Historical Park identifies him among early Braintree tenants occupying land within the future park boundaries. The 1899 printed Mendon proprietors' records nevertheless list both 'John Gurny, a twenty acre lot' and separately 'Grisel Gurney, a twenty acre lot' within the first-proprietors roster. Because Mendon was not incorporated until 15 May 1667, John's name in the post-incorporation print stream is most plausibly explained by a pre-incorporation Mendon grant carried into the proprietor list or by a retrospective allottee record; preserve the chronology as a qualifier and pull the underlying manuscript proprietors' records before treating either reading as final."[^mendon-proprietors-1899]

Footnote:

```markdown
[^mendon-proprietors-1899]: *The Proprietors' Records of the Town of Mendon, Massachusetts: Incorporated May 15, 1667* (1899 print), first-proprietors roster; Internet Archive, https://archive.org/details/proprietorsrecor00mend. Source ID: `mendon-proprietors-records-1899`.
```

Keep the existing NEHGR 22:44 reference for the widow's claim; do not delete it.

### 4.2 Refine the existing Anderson + Newgate de-conflation note

Add a single sentence inside the existing "Anderson + Banks assessment" or "Newgate apprenticeship / 1636 record" section confirming that TAG 10:70-73 has now been read in full and contains no 1636 date for John Gurney. Suggested wording:

> "TAG 10:70-73 has now been read in full from Internet Archive issue `sim_american-genealogist_1933-10_10_2`. Holman gives no 1636 arrival or birth date for John Gurney. Anderson's 1636 in *Great Migration Directory* p. 158 therefore cannot inherit from TAG 10:70-73 and most plausibly inherits from WJ 2:422 / the Newgate-apprentice tradition already documented in this file."

### 4.3 Refine the existing TAG 10:70-73 row in the source pull table

Old:

```markdown
| TAG 10:70–73 | *The American Genealogist*, vol. 10, pp. 70–73 | Not yet pulled | **Highest** |
```

New:

```markdown
| TAG 10:70–73 | *The American Genealogist*, vol. 10, no. 2 (Oct. 1933), pp. 70–73 | Pulled 2026-05-09 from Internet Archive `sim_american-genealogist_1933-10_10_2`; Holman gives Peter Brackett officiant detail and no 1636 date | Resolved (low remaining priority) |
```

## 5. Apply order

When approved:

1. Add `mendon-proprietors-records-1899` to `data/sources.json`.
2. Create `sources/validations/mendon-proprietors-records-1899.md` (thin).
3. Edit `research/case-files/john-gurney-case-file-v4.md` per §3.
4. Edit `research/people/g13-john-gurney-fact-sheet.research.md` per §4.
5. Update `sources/intake/working/john-gurney-audit-state.md` to mark v20 as applied.
