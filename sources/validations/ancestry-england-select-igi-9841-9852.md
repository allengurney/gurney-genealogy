# Validation — Ancestry, England Select Births/Christenings and Select Marriages (IGI)

- **Source IDs:** `ancestry-england-select-births-christenings-9841`; `ancestry-england-select-marriages-9852`
- **Sources:** *England, Select Births and Christenings, 1538–1975* (Ancestry collection 9841) and *England, Select Marriages, 1538–1973* (Ancestry collection 9852), both derived from the International Genealogical Index.
- **Examined:** used intermittently from June 2026; the England-wide Gurney sweeps recorded here run 28 July 2026.

## What was examined

**Collection 9852 (marriages).** Two England-wide sweeps for the colonial John Gurney's English
marriage:

- `name=John_Gurn*&spouse=Mary_&marriage=1628` — 233 rows read in relevance order. Only two pre-1660
  primary marriage rows: Eythorne, Kent, 6 November 1632 (indexed three times) and Ackworth,
  Yorkshire, 6 June 1636. Every other spouse-Mary row is 1688 or later.
- `name=John_Gurn*&marriage=1630`, bride unconstrained — 244 rows, as a completeness check for
  marriages indexed with a blank or unreadable spouse field. Near 1630 the only primary rows are the
  three Eythorne duplicates and John Gurneys × Susan, Farnham Royal, Buckinghamshire, 30 March 1629.

**Collection 9841 (baptisms).** A per-child probe, `name=Richard_Gurn*&birth=1630`, 424 rows. Only one
primary baptism row surfaced at the head of the ranking — Richard Gurnet, 1 June 1628, Allhallows
London Wall, parents Edward and Winefret — with the remainder parent-role rows carrying no date or
place. Recorded as a **method failure, not a result**: see below.

## Scope and limits

- **Index level only. No images in either collection.**
- **9852 indexes both parties**, which makes it the right instrument for a spouse-paired national
  sweep; the county sets and FindMyPast's national sets do not all do this.
- **9852 does not contain the 1611 Norwich Gurney–Rybett marriage**, which is a direct measure of its
  incompleteness and bounds every negative drawn from it. A blank here is a blank in an IGI-derived
  extract, not in the parish registers.
- **Exact-match flags fail closed.** `marriage_x=0-0-0` returned "zero good matches" where the same
  query without it returned 244 rows. Never set the exact toggles when the point is to see candidates;
  search non-exact and filter by reading the Date and Place columns.
- **Place in `birth=` / `marriage=` re-ranks; it does not filter.** Non-matching parishes still appear
  further down.
- **9841 boosts parent-role rows above baptism events.** A forename+surname query returns mostly rows
  where the named person is a *parent*, with no baptism date or place of their own. That makes it a
  poor instrument for a per-child sweep unless the Baptism Date / Baptism Place columns are read row
  by row. The same failure class as FamilySearch record search; prefer a county set with Father /
  Mother / Place columns where one exists.
- `&page=2` does not bind on collection results; tighten the query rather than paging.

## Where findings landed

- [`research/people/g13-john-gurney/topics/identity/60-refactor-matching-by-family-not-by-man.md`](../../research/people/g13-john-gurney/topics/identity/60-refactor-matching-by-family-not-by-man.md) §"The marriage, swept England-wide on a spouse-indexed instrument"
- Interface mechanics: `.claude/skills/findmypast-record-search/SKILL.md` §6
