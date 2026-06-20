# Search Variants Review — Surname Foundation

**Date:** 2026-06-19  
**Status:** Approved and implemented in `data/search-variants.json` and
`tools/repo_search.py`

## Purpose

Establish an evidence-based, human-reviewable surname-variant model before
expanding the registry to given names or other terms. This review compares:

1. canonical direct-ancestor names in `data/ancestors.json`;
2. lineage eras in that file;
3. forms actually present in fact sheets, research companions, and source
   material; and
4. the way `tools/repo_search.py` currently applies variants.

Occurrence counts below establish repository presence, not genealogical
identity. A form can appear because it is an attested spelling, an OCR error, a
place-name, an explicitly rejected comparator, or a discussion of variants.

## Canonical direct-line surname by repository era

| Repository era | Generations | Canonical direct-line forms | Initial interpretation |
|---|---:|---|---|
| Modern America | G1–G3 | Gurney | Stable canonical spelling |
| Gilded Age and Civil War | G4–G6 | Gurney | Stable canonical spelling |
| Early Republic | G7 | Gurney | Stable canonical spelling; `Gurnee` occurs in supporting research but requires record-level review |
| Massachusetts farming generations | G8–G12 | Gurney | Canonical spelling; historical/index variants occur, especially around the Benjamin cluster |
| Emigrant and colonial Massachusetts | G13 | Gurney | Variant-rich discovery environment; many forms are candidate/comparator spellings rather than proven aliases |
| Tudor England | G14–G18 | Gurney; G15 canonically Gurnay | Genuine transition zone among Gurney, Gurnay, and Gournay |
| Medieval Norfolk Gurneys | G19–G23 | Gurney at G19; Gournay at G20–G23 | Transition from Gournay toward Gurney is visible in canonical records |
| Junior Norfolk branch | G24–G31 | de Gournay / Gournay | Stable medieval canonical form, with Latin and documentary variants |
| Norman barons of England | G32–G36 | de Gournay / Gournay | French, Latin, and Anglo-Norman forms are source/language dependent |
| Viking origin | G37 | de Gournay | Retrospective territorial surname; given-name variants are also important |
| End of known record | G~38+ | none | No surname expansion should be inferred |

The ancestor index is useful as the compact locator, but the canonical name and
era come from `data/ancestors.json`. The ancestor JSON has no dedicated alias or
name-variant field at present.

## Current `surname-gurney` set

Whole-token counts exclude `site/`, `tools/`, media, and the variant file
itself. Counts include historical intake material and therefore should not be
treated as independent confirmations.

| Current term | Whole-token hits / files | Current profile | Review assessment |
|---|---:|---|---|
| Gurney | 25,891 / 715 | conservative | Canonical key; should not also be stored as its own variant |
| Gournay | 13,648 / 389 | conservative | Keep; core medieval/Norman form, but place-name collisions require entity-aware ranking |
| Gurnay | 2,647 / 236 | conservative | Keep; G15 is canonically `Gurnay`, with strong medieval/Tudor use |
| Gourney | 1,622 / 193 | conservative | Attested, but likely too permissive as a global conservative expansion |
| Gurny | 892 / 109 | conservative | Attested/indexed form; better as era-scoped or broad rather than global conservative |
| Gurnie | 97 / 40 | conservative | Possible historical/index form; broad and scoped pending record review |
| de Gournay | phrase subset of Gournay | conservative | Keep as medieval phrase form, not as a freestanding global synonym |
| de Gurnay | phrase subset of Gurnay | conservative | Keep as medieval phrase form |
| Gernay | 2 / 2 | broad | Insufficient evidence for automatic expansion |
| Gernays | 23 / 12 | broad | Appears mainly in pre-Lovell/collateral discussion; likely lead-only, not a direct-line alias |
| Gornay | 162 / 40 | broad | Keep in a medieval documentary/Latin-French set |
| Gorney | 230 / 43 | broad | Do not globally expand: repo validation explicitly identifies `Gorney` as a distinct surname in Norfolk/Norwich work |
| Gurne | 142 / 31 | broad | Attested in Costessey material, but ambiguous; whole-token and early-modern scope are mandatory |
| Gourne | 3 / 3 | broad | Remove unless primary evidence is identified |
| Gvrney | 20 / 10 | broad | Keep only as early-modern transcription/index confusion, whole-token matched |

## Important missing candidates

| Candidate | Whole-token hits / files | Preliminary treatment |
|---|---:|---|
| Gurnaye | 60 / 9 | Add to medieval/Tudor documentary forms after checking the Daniel Gurney passages |
| Gournai | 140 occurrences in core corpus/research scan | Add to Old French/medieval source forms |
| Gornai | 40 occurrences in core corpus/research scan | Add to Old French/medieval source forms |
| Gornaco | 103 occurrences in core corpus/research scan | Add to a Latin inflection family, not as a universal English surname alias |
| Gornaio | 102 occurrences in core corpus/research scan | Add to a Latin inflection family |
| Gornacensis | 38 whole-token repository hits | Add to medieval Latin/scholarly sources |
| Gurnee | 58 / 18 | Review as an American/index form; do not assume every Gurnee is the same surname |
| Gerney | 13 / 9 | Broad/index-only pending evidence |
| Girney | 34 / 12 | Broad/index/transcription-only pending evidence |
| Gyrney | 2 / 2 | Broad/index/transcription-only pending evidence |
| Gurnoe | 193 / 28 | Likely comparator/distinct surname in important G13 work; exclude from automatic expansion unless a specific source proves an alias |
| Gourny | 19 / 14 | Medieval/index candidate; source review needed |
| Gourneye | 25 / 12 | Medieval documentary/OCR candidate; source review needed |
| Gerny, Gerneye, Gurnney | 1–2 files each | Do not automate without underlying record evidence |

## Tool behavior corrected during implementation

1. Generation ranges now select `Modern`, `English`, or `Norman`.
2. `sourcePaths` restrict source-specific OCR retrieval.
3. Surname forms use whole-token matching; territorial forms use phrase
   matching.
4. The former global surname set has been replaced by three families.
5. Collision-prone broad candidates generate manifest warnings.

## Proposed v2 organization — three name-variant families

This simpler three-family model is the current proposal for review. Neighboring
generations deliberately share the same family so searches remain predictable.

| CLI name | Generations | Search environment |
|---|---:|---|
| `Modern` | G1–G13 | Modern American, colonial, and Massachusetts records |
| `English` | G14–G28 | Tudor and medieval English records, including the Gurney/Gurnay/Gournay transition |
| `Norman` | G29–G37 | Norman, Old French, Latin, charter, and cross-Channel records |
| `All` | G1–G37 | Union of all three families, only when explicitly requested |

For ancestor searches, `--name-variants auto` should infer the family from the
generation. Explicit searches should permit:

```text
--name-variants modern|english|norman|all|none
--variants conservative|broad
```

`broad` is cumulative: it contains every conservative form plus the broad
additions shown below.

### Proposed review matrix

| Name-variant family | Conservative | Broad additions |
|---|---|---|
| **Modern — G1–G13** | `Gurney`, `Gurnay`, `Gourney`, `Gurny`, `Gurnie`, `Gurnee` | `Gurne`, `Gvrney`, `Gerney`, `Girney`, `Gyrney`, `Gurnoe`, `Gorney`, `Gurnney` |
| **English — G14–G28** | `Gurney`, `Gurnay`, `Gournay`, `de Gurnay`, `de Gournay`, `Gourney`, `Gurnaye`, `Gornay` | `Gurny`, `Gurnie`, `Gurne`, `Gvrney`, `Gerney`, `Gernay`, `Gernays`, `Gerny`, `Gerneye`, `Girney`, `Gyrney`, `Gorney`, `Gurnoe`, `Gourny`, `Gourne`, `Gourneye`, `Gournai`, `Gornai`, `Gurnney` |
| **Norman — G29–G37** | `Gournay`, `de Gournay`, `Gurnay`, `de Gurnay`, `Gurney`, `Gornay`, `Gournai`, `Gornai`, `Gurnaye` | `Gourney`, `Gurny`, `Gurne`, `Gourny`, `Gourne`, `Gourneye`, `Gernay`, `Gernays`, `Gerny`, `Gerneye`, `Gorney`, `Gournat`, `Gournayy`, `Gurnye`, `Gurno`, `Gornaco`, `Gornaio`, `Gornacensis`, `Gornacum`, `Gornaium`, `Gornaii`, `Gornaci`, `Gornayo`, `Gorniaco`, `Gurnaco`, `Gurnaio` |

### Interpretation of the matrix

- The canonical form is included in each conservative list so the selected
  family is self-contained.
- `de Gournay` and `de Gurnay` are phrase forms; they should not be decomposed
  into a generic search for `de`.
- Latin forms such as `Gornaco`, `Gornaio`, and `Gornacensis` are grammatical
  source forms, not English surname spellings.
- `Gorney` and `Gurnoe` are useful broad discovery candidates but often identify
  distinct surnames. Their use should generate collision warnings.
- Sparse forms such as `Gerny`, `Gerneye`, and `Gurnney` remain broad because
  they occur in the repository but have little independent support.
- `Gournat`, `Gournayy`, `Gurnye`, and `Gurno` are retained only in the Norman
  broad family as rare documentary or OCR candidates.
- Source-specific OCR corrections such as `Wilham` and `Basiha` remain separate
  from surname families and must obey their source-path restrictions.

Each variant should eventually support:

- a `nameVariantFamily` and generation bounds;
- `matchMode` (`whole-token`, `phrase`, or deliberately `substring`);
- `autoExpand` level (`conservative`, `broad`, `manual-only`, `exclude`);
- source or path restrictions where applicable;
- language;
- evidence note and, ideally, one or more repository evidence paths;
- ambiguity/collision note.

## Recommended next review sequence

1. Review and approve or amend the three-family matrix.
2. Revise the JSON schema and tool behavior together.
3. Enforce whole-token, phrase, generation, and source-path behavior.
4. Add collision warnings for ambiguous broad candidates.
5. Add a Markdown/table display command so routine review does not require
   reading raw JSON.
