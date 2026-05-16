# Intake patchset v04 — Great Ellingham current-site status / Historic England 1077566; G37 label cleanup

**Prepared:** 2026-04-27  
**Repo:** `allengurney/gurney-genealogy`  
**Repo ref inspected:** `main` @ `109ad8aa2151c7a1e58c14a36f4a9144eea7066e`  
**Patchset destination when applied:** `sources/intake/processed/v04.patchset.md`

## Scope

1. **Great Ellingham, Norfolk, England**
   - Update current site / extant status from `unknown` to **house and two barns exist plus medieval-era moat and ponds**.
   - Update place coordinate to **52.528994, 0.970243** with **high** accuracy.
   - Add Historic England list entry **1077566 — Old Hall Farmhouse** to `data/sources.json`.
   - Add Historic England 1077566 to `research/places/great-ellingham.md` sources section and current-site narrative.
   - Keep prior NHER / Old Hall content from v03.

2. **G37 ancestor label cleanup**
   - Remove all visible `G~37` generation labels and normalize to `G37`.
   - Cross-reference impact: canonical filenames, slugs, and permalinks already use `g37`; this is a display-label and JSON-generation cleanup, not a filename migration.
   - Update canonical files plus site/generated mirrors if they are still committed.

## Source verification

Historic England’s National Heritage List entry **1077566** identifies **Old Hall Farmhouse** as a Grade II listed building in Great Ellingham, Norfolk. It was first listed 21 July 1951 and most recently amended 16 November 1983. The official entry gives National Grid Reference **TM 01591 96491** and describes the house as **c.1570**, timber framed with wattle and daub and some clay lump infill on a brick plinth, black glazed pantiled roof, red to rear, cross-wing plan, two storeys, central range flanked by gabled cross wings, and with an original staircase surviving to the attic. It also notes that it was formerly listed as “Old Hall — and Barns.”

This confirms the house component of the requested current-site statement. The two-barn and moat/fishpond components are supported by the prior v03 NHER material and Historic England entries 1342457 / 1077567.

Repository text search found `G~37` occurrences in these relevant areas:

- Canonical fact sheet: `fact-sheets/g37-eudes-de-gournay-fact-sheet.md`
- Canonical research companion: `research/people/g37-eudes-de-gournay-fact-sheet.research.md`
- Site mirror fact sheet: `site/website/fact-sheets/g37-eudes-de-gournay-fact-sheet.md`
- Site research companion mirror: `site/website/research/companions/g37-eudes-de-gournay-fact-sheet.md`
- Generated data / mirrors: `data/ancestors v26.json`, `site/website/_data/ancestors.json`
- Older/generated/supporting references: `data/ancestors v25.json`, `site/website/llms.txt`, `site/website/_data/placesCatalog.json`, `site/website/_data/placePages.json`, logs/audit/tool docs such as `research/topics/ancestors-json-audit.md`, `research/log/2026-04-16.md`, `research/log/2026-04-17--place-normalization-pass2.md`, `AI-Rules.md`, and `tools/normalize_places_v1.py`.

---

## 1. `data/sources.json`

### 1.1 Update metadata date

Change the current prior value to:

```json
"lastUpdated": "2026-04-27"
```

### 1.2 Add source entry: Historic England 1077566 — Old Hall Farmhouse

Insert near the NHER Great Ellingham / Historic England / Norfolk place sources:

```json
    "historic-england-old-hall-farmhouse-1077566": {
      "shortTitle": "Historic England — Old Hall Farmhouse (1077566)",
      "citation": "Historic England. \"Old Hall Farmhouse.\" National Heritage List for England, List Entry Number 1077566.",
      "archive": "Historic England, National Heritage List for England",
      "url": "https://historicengland.org.uk/listing/the-list/list-entry/1077566",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/historic-england-old-hall-farmhouse-1077566.md",
      "mediaPath": null,
      "validationPath": "sources/validations/historic-england-old-hall-farmhouse-1077566.md",
      "notes": "Grade II listing for Old Hall Farmhouse, Great Ellingham. Historic England describes the house as c.1570, timber framed with wattle and daub and some clay lump infill on a brick plinth, cross-wing plan, two storeys, central range flanked by gabled cross wings, and with original staircase surviving to attic. First listed 21 July 1951; most recent amendment 16 November 1983; NGR TM 01591 96491. Supports the extant-house component of the Great Ellingham current-site status."
    },
```

---

## 2. New source supplement and validation files

### 2.1 Create `sources/corpus_supplement/historic-england-old-hall-farmhouse-1077566.md`

```markdown
# Historic England — Old Hall Farmhouse, Great Ellingham

**Source ID:** `historic-england-old-hall-farmhouse-1077566`

**Citation:** Historic England, "Old Hall Farmhouse," *National Heritage List for England*, List Entry Number 1077566.

**URL:** https://historicengland.org.uk/listing/the-list/list-entry/1077566

## Record summary

- List Entry Name: Old Hall Farmhouse
- List Entry Number: 1077566
- Heritage Category: Listed Building
- Grade: II
- Date first listed: 21 July 1951
- Date of most recent amendment: 16 November 1983
- County: Norfolk
- District: Breckland
- Parish: Great Ellingham
- National Grid Reference: TM 01591 96491
- Listing NGR: TM0166996604
- Legacy System number: 220193

## Description extract / paraphrase

Historic England describes Old Hall Farmhouse as a house, now farmhouse, dating to about 1570. It is timber framed with wattle and daub and some clay lump infill on a brick plinth, with black glazed pantiled roof, red to rear. It has a cross-wing plan, two storeys, and a central range flanked by gabled cross wings.

The entry notes asymmetrical doors, renewed lower casements, three three-light timber mullioned casements above of seventeenth- or eighteenth-century date, exposed timber studding on the north wall, brick encasing to part of the ground floor, an eighteenth-century catslide rear extension, nineteenth- and twentieth-century fenestration, two twentieth-century flat dormers, and two large external stacks.

The original staircase survives to the attic, with heavy turned balusters on square bases, newel posts with incised rectangular fields and top ball finials, and moulded handrails.

## Research value

This listing confirms the house component of the Great Ellingham current-site note: Old Hall Farmhouse is an extant Grade II listed building. Together with NHER MNF9108 and the barn listings, it supports the updated site status: house and two barns exist plus medieval-era moat and ponds.
```

### 2.2 Create `sources/validations/historic-england-old-hall-farmhouse-1077566.md`

```markdown
# Source validation: Historic England — Old Hall Farmhouse (1077566)

**Source ID:** `historic-england-old-hall-farmhouse-1077566`

**Source examined:** Historic England, National Heritage List for England, List Entry Number 1077566.

**Finding destination:** `research/places/great-ellingham.md`; `data/places.json`; possible generated site mirrors.

## Validation result

Strong source. Historic England is the official National Heritage List source for the listed-building designation.

## Supports

- Old Hall Farmhouse is extant as a Grade II listed building.
- First listed 21 July 1951; most recent amendment 16 November 1983.
- Great Ellingham, Breckland, Norfolk.
- NGR TM 01591 96491 / listing NGR TM0166996604.
- c.1570 timber-framed house / farmhouse, cross-wing plan, surviving original stair.

## Limits

This source supports the listed farmhouse and its architectural description. Use NHER MNF9108 for the wider medieval moated manorial complex, fishponds, cropmarks, and two-barn site context.
```

---

## 3. `research/places/great-ellingham.md`

### 3.1 Update coordinate line

Replace:

```markdown
Village in south-central Norfolk. Coordinates: **52.5453, 1.0091774978679044**.
```

with:

```markdown
Village in south-central Norfolk. Current site coordinate: **52.528994, 0.970243** (high accuracy). Broader village coordinate formerly used: **52.5453, 1.0091774978679044**.
```

### 3.2 Tighten the current-site introduction

Replace the existing paragraph beginning:

```markdown
Great Ellingham (also known as "Old Hall") is a medieval moated manorial site...
```

with:

```markdown
Great Ellingham’s Gurney current site is best represented by **Old Hall / Old Hall Farmhouse**: a medieval moated manorial site with a mid-sixteenth-century great house within the main moat, additional moated enclosures and fishponds, two listed barns, and Grade II listed Old Hall Farmhouse. The current-site / extant-status summary should be: **house and two barns exist plus medieval-era moat and ponds**.[^nher-mnf9108-old-hall][^historic-england-old-hall-1077566]
```

If `[^nher-mnf9108-old-hall]` is not yet defined in the file, define it using the existing v03 source footnote. Add the Historic England footnote below.

### 3.3 Revise `## The Manor (current site)`

Replace the section with:

```markdown
## The Manor (current site)

Current site / extant status: **house and two barns exist plus medieval-era moat and ponds**.

The site is a mostly well-preserved medieval moated manorial complex. NHER MNF9108 records the main component as surviving moats and fishponds, with additional moated enclosures and fishponds visible as either extant earthworks or partially levelled cropmarks. The house within the main moat is a mid-sixteenth-century great house, now a farmhouse.[^nher-mnf9108-old-hall]

Historic England list entry 1077566 confirms the extant house component: **Old Hall Farmhouse** is Grade II listed, first listed 21 July 1951 and amended 16 November 1983. Historic England describes it as a c.1570 timber-framed house, now farmhouse, with wattle and daub and some clay lump infill on a brick plinth, a cross-wing plan, two storeys, a central range flanked by gabled cross wings, and an original stair surviving to the attic.[^historic-england-old-hall-1077566]

NHER also records a sixteenth-century barn to the southeast and a seventeenth/eighteenth-century barn to the northwest. Together, NHER and Historic England support the site-status statement: the house and two barns exist, and the medieval-era moat and ponds survive or remain visible as earthworks/cropmarks.[^nher-mnf9108-old-hall]
```

### 3.4 Add Historic England source footnote

Add near the existing NHER footnotes:

```markdown
[^historic-england-old-hall-1077566]: Historic England, "Old Hall Farmhouse," *National Heritage List for England*, List Entry Number 1077566, https://historicengland.org.uk/listing/the-list/list-entry/1077566. Source ID: `historic-england-old-hall-farmhouse-1077566`.
```

### 3.5 Update `## Sources`

Add:

```markdown
- Historic England, "Old Hall Farmhouse," *National Heritage List for England*, List Entry Number 1077566. [Historic England 1077566]
```

### 3.6 Update generated place-registry block

Replace:

```markdown
- Coordinate: 52.5453, 1.0091774978679044 (medium)
```

with:

```markdown
- Coordinate: 52.528994, 0.970243 (high)
```

Replace:

```markdown
- Current-site status: unknown
```

with:

```markdown
- Current-site status: house and two barns exist plus medieval-era moat and ponds
```

If the generated block is not hand-edited, make the same values in `data/places.json` and regenerate the block.

---

## 4. `data/places.json`

Locate `place-great-ellingham-norfolk-england`.

Update coordinate and precision:

```json
"coordinate": {
  "lat": 52.528994,
  "lng": 0.970243
},
"coordinatePrecision": "high",
```

Update current-site status / detail fields per schema. If the record has `currentSiteStatus`, use:

```json
"currentSiteStatus": "house and two barns exist plus medieval-era moat and ponds"
```

If current site is stored in `detail`, append:

```text
Current site / extant status: house and two barns exist plus medieval-era moat and ponds. Historic England 1077566 confirms Old Hall Farmhouse as Grade II and c.1570; NHER MNF9108 records the medieval moated manorial site, fishponds, and two barns.
```

Ensure `sourceIds`, if present, include:

```json
"historic-england-old-hall-farmhouse-1077566",
"nher-mnf9108-old-hall-great-ellingham"
```

Do not create a second coordinate for Great Ellingham unless the data model supports sub-place coordinates. If the repo distinguishes broader locality from current site, create `place-old-hall-great-ellingham-norfolk-england` as described in v03.1 and link it to Great Ellingham.

---

## 5. `data/places_detail.json`

Locate `place-great-ellingham-norfolk-england`.

Add or revise a current-site / extant-status note:

```json
"currentSiteStatus": "house and two barns exist plus medieval-era moat and ponds",
"siteNotes": "Old Hall / Old Hall Farmhouse is the Gurney current-site anchor. Historic England 1077566 confirms Old Hall Farmhouse as a Grade II c.1570 timber-framed house / farmhouse. NHER MNF9108 records the wider medieval moated manorial site, surviving moats and fishponds, additional moated enclosures, and two barns."
```

If this file uses markdown text rather than JSON fields, add equivalent prose under the Great Ellingham detail record.

---

## 6. G37 label cleanup

### 6.1 Canonical fact sheet: `fact-sheets/g37-eudes-de-gournay-fact-sheet.md`

Make the following replacements:

```diff
-subtitle: "Ancestor fact sheet for G~37 in the direct Gurney line. Viking warrior and traditional first lord of Gournay-en-Bray. Updated April 2026."
+subtitle: "Ancestor fact sheet for G37 in the direct Gurney line. Viking warrior and traditional first lord of Gournay-en-Bray. Updated April 2026."

 factsheet:
-  gen: G~37
+  gen: G37
```

Search the rest of the file for `G~37` and replace with `G37`.

### 6.2 Canonical research companion: `research/people/g37-eudes-de-gournay-fact-sheet.research.md`

Make the following replacements:

```diff
-# Eudes (Odon) de Gournay (G~37) — Research Companion
+# Eudes (Odon) de Gournay (G37) — Research Companion
```

Replace:

```markdown
**Note on JSON data pollution:** the `data/ancestors v23.json` G~37 entry also lists West Barsham, Norfolk, as a landholding.
```

with:

```markdown
**Note on JSON data pollution:** the `data/ancestors v23.json` G37 entry also lists West Barsham, Norfolk, as a landholding.
```

Search the rest of the file for `G~37` and replace with `G37`.

### 6.3 `data/ancestors v26.json`

Locate the Eudes record. Search for either:

```json
"name": "Eudes (Odon) de Gournay"
```

or:

```json
"recordId": "ancestor-g37-eudes-odon-de-gournay"
```

Within that object, replace any generation label:

```diff
-"gen": "G~37"
+"gen": "G37"
```

Also replace any `G~37` within `summary`, `notables`, `landHoldings`, `buttons`, or display strings.

Do not change `recordId`, filename, slug, or URL values if they already use `g37`.

### 6.4 Site mirrors / generated files

If the site still commits mirrors, apply the same replacements in:

```text
site/website/fact-sheets/g37-eudes-de-gournay-fact-sheet.md
site/website/research/companions/g37-eudes-de-gournay-fact-sheet.md
site/website/_data/ancestors.json
```

### 6.5 Older data and noncanonical docs

Search found `G~37` in older/generated/supporting files. Apply replacement where these files are meant to remain current:

```text
data/ancestors v25.json
site/website/llms.txt
site/website/_data/placesCatalog.json
site/website/_data/placePages.json
research/places/scandinavia.md
research/topics/ancestors-json-audit.md
research/log/2026-04-16.md
research/log/2026-04-17--place-normalization-pass2.md
AI-Rules.md
tools/normalize_places_v1.py
tools/pedigree_explorer.html
```

Do **not** alter historical logs if the repo policy treats log files as immutable. If logs are left unchanged, add a note to the patch application summary:

```text
Historical logs still contain G~37 as a historical artifact; active display files and generated data now use G37.
```

### 6.6 Cross-reference impact summary

- **No permalink change:** `g37-eudes-de-gournay-fact-sheet.html` already uses `g37`.
- **No filename change:** canonical filenames already use `g37`.
- **No slug change:** fact sheet slug already uses `g37-eudes-de-gournay-fact-sheet`.
- **No recordId change expected:** generated record IDs found in search already appear to use `ancestor-g37-...`.
- **Impacted user-visible values:** subtitle, front matter `factsheet.gen`, research title, ancestor data display `gen`, site mirrors, generated JSON used by the website.

---

## 7. Validation checklist

Run:

```bash
python -m json.tool data/sources.json >/tmp/sources-json-check.json
python -m json.tool data/places.json >/tmp/places-json-check.json
python -m json.tool data/places_detail.json >/tmp/places-detail-json-check.json

grep -R "historic-england-old-hall-farmhouse-1077566\|1077566\|52.528994\|0.970243\|house and two barns exist plus medieval-era moat and ponds" -n \
  data research sources site | head -100

grep -R "G~37" -n \
  fact-sheets research data site tools AI-Rules.md | head -100
```

Manual checks:

- `research/places/great-ellingham.md` no longer shows current-site status as `unknown`.
- Great Ellingham coordinate in the generated block is `52.528994, 0.970243 (high)`.
- `data/places.json` uses `"lat": 52.528994`, `"lng": 0.970243`, and `"coordinatePrecision": "high"` for Great Ellingham or for the dedicated Old Hall site record if the model is split.
- Historic England 1077566 appears in `data/sources.json`, the Great Ellingham place file sources, and the source supplement/validation files.
- No active display file still uses `G~37`.
- No cross-reference or permalink has been renamed from `g37`.
