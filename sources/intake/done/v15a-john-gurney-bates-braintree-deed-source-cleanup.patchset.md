# Intake patchset v15A - John Gurney Bates/Braintree deed source cleanup

## Status

Review patchset only. Not applied.

Prepared 2026-05-09 from the John Gurney case-file source-completeness audit.

## Purpose

Register Samuel A. Bates, *The Ancient Iron Works at Braintree, Mass.* as its own source instead of leaving it embedded under `sprague-braintree` in the John Gurney case-file citation index.

This patchset is intentionally narrow. It extracts and updates the John Gurney/Bates portion of the existing ready patchset:

`sources/intake/processed/Ready/v02-1-new-intake-john-gurney-domesday-hardingham-expanded.patchset.md`

The inspected V4 case file already has endnotes through `n71`, so this patchset uses `n72` for the new Bates case-file note. Do not reuse the older v02 assumption that the next note is `n66`.

## Evidence value

Bates is not an English-origin source. Its value is to strengthen the colonial baseline:

- John Gurney is identified as a tailor in a Braintree land conveyance.
- The 12 February 1661 transaction gives richer property and neighbor context than the current case file preserves.
- The source independently supports John as a working tradesman with Braintree property dealings shortly before death.

## 1. `data/sources.json`

### 1.1 Add source entry

Add the following object in the `sources` object near other G13/New England sources:

```json
    "bates-ancient-iron-works-braintree-1898": {
      "shortTitle": "Bates, Ancient Iron Works at Braintree",
      "citation": "Bates, Samuel A. The Ancient Iron Works at Braintree, Mass.: The First in America. South Braintree, Mass.: Frank A. Bates, 1898.",
      "archive": "Internet Archive / local extracted source note",
      "url": null,
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/bates-ancient-iron-works-braintree-1898-john-gurney-extract.md",
      "mediaPath": null,
      "validationPath": "sources/validations/bates-ancient-iron-works-braintree-1898.md",
      "notes": "Source-control entry for the Bates page-10 John Gurney extract. Substantive treatment belongs in the G13 research companion and, where useful, the John Gurney case file. Not an English-origin source."
    },
```

### 1.2 Source-registry caution

Before applying, verify there is still no existing Samuel A. Bates source entry:

```powershell
Select-String -Path data\sources.json -Pattern "bates-ancient-iron-works-braintree-1898|Ancient Iron Works at Braintree|Samuel A. Bates"
```

Expected current result from audit: no matching Samuel A. Bates source entry.

## 2. New corpus and validation files

### 2.1 Create `sources/corpus_supplement/bates-ancient-iron-works-braintree-1898-john-gurney-extract.md`

```markdown
# Bates, Ancient Iron Works at Braintree (1898) - John Gurney extract

**Source ID:** `bates-ancient-iron-works-braintree-1898`

**Citation:** Samuel A. Bates, *The Ancient Iron Works at Braintree, Mass.: The First in America* (South Braintree, Mass.: Frank A. Bates, 1898), p. 10.

**Scope:** John Gurney material only.

## Extract

Bates preserves a 12 February 1661 Braintree conveyance in which "John Gurney, Taylor" conveyed property to Richard Thayer for fourteen pounds. The described property included one house and orchard on which the house stood, a five-acre parcel bounded south by the Monatiquot/Monoticot River, east by Richard Thayer, Nathaniel Mott, and a partly unclear John-name neighbor, north by Simon Crosby, and west by George Aldridge/Aldrich, plus an adjacent half-acre parcel west of the first lot.

Bates also supplies neighbor context, including references to Nathaniel Mott, George Aldrich/Aldridge, Richard Thayer, and Simon Crosby.
```

### 2.2 Create `sources/validations/bates-ancient-iron-works-braintree-1898.md`

```markdown
# Source validation: Bates, Ancient Iron Works at Braintree

**Source ID:** `bates-ancient-iron-works-braintree-1898`

## Examined

Samuel A. Bates, *The Ancient Iron Works at Braintree, Mass.: The First in America* (South Braintree, Mass.: Frank A. Bates, 1898), p. 10.

## Scope

- Page 10 John Gurney conveyance extract.
- Contextual neighbor names around the 12 February 1661 Braintree deed.

## Validation result

Usable as a secondary local-history extract. The underlying Braintree deed record was not checked in this source pass.

## Findings recorded in

- `research/people/g13-john-gurney-fact-sheet.research.md`
- `research/case-files/john-gurney-case-file-v4.md`
- Optional: `research/places/braintree-ma.md` if maintained

## Detailed execution trail

`sources/intake/processed/Ready/v15a-john-gurney-bates-braintree-deed-source-cleanup.patchset.md`
```

## 3. `research/case-files/john-gurney-case-file-v4.md`

### 3.1 Replace the current baseline occupation row

Current row:

```markdown
| **Occupation** | Tailor | Sprague, p. 695<sup class="fn"><a href="#n2" id="ref-2">2</a></sup> |
```

Replace with:

```markdown
| **Occupation** | Tailor | Sprague, p. 695<sup class="fn"><a href="#n2" id="ref-2">2</a></sup>; Bates, p. 10<sup class="fn"><a href="#n72" id="ref-72">72</a></sup> |
```

### 3.2 Replace current endnote `n2`

Current `n2` incorrectly includes Bates while assigning only `sprague-braintree` as the Source ID.

Replace:

```html
  <li id="n2" value="2">Waldo Chamberlain Sprague, <em>Genealogies of the Families of Braintree, Mass., 1640-1850</em> (Boston: New England Historic Genealogical Society, 2001), p. 695, John Gurney entry; see also Samuel A. Bates, <em>The Ancient Iron Works at Braintree, Mass.: The First in America</em> (South Braintree, Mass.: Frank A. Bates, 1898), p. 10, 12 Feb. 1661 conveyance identifying "John Gurney, Taylor." Source ID: <code>sprague-braintree</code>. <a class="backref" href="#ref-2">Back</a></li>
```

With:

```html
  <li id="n2" value="2">Waldo Chamberlain Sprague, <em>Genealogies of the Families of Braintree, Mass., 1640-1850</em> (Boston: New England Historic Genealogical Society, 2001), p. 695, John Gurney entry. Source ID: <code>sprague-braintree</code>. <a class="backref" href="#ref-2">Back</a></li>
```

Use the file's current character/encoding conventions when applying; the inspected file has mojibake in some punctuation, so prefer a targeted edit that preserves the surrounding file.

### 3.3 Add new endnote `n72`

Add before `</ol>`:

```html
  <li id="n72" value="72">Samuel A. Bates, <em>The Ancient Iron Works at Braintree, Mass.: The First in America</em> (South Braintree, Mass.: Frank A. Bates, 1898), p. 10, 12 Feb. 1661 conveyance in which "John Gurney, Taylor" conveyed property to Richard Thayer. Source ID: <code>bates-ancient-iron-works-braintree-1898</code>. <a class="backref" href="#ref-72">Back</a></li>
```

### 3.4 Add Bates to section 13.3 secondary sources

Current section 13.3 is a single-line list. Add:

```markdown
Bates, *The Ancient Iron Works at Braintree* (1898), p. 10, for the 12 Feb. 1661 Braintree conveyance identifying John Gurney as tailor and describing the property conveyed to Richard Thayer.
```

Keep it brief; the case-file narrative should not over-weight this as origin evidence.

## 4. `research/people/g13-john-gurney-fact-sheet.research.md`

### 4.1 Revise land/property table row

Replace:

```markdown
| 12 Feb 1661 | Braintree land sale | Sold land in Braintree. Deed witnessed by son John Jr. | Braintree deed records |
```

With:

```markdown
| 12 Feb 1661 | Braintree land sale | John Gurney, identified as tailor, conveyed to Richard Thayer for 14 pounds a house and orchard, a five-acre parcel on the Monatiquot/Monoticot River, and an additional half-acre parcel west of the first lot. | Bates, *Ancient Iron Works at Braintree*, p. 10; underlying Braintree deed record still to pull |
```

### 4.2 Add subsection under `### Land and property records`

Add after the paragraph beginning `John appears to have died with no land`:

```markdown
#### 1661 Braintree conveyance to Richard Thayer

The 12 February 1661 Braintree deed is another direct occupation witness: Bates prints the grantor as "John Gurney, Taylor." It also gives a fuller property description than the current summary preserves. Gurney conveyed to Richard Thayer, for fourteen pounds, one house and orchard, a five-acre parcel bounded south by the Monatiquot/Monoticot River, east by Richard Thayer, Nathaniel Mott, and another partly unclear John-name neighbor, north by Simon Crosby, and west by George Aldridge/Aldrich. He also conveyed an adjacent half-acre parcel west of the first lot. The record is useful for occupation and Braintree neighborhood reconstruction, not for English origin proof.[^bates-ironworks-gurney]

[^bates-ironworks-gurney]: Samuel A. Bates, *The Ancient Iron Works at Braintree, Mass.: The First in America* (South Braintree, Mass.: Frank A. Bates, 1898), p. 10, quoting the 12 Feb. 1661 conveyance from John Gurney to Richard Thayer. Source ID: `bates-ancient-iron-works-braintree-1898`.
```

## 5. Optional `research/places/braintree-ma.md` update

If `research/places/braintree-ma.md` is still maintained as a place page, add a short John Gurney Braintree-property note there. Keep it local/contextual and cite `bates-ancient-iron-works-braintree-1898`.

Suggested text:

```markdown
## John Gurney-1 at Braintree

John Gurney-1 appears in Braintree as a working tradesman and local property actor rather than as a large proprietor. The 12 February 1661 conveyance printed by Samuel A. Bates identifies him as "John Gurney, Taylor" and describes his sale to Richard Thayer of a house and orchard, a five-acre parcel on the Monatiquot/Monoticot River, and an adjacent half-acre parcel. Use the record for Braintree neighborhood and occupation context, not as English-origin evidence.[^bates-braintree]

[^bates-braintree]: Samuel A. Bates, *The Ancient Iron Works at Braintree, Mass.: The First in America* (South Braintree, Mass.: Frank A. Bates, 1898), p. 10. Source ID: `bates-ancient-iron-works-braintree-1898`.
```

## 6. Validation checklist

Run after application:

```powershell
Select-String -Path data\sources.json -Pattern "bates-ancient-iron-works-braintree-1898"
Test-Path sources\corpus_supplement\bates-ancient-iron-works-braintree-1898-john-gurney-extract.md
Test-Path sources\validations\bates-ancient-iron-works-braintree-1898.md
Select-String -Path research\case-files\john-gurney-case-file-v4.md -Pattern "bates-ancient-iron-works-braintree-1898|#n72|ref-72|John Gurney, Taylor"
Select-String -Path research\people\g13-john-gurney-fact-sheet.research.md -Pattern "bates-ironworks-gurney|Monatiquot|Monoticot"
```

Then run the usual site validation/package commands if this is applied to publishable content.

## 7. Do not do in this patchset

- Do not apply the Open Domesday or Hardingham material from v02.
- Do not renumber existing case-file endnotes unless a later applied patch has changed the numbering.
- Do not treat Bates as proof of English origin, parentage, or John's first wife's maiden name.
