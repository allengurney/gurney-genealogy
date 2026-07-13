# G13 Cutover — Post-Acceptance Cleanup Manifest

**Status:** do not act on this manifest until Allen has accepted and exercised
the G13 cutover. It is an organizational-hygiene list, not a storage-recovery
exercise. Planning documentation, the promoted library, its coverage ledgers,
and all rollback material remain in place through acceptance.

## Retain through acceptance

| Material | Recommended disposition after acceptance | Rationale |
|---|---|---|
| `research/people/_legacy/g13-pre-refactor/` | Retain in the legacy location, with its `BASELINE.md`. | It is the exact pre-cutover companion and supports rollback levels 1–3. It remains searchable by an explicit legacy path. |
| `research/topics/g13-*.md` and other former G13 topic files | Move, only after acceptance, to `research/topics/_legacy/g13-pre-refactor/`; add a short legacy banner and make ordinary repo-search ranking demote `_legacy/` paths while retaining explicit legacy search. | Preserve old inbound paths and research history while preventing an obsolete topic from competing with the promoted library in ordinary results. Do not delete. |
| `data/context-graphs/g13/exports/website/` | Retain as the protected pre-cutover derived website export until the rollback window closes; then move to an external long-term archive with the staging database. | Windows/OneDrive protects this directory against deletion and it is a usable presentation rollback point. |
| `C:\Users\allen\GitDirs\gurney-genealogy-g13-graph\g13-staging.sqlite`, `staging-archive/`, and `staging-exports/` | Move to the external long-term G13 archive; do not delete. | The old staging graph is a distinct pre-cutover database state and remains needed for audit and rollback evidence. |

## Remove or rehome after acceptance

| Material | Recommended disposition | Rationale |
|---|---|---|
| `tools/tmp-g13-cutover-ops.json` | Delete now after the graph edit is verified. | It is a one-time, already-applied operational input, not research evidence. |
| `data/context-graphs/g13/context.json` | Delete after acceptance if no documented tool consumes it; recreate on demand. | It is a transient exhaustive context export, distinct from the canonical SQLite graph, FTS, snapshot, and website export. |
| `data/context-graphs/g13/exports/website-r244/` | Delete after acceptance. | It is the one-time alternate revision-244 export made while the protected pre-cutover `website/` directory could not be replaced. `website-current/` is the canonical derived location. |
| `research/people/g13-john-gurney/coverage/g13-phase-p-seed.ndjson` | Move to the promoted package's legacy or implementation archive, not delete. | It records the original graph-seeding operation; the SQLite graph and versioned snapshots are canonical, but the seed is useful implementation provenance. |
| Site build output (`site/website/_site/`, generated annex and graph asset copies) | Delete/rebuild through the normal site build workflow when no longer needed. | These are generated presentation artifacts, not research content. |
| Obsolete scratch, backup, and duplicate reports discovered during the acceptance review | Classify individually: delete only reproducible temporary outputs; otherwise move to the long-term archive or legacy location. | Avoid accidental loss of research provenance; no broad cleanup sweep is authorized by this cutover. |

## Preserve

All G13 planning documents, `support/staging-cutover-and-rollback.md`, baseline
hashes, difference reports, the promoted library, and versioned graph snapshots
remain. Any later move must preserve a searchable legacy path and must not break
public inbound URLs.
