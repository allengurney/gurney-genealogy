# Validation — FreeREG

**Source:** `freebmd-freereg` — FreeREG, volunteer transcriptions of English parish registers,
bishop's and archdeacon's transcripts, freereg.org.uk.

## Why this source is used

It is the only instrument in the G13 child-inventory source list that **publishes its own per-parish
coverage**, and it is independent of the commercial indexes in both directions — it returns event
rows with parents named, drawn from the parish registers themselves rather than from the
bishop's-transcript series that Findmypast's Buckinghamshire index is built on.

## What was examined (28 July 2026)

| Query | Scope | Result |
|---|---|---|
| Surname Gurney + Name Soundex, baptisms, all counties, 1622–1636, forename Mary | England-wide | 205 rows, 5 in the Gurney cluster |
| Same, forename Richard, 1624–1638 | England-wide | 116 rows, 3 in the Gurney cluster |
| Same, forename John, 1628–1642 | England-wide | **Did not complete** — hundred-second limit exceeded with soundex on and off |
| Surname Gurney + Name Soundex, all three event types, 1600–1700 | Buckinghamshire | 499 rows — the 500-row display cap — 73 in the Gurney cluster |
| Surname Gurney + Name Soundex, baptisms, 1620–1645 | All counties | Over 500 — capped, not usable |

Record details opened individually for the Epping (Essex) and St Vedast (London) Mary baptisms.

## Scope and limits

- **Coverage is genuinely partial and must be stated per query.** FreeREG returns no Gurney record at
  **Hitcham, Buckinghamshire** for 1600–1700, although Hitcham appears in its Buckinghamshire place
  index (99 places), and it carries no **Great Berkhamsted** Gurney baptism. Both parishes are held by
  Findmypast. No FreeREG blank is an England-wide negative.
- **Name Soundex on "Gurney" collides with "Green"** — both are Soundex G650 — so soundex sweeps are
  dominated by Green/Greene/Grime/Groome rows and reach the display cap quickly. Good for discovery,
  unusable for counting.
- The Buckinghamshire county run is **capped**, so no FreeREG county-level negative can be asserted
  until it is re-run in narrower windows.
- Search mechanics: the form is Rails-driven and the submit button disables itself while a search
  runs, so a query in progress looks like a failed one — wait rather than re-click. A county must be
  chosen before the place list populates.

## Where findings landed

`research/people/g13-john-gurney/topics/identity/67-refactor-freereg-second-instrument.md`;
record instances CR-101 to CR-113 in
`research/people/g13-john-gurney/coverage/child-record-catalog.csv`;
the floor-not-bound restatement at `research/case-files/john-gurney-case-file-v5.md` §6.1.
