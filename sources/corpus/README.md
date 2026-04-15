# sources/corpus/

Searchable full-text extracts of primary and secondary sources. The working-reference layer for citing, quoting, and verifying claims made in fact sheets and case files.

## Where to look for what

- **What sources exist** → `data/sources.json` is the canonical catalog. Every source ever cited gets an entry there with `corpusStatus`, `corpusPath`, archive provenance, and notes. Don't go through this README to find out what's in the corpus — go to `sources.json` or browse the directory listing.
- **Per-source deep documentation** → for sources with multiple files, complex pagination, OCR quirks, or extraction history worth recording, place a `{source-id}-readme.md` next to the corpus files. Example: `daniel-gurney-readme.md` for the four-part Daniel Gurney book.
- **Image captures of specific records** → `sources/media/{source-id}/`.
- **Original PDFs** — live outside the repo (OneDrive) for archival fidelity. Reach for the PDF only when text isn't enough (paleography, marginalia, layout questions).

## Filename convention

- Markdown extracts: kebab-case, source-identifying. `daniel-gurney-part-1.md`, `norfolk-antiquarian-gurneys-of-norwich.md`.
- Raw OCR/text dumps from archive scans may keep their archive-derived filenames if they're easier to trace back to source. Filename quirks are fine; the entry in `sources.json` is what makes the file authoritative.
- Source-specific READMEs: `{source-id}-readme.md`.

## Policy

- **Text-in-repo preferred over PDF-in-repo** for anything longer than a few pages. Text is searchable, quotable, diffable, cheap to fetch.
- **Preserve page markers** when sourcing from OCR scans so citations tie to specific pages. HathiTrust, Internet Archive, and Google Books extractions typically preserve these.
- **Record OCR quirks** in the source-specific README (or in the file header if no separate README exists). Common issues: `ffi`/`fi` ligatures, long-s vs `f`, line-break hyphenation, period-typography artifacts. Documented quirks are far more useful than pretending they aren't there.

## Adding a source to the corpus

1. Drop the text file into this folder.
2. Register or update the entry in `data/sources.json` (set `corpusStatus`, `corpusPath`, `notes`).
3. If the source warrants deep documentation, create a `{source-id}-readme.md` here.
4. No need to update this README.
