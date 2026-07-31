# FMP Parent-Name Baptism Sweep — father John Gurney, 1615-1649

Base query (sid=102, cross-collection parent search): fatherfirstname=john(+variants), fatherlastname=gurney(+variants for VAR), yearofbirth=YYYY, yearofbirth_offset=2, collection=parish+baptisms (bap-) or parish+burials (bur-).

| query_id | father_surname_mode | window | total_results | rows_captured | status |
|---|---|---|---|---|---|
| bap-1617-strict | strict | 1615-1619 | 3 | 3 | done |
| bap-1617-variant (window) | variant | 1615-1619 | 47 | — | CAPPED (page=2 broken; split into per-year sub-slices below) |
| bap-1615-variant | variant | 1615 (offset=0 sub-slice) | 17 | 17 | done |
| bap-1616-variant | variant | 1616 (offset=0 sub-slice) | 15 | 15 | done |
| bap-1617-variant | variant | 1617 (offset=0 sub-slice) | 21 | 20 | CAPPED (1 row not retrieved, page=2 broken) |
| bap-1618-variant | variant | 1618 (offset=0 sub-slice) | 15 | 15 | done |
| bap-1619-variant | variant | 1619 (offset=0 sub-slice) | 10 | 10 | done |
| bap-1622-strict | strict | 1620-1624 | 7 | 7 | done |
| bap-1622-variant (window) | variant | 1620-1624 | 44 | — | CAPPED (split into per-year sub-slices below) |
| bap-1620-variant | variant | 1620 (offset=0 sub-slice) | 15 | 15 | done |
| bap-1621-variant | variant | 1621 (offset=0 sub-slice) | 13 | 13 | done |
| bap-1623-variant | variant | 1623 (offset=0 sub-slice) | 14 | 14 | done |
| bap-1624-variant | variant | 1624 (offset=0 sub-slice) | 20 | 20 | done |
| bap-1622-variant | variant | 1622 (offset=0 sub-slice) | 12 | 12 | done |
| bap-1627-variant | variant | 1627 (offset=0 sub-slice) | 21 | 20 | CAPPED (1 row not retrieved, page=2 broken) |
| bap-1628-variant | variant | 1628 (offset=0 sub-slice) | 27 | 20 | CAPPED (7 rows not retrieved, page=2 broken) |
| bap-1629-variant | variant | 1629 (offset=0 sub-slice) | 17 | 17 | done |
| bap-1630-variant | variant | 1630 (offset=0 sub-slice) | 15 | 15 | done |
| bap-1631-variant | variant | 1631 (offset=0 sub-slice) | 13 | 13 | done |
| bap-1632-variant | variant | 1632 (offset=0 sub-slice) | 17 | 17 | done |
| bap-1633-variant | variant | 1633 (offset=0 sub-slice) | 21 | 20 | CAPPED (1 row not retrieved, page=2 broken) |
| bap-1634-variant | variant | 1634 (offset=0 sub-slice) | 25 | 20 | CAPPED (5 rows not retrieved, page=2 broken) |
| bap-1635-variant | variant | 1635 (offset=0 sub-slice) | 19 | 19 | done |
| bap-1636-variant | variant | 1636 (offset=0 sub-slice) | 18 | 18 | done |
| bap-1637-variant | variant | 1637 (offset=0 sub-slice) | 23 | 20 | CAPPED (3 rows not retrieved, page=2 broken) |
| bap-1638-variant | variant | 1638 (offset=0 sub-slice) | 20 | 20 | done |
| bap-1639-variant | variant | 1639 (offset=0 sub-slice) | 15 | 15 | done |
| bap-1640-variant | variant | 1640 (offset=0 sub-slice) | 16 | 16 | done |
|---|---|---|---|---|---|
| --- PRIORITY WINDOW 1627-1640 COMPLETE --- |
|---|---|---|---|---|---|
| bap-1641-variant | variant | 1641 (offset=0 sub-slice) | 10 | 10 | done |
| bap-1642-variant | variant | 1642 (offset=0 sub-slice) | 15 | 15 | done |
| bap-1643-variant | variant | 1643 (offset=0 sub-slice) | 15 | 15 | done |
| bap-1644-variant | variant | 1644 (offset=0 sub-slice) | 18 | 18 | done |
| bap-1645-variant | variant | 1645 (offset=0 sub-slice) | 13 | 13 | done |
| bap-1646-variant | variant | 1646 (offset=0 sub-slice) | 12 | 12 | done |
| bap-1647-variant | variant | 1647 (offset=0 sub-slice) | 11 | 11 | done |
| bap-1648-variant | variant | 1648 (offset=0 sub-slice) | 12 | 12 | done |
| bap-1649-variant | variant | 1649 (offset=0 sub-slice) | 12 | 12 | done |
| --- STEP 2 (1627-1649 variant per-year) COMPLETE --- |
|---|---|---|---|---|---|
| bap-1632-strict | strict | 1630-1634 | 5 | 5 | done (all rows duplicate exact-Gurney hits already seen in variant slices) |
| bap-1637-strict | strict | 1635-1639 | 12 | 12 | done (all rows duplicate exact-Gurney hits already seen in variant slices) |
| bap-1642-strict | strict | 1640-1644 | 5 | 5 | done (all rows duplicate exact-Gurney hits already seen in variant slices) |
| bap-1647-strict | strict | 1645-1649 | 7 | 7 | done (all rows duplicate exact-Gurney hits already seen in variant slices) |
| --- STEP 3 (strict-surname windows) COMPLETE --- |
|---|---|---|---|---|---|

## Session 2026-07-29 summary

Resumed from 189 captured rows. Completed remaining scope:
- `bap-1622-variant` sub-slice (skipped earlier)
- All of `bap-1627-variant` through `bap-1649-variant` (23 single-year variant slices, the full 1627-1649 span; 1627-1640 = emigrant priority window)
- Strict-surname windows `bap-1632-strict`, `bap-1637-strict`, `bap-1642-strict`, `bap-1647-strict` (offset=2). All strict-window rows were duplicates of exact-"Gurney" hits already captured in the variant per-year slices — strict search surfaced no rows the variant sweep had missed.
- Step 4 (burials collection re-run) NOT executed — out of scope for this session given step 2+3 completion; flagged as remaining work if a future session continues this sweep.

Total rows in file: 598 (409 added this session). CAPPED queries (page=2 broken, >20 results): bap-1627-variant (1 row lost), bap-1628-variant (7 rows lost), bap-1633-variant (1 row lost), bap-1634-variant (5 rows lost), bap-1637-variant (3 rows lost).

Colonial-name-band flags (Mary/Marie/Marye/Maria, Richard/Rychard, John/Jhon as child's first name, 1626-1636 baptism year), by year:
- 1627: `? Richard`, Ludgvan, Cornwall Baptisms; `G Mary`, Rowde Wiltshire, England Births & Baptisms 1538-1975; `G? Marie`, Reading, Berkshire Baptisms Index
- 1628: `Penrose Mary`, Manaccan, Cornwall Baptisms
- 1630: `Bray Mary`, Landulph, Cornwall Baptisms; `Gurny Mary`, Hitcham, Buckinghamshire Baptism Index; `Gernne John`, Toddington, Bedfordshire Baptisms; `Gurley Mary`, Westminster, England Births & Baptisms 1538-1975
- 1631: `G.Uth John` / `G?th John` (dup transcriptions), Wooburn, Buckinghamshire/England Births & Baptisms
- 1632: `Garnes John`, Stepney, England Births & Baptisms; `Gurner Mary` x3, Eythorne, Kent, England Births & Baptisms
- 1633: `? John` x2 (Botus Fleming and Golant-St Sampson, Cornwall Baptisms); `Garnes John`, Stepney; `Gurner Mary` x3, Eythorne, Kent
- 1634: `Gray Mary`, Tilston, Cheshire Diocese Of Chester Parish Baptisms; `G. John`, Norton, Suffolk, England Births & Baptisms
- 1635: `G. John`, Norton, Suffolk (recurs)
- 1636: `? Richard`, Ludgvan, Cornwall Baptisms

New Locations not represented in the earlier 1615-1626 data: Great Crosthwaite (Cumberland Baptisms), Chester St Oswald (Cheshire), Barrow on Humber (Lincolnshire), Guernsey/Channel Islands (Bailiwick Of Guernsey Parish Baptisms), Denton Norfolk, Cartmel (Lancashire), Luton (Bedfordshire), Dent (Yorkshire), Wedmore (Somerset), Kinnersley (Herefordshire), Edvin Loach (Herefordshire), Ayrshire/Perthshire/Haddingtonshire (Scotland), Chenies (Buckinghamshire), Wing (Buckinghamshire), Greenwich (Kent).
