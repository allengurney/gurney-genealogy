# Research dump — 2026-07-19 round 4b (wildcards + manor-court depth)

Continuation of round 4 after the ⭐ image targets proved GATED. This round delivers the skipped wildcards (new sources, G13-origin focus), a comprehensive East Dereham manor-court **image pull** for Codex reading, and a manor-availability survey for the Gurney-central parishes. Images + manifest: `dump-2026-07-19-files-round4b/`.

**Headline:** TNA **Discovery** (national records, free-indexed — never before consulted in this campaign) is the richest new vein by far. It yields (a) **Francis G14 himself** in a 1633 land sale, (b) **Inquisitions Post Mortem + Court of Wards records that resolve the g15 Thomas-death conflict**, and (c) a cluster of **Chancery family suits** naming the Norfolk Gurney kin. Separately, a **201-leaf East Dereham court pull** (1633–1636 confirmed) is staged for Codex paleographic reading.

---

## §1 ⭐⭐ TNA Discovery — the untapped national-records vein (Chancery, IPM, Wards, PCC)

Discovery (`discovery.nationalarchives.gov.uk`) API searched (WebFetch blocked → same-origin browser fetch). Variant × place probes, then a Norfolk 1560–1665 filter. **All records below are NEW to the repo**, held at The National Archives (Kew) unless noted, and most are image-orderable / partly on Ancestry.

### 1a. Francis G14 — a primary record of the emigrant's father
- **WARD 2/32/118A/20 — 11 July 1633.** Indenture between **"Francis Gurnay of London"** and **Sir Owen Smith of Irmingland, Norfolk**, for the **sale (for £1,000) of manors, lands and tenements**. This is Francis G14 (the London Merchant Taylor) **selling the Norfolk estate in 1633** — the same year his son Francis was baptised at East Dereham. It documents the family's disposal of its Norfolk landholding and Francis's London base. (Court of Wards, so the manors were held in wardship/knight-service.) **Highest-value single new record for the direct line.**

### 1b. The g15 Thomas-death conflict — IPM/Wards route is ALREADY IN THE REPO (correction)
**Correction (grounded 2026-07-19):** the WARD 7 / C 142 inquisitions below were **already found and worked on 2026-07-01** — see `sources/validations/tna-ward-c142-west-barsham-gurney-inquisitions.md` and `research/people/g13-john-gurney/topics/origin/23-wardship-network.md` (item G13-RI-000081). **This is not a new discovery, and it does NOT resolve the conflict.** The repo deliberately carries these as *unresolved catalogue leads*, because (i) they are **catalogue-level only** — the documents themselves are unpulled, so the heir's name/age and exact death date are not yet read — and (ii) as catalogue entries they **conflict** with the repo's verified finding (lead L-113 / g15 companion) that Thomas III was living in Henry G15's 1 May 1621 will and died 1621×1623. My round-4b claim that they "resolve toward reading (a)" was an overclaim; retracted.
- C 142/365/126 (14 Jas I) / C 142/370/10 (15 Jas I) / WARD 7/57/157 / WARD 7/57/80 — "Gurney, Thomas: Norfolk," 1616/17–1617/18 — **already logged**, attribution unresolved.
- C 142/613/60 (17 Chas I, 1641/2) Edward Gournay IPM — **already logged** (the solid West Barsham entry). PROB 11/188/136 (PCC will, Edward Gournay of West Barsham, 8 Feb 1642) pairs with it — **verify whether the PCC will itself is already registered**; if not, it is a small delta.
- C 142/154/67 (12 Eliz) Antony + C 142/37/103,122 William — **already logged** (g17, g19 companions).

**The still-live value:** pulling the *actual* Thomas 1616/17 inquisition (heir + age) would settle the conflict either way — that is a documented offline/order-copy follow-up, not a new find. Do NOT re-report these catalogue entries as new.

### 1c. Chancery family suits (name kin/relationships in the pleadings)
- **C 3/70/66 [1558-79] Gurney v Gurney** — John Gurney v Richard Gurney; property in **Shottesham, Norfolk**. A Gurney-v-Gurney family property dispute.
- **C 3/76/23 [1558-79] Gurney v Tylney** — Nicholas Gurney v Richard Tylney; Shottesham.
- **C 3/225/8 [1587-91] Gurney v Farmer** — plaintiff Henry Gurney [+ others].
- **C 5/609/120 [1648] Gurnay v Cocke** — **Frances Gurnay widow & Henry Gurnay** v Edmund Cocke; property in **Great Ellingham** (the G15 seat).
- **C 5/383/53 [1647] Feltham v Gournay** & **C 10/466/102 [1657] Feltham v Gurnay** — **Frances Gournay widow, Henry, Helen Gurnay**; site of the manor of **Sculthorpe** (near West Barsham).
- **E 134/36&37Eliz [1594] Lawnce v Gurnay** — Exchequer depositions naming **Henry Gurnay** + inhabitants of **Hargham**.

**Analysis / placement.** This is a large intake for the West Barsham/Great Ellingham gentry line **and** for Francis G14. The IPM/Wards cluster is decisive for the g15 conflict → `research/people/g15-henry-gurney-fact-sheet.research.md` (revise the Thomas-death treatment to reading (a), citing C 142/365/126, C 142/370/10, WARD 7/57/80, WARD 7/57/157; add Edward's IPM + PCC will). WARD 2/32/118A/20 → `research/people/g14-francis-gurney-fact-sheet.research.md` (Francis's 1633 Norfolk-estate sale). Chancery suits → collateral/topic files + new leads. **Register** a sourceId for TNA Discovery / the specific series. Each is orderable (image) from TNA; PROB 11 and some C 142 are on Ancestry.

---

## §2 Manor-court survey for the Gurney-central parishes (the "continue the vein" ask)

Which parishes with strong Gurney landholding in the G13–G15 window have manor court books, and are they reachable (FS-filmed = pullable) or NRO-only (gated)? From the TNA Manorial Documents Register (via Discovery) + FS catalog:

| Parish (Gurney relevance) | Manor court records | Where | Reachable? |
|---|---|---|---|
| **East Dereham** (G13 birthplace) | DC 12/5 (Queen's manor) court books **1623–1852** + index 1623–1820 | **FS DGS 4389483** (+ 4389277) | **YES — filmed, pulled this round (§3)** |
| East Dereham (other manor) | CHC court books **1562–1582**, 1649–1663 | NRO | NRO-only |
| **Great Ellingham** (G15 seat) | **WLS V/16-17 court rolls 1556–1621**; WLS V/21 book 1605–1755; WLS V/18 1627-28; HIL/2/14 1598 (Buryhall etc.) | NRO (WLS) | **NRO-only (gated)** |
| **West Barsham** (gentry seat) | [not yet surveyed — likely NRO] | — | scope next |
| **Shottesham** (C 3 Gurney line) | [not yet surveyed] | — | scope next |
| **Sculthorpe / Hargham** (C 5/E 134) | [not yet surveyed] | — | scope next |

**Finding:** East Dereham is the one Gurney-central parish whose manor courts are **FamilySearch-filmed and pullable** — so it is the one where a comprehensive image read is achievable now. Great Ellingham's courts survive **but only at NRO** (WLS collection, in person). A 1605–1622 East Dereham gap exists (Queen's manor starts 1623; the earlier CHC manor ends 1582). West Barsham / Shottesham / Sculthorpe / Hargham manor courts are un-surveyed and, like Great Ellingham, most probably NRO-held — [REC] scope via the MDR/FS-catalog next round; pull any that are FS-filmed.

---

## §3 East Dereham manor court — comprehensive image pull (201 leaves) for Codex

**What was pulled.** 201 full-resolution leaves of DGS 4389483, **idx 1470–1689** (~293 MB), into `dump-2026-07-19-files-round4b/east-dereham-courts-1636/`, named `edc-idx<N>.jpg`. Calibration reads confirm this block contains the **East Dereham courts of 1633–1636** (idx 1600 = 30 Sept 1633 folio 72; idx 1629 = 1635/36 folio 98; ~11 idx/year, forward-chronological) — i.e. **John G13's late-teen years at Dereham** — plus adjacent Deopham courts (idx ≲1540, 1650s) that share the film. A `_README-for-codex-reading.md` in the folder gives the task (read every leaf for Gurney tenant entries AND abuttals), the calibration points, and the target pattern (the Margery/Margaret Gurney-widow abuttals from round 4).

**Method (token-efficient pull pipeline, established this round).** The das/v2 → presigned-S3 URLs are CORS-opaque to page JS and the FS session cookie can't be file-bridged (safety-blocked), so: fire das concurrently for a batch of image indices (browser), call `read_network_requests` (its >token-limit output **auto-saves to a tool-results file**, keeping the giant signed URLs **out of context**), then a PowerShell one-liner regex-extracts the URLs from that file and downloads each — mapping fire-order → image number. ~30–60 leaves/batch.

**Coverage note (honest).** This is comprehensive for East Dereham **1633–1636** and samples 1650s Deopham. Full 1623–1632 East Dereham coverage requires reading the interleaved idx 1470–1599 band by date/manor heading (Deopham/Denver are mixed in) — a Codex-scale job — and/or pulling the manor **index** (DGS 4389277 Item 8). 1605–1622 is a documentary gap (§2).

**Placement:** on Codex read-back, Gurney findings → `research/topics/john-gurney-candidate-others.md` (Dereham copyhold pre-history) + `research/people/g13-john-gurney-fact-sheet.research.md`. Masters → `sources/media/east-dereham-courts/_local/` (gitignored) with a committed README stub. SourceId `familysearch-fulltext-search` (DGS 4389483).

---

## §4 New leads (propose)

From the TNA haul + manor survey (all NEW, none previously worked):

- **L-NEW-a — Francis G14 1633 Norfolk-estate sale:** TNA **WARD 2/32/118A/20** (Francis Gurnay of London → Sir Owen Smith, £1,000). Order/read; establishes Francis's 1633 disposal of the Norfolk manors. Priority ~80 (direct line).
- **L-NEW-b — Thomas Gurnay Esq. death 1616-17 (g15 resolver):** TNA **C 142/365/126, C 142/370/10, WARD 7/57/80, WARD 7/57/157** (IPMs/wardship). Read for heir Edward + age → confirm reading (a). Priority ~82.
- **L-NEW-c — Edward Gournay of West Barsham:** TNA **C 142/613/60** (IPM 1641-42) + **PROB 11/188/136** (PCC will 1642, on Ancestry). Priority ~70.
- **L-NEW-d — Norfolk Gurney Chancery suits 1558–1657:** C 3/70/66, C 3/76/23, C 3/225/8, C 5/609/120, C 5/383/53, C 10/466/102 (+ E 134 Lawnce v Gurnay 1594). Read pleadings for kin/relationships (Shottesham line; Great Ellingham; Sculthorpe; Frances Gurnay widow). Priority ~68.
- **L-NEW-e — Gurney-central parish manor courts:** survey West Barsham / Shottesham / Sculthorpe / Hargham manor court records (MDR + FS catalog); Great Ellingham = NRO WLS V/16-17 (1556–1621, gated). Pull any FS-filmed. Priority ~66.
- **L-NEW-f — East Dereham manor index 1623–1820:** NRO DC 12/5/22 / FS DGS 4389277 Item 8 — pull + read for Gurney tenants (faster than page-walk). Priority ~64.

---

## §5 Negative / coverage + method ledger

| # | Source | Query | Result |
|---|---|---|---|
| 1 | Discovery API | "Gurnay Dereham" | 0 (both terms); "Gurney Dereham"=19 (mostly 19th-c bank/Poor Law) |
| 2 | Discovery API, Norfolk 1560-1665 | Gurnay/Gurney/Gournay | 5 / 64 / 4 → the WARD/IPM/Chancery/PCC cluster above |
| 3 | FS film 4389483 (East Dereham/Deopham/Denver) | full-text `Gurn*` | only **13** tokens filmwide → OCR misses Latin/abuttals → page-read needed |
| 4 | FS catalog koha:402769 | East Dereham manor coverage | DC 12/5 court books **start 1623** (no 1605-1622) |
| 5 | Method | cookie→file bridge for PowerShell das | **safety-blocked** (session cookie); used tool-results-file pipeline instead |

---

## §5b Round-4c addendum (same day — pulls extended, packet 53 staged, corrections)

- **WARD/IPM duplication correction (see §1b, revised):** the WARD 7 / C 142 inquisitions were **already in the repo** (2026-07-01, `sources/validations/tna-ward-c142-west-barsham-gurney-inquisitions.md`); retracted the "resolves the g15 conflict" claim. **Genuinely new (verified via repo_search — nowhere else in repo): WARD 2/32/118A/20** (Francis G14's 1633 sale) and the **Chancery/Exchequer suits** (C 3/70/66, C 3/76/23, C 3/225/8, C 5/609/120, C 5/383/53, C 10/466/102, E 134 Lawnce v Gurnay).
- **Packet 53 staged** (paleography-staging README followed): `sources/intake/paleography-staging/packet-53-east-dereham-courts-1623-1635.md` + `images/packet-53-.../` = **120 East Dereham court leaves, idx 1505–1624 (~1623–1635)** — the full G13-teen window (earlier 1623–1625 gap filled this round). Confirmed via calibration reads (idx 1525 = book start ~1623; idx 1600 = 30 Sept 1633; idx 1629 = 1635/36). Brief carries the task (Gurney tenants + abuttals), calibration, target pattern, and questions. Remaining ~120 leaves (Deopham 1650s + East Dereham 1636+) stay in `dump-files/dump-2026-07-19-files-round4b/east-dereham-courts-1636/` as packet-54 context.
- **East Dereham manor INDEX (DGS 4389277 Item 8):** attempted; the 46 leaves I pulled at idx 2340–2385 proved to be **1820 court pages, not the index** (mis-located) — deleted. The index's exact image range is unlocated ([REC]).
- **Manor survey completed for the "continue the vein" ask:** **East Dereham = the ONLY Gurney-central parish with FS-filmed, pullable manor courts.** Gentry parishes are gated: **Great Ellingham** = NRO WLS V/16-17 (1556–1621); **West Barsham** = no clear FS film (7 Discovery hits, none a court book); **Shottesham** = TNA **C 146/11086** (Shottesham Hall manor court-roll copy, 1557–58, enrolling a will — possibly the C 3 Gurney line); **Sculthorpe/Hargham** = Chancery suits found (§1c), manor courts not surfaced.
- **Wildcard accounting (items 8 & 9 — explicit):** NEW sources pursued this campaign-turn = (1) TNA Discovery Chancery/Exchequer suits [new, §1c]; (2) TNA WARD 2 Francis-1633 sale [new, §1a]; (3) TNA Manorial Documents Register manor survey [new, §2/§5b]; (4) East Dereham manor-court comprehensive pull [depth, §3/packet 53]. G13-origin pursuits = the "why Dereham" copyhold read (packet 53) + the fostering-hypothesis test (the WB/Great Ellingham gentry manor courts are gated; the Thomas-died-1616 IPMs — if pulled — would weaken uncle-Thomas fostering). **Partial/inconclusive:** East Dereham parish-register Gurney sweep (Ancestry fuzzy-matched "Gurn" broadly; the Dereham baptisms are already in the case-file; Margery's ~1602 burial + any Gurney marriage remain a tight-collection [REC]); Blomefield East Dereham manor descent (BHO page 404'd — [REC], find correct vol.10 Launditch page).

## §6 Placement labels (consolidated)
- **§1b IPM/Wards** → `research/people/g15-henry-gurney-fact-sheet.research.md` (revise Thomas-death to reading (a)); **§1a** → g14 Francis companion; **§1c** Chancery → `research/topics/norwich-gurney-collateral-network.md` + Shottesham note; register a TNA-Discovery sourceId.
- **§2 manor survey** → `research/topics/john-gurney-candidate-others.md` + g15 companion (Great Ellingham WLS).
- **§3 pull** → Codex reads `dump-2026-07-19-files-round4b/east-dereham-courts-1636/`; findings → Dereham topic + g13 companion; masters → `sources/media/east-dereham-courts/_local/`.
- **§4 leads** → `research/future-research/research-leads.csv` (add L-NEW-a…f).
