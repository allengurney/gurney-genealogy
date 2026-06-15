---
name: paleography-analysis
description: Reusable paleographic manuscript-analysis workflow for genealogy source images. Use before tasks involving handwritten wills, parish registers, deeds, court books, FamilySearch manuscript images, paleographic transcription, ambiguous letterforms, crop/snippet generation, image enhancement sheets, comparator sweeps, or recurring recognition lessons for Gurney/Gournay variants.
---

# Paleography Analysis

## Start Here

Use this workflow before manuscript transcription or crop work. The goal is to spend local compute on generous candidate images and spend AI attention on reading, comparison, and evidence discipline.

Required preflight:

```powershell
.\tools\bootstrap_python_toolchain.cmd -CheckOnly
```

If packages are missing and the user has approved environment setup:

```powershell
.\tools\bootstrap_python_toolchain.cmd
```

Use the `.cmd` wrapper from PowerShell. It runs the repo script with a per-process execution-policy bypass, avoiding the local Windows policy block on direct `.ps1` invocation.

Use only the repo-local interpreter for Python commands:

```powershell
.\.venv\Scripts\python.exe tools\paleography_image_workbench.py ...
```

## Image Workflow

1. Identify the source image and provenance: record URL/ARK/DGS/image number, repository citation, and whether the image is a local-only master.
2. Run `info` to capture dimensions before guessing coordinates.
3. Generate a full-page or page-half grid before detailed cropping.
4. Use an approximate target region to produce a crop ladder with line strips, not one hand-tuned crop.
5. Use enhancement sheets for reading only; cite/transcribe from the primary image and keep uncertainty visible.

Useful commands:

```powershell
.\.venv\Scripts\python.exe tools\paleography_image_workbench.py info image.jpg
.\.venv\Scripts\python.exe tools\paleography_image_workbench.py grid image.jpg --out snippets\image-grid.png
.\.venv\Scripts\python.exe tools\paleography_image_workbench.py crop-ladder image.jpg --box 1200,1800,2200,420 --out-dir snippets --prefix packet-01-target --scale 2 --line-strips --tile-max-width 900
.\.venv\Scripts\python.exe tools\paleography_image_workbench.py sheet image.jpg --box 1200,1800,2200,420 --out snippets\packet-01-target-sheet.png --scale 2 --tile-max-width 900
.\.venv\Scripts\python.exe tools\paleography_image_workbench.py manifest-summary snippets\packet-01-target-manifest.md --selected-only
```

For PDFs:

```powershell
.\.venv\Scripts\python.exe tools\paleography_image_workbench.py render-pdf source.pdf --page 1 --dpi 300 --out images\source-page-001.png
```

## Crop Discipline

Prefer three tiers:

- Locator crop: wider/taller context, usually 3-5 lines, for orientation and comparator hunting.
- Reading strip: one target line with enough padding for ascenders, descenders, word spacing, and nearby ink.
- Token crop: a small ambiguous word or letter, always paired with the reading strip.

Default posture:

- Prefer too much context for analysis; make tight crops only after the reading is stable.
- Do not keep playing coordinate hot-and-cold. If a crop is off, generate a grid or a crop ladder.
- If a strip contains multiple lines, run `line-strips` or `crop-ladder --line-strips` and choose from the contact sheet.
- If automatic line stripping collapses dense or slanted manuscript into one large strip, use manual bands from the grid:
  - `line-strips --line-count N` when the target box has a clear number of lines.
  - `line-strips --line-height N` when the line spacing is regular.
  - `band-ladder --band label:x,y,width,height --band label:x,y,width,height` when you want hand-picked full-image boxes from the grid.
- If segmentation is uncertain, keep multiple labelled candidates rather than picking a single "best" crop.
- Record coordinates through the generated manifest so crops can be reproduced.
- Use `--tile-max-width 800` to `1100` for fast review sheets; use `--tile-max-width 0` only when a full-width contact sheet is worth the file size.
- Use `manifest-summary` to paste selected crop names and coordinates into packet reports instead of hand-copying them.

## Transcription Posture

- Treat the primary image as the authority.
- Treat machine transcripts, OCR, FTS snippets, and poor inherited transcriptions as locator aids only unless the image confirms them.
- Use poor transcripts to find names, neighboring words, approximate page position, and formulaic language.
- Preserve uncertain letters with brackets or alternatives, and attach confidence to the specific reading, not to the whole document.
- Use comparator words from the same hand, same page, or same film before relying on general letterform memory.
- Separate what the line says from what the genealogical finding implies.

## Outputs

During staging, keep generated snippets near the image packet, normally under `sources/intake/paleography-staging/` or the current intake session folder.

After a batch is promoted, follow `.claude/skills/familysearch-fulltext-research/SKILL.md` for disposition of packet reports, master images, working crops, and staging-path cleanup.

Substantive readings and findings belong in the relevant research file or `sources/corpus_supplement/`, not only in image manifests. Manifests are reproducibility aids, not research destinations.

## Continual Improvement

At the end of each paleography task, decide whether a reusable lesson was learned. If yes, append a concise entry to `references/recognition-notes.md`.

Good entries include:

- collection, film, sourceId, or image range
- date range and document type
- hand or scribe clue, if known
- successful enhancement settings
- useful comparator words
- Gurney/Gournay variant or false friend
- failed reading to avoid rediscovering

Do not add one-off guesses or unresolved impressions. Keep durable reading lessons here; keep genealogical conclusions in research files.

## Reference

Read `references/recognition-notes.md` when a task involves a previously seen collection, film, hand, Gurney-name variant, or recurring contrast problem.
