---
paths:
  - "sources/intake/**/*.md"
  - "sources/intake/**/*"
  - "sources/validations/*.md"
  - "sources/media/**/*.md"
  - "sources/media/**/*"
---

# Sources rules — intake, validations, media

Human-facing overview:
- `sources/README.md`

This rule governs three `sources/` subdirectories. `sources/corpus/` and `sources/corpus_supplement/` are searchable extract repositories — they hold the verbatim text of cited sources but do not require their own per-edit rule beyond the conventions described here.

For destination decisions when a finding could land in more than one place, see `sources/README.md`.

## sources/intake/

The raw queue for newly captured research awaiting triage and promotion.

**Directory lifecycle:**
- `new/` = active intake sessions and raw files
- `processed/` = active repo-ready patchsets awaiting review or Phase 2 application, plus the next-version stub
- `done/` = completed patchsets and closed intake materials
- `archive/` = archived raw session bundles after application

**Patchset version stub:** keep one next-version stub in `sources/intake/processed/` named `stub-vNN.md`. To create a new patchset, rename the stub to `vNN-topic.patchset.md` and immediately create `stub-v(NN+1).md`. The stub is the normal source of truth for the next patchset number — do not recursively scan `sources/intake/**` for routine version assignment. If the stub is missing or stale, repair it with a one-time shallow scan and take the highest `vNN` found across `processed/`, `processed/Ready/`, `processed/on-hold/`, and `done/`.

**Session rule:** one markdown session file per batch, `vNN.md`, entries separated by `---`, with referenced files kept in the same `new/` folder until applied.

**Two-phase intake model.**

*Phase 1 (preparation):* inspect files and URLs; OCR/extract/retrieve content as needed; judge relevance and destination; reconcile or propose source tracking; rename the current stub to `vNN-topic.patchset.md`; create the next stub.

*Phase 2 (application):* execute the patchset; perform file moves/copies; update `data/sources.json`; update `research/...`; keep validations thin; after the explicit patchset instructions are complete, prepend a top-line `**Done:** YYYY-MM-DD HH:MM PT` stamp and move the patchset file to `sources/intake/done/`. Do not include commit or validation status in that stamp.

**FamilySearch exports — Phase 0:** FamilySearch Family Group Record PDF exports (under `sources/FS/`) get a content-evaluation pass before Phase 1. The output is an assessment MD attached to chat (not committed) that becomes the input to a Phase-1 patchset. See `.claude/skills/familysearch-export-review/SKILL.md`.

**Patchset standard.** The patchset is an operational script that Phase 2 follows mechanically; it is also the traceability and audit record. Both purposes matter.

- A patchset must contain explicit literal operations for each edit: `str_replace` with verbatim `old_string` and `new_string`, or `new file write` with the full content body. No "Phase 2 should locate…" detective work.
- Outcomes are `promote` or `reject`. `hold-review` is not a valid outcome — if a candidate cannot be made operational, finish the resolving research, ask the user, or drop it as a documented lead.
- No conditional language inside item bodies: no "subject to user approval," "if the user prefers," or "to be confirmed."
- Quoted source material in the patchset preamble must also land in the action steps, written to a durable destination (research companion + `sources/corpus_supplement/` for rich primary extracts). Patchset markdown is process scaffolding; once Phase 2 runs, it is archived.
- Patchsets bundle the findings of a research arc — typically several turns of research → one patchset, not one patchset per turn.
- **Context-to-action proportion:** soft target of roughly 1 line of context for every 2-3 lines of operational repo content. Discovery-heavy patchsets carry more context per action; one-finding promotion patchsets carry less. Use the ratio as a sanity check, not a rule.
- Before treating any extract as "new content," check `sources/corpus_supplement/` and `sources/media/` to confirm it is not already captured.

**Promotion writing standard:** when promoting findings into `research/`, write ordinary research prose — lead with the knowledge, keep intake/processing/OCR/normalization/archival mechanics out of visible research text, keep session/process traceability in HTML comments, footnotes, validations, and patchsets. See `research-writing-style.md`.

**Traceability.** Every retained item should keep a path back to: session file, original file, source URL when available, `data/sources.json`, validation note if created, and the completed patchset in `sources/intake/done/` (or active patchset in `sources/intake/processed/` while still awaiting application).

## sources/validations/

Per-source worksheets that record what was examined, what portion, and where findings landed. Validation files are deliberately thin.

**They should answer:**
- what source was examined
- what portion was examined
- what remains unexamined or uncertain
- where substantive findings were recorded
- where the detailed execution trail lives, if a patchset exists

**Do NOT include detailed facts and findings** which should live in research and fact sheets. Validations are not a substitute for research files and should not become mini case files or patch transcripts.

**Source-validation discipline (default-on).** Every new sourceId added in a patchset gets a corresponding `sources/validations/*.md` file action by default. Skip only when the source is already covered by an existing validation file, or when the source is a single-citation quotation referenced in only one research footnote and adding nothing to a per-source worksheet. The default is *create a validation*; skipping is the exception that should be briefly justified in the patchset's source-tracking section.

**Good content here:** page/image/folio scope; concise method note when it matters; OCR or image limitations when material; whether the index was checked against the image; pointers to media files; pointers to target research files; pointer to the processed patchset when applicable.

**Citation posture:** the validation file itself should still identify the source precisely. If it states a substantive conclusion, cite it. Prefer to move substantive conclusions to the relevant subject file and leave only a pointer here.

## sources/media/

Working-reference images, crops, and associated notes keyed by `sourceId`.

**Structure:** one folder per `sourceId`. Descriptive filenames. Original capture plus detail crops as needed. Optional context/provenance note.

**File discipline:** PNG for screenshots and text-bearing captures; JPG acceptable for photographs of physical documents; files small enough for repo practicality; descriptive filenames over opaque numbering.

**Local-only masters (`_local/`):** some artifacts should not be committed. Park them in a `_local/` folder; the `.gitignore` rule `sources/media/**/_local/` keeps the bytes off GitHub while letting the folder's `README.md` ship as a stub.

Place a file in `_local/` when any of these apply:
- **Oversize** — larger than **35 MB** (project threshold; GitHub's hard limit is 100 MB).
- **Copyright-restricted** — modern in-copyright works, paywalled subscription content, licensed databases (UK Data Service EUL, etc.).
- **Privacy-sensitive** — FamilySearch tree exports with living-person data, any artifact carrying non-ancestor personal information.

Two valid locations: `sources/media/_local/` (loose staging) and `sources/media/<sourceId>/_local/` (per-source local-only masters alongside committed working-reference crops/extracts for the same source).

When a file moves into `_local/`, update that folder's `README.md` (the one exception that *is* committed) with filename, reason (size / copyright / privacy), and where the canonical master can be retrieved (URL, archive, physical repository).

Public-domain works under 35 MB are committed normally.

**Provenance:** if an image is important, ensure there is enough nearby context to understand what it is, where it came from, and what source it belongs to. If a high-resolution master lives elsewhere, keep the repo copy as the working-reference version and note the external location.

## Mandatory related rules (share path scope)
- `.claude/rules/citations.md` — both scope `sources/validations/*.md`; citation discipline applies inside validation worksheets

## See also
- `.claude/rules/data-json.md` — `sources.json` registry where every cited source has its `sourceId`
- `.claude/rules/research-writing-style.md` — promotion writing standard ("lead with the knowledge") when intake content lands in `research/`
- `.claude/skills/research-intake-prep/SKILL.md` — Phase 1 (patchset preparation)
- `.claude/skills/research-intake-apply-patch/SKILL.md` — Phase 2 (patchset application)
- `sources/README.md` — destination guidance for source-side artefacts
