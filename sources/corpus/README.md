# sources/corpus/

Full-text versions of key primary and secondary sources. These are my working-reference copies for searching, quoting, and verifying claims made in fact sheets and case files.

## Media vs. corpus

- **`corpus/`** (this folder) — searchable text for cite-from and verify-against work.
- **`sources/media/`** — image captures of specific register entries, record details, and visual evidence.
- **Original PDFs** — live outside the repo in OneDrive for archival fidelity. Reach for the PDF only when the text version is insufficient (paleography, marginal notes, page-image questions).

## Policy

- **Text-in-repo preferred over PDF-in-repo** for anything longer than a few pages. Text is searchable, quotable, diffable, and cheap to fetch. PDFs are large, opaque to grep, and awkward for both humans and AI to navigate.
- **Preserve page markers** when sourcing from OCR scans so citations tie to specific pages. HathiTrust/Google Books/Internet Archive typically preserve these in their extracted text.
- **Record OCR quirks** in each corpus file's header. Common issues: `ffi`/`fi` ligatures, long-s vs `f`, line-break hyphenation, 19th-century typography collapsing `William` → `Wilham`. Documented quirks are far more useful than pretending they aren't there.

## Currently in corpus

- `daniel-gurney-part-1.md` — *The Record of the House of Gournay*, Part I (Norman origins through G32 Gerard de Gournay). HathiTrust/Yale scan of 1848 original.
- `daniel-gurney-part-2.md` — Part II (Junior Norfolk Branch, West Barsham medieval Gurneys).
- `daniel-gurney-part-3.md` — Part III (Tudor through early-modern: Anthony, Francis G16, Henry, Francis Merchant Taylor, John of Maldon, John of Norwich).

## Not yet in corpus

- **Daniel Gurney, 1858 Supplement** — PDF exists in project knowledge (`Record_of_the_House_of_Gurney_by_Daniel_Gurney-Supplement.pdf`). Text extraction needed.
- **Rye appendix** — referenced in Supplement. Source uncertain.
- **Anderson, *Great Migration Directory* (2015)** — John Gurney-1 entry. Targeted extraction, not full book.
- **Banks/Brownell, *Topographical Dictionary* (1937)** — Gurney entry.
- **Pease genealogy** (pennyghael.org.uk/Gurney.pdf) — Ryvett claim source.
- **Blomefield, *History of Norfolk*** — relevant sections for Harpley, West Barsham, Great Ellingham, Norwich parishes.
- **FG Gurney 121 notebooks** (Buckinghamshire Archaeological Society) — unexamined.

Adding to the corpus: copy text into `sources/corpus/{sourceId}.md` with a header documenting provenance, edition, OCR method, and known quirks. Register the source in `data/sources.json` with a `corpusStatus: "full" | "partial" | "none"` field.
