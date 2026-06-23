# Paleography staging — briefs, images, and returned results

This folder stages manuscript-image **briefs** for outsourced transcription and holds **returned reports** until their findings are assimilated into the repo. It is a working area, not a historical log — the prior packet-by-packet history lives in [`done/historical-staging-log-through-2026-06.md`](done/historical-staging-log-through-2026-06.md).

## Where things go (disposition model)

- **Brief (instructions) → staging root.** The outsourcer writes `packet-NN-<slug>.md` here and stages its images under `images/packet-NN-<slug>/`. Open briefs stay in the root.
- **Result report → staging root, NOT `done/`.** The subcontracted reader returns `packet-NN-<slug>.report.md` (or same-name `.md`) into this root. It **stays in the root until its findings are assimilated into the repo.** `done/` means *already assimilated* — so any unread or un-promoted finding must stay in the root, where it will not be lost. (A report whose name would clash with its brief: keep the report as `…report.md` and, on move, suffix the brief `…brief.md`.)
- **After assimilation → `done/` + `sources/media/`.** Once a report's findings are promoted into the repo (companion / `sources/corpus_supplement/` / leads, via a patchset), move BOTH the brief and the report to `done/`, move the image masters to `sources/media/<sourceId>/_local/` (gitignored; with a committed `README.md` stub naming the files, the FamilySearch-terms reason, and the retrieval arks/waypoints), move regenerable diagnostic crops to `sources/media/_local/<batch>-working-crops/`, and fix any staging-path references.

## Outsourcer — writing a brief

- **Give the subcontractor every image the question needs.** When the question is "who is the testator," include the will's **opening** page, not only the continuation that carries the name of interest. Rather than over-analysing exact pages, include a buffer of pages before/after the target (≤10 buffer images) and notate which are target vs. context.
- Provide the machine transcription text when available — **for localization only**; the surname/forename at the point of interest must come from the image, not the OCR.
- Include the questions the transcription may answer, plus any context, terminology, or names that help the paleographic read.
- **≤100 images per staged batch.** Stage masters to `images/<packet>/`; don't re-stage pages already worked to exhaustion.

## Outsourcer — incorporating a result

- **Each promoted finding needs the full chain:** a citation in the research/corpus file → a `sourceId` in `data/sources.json` (the `familysearch-fulltext-search` catch-all is fine for FTS image reads; mint a dedicated sourceId only for a discrete named document) → a corpus extract in `sources/corpus_supplement/` for any rich primary text → the relied-on masters in `sources/media/<sourceId>/_local/`. **The report in `done/` is transient — preserve full transcriptions in `corpus_supplement`, not only in the report.**
- **Record negatives and false positives as findings** (route open follow-ups to the subject file or a lead).
- When the subcontractor self-locates a missing image, **verify the located page actually matches the intended record** (parish, name, date) before trusting it.
- **Do not re-stage a page already worked to exhaustion.** Re-stage only when something genuinely new is supplied (a different enhancement, additional context pages, or a specialist tier) — not in hope of a different result from the same image.

## Subcontracted paleography — its job and limits

- It transcribes the provided images, attempts to find any images the brief left out, and returns a report with best-effort transcription, confidence notes, and explicit negatives. The report is a finding aid for the outsourcer to verify and incorporate — not itself a citable source layer.
- Treat machine/OCR snippets as locators only; the name at the exact point of interest must come from the image.
