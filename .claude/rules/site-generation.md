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

## Current state
- This directory is still placeholder-oriented until migration is complete.
- Do not build assumptions into site files that conflict with upstream repo structure.

## Mandatory related rules (share path scope)
None — `site/**/*` is scoped only by this rule.

## See also
- `.claude/rules/fact-sheets.md` — canonical published-prose origin (site mirrors from here)
- `.claude/rules/data-json.md` — canonical structured-data origin (site renders from here)
- `site/README.md` — human-facing overview
