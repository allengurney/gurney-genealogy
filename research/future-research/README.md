# Future research

Planning layer for research that has been **documented as a lead** somewhere in the repo but **not yet pursued or resolved**. This directory holds the master leads catalog plus any single-subject lead inventories that grow too large to sit inside one companion.

## Files

- **`research-leads.csv`** — the master prioritized catalog. One row per open lead, de-duplicated across every research companion, topic file, place file, done patchset tail, and the data layer.
- **`research-leads-done.csv`** — thin archive of resolved or rejected lead IDs, with one-line dispositions only. Do not move fat research narratives here.
- **`john-gurney-source-leads.md`** — the pre-existing John Gurney G13 lead notes from the v15 audit. Detail-level companion to the G13 rows in the catalog.

## Tooling

Use `tools/research_leads.py` for routine lead-catalog reads and writes. This keeps AI and human workflows from reading or rewriting the full CSV for single-lead work.

Common commands:

```bash
python tools/research_leads.py priority                 # top online leads; banner flags hidden Online=N
python tools/research_leads.py priority --include-offline   # include Online=N (e.g. College-of-Arms pulls)
python tools/research_leads.py context L-123
python tools/research_leads.py get L-123 --warnings
python tools/research_leads.py list --online-reachable --min-priority 60
python tools/research_leads.py search "Great Ellingham"
python tools/research_leads.py update L-123 --status Partial --dry-run    # compact per-row change preview
python tools/research_leads.py update L-123 --status Partial --dry-run --verbose   # full unified diff
python tools/research_leads.py close L-123 --disposition "Resolved; companion updated." --dry-run
python tools/research_leads.py audit                    # summary counts: stale-done + over-length Status
python tools/research_leads.py audit --verbose          # list affected leads
python tools/research_leads.py validate
```

Notes on `priority`: it is value-ranked and online-optimised — by default it shows
`Online=Y`/`Part` and prints a one-line banner naming the highest hidden `Online=N`
leads (use `--include-offline` to see them). It excludes only concluded
(stale-done) rows, so high-value leads carrying a narrative `Status` still surface.
`--dry-run` prints just the changed rows; add `--verbose` for the full unified diff.
Writes preserve the file's per-column quoting so a single-field edit diffs at one row.

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
| **Status** | Concise workflow state only. Prefer `Open` or `Partial`; do not use this field as a research log. Existing legacy narrative statuses may remain until touched, but new updates should keep narrative findings in the relevant companion/case file. |
| **Source ref** | Where the lead is documented in the repo (traceability, in lieu of inline IDs in the companions). |

## Priority rubric (value/impact, independent of availability)

Priority scores **genealogical impact only** — it deliberately ignores whether the source is online **and how far the lead has already been worked**. That way, if a source's `Online` status later changes, or a lead is partly resolved, the priority does not need recalculating: a partly-worked lead keeps its impact score, and its remaining work is tracked in `Status` / the companion (and surfaced by `audit`), not by demoting it. Use the `Online` column to triage *which* high-value leads are reachable now. Priority is a function of multiple factors including value, impact, importance, quality, reliability, novelty, scope, and others.

- **85–100 — identity- or pedigree-resolving.** Would close a major open question (e.g. the G13 emigrant's origin, the G22 heralds' pedigree).
- **60–84 — strongly anchoring.** Pins a death date, parentage, marriage, or manor descent at a documented transition.
- **40–59 — corroborating.** Sharpens chronology or relationships; confirms an existing reading at source level.
- **20–39 — enrichment / collateral / catalog.** Collateral lines, heraldic curiosities, place/heritage anchors, confirmatory checks on already-decided points.

**Collateral-line discount (esp. Maldon).** Direct ancestors outrank collateral branches. The **Maldon, Essex Gurneys** in particular (Francis of Maldon and the line descending to the Quaker bankers) are a collateral branch that Walter Rye argued is *not* our line; absent a strong overriding factor (e.g. a record that would directly fix the G13 emigrant's paternity), Maldon-specific leads should sit in the 20–39 band, well below direct-ancestor work. Do not let a rich Maldon source pull effort away from direct-line targets.

## Pre-pull sanity check (do this BEFORE pursuing any lead)

A lead in this catalog records that something was *flagged*, not that it is *unheld*. Leads go stale: the source may already be captured, or already worked on a companion. **Before spending effort (and especially before delegating) on any lead, run a fast existence check — seconds, not a project:**

1. **Source already held?** Grep `data/sources.json` / `data/indexes/source-ids.csv` and `sources/corpus*/` for the author, title, or an obvious `sourceId` slug. A clean-OCR extract of the exact source may already exist (e.g. Rye's *Gurneys of Norwich* = `rye-norfolk-antiquarian`, full extract in `sources/corpus/`).
2. **Lead already worked?** Read the companion named in the lead's `Source ref`, and grep the subject's `research/people|places|topics` file for the source. The CSV `Status` lags the companions (see the memory note); the companion is the source of truth.
3. **Only then pursue it** — and scope the pull to the *delta* (what the companion does NOT already have), not the whole source. Do not rework already-held material just because the lead is still listed.

## Maintenance rules

- **Open items only.** The catalog holds leads that are still live. When a lead reaches a disposition (resolved or rejected), move a thin row to `research-leads-done.csv` (`ID`, `Subject`, one-line disposition, date, companion/source ref) and trim it from `research-leads.csv`. Fat disposition narratives belong in the relevant companion/case file and the commit history, not either CSV.
- **Keep CSV fields index-sized.** `Description` should state what the pull would establish and why it matters; `Status` should stay to `Open` / `Partial` or another short workflow note. Do not add long research findings, negative-search histories, or disposition narratives to the CSV; promote those to the relevant companion, case file, source supplement, or patchset.
- **Close-out scrub.** On disposition, open the file named in `Source ref` and clear visible body/headings that describe the lead as open, sought, or pending. Keep `L-` handles only in footnotes or HTML comments when they are useful as a discovery trail.
- **De-duplicate.** A source that surfaces on several companions gets **one** row; cite the best documenting file in `Source ref`. (Several G13 wills, the Spelman pedigree, St Benet Fink, and the Ryvett pedigrees were each consolidated this way.)
- **Eliminated kill-targets are not leads.** Targets that only existed to test a now-eliminated hypothesis (e.g. Candidate D's London confirmation pulls) are excluded.
- **New leads** discovered in future work get the next free `L-` id appended.
- **Exhausted-online → demote from the online view (stops repeat re-working).** A lead that has been worked online to exhaustion — every indexed/full-text/catalogue route tried, only an offline, image-only, or auth-gated residual remaining — should have its **`Online` set to `N`** (or `Part` if a partial image route genuinely survives), with the residual recorded in `Status`/the companion. Because `priority` shows `Online=Y`/`Part` by default and hides `Online=N`, this drops the lead out of the default online worklist so it is **not repeatedly re-recommended and re-worked** (the recurring failure mode where a lead is touched four-plus times across sessions/agents). Its impact-based `Priority` is left unchanged, so it resurfaces immediately if its `Online` status later improves (e.g. a film is digitised). When recommending leads for a new session, prefer `Online=Y`/`Part` leads not already worked this arc, and consult the pre-pull sanity check above before pursuing any of them.
