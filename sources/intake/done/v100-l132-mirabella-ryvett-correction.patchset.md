**Done:** 2026-06-18 19:50 PT

# Patchset v100 — L-132: correct the Mirabella Ryvett marriage (William Burd, not Sir John Heydon)

**Scope.** One bounded factual correction carried in two published-prose files, plus resolution of the matching research-companion flag. The primary **Visitation of Suffolk (Metcalfe, p. 63)** records **Myrable Ryvett married William Burd, Customer of London** — not Sir John Heydon of Baconsthorpe. The Gurney–Heydon kinship is independent and unaffected (Anne Heydon married William Gurney V). Each correction is made **in place / assimilated** — the false statement is revised where it stands, not annotated with a dated note — per the reinforced discipline in `.claude/rules/research-files.md` ("Synthesize by topic or finding … and assimilate") and `.claude/rules/sources.md` ("Promotions assimilate; they do not append"). The corpus extract behind the correction is `sources/corpus_supplement/ryvett-suffolk-visitation-pedigrees-metcalfe.md`.

**Deferred to follow-up patchsets (not in scope here).** This patchset deliberately does not attempt the whole arc's inventory:
- Promotion of the **Edward-Gurney sibling-disappearance synthesis** into `research/people/g13-john-gurney-fact-sheet.research.md` — deferred because it needs a new `data/sources.json` entry for the FamilySearch *Norfolk Parish Registers (County Record Office)* / record-search collections, and careful assimilation into the companion's existing maternal-kin and Norfolk-Gurney-households treatments (not a new dated block). NB the FS index date "27 May 1610" for Edward's baptism is an **indexing artifact** — the register page bears no date; the case file's paleographically-derived **c. 1611** estimate is authoritative and must be the figure used.
- **Formal disposition of paleography packets 13–19**: reports → `sources/corpus_supplement/paleo-2026-06-packet-NN-*.md`, master images → `sources/media/<set>/_local/`, and reference fixes (grep `paleography-staging`).
- **Absorption of packets 14–15** (Norwich depositions; Earsham manorial).
- **`data/sources.json` entries + thin validations** for the Norfolk wills/probate index (`norfolk-wills-probate-index-1371-1858`) and the Garveston parish register, if not already present.

Leads are written directly per standing guidance and are **not** in this patchset: L-135–L-138 are already in `research/future-research/research-leads.csv`, and L-132's `Status` is set to Closed directly there (see Phase-2 note).

---

## Item 1a — G14 fact sheet: remove the false Ryvett–Heydon claim

**File:** `fact-sheets/g14-francis-gurney-fact-sheet.md`

`str_replace`

- **old_string:**
  ```
  Norfolk/Suffolk gentry; the Rybett/Ryvett family of Fritton, Rishangles, and Stowmarket. Mirabella Ryvett married Sir John Heydon of Baconsthorpe, connecting the family to the Gurneys. Margaret probably died c. 1616–1617; her burial has not yet been located.
  ```
- **new_string:**
  ```
  Norfolk/Suffolk gentry; the Rybett/Ryvett family of Fritton, Rishangles, and Stowmarket. Margaret probably died c. 1616–1617; her burial has not yet been located.
  ```

Removes the factually incorrect sentence. The surrounding family context and footnote n5 (generic Norfolk/Suffolk gentry sources) stand; no reader-facing claim now rests on the disproven Heydon marriage.

## Item 1b — John Gurney case file: correct the marriage in place

**File:** `research/case-files/john-gurney-case-file-v4.md`

`str_replace`

- **old_string:**
  ```
  The families moved in overlapping social circles: Mirabella Ryvett married Sir John Heydon of Baconsthorpe, and the Heydons were directly connected to the Gurneys through Anne Heydon's marriage to William Gurney V.<sup class="fn"><a href="#n20" id="ref-20">20</a></sup>
  ```
- **new_string:**
  ```
  The Heydons of Baconsthorpe were directly connected to the Gurneys through Anne Heydon's marriage to William Gurney V; a separately reported marriage of Myrable Ryvett to Sir John Heydon is not borne out by the primary Visitation of Suffolk (Metcalfe, p. 63), which records her husband as William Burd, Customer of London.<sup class="fn"><a href="#n20" id="ref-20">20</a></sup>
  ```

Keeps the true Gurney–Heydon kinship and replaces the false Ryvett–Heydon link with the Visitation reading, cited inline. Footnote n20 is retained for the gentry context. (If a later citation audit finds n20 specifically underwrote the Heydon attribution, it should be re-pointed to the Visitation extract; out of scope here.)

## Item 1c — Rivett companion: resolve the correction flag

**File:** `research/people/rivett-family-of-garveston.md`

`str_replace`

- **old_string:**
  ```
  The Rivett–Heydon leg is therefore in conflict with the primary source
  and should be reconciled/corrected (lead L-132); the Gurney–Heydon tie via Anne Heydon m.
  William Gurney V is independent and unaffected.
  ```
- **new_string:**
  ```
  The Rivett–Heydon leg conflicted with the primary source and has now been corrected in the
  G14 fact sheet and the John Gurney case file — the false Ryvett–Heydon marriage removed from
  the fact sheet and replaced in the case file with the Visitation's William Burd reading; the
  Gurney–Heydon tie via Anne Heydon m. William Gurney V is independent and unaffected.
  ```

Resolves the flag in place and removes the visible `L-132` lead handle from companion prose (per `research-writing-style.md`).

---

**Phase-2 note.** After applying Items 1a–1c: set **L-132 `Status` → Closed** directly in `research/future-research/research-leads.csv`; prepend `**Done:** YYYY-MM-DD HH:MM PT` to this file; move it to `sources/intake/done/`.
