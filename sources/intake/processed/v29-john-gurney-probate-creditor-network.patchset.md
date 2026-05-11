# Phase 1 Patchset — John Gurney probate inventory and creditor-network analysis

**Patchset type:** Phase 1 intake preparation  
**Outcome:** promote  
**Primary subject:** John Gurney-1 of Braintree, Massachusetts  
**Primary destination:** `research/people/g13-john-gurney-fact-sheet.research.md`  
**Corpus supplement:** `sources/corpus_supplement/john-gurney-probate-inventory-spr-case-338.md`  
**Do not apply automatically:** This patchset is prepared for Phase 2 review and application.

---

## 1. Intake items retained

### Item A — SPR Case #338 manuscript image

**Outcome:** promote

**Description:** User-supplied full-page manuscript image of John Gurney Senr probate inventory, Braintree, 16 March 1663. The image preserves the detailed inventory, debt lines, appraiser signatures, land-interest line at Quinapaug, and bottom legal notation.

**Proposed sourceId:** `spr-case-338-john-gurney-probate-1663`

**Proposed media path:**

```text
sources/media/John Gurney Probate/102840311_00516.jpg
```

**Proposed corpus supplement path:**

```text
sources/corpus_supplement/john-gurney-probate-inventory-spr-case-338.md
```

### Item B — NEHGR vol. 12, p. 53, “Suffolk Wills”

**Outcome:** promote

**Description:** Printed NEHGR abstract of John Gurney’s probate inventory and related Widow Wilson entry that also names John Gurney. The page corrects several manuscript-only readings: Joseph Adams, John Dassit Senr, Smith/Collins at Boston, Sam Broadstreet and Richard Wharton as deponents, and inventory amount £55 14s 6d.

**Proposed sourceId:** `nehgr-12-suffolk-wills-1858`

**Online locator:**

```text
https://books.google.com/books/about/The_New_England_Historical_Genealogical.html?id=fMMMAAAAYAAJ
```

---

## 2. File operation

Create or replace:

```text
sources/corpus_supplement/john-gurney-probate-inventory-spr-case-338.md
```

with the prepared corpus-supplement file from this intake session.

---

## 3. Proposed `data/sources.json` additions

Add the following source entries under `sources`.

```json
"spr-case-338-john-gurney-probate-1663": {
  "shortTitle": "SPR Case #338 — John Gurney probate inventory",
  "citation": "Suffolk County, Massachusetts, Probate Records, Case #338, John Gurney Senr probate inventory, Braintree, 16 March 1663; manuscript image supplied by Allen Gurney, file 102840311_00516.jpg.",
  "archive": "Suffolk County probate records / user-supplied manuscript image",
  "url": null,
  "corpusStatus": "partial",
  "corpusPath": "sources/corpus_supplement/john-gurney-probate-inventory-spr-case-338.md",
  "mediaPath": "sources/media/John Gurney Probate/102840311_00516.jpg",
  "validationPath": null,
  "notes": "Primary probate image for John Gurney Senr of Braintree. Includes detailed inventory, debt list, appraisers Gregory Belcher, Edmund Quincy/Quinsey, and Thomas Faxon, a land-interest line at Quinapaug, and bottom legal notation. NEHGR vol. 12 p. 53 provides a supporting abstract but omits some inventory details."
},
"nehgr-12-suffolk-wills-1858": {
  "shortTitle": "NEHGR 12 — Suffolk Wills - John Gurney probate abstract",
  "citation": "New England Historic Genealogical Society. "Suffolk Wills." The New England Historical and Genealogical Register, vol. 12 (Boston: New England Historic Genealogical Society, 1858), p. 53.",
  "archive": "Google Books / public-domain volume",
  "url": "https://books.google.com/books/about/The_New_England_Historical_Genealogical.html?id=fMMMAAAAYAAJ",
  "corpusStatus": "partial",
  "corpusPath": "sources/corpus_supplement/john-gurney-probate-inventory-spr-case-338.md",
  "mediaPath": null,
  "validationPath": null,
  "notes": "Printed abstract of the Widow Wilson and John Gurney entries on p. 53 completed in 1858. Confirms John Gurney probate abstract: Braintree, 16 Mar. 1663; appraisers Gregory Belcher, Edmund Quincy, Thomas Faxon; inventory amount £55 14s 6d; debt names including Peter Brackett, Joseph Adams, Francis Nucomb, John Dassit Senr, Goodman King of Waymouth, Goodman Baly, John Mills, John Cleverly, Smith, Collins at Boston; bottom notation naming Mr Sam Broadstreet and Mr Richard Wharton as deponents. Also includes Widow Wilson entry reporting £4 in the hands of John Gurney."
}
```

---

## 4. Proposed update to `research/people/g13-john-gurney-fact-sheet.research.md`

### Placement

Add under:

```text
### Community and probate records in Braintree, Billerica, and Suffolk County
```

Recommended placement: after the existing paragraph beginning “The Suffolk probate index for vol. 2, G to O...” or replace that paragraph’s final sentence with the expanded block below.

### Proposed research block

```markdown
The underlying Suffolk probate material for John Gurney is no longer merely an index lead. A manuscript image of SPR Case #338 and the NEHGR vol. 12 “Suffolk Wills” abstract show a Braintree probate inventory dated 16 March 1663 for “John Gurney senr, deceased.” The inventory was taken by Gregory Belcher, Edmund Quincy, and Thomas Faxon, and NEHGR abstracts the amount as £55 14s 6d. The manuscript page includes clothing, bedding, household metalware, a musket, agricultural tools, grain, livestock, cart or wheel equipment, and a land-interest line reading approximately “An estate layd out in land at Quinapaug wch we know not.” That Quinapaug line is not visible in the brief NEHGR abstract, but it is a significant new land clue and should be correlated with the Mendon/Nipmug/Quinshipaug proprietary record stream in which John Gurny and Grisel Gurney later appear as twenty-acre lot holders.[^spr-case-338-john-gurney-probate][^nehgr-12-suffolk-wills][^mendon-proprietors-1899]

The debt section is genealogically useful because it maps John’s creditor and obligation network across Braintree, Weymouth, Boston, and the Mendon frontier land orbit. NEHGR names debts due from the estate to Peter Brackett, Joseph Adams, Francis Nucomb, John Dassit Senr, Goodman King of Waymouth, Goodman Baly, John Mills, John Cleverly, Smith, and Collins at Boston. The manuscript also appears to include a substantial allowance to the widow “for goods impaired out of her estate,” a debt to Francis Eliot, charges at Boston and funeral, Mr Alcocke and the Church of Braintree, and a later or separate Wharton-related notation. Peter Brackett is especially important because he was one of the Braintree men associated with the purchase of the Mendon/Nipmug tract; Goodman King of Weymouth is a useful bridge to the Weymouth land question; and the Boston names and “charges at Boston” show Boston-facing probate or commercial obligations without, by themselves, identifying John of Braintree with the 1636 John Newgate apprentice.[^spr-case-338-john-gurney-probate][^nehgr-12-suffolk-wills][^mendon-proprietors-1899]

The same NEHGR page contains a separate “Widow Wilson” entry stating that £4 was “in hands of John Gurney” and that the Wilson children were to receive a due proportion of that £4 “with other creditors to ye late John Gurney’s estate.” This creates another Braintree estate-accounting tie involving Francis Eliot and shows John’s estate as debtor or holder of funds for another local estate.[^nehgr-12-suffolk-wills]
```

### Proposed footnotes to add near the existing footnote block

```markdown
[^spr-case-338-john-gurney-probate]: Suffolk County, Massachusetts, Probate Records, Case #338, John Gurney Senr probate inventory, Braintree, 16 March 1663; manuscript image supplied by Allen Gurney, file `102840311_00516.jpg`; project extract and analysis at `sources/corpus_supplement/john-gurney-probate-inventory-spr-case-338.md`. Source ID: `spr-case-338-john-gurney-probate-1663`.

[^nehgr-12-suffolk-wills]: “Suffolk Wills,” *New England Historical and Genealogical Register*, vol. 12 (Boston: New England Historic Genealogical Society, 1858), p. 53, Widow Wilson and John Gurney entries; Google Books, https://books.google.com/books/about/The_New_England_Historical_Genealogical.html?id=fMMMAAAAYAAJ; project extract at `sources/corpus_supplement/john-gurney-probate-inventory-spr-case-338.md`. Source ID: `nehgr-12-suffolk-wills-1858`.
```

---

## 5. Optional case-file cleanup note

The current case file / research companion language says or implies that John died with no land in the surviving estate framing and gives the estate as £55.14.6. The new probate image requires a narrower statement.

Recommended future revision:

```markdown
John’s 1663 probate inventory did not appraise ordinary Braintree real estate as a stable landholding, but it did note a land interest “layd out in land at Quinapaug wch we know not.” Treat this as an unclarified or unvalued frontier proprietary interest rather than as ordinary appraised Braintree land. The NEHGR abstract gives the inventory amount as £55 14s 6d.
```

---

## 6. Follow-up research tasks

1. Recheck the manuscript line for **John Dassit Senr** against Braintree/Weymouth surnames; do not normalize to Bassett without evidence.
2. Recheck the **Smith / Collins at Boston** wording directly against the manuscript; withdraw the earlier Sweet/Swett reading unless the image proves it.
3. Identify **Mr Sam Broadstreet** in Suffolk probate/court context. Compare with Samuel Broadstreet, Simon Bradstreet, and manuscript abbreviation forms.
4. Identify the **Richard Wharton** role in the bottom legal notation. Treat him as a probate/court deponent unless evidence shows he was also a creditor.
5. Correlate **Quinapaug** with Mendon, Nipmug, Quinshepauge/Quinshipaug, and Quinebaug/Quinapaug land records.
6. Trace **Peter Brackett** in the Mendon purchase and proprietors’ records alongside John Gurny and Grisel Gurney.
7. Trace **Goodman King of Waymouth** in Weymouth and Mendon settler lists.
8. Correlate the **Widow Wilson** £4 in John Gurney’s hands with Suffolk court files or probate records, especially records involving Francis Eliot, William Alis/Ellise, and David Walsbe/Walsby.
