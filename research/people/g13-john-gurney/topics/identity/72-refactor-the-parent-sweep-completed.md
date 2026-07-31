<!-- July 2026 refactor working round. Its findings are carried in the permanent identity units
     30- to 39-, which are the current account; this file is retained as the working record,
     including its own correction and retraction trail, which is deliberate and belongs to the
     research layer. Not yet in the G13 context graph — graph-bearing content is tracked in
     sources/intake/g13-graph-breadcrumb.md. Not linked from published pages. -->

# The parent-name sweep, completed — and what the colonial band actually contains

## What was run

The FindMyPast parent-name search (`sid=102`) asks the one question the child inventory exists to
answer: **which baptisms anywhere in Great Britain name a father John Gurney?** It was retracted in
July after a wrong parameter, then run in fragments. It is now complete for **1615–1649**, sliced one
year at a time because `page=2` is broken on that mode, run both strict and variant-expanded, and
capturing **598 rows**.[^sweep]

Raw capture at `sources/intake/archive/g13-july-2026-sweeps/fmp-parent-sweep-2026-07-28/` with a per-query log. Five year-slices
lost between one and seven rows each to the pagination break and are logged `CAPPED`; the strict
windows returned nothing the variant slices had not already caught.

## The headline

**In the colonial band 1626–1636, the sweep returns 149 rows, of which 68 carry a Gurney-cluster
surname. Deduplicated, every one of them belongs to a household this file already carries — and only
one is an unaccounted-for colonial-name child to a father John.**

| Household | Children in band | Status |
|---|---|---|
| **Great Berkhampstead** | **Richard 1626**, Elizabeth 1629, Michaell 1631, Sarah 1634, Francys 1636 | C(ii), 4% — Richard probably buried there 1638 |
| **Hitcham, Bucks** | **Mary 1631** | **The only unaccounted-for one**, 4% |
| Toddington, Beds | Anne 1628, John 1631, Audrey 1634 | Father Thomas on the county set; household head buried 1641 |
| Eythorne, Kent | Mary 1633, Thomas 1635 | Eliminated — wife Mary Marsh, John buried 1648 |
| East Claydon, Bucks | Elinor 1632, Samuel 1636 | Eliminated — John buried there 1654 |
| Old Swinford, Worcs | Humfry 1628, Elizabeth 1629 | Confirms the FreeREG finding on a second instrument |
| Bishop's Cleeve and Naunton, Glos | Mathew 1629, Alice 1626 | Garne |
| Stepney, London | John 1633 | Eliminated — John Garnes, mariner, wife Elizabeth |
| Weston Turville, Bucks | Elyzabethe 1627 | 3% |
| Windermere, Bromsgrove, Rochester | Mabel 1627, Johes. 1634, Ellinor 1636 | No colonial-name child |

**Three rows are new to the file** and none disturbs the picture: **Edward Gourney, Aylesbury, 1628**;
**Johes. Gurner, Bromsgrove, Worcestershire, 1634**; **Ellinor Gornie, Rochester, Kent, 1636**. The
Aylesbury Edward is the only one worth a second look — a child to a father John at St Mary Aylesbury a
decade before the 1638–53 run the file already carries, and Candidate A(i) married Alice Oliffe at
Bierton in April 1628.

## The statement this finally licenses

The file has been trying since July to say that the colonial children do not surface in England. The
sweep now supports a precise version of it, on the correct instrument, run to completion:

> **Across Great Britain, 1615–1649, exactly one baptism to a father named John Gurney gives a
> colonial child forename in the right window and belongs to no household otherwise accounted for:
> Mary Gurny, Hitcham, Buckinghamshire, 22 January 1631.**

Everything else resolves to a household with a documented English continuation, a documented English
death, a wife who is not Mary, or a father who is not John.

**Three caveats keep this a floor and not a bound**, all established earlier in this refactor and all
still live: the `sid=102` pool does not reach every county set (it misses the Norfolk FHS transcription
entirely, and with it the Earsham household); no single index is complete, as the four-instrument
comparison showed; and five year-slices lost rows to the pagination defect.

## The unreadable-surname tail, and why it is mostly noise

Forty-two rows in the band carry an unreadable surname — `?`, `G.`, `G?`, `G...So`, `G?th`. In
principle a Gurney could hide in any of them. In practice **more than half are Cornwall Baptisms**, a
set in which the surname is routinely unindexed, and the remainder scatter across Wiltshire, Berkshire,
Cheshire, Lincolnshire and Guernsey with no concentration anywhere near a Gurney country.

Two are worth naming rather than dismissing, because they sit in places that matter:

- **"G. John", Norton, Suffolk, 1635** — Suffolk is inside the East Anglian corridor and FindMyPast has
  no Suffolk baptism county set, so the county is thinly covered here.
- **"G?th John" / "G.Uth John", Wooburn, Buckinghamshire, 1632** — two transcriptions of one entry, in
  the target county.

Neither can be resolved from an index; both are image questions, and neither is a priority against the
image pulls already queued at Stewkley and Ackworth.

## Consequence for the table

**No row moves on this sweep.** That is the correct outcome and worth saying plainly: a completed
enumeration that returns no new candidate is a result, not a failure. What it does is convert the
file's central English-side claim from an assertion built out of fragments into a bounded statement
with a named instrument, a stated coverage limit, and a single surviving exception.

It also, once more, leaves **Hitcham** carrying the only unexplained colonial-name child in the
country — on a row whose other support this same day proved to be a coverage artefact.

## Crosslinks

- [`63-refactor-child-sweep-closed-and-reassessment.md`](63-refactor-child-sweep-closed-and-reassessment.md) — the retraction that created this action
- [`68-refactor-four-instruments-compared.md`](68-refactor-four-instruments-compared.md) — why this remains a floor
- [`71-refactor-burials-as-the-elimination-instrument.md`](71-refactor-burials-as-the-elimination-instrument.md) — the same day's burial and marriage work
- Raw capture: `sources/intake/archive/g13-july-2026-sweeps/fmp-parent-sweep-2026-07-28/`

[^sweep]: FindMyPast cross-collection parent search, authenticated session, 28–29 July 2026: `sourcecategory=life+events+(bmds)&collection=parish+baptisms&sourcecountry=great+britain&sid=102&fatherfirstname=john&fatherfirstname_variants=true&fatherlastname=gurney[&fatherlastname_variants=true]&yearofbirth=YYYY&yearofbirth_offset=0`, run for every year 1615–1649 variant-expanded, plus strict-surname windows at 1617, 1622, 1627, 1632, 1637, 1642 and 1647. **598 rows captured**, held with a per-query log at `sources/intake/archive/g13-july-2026-sweeps/fmp-parent-sweep-2026-07-28/results.tsv` and `PROGRESS.md`. Mechanics: `year=` returns a silent zero and must not be used; `page=2` returns page 1 again, which is why every window is a single year and why the slices for 1627, 1628, 1633, 1634 and 1637 are logged `CAPPED` with between one and seven rows unretrieved. The variants engine also returns Gray, Griffith, Gaune and unreadable-surname rows, which are captured and filtered rather than trusted. Row counts and the band analysis were re-derived from the raw TSV rather than taken from the run's own summary. Source ID: `findmypast-uk-parish-baptisms`.
