# Topic-structured G13 website without graph capabilities

## 1. Purpose

Publish the refactored G13 research package as a coherent, mobile-compatible
static research annex before exposing graph findings or relationship navigation.

This plan intentionally excludes:

- Finding/evidence markers.
- Evidence drawers.
- Finding pages and graph JSON.
- Relationship explorers.
- Public graph navigation.

It proves the content structure and website information architecture first.

## 2. Reader-facing model

Keep the G13 fact sheet and case file in their current roles:

- Fact sheet: concise published biography.
- Case file: polished identification argument.
- Research annex: comprehensive working research, organized by topic.

The annex landing page should be named plainly, for example:

> John Gurney Research Library

It should explain that the material is working research, distinguish it from
the case file, and offer clear entry points.

## 3. Public routes

Preserve the existing companion canonical route:

```text
/research/notes/g13-john-gurney
```

Nested routes:

```text
/research/notes/g13-john-gurney/colonial/arrival-chronology
/research/notes/g13-john-gurney/colonial/weymouth-land-community
/research/notes/g13-john-gurney/family/wives-and-grizzell
/research/notes/g13-john-gurney/origin/candidate-b
/research/notes/g13-john-gurney/identity/candidate-comparison
/research/notes/g13-john-gurney/research/open-questions
```

Public canonical URLs remain extensionless after the existing finalization
step.

The case file keeps:

```text
/key-research/john-gurney-case-file
```

Published alternative-candidate topics keep their current URLs. The annex links
them as related research rather than copying them.

## 4. Non-destructive preview

During development:

- Current site build remains legacy by default.
- Staged package may build only when explicitly selected.
- Preview routes must not collide with public routes.

Suggested modes:

```text
G13_CONTENT_MODE=legacy   # current default
G13_CONTENT_MODE=preview  # build staged package under preview routes
G13_CONTENT_MODE=package  # approved cutover mode
```

Preview routes:

```text
/preview/g13-refactor/
/preview/g13-refactor/colonial/...
```

Preview pages should be `noindex` and omitted from sitemap and `llms.txt`.

At cutover, `package` becomes the default and takes the existing canonical
companion route. The legacy page can remain locally buildable or available at a
clearly labeled noindex comparison route during acceptance.

## 5. Generic package discovery

Avoid hardcoding twenty G13 filenames into site scripts.

The staged/final package has a manifest:

```json
{
  "id": "g13-john-gurney",
  "title": "John Gurney Research Library",
  "entryFile": "00-current-state-and-navigation.md",
  "groups": [
    {"id": "colonial", "title": "Colonial life", "order": 10},
    {"id": "family", "title": "Family", "order": 20},
    {"id": "origin", "title": "English origin", "order": 30},
    {"id": "identity", "title": "Identity candidates", "order": 40},
    {"id": "research-state", "title": "Research state", "order": 50}
  ],
  "related": {
    "factSheet": "fact-sheets/g13-john-gurney-fact-sheet.md",
    "caseFile": "research/case-files/john-gurney-case-file-v4.md"
  }
}
```

Each topic file supplies title, summary, group, order, and public status through
the manifest or small content metadata. The site generator discovers the rest.

This convention can support another oversized companion later without changing
the ordinary one-file companion flow.

## 6. Landing page

Required sections:

1. Short identity/current-state summary.
2. Explanation of fact sheet vs case file vs working research.
3. "Start here" cards:
   - Colonial life.
   - Family.
   - English origin.
   - Identity and candidates.
   - Open questions and source coverage.
4. Current standing and material unresolved conflicts.
5. Related case file and fact sheet.
6. Related candidate topics, people, and places.
7. Full topic index.

Cards show:

- Topic title.
- Two- or three-sentence summary.
- Current status where meaningful.
- Estimated reading scope only if useful.

Do not expose repository filenames as the primary reader interface.

## 7. Topic-page template

Each page should provide:

- Breadcrumbs.
- Topic title and summary.
- Working-research disclaimer.
- Local table of contents when useful.
- Main research content with footnotes.
- Related topics.
- Previous/next navigation within its group.
- Persistent links to annex home, fact sheet, and case file.

Desktop:

- Optional restrained group sidebar.
- Comfortable reading width.

Mobile:

- Single column.
- Group navigation above or below content.
- Tables scroll within their container.
- No hover-only interactions.
- No dependence on sticky sidebars.

## 8. Build architecture

The current sync script assumes flat `research/people/*.research.md` companions.
Extend it or replace the sync path with a package-aware generator:

```text
canonical/staged package
        |
        v
manifest validation
        |
        +--> annex landing data
        +--> topic page front matter
        +--> related-topic navigation
        +--> preview/package routes
```

Preferred longer-term direction: Eleventy reads canonical repository content
directly instead of leaving synced Markdown copies dirty. If that cleanup is
too broad for the G13 project, retain the current sync boundary but generate all
copies deterministically and never edit them by hand.

## 9. Linking changes at cutover

After approval:

- Add "Research library" to the G13 fact sheet Related Links.
- Add a research-library button to the G13 ancestor record.
- Preserve the case-file button.
- Update internal links that currently describe the one-file companion as the
  sole detailed research location.
- Preserve inbound links to the current companion route.
- Add redirects only if a previously public URL truly changes.

Do not rewrite all repository crosslinks merely because content moved. The root
hub remains a stable destination and can route readers onward.

## 10. Search and AI discovery

Without graph capabilities:

- Every topic page is included in the sitemap and `llms.txt` after cutover.
- Page descriptions are generated from topic summaries.
- The annex landing page enumerates all topics.
- Internal links connect related topics, case file, fact sheet, people, and
  places.
- Topic headings remain stable.

This provides ordinary crawler discoverability without client-side rendering.

## 11. Accessibility and mobile validation

Required checks:

- Keyboard-visible focus.
- Logical heading hierarchy.
- Breadcrumb landmarks.
- Link text understandable out of context.
- Minimum target sizes for navigation controls.
- No horizontal page overflow at 320, 360, 390, 768, and desktop widths.
- Tables and long source strings wrap or scroll locally.
- Color is not the only status indicator.
- Disclaimer and working-confidence language remain readable.

## 12. Validation

Build validation must check:

- Manifest entries resolve to files.
- Every public topic has a unique route, title, and description.
- All topic pages link back to the annex.
- Related local links resolve.
- Footnote anchors are valid and unique per page.
- Preview routes are excluded from public indexes.
- Canonical URLs are extensionless.
- Legacy and package modes cannot both claim the same output route.
- The current legacy build remains unchanged when mode is `legacy`.

Run the existing site build and validation from `site/website`.

## 13. Implementation phases

### W0 — Manifest and preview switch

- Define package manifest.
- Add strict validation.
- Add legacy/preview/package selection.

### W1 — Basic annex

- Generate landing page and topic pages under preview routes.
- Implement breadcrumbs and group navigation.

### W2 — Content integration

- Render staged topics and citations.
- Add related people/place/candidate links.

### W3 — Responsive/accessibility pass

- Test target widths and keyboard navigation.
- Repair tables and source strings.

### W4 — Comparison and approval

- Compare legacy and package content.
- Review with Allen.

### W5 — Cutover

- Promote package routes to the existing companion URL.
- Update fact-sheet/ancestor links.
- Rebuild sitemap, `llms.txt`, and redirects.

## 14. Acceptance

The non-graph website is successful when:

- A reader can understand where to begin without knowing repository structure.
- No topic page approaches the present companion's scale.
- All current and assimilated research is reachable from the annex.
- The fact sheet and case file remain distinct and prominent.
- The site remains ordinary static HTML on Cloudflare.
- Legacy mode remains available until final acceptance.
- No graph infrastructure is required to read or navigate the research.
