**Done:** 2026-06-15 07:53 PT

# v98 — Blomefield Harpley + Gascon Rolls corroboration; NCC will-register 1624–1642 FTS discovery; leads + FTS-skill updates

**Phase 1 patchset.** Covers the 2026-06-14 research thread: a web-leads round (Blomefield Harpley, Gascon Rolls, Burke, Rye) and three FamilySearch FTS rounds that swept the NCC Consistory will-register gap (1624–1651) and staged five paleography bundles (packets 13–17, 18 images, in `sources/intake/paleography-staging/`).

**Scope discipline.** Two clean, image-or-print-confirmed promotions (Blomefield Harpley → g29; Gascon Rolls Norfolk-signal → soldier-database topic). The FTS manuscript sightings are recorded as findings-in-progress (machine transcript; image reads staged for the paleographer) plus new leads — not promoted as confirmed facts, per the "never promote a forename/kinship from a Latin-entry transcript without an image read" rule. No new `sourceId`s are minted: `blomefield-norfolk`, `gascon-rolls-project`, and `familysearch-fulltext-search` all already exist, so no new `data/sources.json` entries and no new validation files are required.

**Rejected as duplicative (no operation):**
- **L-118 Walter Rye, *The Gurneys of Norwich*** — already held in full as `rye-norfolk-antiquarian` (OCR extract `sources/corpus/norfolk-antiquarian-gurneys-of-norwich.md`, cited in the G14 companion, `francis-gurney-of-maldon.md`, and the case file). Closed to `research-leads-done.csv` (item 5 below).
- **Burke *Landed Gentry* (L-71)** — Maldon-branch collector content; Maldon is collateral and deprioritized. Lead retained at lowered priority (item 5); not promoted to a companion.
- **Earsham John Gurney will body (packet 17)** — the family structure (son John a minor; brother Lyon; contingent remainder under 21) is **already integrated** on `john-gurney-earsham-will-1638.md`. Packet 17 images are confirmatory and remain staged for a definitive full transcription (and to resolve whether the "sister / nephew William" clause is page-boundary bleed from an adjacent will, as happened in packet 11). Lead note only (item 5).

---

## Item 1 — PROMOTE: Blomefield's Harpley extracted (L-46) → g29 Matthew companion

Fulfils the g29 companion's Open Question #1 ("Blomefield's Harpley … Priority extraction") and the "Not yet extracted" note in Sources Consulted. Source: Blomefield, *Topographical History of Norfolk*, vol. 8 (Freebridge Hundred and Half: Harpley), pp. 452–459, read via British History Online. Cite existing `sourceId: blomefield-norfolk`. No new validation (existing source).

**1a. New Working-Notes entry** — `str_replace` in `research/people/g29-matthew-de-gournay-fact-sheet.research.md`:

`old_string`:
```
2026-04-18 — Blomefield's Harpley entry (vol. viii, pp. 452–459) should contain independent detail on how Harpley passed from the Burnhams to the Gurneys via Rose's marriage. This is flagged as a priority Blomefield extraction in the places file for Harpley.
```

`new_string`:
```
2026-04-18 — Blomefield's Harpley entry (vol. viii, pp. 452–459) should contain independent detail on how Harpley passed from the Burnhams to the Gurneys via Rose's marriage. This is flagged as a priority Blomefield extraction in the places file for Harpley.

### Blomefield's Harpley — extracted (2026-06-14)
Blomefield's Harpley account (vol. 8, pp. 452–459) independently confirms the acquisition and traces the full descent. William de Burnham granted the moiety of his fee to his brother Reginald, whose "only daughter and heir, Rose … was given in marriage by **Hameline Plantagenet, Earl Warren** … to **Matthew de Gurney**, who was lord in her right, about the 30th of Henry II"; a fine of 30 Henry II settled the manor on Matthew and his heirs, to hold by half a fee. The line then runs William de Gournay (son of Matthew) → John de Gournay (son of William, "with Sir Henry Hastings at the battle of Lewes" [1264], recovered the advowson 3 Edw. I, granted a fair 35 Edw. I) → John de Gournoy (nephew, son of Catherine, held 27–34 Edw. III) → Edmund de Gurnay (presented and "lord and patron" 1360) → John Gournay (presented 1387) → John Gournay, Esq. (died 9 Hen. IV; widow Alice held a court 10 Hen. IV). The Tudor exit: "Thomas Gurnay presented to the church in 1443, and William Gurnay, Esq. in 1485, and **Anthony Gurnay, in 1511, who, with Elizabeth his wife, was living in 1535, and soon after conveyed it to Sir John Allen, Knt.**" — after which the manor passed through Curson, Stubbs, Yelverton, and Walpole. Harpley church preserved a Gournay rector's gravestone, "Hic jacet corpus Joh'is de Gournay, quonda' rectoris et patroni hujus ecclesie" (John de Gournay, rector, died 6 Edw. III), and the church windows displayed the arms **"Gournay, argent, a cross ingrailed gules."** The rector list also gives "Edmund Gurnay, B.D., presented 1620" — Edmund Gurney the Divine (rector of Harpley 1620–48). This independently corroborates Daniel Gurney and Armstrong (1781) on the Matthew + Rose de Burnham acquisition, supplies the engrailed-cross arms as a Harpley-church witness (relevant to the American-arms question), and fixes the manor's departure from the family c. 1535.[^blomefield-harpley-1810]
```

**1b. Footnote definition** — append at end of file (`str_replace` on the final existing footnote line). `old_string`:
```
[^v71-armstrong-matthew-rose]: Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 5 (Norwich, 1781), Gallow Hundred, West Barsham pedigree-skeleton paragraph. Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_5`. Source ID: `armstrong-norfolk-1781`.
```
`new_string`:
```
[^v71-armstrong-matthew-rose]: Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 5 (Norwich, 1781), Gallow Hundred, West Barsham pedigree-skeleton paragraph. Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_5`. Source ID: `armstrong-norfolk-1781`.

[^blomefield-harpley-1810]: Francis Blomefield, *An Essay Towards a Topographical History of the County of Norfolk*, vol. 8 (Freebridge Hundred and Half: "Harpley"), pp. 452–459, via British History Online (https://www.british-history.ac.uk/topographical-hist-norfolk/vol8/pp452-459); read 2026-06-14. Source ID: `blomefield-norfolk`.
```

**1c. Resolve Open Question #1** — `str_replace`:
`old_string`:
```
1. **Blomefield's Harpley:** The Harpley entry (vol. viii, pp. 452–459) should document the Burnham-to-Gurney descent through Rose. Priority extraction.
```
`new_string`:
```
1. **Blomefield's Harpley:** ~~The Harpley entry (vol. viii, pp. 452–459) should document the Burnham-to-Gurney descent through Rose. Priority extraction.~~ **Done 2026-06-14** — extracted (see Working Notes "Blomefield's Harpley — extracted"): confirms the Rose de Burnham / Hameline Warenne acquisition, the full medieval-Tudor descent to Anthony Gurnay (1511) → Sir John Allen (c. 1535), the rector's gravestone, and the engrailed-cross window arms.
```

**1d. Update Sources Consulted line** — `str_replace`:
`old_string`:
```
- Blomefield, *History of Norfolk* (Harpley entry, vol. viii, pp. 452–459). Not yet extracted. [Blomefield]
```
`new_string`:
```
- Blomefield, *History of Norfolk* (Harpley entry, vol. viii, pp. 452–459). Extracted 2026-06-14: Rose de Burnham/Hameline Warenne acquisition; full medieval–Tudor manorial descent to Anthony Gurnay (1511) → Sir John Allen (c. 1535); rector's gravestone of John de Gournay; engrailed-cross window arms; Edmund Gurnay B.D. presented rector 1620. Source ID: `blomefield-norfolk`. [Blomefield]
```

---

## Item 2 — PROMOTE: Gascon Rolls (C61) corroboration (L-82) → soldier-database topic

Adds the calendared C61 detail that anchors the 1394 Aquitaine man to Norfolk and records the Gascon theatre's Somerset dominance. Cite existing `sourceId: gascon-rolls-project`. No new validation.

**2a. New subsection** — `str_replace` in `research/topics/gurney-medieval-soldier-database.md`:

`old_string`:
```
The practical implication, against the project's standing puzzle that G22 Robert is almost documentarily invisible: the network around Robert — a Gaunt-retained father, an Arundel-steward father, a Lancastrian elder brother, a Holland-serving son — is dense and continuous. Thomas G21's military career is the family following an affinity path Edmund helped lay a generation earlier, not a one-off.
```

`new_string`:
```
The practical implication, against the project's standing puzzle that G22 Robert is almost documentarily invisible: the network around Robert — a Gaunt-retained father, an Arundel-steward father, a Lancastrian elder brother, a Holland-serving son — is dense and continuous. Thomas G21's military career is the family following an affinity path Edmund helped lay a generation earlier, not a one-off.

## Gascon Rolls (C61) — the 1394 Aquitaine attorney names the parson of Harpley

The Gascon Rolls Project calendar (gasconrolls.org) was swept for every Gournay/Gurney spelling. It confirms the soldier-database split from the rolls' own side: the Gascon (C61) theatre is occupied almost entirely by the **Somerset** Gournays — Thomas de Gournay the regicide (attorney/protection 1325; then the 1331–32 orders to transport the fugitive prisoner via Bayonne), a Thomas de Gournay knight serving as a Gascon captain and lieutenant of the seneschal at Monpazier (1342–51), and above all **Sir Matthew de Gournay**, seneschal of the Landes (protections, shipping licences, and diplomatic commissions to 1401; d. 1406). The one unambiguous **Norfolk** signal corroborates the repo's existing reading of Sir John Gurney V's 1394 service: the 1394 entry (C61/104) by which John Gournay, before going to Aquitaine, appointed as his English attorney **"John Dru, parson of the church of Harpley"** — i.e. names the incumbent of the family's own Norfolk manor-church, anchoring the 1394 man to the Harpley line rather than to the West Country. A second, weaker Norfolk lean is **Edmund Gurney** acting as attorney-in-England (1365–70) for knights in the Prince's and Cambridge's Gascon retinues, once alongside the parson of Ingoldisthorpe, Norfolk. (Gascon Rolls Project, C61/104 [1394] and C61/78, 82, 83 [1365–70]; Source ID: `gascon-rolls-project`. Full calendar capture in the 2026-06-14 web-leads discovery notes.)
```

---

## Item 3 — RECORD (finding-in-progress): NCC Consistory will-register gap swept; in-window Gurney sightings staged → g13 companion

The G13 origin campaign mapped and swept the previously-unmapped NCC registered-copy will registers for 1624–1637 (vols 119–130) and re-checked 1638–1651. This characterises the Consistory series for Gurneys across the emigrant's father's window and surfaces three in-window sightings, all machine-transcript only with image reads staged for the paleographer (packets 14 and 16 in `sources/intake/paleography-staging/`). Recorded as a finding-in-progress; not promoted as confirmed fact. Cite existing `sourceId: familysearch-fulltext-search`.

**3a. New dated Working-Notes entry** — `str_replace` in `research/people/g13-john-gurney-fact-sheet.research.md`:

`old_string`:
```
### Colonial document follow-ups (2026-06-12/13) — Billerica re-grant, the Massachusetts "bill" and petition, Bury St Edmunds cleared
```

`new_string`:
```
### 2026-06-14 — NCC Consistory will-register gap (1624–1651) characterised; in-window Gurney sightings staged for paleography
The Norwich Consistory Court registered-copy will registers for **1624–1637** (vols 119–130) — not previously mapped to FamilySearch image-group numbers — were resolved from the catalogue (record `koha:278818`) and swept for Gurn*/Gourn*/Gorn*, and the 1638–1651 volumes re-checked. Across the whole window the Consistory series carries **no Gurney testator of its own** beyond the already-known John Gurney of Earsham (will 1638, vol. 131–132 = DGS 008076858) — a useful bounding result: a humble Gurney testator in the emigrant's father's window is not in the Consistory registers, which redirects the search to the **Archdeaconry of Norwich** court (the lesser-estate jurisdiction; see leads). Three in-window Gurney *sightings* surfaced, each named inside another person's will and each a machine-transcript read with the full-resolution image staged for expert transcription:
- **Clement Gurney, Gent** — a testator's will (NCC regd. wills 1631–32, vol. 124–125, DGS 008076514, [ark 3:1:3Q9M-CSN8-YRB3](https://www.familysearch.org/ark:/61903/3:1:3Q9M-CSN8-YRB3)) bequeaths a bond "bearing date the one and twentieth day of November Anno Dm 1622 … wherein [Clement] Gurne[y] Gent [was bound] … in the penal sum of forty pounds." A *gentleman* Gurney active c. 1622–31; the forename Clement is rare and recurs nowhere else in FamilySearch full-text before the 19th century, so this register page is its sole witness — image staged as paleography packet 16a for confirmation of the forename, the testator's identity, and any residence.
- **John Gurney's house, Langley** — a 1634 will (NCC regd. wills vol. 127, DGS 008076861, [ark 3:1:3Q9M-CSND-T9KS-K](https://www.familysearch.org/ark:/61903/3:1:3Q9M-CSND-T9KS-K)) devising meadow "lying in Langley … next unto John Gurney's house," to the testator's son Robert Pagan after the death of Marion his wife. A John Gurney householder at/near Langley (south Norfolk, by Loddon) in 1634 — image staged as packet 16b.
- **Ellingham poor-charity, 1630** — an original will of 1630 (DGS 008076513, [ark 3:1:3Q9M-CSN8-YF6X](https://www.familysearch.org/ark:/61903/3:1:3Q9M-CSN8-YF6X)) endowing the poor of Ellingham (the core Gurney locus); the Gurney surname token is low-confidence (likely OCR salad) — image staged as packet 16c for a read.

Separately, the **1608 Norwich Consistory depositions** (DGS 004389252) carry several Gurney deponents whose depositions should state age, residence, and occupation — including a "Robertus Gurney," a Gurney styled "of London, yeoman" (1605), and a Gurney with a Suffolk tag — staged as paleography packet 14. Method note: the FamilySearch full-text JSON API caps a single request at ~100 results (count=300 returns empty); the 1624–37 register DGS map is recorded in the FamilySearch FTS skill.[^v98-ncc-window-fts]

### Colonial document follow-ups (2026-06-12/13) — Billerica re-grant, the Massachusetts "bill" and petition, Bury St Edmunds cleared
```

**3b. Footnote definition** — append after the existing `[^...]` footnote block. To anchor without depending on the (large) footnote section, append at the very end of the Working-Notes-3a `new_string` is avoided; instead add the footnote via `str_replace` on the Sources Consulted header. `old_string`:
```
## Sources Consulted
```
`new_string`:
```
[^v98-ncc-window-fts]: FamilySearch Full-Text Search, Norwich Consistory Court registered-copy will registers, films/DGS resolved from catalogue record `koha:278818`: 1624–25 (vol. 119–120) = 008470970; 1626 (vol. 121) = 008219670; 1627–28 (vol. 122–123) = 008076511; 1629/1630 original wills = 008076512 / 008076513; 1631–32 (vol. 124–125) = 008076514; 1633 (vol. 126) = 008472222; 1634 (vol. 127) = 008076861; 1635 (vol. 128) = 008472223; 1636 (vol. 129) = 008076860; 1637 (vol. 130) = 008076859. Machine-transcript reads, 2026-06-14; full-resolution images staged in `sources/intake/paleography-staging/` (packets 14, 16). Source ID: `familysearch-fulltext-search`.

## Sources Consulted
```

---

## Item 4 — SKILL UPDATE: FamilySearch FTS skill — result-count cap + NCC register DGS map

Two durable methodological lessons from this thread. `str_replace` ×2 in `.claude/skills/familysearch-fulltext-research/SKILL.md`.

**4a. Result-count cap** — `old_string`:
```
`count` and `offset` paginate. Same `q.text` operators/`q.groupName` scoping as the URL form.
```
`new_string`:
```
`count` and `offset` paginate. Same `q.text` operators/`q.groupName` scoping as the URL form. **Cap: a single request returns at most ~100 entries — `count=300` returns an empty `entries` array (and no `results` field). Page with `offset` in steps of 100 rather than requesting a larger `count`.** (Also: build `q.text` with `encodeURIComponent` on the *raw* query — do not pre-encode `+` to `%2B` and then `encodeURIComponent` it again, or the AND-operator double-encodes and the probe returns zero.)
```

**4b. NCC register DGS map** — `old_string`:
```
Used to map the whole NCC registered-copy-wills year series in one pass (record `koha:278818`).
```
`new_string`:
```
Used to map the whole NCC registered-copy-wills year series in one pass (record `koha:278818`). The vol→DGS mapping is offset-ambiguous in the flattened table text; anchor on a confirmed pair (vol. 116–118 / 1621–1623 = DGS 008470484) to fix the offset. The 1624–1637 gap (vols 119–130), resolved 2026-06-14: 1624–25=008470970, 1626=008219670, 1627–28=008076511, 1629=008076512, 1630=008076513, 1631–32=008076514, 1633=008472222, 1634=008076861, 1635=008472223, 1636=008076860, 1637=008076859 (1638–39=008076858; 1643–46=008402405; 1647–51=007904832).
```

---

## Item 5 — Leads catalogue maintenance

**5a. Close L-118 — remove the open row** (`str_replace` in `research/future-research/research-leads.csv`):
`old_string`:
```
great-ellingham.md
L-118,60,G13/Related,"Walter Rye, 'The Gurneys of Norwich' essay","Walter Rye, 'The Gurneys of Norwich,' in The Norfolk Antiquarian Miscellany, pp. 68-96 (also FamilySearch DGS 004389182, a Rye antiquarian volume = deeds calendar + essays + indexes)","A 28-page printed treatment of the Norwich Gurneys by the leading Norfolk antiquary. Read to map the Norwich Gurney families and test any medieval/Tudor tie to the West Barsham line — separating the later Quaker banking Gurneys (a large, distinct Norwich population). DGS 004389182 is itself a clean-OCR Rye volume worth a fuller Gurney sweep.",Y,"Open — Available online (Internet Archive: Norfolk Antiquarian Miscellany)",sources/intake/new/2026-06-13-familysearch-browser-link-triage/extended-fts-discovery-campaign.md
```
`new_string`:
```
great-ellingham.md
```

**5b. Archive L-118 disposition** (`str_replace` in `research/future-research/research-leads-done.csv`):
`old_string`:
```
L-112,Anthony G17's 1557 will — death-date and pedigree reconciliation,Resolved: Anthony G17 will reconciliation promoted in v92.,2026-06-13,research/people/g17-anthony-gurney-fact-sheet.research.md
```
`new_string`:
```
L-112,Anthony G17's 1557 will — death-date and pedigree reconciliation,Resolved: Anthony G17 will reconciliation promoted in v92.,2026-06-13,research/people/g17-anthony-gurney-fact-sheet.research.md
L-118,"Walter Rye, 'The Gurneys of Norwich' essay","Duplicative: the essay is already held in full — sourceId rye-norfolk-antiquarian, OCR extract sources/corpus/norfolk-antiquarian-gurneys-of-norwich.md, cited in the G14 companion + francis-gurney-of-maldon.md + case file. The DGS 004389182 deeds-calendar sweep remains separately as L-119.",2026-06-14,sources/corpus/norfolk-antiquarian-gurneys-of-norwich.md
```

**5c. Update L-46 → Done** (`str_replace`):
`old_string`:
```
L-46,35,G29,"Matthew de Gournay","Blomefield, Harpley entry; BL Harleian MS 970","Harpley marriage-acquisition narrative corroboration; Blomefield is online (British History Online).",Unk,Open,research/people/g29-matthew-de-gournay-fact-sheet.research.md
```
`new_string`:
```
L-46,35,G29,"Matthew de Gournay","Blomefield, Harpley entry; BL Harleian MS 970","Harpley marriage-acquisition narrative corroboration; Blomefield is online (British History Online).",Y,"Blomefield part DONE 2026-06-14 (v98) — Harpley vol.8 pp.452-459 read & promoted to the g29 companion: Rose de Burnham/Hameline Warenne acquisition, full medieval-Tudor descent to Anthony Gurnay 1511 > Sir John Allen c.1535, rector-gravestone, engrailed-cross window arms, Edmund Divine rector 1620. Only BL Harleian MS 970 (Hardingham tithe grant, un-digitised) remains open.",research/people/g29-matthew-de-gournay-fact-sheet.research.md
```

**5d. Update L-82 → Done** (`str_replace`):
`old_string`:
```
the Somerset Gascon-theatre Gournays from the Norfolk northern-theatre men. Online.",Y,Open,research/topics/gurney-medieval-soldier-database.md
```
`new_string`:
```
the Somerset Gascon-theatre Gournays from the Norfolk northern-theatre men. Online.",Y,"Done 2026-06-14 (v98) — gasconrolls.org calendared & promoted to the soldier-database topic: Gascon theatre is overwhelmingly Somerset (Thomas the regicide; Sir Matthew de Gournay, seneschal of the Landes, d.1406); sole clear Norfolk signal is the 1394 C61/104 entry where John Gournay names John Dru, parson of Harpley, as his English attorney before Aquitaine (corroborates Sir John V); Edmund Gurney 1365-70 attorney-in-England (ambiguous Norfolk lean).",research/topics/gurney-medieval-soldier-database.md
```

**5e. Update L-71 → lowered priority, lead-only** (`str_replace`):
`old_string`:
```
L-71,55,G13/G14,"Gurney/de Gournay pedigree (Burke 1858)","Burke, Dictionary of the Landed Gentry (1858) — Gurney pedigree incl. 'of Maldon, Essex' and de Gournay descent (Runhall, Hardingham, Hingham, Swathing)","Tertiary collector surfaced via FS Full-Text; trace the Maldon/Norfolk line to primary authority before citing for any fact.",Y,Open,research/people/francis-gurney-of-maldon.md
```
`new_string`:
```
L-71,30,G13/G14,"Gurney/de Gournay pedigree (Burke 1858)","Burke, Dictionary of the Landed Gentry (1858) — Gurney pedigree incl. 'of Maldon, Essex' and de Gournay descent (Runhall, Hardingham, Hingham, Swathing)","Tertiary collector; Maldon is a collateral (Rye-disputed) branch — low priority per the Collateral-line discount. Transcribed 2026-06-14 (1862 4th ed., closest digitised, archive.org bub_gb_BSkAAAAAQAAJ pp.616-17): Francis b.18 Sep 1581 W.Barsham (6th son of Henry G15 & Ellen Blennerhassett), Merchant Taylors' Co. 1606, St Benet Fink, m Ann Browning of Norwich/Maldon > Francis of Maldon b.1623 > John the Quaker b.1655; NO primary authority cited for the 16-17c links. Not promoted; trace to Visitations of London 1633 / Essex 1664 before any fact-sheet use.",Y,Open,research/people/francis-gurney-of-maldon.md
```

**5f. Progress notes on worked leads** — `str_replace` ×2:

L-106 (Earsham — packet 17 staged):
`old_string`:
```
,Lyon-trace strand continues under L-109/L-110",research/people/john-gurney-earsham-will-1638.md
```
`new_string`:
```
,Lyon-trace strand continues under L-109/L-110. 2026-06-14 (v98): the will-body register pages (DGS 008076858, arks 3:1:3Q9M-CSN6-3WWW [opening] & -3W7R [bequests]) pulled at full resolution and staged as paleography packet 17 for a definitive transcription (the family structure — son John a minor, brother Lyon, contingent remainder — is already on the companion; the 'sister / nephew William' clause in -3W7R may be page-boundary bleed from an adjacent will and needs the paleographer to attribute).",research/people/john-gurney-earsham-will-1638.md
```

L-93 (Costessey — packet 13 staged):
`old_string`:
```
the 1659 court's manor (held for Anthony Dobbs of Marsham, esq.)",research/people/gurney-family-costessey-manorial.md
```
`new_string`:
```
the 1659 court's manor (held for Anthony Dobbs of Marsham, esq.). 2026-06-14 (v98): an undated copyhold grant 'John Gurne & Margaret [his] wife' (DGS 004389191, ark 3:1:3Q9M-... -6PNV-DD), a 1625 copyhold (-6PN2-L1), and a surrender of Thomas Rippon to John Gurne (-6PN9-9SP) staged as paleography packet 13 for image reads (the 'Margaret wife' page may name the Costessey John's wife).",research/people/gurney-family-costessey-manorial.md
```

**5g. Append new leads** (`str_replace` on the last CSV row):
`old_string`:
```
L-123,40,Collateral,"Bradfer-Lawrence will-extracts — moderate Gurney mentions","Norfolk wills extracts 1370-1763 (Bradfer-Lawrence; FamilySearch DGS 008176838, 008480296, 008480297)","Moderate one-line Gurney mentions from the will-extracts sweep to trace for kinship/line-relevance: 'sister Joan Gurney' (1606); 'brother John Gurney(s) of Kenton, Suffolk' executor (1514-17); 'Elizabeth Gournay' among a testator's sisters (1654); 'nephew Gourney Crowe' of East Bilney (1683, onomastic).",Y,"Promoted in draft patchset v96 2026-06-13 (logged as collateral sightings on great-ellingham.md); trace each for kinship",research/places/great-ellingham.md
```
`new_string`:
```
L-123,40,Collateral,"Bradfer-Lawrence will-extracts — moderate Gurney mentions","Norfolk wills extracts 1370-1763 (Bradfer-Lawrence; FamilySearch DGS 008176838, 008480296, 008480297)","Moderate one-line Gurney mentions from the will-extracts sweep to trace for kinship/line-relevance: 'sister Joan Gurney' (1606); 'brother John Gurney(s) of Kenton, Suffolk' executor (1514-17); 'Elizabeth Gournay' among a testator's sisters (1654); 'nephew Gourney Crowe' of East Bilney (1683, onomastic).",Y,"Promoted in draft patchset v96 2026-06-13 (logged as collateral sightings on great-ellingham.md); trace each for kinship",research/places/great-ellingham.md
L-124,72,Related,"Archdeaconry of Norwich wills — Gurney testator sweep 1600-1645","FamilySearch catalogue + FTS: Archdeaconry of Norwich (ANW) registered/original wills, the lesser-estate court distinct from the NCC Consistory","The NCC Consistory registered-copy wills are now characterised for Gurneys across 1624-1651 (v98) and carry no Gurney testator beyond the Earsham John 1638; a humble Gurney testator (the laceweaver/yeoman father-candidate for the emigrant John G13) would prove in the Archdeaconry court. Resolve the ANW catalogue's FTS coverage and year-films, then sweep 1600-1645 for a Gurney testator's own will. Highest-value redirect for the G13 origin question.",Unk,Open,research/people/g13-john-gurney-fact-sheet.research.md
L-125,60,Related,"Clement Gurney, Gent (NCC 1631-32)","NCC registered-copy wills 1631-32, vol.124-125, DGS 008076514, ark 3:1:3Q9M-CSN8-YRB3 (image staged paleography packet 16a)","A gentleman Gurney bound in a £40 bond dated 21 Nov 1622, recited in another's 1631-32 NCC will; the rare forename Clement recurs nowhere else in FamilySearch full-text pre-19thc. Read the staged image to confirm the forename/style, identify the testator (read the will opening), and recover any residence; then place Clement among the West Barsham / Great Ellingham Gurneys.",Y,Open,research/people/g13-john-gurney-fact-sheet.research.md
L-126,55,Related,"John Gurney of Langley (1634)","NCC registered-copy wills vol.127 (1634), DGS 008076861, ark 3:1:3Q9M-CSND-T9KS-K (image staged paleography packet 16b)","A John Gurney householder at/near Langley (south Norfolk, by Loddon — cf. the 1373 John Gurney chaplain of Loddon, L-116) named as an abuttal in the Pagan will of 1634. Read the staged image to confirm the location and recover any further Gurney detail; test for kinship to the emigrant-window Norfolk Johns.",Y,Open,research/people/g13-john-gurney-fact-sheet.research.md
L-127,50,Related,"Norwich Consistory depositions 1608 — Gurney deponents","FamilySearch DGS 004389252 (Norwich depositions 1605-15), arks incl. 3:1:S3HY-696W-N42 / -G3L / -B8N / -GL6 / -XLR (images staged paleography packet 14)","Deposition books state each deponent's age, residence, and occupation. Several real Gurney deponents surfaced 1605-15: 'Robertus Gurney' with an age fragment, a Gurney styled 'of London, yeoman' (1605), a Gurney with a Suffolk tag, and a Gurney testator linked to 'Adams' (1614/15). Read the staged images for ages/origins bearing on the emigrant-John generation.",Y,Open,research/people/g13-john-gurney-fact-sheet.research.md
```

---

## Source tracking

- **`blomefield-norfolk`** (existing) — used for Item 1 (Harpley, vol. 8, pp. 452–459). Existing validation `sources/validations/blomefield-norfolk*` covers it; no new validation. The Harpley extract is < 150 words of quoted matter woven into the companion entry, so no separate `corpus_supplement` file is required.
- **`gascon-rolls-project`** (existing, with validation) — used for Item 2. No new validation.
- **`familysearch-fulltext-search`** (existing) — used for Item 3 (machine-transcript sightings; images staged, not yet promoted as fact). No new validation; the per-film/ark detail lives in the companion footnote and the paleography-staging README.
- **No new `sourceId`s minted.** The packet 13–17 transcript contents will mint sourceIds (per-record) and validations when the paleographer's transcriptions are promoted in a later patchset.

## Leads summary
- Closed: **L-118** (duplicative → done CSV).
- Updated: **L-46** (Done — Blomefield part), **L-82** (Done), **L-71** (priority 55→30, lead-only), **L-106** (packet 17 staged), **L-93** (packet 13 staged).
- New: **L-124** (Archdeaconry of Norwich Gurney-testator sweep, the redirect), **L-125** (Clement Gurney Gent), **L-126** (John Gurney of Langley 1634), **L-127** (1608 depositions).
- Standing (already on the staging README, not re-listed here): Dereham pre-1636 male image-walk (L-98) and the NCC 1638-42 / original-wills finer pass.

## Out of scope (future patchsets)
- Promotion of packet 13–17 transcript content awaits the paleographer's reports.
- Disposition of completed packets 10–12 (move reports to `sources/corpus_supplement/`, master images to `sources/media/<set>/_local/`) is a separate cleanup task, not part of this Phase-1 patchset.
