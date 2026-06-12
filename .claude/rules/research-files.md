---
paths:
  - "research/people/*.md"
  - "research/places/*.md"
  - "research/topics/*.md"
---

# Research files rules — people, places, topics

Human-facing overview: `research/README.md`.

This rule governs the three working-research subdirectories. `research/case-files/` is governed separately by `research-case-files.md`.

## Shared discipline (applies to all three subdirectories)

- **A working-notes entry must carry the substance itself** — verbatim quote, concrete fact (date, place, name, relationship), transcribed extract, or explicit negative result. Do not write entries that point elsewhere ("see X for details") and require the reader to follow the pointer. The research companion is the human go-deeper layer — it must *hold* the content, not redirect. A URL or source-id may accompany the substance, never replace it.
- **A companion holds only its own subject's research.** Findings about a different ancestor go on that ancestor's file, with at most a one-sentence crosslink from the file where they surfaced (a G15 will discovered during G13 work → full treatment on the G15 companion; the G13 file records only the G13 bearing). Method notes, tooling recipes, and source-series inventories that serve multiple subjects go to a topic file or the relevant skill, not to whichever companion the session happened to be working from.
- **Synthesize by topic or finding, not by session.** Research files organize current thinking and evidence so a reader can review the state of a question — they do not document chronological effort. Integrate new findings into the existing topical treatment (an initial-finding paragraph followed by a later-dated follow-up paragraph on the same topic is fine; a stream of session diaries is not). Open each entry with enough founding context — the question being answered and why — that a reader who has not followed the work understands what the finding settles.
- Source-traceability for every new factual claim, quotation, transcription, and inferential claim.
- No research content should be inserted from intake unless tied to an existing or newly created `data/sources.json` entry.
- Findings about the subject stay in the subject file. Do not offload substantive findings into `sources/validations/` — validation files point back to research, not the other way around.
- Use topical headings over pure date-order when entries grow. Use dates inside entries when helpful.

## research/people/

The main working layer for people: ancestor companions, pre-fact-sheet ancestor files, spouses and non-ancestor subjects, candidate identities, disambiguation targets.

**What belongs here:** working notes with substance, source extracts, transcriptions, open questions, negative results, conflicting information, hypotheses, crosslinks, supporting detail that would overwhelm a fact sheet. Sustained per-ancestor argument and competing hypotheses for an individual ancestor live here (in their companion), not in a separate case file.

**Relationship to fact sheets:** if there is a paired fact sheet, this file is its evidentiary and analytical companion. Keep the two aligned; not everything here belongs in the published narrative.

**Filename conventions:**
- Paired companion: `g{NN}-{slug}-fact-sheet.research.md`
- Pre-fact-sheet ancestor: `g{NN}-{slug}.md`
- Non-ancestor subject: descriptive slug, no generation prefix

## research/places/

Place-memory narrative and analysis that sits above the canonical place registry.

**Authority split:**
- `data/places.json` is the canonical place spine.
- `data/places_detail.json` is the supplemental detail layer (rich descriptive fields).
- `research/places/*.md` holds narrative, relevance, record context, naming/normalization discussion, and unresolved place-identity questions.

**Do not duplicate the data layer.** Keep structured place attributes in the JSON layer. Keep analytical explanation and place significance here.

**Generated block discipline:** preserve any bounded generated block conventions already in use. Preserve human-authored narrative outside those blocks. Replace older generated blocks cleanly rather than piling new ones on top.

**Good content here:** why the place matters, events tied to the place, record availability/scope, naming/normalization discussion, unresolved place-identity questions, links to affected people and topics.

## research/topics/

Cross-cutting problems, methods, and analytical frames that span multiple people, places, or sources.

**Use this layer when** a question touches multiple subjects, the issue is methodological rather than purely biographical, or the reasoning deserves a reusable home outside a single person file.

**Expected content:** definition of the problem, current state of analysis, evidence discussion, implications for people and places, explicit crosslinks.

**Boundary with people files:** if the issue is still narrow and person-specific, keep it in `research/people/`. If it becomes a sustained dispute or a user-directed publication artefact (problem statement, biography), see `research-case-files.md`.

## Mandatory related rules (share path scope)
- `.claude/rules/citations.md` — both scope `research/**/*.md`; source-traceability for every new factual claim

## See also
- `.claude/rules/research-case-files.md` — adjacent layer; user-initiated publication artefacts (not the destination for sustained per-ancestor argument)
- `.claude/rules/research-writing-style.md` — finding-first prose, compactness, caveat discipline
- `.claude/rules/data-json.md` — `research/places/*.md` narrative pairs with the `data/places.json` and `data/places_detail.json` registry
- `research/README.md` — destination guidance when a finding could land in more than one subdirectory
