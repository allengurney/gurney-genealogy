**Done:** 2026-06-14 07:18 PT

# Patchset v96 â€” Pre-Lovell Gurnay collaterals: Loddon 1373, Heigham 1434, and wider will-extract sightings

**Phase 1 prepared 2026-06-13.** Extends the existing pre-Lovell Gurnay collateral cluster on
`research/places/great-ellingham.md` (the 1454 Thomas / 1465 Joan / 1465 John of Filby analysis)
with two earlier Norwich Consistory Court wills surfaced from the NRO online catalogue, plus
four dispersed later Gurnay sightings from the Bradfer-Lawrence will-extracts sweep (the
"one-liners," recorded so they are not lost). All are unplaced collaterals, not tied to the
West Barsham direct line.

Outcome: **promote** into `research/places/great-ellingham.md`. SourceIds reuse the existing
`nro-ncc-wills-registers` (Loddon, Heigham) and `norfolk-wills-extracts-bradfer-lawrence`
(the four sightings; created in patchset v94 â€” apply v94 first). No new sourceId.

---

## Action 1 â€” extend the pre-Lovell cluster prose

`str_replace` in `research/places/great-ellingham.md` (add two paragraphs after the existing cluster paragraph):

**old_string:**
```
 Taken together, the 1454 Thomas and 1465 Joan point to a distinct central-Norfolk Gurnay presence around Great Ellingham and Deopham two to three generations before the Lovell inheritance reached the West Barsham line; their identity and any relationship to the main line are not established.
```

**new_string:**
```
 Taken together, the 1454 Thomas and 1465 Joan point to a distinct central-Norfolk Gurnay presence around Great Ellingham and Deopham two to three generations before the Lovell inheritance reached the West Barsham line; their identity and any relationship to the main line are not established.

Two further Norwich Consistory Court wills push this dispersed pre-Lovell Gurnay presence back another two generations and out to the Norwich suburbs. The earliest is the 1373 will of **John Gurney (Gernays), chaplain of Loddon, Holy Trinity** (register Heydon, 32) â€” contemporary with the direct line's Edmund Gournay (G23, d. 1387) but, as a chaplain, necessarily a collateral.[^nro-heydon-32-john-gurney-loddon-1373] The second is the 1434 will of **Alice Gurnay, widow of William Gurnay of Heigham juxta Norwich** (register Surflete, 162) â€” a named Gurnay marriage in the Norwich suburb of Heigham, three generations before the Lovell inheritance.[^nro-surflete-162-alice-gurnay-heigham-1434] Neither will text has been read yet; the catalogue gives register, folio, date, and identity. With the 1454 Thomas, the 1465 Joan of Deopham, and John of Filby, they sketch a Gurnay collateral presence threaded across south-central and eastern Norfolk â€” Loddon, Heigham, Great Ellingham, Deopham, Filby â€” from the 1370s onward, well before the West Barsham line acquired Great Ellingham.

A clean-OCR sweep of the Bradfer-Lawrence Norfolk will-abstracts adds four later, geographically dispersed Gurnay sightings of the same unplaced-collateral character, recorded here so they are not lost: a testator's "brother John Gurney(s) of Kenton" (Kenton, Suffolk) named executor, in a will abstracted under 1514â€“17; a testator's "sister Joan Gurney and her children" (1606); an "Elizabeth Gournay" among a testator's sisters (1654); and a "nephew Gourney Crowe" of East Bilney (1683), the forename Gourney itself onomastic evidence of an earlier Croweâ€“Gurney marriage. None is yet tied to the West Barsham line or to one another; they are logged as collateral sightings for future tracing.[^bradfer-collateral-oneliners]
```

## Action 2 â€” add the footnote definitions

`str_replace` in `research/places/great-ellingham.md` (append after the existing cluster footnotes):

**old_string:**
```
[^dg-filby-1465-cobald]: Daniel Gurney, *Record of the House of Gournay* (1848), Part II (Thomas Gournay II chapter, "Cotemporary" note): "John Gurney of Filby left a small legacy, in 1465, for the repair of the chapel of St. John there," citing Reg. Cobalde, f. 30 d.; Norris MSS. Source ID: `dg-rec-pt2`.
```

**new_string:**
```
[^dg-filby-1465-cobald]: Daniel Gurney, *Record of the House of Gournay* (1848), Part II (Thomas Gournay II chapter, "Cotemporary" note): "John Gurney of Filby left a small legacy, in 1465, for the repair of the chapel of St. John there," citing Reg. Cobalde, f. 30 d.; Norris MSS. Source ID: `dg-rec-pt2`.
[^nro-heydon-32-john-gurney-loddon-1373]: Norfolk Record Office, Norwich Consistory Court will register Heydon, 32, will of John Gurney (Gernays), chaplain (*cap.*) of Loddon, Holy Trinity, 1373; original withdrawn, microfilm MF/RO 137, MF 22. NRO online catalogue, [nrocatalogue.norfolk.gov.uk](https://nrocatalogue.norfolk.gov.uk/index.php/gurney-gernays-john-cap-de-lodne-holy-trinity). Source ID: `nro-ncc-wills-registers`.
[^nro-surflete-162-alice-gurnay-heigham-1434]: Norfolk Record Office, Norwich Consistory Court will register Surflete, 162, will of Alice Gurnay (Gurney), formerly wife of William Gurnay of Heigham juxta Norwich, 1434; microfilm MF 25, MF/RO 138; finding aid Norfolk Record Society vol. 16 (Aâ€“Hi). NRO online catalogue, [nrocatalogue.norfolk.gov.uk](https://nrocatalogue.norfolk.gov.uk/index.php/gurney-gurnay-alice-formerly-wife-of-william-gurnay-of-heygham-juxta-norwich). Source ID: `nro-ncc-wills-registers`.
[^bradfer-collateral-oneliners]: <em>Norfolk wills extracts, 1370â€“1763</em> (Bradfer-Lawrence collection, typescript), Gurney-variant sweep 2026-06-13: John Gurney of Kenton (film 008176838, [ark:/61903/3:1:3Q9M-CS2G-J353-5](https://www.familysearch.org/ark:/61903/3:1:3Q9M-CS2G-J353-5?view=fullText)); Joan Gurney 1606 (film 008176838, [ark:/61903/3:1:3Q9M-CS2G-J3YW-X](https://www.familysearch.org/ark:/61903/3:1:3Q9M-CS2G-J3YW-X?view=fullText)); Elizabeth Gournay 1654 (film 008480296, [ark:/61903/3:1:3Q9M-C39V-F99H-W](https://www.familysearch.org/ark:/61903/3:1:3Q9M-C39V-F99H-W?view=fullText)); Gourney Crowe 1683 (film 008480297, [ark:/61903/3:1:3Q9M-C39V-FS5R-9](https://www.familysearch.org/ark:/61903/3:1:3Q9M-C39V-FS5R-9?view=fullText)). Source ID: `norfolk-wills-extracts-bradfer-lawrence`.
```

## Source tracking

No new sourceId. `nro-ncc-wills-registers` is already in `sources.json` (used by the 1454/1465
cluster footnotes; validation exists). `norfolk-wills-extracts-bradfer-lawrence` is added by
patchset v94 (with its validation). The Loddon and Heigham will *texts* remain unpulled (leads
L-116, L-117); this patchset promotes only the catalogue-confirmed existence, identity, register,
and date.

## Phase 2 completion

After Actions 1â€“2, prepend `**Done:** YYYY-MM-DD HH:MM PT` and move this file to
`sources/intake/done/`.
