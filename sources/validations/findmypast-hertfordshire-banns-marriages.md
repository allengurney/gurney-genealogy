# Validation — Findmypast Hertfordshire Banns & Marriages

**Source:** `findmypast-hertfordshire-banns-marriages` — Hertfordshire Banns & Marriages, parish-register
banns and marriage records from Hertfordshire Archives and Local Studies, served via Findmypast.

## What was examined

Authenticated session, 28 July 2026, single-dataset results mode
(`datasetname=hertfordshire+banns+%26+marriages&sid=103` — note the ampersand must be percent-encoded;
the `hertfordshire+banns+and+marriages` slug returns a 500).

Three queries:

- `lastname=gurn*&keywords=berkhamstead` — 19 rows
- `lastname=gourn*&keywords=berkhamstead` — 3 rows
- `spouselastname=gourn*&keywords=berkhamstead` — 3 mirror rows, used to recover the husbands' surnames
- `firstname=john&lastname=gurn*` (county-wide, no place filter) — 57 rows

## Scope and limits

- The set indexes **both parties**, so a one-direction miss is a real miss. The spouse-side query was
  used here to resolve two rows that read as John-Gurney grooms and are in fact Gourney brides.
- The place token in this set is `Berkhamstead`. `keywords=` is a literal token match and fails closed
  on `berkhamsted` and `berkhampstead`.
- Not examined: the whole-county Gurney corpus outside the John-forename query; banns as distinct from
  solemnised marriages; the pre-1560 tail.
- No images opened; index columns only (First name(s) / Last name / Year / Spouse's first name(s) / Place).

## Where findings landed

`research/people/g13-john-gurney/topics/identity/66-refactor-berkhamsted-burials-and-the-departure-gap.md`,
§"The marriage: absent from the county, not just the parish".
