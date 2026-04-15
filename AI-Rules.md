# AI-Rules.md

Operating rules for Claude working in this repo. **Read before first substantive response in any session.** Rules are living — edit in place when warranted; no confirmation needed for minor refinements. Flag significant changes in commit message.

---

## 0. Session start

On new session: read `AI-Rules.md`, `README.md`, most recent `research/log/*.md`. Check if `data/master.json` or `data/sources.json` changed since last reference.

---

## 1. Identity

User: Allen Lawrence Gurney, b. 1972, Portland OR. Dual projects: biography of Brig. Gen. William Gurney (1821–1879, G6); 37-generation genealogy site at genealogy.allengurney.com. Not a professional genealogist; accepts reasoned deduction from indirect evidence when noted. Reviews output critically; corrections are authoritative and incorporated immediately.

---

## 2. Repo map

```
data/            master.json, sources.json, locations.json (canonical structured data)
fact-sheets/     THE per-ancestor canonical file: polished narrative + research appendix
research/
  people/        NON-ANCESTOR subjects only (see §3 delineation rule)
  places/        one file per geographic locus
  topics/        cross-cutting problems (e.g., two-francis-disambiguation.md)
  case-files/    long-form investigations (e.g., candidate-b.md)
  log/           YYYY-MM-DD.md — INDEX ONLY, points into topical files
sources/
  corpus/        full-text source extracts (text preferred over PDF)
  media/{id}/    screengrabs, record crops (in-repo while small)
  validations/   per-source paleographic/analytical worksheets
site/            Eleventy source (output excluded via .gitignore)
tools/           lineage-specific artifacts (pedigree-explorer.html)
```

---

## 3. Workflow

### The delineation rule: one canonical file per ancestor

**Fact sheet** (`fact-sheets/g{NN}-{slug}.md`) = the single per-ancestor document. Contains polished narrative (public, published via Eleventy) AND the research appendix (private, excluded from build via HTML comment markers). New findings for an ancestor go into the fact sheet's research appendix. The narrative gets updated when warranted. This is the file to read when needing everything about an ancestor.

**research/people/** = reserved for subjects who DON'T have and WON'T get fact sheets:
- Non-ancestor research subjects: Margaret Rybett, laceweaver Francis, Ann Gurney of Hingham, candidate matches (Earsham John Girney 1636, etc.)
- Spouses with enough independent research to warrant their own file
- Pre-fact-sheet staging: accumulating findings before producing a fact sheet. Once the fact sheet exists, the staging file gets absorbed into the appendix or deleted.

**Never maintain two parallel files for the same ancestor.** If a fact sheet exists, that's the canonical file — period. research/people/ is not a shadow copy.

**The JSON** (`ancestors_v23.json` / future `master.json`) = structured data only (dates, locations, children, lineage status, buttons). No narrative. No research notes. Links to fact sheets by generation/ancestor ID.

### Commit cadence
Commit in the moment when durable content surfaces — not at session end. Atomic commits (one logical change each). Descriptive message. Don't batch unrelated changes.

### Topical-first discipline
Content → `fact-sheets/` (if ancestor) | `people/` (if non-ancestor) | `places/` | `topics/` | `case-files/`. Log entry = pointer only (filename + section). **If you're writing substantive content in a log entry, move it to the target file.**

### What does NOT go in research/
- Per-ancestor research for ancestors who have fact sheets → `fact-sheets/g{NN}-{slug}.md` § Research Appendix
- Source analysis (paleography, reconciliation) → `sources/validations/{sourceId}.md`
- Full-text source material → `sources/corpus/{sourceId}.md`

---

## 4. Citation discipline

### Citation key format
- `[DG-I-278]` = Daniel Gurney, *Record*, Part I, p.278
- `[DG-II-524]` = Part II, p.524
- `[DG-III-525]` = Part III, p.525
- `[DG-Supp-{page}]` = 1858 Supplement
- `[NRO-PD12/1]` = Norfolk Record Office, PD 12/1
- `[HoP-Gurney]` = History of Parliament Online
- `[Blom-Harpley]` = Blomefield, *History of Norfolk*, Harpley entry
- `[Anderson-GMD]` = Anderson, *Great Migration Directory* (2015)
- `[Banks-Brownell]` = Banks/Brownell, *Topographical Dictionary* (1937)

### Rules
- Every fact in `data/master.json` with a source dependency cites a `sourceId` defined in `data/sources.json`.
- Orphan facts (no source) and orphan sources (no facts cite them) are both bugs.
- When quoting Daniel Gurney text from `sources/corpus/`, cite book page (the `N` in `## p. N (#M) ##`), not scan sequence.
- **Flag OCR variant characters** when quoting: "Wilham" (→William), "Basiha" (→Basilia), hyphenation breaks. Normalize silently when quoting is not the point.
- Index entries (Boyd's, Ancestry, etc.) require image verification before treatment as established. See §9.

---

## 5. Lineage status values

Used in `master.json` for every direct-line ancestor:

- **Direct** — G1 (Allen himself)
- **Confirmed** — multiple independent primary or highly reliable sources
- **Probable** — best-supported hypothesis; active case file; e.g., John Gurney-1 (G13)
- **Uncertain** — attestation exists but evidentiary gap; e.g., Hugh de Gournay I (G36)
- **Tradition** — transmitted family lore without contemporary document; e.g., Eudes (G~37)
- **End of Record** — explicitly beyond the knowable

Collaterals: `Collateral`. Never confuse with direct-line status.

---

## 6. Principles (the corrections Allen has authoritatively established)

### Uncertainty is quantified, not hedged
Use explicit probability/confidence language. "Probable (~55–60%)" beats "fairly likely." Attach to specific claims, not whole documents. Cite what's moving the number.

### Negative results are first-class
"Searched X, found nothing" is a finding. Log it in the target file's § Negative results. Examples of high-value negatives: Peter absent from all England Gurney records; no John Gurney in Bucks Protestation Returns (though London/Essex returns non-surviving, so Francis's absence is uninformative).

### Conclusions don't outrun evidence
Overclaiming is the cardinal sin. If evidence supports "possible," don't write "likely." If it supports one interpretation, don't omit competing ones. Allen has corrected this pattern; continue self-policing. Rejected patterns: "no one left for New England is not provable" (correction); Sunday-baptism test; tight 1618 timeline without basis.

### Conflicting sources exposed, not reconciled by fiat
When sources disagree, document the conflict. Preserve both positions until primary evidence resolves. Don't pick the more convenient one.

### Confidence conservation for living people
Living persons (G0-G2 and collaterals at those generations): minimize detail in public files. Birth year, general geography OK; no street addresses, no sensitive relationships. Working material may contain more, but `data/master.json` and fact sheets are the publication layer.

---

## 7. Standing facts (don't re-derive)

### The 8 critical corrections (from prior chat handoff)
1. Francis G14 died **9 Jan 1646/7** (St Botolph Bishopsgate, FreeREG) — NOT 1641 (Boyd) or 1650 (secondary).
2. Junior Norfolk branch passes through **Walter de Gournay (G31)** — NOT Hugh IV/V (senior baron line, collateral).
3. **Sir John Gurney (d.1408)** is collateral; his son Edmund died under age. Direct line: Edmund G23 → Robert G22 → Thomas I G21 → Thomas II G20.
4. **Two Francis Gurneys** coexist in period: G14 Merchant Taylor (St Benet Fink) + laceweaver Francis (St Giles Cripplegate, wife Mary). See `topics/two-francis-disambiguation.md` (when created). Costessey manor records belong to laceweaver.
5. **Margaret Rybett died c.1616–17**, not c.1618. 1618 Marye (East Dereham Entry D) is Anne Browning's first child.
6. **John Gurney-1 born c.1609–12** (revised from c.1603 after 1611 marriage discovery).
7. **"Peter"** absent from all Gurney families 1500–1700; name came from wife Mary's unknown family.
8. **Eudes (G~37)** is Tradition, not Confirmed — Daniel Gurney acknowledged "matter of tradition."

### Structural facts
- Generation numbering: G1 = Allen. Increase going back.
- Family seat: West Barsham, Norfolk (entered via Wauncy inheritance through Edmund G23's wife Katherine; held until 1661 extinction of direct male line).
- Francis G14 = sixth son of Henry G15; "sprung from younger branches of gentlemen's families" = key social context.
- `ancestors_v23.json` = current authoritative ancestor file; will be normalized into `data/master.json` during schema buildout.

---

## 8. Source-specific flags

### Daniel Gurney, *Record of the House of Gournay* (1848)
- Primary secondary source for G15–G35. Treat as highly reliable but verify dates against primary sources where possible.
- Text in `sources/corpus/daniel-gurney-part-{1,2,3}.md`.
- OCR quirks: "Wilham"/"William" (~6%), "Basiha"/"Basilia" (~16%), hyphenation breaks at line ends, occasional `f`/long-s confusion.
- Page markers: `## p. N (#M) ##` where N=book page (cite), M=scan sequence (ignore).
- Parts I/II/III present. 1858 Supplement and Rye appendix NOT yet in corpus — PDFs in project knowledge.

### Anderson, *Great Migration Directory* (2015)
- For John Gurney-1: assigns "Unknown" origin = **implicit rejection of Banks's Bury St. Edmunds attribution** under modern scholarly standards. Interpretive principle established in case file.
- Arrival date: 1636 (Anderson) vs. June 1641 Weymouth record — **unresolved discrepancy**. See `topics/anderson-1636-vs-weymouth-1641.md` (when created).

### Banks/Brownell, *Topographical Dictionary* (1937)
- East Anglian placement of John-1 **weakens Candidate A (Stewkley) more than Candidate B (Norfolk)**.

### Ancestry Norfolk parish collections
- Draw from **bishop's transcripts and IGI, not original registers**. Negative Ancestry result does NOT close the Norfolk primary-source door. Go to NRO image for final answer.

### Boyd's marriage index
- Known to misread dates (Francis G14 death 1641 → corrected to 1646/7 via FreeREG). **Verify specific entries against original register images** before citing.

### Pennyghael Gurney genealogy (pennyghael.org.uk/Gurney.pdf)
- Source of Ryvett claim for Francis G14's first wife. Confirmed against NRO PD 12/1 marriage record (March 2026).

---

## 9. Verification order

Before treating a claim as established:
1. Primary source image (register, will, deed) — gold standard
2. Primary source transcription (validated)
3. Scholarly compiled work (Daniel Gurney, Blomefield, *History of Parliament Online*)
4. Indexed databases (Anderson, Boyd, Ancestry — flag index-not-image)
5. User-submitted trees — treat as leads only, never citable

Index entries require image verification before "Confirmed" status. Document every verification attempt (successful or failed) in `sources/validations/{sourceId}.md`.

---

## 10. Open research threads (as of April 2026)

Active topics requiring ongoing attention:
- **Candidate B case file** — John Gurney-1 = son of Francis G14 + Margaret Rybett. Currently ~55–60%. See `research/case-files/candidate-b.md`.
- **Anderson 1636 vs. Weymouth 1641** arrival date discrepancy.
- **East Dereham Entry E** — paleographic analysis supports "ffrancis Gurnie" over "Nicholas"; further validation useful.
- **Tier 1 pulls**: TAG 10:70–73, NEHGR 62:94 (highest priority, not yet obtained).
- **Herald and Genealogist vols. 1, 2, 5–8** — exhaustive search if thoroughness required.
- **FG Gurney 121 notebooks** (Buckinghamshire Archaeological Society) — unexamined.
- **Fact sheets remaining**: G21 Thomas Gournay I through G15 Henry de Gournay.
- **1858 Supplement + Rye appendix** — text extraction into `sources/corpus/` pending.

---

## 11. Tooling

- **GitHub MCP server** — direct commit access via Claude Desktop. Small/medium files (<50KB) commit inline cleanly; larger files (>50KB) should be placed locally and pushed via `git` from Allen's machine.
- **Eleventy site** — source in `site/`; build output excluded; Cloudflare Pages builds from the repo on push.
- **No localStorage/sessionStorage in artifacts** — if the pedigree explorer or similar gains data needs, use in-memory state or window.storage.

---

## 12. Tone

Concise, direct, honest. Allen values pushback over sycophancy. Say "I was wrong" when wrong; say "I don't know" when uncertain. No filler, no "great question," no restating the prompt. Reason out loud when reasoning matters; skip ceremony when it doesn't.
