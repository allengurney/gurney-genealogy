---
paths:
  - "site/**/*"
---

# Site generation rules

Human-facing overview:
- `site/README.md`

## Purpose
`site/` is a generated/presentation layer for the public site.

## Canonical-source rule
- Do not treat `site/` as the source of truth for facts.
- Canonical data lives in `data/`.
- Canonical published prose lives in `fact-sheets/`.
- `site/` should render from upstream sources rather than fork them.

## Editing posture
- Avoid hardcoding facts in templates when the same facts should come from upstream data or markdown.
- Prefer structural/template edits over duplicating content.
- Preserve clean separation between content and presentation.

## Public URL and indexing contract
- Treat extensionless `https://genealogy.allengurney.com/...` URLs as the public canonical URL shape.
- Do not publish `.html` URLs in canonical tags, sitemaps, `llms.txt`, navigation, or internal links.
- Keep legacy and `.html` compatibility paths as server-side redirects through the generated Cloudflare `_redirects` file, not as public HTML/meta-refresh pages.
- `sitemap.xml`, `llms.txt`, and `_redirects` are generated from `_site/` by the public-site finalization step; do not hand-maintain deployed copies.
- Homepage helper files such as `fact-sheets/featured-ancestors.md` may feed templates without becoming standalone public pages.
- Run the site package or validation script after URL/indexing changes so the finalizer can fail the build on stale `.html` links, missing canonicals, sitemap drift, or meta-refresh redirects.
- In Search Console, do not treat URL Inspection's “No referring sitemaps detected” as a sitemap error or prescribe re-submitting an already successful sitemap. First verify the sitemap report and URL inclusion; that field records Google’s association/discovery history for the individual URL and can persist after re-submission. Diagnose actual crawl or indexing status separately.

## Published research topics (Misc. Topics)
- Select `research/topics/*.md` files publish to the site as lightly-formatted research notes under **Key Research → Misc. Topics** — a deliberately lighter surface than fact sheets and case files (working evidence the reader can follow, not a vetted publication).
- Publication is opt-in and canonical at `research/topics/_published-topics.csv` (`filename,displayName`). Do not hand-edit the generated copies under `site/website/key-research/topics/`.
- `scripts/sync-site-content.js` (`syncPublishedTopics`) mirrors each listed file into `key-research/topics/{slug}.md`, **adding** front matter at sync time (layout `layouts/research.njk`, permalink `/key-research/topics/{slug}.html`, `activeNav: research`, a generated ≥120-char description). The source topic files stay clean — keep the canonical/presentation split.
- `_data/publishedTopics.js` reads the same CSV to drive the `key-research/misc-topics.njk` index page; `_data/navigation.js` carries the "Misc. Topics" item under Key Research. After changing the CSV or these files, run the site build + `validate:site` so sitemap/llms.txt regenerate and nav routes are checked.

## Current state
- This directory is still placeholder-oriented until migration is complete.
- Do not build assumptions into site files that conflict with upstream repo structure.

## Mandatory related rules (share path scope)
None — `site/**/*` is scoped only by this rule.

## See also
- `.claude/rules/fact-sheets.md` — canonical published-prose origin (site mirrors from here)
- `.claude/rules/data-json.md` — canonical structured-data origin (site renders from here)
- `site/README.md` — human-facing overview
