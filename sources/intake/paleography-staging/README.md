# Paleography staging — open brief

This folder stages manuscript-image briefs for outsourced transcription. 

> **Source terms:** all images are FamilySearch-sourced (17th-c. manuscript, public-domain content under FamilySearch viewing terms). Masters live in `sources/media/<set>/_local/` (off GitHub) or, for in-progress packets, in `images/`.

## Process notes (read before staging or incorporating a batch)

Two distinct roles run through this folder. Keep them separate.

**Outsourcer (this repo / the maintainer) — staging a brief and incorporating the result:**
- **Give the subcontractor every image the question needs.** When the question is "who is the testator," the brief must include the will's **opening** page, not only the continuation that carries the name of interest — packets 16a/16b could not name their testators because only continuation pages were staged (the fix became Packet 20). Rather than costly over-analysis to determine exact pages, it is acceptable to include pages before or after the target (no more than 10 buffer images total). When available, provide the machine transcription text for location purposes-only. The outsourcer should include questions that the transcription may answer and may include context, terminology, or names that may help in the paleographic work.
- **Masters belong in `sources/media/<set>/_local/`, never long-term in this folder's `images/`.** `images/` is a transient handoff staging area; FamilySearch masters must not sit committed here. On incorporation, move every relied-on master into the right `sources/media/<set>/_local/` folder (gitignored) and document it in that folder's committed `README.md`.
- **When incorporating into research after analysis, each promoted finding needs the full chain:** a citation in the research/corpus file → a `sourceId` in `data/sources.json` (the `familysearch-fulltext-search` catch-all is fine for FTS image reads; mint a dedicated sourceId only for a discrete named document, e.g. a specific will) → a corpus extract in `sources/corpus_supplement/` for any rich primary text → the relied-on images in `sources/media/<set>/_local/`. **The packet report in `done/` is transient — preserve full transcriptions in `corpus_supplement`, not only in the report.**
- **Record negatives and false positives as findings** (e.g. packet 16c = Robert Webber, not a Gurney; packet 14f "Cropley" = formulaic Latin), and route open follow-ups to the subject file or a lead — do not accumulate a parallel to-do list in this README.
- When the subcontractor self-locates a missing image (packet 21b admon, packet 23 1758 recital), **verify the located page actually matches the intended record** (parish, name, date) before trusting it.

**Subcontracted paleography (the outsourced AI reader) — its job and its limits:**
- It transcribes the provided images, attempts to find any images the brief left out, and returns a `packet-NN-*.md` report with best-effort transcription, confidence notes, and explicit negatives. Its report is a finding aid for the outsourcer to verify and incorporate — not itself a citable source layer.
- **Dense Latin manorial/secretary court hand routinely defeats it** (Cawston death presentments, the East Dereham 1662/65 page). Treat "blocked / unresolved" as an expected outcome for those and either flag for a specialist or accept the negative; do not re-stage the same hard page expecting a different result.
- **Watch the Syon↔Lyon trap** (the looped opening long-S): the Earsham family forename is **Syon/Sion**, repeatedly misreadable as Lyon (recognition note already logged).
- Treat machine/OCR snippets as locators only; the surname/forename at the exact point of interest is usually where the OCR fails, so it must come from the image.
