# Round 6 raw web and image notes — 2026-07-19

## L-245 — authenticated Findmypast result check

Human results URL: <https://www.findmypast.com/search/results?datasetname=norfolk+burials&sid=103&lastname=r%3Fvett&firstname=edward>.

The signed-in result table contained **33 Edward R?vett/Rivett rows**, sorted by burial year. Its earliest visible entries were Edward Rivett, Shipdham, **1725**; Edward Rivett, Shipdham, **1785**; and Edward Rivett, Wymondham, **1811** (duplicate display row), followed by Edward Rivett, Shipdham, **1813**. The remaining rows are nineteenth century or later. There is no 1653 Great Yarmouth candidate in this Edward-only query.

This is a bounded index negative only. Findmypast's Norfolk parish datasets have known Great Yarmouth coverage gaps; it does not prove that no Edward Rivett was buried there in 1653. The supplied result capture is retained as `L-245-fmp-edward-rivett-results-sorted-by-burial-year.png`.

### Broader signed-in Rivett extension supplied after the Edward-only check

The additional captures are a **different, broader result set**; no exact session URL was supplied, so none is invented here. They show pre-1653 Rivett/Rivett-variant index rows: William Rivett at East Dereham, burial year displayed **1593–1640**; John Rivett at King's Lynn St Margaret with St Nicholas (1620 and 1623); several unnamed, Alice/Alyce, Samuel/Ryvet, Mary, James, Faith/Fayth rows in the same King's Lynn parish (1624–29); and scattered Framingham Pigot, Wymondham, Tharston, Lyng, Ingworth, and Filby rows through 1630. The records establish neither kinship nor identity. In particular, William's multi-year display must be resolved to a source image/transcript before it can be evaluated against the Gurney/Rivett question.

The supplied captures are retained as `L-245-fmp-rivett-burials-1593-1630-page1.png` and `L-245-fmp-rivett-burials-1628-1630-page2.png`.

## L-239 — Whinburgh upper-right-entry re-crop

Source: FamilySearch, *Manorial court rolls on the part of Garvestone, Reymerston, Thuxton, Mattishall and Yaxham, 1595–1790*, DGS 004389244.

- 6 September 1639 leaf: <https://www.familysearch.org/ark:/61903/3:1:S3HT-6X4K-X5>
- 26 October 1648 comparator leaf: <https://www.familysearch.org/ark:/61903/3:1:S3HT-6X45-XZ>

The two local masters copied here are the earlier full-resolution captures, not the 1536 × 791 viewer screenshots: `L-239-whinburgh-1639-S3HT-6X4K-X5-master.jpg` (3302 × 2395) and `L-239-whinburgh-1648-S3HT-6X45-XZ-master.jpg` (3245 × 2585). The `S3HT-6X4K-X5` master confirms its visible court heading as **6 September 1639**.

`L-239-whinburgh-1639-grid.png`, `L-239-whinburgh-1648-grid.png`, and the upper-right-entry crop ladder were generated with `tools/paleography_image_workbench.py`. Reproducible crop coordinates and the contact sheet are in `_local/L-239-1639-upper-right-henry-allen-manifest.md` and `_local/L-239-1639-upper-right-henry-allen-contact-sheet.png`; the 1648 comparison sheet is `L-239-1648-upper-right-comparator-sheet.png`.

**Reading boundary.** The re-crop improves legibility and retains the document-level context, but it does not safely resolve the struck-through relationship phrase or establish the putative Allen-sister inheritance structure. It therefore adds a durable specialist-review artifact, not a new kinship finding. Cite any future transcription by ARK and visible heading, never by inherited filename date.

## No presigned URLs

No presigned FamilySearch or image-CDN URL is retained in this folder.
