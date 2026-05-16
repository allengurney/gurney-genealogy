# v18 John Gurney colonial baseline source/research patchset

Status: Phase 1 proposal only. Do not apply without review.

Scope: This patchset starts anew from the corrected v17 approach and focuses on repo-held colonial land/property notes under `research/case-files/John-gurney-research-to-be-assessed/deeds and misc/`. It does not modify live `data/`, `research/`, or `sources/validations/` files.

Guiding decision: no corpus supplements are proposed here. These are short, targeted extracts and research findings. The findings belong in `research/`; the validation files stay thin.

## 1. Lead triage outcome

| Lead | Status | Decision |
|---|---|---|
| `deeds318904_04_john_gurney_extracts.md` / *Suffolk Deeds. Liber IV* | Repo-held extraction usable; stable online scan not confirmed in this pass | Add source record + thin validation; use in G13 and case file for Braintree Ting/Tyng lease context |
| `proprietors_gurney_extracts.md` / *The Proprietors' Records of Mendon* | Online-accessible at Internet Archive/OpenLibrary and repo-held extraction is substantive | Add source record + thin validation; use in G13 and case file for John/Grisel Mendon proprietary trail |
| `milford_john_gurney_extract_pp27_33.md` / Ballou, *History of Milford* | Online-accessible at Internet Archive; repo-held extraction covers pp. 27-35 | Add source record + thin validation; use in G13 and case file for 1662 accepted allotments and 1667/pre-war land references |
| `john_gurney_extracts_historicalsketch00nash_0.md` / Nash, *Historical Sketch of Weymouth* | Online-accessible at Internet Archive; repo-held extraction covers John/Gurny/Gurnie references | Add source record + thin validation; use in G13 and case file for Weymouth land-grant baseline and spelling variants |
| `porter_gurney_p238_extract.md` / Porter genealogy | Online-accessible at Internet Archive, but derivative of stronger MBCR/court material | Park; no source record in v18 unless later research needs the Weymouth gloss |
| `john_gurney_bartlett_note.md` / Bartlett genealogy | Late derivative settlement summary; stronger Ballou/Proprietors sources cover the same Mendon point | Park; no source record in v18 |

Online leads checked:

- Mendon Proprietors: `https://archive.org/details/proprietorsrecor00mend`
- Ballou, *History of the Town of Milford*, vol. 1: `https://archive.org/details/historyoftownofm01ball`
- Nash, *Historical Sketch of the Town of Weymouth*: `https://archive.org/details/historicalsketch00nash_0`
- Porter genealogy: `https://archive.org/details/genealogyofdesce00port`

## 2. Data source records to add

File: `data/sources.json`

Add these records near the existing colonial Massachusetts John Gurney sources. Keep JSON key order alphabetical only if the file's surrounding section is already alphabetic; otherwise place them near `history-of-weymouth`.

```json
"suffolk-deeds-liber-iv-1888": {
  "shortTitle": "Suffolk Deeds, Liber IV (1888)",
  "citation": "Temple, Thomas F., Register of Deeds. Suffolk Deeds. Liber IV. Boston: Rockwell and Churchill, City Printers, 1888.",
  "archive": "Suffolk County deed-record printed volume; project extraction note at research/case-files/John-gurney-research-to-be-assessed/deeds and misc/deeds318904_04_john_gurney_extracts.md from source filename deeds318904_04.pdf",
  "url": null,
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/suffolk-deeds-liber-iv-1888.md",
  "notes": "Printed Suffolk County deed-record volume. John Gurney appears in the William Ting estate-division material on printed pp. 6 and 89a-90, with the printed index at p. 150 pointing to those references. The material identifies one of two Braintree messuages or tenements allotted to Bethia and Mercy Ting as being occupied by lease by John Gurney. Useful for Braintree tenancy and Ting/Tyng estate context; not a family-relationship record."
},
"mendon-proprietors-records-1899": {
  "shortTitle": "Mendon Proprietors' Records (1899)",
  "citation": "The Proprietors' Records of the Town of Mendon, Massachusetts: Incorporated May 15, 1667. Boston: Rockwell and Churchill Press, 1899.",
  "archive": "Internet Archive; OpenLibrary; project extraction note at research/case-files/John-gurney-research-to-be-assessed/deeds and misc/proprietors_gurney_extracts.md",
  "url": "https://archive.org/details/proprietorsrecor00mend",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/mendon-proprietors-records-1899.md",
  "notes": "Published transcript/abstract of Mendon proprietary records. John Gurny and Grisel Gurney appear as separate twenty-acre lot holders; Grisel's will material links her Mendon accommodation to Joseph Juell and the Juell/Kibbee/Burge family network; later entries preserve John Gurny's house lot, meadow, and swamp-lot references. Useful for the John/Grisel Mendon property trail and for distinguishing proprietary/title survival from proof of John's later residence."
},
"ballou-history-of-milford-1882": {
  "shortTitle": "Ballou, History of Milford (1882)",
  "citation": "Ballou, Adin. History of the Town of Milford, Worcester County, Massachusetts, from Its First Settlement to 1881. In Two Parts. Part I. Strictly Historical; Part II. Biographico-Genealogical Register. Boston: Franklin Press, Rand, Avery, & Co., 1882.",
  "archive": "Internet Archive; project extraction note at research/case-files/John-gurney-research-to-be-assessed/deeds and misc/milford_john_gurney_extract_pp27_33.md",
  "url": "https://archive.org/details/historyoftownofm01ball",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/ballou-history-of-milford-1882.md",
  "notes": "Milford/Mendon town history preserving the institutional context of the Netmooke/Mendham/Mendon plantation. The project extraction covers pp. 27-35, including the 1662 list of persons accepted to allotments, where John Gurney appears in the Braintree contingent, and nearby references to 1667 meadow division and pre-King Philip's War grants. Useful for Mendon proprietary context; later references require caution because John Gurney-1 died in 1662/3."
},
"nash-historical-sketch-weymouth-1885": {
  "shortTitle": "Nash, Historical Sketch of Weymouth (1885)",
  "citation": "Nash, Gilbert. Historical Sketch of the Town of Weymouth, Massachusetts, from 1622 to 1884. Weymouth, Massachusetts: Town of Weymouth, under the auspices of the Weymouth Historical Society, 1885. Printed by Alfred Mudge & Son, Boston.",
  "archive": "Internet Archive; project extraction note at research/case-files/John-gurney-research-to-be-assessed/deeds and misc/john_gurney_extracts_historicalsketch00nash_0.md",
  "url": "https://archive.org/details/historicalsketch00nash_0",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/nash-historical-sketch-weymouth-1885.md",
  "notes": "Weymouth local history preserving early land-list material. John appears under variants Gurny/Gurnie/Gurney on pp. 258, 270, 278, and 282; the strongest entry is the 1651/2 lot-list entry on p. 282, with the index grouping Gurny/Gurnie/Gurney variants. Useful for Weymouth land-grant baseline and spelling-variant search terms."
}
```

Do not add source records for Porter or Bartlett in this patchset.

## 3. Thin validation files to add

### `sources/validations/suffolk-deeds-liber-iv-1888.md`

```markdown
# Suffolk Deeds, Liber IV (1888)

Source ID: `suffolk-deeds-liber-iv-1888`

## Scope Examined

Examined the project extraction note at `research/case-files/John-gurney-research-to-be-assessed/deeds and misc/deeds318904_04_john_gurney_extracts.md`, drawn from source filename `deeds318904_04.pdf`.

The relevant portions are printed pp. 6 and 89a-90, plus printed index p. 150.

## Limits

A stable online scan URL was not confirmed in this pass. The extracted source association is retained, but page-image verification is recommended before using long quotations.

## Findings Location

Substantive findings belong in `research/people/g13-john-gurney-fact-sheet.research.md` and `research/case-files/john-gurney-case-file-v4.md`. No corpus supplement is required for this patchset.

Patchset: `sources/intake/processed/v18-john-gurney-colonial-baseline-source-research.patchset.md`.
```

### `sources/validations/mendon-proprietors-records-1899.md`

```markdown
# Mendon Proprietors' Records (1899)

Source ID: `mendon-proprietors-records-1899`

## Scope Examined

Examined the project extraction note at `research/case-files/John-gurney-research-to-be-assessed/deeds and misc/proprietors_gurney_extracts.md`, with online availability checked at Internet Archive: `https://archive.org/details/proprietorsrecor00mend`.

The relevant portions include pp. 13, 43, 46, 152-153, and later abutter/title-chain references to John Gurny's house lot, meadow, and swamp lot.

## Limits

This is a published transcript/abstract of proprietary records, not the original manuscript volume. Page-image review should precede any long quotation.

## Findings Location

Substantive findings belong in `research/people/g13-john-gurney-fact-sheet.research.md` and `research/case-files/john-gurney-case-file-v4.md`. No corpus supplement is required for this patchset.

Patchset: `sources/intake/processed/v18-john-gurney-colonial-baseline-source-research.patchset.md`.
```

### `sources/validations/ballou-history-of-milford-1882.md`

```markdown
# Ballou, History of Milford (1882)

Source ID: `ballou-history-of-milford-1882`

## Scope Examined

Examined the project extraction note at `research/case-files/John-gurney-research-to-be-assessed/deeds and misc/milford_john_gurney_extract_pp27_33.md`, with online availability checked at Internet Archive: `https://archive.org/details/historyoftownofm01ball`.

The relevant portions are pp. 27-35, especially the 1662 accepted-allotments list and nearby 1667/pre-war land references.

## Limits

Ballou is a nineteenth-century town history using earlier town/proprietary material. Later references to John Gurney in the Mendon record stream should be read as proprietary/title references unless an underlying record proves personal residence after 1662/3.

## Findings Location

Substantive findings belong in `research/people/g13-john-gurney-fact-sheet.research.md` and `research/case-files/john-gurney-case-file-v4.md`. No corpus supplement is required for this patchset.

Patchset: `sources/intake/processed/v18-john-gurney-colonial-baseline-source-research.patchset.md`.
```

### `sources/validations/nash-historical-sketch-weymouth-1885.md`

```markdown
# Nash, Historical Sketch of Weymouth (1885)

Source ID: `nash-historical-sketch-weymouth-1885`

## Scope Examined

Examined the project extraction note at `research/case-files/John-gurney-research-to-be-assessed/deeds and misc/john_gurney_extracts_historicalsketch00nash_0.md`, with online availability checked at Internet Archive: `https://archive.org/details/historicalsketch00nash_0`.

The relevant portions are printed pp. 258, 270, 278, 281-282, and index p. 306.

## Limits

This is a local-history presentation of early Weymouth land-list material. It is useful for John Gurney's Weymouth land baseline and spelling variants, but the original Weymouth town-record images remain the better long-term target.

## Findings Location

Substantive findings belong in `research/people/g13-john-gurney-fact-sheet.research.md` and `research/case-files/john-gurney-case-file-v4.md`. No corpus supplement is required for this patchset.

Patchset: `sources/intake/processed/v18-john-gurney-colonial-baseline-source-research.patchset.md`.
```

## 4. G13 research companion edits

File: `research/people/g13-john-gurney-fact-sheet.research.md`

Replace the current `### Land and property records` table and the short paragraph immediately after it with:

```markdown
### Land and property records

| Date | Record | Detail | Source |
|---|---|---|---|
| c. 1651/52 | Weymouth land grants and lot list | Nash preserves John under Gurny/Gurnie/Gurney variants in early Weymouth land descriptions: two East Field references, one Mill Field reference, and a direct 1651/2 lot-list entry naming John Gurney as no. 16. These entries show early Weymouth land rights later attached to other holders. | Nash, *Historical Sketch of Weymouth*; *History of Weymouth* |
| 25 May 1653 | Tyng/Ting Braintree tenancy | The Tyng inventory places 48 Braintree acres "in the possession of John Gurney." Suffolk Deeds, Liber IV, supplies the deed-record context: one of two Braintree messuages or tenements allotted to Bethia and Mercy Ting was occupied "by lease" by John Gurney, and a later agreement repeats the leasehold description. | NEHGR 30:432; *Suffolk Deeds. Liber IV* |
| 12 Feb 1661 | Braintree land sale | Sold land in Braintree. Deed witnessed by son John Jr. | Bates; Braintree deed records |
| 1662 and later title trail | Mendon proprietary rights | Ballou names John Gurney among the Braintree men accepted to allotments in the Netmooke/Mendon plantation. The Mendon proprietors' records preserve John Gurny and Grisel Gurney as separate twenty-acre lot holders and later preserve John Gurny's house lot, meadow, and swamp-lot references in title and boundary descriptions. | Ballou; Mendon Proprietors' Records |

John's colonial land trail is strongest when read as a sequence across Weymouth, Braintree, and Mendon rather than as a single residence claim. Nash gives the Weymouth baseline: John appears in the 1651/2 lot list and in earlier-grant references under Gurny/Gurnie spelling variants.[^nash-weymouth-1885]

The Braintree evidence is leasehold and community-context evidence, not ownership proof. *Suffolk Deeds. Liber IV* records one Ting/Tyng estate property at Braintree as occupied "by lease" by John Gurney, matching the existing Tyng-property context while identifying the legal setting more precisely.[^suffolk-deeds-liber-iv]

The Mendon material shows recognized proprietary standing and later title survival. Ballou places John among the Braintree men accepted to allotments in 1662, while the Mendon proprietors' records list John Gurny and Grisel Gurney as separate twenty-acre lot holders. Grisel's copied will material ties her Mendon accommodation to Joseph Juell and the Juell/Kibbee/Burge network. Later references to John Gurny's house lot, meadow, and swamp lot preserve the land trail after title had passed to others; because John died in 1662/3, those later references should not be read as proof that he personally resided in Mendon after death.[^ballou-milford-1882][^mendon-proprietors-1899]

John appears to have died with no land. His estate was valued at **GBP55.14.6**, a modest sum consistent with a working tradesman.
```

Add these footnotes near the existing G13 footnotes:

```markdown
[^nash-weymouth-1885]: Gilbert Nash, *Historical Sketch of the Town of Weymouth, Massachusetts, from 1622 to 1884* (Weymouth, Mass.: Town of Weymouth, 1885), pp. 258, 270, 278, 281-282, 306, https://archive.org/details/historicalsketch00nash_0. Source ID: `nash-historical-sketch-weymouth-1885`.
[^suffolk-deeds-liber-iv]: Thomas F. Temple, Register of Deeds, *Suffolk Deeds. Liber IV* (Boston: Rockwell and Churchill, City Printers, 1888), pp. 6, 89a-90, index p. 150; project extraction note at `research/case-files/John-gurney-research-to-be-assessed/deeds and misc/deeds318904_04_john_gurney_extracts.md`. Source ID: `suffolk-deeds-liber-iv-1888`.
[^ballou-milford-1882]: Adin Ballou, *History of the Town of Milford, Worcester County, Massachusetts, from Its First Settlement to 1881. In Two Parts* (Boston: Franklin Press, Rand, Avery, & Co., 1882), pp. 27-35, https://archive.org/details/historyoftownofm01ball. Source ID: `ballou-history-of-milford-1882`.
[^mendon-proprietors-1899]: *The Proprietors' Records of the Town of Mendon, Massachusetts: Incorporated May 15, 1667* (Boston: Rockwell and Churchill Press, 1899), pp. 13, 43, 46, 152-153 and related title/boundary entries, https://archive.org/details/proprietorsrecor00mend. Source ID: `mendon-proprietors-records-1899`.
```

## 5. Case-file edits

File: `research/case-files/john-gurney-case-file-v4.md`

Note numbering: if v17 is applied first, use `n77`-`n80` below. If v17 is not applied first, renumber these to the next available endnotes after the current final note.

### 5.1 Strengthen section 10.3

After the existing paragraph under `### 10.3 The Essex Social Network`, insert:

```html
<p>The property evidence sharpens the colonial side of that network without proving English origin by itself. <em>Suffolk Deeds. Liber IV</em> identifies one of the Braintree Ting/Tyng estate tenements as occupied "by lease" by John Gurney, and a later agreement repeats the same leased-possession description for the Gregory Belcher and John Gurney tenements. That turns the older Tyng-property reference from a general association into a specific leasehold context inside the estate of William Ting/Tyng's heirs.<sup class="fn"><a href="#n77" id="ref-77">77</a></sup></p>
```

### 5.2 Update the evidence summary row

In the `For Candidate B` evidence table, replace row 9's explanation with:

```markdown
| 9 | Essex social network | Strong (cumulative) | John-1's colonial world (son-in-law Shed from Essex, landlord Ting/Tyng of Essex-connected property, Braintree MA named for Braintree Essex) maps to Francis's second wife's family connections. Suffolk Deeds adds a specific Braintree leasehold context for John in the Ting/Tyng estate. |
```

### 5.3 Add a colonial baseline paragraph near the supplemental New England source discussion

After the existing `<h4>Torrey and History of Weymouth: cross-checks on the John1 family group</h4>` paragraph, insert:

```html
<h4>Colonial land baseline: Weymouth, Braintree, and Mendon</h4>
<p>Four local-record sources tighten John-1's American baseline. Nash's Weymouth sketch preserves John under Gurny/Gurnie/Gurney variants in early land descriptions and names him directly in a 1651/2 lot list. <em>Suffolk Deeds. Liber IV</em> identifies his Braintree Ting/Tyng estate occupancy as a leasehold. Ballou places him among the Braintree men accepted to allotments in the Netmooke/Mendon plantation in 1662. The Mendon proprietors' records then preserve John Gurny and Grisel Gurney as separate twenty-acre lot holders, Grisel's will-chain through Joseph Juell, and later title/boundary references to John's house lot, meadow, and swamp lot. This strengthens the colonial chronology and property trail, but it does not identify John's English parentage and should not be read as proof that he personally lived in Mendon after his 1662/3 death.<sup class="fn"><a href="#n78" id="ref-78">78</a></sup><sup class="fn"><a href="#n79" id="ref-79">79</a></sup><sup class="fn"><a href="#n80" id="ref-80">80</a></sup></p>
```

### 5.4 Add endnotes

Append these before `</ol>` in the case-file citation index, renumbering if needed:

```html
  <li id="n77" value="77">Thomas F. Temple, Register of Deeds, <em>Suffolk Deeds. Liber IV</em> (Boston: Rockwell and Churchill, City Printers, 1888), pp. 6, 89a-90, index p. 150; project extraction note at <code>research/case-files/John-gurney-research-to-be-assessed/deeds and misc/deeds318904_04_john_gurney_extracts.md</code>. Source ID: <code>suffolk-deeds-liber-iv-1888</code>. <a class="backref" href="#ref-77">↩</a></li>
  <li id="n78" value="78">Gilbert Nash, <em>Historical Sketch of the Town of Weymouth, Massachusetts, from 1622 to 1884</em> (Weymouth, Mass.: Town of Weymouth, under the auspices of the Weymouth Historical Society, 1885), pp. 258, 270, 278, 281-282, 306, <a href="https://archive.org/details/historicalsketch00nash_0">https://archive.org/details/historicalsketch00nash_0</a>. Source ID: <code>nash-historical-sketch-weymouth-1885</code>. <a class="backref" href="#ref-78">↩</a></li>
  <li id="n79" value="79">Adin Ballou, <em>History of the Town of Milford, Worcester County, Massachusetts, from Its First Settlement to 1881. In Two Parts</em> (Boston: Franklin Press, Rand, Avery, &amp; Co., 1882), pp. 27-35, <a href="https://archive.org/details/historyoftownofm01ball">https://archive.org/details/historyoftownofm01ball</a>. Source ID: <code>ballou-history-of-milford-1882</code>. <a class="backref" href="#ref-79">↩</a></li>
  <li id="n80" value="80"><em>The Proprietors' Records of the Town of Mendon, Massachusetts: Incorporated May 15, 1667</em> (Boston: Rockwell and Churchill Press, 1899), pp. 13, 43, 46, 152-153 and related title/boundary entries, <a href="https://archive.org/details/proprietorsrecor00mend">https://archive.org/details/proprietorsrecor00mend</a>. Source ID: <code>mendon-proprietors-records-1899</code>. <a class="backref" href="#ref-80">↩</a></li>
```

## 6. Candidate implications

This patchset strengthens the colonial baseline more than the English-origin proof. The main effect is pressure against sloppy composite narratives:

- Weymouth: John has a direct 1651/2 lot-list entry plus earlier-grant references under variants.
- Braintree: John has a leasehold context in the Ting/Tyng estate, tying the existing Tyng note to a deed-record setting.
- Mendon: John and Grisel each have proprietary traces; later references preserve title/boundary memory and must be separated from proof of John's post-1662/3 residence.
- Candidate B: modestly strengthened through the Braintree/Tyng social-network context, but not materially changed in probability.
- Candidate A: not directly weakened by these records, except that a better colonial baseline reduces room for late derivative birth/origin traditions to control the narrative.

## 7. Phase 2 checks

After applying:

1. Validate JSON syntax for `data/sources.json`.
2. Confirm case-file endnote numbering and backrefs are continuous.
3. Search for forbidden research prose phrases: `rg -n "obtained source|is now pulled|promoted by audit|intake|processing|OCR mechanics" research/people/g13-john-gurney-fact-sheet.research.md research/case-files/john-gurney-case-file-v4.md sources/validations`.
4. Confirm no new files are added under `sources/corpus_supplement/` by this patchset.
5. Run `git diff --check`.
