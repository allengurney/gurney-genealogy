# Validation — FindMyPast county baptism and marriage index sets (July 2026 Gurney sweep)

**Source ID:** `findmypast-county-baptism-sets-2026-07-sweep`

## What was examined

FindMyPast single-dataset (`sid=103`) county index sets, authenticated session, 29 July 2026. Two
distinct uses:

1. **The eight-county sweep.** Norfolk, Essex, Northamptonshire, Oxfordshire, Cambridgeshire,
   Middlesex, Westminster and Berkshire, each run against six surname stems (`gurn*`, `gourn*`,
   `gorn*`, `gern*`, `girn*`, `garn*`) for baptisms and, where a set exists, for marriages and banns.
   **705 rows captured.**
2. **Targeted single queries** in Herefordshire, Sussex, Warwickshire, Essex and Yorkshire baptisms, to
   date three previously undated households, to enumerate the Epping corpus, and to run coverage
   controls.

## Scope and limits

- **Nine queries were capped at their first result page** by high-noise stems (`garn*` returns 2,913
  rows in Norfolk alone). Those are samples, not enumerations. The per-query status is recorded row by
  row in the progress ledger.
- **Sets that do not exist**, each probed under several slug spellings: no marriage or banns set for
  **Essex**, **Middlesex** or **Huntingdonshire**; no baptism set for **Huntingdonshire**. **Suffolk**
  has no county baptism set in this family.
- **Berkshire marriages were not run** — the sweep reached the end of its budget at that row.
- **Yorkshire coverage for Ackworth before 1689 is unproven.** The control returns 127 Smith baptisms
  with none visible earlier than 1689, and the interface offers no working way to bound the set's
  earliest year (see the defect below), so the Gurney zero there is uninterpretable.

## Instrument defect found

**A year bound and a place keyword in the same `sid=103` query fail closed.** Essex Baptisms returns
349 Smith baptisms at Epping with no year bound and **zero** with
`yearofbaptism=1616&yearofbaptism_offset=5`, in a set that demonstrably holds a 1616 Epping baptism
under another surname. Separately, `sortby` is accepted and silently ignored. Recorded for reuse in
`.claude/skills/findmypast-record-search/SKILL.md` §0d and as method check C2c.

**Any negative in this project resting on both parameters at once is void.**

## Where findings landed

- `research/people/g13-john-gurney/topics/identity/75-refactor-margaret-county-sets-and-loose-ends.md`
  — the full working: the Margaret axis, R-66's result, the three datings, Gurley of Westminster,
  the Epping enumeration, and both instrument defects.
- `research/people/g13-john-gurney/topics/identity/74-refactor-candidates-scored-against-the-shape.md`
  — two new rows in the shape matrix and the retraction of feedback point 1.
- `research/case-files/john-gurney-case-file-v5.md` — §11 probability table (two new rows,
  three revisions), the corrected "exactly one household" claim in §6.1 and its footnote, and
  footnote 129.
- `research/people/g13-john-gurney/coverage/child-record-catalog.csv` — catalogued rows.

## Raw working data

`sources/intake/new/fmp-county-sweep-2026-07-29/results.tsv` (705 rows) and `PROGRESS.md` (per-query
coverage ledger, including every capped and non-existent set).
