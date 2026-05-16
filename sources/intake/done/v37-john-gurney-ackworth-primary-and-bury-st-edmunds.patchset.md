# Intake patchset v37 - Ackworth primary-record confirmation and Bury St Edmunds household

```yaml
patchset_id: v37
created: 2026-05-14
repo_scope: gurney-genealogy
phase: phase_2_research_sources_and_case_file
input_packet: sources/intake/john-gurney-2026May/12May2026-John-Gurney-research-raw.md
sibling_patchset: v38-john-gurney-same-name-household-sweep.patchset.md
phase_2_rule: This patchset carries the two leads from the 12 May 2026 raw research file that change interpretation in the case file. Bulk same-name comparator additions are in v38.
```

## 0. Scope

Two leads from the 12 May 2026 raw research batch carry interpretive weight and update existing case-file content:

1. **Ackworth, Yorkshire.** The Mary Burton marriage and a Yorkshire child baptism are now primary-record reached via Findmypast England Marriages 1538-1973 and England Births & Baptisms 1538-1975. This converts the existing Section 8 Ackworth row from "claimed, no primary record reached" to "primary record reached" and prompts a tight pro/anti read. Probability remains Unlikely.
2. **Bury St Edmunds, St Mary.** A John Gurney burial 11 December 1653 plus 1655 and 1656 same-parish Gurney burials tighten Section 10.6 (Banks's Bury St Edmunds attribution) and add a new Section 8 row.

Bulk same-name comparator household additions (Bucks, Herts, Beds, London, Norfolk, Berks, Worcs, Northants) are handled in sibling patchset v38.

## 1. `data/sources.json` source registry operations

Preserve existing ordering style. Do not reformat the full file.

### 1.1 Add `findmypast-ackworth-gurnoe-burton-marriage-1636`

Insert near the existing `findmypast-uk-parish-baptisms` block.

```json
"findmypast-ackworth-gurnoe-burton-marriage-1636": {
  "shortTitle": "Findmypast England Marriages 1538-1973 - John Gurnoe + Mary Burton, Ackworth, 1636",
  "citation": "England Marriages 1538-1973, Findmypast transcript record R_855220028: John Gurnoe and Mary Burton, marriage 6 June 1636, Ackworth, Yorkshire, England.",
  "archive": "Findmypast",
  "url": "https://www.findmypast.com/transcript?id=R_855220028&tab=this",
  "corpusStatus": "transcript",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/findmypast-ackworth-gurnoe-burton-marriage-1636.md",
  "notes": "Primary record reached for the Ackworth Yorkshire John Gurnoe + Mary Burton marriage previously known only as a claim in compiled genealogies. Surname is transcribed Gurnoe; Burton is the indexed spouse surname, not the older Barton variant carried in some compilations. Marriage date 6 June 1636. The household continued at Ackworth: see paired source `findmypast-ackworth-gurnoe-baptism-1637-john-thomas` for the 19 January 1637 baptism of John Thomas Gurnoe at the same parish."
}
```

### 1.2 Add `findmypast-ackworth-gurnoe-baptism-1637-john-thomas`

```json
"findmypast-ackworth-gurnoe-baptism-1637-john-thomas": {
  "shortTitle": "Findmypast England Births & Baptisms 1538-1975 - John Thomas Gurnoe, Ackworth, 1637",
  "citation": "England Births & Baptisms 1538-1975, Findmypast transcript record R_948023155: John Thomas Gurnoe, male, baptism 19 January 1637, Ackworth, Yorkshire, England; parents not transcribed.",
  "archive": "Findmypast",
  "url": "https://www.findmypast.com/transcript?id=R_948023155&tab=this",
  "corpusStatus": "transcript",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/findmypast-ackworth-gurnoe-burton-marriage-1636.md",
  "notes": "Ackworth parish baptism of John Thomas Gurnoe, 19 January 1637, the year after the John Gurnoe + Mary Burton marriage at the same parish (`findmypast-ackworth-gurnoe-burton-marriage-1636`). Father and mother are not in the transcript index but the household continuity is consistent. First child given a compound name John Thomas — not Sarah — which is the distinctive name discriminator against the colonial John Gurney's first-child Sarah."
}
```

### 1.3 Add `findmypast-bury-st-edmunds-st-mary-gurney-burials-1653-1656`

```json
"findmypast-bury-st-edmunds-st-mary-gurney-burials-1653-1656": {
  "shortTitle": "Findmypast National Burial Index - Bury St Edmunds St Mary Gurney burials 1653-1656",
  "citation": "National Burial Index for England & Wales (Findmypast). Three Gurney burials at St Mary, Bury St Edmunds, Suffolk: John Gurney 11 December 1653; [given name not transcribed] Gurney 6 April 1655; [given name not transcribed] Gurney 13 May 1656 (notes 'Wife'). Anglican denomination.",
  "archive": "Findmypast / Federation of Family History Societies National Burial Index",
  "url": "https://www.findmypast.com/search/results?sourcecategory=life+events+%28bmds%29&firstname=john&firstname_variants=true&lastname=gurney&lastname_variants=true&eventyear=1656&eventyear_offset=20&keywordsplace=hitcham%2C+buckinghamshire%2C+england&keywordsplace_proximity=10&sourcecountry=england&sid=999",
  "corpusStatus": "transcript",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/findmypast-bury-st-edmunds-st-mary-gurney-burials-1653-1656.md",
  "notes": "Three Gurney burials at the same Bury St Edmunds parish in a four-year window: John Gurney 11 Dec 1653; unnamed Gurney 6 Apr 1655; unnamed Gurney 13 May 1656 explicitly noted 'Wife'. Read as one continuing Bury household with the John male burial in 1653, a probable daughter or child in 1655, and the widow in 1656. Material to Section 10.6 of the John Gurney case file: a John Gurney was buried at Bury St Edmunds in December 1653 while the colonial John was deposing at Braintree in 1653. The case file does not currently fix the deposition's month, so the Bury burial does not conclusively eliminate the Bury-Boston identification but does tighten the priors against Banks's attribution. Bury parish register manuscript image not yet pulled; the National Burial Index transcript is the level reached in the present pass."
}
```

## 2. Thin validation notes

### 2.1 New validation `sources/validations/findmypast-ackworth-gurnoe-burton-marriage-1636.md`

```markdown
# Findmypast Ackworth Gurnoe + Burton marriage and 1637 baptism

Examined: 2026-05-12 Findmypast transcripts for England Marriages 1538-1973 (record R_855220028) and England Births & Baptisms 1538-1975 (record R_948023155). Both records relate to Ackworth, Yorkshire.

Findings landed in:
- `research/people/john-gurnoe-ackworth-yorkshire.md`
- `research/case-files/john-gurney-case-file-v4.md` Section 8 Ackworth row update
- `research/people/g13-john-gurney-fact-sheet.research.md` cross-link

Source IDs added:
- `findmypast-ackworth-gurnoe-burton-marriage-1636`
- `findmypast-ackworth-gurnoe-baptism-1637-john-thomas`

Working transcript:
- Marriage: John Gurnoe + Mary Burton, 6 Jun 1636, Ackworth, Yorkshire, England Marriages 1538-1973.
- Baptism: John Thomas Gurnoe, male, 19 Jan 1637, Ackworth, Yorkshire, England Births & Baptisms 1538-1975. Father/mother not transcribed in the index.

Manuscript image not yet pulled; both items are index transcript level. A West Yorkshire Archives or Borthwick Institute image pull of the Ackworth parish register would confirm or refine father/mother fields on the 1637 baptism.
```

### 2.2 New validation `sources/validations/findmypast-bury-st-edmunds-st-mary-gurney-burials-1653-1656.md`

```markdown
# Findmypast National Burial Index - Bury St Edmunds St Mary Gurney burials 1653-1656

Examined: 2026-05-12 Findmypast search of the National Burial Index for England & Wales, Gurney variants at Bury St Edmunds 1640-1680. Three Gurney burials returned at St Mary, Bury St Edmunds:

- John Gurney, 11 Dec 1653.
- Gurney (given name not transcribed), 6 Apr 1655.
- Gurney (given name not transcribed), 13 May 1656, notes "Wife".

Findings landed in:
- `research/case-files/john-gurney-case-file-v4.md` Section 8 new Bury St Edmunds row and Section 10.6 paragraph addition.

Source ID added:
- `findmypast-bury-st-edmunds-st-mary-gurney-burials-1653-1656`

Manuscript image not yet pulled. The Bury St Edmunds St Mary parish register is held by the Suffolk Record Office, Bury branch (FL 541/4); an image-level pull would confirm the John Gurney 11 Dec 1653 entry's parental or marital field and the 1655/1656 given names.
```

## 3. New research file `research/people/john-gurnoe-ackworth-yorkshire.md`

Create this new research file. It supports the case-file Ackworth row and carries the depth that should not live in the case file body. The file follows the `research-people` convention: lead with the finding, keep entries compact, no visible intake or process narration.

```markdown
# John Gurnoe of Ackworth, Yorkshire

John Gurnoe and Mary Burton married at Ackworth, Yorkshire, on 6 June 1636.[^fmp-ackworth-marriage-1636] A John Thomas Gurnoe was baptized at the same parish on 19 January 1637.[^fmp-ackworth-baptism-1637] The household is small in indexed coverage; the indexed Findmypast pass surfaces no Ackworth burial of either spouse and no further indexed children for this household in the present range.

## Relevance to the colonial John Gurney case file

The wife is genuinely named Mary, and the marriage falls in the right window for an emigration cohort departing England in 1636-1638. Those two factors keep this household visible as a same-name comparator in the John Gurney case file (Section 8 of `research/case-files/john-gurney-case-file-v4.md`).

The case against this household being the Massachusetts emigrant remains the stronger reading.

- The first indexed child is John Thomas, not Sarah, and is baptized at Ackworth seven months after the marriage. The colonial John's first child is Sarah (b. about 1628 per Sprague, History of Weymouth Vol. 3, and Torrey New England Marriages Prior to 1700 p. 331). The naming and ordering mismatch is direct.
- Yorkshire sits outside the Norfolk/Suffolk/Essex/London emigration corridor that produced the Great Migration. Yorkshire emigration to New England in the late 1630s exists but is sparse compared with the East Anglian flow.
- No primary-record bridge has been located linking an Ackworth Gurnoe household to a Massachusetts arrival, Weymouth/Braintree town record, or any of the colonial John's identified Essex or Norfolk social associates (the Shed, Tyng, Newgate, or Gilman networks).

The 1636 Mary Burton wife match is strong enough on its own to keep this household above the noise floor — the older Daniel Gurney record (Part II) and compiled family histories sometimes referred to a Mary Barton or Mary Burton wife for the colonial John, and the Ackworth marriage now supplies a primary record of that combination at the right date. The naming, geographic, and corridor mismatches above are independently sufficient to keep this household at the existing Unlikely (~2%) probability rather than promoting it to a serious comparator. Probability adjustment is left to the case file's Section 11 (`research/case-files/john-gurney-case-file-v4.md`).

## Open items

- West Yorkshire Archives or Borthwick Institute parish-register image pull of Ackworth 1636-1637 to recover the 1637 baptism's father and mother fields, confirm the spelling on the 1636 marriage entry, and surface any additional children of this household.
- Ackworth burial register 1640-1680 (not indexed by Findmypast in the current pass) for either spouse.
- Yorkshire / West Riding probate index check for a John Gurnoe / Gurney / Gurny will between 1636 and 1680 that could anchor a death in England.

[^fmp-ackworth-marriage-1636]: Findmypast England Marriages 1538-1973 transcript R_855220028 (https://www.findmypast.com/transcript?id=R_855220028&tab=this): John Gurnoe and Mary Burton, marriage 6 June 1636, Ackworth, Yorkshire. Source ID `findmypast-ackworth-gurnoe-burton-marriage-1636`.
[^fmp-ackworth-baptism-1637]: Findmypast England Births & Baptisms 1538-1975 transcript R_948023155 (https://www.findmypast.com/transcript?id=R_948023155&tab=this): John Thomas Gurnoe, male, baptism 19 January 1637, Ackworth, Yorkshire. Father and mother are not in the transcript index. Source ID `findmypast-ackworth-gurnoe-baptism-1637-john-thomas`.
```

## 4. Cross-link inside `research/people/g13-john-gurney-fact-sheet.research.md`

Inside the existing "Origin Analysis and Elimination Work" section, near the existing "Bucks Gurney household map (Findmypast indexes, 2026-05-09)" subsection, insert a new compact subsection.

Place the insertion immediately after the existing `### Bucks Gurney household map (Findmypast indexes, 2026-05-09)` block (which ends with the "Luke Gurney" Aylesbury household entry) and before the next `### Candidate A Aylesbury family group (FS-verified 2026-05-09)` heading.

```markdown
### Ackworth, Yorkshire: Mary Burton marriage and 1637 baptism reach primary index (2026-05-12)

The long-standing compiled-genealogy claim of a John Gurney + Mary Barton/Burton marriage at Ackworth in 1636 now reaches primary index level. Findmypast England Marriages 1538-1973 transcript R_855220028 records John Gurnoe and Mary Burton married at Ackworth 6 June 1636. The same Findmypast collection surfaces an England Births & Baptisms 1538-1975 transcript R_948023155 for John Thomas Gurnoe baptized at Ackworth 19 January 1637, the year after the marriage and consistent with a continuing Yorkshire household.

The wife is in fact named Mary, and the marriage date sits inside the 1636-1638 emigration-cohort window, so the Ackworth household survives elimination by the wife-name test that disposes of most other same-name candidates. It still fails on the child-naming and geographic-corridor tests: the colonial John's first child is Sarah (about 1628) and the colonial John appears at Weymouth by June 1641 in the Massachusetts corridor that drew from East Anglia rather than the West Riding. Working notes for this household live in `research/people/john-gurnoe-ackworth-yorkshire.md`. The case-file Section 8 Ackworth row in `research/case-files/john-gurney-case-file-v4.md` has been updated to record the primary-record confirmation; probability remains Unlikely (about 2%).

Open items: Ackworth parish-register image pull (West Yorkshire Archives or Borthwick) for the 1636 marriage and 1637 baptism father/mother fields; Ackworth burial-register check for either spouse; West Riding probate index search for a John Gurnoe/Gurney/Gurny death record 1636-1680. Source IDs: `findmypast-ackworth-gurnoe-burton-marriage-1636`, `findmypast-ackworth-gurnoe-baptism-1637-john-thomas`.
```

## 5. Case-file edits in `research/case-files/john-gurney-case-file-v4.md`

### 5.1 Update Section 8 Ackworth row

Find the existing row:

```markdown
| Ackworth, Yorkshire | Yorkshire | **Mary** Barton (claimed) | **Unlikely (~2%)** | Yorkshire is outside the emigrant corridor; the 1636 Mary Barton / Burton marriage attribution is not supported by a primary record reachable in the present pass.<sup class="fn"><a href="#n86" id="ref-86b">86</a></sup> |
```

Replace with:

```markdown
| Ackworth, Yorkshire | Yorkshire | **Mary** Burton | **Unlikely (~2%)** | 1636 John Gurnoe + Mary Burton marriage and 1637 John Thomas Gurnoe baptism now primary-record confirmed at Ackworth. Wife genuinely Mary, marriage in emigration-cohort window; but first child John Thomas (not Sarah), continuing Yorkshire household, and corridor mismatch keep probability at Unlikely. See `research/people/john-gurnoe-ackworth-yorkshire.md`.<sup class="fn"><a href="#n86" id="ref-86b">86</a></sup><sup class="fn"><a href="#n93" id="ref-93a">93</a></sup> |
```

### 5.2 Insert new Section 8 row for Bury St Edmunds household

Place the new row immediately AFTER the existing row beginning `| Norwich, Saint Peter Mancroft | Norfolk | - | **ELIMINATED** | Died in England (buried Saint Peter Mancroft, Norwich 10 February 1639).` and BEFORE the row beginning `| St Botolph Aldgate, London |`. The new row:

```markdown
| Bury St Edmunds, Suffolk | Suffolk | Unknown (1656 widow burial) | **ELIMINATED (probable)** | National Burial Index records three Gurney burials at St Mary, Bury St Edmunds in close sequence: John Gurney 11 December 1653, unnamed Gurney 6 April 1655, unnamed Gurney 13 May 1656 ("Wife"). The household was settled at Bury through the colonial John's 1653 deposition window and beyond. Material to Banks's Bury attribution; see Section 10.6.<sup class="fn"><a href="#n93" id="ref-93b">93</a></sup> |
```

### 5.3 Tighten Section 10.6 Banks paragraph

Find the existing paragraph that begins `A 2026-05-11 FamilySearch England Births and Christenings search for Bury St Edmunds Gurney baptisms 1620-1645 returns no John Gurney father...` (line near 398).

Immediately AFTER that paragraph and BEFORE the next paragraph beginning `The 1636 Newgate apprentice record is a major caution...`, insert this new paragraph:

```markdown
The Bury St Edmunds register also carries an active Gurney household across the 1653-1656 window. The National Burial Index records a John Gurney buried at St Mary, Bury St Edmunds on 11 December 1653, an unnamed Gurney burial at the same parish on 6 April 1655, and an unnamed Gurney burial on 13 May 1656 explicitly noted "Wife." The trio reads most naturally as one continuing household: a male John buried 1653, a child or other family member in 1655, and the widow in 1656. This sharpens the Banks reading without overturning it. A Bury-resident John Gurney was buried at Bury exactly in the same calendar year the colonial John gave the Wilson v. Faxon deposition at Braintree, aged about 50. The case file does not currently fix the deposition's month, so the December 1653 Bury burial does not on its own eliminate Banks's Bury-Boston identification; but the household continuity through 1656 implies that the Bury Gurneys remained at Bury rather than emigrating, so Banks's attribution can only stand if the colonial John was an earlier-departing apprentice from this Bury household rather than its head. The Bury parish-register manuscript image is not yet pulled.<sup class="fn"><a href="#n93" id="ref-93c">93</a></sup>
```

### 5.4 Update footnote n86 (existing) and add footnote n93 (new)

Find the existing footnote `n86` definition in the case-file notes block:

```html
<li id="n86" value="86">Candidate C: Findmypast Hertfordshire Baptisms search 2026-05-09, surname Gurney with variants, father John with variants, place Berkhamsted, baptism year 1610-1650, returning the eight-child Berkhamsted family group described above; source ID <code>findmypast-hertfordshire-baptisms</code>. Ackworth Yorkshire: FamilySearch Records search 2026-05-09 for John Gurney and spouse Barton in Yorkshire returning zero results; a follow-up 2026-05-11 web pass with the Burton spelling variant also returned no matching primary record. Source ID <code>fs-england-births-christenings</code> used for the broader Records collection probed. <a class="backref" href="#ref-86a">back</a> <a class="backref" href="#ref-86b">back</a></li>
```

Replace with:

```html
<li id="n86" value="86">Candidate C: Findmypast Hertfordshire Baptisms search 2026-05-09, surname Gurney with variants, father John with variants, place Berkhamsted, baptism year 1610-1650, returning the eight-child Berkhamsted family group described above; source ID <code>findmypast-hertfordshire-baptisms</code>. Ackworth Yorkshire: the 2026-05-09 FamilySearch Records search and 2026-05-11 web pass returned no primary record at that time; the 2026-05-12 Findmypast England Marriages 1538-1973 and England Births & Baptisms 1538-1975 search surfaced primary index transcripts for the marriage and a Yorkshire child (see n93). Source IDs <code>fs-england-births-christenings</code>, <code>findmypast-ackworth-gurnoe-burton-marriage-1636</code>, <code>findmypast-ackworth-gurnoe-baptism-1637-john-thomas</code>. <a class="backref" href="#ref-86a">back</a> <a class="backref" href="#ref-86b">back</a></li>
```

Insert new footnote `n93` in the same notes block, immediately AFTER the existing `n92` Candidate D footnote:

```html
<li id="n93" value="93">Ackworth, Yorkshire: Findmypast England Marriages 1538-1973 transcript R_855220028 (https://www.findmypast.com/transcript?id=R_855220028&tab=this) for John Gurnoe + Mary Burton, 6 June 1636, Ackworth, Yorkshire; Findmypast England Births & Baptisms 1538-1975 transcript R_948023155 (https://www.findmypast.com/transcript?id=R_948023155&tab=this) for John Thomas Gurnoe, baptized 19 January 1637, Ackworth; source IDs <code>findmypast-ackworth-gurnoe-burton-marriage-1636</code>, <code>findmypast-ackworth-gurnoe-baptism-1637-john-thomas</code>; depth-of-detail file <code>research/people/john-gurnoe-ackworth-yorkshire.md</code>. Bury St Edmunds, Suffolk: Findmypast National Burial Index for England & Wales, three Gurney burials at St Mary, Bury St Edmunds — John Gurney 11 December 1653; unnamed Gurney 6 April 1655; unnamed Gurney 13 May 1656 ("Wife"); source ID <code>findmypast-bury-st-edmunds-st-mary-gurney-burials-1653-1656</code>. Suffolk Record Office Bury branch holds the St Mary parish register (FL 541/4); manuscript image not yet pulled. <a class="backref" href="#ref-93a">back</a> <a class="backref" href="#ref-93b">back</a> <a class="backref" href="#ref-93c">back</a></li>
```

## 6. Audit checklist

Before declaring this patchset applied, confirm each item:

- `data/sources.json` updated with three new source IDs `findmypast-ackworth-gurnoe-burton-marriage-1636`, `findmypast-ackworth-gurnoe-baptism-1637-john-thomas`, `findmypast-bury-st-edmunds-st-mary-gurney-burials-1653-1656`.
- Two new validation files created at the listed paths.
- New research file `research/people/john-gurnoe-ackworth-yorkshire.md` created.
- Cross-link block inserted in `research/people/g13-john-gurney-fact-sheet.research.md` between the existing Bucks-household-map and Candidate-A-Aylesbury-family-group subsections.
- Case-file Section 8 Ackworth row replaced with the updated version.
- Case-file Section 8 new Bury St Edmunds row inserted between Saint Peter Mancroft and St Botolph Aldgate rows.
- Case-file Section 10.6 paragraph inserted between the 2026-05-11 Bury baptism-search paragraph and the 1636 Newgate paragraph.
- Footnote `n86` body replaced; footnote `n93` inserted after `n92`.

## 7. Held-review and deferred items

- Ackworth parish-register manuscript image (West Yorkshire Archives or Borthwick Institute) for the 1636 marriage and 1637 baptism father/mother fields — deferred.
- Bury St Edmunds St Mary parish-register manuscript image (Suffolk Record Office, Bury branch, FL 541/4) for the 11 December 1653 John Gurney burial entry, plus 1655 and 1656 entries — deferred.
- Wilson v. Faxon 1653 deposition month/day — case file currently does not specify. A Suffolk County, Massachusetts court-record image-level pull would let the Bury 11 December 1653 burial be assessed as a hard date conflict or not. Treat as deferred outside this patchset's scope.
