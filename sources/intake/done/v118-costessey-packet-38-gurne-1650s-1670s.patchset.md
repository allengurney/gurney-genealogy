**Done:** 2026-06-28 09:21 PT

# v118 — Costessey manorial: paleography packet 38 (John Gurne, 1650s–1670s)

Assimilates the packet-38 image reads (film 004389191, Costessey court material, analysed 2026-06-24) into `research/people/gurney-family-costessey-manorial.md`. The durable transcription already exists at `sources/corpus_supplement/paleo-2026-06-packet-38-costessey-john-gurne-1650s-1670s.md` (written this thread); this patchset promotes the findings into the companion and corrects the card-level table. Source: `familysearch-fulltext-search` (FS image reads; no new sourceId).

## Findings
- **1651, 1672 confirmed at image level** — John Gurne as a grouping/jury-list name (5 Mar 1651; 22 Oct 1672 courts). Genuine surname occurrences, not Jernegan.
- **1673 is an active court action** — 20 Sep 1673, "ad opus et usum Johannis Gurne," John Gurne admitted/surrendering, not merely a passive abuttal reference.
- **1674 "John Gurney, gentleman"** — the `gen[erosi]` cottage-abuttal (21 Jan 1674) is a property/status reference, **not a burial**. The earlier "[buried?]" guess is rejected.
- **Two card-level false positives corrected:** the "Spencer, John Gurnee" card (`3:1:S3HT-6PNG-DF`) reads *Johannes Spencer* — reject; and the staged image for ark `3:1:S3HT-6PNG-Y4` shows a 3 Oct 1633 page, with the real 1674 Church House abuttal on the adjacent leaf.
- **No John Gurne junior located.** The 1659 "sen[ior]" style still implies one; packet 38 does not find him. The 1670s John is a recurring, active Costessey copyholder styled gentleman.

## Operations

### Op 1 — `research/people/gurney-family-costessey-manorial.md`: correct the card-level table — `promote`

`str_replace`
old:
```
| 1651 | jury/homage list: "Thomas March, John [F]anny, John Gurnee, Thomas [—], John Howard" | 3:1:S3HT-6PNB-3J |
| 1672 | "John Turner … Johnes Gurne, Johnes Somes & Francis…" | 3:1:S3HT-6PN5-9N |
| 1673, 1675 | John Gurne in court entries | 3:1:S3HT-6PNK-4C, 3:1:S3HT-6PNP-7X |
| 1674 | "Church House … John Gurnee [buried?/dwelling?]" | 3:1:S3HT-6PNG-Y4 |
| 1620, 1641 | "Spencer, John Gurnee…" | 3:1:S3HT-6PNG-DF |
```
new:
```
| 1651 — image-confirmed | jury/homage list, John Gurne as a grouping heading (5 Mar 1651 court) | 3:1:S3HT-6PNB-3J |
| 1672 — image-confirmed | jury/homage list "Johannes Gurne" (22 Oct 1672 court) | 3:1:S3HT-6PN5-9N |
| 1673 — image-confirmed | John Gurne active admittance, "ad opus et usum Johannis Gurne" (20 Sep 1673 court) | 3:1:S3HT-6PNP-7X |
| 1674 — image-confirmed | "Johannis Gurne gen[erosi]" cottage abuttal (21 Jan 1674) — a property reference, **not** a burial | 3:1:S3HT-6PNK-4C |
| 1674 — image/ark mismatch | staged image shows a 3 Oct 1633 page; the 1674 Church House abuttal is on the adjacent leaf | 3:1:S3HT-6PNG-Y4 |
| rejected (was "1620, 1641 Spencer, John Gurnee") | reads *Johannes Spencer*, no Gurney — machine false positive | 3:1:S3HT-6PNG-DF |
```

### Op 2 — add the packet-38 reading paragraph (assimilate after the Packet 13 paragraph) — `promote`

`str_replace`
old:
```
**Case relevance.** The father–son pair is now **documentary, not merely inferential**: a John Gurne "the father," wife Margaret, and son John are named together in the 1648 Rippon settlement, corroborating the 1659 "sen[ior]" style. A John Gurney *senior* at Costessey implies a junior John whose birth could sit anywhere from the 1610s to the 1630s — the elimination question stands. The family's location at the laceweaver Francis B's manor keeps the kin-network question open. The decisive next steps are the un-read 1659-adjacent and 1670s pages and the film's earlier items, read with the Jernegan caution in force.
```
new:
```
**Packet 38 reads (2026-06-24) confirm a continuing, active John Gurne through the 1670s.** Image reads of the 1650s–70s court sequence confirm John Gurne as a grouping/jury-list name in the **5 March 1651** and **22 October 1672** courts; an **active admittance** on **20 September 1673** ("ad opus et usum Johannis Gurne," John petitioning for/receiving the lord's grant — more than a passive abuttal); and the **21 January 1674** cottage abuttal styling him **gentleman** ("Johannis Gurne gen[erosi]"). That 1674 Church House entry is a copyhold/property description, **not** a burial — correcting the earlier card-level "[buried?]" guess — and the staged image for ark `3:1:S3HT-6PNG-Y4` is in fact a 3 October 1633 page (the 1674 material sits on the adjacent leaf). The card "Spencer, John Gurnee" (`3:1:S3HT-6PNG-DF`) is rejected as *Johannes Spencer*. No John Gurne **junior** is located in the packet; the 1659 "sen[ior]" style still implies one by inference, but the 1670s gentleman is best read as a single continuing Costessey John Gurne rather than evidence of a distinct junior.[^packet38]

**Case relevance.** The father–son pair is **documentary, not merely inferential**: a John Gurne "the father," wife Margaret, and son John are named together in the 1648 Rippon settlement, corroborating the 1659 "sen[ior]" style. A John Gurney *senior* at Costessey implies a junior John whose birth could sit anywhere from the 1610s to the 1630s — the elimination question stands. The family's location at the laceweaver Francis B's manor keeps the kin-network question open. The decisive next steps are the un-read 1659-adjacent pages and the film's earlier items (the junior John is still unrecovered), read with the Jernegan caution in force.
```

### Op 3 — add the packet-38 footnote (after `[^packet13]`) — `promote`

`str_replace`
old:
```
[^packet13]: Expert paleography reads (packet 13, 2026-06-15) of Costessey court images on film 004389191: [ark:/61903/3:1:S3HT-6PN9-9SP](https://www.familysearch.org/ark:/61903/3:1:S3HT-6PN9-9SP?view=fullText) (Thomas Rippon surrender; "John Gurne the father" + Margaret his wife for life, remainder to son John Gurne; recited court 11 Oct 1648) and [ark:/61903/3:1:S3HT-6PNV-DD](https://www.familysearch.org/ark:/61903/3:1:S3HT-6PNV-DD?view=fullText) ("John Gurne & Margaret his wife … heirs of the said John"); the 1625 image `3:1:S3HT-6PN2-L1` yielded no secure Gurne name. Source ID: `familysearch-fulltext-search`.
```
new:
```
[^packet13]: Expert paleography reads (packet 13, 2026-06-15) of Costessey court images on film 004389191: [ark:/61903/3:1:S3HT-6PN9-9SP](https://www.familysearch.org/ark:/61903/3:1:S3HT-6PN9-9SP?view=fullText) (Thomas Rippon surrender; "John Gurne the father" + Margaret his wife for life, remainder to son John Gurne; recited court 11 Oct 1648) and [ark:/61903/3:1:S3HT-6PNV-DD](https://www.familysearch.org/ark:/61903/3:1:S3HT-6PNV-DD?view=fullText) ("John Gurne & Margaret his wife … heirs of the said John"); the 1625 image `3:1:S3HT-6PN2-L1` yielded no secure Gurne name. Source ID: `familysearch-fulltext-search`.
[^packet38]: Paleography packet 38 (2026-06-24), image reads of Costessey court material on film 004389191: 5 Mar 1651 ([3:1:S3HT-6PNB-3J](https://www.familysearch.org/ark:/61903/3:1:S3HT-6PNB-3J?view=fullText)), 22 Oct 1672 ([3:1:S3HT-6PN5-9N](https://www.familysearch.org/ark:/61903/3:1:S3HT-6PN5-9N?view=fullText)), 20 Sep 1673 admittance ([3:1:S3HT-6PNP-7X](https://www.familysearch.org/ark:/61903/3:1:S3HT-6PNP-7X?view=fullText)), 21 Jan 1674 "Johannis Gurne gen[erosi]" abuttal ([3:1:S3HT-6PNK-4C](https://www.familysearch.org/ark:/61903/3:1:S3HT-6PNK-4C?view=fullText)); the `3:1:S3HT-6PNG-Y4` staged image is a 3 Oct 1633 page and `3:1:S3HT-6PNG-DF` is a Spencer entry. Transcription at `sources/corpus_supplement/paleo-2026-06-packet-38-costessey-john-gurne-1650s-1670s.md`. Source ID: `familysearch-fulltext-search`.
```

### Op 4 — update open question 2 to reflect packet 38 — `promote`

`str_replace`
old:
```
2. Identify **John Gurney junior** implied by the 1659 "sen" style, and the relation of the 1670s "John Gurney, gentleman" to the 1629/1659 men. (Available online — film 004389191, unread pages.)
```
new:
```
2. Identify **John Gurney junior** implied by the 1659 "sen" style. Packet 38 (2026-06-24) read the 1650s–70s sequence and resolved the 1670s "John Gurney, gentleman" as a single continuing, active Costessey copyholder (admittance 1673; gentleman abuttal 1674) — but did **not** locate a distinct junior; the 1659-adjacent and earlier film pages remain the place to look. (Available online — film 004389191, unread pages.)
```

## Staging disposition (Phase 2, after promotion)
- Move both `sources/intake/paleography-staging/packet-38-costessey-john-gurney-1650s-1670s.md` (brief) and `…report.md` to `sources/intake/paleography-staging/done/`.
- Move the packet-38 image masters to `sources/media/familysearch-fulltext-search/_local/` (or a `costessey-004389191/_local/` folder) with a committed README stub naming the files, the FamilySearch-terms reason, and the retrieval arks; the durable transcription already lives in `corpus_supplement`.

## Validation after application
- Confirm the `[^packet38]` footnote resolves and the card table renders.
