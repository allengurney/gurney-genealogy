# Validation — The National Archives, Discovery catalogue

- **Source ID:** `tna-discovery-catalogue`
- **Source:** The National Archives, Discovery online catalogue, https://discovery.nationalarchives.gov.uk, searched through the public search API at `/API/search/records`.
- **Examined:** 28 July 2026.

## What was examined

A systematic surname sweep, not a targeted lookup. Fourteen Gurney surname variants — Gurney, Gurny,
Gurnay, Gournay, Gourney, Gurnie, Gorney, Garney, Gerney, Girney, Gurneye, Gournaye, Gurnoe, Gorny —
each queried separately with `sps.dateFrom=1590-01-01` and `sps.dateTo=1685-12-31`, paging to
exhaustion. Result: 753 unique records across all repositories, 92 of them naming a John of a Gurney
variant.

The same variant list was re-run without a date filter to obtain the complete E 115 (certificates of
residence), REQ 2 (Court of Requests) and STAC (Star Chamber) blocks, which are otherwise clipped by
covering-date overlap.

Eleven keyword-paired runs tested specific propositions: `… AND "East Dereham"`, `… AND Dereham`,
`… AND Hockliffe`, `… AND (Pakington OR "Westwood Park" OR Bedgrove)`, `… AND (tailor OR taylor)`,
`… AND ("Weston Turville" OR Bierton OR Broughton)`, `… AND (Cheddington OR Edlesborough OR Ivinghoe
OR Marsworth OR Stewkley OR Stuteley)`, `… AND (Playstow OR "Stoke Mandeville")`, and full-record
detail calls on seven references.

## Scope and limits

Discovery carries **catalogue descriptions, not document text**. A person named only inside an
uncalendared bill, deposition or deed does not surface, so an absence here is an absence from the
finding aid rather than from the record.

Item-level description is dense for the classes used: Chancery pleadings C 1–C 10, Court of Requests
REQ 2, Exchequer certificates of residence E 115, Exchequer depositions by commission E 134, Star
Chamber STAC, Court of Wards deeds WARD 2, and PCC wills PROB 11. Contributed catalogues from other
repositories vary from full item abstracts (Bedfordshire Archives assize files, Buckinghamshire
Archives deeds, the Pakington Buckinghamshire deeds at Worcestershire) to collection-level stubs.
Manorial court rolls and parish registers are catalogued as volumes, so their contents are invisible.

No document has been examined at image level. Every finding derived from this sweep is catalogue
level.

## Where findings landed

- Extract, with every quoted description verbatim and the full sweep parameters:
  [`sources/corpus_supplement/tna-discovery-gurney-equity-and-estate-records-1590-1685.md`](../corpus_supplement/tna-discovery-gurney-equity-and-estate-records-1590-1685.md)
- Analysis:
  [`research/people/g13-john-gurney/topics/identity/55-refactor-central-court-and-estate-records.md`](../../research/people/g13-john-gurney/topics/identity/55-refactor-central-court-and-estate-records.md)
- Open actions arising, including the three Kew document requests:
  [`research/people/g13-john-gurney/topics/identity/59-refactor-open-actions.md`](../../research/people/g13-john-gurney/topics/identity/59-refactor-open-actions.md)
- Graph tracker: [`sources/intake/g13-graph-breadcrumb.md`](../intake/g13-graph-breadcrumb.md)

## Method note

The API accepts `sps.searchQuery` with boolean operators and phrase quoting, `sps.dateFrom` /
`sps.dateTo` on covering dates (overlap semantics, so a wide-range collection record is returned by
a narrow window), `sps.resultsPageSize` up to 1000, and `sps.page`. `sps.reference` did not filter
in testing; scope by department or class by filtering the returned `reference` field instead.
Full descriptions come from `/API/records/v1/details/{id}`, where `id` is the internal identifier in
the search result, not the archival reference.
