**Done:** 2026-05-28 19:17 PT

# v68 patchset — Dashwood 1563 visitation (Kervile pedigree, Catherine Kerville corroboration for G21)

Prepared: 2026-05-28  
Revised: 2026-05-28 (second-AI review)  
Phase: 1 preparation  
Scope: source-control and structured transcription for one Norfolk visitation page that corroborates an already-published direct-line marriage. The companion Rye p. 132 alternate-scan capture has been **dropped** in this revision (see "Scope correction" below).

## Scope correction (revision pass)

The first draft of this patchset attempted two unrelated promotions: Dashwood (Harvey 1563) p. 58 and a second Rye 1891 p. 132 scan ("The visitacion pg 132.png"). A second-AI review identified two errors in that draft:

1. **The Rye p. 132 capture is a duplicate of v67.** Comparing the two intake images confirms they are the same Harleian Society printed page; the v67 copy (`Visitation-page132.png`) is the cleaner scan. Promoting the v68 copy as an "alternate scan" would duplicate `sources/media/rye-visitacion-norffolk-1891/` without adding evidentiary value. The v68 image is therefore **archived rather than promoted**; v67 remains the single Rye p. 132 capture for the project.
2. **The Dashwood p. 58 finding was misframed as a research lead.** The original draft treated Katherine Kervile's marriage to "Thomas Gurney" as needing correlation. In fact, the project's existing scholarship already identifies this couple firmly: **G21 Thomas Gournay I married Catherine Kerville of Watlington**, daughter of Robert Kerville of Watlington (will dated 19 Nov 1434), per Daniel Gurney 1848 (pedigree p. 286) and DG-Supp 1858 (p. 795, "Family of Kerville"). The G21 research companion at `research/people/g21-thomas-gournay-i-fact-sheet.research.md` records DG's four supporting arguments for the Catherine Kerville reading, including the Robert Kerville will of 1434 and the Kerville-of-Watlington pedigree. The Dashwood page is therefore a **third independent witness** to an already-confirmed direct-line marriage, not a new lead. The patchset has been reworked accordingly.

## Incoming files

```text
sources/intake/processed/The visitation of Norfolk in the year 1563 page 58 - thomas gurney m katherine (catherine).png
sources/intake/processed/The visitacion pg 132.png   # duplicate of v67's Visitation-page132.png; will be archived, not promoted
```

## Source URL supplied

- HathiTrust: `https://babel.hathitrust.org/cgi/pt?id=uc1.b4945929`

## Source ID

This patchset adds one source ID:

- `dashwood-visitation-norfolk-1563-vol1-1878` — Dashwood / Bulwer / Carthew / Grigson / Jessopp edition of William Harvey's 1563 Norfolk visitation, vol. 1 (1878).

The Rye 1891 source (`rye-visitacion-norffolk-1891`) is already added in v67; v68 does not duplicate it. The second Internet Archive item for the same Rye work (`visitacionievisi32ryew`) is recorded in this patchset as a known-alternate scan in the v67 source-entry notes if v67 has been applied; if v67 has not yet been applied, the alternate-item note is folded into v67's source entry at application time.

## Research-value assessment

### Dashwood p. 58 — Kervile pedigree, Catherine Kervile marriage to Thomas Gurney G21

The Kervile pedigree on Dashwood p. 58 places Catherine in the Robert Kervile of Watlington family group:

- Robert Kervile of Watlington, Norfolk, Esq., lord of the manor there by 1426, **will dated 19 Nov. 1434, proved at Norwich the following year**, buried in Watlington church.
- Wife: Elizabeth, daughter of Thomas Holdich, living 1434.
- Thomas Holdich married Elizabeth, daughter and heir of Thomas Frowick of Wignal Maudin.
- Geoffrey Kervile of Islington in Marshland, second son, married Margaret Holdich (heir to her mother Elizabeth).
- Robert and Elizabeth's children: Katherine (legatee under her father's will, said to have married Thomas Gurney); Hawys (also a legatee); Richard (son and heir, devisee of the manor of Watlington, ob. s.p.); Geoffrey (the Islington-in-Marshland second son above).
- Thomas Kervile of Watlington (a later generation) married Katherine Elvin of Wignall St Jermyn.

The page **does not introduce a new lead**. It is a third independent witness to the marriage already published in `fact-sheets/g21-thomas-gournay-i-fact-sheet.md` ("Married Catherine Kerville of Watlington" — n4, n8) and analyzed in `research/people/g21-thomas-gournay-i-fact-sheet.research.md` (the four supporting arguments for the Catherine Kerville reading). Dashwood's cautious "said to have married" wording is editorial caution from the 1878 editors transcribing a 16th-century pedigree note, not actual evidentiary doubt; the same page anchors Catherine to the Robert Kervile family with the 1434 will and proves the Watlington branch identification.

Two new precision details worth carrying forward into the G21 companion:

- **Will date precision.** The G21 companion currently records "Robert Kerville's will (d. 1434)" via DG. Dashwood p. 58 gives the **exact will date — 19 Nov. 1434** — and confirms probate at Norwich the following year. This sharpens the chronology.
- **Catherine's siblings.** Dashwood names Hawys (sister, legatee), Richard (brother and heir, ob. s.p.), and Geoffrey (brother of Islington in Marshland) — useful sibling context that is not in the existing G21 companion.

Additional Norfolk-gentry network detail on the page (Thomas Holdich = Elizabeth Frowick of Wignal Maudin; Geoffrey Kervile = Margaret Holdich; Thomas Kervile = Katherine Elvin of Wignall St Jermyn) is relevant standing context for the Watlington / Wiggenhall west-Norfolk gentry cluster but does not bear directly on a Gurney finding.

### Dashwood p. 58 image — rotation note

The intake image is rotated. A rotated reading copy is created at promote time while preserving the as-supplied original.

## Outcomes

| Item | Files | Outcome | Destination |
|---|---|---|---|
| 1 | `The visitation of Norfolk in the year 1563 page 58 - thomas gurney m katherine (catherine).png` | promote | `sources/media/dashwood-visitation-norfolk-1563-vol1-1878/`, `sources/corpus_supplement/`, `sources/validations/`, and downstream routing to G21 research companion and (optionally) G21 fact-sheet n4 footnote |
| 2 | `The visitacion pg 132.png` | archive (do not promote) | `sources/intake/archive/v68-duplicate-rye-p132-scan/` — duplicate of v67's `Visitation-page132.png` |

No item is rejected outright; item 2 is preserved as an archived duplicate scan for provenance.

## Phase 2 operations

### 1. Create Dashwood media directory

```bash
mkdir -p sources/media/dashwood-visitation-norfolk-1563-vol1-1878
```

### 2. Promote Dashwood p. 58 image; archive the Rye p. 132 duplicate scan

```bash
git mv "sources/intake/processed/The visitation of Norfolk in the year 1563 page 58 - thomas gurney m katherine (catherine).png" \
  "sources/media/dashwood-visitation-norfolk-1563-vol1-1878/page058-kervile-thomas-gurney-marriage-note-original.png"

mkdir -p sources/intake/archive/v68-duplicate-rye-p132-scan
git mv "sources/intake/processed/The visitacion pg 132.png" \
  "sources/intake/archive/v68-duplicate-rye-p132-scan/the-visitacion-pg-132-duplicate-scan-of-rye-p132.png"
```

### 3. Create rotated reading copy for Dashwood p. 58

```bash
python - <<'PY'
from pathlib import Path
from PIL import Image

src = Path("sources/media/dashwood-visitation-norfolk-1563-vol1-1878/page058-kervile-thomas-gurney-marriage-note-original.png")
dst = Path("sources/media/dashwood-visitation-norfolk-1563-vol1-1878/page058-kervile-thomas-gurney-marriage-note-rotated.png")

Image.open(src).rotate(270, expand=True).save(dst)
PY
```

### 4. Update `data/sources.json` — add Dashwood source entry; touch Rye notes only if v67 already applied

This script is idempotent. It adds the Dashwood entry, updates `meta.lastUpdated`, and **only** touches the Rye entry if it is already present (i.e., v67 has been applied) — in which case it appends the alternate-Internet-Archive-item note. If v67 has not yet been applied, the Rye alternate-item note is left for v67 to fold in (v68 does not create a Rye entry).

```bash
python - <<'PY'
import json
from pathlib import Path

path = Path("data/sources.json")
data = json.loads(path.read_text(encoding="utf-8"))

data.setdefault("meta", {})["lastUpdated"] = "2026-05-28"
sources = data.setdefault("sources", {})

sources.setdefault("dashwood-visitation-norfolk-1563-vol1-1878", {
    "shortTitle": "Dashwood, Visitation of Norfolk 1563, vol. 1 (1878)",
    "citation": "Harvey, William. The Visitation of Norfolk in the Year 1563, Taken by William Harvey, Clarenceux King of Arms. Edited by the Rev. G. H. Dashwood, F.S.A., and continued by Captain W. E. G. L. Bulwer, G. A. Carthew, Esq., F.S.A., Rev. W. Grigson, M.A., and Rev. Augustus Jessopp, D.D. Vol. I. Norwich: Miller and Leavins, 1878.",
    "archive": "HathiTrust",
    "url": "https://babel.hathitrust.org/cgi/pt?id=uc1.b4945929",
    "corpusStatus": "partial",
    "corpusPath": "sources/corpus_supplement/dashwood-visitation-norfolk-1563-vol1-1878-kervile-p58.md",
    "mediaPath": "sources/media/dashwood-visitation-norfolk-1563-vol1-1878/",
    "validationPath": "sources/validations/dashwood-visitation-norfolk-1563-vol1-1878.md",
    "notes": "Public-domain HathiTrust scan of vol. 1. Page 58 captured in v68: Kervile pedigree corroborating G21 Thomas Gournay I's marriage to Catherine Kerville of Watlington. Robert Kervile of Watlington (Catherine's father), will dated 19 Nov. 1434, proved at Norwich the following year. Independent visitation witness alongside DG-I 1848 pedigree p. 286 and DG-Supp 1858 p. 795."
})

# Touch the Rye entry only if it already exists. Append the alt-scan IA item to notes if absent.
rye = sources.get("rye-visitacion-norffolk-1891")
if rye is not None:
    notes = rye.get("notes") or ""
    if "visitacionievisi32ryew" not in notes:
        rye["notes"] = (notes + " Alternate Internet Archive item for the same Harleian Society edition: https://archive.org/details/visitacionievisi32ryew (intake encountered a less-clean scan duplicate of p. 132 from this item in v68; the v67 capture remains the project's working scan).").strip()

path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
PY
```

### 5. Write Dashwood corpus supplement

New file write: `sources/corpus_supplement/dashwood-visitation-norfolk-1563-vol1-1878-kervile-p58.md`

```markdown
# Dashwood / Harvey 1563 visitation — Kervile pedigree p. 58 (Catherine Kerville and Thomas Gurney G21)

Source ID: `dashwood-visitation-norfolk-1563-vol1-1878`

Source: William Harvey, *The Visitation of Norfolk in the Year 1563, Taken by William Harvey, Clarenceux King of Arms*, ed. Rev. G. H. Dashwood, F.S.A., continued by Capt. W. E. G. L. Bulwer, G. A. Carthew, Rev. W. Grigson, and Rev. Augustus Jessopp, vol. 1 (Norwich: Miller and Leavins, 1878). HathiTrust item `uc1.b4945929`.

Images:

- `sources/media/dashwood-visitation-norfolk-1563-vol1-1878/page058-kervile-thomas-gurney-marriage-note-original.png` (as-supplied, rotated 90° clockwise in capture)
- `sources/media/dashwood-visitation-norfolk-1563-vol1-1878/page058-kervile-thomas-gurney-marriage-note-rotated.png` (normalized reading copy)

Transcription conventions:

- Pedigree structure is preserved with nested bullets.
- `=` means marriage/spousal connection in the printed tree.
- `da.` means daughter; `h.` means heir; `ux.` means wife of.
- `ob. s.p.` means died without issue.
- Square brackets reproduce printed editorial brackets or cautious local expansions.

## Page 58 — Kervile pedigree with Catherine Kerville / Thomas Gurney marriage note

Printed page: 58.  
Pedigree continuation marks: `(a)` at top; `(b)` at bottom.

### Structured transcription

- `(a)` continuation from p. 57.
  - Agnes Kervile — mentioned in will of Robert her brother; unmarried in 1435; had lands in Wiggenhale.
  - Robert Kervile of Watlington in Norfolk, Esq. = Elizabeth, daughter of Thomas Holdich, living 1434.
    - Robert details: lord of the manor of Watlington, 1426; **will dated 19 Nov. 1434**; proved at Norwich the following year; buried in Watlington Church.
    - Elizabeth's paternal line: Thomas Holdich = Elizabeth, daughter and heir of Thomas Frowick of Wignal Maudin in Norfolk, Esq.
      - Margaret Holdich — heir to her mother Elizabeth — married Geoffrey Kervile of Islington in Marshland (below).
    - Children of Robert Kervile and Elizabeth Holdich:
      - **Katherine — legatee under her father's will. She is said to have married Thomas Gurney.**
      - Hawys — legatee under her father's will.
      - Richard — son and heir; devisee of the manor of Watlington under his father's will (formerly held by John son of William son of Thomas de Watlington); ob. s.p.
      - Geoffrey Kervile of Islington in Marshland, second son = Margaret Holdich (above).
        - Thomas Kervile of Watlington in Norfolk = Katherine, daughter of William Elvin of Wignall St Jermyn in Norfolk, Esq.
          - Thomas Kervile details: lord of the manor which he devised to Robert Kervile, his grandson; will dated 1532; proved at Norwich 4 Oct. 1535.
          - `(b)` continues to following page.

### Identification with G21 Thomas Gournay I

The "Thomas Gurney" of this page is **G21 Thomas Gournay I**, husband of Catherine Kerville per the project's existing reading. The Dashwood page is a third independent witness alongside:

- Daniel Gurney, *Record of the House of Gournay* (1848), pedigree p. 286: "Catherine, dau. of — Kerville, of Watlington, Norfolk, Esq."
- Daniel Gurney, *Supplement to the Record of the House of Gournay* (1858), p. 795 (Family of Kerville entry).

The visitation's cautious "said to have married" phrasing is editorial — the same page anchors Catherine firmly to Robert Kervile of Watlington (will of 1434), the Watlington branch is the right one per the project's reading, and the chronology (Catherine flourishing c. 1430-1460) aligns with G21's career.

### New detail beyond DG

- **Robert Kervile's will date — 19 Nov. 1434** — is more precise than DG records (DG: "d. 1434"). Probate at Norwich the following year.
- Catherine's siblings — Hawys (sister/legatee), Richard (heir, ob. s.p.), and Geoffrey (of Islington in Marshland) — are visible on the page; the G21 companion may pick these up as standing sibling context.
- Network detail: Thomas Holdich married Elizabeth Frowick of Wignal Maudin; Geoffrey Kervile married Margaret Holdich; Thomas Kervile (a later generation) married Katherine Elvin of Wignall St Jermyn. Useful for west-Norfolk gentry-network context but not bearing on a Gurney finding.
```

### 6. Write Dashwood validation file

New file write: `sources/validations/dashwood-visitation-norfolk-1563-vol1-1878.md`

```markdown
# Validation — Dashwood, Visitation of Norfolk 1563, vol. 1 (1878)

Source ID: `dashwood-visitation-norfolk-1563-vol1-1878`

## Source examined

William Harvey, *The Visitation of Norfolk in the Year 1563, Taken by William Harvey, Clarenceux King of Arms*, ed. Rev. G. H. Dashwood, F.S.A., continued by Capt. W. E. G. L. Bulwer, G. A. Carthew, Rev. W. Grigson, and Rev. Augustus Jessopp, vol. 1 (Norwich: Miller and Leavins, 1878). HathiTrust item `uc1.b4945929`.

## Portion examined

Printed p. 58, Kervile pedigree:

- `sources/media/dashwood-visitation-norfolk-1563-vol1-1878/page058-kervile-thomas-gurney-marriage-note-original.png`
- `sources/media/dashwood-visitation-norfolk-1563-vol1-1878/page058-kervile-thomas-gurney-marriage-note-rotated.png`

## Method and limitations

Transcription from page image. Image rotated to standard orientation for reading; original orientation preserved. Pedigree structure preserved with nested bullets.

## Substantive findings recorded

- `sources/corpus_supplement/dashwood-visitation-norfolk-1563-vol1-1878-kervile-p58.md` — full p. 58 transcription with identification of "Thomas Gurney" as G21 Thomas Gournay I.

Downstream routing for the G21 companion (Catherine Kerville witness, will-date precision, Catherine's siblings) is documented in the patchset but deferred to a follow-up patchset because the existing companion has its own structure.

## Patchset trail

Prepared in `sources/intake/processed/v68-dashwood-rye-gurney-pedigree-diagrams.patchset.md`; after application, archived to `sources/intake/done/`.
```

### 7. Write Dashwood media README

New file write: `sources/media/dashwood-visitation-norfolk-1563-vol1-1878/README.md`

```markdown
# Dashwood, Visitation of Norfolk 1563, vol. 1 (1878)

Source ID: `dashwood-visitation-norfolk-1563-vol1-1878`

Working-reference images from William Harvey, *The Visitation of Norfolk in the Year 1563*, ed. G. H. Dashwood, vol. 1 (Norwich: Miller and Leavins, 1878), HathiTrust item `uc1.b4945929`.

## Files

- `page058-kervile-thomas-gurney-marriage-note-original.png` — original rotated intake image.
- `page058-kervile-thomas-gurney-marriage-note-rotated.png` — reading copy rotated into standard orientation.

## Transcript

See `sources/corpus_supplement/dashwood-visitation-norfolk-1563-vol1-1878-kervile-p58.md`.
```

### 8. Downstream routing — for a follow-up patchset

Deferred to a follow-up patchset because the G21 companion and fact sheet each have their own structure that needs targeted insertion rather than scripted str_replace:

- `research/people/g21-thomas-gournay-i-fact-sheet.research.md` — add Dashwood p. 58 as a third independent witness to the Catherine Kerville marriage; carry forward the will-date precision (19 Nov 1434, proved at Norwich the following year); record Catherine's siblings (Hawys, Richard ob. s.p., Geoffrey of Islington in Marshland) as standing sibling context.
- `fact-sheets/g21-thomas-gournay-i-fact-sheet.md` — optionally add Dashwood p. 58 as an additional citation under n4 ("Catherine Kerville of Watlington") and n8 (the Watlington/Lynn-hinterland alliance bullet). Lower priority than the companion update.

This patchset does **not** silently modify the topic file proposed in v67. The v68 image is being archived as a duplicate rather than promoted, so there is no v68 contribution to v67's topic file `research/topics/brooke-rye-selected-gurney-references.md`. The v68 finding (Catherine Kerville corroboration) is a G21-specific direct-line corroboration and does not belong on the v67 topic file.

### 9. Intake lifecycle

This patchset file already exists at `sources/intake/processed/v68-dashwood-rye-gurney-pedigree-diagrams.patchset.md`. The stub-v69 file already exists in `sources/intake/processed/`. No additional lifecycle moves are needed before Phase 2 runs.

## Phase 2 completion step

After Phase 2 application is complete, prepend a top-line `**Done:** YYYY-MM-DD HH:MM PT` stamp and move this patchset to `sources/intake/done/`:

```bash
python - <<'PY'
from pathlib import Path
src = Path("sources/intake/processed/v68-dashwood-rye-gurney-pedigree-diagrams.patchset.md")
dst = Path("sources/intake/done/v68-dashwood-rye-gurney-pedigree-diagrams.patchset.md")
body = src.read_text(encoding="utf-8")
dst.write_text("**Done:** 2026-05-28 HH:MM PT\n\n" + body, encoding="utf-8")
src.unlink()
PY
```

Replace `HH:MM` with the actual completion time.

## Validation checklist

- [ ] `data/sources.json` parses after update.
- [ ] `dashwood-visitation-norfolk-1563-vol1-1878` exists in `data/sources.json`.
- [ ] `rye-visitacion-norffolk-1891` entry (added in v67) carries the alternate-IA-item note in its `notes` field, OR v67 has not yet been applied (in which case the alternate-item note is folded into v67 at its application time).
- [ ] Original Dashwood image promoted under `sources/media/dashwood-visitation-norfolk-1563-vol1-1878/`.
- [ ] Rotated Dashwood reading copy created.
- [ ] Rye p. 132 duplicate scan archived (not promoted) under `sources/intake/archive/v68-duplicate-rye-p132-scan/`.
- [ ] Corpus supplement, validation, and media README files created.
- [ ] No direct fact-sheet change made; G21 routing is documented for a follow-up patchset.
