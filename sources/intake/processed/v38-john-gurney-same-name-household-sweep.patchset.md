# Intake patchset v38 - Same-name household sweep from the 12 May 2026 raw research batch

```yaml
patchset_id: v38
created: 2026-05-14
repo_scope: gurney-genealogy
phase: phase_2_case_file_section8_expansion
input_packet: sources/intake/john-gurney-2026May/12May2026-John-Gurney-research-raw.md
sibling_patchset: v37-john-gurney-ackworth-primary-and-bury-st-edmunds.patchset.md
phase_2_rule: Add tight Section 8 rows and 8.3 cluster updates for the new same-name comparator households surfaced in the 12 May 2026 raw research file. Probability-changing leads are in v37.
```

## 0. Scope

The 12 May 2026 raw research batch surfaced about two dozen additional John Gurney / Garney / Garne / Gurnoe / Girney households not yet represented in `research/case-files/john-gurney-case-file-v4.md`. None individually changes the case file's central conclusion. Their aggregate effect is to thicken the same-name elimination evidence: each fails on wife-name, child-set, geographic-corridor, or chronology grounds and is documented here as a comparator the case file accounts for.

Approach:
- Bucks and Herts hits fold into the existing Section 8.3 same-county cluster narrative.
- London, Beds, Norfolk, Berks, Worcs, Suffolk-Garneys, and Northants hits each get a one-line Section 8 table row.
- All hits are bundled under one new source `findmypast-john-gurney-2026may-supplementary-same-name-sweep` plus one new footnote `n94`.
- Out-of-corridor Yorkshire/Lancashire/Cambs cluster recorded as held-review.

## 1. `data/sources.json` source registry operations

### 1.1 Add `findmypast-john-gurney-2026may-supplementary-same-name-sweep`

Preserve existing ordering style.

```json
"findmypast-john-gurney-2026may-supplementary-same-name-sweep": {
  "shortTitle": "Findmypast John Gurney same-name sweep, 12 May 2026 raw batch",
  "citation": "Findmypast search-results bundle for John Gurney with surname variants (Gurney, Gurny, Gourney, Garney, Garnes, Garneys, Garrne, Gernne, Gerne, Girney, Girny, Guerne, Gourny, Gorme, Grune, Grone, Grine, Grene, Gurnoe), 1620-1680, across the following sets: England Births & Baptisms 1538-1975; England Deaths & Burials 1538-1991; England Marriages 1538-1973; National Burial Index for England & Wales; Bedfordshire Burials; Bedfordshire Baptisms; Bedfordshire Marriages; Buckinghamshire Burial Index; Buckinghamshire Baptism Index; Buckinghamshire Marriage Index; Berkshire Probate Index; Berkshire Baptisms Index; Britain Marriage Licences; Norfolk Burials; Norfolk Baptisms; Norfolk Monumental Inscriptions 1600-1900s Index; Norfolk Wills & Probate; Hertfordshire Banns & Marriages; Hertfordshire Probate Records Index; Yorkshire Burials; Westminster Burials; Northamptonshire And Rutland Probate Index; London Docklands and East End Baptisms.",
  "archive": "Findmypast (subscription)",
  "url": "https://www.findmypast.com/",
  "corpusStatus": "transcript",
  "corpusPath": null,
  "mediaPath": "sources/intake/john-gurney-2026May/",
  "validationPath": "sources/validations/findmypast-john-gurney-2026may-supplementary-same-name-sweep.md",
  "notes": "Bundle source for the 12 May 2026 raw research batch supplementary same-name sweep. Carries the Findmypast index transcript content for the new Section 8 comparator rows added to the case file by patchset v38, plus the Section 8.3 Buckinghamshire same-county cluster expansion. Aylesbury area search screenshots (image-20260512084250360.png, image-20260512084825041.png, image-20260512084943795.png, image-20260512085055660.png) are retained at the intake media path. Use this bundle for comparator-row provenance; cite record-level sources for any household that is later promoted to deeper research."
}
```

### 1.2 Validation note `sources/validations/findmypast-john-gurney-2026may-supplementary-same-name-sweep.md`

```markdown
# Findmypast John Gurney same-name sweep, 12 May 2026 raw batch

Examined: 2026-05-12 Findmypast search results bundled into the raw intake file `sources/intake/john-gurney-2026May/12May2026-John-Gurney-research-raw.md`. Surname variants swept: Gurney, Gurny, Gourney, Garney, Garnes, Garneys, Garrne, Gernne, Gerne, Girney, Girny, Guerne, Gourny, Gorme, Grune, Grone, Grine, Grene, Gurnoe. Index transcripts retained inline in the raw intake file; screenshots retained at `sources/intake/john-gurney-2026May/image-2026051208*.png`.

Findings landed in:
- `research/case-files/john-gurney-case-file-v4.md` Section 8 new comparator rows and Section 8.3 cluster expansion.

Items not promoted in this pass (held-review):
- Out-of-corridor Yorkshire/Lancashire/Cambs cluster: Calverley 1673 baptism Judith Grune; Rochdale 1669 baptism Susan Grune; Meldreth 1653 marriage John Gorne; Bolton Percy 1637 burial John Gorme. Not in the Norfolk-to-Massachusetts emigration corridor; no Mary or matching child set.
- Henry Gurney of London (father of John Gurney infant buried St Dunstan in the West, London, 26 March 1648). New London Henry-Gurney household; surface for future Section 7 / Coleman Street-network expansion if a primary record links Henry to either Francis Gurney's family or the Coleman Street emigrant cohort.

Source ID added: `findmypast-john-gurney-2026may-supplementary-same-name-sweep`. The validation deliberately stays thin; record-level sourcing for any household promoted to deeper research should be added at that time.
```

## 2. Section 8 main table additions

In `research/case-files/john-gurney-case-file-v4.md`, the existing Section 8 candidate table runs from row "Candidate B" through the existing row "Hempnall, Norfolk." Insert the following new rows. Place each row alphabetically or grouped by county where the existing table already groups; the simplest insertion is at the END of the existing table, immediately BEFORE the next prose heading `### 8.1 Candidate A — Aylesbury hundred Buckinghamshire and Walgrave Northamptonshire`.

Each row's footnote anchor uses the new `n94` reference set defined in Section 4 below.

```markdown
| Stepney / Wapping, London (Mariner) | Middlesex | **Elizabeth** | **ELIMINATED** | Alive in 1633 England (John Garnes, mariner of "Nere Ye Hermitage," Wapping; son John baptized St John, Wapping, 6 January 1633, mother Elizabeth). Wife Elizabeth, not Mary; mariner trade.<sup class="fn"><a href="#n94" id="ref-94a">94</a></sup> |
| Stepney, St Dunstan (John + Rose) | Middlesex | **Rose** | **ELIMINATED** | Alive in 1654 England (son John buried St Dunstan, Stepney, 21 January 1654, parents John and Rose Gurney). Wife Rose, not Mary.<sup class="fn"><a href="#n94" id="ref-94b">94</a></sup> |
| St Gregory by St Paul's, London (licence) | London | **Jane** Underwood | **ELIMINATED** | Alive in 1626 England (yeoman of St Clement Danes, London; marriage licence 15 November 1626 to Jane Underwood, single of St Andrew, Holborn). Wife Jane, not Mary.<sup class="fn"><a href="#n94" id="ref-94c">94</a></sup> |
| St Dunstan in the West, London (Henry's son) | Middlesex | - | **ELIMINATED** | Died in England (infant son of Henry Gurney, buried St Dunstan in the West 26 March 1648). Father Henry Gurney is a separately documented London household; see held-review notes.<sup class="fn"><a href="#n94" id="ref-94d">94</a></sup> |
| St Olave Old Jewry, London | London | Unknown | **ELIMINATED** | Died in England (Jn Gourny, buried St Olave Old Jewry 1665).<sup class="fn"><a href="#n94" id="ref-94e">94</a></sup> |
| St Margaret, Westminster | Middlesex | Unknown | **ELIMINATED** | Died in England (John Gurney, buried St Margaret Westminster 11 September 1675).<sup class="fn"><a href="#n94" id="ref-94f">94</a></sup> |
| Lidlington, Beds | Bedfordshire | Unknown | **ELIMINATED** | Died in England (John Gurney "Senr.," buried Lidlington St Margaret 28 February 1674).<sup class="fn"><a href="#n94" id="ref-94g">94</a></sup> |
| Houghton Regis, Beds | Bedfordshire | **Elizabeth** | **ELIMINATED** | Alive in 1640/41 England (John Gurney + Elizabeth marriage at Houghton Regis All Saints, 23 June 1640/41; same event indexed twice across Bedfordshire Marriages and an All-Saints parish-register transcript). Wife Elizabeth, not Mary.<sup class="fn"><a href="#n94" id="ref-94h">94</a></sup> |
| Norwich, St Michael At Thorn (clergyman) | Norfolk | - | **ELIMINATED** | Died in England (Mr John Girny, occupation Clerke, monumental inscription 17 December 1640, Norwich St Michael At Thorn). Clergyman; no wife or child set in the indexed monumental record.<sup class="fn"><a href="#n94" id="ref-94i">94</a></sup> |
| Norwich, St Lawrence | Norfolk | Unknown | **ELIMINATED** | Died in England (John Garrne, buried Norwich St Lawrence 27 November 1641).<sup class="fn"><a href="#n94" id="ref-94j">94</a></sup> |
| Mickfield / Morningthorpe, Suffolk-Norfolk (Garneys gentry) | Suffolk | - | **ELIMINATED** | Garneys gentry: John Garneys gentleman of Mickfield, Suffolk, will 1675 (NCC Wiseman 196); John Garneys son of Charles Garneys, buried Morningthorpe with Fritton, Norfolk, 17 December 1661. Distinct gentry surname; not the Gurney emigrant household.<sup class="fn"><a href="#n94" id="ref-94k">94</a></sup> |
| Warfield, Berks | Berkshire | - | **ELIMINATED** | Died in England (John Guerne, buried Warfield 1674, son of Francis Guerne). Father Francis, not the colonial John's profile.<sup class="fn"><a href="#n94" id="ref-94l">94</a></sup> |
| Sulhamstead Bannister, Berks | Berkshire | Unknown | **ELIMINATED** | Alive in 1658 England (John Gurney baptized Sulhamstead Bannister 1658, father John Gurney). Father John of this household was still resident at Sulhamstead in 1658, after the colonial John's June 1641 Weymouth appearance.<sup class="fn"><a href="#n94" id="ref-94m">94</a></sup> |
| Upton on Severn, Worcs | Worcestershire | Unknown | **ELIMINATED** | Died in England (John Gurney, buried Upton on Severn St Peter & St Paul 19 January 1666). Out of the Norfolk-to-Massachusetts emigration corridor.<sup class="fn"><a href="#n94" id="ref-94n">94</a></sup> |
| Abthorpe, Northants (labourer) | Northamptonshire | Unknown | **ELIMINATED** | Died in England (John Gurney, labourer, will 1664, Archdeaconry Court of Northampton, Series 4TH, Book 6, fol. 260). Labourer trade; distinct from the Candidate A Northants tenancy at Walgrave.<sup class="fn"><a href="#n94" id="ref-94o">94</a></sup> |
```

Notes on placement and table style:
- Each new row uses the same five-column structure as the existing table.
- The footnote anchor IDs `ref-94a` through `ref-94o` are introduced fresh; they all back-reference `n94`.
- The "Mariner" and "John + Rose" Stepney rows are treated as separate households because the indexed mothers differ (Elizabeth at Wapping 1633 vs Rose at Stepney 1654). A future identity-merge is possible if a primary register pull shows them to be one household, but the current index reading supports two.

## 3. Section 8.3 Buckinghamshire same-county cluster expansion

Add new bullets to the existing Section 8.3 bulleted list (the list that currently includes East Claydon, Chesham, Wing, Cublington, Edlesborough + Mary Kidgell, Weston Turville, Haddenham, Great Kimble, and Hitcham).

Find the existing bullet beginning `- **Hitcham (John):** daughter Mary baptized 22 January 1631...` and insert the new bullets immediately AFTER it, BEFORE the closing paragraph `Aylesbury parish records also show a separately documented Edward Gurny household active in the 1660s...`.

```markdown
- **Amersham, Bucks (John + Avis Garter):** marriage 7 February 1638. Wife Avis Garter, not Mary; a separately documented Bucks John Gurney from Candidate A's 1628 Bierton marriage and from the 1638 Aylesbury Cowheard groom.<sup class="fn"><a href="#n94" id="ref-94p">94</a></sup>
- **Ivinghoe, Bucks:** John Gurney marriage 1640. Single indexed event; spouse and household not surfaced in this pass. Ivinghoe sits about 5 miles north-east of Stewkley and 7 miles south-east of Wing, well inside the Aylesbury Vale.<sup class="fn"><a href="#n94" id="ref-94q">94</a></sup>
- **Marsworth, Bucks:** John Gurny burial 1642 (England Deaths & Burials 1538-1991). Marsworth lies between Ivinghoe and Cheddington, again in the Aylesbury Vale.<sup class="fn"><a href="#n94" id="ref-94r">94</a></sup>
- **Aylesbury, Bucks (1644 and 1669 marriages):** John Gurney marriages indexed at Aylesbury in 1644 and 1669, both in England Marriages 1538-1973. Both events sit chronologically outside Candidate A's 1628 Bierton marriage and 1638 Cowheard event; spouses and households are not surfaced in the present pass. Most plausibly second- or third-generation Aylesbury Vale Gurneys rather than fresh Massachusetts emigration candidates.<sup class="fn"><a href="#n94" id="ref-94s">94</a></sup>
- **Edlesborough, Bucks (1663 marriages, second pass):** two further Edlesborough John Gurney marriages indexed in 1663 alongside the previously documented 1661 John + Mary Kidgell event. Spouses for the 1663 events not surfaced in the present pass; consistent with the Edlesborough Gurney yeoman cluster surfaced in the Phillimore Bucks v1 register block.<sup class="fn"><a href="#n94" id="ref-94t">94</a></sup>
- **Chenies, Bucks (John + John):** son John baptized 18 October 1644, father John Gurney. Generationally later than Candidate A; a separately documented south-Bucks household.<sup class="fn"><a href="#n94" id="ref-94u">94</a></sup>
- **Cublington, Bucks (1666 second John child):** in addition to the case-file's previously documented Isaac 1664 child of John + Mary, the Bucks Baptism Index records a John Gurney baptized at Cublington in 1666 (two indexed entries). Reads as a second child of the same Cublington household.<sup class="fn"><a href="#n94" id="ref-94v">94</a></sup>
- **High Wycombe, Whitchurch, and Stone, Bucks (post-1670 baptisms):** John Gurney baptisms at High Wycombe (1671), Whitchurch (1671), and Stone (1673, two index entries). All baptisms are generationally later than the colonial John and are documented here so the case file accounts for them as Bucks Gurney expansion rather than fresh same-name candidates.<sup class="fn"><a href="#n94" id="ref-94w">94</a></sup>
- **Toddington, Beds (John Gernne 1631):** in addition to the already-eliminated Toddington Beds John + Elizabeth Moreton household, the Bedfordshire Baptisms index records a "John Gernne" baptized 13 February 1631 at Toddington St George of England, son of John. Reads as the same Toddington household covered by footnote n90; spelling variant Gernne reflects the wider Gurney/Gurny/Gurnoe/Gernne cluster.<sup class="fn"><a href="#n94" id="ref-94x">94</a></sup>
- **Earsham, Norfolk (John Girney 1636):** in addition to the already-eliminated Earsham John Singler will 1639, the Norfolk Baptisms index records a John Girney baptized at Earsham 23 December 1636, father John. Reads as a child of the same Earsham household; not a separate candidate.<sup class="fn"><a href="#n94" id="ref-94y">94</a></sup>
- **Tring, Herts (John + Elizabeth Shepard):** marriage banns at Tring 4 November 1655 (Hertfordshire Banns & Marriages, also indexed in England Marriages 1538-1973 and Boyd's Marriage Indexes). Wife Elizabeth Shepard, not Mary; a Hertfordshire household adjacent to the eliminated Candidate C Berkhamsted parish, distinct from Candidate C.<sup class="fn"><a href="#n94" id="ref-94z">94</a></sup>
- **Northchurch, Herts (1661 probate):** Hertfordshire Probate Records Index 1415-1858 records a John Gurney probate event at Northchurch in 1661. Northchurch lies adjacent to Berkhamsted; the 1661 probate reads as related to the Candidate C Berkhamsted Hertfordshire cluster rather than as a separate emigration candidate.<sup class="fn"><a href="#n94" id="ref-94aa">94</a></sup>
- **Puttenham, Herts:** John Gurney baptism 1670. Single indexed event; chronologically after the colonial John's 1662/3 death and read as part of the Bucks/Herts post-1660 household expansion.<sup class="fn"><a href="#n94" id="ref-94bb">94</a></sup>
```

Add this closing sentence to the existing Section 8.3 paragraph that begins `Aylesbury parish records also show a separately documented Edward Gurny household active in the 1660s...` (no replacement; append at the end of the paragraph, immediately before the next paragraph `The Aylesbury Prerogative Court of Canterbury probate records show a further Buckinghamshire family with a Daniel Gurney who died 1669...`):

```markdown

The post-1660 Bucks and Herts John Gurney baptisms at Cublington 1666, Chenies 1644, Stone 1671 and 1673, High Wycombe 1671, Whitchurch 1671, Puttenham 1670, and the Northchurch 1661 probate are bundled here as Aylesbury Vale and Chiltern Gurney household expansion. None is independently a Massachusetts-emigration candidate; they are listed so the case file's Section 8 comparator coverage accounts for them.<sup class="fn"><a href="#n94" id="ref-94cc">94</a></sup>
```

## 4. Footnote n94 definition

Insert the following new footnote in the case-file notes block, immediately after the `n93` footnote (which is defined in patchset v37):

```html
<li id="n94" value="94">Findmypast supplementary same-name sweep, 12 May 2026 raw research batch (`sources/intake/john-gurney-2026May/12May2026-John-Gurney-research-raw.md`). Surname variants Gurney, Gurny, Gourney, Garney, Garnes, Garneys, Garrne, Gernne, Girney, Girny, Guerne, Gourny across England Births & Baptisms 1538-1975; England Deaths & Burials 1538-1991; England Marriages 1538-1973; National Burial Index; Bedfordshire Burials and Baptisms and Marriages; Buckinghamshire Burial Index, Baptism Index, Marriage Index; Berkshire Probate Index; Berkshire Baptisms Index; Britain Marriage Licences; Norfolk Burials, Baptisms, and Monumental Inscriptions 1600-1900s Index; Norfolk Wills & Probate; Hertfordshire Banns & Marriages and Probate Records Index; Yorkshire Burials; Westminster Burials; Northamptonshire And Rutland Probate Index; London Docklands and East End Baptisms. Source ID <code>findmypast-john-gurney-2026may-supplementary-same-name-sweep</code>. Aylesbury area screenshots retained at `sources/intake/john-gurney-2026May/image-2026051208*.png`. Out-of-corridor Yorkshire/Lancashire/Cambs cluster (Calverley 1673 Judith Grune; Rochdale 1669 Susan Grune; Meldreth 1653 John Gorne; Bolton Percy 1637 John Gorme) and London Henry Gurney 1648 St Dunstan in the West infant burial are held in the patchset v38 validation note for future review. <a class="backref" href="#ref-94a">back</a> <a class="backref" href="#ref-94b">back</a> <a class="backref" href="#ref-94c">back</a> <a class="backref" href="#ref-94d">back</a> <a class="backref" href="#ref-94e">back</a> <a class="backref" href="#ref-94f">back</a> <a class="backref" href="#ref-94g">back</a> <a class="backref" href="#ref-94h">back</a> <a class="backref" href="#ref-94i">back</a> <a class="backref" href="#ref-94j">back</a> <a class="backref" href="#ref-94k">back</a> <a class="backref" href="#ref-94l">back</a> <a class="backref" href="#ref-94m">back</a> <a class="backref" href="#ref-94n">back</a> <a class="backref" href="#ref-94o">back</a> <a class="backref" href="#ref-94p">back</a> <a class="backref" href="#ref-94q">back</a> <a class="backref" href="#ref-94r">back</a> <a class="backref" href="#ref-94s">back</a> <a class="backref" href="#ref-94t">back</a> <a class="backref" href="#ref-94u">back</a> <a class="backref" href="#ref-94v">back</a> <a class="backref" href="#ref-94w">back</a> <a class="backref" href="#ref-94x">back</a> <a class="backref" href="#ref-94y">back</a> <a class="backref" href="#ref-94z">back</a> <a class="backref" href="#ref-94aa">back</a> <a class="backref" href="#ref-94bb">back</a> <a class="backref" href="#ref-94cc">back</a></li>
```

## 5. Existing-row footnote touch-ups (optional, low priority)

The existing Section 8 row for `Winkfield, Berkshire | Berkshire | **Alice / Ellice** | **ELIMINATED**` already cites the PCC will PROB 11/372/123 (1682). The 12 May 2026 batch surfaced the earlier Berkshire Probate Index entry D/A1/73/51 for John Gurney yeoman of Winkfield, probate year 1671 (Archdeaconry of Berkshire). This is almost certainly the same Winkfield John, with the 1671 lower-court grant preceding the 1682 PCC sentence; the row already eliminates this candidate, so no row text change is required, but a small footnote-body addition can be made if the case file is being touched anyway:

In the existing `n60` (or whichever footnote currently anchors the Winkfield row's elimination citation), the editor may optionally append: `; lower-court Berkshire Probate Index entry D/A1/73/51 (Archdeaconry of Berkshire) 1671 supplies an earlier grant for the same Winkfield John Gurney yeoman. Source ID findmypast-john-gurney-2026may-supplementary-same-name-sweep.` This is genuinely optional and the patchset can be applied without it.

## 6. Audit checklist

Before declaring this patchset applied, confirm each item:

- `data/sources.json` updated with one new source ID `findmypast-john-gurney-2026may-supplementary-same-name-sweep`.
- One new validation file `sources/validations/findmypast-john-gurney-2026may-supplementary-same-name-sweep.md` created.
- Case-file Section 8 table appended with the 15 new rows listed in §2.
- Case-file Section 8.3 bulleted list expanded with the 14 new bullets listed in §3, plus the closing-sentence append.
- Footnote `n94` inserted in the notes block after `n93`.
- (Optional) `n60` Winkfield supplement appended.

## 7. Held-review and deferred items

- **Out-of-corridor Yorkshire/Lancashire/Cambs cluster:** Judith Grune Calverley 1673; Susan Grune Rochdale 1669; John Gorne marriage Meldreth Cambs 1653 (spouse field "[No Name]" — index defect); John Gorme burial Bolton Percy 1637 (father Christopher). Not promoted to the case-file Section 8 table in this pass because each sits well outside the Norfolk-to-Massachusetts emigration corridor and none surfaces a Mary wife or matching child set. If the Ackworth Yorkshire household (see v37) is later promoted to deeper investigation, these Yorkshire/Lancashire same-name households should be re-screened as part of that follow-up.
- **Henry Gurney of London (1648 St Dunstan in the West):** infant son John Gurney buried 26 March 1648, father Henry Gurney. The Henry Gurney household is independently documented in this single index entry and is not currently visible elsewhere in the case file. If a primary London record links Henry Gurney to Francis Gurney's family or to the Coleman Street / St Stephen Coleman Street Puritan emigrant network, the Henry-Gurney London household should be added as a new same-name comparator and cross-linked to Section 10.4 of the case file.
- **Aylesbury area Findmypast screenshots:** four PNG search-results screenshots (`image-20260512084250360.png` for burials; `image-20260512084825041.png` for marriages, 37 results shown 9 on-screen; `image-20260512084943795.png` for baptisms; `image-20260512085055660.png` for the single Northchurch Herts wills hit) are retained at the intake media path. Per direction from the user on 2026-05-14, the off-screen marriages tail (~28 results beyond the on-screen 9) is not pursued in this pass; the on-screen entries are absorbed into the Section 8 and 8.3 additions above.
