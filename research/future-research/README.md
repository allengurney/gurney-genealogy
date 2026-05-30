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
| **Online** | `Y` = known to be online; `Part` = partly online (e.g. index/calendar online, original image/manuscript not); `N` = known not online / archive-only / lost; `Unk` = not yet checked. See the availability triage below. |
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

## Online-availability triage (2026-05-29)

A pass classifying every open lead by how reachable it is **without a physical archive visit or special access**, to steer online-only work. Priority (impact) is unchanged; this only sorts by reachability. Tiers below; the per-row `Online` column is being refined to match as leads are worked.

**🟢 Online now — digitized text, database, or viewable record image (no physical pull)**
- G13 cluster: **L-3** (colonial VRs/probate, FS/Ancestry), **L-11** (Braintree VRs, FS DGS image), **L-16** (St Ann Blackfriars, LMA image), **L-20** (Suffolk probate #338, FS DGS image), **L-15** (Venn *Alumni Cantab.* + CCEd), **L-22** (Dale, *Inhabitants of London 1638*), **L-71** (Burke's *Landed Gentry* 1858).
- Medieval/gentry: **L-37** (History of Parliament — confirmed: no standalone Edmund entry; the "John Gurney d.1408" / Sir John V biography carries the Edmund/West Barsham material and is fully online), **L-36** + **L-33** (IPMs via the published *Calendar of Inquisitions Post Mortem* on British History Online / archive.org), **L-24** (1633 Visitation of Norfolk), **L-28** (Paston Letters), **L-35** (Norfolk Feet of Fines, Rye), **L-27** (*L&P Henry VIII*, BHO), **L-38** (Cal. Patent Rolls), **L-40** (Farrer), **L-47/L-48/L-49/L-54** (French/Latin charters, Gallica & archive.org), **L-58/L-59/L-61/L-62/L-64/L-65/L-66** (MedLands, Ormerod, CIPM 16, Visitations of Norfolk/Suffolk, Norfolk Heritage Explorer, Historic England).

**🟡 Probably online — one verification click**
- **L-13** (East Dereham register image almost certainly on FS; only the paleographic exam is non-digital), **L-21 / L-23** (Suffolk / Yorkshire parish registers, FS/Ancestry), **L-2**, **L-41** (CP40 plea roll — possible AALT images), **L-46** (Blomefield online; its Harleian MS 970 companion is not), **L-50 / L-56 / L-57** (modern Norman-line scholarship), **L-51 / L-53**.

**🔴 Physical pull or special access (deprioritize for online work)**
- **L-32** ⚠️ (Cook 1622 Visitation — College of Arms MS; your highest-priority lead, but not online), **L-29** (1445 Hunstanton feoffment deed, Le Strange archive), **L-39** (BL Add. MS 8841), **L-25** (Bodleian MS Tanner 175 — largely already extracted via the 2005 article), **L-5** (Spelman pedigree, dispersed at the 1936 Sotheby's Gurney sale), **L-69 / L-70** (FamilySearch-Center-restricted).
- *Half-online* (index/calendar online; will or deed images at NRO, order or in-person): **L-6, L-8-remaining, L-26, L-30, L-34, L-68**.
- *Physical or lost*: **L-1** (Masonic lodge records), **L-42 / L-44** (seals/objects/coffin-lid), **L-52 / L-55** (lost or unpublished MSS), **L-10** (earliest American-arms witness — likely a physical object unless already photographed).

Leads not named retain their existing `Online` value pending a check.
