# research/topics/

Cross-cutting problems, methods, and analytical threads that span multiple people, places, or sources.

## Use a topic file when
- the issue affects multiple subjects
- the problem is methodological
- the reasoning deserves a reusable home outside one person file
- the subject is a **low-probability alternative-candidate identity for a direct ancestor** (see below)

## Alternative-candidate identities (documented exception)
A same-name person who is a *low-probability alternative candidate* for a direct ancestor — not a true direct ancestor in our narrowly defined tree, and unlikely enough that the working argument has set them aside — lives here as a topic file, not in `research/people/`. Rationale: at low probability they are part of a research *question* about the ancestor's identity, not a formalized person in the tree. Name them consistently `{ancestor}-candidate-{descriptor}.md` ("John Gurney Candidate — …"), keep a back-link banner to the ancestor's companion and case file, and have the companion carry only a brief standing note plus a cross-link (so the companion stays focused on the ancestor). The G13 John Gurney alternative candidates (Aylesbury/A, Berkhamsted/C, London Draper/D, Ackworth, Earsham, and an "Others" comparator bucket) are the worked example. This is a deliberate narrowing of the people-vs-topics boundary, not a license to move genuine ancestors or favored identities out of `research/people/`.

## Published topics (Misc. Topics on the site)
Select topic files are published to the public site as lightly-formatted research notes under **Key Research → Misc. Topics** — less polished than a fact sheet or case file, but available so readers can follow developing research. Publication is opt-in via [`_published-topics.csv`](_published-topics.csv) in this directory (`filename,displayName`, one row per published file); the site build (`site/website/scripts/sync-site-content.js` → `syncPublishedTopics`) wraps each listed file with front matter and renders it with the research layout. Source topic files stay clean — the front matter is added at sync time. To publish a topic, add a row to the CSV; nothing else is required.

## Typical contents
- the problem
- current analytical state
- evidence and interpretation
- implications
- crosslinks

## Where this fits
See `research/README.md` for the cross-subdirectory destination guidance.

## AI / automation guidance
- `.claude/rules/research-files.md` (people, places, topics — shared and per-subdirectory discipline)
- `.claude/rules/citations.md`
