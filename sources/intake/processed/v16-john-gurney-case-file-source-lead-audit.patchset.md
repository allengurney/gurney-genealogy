# Intake patchset v16 - John Gurney case-file source-lead audit

> Superseded by `sources/intake/processed/v17-john-gurney-case-file-source-lead-audit-redo.patchset.md`.
> Do not apply v16. It incorrectly proposed corpus-supplement files for short extracts and placed research reasoning in source/corpus space.

```yaml
patchset_id: v16
created: 2026-05-09
repo_scope: gurney-genealogy
phase: phase_1_patchset_only
primary_case_file: research/case-files/john-gurney-case-file-v4.md
primary_research_file: research/people/g13-john-gurney-fact-sheet.research.md
working_memo: sources/intake/working/john-gurney-audit-state.md
phase_2_rule: Apply only after review. Do not add source records for TAG 10:70-73 or SPR Case #338 until those sources are obtained.
```

## 0. Audit outcome

This patchset supersedes the untracked `sources/intake/processed/v15-john-gurney-case-file-audit-cleanup.patchset.md` and folds in the verified portions of:

- `sources/intake/processed/Ready/v15a-john-gurney-bates-braintree-deed-source-cleanup.patchset.md`
- `sources/intake/processed/Ready/v15b-john-gurney-colonial-extracts-source-promotion.patchset.md`

Obtained and usable now:

| Source | Outcome | Main use |
|---|---|---|
| John Winthrop / Savage, *History of New England*, Addenda, 21 July 1636 | Promote | Direct Newgate-apprentice John Gurney evidence; two-Johns pressure |
| Shurtleff, *Records of Massachusetts Bay*, vol. 1, p. 331 | Promote | Direct 1641 General Court fine-remission record |
| Bates, *Ancient Iron Works at Braintree*, p. 10 | Promote via v15a | "John Gurney, Taylor" Braintree conveyance |
| Beers, *Representative Men and Old Families of Southeastern Massachusetts*, Lysander F. Gurney sketch | Promote | Earlier derivative witness for American arms, Lysander manuscript, Newgate/1615 conflict |
| Six local colonial extract files under `John-gurney-research-to-be-assessed/deeds and misc/` | Promote via v15b | Source-layer cleanup for already-held colonial record extracts |

Worked but not obtained:

- `TAG 10:70-73`: targeted searches identify this as Mary Lovering Holman, "Grissell of the Many Marriages," *The American Genealogist* 10 (1933-34):70-73. Treat as Grissell/marriage-chain lead; do not call it the likely source for Anderson's 1636 date.
- `SPR Case #338`: no direct online source found in this pass. Keep as probate pull target.

## 1. Source registry operations

Before applying, verify source IDs are still absent:

```powershell
Select-String -Path data\sources.json -Pattern "winthrop-history-new-england-addenda-1636|massachusetts-bay-records-v1-1853|bates-ancient-iron-works-braintree-1898|representative-men-southeastern-ma-gurney-1912"
```

### 1.1 Add source entries

Add these objects near the existing G13/New England source entries:

```json
    "winthrop-history-new-england-addenda-1636": {
      "shortTitle": "Winthrop, History of New England - Addenda, 1636",
      "citation": "Winthrop, John. The History of New England from 1630 to 1649. Edited by James Savage. 2 vols. Boston: Little, Brown and Company, 1853. Vol. 2, Addenda, pp. 422-423, 21 July 1636 John Newgate / John Gurney apprentice entry.",
      "archive": "Internet Archive OCR / Google Books scan",
      "url": "https://archive.org/details/historynewengla03savagoog",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/winthrop-history-new-england-addenda-1636-john-gurney-newgate.md",
      "mediaPath": null,
      "validationPath": "sources/validations/winthrop-history-new-england-addenda-1636.md",
      "notes": "Direct source for the 21 July 1636 John Newgate / John Gurney apprentice entry. Newgate brought John Gurney, his apprentice, before the governor; Gurney had gotten away his indentures; the order set service until age 24, three years from 29 September. Use as obtained evidence for a Newgate-apprentice John Gurney and the two-Johns/composite-entry problem, not as proof that this apprentice is John Gurney-1 of Braintree."
    },
    "massachusetts-bay-records-v1-1853": {
      "shortTitle": "Massachusetts Bay Records, vol. 1",
      "citation": "Shurtleff, Nathaniel B., ed. Records of the Governor and Company of the Massachusetts Bay in New England. Vol. 1, 1628-1641. Boston: William White, 1853.",
      "archive": "Internet Archive OCR",
      "url": "https://archive.org/details/recordsofgoverno01mass",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/massachusetts-bay-records-v1-1853-john-gurney.md",
      "mediaPath": null,
      "validationPath": "sources/validations/massachusetts-bay-records-v1-1853.md",
      "notes": "Direct source for MBCR 1:331. The 1641 General Court record remitted the fines of John Gurney, James Ludden, and John Porter for want of gunpowder. Use as the controlling source for the court action; Porter remains a secondary context source for identifying Ludden and Gurney as of Weymouth."
    },
    "representative-men-southeastern-ma-gurney-1912": {
      "shortTitle": "Representative Men - Lysander F. Gurney sketch",
      "citation": "Representative Men and Old Families of Southeastern Massachusetts: Containing Historical Sketches of Prominent and Representative Citizens and Genealogical Records of Many of the Old Families. Chicago: J. H. Beers & Co., 1912. Lysander Franklin Gurney sketch.",
      "archive": "AccessGenealogy transcription / original Beers publication",
      "url": "https://accessgenealogy.com/massachusetts/lysander-franklin-gurney.htm",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/representative-men-southeastern-ma-gurney-1912-extract.md",
      "mediaPath": null,
      "validationPath": "sources/validations/representative-men-southeastern-ma-gurney-1912.md",
      "notes": "Derivative but useful 1912 biographical/genealogical sketch for Lysander Franklin Gurney. Preserves the American-branch arms claim, cites a manuscript in the possession of the late Lysander F. Gurney's family, repeats the John Newgate apprentice / 29 September 1615 tradition, and treats Richard Gurney of Weymouth as son according to family records. Use as an early family-memory/manuscript pointer and conflict witness, not as primary proof."
    },
```

Then apply `sources/intake/processed/Ready/v15a-john-gurney-bates-braintree-deed-source-cleanup.patchset.md` section 1 exactly, adding `bates-ancient-iron-works-braintree-1898`.

Then apply `sources/intake/processed/Ready/v15b-john-gurney-colonial-extracts-source-promotion.patchset.md` section 1 exactly, adding the six colonial extract source entries.

Do not add a new source record for `TAG 10:70-73`; keep the existing `tag-10-70` record lead-only unless the article is obtained. Do not add a source record for `SPR Case #338`.

### 1.2 Update `tag-10-70` notes

Replace only the `notes` value for existing `tag-10-70` with:

```json
"Cited by Anderson in the John Gurney sketch. Not yet obtained. 2026-05-09 audit correction: do not treat this as the likely source of Anderson's 1636 arrival date until the article is pulled. Targeted searches identify the article as Mary Lovering Holman, 'Grissell of the Many Marriages,' The American Genealogist 10 (1933-34):70-73, so the current lead hypothesis is that it supports the Grissell Fletcher/Jewell/Griggs/Kibbee/Gurney/Burge marriage sequence."
```

## 2. Corpus files

Create these three new corpus files.

### 2.1 `sources/corpus_supplement/winthrop-history-new-england-addenda-1636-john-gurney-newgate.md`

```markdown
# Winthrop / Savage, History of New England - Addenda - John Newgate and John Gurney, 1636

**Source ID:** `winthrop-history-new-england-addenda-1636`

**Citation:** John Winthrop, *The History of New England from 1630 to 1649*, ed. James Savage, 2 vols. (Boston: Little, Brown and Company, 1853), vol. 2, Addenda, pp. 422-423.

**Scope:** John Newgate / John Gurney apprentice entry only.

## Extract

On 21 July 1636, John Newgate brought John Gurney, described as his apprentice, before the governor. Gurney had gotten away his indentures. The order required him to serve Newgate until age twenty-four, specified as three years from the following 29 September.

## Research use

This is direct evidence that a John Gurney was in the John Newgate apprentice/service context in 1636. It should be used to frame a two-Johns or composite-source problem. Do not identify this apprentice with John Gurney-1 of Braintree without reconciling the 1615 implied birth year against John Gurney-1's 1653 age deposition and likely older child chronology.
```

### 2.2 `sources/corpus_supplement/massachusetts-bay-records-v1-1853-john-gurney.md`

```markdown
# Massachusetts Bay Records, vol. 1 - John Gurney extract

**Source ID:** `massachusetts-bay-records-v1-1853`

**Citation:** Nathaniel B. Shurtleff, ed., *Records of the Governor and Company of the Massachusetts Bay in New England*, vol. 1, 1628-1641 (Boston: William White, 1853), p. 331.

**Scope:** John Gurney entry only.

## Extract

The 1641 General Court record on p. 331 states that John Gurney, James Ludden, and John Porter were remitted the fines they had forfeited for want of gunpowder.

## Research use

This is the controlling court-record source for the 1641 fine-remission event. It supports John Gurney's presence in the Massachusetts Bay record set by June 1641. It does not, in the line itself, supply English origin, age, family, or a Weymouth residence label; Porter and later local histories can remain supporting context for Weymouth identification.
```

### 2.3 `sources/corpus_supplement/representative-men-southeastern-ma-gurney-1912-extract.md`

```markdown
# Representative Men and Old Families of Southeastern Massachusetts - Lysander F. Gurney sketch extract

**Source ID:** `representative-men-southeastern-ma-gurney-1912`

**Citation:** *Representative Men and Old Families of Southeastern Massachusetts* (Chicago: J. H. Beers & Co., 1912), Lysander Franklin Gurney sketch; AccessGenealogy transcription.

**Scope:** John Gurney / American-branch arms / Lysander-family manuscript material only.

## Extract

The Lysander Franklin Gurney sketch states that the Gurney arms cherished by the American branch showed a connection with the English Gurneys. It then reports, from a manuscript in the possession of the late Lysander F. Gurney's family, that there were two early emigrants of the name: Edward Gurney to Cambridge in 1636 and John Gurney to Braintree. The sketch says the latter was an apprentice to John Newgate, was born 29 September 1615, died in 1663, and that Richard Gurney of Weymouth appears to have been his son according to the direct line in the family records.

## Research use

Use this as a derivative family-memory and manuscript-pointer source. It is valuable because it is earlier than the 1926 *American Biography* entry and because it names a family manuscript tradition, but it should not override the 1653 age deposition, the History of Weymouth chronology, or the direct Winthrop Newgate entry.
```

Apply `v15a` section 2 for the Bates corpus and validation files. Apply `v15b` section 2 for the six colonial corpus files, preserving the existing local extract detail.

## 3. Validation files

Create these three validation files.

### 3.1 `sources/validations/winthrop-history-new-england-addenda-1636.md`

```markdown
# Source validation: Winthrop, History of New England - Addenda, 1636

**Source ID:** `winthrop-history-new-england-addenda-1636`

## Examined

John Winthrop, *The History of New England from 1630 to 1649*, ed. James Savage, 2 vols. (Boston: Little, Brown and Company, 1853), vol. 2, Addenda, pp. 422-423, Internet Archive item `historynewengla03savagoog`.

## Scope

- 21 July 1636 John Newgate / John Gurney apprentice entry.
- Nearby date context in the Addenda.

## Validation result

Usable as direct published text of the Winthrop/Savage Addenda entry. Page-image review is still preferable before final quotation, but the OCR and page context are sufficient for source-promotion and research framing.

## Findings proposed in

- `research/people/g13-john-gurney-fact-sheet.research.md`
- `research/case-files/john-gurney-case-file-v4.md`

## Detailed execution trail

`sources/intake/processed/v16-john-gurney-case-file-source-lead-audit.patchset.md`
```

### 3.2 `sources/validations/massachusetts-bay-records-v1-1853.md`

```markdown
# Source validation: Massachusetts Bay Records, vol. 1

**Source ID:** `massachusetts-bay-records-v1-1853`

## Examined

Nathaniel B. Shurtleff, ed., *Records of the Governor and Company of the Massachusetts Bay in New England*, vol. 1, 1628-1641 (Boston: William White, 1853), p. 331, Internet Archive item `recordsofgoverno01mass`.

## Scope

- Page 331 General Court entry remitting fines of John Gurney, James Ludden, and John Porter for want of gunpowder.
- General index confirms "Gurney, John, 331."

## Validation result

Usable as the direct court-record source for MBCR 1:331. It should replace secondary-only reliance for the 1641 fine-remission event.

## Findings proposed in

- `research/people/g13-john-gurney-fact-sheet.research.md`
- `research/case-files/john-gurney-case-file-v4.md`

## Detailed execution trail

`sources/intake/processed/v16-john-gurney-case-file-source-lead-audit.patchset.md`
```

### 3.3 `sources/validations/representative-men-southeastern-ma-gurney-1912.md`

```markdown
# Source validation: Representative Men - Lysander F. Gurney sketch

**Source ID:** `representative-men-southeastern-ma-gurney-1912`

## Examined

*Representative Men and Old Families of Southeastern Massachusetts* (Chicago: J. H. Beers & Co., 1912), Lysander Franklin Gurney sketch, as transcribed at AccessGenealogy.

## Scope

- American-branch arms statement.
- Claimed Lysander-family manuscript.
- John Newgate apprentice / 29 September 1615 tradition.
- Richard Gurney of Weymouth as reported son in family records.

## Validation result

Usable as derivative family-memory/manuscript-pointer evidence. Do not use as primary proof for birth date, parentage, or the John1-Richard relationship.

## Findings proposed in

- `research/people/g13-john-gurney-fact-sheet.research.md`
- `research/case-files/john-gurney-case-file-v4.md`

## Detailed execution trail

`sources/intake/processed/v16-john-gurney-case-file-source-lead-audit.patchset.md`
```

Apply `v15a` section 2.2 and `v15b` section 3 for the Bates and six colonial-extract validation files.

## 4. `research/people/g13-john-gurney-fact-sheet.research.md`

### 4.1 Correct Anderson/TAG interpretation

Replace the current Anderson observation 2:

```markdown
2. **Arrival 1636.** Earlier than the June 1641 Weymouth record that had been treated as John's first Massachusetts appearance. Discrepancy unresolved. TAG 10:70-73 is the most likely source feeding the 1636 date.
```

with:

```markdown
2. **Arrival 1636.** Earlier than the June 1641 Massachusetts Bay record that had been treated as John's first appearance. The likely source for the 1636 date is now the Winthrop/Savage Addenda entry in which John Newgate brought John Gurney, his apprentice, before the governor on 21 July 1636. TAG 10:70-73 has not been obtained; targeted searches identify it as Mary Lovering Holman's "Grissell of the Many Marriages," so it should be treated as a Grissell/marriage-chain lead rather than the likely 1636-arrival source.[^winthrop-newgate-g13]
```

### 4.2 Replace the current Newgate section

Replace the section headed `### The Newgate apprenticeship / 1636 record - de-conflated` through the sentence about John Newgate being documented with:

```markdown
### The Newgate apprenticeship / 1636 record - obtained and de-conflated

The 1636 Newgate lead is now an obtained source, not just a derivative tradition. In the Winthrop/Savage Addenda, under 21 July 1636, John Newgate brought John Gurney, described as his apprentice, before the governor. The entry says Gurney had gotten away his indentures, and that he was ordered to serve Newgate until age twenty-four, specified as three years from the following 29 September.[^winthrop-newgate-g13]

This directly explains the later derivative tradition that a John Gurney was age twenty-one on 29 September 1636 and had three years remaining to serve John Newgate. It also sharpens the problem: the implied 1615 birth year is hard to reconcile with the direct-line John Gurney's 1653 deposition age of about fifty and with a family chronology that places children such as Mary and Richard in the late 1620s or early 1630s. Treat the Newgate apprentice as a serious same-name or composite-entry candidate until the record can be tied to the Braintree man by independent evidence.

John Newgate himself is securely documented in Boston. A 1639 Winthrop-family deed describes him as a Boston feltmaker, matching the occupational context repeated in derivative Gurney accounts.[^newgate-feltmaker-g13]
```

Add these footnotes near the other G13 footnotes:

```markdown
[^winthrop-newgate-g13]: John Winthrop, *The History of New England from 1630 to 1649*, ed. James Savage, 2 vols. (Boston: Little, Brown and Company, 1853), vol. 2, Addenda, pp. 422-423, 21 July 1636 John Newgate / John Gurney apprentice entry, Internet Archive item `historynewengla03savagoog`. Source ID: `winthrop-history-new-england-addenda-1636`.
[^newgate-feltmaker-g13]: "Deed of John Winthrop to John Newgate," 18 December 1639, *Papers of the Winthrop Family*, vol. 4, Massachusetts Historical Society web edition, https://www.masshist.org/publications/winthrop/index.php/view/PWF04p162.
```

### 4.3 Add direct MBCR note under `### Deposition and court records`

Add after the May 1645 petition sentence:

```markdown
**1641 General Court fine remission:** MBCR 1:331 is now pulled. The court record remitted the fines of John Gurney, James Ludden, and John Porter for want of gunpowder. This is the direct source for the earliest Massachusetts Bay appearance; Porter remains useful secondary context because it identifies Ludden and Gurney as of Weymouth, but the court record itself should control the event wording.[^mbcr-gurney-g13]

[^mbcr-gurney-g13]: Nathaniel B. Shurtleff, ed., *Records of the Governor and Company of the Massachusetts Bay in New England*, vol. 1, 1628-1641 (Boston: William White, 1853), p. 331, Internet Archive item `recordsofgoverno01mass`. Source ID: `massachusetts-bay-records-v1-1853`.
```

### 4.4 Add Representative Men under the arms/Newgate conflict

After the existing `American Biography, colonial arms, and the Norfolk-line memory` section, add:

```markdown
The 1912 Lysander Franklin Gurney sketch in *Representative Men and Old Families of Southeastern Massachusetts* is an earlier derivative witness to the same family-memory cluster later repeated in *American Biography*. It states that the American-branch arms showed connection with the English Gurneys, and says the John Newgate apprentice / 29 September 1615 tradition came through a manuscript in the possession of the late Lysander F. Gurney's family. That makes the sketch useful as a pointer to a possible family manuscript and arms object, but it also reinforces the conflict: the family-memory tradition compresses the Newgate apprentice and the Braintree/Weymouth line into one John without reconciling the 1653 age deposition or older-child chronology.[^representative-men-g13]

[^representative-men-g13]: *Representative Men and Old Families of Southeastern Massachusetts* (Chicago: J. H. Beers & Co., 1912), Lysander Franklin Gurney sketch, AccessGenealogy transcription, https://accessgenealogy.com/massachusetts/lysander-franklin-gurney.htm. Source ID: `representative-men-southeastern-ma-gurney-1912`.
```

### 4.5 Apply verified v15a/v15b G13 edits

Apply `v15a` section 4 to add the Bates/Braintree conveyance detail.

Apply `v15b` section 4 to add the promoted colonial property and settlement extracts.

Then update the Anderson source-status table:

```markdown
| WJ 2:422 | Winthrop/Savage Addenda, 21 July 1636 John Newgate / John Gurney apprentice entry | Pulled in v16; use for Newgate/two-Johns pressure, not direct identification | High |
| MBCR 1:331 | *Massachusetts Bay Records*, vol. 1, p. 331 | Pulled in v16; direct fine-remission source | Medium |
| SPR Case #338 | Suffolk Probate Records, Case #338 | Not yet pulled | High |
| TAG 10:70-73 | Mary Lovering Holman, "Grissell of the Many Marriages," *The American Genealogist* 10:70-73 | Not yet pulled; likely Grissell/marriage-chain source, not 1636-arrival source | High |
```

Replace the Tier 1 TAG item:

```markdown
2. **TAG 10:70-73** - likely source of Anderson's 1636 date.
```

with:

```markdown
2. **TAG 10:70-73** - pull for the Grissell Fletcher/Jewell/Griggs/Kibbee/Gurney/Burge marriage-chain problem; do not treat as the likely source of Anderson's 1636 date.
```

Add a new Tier 1 item:

```markdown
4. **SPR Case #338** - probate file may name children, administrator, widow, estate distribution, or other relationship evidence.
```

Renumber the following items as needed.

## 5. `research/case-files/john-gurney-case-file-v4.md`

The case file currently has endnotes through `n71`. If no other patchset has been applied first, use:

- `n72` for Bates, per v15a.
- `n73` for Winthrop/Newgate.
- `n74` for MBCR.
- `n75` for Representative Men.
- `n76` if a single grouped note is needed for the v15b colonial extract set.

### 5.1 Replace baseline table sources

Replace the `First recorded in Colonial America` row with:

```markdown
| **First recorded in <br />Colonial America** | 1641, General Court fine remission for want of gunpowder; Weymouth identification from supporting local-history context | MBCR 1:331<sup class="fn"><a href="#n74" id="ref-74">74</a></sup>; Porter context |
```

Apply `v15a` section 3 to add Bates to the occupation row and split Bates out of Sprague into its own note.

### 5.2 Add Newgate/composite-source paragraph

Add a short paragraph after the baseline table or in section 8/13 where same-name pressure is discussed:

```html
<p><strong>Newgate-apprentice caution.</strong> The 1636 Newgate lead is now an obtained source. In the Winthrop/Savage Addenda, John Newgate brought John Gurney, his apprentice, before the governor on 21 July 1636 after Gurney had gotten away his indentures; the order required service until age twenty-four, three years from the following 29 September. This explains the later 1615-birth tradition, but it also increases two-Johns or composite-entry pressure because the implied age conflicts with John Gurney-1's 1653 "aged about 50" deposition and with the older-child chronology used in this case file.<sup class="fn"><a href="#n73" id="ref-73">73</a></sup></p>
```

### 5.3 Add Representative Men as family-memory conflict evidence

In the "Supplemental heraldic family-memory lead" paragraph, add one sentence before the closing citation:

```html
The 1912 Lysander Franklin Gurney sketch in <em>Representative Men and Old Families of Southeastern Massachusetts</em> is an earlier witness to this same family-memory cluster: it reports American-branch arms, a Lysander-family manuscript, the Newgate-apprentice tradition, and the 29 September 1615 birth date, but without reconciling those claims to the 1653 age deposition.<sup class="fn"><a href="#n75" id="ref-75">75</a></sup>
```

### 5.4 Update `13.4 What's Still Needed`

Replace the current TAG item with:

```markdown
1. **TAG 10:70-73** - pull for direct review of Mary Lovering Holman's "Grissell of the Many Marriages." Current lead value is Grissell's marriage sequence, not Anderson's 1636 date.
```

Replace or add Anderson-reference control language:

```markdown
**Anderson reference-control status.** Anderson cites WJ 2:422, MBCR 1:331, NEHGR 62:94, SPR Case #338, Weymouth Hist 3:251, and TAG 10:70-73. WJ/Newgate, MBCR, NEHGR 62:94, and History of Weymouth have now been pulled or partially incorporated. Remaining high-value pulls are SPR Case #338 and TAG 10:70-73. The Newgate entry is obtained but unresolved: it should be used as two-Johns/composite-source pressure until independently tied to the Braintree man.
```

Apply `v15b` section 5 only as a concise colonial-baseline cleanup note; do not flood the case file with the full colonial extract detail.

### 5.5 Add endnotes

Add before `</ol>`:

```html
  <li id="n73" value="73">John Winthrop, <em>The History of New England from 1630 to 1649</em>, ed. James Savage, 2 vols. (Boston: Little, Brown and Company, 1853), vol. 2, Addenda, pp. 422-423, 21 July 1636 John Newgate / John Gurney apprentice entry; Internet Archive item <code>historynewengla03savagoog</code>. Source ID: <code>winthrop-history-new-england-addenda-1636</code>. <a class="backref" href="#ref-73">Back</a></li>
  <li id="n74" value="74">Nathaniel B. Shurtleff, ed., <em>Records of the Governor and Company of the Massachusetts Bay in New England</em>, vol. 1, 1628-1641 (Boston: William White, 1853), p. 331, remission of fines of John Gurney, James Ludden, and John Porter for want of gunpowder; Internet Archive item <code>recordsofgoverno01mass</code>. Source ID: <code>massachusetts-bay-records-v1-1853</code>. <a class="backref" href="#ref-74">Back</a></li>
  <li id="n75" value="75"><em>Representative Men and Old Families of Southeastern Massachusetts</em> (Chicago: J. H. Beers &amp; Co., 1912), Lysander Franklin Gurney sketch, AccessGenealogy transcription, American-branch arms, Lysander-family manuscript, Newgate-apprentice, and 29 September 1615 tradition. Source ID: <code>representative-men-southeastern-ma-gurney-1912</code>. <a class="backref" href="#ref-75">Back</a></li>
```

If v15a adds `n72`, keep it before `n73`. If v15b adds a grouped case-file note, assign it `n76` and keep all backrefs synchronized.

## 6. Follow-up decisions

- `SPR Case #338`: genuine high-value inaccessible/paywalled/offline pull. Do not create source record yet.
- `TAG 10:70-73`: obtain article before using. Current searches support a Grissell-focused purpose.
- `Two Directory Entries - English emigrants to New England_backup version.md`: do not promote until conflict markers are cleaned and it is attached to existing Banks/Anderson records.
- `tna-probate-analysis-john-gurney.md`: valuable later candidate-exclusion appendix, but not part of this source-lead patchset unless the user asks for a TNA/PCC-focused Phase 1.

## 7. Acceptance checks

After Phase 2 application:

```powershell
Select-String -Path data\sources.json -Pattern "winthrop-history-new-england-addenda-1636|massachusetts-bay-records-v1-1853|representative-men-southeastern-ma-gurney-1912|bates-ancient-iron-works-braintree-1898"
Select-String -Path research\people\g13-john-gurney-fact-sheet.research.md -Pattern "winthrop-newgate-g13|mbcr-gurney-g13|representative-men-g13|TAG 10"
Select-String -Path research\case-files\john-gurney-case-file-v4.md -Pattern "#n72|#n73|#n74|#n75|ref-72|ref-73|ref-74|ref-75|Newgate-apprentice caution"
git diff --check
```

If content is applied to publishable site-facing research files, run the normal site validation from `site/website`.
