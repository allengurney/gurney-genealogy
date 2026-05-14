# Intake patchset v33 - Candidate D register-image and comparator-source setup

```yaml
patchset_id: v33
created: 2026-05-14
repo_scope: gurney-genealogy
phase: phase_1_patchset_only
input_packet: sources/intake/john-gurney-2026May/john-gurney-candidate-d-working-packet-audited-v13.md
companion_packet: sources/intake/john-gurney-2026May/john-gurney-candidate-d-working-packet-ai-ready-v14.md
depends_on: v32-john-gurney-candidate-d-source-foundation.patchset.md
phase_2_rule: Create source records and thin validations for packet sections 13-23. Do not do the deeper Candidate D reasoning or case-file rewrite in this pass.
```

## 0. Scope

This patchset handles mechanical source setup for packet sections 13-23:

- Section 13: Harleian Society St Vedast / St Michael le Quern printed registers.
- Sections 14-17: St Augustine Watling Street original-register image reviews.
- Section 18 and section 19.2: St Magnus the Martyr register images.
- Section 20: St Swithin, London Stone marriage image.
- Section 21: St Giles Cripplegate baptism-image lead.
- Section 22.1: St Mary Magdalen Old Fish Street image.
- Sections 19.1, 22.2, and 23: index-only comparator leads bundled together.

The image/PDF filenames referenced in sections 13-23 were not present anywhere under the repo checkout during Phase 1 authoring on 2026-05-14. This patchset therefore creates stable source records and validation notes now, and reserves media folders for later image/PDF placement if the files are supplied before Phase 2 application.

## 1. Source registry operation

Add the following records to `data/sources.json` under the top-level `sources` object. Preserve existing ordering style and do not reformat the full file.

### 1.1 `harleian-st-vedast-st-michael-le-quern-registers`

```json
"harleian-st-vedast-st-michael-le-quern-registers": {
  "shortTitle": "Harleian Society - St Vedast and St Michael le Quern registers",
  "citation": "Littledale, Willoughby A., ed. The Registers of St. Vedast, Foster Lane, and of St. Michael le Quern, London. Harleian Society Registers, vols. 29-30. London: Harleian Society, 1902-1903. User-supplied PDFs FL3830041_284895_29.pdf and FL3830150_284895_30.pdf searched in Candidate D packet.",
  "archive": "FamilySearch catalog 284895 / user-supplied PDF copies",
  "url": "https://www.familysearch.org/search/catalog/284895",
  "corpusStatus": "partial",
  "corpusPath": null,
  "mediaPath": "sources/media/harleian-st-vedast-st-michael-le-quern-registers",
  "validationPath": "sources/validations/harleian-st-vedast-st-michael-le-quern-registers.md",
  "notes": "Candidate D collateral source. Packet search found no direct Robert/John Gurney, Anne Morris, Dunnell, or Henscott bridge, but it clarified poor pre-1666 St Michael le Quern register survival and preserved St Vedast same-neighborhood Gurney/Gourney comparator entries."
}
```

### 1.2 `lma-st-augustine-watling-register-candidate-d-images`

```json
"lma-st-augustine-watling-register-candidate-d-images": {
  "shortTitle": "LMA St Augustine Watling Street register - Candidate D images",
  "citation": "Parish register, St Augustine Watling Street, City of London. London Metropolitan Archives, parish collection P69/AUG; selected user-supplied Ancestry images reviewed in the Candidate D packet, including 31281_a101009-00022.jpg through 31281_a101009-00030.jpg and burial images 31281_a101009-00121.jpg through 31281_a101009-00130.jpg.",
  "archive": "London Metropolitan Archives parish registers via Ancestry, London, England, Church of England Baptisms, Marriages and Burials, 1538-1812; user-supplied images",
  "url": null,
  "corpusStatus": "partial",
  "corpusPath": null,
  "mediaPath": "sources/media/lma-st-augustine-watling-register-candidate-d-images",
  "validationPath": "sources/validations/lma-st-augustine-watling-register-candidate-d-images.md",
  "notes": "Core Candidate D parish-register source. Packet sections 14-17 confirm early Robert Gurny/Gorney child events at St Augustine, record a negative post-1601 replacement-John christening search through 1610, and record a negative 1601-1612 first-wife burial search in supplied images."
}
```

### 1.3 `lma-st-magnus-martyr-register-candidate-d-images`

```json
"lma-st-magnus-martyr-register-candidate-d-images": {
  "shortTitle": "LMA St Magnus the Martyr register - Candidate D images",
  "citation": "Parish register, St Magnus the Martyr, City of London. London Metropolitan Archives, parish collection P69/MAG; user-supplied Ancestry images reviewed in the Candidate D packet, including 31281_a101911-00014.jpg and 31281_a101911-00131.jpg.",
  "archive": "London Metropolitan Archives parish registers via Ancestry, London, England, Church of England Baptisms, Marriages and Burials, 1538-1812; user-supplied images",
  "url": null,
  "corpusStatus": "partial",
  "corpusPath": null,
  "mediaPath": "sources/media/lma-st-magnus-martyr-register-candidate-d-images",
  "validationPath": "sources/validations/lma-st-magnus-martyr-register-candidate-d-images.md",
  "notes": "Candidate D source for the image-confirmed 4 April 1611 marriage of Robert Gourney of St Augustine in Watling Street and Anne Morris of St Michael in the Querne, by licence. Also preserves the likely false-positive/exclusionary John Grone burial at St Magnus, 5 July 1625."
}
```

### 1.4 `lma-st-swithin-london-stone-register-john-grine-1640`

```json
"lma-st-swithin-london-stone-register-john-grine-1640": {
  "shortTitle": "LMA St Swithin London Stone - John Grine marriage (1640/1)",
  "citation": "Parish register, St Swithin, London Stone, City of London. London Metropolitan Archives, P69/SWI/A/001/MS04311. Ancestry.com, London, England, Church of England Baptisms, Marriages and Burials, 1538-1812, index reference 24930171 / additional reference 1888376; user-supplied image 31281_a102288-00110.jpg reviewed in the Candidate D packet.",
  "archive": "London Metropolitan Archives parish registers via Ancestry; user-supplied image",
  "url": null,
  "corpusStatus": "partial",
  "corpusPath": null,
  "mediaPath": "sources/media/lma-st-swithin-london-stone-register-john-grine-1640",
  "validationPath": "sources/validations/lma-st-swithin-london-stone-register-john-grine-1640.md",
  "notes": "Broad-area comparator and possible false-positive source. Packet image review reads John Grine and Mary of the same parish, married 24 January 1640/1. Wife Mary and City geography are interesting, but the image does not strongly support Gurney and no Robert/Drapers/Old Change bridge is present."
}
```

### 1.5 `lma-st-giles-cripplegate-register-john-grone-1630`

```json
"lma-st-giles-cripplegate-register-john-grone-1630": {
  "shortTitle": "LMA St Giles Cripplegate - John Grone baptism (1630)",
  "citation": "Parish register, St Giles Cripplegate, City of London. London Metropolitan Archives parish registers via Ancestry.com, London, England, Church of England Baptisms, Marriages and Burials, 1538-1812; user-supplied index reference 23300657 / additional reference 1813505 and image 31281_a101526-00185.jpg reviewed in the Candidate D packet.",
  "archive": "London Metropolitan Archives parish registers via Ancestry; user-supplied image",
  "url": null,
  "corpusStatus": "partial",
  "corpusPath": null,
  "mediaPath": "sources/media/lma-st-giles-cripplegate-register-john-grone-1630",
  "validationPath": "sources/validations/lma-st-giles-cripplegate-register-john-grone-1630.md",
  "notes": "Broad-area comparator source. Indexed as John Grone, son of John Grone, baptized 4 August 1630 at St Giles Cripplegate. Packet notes the supplied image is not clear enough for confident surname correction and should not be treated as Candidate D without better image review."
}
```

### 1.6 `lma-st-mary-magdalen-old-fish-street-john-grene-1634`

```json
"lma-st-mary-magdalen-old-fish-street-john-grene-1634": {
  "shortTitle": "LMA St Mary Magdalen Old Fish Street - John Grene baptism (1634)",
  "citation": "Parish register, St Mary Magdalen, Old Fish Street, City of London. London Metropolitan Archives parish registers via Ancestry.com, London, England, Church of England Baptisms, Marriages and Burials, 1538-1812; user-supplied index reference 24296258 / additional reference 1860129 and image 31281_a101952-00044.jpg reviewed in the Candidate D packet.",
  "archive": "London Metropolitan Archives parish registers via Ancestry; user-supplied image",
  "url": null,
  "corpusStatus": "partial",
  "corpusPath": null,
  "mediaPath": "sources/media/lma-st-mary-magdalen-old-fish-street-john-grene-1634",
  "validationPath": "sources/validations/lma-st-mary-magdalen-old-fish-street-john-grene-1634.md",
  "notes": "Same-neighborhood comparator source. Image supports John Grene, son of Jeames/James Grene, baptized 16 November 1634. The parish is highly relevant to Old Change geography, but this record is not Candidate D without further evidence."
}
```

### 1.7 `candidate-d-london-grine-grene-index-leads-bundle`

```json
"candidate-d-london-grine-grene-index-leads-bundle": {
  "shortTitle": "Candidate D London Grine/Grene index-lead bundle",
  "citation": "Index-only comparator leads recorded in Candidate D packet sections 19.1, 22.2, and 23: Jhon Grine baptized 6 March 1603/4 at St Mary-at-Hill, FHL film 374485; John Grene, son of Robart Grene, baptized 31 August 1600 at All Hallows Bread Street, FHL film 94511; John Grene, son of Rich Grene, baptized 1 January 1610/11 at St Mary Whitechapel / Stepney, FHL film 94691. Index records supplied by user; original images not available in this pass.",
  "archive": "User-supplied index records from Ancestry/FamilySearch-derived collections",
  "url": null,
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/candidate-d-london-grine-grene-index-leads-bundle.md",
  "notes": "Bundled index-only false-positive/comparator leads. Use only as leads until original images are retrieved. The All Hallows Bread Street 1600 Robart Grene item is geographically and chronologically the most interesting of the three; the Whitechapel item is low value for Candidate D."
}
```

## 2. Media directories

Create these directories. Move/copy only files that are actually present at Phase 2 time; do not invent absent media.

```text
sources/media/harleian-st-vedast-st-michael-le-quern-registers/
sources/media/lma-st-augustine-watling-register-candidate-d-images/
sources/media/lma-st-magnus-martyr-register-candidate-d-images/
sources/media/lma-st-swithin-london-stone-register-john-grine-1640/
sources/media/lma-st-giles-cripplegate-register-john-grone-1630/
sources/media/lma-st-mary-magdalen-old-fish-street-john-grene-1634/
```

Expected files if supplied:

```text
FL3830041_284895_29.pdf
FL3830150_284895_30.pdf
31281_a101009-00022.jpg
31281_a101009-00023.jpg
31281_a101009-00024.jpg
31281_a101009-00025.jpg
31281_a101009-00026.jpg
31281_a101009-00027.jpg
31281_a101009-00028.jpg
31281_a101009-00029.jpg
31281_a101009-00030.jpg
31281_a101009-00121.jpg
31281_a101009-00121(1).jpg
31281_a101009-00122.jpg
31281_a101009-00123.jpg
31281_a101009-00124.jpg
31281_a101009-00125.jpg
31281_a101009-00126.jpg
31281_a101009-00127.jpg
31281_a101009-00128.jpg
31281_a101009-00129.jpg
31281_a101009-00130.jpg
31281_a101911-00014.jpg
31281_a101911-00131.jpg
31281_a102288-00110.jpg
31281_a101526-00185.jpg
31281_a101952-00044.jpg
```

## 3. Validation notes

Create thin validation files matching the seven new source IDs. Each should state:

- Source ID.
- Packet section(s) examined.
- Whether media was present in the repo at Phase 2 time.
- The exact record or search scope.
- That substantive findings remain in the working packet pending later case-file/research updates.
- This patchset path.

Use these bodies.

### 3.1 `sources/validations/harleian-st-vedast-st-michael-le-quern-registers.md`

```markdown
# Harleian Society - St Vedast and St Michael le Quern registers

Source ID: `harleian-st-vedast-st-michael-le-quern-registers`

Examined material: user-supplied PDFs `FL3830041_284895_29.pdf` and `FL3830150_284895_30.pdf`, as summarized in Candidate D packet section 13.

Examined scope: Gurney/Gurny/Gurnie/Gourney/Gournay/Garney, Morris, Dunnell/Dunell/Dunnett, Henscott/Hencott/Henscot, Romney/Romeny, Symons/Simmons, Lloyd/Loyd, and Old Change variants.

Result summary: no direct Candidate D family event found; St Michael le Quern early-register loss clarified; several St Vedast Gurney/Gourney comparator entries retained in the packet.

Media status: PDFs were referenced in the packet but were not present in the repo checkout during Phase 1 authoring on 2026-05-14. Place them under `sources/media/harleian-st-vedast-st-michael-le-quern-registers/` if supplied.

Patchset: `sources/intake/processed/v33-john-gurney-candidate-d-register-and-comparator-sources.patchset.md`.
```

### 3.2 `sources/validations/lma-st-augustine-watling-register-candidate-d-images.md`

```markdown
# LMA St Augustine Watling Street register - Candidate D images

Source ID: `lma-st-augustine-watling-register-candidate-d-images`

Examined material: St Augustine Watling Street register images named in Candidate D packet sections 14-17.

Examined scope: Robert Gurny/Gorney child baptisms and burials; post-1601 search for a replacement John baptism through 1610; 1601-1612 burial search for Robert's first wife and Gurney variants.

Result summary: packet records image-confirmed John and Mary child events for Robert, an unnamed stillborn son of Robert, negative replacement-John christening search in supplied pages through 1610, and negative adult female Gurney first-wife burial search in supplied pages 1601-1612.

Media status: named images were referenced in the packet but were not present in the repo checkout during Phase 1 authoring on 2026-05-14. Place them under `sources/media/lma-st-augustine-watling-register-candidate-d-images/` if supplied.

Patchset: `sources/intake/processed/v33-john-gurney-candidate-d-register-and-comparator-sources.patchset.md`.
```

### 3.3 `sources/validations/lma-st-magnus-martyr-register-candidate-d-images.md`

```markdown
# LMA St Magnus the Martyr register - Candidate D images

Source ID: `lma-st-magnus-martyr-register-candidate-d-images`

Examined material: St Magnus the Martyr images named in Candidate D packet sections 18 and 19.2.

Examined scope: Robert Gourney and Anne Morris marriage, 4 April 1611; John Grone burial, 5 July 1625.

Result summary: packet confirms the Robert Gourney / Anne Morris marriage as 4 April 1611 by licence, with Robert of St Augustine in Watling Street and Anne of St Michael in the Querne. Packet treats the 5 July 1625 John Grone burial as a nearby false-positive/exclusionary note because Candidate D John proved Robert's will on 23 September 1625.

Media status: named images were referenced in the packet but were not present in the repo checkout during Phase 1 authoring on 2026-05-14. Place them under `sources/media/lma-st-magnus-martyr-register-candidate-d-images/` if supplied.

Patchset: `sources/intake/processed/v33-john-gurney-candidate-d-register-and-comparator-sources.patchset.md`.
```

### 3.4 `sources/validations/lma-st-swithin-london-stone-register-john-grine-1640.md`

```markdown
# LMA St Swithin London Stone - John Grine marriage (1640/1)

Source ID: `lma-st-swithin-london-stone-register-john-grine-1640`

Examined material: St Swithin, London Stone marriage index record and image named in Candidate D packet section 20.

Examined scope: John Grine and Mary / Mary Jones marriage, 24 January 1640/1.

Result summary: packet treats this as a possible false-positive or broad-area lead. Bride Mary and City geography are interesting, but the image does not strongly support Gurney and no Robert/Drapers/Old Change bridge is present.

Media status: named image was referenced in the packet but was not present in the repo checkout during Phase 1 authoring on 2026-05-14. Place it under `sources/media/lma-st-swithin-london-stone-register-john-grine-1640/` if supplied.

Patchset: `sources/intake/processed/v33-john-gurney-candidate-d-register-and-comparator-sources.patchset.md`.
```

### 3.5 `sources/validations/lma-st-giles-cripplegate-register-john-grone-1630.md`

```markdown
# LMA St Giles Cripplegate - John Grone baptism (1630)

Source ID: `lma-st-giles-cripplegate-register-john-grone-1630`

Examined material: St Giles Cripplegate baptism index record and image named in Candidate D packet section 21.

Examined scope: John Grone, son of John Grone, baptized 4 August 1630.

Result summary: packet treats this as a broad-area comparator lead. The supplied image was too difficult for a confident surname correction; do not treat as Gurney or Candidate D without a tighter crop or higher-resolution image.

Media status: named image was referenced in the packet but was not present in the repo checkout during Phase 1 authoring on 2026-05-14. Place it under `sources/media/lma-st-giles-cripplegate-register-john-grone-1630/` if supplied.

Patchset: `sources/intake/processed/v33-john-gurney-candidate-d-register-and-comparator-sources.patchset.md`.
```

### 3.6 `sources/validations/lma-st-mary-magdalen-old-fish-street-john-grene-1634.md`

```markdown
# LMA St Mary Magdalen Old Fish Street - John Grene baptism (1634)

Source ID: `lma-st-mary-magdalen-old-fish-street-john-grene-1634`

Examined material: St Mary Magdalen Old Fish Street baptism index record and image named in Candidate D packet section 22.1.

Examined scope: John Grene, son of Jeames/James Grene, baptized 16 November 1634.

Result summary: packet treats this as a same-neighborhood comparator only. The parish is highly relevant to Old Change geography, but the image supports Grene and father Jeames/James, not Candidate D.

Media status: named image was referenced in the packet but was not present in the repo checkout during Phase 1 authoring on 2026-05-14. Place it under `sources/media/lma-st-mary-magdalen-old-fish-street-john-grene-1634/` if supplied.

Patchset: `sources/intake/processed/v33-john-gurney-candidate-d-register-and-comparator-sources.patchset.md`.
```

### 3.7 `sources/validations/candidate-d-london-grine-grene-index-leads-bundle.md`

```markdown
# Candidate D London Grine/Grene index-lead bundle

Source ID: `candidate-d-london-grine-grene-index-leads-bundle`

Examined material: index-only leads recorded in Candidate D packet sections 19.1, 22.2, and 23.

Examined scope: Jhon Grine baptized 6 March 1603/4 at St Mary-at-Hill; John Grene son of Robart Grene baptized 31 August 1600 at All Hallows Bread Street; John Grene son of Rich Grene baptized 1 January 1610/11 at St Mary Whitechapel / Stepney.

Result summary: packet treats these as comparator leads only. The All Hallows Bread Street item is the highest-value image-check lead because of father Robart, date, and geography. The Whitechapel item is low value for Candidate D.

Media status: no images were available in the packet/repo for these index-only leads during Phase 1 authoring on 2026-05-14.

Patchset: `sources/intake/processed/v33-john-gurney-candidate-d-register-and-comparator-sources.patchset.md`.
```

## 4. Apply order

1. Add the seven `data/sources.json` records.
2. Create the six media directories.
3. Move/copy only packet-referenced PDFs/images that are actually available at Phase 2 time.
4. Create the seven validation notes.
5. Parse `data/sources.json`.
6. Run `git diff --check`.

## 5. Phase 2 non-goals

- Do not update the John Gurney case file in this register-source setup pass.
- Do not decide Candidate D probability in this register-source setup pass.
- Do not turn index-only Grine/Grene leads into Gurney facts.
- Do not mark missing media as present.
