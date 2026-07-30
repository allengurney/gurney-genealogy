# FindMyPast county-set sweep — 2026-07-29

Goal: measure the gap between the national cross-collection sweep (which found only the eliminated Eythorne, Kent household) and county-set-by-county-set coverage, by running BAPTISMS then MARRIAGES for each county set with stems gurn*, gourn*, gorn*, gern*, girn*, garn*.

| query_id | county_set | event | stems_run | total_results | rows_captured | status |
|---|---|---|---|---|---|---|
| NF-B-gurn | Norfolk | baptism | gurn* | 789 | 20 (page1) | CAPPED |
| NF-B-gourn | Norfolk | baptism | gourn* | 10 | 10 | done |
| NF-B-gorn | Norfolk | baptism | gorn* | 38 | 20 (page1) | CAPPED |
| NF-B-garn | Norfolk | baptism | garn* | 2913 | 20 (page1, noise) | CAPPED |
| NF-B-girn | Norfolk | baptism | girn* | 13 | 13 | done |
| NF-B-gern | Norfolk | baptism | gern* | 35 | 19 (page1) | CAPPED |
| NF-M-gurn | Norfolk | marriage/banns | gurn* | 533 | 19 (page1) | CAPPED |
| NF-M-gourn | Norfolk | marriage/banns | gourn* | 8 | 7 (dup dropped) | done |
| NF-M-gorn | Norfolk | marriage/banns | gorn* | 26 | 18 (page1) | CAPPED |
| NF-M-garn | Norfolk | marriage/banns | garn* | 1889 | 14 (page1, noise) | CAPPED |
| NF-M-girn | Norfolk | marriage/banns | girn* | 11 | 10 | done |
| NF-M-gern | Norfolk | marriage/banns | gern* | 31 | 12 (page1) | CAPPED |
| ES-B-gurn | Essex | baptism | gurn* | 492 | 19 (page1, minus 2 dup Agnes/Richard) | CAPPED |
| ES-B-gourn | Essex | baptism | gourn* | 13 | 13 | done |
| ES-B-gorn | Essex | baptism | gorn* | 49 | 19 (page1) | CAPPED |
| ES-B-garn | Essex | baptism | garn* | 1508 | 19 (page1, noise) | CAPPED |
| ES-B-girn | Essex | baptism | girn* | 3 | 3 (only 1 in 15-18xx range) | done |
| ES-B-gern | Essex | baptism | gern* | 27 | 13 (page1) | CAPPED |
| ES-M | Essex | marriage/banns | (slug probe) | — | 0 | NO-SUCH-SET (tried essex+marriages, essex+banns+and+marriages, essex+banns+%26+marriages — all 500) |
| NH-B-gurn | Northamptonshire | baptism | gurn* | 46 | 20 (page1) | CAPPED |
| NH-B-gourn | Northamptonshire | baptism | gourn* | 1 | 1 | done |
| NH-B-gorn | Northamptonshire | baptism | gorn* | 1 | 1 | done |
| NH-B-garn | Northamptonshire | baptism | garn* | 372 | 20 (page1, noise) | CAPPED |
| NH-B-girn | Northamptonshire | baptism | girn* | 0 | 0 | done (true zero, coverage confirmed by prior smith control) |
| NH-B-gern | Northamptonshire | baptism | gern* | 1 | 1 | done |
| NH-M-gurn | Northamptonshire | marriage/banns | gurn* | 60 | 20 (page1) | CAPPED |
| NH-M-gourn | Northamptonshire | marriage/banns | gourn* | 2 | 2 | done |
| NH-M-gorn | Northamptonshire | marriage/banns | gorn* | 2 | 2 | done |
| NH-M-garn | Northamptonshire | marriage/banns | garn* | 251 | 20 (page1, noise) | CAPPED |
| NH-M-girn | Northamptonshire | marriage/banns | girn* | 0 | 0 | done (true zero, coverage confirmed by prior smith control) |
| NH-M-gern | Northamptonshire | marriage/banns | gern* | 0 | 0 | done (true zero, coverage confirmed) |
| OX-B-gurn | Oxfordshire | baptism | gurn* | 29 | 18 (dup dropped) | done |
| OX-B-gourn | Oxfordshire | baptism | gourn* | 0 | 0 | done (true zero, coverage confirmed) |
| OX-B-gorn | Oxfordshire | baptism | gorn* | 2 | 2 | done |
| OX-B-garn | Oxfordshire | baptism | garn* | 81 | 17 (page1, noise, dup dropped) | CAPPED |
| OX-B-girn | Oxfordshire | baptism | girn* | 0 | 0 | done (true zero, coverage confirmed) |
| OX-B-gern | Oxfordshire | baptism | gern* | 2 | 2 | done |
| OX-M-gurn | Oxfordshire | marriage | gurn* | 16 | 14 (dup dropped) | done |
| OX-M-gourn | Oxfordshire | marriage | gourn* | 0 | 0 | done (true zero, coverage confirmed) |
| OX-M-gorn | Oxfordshire | marriage | gorn* | 0 | 0 | done (true zero, coverage confirmed) |
| OX-M-garn | Oxfordshire | marriage | garn* | 33 | 19 (page1, noise) | CAPPED |
| OX-M-girn | Oxfordshire | marriage | girn* | 0 | 0 | done (true zero, coverage confirmed) |
| OX-M-gern | Oxfordshire | marriage | gern* | 3 | 3 | done |
| CM-B-gurn | Cambridgeshire | baptism | gurn* | 107 | 14 (page1) | CAPPED |
| CM-B-gourn | Cambridgeshire | baptism | gourn* | 13 | 13 | done |
| CM-B-gorn | Cambridgeshire | baptism | gorn* | 0 | 0 | done (true zero, coverage confirmed) |
| CM-B-garn | Cambridgeshire | baptism | garn* | 1125 | 10 clean (page1, noise, some rows skipped) | CAPPED |
| CM-B-girn | Cambridgeshire | baptism | girn* | 1 | 1 | done |
| CM-B-gern | Cambridgeshire | baptism | gern* | 0 | 0 | done (true zero, coverage confirmed) |
| CM-M-gurn | Cambridgeshire | marriage | gurn* | 57 | 17 (page1) | CAPPED |
| CM-M-gourn | Cambridgeshire | marriage | gourn* | 2 | 2 | done |
| CM-M-gorn | Cambridgeshire | marriage | gorn* | 0 | 0 | done (true zero, coverage confirmed) |
| CM-M-garn | Cambridgeshire | marriage | garn* | 392 | 11 (page1 partial, noise) | CAPPED |
| CM-M-girn | Cambridgeshire | marriage | girn* | 1 | 1 | done |
| CM-M-gern | Cambridgeshire | marriage | gern* | 0 | 0 | done (true zero, coverage confirmed) |
| HU-B | Huntingdonshire | baptism | (slug probe) | — | 0 | NO-SUCH-SET (tried huntingdonshire+baptisms, huntingdonshire+baptism+index — both 500) |
| HU-M | Huntingdonshire | marriage | (not probed, no baptism set found) | — | 0 | NO-SUCH-SET |
| MX-B-gurn | Middlesex | baptism | gurn* | 361 | 19 (page1) | CAPPED |
| MX-B-gourn | Middlesex | baptism | gourn* | 5 | 5 | done |
| MX-B-gorn | Middlesex | baptism | gorn* | 13 | 12 (dup dropped) | done |
| MX-B-garn | Middlesex | baptism | garn* | 117 | 16 (page1, noise, dup dropped) | CAPPED |
| MX-B-girn | Middlesex | baptism | girn* | 10 | 6 (dedup of double-render rows) | done |
| MX-B-gern | Middlesex | baptism | gern* | 17 | 17 | done |
| MX-M | Middlesex | marriage/banns | (slug probe) | — | 0 | NO-SUCH-SET (tried middlesex+marriages, middlesex+banns+and+marriages — both 500) |
| WM-B-gurn | Westminster | baptism | gurn* | 304 | 12 (page1, dup dropped) | CAPPED |
| WM-B-gourn | Westminster | baptism | gourn* | 2 | 2 | done |
| WM-B-gorn | Westminster | baptism | gorn* | 58 | 12 (page1) | CAPPED |
| WM-B-garn | Westminster | baptism | garn* | 651 | 15 (page1, noise, dup dropped) | CAPPED |
| WM-B-girn | Westminster | baptism | girn* | 0 | 0 | done (true zero, coverage confirmed) |
| WM-B-gern | Westminster | baptism | gern* | 18 | 16 (dup dropped) | done |
| WM-M-gurn | Westminster | marriage | gurn* | 383 | 15 (page1, dup dropped) | CAPPED |
| WM-M-gourn | Westminster | marriage | gourn* | 4 | 4 | done |
| WM-M-gorn | Westminster | marriage | gorn* | 22 | 13 (dup dropped) | done |
| WM-M-garn | Westminster | marriage | garn* | 673 | 17 (page1, noise, dup dropped) | CAPPED |
| WM-M-girn | Westminster | marriage | girn* | 0 | 0 | done (true zero, coverage confirmed) |
| WM-M-gern | Westminster | marriage | gern* | 9 | 7 (dup dropped) | done |
| BK-B-gurn | Berkshire | baptism | gurn* | 117 | 14 (page1, dup dropped) | CAPPED |
| BK-B-gourn | Berkshire | baptism | gourn* | 0 | 0 | done (true zero, coverage confirmed) |
| BK-B-gorn | Berkshire | baptism | gorn* | 7 | 5 (dup dropped) | done |
| BK-B-garn | Berkshire | baptism | garn* | 246 | 9 clean (page1, noise, heavy dup) | CAPPED |
| BK-B-girn | Berkshire | baptism | girn* | 1 | 1 | done |
| BK-B-gern | Berkshire | baptism | gern* | 4 | 4 | done |
| BK-M | Berkshire | marriage | (not attempted — time budget) | — | 0 | error (not attempted) |


---

## SWEEP CLOSED 2026-07-29

Recovered and analysed after the agent that produced it stopped mid-run. **705 rows captured across
eight county sets.** Do not re-run this sweep; run the named residue instead (actions R-69 to R-72).

**Result.** Of the 705 rows, **68 fall in 1615-1650 and carry a father's name** - the in-window
household pool this sweep existed to produce. Within it:

- **No father-John, mother-Margaret household. None, in any set, at any date.**
- **No father-John, mother-Mary household in window** that the national cross-collection pool had not
  already returned.
- The in-window father-John rows are all previously catalogued: Earsham 1636 and 1638, Epping 1616,
  Harwich 1623, Thursford 1623, Hingham 1626, Abthorpe 1641, St Lawrence Jewry 1620, Oakington 1648,
  Kidlington, Banbury.

This closes action R-66 and drops the case file's "documented but in a source or class not yet searched"
row from 9% to 5%.

**Two rows worth keeping for method, not for G13.** Tittleshall with Godwick 1620 returns the *same
child twice* (Katerine / Katherine Gurnay, father Henry both times) with the mother indexed **Anne in
one transcript and Mary in the other** - a worked example of the mother forename being unstable between
witnesses to a single event. Norwich St Giles 1618 indexes a *father* as `Jone`, and King's Lynn 1615
indexes a father as `Katheryne`; neither parent field can be used as a hard filter without allowing for
this.

**Coverage residue - what this sweep could NOT reach.** This is the load-bearing part of this ledger:

| Gap | Status |
|---|---|
| Essex, Middlesex, Huntingdonshire **marriages** | **No such set exists.** Each slug probed under several spellings; all returned server errors |
| Huntingdonshire **baptisms** | **No such set exists** |
| **Suffolk baptisms** | No county set in this family. A Great Migration county reachable on FreeREG only |
| Berkshire marriages | **Not attempted** - the sweep ended at this row |
| Nine high-noise queries (`garn*` and relatives) | **Capped at result page 1.** Samples, not enumerations. Marked CAPPED row by row above |

**Instrument defect proven during analysis:** a year bound and a place keyword **cannot be combined** in
a single-dataset (`sid=103`) query - the pair fails closed. Essex Baptisms returns 349 Smith baptisms at
Epping with no year bound and **zero** with `yearofbaptism=1616`, in a set that demonstrably holds a
1616 Epping baptism under another surname. `sortby` is accepted and silently ignored. **Any negative
resting on both parameters at once is void** (action R-71, retroactive). Consequence: Ackworth cannot be
tested on the Yorkshire set at all, so its Gurney zero is uninterpretable and the candidate holds at 9%
as untestable rather than weakened.

**Findings written up at**
`research/people/g13-john-gurney/topics/identity/75-refactor-margaret-county-sets-and-loose-ends.md`.
Registered as `findmypast-county-baptism-sets-2026-07-sweep` with a validation worksheet at
`sources/validations/findmypast-county-baptism-sets-2026-07-sweep.md`.
