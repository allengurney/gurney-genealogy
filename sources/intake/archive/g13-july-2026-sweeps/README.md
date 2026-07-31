# G13 identity sweeps, July 2026 — archived working datasets

Three captured record sweeps behind the July 2026 John Gurney identity work. Their findings are
assimilated into the identity research units at
`research/people/g13-john-gurney/topics/identity/` and into the case file; the row data is kept here
so any statement drawn from it stays checkable.

| Dataset | Captured | Rows | What it is |
|---|---|---|---|
| `freereg-g13-sweep-2026-07-28/` | 28 July 2026 | 585 | Twenty surname spellings × three event types × all counties × 1600–1660, sixty queries against FreeREG. The independent second instrument. |
| `fmp-parent-sweep-2026-07-28/` | 28 July 2026 | 598 | The completed parent-name enumeration, Great Britain 1615–1649, every year sliced individually. |
| `fmp-county-sweep-2026-07-29/` | 29 July 2026 | 705 | Eight FindMyPast county baptism and marriage sets × six surname stems. |

## The `PROGRESS.md` in each folder is the load-bearing part

Each dataset carries a per-query coverage ledger, and **the ledger matters more than the rows.** It
records which queries were capped at a result page and are therefore samples rather than
enumerations; which record sets do not exist at all; and which zero results are uninterpretable
because the set's coverage for that parish or window is unproven. **A negative drawn from the row
data without reading the ledger will be wrong**, because the row data cannot show what was never
searched.

Do not discard or summarise the ledgers if the row data is ever compressed or pruned.

## Registered sources

The sweeps are cited in the research layer through their registered source identifiers, not by file
path: `freebmd-freereg`, `findmypast-uk-parish-baptisms`, and
`findmypast-county-baptism-sets-2026-07-sweep` (which has its own validation worksheet at
`sources/validations/findmypast-county-baptism-sets-2026-07-sweep.md`).
