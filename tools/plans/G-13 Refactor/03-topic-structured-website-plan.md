# Topic-structured G13 website without graph capabilities

Status: approved design direction; revised 2026-07-05 to use a small G13
package adapter and the existing Eleventy presentation stack; revised
2026-07-06 for the Cloudflare preview-host deployment model (Claude review
with Allen).

## Decisions accepted 2026-07-06

1. The preview deliverable is a **cutover-shaped full-site zip** deployed by
   Allen to `preview.genealogy-1l3.pages.dev`. Because the preview lives on a
   separate host, route collision with the public site is not a risk: the
   preview builds the annex at its **real canonical routes** (the annex hub
   takes `/research/notes/g13-john-gurney`, topics nest beneath it, the flat
   legacy companion is suppressed). The `/preview/g13-refactor/` route tree
   from the earlier draft is dropped — it would have previewed routes that
   never ship.
2. The preview zip bakes in noindex protection (`robots.txt` disallow-all and
   a site-wide `noindex` meta), applied by the packaging step only. The
   ordinary production build and package path are untouched.
3. The package adapter is a **sync step** in the existing
   `sync-site-content.js` family, gated by a `G13_PACKAGE` environment
   selector (`off` by default). It always cleans its generated targets, and
   writes only when enabled, so an ordinary build can never consume leftover
   preview inputs.
4. Group set for the staged package today: colonial, family, research-state.
   Origin and identity groups arrive with the deferred identity/origin
   authoring pass; the manifest schema carries them without site changes.

## Decisions accepted 2026-07-05

1. The existing public G13 companion route becomes the research-library landing
   page. The canonical root companion remains a compact substantive hub; the
   topic package supplies the child pages.
2. The ordinary site build remains unchanged and legacy by default throughout
   development.
3. An explicit G13 preview command runs a small package adapter against the
   staged Markdown, then uses the existing Eleventy layouts, assets,
   finalization, and validation in an isolated preview build.
4. The adapter is a content-discovery and presentation-input step, not a second
   static-site generator. Do not merge independently rendered G13 HTML into an
   already-finalized `_site`.
5. At cutover, the same adapter reads the promoted production package and
   becomes one step in the ordinary build. The legacy/package selection remains
   available during the acceptance window for rollback.
6. Repository paths, topic identity, and public URLs remain separate. Cutover
   changes the configured package root; it does not rewrite topic prose.

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

Nested routes (the nine staged topics as of 2026-07-06; identity/origin
topics join the same pattern when authored):

```text
/research/notes/g13-john-gurney/colonial/arrival-chronology
/research/notes/g13-john-gurney/colonial/weymouth-community
/research/notes/g13-john-gurney/colonial/braintree-community
/research/notes/g13-john-gurney/colonial/frontier-rights
/research/notes/g13-john-gurney/colonial/material-life
/research/notes/g13-john-gurney/colonial/record-coverage
/research/notes/g13-john-gurney/family/wives-and-marriages
/research/notes/g13-john-gurney/research-state/source-coverage
/research/notes/g13-john-gurney/research-state/open-questions
```

Public canonical URLs remain extensionless after the existing finalization
step.

The case file keeps:

```text
/key-research/john-gurney-case-file
```

Published alternative-candidate topics move into the subject-owned annex at
cutover. Their current URLs remain as pointer stubs and static redirects until
inbound links are migrated; they do not remain a second canonical copy.

## 4. Non-destructive preview (revised 2026-07-06)

During development:

- Current site build remains legacy by default.
- The ordinary `npm run build` behavior does not read `_staging`.
- The staged package builds only through the explicit preview command, which
  sets `G13_PACKAGE=staging` for the same pipeline.

Commands:

```text
npm run build           # current production-shaped legacy build
npm run preview:g13     # cutover-shaped full-site build + noindex + zip
```

The preview build is **cutover-shaped**: the annex takes the canonical
companion route and nested topic routes (§3), and the flat legacy G13
companion is suppressed for that build. There is no separate preview route
tree. Route safety comes from host separation (the zip deploys only to
`preview.genealogy-1l3.pages.dev`), not from route renaming.

The preview packaging step post-processes the built `_site` copy with a
`robots.txt` disallow-all and a site-wide `noindex` meta before zipping, so
the preview host cannot be indexed as a duplicate. Sitemap and `llms.txt` are
generated normally (they preview the cutover output); the robots layer keeps
crawlers out at the host level.

Because the package sync step always cleans its generated targets and writes
only when `G13_PACKAGE` is enabled, an ordinary build after a preview build
returns to pure legacy output with no leftover pages.

At cutover, the ordinary build sets the same selector to the promoted
production package root and the package takes the existing canonical companion
route permanently. The legacy selection remains available through the
acceptance window for rollback.

## 5. Generic package discovery

Avoid hardcoding twenty G13 filenames into site scripts.

Extend the existing staged/final `manifest.json`; do not create a second
website-only manifest alongside the graph/topic manifest. Shape as
implemented (website fields added 2026-07-06, W0):

```json
{
  "subject": "ancestor-g13-john-gurney-1",
  "status": "staging",
  "website": {
    "title": "John Gurney Research Library",
    "hubSlug": "g13-john-gurney",
    "introFile": "topics/00-research-library.md",
    "groups": [
      {"id": "colonial", "title": "Colonial life", "order": 10},
      {"id": "family", "title": "Family", "order": 20},
      {"id": "research-state", "title": "Research state", "order": 50}
    ],
    "related": {
      "factSheetUrl": "/fact-sheets/g13-john-gurney-fact-sheet",
      "caseFileUrl": "/key-research/john-gurney-case-file"
    }
  },
  "topics": [
    {
      "topicId": "g13-colonial-arrival-chronology",
      "path": "research/people/_staging/g13-john-gurney/topics/colonial/01-arrival-chronology.md",
      "title": "Colonial arrival chronology",
      "summary": "The surviving evidence for when and how John Gurney reached Massachusetts…",
      "group": "colonial",
      "order": 10,
      "publicSlug": "colonial/arrival-chronology",
      "publicationStatus": "public",
      "researchItemIds": ["G13-RI-000001"]
    }
  ]
}
```

`topicId` remains the durable identity used by coverage and graph work.
`publicSlug` controls the website route independently. `path` stays
repo-root-relative because the graph tooling and coverage checker already
read it that way; the manifest is a machine-maintained artifact, so
mechanically rewriting `path` values at promotion is acceptable — the
no-rewrite rule protects topic **prose**, which must not contain `_staging`
or production filesystem paths. The adapter validates the manifest and
discovers the files. Origin/identity `groups` entries are added when those
topics are authored.

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
Leave that ordinary path alone during preview development. Add one small
package adapter:

```text
selected package root + manifest
              |
              v
      G13 package adapter
              |
              +--> strict manifest/file validation
              +--> annex landing input
              +--> topic-page inputs/front matter
              +--> related-topic navigation data
              +--> preview or canonical route base
              |
              v
 existing Eleventy layouts/assets/finalizer/validator
```

As implemented, the adapter is `site/website/scripts/sync-g13-package.js`,
invoked from `sync-site-content.js` exactly like the existing fact-sheet,
companion, and published-topic sync functions. It reads the selected package
root's manifest, cleans its generated target directory, and (only when
`G13_PACKAGE` is enabled) writes hub and topic Markdown with front matter
into the site source, where the ordinary Eleventy build renders them. Prose
transformations are limited to link/marker plumbing: inter-topic relative
links rewrite to public routes, repo-relative artifact links rewrite to
GitHub blob URLs (matching the existing companion convention), and graph
marker tokens become Evidence links (Plan 04) or are dropped when the marker
is not publicly exported. In package mode the same script suppresses the flat
legacy G13 companion, and `generate-site-data.js` keeps the ancestor record's
"Research notes" button pointing at the hub (same URL as today).

Requirements either way:

- Do not build an independent G13 renderer.
- Do not merge completed G13 HTML into a finalized `_site`.
- Do not hand-edit generated G13 presentation files.
- Do not make the normal build inspect `_staging`.
- Use the same layouts, navigation chrome, CSS, canonical-URL handling,
  sitemap/`llms.txt` finalizer, redirects, and validators as the rest of the
  site.

At cutover:

1. Promote the package to `research/people/g13-john-gurney/`.
2. Change the adapter source root from staging to production configuration.
3. Make the ordinary build call the adapter before Eleventy.
4. Exclude the flat legacy G13 companion from `syncResearchCompanions()` when
   package mode is selected, so only one page claims the canonical route.
5. Keep the legacy selection available through the acceptance window.

Preferred longer-term direction remains Eleventy reading canonical repository
content directly. That broader cleanup is not required for this project.

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
`llms.txt` should enumerate the hub and topic routes with compact descriptions;
it must not concatenate the full annex into one default AI payload. The hub
remains the ordinary first grounding surface.

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
- The selected package root is either the explicit staging preview root or the
  approved production root.
- Every public topic has a unique route, title, and description.
- Every public topic has a stable `topicId`, manifest-relative `path`, and
  `publicSlug`.
- All topic pages link back to the annex.
- Related local links resolve.
- Footnote anchors are valid and unique per page.
- The preview zip carries `robots.txt` disallow-all and `noindex` meta on
  every page (checked by the packaging step).
- Canonical URLs are extensionless.
- Legacy and package modes cannot both claim the same output route (package
  mode suppresses the flat companion; legacy mode writes no package pages).
- The current legacy build remains unchanged when `G13_PACKAGE` is off.
- An ordinary development build cannot accidentally consume leftover preview
  inputs (the package sync always cleans its targets).

Run the existing site build and validation from `site/website`.

## 13. Implementation phases

### W0 — Manifest extension and preview command

- Extend the existing package manifest with website metadata.
- Add strict validation.
- Add the `preview:g13` command (env-gated package sync + noindex + zip).
- Prove that the ordinary build remains behaviorally unchanged.

### W1 — Basic annex

- Generate landing page and topic pages at the canonical routes
  (package mode).
- Implement breadcrumbs and group navigation.
- Render them through the existing Eleventy presentation stack.

### W2 — Content integration

- Render staged topics and citations.
- Add related people/place/candidate links.

### W3 — Responsive/accessibility pass

- Test target widths and keyboard navigation.
- Repair tables and source strings.

### W4 — Comparison and approval

- Deploy the preview zip to `preview.genealogy-1l3.pages.dev` and review the
  annex against the live legacy companion on the production host.
- Compare ordinary-build output before and after adding the dormant adapter.
- Review with Allen.

### W5 — Cutover

- Promote the staged package and change the adapter root through configuration.
- Add the adapter to the ordinary build and suppress the flat legacy G13
  companion in package mode.
- Promote package routes to the existing companion URL.
- Update fact-sheet/ancestor links.
- Rebuild sitemap, `llms.txt`, and redirects.
- Retain the one-choice legacy rollback until final acceptance.

## 14. Acceptance

The non-graph website is successful when:

- A reader can understand where to begin without knowing repository structure.
- No topic page approaches the present companion's scale.
- All current and assimilated research is reachable from the annex.
- The fact sheet and case file remain distinct and prominent.
- The site remains ordinary static HTML on Cloudflare.
- Development did not create or maintain a second G13 rendering stack.
- Cutover requires no prose rewrite from `_staging` paths to production paths.
- Legacy mode remains available until final acceptance.
- No graph infrastructure is required to read or navigate the research.
