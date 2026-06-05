<!--
  Human-facing orientation guide. Not an AI entry point.
  AI agents in this repo are steered by AGENTS.md and .claude/rules/*; nothing
  references this file, so agents will not load it unless a human points them here.
-->

# Site & Repo Guide

A plain-English orientation to how this repository turns research files into the
public website at [genealogy.allengurney.com](https://genealogy.allengurney.com/),
and to the safeguards that keep the content trustworthy.

**Who this is for:** anyone comfortable with basic HTML/CSS and files, but new to
this repo, to website "build" tooling, and to the jargon around it. You do not
need prior experience with site generators or deployment.

> Looking for the developer-level reference (every template, every field)? That
> lives in [`site/website/README.md`](site/website/README.md). This guide is the
> on-ramp; that one is the manual.

---

## 1. The big idea in one minute

The website is a **static site**: a folder of plain `.html`, `.css`, and image
files. There is no live database and no server-side code running when a visitor
loads a page — the pages are pre-built and simply handed out as-is. That makes
the site fast, cheap, secure, and easy to archive.

Those finished HTML files are **not written by hand**. Instead:

1. The genealogy facts live as structured **data** and as **Markdown** documents.
2. A tool called **Eleventy** reads that content and stamps it into HTML pages
   using reusable page **templates**.
3. The finished folder is **uploaded** to the host (Cloudflare Pages).

The guiding principle is **separation of content from presentation**: *what* the
site says (the facts and the prose) is kept apart from *how* it looks (the
templates and CSS). Change a date once in the data, and every page showing that
date updates on the next build.

```
   data/ + fact-sheets/ + research/        →    Eleventy build    →    _site/        →    Cloudflare Pages
   (the content: JSON + Markdown)                (the assembler)         (finished HTML)     (the public host)
```

---

## 2. The technologies, and why each was chosen

| Technology | What it is | Why it's here |
|---|---|---|
| [**Eleventy** (a.k.a. 11ty)](https://www.11ty.dev/) | A *static site generator* — it merges content with templates to produce HTML. | Simple, no heavy framework, no lock-in. It reads ordinary files and outputs ordinary HTML. |
| [**Nunjucks**](https://mozilla.github.io/nunjucks/) (`.njk` files) | A *templating language*: HTML with placeholders and loops (`{% for ... %}`, `{{ value }}`). | Lets one template render hundreds of records. The ancestor table is one template looped over all ancestors. |
| [**Markdown**](https://commonmark.org/help/) (`.md` files) | A simple plain-text format for prose (`# Heading`, `**bold**`). | Authors write readable text without touching HTML tags. The fact sheets and case files are Markdown. |
| [**markdown-it**](https://github.com/markdown-it/markdown-it) (+ footnote/attrs plugins) | The engine that converts Markdown into HTML during the build. | Adds footnotes and other niceties the genealogy prose relies on. |
| [**Node.js**](https://nodejs.org/) + [**npm**](https://docs.npmjs.com/about-npm) | The runtime that executes Eleventy and the build scripts, and its package manager. | Standard, free tooling. `npm` installs Eleventy and runs the build commands. |
| [**JSON**](https://www.json.org/) | A structured data format (lists of records with named fields). | The canonical ancestor / place / source data is JSON, so it's machine-readable and consistent. |
| [**Cloudflare Pages**](https://pages.cloudflare.com/) | The web host. | Free static hosting with a global CDN, custom domain, and redirect support. |
| [**Git**](https://git-scm.com/) / [GitHub](https://github.com/) | Version control — a tracked history of every change. | Every edit is recoverable; nothing is lost. |

### Why Markdown for authoring (the content/code split)

Genealogy prose is written in `.md` files instead of HTML for three reasons:

- **Readability** — a Markdown file reads cleanly even before it becomes a web
  page; you can open it in any text editor (the author uses [Typora](https://typora.io/)).
- **Durability** — the words are not tangled up in `<div>`s and styling. If the
  site's look is redesigned, the content files don't change at all.
- **Reuse** — the same Markdown fact sheet feeds the website *and* stays the
  canonical published narrative in the repo. One source, no copy-paste drift.

---

## 3. How content flows (the repo layers)

Content lives "upstream" in canonical files and is **mirrored downstream** into
the site at build time. You edit upstream; the site regenerates.

| Layer | Folder | Role |
|---|---|---|
| **Canonical data** | `data/` | The single source of truth: `ancestors.json`, `places.json`, `places_detail.json`, `sources.json`. |
| **Published narratives** | `fact-sheets/` | The polished per-ancestor write-ups (Markdown). |
| **Research layer** | `research/` | Working knowledge — companions, places, topics, case files. |
| **Presentation** | `site/website/` | Templates, styles, and build scripts. **Generated copies land here — do not hand-edit them.** |

**Key rule:** never fix a fact by editing files inside `site/`. The build
overwrites them. Fix it upstream in `data/`, `fact-sheets/`, or `research/`, then
rebuild.

---

## 4. Running a build

All commands run from inside the site folder, so start there:

```bash
cd site/website
```

### One-time setup (and only when dependencies change)

```bash
npm ci           # install the exact dependencies recorded in package-lock.json
```

`npm ci` ("clean install") deletes `node_modules/` and reinstalls every
dependency from scratch to match the lockfile exactly. You need it **once** when
you first set up the repo on a machine, and again **only** if `package.json` or
`package-lock.json` changes (i.e., a dependency was added or upgraded).
`npm install` does the same job but may update the lockfile; `npm ci` is the
safer "give me exactly what's pinned" choice.

**You do _not_ need to run this after editing content.** Editing a fact sheet,
research file, or data file changes nothing about the dependencies, so
reinstalling them every time just adds a slow, pointless step.

### The everyday workflow — after editing an `.md` (or any content)

```bash
npm run package      # build + validate + zip, in one command
```

Then upload the new dated zip from `site/website/dist/` to Cloudflare Pages.
That's the whole loop: **edit → `npm run package` → upload.** No `npm ci` in
between.

> So is your current `npm ci` + `npm run package` "wrong"? It works and is safe —
> it just does extra work. The `npm ci` is only earning its keep right after a
> dependency change; for ordinary content edits you can drop it.

### All the commands

These are defined in `site/website/package.json`. Each one *includes* the ones
above it, so you only ever run the single command that matches your goal:

| Command | What it does | When to use |
|---|---|---|
| `npm run build` | Builds the finished site into `_site/`. | Quick local build, no checks or zip. |
| `npm run validate` | Runs `build`, then the safety checks (see §6). | Confirm an edit is clean without packaging. |
| `npm run package` | Runs `validate`, then zips `_site/` into `dist/`. | **Publishing — the everyday command.** |
| `npm run serve` | Builds, then serves a live local preview in your browser. | Previewing while you write. |
| `npm run watch` | Rebuilds automatically as you save files. | Long editing sessions (pair with a browser refresh). |

In short: `package` ⊇ `validate` ⊇ `build`. Running `npm run package` already did
a build and a validation — there's no need to run those separately first.

### What `npm run build` actually does

The build is a small pipeline of steps run in order. Each is a Node script under
`site/website/scripts/`:

1. **`sync:content`** — copies the canonical Markdown (fact sheets, research
   companions, key case files) *into* the site folder so Eleventy can see them.
   This is the "mirror downstream" step.
2. **`data:generate`** — reads the canonical JSON in `data/` and produces the
   site's own data files (the ancestor list, the places catalog, the sources
   catalog) shaped the way the templates expect. This is where, e.g., each
   ancestor automatically gets a "Fact sheet" button if a fact sheet exists.
3. **`clean`** — deletes the old `_site/` output so nothing stale lingers.
4. **`eleventy`** — the main event: Eleventy reads every template and Markdown
   file and writes finished HTML into `_site/`.
5. **`finalize-public-site`** — post-processing for the public web: rewrites
   links to clean extensionless URLs, adds the correct `canonical` tag to each
   page, and generates `sitemap.xml`, `llms.txt`, and the `_redirects` file. It
   also **fails the build** if it finds problems (see §6).

The result is the `_site/` folder — the actual website, ready to deploy.

### Deploying

`npm run package` (above) writes a dated zip into `site/website/dist/`. To
publish, upload that zip to **Cloudflare Pages**. There is no automatic deploy on
commit — publishing is always a deliberate manual upload, so nothing goes live
until you upload it.

---

## 5. Guardrails — what keeps the content honest

This repo treats correctness as a first-class concern. Three kinds of safeguards
work together.

### Rules — standing instructions for AI assistants

The files in `.claude/rules/` encode how AI must behave when editing each part of
the repo: citation discipline, how facts are sourced, what belongs in a fact
sheet vs. research notes, how dates are written, and so on. They load
automatically based on which file is being edited. The full catalog is in
[`AGENTS.md`](AGENTS.md) §3. These are *content-quality* guardrails — they exist
so AI-assisted edits match the project's evidence standards.

### Skills — repeatable expert workflows

The folders in `.claude/skills/` are step-by-step procedures for recurring,
multi-step jobs (e.g., reviewing a FamilySearch export, processing new source
material through "intake," running a citation audit). They keep complex tasks
consistent each time they're done. Catalog also in [`AGENTS.md`](AGENTS.md) §3.

### Validation — automated checks the build enforces

Two scripts act as automated reviewers and will **stop a bad build**:

- **`finalize-public-site.js`** rejects pages that would harm the public site:
  leftover template code, `.html` links that should be clean URLs, missing or
  wrong `canonical` tags, pages absent from the sitemap, more than one main
  heading per page, etc.
- **`validate-site.js`** (`npm run validate`) checks the *data*: that every
  ancestor button points to a real page, that navigation links aren't broken,
  that the generated catalogs aren't empty, and that ancestor↔place links line
  up in both directions. Hard problems are *errors* (build fails); softer ones
  are *warnings* (build continues, but you're told).

Together: the **rules** govern how content is written, the **skills** govern how
big jobs are done, and **validation** is the automated gate that catches mistakes
before they reach the web.

---

## 6. Quick reference

| I want to… | Do this |
|---|---|
| Fix a fact (date, place, name) | Edit the canonical file in `data/` or `fact-sheets/`, then rebuild. |
| Edit an ancestor's narrative | Edit the `.md` in `fact-sheets/`. |
| Change the site's look | Edit the CSS / templates in `site/website/`. |
| Preview locally as I edit | `cd site/website && npm run serve`. |
| Build the finished site | `cd site/website && npm run build`. |
| Check for problems | `npm run validate`. |
| Publish | `npm run package`, then upload the `dist/` zip to Cloudflare Pages. |

**The one rule to remember:** edit content *upstream* (`data/`, `fact-sheets/`,
`research/`); never hand-edit generated files under `site/`. The build is the
bridge between the two.

---

## Mini-glossary

- **Static site** — a website made of pre-built files with no live server logic.
- **Static site generator** — a tool (here, Eleventy) that builds those files
  from content + templates.
- **Build** — the act of running that tool to produce the finished site.
- **Template** — a reusable page skeleton with placeholders, filled in per record.
- **Canonical source** — the one authoritative copy of a fact; everything else
  is generated from it.
- **Deploy** — copying the finished site to the host so the public can see it.
- **CDN** — a network of servers that cache the site close to visitors for speed.
