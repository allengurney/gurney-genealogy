# Intake patchset v19 - John Gurney Braintree vital-record conflict

```yaml
patchset_id: v19
created: 2026-05-09
repo_scope: gurney-genealogy
phase: phase_1_patchset_only
primary_case_file: research/case-files/john-gurney-case-file-v4.md
primary_research_file: research/people/g13-john-gurney-fact-sheet.research.md
working_memo: sources/intake/working/john-gurney-audit-state.md
phase_2_rule: Apply only after review. Do not create corpus-supplement files for the short extracts in this patchset.
```

## 0. Audit report

### 0.1 Scope

This patchset works the original-record lead behind the case file's Braintree vital-record statements for Mary, first wife of John Gurney, and Grizzell Fletcher/Kibbee, later wife of John Gurney.

The key source examined is Samuel A. Bates, editor, *Records of the Town of Braintree, 1640 to 1793* (Randolph, Mass.: D. H. Huxford, printer, 1886), available at Internet Archive: `https://archive.org/details/recordsoftownofb00brai`.

### 0.2 Lead triage outcome

| Lead | Work done | Outcome | Incorporation decision |
|---|---|---|---|
| 1886 printed Braintree town-record volume | Checked Internet Archive metadata, full text, index hits, and page images for Gurney/Gurny/Gurnie/Guerny, Cheny/Cheney, Kidbee/Kibbee, Fletcher, Jewell, Greggs/Griggs, Grizell/Grizzell | Obtained and usable. Printed p. 638 has the 20 Sept. 1661 death line under Cheny, not Gurney. Printed p. 717 has the 12 Nov. 1661 marriage line as John Cheny Senior and Grizell Kidbee, not John Gurney and Grizzell Fletcher. | Add source record + thin validation. Use in G13 and case file as a conflict note, not as a final correction. |
| Braintree Town Clerk manuscript vital records | Targeted FamilySearch catalog search located the filmed manuscript set: `Births, marriages, intentions of marriage, and deaths, 1640-1848 [Braintree, Massachusetts]`, film 940974 / DGS 7009769 | Online-accessible in a FamilySearch collection but not examined here because record-image access was not available in this pass | No source record. Carry as highest next pull to resolve whether the 1886 printed Cheny readings reflect manuscript text, a transcription error, or a separate Cheney record later conflated with Gurney. |
| TAG 10:70-73, Mary Lovering Holman, "Grissell of the Many Marriages" | Prior v17 searches identified title/author but did not obtain article text | Still not obtained. Critical because it likely explains the Grissell marriage sequence and may reveal whether Holman corrected or reinterpreted the Braintree line. | No new source record beyond existing `tag-10-70`; keep as pull target and explicitly connect it to this conflict. |
| Clemens-derived pre-1699 marriage transcription | Targeted web search found a derivative list under Cheney: John Cheney Sr. and Grizell Kidbee, 12 September 1661, Braintree | Derivative pointer only; the September date misreads old-style 9th month as September rather than November | Do not add source record and do not use in research. The 1886 Braintree page image is the controlling source for v19. |

### 0.3 Candidate implications

- This is a direct pressure point against the current case-file wording, not against Candidate B by itself.
- The accessible printed Braintree volume does not support the current claim that a Braintree vital record directly names Mary Gurney dying 20 Sept. 1661 or John Gurney marrying Grizzell Fletcher/Kibbee on 12 Nov. 1661.
- The dates are the same as the Gurney tradition, so the conflict is not random. The plausible explanations are: printed transcriber error from an original Gurney/Gurny line; later Gurney compilers reattributing a Cheney line because of separate Grisel Gurney evidence; or TAG/Sprague/Torrey using another record stream not yet inspected.
- The Mendon proprietary record stream proposed in v18 remains important because it independently preserves Grisel Gurney/Widow Gurny in the Juell/Kibbee/Burge network. This v19 conflict should therefore qualify the Braintree vital citation, not erase Grizzell from the John Gurney research file.

## 1. Source registry operation

Before applying, verify the proposed source ID is still absent:

```powershell
Select-String -Path data\sources.json -Pattern "braintree-records-1640-1793-1886"
```

Add this object near the existing colonial Massachusetts John Gurney sources in `data/sources.json`:

```json
    "braintree-records-1640-1793-1886": {
      "shortTitle": "Braintree town records, 1640-1793",
      "citation": "Braintree (Mass.). Records of the Town of Braintree, 1640 to 1793. Edited by Samuel A. Bates. Randolph, Mass.: D. H. Huxford, printer, 1886.",
      "archive": "Internet Archive; FamilySearch catalog also lists the printed volume",
      "url": "https://archive.org/details/recordsoftownofb00brai",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/braintree-records-1640-1793-1886.md",
      "notes": "Published Braintree town-record transcription. For the John Gurney case file, the important conflict is in the vital-record section: printed p. 638 gives the 20 Sept. 1661 wife-death line under John Cheny, and printed p. 717 gives the 12 Nov. 1661 marriage line as John Cheny Senior and Grizell Kidbee. Use as a conflict source against the current Braintree vital-record wording; the original town manuscript and TAG 10:70-73 remain necessary before treating the Cheny reading as final."
    },
```

Do not create a corpus supplement for this source in v19. The extracts are short and belong in research with citation.

## 2. Validation file

Create `sources/validations/braintree-records-1640-1793-1886.md`:

```markdown
# Source validation: Braintree town records, 1640-1793

**Source ID:** `braintree-records-1640-1793-1886`

## Examined

Braintree (Mass.), *Records of the Town of Braintree, 1640 to 1793*, ed. Samuel A. Bates (Randolph, Mass.: D. H. Huxford, printer, 1886), Internet Archive item `recordsoftownofb00brai`.

## Scope

- Printed p. 638, death entries around 1659-1662.
- Printed p. 717, marriage entries around 1659-1666.
- Full-text and index searches for Gurney, Gurny, Gurnie, Guerny, Cheny, Cheney, Kidbee, Kibbee, Fletcher, Jewell, Greggs/Griggs, Grizell, and Grizzell.

## Validation result

Usable as a conflict source for the Braintree vital-record foundation in the John Gurney case file.

The printed volume gives the 7th month 20, 1661 wife-death line as "Cheny the wife of John Cheny" and the 9th month 12, 1661 marriage line as "John Cheny Senior and Grizell Kidbee." Those dates correspond to the traditional Mary-death and Grizzell-marriage dates in the Gurney case file, but the printed surname is Cheny/Cheney rather than Gurney.

## Limits

This is an 1886 printed transcription, not the original Braintree town manuscript. The manuscript vital-record set is identified in the FamilySearch catalog as `Births, marriages, intentions of marriage, and deaths, 1640-1848 [Braintree, Massachusetts]`, film 940974 / DGS 7009769, but the images were not examined in this pass.

TAG 10:70-73, Mary Lovering Holman, "Grissell of the Many Marriages," remains a necessary comparison pull for the marriage-sequence interpretation.

## Findings recorded in

- `research/people/g13-john-gurney-fact-sheet.research.md`
- `research/case-files/john-gurney-case-file-v4.md`

## Patchset

`sources/intake/processed/v19-john-gurney-braintree-vital-record-conflict.patchset.md`
```

## 3. G13 research companion edits

File: `research/people/g13-john-gurney-fact-sheet.research.md`

### 3.1 Update the opening summary

In the first paragraph, replace:

```markdown
Later married Grizzell Fletcher on 12 Nov 1661.
```

with:

```markdown
Later marriage to Grizzell Fletcher/Kidbee is traditionally placed at Braintree on 12 Nov 1661, but the accessible 1886 Braintree town-record transcription prints that marriage line under John Cheny Senior and Grizell Kidbee; treat the Braintree vital-record basis as a conflict until the town manuscript or TAG 10:70-73 is checked.
```

### 3.2 Update the Known Facts table

Replace this row:

```markdown
| Second wife: Grizzell Fletcher, m. 12 Nov 1661 | Colonial record set | Confirmed |
```

with:

```markdown
| Second wife: Grizzell Fletcher/Kidbee, traditional m. 12 Nov 1661 | Torrey/Sprague/TAG tradition; 1886 Braintree printed town-record conflict | Conflict to resolve |
```

### 3.3 Replace the Grizzell section opening

In `### Grizzell Fletcher (second wife)`, replace the current first paragraph, numbered marriage list, and sentence about Grizzell's later Mendon lot with:

```markdown
Compiled Gurney sources identify Grizzell as the daughter of Robert Fletcher of Chelmsford, Essex, England, and place John Gurney as her fourth husband after Thomas Jewell, Humphrey Greggs/Griggs, and Henry Kibby/Kibbee. The accessible 1886 Braintree town-record transcription complicates that statement: the 9th month 12, 1661 marriage line is printed as "John Cheny Senior and Grizell Kidbee," and the 7th month 20, 1661 wife-death line is printed as "Cheny the wife of John Cheny." Those two dates correspond to the traditional Gurney chronology, but the printed surname is Cheny/Cheney rather than Gurney.[^braintree-records-1886]

Do not flatten this into a rejection of the Grizzell-Gurney connection. Torrey, Sprague, and TAG preserve the Grizzell marriage sequence, and the Mendon proprietary record stream separately preserves Grisel Gurney/Widow Gurny in the Juell/Kibbee/Burge network. The next source question is whether the original Braintree manuscript reads Gurney/Gurny, whether the 1886 Cheny reading is correct, or whether later compilers merged a Cheney vital line with the Grisel Gurney proprietary evidence.[^braintree-records-1886]

The Chelmsford connection is purely colonial. There is no evidence linking John to Chelmsford, Essex as an English origin point.
```

Add this footnote near the existing G13 footnotes:

```markdown
[^braintree-records-1886]: Braintree (Mass.), *Records of the Town of Braintree, 1640 to 1793*, ed. Samuel A. Bates (Randolph, Mass.: D. H. Huxford, printer, 1886), pp. 638, 717, Internet Archive, https://archive.org/details/recordsoftownofb00brai. Source ID: `braintree-records-1640-1793-1886`.
```

### 3.4 Add to Sources Consulted

Add this row to the `## Sources Consulted` table:

```markdown
| `braintree-records-1640-1793-1886` | Printed Braintree vital-record conflict on the 1661 wife-death and Grizell Kidbee marriage lines | `sources/validations/braintree-records-1640-1793-1886.md` |
```

## 4. Case-file edits

File: `research/case-files/john-gurney-case-file-v4.md`

Note numbering: if v17 and v18 are applied first, use `n81` below. If either patchset is not applied first, renumber this note to the next available endnote after the live file's final note and adjust all `ref-81`/`n81` links.

### 4.1 Update the identity table

Replace the two wife rows:

```markdown
| **Wife** | Mary (maiden name unknown), d. 20 Sept 1661 | Braintree vital records<sup class="fn"><a href="#n6" id="ref-6">6</a></sup> |
| **Second wife** | Grizzell Fletcher, m. 12 Nov 1661 (her 4th husband) | Braintree vital records<sup class="fn"><a href="#n7" id="ref-7">7</a></sup> |
```

with:

```markdown
| **Wife** | Mary (maiden name unknown), traditionally d. 20 Sept 1661; Braintree printed-record surname conflict | Sprague/Torrey tradition; Braintree printed records conflict<sup class="fn"><a href="#n6" id="ref-6">6</a></sup><sup class="fn"><a href="#n81" id="ref-81a">81</a></sup> |
| **Second wife** | Grizzell Fletcher/Kidbee, traditionally m. 12 Nov 1661; Braintree printed-record surname conflict | Torrey/TAG tradition; Braintree printed records conflict<sup class="fn"><a href="#n7" id="ref-7">7</a></sup><sup class="fn"><a href="#n81" id="ref-81b">81</a></sup> |
```

### 4.2 Update the timeline rows

Replace:

```markdown
| 20 Sept 1661 | — | Wife Mary dies, Braintree |
| 12 Nov 1661 | — | Marries Grizzell Fletcher |
```

with:

```markdown
| 20 Sept 1661 | — | Traditional death date for wife Mary; accessible 1886 Braintree transcription prints the same-date wife-death line under John Cheny |
| 12 Nov 1661 | — | Traditional marriage date to Grizzell Fletcher/Kidbee; accessible 1886 Braintree transcription prints the line as John Cheny Senior and Grizell Kidbee |
```

### 4.3 Add a conflict note after the Torrey/Weymouth cross-check paragraph

After the existing paragraph beginning `<h4>Torrey and History of Weymouth: cross-checks on the John1 family group</h4>`, insert:

```html
<h4>Braintree vital-record conflict: Cheny/Cheney vs. Gurney</h4>
<p>The accessible 1886 printed Braintree town-record transcription conflicts with the usual Gurney reading for the 1661 wife-death and remarriage sequence. On printed p. 638, the death entry dated 7th month 20, 1661 is printed as "Cheny the wife of John Cheny," not Mary Gurney. On printed p. 717, the marriage entry dated 9th month 12, 1661 is printed as "John Cheny Senior and Grizell Kidbee," not John Gurney and Grizzell Fletcher/Kibbee. Those dates correspond to the traditional Gurney chronology, so this is a focused source conflict rather than a loose same-name coincidence. The Grizzell-Gurney connection should remain in the case file because Torrey, Sprague, and TAG preserve the marriage sequence and the Mendon proprietary stream separately preserves Grisel Gurney/Widow Gurny; however, the Braintree vital-record citation should be treated as unresolved until the original town manuscript or TAG 10:70-73 is checked.<sup class="fn"><a href="#n81" id="ref-81c">81</a></sup></p>
```

### 4.4 Update the source-pull list

In the `Highest-priority source pulls still needed` list, add this item immediately before TAG or combine with the existing TAG item if v17 has already revised that list:

```markdown
1. **Braintree town manuscript vital records, film 940974 / DGS 7009769** - check the original/copy manuscript pages behind the 7th month 20, 1661 wife-death entry and the 9th month 12, 1661 Grizell Kidbee marriage entry. The 1886 printed transcription reads Cheny/Cheney, not Gurney.
```

If the list is renumbered manually, keep TAG 10:70-73 as the paired follow-up:

```markdown
2. **TAG 10:70-73, Mary Lovering Holman, "Grissell of the Many Marriages"** - compare Holman's marriage-sequence evidence against the Braintree printed Cheny/Cheney reading.
```

### 4.5 Add endnote

Append this note before `</ol>` in the case-file citation index, renumbering if needed:

```html
  <li id="n81" value="81">Braintree (Mass.), <em>Records of the Town of Braintree, 1640 to 1793</em>, ed. Samuel A. Bates (Randolph, Mass.: D. H. Huxford, printer, 1886), p. 638, wife-death line dated 7th month 20, 1661, and p. 717, marriage line dated 9th month 12, 1661, <a href="https://archive.org/details/recordsoftownofb00brai">https://archive.org/details/recordsoftownofb00brai</a>. Source ID: <code>braintree-records-1640-1793-1886</code>. The manuscript lead is Braintree Town Clerk, <em>Births, marriages, intentions of marriage, and deaths, 1640-1848 [Braintree, Massachusetts]</em>, FamilySearch catalog no. 399351, film 940974 / DGS 7009769. <a class="backref" href="#ref-81a">back</a> <a class="backref" href="#ref-81b">back</a> <a class="backref" href="#ref-81c">back</a></li>
```

## 5. Non-applied lead ledger

Do not add source records for these in v19:

- FamilySearch Braintree manuscript vital records: identified but not examined.
- Clemens / New Horizons pre-1699 derivative marriage list: derivative pointer only and date conversion is unreliable.
- TAG 10:70-73: existing source lead remains, but article text was not obtained.

## 6. Validation after Phase 2 application

Run:

```powershell
Select-String -Path data\sources.json -Pattern "braintree-records-1640-1793-1886"
Test-Path sources\validations\braintree-records-1640-1793-1886.md
Select-String -Path research\people\g13-john-gurney-fact-sheet.research.md -Pattern "Braintree printed town-record conflict|Cheny Senior and Grizell Kidbee|braintree-records-1886"
Select-String -Path research\case-files\john-gurney-case-file-v4.md -Pattern "Braintree vital-record conflict|John Cheny Senior and Grizell Kidbee|n81"
git diff --check
```

Expected outcome:

- `data/sources.json` contains exactly one `braintree-records-1640-1793-1886` source record.
- Validation exists and remains thin.
- G13 and the case file preserve the Grizzell-Gurney tradition but mark the Braintree vital-record basis as unresolved.
- No corpus supplement is created.
