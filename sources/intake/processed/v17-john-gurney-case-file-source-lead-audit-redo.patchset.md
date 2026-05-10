# Intake patchset v17 - John Gurney source-lead audit redo

```yaml
patchset_id: v17
created: 2026-05-09
repo_scope: gurney-genealogy
phase: phase_1_patchset_only
supersedes: sources/intake/processed/v16-john-gurney-case-file-source-lead-audit.patchset.md
primary_case_file: research/case-files/john-gurney-case-file-v4.md
primary_research_file: research/people/g13-john-gurney-fact-sheet.research.md
working_memo: sources/intake/working/john-gurney-audit-state.md
phase_2_rule: Apply only after review. Do not create corpus-supplement files for the short extracts in this patchset.
```

## 0. Audit report

### 0.1 Salvaged useful findings from prior attempts

- `v15-john-gurney-case-file-audit-cleanup.patchset.md` was useful mainly for the policy correction that leads are not source records. It is not sufficient as a final audit because it left the Anderson citation set mostly unworked.
- `Ready/v15a` correctly identified the Bates/Braintree deed gap, but its corpus proposal is too heavy for a short extract. Bates should become a source entry, thin validation, and research/case-file citation.
- `Ready/v15b` correctly noticed that colonial extracts under `research/case-files/John-gurney-research-to-be-assessed/deeds and misc/` are underused. Do not apply it as written; it defaults too much material into corpus. Treat those files as a follow-on research/source cleanup pass.
- The current live case file already includes v11-era additions through endnote `n71`. Preserve those as the baseline and add only targeted new notes.

### 0.2 Internal repo/library opportunities found and worked

| Rank | Opportunity | Outcome | Incorporation decision |
|---|---|---|---|
| 1 | G13 says TAG 10:70-73 likely feeds Anderson's 1636 date | Worked against targeted web/title evidence | Correct G13 and case-file future-research text: TAG is a Grissell marriage-chain article lead, not the 1636 Newgate source |
| 2 | G13 says underlying Newgate apprenticeship record not pulled | Worked online via Winthrop/Savage Addenda | Add source entry, thin validation, G13 Newgate section, and case-file competing-candidate note |
| 3 | Case file embeds Bates in the Sprague note | Worked online, Bates p. 10 confirmed | Add Bates source entry/validation; cite separately in occupation/property discussion |
| 4 | `John-gurney-research-to-be-assessed/deeds and misc/` contains substantive colonial extracts | Targeted scan only | Preserve as next patchset; convert to research/source entries, not default corpus |
| 5 | `Two Directory Entries - English emigrants to New England_backup version.md` has conflict markers | Targeted scan | Do not promote until conflict cleanup |

### 0.3 Online leads worked

| Lead | Search angle | Outcome | Decision |
|---|---|---|---|
| WJ 2:422 / Winthrop Addenda | John Newgate + John Gurney + indentures/service | Direct 21 July 1636 Newgate-apprentice entry located in Winthrop/Savage Addenda | Promote source; use for two-Johns/composite pressure |
| MBCR 1:331 | Massachusetts Bay Records p. 331 + associates John Porter/James Ludden | Direct General Court fine-remission entry located | Promote source; use as controlling 1641 court citation |
| Bates p. 10 | Braintree + Richard Thayer + Monatiquot + tailor | 12 Feb. 1661 conveyance located | Promote source; no corpus |
| TAG 10:70-73 | title/author/content searches | Article identified as Mary Lovering Holman, "Grissell of the Many Marriages"; not obtained | Keep as pull target; no new source record beyond existing lead entry |
| SPR Case #338 | Suffolk probate case/citation searches | Probate file not located online; Suffolk probate index vol. 2 located | Promote index source cautiously; keep probate file as pull target |
| Representative Men / Lysander F. Gurney | Lysander + Newgate + manuscript + arms | AccessGenealogy transcription and IA/OpenLibrary bibliographic pages located | Promote as derivative manuscript-pointer source; no corpus |
| John Newgate occupation | MHS Winthrop Papers deed | 1639 deed identifies John Newgate of Boston as feltmaker | Promote source if used in G13 context |

### 0.4 Candidate implications

- The Winthrop/Newgate evidence weakens a single-person reading of the 1636 arrival date. A John Gurney serving John Newgate until age 24 from 29 September 1636 implies a birth around 29 September 1615. That conflicts with the Braintree John aged about 50 in 1652/3 and with the older-child chronology used for Richard/Mary/Peter/John/Isaac.
- The evidence does not identify another fully viable English-origin candidate. It strengthens the two-Johns/composite-source explanation: Anderson's "1636; Boston, Braintree" may conflate a Boston/Newgate apprentice with the older Braintree/Weymouth man.
- Bates strengthens Candidate B only indirectly: it confirms John Gurney as a tailor in Braintree in 1661, fitting the Merchant Taylor father/son occupational argument. It does not prove English origin.
- The Suffolk probate index supports the case-file's probate anchor by confirming the existence of a John Gurney/Gurny administration case no. 338 in the 1663 probate-index context, but the case file itself remains necessary for heirs, inventory, and relationship evidence.

### 0.5 Ranked patchsets

1. Apply this v17 source-lead correction: new source records, thin validations, G13/case-file updates, no small-extract corpus.
2. Follow with a corrected colonial-extract patchset replacing v15b: source records plus substantive research insertions for Suffolk Deeds, Mendon Proprietors, Ballou, Bartlett, Porter, and Nash; corpus only if a held extract is large enough to justify source-text preservation.
3. Then work inaccessible/high-value pulls: Suffolk probate case #338, TAG 10:70-73, Suffolk Court Files item 188, original Braintree town/vital/deed entries, Lysander-family manuscript/arms object, and Bury St Edmunds/Newgate apprenticeship records.

## 1. Source registry operations

Before applying, verify the proposed IDs are still absent:

```powershell
Select-String -Path data\sources.json -Pattern "winthrop-history-new-england-addenda-1636|massachusetts-bay-records-v1-1853|bates-ancient-iron-works-braintree-1898|accessgenealogy-lysander-franklin-gurney|suffolk-probate-index-v2-1895|mhs-winthrop-papers-newgate-deed-1639"
```

### 1.1 Add six source entries

Add these objects near the existing G13/New England source entries in `data/sources.json`.

```json
    "winthrop-history-new-england-addenda-1636": {
      "shortTitle": "Winthrop/Savage, History of New England Addenda",
      "citation": "Winthrop, John. The History of New England from 1630 to 1649. Edited by James Savage. Vol. 2. Boston: Little, Brown and Company, 1853. Addenda, p. 422, 21 July 1636 John Newgate / John Gurney apprentice entry.",
      "archive": "Internet Archive",
      "url": "https://archive.org/details/historynewengla03savagoog",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/winthrop-history-new-england-addenda-1636.md",
      "notes": "Direct published text of the 21 July 1636 John Newgate / John Gurney apprentice entry. Use for the Newgate-apprentice chronology and two-Johns/composite-source problem, not as proof that the apprentice was John Gurney of Braintree."
    },
    "massachusetts-bay-records-v1-1853": {
      "shortTitle": "Massachusetts Bay Records, vol. 1",
      "citation": "Shurtleff, Nathaniel B., ed. Records of the Governor and Company of the Massachusetts Bay in New England. Vol. 1, 1628-1641. Boston: William White, 1853.",
      "archive": "Internet Archive",
      "url": "https://archive.org/details/recordsofgoverno01mass",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/massachusetts-bay-records-v1-1853.md",
      "notes": "Direct source for MBCR 1:331. The 1641 General Court record remits fines of John Gurney, James Ludden, and John Porter for want of gunpowder. Use as the controlling court citation; Weymouth identification depends on supporting local context."
    },
    "bates-ancient-iron-works-braintree-1898": {
      "shortTitle": "Bates, Ancient Iron Works at Braintree",
      "citation": "Bates, Samuel A. The Ancient Iron Works at Braintree, Mass.: The First in America. South Braintree, Mass.: Frank A. Bates, 1898.",
      "archive": "Internet Archive",
      "url": "https://archive.org/details/ancientironworks00bate",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/bates-ancient-iron-works-braintree-1898.md",
      "notes": "Source for the page-10 12 February 1661 Braintree conveyance identifying John Gurney as tailor and describing the sale to Richard Thayer. Use for occupation, Braintree property, and neighborhood context, not English origin."
    },
    "accessgenealogy-lysander-franklin-gurney": {
      "shortTitle": "AccessGenealogy, Lysander Franklin Gurney",
      "citation": "AccessGenealogy. \"Ancestry of Lysander Franklin Gurney.\" Transcription from Representative Men and Old Families of Southeastern Massachusetts (Chicago: J. H. Beers & Co., 1912).",
      "archive": "AccessGenealogy / Internet Archive cataloged original publication",
      "url": "https://accessgenealogy.com/massachusetts/lysander-franklin-gurney.htm",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/accessgenealogy-lysander-franklin-gurney.md",
      "notes": "Derivative transcription preserving a Lysander-family manuscript claim, American-branch arms tradition, and the Newgate/29 September 1615 conflict tradition. Use as a manuscript-pointer and conflict witness, not as primary proof."
    },
    "suffolk-probate-index-v2-1895": {
      "shortTitle": "Suffolk Probate Index, vol. 2",
      "citation": "George, Elijah, register. Index to the Probate Records of the County of Suffolk, Massachusetts, from the Year 1636 to and including the Year 1893. Vol. 2, G to O. Boston: Rockwell and Churchill, City Printers, 1895.",
      "archive": "Internet Archive",
      "url": "https://archive.org/details/indextoprobatere02geor",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/suffolk-probate-index-v2-1895.md",
      "notes": "Index source for the Gurney/Gurny probate entries. Use to confirm the probate-index existence of John Gurney/Gurny administration case no. 338 in the 1663 context; the underlying Suffolk probate case file remains a necessary pull target."
    },
    "mhs-winthrop-papers-newgate-deed-1639": {
      "shortTitle": "MHS Winthrop Papers, Newgate deed",
      "citation": "Massachusetts Historical Society, Winthrop Papers Digital Edition, Papers of the Winthrop Family, vol. 4, deed of John Winthrop to John Newgate, 18 December 1639.",
      "archive": "Massachusetts Historical Society",
      "url": "https://www.masshist.org/publications/winthrop/index.php/view/PWF04p162",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/mhs-winthrop-papers-newgate-deed-1639.md",
      "notes": "Context source identifying John Newgate of Boston as a feltmaker in a 1639 Winthrop deed. Use only for Newgate occupational/context discussion."
    },
```

### 1.2 Update existing `tag-10-70` note

Replace only the `notes` value for `tag-10-70`:

```json
"Cited by Anderson in the John Gurney sketch. Article not yet obtained. Targeted title/content searches identify this as Mary Lovering Holman, 'Grissell of the Many Marriages,' The American Genealogist 10 (1933-34):70-73. Treat as a Grissell Fletcher/Jewell/Griggs/Kibbee/Gurney/Burge marriage-chain pull target, not as the likely source of Anderson's 1636 Newgate date unless the article itself proves otherwise."
```

## 2. Validation files

Create these thin files. Do not paste the research analysis into them.

### 2.1 `sources/validations/winthrop-history-new-england-addenda-1636.md`

```markdown
# Source validation: Winthrop/Savage, History of New England Addenda

**Source ID:** `winthrop-history-new-england-addenda-1636`

## Examined

John Winthrop, *The History of New England from 1630 to 1649*, ed. James Savage, vol. 2 (Boston: Little, Brown and Company, 1853), Addenda, p. 422, Internet Archive item `historynewengla03savagoog`.

## Scope

- 21 July 1636 John Newgate / John Gurney apprentice entry.

## Validation result

Usable for the Newgate-apprentice chronology and the two-Johns/composite-source question. Page-image review is preferable before using a verbatim long quotation.

## Findings recorded in

- `research/people/g13-john-gurney-fact-sheet.research.md`
- `research/case-files/john-gurney-case-file-v4.md`

## Patchset

`sources/intake/processed/v17-john-gurney-case-file-source-lead-audit-redo.patchset.md`
```

### 2.2 `sources/validations/massachusetts-bay-records-v1-1853.md`

```markdown
# Source validation: Massachusetts Bay Records, vol. 1

**Source ID:** `massachusetts-bay-records-v1-1853`

## Examined

Nathaniel B. Shurtleff, ed., *Records of the Governor and Company of the Massachusetts Bay in New England*, vol. 1, 1628-1641 (Boston: William White, 1853), p. 331, Internet Archive item `recordsofgoverno01mass`.

## Scope

- Page 331 General Court fine-remission entry naming John Gurney, James Ludden, and John Porter.
- General index entry for John Gurney checked as a locator.

## Validation result

Usable as the direct court-record citation for MBCR 1:331. The line itself does not supply English origin, age, family, or a Weymouth residence label.

## Findings recorded in

- `research/people/g13-john-gurney-fact-sheet.research.md`
- `research/case-files/john-gurney-case-file-v4.md`

## Patchset

`sources/intake/processed/v17-john-gurney-case-file-source-lead-audit-redo.patchset.md`
```

### 2.3 `sources/validations/bates-ancient-iron-works-braintree-1898.md`

```markdown
# Source validation: Bates, Ancient Iron Works at Braintree

**Source ID:** `bates-ancient-iron-works-braintree-1898`

## Examined

Samuel A. Bates, *The Ancient Iron Works at Braintree, Mass.: The First in America* (South Braintree, Mass.: Frank A. Bates, 1898), p. 10, Internet Archive item `ancientironworks00bate`.

## Scope

- Page 10 12 February 1661 John Gurney conveyance to Richard Thayer.

## Validation result

Usable as a printed local-history/deed extract for occupation and Braintree property context. The underlying Braintree deed record remains a separate pull target.

## Findings recorded in

- `research/people/g13-john-gurney-fact-sheet.research.md`
- `research/case-files/john-gurney-case-file-v4.md`

## Patchset

`sources/intake/processed/v17-john-gurney-case-file-source-lead-audit-redo.patchset.md`
```

### 2.4 `sources/validations/accessgenealogy-lysander-franklin-gurney.md`

```markdown
# Source validation: AccessGenealogy, Lysander Franklin Gurney

**Source ID:** `accessgenealogy-lysander-franklin-gurney`

## Examined

AccessGenealogy, "Ancestry of Lysander Franklin Gurney," transcription from *Representative Men and Old Families of Southeastern Massachusetts* (Chicago: J. H. Beers & Co., 1912).

## Scope

- American-branch arms statement.
- Lysander-family manuscript statement.
- John Newgate apprentice / 29 September 1615 tradition.
- Richard Gurney of Weymouth as reported son in family records.

## Validation result

Usable as derivative family-memory/manuscript-pointer evidence. Do not use as primary proof of birth date, parentage, or the John-Richard relationship.

## Findings recorded in

- `research/people/g13-john-gurney-fact-sheet.research.md`
- `research/case-files/john-gurney-case-file-v4.md`

## Patchset

`sources/intake/processed/v17-john-gurney-case-file-source-lead-audit-redo.patchset.md`
```

### 2.5 `sources/validations/suffolk-probate-index-v2-1895.md`

```markdown
# Source validation: Suffolk Probate Index, vol. 2

**Source ID:** `suffolk-probate-index-v2-1895`

## Examined

Elijah George, register, *Index to the Probate Records of the County of Suffolk, Massachusetts, from the Year 1636 to and including the Year 1893*, vol. 2, G to O (Boston: Rockwell and Churchill, City Printers, 1895), Gurney/Gurny entries, Internet Archive item `indextoprobatere02geor`.

## Scope

- Gurney/Gurny probate-index entries around the John administration case no. 338.

## Validation result

Usable as an index locator for John Gurney/Gurny administration case no. 338 in the 1663 probate context. The probate case file itself remains unexamined.

## Findings recorded in

- `research/people/g13-john-gurney-fact-sheet.research.md`
- `research/case-files/john-gurney-case-file-v4.md`

## Patchset

`sources/intake/processed/v17-john-gurney-case-file-source-lead-audit-redo.patchset.md`
```

### 2.6 `sources/validations/mhs-winthrop-papers-newgate-deed-1639.md`

```markdown
# Source validation: MHS Winthrop Papers, Newgate deed

**Source ID:** `mhs-winthrop-papers-newgate-deed-1639`

## Examined

Massachusetts Historical Society, Winthrop Papers Digital Edition, Papers of the Winthrop Family, vol. 4, deed of John Winthrop to John Newgate, 18 December 1639.

## Scope

- Deed heading and body identification of John Newgate of Boston as feltmaker.

## Validation result

Usable as a context source for John Newgate's occupation and Boston setting.

## Findings recorded in

- `research/people/g13-john-gurney-fact-sheet.research.md`

## Patchset

`sources/intake/processed/v17-john-gurney-case-file-source-lead-audit-redo.patchset.md`
```

## 3. `research/people/g13-john-gurney-fact-sheet.research.md`

### 3.1 Update opening summary

Current opening sentence includes:

```markdown
Emigrated to New England by June 1641 at latest; Anderson assigns 1636 arrival (unresolved).
```

Replace that clause with:

```markdown
Emigrated to New England by June 1641 at latest; Anderson assigns 1636 arrival, probably reflecting the John Newgate apprentice record rather than the first secure Braintree/Weymouth record.
```

### 3.2 Replace Anderson assessment item 2

Replace current item 2 under `### External compiler assessments (Anderson, Banks)`:

```markdown
2. **Arrival 1636.** Earlier than the June 1641 Weymouth record that had been treated as John's first Massachusetts appearance. Discrepancy unresolved. TAG 10:70–73 is the most likely source feeding the 1636 date.
```

With:

```markdown
2. **Arrival 1636.** Winthrop/Savage's Addenda gives a direct 21 July 1636 record in which John Newgate brought John Gurney, his apprentice, before the governor after Gurney had gotten away his indentures. The order set service until age 24, three years from the following 29 September. That record is the strongest visible source for Anderson's 1636 date, but it creates a chronology conflict if identified with the older Braintree John: the implied 29 September 1615 birth is difficult to reconcile with John Gurney of Braintree aged about 50 in 1652/3 and with the older-child chronology. TAG 10:70–73 appears instead to be the Grissell Fletcher marriage-chain article.[^winthrop-addenda-newgate][^tag-grissell-lead]
```

Add footnotes near the other G13 footnotes:

```markdown
[^winthrop-addenda-newgate]: John Winthrop, *The History of New England from 1630 to 1649*, ed. James Savage, vol. 2 (Boston: Little, Brown and Company, 1853), Addenda, p. 422, 21 July 1636 John Newgate / John Gurney apprentice entry. Source ID: `winthrop-history-new-england-addenda-1636`.
[^tag-grissell-lead]: `tag-10-70` remains a pull target. Targeted title/content searches identify it as Mary Lovering Holman, "Grissell of the Many Marriages," *The American Genealogist* 10 (1933-34):70-73, a Grissell Fletcher/Jewell/Griggs/Kibbee/Gurney/Burge article lead.
```

### 3.3 Replace Newgate section

Replace the text under `### The Newgate apprenticeship / 1636 record — de-conflated` through the sentence about the underlying original not yet pulled with:

```markdown
Winthrop/Savage's Addenda records the 21 July 1636 Newgate episode directly. John Newgate brought John Gurney, described as his apprentice, before the governor; Gurney had gotten away his indentures; the order required service until age 24, specified as three years from the following 29 September.[^winthrop-addenda-newgate]

That record explains the derivative tradition that John Gurney was age 21 on 29 September 1636 and therefore born about 29 September 1615. It does not, by itself, identify the apprentice as John Gurney of Braintree. The 1615 chronology remains in tension with the Braintree age witness of about 50 in 1652/3 and with the older-child chronology attached to Richard, Mary, Peter, John, and Isaac.

John Newgate himself is securely documented in Boston. A 1639 Winthrop deed identifies him as "John Newgate of Boston in New England Feltmaker," which fits the hatter/feltmaker form in later derivative accounts.[^mhs-newgate-feltmaker]
```

Add footnote:

```markdown
[^mhs-newgate-feltmaker]: Massachusetts Historical Society, Winthrop Papers Digital Edition, Papers of the Winthrop Family, vol. 4, deed of John Winthrop to John Newgate, 18 Dec. 1639, https://www.masshist.org/publications/winthrop/index.php/view/PWF04p162. Source ID: `mhs-winthrop-papers-newgate-deed-1639`.
```

### 3.4 Add direct MBCR note

In `### Community and probate records in Braintree, Billerica, and Suffolk County`, add before the NEHGR 62:94 paragraph:

```markdown
The Massachusetts Bay Records entry behind MBCR 1:331 is a direct court-record anchor for John Gurney's presence in the colony by June 1641. The page records that John Gurney, James Ludden, and John Porter had their fines remitted for want of gunpowder. The entry is a court action, not an origin, age, family, or residence statement; Weymouth identification still depends on the associated local-history context.[^mbcr-gurney-1641]
```

Add footnote:

```markdown
[^mbcr-gurney-1641]: Nathaniel B. Shurtleff, ed., *Records of the Governor and Company of the Massachusetts Bay in New England*, vol. 1, 1628-1641 (Boston: William White, 1853), p. 331. Source ID: `massachusetts-bay-records-v1-1853`.
```

### 3.5 Add Bates/property note

Under the land/property section, add:

```markdown
The 12 February 1661 Braintree conveyance printed by Samuel A. Bates identifies the grantor as John Gurney, tailor. Gurney conveyed to Richard Thayer, for fourteen pounds, a house and orchard, a five-acre parcel on the Monatiquot/Monoticot River, and an adjacent half-acre parcel. The record is useful for occupation, Braintree property, and neighborhood reconstruction; it is not English-origin evidence.[^bates-ironworks-gurney]
```

Add footnote:

```markdown
[^bates-ironworks-gurney]: Samuel A. Bates, *The Ancient Iron Works at Braintree, Mass.: The First in America* (South Braintree, Mass.: Frank A. Bates, 1898), p. 10. Source ID: `bates-ancient-iron-works-braintree-1898`.
```

### 3.6 Add probate-index note

After the probate/Baxter paragraphs, add:

```markdown
The Suffolk probate index for vol. 2, G to O, identifies the Gurney/Gurny probate-index entry for John Gurney/Gurny administration case no. 338 in the 1663 context. This confirms the case-number anchor used by Anderson and the case file, but the underlying probate file is still needed for the inventory, administration details, and any relationship statements.[^suffolk-probate-index-gurney]
```

Add footnote:

```markdown
[^suffolk-probate-index-gurney]: Elijah George, register, *Index to the Probate Records of the County of Suffolk, Massachusetts, from the Year 1636 to and including the Year 1893*, vol. 2, G to O (Boston: Rockwell and Churchill, City Printers, 1895), Gurney/Gurny entries. Source ID: `suffolk-probate-index-v2-1895`.
```

### 3.7 Add family-memory/manuscript note

After the existing 1926 American Biography paragraph, add:

```markdown
The Lysander Franklin Gurney sketch in *Representative Men and Old Families of Southeastern Massachusetts*, as transcribed by AccessGenealogy, preserves an earlier form of the same family-memory problem. It says the American branch cherished Gurney arms, cites a manuscript in the possession of the late Lysander F. Gurney's family, and presents John of Braintree as a John Newgate apprentice born 29 September 1615, with Richard of Weymouth appearing as son according to the family records. Treat the passage as a manuscript pointer and conflict witness, not as controlling proof over the Braintree age and chronology evidence.[^accessgenealogy-lysander]
```

Add footnote:

```markdown
[^accessgenealogy-lysander]: AccessGenealogy, "Ancestry of Lysander Franklin Gurney," transcription from *Representative Men and Old Families of Southeastern Massachusetts* (Chicago: J. H. Beers & Co., 1912), https://accessgenealogy.com/massachusetts/lysander-franklin-gurney.htm. Source ID: `accessgenealogy-lysander-franklin-gurney`.
```

### 3.8 Update Anderson citation pull list

Replace the rows for WJ, MBCR, SPR, and TAG in `### Anderson citation pull list` with:

```markdown
| WJ 2:422 | Winthrop/Savage Addenda, 21 July 1636 Newgate/Gurney apprentice entry | Direct source identified; use for Newgate/two-Johns pressure | Incorporated by v17 |
| MBCR 1:331 | *Massachusetts Bay Records*, vol. 1, p. 331 | Direct source identified; controls 1641 court action | Incorporated by v17 |
| NEHGR 62:94 | *New England Historical and Genealogical Register*, vol. 62, p. 94 | Pulled in v08/v08a; underlying Suffolk Court Files paper still unpulled | High |
| SPR Case #338 | Suffolk Probate Records, Case #338 | Probate index confirms case-number anchor; case file still unpulled | Highest |
| Weymouth Hist 3:251 | *History of Weymouth*, vol. 3 | Already registered as derivative family/group source | Incorporated earlier |
| TAG 10:70-73 | Mary Lovering Holman, "Grissell of the Many Marriages" | Not obtained; likely Grissell marriage-chain support, not 1636 source | High |
```

Replace the related checklist bullets near the end:

```markdown
- [ ] Pull **TAG 10:70–73** and extract only the Grissell/Gurney marriage-chain evidence it actually contains.
- [ ] Pull **SPR Case #338**; probate index confirms the case-number anchor, but the file may contain inventory, administration, or relationship details.
- [ ] Reconcile **Anderson's 1636** with the **June 1641 court record** as a likely Newgate-apprentice/two-Johns issue.
- [ ] Determine whether Anderson's **"Boston"** comes from the Newgate/Boston apprentice entry, a real pre-Braintree residence for the older John, or a composite entry.
```

## 4. `research/case-files/john-gurney-case-file-v4.md`

### 4.1 Baseline table updates

Replace occupation row:

```markdown
| **Occupation** | Tailor | Sprague, p. 695<sup class="fn"><a href="#n2" id="ref-2">2</a></sup>; Bates, p. 10<sup class="fn"><a href="#n72" id="ref-72">72</a></sup> |
```

Replace first-record row:

```markdown
| **First recorded in <br />Colonial America** | June 1641 General Court fine-remission record; Weymouth identification depends on supporting local context | MBCR 1:331<sup class="fn"><a href="#n73" id="ref-73">73</a></sup> |
```

Replace estate/death row:

```markdown
| **Estate / Death** | Died intestate; inventory dated 16 Mar 1662/63; Suffolk probate index identifies administration case no. 338 in the 1663 context | SPR Case #338; Suffolk probate index<sup class="fn"><a href="#n74" id="ref-74">74</a></sup> |
```

### 4.2 Add competing-candidate note

After the discussion of Banks/Bury St Edmunds in the English-origin argument, add:

```markdown
The 1636 Newgate apprentice record is a major caution against treating every early "John Gurney" reference as the same man. Winthrop/Savage's Addenda records John Newgate bringing his apprentice John Gurney before the governor on 21 July 1636 after the apprentice had gotten away his indentures; the order set service until age 24, three years from the following 29 September. If that apprentice was born about 29 September 1615, he is difficult to reconcile with the older Braintree man aged about 50 in 1652/3 and with the traditional older-child chronology. This supports a two-Johns or composite-source explanation for Anderson's "1636; Boston, Braintree" entry.<sup class="fn"><a href="#n75" id="ref-75">75</a></sup>
```

### 4.3 Add family-memory caution

Near the source discussion of derivative family traditions, add:

```markdown
The Lysander Franklin Gurney sketch preserves a useful family-memory lead rather than proof. Its cited family manuscript links John of Braintree to John Newgate, gives the 29 September 1615 birth tradition, and says Richard of Weymouth appears as son in the family records. That makes it a pointer to a possible manuscript/arms object and a witness to the composite tradition, not a controlling source for parentage or chronology.<sup class="fn"><a href="#n76" id="ref-76">76</a></sup>
```

### 4.4 Replace section 13.4 top items

Replace the first two items currently reading TAG as the likely 1636 source and SPR as generic future pull with:

```markdown
1. **Suffolk Probate Records Case #338** — the Suffolk probate index confirms the John Gurney/Gurny administration case-number anchor in the 1663 context, but the case file itself is still needed for inventory, administrator, distribution, and relationship evidence.
2. **TAG 10:70-73** — pull Mary Lovering Holman's "Grissell of the Many Marriages" for Grissell Fletcher's marriage sequence; do not treat it as the likely 1636 Newgate source unless the article itself proves otherwise.
3. **Suffolk Court Files item no. 188** — underlying file behind the 1652/3 Braintree age note remains high value.
4. **Original Braintree town/vital/deed entries** — especially the 1661 wife death/marriage context and the 12 Feb. 1661 Richard Thayer conveyance behind Bates.
5. **Lysander-family manuscript / arms object** — the 1912/AccessGenealogy tradition points to family-held material that may clarify whether the Newgate tradition was copied into the American branch from a manuscript or from printed compilers.
```

### 4.5 Endnotes

Replace current `n2` so it no longer embeds Bates under Sprague:

```html
  <li id="n2" value="2">Waldo Chamberlain Sprague, <em>Genealogies of the Families of Braintree, Mass., 1640-1850</em> (Boston: New England Historic Genealogical Society, 2001), p. 695, John Gurney entry. Source ID: <code>sprague-braintree</code>. <a class="backref" href="#ref-2">↩</a></li>
```

Add new notes before `</ol>`:

```html
  <li id="n72" value="72">Samuel A. Bates, <em>The Ancient Iron Works at Braintree, Mass.: The First in America</em> (South Braintree, Mass.: Frank A. Bates, 1898), p. 10, 12 Feb. 1661 conveyance identifying John Gurney as tailor and conveying Braintree property to Richard Thayer. Source ID: <code>bates-ancient-iron-works-braintree-1898</code>. <a class="backref" href="#ref-72">↩</a></li>
  <li id="n73" value="73">Nathaniel B. Shurtleff, ed., <em>Records of the Governor and Company of the Massachusetts Bay in New England</em>, vol. 1, 1628-1641 (Boston: William White, 1853), p. 331, General Court fine-remission entry for John Gurney, James Ludden, and John Porter. Source ID: <code>massachusetts-bay-records-v1-1853</code>. <a class="backref" href="#ref-73">↩</a></li>
  <li id="n74" value="74">Elijah George, register, <em>Index to the Probate Records of the County of Suffolk, Massachusetts, from the Year 1636 to and including the Year 1893</em>, vol. 2, G to O (Boston: Rockwell and Churchill, City Printers, 1895), Gurney/Gurny entries, John administration case no. 338 in the 1663 context; compare Suffolk Probate Records Case #338, John Gurney estate, still to be examined directly. Source ID: <code>suffolk-probate-index-v2-1895</code>. <a class="backref" href="#ref-74">↩</a></li>
  <li id="n75" value="75">John Winthrop, <em>The History of New England from 1630 to 1649</em>, ed. James Savage, vol. 2 (Boston: Little, Brown and Company, 1853), Addenda, p. 422, 21 July 1636 John Newgate / John Gurney apprentice entry; Massachusetts Historical Society, Winthrop Papers Digital Edition, Papers of the Winthrop Family, vol. 4, deed of John Winthrop to John Newgate, 18 Dec. 1639, identifying Newgate of Boston as feltmaker. Source IDs: <code>winthrop-history-new-england-addenda-1636</code>; <code>mhs-winthrop-papers-newgate-deed-1639</code>. <a class="backref" href="#ref-75">↩</a></li>
  <li id="n76" value="76">AccessGenealogy, "Ancestry of Lysander Franklin Gurney," transcription from <em>Representative Men and Old Families of Southeastern Massachusetts</em> (Chicago: J. H. Beers & Co., 1912), https://accessgenealogy.com/massachusetts/lysander-franklin-gurney.htm. Source ID: <code>accessgenealogy-lysander-franklin-gurney</code>. <a class="backref" href="#ref-76">↩</a></li>
```

## 5. Do not do in this patchset

- Do not create `sources/corpus_supplement/` files for Winthrop/Savage, MBCR, Bates, AccessGenealogy/Representative Men, the Suffolk probate index, or the MHS Newgate deed.
- Do not add a new source record for TAG 10:70-73 beyond the existing lead-only `tag-10-70` record until the article is obtained.
- Do not add a source record for Suffolk Probate Records Case #338 itself until the probate file is obtained.
- Do not apply `v15b` as written. Its source opportunities are real, but the destination model should be research/source entries plus thin validations, not blanket corpus copying.
- Do not promote `Two Directory Entries - English emigrants to New England_backup version.md` while it contains conflict markers.

## 6. Validation checklist after application

```powershell
Select-String -Path data\sources.json -Pattern "winthrop-history-new-england-addenda-1636|massachusetts-bay-records-v1-1853|bates-ancient-iron-works-braintree-1898|accessgenealogy-lysander-franklin-gurney|suffolk-probate-index-v2-1895|mhs-winthrop-papers-newgate-deed-1639"
Test-Path sources\validations\winthrop-history-new-england-addenda-1636.md
Test-Path sources\validations\massachusetts-bay-records-v1-1853.md
Test-Path sources\validations\bates-ancient-iron-works-braintree-1898.md
Test-Path sources\validations\accessgenealogy-lysander-franklin-gurney.md
Test-Path sources\validations\suffolk-probate-index-v2-1895.md
Test-Path sources\validations\mhs-winthrop-papers-newgate-deed-1639.md
Select-String -Path research\people\g13-john-gurney-fact-sheet.research.md -Pattern "Winthrop/Savage|John Newgate|MBCR|Bates|Suffolk probate index|Lysander Franklin Gurney"
Select-String -Path research\case-files\john-gurney-case-file-v4.md -Pattern "ref-72|ref-73|ref-74|ref-75|ref-76|two-Johns|composite-source"
git diff --check
```
