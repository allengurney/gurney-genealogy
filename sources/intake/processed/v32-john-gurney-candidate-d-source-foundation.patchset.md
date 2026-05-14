# Intake patchset v32 - Candidate D source foundation: Boyd cards, ROLLCO, Robert Gurney will, and context bundle

```yaml
patchset_id: v32
created: 2026-05-14
repo_scope: gurney-genealogy
phase: phase_1_patchset_only
input_packet: sources/intake/john-gurney-2026May/john-gurney-candidate-d-working-packet-audited-v13.md
companion_packet: sources/intake/john-gurney-2026May/john-gurney-candidate-d-working-packet-ai-ready-v14.md
phase_2_rule: Source-foundation apply only. Do not redo Candidate D analysis. Create source registry entries, thin validations, media folders, and corpus supplements so a later analysis pass can cite stable repo sources.
```

## 0. Scope

This patchset handles the mechanical and low-analytical source setup for packet sections 1-12:

- Sections 1-5: Boyd's Inhabitants of London selected Gurney/Garney/Gourney cards.
- Sections 6-7: ROLLCO Drapers' Company Robert/John Gurney cluster.
- Section 8: Robert Gurney will, Archdeaconry Court of London, proved 23 September 1625.
- Sections 9-10: religious-context and Old Change/parish-record-strategy public web sources as one bundled context source.
- Sections 11-12: no independent source record; these are analysis/audit sections that cite the source IDs created above.

This patchset intentionally does not update `research/case-files/john-gurney-case-file-v4.md`, `research/people/g13-john-gurney-fact-sheet.research.md`, or generated site files.

## 1. Source registry operation

Add the following records to `data/sources.json` under the top-level `sources` object. Preserve existing ordering style and do not reformat the full file.

### 1.1 `findmypast-boyds-inhabitants-london-candidate-d-gurney-cards`

```json
"findmypast-boyds-inhabitants-london-candidate-d-gurney-cards": {
  "shortTitle": "Findmypast Boyd's Inhabitants - Candidate D Gurney cards",
  "citation": "Boyd's Inhabitants of London & Family Units 1200-1946, selected Gurney/Garney/Gourney cards for John Gourney/Gurny, William Shipman with Mary Garney/Gurney, John Gurny/Gurney, and Robert Gurny/Gurney. Images GBOR/BIL/SOG25/0595, GBOR/BIL/SOG26/0392, GBOR/BIL/SOG36/0477, GBOR/BIL/SOG59/0240, and GBOR/BIL/SOG82/0603. Accessed via Findmypast from user-supplied image captures.",
  "archive": "Findmypast; Society of Genealogists Boyd's Inhabitants of London images supplied in intake packet",
  "url": "https://www.findmypast.com/",
  "corpusStatus": "partial",
  "corpusPath": "sources/corpus_supplement/boyds-inhabitants-london-candidate-d-gurney-cards.md",
  "mediaPath": "sources/media/findmypast-boyds-inhabitants-london-candidate-d-gurney-cards",
  "validationPath": "sources/validations/findmypast-boyds-inhabitants-london-candidate-d-gurney-cards.md",
  "notes": "Candidate D source foundation. Preserves five Boyd's card transcriptions from working packet sections 1-5, including the key Robert Gurny / John Gurny St Augustine / Anne Morris cross-reference and other London Gurney comparator cards. Use as card-transcription evidence; deeper identity analysis remains in the Candidate D working packet and later case-file updates."
}
```

### 1.2 `rollco-drapers-gurney-old-change-cluster`

```json
"rollco-drapers-gurney-old-change-cluster": {
  "shortTitle": "ROLLCO Drapers - Robert and John Gurney Old Change cluster",
  "citation": "Records of London's Livery Companies Online (ROLLCO), Drapers' Company records for the Robert and John Gurney Old Change cluster: Robert Gurney as apprenticeship master, 1617; John Gurney freedom by redemption, 11 February 1623/4, father Robert Gurney; Robert Gurney as freedom-event master, 1629; John Gurney as apprenticeship master, 1630. Search results and record details supplied in the Candidate D working packet.",
  "archive": "Records of London's Livery Companies Online (ROLLCO), public database at londonroll.org",
  "url": "https://www.londonroll.org/",
  "corpusStatus": "partial",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/rollco-drapers-gurney-old-change-cluster.md",
  "notes": "Drapers' Company source spine for Candidate D. The 1623/4 freedom entry identifies John Gurney as new freeman by redemption and names father Robert Gurney. The 1617 result places Robert Gurney, tailor, Old Change, as a Drapers' apprenticeship master. Full ROLLCO exports or underlying Drapers/Boyd's Roll entries remain high-value follow-up."
}
```

### 1.3 `acl-robert-gurney-will-1625`

```json
"acl-robert-gurney-will-1625": {
  "shortTitle": "Archdeaconry Court of London - Robert Gurney will (1625)",
  "citation": "Robert Gurney, citizen and draper of London, will written 18 January 1621/2 and proved 23 September 1625, Archdeaconry Court of London; parish indexed as London. User-supplied Ancestry metadata: Name: Robert Gurney; Probate Date: 23 Sep 1625; Parish: London. Working transcription from supplied image 31787_A002570-00422.jpg.",
  "archive": "Ancestry, London, England, Wills and Probate, 1507-1858; Archdeaconry Court of London probate image supplied in intake",
  "url": null,
  "corpusStatus": "partial",
  "corpusPath": "sources/corpus_supplement/robert-gurney-1625-will-full-working-transcription.md",
  "mediaPath": "sources/media/acl-robert-gurney-will-1625",
  "validationPath": "sources/validations/acl-robert-gurney-will-1625.md",
  "notes": "Key Candidate D primary source. Names Robert Gurney, citizen and draper of London; wife Anne; son John; Old Change dwelling/business premises; John as sole executor; and probate by John as son and executor. Working transcription is not a final diplomatic edition; shop/cellar/hall wording and some witness/probate formulae require high-resolution recheck."
}
```

### 1.4 `candidate-d-london-context-web-bundle`

```json
"candidate-d-london-context-web-bundle": {
  "shortTitle": "Candidate D London context web bundle",
  "citation": "Public web-source bundle used in Candidate D working packet sections 9-10: Massachusetts Secretary of the Commonwealth, 'The Great Migration'; Britannica, 'Massachusetts Bay Colony'; London Online, 'Old Change'; London Museum, 'St Augustine's church from Old Change, Cheapside'; City of London, 'St Augustine Watling Street'; AIM25/The National Archives catalogue entries for St Augustine Watling Street (P69/AUG) and St Magnus the Martyr (P69/MAG); FamilySearch catalog entries for St Vedast Foster Lane and St Michael le Querne; The London Archives parish-register and pre-1858 wills guides.",
  "archive": "Public web pages cited in the Candidate D working packet",
  "url": null,
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/candidate-d-london-context-web-bundle.md",
  "notes": "Bundled context source for religious-background and Old Change/parish-record strategy. Use for locator/context claims only. Do not treat this bundle as primary evidence for Robert or John Gurney events; cite the will, ROLLCO, Boyd's cards, and parish-register sources for person facts."
}
```

## 2. File operations

### 2.1 Boyd's card media

Create directory:

```text
sources/media/findmypast-boyds-inhabitants-london-candidate-d-gurney-cards/
```

Move these files from `sources/intake/john-gurney-2026May/` into that directory:

```text
gbor_bil_sog25_0595.jpg
gbor_bil_sog26_0392.jpg
gbor_bil_sog36_0477.jpg
gbor_bil_sog59_0240.jpg
gbor_bil_sog82_0603.jpg
```

### 2.2 Boyd's card corpus supplement

Create:

```text
sources/corpus_supplement/boyds-inhabitants-london-candidate-d-gurney-cards.md
```

Begin the file with:

```markdown
# Boyd's Inhabitants of London - Candidate D Gurney/Garney/Gourney card transcriptions

Citation: Boyd's Inhabitants of London & Family Units 1200-1946, selected Gurney/Garney/Gourney cards for John Gourney/Gurny, William Shipman with Mary Garney/Gurney, John Gurny/Gurney, and Robert Gurny/Gurney. Images GBOR/BIL/SOG25/0595, GBOR/BIL/SOG26/0392, GBOR/BIL/SOG36/0477, GBOR/BIL/SOG59/0240, and GBOR/BIL/SOG82/0603. Accessed via Findmypast from user-supplied image captures. Source ID: findmypast-boyds-inhabitants-london-candidate-d-gurney-cards.

Source packet: sources/intake/john-gurney-2026May/john-gurney-candidate-d-working-packet-audited-v13.md, sections 1-5.

---
```

Then copy the complete content of sections 1-5 from the input packet exactly as-is, beginning with:

```markdown
# 1. `gbor_bil_sog25_0595.jpg`
```

and ending immediately before:

```markdown
# 6. ROLLCO Drapers
```

Do not summarize, normalize, or shorten the copied section text.

### 2.3 Robert Gurney will corpus supplement

Move:

```text
sources/intake/john-gurney-2026May/robert-gurney-1625-will-full-working-transcription.md
```

to:

```text
sources/corpus_supplement/robert-gurney-1625-will-full-working-transcription.md
```

Do not rewrite the transcription in Phase 2 except for a minimal top citation block if needed. If adding a top citation block, use:

```markdown
Citation: Robert Gurney, citizen and draper of London, will written 18 January 1621/2 and proved 23 September 1625, Archdeaconry Court of London; working transcription from user-supplied image 31787_A002570-00422.jpg. Source ID: acl-robert-gurney-will-1625.
```

### 2.4 Robert Gurney will media

Create directory:

```text
sources/media/acl-robert-gurney-will-1625/
```

If the underlying will image `31787_A002570-00422.jpg` is present in the intake folder or supplied before Phase 2, move it into that directory. It is referenced by the packet but was not present in the repo checkout during Phase 1 authoring on 2026-05-14.

## 3. Validation notes

Create these thin validation files.

### 3.1 `sources/validations/findmypast-boyds-inhabitants-london-candidate-d-gurney-cards.md`

```markdown
# Findmypast Boyd's Inhabitants - Candidate D Gurney cards

Source ID: `findmypast-boyds-inhabitants-london-candidate-d-gurney-cards`

Examined material: five user-supplied Boyd's Inhabitants of London card images: `GBOR/BIL/SOG25/0595`, `GBOR/BIL/SOG26/0392`, `GBOR/BIL/SOG36/0477`, `GBOR/BIL/SOG59/0240`, and `GBOR/BIL/SOG82/0603`.

Examined portions: the visible card images and user-supplied Findmypast transcript/record URLs recorded in the Candidate D working packet.

Retained artifacts: media files in `sources/media/findmypast-boyds-inhabitants-london-candidate-d-gurney-cards/`; transcription corpus supplement at `sources/corpus_supplement/boyds-inhabitants-london-candidate-d-gurney-cards.md`.

Substantive findings: retained in the Candidate D working packet and intended for later case-file/research-companion analysis. This validation only records source handling.

Patchset: `sources/intake/processed/v32-john-gurney-candidate-d-source-foundation.patchset.md`.
```

### 3.2 `sources/validations/rollco-drapers-gurney-old-change-cluster.md`

```markdown
# ROLLCO Drapers - Robert and John Gurney Old Change cluster

Source ID: `rollco-drapers-gurney-old-change-cluster`

Examined material: ROLLCO search-result details recorded in the Candidate D working packet for Robert Gurney and John Gurney in Drapers' Company records.

Examined portions: Robert Gurney as apprenticeship master in 1617; John Gurney freedom by redemption on 11 February 1623/4 with father Robert Gurney; Robert Gurney in a 1629 freedom-event master role; John Gurney in a 1630 apprenticeship-master role.

Unexamined or uncertain: full event-detail exports, event IDs, and underlying Drapers' Company/Boyd's Roll entries have not yet been captured in the repo.

Substantive findings: retained in the Candidate D working packet and intended for later case-file/research-companion analysis.

Patchset: `sources/intake/processed/v32-john-gurney-candidate-d-source-foundation.patchset.md`.
```

### 3.3 `sources/validations/acl-robert-gurney-will-1625.md`

```markdown
# Archdeaconry Court of London - Robert Gurney will (1625)

Source ID: `acl-robert-gurney-will-1625`

Examined material: user-supplied probate image identified as `31787_A002570-00422.jpg` and Ancestry metadata for Robert Gurney, probate 23 September 1625, parish London.

Examined portions: full working transcription of the will and probate clause in the Candidate D working packet and corpus supplement.

Retained artifacts: `sources/corpus_supplement/robert-gurney-1625-will-full-working-transcription.md`; media directory reserved at `sources/media/acl-robert-gurney-will-1625/`.

Unexamined or uncertain: the image file was referenced in the packet but was not present in the repo checkout during Phase 1 authoring on 2026-05-14. A higher-resolution image should be retained when available; shop/cellar/hall wording and some witness/probate formulae need recheck before final diplomatic publication.

Substantive findings: retained in the Candidate D working packet and intended for later case-file/research-companion analysis.

Patchset: `sources/intake/processed/v32-john-gurney-candidate-d-source-foundation.patchset.md`.
```

### 3.4 `sources/validations/candidate-d-london-context-web-bundle.md`

```markdown
# Candidate D London context web bundle

Source ID: `candidate-d-london-context-web-bundle`

Examined material: public web pages cited in Candidate D working packet sections 9-10 for Great Migration context, Old Change location, St Augustine Watling Street, London parish-register access, and London probate access.

Examined portions: context and locator claims only.

Use limits: this bundled source should not be cited for person-event facts about Robert or John Gurney. Cite the will, ROLLCO, Boyd's cards, and parish-register records for those.

Substantive findings: retained in the Candidate D working packet and intended for later analysis.

Patchset: `sources/intake/processed/v32-john-gurney-candidate-d-source-foundation.patchset.md`.
```

## 4. Apply order

1. Add the four `data/sources.json` records.
2. Move the five Boyd's card images into the new media folder.
3. Create the Boyd's corpus supplement by copying packet sections 1-5 exactly as-is after the citation header.
4. Move the Robert Gurney will transcription into `sources/corpus_supplement/`.
5. Create the Robert Gurney will media directory; move the will image only if it is available in the repo/intake folder at Phase 2 time.
6. Create the four validation notes.
7. Parse `data/sources.json`.
8. Run `git diff --check`.

## 5. Phase 2 non-goals

- Do not update the John Gurney case file in this source-foundation pass.
- Do not decide Candidate D probability in this source-foundation pass.
- Do not treat the context bundle as evidence for person identity.
- Do not invent media files for packet-referenced images that are not present in the repo checkout.
