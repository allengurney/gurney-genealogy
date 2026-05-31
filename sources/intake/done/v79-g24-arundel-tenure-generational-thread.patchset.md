**Done:** 2026-05-30 21:06 PT

# v79 — G24 fact sheet: the Arundel-tenure generational thread

**Scope:** Phase 2 application. A light, evidence-grounded touch to `fact-sheets/g24-john-de-gournay-iv-fact-sheet.md` that surfaces the connective thread the user flagged: the family held Harpley *of* the FitzAlan earls of Arundel (and the Warenne earls before them) — a tenurial bond present in John IV's (G24's) own generation that his son Edmund (G23) turned into active service as steward of the earl of Arundel's Norfolk estates, and that Sir John Gurney V held again in G21's generation. This is not the medieval-soldier arc; it is the generational-affinity story made explicit at its tenurial root.

This is a **single Narrative sentence-pair plus one footnote (n10)** — a light touch, not a rewrite, per `.claude/rules/fact-sheets.md` (prefer light-touch revision over stylistic churn). The active Gaunt/Arundel *service* remains correctly attributed to Edmund (G23), not to G24. Sources already registered: `hop-gurney`, `farrer-honors-knights-fees-v3-gurnay-extracts`, `blomefield-norfolk`.

---

## Item 01 — Add the Arundel-tenure thread to the G24 Narrative (`fact-sheets/g24-john-de-gournay-iv-fact-sheet.md`)

**Outcome:** promote. **Operation:** `str_replace`.

**old_string:**
```
What John IV's tenure did accomplish — in the most important sense — was to raise and launch his son Edmund into the legal career that made the family's next great transformation possible. Edmund became a lawyer of sufficient eminence to be retained as steward or joint steward of John of Gaunt's East Anglian estates and as counsel to Norwich and Bishop's Lynn (King's Lynn). Men of that calibre did not spring from nowhere; the stable, respectable gentry household John IV maintained at Harpley provided the platform for Edmund's advancement.<sup class="fn"><a href="#n8" id="ref-8b">8</a></sup>
```

**new_string:**
```
What John IV's tenure did accomplish — in the most important sense — was to raise and launch his son Edmund into the legal career that made the family's next great transformation possible. Edmund became a lawyer of sufficient eminence to be retained as steward or joint steward of John of Gaunt's East Anglian estates and as counsel to Norwich and Bishop's Lynn (King's Lynn). Men of that calibre did not spring from nowhere; the stable, respectable gentry household John IV maintained at Harpley provided the platform for Edmund's advancement.<sup class="fn"><a href="#n8" id="ref-8b">8</a></sup>

That platform rested on an older bond. The Gurneys held Harpley of the FitzAlan earls of Arundel, as they had held it of the Warenne earls before them — so John IV was, in feudal terms, the earl of Arundel's man at Harpley. In his own generation that was a matter of simple tenancy; in his son's it became something more, as Edmund was retained to run the earl's Norfolk estates as well as the Duke of Lancaster's. The same Arundel connection would pass on again to John IV's grandson Sir John Gurney V. What began under John IV as the relationship of a tenant to his lord became, in the hands of his son and grandson, an active and rewarding service — one more thread binding the family into the great affinities of late-fourteenth-century Norfolk.<sup class="fn"><a href="#n10" id="ref-10">10</a></sup>
```

---

## Item 02 — Add footnote n10 to the G24 citation list (`fact-sheets/g24-john-de-gournay-iv-fact-sheet.md`)

**Outcome:** promote. **Operation:** `str_replace` (insert before the closing `</ol>`).

**old_string:**
```
 <a class="citation-back" href="#ref-9">↩</a></li>
</ol>
```

**new_string:**
```
 <a class="citation-back" href="#ref-9">↩</a></li>
  <li id="n10">The Gurneys held the manor of Harpley of the Warenne earls and then of the FitzAlan earls of Arundel; Edmund Gournay (G23) was retained as steward of the Norfolk estates of Richard FitzAlan, earl of Arundel, "from whom the Gurneys held their manor at Harpley," and Sir John Gurney V held the same Arundel stewardship in the next generation. See the History of Parliament Online biography of Sir John Gurney (d. 1408), and, for the Harpley tenure under the Honor of Arundel, William Farrer, <em>Honors and Knights' Fees</em>, vol. 3 (1923–25). Source IDs: <code>hop-gurney</code>, <code>farrer-honors-knights-fees-v3-gurnay-extracts</code>, <code>blomefield-norfolk</code>. <a class="citation-back" href="#ref-10">↩</a></li>
</ol>
```

---

## Phase-2 follow-up (record in chat after application, not in this file)

After applying: footnote sweep (`#n10` / `#ref-10` resolve, back-link points to `#ref-10`, label matches). Prepend the `**Done:** YYYY-MM-DD HH:MM PT` stamp and move to `sources/intake/done/`. This closes the fact-sheet generational-thread work; the medieval-soldier arc's own promotions (G23/G22/G21) and the G24 companion disambiguation are in v75–v78. After all are applied, archive `sources/intake/new/gurney_medievalsoldier_results_analysis_2026-05-30_v4.xlsx` to `sources/intake/archive/`.
