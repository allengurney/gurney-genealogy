**Done:** 2026-06-14 07:18 PT

# Patchset v97 â€” Edmund and Ellen Gurnay in the 1643 Smith of Great Massingham will

<!-- Numbered v97 (v95 = the parallel berney-gunton/edmund-acad patchset, v96 = pre-Lovell collaterals). NB: patchset v95 also edits research/people/edmund-gurney-divine.research.md (its Edmund ACAD item); the two edits target different anchors. The only contention is the end-of-file footnote append â€” see Action 1's footnote step. -->


**Phase 1 prepared 2026-06-13.** Promotes one finding from the Bradfer-Lawrence will-extracts
sweep: the will of William Smith of Great Massingham (d. 1643, pr. 1645) names "Edm: Gurnay"
and "Ellen Gournay" as a couple. Great Massingham adjoins Harpley, where Edmund Gurnay the
divine held the rectory, and his DNB-attested wife was named Ellen â€” so this is a very probable
independent corroboration of the wife Ellen and the first dated sighting of her (alive 1643)
outside the DNB notice.

Outcome: **promote** into `research/people/edmund-gurney-divine.research.md`. Uses the sourceId
`norfolk-wills-extracts-bradfer-lawrence` added in patchset v94 (apply v94 first).

---

## Action 1 â€” promote into the Edmund Gurnay research file

`str_replace` in `research/people/edmund-gurney-divine.research.md` (insert the new section after the Protestant working-facts table, before the Education section):

**old_string:**
```
| Parentage | Apparently Edmund's son | DNB cautious; needs register / monument validation |

## Education and academic career
```

**new_string:**
```
| Parentage | Apparently Edmund's son | DNB cautious; needs register / monument validation |

## Edmund and Ellen Gurnay named in the 1643 Smith of Great Massingham will

An independent contemporary record corroborates the wife's name Ellen and dates the couple alive together in 1643. The will of **William Smith, esquire, of Great Massingham** â€” the parish adjoining Harpley, where Edmund held the rectory â€” names, after Smith's own wife Martha and brother, "Edm: Gurnay" and "Ellen Gournay" as a paired couple. The will is dated 19 June 1643 and was proved 19 August 1645 (Norwich Consistory Court, 1644â€“5 register, fol. 215).[^smith-massingham-1643]

The identification with Edmund Gurnay the divine (d. May 1648, rector of Harpley) and his wife Ellen is very probable rather than certain: the forename pair Edmund + Ellen matches the household DNB attests exactly, and Great Massingham lies about five miles from Harpley.[^dnb-edmund] If correct, the entry independently confirms the wife Ellen that DNB reports and newly places her alive in 1643 â€” the first dated sighting of her outside the DNB notice â€” alongside a documented tie to the Smith family of Great Massingham. A different Edmund Gurnay of the wider Norfolk family cannot be fully excluded without the will body, which would also fix the relationship in which the Gurnays are named.

## Education and academic career
```

`str_replace` in the same file (append the footnote after the final footnote definition):

**old_string:**
```
[^thoms-anecdote]: Thoms, ed., <em>Anecdotes and Traditions</em> (1839), p. 6, no. XI, "A Mathematician Defined," from L'Estrange no. 30, with Fuller's account of Edmond Gourney. [Internet Archive](https://archive.org/details/anecdotestraditi00thomrich/page/6/mode/1up). Source ID: `thoms-anecdotes-traditions-1839`.
```

**new_string:**
```
[^thoms-anecdote]: Thoms, ed., <em>Anecdotes and Traditions</em> (1839), p. 6, no. XI, "A Mathematician Defined," from L'Estrange no. 30, with Fuller's account of Edmond Gourney. [Internet Archive](https://archive.org/details/anecdotestraditi00thomrich/page/6/mode/1up). Source ID: `thoms-anecdotes-traditions-1839`.

[^smith-massingham-1643]: Will of William Smith, esquire, of Great Massingham, Norfolk, dated 19 June 1643, proved 19 August 1645 (Norwich Consistory Court register 1644â€“5, fol. 215), naming "Edm: Gurnay" and "Ellen Gournay"; abstracted in <em>Norfolk wills extracts, 1370â€“1763</em> (Bradfer-Lawrence collection, typescript), FamilySearch film 008480295, image 41, [ark:/61903/3:1:3Q9M-C39V-K2LV](https://www.familysearch.org/ark:/61903/3:1:3Q9M-C39V-K2LV?view=fullText); page image `sources/media/norfolk-wills-extracts-bradfer-lawrence/smith-massingham-1643-img41.jpg`. Source ID: `norfolk-wills-extracts-bradfer-lawrence`.
```

**Concurrency note:** patchset v95 (Edmund ACAD) also adds an end-of-file footnote to this
research file. If v95 is applied first and appends its footnote after `[^thoms-anecdote]`, the
anchor above will no longer match; in that case append `[^smith-massingham-1643]` after the
then-final footnote instead. Both are end-of-file footnote additions and the order among them
is immaterial.

## Action 2 â€” durable media

Copy the abstract image into the v94 per-sourceId media folder:

- `sources/intake/new/2026-06-13-familysearch-browser-link-triage/images/sweep-smith-massingham-1643-gurnay-K2LV-img41.jpg` â†’ `sources/media/norfolk-wills-extracts-bradfer-lawrence/smith-massingham-1643-img41.jpg`

Append to `sources/media/norfolk-wills-extracts-bradfer-lawrence/README.md`:

```markdown
- `smith-massingham-1643-img41.jpg` â€” William Smith of Gt Massingham will abstract naming Edm: & Ellen Gurnay, NCC reg. 1644-5 fol. 215 (DGS 008480295, img 41, ark 3:1:3Q9M-C39V-K2LV).
```

## Source tracking

No new sourceId: reuses `norfolk-wills-extracts-bradfer-lawrence` (created in patchset v94, with its validation worksheet). The wife-Ellen corroboration also touches `dnb-edmund-gurney-1890` (already in `sources.json`), cited adjacently.

## Phase 2 completion

After Actions 1â€“2, prepend `**Done:** YYYY-MM-DD HH:MM PT` and move this file to
`sources/intake/done/`.
