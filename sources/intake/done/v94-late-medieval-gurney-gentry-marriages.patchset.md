**Done:** 2026-06-14 07:18 PT

# Patchset v94 â€” Late-medieval Gurney gentry marriages (Calthorpe 1494, L'Estrange 1505)

**Phase 1 prepared 2026-06-13.** Promotes two new, image-confirmed documentary findings from
the Bradfer-Lawrence "Norfolk wills extracts, 1370â€“1763" sweep (see
`sources/intake/new/2026-06-13-familysearch-browser-link-triage/will-abstract-sweep-results.md`):
a Gurney married a daughter of Sir William Calthorpe (will d. 1494) and a Gurnay married a
sister of Sir Roger L'Estrange (will pr. 1505). Both abstracts are typed (clean OCR) and
were read against full-resolution page images. They establish two new Gurneyâ†”top-gentry
marriages in the G18â€“G20 window; the Gurney's forename is not in either abstract (open
question â†’ lead L-122).

Outcome for both items: **promote.** Destination: the existing topic file
`research/topics/gurney-heraldry-and-pedigree-evidence-g17-g28.md` (the marriage-network
layer, where the G18 Heydon/L'Estrange context already sits), not a single ancestor companion,
because the specific Gurney is unidentified.

Sibling findings from the same sweep are sequenced to later patchsets: Smith of Great
Massingham 1643 (Edmund the Divine + "Ellen") â†’ next; the Walter Rye "Gurneys of Norwich"
essay and medieval Rye-calendared Gurnay deeds (leads L-118â€“L-121) remain leads pending
reading. The Spilman 1524 abstract from the same volume is already promoted (G17 companion,
`spilman-1524`).

---

## Action 1 â€” add sourceId `norfolk-wills-extracts-bradfer-lawrence` to `data/sources.json`

`str_replace` in `data/sources.json`:

**old_string:**
```
      "validationPath": "sources/validations/familysearch-fulltext-search.md",
      "notes": "Keyword search across AI-transcribed images. 2026-05-29 'Francis Gurnay' pass corroborated Francis Gurney of Maldon (Maldon borough Employment/freemen 1661-1688 'merchant and salt refiner, born in London'; Account Records 1624-1678; Court Records) and surfaced Burke's Landed Gentry 1858 Gurney pedigree plus three FamilySearch-Center-restricted records (Kent Probate 1633-36; St Peter le Poer w/ St Benet Fink Poor Rate; Norfolk History Records 1701, 1825). Machine transcriptions; verify against the image before quoting."
    },
    "may-henry-gurney-spenser-2005": {
```

**new_string:**
```
      "validationPath": "sources/validations/familysearch-fulltext-search.md",
      "notes": "Keyword search across AI-transcribed images. 2026-05-29 'Francis Gurnay' pass corroborated Francis Gurney of Maldon (Maldon borough Employment/freemen 1661-1688 'merchant and salt refiner, born in London'; Account Records 1624-1678; Court Records) and surfaced Burke's Landed Gentry 1858 Gurney pedigree plus three FamilySearch-Center-restricted records (Kent Probate 1633-36; St Peter le Poer w/ St Benet Fink Poor Rate; Norfolk History Records 1701, 1825). Machine transcriptions; verify against the image before quoting."
    },
    "norfolk-wills-extracts-bradfer-lawrence": {
      "shortTitle": "Norfolk wills extracts, 1370-1763 (Bradfer-Lawrence)",
      "citation": "Norfolk wills extracts, 1370-1763, from the Bradfer-Lawrence collection (typescript abstracts of Norfolk Record Office wills; GSU microfilm, 6 reels). FamilySearch catalog koha:1056823; surname-ordered DGS films 008100792, 008480297, 008176838, 008480296, 008085264, 008480295.",
      "archive": "Norfolk Record Office (originals); FamilySearch International (GSU microfilm / Full-Text Search)",
      "url": "https://www.familysearch.org/search/catalog/koha:1056823",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": "sources/media/norfolk-wills-extracts-bradfer-lawrence/",
      "validationPath": "sources/validations/norfolk-wills-extracts-bradfer-lawrence.md",
      "notes": "Typed will-abstract series; clean OCR (unlike manuscript registers). Each entry abstracts one will and cites its source register. Swept for Gurney variants 2026-06-13 (Gurn*/Gourn*/Gorn*, all reels except 008100792 which is not FTS-indexed). Distinct from the generic 'familysearch-fulltext-search' handle; the G17 companion's spilman-1524 and wymondham-1475 footnotes cite the same volume and may be re-aligned to this sourceId in a later cleanup."
    },
    "may-henry-gurney-spenser-2005": {
```

## Action 2 â€” new validation worksheet (thin)

`new file write` â†’ `sources/validations/norfolk-wills-extracts-bradfer-lawrence.md`:

```markdown
# Validation â€” Norfolk wills extracts, 1370-1763 (Bradfer-Lawrence)

**Source:** `norfolk-wills-extracts-bradfer-lawrence` (`data/sources.json`). Typescript
abstract series, 6 surname-ordered reels; FamilySearch catalog koha:1056823.

**Examined:** Gurney-variant Full-Text sweep of all six reels, 2026-06-13
(`Gurn* Gourn* Gorn*`, count=100). Five reels FTS-indexed and returned complete result
sets; reel 1 (DGS 008100792, surnames Aldrychâ€“Bedingfeld) is **not FTS-indexed** (a `wife`
probe also returns zero) and is unsearched. Full-resolution page images read for the two
folios promoted in patchset v94:
- Sir William Calthorpe, d. 1494 â€” DGS 008480297, image 489 (NCC reg. Wolman 213) and image 490 (PCC reg. Vox 23).
- Sir Roger L'Estrange, pr. 1505 â€” DGS 008480295, image 251 (PCC reg. Adeane 2).

**Remains / uncertain:** reel 1 unsearched; the underlying full wills (NCC/PCC registers)
not yet pulled, so the Gurney forenames are unknown (lead L-122). Other Gurney hits from the
sweep (Smith of Gt Massingham 1643; moderate one-liners L-123) await later patchsets.

**Findings recorded in:** `research/topics/gurney-heraldry-and-pedigree-evidence-g17-g28.md`
(Calthorpe 1494 and L'Estrange 1505 marriages). Page images:
`sources/media/norfolk-wills-extracts-bradfer-lawrence/`. Execution trail: patchset
`sources/intake/done/v94-late-medieval-gurney-gentry-marriages.patchset.md`.
```

## Action 3 â€” promote into the topic file

`str_replace` in `research/topics/gurney-heraldry-and-pedigree-evidence-g17-g28.md` (insert the new section before Recommendations):

**old_string:**
```
6. **Image evidence:** the Daniel Gurney image extraction catalog already contains the key visual assets for pp. 279, 283, 284, 319, 321, 415, 418, 446, and 448.[^images]

## Recommendations
```

**new_string:**
```
6. **Image evidence:** the Daniel Gurney image extraction catalog already contains the key visual assets for pp. 279, 283, 284, 319, 321, 415, 418, 446, and 448.[^images]

## Late-medieval gentry marriages â€” Calthorpe (1494) and L'Estrange (1505)

Two contemporary wills place a Gurney, by marriage, inside the front rank of late-medieval Norfolk gentry in the G18â€“G20 window â€” reinforcing the marriage-network layer that the Heydon match at G18 already signals.

**Sir William Calthorpe of Burnham Thorpe (d. 1494)** named a Gurney son-in-law among his executors. The Prerogative Court of Canterbury copy of his will abstracts as:

> Sir William Calthorp, Knt â€” to be buried in the Church of the Whyte Friers in Norwich. Wife Dame Elizabeth. Cousin Philip. Sons, Francis, William, Edward; **Gurney and my dr [daughter] his wife**. Francis Hasilden and my dr his wife under 21. Robert Glore Esq. Walter Aslache Gent. Servant John Hasilden Esq. Dame Sibell Lowes. Master Richard Regill. (d: 31 May 1494. (P: 23 May 1495.)

A daughter of Sir William Calthorpe â€” one of the great Norfolk knightly families of the period â€” had therefore married a Gurney before 1494, and that Gurney son-in-law was trusted enough to act as an executor (the Norwich Consistory copy adds him, with Walter Aslak, administering money for building the choir and presbytery at an abbey).[^calthorpe-1494]

**Sir Roger L'Estrange of Hunstanton** (will proved 7 October 1505), directing burial in Hunstanton chancel, named a Gurnay among his sisters:

> P.C.C. Adeane: 2. ROGER LESTRANGE Knt. to be buried in Hunstanton Chancel â€” sister Heydon, Mrs. Townsend, sister Ann, sister Margaret, **sister Gurnay**. (P: 7 Oct 1505.)

A L'Estrange daughter had thus married a Gurnay by 1505 â€” a kinship distinct from the Gurney service relationship to the L'Estranges already documented in Daniel Gurney's printed Hunstanton household accounts.[^lestrange-1505]

Both abstracts give the Gurney **surname only**, so the husband's forename is unresolved. The two marriages sit in the documented Gurneyâ€“Heydonâ€“Calthorpeâ€“L'Estrangeâ€“Townshendâ€“Lovell cousinage that the G17 line's Lovell/Spelman/Conyers connections already run through; whether the Calthorpe and L'Estrange husbands are West Barsham direct-line Gurneys (G18 William Gurney V is here recorded married to Anne Heydon), their brothers, or near collaterals is the open question. Pulling the two full wills for the forenames is the resolving step (lead L-122).[^calthorpe-1494][^lestrange-1505]

## Recommendations
```

`str_replace` in the same file (add the two footnote definitions after `[^images]`):

**old_string:**
```
[^images]: `sources/corpus_images/daniel_gurney_extracts/30April2026/daniel_gurney_image_extract_v4_combined/part2_norfolk_line/catalog/daniel_gurney_part2_norfolk_line_image_catalog.md`.
```

**new_string:**
```
[^images]: `sources/corpus_images/daniel_gurney_extracts/30April2026/daniel_gurney_image_extract_v4_combined/part2_norfolk_line/catalog/daniel_gurney_part2_norfolk_line_image_catalog.md`.
[^calthorpe-1494]: Will of Sir William Calthorpe, knight, of Burnham Thorpe, dated 31 May 1494, proved 23 May 1495, naming a Gurney son-in-law ("Son Gurney â€¦ and my dr his wife") executor; abstracted in *Norfolk wills extracts, 1370â€“1763* (Bradfer-Lawrence collection, typescript), at the Norwich Consistory Court register Wolman 1488â€“96, fol. 213 (FamilySearch film 008480297, image 489, [ark:/61903/3:1:3Q9M-C39V-FS5W-X](https://www.familysearch.org/ark:/61903/3:1:3Q9M-C39V-FS5W-X?view=fullText)) and the Prerogative Court of Canterbury register Vox, fol. 23 (image 490, [ark:/61903/3:1:3Q9M-C39V-FSPJ-W](https://www.familysearch.org/ark:/61903/3:1:3Q9M-C39V-FSPJ-W?view=fullText)). Page images: `sources/media/norfolk-wills-extracts-bradfer-lawrence/`. Source ID: `norfolk-wills-extracts-bradfer-lawrence`.
[^lestrange-1505]: Will of Sir Roger L'Estrange, knight, of Hunstanton, proved 7 October 1505 (Prerogative Court of Canterbury register Adeane, fol. 2), naming "sister Gurnay" among his sisters; abstracted in *Norfolk wills extracts, 1370â€“1763* (Bradfer-Lawrence collection, typescript), FamilySearch film 008480295, image 251, [ark:/61903/3:1:3Q9M-C39V-KLZH](https://www.familysearch.org/ark:/61903/3:1:3Q9M-C39V-KLZH?view=fullText). Page image: `sources/media/norfolk-wills-extracts-bradfer-lawrence/`. Source ID: `norfolk-wills-extracts-bradfer-lawrence`.
```

## Action 4 â€” durable media home

Copy the three full-resolution abstract images from the intake folder into a new
per-sourceId media folder (public-domain typed abstracts, <35 MB â†’ committed normally):

- `sources/intake/new/2026-06-13-familysearch-browser-link-triage/images/sweep-calthorpe-1494-ncc-wolman213-FS5W-img489.jpg` â†’ `sources/media/norfolk-wills-extracts-bradfer-lawrence/calthorpe-1494-ncc-wolman213-img489.jpg`
- `sources/intake/new/2026-06-13-familysearch-browser-link-triage/images/sweep-calthorpe-1494-pcc-vox23-FSPJ-img490.jpg` â†’ `sources/media/norfolk-wills-extracts-bradfer-lawrence/calthorpe-1494-pcc-vox23-img490.jpg`
- `sources/intake/new/2026-06-13-familysearch-browser-link-triage/images/sweep-lestrange-1505-pcc-adeane-KLZH-img251.jpg` â†’ `sources/media/norfolk-wills-extracts-bradfer-lawrence/lestrange-1505-pcc-adeane-img251.jpg`

`new file write` â†’ `sources/media/norfolk-wills-extracts-bradfer-lawrence/README.md`:

```markdown
# Norfolk wills extracts, 1370-1763 (Bradfer-Lawrence) â€” page images

Working-reference page images from the typescript will-abstract series (sourceId
`norfolk-wills-extracts-bradfer-lawrence`). Captured 2026-06-13 via the FamilySearch
das/v2 full-resolution API. Findings in
`research/topics/gurney-heraldry-and-pedigree-evidence-g17-g28.md`.

- `calthorpe-1494-ncc-wolman213-img489.jpg` â€” Sir William Calthorpe will abstract, NCC reg. Wolman 213 (DGS 008480297, img 489, ark 3:1:3Q9M-C39V-FS5W-X).
- `calthorpe-1494-pcc-vox23-img490.jpg` â€” same will, PCC reg. Vox 23 copy (DGS 008480297, img 490, ark 3:1:3Q9M-C39V-FSPJ-W).
- `lestrange-1505-pcc-adeane-img251.jpg` â€” Sir Roger L'Estrange will abstract, PCC reg. Adeane 2 (DGS 008480295, img 251, ark 3:1:3Q9M-C39V-KLZH).
```

## Source tracking

- New sourceId `norfolk-wills-extracts-bradfer-lawrence` (Action 1) â†’ validation worksheet created (Action 2), per default-on discipline.
- No `corpus_supplement` file needed: both abstracts are short (<150 words) and land verbatim as fenced quotes in the topic file (Action 3), per the README's short-quotation rule.

## Phase 2 completion

After Actions 1â€“4, prepend `**Done:** YYYY-MM-DD HH:MM PT` and move this file to
`sources/intake/done/`.
