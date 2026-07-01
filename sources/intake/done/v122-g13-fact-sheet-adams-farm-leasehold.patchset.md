**Done:** 2026-06-30 16:28 PT

# v122 — G13 John Gurney fact sheet: the Adams-farm story and the dated Tyng leasehold

Phase 1 patchset, standalone, for the published fact sheet `fact-sheets/g13-john-gurney-fact-sheet.md`. Promotes the single most powerful colonial detail surfaced this thread — the 45-acre Braintree farm John Gurney leased from William Tyng (1647–1662) whose fields became the Adams family seat — to published-narrative standard. Light-touch per `.claude/rules/fact-sheets.md`: story-led, plain English, written as if known all along, Highlights kept to six bullets. New citation `n15` cites the registered source `nps-adams-nhp` (added/updated in v120).

---

## Item 1 — Highlights: trim the property bullet, add the Adams-farm bullet — PROMOTE

The "craftsman" bullet currently carries the leased-acres detail; move that to a new dedicated bullet so the two don't overlap, and add the Adams-farm story (sixth bullet; still within the 4–6 band). `str_replace`:

`old_string`:
```
  <li><strong>A craftsman, not a landed man.</strong> His New England property is mostly leasehold and grant rights spread across Weymouth, Braintree, and the Mendon frontier rather than a settled estate; he held forty-eight Braintree acres "by lease" and left goods worth only £55 14s 6d. <sup class="fn"><a href="#n9" id="ref-9">9</a></sup></li>
```
`new_string`:
```
  <li><strong>Land in town after town, on a tradesman's purse.</strong> A tailor of modest means — his goods were appraised at just £55 14s 6d — John nonetheless held close to a dozen New England parcels over his life: grant lots at Weymouth, a house and farmland of his own at Braintree, the leased Tyng farm, and frontier allotments at Billerica and Mendon. <sup class="fn"><a href="#n9" id="ref-9">9</a></sup></li>
  <li><strong>The land he farmed became the home of presidents.</strong> From 1647 until 1662 John leased a forty-five-acre Braintree farm from the Boston merchant William Tyng. A century later its northern fields became the Adams family seat and the birthplaces of Presidents John Adams and John Quincy Adams. <sup class="fn"><a href="#n15" id="ref-15">15</a></sup></li>
```

---

## Item 2 — Narrative: weave the dated leasehold and the Adams connection into the property paragraph — PROMOTE

`str_replace`:

`old_string`:
```
His land trail reads as a sequence of grant rights and leaseholds rather than an estate: lot rights at Weymouth, forty-eight Braintree acres he occupied "by lease" within the Tyng estate, a house and orchard he sold at Braintree in 1661, and a frontier interest among the proprietors of Mendon.
```
`new_string`:
```
His land trail ran through a string of grants, leaseholds, and a farm across several towns: lot rights at Weymouth, a forty-five-acre Braintree farm he leased from the merchant William Tyng from 1647 until 1662 — land whose northern fields would, a century later, become the Adams family seat at Quincy and the birthplaces of two presidents<sup class="fn"><a href="#n15" id="ref-15b">15</a></sup> — a house and orchard of his own that he sold at Braintree in 1661, and a frontier interest among the proprietors of Mendon.
```

---

## Item 3 — Citations: add note 15 (NPS Cultural Landscape Report) — PROMOTE

Insert the new citation after note 14, at the end of the citation list. `str_replace`:

`old_string`:
```
  <li id="n14">See the <a href="/fact-sheets/g12-richard-gurney-fact-sheet.html">Richard Gurney (G12) fact sheet</a>; Rigler, <em>Gurney Family from Aaron to Zuinglius</em>, Richard-2 entry, for his Weymouth residence, 1681 Freeman admission, and marriage to Rebecca Taylor. Source ID: <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-14">↩</a></li>
</ol>
```
`new_string`:
```
  <li id="n14">See the <a href="/fact-sheets/g12-richard-gurney-fact-sheet.html">Richard Gurney (G12) fact sheet</a>; Rigler, <em>Gurney Family from Aaron to Zuinglius</em>, Richard-2 entry, for his Weymouth residence, 1681 Freeman admission, and marriage to Rebecca Taylor. Source ID: <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-14">↩</a></li>
  <li id="n15">National Park Service, <em>Cultural Landscape Report, Adams National Historic Site</em>, Quincy, Massachusetts (1997), pp. 12–13 and fig. 1, "William Tyng's 45-acre farm, Braintree, 1649," drawing on the Ezekiel Sargent manuscripts (Quincy Historical Society, "Land Formerly of William Tyng"): William Tyng leased John Gurney a forty-five-acre Braintree farm in 1647 for ten years, and Gurney continued to lease it from Tyng's daughters Bethia and Mercy until 1662; the northern part of the farm later became the Adams property. The 1653 Tyng inventory of the same land is read as forty-five acres here and as forty-eight in the <em>New England Historical and Genealogical Register</em> vol. 30 (1876), p. 432. <a href="https://npshistory.com/publications/adam/clr-1997.pdf">npshistory.com</a>. Source ID: <code>nps-adams-nhp</code>. <a class="citation-back" href="#ref-15">↩</a></li>
</ol>
```

---

## Item 4 — Timeline sidebar: add the 1647 leasehold — PROMOTE

`str_replace`:

`old_string`:
```
      <tr><td>1645</td><td>Signed the petition for the new plantation at Braintree.</td></tr>
      <tr><td>1653</td><td>Deposed that he was "aged about 50."</td></tr>
```
`new_string`:
```
      <tr><td>1645</td><td>Signed the petition for the new plantation at Braintree.</td></tr>
      <tr><td>1647</td><td>Leased a Braintree farm from William Tyng — later the Adams family seat.</td></tr>
      <tr><td>1653</td><td>Deposed that he was "aged about 50."</td></tr>
```

---

## Item 5 — Highlights: drop the inaccurate "never a large property holder" clause — PROMOTE

The "trusted neighbor" bullet calls John "never a large property holder," which the leasehold/grant record contradicts (close to a dozen parcels, plus the 45-acre farm). `str_replace`:

`old_string`:
```
  <li><strong>A trusted neighbor.</strong> Though never a large property holder, John was repeatedly relied on by his Braintree neighbors — he signed the 1645 petition for the new plantation and served as a witness and appraiser for other families' estates. <sup class="fn"><a href="#n10" id="ref-10">10</a></sup></li>
```
`new_string`:
```
  <li><strong>A trusted neighbor.</strong> John was repeatedly relied on by his Braintree neighbors — he signed the 1645 petition for the new plantation and served as a witness and appraiser for other families' estates. <sup class="fn"><a href="#n10" id="ref-10">10</a></sup></li>
```

---

## Source tracking
`nps-adams-nhp` is registered and updated in v120 (URL, 1997 edition, corpus, media). No new sourceId. No new lead.

## Citation-sweep note (Phase 2)
After applying: confirm note 15's anchors resolve (`#n15` / `#ref-15` / `#ref-15b`), the Highlights count is six, and no placeholder labels remain.
