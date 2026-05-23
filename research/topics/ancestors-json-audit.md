# ancestors v23.json — Data Audit

Cross-cutting topic file. Tracks data-quality issues in `data/ancestors v23.json` identified during the G20–G37 transcript migration sweep.

---

## Filename mismatch — AI-Rules vs. actual

**AI-Rules §2 and §7 reference `ancestors_v23.json` (underscore).**
**Actual file: `data/ancestors v23.json` (space).**

Either AI-Rules should be updated to match the actual filename, or the file should be renamed via the bulk-script exception in §3. Renaming is more aesthetic but requires Allen to run a local operation; updating AI-Rules is zero-friction via MCP.

Recommendation: rename the file locally to `ancestors_v23.json` for consistency with the citation style (`[DG-II-NNN]`, `[NRO-PD12/1]`, underscore-free internal references throughout the repo). Until that happens, AI-Rules references should be understood as referring to the space-named file.

---

## Landholding-location data pollution

Several ancestor entries in `data/ancestors v23.json` have **`sourceQuote` or `eventDate` fields that concatenate values from multiple ancestors** — clearly a data-generation bug where a merge or rewrite operation accumulated values across successive generations rather than scoping them per-ancestor.

### Confirmed instances (G20–G37 sweep, 2026-04-16)

| Ancestor | Gen | Location | Symptom |
|---|---|---|---|
| Thomas Gournay II | G20 | Harpley landholding | `eventDate` reads: "21 Jan. 1548/9 — d. 1615/16 \| c. 1430 – d. before 27 July 1471 \| d. 1408 \| d. 1387 \| fl. c. 1300–1360" — five generations concatenated |
| Thomas Gournay II | G20 | West Barsham landholding | `eventDate` reads: seven-plus-generation concatenation ending with "…" truncation |
| Edmund Gournay | G23 | Harpley landholding | Same five-generation concatenation as G20 Harpley |
| Edmund Gournay | G23 | West Barsham landholding | Same seven-plus-generation concatenation as G20 West Barsham |
| Edmund Gournay | G23 | King's Lynn landholding | `eventDate` reads: "13 Sept. 1581 — d. 1640 \| d. 1387" — Henry G15 dates concatenated with Edmund's |
| Edmund Gournay | G23 | Hardingham landholding | `eventDate` reads: "c. 1465 – before 18 Jan. 1507/8 \| d. 1408 \| d. 1387 \| fl. c. 1300–1360" — William V and others concatenated |
| Gerard de Gournay | G32 | Norfolk landholding | `eventDate` reads: "d. 1408 \| c. 1098 — d. 1180 \| c. 1040 — d. before 1104, Palestine \| c. 1020 — d. c. 1093" — four generations |
| Gerard de Gournay | G32 | Gournay-en-Bray landholding | Seven-plus-generation concatenation on the shared senior-line seat |
| Hugh de Gournay III | G33 | Norfolk landholding | Same four-generation concatenation as G32 Norfolk |
| Hugh de Gournay III | G33 | Gournay-en-Bray landholding | Same seven-plus-generation concatenation |
| Hugh de Gournay II | G34 | Gournay-en-Bray landholding | Same seven-plus-generation concatenation |
| Renaud de Gournay | G35 | Gournay-en-Bray landholding | Same seven-plus-generation concatenation |
| Hugh de Gournay I | G36 | Gournay-en-Bray landholding | Same seven-plus-generation concatenation |
| Eudes de Gournay | G37 | Gournay-en-Bray landholding | Same seven-plus-generation concatenation |

### Pattern

The Gournay-en-Bray entry is shared as a landholding across G37 through G33 (six ancestors) and the concatenation appears to be the full chain of their `eventDate` values merged into one field, separated by ` | ` and truncated at the end with "…". The Norfolk, Harpley, and West Barsham entries show the same pattern at their respective generational depths.

### Incorrect landholding assignment — G37 Eudes

In addition to the concatenation bug, **G37 Eudes has a landholding entry for West Barsham, Norfolk** (coordinates 52.867826, 0.830094). This is categorically wrong. West Barsham did not enter the Gurney family until 1372, via Katherine de Wauncy's marriage to Edmund (G23) — nearly 500 years after Eudes. This is a data error that needs removal, not just cleanup of the `eventDate` field.

### Likely cause

The JSON appears to have been edited by a script that aggregated shared-location landholding entries across generations, populating the location entry once and then accumulating all relevant `eventDate` / `sourceQuote` values into that single entry rather than creating separate per-ancestor location records. Normal structure would be: **one location record per (ancestor, place) pair**, each with its own scoped `eventDate`.

### Fix plan

This is not urgent — the fact sheets, research companions, and place files all render correctly. The JSON bug only surfaces when someone:
1. Reads the JSON directly (e.g., for a future app or export).
2. Builds a map visualization that reads `eventDate` verbatim.
3. Uses the landholding records for timeline generation.

When the site's build system or a future application consumes `landholding / property reference` event types, this will need to be cleaned. For now, the place files in `research/places/` carry the correct per-ancestor chronology in markdown form, which is the authoritative narrative.

Proposed fix:
- Split each contaminated location record into one record per ancestor holding the place.
- Remove the West Barsham entry from G37 Eudes entirely.
- Trim any `…` truncation artifacts from concatenated fields.

This is a bulk-script job (not MCP) per AI-Rules §3 exception — 14+ locations across 8 ancestors.

---

## Action

- [x] Document the concatenation bug (this file).
- [x] Document the West Barsham / G37 incorrect-assignment bug.
- [x] Document the filename mismatch.
- [ ] Decide: rename `ancestors v23.json` → `ancestors_v23.json`, or update AI-Rules.
- [ ] Script to de-concatenate the `eventDate` / `sourceQuote` fields and split into per-ancestor location records.
- [ ] Remove West Barsham landholding from G37.
- [ ] Verify the map visualization in `tools/pedigree-explorer.html` (or future map tool) renders correctly after cleanup.

## Related

- AI-Rules §2 (repo map) and §7 (structural facts — current ancestor data file reference).
- `research/places/` — 17 place files created 2026-04-16; markdown-authoritative for per-ancestor landholding chronology.
- `research/topics/dg-citation-audit.md` — companion citation-audit topic file.
