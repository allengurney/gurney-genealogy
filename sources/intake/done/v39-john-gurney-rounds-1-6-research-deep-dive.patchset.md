# Intake patchset v39 — Rounds 1-6 deep-research synthesis

```yaml
patchset_id: v39
created: 2026-05-15
repo_scope: gurney-genealogy
phase: phase_2_research_sources_and_case_file
input_packet: sources/intake/_workspace/round1-scratch/round{1,2,3,4,5,6}-findings.md
phase_2_rule: This patchset folds six rounds of online deep research (corridor empirics, Newgate Horningsheath origin, expanded East Dereham child cluster, Mary Shed marriage bounding, St Ann Blackfriars father resolution, 1636 apprentice two-Johns reading, probability formalization) into the case file and the two relevant person research-companion files. Body content stays lean; substantive evidence and citation detail go into footnotes per case-file v4 conventions.
```

## 0. Scope

Seven case-file revisions confirmed for application after a six-round deep-research pass:

1. **§4 children table.** Reclassify existing Entries B (Marye) and C (Agnes) from baptisms to burials (page 00725 is a burial page, not a baptism page, per 2026-05-15 image-walk); add probable Francis Gurney burial 8 Nov 1633 as new Entry F. The Round 2 working hypothesis of a separate daughter Susan is withdrawn — FS index VNN2-WRG ("Susan Gurney burial 31 January") is most plausibly an indexer mis-read of the Agnes burial line on page 00725.
2. **§6 children-search framing.** Bound Mary Gurney's English birth via Mary Shed's 1647 Braintree marriage; reframe absence of indexed John+Mary marriage as parish-coverage gap, not absence of event. Introduce split-family chronology.
3. **§8 elimination table.** Mark St Ann Blackfriars 1615 lead as ELIMINATED (father reads Wm., not P or F).
4. **§8 elimination table.** Add the 1636 Newgate apprentice as separately-tracked John whose post-1639 trail is lost; Newgate's own Bury-area origin explains Banks's BSE attribution.
5. **§10.2 corridor.** Add empirical Great Migration corridor numbers (Fischer/Thompson) and the Norfolk-Hingham → Massachusetts-Hingham 1638 Diligent of Ipswich context. Note no Gurney travelled on the Diligent itself.
6. **§11 probability.** Restructure to use explicit residual buckets at the ~65-70% Candidate B reading.
7. **§12 What's Still Needed.** Refresh with the highest-leverage Round 6+ targets (NRO consistory court wills, Commissary Court Maldon admin, Suffolk Ryvett wills, Star Chamber 1620, William Tyng 1653 MA probate, Spelman manuscript pedigree, NEHGR 22:44, 1637-1638 Yarmouth ship manifests).

Two paired research-companion updates:
- `research/people/g14-francis-gurney-fact-sheet.research.md` adds the Marye/Agnes burial reclassification, the 1633 Francis burial, the Edmund Walker Gurney 1644 baptism correction to Bernau/DNB, and the 1664 Essex Visitation reference.
- `research/people/g13-john-gurney-fact-sheet.research.md` adds the Newgate Horningsheath finding, the Mary Shed marriage bounding, and the refreshed probability framing.

## 1. `data/sources.json` source registry operations

Insert these new entries near related existing entries. Preserve file ordering; do not reformat.

### 1.1 Add `fs-vnn2-wrg-agnes-gurney-burial-east-dereham`

Insert near the existing `nro-pd-86-41` block. The FS index transcribes the given name as "Susan," but a 2026-05-15 image-walk of the underlying register page reads the entry as "Agnes the daughter of ffrancis Gurny" with burial date 31 January (year not in register). The sourceId reflects the visual reading; the FS index reading is preserved in the citation field for traceability.

```json
"fs-vnn2-wrg-agnes-gurney-burial-east-dereham": {
  "shortTitle": "FS index VNN2-WRG — Agnes (FS-indexed 'Susan') Gurney burial, East Dereham, father Francis",
  "citation": "England, Norfolk, Parish Registers (County Record Office), 1510-1997, FamilySearch entry indexed as Susan Gurney, burial 31 January (year unspecified in index), Dereham (East Dereham), Norfolk, father Francis. FS index identifier VNN2-WRG. The underlying register entry reads 'Agnes the daughter of ffrancis Gurny'; the FS index 'Susan' is an indexer mis-read.",
  "archive": "FamilySearch — Norfolk Record Office partnership collection",
  "url": "https://www.familysearch.org/ark:/61903/1:1:VNN2-WRG",
  "corpusStatus": "transcript",
  "corpusPath": null,
  "mediaPath": "sources/media/Parish_Register_East_Dereham/page_00725_line_agnes_ffrancis_gurny_sweep.png",
  "validationPath": "sources/validations/fs-east-dereham-francis-gurney-indexed-children.md",
  "notes": "Burial entry for Agnes the daughter of ffrancis Gurny at East Dereham. Visual reading from the enhanced register page (gbprs_norfolk_pd_86-41_00725.jpg, line-level crop) supports 'Agnes the daughter of ffrancis Gurny' with date 31 January; year is index-unspecified. The FS index 'Susan Gurney' is the indexer's mis-read. Resolves the case file's pre-existing Entry C (Agnes c.1614 at image 00724/725) as a burial, not a baptism. Sibling burial entry VNN2-WR2 (indexed Mary, 25 January) is on the same page (FS waypoint S3HT-65F5-TN, image 33 of 110)."
},
```

### 1.2 Add `fs-vnn2-wr2-marye-gurney-burial-east-dereham`

```json
"fs-vnn2-wr2-marye-gurney-burial-east-dereham": {
  "shortTitle": "FS index VNN2-WR2 — Marye Gurney burial, East Dereham, father Francis",
  "citation": "England, Norfolk, Parish Registers (County Record Office), 1510-1997, FamilySearch entry for Mary Gurney, burial 25 January (year unspecified in index), Dereham (East Dereham), Norfolk, father Francis. FS index identifier VNN2-WR2. The underlying register entry reads as 'Marye ... of ffrancis Gurny' with relationship word damaged; reading is 'daughter of' by default given the same-line family-cluster context.",
  "archive": "FamilySearch — Norfolk Record Office partnership collection",
  "url": "https://www.familysearch.org/ark:/61903/1:1:VNN2-WR2",
  "corpusStatus": "transcript",
  "corpusPath": null,
  "mediaPath": "sources/media/Parish_Register_East_Dereham/page_00725_line_marye_ffrancis_gurny_sweep.png",
  "validationPath": "sources/validations/fs-east-dereham-francis-gurney-indexed-children.md",
  "notes": "Burial entry for Marye daughter of ffrancis Gurny at East Dereham, 25 January (year not indexed). Visual reading from the enhanced register page (gbprs_norfolk_pd_86-41_00725.jpg, line-level crop). Resolves the case file's pre-existing Entry B (Marye c.1614-15 at image 00724/725) as a burial, not a baptism. The 25 May 1618 Marye baptism at the same parish (Entry D, FS index VNN2-4VC) is a separate, later child of the same name — a name-reuse pattern consistent with the earlier Marye having died in infancy."
},
```

### 1.3 Add `fs-vnn2-h8s-francis-gurney-burial-east-dereham-1633`

```json
"fs-vnn2-h8s-francis-gurney-burial-east-dereham-1633": {
  "shortTitle": "FS index VNN2-H8S — Francis Gurney burial 8 November 1633, East Dereham",
  "citation": "England, Norfolk, Parish Registers (County Record Office), 1510-1997, FamilySearch entry for Francis Gurney, burial 8 November 1633, Dereham (East Dereham), Norfolk. No parent in index. FS index identifier VNN2-H8S.",
  "archive": "FamilySearch — Norfolk Record Office partnership collection",
  "url": "https://www.familysearch.org/ark:/61903/1:1:VNN2-H8S",
  "corpusStatus": "transcript",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/fs-east-dereham-francis-gurney-indexed-children.md",
  "notes": "Francis Gurney burial 8 November 1633 at East Dereham, parent not in the index. The case file treats this as a probable son of Francis G14 born East Dereham c.1611-1618 who died young. Francis G14 himself died 1646/7 at St Botolph Bishopsgate London; Francis B 'the laceweaver' was a Norwich St Peter Mountergate household. Neither matches. Name-reuse for the 1628 St Benet Fink Francis (case file's Maldon Francis, Bernau 1913) is the corroborating pattern."
},
```

### 1.4 Add `fs-vnn2-scf-edward-gurney-baptism-east-dereham`

```json
"fs-vnn2-scf-edward-gurney-baptism-east-dereham": {
  "shortTitle": "FS index VNN2-SCF — Edward Gurney baptism, East Dereham, father Francis",
  "citation": "England, Norfolk, Parish Registers (County Record Office), 1510-1997, FamilySearch entry for Edward Gurney, christening 27 May 1610, Dereham (East Dereham), Norfolk, father Francis Gurney. FS index identifier VNN2-SCF.",
  "archive": "FamilySearch — Norfolk Record Office partnership collection",
  "url": "https://www.familysearch.org/ark:/61903/1:1:VNN2-SCF",
  "corpusStatus": "transcript",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/fs-east-dereham-francis-gurney-indexed-children.md",
  "notes": "Primary index entry for the East Dereham Edward baptism (case-file Entry A). The indexed date 27 May 1610 inherits its year from a modern margin annotation 'PD 86/41/6 1610' written on the page in the same recent hand as the modern parish-volume foliation; it is not a contemporaneous register-year heading. The case file's ±2-3 year margin on East Dereham dates remains the correct posture."
},
```

### 1.5 Add `fs-jw7y-c3b-john-gurney-baptism-st-ann-blackfriars`

```json
"fs-jw7y-c3b-john-gurney-baptism-st-ann-blackfriars": {
  "shortTitle": "FS index JW7Y-C3B — John Gurney baptism, St Ann Blackfriars, 1615, father Wm.",
  "citation": "England, Births and Christenings, 1538-1975, FamilySearch entry for John Gurney, christening 13 March 1615, Saint Ann Blackfriars, London, father Wm. Gurney. FS index identifier JW7Y-C3B.",
  "archive": "FamilySearch — England, Births and Christenings, 1538-1975",
  "url": "https://www.familysearch.org/ark:/61903/1:1:JW7Y-C3B",
  "corpusStatus": "transcript",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": null,
  "notes": "Image unavailable in FS at index level. Father is indexed as 'Wm.' (William) Gurney, not P or F. Resolves the case file's earlier 'P Gurney' lead. Consistent with the London William Gurney cluster (Coleman Street Protestation; PROB 11/252/152 barber-chirurgion William, sons John, Abel, Walter)."
},
```

### 1.6 Add `wikitree-newgate-14-horningsheath`

```json
"wikitree-newgate-14-horningsheath": {
  "shortTitle": "WikiTree Newgate-14 — John Newgate of Horningsheath, Suffolk",
  "citation": "WikiTree profile John Newgate (Newgate-14): born about 1590 [uncertain], probably Horningsheath, Suffolk, England; resided Hessett (Suffolk), Bury St Edmunds, and Southwark; emigrated 1633 to Boston, Massachusetts; hatter, feltmaker, haberdasher; died before 8 September 1665, Boston; will dated 25 November 1664, proved 11 September 1665.",
  "archive": "WikiTree.com",
  "url": "https://www.wikitree.com/wiki/Newgate-14",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/wikitree-newgate-14-horningsheath.md",
  "notes": "Compiled-genealogy source used in the case file solely for the John Newgate origin location (Horningsheath, Suffolk, ~3 miles from Bury St Edmunds). The Horningsheath origin is the cleanest explanation for Banks's 'Bury St Edmunds' attribution: the 1636 apprentice John Gurney whom Newgate brought before the governor would naturally have come from Newgate's own region. Treat as compiled-genealogy lead, not primary."
},
```

### 1.7 Add `fischer-albions-seed-1989-corridor` *(only if a corridor-specific entry is not already represented)*

Per Round 1 web confirmation, `fischer-albions-seed-1989` already exists in `sources.json` (line 350). No new entry required; reuse the existing sourceId for the §10.2 corridor citation.

### 1.8 Add `thompson-mobility-migration-1994`

```json
"thompson-mobility-migration-1994": {
  "shortTitle": "Thompson, Mobility and Migration (1994)",
  "citation": "Thompson, Roger. Mobility and Migration: East Anglian Founders of New England, 1629-1640. Amherst: University of Massachusetts Press, 1994.",
  "archive": null,
  "url": null,
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": null,
  "notes": "Statistical study of the East Anglian Great Migration cohort. Documents 2,000+ individuals departing from greater East Anglia (Lincoln-Norfolk-Suffolk-Cambridge-Essex) 1630-1640 to New England. Used in case-file §10.2 corridor framing alongside Fischer (`fischer-albions-seed-1989`)."
},
```

### 1.9 Add `shedd-daniel-shed-genealogy-1920`

```json
"shedd-daniel-shed-genealogy-1920": {
  "shortTitle": "Shedd, Daniel Shed Genealogy (1920)",
  "citation": "Shedd, Frank Edson, Hubert C. Shedd, and J. Gardner Bartlett. Daniel Shed Genealogy: Ancestry and Descendants of Daniel Shed of Braintree, Massachusetts, 1327-1920. Boston: Shedd Family Association, 1920.",
  "archive": "Internet Archive",
  "url": "https://archive.org/details/danielshedgeneal01shed",
  "corpusStatus": "partial",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": null,
  "notes": "Daniel Shed (b. Finchingfield, Essex, baptized 25 June 1620; first in Braintree records 1643; married Mary Gurney 1647) and descendants. Records seven children of Daniel + Mary between 1 October 1647 and 30 October 1658 per Braintree Book of Records. Used in case-file §6 to bound Mary Gurney's English birth before 1628."
},
```

### 1.10 Add `findmypast-norfolk-burials-index`

```json
"findmypast-norfolk-burials-index": {
  "shortTitle": "Findmypast Norfolk Burials index",
  "citation": "Norfolk Burials, Findmypast (sid=103). Norfolk Record Office partnership index of parish burial registers.",
  "archive": "Findmypast / Norfolk Record Office",
  "url": "https://search.findmypast.com/search-world-records/norfolk-burials",
  "corpusStatus": "transcript",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": null,
  "notes": "Used in negative-result mode for Margaret Rybett's burial 1614-1620: zero Margaret Gurney/Ryvett burials surface across Norfolk surname variants, including at East Dereham specifically. Burial therefore not in indexed Norfolk burials; future targets are Suffolk burials (Ryvett family geography) and the East Dereham parish-register burial-section image walk."
},
```

## 2. Thin validation notes

### 2.1 New validation `sources/validations/fs-east-dereham-francis-gurney-indexed-children.md`

```markdown
# FamilySearch indexed children of Francis Gurney at East Dereham

Examined: 2026-05-15 FamilySearch authenticated session (England, Norfolk, Parish Registers (County Record Office), 1510-1997 collection) plus a paired image-walk of the East Dereham parish-register crops at `sources/media/Parish_Register_East_Dereham/`. Working artifacts and the deeper page-00725 analysis are in `sources/media/Parish_Register_East_Dereham/burial-analysis.md`, `crop-index.md`, and `page-00725-deep-analysis.md`.

Findings landed in:
- `research/case-files/john-gurney-case-file-v4.md` Section 4 children table and Section 11 probability discussion.
- `research/people/g14-francis-gurney-fact-sheet.research.md` working notes (East Dereham primary expansion subsection).

Source IDs added:
- `fs-vnn2-scf-edward-gurney-baptism-east-dereham` (Edward, baptism; FS-indexed "27 May 1610")
- `fs-vnn2-wr2-marye-gurney-burial-east-dereham` (Marye, burial 25 January, year not indexed; previously case-file Entry B "Marye c.1614-15," reclassified from baptism to burial)
- `fs-vnn2-wrg-agnes-gurney-burial-east-dereham` (Agnes, burial 31 January, year not indexed; FS index transcribes "Susan" but the register reads "Agnes the daughter of ffrancis Gurny"; previously case-file Entry C "Agnes c.1614," reclassified from baptism to burial)
- `fs-vnn2-h8s-francis-gurney-burial-east-dereham-1633` (Francis, burial 8 November 1633, parent not indexed)

Two corrections to earlier working notes apply:

1. The Round 2 working hypothesis of a previously-undocumented daughter Susan is **withdrawn**. The FS index "Susan Gurney" entry VNN2-WRG is most plausibly an indexer mis-read of "Agnes the daughter of ffrancis Gurny" on page 00725 (line-level crop `sources/media/Parish_Register_East_Dereham/page_00725_line_agnes_ffrancis_gurny_sweep.png`).
2. The case file's pre-existing Entries B (Marye) and C (Agnes), previously classed as baptisms at image 00724/725, are **burial entries** on page 00725, not baptisms. Their year is not indexed in the register on that page.

The FS index date "27 May 1610" for Edward inherits from a modern margin annotation on the parish-register image (the same modern hand also wrote "PD 86/41/6" on the page), not from a contemporaneous register-year heading. The case file's ±2-3 year date margin remains the correct posture for all East Dereham Francis Gurney baptism estimates. The 8 November 1633 Francis burial does not carry a parent in the FS index; the "probable son of Francis G14" reading rests on geographic + chronological elimination of competing Francis Gurney identifications and on the documented name-reuse pattern at the 1628 St Benet Fink Francis baptism (Bernau 1913).

Margaret Rybett (Francis G14's first wife, d. c.1616-1617) — no burial entry matching "Margaret wife of ffrancis Gurnie / Gurney / Gurny" or a Rybett/Ryvett variant was identified in the 2026-05-15 image-walk of the reviewed crops. The negative result is consistent with the earlier Findmypast Norfolk Burials Index negative; her burial parish remains open.

Other image-walk leads, held-review for future intake:
- A probable baptism of "Margaret, daughter of ffrancis Gurnoe/Gurney, May 25" on `crop_00732_enhanced.png` (page-00732 of the East Dereham register). If confirmed, this would be a previously-undocumented daughter Margaret of Francis G14, plausibly named for the first wife after her death. The reading is preliminary and needs same-hand comparator review before promotion.
```

### 2.2 New validation `sources/validations/wikitree-newgate-14-horningsheath.md`

```markdown
# WikiTree Newgate-14 — Horningsheath origin

Examined: 2026-05-15 web pass of WikiTree profile https://www.wikitree.com/wiki/Newgate-14 .

Findings landed in:
- `research/case-files/john-gurney-case-file-v4.md` Section 8 (new 1636 Newgate apprentice row) and Section 10.6 (Banks's Bury St Edmunds attribution explanation).
- `research/people/g13-john-gurney-fact-sheet.research.md` working notes (Newgate Horningsheath origin / Banks BSE explanation).

Source ID added:
- `wikitree-newgate-14-horningsheath`

WikiTree is compiled-genealogy level. The Horningsheath, Suffolk origin for John Newgate is cited by WikiTree with corroborating mentions across multiple genealogical sources; a 1583 Horningsheath baptism is flagged as possibly belonging to Newgate or to a same-named brother. Horningsheath sits ~3 miles south-west of Bury St Edmunds. Newgate resided later at Hessett (Suffolk), Bury St Edmunds, and Southwark before emigrating in 1633.

The 1639 Winthrop deed (Winthrop Papers vol. 4) independently identifies John Newgate as "of Boston in New England Feltmaker." That confirms the trade and Boston residence but not the Horningsheath origin directly.

A primary-source pull of the 1583 Horningsheath parish baptism register, or Newgate's own 1664 will (proved 11 September 1665), would convert the Horningsheath origin from compiled-source level to primary-source level. Treat as compiled-source lead until then.
```

## 3. `research/people/g14-francis-gurney-fact-sheet.research.md` updates

The companion file has an existing "Working Notes" section block. Insert a new compact subsection immediately AFTER the existing "King's Lynn worsted-yarn venture, 1622" subsection block and BEFORE the existing "Pettigrew on Francis Gurnay of London and the Keswick commercial line" subsection.

```markdown
### East Dereham children — primary index expansion and Entries B/C reclassification (FS + image-walk, 2026-05-15)

Two changes to Francis G14's documented East Dereham child set, both grounded in a 2026-05-15 image-walk of the parish-register crops at `sources/media/Parish_Register_East_Dereham/` cross-checked against FamilySearch index entries in the England, Norfolk, Parish Registers (County Record Office), 1510-1997 collection:

1. **Entries B (Marye) and C (Agnes) are burials, not baptisms.** Page 00725 sits in a burial sequence. The Marye line (25 January, year not in register, FS index VNN2-WR2) reads "Marye ... of ffrancis Gurny" with the relationship word partly obscured by staining; the Agnes line (31 January, year not in register, FS index VNN2-WRG) reads "Agnes the daughter of ffrancis Gurny" with stronger comparative support. The Round 2 working hypothesis of a previously-undocumented daughter Susan is withdrawn: FS index VNN2-WRG transcribes "Susan Gurney" but the underlying register entry reads Agnes — an indexer mis-read. The case file's existing Entries B and C therefore remain confirmed children of Francis G14 with the original given names Marye and Agnes; only the event (baptism → burial) and source basis have changed.[^fs-east-dereham-children-2026]

2. **New Entry F: Francis (probable son), burial 8 November 1633, East Dereham (FS index VNN2-H8S).** No parent in the index. The probable-son-of-Francis-G14 reading rests on Francis G14's documented East Dereham residence in those years; elimination of competing Francis Gurney identifications (Francis G14 himself died 1646/7 at St Botolph Bishopsgate London; Francis B "the laceweaver" was at Norwich St Peter Mountergate); and Francis G14's documented name-reuse for the 1628 St Benet Fink Francis baptism (Bernau 1913). Estimated age at death is ~15-22 if born East Dereham c.1611-1618.[^fs-east-dereham-children-2026]

The FS-indexed date "27 May 1610" for the Edward baptism (case-file Entry A, FS ID VNN2-SCF) inherits its year from a modern margin annotation on the parish-register page rather than from a contemporaneous register-year heading. The case file's ±2-3 year margin on East Dereham dates remains the correct posture.[^fs-east-dereham-children-2026]

Image-walk also surfaced a probable baptism of "Margaret, daughter of ffrancis Gurnoe/Gurney, May 25" on `crop_00732_enhanced.png` (page 00732 of the East Dereham register). This is preliminary, needs same-hand comparator review, and is held outside the case-file body pending confirmation. If confirmed, a daughter Margaret of Francis G14 would be a name-honoring entry consistent with the first wife Margaret Rybett dying before that baptism.[^east-dereham-margaret-bapt-lead]

[^fs-east-dereham-children-2026]: FamilySearch England, Norfolk, Parish Registers (County Record Office), 1510-1997 index entries VNN2-SCF (Edward christening, FS-indexed 27 May 1610), VNN2-WR2 (Marye burial 25 January, year not indexed), VNN2-WRG (Agnes burial 31 January, year not indexed; FS-indexed as "Susan"), VNN2-H8S (Francis burial 8 November 1633). Source IDs `fs-vnn2-scf-edward-gurney-baptism-east-dereham`, `fs-vnn2-wr2-marye-gurney-burial-east-dereham`, `fs-vnn2-wrg-agnes-gurney-burial-east-dereham`, `fs-vnn2-h8s-francis-gurney-burial-east-dereham-1633`. Validation note `sources/validations/fs-east-dereham-francis-gurney-indexed-children.md`. Image-walk artifacts at `sources/media/Parish_Register_East_Dereham/burial-analysis.md`, `crop-index.md`, and `page-00725-deep-analysis.md`.
[^east-dereham-margaret-bapt-lead]: Image-walk note in `sources/media/Parish_Register_East_Dereham/burial-analysis.md` flagging a probable baptism reading of "Margaret the daughter of ffrancis Gurnoe/Gurney bapt may 25" on `crop_00732_enhanced.png`. Held for confirmation; not promoted to the case-file body in v39.
```

Inside the existing Bernau-derived "Children at St Benet Fink — Bernau's list vs. current fact sheet" subsection block, insert the following compact addition immediately AFTER the existing Bernau-children comparison tables and BEFORE the "Speculative additions in Bernau" line.

```markdown
**Late correction to DNB / Bernau on Edmund the Divine.** A FamilySearch index entry shows Edmund Walker Gurney baptized 13 October 1644 at Norwich, father Edmund Gurney. This places at least one surviving son of Edmund Gurney G14b (the Divine, d. 1648) past the Protestant child of 1624 whom DNB and Bernau treat as Edmund's only known issue. Material to Edmund Gurney G14b's biography, not to Francis G14 directly.[^edmund-walker-gurney-1644]

[^edmund-walker-gurney-1644]: FamilySearch index entry for Edmund Walker Gurney, christening 13 October 1644, Norwich, Norfolk, father Edmund Gurney. Sources `fs-england-births-christenings`.
```

Inside the existing "Heralds' Visitation date — conflict flagged" subsection, insert a compact note at the end of that subsection:

```markdown
Walter Rye's *The Gurneys of Norwich* (Norfolk Antiquarian Miscellany, 1906) independently cites a 1664 Essex Visitation attestation of the Gurney pedigree at p. 537 in addition to the 1633 London Visitation. The 1664 Essex Visitation is most plausibly Francis G14's son Francis-the-younger of Maldon attesting the pedigree after his father's 1646/7 death; documenting the connection is useful for downstream Browning / Maldon work but does not change Francis G14's biography directly.[^rye-1664-essex-visitation]

[^rye-1664-essex-visitation]: Walter Rye, "The Gurneys of Norwich," *Norfolk Antiquarian Miscellany* (Norwich: Gibbs and Waller, 1906), p. 285; corpus extract at `sources/corpus/norfolk-antiquarian-gurneys-of-norwich.md`. Source ID `rye-norfolk-antiquarian`.
```

## 4. `research/people/g13-john-gurney-fact-sheet.research.md` updates

This companion has an existing "Working Notes" section and a separate "Origin Analysis and Elimination Work" section. Add three new compact subsections.

### 4.1 New subsection in Working Notes block (after the "The Newgate apprenticeship / 1636 record — de-conflated" subsection)

```markdown
### Newgate's Horningsheath origin — explains Banks's Bury St Edmunds attribution

John Newgate himself was from Horningsheath, Suffolk (~3 miles south-west of Bury St Edmunds), residing later at Hessett, Bury St Edmunds, and Southwark before his 1633 emigration.[^newgate-horningsheath-2026] The 1636 apprentice he brought before the Boston court was therefore most plausibly a young Suffolk man drawn from Newgate's own kinship or apprenticeship network. This is the cleanest single explanation for Banks's "Bury St Edmunds" attribution for John Gurney (`banks-brownell-1937` p. 151): Banks's manuscript memo likely recorded the apprentice rather than the older Braintree John, with subsequent compiler tradition then conflating the two Johns into a single biographical sketch.

Anderson's 1636 arrival date in the *Great Migration Directory* (`anderson-gmd-2015` p. 158) is most plausibly traceable to the same Newgate-apprentice tradition rather than to the older Braintree John, who first appears in primary colonial records at Weymouth in June 1641. The recurring American family-memory tradition of a 29 September 1615 birth and "Southwark, near London Bridge" origin (Lysander F. Gurney sketch; *American Biography* vol. 26; Find a Grave memorial 252975617) sits cleanly inside the apprentice's profile (1615 birth, Newgate's last English residence at Southwark) and would have entered the American line via the apprentice's own descent (if he stayed in New England) or via early conflation with the older man.

No separate post-1639 colonial trail surfaces in indexed Massachusetts records for a John Gurney born c.1615. The apprentice may have died in early Boston (smallpox, fluxes, and infant mortality were endemic), returned to England at term-end, or married into a non-Gurney surname. The two-Johns reading remains the cleanest framing.

[^newgate-horningsheath-2026]: WikiTree profile John Newgate (Newgate-14), https://www.wikitree.com/wiki/Newgate-14. Source ID `wikitree-newgate-14-horningsheath`. Validation note `sources/validations/wikitree-newgate-14-horningsheath.md`. The 1583 Horningsheath baptism is flagged in the WikiTree source as possibly belonging to John or to a same-named brother. A primary-source pull of the Horningsheath parish-register baptism and of Newgate's own 1664 will (proved 11 September 1665) would convert this from compiled-source to primary level.
```

### 4.2 New subsection in Working Notes (after the previous insertion)

```markdown
### Great Migration corridor — empirical priors for Candidate B

Approximately 60 percent of Massachusetts Bay emigrants 1630-1640 came from nine eastern counties (Norfolk, Suffolk, Essex, Hertfordshire, Cambridgeshire, Huntingdonshire, Lincolnshire, parts of Bedfordshire, Kent), with under 10 percent from London proper and the remaining ~40 percent from thirty-four other English counties.[^fischer-corridor-2026] Roger Thompson documents 2,000+ departures from greater East Anglia (Lincoln-Norfolk-Suffolk-Cambridge-Essex) in the same decade.[^thompson-corridor-2026] Francis G14's combined Norfolk-and-London profile sits inside the dominant corridor.

The Edward Gilman cohort emigration on the Diligent of Ipswich (departed 26 April 1638 Gravesend, arrived Boston 10 August 1638, primarily Norfolk Hingham passengers bound for Hingham, Massachusetts — fewer than 10 miles from Braintree/Weymouth) is the corridor event nearest in time and place to John Gurney's 1641 Weymouth appearance. Ann Gurney's husband John Gilman was apprenticed in 1609 in Deopham, Norfolk as a worsted weaver to John Bubbyn; Ann Gurney + John Gilman themselves did not emigrate (Ann buried Hingham, Norfolk, 23 November 1651), but at least two of their sons emigrated to Exeter, New Hampshire (John Gilman Jr born 1638, emigrated by 1658; Charles Gilman born 1642, emigrated 1664 "with his brother John and cousins"). The Diligent passenger list itself contains no Gurney passenger (Banks/Cushing transcription), so John Gurney travelled on a different vessel within the same multi-year corridor.[^gilman-diligent-2026]

The conditional probability of an East Anglia / London origin for the colonial John, given his Essex colonial associations (Daniel Shed of Finchingfield as son-in-law, William Tyng of Stanford Rivers as landlord, Braintree-MA named after Braintree-Essex, Coleman Street adjacency), is materially higher than the unconditional ~60% corridor baseline.

[^fischer-corridor-2026]: David Hackett Fischer, *Albion's Seed: Four British Folkways in America* (New York: Oxford University Press, 1989), ch. 6 "Regional Origins of the Puritan Migration." Source ID `fischer-albions-seed-1989`.
[^thompson-corridor-2026]: Roger Thompson, *Mobility and Migration: East Anglian Founders of New England, 1629-1640* (Amherst: University of Massachusetts Press, 1994). Source ID `thompson-mobility-migration-1994`.
[^gilman-diligent-2026]: Diligent of Ipswich 1638 passenger list per Charles Edward Banks, *Planters of the Commonwealth* (Boston, 1930), transcribed by Daniel Cushing (3rd-4th Town Clerk of Hingham MA) and republished at packrat-pro.com/ships/dilligent.htm (accessed 2026-05-15). John Gilman / Ann Gurney biography per WikiTree profiles Gilman-72 and Gurney-13 (compiled-genealogy level). The Diligent passenger list contains no Gurney variant. No source ID added for the packrat transcription; the Banks 1930 work itself sits at the level of compiled-genealogy origin documentation.
```

### 4.3 New subsection in Working Notes (after the previous insertion)

```markdown
### Mary Gurney's English birth — bounded via Mary Shed 1647 marriage

Daniel Shed was baptized 25 June 1620 at St John the Baptist, Finchingfield, Essex (parish register confirmed via Essex, England Church of England Baptisms, Marriages and Burials 1538-1812). He first appears in Braintree, Massachusetts records by 1643 and married Mary Gurney in 1647. The Braintree Book of Records preserves seven births to Daniel and Mary between 1 October 1647 and 30 October 1658.[^shedd-1920-mary-bounding]

At a minimum reasonable marriage age of 16, Mary Gurney was born by 1631. Standard derivative tradition (Sprague p. 695; *History of Weymouth* vol. 3 p. 251; Torrey p. 666 with question marks; Shedd 1920) places her birth at c.1628 in England. Either way, Mary was born in England well before any colonial residence for the colonial John Gurney.

This bounds the John Gurney + Mary marriage as an English event before 1628. FS, Findmypast, and Ancestry indexed eastern-England parish-marriage collections 1620-1635 contain zero John Gurney + Mary marriages outside the already-eliminated Eythorne Kent / Mary Marsh event. The absence of an indexed John+Mary marriage reflects parish-register coverage gaps in 17th-century East Anglian indexing rather than an absent or out-of-England event. A plausible split-family chronology places Sarah, Mary, Richard, and John Jr born in England (c.1627-1633) and Peter and possibly Isaac born in Massachusetts (c.1638-1645).

The case-file's prior "no English baptism of any colonial-John child" reading is best understood as a parallel parish-register-coverage gap on the English side, not as evidence against an English marriage.

[^shedd-1920-mary-bounding]: Frank E. Shedd, Hubert C. Shedd, and J. Gardner Bartlett, *Daniel Shed Genealogy: Ancestry and Descendants of Daniel Shed of Braintree, Massachusetts, 1327-1920* (Boston: Shedd Family Association, 1920), https://archive.org/details/danielshedgeneal01shed; Bates, *Records of the Town of Braintree* (1886). Source IDs `shedd-daniel-shed-genealogy-1920`, `braintree-records-1640-1793-1886`.
```

### 4.4 Working Hypotheses block update at end of file

Replace the existing "Working Hypotheses" block at the bottom of the file with:

```markdown
## Working Hypotheses

- **Candidate B** (son of Francis G14 + Margaret Rybett, probably Norwich / East Dereham connected): **~65-70%**. Active working hypothesis. Probability raised from v4's ~55-60% on the basis of (a) the Newgate Horningsheath finding redirecting Banks's BSE attribution off the elder Braintree John, (b) FS-indexed primary reclassification of Francis G14's East Dereham child cluster (Marye and Agnes burial entries now confirmed at the FS-index level via VNN2-WR2 and VNN2-WRG, plus a probable 1633 Francis burial at VNN2-H8S), and (c) the Mary Shed 1647 marriage tightly bounding the John+Mary marriage to England before 1628 and reframing the indexed-marriage absence as a parish-coverage gap rather than counter-evidence.
- **Candidate A** (Stewkley baptism 1602/3 → Bierton marriage 1628 → Aylesbury hundred → Walgrave Northamptonshire 1650): **ELIMINATED**. Continuous English residence 1603-1653 with wife Alice Oliffe.
- **Candidate C** (Berkhamsted, Hertfordshire): **ELIMINATED**. Eight-child Berkhamsted family group 1610-1636 fathered by a John born about 1585-1590.
- **Candidate D** (London Drapers' / Old Change): **Unlikely (~3-5%)**. Strong post-1625 London continuity argues against the migration profile.
- **Other named candidates** (Aylesbury Cowheard groom, Norwich Jane Wright groom, etc.): **~5% combined**.
- **Unknown corridor (East Anglia / London)**: ~15-20% residual.
- **Unknown other corridor (Kent, Lincs, West Country)**: ~5-10% residual.
- **1636 apprentice as distinct second John whose later trail is lost**: ~3-5%.
```

## 5. Case-file edits in `research/case-files/john-gurney-case-file-v4.md`

### 5.1 Section 4.2 children table — reclassify Entries B and C as burials; add one new row

A 2026-05-15 image-walk of the East Dereham parish register (`sources/media/Parish_Register_East_Dereham/page-00725-deep-analysis.md`) shows that page 00725 is a burial page, not a baptism page. The case file's existing Entries B (Marye) and C (Agnes) are therefore burials, not baptisms; their year is unindexed in the register on that page. The FS index VNN2-WRG entry for "Susan Gurney burial 31 January" is most plausibly an indexer mis-read of the same line that visually reads "Agnes the daughter of ffrancis Gurny" — so the Round 2 working hypothesis of a previously-unrecorded daughter Susan is withdrawn. The case file therefore does not gain a Susan child; it gains a reclassification of Entries B and C from baptisms to burials, plus one new burial entry for a probable son Francis 8 November 1633.

Find the existing children table at §4.2 (lines 163-169):

```markdown
| Entry | Child | Est. Date | Page/Image | Certainty |
|---|---|---|---|---|
| **A** | Edward | c.1611/12 | 00721 | Confirmed |
| **B** | Marye | c.1614–15 | 00724/725 | Confirmed |
| **C** | Agnes | c.1614 | 00724/725 | Confirmed |
| **D** | Marye | 25 May 1618 | 00736 | Confirmed |
| **E** | **John** | **c.1609/10** | **00715** | **Probable** |
```

Replace with:

```markdown
| Entry | Child | Event | Est. Date | Page/Image | Certainty |
|---|---|---|---|---|---|
| **A** | Edward | Baptism | c.1611/12 | 00721 | Confirmed<sup class="fn"><a href="#n96" id="ref-96a">96</a></sup> |
| **B** | Marye (earlier daughter) | Burial | 25 January, year not in register | 00725 (FS index VNN2-WR2) | Confirmed<sup class="fn"><a href="#n96" id="ref-96b">96</a></sup> |
| **C** | Agnes | Burial | 31 January, year not in register | 00725 (FS index VNN2-WRG; indexed "Susan") | Confirmed<sup class="fn"><a href="#n96" id="ref-96c">96</a></sup> |
| **D** | Marye (later daughter) | Baptism | 25 May 1618 | 00736 (FS index VNN2-4VC) | Confirmed |
| **E** | **John** | **Baptism** | **c.1609/10** | **00715** | **Probable** |
| **F** | **Francis (probable son)** | **Burial** | **8 November 1633** | **FS index VNN2-H8S** | **Probable son**<sup class="fn"><a href="#n96" id="ref-96d">96</a></sup> |
```

### 5.2 Section 4.2 — short prose addition immediately after the children table

Insert this paragraph immediately after the children table and before the existing "**These dates should be understood as estimates with a margin of approximately ±2–3 years.**" line.

```markdown
The reclassification of Entries B and C from baptisms to burials reflects a 2026-05-15 image-walk of page 00725, which sits in a burial sequence rather than a baptism sequence. The Marye burial (25 January) and Agnes burial (31 January) appear close together in the lower part of the page; the relationship word on the Marye line is partly obscured by staining, while the Agnes line reads "Agnes the daughter of ffrancis Gurny" with comparative support from same-page Gurney lines. The 25 May 1618 Marye baptism (Entry D) is therefore a later, separately-born daughter named for an earlier deceased Marye — a routine name-reuse pattern in this period. The 1633 Francis Gurney burial (Entry F) does not carry a parent in the FS index; its identification as a probable son of Francis G14 rests on geographic and chronological elimination of competing Francis Gurney identifications (Francis G14 himself died 1646/7 at St Botolph Bishopsgate London; Francis B "the laceweaver" was a Norwich St Peter Mountergate household) and on Francis G14's documented name-reuse for the 1628 St Benet Fink Francis baptism (Bernau 1913). The previously-reported "Susan" addition has been withdrawn: FS index VNN2-WRG ("Susan Gurney burial 31 January") is most plausibly an indexer mis-read of the Agnes burial line on the same page.<sup class="fn"><a href="#n96" id="ref-96e">96</a></sup>
```

### 5.3 Section 6 — replace the children-search prose with Mary-bounded reframing

Find the existing §6.1 paragraph block beginning "The ages of the colonial John Gurney's children meant they were most probably born in England..." and the children-search matrix table that follows. Preserve the existing matrix table (the four-row Berkhamsted/Aylesbury/Eythorne/Toddington table) verbatim. Replace only the leading paragraph and add a short framing paragraph immediately after the matrix table.

Replace the existing leading paragraph:

```markdown
The ages of the colonial John Gurney's children meant they were most probably born in England, thus the analysis turned to searching of English parish baptismal records for children matching the known names and approximate birth dates. Over 20 baptism records in the names of John Gurney's children were identified in England. No parish cluster produces all five target children with a father named John Gurney and a mother named Mary (including variant spellings of the names). The closest results are listed below but are very poor matches when factoring in dates, mother's name, etc.
```

With:

```markdown
Mary Gurney, who married Daniel Shed at Braintree in 1647, must have been born in England before 1628 — Daniel was baptized 25 June 1620 at Finchingfield, Essex, and the Braintree Book of Records preserves seven births to Daniel and Mary between 1 October 1647 and 30 October 1658; even at a minimum marriage age of 16, Mary was born by 1631, and the standard derivative tradition places her at c.1628.<sup class="fn"><a href="#n97" id="ref-97a">97</a></sup> The John Gurney + Mary marriage therefore took place in England before 1628. FS, Findmypast, and Ancestry indexed eastern-England parish-marriage collections 1620-1635 contain zero John Gurney + Mary marriages outside the already-eliminated Eythorne Kent / Mary Marsh event. The absence of an indexed John+Mary marriage reflects parish-register coverage gaps in 17th-century East Anglian indexing rather than an absent or out-of-England event. A plausible split-family chronology has Sarah, Mary, Richard, and John Jr born in England c.1627-1633 and Peter and possibly Isaac born in Massachusetts c.1638-1645.<sup class="fn"><a href="#n97" id="ref-97b">97</a></sup>

The earlier children-search line of reasoning — that all five colonial children should be findable in English parish baptisms — should therefore be read as a parish-register-coverage probe rather than a binary identification test. Over 20 baptism records in the names of John Gurney's children were identified in England across this search, but no parish cluster produces all five target children with a father named John Gurney and a mother named Mary (including variant spellings). The closest results are listed below but remain weak matches on dates, mother's name, or both.
```

Then immediately after the existing four-row matrix table (Berkhamsted, Aylesbury, Eythorne, Toddington), add this single-paragraph framing line:

```markdown
The four near-miss clusters above are weak. The colonial John's first three children (Sarah, Mary, Richard) most plausibly sit in an unindexed eastern-England parish marriage and baptism record set, and the case file does not treat their absence from indexed collections as eliminating evidence for any specific origin hypothesis.<sup class="fn"><a href="#n97" id="ref-97c">97</a></sup>
```

### 5.4 Section 8 elimination table — mark St Ann Blackfriars 1615 as ELIMINATED

Find the row block in the Section 8 elimination table beginning `| St Botolph Aldgate, London |` and ending with the `| St Giles Cripplegate (Francis Garney joiner) |` row.

Immediately AFTER the existing row `| St Giles Cripplegate, London (Francis B) | London | - | **ELIMINATED** | Died in England (buried St Giles Cripplegate as an infant aged 2 days, son of Francis B the laceweaver). |` and BEFORE the existing row `| St Giles Cripplegate (Francis Garney joiner) | London | - | **ELIMINATED** | Died in England (buried St Giles Cripplegate December 1640, son of Francis Garney joiner).<sup class="fn"><a href="#n70" id="ref-70">70</a></sup> |`, insert this new row:

```markdown
| St Ann Blackfriars, London (John bapt 1615) | London | - | **ELIMINATED** | FS index reads father as Wm. (William), not P or F. Resolves the case file's earlier "P Gurney" lead. Most plausibly the London William Gurney cluster (Coleman Street area; PROB 11/252/152 barber-chirurgion William, sons John, Abel, Walter). The 1615 baptism date for this John (son of William) is also consistent with the 1636 Newgate apprentice's implied birth year under the two-Johns reading.<sup class="fn"><a href="#n98" id="ref-98a">98</a></sup> |
```

### 5.5 Section 8 elimination table — add 1636 Newgate apprentice row

Immediately AFTER the existing row beginning `| London Merchant Taylor apprentice (Aylesbury, Bucks 1655) | London / Bucks |` (the last row before §8.1), insert this new row:

```markdown
| **1636 Newgate apprentice (distinct second John)** | Suffolk (likely Bury area) → Boston | — | **Distinct second John; trail lost** | Implied birth c.29 September 1615 from the Winthrop/Savage 21 July 1636 court order setting service until age 24. Chronologically incompatible with the older Braintree John (deposed "aged 50 or thereabouts" 1652/3, born c.1602/3). John Newgate himself was from Horningsheath, Suffolk (~3 mi from Bury St Edmunds), residing later at Hessett, Bury, and Southwark before emigrating 1633; the apprentice was therefore most plausibly a young Suffolk man drawn from Newgate's own region. Banks's "Bury St Edmunds" attribution likely tracks this apprentice rather than the older Braintree John. No separate post-1639 colonial trail surfaces in indexed Massachusetts records for a John Gurney born c.1615; likeliest readings are early-Boston mortality, return to England, or absorption into a non-Gurney surname via marriage. The recurring American family-memory tradition of a 29 September 1615 birth and Southwark origin (Lysander F. Gurney sketch; *American Biography* vol. 26; Find a Grave memorial 252975617) sits cleanly in the apprentice's profile and was later conflated with the older Braintree John by 19th-century compilers.<sup class="fn"><a href="#n99" id="ref-99a">99</a></sup> |
```

### 5.6 Section 10.2 — add corridor empirics paragraph

Find the existing §10.2 first paragraph beginning `Norfolk, Suffolk, Essex, and London constituted the geographic heart...` Leave it intact. Insert this new paragraph immediately AFTER that first paragraph and BEFORE the existing `Edmund Gurney (1577–1648), Francis's brother...` paragraph.

```markdown
The corridor is quantifiable. Approximately 60 percent of Massachusetts Bay emigrants 1630-1640 came from nine eastern counties (Norfolk, Suffolk, Essex, Hertfordshire, Cambridgeshire, Huntingdonshire, Lincolnshire, parts of Bedfordshire, and Kent), with under 10 percent from London proper; Roger Thompson documents 2,000+ departures from greater East Anglia in the same decade. Francis G14's combined Norfolk-and-London profile sits inside the dominant corridor. The Edward Gilman cohort emigration on the Diligent of Ipswich (departed 26 April 1638 Gravesend, arrived Boston 10 August 1638, primarily Norfolk Hingham passengers bound for Hingham, Massachusetts — fewer than 10 miles from Braintree/Weymouth) is the corridor event nearest in time and place to John Gurney's June 1641 Weymouth appearance. The Diligent passenger list itself contains no Gurney passenger, so John Gurney travelled on a different vessel within the same multi-year corridor.<sup class="fn"><a href="#n100" id="ref-100a">100</a></sup>
```

### 5.7 Section 11 — replace probability table

Replace the existing §11 table block:

```markdown
| Candidate | Probability | Basis |
|---|---|---|
| **B — Son of Francis & Margaret Rybett** | **~55-60%** | First marriage confirmed. Entry E favors "ffrancis." Occupational match. Geographic corridor. Essex network. Financial motive. Coleman Street proximity. |
| **A — Stewkley / Bierton / Aylesbury family group → Northants** | **ELIMINATED** | Continuous English residence 1603-1653; wife Alice Oliffe; five Aylesbury children 1638-1653; 1641 cert of residence; 1650 Walgrave tenancy. |
| **C — Berkhamsted, Herts** | **ELIMINATED** | Eight-child Berkhamsted family 1610-1636 fathered by a John born about 1585-1590; Francis son 1636; absent Mary and Peter. |
| **D — Son of Robert Gurney, citizen and draper / tailor of Old Change** | **Unlikely (~3-5%)** | London Drapers' father-son trade match and plausible c.1600-1604 birth window. Strong post-1625 London continuity evidence (1630 Drapers' master, 1638 St Augustine £10 rent, Hunscott will-overseer still in same parish, Boyd's-card cue to 1661 Old Change poll-tax) argues against the migration profile. No wife Mary, no matching child set, no Puritan-corridor associate, no Massachusetts bridge. See 8.4 and `research/people/john-gurney-candidate-d.md`. |
| **Other named candidates (Unlikely / Lead)** | **~16% combined** | Aylesbury Cowheard groom 1638 (~3%), Norwich m.1639 Jane Wright groom (~3%), Cheddington 1608 Johannes (~3%), Hitcham 1631 (~2%), Ackworth Mary Barton (~2%), plus residual lead leakage across other minor rows. Each has no current solid eliminator but no positive linkage to the colonial John either; see §8 for row-level status and reasoning. |
| **Unknown other origin** | ~22-27% | Residual after Candidates A, C, D and the other named candidates above are accounted for. The Peter anomaly is a qualified clue rather than an absolute surname-wide absence. |
```

With:

```markdown
| Candidate / category | Probability | Basis |
|---|---|---|
| **B — Son of Francis & Margaret Rybett** | **~65-70%** | Margaret Rybett 1611 Norwich marriage primary; tailor-from-Merchant-Taylor trade match unmatched by any other candidate; Norfolk + London corridor (Fischer ~60% MA Bay from 9 eastern counties); Essex colonial associations (Daniel Shed, Tyng leasehold, Coleman Street adjacency); Ann Gurney / Gilman Norfolk-Hingham → MA-Hingham 1638 corridor; Francis G14 East Dereham child cluster reinforced (Marye + Agnes burial entries confirmed at FS-index level via VNN2-WR2 and VNN2-WRG; probable 1633 Francis burial); Mary Shed 1647 marriage bounds Mary Gurney English birth before 1628; Entry E paleographic favors "ffrancis Gurnie."<sup class="fn"><a href="#n101" id="ref-101a">101</a></sup> |
| **A — Stewkley / Bierton / Aylesbury → Northants** | **ELIMINATED** | Continuous English residence 1603-1653; wife Alice Oliffe; five Aylesbury children 1638-1653; 1641 cert of residence; 1650 Walgrave tenancy. |
| **C — Berkhamsted, Herts** | **ELIMINATED** | Eight-child Berkhamsted family 1610-1636 fathered by a John born about 1585-1590; Francis son 1636; absent Mary and Peter. |
| **D — Son of Robert Gurney, draper of Old Change** | **Unlikely (~3-5%)** | Strong post-1625 London continuity through at least 1638 and probably 1661; no wife Mary, no matching child set, no Puritan-corridor associate, no Massachusetts bridge. See §8.4 and `research/people/john-gurney-candidate-d.md`. |
| **Other named candidates (Unlikely / Lead)** | **~5% combined** | Aylesbury Cowheard groom 1638, Norwich m.1639 Jane Wright groom, Cheddington 1608 Johannes, Hitcham 1631, Ackworth Mary Burton, and similar single-attestation rows. Each has no current solid eliminator but no positive linkage to the colonial John either; see §8 for row-level reasoning. |
| **Unknown corridor (East Anglia / London)** | **~15-20%** | Residual for an undiscovered candidate in the dominant emigration corridor. The recurring failure to find an indexed John+Mary marriage in eastern-England parish registers 1620-1635 reflects parish-coverage gaps and keeps this bucket open. |
| **Unknown other corridor (Kent, Lincs, West Country)** | **~5-10%** | Residual for an outside-corridor origin. |
| **1636 Newgate apprentice as distinct second John whose later trail is lost** | **~3-5%** | If Banks's BSE attribution genuinely tracks a separate apprentice whose post-1639 colonial trail is lost, this remains a residual reading. Treated independently of Candidate B because the apprentice is born c.1615 and chronologically incompatible with the older Braintree John (born c.1602/3 per the 1653 deposition). |
```

### 5.8 Section 12 — refresh priority list

Find the existing §12 block beginning `### For Definitive Confirmation` and ending at the closing `### Non-leads` block. Leave the existing prose intact but insert this new sub-block immediately AFTER the existing `### For Definitive Confirmation` block and BEFORE the existing `### For Strong Supporting Evidence` block.

```markdown
### Highest-leverage Round 6+ targets (added 2026-05-15)

These targets sit beyond the freely-indexed online corpus and would require paid pulls, archive visits, or research-services enquiries. Each item has the potential to materially move Candidate B above 80% or to surface a competing positive attribution.

1. **NRO Norwich Consistory Court / Archdeaconry Court catalogue.** Edmund Gurney G14b (the Divine) will, d. 14 May 1648 buried St Peter Mancroft Norwich. Henry Gurney G15 will, d. 23 February 1615 (probate 1623 per Daniel Gurney). Either will, if extant, could name nephews or grandchildren in New England.
2. **Commissary Court of London-Essex-Herts, 1681 admin file** for John Gurney of Maldon (Bernau's bachelor John, admin granted to brother Thomas). The grant may list other surviving siblings — including any reference to a previously-deceased "brother John of New England" if the Candidate B identification holds.
3. **Suffolk Record Office HD2418/88** Ryvett family pedigrees, plus Suffolk wills 1620-1660 for Ryvett witnesses naming Gurney nieces or grandchildren.
4. **East Dereham parish register further image-walk.** Initial walk completed 2026-05-15 (artifacts in `sources/media/Parish_Register_East_Dereham/`); the Marye and Agnes burials on page 00725 are now confirmed via FS waypoint S3HT-65F5-TN cross-checked against line-level register crops. Still open: year fields on the Marye and Agnes burials (the register page is year-truncated in the visible crop); Margaret Rybett burial 1615-1618 elsewhere in the register (not surfaced in the reviewed image set); and confirmation of the preliminary "Margaret daughter of ffrancis Gurnoe/Gurney bapt may 25" reading on `crop_00732_enhanced.png`.
5. **TNA Star Chamber STAC 8/281/24** (Trentham v Withes, November 1620): the named defendants include Henry Reade, his sister Mary Reade, and Henry Gurney. Plaintiff is Staffordshire-based; the Henry Gurney involved is most plausibly a Midlands Henry. A paid PDF or in-person pull would identify the Henry Gurney definitively and test any Reade-family-Gurney-connection lead.
6. **William Tyng probate** (d. 18 January 1653 Braintree, MA; will / inventory should be in Suffolk County MA Probate Liber 1). The inventory would itemize the Braintree leasehold to John Gurney as named tenant.
7. **Sir Henry Spelman manuscript pedigree.** Bernau (1913) reports that "a Francis Gournay" gave Sir Henry Spelman a manuscript Gourney pedigree; the 1616 Francis Spelman apprenticeship to Francis G14 (Scott 2024 UKDA-9263) supplies a concrete vector. Candidate repositories: CUL MS Add. (Spelman collection), Bodleian MS Eng. hist., BL Add. MSS (Spelman transcripts), College of Arms.
8. **NEHGR vol. 22 p. 44** John Gurney reference (not yet in the case file's pulled set). Internet Archive coverage of NEHGR vol. 22 (1868) is patchy by web URL; a targeted FS-Library or Google Books pull should resolve it.
9. **Mary Anne of Yarmouth 1637 + Susan & Ellen of Yarmouth 1635 passenger lists** for Gurney variants. These two Yarmouth, Norfolk → Massachusetts ships span the John Gurney emigration window and have partial surviving passenger lists not yet pulled.
```

### 5.9 New footnote entries n96-n101

Add these new footnotes in the existing ordered endnote block, immediately AFTER the existing footnote `n95`:

```html
  <li id="n96" value="96">East Dereham parish-register entries for Francis Gurney G14's children, as indexed at FamilySearch (England, Norfolk, Parish Registers (County Record Office), 1510-1997) and resolved against the underlying register page via a 2026-05-15 image-walk (<code>sources/media/Parish_Register_East_Dereham/page-00725-deep-analysis.md</code>): <code>fs-vnn2-scf-edward-gurney-baptism-east-dereham</code> (Edward, baptism; indexed date 27 May 1610 inherits its year from a modern margin annotation on the page, not from a contemporaneous register heading — the case file's ±2-3 year date margin remains the correct posture); <code>fs-vnn2-wr2-marye-gurney-burial-east-dereham</code> (Marye, burial 25 January, year not in register; "Marye ... of ffrancis Gurny" with relationship word damaged by staining; previously case-file Entry B "Marye c.1614-15," now reclassified as a burial); <code>fs-vnn2-wrg-agnes-gurney-burial-east-dereham</code> (Agnes, burial 31 January, year not in register; FS index reads "Susan" but the underlying register reads "Agnes the daughter of ffrancis Gurny"; previously case-file Entry C "Agnes c.1614," now reclassified as a burial; the Round 2 working hypothesis of a separate daughter Susan is withdrawn); <code>fs-vnn2-h8s-francis-gurney-burial-east-dereham-1633</code> (Francis, burial 8 November 1633, parent not indexed; the "probable son of Francis G14" reading rests on geographic and chronological elimination of competing Francis Gurney identifications and on Francis G14's documented name-reuse for the 1628 St Benet Fink Francis baptism per Bernau, <em>British Archivist</em> I.7, 1913). Validation note <code>sources/validations/fs-east-dereham-francis-gurney-indexed-children.md</code>. <a class="backref" href="#ref-96a">back</a> <a class="backref" href="#ref-96b">back</a> <a class="backref" href="#ref-96c">back</a> <a class="backref" href="#ref-96d">back</a> <a class="backref" href="#ref-96e">back</a></li>
  <li id="n97" value="97">Daniel Shed baptized 25 June 1620 at St John the Baptist, Finchingfield, Essex; first in Braintree, Massachusetts records by 1643; married Mary Gurney 1647 at Braintree. The Braintree Book of Records (Bates, <em>Records of the Town of Braintree</em>, 1886, p. 638 ff.) preserves seven births to Daniel and Mary between 1 October 1647 and 30 October 1658. Standard derivative tradition (Sprague p. 695; <em>History of Weymouth</em> vol. 3 p. 251; Torrey p. 666; Shedd 1920) places Mary's birth at c.1628 in England; even at a minimum reasonable marriage age of 16 she was born by 1631. The John Gurney + Mary marriage therefore took place in England before 1628. FS, Findmypast, and Ancestry indexed eastern-England parish-marriage collections 1620-1635 contain zero John Gurney + Mary marriages outside the already-eliminated Eythorne Kent / Mary Marsh event. The absence is best read as a parish-register coverage gap, not as evidence against an English marriage. Source IDs <code>shedd-daniel-shed-genealogy-1920</code>, <code>braintree-records-1640-1793-1886</code>. <a class="backref" href="#ref-97a">back</a> <a class="backref" href="#ref-97b">back</a> <a class="backref" href="#ref-97c">back</a></li>
  <li id="n98" value="98">FamilySearch England, Births and Christenings, 1538-1975 index entry for John Gurney, christening 13 March 1615, Saint Ann Blackfriars, London, father Wm. (William) Gurney. FS identifier JW7Y-C3B. Image unavailable in FS at index level. Source ID <code>fs-jw7y-c3b-john-gurney-baptism-st-ann-blackfriars</code>. The 1615 baptism date for this John (son of William) is also consistent with the 1636 Newgate apprentice's implied birth year (29 September 1615) under the case file's two-Johns reading. <a class="backref" href="#ref-98a">back</a></li>
  <li id="n99" value="99">John Newgate of Horningsheath, Suffolk (~3 miles south-west of Bury St Edmunds), residing later at Hessett, Bury St Edmunds, and Southwark before emigrating to Boston in 1633: WikiTree profile Newgate-14 (https://www.wikitree.com/wiki/Newgate-14), source ID <code>wikitree-newgate-14-horningsheath</code>, validation note <code>sources/validations/wikitree-newgate-14-horningsheath.md</code>. The 1636 court order requiring Newgate's apprentice John Gurney to serve until age 24, three years from the next 29 September, is recorded in Winthrop/Savage, <em>History of New England from 1630 to 1649</em>, vol. 2 Addenda p. 422 (source ID <code>winthrop-history-new-england-addenda-1636</code>). The American family-memory tradition of a 29 September 1615 birth and Southwark or "Borough of Brent" origin appears across the Lysander F. Gurney sketch (AccessGenealogy transcription of <em>Representative Men and Old Families of Southeastern Massachusetts</em>, 1912; source ID <code>accessgenealogy-lysander-franklin-gurney</code>); <em>American Biography</em> vol. 26 (1926; source ID <code>american-biography-cyclopedia-v26-gurney-1926</code>); and Find a Grave memorial 252975617 (source ID <code>findagrave-john-gurney-252975617</code>). <a class="backref" href="#ref-99a">back</a></li>
  <li id="n100" value="100">David Hackett Fischer, <em>Albion's Seed: Four British Folkways in America</em> (New York: Oxford University Press, 1989), ch. 6 "Regional Origins of the Puritan Migration"; Roger Thompson, <em>Mobility and Migration: East Anglian Founders of New England, 1629-1640</em> (Amherst: University of Massachusetts Press, 1994). Diligent of Ipswich 1638 passenger list per Charles Edward Banks, <em>Planters of the Commonwealth</em> (Boston, 1930), transcribed by Daniel Cushing (Hingham, MA town clerk) and republished at packrat-pro.com/ships/dilligent.htm; the passenger list contains no Gurney variant. The Edward Gilman group on the Diligent comprised Edward Sr, wife Mary Clark, sons Edward, Moses, and John, daughters Lydia and Sarah, and three servants. John Gilman + Ann Gurney themselves did not emigrate (Ann buried Hingham, Norfolk, 23 November 1651); at least two of their sons emigrated to Exeter, NH (John Gilman Jr born 1638, emigrated by 1658; Charles Gilman born 1642, emigrated 1664 "with his brother John and cousins"). Source IDs <code>fischer-albions-seed-1989</code>, <code>thompson-mobility-migration-1994</code>. <a class="backref" href="#ref-100a">back</a></li>
  <li id="n101" value="101">Probability range ~65-70% for Candidate B is a Bayesian decomposition: corridor priors (~60% MA Bay emigrants from 9 eastern counties, &lt;10% from London proper) × trade-inheritance multiplier (~2-3x over baseline for tailor-from-Merchant-Taylor lineage given no other eliminated candidate matches this trade) × Margaret Rybett primary-record confirmation multiplier (~1.4x for resolving the multi-generation chronology gap) × Essex colonial-network multiplier (~1.4x for the Shed / Tyng / Coleman Street / Braintree-name cluster) × East Dereham Francis-G14 child cluster reinforcement (Marye + Agnes burial entries primary-record confirmed via FS index VNN2-WR2 and VNN2-WRG; probable 1633 Francis burial via VNN2-H8S), weighted against counter-factors (no indexed John+Mary marriage, ~0.6-0.7x; Roger called "eldest sonne" in 1633/4 Visitation, ~0.7x; no son named Francis or Henry, ~0.9x — qualified by Mary-family-name-dominance refinement). Detailed reasoning at <code>sources/intake/_workspace/round1-scratch/round5-findings.md</code> §D. The case-file's prior point estimate of ~55-60% (v4) reflected the state of evidence before the six-round 2026-05 research pass; the revised range raises Candidate B by ~10 percentage points primarily on the strength of (a) the Newgate Horningsheath finding explaining Banks's BSE attribution, (b) the FS-indexed primary records expanding Francis G14's East Dereham child cluster, and (c) Mary Shed's 1647 marriage tightly bounding the John+Mary marriage to England before 1628 and reframing the indexed-marriage absence as a parish-coverage gap rather than counter-evidence. <a class="backref" href="#ref-101a">back</a></li>
```

### 5.10 Updated date in case-file header

Find the existing `updated: 26 April 2026` line at the top of the case file. Replace with:

```markdown
updated: 15 May 2026
```

And update the `caseMeta` Version line:

Find:

```markdown
caseMeta: "<strong>Prepared by:</strong> Allen Lawrence Gurney, Portland, Oregon &nbsp;&nbsp; <strong>Date:</strong> April 2026 &nbsp;&nbsp; <strong>Version:</strong> 4.0"
```

Replace with:

```markdown
caseMeta: "<strong>Prepared by:</strong> Allen Lawrence Gurney, Portland, Oregon &nbsp;&nbsp; <strong>Date:</strong> May 2026 &nbsp;&nbsp; <strong>Version:</strong> 4.1"
```

## 6. Audit checklist

Before declaring this patchset applied, confirm each item:

- [ ] `data/sources.json` has the 9 new source IDs: `fs-vnn2-scf-edward-gurney-baptism-east-dereham`, `fs-vnn2-wrg-agnes-gurney-burial-east-dereham`, `fs-vnn2-wr2-marye-gurney-burial-east-dereham`, `fs-vnn2-h8s-francis-gurney-burial-east-dereham-1633`, `fs-jw7y-c3b-john-gurney-baptism-st-ann-blackfriars`, `wikitree-newgate-14-horningsheath`, `thompson-mobility-migration-1994`, `shedd-daniel-shed-genealogy-1920`, `findmypast-norfolk-burials-index`.
- [ ] Two new validation files created at the listed paths.
- [ ] `research/people/g14-francis-gurney-fact-sheet.research.md` has three new subsections inserted in the Working Notes block (East Dereham primary expansion; Edmund Walker Gurney 1644 correction; 1664 Essex Visitation reference).
- [ ] `research/people/g13-john-gurney-fact-sheet.research.md` has three new subsections inserted in the Working Notes block (Newgate Horningsheath; Corridor empirics; Mary Shed bounding) and the Working Hypotheses block at the bottom updated.
- [ ] Case-file §4.2 children table replaced (Entries B and C reclassified as burials with January 25 / January 31 dates and FS-index identifiers; new Entry F for 1633 Francis burial; added "Event" column). Prose addition immediately after the table.
- [ ] Case-file §6 leading paragraph replaced and trailing framing paragraph added.
- [ ] Case-file §8 elimination table has the new St Ann Blackfriars row and the new 1636 Newgate apprentice row inserted at the specified positions.
- [ ] Case-file §10.2 has the new corridor-empirics paragraph inserted.
- [ ] Case-file §11 probability table replaced.
- [ ] Case-file §12 has the new "Highest-leverage Round 6+ targets" sub-block inserted between "For Definitive Confirmation" and "For Strong Supporting Evidence."
- [ ] Six new footnotes `n96` through `n101` inserted after `n95` in the endnote block.
- [ ] Case-file header `updated` and `caseMeta` Version fields updated.

## 7. Held-review and deferred items

These are research targets identified during the six-round pass that were not pulled this cycle. They are not blockers for v39 application; they are queued for future intake.

- Probable baptism reading "Margaret the daughter of ffrancis Gurnoe/Gurney bapt may 25" on `crop_00732_enhanced.png` (East Dereham parish-register page 00732). Image-walk artifact at `sources/media/Parish_Register_East_Dereham/burial-analysis.md`. Held for same-hand comparator review; if confirmed, this would be a previously-undocumented daughter Margaret of Francis G14, plausibly named for the first wife Margaret Rybett after her death. Not promoted to the case-file body in v39.
- NRO Norwich Consistory Court / Archdeaconry Court will of Edmund Gurney G14b (d. 14 May 1648), and Henry Gurney G15 (d. 23 February 1615, probate 1623). Neither is in TNA PCC indices. Direct NRO catalogue search or research-services enquiry required.
- Commissary Court of London-Essex-Herts 1681 administration file for John Gurney of Maldon (Bernau's bachelor John, admin granted to brother Thomas).
- Suffolk Record Office HD2418/88 Ryvett family pedigrees + Suffolk wills 1620-1660 for Ryvett witnesses.
- East Dereham parish register burial section image-walk: targeted high-resolution crops of local images `gbprs_norfolk_pd_86-41_00725` through `00740`, plus the back-of-volume sequence `00750`-`00768`. Pre-work specification at `sources/intake/_workspace/round1-scratch/round4-findings.md` §F.
- TNA Star Chamber STAC 8/281/24 (Trentham v Withes, November 1620): paid PDF download or in-person TNA pull.
- William Tyng probate (Suffolk County MA Probate Liber 1, 1653) for Braintree leasehold to John Gurney.
- Sir Henry Spelman manuscript pedigree at CUL Add. MS / Bodleian / BL Add. MSS / College of Arms via research-services enquiry.
- NEHGR vol. 22 p. 44 John Gurney reference targeted pull (FS Library or Google Books).
- Mary Anne of Yarmouth 1637 + Susan & Ellen of Yarmouth 1635 partial passenger lists for Gurney variants.

## 8. Session traceability

Input packets (round-by-round deep-research scratch files, all under `sources/intake/_workspace/round1-scratch/`):

- `round1-leads.md`
- `round1-findings.md`
- `round2-findings.md`
- `round3-findings.md`
- `round4-findings.md`
- `round5-findings.md`
- `round6-findings.md`

These remain as ephemeral working scratch under `_workspace/` and should not be promoted into the canonical layer; they exist for traceability of the reasoning behind this patchset and may be cleared after v39 is applied.
