# Prompt — cutover (Opus) — GATED, this is the finish line

**Do not run this next.** Cutover promotes the staged package to canonical and
switches the site (Plan 02 §15, support/staging-cutover-and-rollback.md §6). It is
the *last* step, not something that follows 2a. It is **independent of and later
than** the G4 editor polish. Run it only when every gate below is green.

## Gate — all must hold before cutover
- The staged topic package is substantially complete (Plan 02 §4) — **satisfied
  2026-07-09: all 25 planned units are authored and `increment-complete`.**
- The root hub (`g13-john-gurney-fact-sheet.research.md` replacement) is authored
  (Plan 02 §6; 2,500–4,000 words, substantive current-state).
- The coverage checker reports **zero un-dispositioned items and zero untracked
  citation gaps** across all three ledgers (Plan 02 §7.4, §14).
- The difference reports (content / evidence / conclusion / website) are produced
  (support doc §5) and reviewed.
- Graph `validate` is 0-error; recovery export and latest snapshot match the live
  DB revision.
- Allen has explicitly approved the cutover.

Until then, keep authoring topics (g13-graph-authoring skill), building ledgers,
and leaving the live companion and public route untouched (Plan 02 non-destructive
invariant).

## Resolved decisions (Allen, 2026-07-10)

The two decisions this gate was waiting on are taken:

1. **Fact-sheet probability → ~65%.** The fact sheet's "roughly a sixty percent
   probability" (n8, the parentage highlight, and narrative para 2) is updated
   to match the case file's and topic files' ~65%. Execute it **within the
   cutover change** (step 4b below) — the fact sheet is a frozen Plan 2b input,
   so an earlier edit breaks the §8.1 frozen-hash gate. The edit carries four
   follow-ons in the same reviewed change:
   - a dated re-freeze note + new whole-file hash on the Plan 2b frozen-inventory
     record (`coverage/README.md` supplemental table);
   - resolution of the `confidence_mismatch` friction annotations on the two
     fact-sheet supplemental rows (parentage highlight, narrative para 2), the
     case-file s11 row, and the legacy "Working Hypotheses" row;
   - a revision (apply-graph-edits.py) to `G13-RI-000178` in
     `g13-identity-assessment`, whose statement currently asserts that the fact
     sheet lags the case file — after the edit that assertion is stale;
   - the matching statement in the assessment unit's topic prose.
2. **Identity units stay `public`.** All 25 units already carry
   `publicationStatus: public` in the staging `manifest.json`; no change is
   required. Cutover proceeds with the identity units public.

## Prompt (only when the gate is green)

```
Work in main. Execute the G13 cutover as one coherent reviewed change, per Plan 02
§15 and support/staging-cutover-and-rollback.md §6. Confirm every gate condition
first and stop if any is not met.

1. Verify the intended worktree scope is clean and bounded to this cutover.
2. Copy the exact legacy companion to research/people/_legacy/g13-pre-refactor/;
   store checksums + baseline metadata beside it.
3. Promote staged topics from research/people/_staging/g13-john-gurney/ to
   research/people/g13-john-gurney/.
4. Replace the root companion with the approved hub.
4b. Apply the approved publication edit (Resolved decisions above): update the
    fact sheet's "roughly a sixty percent probability" to the case file's ~65%
    in n8, the parentage highlight, and narrative para 2; then the re-freeze
    note + new hash, the three friction-annotation resolutions, and the
    RI-000178 graph + prose revision.
5. Migrate the staging graph DB content to the canonical location/config (export
   from staging → restore, or repoint config), refresh current.ndjson, and commit a
   versioned snapshot.
6. Switch the site default from legacy to package mode; update the few entry links;
   keep public inbound URLs stable.
7. Rebuild repo indexes; validate the canonical graph; refresh only its derived
   FTS/context/website exports.
8. Build and validate the site; run research-item / source / footnote / link
   validation.
9. Keep the legacy copy, the mode switch, the difference reports, and baseline
   hashes in place (rollback levels 1–3 must remain available) until Allen accepts.
10. Review the full Git diff before committing. Do not combine unrelated research
    promotions with this cutover.
```

## SEO / index-readiness checklist (validated 2026-07-11 against the staging build)

The staged annex is already index-ready; a `G13_PACKAGE=staging npm run build`
was audited on 2026-07-11 and every check below passed. Re-verify the same
checks on the **production** build at cutover — they are cheap and mechanical.

Validated (staging build, graph revision 179):

- **Sitemap**: `_site/sitemap.xml` carried all 509 pages including the annex —
  hub, 25 topic pages + explorer, 103 evidence pages, 194 finding pages. Zero
  `.html`-suffixed URLs (extensionless canonical shape throughout).
- **llms.txt**: includes the full annex (hub, topics, all findings + evidence).
- **Canonicals**: exactly one per page, extensionless, injected by
  `finalize-public-site.js`; spot-checked on finding pages and the explorer.
- **Robots**: site `robots.txt` is allow-all (incl. AI crawlers); every page
  carries `robots: index,follow`; no `noindex` anywhere in a plain build.
- **Meta descriptions**: present and ≥120 chars (validator warns below that).
- **Redirects**: `_redirects` 301s every `.html`/`index.html` variant to the
  canonical URL (651 rules), so no duplicate-content URLs resolve 200.
- **Crawl graph**: topic pages ↔ evidence pages ↔ finding pages ↔ hub are all
  interlinked server-side (the explorer app is JS-only, but every item it shows
  has a crawlable permanent page, and the hub/menu link both).

Cutover deployment path (the part that CANNOT come from the preview pipeline):

- **Deploy `G13_PACKAGE=production npm run package`** (indexable zip in
  `dist/gurney-genealogy-site-<date>.zip`). **Never deploy the
  `preview:g13` zip to production** — `build-g13-preview.js` bakes
  `noindex,nofollow` meta into every page and a disallow-all robots.txt.
  Quick check on the deploy zip: `robots.txt` must be allow-all and no page
  may contain `noindex`.
- `production` mode reads `research/people/g13-john-gurney/` (the promoted
  package location) and also enables the two Key Research menu items
  (`_data/navigation.js` gates on the same env var).

Post-deploy actions (manual, after DNS/Pages serve the new build):

- Google Search Console: submit the updated `sitemap.xml`, then URL-Inspect +
  request indexing for the hub and explorer. Expect "Crawled — currently not
  indexed" lag on deep finding pages (authority-driven, see the indexing-
  warnings note); the sitemap + interlinking are correct, so no action beyond
  waiting is required.
- Bing Webmaster Tools: submit the sitemap (Bing also honors IndexNow if ever
  wanted; optional).
- Keep the `preview.genealogy-1l3.pages.dev` host noindexed (it already is via
  the preview zip) and the `genealogy-1l3.pages.dev` duplicate non-canonical.

Optional (site-wide, not annex-specific; note only):

- `sitemap.xml` has no `lastmod` values and pages carry no `og:image` /
  Twitter-card tags — both are site-wide characteristics that predate the
  annex, optional for indexing, and better handled as a separate site task.
