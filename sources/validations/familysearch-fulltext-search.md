# Validation — FamilySearch Full-Text Search (AI-transcribed images)

**Source ID:** `familysearch-fulltext-search`

**What was examined.** Keyword full-text searches for "Francis Gurnay" and "Francis Gurney" across FamilySearch's AI-transcribed manuscript image collections, 2026-05-29.

**Scope and method.** Machine-transcribed text search (not a human index). The "Francis Gurney" spelling is dominated by an unrelated 18th-century Philadelphia merchant and the "Francis Gurney Smith" family (American noise). The English 17th-century returns under "Francis Gurnay" are the relevant set.

**Findings landed.** Recorded on `research/people/francis-gurney-of-maldon.md` (2026-05-29 corroboration subsection): Maldon, Essex borough Employment/freemen records (1661–1688) describe "Francis Gurnay, merchant and salt refine[r], born in London," corroborating Bernau's Francis of Maldon; Account Records (1624–1678) and Court Records also name him. The L-8 disposition on `research/people/g13-john-gurney-fact-sheet.research.md` points here.

**Unexamined / uncertain (leads).** Burke's *Landed Gentry* (1858) Gurney pedigree (tertiary — trace before citing). Three FamilySearch-Center / affiliate-library-restricted records not yet viewable remotely: Kent Probate 1633–1636; St Peter le Poer with St Benet Fink Poor Rate; Norfolk History Records 1701, 1825.

**Reliability note.** Transcriptions are AI-generated; verify any quoted wording against the underlying image before promoting to a fact sheet.

---

**Operational procedures** (query syntax, DGS film constructs, image-download API, browser extraction recipes) live in `.claude/skills/familysearch-fulltext-research/SKILL.md` — read that before any FTS task. This file keeps only the source-reliability record.

## Transcript-quality failure modes (each cost real time; check before believing)
- **Latin court hand transcribes as word salad**; only formulaic phrases and some names survive. A thin hit count on a Latin-era film is a transcription limit, not absence — the East Dereham 1623–1689 film yields 13 Gurney-family cards against a 17th-century reality that is certainly richer.
- **Lookalike-name false positives are systematic, not random.** Confirmed cases: *Jernegan* (lords of Costessey) → "Gurny/Gurney"; *Atturney* → "At-Gurney"; *Gurnet's Nose* (Plymouth headland) → "Gurnet"; "given unto them as well lond" → "Gurney unto the well land"; *guns* → "Gurns"; *naturall* → "Gurnaturall"; *Horne* (the Horne de Fforncett admons on the Jekkys film) → "Gorn" under a `gorn*` sweep; *Franny/Frannie* → "Gurney" (the Maldon 1677 "John Gurney" ark was a Franny false positive). Distinct real surnames that ride the same wildcard: **Gurnell** (Dorchester MA, tanner family), **Garnsey/Guernsey** (Dorchester MA), **Garner**. For the surname **Rivett** specifically, **"Almain rivet(te)s"** — a class of light armour — is a systematic false positive in muster and military records (e.g. "…an Alman Rivette a pre…" in a Norwich armour list); it is not the surname.
- **Some films carry no name-extraction at all, so a film-scoped negative there is meaningless.** The NCC will-register films DGS 008470476 (Jekkys) and the Aleyn act-book film returned zero extracted Gurnays under every `q.fullName`/`Gurn*` probe despite each holding a *known* Gurnay object (the 1471 Jekkys-211 will; the 1454 Aleyn-19 admon). These Latin registers were walked by foliation, not by name. Confirm a film actually extracts names (probe a common word scoped to the DGS) before logging any name-search negative on it.

## Venue notes (interface behaviour that shaped campaign negatives)
- **NROCAT is now an AtoM catalogue** at `http://nrocatalogue.norfolk.gov.uk/index.php/informationobject/browse?query=%22<term>%22&topLod=0&page=N` (15 rows/page; `nrocat.norfolk.gov.uk` 302-redirects here). It carries parish + year per NCC register entry and a rich deed layer. **It can 502 (Bad Gateway) server-wide** — a 502 is a venue outage, not a negative; retry a later session.
- **CCEd (theclergydatabase.org.uk) begins at the Reformation (1540)** — it cannot test any medieval cleric (e.g. the 1435 Thomas Gurnay institution). The surname search is a JS-framed AJAX form; under claude-in-chrome the results frame renders but screenshots time out after each submit (renderer freeze) — read the count/list from the frame between freezes, and clear the field with a fresh click before retyping (select-all was unreliable and produced doubled terms → false zeros).
- **DEEDS (utoronto) mirrors SCRIPTA** for the Norman charter texts: DEEDS "Assigned" dates are SCRIPTA's editorial calls, not independent datings — treat a DEEDS date and its SCRIPTA counterpart as one witness, not two.
- **Card year-lists mix document dates with stray numbers** (OCR-read folio numbers, "1890" for 1690, future years); treat them as hints. Internal date phrases can also mislead — a card's "22d Caroli" proved to be 1629 on image read.
- **Forename reliability is low in Latin entries**: the machine's "Michie/Michael Gurney 1697" read as *Mathei* (Matthew) at expert level; machine "son of John" was *et Johannes Bower*. Promote no forename or kinship from a Latin-entry transcript without an image read.

**Where campaign findings landed.** Method notes and per-pass results: `research/people/g13-john-gurney-fact-sheet.research.md` (2026-06-09/10/11 session entries). Expert image-read reports: `sources/corpus_supplement/paleo-2026-06-packet-*.md` (master images under `sources/media/*/_local/`). Subject files created from sweeps: Earsham, Costessey, Cawston, Providence, Isaac Gurney (all under `research/people/`).
