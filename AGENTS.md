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

For routine edits, open only files the task requires. Do not pre-load full source corpora, all fact sheets, all research companions, or unrelated generations unless the task specifically calls for them.

For discovery and research tasks where exploring the repo *is* the work, breadth is appropriate — but use targeted search (Grep / Glob) to find candidates first, then read only the files that match. Sequential full-file reads of large directories should be rare.

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
  topics/        cross-cutting analytical or methodological files
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

---

## 3. Rules and skills — explicit enumeration (cross-AI discovery)

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

Repo file resolution (lookup order, direct-open known paths, destination discipline) is documented in §4 below rather than as a separate rule file.

### Skills (`.claude/skills/`)

Skills follow the Agent Skills open standard ([agentskills.io](https://agentskills.io)) and work cross-tool. Skill discovery in this repo is by explicit invocation or by enumeration here.

| Skill folder | Purpose |
|---|---|
| `familysearch-export-review/` | Phase 0 review of a FamilySearch Family Group Record PDF export against existing repo knowledge; produces an assessment MD as input to Phase 1. |
| `familysearch-fulltext-research/` | Operational recipes for FamilySearch Full-Text Search: query syntax/URL parameters, DGS film constructs, full-resolution image download API (presigned S3 + TLS note), shadow-DOM extraction, failure modes. Read before any FTS task. |
| `familysearch-tree-updates/` | Compose updates to push back to the FamilySearch tree based on repo findings. |
| `findmypast-record-search/` | Operational recipes for FindMyPast indexed record sets (parish baptisms, banns & marriages, burials): URL-parameter search, dataset slugs, wildcard/spelling tactics, the spouse-search trick, reading results without opening paywalled images, coverage caveats. Read before any FindMyPast record-search task. |
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

## 5. Lineage status values

- **Direct** — G1 (Allen himself)
- **Confirmed** — multiple independent primary or highly reliable sources
- **Probable** — best-supported hypothesis; active case file. Lacks primary sources.
- **Tradition** — transmitted family lore without sources
- **End of Record** — explicitly beyond the knowable
- **Related** — (also collateral) never confuse with direct-line status.

---

## 6. Standing facts (don't re-derive)

### Critical corrections
1. Francis G14 died **9 Jan 1646/7** (FreeREG) — NOT 1641 (Boyd) or 1650.
2. Junior Norfolk branch through **Walter (G31)** — NOT Hugh IV/V (collateral).
3. **Sir John Gurney (d.1408)** is collateral. Direct: Edmund G23 → Robert G22 → Thomas I G21 → Thomas II G20.
4. **Two Francis Gurneys** coexist: G14 Merchant Taylor (St Benet Fink) + laceweaver (St Giles Cripplegate, wife Mary). Costessey = laceweaver.
5. **Margaret Rybett died c.1616–17**, not c.1618.
6. **John Gurney-1 born c.1607–12, early edge favored** (revised from c.1603; Entry E baptism c.1609/10 ±2, with the 1653 deposition and the c.1627 marriage both favoring the early edge).

### Structural facts
- G1 = Allen. Numbers increase going back.
- West Barsham entered via Wauncy inheritance (Edmund G23's wife Katherine); held until 1661.
- Francis G14 = sixth son of Henry G15.
- `data/ancestors.json` = canonical ancestor data file (renamed 2026-05-25 from versioned `ancestors v26.json`).
- `data/places.json` + `data/places_detail.json` = canonical two-layer place spine. `locations.json` was retired.

---

## 7. Source-specific flags

### Daniel Gurney, *Record* (1848)
Primary secondary source G15–G35. Text in `sources/corpus/daniel-gurney-part-{1,2,3,4}.md`. OCR: "Wilham"/"William" ~6%, "Basiha"/"Basilia" ~16%. Page markers: `## p. N (#M) ##` (cite N). Supplement text extracted (Google Books OCR) into `sources/corpus/daniel-gurney-supplement.md` — OCR quality varies, especially for Latin passages and marginal notes. Rye appendix NOT yet in corpus.

**Supplement vs. Parts I–III pagination test.** The 1858 Supplement runs pp. 725–1096. Any "Supplement" citation with a page number below 725 is miscited (should be DG-I, DG-II, or DG-III).

---

## 8. Verification order

1. Primary source image — gold standard
2. Primary source transcription
3. Scholarly compiled work (DG, Blomefield, HoP)
4. Indexed databases (Anderson, Boyd, Ancestry — flag index-not-image)
5. User-submitted trees — leads only, never citable

---

## 9. Evidence discipline

- **Uncertainty is quantified, not hedged.** "Probable (~55–60%)" beats "fairly likely." Attach to specific claims, not whole documents.
- **Negative results are first-class.** "Searched X, found nothing" can be a finding but also that it can be a result of source incompleteness. Log it on the subject's file, not on the source's.
- **Conclusions don't outrun evidence.** Overclaiming is the cardinal sin.
- **Conflicting sources exposed, not reconciled by fiat.** Document the conflict; preserve both positions until primary evidence resolves.
- **Confidence conservation for living people.** living ancestors in G0–G1: minimize detail in public files. General geography OK; no addresses, no sensitive detail.

Citation discipline lives in `.claude/rules/citations.md`. Research prose style in `.claude/rules/research-writing-style.md`. Both apply to all AI working in this repo.

---

## 10. Local environment — OneDrive + git layout

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
- **No local OCR.** If a scanned source needs OCR, flag it rather than assuming it can run locally — Tesseract is not installed (it can be added via `winget install UB-Mannheim.TesseractOCR`).

---

## 11. Tone

Concise, direct, honest. Pushback over sycophancy. "I was wrong" when wrong. No filler.

---

## 12. Efficiency — don't over-engineer

### Stop retrying
If a tool call fails or produces an unexpected result, try **once** more with a clear correction. If the second attempt also fails, stop and surface the problem rather than grinding through attempts 3+. Allen's time is more valuable than the work being done.

### Directory listings
Don't fetch full directory listings unless you actually need them. Knowing that `fact-sheets/` contains G04–G37 is sufficient for most tasks; the actual file list is only needed when looking for something specific.
