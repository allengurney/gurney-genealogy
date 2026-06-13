**Done:** 2026-06-13 15:55 PT

# Patchset v91 — archive.org finds triage and research-leads ledger cleanup

**Prepared:** 2026-06-12

**Session source:** `sources/intake/new/12June2026-archive-org-finds.md`

**Scope:** Phase 1 discovery only. The archive.org leads were tested against existing source coverage and by a broad OCR-tolerant search sweep. No new corpus supplement is proposed: the meritorious facts are already present in stronger or already-registered sources. The only Phase 2 action proposed here is cleanup of stale lead-ledger rows.

**Search method note:** The sweep used more than exact `Gourney`: surname fragments (`gou*`, `gorn*`, `gurn*`, `geneu*`, `garn*`), expected OCR/name variants (`Gurney`, `Gourney`, `Gournay`, `Gorneye`, `Gornay`, `Gourneie`, `Gournie`, `Geneuay`/`Genevay`), first-name/context searches (`Hugh`, `Hue`, `Matthew`, `Maheu`, `Thomas`, `Robert`, `John`, `Despenser`, `Maltravers`, `Berkeley`, `Stoke`, `Hamden`, `Landes`, `Dax`, `Redwick`, `Gaunt`, `Mountfort`), and Norfolk place/topic sweeps around Beatniffe. Archive page OCR/XML and the Project Gutenberg/IA Holinshed splits were checked because the printed OCR is noisy.

---

## Lead Disposition

| Lead | Outcome | Reason |
|---|---|---|
| Richard Beatniffe, *The Norfolk Tour* (1786) | reject | The meaningful Gourney hit is the Norwich Cathedral cloister-window arms notice. The same fact is already better covered by the registered Armstrong 1781 extract/source (`armstrong-norfolk-1781`). The broader Norfolk-place sweep did find some repo-place mentions, but they are low-level gazetteer/distance/table or generic county-context material rather than new Gurney evidence or a stronger place-source basis. |
| *A Collection of Curious Discourses* (1773), vol. 1 | reject | The Sir Matthew / Maheu de Gurnay epitaph text is duplicate of the stronger Leland/Tyrwhitt route already captured under `tyrwhitt-canterbury-tales-1798-v2`. The added "Sir H. Newton is descended" aside is derivative and too thin for promotion. |
| Francis Sandford, *A Genealogical History* (1677) | reject | The p.148 "Hugh le Despenser" item is not a Gournay/Gurney Hugh. The p.12 Gundred/Gerald de Gurney passage is derivative and confused against the current G32 source-critical treatment. The Thomas Gourney/Maltravers material is already captured through better regicide/chronicle coverage. |
| Samuel Rudder, *A New History of Gloucestershire* (1779) | reject as new source | Already registered and promoted as `rudder-gloucestershire-1779`, with corpus, validation, and Somerset collateral research coverage. The Redwick/Gaunt's Urcot item is already landed. |
| Holinshed 1577/1586/1587 and Gutenberg/IA split texts | reject as new source | Existing `holinshed-chronicles-1577` coverage already captures the Gurney loci. The broader split-text sweep confirmed cleaner spellings such as `Genevay`, `Gourneie`, and `Gournie`, but no new event beyond the selected Holinshed supplement. |

**No new source IDs.** Existing relevant IDs are `armstrong-norfolk-1781`, `tyrwhitt-canterbury-tales-1798-v2`, `rudder-gloucestershire-1779`, `holinshed-chronicles-1577`, and existing BHO/IPM source IDs.

**Beatniffe place-sweep note.** Beatniffe is not empty for Norfolk geography: OCR hits against the repo's Norfolk place spine include Attleborough, Burnham Thorpe, East Dereham/Dereham, Flegg, Hardingham, Harpley, Hingham, King's Lynn/Lynn, Runhall, and Saxthorpe. The substantive snippets found in this pass are generic (for example East Dereham as a neat market town, Flegg as a rich peninsula/soil district, Hingham as a small mere, Saxthorpe on the Bure route) or table/index entries. They do not add a Gurney-specific fact, improve an existing Gurney-place citation, or justify source registration from this intake batch.

**No corpus supplement.** None of these archive.org leads adds a new, source-worthy extract not already represented by stronger or existing corpus material.

---

## Item 01 (promote) — research-leads.csv ledger cleanup

**Target:** `research/future-research/research-leads.csv`

These rows are stale because later work has already landed the source material or narrowed the remaining task. Apply the replacements exactly.

### Operation 01a — L-59 Ormerod / East Harptree

Replace:

```csv
L-59,40,Collateral,"Somerset Gournays (regicide line)","Ormerod, Strigulensia (1861) p.103 — 1329 demise to 'Thomas son of Hugh de Gournay' (Close Roll, Rot. Claus. 3 Edw. III)","East Harptree life-tenure naming a Hugh as father; could correct the standard Pettigrew descent of the regicide. Ormerod on HathiTrust.",Y,Open,research/places/somerset-gournay-collateral.md
```

with:

```csv
L-59,40,Collateral,"Somerset Gournays (regicide line)","Ormerod, Strigulensia (1861) p.103 — 1329 demise to 'Thomas son of Hugh de Gournay' (Close Roll, Rot. Claus. 3 Edw. III)","East Harptree life-tenure naming a Hugh as father; Ormerod extract/source landed in the Somerset collateral file, but the underlying Close Roll/Chancery enrolment remains the tie-breaker for whether this corrects the standard Pettigrew descent of the regicide.",Part,"Partial 2026-06-12 — Ormerod extract landed; primary Close Roll/Chancery check still open",research/places/somerset-gournay-collateral.md
```

### Operation 01b — L-60 Gaunt's Hospital / Bilswick founder conflict

Replace:

```csv
L-60,30,Collateral,"Somerset/Bristol Gournays","Gaunt's Hospital (Bilswick, Bristol) foundation charter — Richard vs Robert de Gournay founder conflict","Rudder 1779 names Richard; Pettigrew 1871 names Robert II. The Berkeley/Bristol cartulary charter is the tie-breaker.",Unk,Open,research/places/somerset-gournay-collateral.md
```

with:

```csv
L-60,30,Collateral,"Somerset/Bristol Gournays","Gaunt's Hospital (Bilswick, Bristol) foundation charter — Richard vs Robert de Gournay founder conflict","Rudder 1779 names Richard; Pettigrew 1871 names Robert II. Both printed witnesses are now captured; the Berkeley/Bristol cartulary or foundation charter remains the tie-breaker.",Part,"Partial 2026-06-12 — Rudder/Pettigrew conflict landed; primary charter/cartulary check still open",research/places/somerset-gournay-collateral.md
```

### Operation 01c — L-61 BHO IPM vol. 16 index

Replace:

```csv
L-61,25,Collateral,"Somerset Gournays","Calendar of Inquisitions Post Mortem vol. 16 — index for Matthew/Philippa/Roger/Thomas de Gournay","Finding aid for later Somerset/Harpetre Gournay follow-up; published (British History Online).",Y,Open,research/topics/anderson-yvery-harpetre-gournay-collateral.md
```

with:

```csv
L-61,25,Collateral,"Somerset Gournays","Calendar of Inquisitions Post Mortem vol. 16 — index for Matthew/Philippa/Roger/Thomas de Gournay","Finding-aid value landed: IPM vol. 16 index confirms Matthew/Philippa/Roger/Thomas de Gournay entries and no Edmund Gournay; use only as an index unless a specific entry is being pulled.",Y,"Done 2026-06-12 — index/source note landed; future pulls should target individual IPM entries",research/topics/anderson-yvery-harpetre-gournay-collateral.md
```

### Operation 01d — L-80 Sir Matthew soldier database / Trevet kinship

Replace:

```csv
L-80,38,Collateral,"Sir Matthew de Gournay — soldier-database service + Trevet kinship","Soldier in Later Medieval England database + TNA C61/C76/E101 rows; Green, 'Household and Military Retinue of the Black Prince' (Nottingham PhD 1998) ii.183 for Trevet","Add Matthew's dated muster/protection rows (Despenser's retinue 1373 E101/32/26; banneret commanding the Calais garrison 1386 E101/40/26+E101/42/14; 1381 Iberian expedition retinue of ~20) and the Sir Thomas Trevet = nephew of Sir Matthew kinship to the Somerset collateral file.",Y,Open,research/places/somerset-gournay-collateral.md
```

with:

```csv
L-80,38,Collateral,"Sir Matthew de Gournay — soldier-database service + Trevet kinship","Soldier in Later Medieval England database + TNA C61/C76/E101 rows; Green, 'Household and Military Retinue of the Black Prince' (Nottingham PhD 1998) ii.183 for Trevet","Matthew's dated service rows and the Sir Thomas Trevet = nephew of Sir Matthew kinship are now in the Somerset collateral file; future work can move to individual primary rolls only if a narrower question requires images.",Y,"Done 2026-06-12 — service rows and Trevet kinship landed in Somerset collateral file",research/places/somerset-gournay-collateral.md
```

---

## Phase 2 Notes

- Do not add Beatniffe, Curious Discourses, or Sandford as source IDs from this intake batch.
- Do not add a new Holinshed source for the Gutenberg/IA split texts; they were useful for search confirmation only.
- If Phase 2 touches only `research-leads.csv`, no `data/sources.json` or ID-index regeneration is required.
- Preserve unrelated local edits already present in `research/future-research/research-leads.csv`; the replacements above target rows L-59, L-60, L-61, and L-80 only.
