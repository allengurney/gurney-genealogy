# Spec: site build rewrites relative repo-links → published-URL / GitHub-URL

Status: draft (2026-07-04). Owner: site build (`site/website/scripts/`). Prereq for
publishing the G13 topic package (relative links are being adopted there now).

## Problem / decision

Research, topic, place, and companion markdown should link to other repo files with
**relative paths** (`../../research/places/foo.md`) so the links are clickable in local
editors (Typora, VS Code) and on GitHub's web view, and so they carry no host/owner/branch
coupling. Historically the repo hard-coded absolute
`https://github.com/allengurney/gurney-genealogy/blob/main/<path>` URLs instead, which are
**not** clickable-to-local in Typora and pin to `main`.

Decision: author intra-repo links as **relative**; the **site build rewrites them at publish
time**. This spec is that build step.

## Goal

A deterministic build transform that, for each markdown file being published, rewrites every
**relative** markdown link to:

1. the target's **published site URL** — if the target file is itself published; else
2. the **GitHub blob URL** `${GITHUB_BASE}/blob/${BRANCH}/${repoPath}` — if the target is not
   published (place files, `sources/corpus_supplement/**` and `sources/media/**` extracts,
   unpublished topics, research companions).

Absolute URLs (`http(s):`, `mailto:`), pure anchors (`#…`), and links inside code fences/spans
are left untouched.

## Where it hooks

The site content pipeline where source markdown is ingested/rendered:
`site/website/scripts/sync-site-content.js` (content sync) and/or `generate-site-data.js`,
before or at markdown→HTML. Reuse the existing dead-internal-link validation in
`finalize-public-site.js` / `validate-site.js` so a relative link resolving to a nonexistent
repo file becomes a build warning (or hard failure under a strict flag). Confirm the build
entrypoint/scripts in `site/website/package.json`.

## Config / inputs

- `GITHUB_BASE` = `https://github.com/allengurney/gurney-genealogy`; `BRANCH` = `main`
  (make both config; consider a pinned commit/permalink policy later, default `main`).
- A **published-page map**: `repoPath → publicSlug/URL`, derived from what the site actually
  publishes — fact-sheets, case files, and the topics listed in
  `research/topics/_published-topics.csv`. The build already enumerates its public outputs
  (`finalize-public-site.js`); reuse that set rather than recomputing.
- The source file's own repo-relative path `S` (to resolve relative hrefs).

## Algorithm (per published source file `S`)

1. Parse markdown links `[text](href)` (and reference-style if the repo uses them). **Skip**
   anything inside ``` fences and `` `inline code` `` spans — rewrite only real link hrefs.
2. If `href` is absolute (`^[a-z][a-z0-9+.-]*://`), `mailto:`, or starts with `#` → leave.
3. Else treat as relative: split off any `#fragment`; resolve
   `posix.normalize(dirname(S) + '/' + hrefPath)` → repo-relative target `T`.
4. If `T` is not a file on disk → record a dead-link warning (throw under strict).
5. If `T` is in the published-page map → rewrite to that page's site URL (site-root-relative
   like `/fact-sheets/…` preferred, or absolute canonical); re-append `#fragment` (map to the
   published anchor if anchors are slugified, else pass through).
6. Else → rewrite to `${GITHUB_BASE}/blob/${BRANCH}/${T}` + `#fragment`.
7. Leave link **text** unchanged — including backtick-wrapped code text (`[`path`](rel)` →
   only the href changes).

## Edge cases

- Code fences/spans never rewritten; a code span used as link *text* is fine.
- Fragment-only (`#section`) and `foo.md#anchor` — preserve the fragment.
- Images `![alt](rel)` — apply the same rule if repo-relative image links exist.
- Case: repo authored on Windows (case-insensitive FS), CI may be Linux (case-sensitive) —
  compare exact case and warn on mismatch to catch links that would 404 on the deployed site.
- `research/people/_staging/**` files are **not** published, so this step never processes them;
  their relative links serve local/GitHub use and are rewritten only when a file is
  promoted + published at cutover (which also recomputes the `..` depth for the file's new home).

## Determinism / safety

- Pure function
  `rewriteLinks(markdown, { sourceRepoPath, publishedMap, githubBase, branch, strict }) → markdown`.
  Same input → same output.
- Never mutate repo source files; rewrite only the build/output copy.

## Tests

Unit tests for `rewriteLinks`:
- published target → site URL (with and without `#fragment`);
- unpublished target (place file, corpus extract) → GitHub blob URL;
- absolute URL / `mailto:` / `#anchor` left untouched;
- link inside a code fence left untouched;
- dead relative link → warning (and throw under `strict`);
- backtick link-text preserved.
Plus a golden test over a real sample (e.g. the staged
`topics/colonial/02-weymouth-community.md`, which now carries several relative links).

## Acceptance

- The site build emits a public site with **no unresolved relative `../` links** in the HTML;
  the internal-link validator passes.
- The three staged G13 colonial topics, once published, render with working links.
- Legacy absolute-URL links (existing fact-sheets/case-files) still work; add a **follow-up** to
  migrate them to relative once this step is trusted, so the whole repo shares one convention.
