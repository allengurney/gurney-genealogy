**Done:** 2026-05-28 19:17 PT

# v72 patchset — Armstrong 1781 findings absorbed into topic files + new research leads + stub housekeeping

Prepared: 2026-05-28  
Phase: 1 preparation  
Scope: embed Armstrong 1781 findings (per v69) into the affected topic files (senior-collateral; anderson-yvery; Saint-Hildevert chapter), capture the three new research leads as proper companion notes, and complete the intake-folder stub housekeeping.

Companion to v69 (source-tracking + corpus supplement), v70 (fact-sheet absorption), and v71 (research companions + place files).

## Dependency on v69 + v71

This patchset assumes `armstrong-norfolk-1781` is in `data/sources.json` (v69) and that the Saint-Hildevert-at-Hardingham extension has already been recorded in `research/places/hardingham.md` (v71). Phase 2 application of v69 and v71 must run first; v70 and v72 are independent of each other.

## Findings absorbed in v72

| Target | Content |
|---|---|
| `research/topics/senior-gournay-baron-line-collateral.md` | Bastwick Henry I grant on Baynard rebellion (c. 1110–1115, G33 Hugh III); Kimberley parallel-to-Bedingham Stuteville/Gunnora marriage; Langley Priory burial of "Sir Hugh Gourney" (collateral knight); Cantley Uphall 1229 grant to Roger Botetourt. |
| `research/topics/anderson-yvery-harpetre-gournay-collateral.md` | Armstrong as an additional eighteenth-century printed witness to the Cantley / Bedingham / Kimberley senior-collateral cluster. |
| `research/places/collegiale-saint-hildevert-gournay.md` | The Hardingham-church tithe-gift extends the existing Caister + Cantley pattern; cross-reference. |
| New research-lead file `research/people/wentworth-impalement-west-barsham-church.md` | The "probable Wentworth" eighth shield at West Barsham church — open lead, no known Gurney-Wentworth marriage. |
| New research-lead file `research/people/herward-gourney-impalement-south-erpingham.md` | Herward impaling Gourney arms in a South Erpingham parish church (Armstrong vol. 3) — open lead. |
| New research-lead note `research/people/sir-hugh-gourney-langley-priory-burial.md` | Sir Hugh Gourney buried at Langley Priory (late 13th / early 14th c., per Armstrong vol. 7) — collateral knight, identity TBD. |
| `sources/intake/processed/` | Remove stale `stub-v67.md`; create `stub-v73.md`. |

## Phase 2 operations

### 1. Senior-collateral topic file — Armstrong additions

File: `research/topics/senior-gournay-baron-line-collateral.md`.

```str_replace
old_string: [^dcclii-sigy]: Delisle and Berger, *Recueil des actes de Henri II*, vol. 2 (Paris, 1920), act DCCLII at pp. 396–397. Charter dated 1185–1189 at Argentan; subscription of Walter of Coutances as archbishop of Rouen narrows to post-early-1185. Source ID: `recueil-actes-henri-ii-delisle-berger-vol-2`.
new_string: [^dcclii-sigy]: Delisle and Berger, *Recueil des actes de Henri II*, vol. 2 (Paris, 1920), act DCCLII at pp. 396–397. Charter dated 1185–1189 at Argentan; subscription of Walter of Coutances as archbishop of Rouen narrows to post-early-1185. Source ID: `recueil-actes-henri-ii-delisle-berger-vol-2`.

## Armstrong 1781 — additional senior-collateral attestations

Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk* (1781), supplies four additional eighteenth-century attestations to the senior-collateral cluster already covered in this topic file.

**Bastwick (Tunstead Hundred) — Henry I grant on Baynard rebellion (c. 1110–1115; G33 Hugh III).** Armstrong vol. 7: the Bastwick manor "was granted to Hugh de Gourney by Henry I. on the rebellion of lord Baynard, and by Julian, daughter and heiress of that family, came to William lord Bardolph; her husband." William Baynard's English honour was forfeited 1110; the Henry I grant to Hugh de Gourney is therefore datable c. 1110–1115. The recipient is most parsimoniously **G33 Hugh III**, who was raised at Henry I's court during minority per Orderic + the existing G33 companion. The eventual transmission to William Bardolph via Julian de Gournay matches the broader Bardolph-as-Gournay-heir pattern.[^v72-armstrong-bastwick-henry-i-1110]

**Kimberley parallel to Bedingham — Stuteville / Gunnora marriage (Forehoe Hundred).** Armstrong vol. 4: the Kimberley lordship at the beginning of king John's reign was held by "Hugh de Gurnaco, or Gournay, a Norman, was possessed of it, and gave it to Nicholas de Stutevile with Gunnora, his daughter, in marriage; he was disseized of it at the time of the disseizing all the Normans from their lands, for their rebellion, which was in 1205, in the 7th of king John, who the next year directed his writ to the sheriff, to restore Nicholas de Stutevile to all his lands that Nicholas, his father, was disseized of." The 1206 restoration writ to the Stuteville son, the 1284 attestation that the Stuteville heir "held this town of the barony of Gournay," and the 1345 attestation that the Bardolph honour was "more rightly of Gournay" — independent senior-line attestations carried forward to the Edward III period via the Bardolph descent.

The Kimberley parallel extends the Stuteville/Gunnora marriage already documented for Bedingham (Blomefield, Cantley/Bedingham; G33 companion) to a second Norfolk parish. The marriage carried two Norfolk manors at once.[^v72-armstrong-kimberley-stuteville-gunnora]

**Cantley Uphall — Hugh de Gournay → Roger Botetourt 1229 (Loddon Hundred).** Armstrong vol. 1: "Uphall Manor took its rise from the grant of Hugh de Gournay, (capital lord of the town) to Roger Botetourt; which he held of Hugh in the 13th of Henry III. anno 1229." A second "Uphall" in the senior-line distribution pattern (the first being Harpley's Uphall transferred to Sir John de Gourney rector in 1325 — see `research/places/harpley.md`). The Cantley Uphall sub-infeudation predates the Harpley Uphall by approximately a century and reflects the senior-line continuing to fragment its Norfolk holdings through the mid-13th century. The grantor "Hugh de Gournay" at Cantley in 1229 (13 Henry III) is most parsimoniously a collateral or junior figure surviving from the 1205 forfeiture's aftermath.[^v72-armstrong-cantley-uphall-1229]

**Langley Priory burial — "Sir Hugh Gourney" (collateral knight).** Armstrong vol. 7: among the burials in the church of Langley Priory are "Sir Robert Thurkelby, Sir Thomas Roscelyn, Sir Peter Roscelyn, **Sir Hugh Gourney**, Sir Jeffrey Say, Sir Henry [Wodehouse?], Sir Fulk Kerdeston, Sir William Kerdeston, and Margaret, his wife, who died in 1328..."

A "Sir Hugh Gourney" buried at Langley Priory (Norfolk) in the late 13th / early 14th century is not currently identified in the project's senior or junior direct lines. Possibilities: (a) a younger son of one of the senior Hugues (IV or V); (b) a collateral figure of the la-Ferté line; (c) a knight of one of the Gurney junior-Norfolk subbranches who took the elder family name in religious-burial context. The Roscelyn / Say / Kerdeston co-burials place the burial in the Norfolk-knightly social network of the period. Carried forward as a research lead in `research/people/sir-hugh-gourney-langley-priory-burial.md`.[^v72-armstrong-langley-sir-hugh]

[^v72-armstrong-bastwick-henry-i-1110]: Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 7 (Norwich, 1781), Tunstead Hundred — Bastwick / D'Aggs entry. Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_7`. Source ID: `armstrong-norfolk-1781`.

[^v72-armstrong-kimberley-stuteville-gunnora]: Armstrong, *Norfolk*, vol. 4 (Norwich, 1781), Forehoe Hundred — Kimberley parish entry. Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_4`. Source ID: `armstrong-norfolk-1781`.

[^v72-armstrong-cantley-uphall-1229]: Armstrong, *Norfolk*, vol. 1 (Norwich, 1781), Loddon Hundred — Cantley parish entry, Uphall Manor section. Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_1`. Source ID: `armstrong-norfolk-1781`.

[^v72-armstrong-langley-sir-hugh]: Armstrong, *Norfolk*, vol. 7 (Norwich, 1781), Tunstead / Walsham area — Langley Priory burial list. Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_7`. Source ID: `armstrong-norfolk-1781`.
```

### 2. Anderson-Yvery topic file — Armstrong as additional Cantley/Bedingham printed witness

File: `research/topics/anderson-yvery-harpetre-gournay-collateral.md`.

```str_replace
old_string: ## Sources

- Vol. I extract: `sources/corpus/anderson-yvery-1742-vol-i-extract.md` (sourceId `anderson-yvery-1742-vol-i`).
- Vol. II extract: `sources/corpus/agenealogical-history-gournay-extract.md` (sourceId `anderson-yvery-1742`).
- Daniel Gurney 1848: junior Norfolk branch in DG-II; Somerset Gournays in DG-IV (sourceIds `dg-rec-pt2`, `dg-rec-pt4`).
new_string: ## Sources

- Vol. I extract: `sources/corpus/anderson-yvery-1742-vol-i-extract.md` (sourceId `anderson-yvery-1742-vol-i`).
- Vol. II extract: `sources/corpus/agenealogical-history-gournay-extract.md` (sourceId `anderson-yvery-1742`).
- Daniel Gurney 1848: junior Norfolk branch in DG-II; Somerset Gournays in DG-IV (sourceIds `dg-rec-pt2`, `dg-rec-pt4`).
- Mostyn John Armstrong, *History and Antiquities of the County of Norfolk* (1781): vol. 1 Cantley / Caister / Bedingham general descent; vol. 4 Kimberley (parallel-to-Bedingham Stuteville/Gunnora marriage); vol. 7 Lessingham (Gerard de Gournay's grant to Bec, corroborating the existing project documentation). All three corroborate the Anderson-Yvery / Cantley senior-collateral picture from an independent eighteenth-century printed witness. SourceId `armstrong-norfolk-1781`.
```

### 3. Saint-Hildevert place file — Hardingham church tithe-gift cross-reference

File: `research/places/collegiale-saint-hildevert-gournay.md`.

```str_replace
old_string: - Split from the Gournay-en-Bray town / honor record.
- Use this record for church-specific architecture, dedication, relic, and surviving-monument context.
- Keep broad seigneurial and frontier-honor narrative in `gournay-en-bray.md`.

<!-- GENERATED:PLACE-REGISTRY:END -->
new_string: - Split from the Gournay-en-Bray town / honor record.
- Use this record for church-specific architecture, dedication, relic, and surviving-monument context.
- Keep broad seigneurial and frontier-honor narrative in `gournay-en-bray.md`.

<!-- GENERATED:PLACE-REGISTRY:END -->

## Armstrong 1781 — Saint-Hildevert tithe-gift pattern extended to Hardingham church

Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 8 (Norwich, 1781), Mitford Hundred entry for the Hardingham / Swathing cluster, records that "Hugh [de Gurney] gave to the chapter of the church of St. Ildebert, of Gourney, in Normandy, the said church [i.e. Hardingham church]." The full passage is preserved at `research/places/hardingham.md` under the Armstrong 1781 section.

This extends the project's existing Saint-Hildevert tithe-gift pattern — already documented for **Caister** and **Cantley** (Norfolk) via Potin 1842 and preserved on this place file as the senior-line collegiate-church relationship — to a **third Norfolk church**. Hugh's pattern was systematic: take English manorial advowsons and assign them to the Gournay-en-Bray collegiate chapter. Hardingham church joins Caister and Cantley as a documented Saint-Hildevert tithe-recipient, with the qualification that Hardingham was a junior-branch holding (G31 Walter's Swathings/Cranworth/Letton/Hardingham cluster) — meaning Hugh's tithe-gift discipline operated across both the senior and junior English-lands portfolios.

The "Hugh" grantor in Armstrong's Hardingham passage is most parsimoniously **Hugh V de Gournay** (the senior-line baron forfeited 1205), giving the gift in the closing decade of pre-Capetian-conquest unity. The grant was made at "Ferretre" — most plausibly **La Ferté** (Normandy), the same la-Ferté collateral seat documented elsewhere on this place file. Source: `armstrong-norfolk-1781`; cross-reference: `research/places/hardingham.md`.
```

### 4. New research-lead file — probable Wentworth shield at West Barsham church

New file write: `research/people/wentworth-impalement-west-barsham-church.md`.

```markdown
# Probable Wentworth shield at West Barsham church — open research lead

## Source

Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 5 (Norwich, 1781), Gallow Hundred entry for West Barsham. Armstrong records the impaled / quartered arms at West Barsham church and identifies the eighth shield only tentatively:

> The arms of Gurney were argent, a cross ingrailed, gules, and impaled the arms of Wauci, gules, three dexter hands erect, argent; also Calthorpe, Lovell, Holdich, Blennerhasset and Lewknor; also they impaled Jernegan, and sable, a chevron between three leopards heads, &c. **probably Wentworth**.

Of the eight families, seven match marriages already documented in the project (Wauci, Calthorpe, Lovell, Holdich, Blennerhasset, Lewknor, Jernegan / Jerningham). The eighth — "sable, a chevron between three leopards' heads, probably Wentworth" — is unidentified.

## What's known

- **No Gurney-Wentworth marriage** is recorded in the published West Barsham line through the late-medieval and Tudor period.
- The "sable, a chevron between three leopards' heads" charge is widely borne in 16th-century English heraldry; without specific tinctures of the chevron and field beyond Armstrong's terse "sable, a chevron between three leopards heads, &c." the identification is provisional.
- The seven known impalements span G19 through G15's daughter-in-law (Lewknor, via Thomas G15-son's wife Martha) — i.e., the late-15th-century through early-17th-century generations of the West Barsham line. A Wentworth alliance would most plausibly belong to the same span.
- The Wentworth family of Nettlestead, Suffolk, was one of the major East Anglian gentry families of the period; a Norfolk-Suffolk gentry alliance with the Gurneys would be plausible.

## Lines of investigation

- **Availability tag: Unknown online.** No specific online source has been checked for a Gurney-Wentworth marriage.
- Visitation of Suffolk (1561 Cooke) for the Wentworths of Nettlestead.
- History of Parliament biographies for the Wentworth knights of the Suffolk-Norfolk border.
- Burke's *Extinct and Dormant Baronetcies* for the various Wentworth lines.
- Cross-check the Wentworth blazons against Foster's *Wentworth Genealogy* (1885) to disambiguate the leopards'-heads charge.

## Origin and routing

Identified in v69 patchset preparation from Armstrong vol. 5. Cross-referenced from `research/places/west-barsham.md` and the v71 absorption of the West Barsham church arms list.

Source ID: `armstrong-norfolk-1781`.
```

### 5. New research-lead file — Herward impaling Gourney in South Erpingham parish church

New file write: `research/people/herward-gourney-impalement-south-erpingham.md`.

```markdown
# Herward impaling Gourney — open research lead

## Source

Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 3 (Norwich, 1781), South Erpingham Hundred. In an arms-in-windows passage for a parish church, Armstrong records: "Brotherton, earl of Norfolk, impaling ... — Morley impaling ditto. — Herward impaling Reymes. — **Herward impaling Gourney**."

The specific parish is not yet pinned to a fact-sheet — the passage sits in a longer South Erpingham arms paragraph that the corpus-supplement v69 transcription preserves with page-context detail. The most likely parish, based on the surrounding Reymes and Brotherton arms, is in the cluster of late-medieval Norfolk gentry parishes near Aylsham.

## What's known

- A **Herward / Hereward alliance with a Gurney** is recorded in heraldic display.
- The Hereward family was descended (per Norfolk antiquarian tradition) from Hereward the Wake; whether the specific Herward who impaled Gourney is of that line or a separate Norfolk Herward family of the period requires further work.
- The Reymes (or Raymes) family was a Norfolk-Suffolk gentry name of the late medieval period; the side-by-side Herward-Reymes / Herward-Gourney pattern suggests both alliances were contemporaneous, late-medieval.

## Lines of investigation

- **Availability tag: Unknown online.** The Hereward family genealogy is partly accessible through 19th-century Norfolk antiquarian publications (Blomefield, Mason, Bryant) but the printed coverage is patchy.
- Cross-check the visitation pedigrees for the Herwards (Visitations of Norfolk 1563 / 1589 / 1613, ed. Walter Rye, Harleian Society 1891) for any Gurney marriage.
- Cross-check the cadet Gurney lines (Walter of Cley → Cawston / Aylsham descent per Rye p. 132 visitation; or the Mitford-Hundred junior branch through G31 Walter de Gournay) for a Herward marriage.

## Origin and routing

Identified in v69 patchset preparation from Armstrong vol. 3. Cross-referenced in `research/places/west-barsham.md` heraldic context as one of three open Armstrong-sourced heraldic leads (the others being the probable Wentworth at West Barsham and the Cawston cadet-branch Wayte impalement).

Source ID: `armstrong-norfolk-1781`.
```

### 6. New research-lead file — Sir Hugh Gourney buried at Langley Priory

New file write: `research/people/sir-hugh-gourney-langley-priory-burial.md`.

```markdown
# Sir Hugh Gourney buried at Langley Priory — open research lead

## Source

Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 7 (Norwich, 1781), in a listing of burials in the church of Langley Priory (Norfolk):

> In the priory church were buried — Sir Robert Thurkelby, Sir Thomas Roscelyn, Sir Peter Roscelyn, **Sir Hugh Gourney**, Sir Jeffrey Say, Sir Henry [Wodehouse?], Sir Fulk Kerdeston, Sir William Kerdeston, and Margaret, his wife, who died in 1328 ...

## What's known

- A **"Sir Hugh Gourney"** was buried at Langley Priory, in a list whose anchor date is 1328 (Margaret Kerdeston's burial). The burial is therefore late 13th / early 14th century.
- The co-buried knights — Thurkelby, two Roscelyns, Say, possibly Wodehouse, two Kerdestons — are all Norfolk-knightly gentry of the period. Sir Hugh Gourney is buried in their social network.
- **No "Sir Hugh Gourney" of this period is currently identified** in the project's senior line (Hugues IV d. c. 1180; Hugues V d. 1214) or junior line (G31 Walter de Gournay and his descendants through the 14th century).

## Possible identities

- **A younger son of one of the senior Hugues** (IV or V), surviving into the late 13th / early 14th century, would fit the date but no such son is named in the FMG / Cawley senior-line apparatus.
- **A collateral figure of the la-Ferté line** (the project's senior-collateral topic file records "Hugh I de la Ferté" as founder of Sigy priory c. 1030/35 and "Hugh II" as his son, monk at St Ouen Rouen — but a 14th-century la-Ferté Hugh would be more than two centuries later than these named figures and would require a lost intervening pedigree).
- **A knight of one of the Norfolk junior subbranches** — the Cley / Cawston / Aylsham cadet branch (originated by Walter Gurney, son of G19 William IV, in the 1490s) is too late; but a junior subbranch of G31 Walter's family living through to the late 13th / early 14th century is possible. The 1316 John de Gurney free-warren plea at Swathing (Armstrong vol. 8) places a working John de Gurney at Hardingham in the exactly contemporary window.

## Lines of investigation

- **Availability tag: Unknown online.** Langley Priory burial registers are not currently in the project corpus.
- Blomefield's Walsham Hundred entry for Langley Priory (vol. xi of the 1810 posthumous edition) — see whether a fuller burial list survives there.
- Norfolk Record Office Langley Priory cartulary (if extant).
- Cross-check the c. 1280–1330 Gurney attestations in Norfolk against any "Hugh" given knight rank.

## Origin and routing

Identified in v69 patchset preparation from Armstrong vol. 7. Cross-referenced from `research/topics/senior-gournay-baron-line-collateral.md` v72 absorption of the Bastwick / Langley collateral cluster.

Source ID: `armstrong-norfolk-1781`.
```

### 7. Intake stub housekeeping — remove stale stub-v67.md; create stub-v73.md

Repair the intake processed-folder stub state. The stale `stub-v67.md` was queued for removal in v69 Phase 2 step 5; v72 explicitly performs the removal in case any of the prior patchsets are not yet applied, and then creates the post-v72 stub.

```bash
# Idempotent stale-stub removal
rm -f sources/intake/processed/stub-v67.md
# Idempotent post-v72 stub creation
cat > sources/intake/processed/stub-v73.md <<'EOF'
Next patchset stub.

Rename this file to `v73-topic.patchset.md` when creating the next patchset, then immediately create `stub-v74.md`.
EOF
```

If `stub-v70.md` was created by v69's Phase 2, it should be removed (it is now stale because v70 has been promoted to a live patchset):

```bash
rm -f sources/intake/processed/stub-v70.md
rm -f sources/intake/processed/stub-v71.md
rm -f sources/intake/processed/stub-v72.md
```

## Validation checklist

- [ ] `research/topics/senior-gournay-baron-line-collateral.md` — gains Armstrong 1781 section covering Bastwick / Kimberley / Cantley Uphall / Langley priory Sir Hugh.
- [ ] `research/topics/anderson-yvery-harpetre-gournay-collateral.md` — Sources list gains Armstrong 1781 entry.
- [ ] `research/places/collegiale-saint-hildevert-gournay.md` — gains Hardingham-church tithe-gift cross-reference section.
- [ ] `research/people/wentworth-impalement-west-barsham-church.md` — new lead file exists.
- [ ] `research/people/herward-gourney-impalement-south-erpingham.md` — new lead file exists.
- [ ] `research/people/sir-hugh-gourney-langley-priory-burial.md` — new lead file exists.
- [ ] `sources/intake/processed/stub-v67.md` — removed (if not already removed by v69).
- [ ] `sources/intake/processed/stub-v73.md` — created with the standard next-stub template.
- [ ] No stub-v70/71/72 remaining (these are obsolete after v70/71/72 promotion).

## Phase 2 completion step

After application:

```bash
python - <<'PY'
from pathlib import Path
src = Path("sources/intake/processed/v72-armstrong-1781-topic-files-and-research-leads.patchset.md")
dst = Path("sources/intake/done/v72-armstrong-1781-topic-files-and-research-leads.patchset.md")
body = src.read_text(encoding="utf-8")
dst.write_text("**Done:** 2026-05-28 HH:MM PT\n\n" + body, encoding="utf-8")
src.unlink()
PY
```

Replace `HH:MM` with the actual completion time.
