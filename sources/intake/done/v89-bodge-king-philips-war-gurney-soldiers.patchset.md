**Done:** 2026-06-06 23:56 PT

# v89 — Bodge, *Soldiers in King Philip's War* (1891): the Weymouth Gurney soldiers Peter (G13's son) and Zachariah (G12's son)

**Outcome:** promote.

## Context

A page-by-page review of George Madison Bodge, *Soldiers in King Philip's War* (Boston: Printed for the Author, 1891) — Internet Archive `soldiersinkingph00bodg`, the Boston University copy — found exactly three Gurney references, confirmed against the page images (the OCR text layer silently drops one of them) and against Bodge's own name index (p. 364), which groups the surname "Gorney / Gurney" at pp. 113, 114, 236 and nowhere else:

- **p. 114** — "**Peeter Gurnay**," under the *Weymouth* file of Captain Isaac Johnson's company, mustered at Dedham 10 December 1675 for the Narragansett (Great Swamp) campaign.
- **p. 113** — "**Zachariah Gurny**," a pay credit (24 July, £2 14s) in the "Credited under Capt. Isaac Johnson" roll.
- **p. 236** — "**Zacha-ry Gorney**," of Weymouth, among the men returned as failing to appear at the 29 April 1676 Concord muster of Captain John Holbrooke's company.

These map onto known family members already reasoned about in the repo from secondary sources (Rigler 1994; Savage), but never before tied to Bodge's primary lists:

- **Peter** is a son of the emigrant **John Gurney-1 (G13)** — brother of Richard G12. Rigler's John Gurney-1 entry already calls him "of Weymouth, a soldier in Johnson's Co. Dec. 1675, killed in King Philip's War, Dec. 1676 (Savage 2:325)." Bodge p. 114 is that primary record; Peter's absence from the same page's December 1675 casualty list is consistent with his survival of the Fort Fight and death later in 1676. Born c. 1638–45 in Massachusetts, he was a grown man (~30–37) in the campaign.
- **Zachariah** is a son of **Richard Gurney (G12)** — Rigler's Richard-2 child "Zachariah, b.c. 1660, m. Mary Benson," whom Robert G. Rigler's c. 1980 worksheet only *tagged* a King Philip's War soldier without a citation. Bodge pp. 113 and 236 are the missing primary documentation. At ~15–16 he was a youth soldier; he survived, married Mary Benson, and co-administered his father's estate in 1691.

The age-patterning corroborates both identifications: the grown uncle Peter appears in the front-line December 1675 muster (p. 114), while the teenaged nephew Zachariah appears only in the lighter 1676 records (a pay credit, p. 113; a no-show default, p. 236).

The repo previously listed Bodge only under "Sources to obtain" in the G12 companion. This patchset registers the source, lands the verbatim extracts, documents Zachariah's service for the first time, supplies the primary record behind Peter's, and threads the multi-source agreement (Bodge ↔ Rigler ↔ Savage ↔ Sprague) into the citations.

## Source tracking

- **New `sourceId`: `bodge-soldiers-king-philips-war-1891`.** Added to `data/sources.json` (Operation 1). Rich verbatim extracts → `sources/corpus_supplement/bodge-soldiers-king-philips-war-1891-gurney-extracts.md` (Operation 2). Default-on validation worksheet → `sources/validations/bodge-soldiers-king-philips-war-1891.md` (Operation 3).
- **Existing `sourceId`s reused:** `rigler-gurney-family-aaron-zuinglius-1994`, `rigler-genealogy-notes-c1980`, `sprague-braintree` (footnote corroboration only).
- **Raw file disposition:** the 27 MB public-domain PDF is freely available on the Internet Archive and is redundant with the registered URL and the text extract, so it is **not** committed; Phase 2 moves it to a git-ignored `_local/` master with a committed README stub (Operation 8). Consistent with every other Bodge-class book source in the registry (`mediaPath: null`).

---

## Operation 1 — `data/sources.json`: register the source

`str_replace` in `data/sources.json`:

**old_string:**
```
      "notes": "Secondary attestation: places John Gurney at Weymouth on 2 June 1641, when the General Court remitted the fine of John Porter, James Ludden, and John Gurney 'for want of gunpowder.' The author glosses the quoted record 'Ludden and Gurney were of Weymouth.' Independent confirmation alongside MBCR 1:331 of John's June 1641 Weymouth presence."
    },
```

**new_string:**
```
      "notes": "Secondary attestation: places John Gurney at Weymouth on 2 June 1641, when the General Court remitted the fine of John Porter, James Ludden, and John Gurney 'for want of gunpowder.' The author glosses the quoted record 'Ludden and Gurney were of Weymouth.' Independent confirmation alongside MBCR 1:331 of John's June 1641 Weymouth presence."
    },
    "bodge-soldiers-king-philips-war-1891": {
      "shortTitle": "Bodge, Soldiers in King Philip's War (1891)",
      "citation": "Bodge, George Madison. Soldiers in King Philip's War: Containing Lists of the Soldiers of Massachusetts Colony, Who Served in the Indian War of 1675-1677, with Sketches of the Principal Officers, and Copies of Ancient Documents and Records Relating to the War. Boston: Printed for the Author, 1891.",
      "archive": "Internet Archive (Boston University copy).",
      "url": "https://archive.org/details/soldiersinkingph00bodg",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/bodge-soldiers-king-philips-war-1891-gurney-extracts.md",
      "mediaPath": null,
      "validationPath": "sources/validations/bodge-soldiers-king-philips-war-1891.md",
      "notes": "Massachusetts muster, pay, and casualty rolls of King Philip's War (1675-1677). Three Gurney references, all of Weymouth and all confirmed against the page images (the OCR text layer drops the p. 113 entry): Peeter Gurnay under Weymouth in Capt. Isaac Johnson's company, Dedham muster 10 Dec. 1675 (p. 114); Zachariah Gurny credited under Capt. Isaac Johnson's company, 24 July credit (p. 113); Zacha-ry Gorney of Weymouth among the men returned as not appearing at Capt. John Holbrooke's Concord muster, 29 Apr. 1676 (p. 236). Bodge's index (p. 364) groups the surname 'Gorney / Gurney' at pp. 113, 114, 236 and nowhere else. Peter is a son of John Gurney-1 (G13); Zachariah is a son of Richard Gurney (G12). First edition, 100 copies, printed by David Clapp & Son."
    },
```

---

## Operation 2 — new file: `sources/corpus_supplement/bodge-soldiers-king-philips-war-1891-gurney-extracts.md`

`new file write` with the full body below:

```markdown
# Bodge, *Soldiers in King Philip's War* (1891) — Gurney extracts

Source ID: `bodge-soldiers-king-philips-war-1891`

Working transcriptions of the three Gurney references in George Madison Bodge, *Soldiers in King Philip's War* (Boston: Printed for the Author, 1891), with the surrounding context that fixes each man's company, date, and service. Readings are from the page images on the Internet Archive copy `soldiersinkingph00bodg` (book pages 113, 114, 236, 364 = PDF images 141, 142, 266, 394). Spelling and capitalization follow the print; bracketed text marks editorial expansion of a line-break or an obvious reading.

All three men are of Weymouth. Bodge's index (p. 364) groups the surname under one head — "Gorney, / Gurney, } 113, 114, 236" — and lists no other page, so these are the only Gurney references in the volume.

---

## Peter — Capt. Isaac Johnson's company, p. 114 (with chapter context, pp. 112-114)

Chapter IX, "Capt. Isaac Johnson and his Men." The company narrative (p. 112):

> "Upon the mustering of forces for the Narraganset campaign, Capt. Johnson was placed in command of a company made up of men from Roxbury, Dorchester, Milton, Braintree, Weymouth, Hingham and Hull, seventy-five all told. ... The company took part in the memorable march and attack on the fort, as before related, and the brave captain was among the first to fall while gallantly leading his men across the fatal tree[-]bridge at the entrance to the fort."

— i.e. the Great Swamp Fight, 19 December 1675. "List of Capt Johnson's Company," made at Dedham 10 December 1675 (Mass. Archives 67:293), *Weymouth* file (p. 114):

> Hezek: King · Jonas Humphrey · Joseph Richards · Allin Dugland · John Whitmarsh · **Peeter Gurnay** · Edward Kingman · John Read · James Read · John Lovet

The same page's casualty list — "The names of those soldiers y[a]t were slayne & wounded of Capt Johnson's Comp[an]a December 1675" — names Capt. Isaac Johnson, Jonathan Pitcher, Jos. Watson, Wm. Linckorn, John Spur, Benj. Crane, Jno. Langley, Tho. Davenport, Allin Dugland of Weymouth (among the four slain), Jno. Faxton, Isaack King of Weymouth, and Lieut. Phineas Upham, who were "at Road Island Jan. 6th 1675-6." **Peter is not in the casualty list**, consistent with his surviving the Fort Fight and being killed later in the war (December 1676 per Savage 2:325 and Rigler).

## Zachariah — Capt. Isaac Johnson's company credit roll, p. 113

"Credited under Capt. Isaac Johnson," the pay roll carrying dated credits from August 1675 through September 1676. Under the heading "July 24" (1676):

> John Plum — 02 14 00
> **Zachariah Gurny** — 02 14 00
> Charles Cahan — 02 14 00
> Onesiphorus Stanly — 02 14 00
> John Spurr — 02 14 00

## Zachariah — Capt. John Holbrooke's company, defaulter list, p. 236

Holbrooke of Weymouth "in the spring of 1676 was appointed to command one of the companies raised and sent out to suppress the 'Insolencies' of the Indians and to 'range the woods towards Hassanamesit.'" His muster letter:

> "Concord ye 29th of Aprill 1676 ... According to orders I have ... this Day ... mustered my Company, And have here send the list of those that not appear according to order ..."

The attached return of defaulters lists men from Boston, Roxbury, Dorchester, Dedham, Braintry, Weymouth, and Hingham who were impressed (with horses) but failed to appear, closing:

> "& Defects ... From Waymouth, **Zacha[-]ry Gorney**. From Hingham, Jn[o] Feres & Arthur Sherman. p[er] me John Holbrooke Capn."
> *Mass. Archives, Vol. 69, p. 12. Credited under Capt. John Holbrooke.*

## Index, p. 364

> Gorney, ⎫
> Gurney, ⎰ 113, 114, 236

<!-- Method: the printed text was read from the page images; the OCR text layer of the Internet Archive PDF drops the p. 113 "Zachariah Gurny" entry entirely and garbles the index head, so the image read (not the OCR) is authoritative here. See the validation worksheet. -->
```

---

## Operation 3 — new file: `sources/validations/bodge-soldiers-king-philips-war-1891.md`

`new file write` with the full body below:

```markdown
# Validation — Bodge, *Soldiers in King Philip's War* (1891)

Source ID: `bodge-soldiers-king-philips-war-1891`

**Examined:** book pages 113, 114, 236, and the name index on p. 364 (PDF images 141, 142, 266, 394) of the Internet Archive copy `soldiersinkingph00bodg` (Boston University copy). Title page confirms first edition, Boston, "Printed for the Author," 1891.

**Method note (material).** The full text was extracted and searched, then every candidate was confirmed against the page images. The OCR text layer is unreliable for this purpose: it **drops the p. 113 "Zachariah Gurny" entry entirely** and garbles the index head. The image read — not the OCR — is authoritative. The index (p. 364) groups "Gorney / Gurney" at pp. 113, 114, 236 and no other page, so the volume's Gurney references are complete at three.

**Findings landed:**
- Peter Gurney (son of John Gurney-1, G13) — primary muster record (p. 114) recorded in `research/people/g13-john-gurney-fact-sheet.research.md`.
- Zachariah Gurney (son of Richard Gurney, G12) — primary service records (pp. 113, 236) recorded in `research/people/g12-richard-gurney-fact-sheet.research.md` and surfaced in `fact-sheets/g12-richard-gurney-fact-sheet.md`.
- Verbatim extracts: `sources/corpus_supplement/bodge-soldiers-king-philips-war-1891-gurney-extracts.md`.

**Unexamined / open:** no full read beyond the Gurney pages and their immediate chapter context; Bodge's introductory matter and the balance of the company rolls were not transcribed.

**Local master:** the source PDF is git-ignored at `sources/media/bodge-soldiers-king-philips-war-1891/_local/`; the canonical public copy is the Internet Archive URL in `data/sources.json`.

**Execution trail:** `sources/intake/done/v89-bodge-king-philips-war-gurney-soldiers.patchset.md`.
```

---

## Operation 4 — `fact-sheets/g12-richard-gurney-fact-sheet.md`: Children table (Zachariah row)

`str_replace`:

**old_string:**
```
    <tr><td>Zachariah Gurney</td><td>c. 1660</td><td>Married Mary Benson; co-administrator of his father's estate in 1691. <sup class="fn"><a href="#n7" id="ref-7e">7</a></sup></td></tr>
```

**new_string:**
```
    <tr><td>Zachariah Gurney</td><td>c. 1660</td><td>Married Mary Benson; as a youth he was swept into the 1676 musters of King Philip's War and came home; co-administrator of his father's estate in 1691. <sup class="fn"><a href="#n7" id="ref-7e">7</a></sup><sup class="fn"><a href="#n9" id="ref-9">9</a></sup></td></tr>
```

## Operation 5 — `fact-sheets/g12-richard-gurney-fact-sheet.md`: Highlights bullet

`str_replace`:

**old_string:**
```
  <li><strong>King Philip's War struck the wider family hard.</strong> Richard's brother John was among the dead in the Mendon massacre of 14 July 1675 — the first major bloodshed of the war — and a second brother, Peter, a soldier in Captain Johnson's company, was killed in the fighting late in 1676. Richard himself stayed at Weymouth, and his own children all outlived the war. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></li>
```

**new_string:**
```
  <li><strong>King Philip's War struck the wider family hard.</strong> Richard's brother John was among the dead in the Mendon massacre of 14 July 1675 — the first major bloodshed of the war — and a second brother, Peter, a soldier in Captain Isaac Johnson's company, was killed in the fighting late in 1676. Richard himself stayed at Weymouth; his teenage son Zachariah was caught up in the 1676 musters but survived, and all his children outlived the war. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup><sup class="fn"><a href="#n9" id="ref-9b">9</a></sup></li>
```

## Operation 6 — `fact-sheets/g12-richard-gurney-fact-sheet.md`: Narrative paragraph

`str_replace`:

**old_string:**
```
<p>The most personal mark of those years on the family is bleak, though it fell on Richard's brothers rather than his sons. His brother John was among the dead at the Mendon massacre of 14 July 1675 — the first major violence of King Philip's War, when Nipmuc fighters attacked the small frontier town of Mendon and killed several inhabitants — and another brother, Peter, a soldier in Captain Johnson's company, was killed in the war late in 1676. Richard himself remained at Weymouth through it all, neither soldier nor displaced. He died intestate in October 1691, his estate administered by two of his sons, Richard and Zachariah, after the eldest son John declined the duty — the very record that finally untangles Richard from the 1719 death date long misattributed to him from his same-named son.</p>
```

**new_string:**
```
<p>The most personal mark of those years on the family is bleak. His brother John was among the dead at the Mendon massacre of 14 July 1675 — the first major violence of King Philip's War, when Nipmuc fighters attacked the small frontier town of Mendon and killed several inhabitants — and another brother, Peter, a soldier in Captain Isaac Johnson's company, was killed in the war late in 1676.<sup class="fn"><a href="#n6" id="ref-6b">6</a></sup> The war reached the next generation too: Richard's teenage son Zachariah was caught up in the 1676 musters — credited for service under Captain Johnson's company, and listed among the Weymouth men who failed to answer Captain John Holbrooke's call to muster at Concord that April — but he came home.<sup class="fn"><a href="#n9" id="ref-9c">9</a></sup> Richard himself remained at Weymouth through it all, neither soldier nor displaced. He died intestate in October 1691, his estate administered by two of his sons, Richard and Zachariah, after the eldest son John declined the duty — the very record that finally untangles Richard from the 1719 death date long misattributed to him from his same-named son.</p>
```

## Operation 7 — `fact-sheets/g12-richard-gurney-fact-sheet.md`: footnote n6 (add Bodge corroboration) and new footnote n9

### 7a — augment footnote n6

`str_replace`:

**old_string:**
```
  <li id="n6">The Mendon massacre of 14 July 1675 opened King Philip's War. The John Gurney killed there, and Peter Gurney, "a soldier in Johnson's Co.… killed in King Philip's War, Dec. 1676," were sons of the emigrant John Gurney-1 (G13) — Richard's brothers, not his sons — as shown by Rigler's John Gurney-1 children and by the eldest son John of Richard being alive to refuse administration in 1691. See the <a href="/key-research/john-gurney-case-file.html">John Gurney case file</a> and Rigler, <em>Gurney Family from Aaron to Zuinglius</em>. Corroborated for the John Gurney-1 family group by Sprague, <em>Genealogies of Braintree</em>. Source IDs: <code>rigler-gurney-family-aaron-zuinglius-1994</code>; <code>sprague-braintree</code>. <a class="citation-back" href="#ref-6">↩</a></li>
```

**new_string:**
```
  <li id="n6">The Mendon massacre of 14 July 1675 opened King Philip's War. The John Gurney killed there, and Peter Gurney, "a soldier in Johnson's Co.… killed in King Philip's War, Dec. 1676," were sons of the emigrant John Gurney-1 (G13) — Richard's brothers, not his sons — as shown by Rigler's John Gurney-1 children and by the eldest son John of Richard being alive to refuse administration in 1691. Peter's service is documented at primary level in George Madison Bodge, <em>Soldiers in King Philip's War</em> (Boston, 1891), p. 114, which lists "Peeter Gurnay" under Weymouth in Captain Isaac Johnson's company at the Dedham muster of 10 December 1675; he is absent from that company's December 1675 casualty list, consistent with his death later in 1676. See the <a href="/key-research/john-gurney-case-file.html">John Gurney case file</a> and Rigler, <em>Gurney Family from Aaron to Zuinglius</em>. Corroborated for the John Gurney-1 family group by Sprague, <em>Genealogies of Braintree</em>. Source IDs: <code>bodge-soldiers-king-philips-war-1891</code>; <code>rigler-gurney-family-aaron-zuinglius-1994</code>; <code>sprague-braintree</code>. <a class="citation-back" href="#ref-6">↩</a></li>
```

### 7b — insert footnote n9 after n8

`str_replace`:

**old_string:**
```
  <li id="n8">See the <a href="/fact-sheets/g11-benjamin-gurney-fact-sheet.html">Benjamin Gurney (G11) fact sheet</a> for the Abington-line continuation; Rigler gives his marriage to Rebecca Staples. Source ID: <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-8">↩</a></li>
</ol>
```

**new_string:**
```
  <li id="n8">See the <a href="/fact-sheets/g11-benjamin-gurney-fact-sheet.html">Benjamin Gurney (G11) fact sheet</a> for the Abington-line continuation; Rigler gives his marriage to Rebecca Staples. Source ID: <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-8">↩</a></li>
  <li id="n9">Zachariah's war service is recorded in George Madison Bodge, <em>Soldiers in King Philip's War</em> (Boston: Printed for the Author, 1891): page 113 credits "Zachariah Gurny" under Captain Isaac Johnson's company (24 July, £2 14s), and page 236 lists "Zacha-ry Gorney" of Weymouth among the men who failed to appear at the 29 April 1676 Concord muster of Captain John Holbrooke's company. Bodge's index (p. 364) groups the surname at pp. 113, 114, 236. This matches the King Philip's War soldier carried in the Gurney family records compiled by Rigler. Source IDs: <code>bodge-soldiers-king-philips-war-1891</code>; <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-9">↩</a></li>
</ol>
```

## Operation 8 — `fact-sheets/g12-richard-gurney-fact-sheet.md`: Timeline row

`str_replace`:

**old_string:**
```
      <tr><td>1675–76</td><td>Brother John killed at the Mendon massacre (14 July 1675); brother Peter killed in King Philip's War (1676).</td></tr>
```

**new_string:**
```
      <tr><td>1675–76</td><td>Brothers John (Mendon massacre, 14 July 1675) and Peter (1676) killed in King Philip's War; son Zachariah served in the 1676 musters and survived.</td></tr>
```

---

## Operation 9 — `research/people/g13-john-gurney-fact-sheet.research.md`: Peter's primary muster record

`str_replace`:

**old_string:**
```
[^fmp-peter-gurney-2026-05-09]: Findmypast UK Parish Baptisms search, first name Peter, surname Gurney with variants, year of birth 1632-1642, Britain-wide; transcript `R_880200102` for Peter G., christened 27 February 1641 at Smallburgh, Norfolk, father Peter G. Source ID: `findmypast-uk-parish-baptisms`.

**Isaac:** Attribution remains uncertain. Possibly born c. 1643 in Massachusetts.
```

**new_string:**
```
[^fmp-peter-gurney-2026-05-09]: Findmypast UK Parish Baptisms search, first name Peter, surname Gurney with variants, year of birth 1632-1642, Britain-wide; transcript `R_880200102` for Peter G., christened 27 February 1641 at Smallburgh, Norfolk, father Peter G. Source ID: `findmypast-uk-parish-baptisms`.

Peter's New England military service is documented at primary level. Bodge's *Soldiers in King Philip's War* lists "Peeter Gurnay" under Weymouth in Captain Isaac Johnson's company, mustered at Dedham 10 December 1675 for the Narragansett (Great Swamp) campaign — the company in which Johnson was killed leading his men across the log bridge at the Narragansett fort on 19 December 1675. Peter is absent from the same page's list of that company's December 1675 slain and wounded, consistent with his surviving the Fort Fight and being killed later in the war, in December 1676. This is the record behind the "soldier in Johnson's Co. Dec. 1675, killed … Dec. 1676" found in Savage and Rigler.[^bodge-peter-g13]

[^bodge-peter-g13]: George Madison Bodge, *Soldiers in King Philip's War* (Boston: Printed for the Author, 1891), p. 114 (Captain Isaac Johnson's company, Weymouth file, "Peeter Gurnay"; Dedham muster 10 December 1675), with the company narrative and December 1675 casualty list at pp. 112–114, and the name index at p. 364 grouping "Gorney / Gurney" at pp. 113, 114, 236. Corroborates James Savage, *A Genealogical Dictionary of the First Settlers of New England*, vol. 2, p. 325 (cited via Rigler), and Jean Gurney Rigler, *The Gurney Family from Aaron to Zuinglius* (1994), John Gurney-1 entry. Verbatim extracts at [`sources/corpus_supplement/bodge-soldiers-king-philips-war-1891-gurney-extracts.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/bodge-soldiers-king-philips-war-1891-gurney-extracts.md). Source IDs: `bodge-soldiers-king-philips-war-1891`; `rigler-gurney-family-aaron-zuinglius-1994`.

**Isaac:** Attribution remains uncertain. Possibly born c. 1643 in Massachusetts.
```

---

## Operation 10 — `research/people/g12-richard-gurney-fact-sheet.research.md`: Zachariah's King Philip's War service

`str_replace`:

**old_string:**
```
### Mendon massacre, 14 July 1675

The death of Richard's son John Gurney Jr. at the Mendon massacre is corroborated by multiple secondary sources — King Philip's War standard histories (Drake, Bourne, et al.) routinely list Mendon's casualties of 14 July 1675. The exact wording in <code>data/ancestors v26.json</code> says "Killed at Mendon massacre 1675"; Sprague, <em>Genealogies of Braintree</em>, p. 695, also lists this son in the John Gurney-1 family group ("of Weymouth/Mendon; killed at Mendon, July 1675").
```

**new_string:**
```
### Mendon massacre, 14 July 1675

The death of Richard's son John Gurney Jr. at the Mendon massacre is corroborated by multiple secondary sources — King Philip's War standard histories (Drake, Bourne, et al.) routinely list Mendon's casualties of 14 July 1675. The exact wording in <code>data/ancestors v26.json</code> says "Killed at Mendon massacre 1675"; Sprague, <em>Genealogies of Braintree</em>, p. 695, also lists this son in the John Gurney-1 family group ("of Weymouth/Mendon; killed at Mendon, July 1675").

### Zachariah's King Philip's War service (Bodge, p. 113 and p. 236)

Richard's son Zachariah (b. c. 1660, m. Mary Benson) appears by name in the 1676 muster rolls, supplying the primary record behind the "King Philip's War soldier" tag carried only as an unsourced note in Robert G. Rigler's c. 1980 worksheet. Bodge's *Soldiers in King Philip's War* records him twice: "Zachariah Gurny," credited under Captain Isaac Johnson's company (a pay credit dated 24 July, £2 14s, p. 113); and "Zacha-ry Gorney" of Weymouth, returned among the men who failed to appear at the Concord muster of Captain John Holbrooke's company on 29 April 1676 — the company Holbrooke raised that spring to "range the woods towards Hassanamesit" (p. 236). At roughly fifteen or sixteen he was a youth soldier; he survived the war, married Mary Benson, and was alive in 1691 to co-administer his father's estate. The same Captain Johnson's-company material carries his older uncle Peter on the facing page (p. 114; see the [G13 companion](https://github.com/allengurney/gurney-genealogy/blob/main/research/people/g13-john-gurney-fact-sheet.research.md)) — the grown uncle in the front-line December 1675 muster, the teenaged nephew only in the lighter 1676 records. Bodge's index (p. 364) groups the surname under "Gorney / Gurney" at pp. 113, 114, 236 — the book's only Gurney references.[^bodge-zachariah-g12]

[^bodge-zachariah-g12]: George Madison Bodge, *Soldiers in King Philip's War* (Boston: Printed for the Author, 1891), p. 113 ("Zachariah Gurny," Captain Isaac Johnson's company credit roll, 24 July credit, £2 14s) and p. 236 ("Zacha-ry Gorney" of Weymouth, defaulter at the 29 April 1676 Concord muster of Captain John Holbrooke's company; Mass. Archives 69:12), with the name index at p. 364. The entries were confirmed against the page images; the OCR text layer drops the p. 113 entry. Provides the primary documentation for the soldier tag in Robert G. Rigler's c. 1980 worksheet (Source ID: `rigler-genealogy-notes-c1980`). Verbatim extracts at [`sources/corpus_supplement/bodge-soldiers-king-philips-war-1891-gurney-extracts.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/bodge-soldiers-king-philips-war-1891-gurney-extracts.md). Source ID: `bodge-soldiers-king-philips-war-1891`.
```

---

## Operation 11 — `research/people/g12-richard-gurney-fact-sheet.research.md`: clear the "Sources to obtain" Bodge line

`str_replace`:

**old_string:**
```
- Drake, <em>The Book of the Indians</em>, or Bodge's <em>Soldiers in King Philip's War</em>, for the Mendon casualties of 14 July 1675.
```

**new_string:**
```
- Drake, <em>The Book of the Indians</em>, for the Mendon casualties of 14 July 1675. (Bodge, <em>Soldiers in King Philip's War</em>, now examined — see the Zachariah service note above and the [G13 companion](https://github.com/allengurney/gurney-genealogy/blob/main/research/people/g13-john-gurney-fact-sheet.research.md) for Peter; Source ID <code>bodge-soldiers-king-philips-war-1891</code>.)
```

---

## Operation 12 — raw-file disposition (local-only master)

1. Create directory `sources/media/bodge-soldiers-king-philips-war-1891/_local/`.
2. Move `sources/intake/new/soldiersinkingph00bodg.pdf` → `sources/media/bodge-soldiers-king-philips-war-1891/_local/soldiersinkingph00bodg.pdf`.
3. `new file write` — `sources/media/bodge-soldiers-king-philips-war-1891/_local/README.md`:

```markdown
# Bodge, *Soldiers in King Philip's War* (1891) — local master

`soldiersinkingph00bodg.pdf` (~27 MB) is the Internet Archive scan of the Boston University copy. Held local-only (git-ignored) because it is a large binary freely and stably available online; the repo cites the public copy instead.

- Source ID: `bodge-soldiers-king-philips-war-1891`
- Canonical public copy: https://archive.org/details/soldiersinkingph00bodg
- Gurney content (pp. 113, 114, 236; index p. 364) transcribed at `sources/corpus_supplement/bodge-soldiers-king-philips-war-1891-gurney-extracts.md`.
```

---

## Operation 13 — regenerate ID indexes

After the `data/sources.json` edit, run:

```
.\.venv\Scripts\python.exe tools\generate_id_indexes.py --write
```

This refreshes `data/indexes/source-ids.csv` and `all-ids.csv` to include `bodge-soldiers-king-philips-war-1891`.

---

## Phase 2 completion

After all operations: confirm `data/sources.json` is valid JSON; confirm no `NEW`/placeholder footnote labels remain in the G12 fact sheet and that the `#n9` / `#ref-9*` anchors resolve and are unique; prepend `**Done:** YYYY-MM-DD HH:MM PT` and move this file to `sources/intake/done/`.
