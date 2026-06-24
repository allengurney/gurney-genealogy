**Done:** 2026-06-23 21:05 PT

# Patchset v115 — BHO discovery consolidation (IPM / Cecil / VCH promotions, paleography P37, FS + BHO skills)

**Phase 1 draft.** Consolidates the June-2026 British History Online full-text discovery arc and the returned Costessey-1659 paleography read. Corpus supplements, the Cecil and Townshend-IPM sourceIds, and all lead writes (L-174–L-179 added; L-93, L-98 updated) were already applied **directly** this arc per the user's split; this patchset carries the remaining research-companion promotions, two new VCH sources + four validations, the P37 disposition, and the FS/BHO skill updates.

Scope notes for the applier:
- Paleography packets 34/35/36 are already incorporated and in `done/`; only **P37** needs incorporation + disposition here. P38/P39 stay staged (awaiting reads).
- Every promotion **assimilates** into existing prose (no dated session blocks); footnotes are preserved and added per `citations.md`.
- No open-question / to-do prose is added to companions; residual pursuit lives in leads (L-93, L-176, L-177, L-178, L-179).

---

## Item 1 — promote: William Gurney IV (G19) as Sir Roger Townshend's feoffee (1493)

**Outcome:** promote. **Destination:** `research/people/g19-william-gurney-iv-fact-sheet.research.md`. Source already registered: `bho-ipm-henry-vii-townshend-gurnay-feoffee` (corpus extract at `sources/corpus_supplement/bho-ipm-henry-vii-townshend-gurnay-feoffee.md`).

`str_replace` in `research/people/g19-william-gurney-iv-fact-sheet.research.md`:

- old_string:
```
### Calthorpe residence — Pockthorpe (DG-Supp Note 131)
```
- new_string:
```
### Townshend feoffee, 1493 (Calendar of Inquisitions Post Mortem, Henry VII)

William Gurnay, esq., recurs as a feoffee-to-uses (trustee) throughout the estate of **Sir Roger Townshend, knight**, of Raynham, in Townshend's inquisitions post mortem; Townshend died 9 November, 9 Henry VII (1493), and the trust was still live at his death. The lands William helped hold to the family's use include the Townshend manor called "Havyles" in East, West, and South Raynham, with Helloughton, Toftes, Oxwick, Whissonsett, Horningtoft, and Gateley, and a messuage and land at Hadleigh in Suffolk. His co-feoffees are the top tier of late-fifteenth-century Norfolk society and church: William Pekenham, Archdeacon of Suffolk, Thomas Woodhouse, Edward Knyvet, John and Thomas Blakeney, Thomas Gygges, gent., Edmund Harberd (clerk), William Wayte, and John Pegeon.[^townshend-feoffee-1493]

This puts the West Barsham line inside the Townshend–Heydon–Knyvet–Blakeney trust circle at primary-record level. The same affinity is documented on the marriage side: Sir Roger Townshend's wife Amy Heydon was the sister of Anne Heydon, wife of William IV's son William Gurney V (G18). The calendar abstract gives the family forename as "William Gurnay, esq." without a distinguishing descriptor — most economically William IV himself (the family head and escheator), though his same-named son William V was also living in 1493.[^townshend-feoffee-1493]

[^townshend-feoffee-1493]: "Inquisitions Post Mortem, Henry VII, Entries 1101–1150," in *Calendar of Inquisitions Post Mortem: Series 2, Volume 1, Henry VII* (London: HMSO), pp. 469–504, British History Online, https://www.british-history.ac.uk/inquis-post-mortem/series2-vol1/pp469-504. William Gurnay, esq., named as feoffee in the IPMs of Sir Roger Townshend, knt. (d. 9 Nov. 1493); verbatim extracts and co-feoffee list at `sources/corpus_supplement/bho-ipm-henry-vii-townshend-gurnay-feoffee.md`. Surfaced via a BHO full-text "Gurnay" sweep, June 2026. Source ID: `bho-ipm-henry-vii-townshend-gurnay-feoffee`.

### Calthorpe residence — Pockthorpe (DG-Supp Note 131)
```

---

## Item 2 — promote: Edmund Gurnay's 1606 appeal to Salisbury over the Corpus Christi suspension

**Outcome:** promote. **Destination:** `research/people/edmund-gurney-divine.research.md`. Source already registered: `cal-cecil-papers-hatfield` (corpus extract at `sources/corpus_supplement/cecil-papers-vol18-edmund-gurnay-1606-cambridge.md`). This primary-sources and re-dates DNB's "1607 suspension" (already in the academic-career table) to a live 1606 dispute and names the antagonists.

`str_replace` in `research/people/edmund-gurney-divine.research.md`:

- old_string:
```
## Clerical career: Edgefield and Harpley
```
- new_string:
```
## The 1606 Corpus Christi suspension — Edmund's own appeal to Salisbury

The Cecil (Hatfield) Papers preserve Edmund's own letter behind the Cambridge fellowship suspension that DNB and the Venn/ACAD record date to 1607. Calendared as undated and assigned to 1606, **Edmund Gurnay writes to Robert Cecil, Earl of Salisbury, as Chancellor of the University of Cambridge**, appealing a suspension imposed within Corpus Christi. He says the College "prefect" (the Master) suspended him and, in the person of the visitor, ratified the suspension under an enclosed statute; he has not yet lost his board and emoluments. He frames the obstacle as fear of the see of Norwich — the College lawyers "will not open their mouths against the Bishop of that see or the Bishop's brother who is their present prefect" — and asks Salisbury to have the case referred to neutral civil lawyers, naming Sir Daniel Dunn, Dr. Richard Swale, and Dr. Steward.[^cecil-1606-suspension]

In 1606 the Bishop of Norwich was John Jegon and the Master of Corpus Christi was his brother Thomas Jegon — so the letter identifies the antagonist as Master Thomas Jegon, backed by his brother the bishop, and shows the dispute already live in 1606, a year before the suspension that DNB reports. It is the primary-document witness to the episode the secondary record summarizes, and it places Edmund appealing over the Master's head to the university Chancellor.[^cecil-1606-suspension]

[^cecil-1606-suspension]: "Cecil Papers: Miscellaneous 1605," in *Calendar of the Cecil Papers in Hatfield House: Volume 18, 1606*, ed. M. S. Giuseppi (London, 1940), pp. 371–462, British History Online, https://www.british-history.ac.uk/cal-cecil-papers/vol18/pp371-462. Edmund Gurnay to the Earl of Salisbury, Chancellor of Cambridge, [1606], appealing his Corpus Christi suspension; full extract at `sources/corpus_supplement/cecil-papers-vol18-edmund-gurnay-1606-cambridge.md`. Bishop John Jegon of Norwich and his brother Master Thomas Jegon of Corpus Christi identified from standard episcopal/college lists. A second Edmund Gurnay calendar entry falls in December 1602 (Cecil Papers vol. 12), not yet extracted (lead L-179). Source ID: `cal-cecil-papers-hatfield`.

## Clerical career: Edgefield and Harpley
```

---

## Item 3 — promote: the Hampshire manor of Wellow Gurnay (West Wellow), Robert de Gurnay's holding

**Outcome:** promote. **Destination:** `research/places/somerset-gournay-collateral.md`. **New source:** `vch-hants-vol4-wellow-gurnay` (Item 7 registers it). Robert de Gurnay (d. 1269) is the same baron whose Over/Redwick/Almondsbury descent (Robert → Anselm → John → Elizabeth → John ap Adam) is already documented in this file from Pettigrew and Rudder; the VCH Hampshire entry adds a Hampshire limb of the same inheritance.

`str_replace` in `research/places/somerset-gournay-collateral.md`:

- old_string:
```
## Sir Matthew de Gournay

Sir Matthew de Gournay, fourth son of the regicide Sir Thomas, is a major collateral military figure.
```
- new_string:
```
## VCH Hampshire — Wellow Gurnay (West Wellow), a further ap-Adam-transmitted manor

The Victoria County History of Hampshire records a Gurnay manor at **West Wellow** that descended through the same Somerset baronial heirs already traced here from the Gloucestershire side. About 1240 **Robert de Gurnay held a quarter of a knight's fee in Wellow**; in 1267–8 certain of his West Wellow tenants complained that through his default they were distrained by Henry de Lacy and his wife Margaret. **Robert de Gurnay died in 1269**, and the manor passed, with that of Hyde in South Damerham, to his grandson **John**. In 1296 it was settled, **under the name of Wellow Gurnay, upon John de Badeham (John ap Adam) and his wife Elizabeth** — the Elizabeth de Gournay (daughter and heir of John de Gournay) whose marriage to John ap Adam carried the Over, Redwick, and Northwick manors in the same years.[^vch-hants-wellow-gurnay]

The Hampshire entry is therefore an independent witness to the Robert → John → Elizabeth → ap Adam transmission, adding two holdings (the manor of Wellow Gurnay in West Wellow and Hyde in South Damerham) and the place-name "Wellow Gurnay" that fossilizes the family's tenure. No Gurnay holding is recorded in East Wellow or Embley proper; the family's interest was in West Wellow.[^vch-hants-wellow-gurnay]

[^vch-hants-wellow-gurnay]: "Parishes: East Wellow with Dunwood and Embley," in *A History of the County of Hampshire: Volume 4* (London: VCH, 1911), pp. 535–540, British History Online, https://www.british-history.ac.uk/vch/hants/vol4/pp535-540. West Wellow manor ("Wellow Gurnay"): Robert de Gurnay held a quarter-fee c. 1240, died 1269, manor to grandson John with Hyde in South Damerham, settled 1296 on John ap Adam (John de Badeham) and Elizabeth his wife. Surfaced via a BHO full-text "Gurnay" sweep, June 2026 (lead L-176). Source ID: `vch-hants-vol4-wellow-gurnay`.

## Sir Matthew de Gournay

Sir Matthew de Gournay, fourth son of the regicide Sir Thomas, is a major collateral military figure.
```

---

## Item 4 — promote: VCH Buckinghamshire detail on the Bledlow manor (Bec exchange + Juliana's recovery)

**Outcome:** promote. **Destination:** `research/topics/brooke-rye-selected-gurney-references.md` (where the Juliana de Gournay × William Bardolf identification is discussed). **New source:** `vch-bucks-vol2-bledlow` (Item 7 registers it). The core Juliana/Bardolf descent is already held; the VCH adds the Henry II grant, the 1198 Bec-Hellouin exchange, and Juliana's 1285–6 recovery attempt.

`str_replace` in `research/topics/brooke-rye-selected-gurney-references.md`:

- old_string:
```
The page also preserves the Mountfort burial at Keynsham (Somerset) — a useful place anchor for any future senior-collateral place work.[^brooke-p92]
```
- new_string:
```
The page also preserves the Mountfort burial at Keynsham (Somerset) — a useful place anchor for any future senior-collateral place work.[^brooke-p92]

The Victoria County History of Buckinghamshire fills in the manor by which the senior English lands reached the Bardolfs. Henry II appears to have granted the manor of **Bledlow** to **Hugh de Gurnay** before 1177; in **1198 Hugh exchanged it to the abbey of Bec-Hellouin** in Normandy, after which it was held in frankalmoign in chief of the king. Hugh kept certain Bledlow tenements, which passed to his daughter **Juliana**, wife of **William Bardolf**; in 1285–6 Juliana and her husband attempted to recover the manor itself from the Abbot of Bec. Their Bardolf descendants held rents in Bledlow without interruption until the early fifteenth century (Sir Thomas Bardolf). This dates the Gournay–Bardolf transmission of the senior English lands to a specific manor and pair of transactions.[^vch-bucks-bledlow]

[^vch-bucks-bledlow]: "The parishes of Risborough hundred: Bledlow," in *A History of the County of Buckingham: Volume 2* (London: VCH, 1908), pp. 247–253, British History Online, https://www.british-history.ac.uk/vch/bucks/vol2/pp247-253. Henry II's grant of Bledlow to Hugh de Gurnay (before 1177); the 1198 exchange to Bec-Hellouin; retained tenements to his daughter Juliana (m. William Bardolf) and her 1285–6 recovery attempt from the Abbot of Bec; Bardolf rents to the early fifteenth century. Surfaced via a BHO full-text "Gurnay" sweep, June 2026 (lead L-177). Source ID: `vch-bucks-vol2-bledlow`.
```

---

## Item 5 — promote + dispose: Costessey 1659 court (paleography Packet 37)

**Outcome:** promote (the image-confirmed reading and the negative) + dispose the packet. **Destinations:** `research/people/gurney-family-costessey-manorial.md`; `sources/corpus_supplement/`; `sources/media/costessey-manorial-court-fts/_local/`; `sources/intake/paleography-staging/done/`. The manor-name residual stays as lead L-93 (already updated). No new open-question prose is added.

### 5a — `str_replace` in `research/people/gurney-family-costessey-manorial.md`

- old_string:
```
2. **April 1659**: a court leet/court baron default memorandum (the court held for **Anthony Dobbs of Marsham, esquire** — note the lord is not the Jernegan baronet, so this list may belong to a different manor bundled on the film) lists among tenants/suitors "…Richard Knight, John [Burbis?], **John Gurney sen**[ior]…" with Thomasine Rookwood and others. The "senior" style implies a **junior John Gurney** existed in 1659 — the father-son pair survives, by inference rather than by the earlier "son of John" misreading.[^packet4]
```
- new_string:
```
2. **April 1659**: a court leet/court baron default memorandum (the court held for **Anthony Dobbs of Marsham, esquire** — note the lord is not the Jernegan baronet, so this list may belong to a different manor bundled on the film) lists among tenants/suitors "…Richard Knight, John [Burbis?], **John Gurney sen**[ior]…" with Thomasine Rookwood and others. The "senior" style implies a **junior John Gurney** existed in 1659 — the father-son pair survives, by inference rather than by the earlier "son of John" misreading.[^packet4] A 2026 image re-read confirmed from the manuscript the court heading "…twentieth daye of Aprill … one thousand six hundred fiftie nine … of Anthony Dobbs of Marsham Esq[uire]" and the suit-list reading "John Gurney sen"; an adjacent crowded "Gurney jun[?]"-looking form is too uncertain to promote. The **manor name was not legible on the staged leaves**, so which manor held the Dobbs court is unresolved and pursued as lead L-93.[^packet37]
```

### 5b — `str_replace` to add the Packet 37 footnote (place it immediately after the existing `[^packet4]` definition)

- old_string:
```
[^packet4]: Expert read of [ark:/61903/3:1:S3HT-6PN9-SXB](https://www.familysearch.org/ark:/61903/3:1:S3HT-6PN9-SXB?view=fullText) (court leet memorandum, April 1659), 2026-06-11; report at `sources/corpus_supplement/paleo-2026-06-packet-04-costessey-name-list-john-gurnee.md`. Source ID: `familysearch-fulltext-search`.
```
- new_string:
```
[^packet4]: Expert read of [ark:/61903/3:1:S3HT-6PN9-SXB](https://www.familysearch.org/ark:/61903/3:1:S3HT-6PN9-SXB?view=fullText) (court leet memorandum, April 1659), 2026-06-11; report at `sources/corpus_supplement/paleo-2026-06-packet-04-costessey-name-list-john-gurnee.md`. Source ID: `familysearch-fulltext-search`.

[^packet37]: Expert image re-read of the April 1659 court memorandum on film/DGS 004389191, ark [3:1:S3HT-6PN9-SXB](https://www.familysearch.org/ark:/61903/3:1:S3HT-6PN9-SXB?view=fullText), with staged context leaves (manuscript pp. 302–304), 2026-06-23 (paleography Packet 37); transcription at `sources/corpus_supplement/paleo-2026-06-packet-37-costessey-1659-court-opening.md`. Confirmed the "twentieth daye of Aprill … 1659 … of Anthony Dobbs of Marsham Esq" heading and the "John Gurney sen" suit-list reading; the court's manor name was not legible on the staged or adjacent leaves. Source ID: `familysearch-fulltext-search`.
```

### 5c — `new file write`: `sources/corpus_supplement/paleo-2026-06-packet-37-costessey-1659-court-opening.md`

```
# Costessey court roll — the April 1659 default memorandum (paleography Packet 37, 2026-06-23)

Manorial court rolls, 1540–1900 (Costessey and bundled manors), FamilySearch film/DGS 004389191. Court hand, English with Latin formulae. The April 1659 default/suit memorandum sits on the manuscript opening at ark `3:1:S3HT-6PN9-SXB`; context leaves at arks `3:1:S3HT-6PN9-9TS` and `3:1:S3HT-6PNG-DX`.

## Confirmed reading

The right-hand page continues a memorandum dated, in substance:

> … and twentieth daye of Aprill in the yeare of our lord one thousand six hundred fiftie nine … of Anthony Dobbs of Marsham Esq[uire] …

The compact suit/default name-list on the same page reads, in part:

> … John Windage, John Brereton gent, Edward Tyler, Albert […] Wandulff gent, Richard Knight, John [Burbis?], John Gurney sen, John […] Gurney jun[?], Thomasine Rookwood, Gregory Moore, Thomas […] Gibson, Thomas [ffre?], Wearyard, Edward […]

The secure reading is **"John Gurney sen"**; the adjacent "Gurney jun[?]" form is in crowded text and is not secure (it may be a different surname or a visual carryover from the target line).

## Negative / limits

- The **manor name is not stated** on the staged or adjacent leaves; the memorandum is a continuation/subsequent entry rather than a full court-opening formula, so which manor held the court "of Anthony Dobbs of Marsham" was not recoverable here.
- The machine-transcript place token "in Burton aforesaid" was not confirmed from the images.
- Costessey's lords were the Jernegan (Jerningham) baronets; machine transcripts of this film systematically misread *Jernegan* as a Gurney-form, so Gurney readings on this film require image confirmation.

Confidence: April 1659 / Anthony Dobbs of Marsham context, high; "John Gurney sen" reading, high; second "Gurney jun" name, low; manor name, unresolved.
```

### 5d — file moves (disposition)

1. Move `sources/intake/paleography-staging/packet-37-costessey-1659-court-opening.md` → `sources/intake/paleography-staging/done/packet-37-costessey-1659-court-opening.brief.md`.
2. Move `sources/intake/paleography-staging/packet-37-costessey-1659-court-opening.report.md` → `sources/intake/paleography-staging/done/packet-37-costessey-1659-court-opening.report.md`.
3. Move the staged context masters `sources/intake/paleography-staging/images/packet-37-costessey-1659-court-opening/img-1707-3-1-S3HT-6PN9-9TS.jpg` and `img-1708-3-1-S3HT-6PNG-DX.jpg` → `sources/media/costessey-manorial-court-fts/_local/` (working masters for manuscript pp. 302–303). Delete the two byte-identical page-304 captures `img-1709-3-1-S3HT-6PNK-3Z.jpg` and `img-1710-3-1-S3HT-6PN9-SXB.jpg` (duplicates of each other; the real SXB master is already at `sources/media/costessey-manorial-court-fts/_local/costessey-son-of-john-sxb.jpg`), then remove the emptied `images/packet-37-costessey-1659-court-opening/` folder.
4. Append to `sources/media/costessey-manorial-court-fts/_local/README.md` two rows naming `img-1707-…-9TS.jpg` (Costessey court, ms p. 302, context before the April 1659 memorandum) and `img-1708-…-DX.jpg` (ms p. 303, context), with the FamilySearch-terms reason and the retrieval arks `3:1:S3HT-6PN9-9TS` and `3:1:S3HT-6PNG-DX`.

---

## Item 6 — skill update: FamilySearch full-text research (new image-pull learnings)

**Outcome:** promote. **Destination:** `.claude/skills/familysearch-fulltext-research/SKILL.md`.

### 6a — `str_replace` (add the concurrent-batch download unlock to §3)

- old_string:
```
The deepzoom tile URLs visible in the viewer (`.../deepzoomcloud/dz/v1/apid:TH-.../image_files/...`) expose the current image's apid but not its neighbours'.
```
- new_string:
```
The deepzoom tile URLs visible in the viewer (`.../deepzoomcloud/dz/v1/apid:TH-.../image_files/...`) expose the current image's apid but not its neighbours'.

**Batch many images per round trip — fire the das requests *concurrently* (the throughput unlock, 2026-06).** Under the Claude-in-Chrome MCP the network log surfaces only ~one fresh das→S3 redirect per *sequential, awaited* das fetch, and the das/v2 response is cacheable, so a sequential loop re-reads the cache and only the first ark redirects. Two fixes together make batching reliable: (a) fire all arks at once with `Promise.all(arks.map(a => fetch(\`https://www.familysearch.org/das/v2/${a}/dist.jpg?cb=${Date.now()}_${i}\`, {credentials:'include', cache:'no-store'}).catch(()=>null)))` — concurrent firing logs *all* the S3 redirects; the `?cb=` cache-buster + `cache:'no-store'` defeats the das cache. (b) To pull "image N" without returning arks past the browser MCP's privacy guard, look the ark up from `window.__imgs[N-1]` *inside* the page and fetch it there, returning only a fired-count; then read the presigned S3 URLs from the network log (they carry `TH-…` ids, not arks/query-bearing FS URLs, so they pass the guard). The S3 requests appear in **fire order**, so map `TH-id → image number` positionally. One `read_network_requests` (pattern `pipe-storage-das-cloud-prod-dasS3`) then yields ~6–14 presigned URLs to hand to one PowerShell `Invoke-WebRequest` loop. Net cost ≈ fire + one network read + one download ≈ 0.3–0.5 tool calls per image.

**Caveat — the in-memory `window.__imgs` index can be off by ~one leaf from the manuscript page.** Confirmed 2026-06: opening ark `…SXB` placed it at array index 1709 and the "preceding" ark `…3Z` resolved (via das) to the *same scan* already pulled as the "image 1710" SXB target — i.e. the array's index-to-leaf alignment, and das's ark-to-scan mapping, can both drift by one and can collapse adjacent arks onto one physical scan. **Anchor on a confirmed ark, not the image number:** verify `window.__imgs[N-1].ark` against a known page before trusting the label, and treat duplicate byte-sizes across "adjacent" pulls as a collapsed/duplicate scan.
```

### 6b — `str_replace` (add the image-restricted-collection failure mode to §5)

- old_string:
```
Full catalogue with examples in `sources/validations/familysearch-fulltext-search.md`. Headlines: Latin court hand transcribes as word salad (thin hit counts ≠ absence); lookalike names are systematic (*Jernegan*→"Gurney" at Costessey, *Atturney*→"At-Gurney", place-name *Gurnet's Nose*; real distinct surnames Gurnell/Garnsey/Garner ride the wildcards); card year-lists mix document dates with stray numbers; never promote a forename or kinship from a Latin-entry transcript without an image read.
```
- new_string:
```
Full catalogue with examples in `sources/validations/familysearch-fulltext-search.md`. Headlines: Latin court hand transcribes as word salad (thin hit counts ≠ absence); lookalike names are systematic (*Jernegan*→"Gurney" at Costessey, *Atturney*→"At-Gurney", place-name *Gurnet's Nose*; real distinct surnames Gurnell/Garnsey/Garner ride the wildcards); card year-lists mix document dates with stray numbers; never promote a forename or kinship from a Latin-entry transcript without an image read.

**Image-restricted (index-only) collections — the index hit is real but the image is not pullable on FS.** Confirmed 2026-06 for **"England, Norfolk, Parish Registers (County Record Office), 1510–1997"**: indexed christening/burial records (e.g. the Shimpling Wales entries `VNN6-7MQ`, `VNN6-7S2`, `VNN6-D2B`) resolve to a record page that shows **"Image Unavailable"** — the NRO-contract collection exposes the index only, so the das/v2 path returns nothing and there is no viewer image to walk. Confirm a target is image-bearing (open one record and check for a viewable image) before staging a pull; for index-only Norfolk-CRO parish registers the image route is FindMyPast, Ancestry, or the Norfolk Record Office, not FamilySearch.
```

---

## Item 7 — new sources + validations

### 7a — `str_replace` in `data/sources.json` (register the two new VCH sources; insert after the `bho-ipm-henry-vii-townshend-gurnay-feoffee` block)

- old_string:
```
      "notes": "William Gurnay, esq. (West Barsham family; most likely G19 William IV, escheator, d.1508, or his son William V) recurs as feoffee-to-uses in the IPMs of Sir Roger Townshend, knt., d. 9 Nov 1493 (9 Hen VII) - the Raynham manor 'Havyles', Helloughton, Whissonsett, Horningtoft, Gateley, and Hadleigh (Suffolk). Co-feoffees: William Pekenham (Archdeacon of Suffolk), Thomas Woodhouse, Edward Knyvet, John/Thomas Blakeney, Thomas Gygges. Primary-record evidence of the Gurney-Townshend-Heydon-Knyvet trust affinity (Townshend's wife Amy Heydon was sister to Anne Heydon, wife of G18 William V). Calendar abstract level. Surfaced via BHO full-text 'Gurnay' sweep, June 2026."
    },
```
- new_string:
```
      "notes": "William Gurnay, esq. (West Barsham family; most likely G19 William IV, escheator, d.1508, or his son William V) recurs as feoffee-to-uses in the IPMs of Sir Roger Townshend, knt., d. 9 Nov 1493 (9 Hen VII) - the Raynham manor 'Havyles', Helloughton, Whissonsett, Horningtoft, Gateley, and Hadleigh (Suffolk). Co-feoffees: William Pekenham (Archdeacon of Suffolk), Thomas Woodhouse, Edward Knyvet, John/Thomas Blakeney, Thomas Gygges. Primary-record evidence of the Gurney-Townshend-Heydon-Knyvet trust affinity (Townshend's wife Amy Heydon was sister to Anne Heydon, wife of G18 William V). Calendar abstract level. Surfaced via BHO full-text 'Gurnay' sweep, June 2026."
    },
    "vch-hants-vol4-wellow-gurnay": {
      "shortTitle": "VCH Hampshire vol. 4 - East Wellow / Wellow Gurnay",
      "citation": "\"Parishes: East Wellow with Dunwood and Embley.\" A History of the County of Hampshire, Volume 4 (London: VCH, 1911), pp. 535-540. British History Online.",
      "archive": "British History Online",
      "url": "https://www.british-history.ac.uk/vch/hants/vol4/pp535-540",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/vch-hants-vol4-wellow-gurnay.md",
      "notes": "West Wellow manor 'Wellow Gurnay': Robert de Gurnay held a quarter-fee c.1240, died 1269; manor passed with Hyde in South Damerham to his grandson John; settled 1296 on John ap Adam (John de Badeham) and Elizabeth his wife - the Hampshire limb of the Somerset Robert->John->Elizabeth->ap Adam transmission. Collateral/senior-line, not direct Norfolk. Surfaced via BHO full-text 'Gurnay' sweep, June 2026 (lead L-176)."
    },
    "vch-bucks-vol2-bledlow": {
      "shortTitle": "VCH Buckinghamshire vol. 2 - Bledlow",
      "citation": "\"The parishes of Risborough hundred: Bledlow.\" A History of the County of Buckingham, Volume 2 (London: VCH, 1908), pp. 247-253. British History Online.",
      "archive": "British History Online",
      "url": "https://www.british-history.ac.uk/vch/bucks/vol2/pp247-253",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/vch-bucks-vol2-bledlow.md",
      "notes": "Bledlow manor: granted by Henry II to Hugh de Gurnay before 1177; exchanged 1198 to Bec-Hellouin abbey; retained tenements to his daughter Juliana (m. William Bardolf), who with her husband sought recovery from the Abbot of Bec in 1285-6; Bardolf rents to the early 15th c. Adds the Bec-exchange + recovery specifics to the known Juliana-de-Gournay/Bardolf descent. Senior line. Surfaced via BHO full-text 'Gurnay' sweep, June 2026 (lead L-177)."
    },
```

### 7b — `new file write`: `sources/validations/cal-cecil-papers-hatfield.md`

```
# Validation — Calendar of the Cecil Papers in Hatfield House (`cal-cecil-papers-hatfield`)

- **Source examined:** Calendar of the Cecil Papers in Hatfield House, British History Online (free series). Vol. 18 (1606), pp. 371–462, "Cecil Papers: Miscellaneous 1605."
- **Portion examined:** the single calendar entry of Edmund Gurnay's [1606] letter to the Earl of Salisbury, Chancellor of Cambridge, appealing his Corpus Christi College suspension. Abstract level (English calendar of the manuscript).
- **Unexamined / uncertain:** the manuscript original; the December 1602 Edmund Gurnay entry (Cecil Papers vol. 12) is not yet pulled (lead L-179); broader Cecil/State Papers sweep for Henry G15 outstanding (L-179).
- **Findings recorded at:** `research/people/edmund-gurney-divine.research.md` (1606 suspension section); full extract at `sources/corpus_supplement/cecil-papers-vol18-edmund-gurnay-1606-cambridge.md`.
```

### 7c — `new file write`: `sources/validations/bho-ipm-henry-vii-townshend-gurnay-feoffee.md`

```
# Validation — Calendar of IPM, Henry VII, Townshend feoffee entries (`bho-ipm-henry-vii-townshend-gurnay-feoffee`)

- **Source examined:** Calendar of Inquisitions Post Mortem, Series 2, Vol. 1 (Henry VII), entries 1101–1150, British History Online (free series), pp. 469–504.
- **Portion examined:** the inquisitions of Sir Roger Townshend, knt. (d. 9 Nov. 1493), where William Gurnay, esq., is named as feoffee; co-feoffees and the manors (Havyles/Raynham, Helloughton, Whissonsett, Horningtoft, Gateley, Hadleigh) captured. Calendar abstract; the Latin originals not consulted.
- **Unexamined / uncertain:** whether the feoffee is G19 William IV or his son William V (both living 1493); adjacent Henry VII/VIII IPMs of Townshend, Knyvet, Heydon, Calthorpe for further Gurnay feoffee appearances (lead L-175).
- **Findings recorded at:** `research/people/g19-william-gurney-iv-fact-sheet.research.md` (Townshend feoffee section); full extract at `sources/corpus_supplement/bho-ipm-henry-vii-townshend-gurnay-feoffee.md`.
```

### 7d — `new file write`: `sources/validations/vch-hants-vol4-wellow-gurnay.md`

```
# Validation — VCH Hampshire vol. 4, East Wellow / Wellow Gurnay (`vch-hants-vol4-wellow-gurnay`)

- **Source examined:** "Parishes: East Wellow with Dunwood and Embley," VCH Hampshire vol. 4 (1911), pp. 535–540, British History Online (free series).
- **Portion examined:** the West Wellow (Wellow Gurnay) manor descent only — Robert de Gurnay's quarter-fee c. 1240, his death 1269, passage to grandson John with Hyde in South Damerham, and the 1296 settlement on John ap Adam and Elizabeth.
- **Unexamined / uncertain:** the underlying feet-of-fines / IPM references behind the VCH descent; whether "Hyde in South Damerham" warrants separate place treatment.
- **Findings recorded at:** `research/places/somerset-gournay-collateral.md` (Wellow Gurnay section).
```

### 7e — `new file write`: `sources/validations/vch-bucks-vol2-bledlow.md`

```
# Validation — VCH Buckinghamshire vol. 2, Bledlow (`vch-bucks-vol2-bledlow`)

- **Source examined:** "The parishes of Risborough hundred: Bledlow," VCH Buckinghamshire vol. 2 (1908), pp. 247–253, British History Online (free series).
- **Portion examined:** the Gurnay/Bardolf descent of the Bledlow manor only — Henry II's grant to Hugh de Gurnay (pre-1177), the 1198 Bec-Hellouin exchange, Juliana de Gurnay's (m. William Bardolf) 1285–6 recovery attempt, and the Bardolf rents to the early 15th century.
- **Unexamined / uncertain:** the post-Bec Abbey descent; the Camden/Bardolf cross-references already noted in `data/sources.json` for the related Mapledurham/Wendover/Hulcott holdings.
- **Findings recorded at:** `research/topics/brooke-rye-selected-gurney-references.md` (Juliana/Bardolf discussion).
```

---

## Item 8 — new skill: British History Online research

**Outcome:** promote. **Destination:** `.claude/skills/british-history-online-research/SKILL.md` (new skill folder + file).

`new file write`: `.claude/skills/british-history-online-research/SKILL.md`

```
---
name: british-history-online-research
description: Operational recipes for British History Online (BHO) full-text research - the in-browser search that bypasses the bot-gate, variant + co-occurrence query design across the BHO series landscape, free vs gold-paywalled content, result-anchor extraction, and the ground-before-claiming discipline that keeps a wide net from re-capturing held material. Read before any BHO full-text discovery task.
---

British History Online (british-history.ac.uk) is a large free/subscription digitised corpus of British printed primary and secondary sources. For the Gurney project it is far more than Blomefield's *Norfolk* topography (the parish pages for the family's own manors are already captured): the high-yield, under-mined veins are the **other series** that incidentally name the family.

> **Search *strategy* (variants, wildcarding, co-occurrence/token anchoring, source-awareness) is source-agnostic and lives in [`online-discovery-strategy`](../online-discovery-strategy/SKILL.md) — read that first.** This file is BHO *mechanics*: how to search it, what it holds, what is free, and how to triage.

## 1. The search works in the live browser (not headless fetch)

The BHO search endpoint `https://www.british-history.ac.uk/search?query=<terms>` returns a **CAPTCHA / bot-challenge** to a plain server-side fetch (WebFetch), so it reads as "no results." In an **authenticated/live browser** (Claude-in-Chrome) the same URL renders normally — navigate to it and read the page. Phrase search: wrap in `%22…%22`. The search is loose (terms can match in different parts of a long page), so treat multi-word and "phrase" hits as candidates to verify, not exact matches.

- **Result list:** the rendered page lists ~10 hits/page with the series title and a snippet. `get_page_text` returns the list cleanly. To get the result **URLs**, walk the anchors in-page (`document.querySelectorAll('a')`, keep hrefs containing `british-history.ac.uk` and not `/search`).
- **Content pages** (the actual articles, e.g. `/topographical-hist-norfolk/…`, `/vch/…`, `/inquis-post-mortem/…`) are **not** bot-gated — WebFetch reads them. For a long page, extract just the Gurnay context in-page: `body.innerText`, find each case-insensitive `gurnay`/`gournay`/`gurney` and slice ~±220 chars, or select paragraphs/entries containing the variant. WebFetch summarises but caps verbatim quotes — for a corpus extract pull the verbatim from the live page instead.

## 2. Variant + co-occurrence query design

Use the project variant set (`data/search-variants.json`). Practical notes for BHO's clean OCR of printed editions:
- Search the **Tudor/medieval spelling `Gurnay`** to surface the family with far less pollution than `Gurney` (which is swamped by the 19th-c. Buxton/Gurney bankers and modern indexes). Then `Gournay` (Norman/senior line) and the documentary forms (`Gornay`, `Gerneye`/`Gernay` — collision-prone, treat as leads).
- **Co-occurrence / in-law anchoring** is the high-yield move the user asked for: pair a variant with a **property name** (West Barsham, Harpley, Swathing/Hardingham, Pockthorpe, Saxthorpe) or an **in-law surname** (Calthorpe, Heydon, Blennerhasset, Jerningham/Jernegan, Hovell, Knyvet, Townshend, Bardolf). This finds incidental mentions (feoffee/trustee roles, marriage settlements, manor descents) the bare-name query buries.
- Enumerate the family's footprint by drilling the *index* pages (e.g. CIPM "Index of Persons and Places: G") to find which volumes hold a Gurnay, then read those entries.

## 3. The series landscape — and free vs gold

BHO mixes **free** content (digitised by rekeying/OCR) and **gold** (subscription) content; gold pages render only the access/navigation chrome (and WebFetch reports a paywall / login). Known from the June-2026 sweep:
- **Free, high-yield:** Blomefield *Norfolk* (topography — mostly already captured); **Calendar of the Cecil Papers (Hatfield)**; **Letters and Papers, Henry VIII**; **Victoria County History** (per-county, e.g. Hants, Bucks, Glos for the West-Country Gournays); **Calendar of Inquisitions Post Mortem** (including the Series-2 Henry VII–VIII volumes and the per-volume "Index: G" pages).
- **Gold-paywalled (snippet only):** **Calendar of Close Rolls** and at least some **Calendar of Patent Rolls** volumes — the search snippet is visible but the full entry needs a subscription (or the AALT/TNA image route).

## 4. Ground before claiming new (mandatory)

BHO is a *wide net* over a repo that is already deep. **Before promoting any BHO hit, ground it** with `repo_search.py` (locate the names/manor in `research/`, `sources/corpus*`, `data/sources.json`) — much of the medieval material is already held via Blomefield, Daniel Gurney, Farrer, Pettigrew, Rudder, Brooke/Rye, and the Camden/Cawley senior-line work. Worked June-2026 outcomes that show the discipline paying off:
- **New & promoted:** William Gurnay as Sir Roger Townshend's feoffee (CIPM Henry VII, 1493); Edmund Gurnay's 1606 Cecil-Papers appeal to Salisbury; the Hampshire manor "Wellow Gurnay" (VCH Hants); the Bledlow Bec-exchange detail (VCH Bucks).
- **Caught as already-held (not re-captured):** the Hardingham/Swathing manor descent; the 1469/70 Thomas Gurnay will; the core Juliana de Gournay × Bardolf descent.
- **Grounded out as not-our-line:** "John Gerneye" granted an Exeter consistory office (Letters & Papers Henry VIII vol. 17, 1542) — a Devon/West-Country or distinct-surname figure, the `Gerneye` variant being collision-prone; retained as a checked negative, not promoted.

## See also
- `.claude/skills/online-discovery-strategy/SKILL.md` — the two reasoning gates and cause-matched technique selection (read first).
- `data/search-variants.json` — the variant registry.
- `tools/repo_search_README.md` — the grounding tool.
```

---

## Source-tracking

- **Existing sourceIds reused:** `familysearch-fulltext-search` (Costessey P37), `cal-cecil-papers-hatfield` (added directly this arc — validation added here, Item 7b), `bho-ipm-henry-vii-townshend-gurnay-feoffee` (added directly this arc — validation added here, Item 7c).
- **New sourceIds (Item 7a):** `vch-hants-vol4-wellow-gurnay` (+ validation 7d), `vch-bucks-vol2-bledlow` (+ validation 7e).
- **Corpus supplements:** `cecil-papers-vol18-edmund-gurnay-1606-cambridge.md` and `bho-ipm-henry-vii-townshend-gurnay-feoffee.md` already written directly; `paleo-2026-06-packet-37-costessey-1659-court-opening.md` written here (Item 5c).

## Lead-tracking (already applied directly; recorded here for traceability)

- **Added:** L-174 (BHO non-Blomefield variant sweep), L-175 (Townshend feoffee network), L-176 (Wellow Gurnay, Hants), L-177 (Bledlow Bec-exchange detail), L-178 (Bardolf overlordship origin — derived), L-179 (Henry G15 in Cecil/State Papers — derived).
- **Updated:** L-93 (Costessey — P37 read: manor unrecovered; P38 staged), L-98 (East Dereham — P39 calibration staged).
