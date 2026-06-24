---
name: british-history-online-research
description: Operational recipes for British History Online (BHO) full-text research - the in-browser search that bypasses the bot-gate, variant + co-occurrence query design across the BHO series landscape, free vs gold-paywalled content, result-anchor extraction, and the ground-before-claiming discipline that keeps a wide net from re-capturing held material. Read before any BHO full-text discovery task.
---

British History Online (british-history.ac.uk) is a large free/subscription digitised corpus of British printed primary and secondary sources. For the Gurney project it is far more than Blomefield's *Norfolk* topography (the parish pages for the family's own manors are already captured): the high-yield, under-mined veins are the **other series** that incidentally name the family.

> **Search *strategy* (variants, wildcarding, co-occurrence/token anchoring, source-awareness) is source-agnostic and lives in [`online-discovery-strategy`](../online-discovery-strategy/SKILL.md) — read that first.** This file is BHO *mechanics*: how to search it, what it holds, what is free, and how to triage.

## 1. The search works in the live browser (not headless fetch)

The BHO search endpoint `https://www.british-history.ac.uk/search?query=<terms>` returns a **CAPTCHA / bot-challenge** to a plain server-side fetch (WebFetch), so it reads as "no results." In an **authenticated/live browser** (Claude-in-Chrome) the same URL renders normally — navigate to it and read the page. Phrase search: wrap in `%22…%22`. The search is loose (terms can match in different parts of a long page), so treat multi-word and "phrase" hits as candidates to verify, not exact matches.

- **Result list:** the rendered page lists ~10 hits/page with the series title and a snippet. `get_page_text` returns the list cleanly. To get the result **URLs**, walk the anchors in-page (`document.querySelectorAll('a')`, keep hrefs containing `british-history.ac.uk` and not `/search`).
- **Content pages** (the actual articles, e.g. `/topographical-hist-norfolk/…`, `/vch/…`, `/inquis-post-mortem/…`) are **not** bot-gated — WebFetch reads them. For a long page, extract just the Gurnay context in-page: `body.innerText`, find each case-insensitive `gurnay`/`gournay`/`gurney` and slice ~±220 chars, or select paragraphs/entries containing the variant. WebFetch summarises but caps verbatim quotes — for a corpus extract pull the verbatim from the live page instead.

## 2. Variant + co-occurrence query design

Use the project variant set (`data/search-variants.json`). Practical notes for BHO's clean OCR of printed editions:
- Search the **Tudor/medieval spelling `Gurnay`** to surface the family with far less pollution than `Gurney` (which is swamped by the 19th-c. Buxton/Gurney bankers and modern indexes). Then `Gournay` (Norman/senior line) and the documentary forms (`Gornay`, `Gerneye`/`Gernay` — collision-prone, treat as leads).
- **Co-occurrence / in-law anchoring** is the high-yield move the user asked for: pair a variant with a **property name** (West Barsham, Harpley, Swathing/Hardingham, Pockthorpe, Saxthorpe) or an **in-law surname** (Calthorpe, Heydon, Blennerhasset, Jerningham/Jernegan, Hovell, Knyvet, Townshend, Bardolf). This finds incidental mentions (feoffee/trustee roles, marriage settlements, manor descents) the bare-name query buries.
- Enumerate the family's footprint by drilling the *index* pages (e.g. CIPM "Index of Persons and Places: G") to find which volumes hold a Gurnay, then read those entries.

## 3. The series landscape — and free vs gold

BHO mixes **free** content (digitised by rekeying/OCR) and **gold** (subscription) content; gold pages render only the access/navigation chrome (and WebFetch reports a paywall / login). Known from the June-2026 sweep:
- **Free, high-yield:** Blomefield *Norfolk* (topography — mostly already captured); **Calendar of the Cecil Papers (Hatfield)**; **Letters and Papers, Henry VIII**; **Victoria County History** (per-county, e.g. Hants, Bucks, Glos for the West-Country Gournays); **Calendar of Inquisitions Post Mortem** (including the Series-2 Henry VII–VIII volumes and the per-volume "Index: G" pages).
- **Gold-paywalled (snippet only):** **Calendar of Close Rolls** and at least some **Calendar of Patent Rolls** volumes — the search snippet is visible but the full entry needs a subscription (or the AALT/TNA image route).

## 4. Ground before claiming new (mandatory)

BHO is a *wide net* over a repo that is already deep. **Before promoting any BHO hit, ground it** with `repo_search.py` (locate the names/manor in `research/`, `sources/corpus*`, `data/sources.json`) — much of the medieval material is already held via Blomefield, Daniel Gurney, Farrer, Pettigrew, Rudder, Brooke/Rye, and the Camden/Cawley senior-line work. Worked June-2026 outcomes that show the discipline paying off:
- **New & promoted:** William Gurnay as Sir Roger Townshend's feoffee (CIPM Henry VII, 1493); Edmund Gurnay's 1606 Cecil-Papers appeal to Salisbury; the Hampshire manor "Wellow Gurnay" (VCH Hants); the Bledlow Bec-exchange detail (VCH Bucks).
- **Caught as already-held (not re-captured):** the Hardingham/Swathing manor descent; the 1469/70 Thomas Gurnay will; the core Juliana de Gournay × Bardolf descent.
- **Grounded out as not-our-line:** "John Gerneye" granted an Exeter consistory office (Letters & Papers Henry VIII vol. 17, 1542) — a Devon/West-Country or distinct-surname figure, the `Gerneye` variant being collision-prone; retained as a checked negative, not promoted.

## See also
- `.claude/skills/online-discovery-strategy/SKILL.md` — the two reasoning gates and cause-matched technique selection (read first).
- `data/search-variants.json` — the variant registry.
- `tools/repo_search_README.md` — the grounding tool.
