# AGENTS.md

**Universal entry point for all AI agents in this repo.** Codex reads by convention. Claude Code reads via `@AGENTS.md` import from `.claude/CLAUDE.md`. ChatGPT / web LLMs are seeded by initial prompt. Copilot `.github/copilot-instructions.md` points here.

---

## Multi-AI compatibility

**All rules and skills in this repo are AI-agnostic content.** Path-scoping (`.claude/rules/*.md` with YAML `paths:` frontmatter listing glob patterns) is a Claude Code auto-load optimization. The canonical discovery mechanism for any AI is (a) explicit cross-references inside each rule file and (b) the enumeration of rules and skills below in §3.

Any AI reading a rule may consult its `paths:` field manually and observe the same convention: load the rule when working on a file matching one of those globs. The convention is just YAML — readable by any LLM.

---

## 0. Session start

On new session: read `AGENTS.md` and `README.md`. For a specific ancestor, read both `fact-sheets/g{NN}-{slug}-fact-sheet.md` and `research/people/g{NN}-{slug}-fact-sheet.research.md`.

## 0a. Match context to task shape

For routine edits, open only files the task requires. Do not pre-load full source corpora, all fact sheets, all research companions, or unrelated generations unless the task specifically calls for them. Read the relevant directory `README.md`. The READMEs carry destination guidance — where a finding belongs. Read the matching path-scoped rule(s) auto-load when you open a target file. Trust them; re-read only on a genuine question.

**`repo_search.py` is the default — and first — tool for reading-in repo content; use it for any repo lookup — including finding *where a known string lives*: `repo_search.py locate "<string>"` returns the real `path:line` (add `--context N` for the surrounding lines, e.g. to grab an edit block; `--path <dir>` triages a scratch/tmp directory live).** Reaching for `grep`/`Grep` on repo content is itself the signal you should have run `repo_search`: `locate` is the sanctioned precise-locator, so there is no exact-literal-target or existence-check exception for grep. `Glob` remains fine for pure filename matching. **To go deep on a single source file — a corpus extract, an intake transcript, a freshly OCR'd text — use `repo_search.py infile <file> --terms ...`:** it returns fuzzy, context-windowed passages from that file (OCR- and line-wrap-tolerant), so reach for it instead of reading a long source file end-to-end to find what it says about a name or place. **Default to running this tool many times per task, not once.** A typical fact-sheet, research, or audit task warrants *several* `search`/`map`/`infile`/`locate` calls — when grounding the subject, before each new claim, before each edit anchor, and before concluding a negative result — not a single up-front query. If you have done substantive work on a subject without consulting the tool, that is the under-use signal: stop and run it. The cost of an extra query is trivial against the cost of duplicative or unstaged work. **Ground before acting:** before online discovery, drafting, editing, or auditing, first establish what the repo already knows about the subject with `repo_search.py` and the subject's companion/place/topic file; work the *delta after the known knowns*. This is the single biggest guard against duplicative work. Sequential full-file reads of large directories should be rare.

**Design before searching — not optional.** For any non-trivial online (or repo) discovery, apply the two gates in `.claude/skills/online-discovery-strategy/SKILL.md` *before* running queries, then adapt as results return: (A) stay anchored to the objective, not the tool you are in, and treat a miss as a signal to pivot and widen outward, not a dead end; (B) characterise the source (capture fidelity × spelling/language × index model) and match terms to it — pulling name variants from `data/search-variants.json` (era-aware; conservative→broad→all as a scalpel), wildcarding where the rendering may break (internal/multi-position, geography-tuned), and dropping to token/transitive anchoring (parish + rare in-law co-occurrence, name omitted) when the name may not survive as a searchable string. Running one exact-name query and reading its count as truth is the failure this guards against; a low or zero result is unverified until breadth is confirmed.

For context-heavy repository discovery, use `.\.venv\Scripts\python.exe tools\repo_search.py`: let local tools search, rank, group, and deduplicate broadly; read the compact manifest first, then expand the most relevant saved volumes or results. **Read a staged result — a top manifest locator or an `expand`ed volume — before reaching for raw Grep on the same question; the file you need is usually already staged (including the relevant place/topic companion, with its footnotes attached).** Efficiency must not reduce required scope, suppress conflicting or negative evidence, or substitute ranking for verification. Search packages preserve the exhaustive result and exact-match ledgers outside OneDrive.

For repo-search command choice and examples, use `tools/repo_search_README.md`; this entry point only sets routing.

For canonical ancestor, place, source, or record-ID lookup, search `data/indexes/` before opening the larger canonical JSON files.

For `research/future-research/research-leads.csv`, do not read or rewrite the full CSV for single-lead work. Use `python tools/research_leads.py context L-123`, `priority`, `get`, `update`, `close`, or `audit` instead. Read the full CSV only for broad catalog audits, schema changes, or when the lead CLI cannot answer the task.

When in doubt for an edit task, open the target file first and let it tell you what adjacent files matter.

---

## 1. Identity

User: Allen Lawrence Gurney, Portland OR. Dual projects: biography of Brig. Gen. William Gurney (1821–1879, G6); 37-generation genealogy site at genealogy.allengurney.com. Not a professional genealogist; accepts reasoned deduction from indirect evidence when noted. Reviews output critically; corrections are authoritative and incorporated immediately.

---

## 2. Repo map

```
data/            ancestors.json, places.json, places_detail.json, sources.json (canonical structured data)
                 familysearch-ids.csv (FS PID-to-generation crosswalk)
fact-sheets/     g{NN}-{slug}-fact-sheet.md (PUBLISHED narrative only)
research/
  people/        g{NN}-{slug}-fact-sheet.research.md (companion to a fact sheet)
                 g{NN}-{slug}.md (pre-fact-sheet staging)
                 {descriptive-slug}.md (non-ancestor subjects)
  places/        one file per geographic locus, narrative above the data/places.json registry
  topics/        cross-cutting analytical/methodological files; also low-probability
                 alternative-candidate identities; _published-topics.csv designates site-published topics
  case-files/    user-initiated in-depth publication artefacts (problem statements, biographies)
  future-research/  research-leads.csv master leads catalog + single-subject lead inventories
  log/           historical operational notes; not currently maintained
sources/
  corpus/        full-text source extracts (text preferred over PDF)
  corpus_supplement/  additional searchable extracts; canonical home for rich primary text
  intake/        new/ (raw queue), processed/ (active patchsets + stub), done/ (completed), archive/
  media/{id}/    images, crops, sidecar transcriptions; _local/ subdir for oversized/restricted
  validations/   per-source worksheets — thin; findings live in research files
site/            Eleventy source for the public site; generated from data/ + fact-sheets/
tools/           lineage-specific utilities and exploratory artifacts
```

For destination guidance ("where does this finding go?"), see the directory README (`data/README.md`, `research/README.md`, `sources/README.md`, `fact-sheets/README.md`).

## Canonical locations

- `data/` = canonical structured spine (`ancestors.json`, `places.json`, `places_detail.json`, `sources.json`)
- `fact-sheets/` = published ancestor narratives
- `research/` = working knowledge layer — see `research/README.md` for destination guidance
- `sources/` = source artefacts, intake queue, validations — see `sources/README.md` for destination guidance
- `site/` = generated/presentation layer (do not hand-edit; the build mirrors from `fact-sheets/` and `data/`)

---

## 3. Rules and skills — explicit enumeration

Any AI working in this repo should consult these files based on the work being performed.

### Rules (`.claude/rules/`)

| File | Path scope | Purpose |
|---|---|---|
| `citations.md` | `fact-sheets/*.md`, `research/**/*.md`, `sources/validations/*.md` | Citation and sourcing discipline — footnote placement, source-ID alignment, Wikipedia and tertiary-source posture, omnibus footnote limit. |
| `continual-improvement.md` | always-loaded | When to update a rule, when not to, consolidation passes, avoid reactive absolutes, bias toward restraint, online-availability tags for research leads. |
| `data-json.md` | `data/*.json` | Edit discipline for the structured data spine. |
| `fact-sheets.md` | `fact-sheets/*.md` | Published-narrative discipline — plain-English contract, Highlights bullet shape, Vitals overflow, citation rigour, finding-in-main / sources-in-footnote. |
| `git-onedrive-codex.md` | always-loaded | OneDrive working-tree health checks. |
| `research-case-files.md` | `research/case-files/*.md` | Case files are user-initiated in-depth publication artefacts; AI does not promote findings here without direction. |
| `research-files.md` | `research/people/*.md`, `research/places/*.md`, `research/topics/*.md` | Shared research-file discipline plus per-subdirectory rules for people, places, topics. |
| `research-writing-style.md` | always-loaded | Research prose style — lead with finding, compactness, caveat discipline. |
| `site-generation.md` | `site/**/*` | Site is generated/presentation only; canonical content lives upstream. |
| `sources.md` | `sources/intake/**`, `sources/validations/*.md`, `sources/media/**` | Intake (patchset standard), validation worksheets, media file discipline. |

Repo file resolution (lookup order, direct-open known paths, destination discipline) is documented in §4 below rather than as a separate rule file.Bind rules to nested artifacts and subtasks

A larger task can contain smaller artefacts with their own rules. Apply the rule for the thing being authored, even when it is embedded inside another deliverable. Proposed `sources/validations/*.md` content inside an intake patchset follows the validation rules, not the patchset-writing style. Proposed `research/...` content inside an intake patchset follows the research rules. **Proposed `fact-sheets/*.md` content inside an intake patchset follows `.claude/rules/fact-sheets.md`** — including the Plain-English reader contract, the Read-as-if-written-all-at-once rule, the Story-led-not-source-led rule, and the Dates-in-years rule. Git, branch, commit, push, or PR work remains governed by `git-onedrive-codex.md` even when publication is only the final subtask of a larger task. Do not let the outer task type override the inner artefact or workflow rule.

**Read the nested rule before drafting the nested content.** Path-scoped rules auto-load only when the file at the target path is opened. When a patchset (or any outer artefact) proposes content that will land in a path-scoped destination, the nested rule must be explicitly read at the start of the drafting step, not relied on from memory. This is the operational requirement behind the bind-to-nested-artefacts principle — a rule cannot be applied if it was never seen.

### Skills (`.claude/skills/`)

Skills follow the Agent Skills open standard ([agentskills.io](https://agentskills.io)) and work cross-tool. Skill discovery in this repo is by explicit invocation or by enumeration here.

| Skill folder | Purpose |
|---|---|
| `familysearch-export-review/` | Phase 0 review of a FamilySearch Family Group Record PDF export against existing repo knowledge; produces an assessment MD as input to Phase 1. |
| `familysearch-fulltext-research/` | Operational recipes for FamilySearch Full-Text Search: query syntax/URL parameters, DGS film constructs, full-resolution image download API (presigned S3 + TLS note), shadow-DOM extraction, failure modes. Read before any FTS task. |
| `familysearch-tree-updates/` | Compose updates to push back to the FamilySearch tree based on repo findings. |
| `findmypast-record-search/` | Operational recipes for FindMyPast indexed record sets (parish baptisms, banns & marriages, burials): URL-parameter search, dataset slugs, wildcard/spelling tactics, the spouse-search trick, reading results without opening paywalled images, coverage caveats. Read before any FindMyPast record-search task. |
| `online-discovery-strategy/` | Source-agnostic search *design* — the two reasoning gates (objective, source) and cause-matched technique selection (name variants / wildcarding / token-anchoring). Read before designing any non-trivial online or repo search; the FS/FMP skills hold the per-source mechanics. |
| `paleography-analysis/` | Reusable paleographic image-analysis workflow: toolchain preflight, grid/crop/line-strip generation, enhancement sheets, transcription posture, and durable recognition notes. Read before manuscript transcription or paleographic crop work. |
| `research-intake-prep/` | Phase 1 of intake — analyze a session, produce a repo-ready patchset at `sources/intake/processed/`. |
| `research-intake-apply-patch/` | Phase 2 — apply a reviewed patchset mechanically. |
| `research-intake-session-processor/` | Multi-entry intake-session helper. |
| `citation-rigour/` | Heavy citation audit and normalization. |
| `connector-publish/` | GitHub Connector / API publish recipe for branch-and-PR work (Codex-driven flow, Windows ARM credential failure modes). |

---

## 4. Repo file resolution

1. **Lookup order:** exact repo-relative path → file attached to chat → file in another connected workspace → external URL. Distinguish these source types in any response.
2. **Direct-open known paths.** Do not search to rediscover a file when the exact path is already known. Carry the working branch/ref through the whole task.
3. **Resolve filename ambiguity once,** then reuse the exact path. When the same filename may exist in more than one place, say which one is in use.
4. **Destination discipline:** put new knowledge in `research/`, not in validations or logs. Validations are thin source/method notes. Patchsets carry step-by-step execution instructions. Directory READMEs (`research/README.md`, `sources/README.md`, etc.) carry destination guidance when a finding could land in more than one place.

---

## 5. not used

---

## 6. Source-specific flags

### Daniel Gurney, *Record* (1848)
Primary secondary source G15–G35. Text in `sources/corpus/daniel-gurney-part-{1,2,3,4}.md`. OCR: "Wilham"/"William" ~6%, "Basiha"/"Basilia" ~16%. Page markers: `## p. N (#M) ##` (cite N). Supplement text extracted (Google Books OCR) into `sources/corpus/daniel-gurney-supplement.md` — OCR quality varies, especially for Latin passages and marginal notes. Rye appendix NOT yet in corpus.

**Supplement vs. Parts I–III pagination test.** The 1858 Supplement runs pp. 725–1096. Any "Supplement" citation with a page number below 725 is miscited (should be DG-I, DG-II, or DG-III).

---

## 7. Verification order

1. Primary source image — gold standard
2. Primary source transcription
3. Scholarly compiled work (DG, Blomefield, HoP)
4. Indexed databases (Anderson, Boyd, Ancestry — flag index-not-image)
5. User-submitted trees — leads only, never citable

---

## 8. Evidence discipline

- **Edit narrowly.** Prefer targeted edits over wholesale rewrites. Preserve established prose unless fact, citation, structure, or clarity requires change.

- **Findings go on the subject file.** Person findings → `research/people/`. Place findings → `research/places/`. Cross-cutting analysis → `research/topics/`. Sustained per-ancestor argument → the ancestor's people-companion (not a case file). Case files are user-initiated publication artefacts only. Logs and validations stay thin. Detailed multi-destination guidance is in `research/README.md` and `sources/README.md`.

- **Uncertainty is quantified, not hedged.** "Probable (~55–60%)" beats "fairly likely." Attach to specific claims, not whole documents.
- **Negative results are first-class.** "Searched X, found nothing" can be a finding but also that it can be a result of source incompleteness. Log it on the subject's file, not on the source's.
- **Conclusions don't outrun evidence.** Overclaiming is the cardinal sin.
- **Conflicting sources exposed, not reconciled by fiat.** Document the conflict; preserve both positions until primary evidence resolves.
- **Confidence conservation for living people.** living ancestors in G0–G1: minimize detail in public files. General geography OK; no addresses, no sensitive detail.

Citation discipline lives in `.claude/rules/citations.md`. Research prose style in `.claude/rules/research-writing-style.md`. Both apply to all AI working in this repo.

---

## 9. Local environment — OneDrive + git layout

This repository is intentionally split between a OneDrive working tree and a git directory outside OneDrive.

- **Working tree:** `C:\Users\allen\OneDrive\Documents\GitHub\gurney-genealogy`
- **Git directory:** `C:\Users\allen\GitDirs\gurney-genealogy.git`
- The repo-root `.git` path is a small pointer file containing `gitdir: C:/Users/allen/GitDirs/gurney-genealogy.git`.

OneDrive is mandatory for the user's recovery/audit workflow. Git internals stay outside OneDrive to avoid lock, sync, and permission churn. Do not move git internals back into the OneDrive working tree. Do not reclone into a temporary workspace as a substitute for fixing the durable checkout.

For health checks, branch-and-PR publish recipes, and Windows credential failure modes, see `.claude/rules/git-onedrive-codex.md` and `.claude/skills/connector-publish/SKILL.md`.

### Shell and tooling (avoid known friction)

- **Pick the shell deliberately.** Use the Bash tool for POSIX commands, the PowerShell tool for Windows cmdlets — don't mix them (running `Get-Content` or `grep` in the wrong tool is a recurring time-sink). The Bash tool runs an MSYS shell (`/usr/bin/bash`, with `/mingw64` on PATH).
- **Python:** `python` (3.14) is on PATH, but **bare `pip` is not** — always invoke `python -m pip`. Installs persist to the user interpreter (`%LOCALAPPDATA%\Python\pythoncore-3.14-64`). The pinned working set is `tools/requirements.txt` (`python -m pip install -r tools/requirements.txt`).
- **Pre-installed Python libraries:** Pillow, PyMuPDF (`fitz`), pypdf, pdfplumber (+ pdfminer.six), pypdfium2, lxml, beautifulsoup4, requests, openpyxl, cryptography. Add others with `python -m pip install <pkg>`.
- **PDF / image command-line tools:** `pdftotext` is available; the rest of poppler (`pdfinfo`, `pdftoppm`, `pdfimages`), Tesseract OCR, ImageMagick, and Ghostscript are **not** installed. To render PDF pages to images, use PyMuPDF or pypdfium2 (neither needs poppler). Note: `convert` on PATH is the Windows disk utility, **not** ImageMagick.

---

## 10. Tone

Concise, direct, honest. Pushback over sycophancy. "I was wrong" when wrong. No filler.

---

## 11. Efficiency — don't over-engineer

### Stop retrying
If a tool call fails or produces an unexpected result, try **once** more with a clear correction. If the second attempt also fails, stop and surface the problem rather than grinding through attempts 3+. Allen's time is more valuable than the work being done.

### Directory listings
Don't fetch full directory listings unless you actually need them. Knowing that `fact-sheets/` contains G04–G37 is sufficient for most tasks; the actual file list is only needed when looking for something specific.

### Continual improvement

When the user offers a critical correction or durable guidance, update the matching rule file in the same turn and disclose the update plainly. AI may correct narrow adjacent issues found in the same files (typos, broken anchors, acronym expansions, internal-mechanics vocabulary, citation placement) without separate permission, with disclosure. See `.claude/rules/continual-improvement.md` for the consolidation-pass discipline, avoid-reactive-absolutes guidance, and bias-toward-restraint check.
