# Packet 44 — East Dereham PD 86/41: burial subsections of the 1616–1619 annual returns — the Margaret (Rivett) Gurney burial hunt (L-131)

Staged: 2026-07-16. **Images are ALREADY IN THE REPO** (not re-staged): `sources/media/Parish_Register_East_Dereham/gbprs_norfolk_pd_86-41_00726.jpg` through `..._00734.jpg` (plus context `00725.jpg`). Structure and year anchors are established in `sources/validations/east-dereham-pd-86-41-register-structure-and-chronology.md` — READ THAT FIRST; it maps image→register-year and the combined-annual-return layout (christenings + "Mariages" + burials per Lady-Day year).

## The question

**Find (or negative-confirm) the burial of Margaret Gurney (née Rivett), first wife of Francis Gurney, who died c. 1616–17** — the event that dates John Gurney G13's motherlessness. The prior pass scanned only the 1615-year burial subsection (00725, negative) and the 1617-year MARRIAGES subsection; the burial subsections of the 1616, 1617, 1618 and 1619 annual returns "remain unscanned for the burial target" (validation file, Negative findings).

Year map (validation file §3): 00726/00727 = 1616 return (25 Mar 1616–25 Mar 1617, D-class anchor); 00728/00729/00730 = 1617 return (interpolated); 00731/00732 = 1618 return (contains the known Marye Gurnoe bp 25 May 1618); 00733/00734 = 1619 return. Duplicate-scan pairs are flagged in the validation file — skip duplicates.

## Tasks

1. For each annual return 1616→1619: locate the burial subsection on the page (below/after the Mariages header per the layout) and scan every burial line for **Gurney/Gurnay/Gurny/Gurnoe/Gurnye/Girnye and Rivett/Rivet/Ryvett/Rybett** surnames, and for any "Margaret/Margarett/Margeria" forename with an ambiguous surname.
2. Transcribe verbatim any candidate line (with its neighbours for anchoring). If Margaret's burial is found: exact date + styling ("wife of Francis"?) — this is a top-5 finding for the whole project; flag prominently.
3. Explicit negatives per year if not found ("1616 return burial subsection read line-by-line: no Gurney/Rivett variant" etc.).
4. Known anchor to verify in passing: **Agnes Gurney burial 31 Jan 1616 (modern)** is already documented (sourceId `fs-vnn2-wrg-agnes-gurney-burial-east-dereham`) — locate her line in the 1615-return (00725) or 1616-return pages as a calibration check, and note which return actually carries her.
5. Bonus (cheap while there): note any OTHER Gurney lines in the 1616–1619 returns' christening subsections (an Anne-Browning-era child pre-1618 would refine the remarriage date).

## Bounds

Line-scan only (grid + band ladder per page); ≤1 line-strip pass per candidate; per packet-14 lessons, mark low-contrast pages `blocked by image quality` rather than grinding. Prior tooling: `tools/east_dereham_image_sweeps.py` (six-state recipe; `next-pulls` CLI).

## Findings destination

Report → staging root as `packet-44-east-dereham-burials-1616-1619.report.md`. Feeds L-131, `research/people/rivett-family-of-garveston.md`, the G13 chronology (case file), `research/topics/east-dereham-parish-register-paleography.md`, and dump `dump-2026-07-16-round3.md`. Source ID: `familysearch-fulltext-search` catch-all or the existing PD 86/41 source entries.
