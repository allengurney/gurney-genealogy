# Intake patchset v23 - John Gurney Candidate A effectively eliminated + SPR Case #338 image-verified

```yaml
patchset_id: v23
created: 2026-05-09
repo_scope: gurney-genealogy
phase: phase_1_patchset_only
primary_case_file: research/case-files/john-gurney-case-file-v4.md
primary_research_file: research/people/g13-john-gurney-fact-sheet.research.md
working_memo: sources/intake/working/john-gurney-audit-state.md
phase_2_rule: Apply only after v20/v21/v22. v23 contains the controlling Cand A elimination via FS-verified Aylesbury baptisms; treat as superseding the placeholder Cand A wording introduced in v22.
```

## 0. Audit report

### 0.1 Scope

Pass 5 used the project's live FamilySearch subscription via the Chrome extension to:
1. Verify the 1647 Jonathan Aylesbury baptism claimed in older repo notes (case file's `Gurney_ProtestationReturns_Analysis.md`).
2. Locate and image-verify Suffolk Probate Case #338 (John Gurney 1662/3) in FS DGS 102840311.
3. Map Cand A's complete Aylesbury family group via FS England Births and Christenings index.

Pass 5 also walked Findmypast's London Apprenticeship Abstracts 1442-1850 for the case file's standing `n57` Haberdashers 1632 John Gurney apprentice claim and returned zero results.

### 0.2 Direct pulls obtained

| Record | Source | Significance |
|---|---|---|
| **Jonathan Gurney**, christened 22 Nov 1647, Saint Mary Aylesbury, son of John Gurney | FS England Births and Christenings 1538-1975, FS ID `JMBC-P2G`, tree `LBKR-M1H` | Confirms the older repo claim. Anchors Cand A's John in Aylesbury 1647. |
| **Daniell Gurney**, christened 26 Dec 1645, Saint Mary Aylesbury, son of John Gurney | FS England Births and Christenings 1538-1975, FS ID `JWN5-W5B`, tree `MSRS-B8Z` | New Cand A child. Anchors Aylesbury fathering in 1645. |
| **Sarah Gurney**, christened 22 Aug 1639, Saint Mary Aylesbury, daughter of John Gurney | FS England Births and Christenings index entry | Earliest indexed Cand A Aylesbury child. Distinct from the colonial John's daughter Sarah (no documented Aylesbury connection). |
| **Hannah Gurney**, christened 12 Nov 1653, Saint Mary Aylesbury, daughter of John Gurney | FS England Births and Christenings index entry | Latest indexed Cand A Aylesbury child. Anchors fathering through 1653. |
| **Suffolk Probate Case #338, John Gurney, 1662/3** | FS Catalog `olib:2822393`, DGS 102840311; image 514 (case cover) + image 516 (inventory header) | Inventory header "Boston March 16th 1663 / An Inventory of the goods & estate of John Gurney [late deceased]." Confirms case file's standing 16 Mar 1662/3 inventory date. |

### 0.3 Negative findings

- **Findmypast London Apprenticeship Abstracts, surname Gurney (variants on), all years**: zero results. The case file's `n57` "John Gurney apprentice Haberdashers' Company 1632" claim is unsupported by this index. Original repo source for the claim should be re-verified before continuing to cite the lead.

### 0.4 Cand A — effective elimination

The Aylesbury family group, combined with the prior v22 evidence, gives the complete Cand A reconstruction:

| Date | Event | Source |
|---|---|---|
| 21 Feb 1602/3 | Stewkley baptism (claimed) | Sprague (not yet image-verified) |
| 24 Apr 1628 | Married Alice Oliffe, Bierton with Broughton | Findmypast Bucks Marriage Index, PR16/1/1Q p. 30 |
| 22 Aug 1639 | Daughter Sarah christened, Saint Mary Aylesbury | FS England B&C |
| 1641 | Certificate of residence Aylesbury → Northants | TNA E 115/180/113 (repo note) |
| 26 Dec 1645 | Son Daniell christened, Saint Mary Aylesbury | FS England B&C, FS ID JWN5-W5B |
| 22 Nov 1647 | Son Jonathan christened, Saint Mary Aylesbury | FS England B&C, FS ID JMBC-P2G |
| 1650 | Tenant at Walgrave, Northants | Repo note in Findings V7 |
| 12 Nov 1653 | Daughter Hannah christened, Saint Mary Aylesbury | FS England B&C |

Cand A is the Aylesbury John, with a continuously documented English residence from 1628 through at least 1653 — twelve years past the colonial John's first MA appearance (June 1641 Weymouth). **Probability as MA emigrant drops from ~8-10% (case file) → ~1-2% (effectively eliminated).** The only residual ambiguity is whether the Stewkley 1602/3 baptized John is the same individual as the Bierton 1628 husband of Alice Oliffe; pulling the Stewkley Dickson/Putnam 1897 register would close that gap entirely.

### 0.5 Other candidate implications

- **Candidate B (Francis G14's son):** No direct effect from Pass 5.
- **Candidate C (Berkhamsted):** No direct effect.
- **Unknown other origin:** Residual probability tightens by approximately the 5-8 percentage points freed from Cand A.

## 1. Source registry operation

Before applying, verify the proposed source IDs are still absent:

```powershell
Select-String -Path data\sources.json -Pattern "fs-england-births-christenings"
Select-String -Path data\sources.json -Pattern "fs-suffolk-probate-1636-1915"
```

Add two source objects in `data/sources.json`:

```json
    "fs-england-births-christenings": {
      "shortTitle": "FamilySearch England, Births and Christenings, 1538-1975",
      "fullTitle": "England, Births and Christenings, 1538-1975 (FamilySearch indexed records)",
      "publisher": "FamilySearch International",
      "type": "parish register index (subscription)",
      "url": "https://www.familysearch.org/search/collection/1473015",
      "notes": "Used 2026-05-09 to verify Cand A's Aylesbury family group at Saint Mary Aylesbury: Sarah 1639, Daniell 1645 (JWN5-W5B), Jonathan 1647 (JMBC-P2G), Hannah 1653, all children of John Gurney."
    },
    "fs-suffolk-probate-1636-1915": {
      "shortTitle": "Mass. Suffolk County probate & family court records, 1636-1915 (FS)",
      "fullTitle": "Massachusetts, Suffolk County, probate & family court records, 1636-1915 (digital images from Massachusetts Supreme Judicial Court Archives & Records Preservation, Boston, via FamilySearch)",
      "publisher": "FamilySearch International / Massachusetts Supreme Judicial Court",
      "type": "probate court manuscript (digital images)",
      "url": "https://www.familysearch.org/en/search/catalog/olib:2822393",
      "notes": "Case #338 (Gurney, John, 1663 Adm.) in Probate FILE PAPERS Box 003 (Cases 250-399), DGS 102840311. Cover image 514; inventory image 516 'Boston March 16th 1663 An Inventory of the goods & estate of John Gurney late deceased.'"
    }
```

## 2. Validation notes (proposed thin files)

Create `sources/validations/fs-england-births-christenings.md`:

```markdown
# Validation - FamilySearch England Births and Christenings, 1538-1975

- Source ID: `fs-england-births-christenings`
- Title: England, Births and Christenings, 1538-1975 (FamilySearch indexed records)
- Online: https://www.familysearch.org/search/collection/1473015
- Method: FamilySearch subscription search via Chrome extension on 2026-05-09.
- Key entries used: Jonathan Gurney 22 Nov 1647 Saint Mary Aylesbury son of John (`JMBC-P2G`); Daniell Gurney 26 Dec 1645 Saint Mary Aylesbury son of John (`JWN5-W5B`); Sarah Gurney 22 Aug 1639 Saint Mary Aylesbury daughter of John; Hannah Gurney 12 Nov 1653 Saint Mary Aylesbury daughter of John. Used in `research/case-files/john-gurney-case-file-v4.md` §8 Cand A row and `research/people/g13-john-gurney-fact-sheet.research.md`.
```

Create `sources/validations/fs-suffolk-probate-1636-1915.md`:

```markdown
# Validation - FamilySearch Mass. Suffolk County probate records 1636-1915

- Source ID: `fs-suffolk-probate-1636-1915`
- Title: Massachusetts, Suffolk County, probate & family court records, 1636-1915 (FS digital images)
- Online: https://www.familysearch.org/en/search/catalog/olib:2822393
- Method: FamilySearch subscription image walk via Chrome extension on 2026-05-09.
- Key images used: Box 003 Cases 250-399, DGS 102840311. Case #338 cover at image 514 ("Gurney, John 1663 Adm., Suffolk #338"); inventory at image 516 ("Boston March 16th 1663 An Inventory of the goods & estate of John Gurney late deceased"). Image 515 verso of cover.
- Used in `research/case-files/john-gurney-case-file-v4.md` §1 baseline-facts table SPR Case #338 row, endnote `n9`, and §13.2 Primary Sources table.
```

## 3. Proposed case-file edits (research/case-files/john-gurney-case-file-v4.md)

### 3.1 §8 Cand A row — final rewrite (superseding the v22 placeholder)

Old (after v22 application):

```markdown
| **Candidate A** | Stewkley (1602/3 bapt., per Sprague); married Bierton with Broughton, Bucks (1628); Aylesbury hundred → Northamptonshire (1641-1650) | **Alice Oliffe** (m. 24 Apr 1628, Bierton with Broughton; Bucks Archives PR16/1/1Q p. 30) | **Very unlikely (~2-4%)** | ... |
```

New:

```markdown
| **Candidate A** | Stewkley (1602/3 bapt., per Sprague, not image-verified); married Bierton with Broughton, Bucks (1628); Aylesbury family group 1639-1653; Aylesbury hundred → Northamptonshire (1641-1650) | **Alice Oliffe** (m. 24 Apr 1628, Bierton with Broughton; Bucks Archives PR16/1/1Q p. 30) | **Effectively eliminated (~1-2%)** | Documented continuous English residence 1628-1653 incompatible with the MA emigrant. Bucks Marriage Index entry for the 1628 Bierton marriage to Alice Oliffe (not Collindridge); FS England Births and Christenings index entries for four Saint Mary Aylesbury children Sarah 1639, Daniell 1645 (FS ID JWN5-W5B), Jonathan 1647 (FS ID JMBC-P2G), Hannah 1653, all with father John Gurney; repo-internal TNA E 115/180/113 (1641 cert of residence Aylesbury → Northants) and 1650 Walgrave Northants tenancy. Only residual ambiguity: whether the Stewkley 1602/3 John is the same individual as the Bierton 1628 husband of Alice Oliffe; Stewkley register (Dickson/Putnam 1897) pull closes the gap.<sup class="fn"><a href="#nZA" id="ref-ZA">ZA</a></sup> |
```

Add new endnote (numbering on application):

```html
<li id="nZA" value="ZA">FamilySearch, "England, Births and Christenings, 1538-1975," indexed records for the Saint Mary Aylesbury Gurney family group: Sarah Gurney bapt. 22 Aug 1639 daughter of John; Daniell Gurney bapt. 26 Dec 1645 son of John, <a href="https://www.familysearch.org/ark:/61903/1:1:JWN5-W5B">https://www.familysearch.org/ark:/61903/1:1:JWN5-W5B</a>; Jonathan Gurney bapt. 22 Nov 1647 son of John, <a href="https://www.familysearch.org/ark:/61903/1:1:JMBC-P2G">https://www.familysearch.org/ark:/61903/1:1:JMBC-P2G</a>; Hannah Gurney bapt. 12 Nov 1653 daughter of John. Source ID: <code>fs-england-births-christenings</code>. Findmypast Buckinghamshire Marriage Index, John Gurney + Alice Oliffe 24 Apr 1628, Bierton with Broughton, Bucks Archives PR16/1/1Q p. 30 (source ID <code>findmypast-bucks-marriage-index</code>). TNA E 115/180/113 and Walgrave Northants 1650 tenancy preserved in <code>research/case-files/Initial foundation work for john-gurney-case-file/Gurney_ProtestationReturns_Analysis.md</code> and <code>Gurney_Research_Findings_V7.md</code> respectively. <a class="backref" href="#ref-ZA">↩</a></li>
```

### 3.2 §1 baseline-facts table — SPR Case #338 row + endnote n9

Old endnote n9:

```html
<li id="n9" value="9">Suffolk County, Massachusetts, Suffolk Probate Records, Case #338, John Gurney estate, inventory dated 16 Mar. 1662/63; cited in Anderson, <em>Great Migration Directory</em>, p. 158. Source ID: <code>anderson-gmd-2015</code>. <a class="backref" href="#ref-9">↩</a></li>
```

New endnote n9:

```html
<li id="n9" value="9">Suffolk County, Massachusetts, Suffolk Probate Records, Case #338, John Gurney estate, inventory dated 16 Mar. 1662/63; FamilySearch, Mass. Suffolk County probate & family court records, 1636-1915, FILE PAPERS Box 003 (Cases 250-399), DGS 102840311, image 514 (case cover "Gurney, John 1663 Adm., Suffolk #338") and image 516 (inventory header "Boston March 16th 1663 / An Inventory of the goods & estate of John Gurney [late deceased]"); <a href="https://www.familysearch.org/en/search/catalog/olib:2822393">https://www.familysearch.org/en/search/catalog/olib:2822393</a>. Source IDs: <code>fs-suffolk-probate-1636-1915</code>; <code>anderson-gmd-2015</code>. <a class="backref" href="#ref-9">↩</a></li>
```

### 3.3 §11 Probability Assessment table — Cand A row

Old (after v22 application):

```markdown
| **A — Stewkley / Bierton / Aylesbury → Northants** | **~2-4%** | ... |
```

New:

```markdown
| **A — Stewkley / Bierton / Aylesbury family group → Northants** | **~1-2%** | Continuous English residence 1628-1653 documented: Bierton 1628 marriage to Alice Oliffe; Saint Mary Aylesbury baptisms of children Sarah 1639, Daniell 1645, Jonathan 1647, Hannah 1653 (FS); 1641 Aylesbury → Northants cert; 1650 Walgrave tenancy. |
```

Adjust "Unknown other origin" residual upward by the difference.

### 3.4 §13.3 Other Leads — qualify the Haberdashers' 1632 note

Old `n57`:

```html
<li id="n57" value="57">City of London apprenticeship lead: John Gurney, Haberdashers' Company apprentice, 1632, located in indexed London apprenticeship material at Findmypast. The underlying detail record has not yet been pulled; use as a research target, not evidence of parentage. <a class="backref" href="#ref-57">↩</a></li>
```

New:

```html
<li id="n57" value="57">City of London apprenticeship lead: a John Gurney was reportedly apprenticed to the Haberdashers' Company in 1632 per an earlier repo research note. A 2026-05-09 walk of the Findmypast "London Apprenticeship Abstracts, 1442-1850" dataset with surname Gurney and full name variants returned zero results across the entire 1442-1850 span. The repo's original lead therefore does not match this Findmypast dataset and may instead trace to a different printed source (e.g., Cliff Webb's Haberdashers' apprenticeship register transcripts) or to an indexing under a non-standard surname variant. Treat as an unconfirmed lead pending re-identification of the original source. <a class="backref" href="#ref-57">↩</a></li>
```

## 4. Proposed G13 research-file edits (research/people/g13-john-gurney-fact-sheet.research.md)

### 4.1 New section "Candidate A Aylesbury family group (FS-verified 2026-05-09)"

Insert under "Origin Analysis and Elimination Work":

```markdown
### Candidate A Aylesbury family group (FS-verified 2026-05-09)

FamilySearch England, Births and Christenings, 1538-1975 returns four directly relevant Cand A children at Saint Mary, Aylesbury, all with father John Gurney:

- Sarah Gurney, bapt. 22 August 1639
- Daniell Gurney, bapt. 26 December 1645 (FS ID `JWN5-W5B`, attached tree `MSRS-B8Z`)
- Jonathan Gurney, bapt. 22 November 1647 (FS ID `JMBC-P2G`, attached tree `LBKR-M1H`)
- Hannah Gurney, bapt. 12 November 1653

The 1639-1653 family group at Saint Mary Aylesbury is incompatible with the colonial John Gurney's continuous New England career (Weymouth fine June 1641; Wilson v. Faxon deposition 1653; Braintree death 1662/3). Cand A is therefore the Aylesbury John, not the MA emigrant. Combined with the 1628 Bierton with Broughton marriage to Alice Oliffe (Bucks Marriage Index, Bucks Archives PR16/1/1Q p. 30) and the repo-internal 1641 TNA E 115/180/113 cert of residence Aylesbury → Northants and 1650 Walgrave Northants tenancy, the Cand A elimination is effectively complete. Only residual ambiguity is whether the Stewkley 1602/3 baptized John is the same individual; the Stewkley Dickson/Putnam 1897 register pull closes that gap.[^fs-aylesbury-2026-05-09]

[^fs-aylesbury-2026-05-09]: FamilySearch, "England, Births and Christenings, 1538-1975," index entries at FS IDs `JWN5-W5B` (Daniell Gurney 1645) and `JMBC-P2G` (Jonathan Gurney 1647); Sarah Gurney 1639 and Hannah Gurney 1653 surfaced in the same Aylesbury-John-father search. Source ID: `fs-england-births-christenings`.
```

### 4.2 Update Suffolk probate target-pull entry

Replace the existing "SPR Case #338 - Not yet pulled" line with:

```markdown
| SPR Case #338 | Suffolk Probate Records, Case #338 | **Pulled 2026-05-09 via FamilySearch DGS 102840311 (Box 003 Cases 250-399). Cover image 514, inventory image 516 "Boston March 16th 1663". Source ID `fs-suffolk-probate-1636-1915`. Full transcription of inventory items and debtor/creditor list deferred to a focused future pull.** | Done (preliminary) |
```

### 4.3 Probability re-scoring in the "Working Hypotheses" block

Replace the existing Cand A line:

```markdown
- **Candidate A** (Stewkley bapt. 1602/3 → Bierton with Broughton m. 1628 → Aylesbury hundred → Walgrave Northants 1650): **~1-2% (effectively eliminated)**. Documented continuous English residence 1628-1653 incompatible with the MA emigrant. Pull Stewkley register (Dickson/Putnam 1897) to close the Stewkley 1602/3 question.
```

## 5. Apply order

When approved (after v20, v21, v22):

1. Add the two source IDs (`fs-england-births-christenings`, `fs-suffolk-probate-1636-1915`) to `data/sources.json`.
2. Create the two thin validation files in `sources/validations/`.
3. Edit `research/case-files/john-gurney-case-file-v4.md` per §3 (Cand A row rewrite; n9 rewrite; §11 row; n57 qualification).
4. Edit `research/people/g13-john-gurney-fact-sheet.research.md` per §4.
5. Update `sources/intake/working/john-gurney-audit-state.md` to mark v23 as applied.
