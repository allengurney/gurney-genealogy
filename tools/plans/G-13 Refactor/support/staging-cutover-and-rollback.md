# Non-destructive staging, cutover, and rollback

## 1. Objective

Develop and compare the G13 refactor without changing the current canonical
companion, public route, or research dump until explicit approval.

## 2. Isolation layers

### Research staging

```text
research/people/_staging/g13-john-gurney/
```

The site and normal ancestor resolver ignore this path unless preview mode is
explicitly enabled.

### Canonical structured graph

```text
C:\Users\allen\GitDirs\gurney-genealogy-g13-graph\
```

This is durable canonical state, not a cache. It is separate from the
repo-search cache and is retired or restored only through the documented graph
lifecycle.

### Website preview

```text
/preview/g13-refactor/
```

Preview mode is explicit, noindex, and excluded from public discovery files.

## 3. Baseline capture

Before implementation:

- Record a clean Git commit containing every dump input. If that is impossible,
  freeze an immutable content-addressed copy and manifest; a commit ref alone
  does not capture modified or untracked files.
- Hash current companion, case file, relevant topics, dump files, and media.
- Record current word/line/heading/footnote counts.
- Record current public routes and generated page hashes.
- Capture current site validation result.
- Freeze the dump inventory.

The baseline report belongs inside staged coverage material, not in the current
companion.

## 4. Development rules

- Staged files may be rewritten freely; legacy files may not.
- Research items reference staged research locations and source provenance
  during development.
- Site legacy mode remains default.
- No generated site mirror is treated as canonical.
- The **live SQLite is outside OneDrive and Git** at the dedicated GitDirs path.
  Its atomically refreshed, git-ignored `current.ndjson` recovery export lives
  in OneDrive, while versioned milestone snapshots under
  `data/context-graphs/g13/exports/snapshots/` live in OneDrive and Git. The live
  DB binary itself is never committed. (See Plan 01 §6–§7.)
- No graph-editor save bypasses validation; every accepted save writes an
  `item_revisions` row.
- The current recovery export matches the live DB revision (and destructive DB
  operations refuse to run otherwise) before the DB holds anything valuable.
- No dump file is deleted after assimilation.
- Cross-subject findings are routed through the coverage ledger.

## 5. Difference reports

Before cutover produce:

### Content coverage

- Every legacy heading/block and destination.
- Every dump finding and destination.
- Missing, duplicated, externalized, superseded, and unresolved counts.

### Evidence coverage

- Source IDs before and after.
- New sources requiring registration.
- Findings without source evidence or documented collective evidence groups.
- Sources no longer cited and explanation.
- Negative results and coverage limitations.

### Conclusion comparison

- Identity/probability changes.
- Date or chronology changes.
- Conflict-status changes.
- Open-question changes.
- Fact-sheet/case-file statements needing later review.

### Website comparison

- Route map.
- Link and footnote integrity.
- Page sizes.
- Mobile screenshots at representative widths.
- Legacy versus preview navigation.

## 6. Cutover transaction

Cutover should be one coherent reviewed patchset:

1. Verify clean intended worktree scope.
2. Copy the exact legacy companion to:
   `research/people/_legacy/g13-pre-refactor/`.
3. Store checksums and baseline metadata beside it.
4. Promote staged topics to:
   `research/people/g13-john-gurney/`.
5. Replace the legacy root companion (`g13-john-gurney-fact-sheet.research.md`)
   with a compact pointer to the promoted research library; the library's own
   intro (`00-research-library.md`) is the substantive front door (Plan 02 §6,
   revised 2026-07-13 — no separate hub).
6. Migrate the staging graph DB content to its dedicated canonical
   location/config (export from staging → restore into the canonical DB, or
   repoint config at it), refresh the current recovery export, and commit a
   versioned snapshot.
7. Change site default from legacy to package.
8. Update the small number of entry links.
9. Rebuild repository indexes.
10. Validate the canonical graph and refresh only its derived FTS, context, and
    website exports.
11. Build and validate site.
12. Run research-item/source/footnote/link validation.
13. Review Git diff before commit.

Do not combine unrelated research promotions with this cutover.

## 7. Rollback levels

### Level 1 — Site only

Switch `G13_CONTENT_MODE` or its final configuration back to `legacy`.
Research files remain available but public presentation returns to the old page.

### Level 2 — Root companion

Restore the exact legacy companion copy to the conventional root path. Leave
the staged/package directory present but noncanonical.

### Level 3 — Full refactor

Remove or quarantine the promoted package, restore the legacy companion, select
   legacy site mode, retire the canonical graph through a current recovery export
   plus a committed archive snapshot—not deletion—and rebuild repository/site
   indexes.

Raw dump and source artifacts are unchanged at every rollback level. Because the
graph is canonical, "retire" means archive-via-export, not discard.

## 8. Acceptance window

Keep:

- Legacy copy.
- Package mode switch.
- Difference reports.
- Baseline hashes.

until Allen explicitly accepts the refactor and no longer needs immediate
side-by-side comparison.

Even after acceptance, committed graph export snapshots and Git history together
provide durable recovery. The legacy copy may later move to an archive location
by a separate decision.

## 9. Definition of easy transition

The transition is easy only if:

- One configuration choice selects legacy or package website presentation.
- One root-file replacement selects legacy or package AI entry point.
- The graph can be restored from its latest export snapshot.
- No source artifact must be reconstructed.
- Public inbound URLs remain stable.
- The cutover and rollback procedures are documented and tested before use.
