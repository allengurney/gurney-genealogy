**Done:** 2026-06-18 19:50 PT

# Patchset v101 — Gurney G13 direct-line discovery arc (Phase 1)

Bundles the promotable findings of the June 2026 multi-turn research arc on the **John Gurney
(G13) Candidate-B** question and the **direct line's Norfolk manorial geography**
(FamilySearch Full-Text + FindMyPast + Ancestry sessions). The arc's **leads** and **source
extracts** were already written directly to the repo during research (research-leads.csv;
`sources/corpus_supplement/`); this patchset promotes the **companion/places assimilations**
that are gated to Phase 2.

This is the **first patchset of the arc**. It executes the two headline promotions in full and
scopes the remaining companion assimilations to a documented v102 (see "Deferred to v102"). All
v101 items are mechanically applyable.

## Already applied directly during research (no action here — recorded for traceability)

- **Leads** (`research/future-research/research-leads.csv`): updated L-21, L-98, L-123, L-128,
  L-129, L-131, L-134, L-135, L-136, L-137, L-138, L-140; added L-139 (John × Mary first
  wife), L-141 (Lovell IPM primary corroboration). All carry the verbatim findings + arks.
- **Source extracts** (`sources/corpus_supplement/`):
  - `great-ellingham-manorial-henry-gurney-closes-2026-06.md` — **new file** (Henry Gurney Esq's
    Great Ellingham closes fossilized in the Buckenham manor-court rolls; sourceId
    `familysearch-fulltext-search`).
  - `rivett-garveston-maternal-family-2026-06.md` — Garveston register image-read subsection
    added (Packet 19: three Rivet households; sourceId `fs-england-births-christenings`).
- **Method (skills)**: `familysearch-fulltext-research` (reliable-token / parish-name /
  era-spelling / no-date-filter vectors) and `findmypast-record-search` (Ancestry collection
  URLs; Yarmouth coverage gap).
- **Paleography staging**: Packet 20 (Clement Gurney will, NCC 1631/32, images 363–365 of DGS
  008076514) briefed in `sources/intake/paleography-staging/README.md`; awaits transcription.

## Source tracking

No new `sourceId` is introduced by this patchset. The promotions cite extracts already keyed to
existing sources: `familysearch-fulltext-search` (validation file exists) and
`fs-england-births-christenings`. The Great Ellingham manorial extract is, longer-term, a
candidate for a dedicated `nro-buckenham-manorial-court-rolls` sourceId + validation if the
NRO-held Gurney-tenure rolls (L-140) are pursued; not created here because the present extract
is sourced through FamilySearch FTS under the existing sourceId.

---

## Item 1 — PROMOTE: Great Ellingham manor-court fossil of Henry Gurney Esq's closes → `research/places/great-ellingham.md`

**Finding.** The Buckenham manorial court rolls ("Lathes, Close, Castle and Buckenham Priory,
1595–1847," FamilySearch DGS 004389549/550), which carried copyhold business for land in Great
Ellingham, preserve Henry Gurney (G15)'s landholding at parcel level as a recurring boundary
abuttal: the south of the copyhold **Tenement Bovells** by Town Green ("formerly of Henry
Gurney Esqr late of Robert Morley and afterwards of Hannah Sprall"), and a close called **Lay
Close** ("formerly of Henry Gurney Esqr late of Sir Roger Potts Bart"). This corroborates the
Armstrong/Blomefield descent (Gurney → Morley/Davy/Potts) with primary manorial-court evidence
and ties two specific named parcels to G15. Verbatim recitals are in the new corpus file.

Insert a new section after the Armstrong "Berryhall divergence" paragraph.

`str_replace` in `research/places/great-ellingham.md`:

old_string:
```
**Berryhall divergence in 1525.** Armstrong notes that at the 1525 division, "Berryhall went to the heirs of William De-Grey, of Merton, in right of Christian his wife, the daughter and co-heiress of Thomas Manning" — the Berryhall manor in Great Ellingham did not come to Anthony Gurney but went to the De-Grey of Merton line via a different Manning co-heiress, ending in 1474 with William De-Grey's death.[^v71-armstrong-great-ellingham]
```

new_string:
```
**Berryhall divergence in 1525.** Armstrong notes that at the 1525 division, "Berryhall went to the heirs of William De-Grey, of Merton, in right of Christian his wife, the daughter and co-heiress of Thomas Manning" — the Berryhall manor in Great Ellingham did not come to Anthony Gurney but went to the De-Grey of Merton line via a different Manning co-heiress, ending in 1474 with William De-Grey's death.[^v71-armstrong-great-ellingham]

## Manor-court fossil of Henry Gurney Esq's closes (parcel level)

The printed antiquarian descent (Armstrong, Blomefield) is corroborated at parcel level by the manorial court rolls themselves. The Buckenham manor-court rolls ("Lathes, Close, Castle and Buckenham Priory, 1595–1847"), which carried copyhold business for land in Great Ellingham, preserve **Henry Gurney (G15)'s holding as a recurring boundary abuttal** in 18th–19th-century admissions: the south side of the copyhold **Tenement Bovells**, by Town Green, is "the lands formerly of Henry Gurney Esqr late of Robert Morley and afterwards of Hannah Sprall," and a separate close is "formerly of Henry Gurney Esqr late of Sir Roger Potts Bart, called **Lay Close**." The parcels therefore descended out of the family **Gurney → Morley (the chief lord) → Sprall/Snell** (the Tenement Bovells land) and **Gurney → Sir Roger Potts** (Lay Close) — the same Morley/Potts names Armstrong gives for the manor as a whole, now fixed to specific closes. No Gurney holder is named between G15 and a later **Joseph Gurney** admitted in 1788 (a distinct, later man), so no continuing direct-line copyhold at Great Ellingham is visible after Henry. Verbatim recitals and arks are gathered in [`sources/corpus_supplement/great-ellingham-manorial-henry-gurney-closes-2026-06.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/great-ellingham-manorial-henry-gurney-closes-2026-06.md).[^buckenham-manorial-gurney]
```

Append the footnote definition immediately before the file's existing `[^v71-armstrong-great-ellingham]:` footnote definition.

`str_replace` in `research/places/great-ellingham.md`:

old_string:
```
[^v71-armstrong-great-ellingham]: Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 8 (Norwich, 1781), Shropham Hundred — Great Ellingham capital manor + rectory mediety entries. Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_8`. Source ID: `armstrong-norfolk-1781`.
```

new_string:
```
[^buckenham-manorial-gurney]: Buckenham manorial court rolls ("Lathes, Close, Castle and Buckenham Priory, 1595–1847"), FamilySearch Full-Text Search collection "England, Norfolk, Legal," films DGS 004389549 and 004389550; boundary recitals "formerly of Henry Gurney Esqr late of Robert Morley and afterwards of Hannah Sprall" (Tenement Bovells, e.g. admissions 1751 ark `3:1:S3HT-DW22-RD`, 1813 ark `3:1:S3HT-D474-YHZ`) and "formerly of Henry Gurney Esqr late of Sir Roger Potts Bart, called Lay Close" (1787 ark `3:1:S3HT-D474-1LL`). Full extracts: `sources/corpus_supplement/great-ellingham-manorial-henry-gurney-closes-2026-06.md`. Surfaced June 2026 via a no-date-filter "Ellingham Magna" Full-Text pull. Source ID: `familysearch-fulltext-search`.
[^v71-armstrong-great-ellingham]: Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 8 (Norwich, 1781), Shropham Hundred — Great Ellingham capital manor + rectory mediety entries. Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_8`. Source ID: `armstrong-norfolk-1781`.
```

---

## Item 2 — PROMOTE: Packet 19 Garveston register (three Rivet households; burial negative) → `research/people/rivett-family-of-garveston.md`

**Finding.** The Packet 19 image read of the Garveston parish register confirms Margaret Rivet's
21 May 1586 christening at image level (father "ffrancis," mother not named) and separates the
parish's Rivet households: at least **three** household heads in the parental generation —
**Francis** (Margaret 1586, Grace 1603), **Edmund** (Elen, chr. 11 Apr 1593), and **Robert** (a
child chr. Oct 1571) — none of whose register entries names a mother. The burial section
(1561–1625) was read with **no Margaret Rivet/Gurney burial** located c. 1616–17.

`str_replace` in `research/people/rivett-family-of-garveston.md` (household count):

old_string:
```
with **Margaret Bate Rivett**
dying at Garveston in 1584 (probate) — the likely namesake.[^fs][^prob] Three miles the other
```

new_string:
```
with **Margaret Bate Rivett**
dying at Garveston in 1584 (probate) — the likely namesake.[^fs][^prob] An image read of the
register (paleography packet 19) confirms Margaret's 21 May 1586 christening as "daughter of
ffrancis" (the mother is not named) and separates the parish's Rivet households into at least
**three** in the parental generation — **Francis** (Margaret 1586, Grace 1603), **Edmund**
(Elen, chr. 11 April 1593), and **Robert** (a child chr. October 1571) — the latter two
plausibly the Edmund Rivett of the 1613–14 inventory and the Robert Rivett of the 1597
administration below.[^reg-p19] Three miles the other
```

`str_replace` in `research/people/rivett-family-of-garveston.md` (L-131 burial bullet):

old_string:
```
- L-131 — Margaret's burial c.1616–17. The first place to look is the **Garveston register
  1538–1675** (DGS 004033226, item 14) now pinned under L-128; failing that, the East Dereham
  register (worked in the John Gurney case-file paleography).
```

new_string:
```
- L-131 — Margaret's burial c.1616–17. The **Garveston register** burial section (1561–1625)
  has now been read (paleography packet 19) with **no Margaret Rivet or Margaret Gurney burial**
  located — a per-pass negative, not proof of absence. So if she died c.1616–17 her burial was
  most likely elsewhere; the **East Dereham register** (worked in the John Gurney case-file
  paleography) is the next test, consistent with the family living at East Dereham when she died.
```

Append the footnote definition before the existing `[^fs]:` footnote definition.

`str_replace` in `research/people/rivett-family-of-garveston.md`:

old_string:
```
[^fs]: FamilySearch, "England, Births and Christenings, 1538–1975," Margaret Rivet christening 21 May 1586, Garveston, Norfolk, parents Francis Rivet; Grace Rivet christening 4 September 1603, parents Francis Rivet. Source ID: `fs-england-births-christenings`. Dossier: `sources/corpus_supplement/rivett-garveston-maternal-family-2026-06.md`.
```

new_string:
```
[^reg-p19]: Garveston parish register, Norfolk Record Office, FamilySearch DGS 004033226 item 14; image-read transcription (paleography packet 19, June 2026): Margaret Rivet christening "the xxjth of May" 1586, father "ffrancis," mother not named (image 34); Elen Rivet christening 11 April 1593, father Edmund (image 36); a Rivet child of Robert christened October 1571, forename uncertain (images 26/27). Burial section 1561–1625 read with no Margaret Rivet/Gurney burial found. Full extracts: `sources/corpus_supplement/rivett-garveston-maternal-family-2026-06.md`. Source ID: `fs-england-births-christenings`.
[^fs]: FamilySearch, "England, Births and Christenings, 1538–1975," Margaret Rivet christening 21 May 1586, Garveston, Norfolk, parents Francis Rivet; Grace Rivet christening 4 September 1603, parents Francis Rivet. Source ID: `fs-england-births-christenings`. Dossier: `sources/corpus_supplement/rivett-garveston-maternal-family-2026-06.md`.
```

---

## Deferred to v102 (companion assimilations — findings established, targets named; require reading each companion to author verbatim `str_replace`)

These are not half-operations: the findings are committed to leads/corpus already; v102 will Read
each target companion and author the literal edits. Listed so the arc's plan is explicit.

1. **`research/people/g13-john-gurney-fact-sheet.research.md`** — (a) L-137: the Great Yarmouth
   Edward × Anne candidate is rejected on chronology (first child 1629 ⇒ marriage ~1627 ⇒ birth
   ~1600–05, a decade before our Edward bp c.1611), closing the residual sibling candidate;
   (b) L-136: paternal-uncle fostering net cast, no indexed placement, redirect to West
   Barsham/Great Ellingham manorial + probate; (c) L-138: Clement Gurney will located (packet 20);
   (d) L-98: **Michael Gurney, supervisor of a 1563 East Dereham will** (Baxter Row) + the
   recurring 16th–19th-c. East Dereham "Michael" Gurney — strengthens a humble-East-Dereham
   origin frame over the West-Barsham-gentry descent.
2. **`research/people/g14-francis-gurney-fact-sheet.research.md`** — L-135: the Browning family
   placed at Maldon, Essex as linendrapers/merchants ("Thomas Browning, linendraper," burgess
   1680–87); the c.1617 Francis × Anne Browning marriage absent from the FMP Norfolk set.
3. **`research/people/g15-henry-gurney-fact-sheet.research.md`** — the Great Ellingham manor-court
   fossil (Item 1) as primary manorial confirmation of G15's specific closes (Lay Close; Tenement
   Bovells parcel).
4. **`research/people/g17-anthony-gurney-fact-sheet.research.md`** — L-141: the printed Sussex
   Inquisitions abstract of Sir Thomas Lovell's 1524 IPM naming "Margaret Gurney, wife of Anthony
   Gurney, esq., aged 26+" as coheir — primary corroboration of Margaret Lovell's parentage.
5. **`research/topics/` or `research/places/west-barsham.md`** — L-134: the Visitation of Norfolk
   1563 (Harvey) pedigree giving Constance Gurney of (West) Barsham m. Robert Blundeville of
   Newton Flotman (dating G19 c. 1460–1500).

No `reject` outcomes in this arc — every worked item produced a promotable finding or a recorded
negative.
