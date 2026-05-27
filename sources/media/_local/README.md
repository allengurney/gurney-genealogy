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

## Cross-reference
- `.claude/rules/sources.md` (intake + validations + media discipline)
- `sources/media/README.md`
