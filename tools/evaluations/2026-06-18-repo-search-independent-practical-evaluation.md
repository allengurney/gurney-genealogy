# Independent practical evaluation — `repo_search.py` — 2026-06-18

Second, independent pass complementing `2026-06-18-repo-search-initial-evaluation.md`.
Focus: a realistic end-to-end *grounding* task (the work done before any online
search), measured against the iterative grep-and-read workflow an agent actually
runs — not against a raw `rg` dump no agent would read into context.

## Build under test

- Local Windows-ARM checkout; cache external at `%USERPROFILE%\GitDirs\gurney-genealogy-search-cache`.
- Normal-search inventory: 827 text files (`site/`, `.claude/`, `.codex/`, `tools/` excluded).
- Two fixes applied during this evaluation (see "Defects found and fixed").

## Method

Subject: lead **L-128** (Margaret Rybett = Rivett of Garveston; P95; source ref
`research/people/rivett-family-of-garveston.md`). Task: ground on what the repo
already knows — the parentage link, the Rivett family, and crucially *what has
already been searched and exhausted* — before spending any online-search effort.

Two workflows, each measured by characters pulled into context (token proxy =
chars / 4):

- **Manual:** `grep` for Rivett/Rybett/Garveston variants, then targeted reads.
- **Tool:** `search` → manifest → `expand` selected volumes.

## Defects found and fixed

These were not visible in the first evaluation because that run executed in an
environment where ripgrep was present and stdout was UTF-8.

1. **Hard `rg` dependency, absent locally (blocker).** `run_exact_rg` called
   `shutil.which("rg")` and exited if missing. ripgrep was not installed on the
   local machine at all, so first run was a hard failure.
   - Fix: new `find_ripgrep()` resolves rg via env override
     (`GURNEY_REPO_SEARCH_RG` / `RIPGREP_PATH`), then PATH, then common Windows
     install locations (winget Links shim + Packages dir, scoop, chocolatey,
     Program Files) and Unix locations; prepends the found directory to PATH for
     the run; caches the result. Verified: the tool now runs with `rg` **not** on
     PATH. No AGENTS.md or shell-PATH change required.
2. **`UnicodeEncodeError` on the default Windows console (blocker).** A manifest
   containing `★` (U+2605, from a research heading "★ Primary Source Discovery")
   crashed at `print(manifest)` under cp1252. The package still wrote to disk;
   only the print died — an intermittent crash on ordinary repo content.
   - Fix: `_configure_stdio()` reconfigures stdout/stderr to UTF-8 with
     `errors="replace"` at the start of `main()`. Verified: the `★` manifest now
     prints with exit 0 and no `PYTHONIOENCODING` override.

Regression: `python -m unittest tools.tests.test_repo_search` → 6/6 OK after fixes.

## L-128 grounding comparison

| Measure | Manual (grep + reads) | Tool (manifest + expand) |
|---|---:|---:|
| Round-trips to ground | grep + 4–6 reads/greps | 1 `search` + 1–3 `expand` |
| Context for equivalent grounding | ~49,700 chars ≈ ~12.4k tok (est.) | ~20,000 chars ≈ ~5.0k tok (measured) |
| Minimal-grounding floor | ~17k chars (companion only, partial) | ~7,900 chars ≈ ~2.0k tok (manifest + 1 vol) |
| Thorough ceiling | read G13 companion whole → +190k chars → ~60k+ tok | bounded; manifest reports 226 sections, pull on demand |
| Negative-result footnotes | severed (claims at L165–189, defs at L227–230) | 266/266 attached in full |
| Completeness signal | none; 59 candidate files, no ranking | ledger: 432 lines / 56 files / 226 sections, ranked |
| Cross-thread resume | redo from scratch | `resume` reprints manifest ~865 tok |

Manual char counts are estimated from real file sizes and the actual grep
(519 hits / 59 files); the tool counts are measured command/volume lengths.

### Headline findings

- **Reduction ~60% at equal depth, ~84% at the minimal floor**, and — more
  important — the *unbounded* manual ceiling (reading the 190k-char G13
  companion, or iterating) is removed. This is the mechanism behind the
  previously observed 100k-token searches.
- **Footnote attachment is the decisive qualitative win.** The "Controlling
  negatives" section returned *with* its FMP/FTS negative-result footnotes,
  including exact wildcards, year windows, and FamilySearch ark IDs — the
  precise parameters that prevent re-running dead online searches. Manual grep
  structurally severs these: in `rivett-garveston-maternal-family-2026-06.md`
  the negative claims cite `[^fts-neg]` etc. at lines 165–189 while the
  definitions sit at lines 227–230. The gap is recoverable only by reading the
  whole file — infeasible for the 190k-char G13 companion.
- **Precision is high.** Top-12 ranked locators were exactly the decisive set:
  the maternal-family supplement ("Controlling negatives", "Method note", "The
  identification"), the Rivett companion's parentage finding, the 1584 Margaret
  Bate Rivett will validation, and the case-file "First Marriage: Margaret
  Rybett" section.
- **No evidence loss vs. manual.** The tool's 56 matched files vs. grep's 59
  differ only by intentional exclusions (`.claude/`, `tools/old/`, `.bak`); the
  exhaustive `all-results.jsonl` retains all 226 grouped sections.

## Functionality confirmed

- `search --lead`, `search --terms`, `--variants conservative`, `expand
  --volume`, `runs`, `resume` all work; `runs` lists prior packages and `resume`
  reprints a manifest in a fresh process (cross-thread continuity).
- Cache correctly lives outside the OneDrive working tree.
- Staleness ledger reported `0 changed, 827 unchanged` on a clean index.

## Observations / lower-priority recommendations

- `search --lead L-128` searches the literal lead *handle*, so it surfaces
  packet/checkpoint files that merely mention "L-128" rather than the lead's
  subject. A terms search is the better grounding entry point today; consider
  having `--lead` fold the lead's subject terms into the query so a one-shot
  lead search grounds on the topic.
- HTML fact-sheet parsing still tends to one-page-one-section (noted in the
  first evaluation); not exercised heavily here.

## Bottom line

For multi-file, footnote-heavy grounding the tool is well-built and earns its
keep: better grounding than the manual workflow at ~40–60% of the token cost,
with footnote fidelity and a bounded ceiling. The two defects were
environment/portability, not design, and are now fixed in-tool.
