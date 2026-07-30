# sources/media/_local/

Local-only working masters. Contents are **gitignored** and never pushed to GitHub.

## When to place a file here
Use `_local/` for any of:

1. **Oversize** — files larger than **35 MB**. (GitHub's hard limit is 100 MB, but 35 MB is the project threshold for "too bulky to commit.")
2. **Copyright-restricted** — modern in-copyright works, paywalled subscription content, licensed databases (e.g., UK Data Service EUL) where redistribution is restricted.
3. **Privacy-sensitive** — FamilySearch tree exports with living-person data, or any artifact carrying non-ancestor personal information.

Public-domain works under 35 MB are committed normally.

## Two valid locations
- `sources/media/_local/` — loose staging for masters not yet sorted into a `sourceId` folder.
- `sources/media/<sourceId>/_local/` — per-source local-only masters, sitting beside the committed working-reference crops/extracts for the same source.

Both are covered by the single `.gitignore` rule `sources/media/**/_local/`.

## Stub discipline
When a file moves into `_local/`, leave a small note in the **parent folder** (or update an existing `README.md` / `SOURCE.md`) recording:
- the filename now in `_local/`
- why it's local-only (size / copyright / privacy)
- where the canonical master can be retrieved (URL, archive, or physical repository)

The repo stays self-describing — readers can see what exists locally even when they can't see the bytes.

## Current contents of this folder
| File | Size | Reason | Canonical source |
|---|---|---|---|
| `rhgf-vol15-1878.pdf` | 459 MB | Oversize | *Recueil des historiens des Gaules et de la France*, vol. 15 (Paris, 1878). Public domain. Available at Gallica (BnF) and archive.org. |
| `Collectanea_Archaeologica.pdf` | 55 MB | Oversize | *Collectanea Archaeologica: Communications made to the British Archaeological Association*. 19th-century, public domain. Available at archive.org / HathiTrust. |
| `recueildesactesd01grea.pdf` | 38 MB | Oversize | Léopold Delisle (ed.), *Recueil des actes de Henri II*, vol. 1 (Paris, Imprimerie nationale). Public domain. Available at archive.org (`recueildesactesd01grea`) and Gallica. |
| `packets-34-36-working-crops/` | folder | Regenerable paleography diagnostics | Contact sheets, enhancement sheets, and crops generated from FamilySearch Packet 34-36 masters. Durable source masters live under `sources/media/fs-england-norfolk-parish-registers-1510-1997/_local/` and `sources/media/familysearch-fulltext-search/_local/`; reports live in `sources/intake/paleography-staging/done/`. |
| `cpr-edward-iv-1461-1467-fulltext-calendarpatentr14offigoog.txt` | ~4 MB | Raw OCR master; extracts cut | *Calendar of the Patent Rolls, Edward IV, 1461–1467* (HMSO 1897), public domain; archive.org `calendarpatentr14offigoog`. Curated Gurney extracts at `sources/corpus_supplement/cpr-edward-iv-1461-1477-gurney-entries.md`. |
| `cpr-edward-iv-henry-vi-1467-1477-fulltext-calendarofpatent00grea.txt` | ~3 MB | Raw OCR master; extracts cut | *Calendar of the Patent Rolls, Edward IV–Henry VI, 1467–1477* (HMSO 1900), public domain; archive.org `calendarofpatent00grea`. Same extracts file. |
| `norwich-freemen-calendar-1317-1603-fulltext-cu31924029785528.txt` | ~1 MB | Raw OCR master; extracts cut | L'Estrange/Rye, *Calendar of the Freemen of Norwich 1317–1603* (1888), public domain; archive.org `cu31924029785528`. Curated Gurney extracts at `sources/corpus_supplement/norwich-freemen-calendar-1317-1603-gurney-entries.md`. |
| `east-dereham-2026-07-working-crops/` | ~222 MB | Regenerable paleography diagnostics, plus superseded 2026-03 working inputs | `wip/` holds the crops, enhancement sweeps and comparator sheets from the July 2026 deviation audit of the East Dereham analysis — all regenerable from the masters with `tools/paleography_image_workbench.py`, and their boxes are recorded in the audit report. `original-content-2026-03-inputs/` holds the March–May 2026 inputs the audit was run against (April 2026 notebook bundle, earlier case-file drafts), retained for provenance only. **The register masters are not here:** NRO PD 86/41 is held complete, all 110 images, at `sources/media/nro-pd-86-41/_local/`. Findings at `sources/intake/paleography-staging/done/east-dereham-re-review-2026-07-*.md` and `research/people/g13-john-gurney/topics/identity/50-refactor-east-dereham-register-limits.md`. |

## Cross-reference
- `.claude/rules/sources.md` (intake + validations + media discipline)
- `sources/media/README.md`
