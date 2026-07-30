# Validation — England & Wales Published Wills & Probate Indexes, 1300-1858

- **Source ID:** `england-wales-published-probate-indexes`
- **What it is:** FindMyPast page images of the printed British Record Society county probate index volumes.
- **Examined:** 2026-07-27, authenticated FindMyPast session (Everything tier).

## Portion examined

- **British Record Society vol. 114**, *Index to Buckinghamshire Probate Records 1483–1660 and Buckinghamshire Peculiars 1420–1660*: the complete GURNEY block, printed pages **173–174** (FindMyPast records `OR/BRS/333/0197`, `OR/BRS/333/0198`), plus printed p. 154 to confirm the `GERNEY, see GURNEY` cross-reference and so the completeness of the block. Forty-two Gurney-variant testators transcribed verbatim.
- Coverage probes for adjacent counties (below). No other volume read.

## Coverage limits that bound any negative

- **Hertfordshire is not in the dataset at all.** `keywords=gurn*&place=hertfordshire` returns zero, and so does `keywords=smith&place=hertfordshire` — there is no Hertfordshire volume. A blank for Hertfordshire is a coverage gap, not a negative. This matters for Candidate C (Berkhamsted).
- **Northamptonshire is represented only by administrations indexes** — British Record Society vols 70 (1677–1710) and 92 (1711–1800), four Gurney-variant rows. Nothing before 1677, and no wills index. The death window of the John Gurney of the 1641 certificate of residence is therefore not covered.
- The results table returns **place, page number, source and publication only — no testator name and no year**. Names must be read from the page image, so a row count is not a name list.

## Method note

The record page exposes a direct, non-cookie-bound PDF at `/media/pdf/<ID>/<ID>/<32-hex-hash>/pdf`. The PDF is a **scanned page image with no text layer** — `extract_text()` returns empty; the page must be pulled out with `pypdf` `page.images` and read visually. The embedded Chrome PDF pane freezes the browser tool, so the document must be fetched rather than viewed. Full mechanics in `.claude/skills/findmypast-record-search/SKILL.md` §7.

## Findings recorded in

- Extract: [`sources/corpus_supplement/bucks-probate-index-brs114-gurney-variants-to-1660.md`](../corpus_supplement/bucks-probate-index-brs114-gurney-variants-to-1660.md)
- Analysis: `research/people/g13-john-gurney/topics/identity/52-refactor-bucks-herts-elimination.md`
