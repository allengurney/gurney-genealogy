**Done:** 2026-06-19 10:47 PT

# Patchset v103 — same-name comparators and online negatives (Phase 1)

Completes the June 2026 online lead-discovery arc by promoting the findings deferred from v102: the L-148 Norwich comparator (now resolved at transcript level), and the first-class negative/method results for L-94, L-8, and L-93. All edits are literal `str_replace`; all reuse existing sources (`fs-england-marriages-1538-1973`, `findmypast-norfolk-baptisms-index`, `familysearch-fulltext-search`), so no new `sourceId` or validation is introduced. Item 5 is a method-note edit to the FindMyPast skill (continual improvement).

---

## Item 1 — PROMOTE: L-148 Robert Gvrney × Mary Lame resolved → `research/people/g13-john-gurney-fact-sheet.research.md`

**Finding.** The Norwich "Robert Gvrney + Mary 1622" comparator resolves at transcript level: Robert Gvrney m. **Mary Lame**, 27 July 1622 at Norwich; two children traced at adjacent SW-Norwich parishes (Samuel bp 1623 St Stephen; Katherine bp 1639 St Benedict). Not a candidate (wrong groom forename; bride's maiden name Lame).

`str_replace` in `research/people/g13-john-gurney-fact-sheet.research.md`:

old_string:
```
 The single East Anglian Gurney-surname hit is **Robert Gvrney + Mary, Norwich, 1622** — not a candidate (wrong forename; a 1622 Norwich marriage cannot produce the emigrant b. c.1607–12) but a previously unlogged Norwich Gurney household with a wife named Mary; the transcript's parish field is an open one-click pull. Case file §6.1 upgraded to wildcard-verified.[^wildcard-sweep-2026-06]

## Wider Norfolk and same-name Gurney records (comparators)
```

new_string:
```
 The single East Anglian Gurney-surname hit is **Robert Gvrney + Mary, Norwich, 1622** — resolved at transcript level as **Robert Gvrney m. Mary Lame, 27 July 1622 at Norwich**, with two children traced at adjacent south-west Norwich parishes (**Samuel** bp 1623 at St Stephen; **Katherine** bp 1639 at St Benedict). It is **not a candidate** (wrong groom forename; a 1622 Norwich marriage cannot produce the emigrant b. c.1607–12, and the bride's maiden name Lame is unrelated to the emigrant's wife Mary) but stands as a documented Norwich Gurney household with a wife named Mary. Case file §6.1 upgraded to wildcard-verified.[^wildcard-sweep-2026-06][^robert-gvrney-mary-lame-2026-06]

[^robert-gvrney-mary-lame-2026-06]: Robert Gvrney m. Mary Lame, 27 July 1622, Norwich — Findmypast "England Marriages 1538-1973" transcript (IGI; parish given only as "Norwich"); children at Norwich: Samuel (bp 1623, St Stephen, father Robert) and Katherine (bp 1639, St Benedict, father Robert, mother Mary), Findmypast "Norfolk Baptisms." A SW-Norwich household; not a candidate. Source IDs: `fs-england-marriages-1538-1973`; `findmypast-norfolk-baptisms-index`.

## Wider Norfolk and same-name Gurney records (comparators)
```

---

## Item 2 — PROMOTE: L-94 Isaac Gurney — Middlesex 1666 / Suffolk file 911 not in full-text → `research/people/isaac-gurney-scituate-boston.md`

**Finding.** A June 2026 FamilySearch full-text pass does not surface the 1666 Middlesex County (Cambridge sessions) record or Suffolk file 911 for Isaac Gurney by name (the indexed Isaac/Isacke Gurney hits in the Massachusetts collections are all 18th–19th-century); recovery needs a direct image read of the specific court film.

`str_replace` in `research/people/isaac-gurney-scituate-boston.md`:

old_string:
```
3. Any later trace — court, town, or death record after June 1667. (Unknown online.)
```

new_string:
```
3. Any later trace — court, town, or death record after June 1667. (Unknown online.)
4. **Middlesex 1666 session papers and Suffolk file 911 — not recoverable via FamilySearch full-text.** A June 2026 full-text pass did not surface the 1666 Middlesex County (Cambridge sessions) record or Suffolk file 911 by name (the indexed Isaac/Isacke Gurney hits in the Massachusetts collections are all 18th–19th-century). Recovery needs a direct image read of the specific court film, not full-text discovery.
```

---

## Item 3 — PROMOTE: L-8 Francis Gurnay probate — full-text negative for the remaining jurisdictions → `research/people/g14-francis-gurney-fact-sheet.research.md`

**Finding.** With PCC negative, a June 2026 full-text pass for Francis G14's will or administration in the London Commissary and Archdeaconry of Norwich courts (c. 1646–1660) returned nothing — those manuscript probate registers are not in FamilySearch full-text, redirecting the search to the NRO Archdeaconry-of-Norwich and LMA London-Commissary probate indexes (overlaps L-124). A "Francis Gurnay" marriage at Mattishall Burgh, Norfolk surfaced incidentally (logged as L-153).

`str_replace` in `research/people/g14-francis-gurney-fact-sheet.research.md`:

old_string:
```
- Bernau found no Francis Gurney will or administration. The 1677 PCC caveat he quotes refers to Francis *the younger* of Maldon, not to Francis G14.
```

new_string:
```
- Bernau found no Francis Gurney will or administration. The 1677 PCC caveat he quotes refers to Francis *the younger* of Maldon, not to Francis G14.
- **No Francis Gurnay probate surfaces in FamilySearch full-text for the remaining jurisdictions.** With PCC negative, a June 2026 full-text pass for Francis G14's will or administration in the London Commissary and Archdeaconry of Norwich courts (the lesser-estate jurisdictions, c. 1646–1660) returned nothing — these manuscript probate registers are not in FamilySearch full-text, so the search must move to the NRO Archdeaconry-of-Norwich and LMA London-Commissary probate indexes (overlaps the L-124 ANW testator sweep). A "Francis Gurnay" marriage indexed at Mattishall Burgh, Norfolk (near East Dereham) surfaced incidentally and is logged as lead L-153.
```

---

## Item 4 — PROMOTE: L-93 Costessey April 1659 court — manor name not in transcript → `research/people/gurney-family-costessey-manorial.md`

**Finding.** A June 2026 full-text sweep of film 004389191 confirms Anthony Dobbs of Marsham recurs in the film's court material, but the April 1659 court heading does not survive the machine transcript (Latin/secretary-hand salad; only "in Burton aforesaid" recovered), so the manor name needs an image read of the 1659 court opening, not full-text.

`str_replace` in `research/people/gurney-family-costessey-manorial.md`:

old_string:
```
3. Which manor held the April 1659 court "of Anthony Dobbs of Marsham, esquire"? If not Costessey (Jernegan lords), the 1659 John Gurney senior may belong to a neighbouring manor bundled on the film. (Available online — read the film's item structure.)
```

new_string:
```
3. Which manor held the April 1659 court "of Anthony Dobbs of Marsham, esquire"? A June 2026 full-text sweep of film 004389191 confirms Anthony Dobbs of Marsham recurs in the film's court material, but the April 1659 court heading does not survive the machine transcript (it reads as Latin/secretary-hand salad — the phrase "in Burton aforesaid" is the only place token recovered), so the manor name needs an **image read** of the 1659 court opening, not full-text. If not Costessey (Jernegan lords), the 1659 John Gurney senior may belong to a neighbouring manor bundled on the film.
```

---

## Item 5 — METHOD NOTE: FindMyPast `mothersfirstname` does not bind → `.claude/skills/findmypast-record-search/SKILL.md`

**Finding.** The `mothersfirstname=` URL parameter on the FindMyPast baptisms results page does not bind — a `mothersfirstname` filter returns the full unfiltered result set. Filter by the Mother column instead. (Confirmed June 2026.) Added per the skill's continual-improvement clause.

`str_replace` in `.claude/skills/findmypast-record-search/SKILL.md`:

old_string:
```
- `page=<n>` paginates.
- `spouselastname` (marriages set) — see §3.
```

new_string:
```
- `page=<n>` paginates.
- `spouselastname` (marriages set) — see §3.
- ⚠ **`mothersfirstname` does not bind** on the baptisms results URL — a `mothersfirstname=` filter returns the full unfiltered result set (confirmed June 2026). Filter baptisms by reading the **Mother** column, or constrain via father's-first-name / year / place instead.
```

---

## Phase-2 close-out (after application)

After application, close **L-148** is already done (closed directly this turn). Leave **L-94**, **L-8**, **L-93** as **Partial** (each carries a route-limited residual: court-film image, NRO/LMA probate index, and 1659-court image read respectively).

## Notes

- The corpus supplements for the arc (`blomefield-norfolk-vol5-pp63-70-newton-flotman.md`, `suffolk-deeds-liber-xii-gurnell-dorchester.md`) and the v102 companion promotions remain the substantive layer; this patchset is the comparator/negative tail.
- L-145 (FTDNA Y-DNA scoping) remains **held** at user direction — not promoted in v102 or v103.
