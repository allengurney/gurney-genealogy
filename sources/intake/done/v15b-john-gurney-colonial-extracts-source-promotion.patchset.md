# Intake patchset v15B - John Gurney colonial extract source promotion

## Status

Review patchset only. Not applied.

Prepared 2026-05-09 from the John Gurney case-file source-completeness audit.

## Purpose

Promote the colonial John Gurney extracts currently held under:

`research/case-files/John-gurney-research-to-be-assessed/`

into the normal source layer: `data/sources.json`, `sources/corpus_supplement/`, and `sources/validations/`.

These sources mostly strengthen the Massachusetts baseline rather than the English-origin argument. Their value is still important: they prevent the case file from resting on over-compressed secondary summaries for John's Weymouth, Braintree, and Mendon record trail.

## Scope

Promote these six reviewed extract files:

| New Source ID | Current holding file | Evidence role |
|---|---|---|
| `suffolk-deeds-liber-iv-1888` | `research/case-files/John-gurney-research-to-be-assessed/deeds and misc/deeds318904_04_john_gurney_extracts.md` | Braintree Tyng/Ting estate tenancy and lease context |
| `mendon-proprietors-records-1899` | `research/case-files/John-gurney-research-to-be-assessed/deeds and misc/proprietors_gurney_extracts.md` | John and Grisel/Grisell Gurney Mendon lots, will/title chain, abutters |
| `ballou-history-of-milford-1882` | `research/case-files/John-gurney-research-to-be-assessed/deeds and misc/milford_john_gurney_extract_pp27_33.md` | Mendon/Milford founding narrative and John Gurney allotment context |
| `bartletts-of-weymouth-1892` | `research/case-files/John-gurney-research-to-be-assessed/deeds and misc/john_gurney_bartlett_note.md` | Late secondary Braintree-to-Mendon settler tradition |
| `porter-descendants-richard-porter-1878` | `research/case-files/John-gurney-research-to-be-assessed/deeds and misc/porter_gurney_p238_extract.md` | Secondary pointer to 2 June 1641 Weymouth gunpowder fine |
| `nash-historical-sketch-weymouth-1885` | `research/case-files/John-gurney-research-to-be-assessed/deeds and misc/john_gurney_extracts_historicalsketch00nash_0.md` | Weymouth land grants and 1651/2 lot-list context |

Do not promote `Two Directory Entries - English emigrants to New England_backup version.md` in this patchset. It contains unresolved conflict markers and overlaps already-registered Banks/Anderson analysis. Treat it as a cleanup target for a later Candidate A/Candidate B source-status patchset.

## 1. `data/sources.json`

### 1.1 Add six source entries

Add the following objects near the existing G13/New England source entries.

```json
    "suffolk-deeds-liber-iv-1888": {
      "shortTitle": "Suffolk Deeds, Liber IV",
      "citation": "Temple, Thomas F., Register of Deeds. Suffolk Deeds. Liber IV. Boston: Rockwell and Churchill, City Printers, 1888.",
      "archive": "Extracted from local file deeds318904_04.pdf / source note",
      "url": null,
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/suffolk-deeds-liber-iv-1888-john-gurney-extract.md",
      "mediaPath": null,
      "validationPath": "sources/validations/suffolk-deeds-liber-iv-1888.md",
      "notes": "Source-control entry for the promoted John Gurney extract from Suffolk Deeds, Liber IV. Substantive treatment belongs in the G13 research companion and, where useful, the John Gurney case file. Not an English-origin source."
    },
    "mendon-proprietors-records-1899": {
      "shortTitle": "Mendon Proprietors' Records",
      "citation": "The Proprietors' Records of the Town of Mendon, Massachusetts: Incorporated May 15, 1667. Boston: Rockwell and Churchill Press, 1899.",
      "archive": "Extracted from local file proprietorsrecor00men.pdf / source note",
      "url": null,
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/mendon-proprietors-records-1899-gurney-extracts.md",
      "mediaPath": null,
      "validationPath": "sources/validations/mendon-proprietors-records-1899.md",
      "notes": "Source-control entry for promoted Gurney/Gurny/Grisel extracts from the printed Mendon proprietors' records. Substantive treatment belongs in the G13 research companion or a later Grisel/Jewell/Kibbee/Burge note."
    },
    "ballou-history-of-milford-1882": {
      "shortTitle": "Ballou, History of Milford",
      "citation": "Ballou, Adin. History of the Town of Milford, Worcester County, Massachusetts, from Its First Settlement to 1881. Boston: Franklin Press, Rand, Avery, & Co., 1882.",
      "archive": "Extracted from local file milford_TN-215721_1.pdf / source note",
      "url": null,
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/ballou-history-of-milford-1882-john-gurney-extract.md",
      "mediaPath": null,
      "validationPath": "sources/validations/ballou-history-of-milford-1882.md",
      "notes": "Source-control entry for the promoted John Gurney extract from Ballou's Milford history. Substantive treatment belongs in the G13 research companion and, where useful, the John Gurney case file."
    },
    "bartletts-of-weymouth-1892": {
      "shortTitle": "Bartlett, Bartletts of Weymouth",
      "citation": "Bartlett, Thomas Edward. The Bartletts: Ancestral, Genealogical, Biographical, Historical. New Haven, Conn.: Press of the Stafford Printing Co., 1892.",
      "archive": "Extracted from local source note TN-244870 The Bartletts of Weymouth",
      "url": null,
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/bartletts-of-weymouth-1892-john-gurney-extract.md",
      "mediaPath": null,
      "validationPath": "sources/validations/bartletts-of-weymouth-1892.md",
      "notes": "Source-control entry for the promoted John Gurney extract from Bartlett's Weymouth/Bartlett genealogy. Substantive treatment belongs in the G13 research companion and, where useful, the John Gurney case file."
    },
    "porter-descendants-richard-porter-1878": {
      "shortTitle": "Porter, Descendants of Richard Porter",
      "citation": "Porter, Joseph W. A Genealogy of the Descendants of Richard Porter, Who Settled at Weymouth, Mass., 1635, and Allied Families. Bangor, 1878.",
      "archive": "Extracted from local file Porter_genealogyofdesce00port.pdf / source note",
      "url": null,
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/porter-descendants-richard-porter-1878-john-gurney-extract.md",
      "mediaPath": null,
      "validationPath": "sources/validations/porter-descendants-richard-porter-1878.md",
      "notes": "Source-control entry for the promoted John Gurney extract from Porter. Substantive treatment belongs in the G13 research companion and, where useful, the John Gurney case file. MBCR 1:331 remains the controlling court citation."
    },
    "nash-historical-sketch-weymouth-1885": {
      "shortTitle": "Nash, Historical Sketch of Weymouth",
      "citation": "Nash, Gilbert. Historical Sketch of the Town of Weymouth, Massachusetts, from 1622 to 1884. Weymouth, Mass.: Town of Weymouth / Alfred Mudge & Son, 1885.",
      "archive": "Extracted from local file historicalsketch00nash_0.pdf / source note",
      "url": null,
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/nash-historical-sketch-weymouth-1885-john-gurney-extract.md",
      "mediaPath": null,
      "validationPath": "sources/validations/nash-historical-sketch-weymouth-1885.md",
      "notes": "Source-control entry for the promoted John Gurney extracts from Nash's Weymouth history. Substantive treatment belongs in the G13 research companion and, where useful, the John Gurney case file. Not an English-origin source."
    },
```

## 2. Corpus files

Create these six files by copying the corresponding holding-file text and normalizing only the top matter to include the new Source ID.

Do not delete the original holding files until review is complete.

| New corpus file | Source holding file |
|---|---|
| `sources/corpus_supplement/suffolk-deeds-liber-iv-1888-john-gurney-extract.md` | `research/case-files/John-gurney-research-to-be-assessed/deeds and misc/deeds318904_04_john_gurney_extracts.md` |
| `sources/corpus_supplement/mendon-proprietors-records-1899-gurney-extracts.md` | `research/case-files/John-gurney-research-to-be-assessed/deeds and misc/proprietors_gurney_extracts.md` |
| `sources/corpus_supplement/ballou-history-of-milford-1882-john-gurney-extract.md` | `research/case-files/John-gurney-research-to-be-assessed/deeds and misc/milford_john_gurney_extract_pp27_33.md` |
| `sources/corpus_supplement/bartletts-of-weymouth-1892-john-gurney-extract.md` | `research/case-files/John-gurney-research-to-be-assessed/deeds and misc/john_gurney_bartlett_note.md` |
| `sources/corpus_supplement/porter-descendants-richard-porter-1878-john-gurney-extract.md` | `research/case-files/John-gurney-research-to-be-assessed/deeds and misc/porter_gurney_p238_extract.md` |
| `sources/corpus_supplement/nash-historical-sketch-weymouth-1885-john-gurney-extract.md` | `research/case-files/John-gurney-research-to-be-assessed/deeds and misc/john_gurney_extracts_historicalsketch00nash_0.md` |

For each copied corpus file, add this immediately below the title if missing:

```markdown
**Source ID:** `<matching-source-id>`

**Promotion note:** Promoted from `research/case-files/John-gurney-research-to-be-assessed/` by patchset v15B. The extract is retained for source-layer tracking; interpretive conclusions should live in the relevant research/case files.
```

Preserve the useful extraction notes already present in those files. They contain page numbers, search variants, and negative search scope that should not be compressed away.

## 3. Validation files

Create one validation file per source.

### 3.1 `sources/validations/suffolk-deeds-liber-iv-1888.md`

```markdown
# Source validation: Suffolk Deeds, Liber IV

**Source ID:** `suffolk-deeds-liber-iv-1888`

## Examined

Thomas F. Temple, Register of Deeds, *Suffolk Deeds. Liber IV* (Boston: Rockwell and Churchill, City Printers, 1888).

## Scope

- Local extract file `deeds318904_04_john_gurney_extracts.md`.
- Printed pages [5]-[6], [89]-[90a], and index entry "Gurney, John, 6, 89a, 90."

## Validation result

Usable as a printed deed-book extract. Original deed record not checked in this source pass.

## Findings recorded in

- `research/people/g13-john-gurney-fact-sheet.research.md`
- Optional concise colonial-baseline note in `research/case-files/john-gurney-case-file-v4.md`

## Detailed execution trail

`sources/intake/processed/Ready/v15b-john-gurney-colonial-extracts-source-promotion.patchset.md`
```

### 3.2 `sources/validations/mendon-proprietors-records-1899.md`

```markdown
# Source validation: Mendon Proprietors' Records

**Source ID:** `mendon-proprietors-records-1899`

## Examined

*The Proprietors' Records of the Town of Mendon, Massachusetts: Incorporated May 15, 1667* (Boston: Rockwell and Churchill Press, 1899).

## Scope

- Local extract file `proprietors_gurney_extracts.md`.
- Gurney/Gurny/Grisel/Grisell/Grizel references.

## Validation result

Usable as a printed proprietors-record extract. Original town record manuscript not checked in this source pass.

## Findings recorded in

- `research/people/g13-john-gurney-fact-sheet.research.md`
- Future Grisel/Jewell/Kibbee/Burge research note

## Detailed execution trail

`sources/intake/processed/Ready/v15b-john-gurney-colonial-extracts-source-promotion.patchset.md`
```

### 3.3 `sources/validations/ballou-history-of-milford-1882.md`

```markdown
# Source validation: Ballou, History of Milford

**Source ID:** `ballou-history-of-milford-1882`

## Examined

Adin Ballou, *History of the Town of Milford, Worcester County, Massachusetts, from Its First Settlement to 1881* (Boston: Franklin Press, Rand, Avery, & Co., 1882).

## Scope

- Local extract file `milford_john_gurney_extract_pp27_33.md`.
- PDF pages 27-35 as extracted.

## Validation result

Usable as a local-history extract. Underlying town/proprietors records behind Ballou's narrative not checked in this source pass.

## Findings recorded in

- `research/people/g13-john-gurney-fact-sheet.research.md`
- Optional concise colonial-baseline note in `research/case-files/john-gurney-case-file-v4.md`

## Detailed execution trail

`sources/intake/processed/Ready/v15b-john-gurney-colonial-extracts-source-promotion.patchset.md`
```

### 3.4 `sources/validations/bartletts-of-weymouth-1892.md`

```markdown
# Source validation: Bartletts of Weymouth

**Source ID:** `bartletts-of-weymouth-1892`

## Examined

Thomas Edward Bartlett, *The Bartletts* (New Haven, Conn.: Press of the Stafford Printing Co., 1892), printed pp. 14-15.

## Scope

- Local extract file `john_gurney_bartlett_note.md`.

## Validation result

Usable as a late compiled-genealogy/local-history extract. Underlying records behind Bartlett's compiled statement not checked in this source pass.

## Findings recorded in

- `research/people/g13-john-gurney-fact-sheet.research.md`
- Optional future Mendon settlement context note

## Detailed execution trail

`sources/intake/processed/Ready/v15b-john-gurney-colonial-extracts-source-promotion.patchset.md`
```

### 3.5 `sources/validations/porter-descendants-richard-porter-1878.md`

```markdown
# Source validation: Porter, Descendants of Richard Porter

**Source ID:** `porter-descendants-richard-porter-1878`

## Examined

Joseph W. Porter, *A Genealogy of the Descendants of Richard Porter* (Bangor, 1878), printed pp. 224-225.

## Scope

- Local extract file `porter_gurney_p238_extract.md`.

## Validation result

Usable as a secondary pointer to the 1641 Weymouth gunpowder-fine context. MBCR 1:331 is the controlling court citation.

## Findings recorded in

- `research/people/g13-john-gurney-fact-sheet.research.md`
- Case-file note only if clarifying the Weymouth baseline

## Detailed execution trail

`sources/intake/processed/Ready/v15b-john-gurney-colonial-extracts-source-promotion.patchset.md`
```

### 3.6 `sources/validations/nash-historical-sketch-weymouth-1885.md`

```markdown
# Source validation: Nash, Historical Sketch of Weymouth

**Source ID:** `nash-historical-sketch-weymouth-1885`

## Examined

Gilbert Nash, *Historical Sketch of the Town of Weymouth, Massachusetts, from 1622 to 1884* (Weymouth, Mass.: Town of Weymouth / Alfred Mudge & Son, 1885).

## Scope

- Local extract file `john_gurney_extracts_historicalsketch00nash_0.md`.
- Printed pp. 258, 270, 278, 282, and index p. 306.

## Validation result

Usable as a printed local-history extract. Original Weymouth town records behind Nash's printed local history not checked in this source pass.

## Findings recorded in

- `research/people/g13-john-gurney-fact-sheet.research.md`
- Optional concise colonial-baseline note in `research/case-files/john-gurney-case-file-v4.md`

## Detailed execution trail

`sources/intake/processed/Ready/v15b-john-gurney-colonial-extracts-source-promotion.patchset.md`
```

## 4. `research/people/g13-john-gurney-fact-sheet.research.md`

### 4.1 Add colonial-source promotion subsection

Add after the existing `### Land and property records` table and before `### Deposition and court records`:

```markdown
#### Promoted colonial property and settlement extracts

Six additional colonial-context extracts are now source-tracked rather than left only in the case-file assessment folder. They sharpen John's Massachusetts baseline but do not prove English origin.

`Suffolk Deeds. Liber IV` places John Gurney in Braintree in the William Ting/Tyng estate division. In the first estate-division passage, Bethia and Mercy Ting received two Braintree messuages or tenements, one in the hands of Gregory Belcher and the other in the hands of John Gurney. A later agreement about the same Braintree farms again describes them as by lease in the possession of Gregory Belcher and John Gurney. This is important because it presents John as a leaseholder/occupant in a specific Braintree property network rather than as a large proprietor.[^suffolk-deeds-liber-iv]

The Mendon proprietors' records preserve both John Gurny and Grisel Gurney as separate twenty-acre lot holders. The same source carries Grisel's lot through will and title-chain material: the widow Gurny, later wife of John Burge, left her Mendon accommodation to Joseph Juell, with payments to Nathaniel Juell, Mercy Juell, and Sherabiah Keby. John Gurny's house lot, meadow, and swamp-lot references also persist in later abutter and conveyancing descriptions. This material belongs in the John/Grisel property and family-network research trail, not merely in a validation note.[^mendon-proprietors]

Ballou's Milford history adds the longer Mendon/Milford founding context and places John in the early allotment/meadow-division setting. Because John died in 1662/3, use this evidence carefully: it supports his connection with the Braintree-to-Mendon venture, but later settlement deadlines should not be read as proof that he personally removed to Mendon.[^ballou-milford]

Bartlett lists John Gurney among the first settlers from Braintree connected with the Mendon/Nipmug plantation. Because Bartlett is a late compiled genealogy/local history, use it as supporting tradition only and test it against the proprietors' records before making any personal-removal claim.[^bartlett-weymouth]

Porter quotes or summarizes the 2 June 1641 General Court remission of a fine involving John Porter, James Ludden, and John Gurney for want of gunpowder, adding that Ludden and Gurney were of Weymouth. Porter is useful context, but MBCR 1:331 remains the controlling court citation.[^porter-richard-porter]

Nash preserves John Gurny/Gurnie as first grantee in several Weymouth land descriptions and lists John Gurney directly in the 1651/2 lot list. This helps refine Weymouth land context, spelling variants, and the question of whether Weymouth represents a real settlement phase or a shorter/transitional appearance.[^nash-weymouth]

[^suffolk-deeds-liber-iv]: Thomas F. Temple, Register of Deeds, *Suffolk Deeds. Liber IV* (Boston: Rockwell and Churchill, City Printers, 1888), printed pp. [5]-[6], [89]-[90a]. Source ID: `suffolk-deeds-liber-iv-1888`.
[^mendon-proprietors]: *The Proprietors' Records of the Town of Mendon, Massachusetts: Incorporated May 15, 1667* (Boston: Rockwell and Churchill Press, 1899), selected Gurney/Gurny/Grisel entries. Source ID: `mendon-proprietors-records-1899`.
[^ballou-milford]: Adin Ballou, *History of the Town of Milford, Worcester County, Massachusetts, from Its First Settlement to 1881* (Boston: Franklin Press, Rand, Avery, & Co., 1882), extracted pp. 27-35. Source ID: `ballou-history-of-milford-1882`.
[^bartlett-weymouth]: Thomas Edward Bartlett, *The Bartletts* (New Haven, Conn.: Press of the Stafford Printing Co., 1892), printed pp. 14-15. Source ID: `bartletts-of-weymouth-1892`.
[^porter-richard-porter]: Joseph W. Porter, *A Genealogy of the Descendants of Richard Porter* (Bangor, 1878), printed pp. 224-225. Source ID: `porter-descendants-richard-porter-1878`.
[^nash-weymouth]: Gilbert Nash, *Historical Sketch of the Town of Weymouth, Massachusetts, from 1622 to 1884* (Weymouth, Mass.: Town of Weymouth / Alfred Mudge & Son, 1885), selected Gurny/Gurnie/Gurney entries. Source ID: `nash-historical-sketch-weymouth-1885`.
```

### 4.2 Update source-status checklist

Add the six source IDs to the `Sources Consulted` or source-status table in the companion, marking them as promoted from local extracts with validation files.

## 5. `research/case-files/john-gurney-case-file-v4.md`

### 5.1 Add a concise colonial-baseline note

The main case file should not absorb all colonial property detail. Add a short note under section 12 `For Enrichment`, or create a short `### Colonial Baseline Cleanup` subsection in section 13.

Suggested text:

```markdown
3. **Colonial baseline source cleanup.** Promote the local Suffolk Deeds, Mendon Proprietors, Ballou, Bartlett, Porter, and Nash extracts into the formal source layer. These sources do not identify John's English origin, but they sharpen the Massachusetts baseline: Weymouth land grants, Braintree tenancy/property, the 1641 gunpowder fine context, and Mendon allotment/title-chain material.
```

If this is added as a footnoted case-file note, use the next available endnote after any applied v15A Bates note.

## 6. Holding-folder cleanup note

After the corpus/validation files are created and reviewed, add a small status note in:

`research/case-files/John-gurney-research-to-be-assessed/`

Suggested file:

`PROMOTION_STATUS.md`

Suggested content:

```markdown
# John Gurney to-be-assessed promotion status

Promoted by patchset v15B:

- `deeds and misc/deeds318904_04_john_gurney_extracts.md` -> `sources/corpus_supplement/suffolk-deeds-liber-iv-1888-john-gurney-extract.md`
- `deeds and misc/proprietors_gurney_extracts.md` -> `sources/corpus_supplement/mendon-proprietors-records-1899-gurney-extracts.md`
- `deeds and misc/milford_john_gurney_extract_pp27_33.md` -> `sources/corpus_supplement/ballou-history-of-milford-1882-john-gurney-extract.md`
- `deeds and misc/john_gurney_bartlett_note.md` -> `sources/corpus_supplement/bartletts-of-weymouth-1892-john-gurney-extract.md`
- `deeds and misc/porter_gurney_p238_extract.md` -> `sources/corpus_supplement/porter-descendants-richard-porter-1878-john-gurney-extract.md`
- `deeds and misc/john_gurney_extracts_historicalsketch00nash_0.md` -> `sources/corpus_supplement/nash-historical-sketch-weymouth-1885-john-gurney-extract.md`

Not promoted in v15B:

- `Two Directory Entries - English emigrants to New England_backup version.md` - contains unresolved conflict markers and overlaps Banks/Anderson analysis.
- `tna-probate-analysis-john-gurney.md` - belongs in a separate competing-candidates/exclusion patchset.
```

## 7. Validation checklist

Run after application:

```powershell
Select-String -Path data\sources.json -Pattern "suffolk-deeds-liber-iv-1888|mendon-proprietors-records-1899|ballou-history-of-milford-1882|bartletts-of-weymouth-1892|porter-descendants-richard-porter-1878|nash-historical-sketch-weymouth-1885"
Test-Path sources\corpus_supplement\suffolk-deeds-liber-iv-1888-john-gurney-extract.md
Test-Path sources\corpus_supplement\mendon-proprietors-records-1899-gurney-extracts.md
Test-Path sources\corpus_supplement\ballou-history-of-milford-1882-john-gurney-extract.md
Test-Path sources\corpus_supplement\bartletts-of-weymouth-1892-john-gurney-extract.md
Test-Path sources\corpus_supplement\porter-descendants-richard-porter-1878-john-gurney-extract.md
Test-Path sources\corpus_supplement\nash-historical-sketch-weymouth-1885-john-gurney-extract.md
Test-Path sources\validations\suffolk-deeds-liber-iv-1888.md
Test-Path sources\validations\mendon-proprietors-records-1899.md
Test-Path sources\validations\ballou-history-of-milford-1882.md
Test-Path sources\validations\bartletts-of-weymouth-1892.md
Test-Path sources\validations\porter-descendants-richard-porter-1878.md
Test-Path sources\validations\nash-historical-sketch-weymouth-1885.md
Select-String -Path research\people\g13-john-gurney-fact-sheet.research.md -Pattern "suffolk-deeds-liber-iv|mendon-proprietors|ballou-milford|bartlett-weymouth|porter-richard-porter|nash-weymouth"
```

Then run the usual site validation/package commands if this is applied to publishable content.

## 8. Follow-up patchsets suggested

- Candidate-exclusion patchset: promote `tna-probate-analysis-john-gurney.md` into a structured competing-Johns appendix.
- Banks/Anderson source-status patchset: clean up `Two Directory Entries - English emigrants to New England_backup version.md`, remove conflict markers, and attach it to the existing Banks/Anderson source records rather than creating duplicate source IDs.
- Grisel/Jewell/Kibbee/Burge patchset: use the Mendon Proprietors material for a focused second-wife/family-network note.
