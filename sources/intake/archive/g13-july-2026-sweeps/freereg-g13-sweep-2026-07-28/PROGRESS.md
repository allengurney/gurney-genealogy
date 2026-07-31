# FreeREG G13 sweep — 2026-07-28

Sweep of freereg.org.uk for Gurney-variant parish records, all counties, 1600-1660.

## Calibration query

Surname `Gurney`, no forename, Baptism, 1600-1660, all counties, soundex OFF: **"We found 143 Results"**, and every returned surname token was exact `GURNEY` (checked via `[A-Z]{4,}` token scan across all result rows — no `GOURNEY`/`GURNY`/`GURNIE`/etc. present). FreeREG's non-soundex surname matching is therefore **exact-only, not fuzzy**. Conclusion: every spelling in the priority list must be run as its own separate query (no spellings can be skipped as "already covered").

Extraction method used for the full sweep: FreeREG's search form (`POST /search_queries`, Rails formtastic form, fields `search_query[last_name/first_name/start_year/end_year/record_type/chapman_codes][]/fuzzy/inclusive/witness/no_surname/search_nearby_places]` + CSRF `authenticity_token`) and the resulting `/search_records/<id>/<slug>` detail pages are both served anonymously (no login/session required). Rather than driving this through the browser UI (which hit a small per-call text-output cap unsuitable for hundreds of rows), the sweep was executed with a Python `requests`+`BeautifulSoup` script (`freereg_sweep.py`, run from scratch pad, not committed to the repo) that replicates the exact same form POST and detail-page parse the browser workflow would have done, with 8-way concurrent detail-page fetches per query. Field mapping per record type:
- Baptism: `Person forename` / `Father surname` / `Father forename` / `Mother forename` / `Baptism date`.
- Marriage: `Groom|Bride forename/surname` (whichever side matches the searched spelling) / `Marriage date`; father/mother fields are almost never present on marriage entries.
- Burial: `Burial person forename/surname` / `Relationship` + `Male relative forename` mapped to father_forename (and `Female relative forename` to mother_forename) only when `Relationship` is "son of"/"daughter of"/"child of" — a "wife of"/"husband of" relative is not a parent and is left blank.

## Query log

| query_id | surname | record_type | years | counties | rows_returned | gurney_cluster_rows | status |
|---|---|---|---|---|---|---|---|
| bap-gurney | Gurney | Baptism | 1600-1660 | all | 143 | 143 | done |
| bap-gurny | Gurny | Baptism | 1600-1660 | all | 13 | 13 | done |
| bap-gurnie | Gurnie | Baptism | 1600-1660 | all | 1 | 1 | done |
| bap-gourney | Gourney | Baptism | 1600-1660 | all | 16 | 16 | done |
| bap-gourny | Gourny | Baptism | 1600-1660 | all | 1 | 1 | done |
| bap-gorney | Gorney | Baptism | 1600-1660 | all | 0 | 0 | done |
| bap-gurnay | Gurnay | Baptism | 1600-1660 | all | 4 | 4 | done |
| bap-gournay | Gournay | Baptism | 1600-1660 | all | 3 | 3 | done |
| bap-garney | Garney | Baptism | 1600-1660 | all | 9 | 9 | done |
| bap-girney | Girney | Baptism | 1600-1660 | all | 5 | 5 | done |
| bap-gerney | Gerney | Baptism | 1600-1660 | all | 1 | 1 | done |
| bap-gernne | Gernne | Baptism | 1600-1660 | all | 0 | 0 | done |
| bap-gowrney | Gowrney | Baptism | 1600-1660 | all | 0 | 0 | done |
| bap-gorne | Gorne | Baptism | 1600-1660 | all | 1 | 1 | done |
| bap-garne | Garne | Baptism | 1600-1660 | all | 10 | 10 | done |
| bap-gurnoe | Gurnoe | Baptism | 1600-1660 | all | 0 | 0 | TIMEOUT (resolved by bap-gurnoe-retry below, n=2) |
| bap-gurner | Gurner | Baptism | 1600-1660 | all | 22 | 22 | done |
| bap-greney | Greney | Baptism | 1600-1660 | all | 1 | 1 | done |
| bap-gowrne | Gowrne | Baptism | 1600-1660 | all | 0 | 0 | done |
| bap-hurney | Hurney | Baptism | 1600-1660 | all | 0 | 0 | done |
| mar-gurney | Gurney | Marriage | 1600-1660 | all | 108 | 108 | done |
| mar-gurny | Gurny | Marriage | 1600-1660 | all | 5 | 5 | done |
| mar-gurnie | Gurnie | Marriage | 1600-1660 | all | 4 | 4 | done |
| mar-gourney | Gourney | Marriage | 1600-1660 | all | 13 | 13 | done |
| mar-gourny | Gourny | Marriage | 1600-1660 | all | 0 | 0 | done |
| mar-gorney | Gorney | Marriage | 1600-1660 | all | 2 | 2 | done |
| mar-gurnay | Gurnay | Marriage | 1600-1660 | all | 5 | 5 | done |
| mar-gournay | Gournay | Marriage | 1600-1660 | all | 0 | 0 | done |
| mar-garney | Garney | Marriage | 1600-1660 | all | 5 | 5 | done |
| mar-girney | Girney | Marriage | 1600-1660 | all | 4 | 4 | done |
| mar-gerney | Gerney | Marriage | 1600-1660 | all | 4 | 4 | done |
| mar-gernne | Gernne | Marriage | 1600-1660 | all | 0 | 0 | done |
| mar-gowrney | Gowrney | Marriage | 1600-1660 | all | 1 | 1 | done |
| mar-gorne | Gorne | Marriage | 1600-1660 | all | 2 | 2 | done |
| mar-garne | Garne | Marriage | 1600-1660 | all | 14 | 14 | done |
| mar-gurnoe | Gurnoe | Marriage | 1600-1660 | all | 0 | 0 | done |
| mar-gurner | Gurner | Marriage | 1600-1660 | all | 10 | 10 | done |
| mar-greney | Greney | Marriage | 1600-1660 | all | 0 | 0 | done |
| mar-gowrne | Gowrne | Marriage | 1600-1660 | all | 0 | 0 | done |
| mar-hurney | Hurney | Marriage | 1600-1660 | all | 1 | 1 | done |
| bur-gurney | Gurney | Burial | 1600-1660 | all | 107 | 107 | done |
| bur-gurny | Gurny | Burial | 1600-1660 | all | 16 | 16 | done |
| bur-gurnie | Gurnie | Burial | 1600-1660 | all | 1 | 1 | done |
| bur-gourney | Gourney | Burial | 1600-1660 | all | 7 | 7 | done |
| bur-gourny | Gourny | Burial | 1600-1660 | all | 0 | 0 | done |
| bur-gorney | Gorney | Burial | 1600-1660 | all | 0 | 0 | done |
| bur-gurnay | Gurnay | Burial | 1600-1660 | all | 1 | 1 | done |
| bur-gournay | Gournay | Burial | 1600-1660 | all | 1 | 1 | done |
| bur-garney | Garney | Burial | 1600-1660 | all | 5 | 5 | done |
| bur-girney | Girney | Burial | 1600-1660 | all | 10 | 10 | done |
| bur-gerney | Gerney | Burial | 1600-1660 | all | 0 | 0 | done |
| bur-gernne | Gernne | Burial | 1600-1660 | all | 0 | 0 | done |
| bur-gowrney | Gowrney | Burial | 1600-1660 | all | 0 | 0 | done |
| bur-gorne | Gorne | Burial | 1600-1660 | all | 2 | 2 | done |
| bur-garne | Garne | Burial | 1600-1660 | all | 12 | 12 | done |
| bur-gurnoe | Gurnoe | Burial | 1600-1660 | all | 0 | 0 | done |
| bur-gurner | Gurner | Burial | 1600-1660 | all | 13 | 13 | done |
| bur-greney | Greney | Burial | 1600-1660 | all | 0 | 0 | done |
| bur-gowrne | Gowrne | Burial | 1600-1660 | all | 0 | 0 | done |
| bur-hurney | Hurney | Burial | 1600-1660 | all | 0 | 0 | done |
| bap-gurnoe-retry | Gurnoe | Baptism | 1600-1660 | all | 2 | 2 | done |

## Final summary

- **Queries planned:** 60 (20 spellings x 3 record types, Baptism/Marriage/Burial, all counties, 1600-1660).
- **Queries run:** 61 (60 planned + 1 retry of the single timeout, `bap-gurnoe-retry`). All 61 completed successfully; 0 left in a CAPPED-500 or unresolved-TIMEOUT state.
- **Total Gurney-cluster records captured:** 585 rows in `results.tsv` (largest single-spelling counts: `Gurney` baptism 143, `Gurney` marriage 108, `Gurney` burial 107 — all comfortably under the 500-row display cap, so no query needed date-range splitting).
- **Spellings with zero hits across all three record types (1600-1660, all counties):** Gorney, Gernne, Gowrney, Gowrne, Hurney (baptism only had 0 for Hurney; Hurney had 1 marriage hit and 0 burial).
- **Timeouts:** 1 (`bap-gurnoe`, first attempt) — resolved on retry (`bap-gurnoe-retry`, n=2). No unresolved timeouts remain.
- **Capped queries:** none.
- **Father-named-John rows:** 38 records (full list with URLs in `_summary.txt` in this same folder) span baptisms and burials from ~1600 to ~1659, across Bedfordshire, Buckinghamshire, Worcestershire, Northamptonshire (Lamport — a large John+Anne Gurney/Gournay family recurring 1630-1650), Norfolk (Earsham — John+Ales Girney), Kent, and London.
- **Father John + mother Mary (the colonial-target combination):** **no rows in the entire 585-row dataset have both father=John and mother=Mary/variant.** The 38 father-John rows have mothers Frauncis/Dorothy/Anne/Isabell/Jane/Elizabeth/Ales or blank (none Mary); separately, 30 rows have mother=Mary/variant but fathers are Robert, James, Walter, Edward, Richard, William/Willm, Henry, or Jeames/Georgii (none John). No baptism matches the colonial target children (Mary b.~1628, Richard b.~1630, John b.~1633) under a John+Mary parentage in this sweep.
