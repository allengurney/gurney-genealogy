**Done:** 2026-05-30 21:06 PT

# v77 — Medieval-soldier discovery: G23 Edmund fact-sheet promotion

**Scope:** Phase 2 application. Closes the promotion stage of the 2026-05-30 medieval-soldier arc (v75 topic file + sources; v76 companion cross-links). Promotes the Walker finding — Edmund Gournay as a retained member of John of Gaunt's East Anglian affinity, with a fee from St Benet's Holme abbey — into `fact-sheets/g23-edmund-gurney-fact-sheet.md`. The evidence and full apparatus already live in the G23 companion (v76 Item 01) and the topic file; this is a promotion, not new research.

The edit *deepens the existing Gaunt material* (Highlights bullet 2 and the Narrative Gaunt paragraph) rather than adding a sixth Highlights bullet, keeping the bullet count at five per `.claude/rules/fact-sheets.md`. New footnote **n16** (`walker-lancastrian-affinity-1361-1399`, registered in v75); no renumbering.

**Deferred / optional — G29 Sir Matthew:** the banneret service rows + Trevet kinship promotion to `fact-sheets/g29-matthew-de-gournay-fact-sheet.md` is held pending user confirmation (collateral, secondary). If wanted, it becomes v78; the evidence already lands in `research/places/somerset-gournay-collateral.md` via v75.

---

## Item 01 — Deepen the Gaunt Highlights bullet (`fact-sheets/g23-edmund-gurney-fact-sheet.md`)

**Outcome:** promote. **Operation:** `str_replace`.

**old_string:**
```
  <li><strong>Steward of John of Gaunt's East Anglian estates, 1372–1387.</strong> John of Gaunt — Duke of Lancaster, father of the future Henry IV, and the most powerful man in England after the king — retained Edmund as his steward for the East Anglian portion of his vast holdings. Edmund was not merely a local gentleman; he was a trusted officer of the most powerful magnate in the realm, managing revenues and legal affairs on a scale that dwarfed anything the Norfolk gentry typically handled. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></li>
```

**new_string:**
```
  <li><strong>Steward of John of Gaunt's East Anglian estates, 1372–1387.</strong> John of Gaunt — Duke of Lancaster, father of the future Henry IV, and the most powerful man in England after the king — retained Edmund as his steward for the East Anglian portion of his vast holdings. Edmund was not merely a local gentleman; he was a trusted officer of the most powerful magnate in the realm, managing revenues and legal affairs on a scale that dwarfed anything the Norfolk gentry typically handled. He belonged to the tight circle of lawyers and stewards through whom the Duke ran Lancastrian Norfolk, and like them he gathered a web of other retainers — drawing a fee even from the great Broadland abbey of St Benet's Holme. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup><sup class="fn"><a href="#n16" id="ref-16">16</a></sup></li>
```

---

## Item 02 — Add the named affinity cohort to the Narrative (`fact-sheets/g23-edmund-gurney-fact-sheet.md`)

**Outcome:** promote. **Operation:** `str_replace`.

**old_string:**
```
Edmund's Gaunt connection is the key to his leap in status. Gaunt was not just another noble employer: in the 1370s and 1380s he was the royal uncle whose lands, household, and political reach made him one of the strongest forces in England. Edmund's job was to help make that East Anglian machinery work.<sup class="fn"><a href="#n7" id="ref-7c">7</a></sup>
```

**new_string:**
```
Edmund's Gaunt connection is the key to his leap in status. Gaunt was not just another noble employer: in the 1370s and 1380s he was the royal uncle whose lands, household, and political reach made him one of the strongest forces in England. Edmund's job was to help make that East Anglian machinery work, shoulder to shoulder with the other men who staffed it — John Winter, Robert Cayley, Thomas Pinchbeck, John Methwold, and his fellow Norwich counsel Edmund de Clipesby — the interlocking professional class on whom the Duke, the bishops, and the towns alike depended.<sup class="fn"><a href="#n7" id="ref-7c">7</a></sup><sup class="fn"><a href="#n16" id="ref-16b">16</a></sup>
```

---

## Item 03 — Add footnote n16 to the citation list (`fact-sheets/g23-edmund-gurney-fact-sheet.md`)

**Outcome:** promote. **Operation:** `str_replace` (insert before the closing `</ol>`).

**old_string:**
```
  <li id="n15">Daniel Gurney, <em>Supplement to the Record of the House of Gournay</em> (1858), Note 118, pp. 789–791, full Latin copy of Edmund Gurnay's will from Harl. MSS. 10, fol. 144 / pencil 148, copied from the decayed Registrum Harsyke. Names Katherine his wife, John his son, Osbert de Mundeford, and Thomas Kempe as executors; specifies thirteen paupers in white vestments holding thirteen torches around the body; and includes the restitution clause for wrongfully detained, extorted, or disseised property. Source ID: <code>dg-rec-supp</code>. <a class="citation-back" href="#ref-15">↩</a></li>
</ol>
```

**new_string:**
```
  <li id="n15">Daniel Gurney, <em>Supplement to the Record of the House of Gournay</em> (1858), Note 118, pp. 789–791, full Latin copy of Edmund Gurnay's will from Harl. MSS. 10, fol. 144 / pencil 148, copied from the decayed Registrum Harsyke. Names Katherine his wife, John his son, Osbert de Mundeford, and Thomas Kempe as executors; specifies thirteen paupers in white vestments holding thirteen torches around the body; and includes the restitution clause for wrongfully detained, extorted, or disseised property. Source ID: <code>dg-rec-supp</code>. <a class="citation-back" href="#ref-15">↩</a></li>
  <li id="n16">Simon Walker, <em>The Lancastrian Affinity 1361–1399</em>, Oxford Historical Monographs (Oxford: Clarendon Press, 1990), note 19: Edmund Gournay was "the principal legal adviser to the burgesses of Lynn" and, with Edmund Clippesby, "took fees from the abbey of St. Benet's, Holme," bracketed among John of Gaunt's retained East Anglian men with John Winter, Robert Cayley, Thomas Pinchbeck, and John Methwold. Walker cites Staffordshire Record Office D.641/1/2/4 m.4; The National Archives E.403/478 m.16; Historical Manuscripts Commission, <em>MSS of the Corporations of Southampton and King's Lynn</em> (1887), pp. 221–2; Calendar of Patent Rolls 1381–5, p. 380; KB 9/166/1 m.69. Source ID: <code>walker-lancastrian-affinity-1361-1399</code>. <a class="citation-back" href="#ref-16">↩</a></li>
</ol>
```

---

## Phase-2 follow-up (record in chat after application, not in this file)

After applying: confirm the footnote sweep — `#n16` / `#ref-16` / `#ref-16b` anchors resolve, the n16 back-link points to `#ref-16`, the visible "16" labels match. Prepend the `**Done:** YYYY-MM-DD HH:MM PT` stamp and move this file to `sources/intake/done/`. If the user approves the G29 Sir Matthew promotion, that is v78; otherwise the arc closes here and the `gurney_medievalsoldier_results_analysis_2026-05-30_v4.xlsx` workbook is archived from `sources/intake/new/` to `sources/intake/archive/`.
