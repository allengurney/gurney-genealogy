# G13 refactor — coverage ledgers (Plan 02 §7 + Plan 2b §6)

Losslessness for the G13 companion/dump refactor (Plan 02 §14) is controlled by
four ledgers and a mechanized checker (§7.4; expanded per Plan 2b §8). This
directory holds the ledgers. It is **tracking metadata, not research** — do not
put findings here.

## Frozen inventory (§8 step 1)

**Cutoff commit ref:** `e782703f` (`g13 graph initial release`, 2026-07-03).

The working tree is **not fully clean** at the cutoff. Exactly one inventory
input has uncommitted working-tree modifications, so the commit ref alone would
omit it; per §8 step 1 the frozen basis for every input is content-addressed by
SHA-256 below (whole-file), and the modified file is frozen at its **working-tree**
content, not its committed blob. Nothing in the current inputs is missed.

| Input | Lines | State at cutoff | Frozen SHA-256 (whole file) |
|---|---|---|---|
| `research/people/g13-john-gurney-fact-sheet.research.md` (legacy companion) | 617 | clean @ e782703f | `41189a50f694ca749e40f3ae5cd870e8423949ad6d8de4bc50dabaf2fccef364` |
| `sources/intake/dump-files/dump-2026-07-01-g13-colonial-massbay-campaign.md` | 567 | **modified (uncommitted, +4/−3)** — frozen at working tree | `4ed9820e7684e6a58a27ccfcc6394e7c89d96abf13be0ba04b4ace74ff12b10d` |
| `sources/intake/dump-files/dump-2026-07-01-g13-colonial-round2-ward-county.md` | 466 | clean @ e782703f | `65e8ada86ad661adf2c38a8505eecbf2fd6dc1ada3eb9e4bd06aef2df120e481` |
| `sources/intake/dump-files/dump-2026-07-02-g13-colonial-round3-english-network.md` | 197 | clean @ e782703f | `1c5db3e2e16c19aa6a7731af2110189a97d901a5fb6813f657edce1812e56b57` |
| `sources/intake/dump-files/dump-2026-07-02-g13-colonial-round3-part2.md` | 264 | clean @ e782703f | `6a1810a25e29a3f4c2a182bb1dfb96afbdd6c4091ab8e42e72960b35b7d377d1` |
| `sources/intake/dump-files/dump-2026-07-02-g13-colonial-round4-arch45-and-network.md` | 681 | clean @ e782703f | `50c82ad7c00cdaa3670386b7f0b826aa2de95347e4a8646c078b70cb98744c80` |
| `sources/intake/dump-files/dump-2026-07-03-round5-G-14-to-G-37.md` | 322 | clean @ e782703f | `f5f8caa1aa02f224623c0da8c27900c9e97000957b31442f75c4f3093fc39408` |
| `sources/intake/dump-files/hobart-journal-pages-8-24-transcription.md` | 1173 | clean @ e782703f | `9afa515fd9e9723efed10586c210063f5835c5491aad48fe68f53b4eb1db3120` |

Dump image folders (`dump-2026-07-01-images/`, `dump-2026-07-02-images/`,
`dump-2026-07-03-images/`, `dump-2026-07-02-g13-colonial-round4-files/`) are
source-artifact candidates (§8, §9), not narrative findings; they are handled at
source-review time and are not enumerated as finding rows.

Material added to any input **after** this cutoff is queued for a later round,
not folded into this refactor (§8 step 1). If the modified massbay dump is later
committed, re-freeze that row against the new blob.

The live companion and dump are **not** touched by this work.

## The four ledgers

All ledgers use `topicId`, never numbered shorthand (§5) — a file rename cannot
silently change a destination.

- **`legacy-companion-map.csv`** (§7.1) — one row per legacy heading or
  independently-meaningful block, with a per-block `content_hash` (16-hex SHA-256
  over the exact frozen line span). Two shared sections ("Land and property
  records", "Community and probate records") are split into sub-blocks because
  their material fans out to more than one destination plus backlog. `disposition`
  is one of the §7.1 set (`moved`, `synthesized`, `retained_in_hub`,
  `external-canonical`, `superseded-but-preserved`, `duplicate`, `needs-decision`);
  an **empty `disposition` is the backlog signal** the checker reports.
- **`dump-findings-map.csv`** (§7.2) — one row per dump finding / input / negative
  ledger across all frozen dump files. `destination_path` carries the provisional
  §9 routing where known; `disposition` is empty until a finding is actually
  assimilated per topic.
- **`source-and-citation-map.csv`** (§7.3) — one row per (staged unit × cited
  `sourceId`): registration status in `data/sources.json`, cited role, exact-locator
  availability, media/corpus artifact path, and the findings each source supports /
  contradicts / qualifies. No staged unit may be approved with an untracked citation
  gap (§7.3). A `cited_role` of `context_only` or `cross_unit` marks a reviewed
  prose citation deliberately carried without an item link in that unit — it
  exempts the pair from the Plan 2b §8.4 prose↔graph parity gate.
- **`supplemental-surfaces-map.csv`** (Plan 2b §6.2) — one row per independently
  meaningful assertion/block of the *supplemental* source-bearing inputs: the
  published fact sheet, the case file, and the seven pre-existing G13/John topic
  files (enumerated in Plan 2b §3.3). Each row carries the block's complete
  `source_ids` set, a Plan 2b disposition (`incorporated`, `summarized`,
  `publication_only`, `external_canonical`, `superseded_but_preserved`,
  `duplicate_but_preserved`, `routed_elsewhere`, `needs_decision`), and optional
  `friction` values (§6.2 controlled set). `origin_anchor` is the block's heading
  text — the checker uses it to locate and mechanically re-parse the block's
  cited sources. Header established by Plan 2b Thread 1 (2026-07-04); rows are
  populated by Thread 2 (freeze + inventory). The map never authorizes edits to
  any origin surface.

The dump map also carries a Plan 2b `source_ids` column (empty until a finding
is dispositioned): a dump finding cannot be dispositioned without recording its
complete source set (Plan 2b §6.1).

## What is dispositioned so far

Three topics are authored (Phase P and two Phase G3 increments), all colonial:
`g13-colonial-arrival-chronology` (items `G13-RI-000001..000007`),
`g13-colonial-braintree-community` (items `G13-RI-000008..000017`), and
`g13-colonial-weymouth-community` (items `G13-RI-000018..000023`). All were
synthesized from **legacy-companion** blocks; the July dump-campaign findings feed
topics not yet authored (wives/marriages, mendon-descendants, origin, identity,
record-coverage), so the dump rows remain backlog apart from the §0 county-scope
map, routed (not assimilated) to the Weymouth place file.

Ongoing rows are added per topic by the `g13-graph-authoring` skill (§11); this
pass establishes the structure and the first real rows only.

The `g13-colonial-braintree-community` topic carries five Plan 2a prose evidence
markers (`G13-PM-000001..000005`); the `g13-colonial-weymouth-community` topic was
authored with four more (`G13-PM-000006..000009`) in the same batch as its items.
Markers are a passage→item mapping held in SQLite (schema v3); they cite no new
sources and assimilate no new legacy/dump blocks, so they add no ledger rows and
leave the citation-gap count at zero.

## Coverage snapshot (computed at freeze)

| Ledger | Rows | Dispositioned | Coverage | Backlog |
|---|---|---|---|---|
| Legacy companion map | 41 | 8 | 19.5% | 33 |
| Dump findings map | 82 | 0 | 0.0% | 82 |
| Source & citation map | 14 (2 units) | — | 0 untracked citation gaps | — |

- **Legacy:** the 8 dispositioned rows are the colonial blocks the two authored
  topics assimilated (2 → arrival-chronology, 6 → braintree-community). The 33
  backlog rows are the family/origin/identity/research-state material and the
  Billerica/Mendon/estate remainders of the two split colonial sections.
- **Dump:** 82 findings frozen, none yet assimilated into the two authored topics.
- **Citation gaps:** all 14 cited `sourceId` values across both staged units are
  registered in `data/sources.json`; zero untracked gaps.

### One losslessness flag — RESOLVED (2026-07-04)

The legacy "Land and property records — Weymouth" block also cites the manuscript
`weymouth-land-grants-book-ms` (primary corroboration of the three original East/Mill
Field grants), which the `g13-colonial-arrival-chronology` unit carried only through
Nash (secondary). Deliberate decision taken with the Weymouth-community increment:
the manuscript is now carried into the graph as `source_evidence` **G13-RI-000019**
in `g13-colonial-weymouth-community` (its natural home — the manuscript primarily
evidences John's inhabitant standing), supporting the standing finding G13-RI-000018,
which in turn `DEPENDS_ON` the arrival finding G13-RI-000006. The aligned manuscript
source is preserved per §10; the legacy-map row is updated to RESOLVED.

### Pre-existing G13 topic files not in the frozen inventory (flag, 2026-07-04)

The frozen inventory (§8 step 1) covers the legacy companion and the dump files
only. It does **not** include the seven pre-existing `research/topics/g13-john-gurney-*.md`
topic files that Plan 02 §2 counts (~24,269 words) and §9 routes. One of them —
`research/topics/g13-john-gurney-immigration-by-association.md` — materially
**overlaps the authored colonial topics**: its Weymouth-reception section already
carries, in fuller form, the inhabitant-standing, Rev. Jenner credit-tie, and
Ludden/Porter/King associate-network findings now authored into
`g13-colonial-weymouth-community`, and its land-timing section overlaps
`g13-colonial-arrival-chronology`.

Per Plan 02 §9 this topic **subdivides**; it does not move as-is: Weymouth/Braintree
associate networks → `g13-colonial-weymouth-community` / `g13-colonial-braintree-community`;
migration/reception network classes → `g13-origin-migration-network` and the surviving
(rehomed) immigration/migration-network unit; the Candidate-B / Hingham-corridor /
Bucks-as-origin threads → `g13-identity-candidate-b` and the origin-network units. The
Weymouth-community increment reconciles its slice in prose (cross-referencing the
immigration topic as the fuller migration/reception home) but does not dissolve it.

**Follow-up before cutover:** add the seven G13 topic files to the frozen inventory as
a fourth input class (or an extension of the legacy-companion ledger) and disposition
each, so the checker tracks their assimilation like the companion and dumps. Until then
their content sits outside the checker's coverage denominator, and a topic authored from
the companion (as this one was) can silently duplicate a topic-file treatment — exactly
what happened here before the prose reconciliation.
