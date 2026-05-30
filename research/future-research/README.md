# Future research

Planning layer for research that has been **documented as a lead** somewhere in the repo but **not yet pursued or resolved**. This directory holds the master leads catalog plus any single-subject lead inventories that grow too large to sit inside one companion.

## Files

- **`research-leads.csv`** — the master prioritized catalog. One row per open lead, de-duplicated across every research companion, topic file, place file, done patchset tail, and the data layer.
- **`john-gurney-source-leads.md`** — the pre-existing John Gurney G13 lead notes from the v15 audit. Detail-level companion to the G13 rows in the catalog.

## `research-leads.csv` columns

| Column | Meaning |
|---|---|
| **ID** | Stable handle `L-1`, `L-2`, … Cite it in chat and commits. IDs are never reused; a trimmed lead's ID is retired, not reassigned. |
| **Priority** | Subjective **value/impact** estimate, 1–100 (100 = best). See rubric below. |
| **Gen** | Generation anchor (G1 = Allen … G37 = Eudes de Gournay). Ranges and `Collateral` / `Heraldic` / `Places` are used where a lead is not tied to one direct ancestor. |
| **Subject** | The person, place, or family the lead bears on. |
| **Lead/Source** | The specific source, record series, or repository to pull. |
| **Description** | One line: what the pull would establish and why it matters. |
| **Online** | `Y` = known to be online; `N` = known not online / archive-only / lost; `Unk` = not yet checked. |
| **Status** | `Open` for all live leads. `Partial` = preliminarily pulled, work remaining. |
| **Source ref** | Where the lead is documented in the repo (traceability, in lieu of inline IDs in the companions). |

## Priority rubric (value/impact, independent of availability)

Priority scores **genealogical impact only** — it deliberately ignores whether the source is online. That way, if a source's `Online` status later changes, the priority does not need recalculating. Use the `Online` column to triage *which* high-value leads are reachable now.

- **85–100 — identity- or pedigree-resolving.** Would close a major open question (e.g. the G13 emigrant's origin, the G22 heralds' pedigree).
- **60–84 — strongly anchoring.** Pins a death date, parentage, marriage, or manor descent at a documented transition.
- **40–59 — corroborating.** Sharpens chronology or relationships; confirms an existing reading at source level.
- **20–39 — enrichment / collateral / catalog.** Collateral lines, heraldic curiosities, place/heritage anchors, confirmatory checks on already-decided points.

## Maintenance rules

- **Open items only.** The catalog holds leads that are still live. When a lead reaches a disposition (resolved or rejected), **trim its row** to keep the list tidy — the disposition belongs in the relevant companion/case file and the commit history, not here.
- **De-duplicate.** A source that surfaces on several companions gets **one** row; cite the best documenting file in `Source ref`. (Several G13 wills, the Spelman pedigree, St Benet Fink, and the Ryvett pedigrees were each consolidated this way.)
- **Eliminated kill-targets are not leads.** Targets that only existed to test a now-eliminated hypothesis (e.g. Candidate D's London confirmation pulls) are excluded.
- **New leads** discovered in future work get the next free `L-` id appended.

## Scope note

The crawl behind the first build covered: all `research/people/` companions, all `research/topics/` and `research/places/` files (including the England landholding catalog-gap rounds), the `sources/intake/done/` patchset tails, the John Gurney case file, `research/future-research/john-gurney-source-leads.md`, and the `data/places_detail.json` review-notes. Pure internal catalog-linking tasks (place-registry geocoding decisions) and fully-resolved heritage-anchor extractions were left out as not being research *pulls*.
