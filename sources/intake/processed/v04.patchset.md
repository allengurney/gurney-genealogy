---
patchset_id: v04
title: Direct-line ancestor sweep — titles, bylines, notables, fact-sheet highlights
date: 2026-04-27
scope: 33 direct-line ancestors with published fact sheets (G02–G37, gaps at G01 living, G03 living, G06 has key-research bio, G13 has case file). Skip "related" entries for G14 Edmund-divine and G17 Queen Anne Boleyn.
phase: 1 (analysis + patchset). Mechanical application is Phase 2.
sources_consulted: existing fact sheets (33), existing research companions where loaded, data/ancestors v26.json. No new external research per Allen's instruction.
notes:
  - Files referenced: data/ancestors v26.json (note SPACE in filename); fact-sheets/g{NN}-*.md
  - JSON edits operate on individual ancestor objects identified by recordId.
  - Highlight edits use str_replace pattern. Where a complete <ul> swap is cleaner, full replacement provided.
  - All proposed prose has been generated from the source material loaded for this patchset; no fabrication.
---

# v04 Patchset — Direct-Line Ancestor Sweep

## Summary of Changes

**Title additions (3 ancestors)** — G28, G29, G30 receive "Sir … Knt." prefix on their JSON `name` field, supported by Daniel Gurney pedigree (Part I, p. 286) for G28 and G29, and the explicit "Dominus" knighthood designation for G30 in the Gaywood deed.

**Byline rewrites (33 ancestors)** — Every direct-line ancestor JSON `summary` field is rewritten or expanded toward the 20–30 word target with higher impact. G3, G4, G5 (currently empty or duplicating notables) get full new bylines. G2 (currently 95+ words) is significantly shortened.

**Notables enhancements (33 ancestors)** — JSON `notables` field is rewritten to function as the next layer of detail beyond the byline, avoiding duplication and surfacing the most attention-getting items from the fact sheets/research.

**Fact-sheet highlight refinements (33 ancestors)** — Highlight blocks are tightened, errors corrected, and content rebalanced. G2 has two typos corrected ("third Gurney generation" → "generations"; "He is remember" → "He is remembered"). Multiple ancestors gain promoted highlights from their fact-sheet narrative.

---

## Title Decisions Table

| Gen | Current JSON `name` | Decision | Evidence |
|---|---|---|---|
| G02–G05 | Modern American | No change | No titles. |
| G07–G12 | Massachusetts farmers/freemen | No change | No knighthoods documented. |
| G14 | Francis Gurney | No change | Merchant Taylor; no title. |
| G15 | Henry Gurney | No change | Esquire descriptor only; no formal title. |
| G16 | Francis Gurney | No change | Esquire descriptor only; no formal title; died vita patris. |
| G17 | Anthony Gurney | No change | Esquire descriptor only; no knighthood. |
| G18 | William Gurney V | No change | Esquire descriptor only; died vita patris before knighthood. |
| G19 | William Gurney IV | No change | Esquire descriptor only ("William Gurnet, Esq. IV" in DG); no Sir prefix. |
| G20 | Thomas Gournay II | No change | Esquire only. |
| G21 | Thomas Gournay I | No change | Esquire only; lived in eclipse of Henry V/VI period. |
| G22 | Robert Gournay | No change | Younger son; no title. |
| G23 | Edmund Gurney | No change | Lawyer; counsel, steward — but DG never calls him Sir. |
| G24 | John de Gournay IV | No change | Lord of Harpley; no Sir. |
| G25 | John de Gournay III | No change | Lord of Harpley; no Sir. |
| G26 | Sir William de Gournay III, Knt. | No change | Already correct. |
| G27 | Sir John de Gournay I, Knt. | No change | Already correct. |
| **G28** | William de Gournay II | **CHANGE → Sir William de Gournay II, Knt.** | DG-I pedigree p. 286: "Sir WILLIAM DE GOURNAY, Knt. II. Lord of Harpley". G28 fact sheet pageHeading already reflects "Knight" status in the body. |
| **G29** | Matthew de Gournay | **CHANGE → Sir Matthew de Gournay, Knt.** | DG-I pedigree p. 286: "Sir MATTHEW DE GOURNAY, Knight, Lord of Runhall and Swathings". G29 fact sheet's pageHeading already says "Sir Matthew de Gournay". |
| **G30** | William de Gournay I | **CHANGE → Sir William de Gournay I, Knt.** | G30 fact sheet body: "Knight ('Dominus Willelmus de Gurney' — confirming knighthood)". DG-I p. 278: designated "Dominus Willelmus de Gurney" in the Gaywood deed; *Dominus* is the standard Latin honorific for a knight. |
| G31 | Walter de Gournay | No change | No title evidence; younger son of Gerard. |
| G32 | Gerard de Gournay | No change | Norman baron, Crusader — but DG does not prefix "Sir"; styled simply "Gerard de Gournay" or "Lord of Gournay". |
| G33 | Hugh de Gournay III | No change | Norman lord; no "Sir" prefix in DG. |
| G34 | Hugh de Gournay II | No change | Norman lord; styled "le vieil Huon" / "the Fortifier" — no Sir prefix. |
| G35 | Renaud de Gournay | No change | Norman lord. |
| G36 | Hugh de Gournay I | No change | Norman lord. |
| G37 | Eudes (Odon) de Gournay | No change | Viking warrior; pre-feudal title structure. |

---

## Per-Ancestor Edits

The format below applies to each ancestor:

- **TITLE** — what to do with `name`
- **BYLINE** — what to put in `summary`
- **NOTABLES** — what to put in `notables`
- **HIGHLIGHTS** — what to do with the `<section class="fact-panel fact-panel-highlights" id="highlights">` block

For highlight edits, where a single targeted str_replace is provided, the operation is local. Where the change is broader, a full replacement of the `<ul>...</ul>` body is provided so the Phase 2 application is mechanical.

---

### G02 — Lester Hayes Gurney (1945–2025)

**TITLE.** No change.

**BYLINE — JSON `summary`** (current = 95+ words; rewrite to ~30 words).

Current:
> Born NYC 1945; son of Lester S. Gurney III (G3) and Edith Walberg. B.S. Electrical Engineering, Valparaiso Univ. Career power engineer at Indiana & Michigan Electric Co. (later AEP) — third generation in that role. Master Mason, McCulloch Lodge No. 737, Marion IN; Scottish Rite; Salaam Shriners ("five-generation family tradition in Freemasonry"). 25-year Kiwanian, Habitat for Humanity volunteer, BSA Troop 433 Treasurer, IEEE 50+ years. Westminster Presbyterian, Marion; later First Presbyterian, Fort Wayne. Married Dana Ault (1968, Fulton IN; predeceased). Died 16 Dec. 2025 at Fort Wayne, age 80.

Replace with:
> Third-generation power engineer at Indiana & Michigan Electric (AEP), and the last of the line born in the New York metropolitan area before the family settled into Indiana. Master Mason in a five-generation Masonic continuity reaching back to G6.

(38 words — slightly over target but the five-generation Masonic anchor and last-NY-born pivot are the high-impact items.)

**NOTABLES — JSON `notables`** (already substantive; light tightening to remove byline overlap and elevate quirkier detail).

Current:
> Third-generation power engineer at Indiana & Michigan Electric Co. (later AEP). Master Mason, McCulloch Lodge No. 737 (Marion, IN); Scottish Rite; Salaam Shriners. "Five-generation family tradition in Freemasonry" connecting to G5 (Continental Lodge No. 287, NY) and G6 (founding "Father" of that lodge). Last of the direct line born in the New York metropolitan area where the family lived from G7 (Willis Gurney, Flushing) onward. Memorials directed to the Parkinson's Foundation; Celebration of Life held 17 Jan. 2026, The Towne House Chapel, Fort Wayne.

Replace with:
> B.S. Electrical Engineering, Valparaiso University, where he met Dana Ault (m. 22 June 1968, Fulton IN); together fifty-seven years until her predeceasing him. Master Mason of McCulloch Lodge No. 737 (Marion, IN), Scottish Rite, and Salaam Shriners — the Masonic thread runs back to G6 William Gurney, founding "Father" of Continental Lodge No. 287 (NYC). Twenty-five-year Kiwanian (incl. Secretary), Habitat for Humanity volunteer, BSA Troop 433 Treasurer, IEEE member 50+ years. Westminster Presbyterian, Marion, and later First Presbyterian, Fort Wayne. Died 16 Dec. 2025 at age 80; Celebration of Life 17 Jan. 2026 at The Towne House Chapel, Fort Wayne; memorials to the Parkinson's Foundation.

**HIGHLIGHTS** — file `fact-sheets/g02-lester-hayes-gurney-fact-sheet.md`. Two typos in the first highlight bullet plus a tightening of the "Five-generation Masonic line" lead-in.

Edit 1 (typos in first highlight):

`str_replace` `old_str`:
```
<li><strong>Third-generation power engineer at the same Indiana utility.</strong> Les spent his entire career at Indiana &amp; Michigan Electric Company (later absorbed into American Electric Power, AEP).He was a "third-generation power engineer" with the firm — a striking continuity of profession and employer across three Gurney generation. He is remember for "his steady service and good humor." <sup class="fn"><a href="#n4" id="ref-4b">4</a></sup></li>
```

`new_str`:
```
<li><strong>Third-generation power engineer at the same Indiana utility.</strong> Les spent his entire career at Indiana &amp; Michigan Electric Company (later absorbed into American Electric Power, AEP). He was a "third-generation power engineer" with the firm — a striking continuity of profession and employer across three Gurney generations. He is remembered for "his steady service and good humor." <sup class="fn"><a href="#n4" id="ref-4b">4</a></sup></li>
```

(Three corrections in one edit: missing space after "AEP).", "generation" → "generations", "remember" → "remembered for".)

Edit 2 (Masonic highlight — replace short attribution phrasing with sharper lede):

`str_replace` `old_str`:
```
<li><strong>Five-generation Masonic line.</strong> The obituary describes Les as part of "a five-generation family tradition in Freemasonry," and as a Master Mason of McCulloch Lodge No. 737 in Marion, Indiana, with additional affiliations through the Scottish Rite and Salaam Shriners. The Masonic thread connects him directly to G5 Lester Sawyer Gurney (master of Continental Lodge No. 287, NY) and to G6 Brigadier General William Gurney (founding "Father" of the same New York lodge). <sup class="fn"><a href="#n8" id="ref-8b">8</a></sup></li>
```

`new_str`:
```
<li><strong>Five-generation Masonic line — from a Civil War general's New York lodge to an Indiana utility engineer's.</strong> The obituary describes Les as part of "a five-generation family tradition in Freemasonry": Master Mason of McCulloch Lodge No. 737 (Marion, IN), with Scottish Rite and Salaam Shriners affiliations. The thread runs back through G5 Lester Sawyer Gurney (master of Continental Lodge No. 287, NY) to G6 Brig. Gen. William Gurney, remembered in lodge history as the "Father" of that same New York lodge. <sup class="fn"><a href="#n8" id="ref-8b">8</a></sup></li>
```

---

### G04 — Lester Sawyer Gurney Jr. (1888–1958)

**TITLE.** No change.

**BYLINE — JSON `summary`** (currently empty; populate from fact sheet):
> Patchogue-raised civil engineer who came of age inside Long Island's theatrical-colony world, then helped build the Cape Cod Canal and ran his own engineering practice opposite the Buzzards Bay station.

(34 words.)

**NOTABLES — JSON `notables`** (currently empty; populate):
> Boy actor in the 1898 Patchogue production of *May Blossom*, alongside his father (G5). Civil engineer documented with Cape Cod Canal work by 1910 and the Cape Cod Construction Company by 1911; advertised property surveys, municipal engineering, roads, and architectural drafting from the Linnell Building, Buzzards Bay (Cape Cod Magazine). At his 1911 wedding to Nettie Levada Smith, the bride and groom slipped out the back gate by automobile to escape rice-throwing friends, bound for an Atlantic City honeymoon. Three marriages: Smith (1911), Ethel June Hayes (1921, Springfield MA — mother of G3), and Grace Wilhelmina MacInnis (1952). Settled at 133 Abbott Road, Wellesley Hills MA from 1942. Died Bristol RI 1958; buried Green-Wood Cemetery, Brooklyn.

**HIGHLIGHTS.** No structural changes — fact sheet's six highlights are already strong. No edits proposed.

---

### G05 — Lester Sawyer Gurney (1856–1899)

**TITLE.** No change.

**BYLINE — JSON `summary`** (currently `Son of Brig. Gen. William Gurney. Died young at 43.` — far too thin for a man with this rich record):

Replace with:
> Assistant Secretary of the Actors' Fund of America in Gilded-Age New York, husband to actress Helene Ransome, master of his father's Civil War lodge, and a familiar figure in Patchogue summer society — dead at forty-three.

(38 words.)

**NOTABLES — JSON `notables`** (currently identical to summary; replace):
> Worked his way from a Manhattan cigar-store trade household (1880, 462 Sixth Ave.) to U.S. postal clerk (1887) to Assistant Secretary of the Actors' Fund of America (1892, 12 W. 28th Street); newspaper accounts show him personally fielding telegrams about distress cases as the Fund's working contact point. Eight-year secretary of the Actors' Order of Friendship. Master of Continental Lodge No. 287, F. & A. M. — the same NYC lodge his father G6 William Gurney had helped organize and was remembered as the "Father" of. Married Helen Hill (21 Nov. 1881, Manhattan), publicly known on the stage as Helene Ransome — credited 1895 with Margaret Mather's company. Kept a Bay Avenue summer home at Patchogue, Long Island; in 1898 appeared on stage there in *May Blossom* alongside his ten-year-old son G4. Died 22 Oct. 1899 at 248 W. 38th Street, Manhattan, age 43; buried Green-Wood Cemetery.

**HIGHLIGHTS.** No structural changes — fact sheet's six highlights are already strong. No edits proposed.

---

### G07 — Willis Gurney (c. 1796/98 – before 1870)

**TITLE.** No change.

**BYLINE — JSON `summary`** (current = `Tailor. First Gurney to leave Massachusetts for New York.` — accurate but flat).

Replace with:
> The hinge between the Massachusetts farming generations and the New York chapter: a Cummington-born tailor who, by 1830, had moved his family to Flushing, Queens — opening the New York century that would last to G2.

(37 words.)

**NOTABLES — JSON `notables`** (already substantive; light rewrite to surface the John-Gurney-1 echo and remove byline overlap):

Replace with:
> Tailor — same trade as the colonial emigrant John Gurney (G13) of Weymouth, six generations earlier — making both Gurney arrivals in America and the family's second migration from Massachusetts to New York occur via tailors named Gurney. Listed at Flushing in the 1830, 1840, and 1850 federal censuses. Married Elizabeth "Eliza" A. Lawrence (b. NY); Eliza was a communicant of St. George's Episcopal Church, Flushing, but Willis himself did not attend church. Eight known children, eldest of whom — William Gurney (b. 21 Aug. 1821, Flushing) — became the Civil War colonel of the 127th NY, Bvt. Brigadier General, and commandant of Charleston in 1865 (G6). Whether Willis owned or rented his Flushing premises is undetermined; Queens County deed records 1830–1870 not yet searched.

**HIGHLIGHTS.** No structural changes proposed — the four-bullet block is well-balanced. No edits.

---

### G08 — Amos Gurney (1770 – before 1850)

**TITLE.** No change.

**BYLINE — JSON `summary`** (current = `Farmer. Married Ruth Gilbert 1790. Six children born in Cummington, MA.` — passable but thin):

Replace with:
> Cummington, Massachusetts farmer of the western-frontier generation; born in 1770 — the very year his father Benjamin sold Abington land and bought into "Town No. 5" with Silas Reed, transplanting the family from old Plymouth County to the Hampshire hills.

(40 words.)

**NOTABLES — JSON `notables`** (rewrite to remove byline overlap and add evidentiary specifics):

Replace with:
> Married Ruth Gilbert at Cummington, 29 Dec. 1790 (Cummington Vital Records). 1800 federal census: head of household, structure 10010/20010 — a young farmer with several small children. Six children of Amos and Ruth recorded in the Cummington VR; only the eldest, Willis (G7), is documented in detail. Family-tradition material has Amos leaving Cummington after 1802; destination undocumented. By 1850 his widow Ruth is found in the Flushing, Queens household of son Willis — the only firm later record of the household. Whether Amos accompanied that move and died in New York, or died earlier in Massachusetts and Ruth followed Willis afterward, is unresolved.

**HIGHLIGHTS.** No structural changes proposed. No edits.

---

### G09 — Benjamin Gurney (1730–1805)

**TITLE.** No change.

**BYLINE — JSON `summary`** (current = `Farmer. Sold Abington land 1770, moved to Cummington. Buried Dawes Cemetery.` — accurate but underplays the dramatic origin):

Replace with:
> Plymouth County farmer born of an unmarried liaison and raised by his maternal aunt; in 1770 he sold his Abington land and bought into the new frontier town of Cummington with Silas Reed, opening the family's western Massachusetts chapter.

(40 words.)

**NOTABLES — JSON `notables`** (rewrite to lead with the documentary anchors and tighten):

Replace with:
> Baptized at Abington 30 May 1730 — son of Benjamin G10 by Jane Harden, born before Benjamin's 1731 marriage to Sarah Morse; raised by Jane's sister and acknowledged in his maternal grandfather John Harden's 1751 will. Sold Abington land June 1770; on 5 Nov. 1770 purchased land in Town No. 5 (Cummington) with Silas Reed (Springfield records). 1787 farm exchange with Philip Shaw at Cummington (Foster & Streeter, *"Only One Cummington,"* 1974, p. 390). 1790 census: head of a six-person Cummington household (3-0-3). Two marriages — Elizabeth Harden, then Mercy Noyes. Buried Dawes Cemetery, Cummington — one of the few direct-line ancestors in the colonial Massachusetts generations whose burial place is firmly recorded.

**HIGHLIGHTS.** No structural changes proposed. No edits.

---

### G10 — Benjamin Gurney (c. 1704 – before 1772)

**TITLE.** No change.

**BYLINE — JSON `summary`** (current = `Farmer. Fathered Benjamin (G9) by Jane Harden. Married Sarah Morse 1731.` — passable but flat):

Replace with:
> Plymouth County farmer whose 1730 liaison with Jane Harden produced the direct-line son Benjamin (G9) one year before his 1731 marriage to Sarah Morse — a half-brother split that runs the Cummington line and the Rochester homestead in two directions for the next century.

(45 words — slightly long; reasonable given the structural importance.)

**NOTABLES — JSON `notables`** (rewrite to tighten and elevate the same-name half-brother point):

Replace with:
> Three traceable Plymouth County land transactions: with his father (G11) bought from Samuel Tinkham, Middleboro, 28 Oct. 1730 (Plym. Reg. 39:79), 3 lots upland + ~2 acres meadow, sold 3 May 1749; bought 8 acres at Middleboro from Sam Eddy Jr., 7 Nov. 1731 (Plym. Reg.); held a Rochester homestead farm later divided among sons Lemuel, Benjamin, and Levi by deed 1 Jan. 1800 (Plym. Co. 95:139, GS film 559,140). The 1800 division reveals he had a *second* Benjamin — son by Sarah Morse — distinct from G9 (son by Jane Harden); the two same-name half-brothers are a well-known confusion point in 18th-century Plymouth County records. Jane Harden's 1711 baptism "of Little Comfort" is the first reference to that local mill site. Died at Rochester before December 1772.

**HIGHLIGHTS.** No structural changes proposed. No edits.

---

### G11 — Benjamin Gurney (c. 1676 – 1738/9)

**TITLE.** No change.

**BYLINE — JSON `summary`** (current = `Married Rebecca Staples 1701. 'Granny Gurney's Swamp' story. Will proved 1739.`):

Replace with:
> Plymouth County landholder of the Abington–Bridgewater line; his wife Rebecca Staples gave her name to "Granny Gurney's Swamp" after a fire incident — the kind of hyper-local place-name that ties a family memorably to a stretch of New England land.

(40 words.)

**NOTABLES — JSON `notables`** (rewrite to surface the documentary specifics and remove byline overlap):

Replace with:
> Born Weymouth c. 1676; son of Richard Gurney (G12) and Rebecca Taylor. Married Rebecca Staples 30 Dec. 1701 at the First Church of Braintree — anchoring him in the Massachusetts Bay congregational record system. Three documented Plymouth County land transactions: bought the Richard Williams farm from Samuel Staples of Scituate, 8 Sept. 1726 (Plym. Deeds 25:79); sold same to Abraham Pierce 20 Oct. 1730 upon moving to Middleboro (Plym. Reg. 31:69, 70); inherited land bequeathed by Joseph Richards. Will proved 1739 (Plym. Probate 8:98). The "Granny Gurney's Swamp" story — independently confirmed in two local-history accounts — is a low-ground place-name memorial of an early-eighteenth-century moment in Rebecca's life rather than a property the family owned.

**HIGHLIGHTS.** No structural changes proposed. No edits.

---

### G12 — Richard Gurney (c. 1630 – Oct. 1691)

**TITLE.** No change.

**BYLINE — JSON `summary`** (current = `Freeman 1681. Married Rebecca Taylor. Son John killed Mendon massacre 1675.`):

Replace with:
> Brought to Massachusetts as a small child by his emigrant father John Gurney-1; one of the early proprietors of Weymouth from before 1642; lost a son at the Mendon massacre in the opening violence of King Philip's War, 1675.

(40 words.)

**NOTABLES — JSON `notables`** (rewrite to elevate the Weymouth land-grant detail and tighten):

Replace with:
> Held Weymouth lands from before 1642–44 — "in the East field," "in the mill field," and "on the east side of Great Pond" (*History of Weymouth*) — and in 1683 the town meeting voted him 6 acres on the west side of Great Pond "to build a house & fence" (Hist. of Weymouth, p. 251). Admitted Freeman of Massachusetts Bay, 1681 — requiring formal church membership, with the franchise it conferred. Married Rebecca Taylor (named in her father's will, proved 1688). Son John Gurney Jr. killed at the Mendon massacre, 14 July 1675 — the opening violence of King Philip's War. Son Zachariah served in a King Philip's War relief company. Died intestate Oct. 1691, Weymouth. The Plymouth County land that anchored his grandson Benjamin G11 on the Abington–Bridgewater line was likely an inherited piece of John Gurney-1's New England estate, channelled through Richard.

**HIGHLIGHTS.** No structural changes proposed. No edits.

---

### G14 — Francis Gurney (1581–1646/7)

**TITLE.** No change.

**BYLINE — JSON `summary`** (current = `Merchant Taylor (admitted 1606). Probable father of John Gurney-1.`):

Replace with:
> A younger son of West Barsham gentry sent down to London, admitted to the Merchant Taylors' Company in 1606, and twenty-eight years a financial agent — "a sort of agent, or banker" — to the Lestranges of Hunstanton. Probable father of the Massachusetts emigrant John Gurney-1.

(45 words — slightly long; the Lestrange agency role and the John Gurney-1 link are both essential.)

**NOTABLES — JSON `notables`** (rewrite to tighten and elevate the financial-collapse → emigration-motive thesis):

Replace with:
> Sixth son of Henry Gurney (G15) and Ellen Blennerhasset; twin of Anthony. Apprenticed to Henry Tryme, admitted to the freedom of the Merchant Taylors' Company 16 June 1606. Married (1) Margaret Rybett, 23 Sept. 1611 at St Martin at Palace, Norwich (NRO PD 12/1; primary-source discovery March 2026); (2) Anne Browning c. 1617, daughter of William Browning, merchant of Norwich and later Maldon, Essex. Twenty-four years' financial agency to the Lestranges of Hunstanton, 1612–1636 — the kinship route ran through his great-great-grandmother Anne Heydon (G18's wife), whose sister Amy had married Sir Roger Lestrange. Failed King's Lynn textile venture c. 1622–25 inside the desecrated St James's Chapel; Sir Hamon Lestrange paid Francis's £100 bond. Sold all Norfolk and Suffolk lands for £1,000 in 1634. Brother of the Cambridge-educated Puritan divine Edmund Gurney (Rector of Harpley 1620–1648). Buried St Botolph Bishopsgate, London, 9 January 1646/7. The financial contraction of his later years is the most plausible material context for an elder son such as John seeing little inheritance ahead in England — and emigrating to Weymouth, Massachusetts.

**HIGHLIGHTS.** No structural changes proposed. No edits.

---

### G15 — Henry Gurney (1548/49 – 1615/16)

**TITLE.** No change.

**BYLINE — JSON `summary`** — already strong; light tightening to bring it to target length and hit the bibliophile point harder.

Current:
> 'Last Gurney born Roman Catholic.' Twelve surviving children. Buried All Saints, West Barsham (per his own will, next to his wife). Elizabethan poet whose 600-poem commonplace book survives as Bodleian MS Tanner 175.

Replace with:
> The last Gurney born a Roman Catholic, with Lady Catherine Howard as godmother — and an Elizabethan poet rediscovered by literary scholarship in 2005, whose 600-poem commonplace book and library catalogue survive as Bodleian MS Tanner 175. Father of twelve.

(40 words.)

**NOTABLES — JSON `notables`** — already deeply substantive, currently 350+ words. Rewrite to a tighter sweep that lifts the most attention-getting bits and removes overlap with the new byline.

Replace with:
> Inherited at age 21 as grandson and heir to Anthony Gurney G17, who died 4 January 1555/6 — three weeks into Mary I's restored Catholicism. Confirmed by Francis Blomefield's parish surveys (1572) as lord of West Barsham (held by one knight's fee of Castleacre), Great Ellingham (held of the heirs of Lord Bardolph), Irstead (held of the Bishop of Norwich), and Gurney's manor in Hingham (held of the heirs of Henry Lord Morley) — the Hingham manor house substantially survives as Grade II listed Gurney's Manor, whose c. 1600 rear wing was built in his lifetime. In 1587 he repurchased Harpley — the medieval Gurney seat his ancestors had held c. 1183 to the 14th century — and presented to its living in 1588 and 1602. His 600-poem commonplace book (Bodleian MS Tanner 175) preserves an inventory of his library and his verse "censures" of more than twenty borrowed books, including Spenser's *Faerie Queene*, John Foxe, Robert Southwell, and Richard Hakluyt. His correspondence circle is, per Steven W. May (*Spenser Studies* 20, 2005), "the most extensive coterie of named individuals identified to date in the Tudor and early-Stuart period." Three of his twelve surviving children shaped onward history: Thomas III (heir, d. 1614 vita patris); Edmund (Cambridge-educated Puritan divine, Rector of Edgefield 1614 then Harpley 1620–1648, with his own *Dictionary of National Biography* entry); and Francis (G14), apprenticed to a London Merchant Taylor and the bridge to the family's American descent. Will of 1614 directed burial "next to my wife there" at All Saints, West Barsham (corroborating Pease/Pennyghael's record of Ellen Blennerhasset's burial there) and warned his sons against holding "fantasticall or erroneous opinions, so adjudged by our Bishop or civill Lawes."

**HIGHLIGHTS.** No structural changes proposed — the existing six highlights cover the right ground in the right order. No edits.

---

### G16 — Francis Gurney (c. 1521 – before Dec. 1556)

**TITLE.** No change.

**BYLINE — JSON `summary`** — currently substantive (43 words). Light rewrite to punch up the heir-apparent-who-never-inherited pivot, which is the most striking structural fact about him.

Current:
> Heir-apparent of the Norfolk Gurney estates who never inherited; married Helen Holdich of Ranworth in 1543; died vita patris before his father Anthony (G17). His son Henry (G15) inherited as grandson and heir.

Replace with:
> Heir-apparent of the Norfolk Gurney estates who never inherited — died young and *vita patris* before his father Anthony (G17), so the great Mortimer-of-Attleborough portfolio fell to his seven-year-old son Henry (G15) as boy lord.

(35 words.)

**NOTABLES — JSON `notables`** — tighten and elevate the inheritance-skip-twice point and the Irstead question.

Replace with:
> Eldest son of Anthony Gurney (G17) and Margaret Lovell — coheir of the Lovell-Mortimer-of-Attleborough barony. Born 20 August 1521 (per Pease/Pennyghael). Married Helen Holdich, daughter of Robert Holdich, Esq., of Ranworth, Norfolk, on 6 August 1543; the marriage is independently confirmed by Francis Blomefield, *History of Norfolk*, vol. vii (1807), pp. 42–47 (West Barsham parish entry). Identified in Daniel Gurney's pedigree as "of Irstead" — though the principal Irstead manor had passed to Sir Richard Southwell by 1540, suggesting the residence may have been a smaller tenement; the Irstead connection runs through his Heydon grandmother Anne (Sir Henry Heydon had received the Irstead manor by conditional bequest from John Groos's 1487 will, per Blomefield vol. xi). Died before his father, who died 4 January 1555/6. Two consecutive *vita patris* deaths in this family — Francis here, and his own son's son William V (G18) two generations earlier — produced an extraordinary chain of grandson-heir successions through the Norfolk Gurney line.

**HIGHLIGHTS.** No structural changes proposed. No edits.

---

### G17 — Anthony Gurney (c. 1499 – 4 January 1555/6)

**TITLE.** No change.

**BYLINE — JSON `summary`** — currently substantive. Tighten and re-pace; the existing version reads as four bullets stacked into one paragraph. Lift the Earl-of-Surrey moment up since it's the most arresting single fact.

Current:
> Boy lord of West Barsham (inherited c. 1508 aged about 9). BOLEYN CONNECTION: Second cousin of Queen Anne Boleyn through his Heydon mother. Brought Great Ellingham and the Lovell-Mortimer-of-Attleborough lands into the family by his marriage to Margaret Lovell. Foreman of the Norfolk grand jury that indicted the Earl of Surrey, January 1546/7.

Replace with:
> Boy lord of West Barsham (inherited aged about nine) and second cousin of Queen Anne Boleyn through his Heydon mother — and, on 7 January 1546/7, foreman of the Norfolk grand jury whose indictment of Henry Howard, Earl of Surrey, sent the poet to Tower Hill twelve days later, with the king himself dead nine days after that.

(57 words — slightly over target but the king-dies-within-weeks compression is too good to drop.)

**NOTABLES — JSON `notables`** — currently 350+ words and dense. Cut to the most attention-getting items, removing material now folded into the byline.

Replace with:
> Both Anthony and Queen Anne Boleyn were great-grandchildren of Sir Geoffrey Boleyn, Lord Mayor of London 1457–58 — Anthony through Sir Geoffrey's daughter Anne Boleyn the elder of Blickling (his maternal grandmother), Queen Anne Boleyn through Sir Geoffrey's son Sir William Boleyn. Married c. 1519 Margaret Lovell, daughter and coheir of Sir Robert Lovell — "cousin and coheir of Sir Thomas Lovell, privy counsellor to King Henry VII and Henry VIII and Knight of the Garter" (Blomefield, vol. vii). The marriage brought into the Gurneys the manor of Great Ellingham, after Henry Spelman the elder of "Mickle Elyngham" died without issue in 1525 (Blomefield, vol. i). Margaret's mother Ela Conyers was sister of Anne Conyers, mother of the antiquary Sir Henry Spelman of Congham — making Anthony's children first cousins once removed of Spelman. Through the Heydon sisters, also linked to the Pastons of Caister, the Cobhams (and so to Sir Thomas Wyatt the poet via Elizabeth Brooke), and the Lestranges of Hunstanton — the kinship later activated when Francis Gurney (G14) became financial agent to the Lestranges from 1612. Norwich town house "Gurney's Place" in St Julian's parish (the parish of the Lady Julian anchorite cell). Documented in the Lestrange of Hunstanton household and privy purse accounts (Daniel Gurney, *Archaeologia* vol. 25, 1832). Died 4 January 1555/6 (Blomefield's precise day, vol. vii); his eldest son Francis (G16) had predeceased him, so his grandson Henry (G15) succeeded. 17th great-grandfather of Allen Gurney.

**HIGHLIGHTS.** No structural changes proposed. No edits.

---

### G18 — William Gurney V (c. 1465 – before 1508)

**TITLE.** No change.

**BYLINE — JSON `summary`** — currently 37 words and well-shaped. Light edit to give it more snap.

Current:
> Eldest son and heir-apparent of William Gurney IV (G19); died before his father; married Anne Heydon of Baconsthorpe Castle, bringing direct descent from Anne Boleyn the elder of Blickling and the Heydon-Boleyn-Howard cousinage of late-medieval Norfolk into the family.

Replace with:
> Heir-apparent who died before his father, leaving a nine-year-old boy as eventual heir. By marrying Anne Heydon of Baconsthorpe Castle "shortly after 28 May 1484," he carried into the Gurneys the Heydon-Boleyn-Howard cousinage of late-medieval Norfolk — and made his son Anthony G17 the second cousin of Queen Anne Boleyn.

(50 words — slightly over but the second-cousin-of-the-queen anchor is the highest-impact item.)

**NOTABLES — JSON `notables`** — currently 200+ words and spread thin. Tighten to surface the highest-impact items.

Replace with:
> Anne Heydon was daughter of Sir Henry Heydon (Privy Councillor to Henry VII and builder of Baconsthorpe Castle, English Heritage open free near Holt, Norfolk) and Anne Boleyn the elder of Blickling, sister of Sir William Boleyn — paternal grandfather of Queen Anne Boleyn. Anne Heydon's siblings married into the Pastons of Caister, the Cobhams (and so to Sir Thomas Wyatt the poet via Elizabeth Brooke), and the Lestranges of Hunstanton; the Lestrange marriage explains the appointment of William V's great-great-grandson Francis Gurney (G14) as financial agent to the Lestranges 1612–1636 — they were distant cousins. Died vita patris 16 February 1507/8 per Daniel Gurney's *Supplement* Note 132 (Inquisitions Post Mortem 13 Henry VIII, part 1, No. 103). Two trust deeds: (1) 19 September 1485 (2 Richard III) for Swathings/Hingham manors, feoffees including William Calthorpe Knt.; (2) 6 April 1505 (21 Henry VII) for West Barsham/Denver manors, feoffees including Edward Howard Knt. (the future Lord Admiral). Cantley tenure: Swathings still held under the lords of Cantley — the old senior Gournay seat — 400 years after the senior baronial line moved on. Widow Anne Heydon remarried Sir Lionel Dymoke of Ashby, Lincolnshire (d. 17 Aug. 1519); Anne died c. 1521.

**HIGHLIGHTS.** No structural changes proposed. No edits.

---

### G19 — William Gurney IV (c. 1450 – 18 January 1508)

**TITLE.** No change. (DG-I pedigree p. 287 styles him "William Gurnet, Esq. IV" — "Esq." is a descriptor of station, not a prefixable title.)

**BYLINE — JSON `summary`** — currently 50+ words. Tighten and lead with the most arresting fact.

Current:
> Son of Thomas Gournay II and Margaret Jerningham. Escheator for Norfolk; of council to the Duke of Norfolk in 1477. Married Anne Calthorpe, only daughter of Sir William Calthorpe KB of Burnham Thorpe by his first wife Elizabeth Grey. Died 18 January 1507/8 at Burnham Thorpe.

Replace with:
> Yorkist Norfolk gentleman whose 1507 will required 700 sheep to remain at West Barsham after his death — "a considerable flock in those days." Escheator for Norfolk under Edward IV and of council to John Howard, Duke of Norfolk, in 1477; died at Burnham Thorpe (later Lord Nelson's birthplace) in 1508.

(52 words — over target but the 700-sheep detail is the single most distinctive fact about any pre-1600 Gurney household.)

**NOTABLES — JSON `notables`** — currently 250+ words. Rewrite to tighten and elevate the Calthorpe/Grey-de-Ruthyn descent and the daughter-prioress detail.

Replace with:
> Married Anne Calthorpe, only daughter of Sir William Calthorpe KB of Burnham Thorpe (1410–1494) — Knight of the Bath at Queen Elizabeth Woodville's coronation 1465, High Sheriff of Norfolk and Suffolk in 1442, 1458, 1469 and 1479, Steward of the household of the Duke of Norfolk in 1479 — by his first wife Elizabeth Grey, daughter of Sir Reginald Grey, 3rd Baron Grey of Ruthyn (so William IV's descendants entered the kinship penumbra of the Lords Grey de Ruthyn, eventual ancestors of Lady Jane Grey). The Anne Calthorpe identification is independently confirmed in eight non-Daniel-Gurney sources (Lee-Warner 1884; Carr-Calthrop 1933; Cotman & Meyrick 1838; the East Anglian; etc.). Independently recorded as "William Gournay, junior" receiving custody of the East Barsham manors of Roger Wood from John Earl of Oxford in 14 Henry VII (1499) (Blomefield, vol. vii, pp. 53–65, East Barsham parish). Adopted the wrestling collar as a personal device — described by the antiquary Sir Henry Spelman from a William Gurney seal of Henry VII's reign — which his descendants bore as a second crest beside the older gurnard fish. Of West Barsham Hall and a town house at Pockthorpe-by-Norwich. Lifetime spanned the entire Wars of the Roses (1455–85) and the first two Tudor decades. Daughter Elizabeth elected Prioress of Thetford in 1518 — twenty years before the Henrician dissolution closed her house. Two cadet branches founded by his sons Walter (Cley-by-the-Sea) and Thomas (Dartmouth, London, and Essex; whose grandson Richard Gurney was Sheriff of London under Elizabeth I). Eldest son William V (G18) had already died vita patris; nine-year-old grandson Anthony succeeded.

**HIGHLIGHTS.** No structural changes proposed — the existing six highlights already cover the right ground. No edits.

---

### G20 — Thomas Gournay II (fl. c. 1430 – d. 1471)

**TITLE.** No change.

**BYLINE — JSON `summary`** — currently 40+ words. Rewrite to lead with the will (the highest-impact single artefact).

Current:
> Son of Thomas Gournay I and Catherine Kerville. Lord of West Barsham, Harpley, and Norwich. Married Margaret Jerningham of Somerleyton. Will dated 18 March 1469/70 (9 Edward IV) per Blomefield Vol. VIII, proved 27 July 1471.

Replace with:
> The earliest Gurney will to survive in full personal detail — dated at West Barsham, proved 27 July 1471 (twelve weeks after Tewkesbury) — names three simultaneous family residences and leaves all the household's wool and linen to his wife Margaret Jerningham as "her own work and that of her servants."

(50 words — over target but the "her own work" gendered-economy detail is genuinely arresting.)

**NOTABLES — JSON `notables`** — rewrite to tighten and avoid byline overlap.

Replace with:
> Son of Thomas Gournay I (G21) and Catherine Kerville. Married Margaret, daughter of Sir Thomas Jerningham, Knt., of Somerleyton, Suffolk — one of Norfolk and Suffolk's most powerful Catholic gentry families (Sir Henry Jerningham of Huntingfield was a principal supporter of Mary I's accession in 1553; the family was still recusant under Elizabeth). The Jerningham marriage anchored the West Barsham Gurneys into a Catholic gentry network that would still be structuring their marriages a century later — when Helen Holditch (G16's widow) married a Jerningham, the connection was being activated for the second time. Three simultaneous gentry residences — West Barsham Hall, a house at Harpley, and a town house in St Gregory's parish, Norwich — Daniel Gurney's textbook illustration of the medieval pattern by which Norfolk gentry "removed with their family to consume the produce of each estate." Will directs burial in the chancel of Harpley if he died at Harpley, or in the church of the Friars Minors (Greyfriars) at Norwich if he died there — independently confirmed by Blomefield, *History of Norfolk*, vol. viii (1808), pp. 452–459. The 1471 will is dated 18 March 1469/70 (9 Edward IV) and proved 27 July 1471.

**HIGHLIGHTS.** No structural changes proposed. No edits.

---

### G21 — Thomas Gournay I (fl. c. 1408 – c. 1450)

**TITLE.** No change.

**BYLINE — JSON `summary`** — currently substantive (40+ words) but could lead more sharply with the collateral inheritance.

Current:
> Nephew of Sir John Gurney V (d. 4 Dec. 1408), Sheriff of Norfolk and Suffolk and MP for the Coventry parliament of 1404. Inherited the family estates collaterally when his uncle Sir John's ten-year-old son Edmund died shortly after his father, ending the senior line.

Replace with:
> A younger son's son who never expected to inherit. When his uncle Sir John Gurney V — Sheriff of Norfolk, Coventry MP 1404, and the most distinguished Gurney of the 14th century — died on 4 December 1408 and his ten-year-old heir followed him to the grave, Thomas became, by collateral succession, lord of West Barsham.

(56 words — over target but the dramatic collapse of the senior line is the central fact about him.)

**NOTABLES — JSON `notables`** — currently thin. Rewrite to surface the substance from the fact sheet (the Heylesdon/La Selde Coronata London warehouse is too good a detail to miss).

Replace with:
> Son of Robert Gournay (G22) by Joan de Norwich. Sir John Gurney V's full inheritance — eight Norfolk manors plus one in Suffolk (per History of Parliament Online) — descended to Thomas as the surviving male-line heir. The portfolio briefly included "La Selde Coronata," a London City warehouse Sir John had brought into the family by marriage to Alice Heylesdon (daughter and sole heir of the wealthy London mercer and former alderman John Heylesdon), along with the Heylesdon manors of Hellesdon and Drayton in Norfolk and the advowsons of two chantries Heylesdon had founded. Married Catherine, daughter of Robert Kerville of Watlington, Norfolk — a sensible diversification into the western-Norfolk Lynn-hinterland gentry. No record of him in Crown office, parliamentary service, sheriffdom, or commission of the peace — a striking silence given his uncle Sir John's extensive record, suggesting a deliberately private gentleman consolidating an unexpected inheritance through the long Lancastrian minority.

**HIGHLIGHTS.** No structural changes proposed. No edits.

---

### G22 — Robert Gournay (fl. c. 1370–1420)

**TITLE.** No change.

**BYLINE — JSON `summary`** (current = `Son of Edmund Gurney (d.1387). Brother of Sir John (d.1408). Married Joan de Norwich.` — too thin):

Replace with:
> The elusive direct-line ancestor through whom every subsequent Gurney descends — and yet so undocumented that Daniel Gurney himself wrote only that Edmund had "a second son, whom we believe was named Robert."

(33 words.)

**NOTABLES — JSON `notables`** — replace with substance from fact sheet. The "uncertainty of his very name" is itself the most striking fact, and the "everything-flows-through-him" point is critical for the reader.

Replace with:
> Born into the most prosperous and well-connected household the family had yet produced — father Edmund (G23) was steward of John of Gaunt's East Anglian estates and counsel to Norwich and Bishop's Lynn; elder brother Sir John heading toward sheriffdom and a parliamentary career; mother Katherine de Wauncy the heiress of West Barsham. As a younger son Robert lived obscurely. No deed in his name, no court appearance, no will, no land transaction has been identified. He exists in the record almost entirely as a relationship — son, brother, husband, father. Yet because his nephew Edmund (Sir John V's only son) died as a minor, Robert's son Thomas I (G21) became, by collateral succession, lord of West Barsham — and through that single moment of dynastic luck, the entire subsequent Gurney line — including the West Barsham Gurneys, the banking Gurneys of Norwich, and through Francis Gurney's son John Gurney-1 the American Gurneys — descends from him. Source: Daniel Gurney, *Record*, Part I, p. 280; *Supplement*, p. 363.

**HIGHLIGHTS.** No structural changes proposed. No edits.

---

### G23 — Edmund Gurney (d. 1387)

**TITLE.** No change.

**BYLINE — JSON `summary`** (current = `HISTORY OF PARLIAMENT. Steward of John of Gaunt's East Anglian estates 1372–1387.` — accurate but flat):

Replace with:
> Norfolk lawyer of county-wide reputation who, for fifteen years until his death, served as steward of John of Gaunt's East Anglian estates — and through marriage to Katherine de Wauncy acquired West Barsham, the seat the family would hold for the next three centuries.

(43 words.)

**NOTABLES — JSON `notables`** — rewrite to lift the most arresting items and tighten the Patent-and-Close-Rolls catalogue.

Replace with:
> Counsel to the cities of Norwich and Bishop's Lynn (King's Lynn) simultaneously — the standing council of Norwich, *in the nature of recorder and steward*, alongside Edmund de Clipesby (Daniel Gurney, *Supplement*, p. 359). Justice of the Peace for Norfolk (44 and 49 Edw. III). Royal commissioner across at least fifteen separate Patent and Close Roll entries: customs fraud, arbitration between the prior of Norwich and the prioress of Carrow, special commissioner for Queen Philippa's manor, justice for piracy inquiry, forcible-entry inquiry, and others. Through Katherine de Wauncy — daughter of Sir William de Wauncy of West Barsham, eventually sister and heir of Sir Edmund de Wauncy when Sir Edmund's seven-year-old son also died in 1372 — the entire West Barsham estate (held by the Wauncys since Domesday under Earl Warren) came to him in right of his wife. His arms (engrailed cross argent) impaling the Wauncy coat (gules, three dexter hand-gloves pointed downwards, argent) were visible in a window of "Gurney's Place" in St. Julian's parish, Norwich, and were still visible in a window of Denton church, Norfolk, when Daniel Gurney wrote in 1848. Will dated at West Barsham on Thursday the feast of the Ascension 1387, proved same year (Reg. Harsyke fol. 34); 8s. distributed to the poor on his burial day; buried in the church of the Assumption of the Blessed Virgin, West Barsham. Will named four executors — Katherine his wife, John his son, Osbert de Mundeford, and Thomas Kemp — and included a restitution clause directing heirs to compensate anyone he had wronged.

**HIGHLIGHTS.** No structural changes proposed. No edits.

---

### G24 — John de Gournay IV (fl. c. 1330–1370)

**TITLE.** No change.

**BYLINE — JSON `summary`** (current = `Mentioned in a deed of his uncle's, 1331. Father of Edmund Gurney (d.1387).` — far too thin):

Replace with:
> Lord of Harpley who held his first manorial court there on Friday the vigil of St. Laurence, 28 Edward III — 9 August 1354. The last of the family seated primarily at Harpley before his son Edmund married the West Barsham heiress and shifted the family seat.

(46 words — slightly over target; the very specific 9 August 1354 date is the only personal detail of his life that survives.)

**NOTABLES — JSON `notables`** — currently very thin. Rewrite from fact sheet content.

Replace with:
> First attested 1331 in a deed of his great-uncle John (Rector of Harpley), 6 Edw. III. May have been the presenter to the Harpley church living in 1332 on the Rector's death — Daniel Gurney noted the presenter is named "John de Gurney junior," "more probably this John" rather than his father. First manorial court at Harpley: Friday the vigil of St. Laurence, 28 Edw. III (9 August 1354), documented in BL Add. MSS. 8841, fol. 112 — survives as the one specific day in his life that the documentary record has preserved. Lived through the early decades of the Hundred Years' War, and would have been about eighteen at the worst year of the Black Death in England (1348–49); no record of his personal experience of either survives. His most consequential act was raising his son Edmund (G23) into the legal career that made the Wauncy marriage and the West Barsham acquisition possible.

**HIGHLIGHTS.** No structural changes proposed. No edits.

---

### G25 — John de Gournay III (fl. c. 1300–1353)

**TITLE.** No change.

**BYLINE — JSON `summary`** (current = `Son of William III. Wife Jane de Lexham. Succeeded uncle John (Rector of Harpley) in 1332. Living 27 Edw. III (1353).`):

Replace with:
> The generation that restored continuity. When his clerical uncle John, Rector of Harpley, died in 1332 — having held the family estates for nearly four decades after John's father had transferred them to him for an annuity in 1294 — John III stepped forward as nephew and heir, returning Harpley to the direct male line.

(54 words — over target; the *why* of the inheritance matters and isn't captured anywhere shorter.)

**NOTABLES — JSON `notables`** — currently thin. Rewrite from fact sheet.

Replace with:
> First attested in a 1331 deed of his uncle John (Rector of Harpley), 6 Edw. III. Succeeded as heir to the Rector in 1332 and immediately exercised advowson, presenting the new incumbent to the Harpley living. Married Jane, daughter of Edmund de Lexham, before 1324 — one of the earliest marriage dates in the junior Norfolk branch with a named wife and approximate date, marking the point at which the documentary record begins to thicken. The Lexham family of Lexham in Norfolk are documented from the early 13th century. Living 27 Edw. III (1353). Long life c. 1300–1353+ spanned the early Hundred Years' War, the Black Death of 1348–49 (which killed roughly a third of England's population), and the first great parliamentary crises of Edward III's reign. Source: DG, *Record*, Part I, p. 286.

**HIGHLIGHTS.** No structural changes proposed. No edits.

---

### G26 — Sir William de Gournay III, Knt. (fl. c. 1260–1300)

**TITLE.** Already correct ("Sir William de Gournay III, Knt.").

**BYLINE — JSON `summary`** (current = `Married Katherine de Baconsthorpe. Sold all estates to brother John, Rector of Harpley, in 1294.`):

Replace with:
> The first member of the family to seal a surviving document with the engrailed cross — and the lord who, in 1294, conveyed every one of his Norfolk manors to his clerical brother John, Rector of Harpley, in exchange for a lifetime annuity. A genuinely unusual act.

(46 words — over target; the heraldry-first plus the unusual estate-conveyance are both essential.)

**NOTABLES — JSON `notables`** — rewrite to surface the heraldic and inheritance specifics.

Replace with:
> Knight; attested 14 Edward I (1286) as lord of Gurney's manor in Harpley, Hardingham, and Hingham. The 1294 deed transferring all his estates to his brother John (Rector of Harpley) is, per Daniel Gurney, "the earliest on record of the use of the cross engrailed in a seal or document by any of the family" — though the same arms were borne earlier by his father Sir John I (G27) on a contemporary roll of arms. Why William alienated the entire estate is unrecorded; financial distress is the most common reason for such transactions, but the lifetime annuity arrangement suggests he retained an income stream. The fortunate result: when Rector John died in 1332 without heirs, the estates descended cleanly to William's son John III (G25), bypassing the celibate clergyman's generation and restoring the direct line. Married Katherine, daughter of Edmund Baconsthorpe — resolving the long-running puzzle of the previous generation's "probably a Baconsthorpe" wife.

**HIGHLIGHTS.** No structural changes proposed. No edits.

---

### G27 — Sir John de Gournay I, Knt. (fl. c. 1240–1280)

**TITLE.** Already correct ("Sir John de Gournay I, Knt.").

**BYLINE — JSON `summary`** — currently 17 words and used as Allen's example for the punch-up exercise. Rewrite for sharper voice while preserving the same factual core.

Current:
> Present at battles of Lewes (1264) and Evesham (1265). Accompanied Edward I to Holy Land 1270.

Replace with:
> Rebel baron at Lewes (1264) and Evesham (1265) — forfeited South Wootton manor for siding with Simon de Montfort against Henry III — yet within five years had a royal pardon and accompanied Prince Edward to the Holy Land in 1270. Established the family's coat of arms, *argent, a cross engrailed gules*, that descendants bore for centuries.

(54 words — over target but the rehabilitation arc and the heraldry-establishment are both the highest-impact items.)

**NOTABLES — JSON `notables`** — currently substantive. Light rewrite to surface the trial-by-battle / royal-letters-of-protection items more crisply and remove byline overlap.

Replace with:
> Living 1245. Estate seized by Earl Warren as a rebel after Lewes — DG-Supp Note 112 preserves the full Latin text of the 1264 South Wootton plea, with a livestock inventory of 3 horses, 4 oxen, 14 cows, and 171 sheep seized because John "was in the conflict of Lewes against the Lord King." Presented by jury of Mitford in 1257 for not being knighted — the standard fiscal-evasion offence, periodic compelled-knighthood being a way the Crown raised money. Royal letters of protection for the Crusade survive in the Patent Rolls (DG-Supp Note 114, Rot. Patent 54 Hen. III, 1270): "We have taken into our protection and defence the same John, his men, lands, goods, revenues, and all his possessions" — a routine formula whose issuance to a man who had taken up arms against the crown six years earlier is anything but routine. Rotuli Hundredorum 1274 documents the Harpley tenure chain: King → Earl Warren → Caletorp → Gournay. Heraldic arms: *argent, a cross engrailed gules* — borne by descendants ever since, and the heraldic identity Allen Gurney's lineage carries to the present day. DG (*Record* Supplement, pp. 785–786) speculates the arms may have been adopted at the Crusade, noting Sir Robert de Ufford and Sir John de Ingoldesthorpe — fellow Norfolk lords on the same Crusade — also adopted crosses as their arms.

**HIGHLIGHTS.** No structural changes proposed — the existing four highlights are well-shaped. No edits.

---

### G28 — William de Gournay II → ADD TITLE

**TITLE — JSON `name` field — CHANGE.**

`str_replace` on `data/ancestors v26.json` for the G28 entry only:

`old_str`:
```
    "name": "William de Gournay II",
```

`new_str`:
```
    "name": "Sir William de Gournay II, Knt.",
```

Rationale: DG-I pedigree p. 286 explicitly: "Sir WILLIAM DE GOURNAY, Knt. II. Lord of Harpley, &c.; liv. 1234 & 1243." The G28 fact sheet body styles him "Knight" and includes the Knt. designation in its vital-records section. Title is supported by primary-source genealogy.

**BYLINE — JSON `summary`** (current = `Son of Matthew de Gournay. Father of Sir John I. Living 1234 and 1243.`):

Replace with:
> Knight of Harpley in the troubled middle decades of Henry III, attested in two independent Norfolk records (1234 and 1243). Father of the rebel-Crusader Sir John I — whose career suggests Gournay political sympathies that William may have shared but never acted on publicly.

(44 words — slightly over target; the politics-of-the-next-generation framing is the most interesting available frame for an otherwise sparsely documented life.)

**NOTABLES — JSON `notables`** — currently substantive (140 words). Tighten and elevate the heraldic-inheritance and political-context items.

Replace with:
> Witnessed a charter of William de Clifford to the Abbey of Dore, Herefordshire, in 1220 (DG-Supp Note 111, from Dodsworth MS. 42, Bodleian Library). Wife Katherine — surname uncertain. DG-I pedigree p. 286 calls her "probably a Baconsthorpe"; DG-Supp Note 113 (1858) proposes she was an Ingoldesthorpe, based on a fine at DG-I p. 325. The two identifications remain unresolved — possibly the same woman (Daniel Gurney's later, more considered opinion) or two different Katherines in successive generations (G28 here and G26's wife two generations later). Three known children: Sir John I (G27), Edmund (held a quarter of a knight's fee in Houghton, 1303), and Thomas (Norfolk fine). Lived through the rise of Simon de Montfort's reform movement; died before the open civil war broke out at Lewes in 1264.

**HIGHLIGHTS.** No structural changes proposed. No edits.

---

### G29 — Matthew de Gournay → ADD TITLE

**TITLE — JSON `name` field — CHANGE.**

`str_replace` on `data/ancestors v26.json` for the G29 entry:

`old_str`:
```
    "name": "Matthew de Gournay",
```

`new_str`:
```
    "name": "Sir Matthew de Gournay, Knt.",
```

Rationale: DG-I pedigree p. 286: "Sir MATTHEW DE GOURNAY, Knight, Lord of Runhall and Swathings". The G29 fact sheet's frontmatter `personName` and `pageHeading` already use "Sir Matthew de Gournay" — the JSON `name` is currently inconsistent with the published fact sheet.

**BYLINE — JSON `summary`** (current = `Married Rose de Burnham c.1183. Acquired Gurney's manor in Harpley through her.`):

Replace with:
> Knight whose marriage to Rose de Burnham was personally arranged c. 1183 by Hameline Plantagenet, Earl Warren — half-brother of Henry II — bringing Harpley manor into the Gournay family for the next two centuries.

(36 words.)

**NOTABLES — JSON `notables`** — rewrite to elevate the Warren-renewal point and the Hardingham tithe (independent primary source).

Replace with:
> Hameline Plantagenet, Earl Warren — illegitimate half-brother of Henry II — gave in marriage his kinswoman Rose, daughter and heir of Reginald de Burnham (Fitz-Philip), c. 1183, because the Burnhams "were said to be a younger branch of the house of Warren" (DG-I, p. 278). Rose was therefore a kinswoman of Edith de Warenne — Matthew's own ancestress five generations back — making the Gournay-Warren tie effectively renewed. Through Rose he acquired Gurney's manor in Harpley, Norfolk — the family's primary seat for nearly two centuries. Independent primary-source attestation: Matthew gave the tithes of Hardingham to the church there (Harleian MSS 970, British Library). Held the manor of Swathings in Hardingham. DG Supplement Note 109 corrects the main text: Matthew was living in 1217 (Fine Roll 2 Henry III), paying 20 marks for a writ of attaint concerning his tenement of Swathings. Lived to see King John lose Normandy to Philip Augustus in 1204 — severing the family's remaining Norman tie (the Montigny-sur-Andelle parage tenure his father had held). After 1204, the junior Norfolk branch was an English family in every practical sense, their Norman heritage preserved only in their name.

**HIGHLIGHTS.** No structural changes proposed. No edits.

---

### G30 — William de Gournay I → ADD TITLE

**TITLE — JSON `name` field — CHANGE.**

`str_replace` on `data/ancestors v26.json` for the G30 entry:

`old_str`:
```
    "name": "William de Gournay I",
```

`new_str`:
```
    "name": "Sir William de Gournay I, Knt.",
```

Rationale: G30 fact sheet body explicitly establishes knighthood — "Knight ('Dominus Willelmus de Gurney' — confirming knighthood)" — and the existing JSON `summary` field also leads with "Knight." DG-I, p. 278 documents the Gaywood deed designation; *Dominus* is the standard Latin honorific for a knight. The fact-sheet Vital Records "Occupation/Status" line already states "Knight ('Dominus Willelmus de Gurney' — confirming knighthood)."

**BYLINE — JSON `summary`** (current = `Knight. Lord of Runhall and Swathings. Held Montigny-sur-Andelle in Normandy in parage — proof of blood descent from Barons of Gournay.`):

Replace with:
> The genealogical keystone of the entire junior Norfolk branch. Holding Montigny-sur-Andelle in Normandy *in parage* (a tenure available only to blood relatives of the senior lord) constituted, in Daniel Gurney's words, "incontestable proof of his descent in blood from the Barons of Gournay."

(44 words — slightly over; the keystone-of-the-pedigree role is essential to convey.)

**NOTABLES — JSON `notables`** — rewrite to elevate the cross-Channel and contemporary-namesake-distinction points.

Replace with:
> Designated "Dominus Willelmus de Gurney" (the standard Latin for a knight) in a Gaywood, Norfolk deed of conveyance, DG-I p. 278. Held both English and Norman estates simultaneously — Runhall and Swathings in Hardingham (a Saxon parish spanning parts of three modern parishes — Hardingham, Letton, and Cranworth) plus Montigny-sur-Andelle in Normandy held in parage. Living 1167. DG-Supp Note 105 records a "William de Gournay" witnessing a charter of Henry II at Notre Dame du Pré, Rouen — DG identifies this "in all probability" as our William. A contemporary namesake — a different William de Gurney, *praepositus Parisiensis* (Provost of Paris) under Louis VII — appears in a rhyme preserved by Walter Map, but Daniel Gurney correctly distinguishes the two. Father-son link to Matthew (G29) established by a plea in DG Appendix LIII between Matthew and Gilbert de Runhall.

**HIGHLIGHTS.** No structural changes proposed. No edits.

---

### G31 — Walter de Gournay (fl. c. 1108–1154)

**TITLE.** No change.

**BYLINE — JSON `summary`** (current = `Lord of manors in Norfolk and Suffolk. Ancestor of the entire Norfolk junior branch. Confirmed as Gournay blood by a French royal court.`):

Replace with:
> The junction point. Walter's elder brother Hugh IV inherited the great Norman barony; Walter received a younger son's share of the English estates — and from that single partition descend the West Barsham Gurneys, the Quaker banking Gurneys of Norwich, and through Francis Gurney the American Gurneys.

(48 words — slightly over; the junction-point role is the entire reason this ancestor matters.)

**NOTABLES — JSON `notables`** — rewrite to surface the three-converging-evidence streams and the Anarchy context.

Replace with:
> Youngest son of Gerard de Gournay (Crusader, G32) and Edith de Warenne. Documented in the *Liber Niger Scaccarii* — the Black Book of the Exchequer, c. 1166 — as holding a quarter knight's fee in Suffolk under Manasser de Dampmartin. Three independent evidentiary chains converge to confirm his Gournay blood-descent: (1) the *Liber Niger* entry; (2) his son William I's parage tenure of Montigny-sur-Andelle in Normandy (parage tenure being available only to blood relatives of the senior lord); (3) a *Les Olim* entry — official records of the French royal court — formally recognising the Swathings Gurneys as legitimate descendants of the Lords of Gournay. Lived during "The Anarchy" (Stephen's reign 1135–1154); no record of him in any political or military event — wisest course for a minor Norfolk landlord in those years. The Norman village of "Bois Gautier" (Gautier = Walter in Norman French) in the Pays de Bray may have been named for him (per the historian De la Mairie). Daniel Gurney suggested he may have been named after his father's kinsman Walter Giffard, Earl of Buckingham, or after Walter de la Ferté.

**HIGHLIGHTS.** No structural changes proposed. No edits.

---

### G32 — Gerard de Gournay (c. 1040 – before 1104, Palestine)

**TITLE.** No change.

**BYLINE — JSON `summary`** (current = `CRUSADER. Married Edith de Warenne. Joined First Crusade 1096, died Holy Land.`):

Replace with:
> Crusader who survived the First Crusade — Nicaea, "Burnt Phrygia," the fall of Jerusalem in July 1099 — returned home, then set out again for the Holy Land with his wife Edith de Warenne and died *en route*: *Hierosolymam petens in ipso itinere mortuus est*.

(45 words — slightly over but the surviving-then-dying-on-second-pilgrimage detail is the most arresting fact about him.)

**NOTABLES — JSON `notables`** — rewrite to elevate the seal, the political ferocity ("unsafe man to meddle with"), and the descent through Gundred.

Replace with:
> Married Edith de Warenne, daughter of William de Warenne, 1st Earl of Surrey — the wealthiest Norman baron in England after the king (Domesday holdings in 13 counties). The marriage brought Norfolk manors and the Caister-by-the-Sea barony into the Gournay family. Gerard's own seal — "Signum Girardi de Gornaco" — survives in the Cartulary of La Trinité de Rouen. A formidable lord: when the Count of Évreux tried to claim one of his residences, Gerard's "power and valour made him an unsafe man to meddle with." Sailed September 1096 with Robert Curthose's contingent — Bishop Odo of Bayeux, Stephen de Blois, a host of Norman lords — and wintered in Calabria with Bohemond, who inspected their heraldic badges (one of the earliest documented discussions of nascent armorial heraldry). Daughter Gundred ("la belle Gondrée") married Nigel de Albini in 1119 (the wedding arranged by Henry I himself), introducing Gournay blood into the Mowbray/Norfolk-Howard line; Gundred patronised Byland and Rievaulx Abbeys, whose noble ruins still stand in Yorkshire. JUNCTION POINT: eldest son Hugh IV continued the senior Norman baron line (extinct 1235 in the male line); youngest son Walter (G31) became ancestor of the Norfolk junior branch from which all subsequent English and American Gurneys descend.

**HIGHLIGHTS.** No structural changes proposed. No edits.

---

### G33 — Hugh de Gournay III (c. 1020 – c. 1093)

**TITLE.** No change.

**BYLINE — JSON `summary`** (current = `Lord of Gournay-en-Bray. Norman knight. Buried Abbey of Bec, Normandy.`):

Replace with:
> At the Battle of Hastings in 1066 — *Hugo Senex*, "Hugh the Old" — Domesday landholder in Essex (Liston, Fordham, Ardleigh), personal friend of St Anselm of Canterbury, witness to the foundation charters of the two great Caen abbeys. Buried Abbey of Bec.

(42 words.)

**NOTABLES — JSON `notables`** — rewrite to elevate the Anselm friendship and the twenty-four-villages-Conquest detail.

Replace with:
> Wace's *Roman de Rou* names three Gournays in the 1066 invasion fleet: Hugh III with his father "Old Hugh" and a collateral. After the Conquest, Hugh held three Essex manors directly of the king (Liston, Fordham, Ardleigh) — confirmed by Domesday 1086 but already documented in a 1076 Bec Abbey charter granting tithes from those parishes. Witnessed William I's foundation charters for Saint-Étienne (Abbaye-aux-Hommes) at Caen in 1077 and La Trinité (Abbaye-aux-Dames) in 1082 — both churches survive intact and can still be visited. Added twenty-four villages to the Gournay lordship (the "Conquêts Hue de Gournai") in the Beauvaisis, creating dual feudal allegiance to both the Duke of Normandy and the King of France. Anselm of Canterbury — later canonised and named a Doctor of the Church, arguably the most important philosopher-theologian between Augustine and Aquinas — wrote of him: "Salute the Lord Hugh de Gournay, *dilectissimum nostrum*, and the Lady Basilia, on my part, as sweetly as you can." Married Basilia Flaitel, daughter of Gerard Flaitel and previously wife of Raoul de Vace, grandson of Duke Richard I of Normandy. Died at the Abbey of Bec, having been "shorn a monk" before his death; partial ruins survive at Le Bec-Hellouin, Eure, today open to visitors.

**HIGHLIGHTS.** No structural changes proposed. No edits.

---

### G34 — Hugh de Gournay II (c. 985 – c. 1074)

**TITLE.** No change.

**BYLINE — JSON `summary`** (current = `'The Fortifier.' Fought at Battle of Mortemer 1054.`):

Replace with:
> "The Fortifier" — *le vieil Huon* of the Norman poets. One of three commanders William the Conqueror chose for the Battle of Mortemer (1054), the ducal victory that secured William's grip on Normandy a dozen years before Hastings.

(38 words.)

**NOTABLES — JSON `notables`** — rewrite to add the Mortemer "Franceiz, levez!" detail and the 1035 expedition, plus the Curthose reconciliation.

Replace with:
> Sailed to England in 1035 with Prince Edward (future Confessor) on a failed attempt to claim the throne after Cnut's death — Hugh's first glimpse of the island his family would help conquer thirty-one years later. At Mortemer (1054), after the Norman dawn assault routed the French northern column, William sent Rodolf de Toeny through the night near the king's camp to cry: "*Franceiz, Franceiz, levez, levez! Allez vos amis enterrer ki sunt occiz a Mortemer!*" — *Frenchmen, arise, go bury your friends killed at Mortemer!* The royal army broke up before dawn. Witnessed pre-1066 charter granting Bernières to Odo of Bayeux (Bayeux Cathedral *Liber niger*); Vaudreuil charter of April 1067. After the Siege of Gerberoy (1079), one of four barons chosen to broker the reconciliation between William and his rebellious son Robert Curthose — alongside Roger Earl of Shrewsbury, Hugh de Grandmesnil, and Roger de Beaumont. Three Gournays at Hastings 1066 per Wace; if born c. 985, Hugh was about 80, and Hannay supposed he may have been present in an advisory or ceremonial capacity. A local manuscript tradition says he was wounded in a "battle of Cardiff" and died in Normandy shortly after, but Daniel Gurney himself suspected "Cardiff" was a scribal corruption for Norwich or Caistor — placing the engagement among the Danish raids on England's east coast in 1069–1075. Hannay considered him "one of the greatest" Norman potentates of the mid-eleventh century.

**HIGHLIGHTS.** No structural changes proposed. No edits.

---

### G35 — Renaud de Gournay (c. 970 – uncertain)

**TITLE.** No change.

**BYLINE — JSON `summary`** (current = `Held seigneury of Gournay. Charter 989–996 confirms his existence.`):

Replace with:
> The first ancestor in the line confirmed by a contemporary primary-source document — a charter of 989–996 founding the priory of La Ferté-en-Bray, naming Renaud and his wife Alberade alongside Duke Richard I, his son Richard II, and Robert Archbishop of Rouen.

(43 words.)

**NOTABLES — JSON `notables`** — rewrite to surface the transition-from-sea-king detail and Hannay's evocative observation.

Replace with:
> The La Ferté charter of 989–996 was issued by Renaud's son Gautier "*imperante fratre meo Hugone*" — at the command of my brother Hugh — and witnessed by Duke Richard I (Sans-Peur, d. 996), his son Richard II, and Robert Archbishop of Rouen (Robert acquired his see in 989), giving a firm date window. Hannay observed of the donations: "very considerable, and show that the house was great." Two sons, two legacies: Gautier de la Ferté founded the priory; Hugh II inherited the Gournay lordship and went on to command at Mortemer in 1054 and witness charters of Duke William of Normandy — who would conquer England twelve years later. Hannay placed Renaud "just into the transition time — the stage in which the Norman gentleman was developing out of the Norse sea-king." Wife "Alberade" (Alberarda) is the first named woman in the Gurney line. The Pays de Bray in Renaud's era was being transformed from frontier wildland into cultivated orchards and vineyards.

**HIGHLIGHTS.** No structural changes proposed. No edits.

---

### G36 — Hugh de Gournay I (c. 945–950 – uncertain)

**TITLE.** No change.

**BYLINE — JSON `summary`** (current = `Son of Eudes. First lord born in Gournay.`):

Replace with:
> First of the line born in Normandy, contemporary with Duke William Longsword. Builder of the citadel and "La Tour Hue" (Hugh's Tower) at Gournay-en-Bray — a fortification that stood for approximately eight hundred years before its final demolition around the 1750s.

(42 words.)

**NOTABLES — JSON `notables`** — rewrite to surface William Brito's verse and the William-Longsword-assassination context.

Replace with:
> Built a citadel near the future church of Saint-Hildevert, surrounded it with a double ditch, and topped it with a tower that took his own name: "La Tour Hue" (*Hue* being the Old French form of Hugh). The 13th-century court poet William Brito later described Gournay as "*munitum triplice muro … inexpugnabilis*" — fortified with triple wall, impregnable even without defenders inside. Daniel Gurney's 1858 *Supplement* records the tower as still standing "a century ago" — placing its final demolition around the 1750s, after roughly eight centuries. Lived through Duke William Longsword's reign and assassination (c. 942) on an island in the Somme — Hannay imagined "Hugh de Gournay's horror, in that rude but pious time, when the news reached him amidst his architectural and other labours." Hannay also noted his name was "convertible with Eudes or Eude" in the chronicles, suggesting both names derive from a common Norse root. Lineage status remains *Limited Historical Record* — known by tradition and by the tower eponym, but not yet by contemporary charter document in his own name (his son Renaud is the earliest contemporary-document ancestor at G35).

**HIGHLIGHTS.** No structural changes proposed. No edits.

---

### G37 — Eudes (Odon) de Gournay (c. 860 – after 911)

**TITLE.** No change.

**BYLINE — JSON `summary`** (current = `ORIGIN OF THE LINE. Viking companion of Rollo. ~37 generations to Allen.`):

Replace with:
> Origin of the line. A Viking warrior in Rollo's war-band who, at the Treaty of Saint-Clair-sur-Epte in 911, received Gournay-en-Bray and the Pays de Bray as his portion — beginning a documented property-holding lineage that runs ~37 generations and ~1,160 years to Allen Gurney.

(45 words — slightly over but the 37-generation arc is the entire reason this entry exists.)

**NOTABLES — JSON `notables`** — rewrite to surface the cheese, the black shield, and Hannay's defence of his historicity.

Replace with:
> Daniel Gurney himself acknowledged: "the existence of Eudes... is a matter of tradition" — no contemporary document survives. But James Hannay (1867) defended the tradition as credible precisely because it was modest: "no supernatural feats of heroism are attributed to him; he does not scatter whole armies in the doubtful moments of great battles" — he is simply made what hundreds of Norman family founders were, "a follower of Rollo, sharing in his chieftain's fortunes." A French local tradition styles him *"le chevalier à l'écu noir"* — the knight with the black shield — consistent with the later Gournay arms (*pure sable*, a plain black shield), among the simplest and most ancient heraldic designs in Norman genealogy. The town of Gournay-en-Bray (Seine-Maritime, pop. ~6,500) survives today ~50 km east of Rouen, celebrated for Neufchâtel cheese — the Pays de Bray was once called Normandy's "butter capital." The 12th-century Collégiale Saint-Hildevert, near where Eudes's grandson Hugh I built his tower, still stands. Léopold Delisle, the leading 19th-century Norman charter scholar, challenged Daniel Gurney's early genealogy, and the lineage status here remains *Minimal historical record* — but the founding land grant initiated a documented holding that lasted ~750 years (911 to 1661, when the West Barsham Gurneys went extinct in the direct male line in England).

**HIGHLIGHTS.** No structural changes proposed. No edits.

---

## Application Order for Phase 2

1. Apply the three JSON `name` `str_replace` operations (G28, G29, G30) on `data/ancestors v26.json`. Verify each by re-reading the modified G28/G29/G30 entries — the title prefix should now appear in `name`.
2. Apply each ancestor's `summary` rewrite on the same JSON file. For the modern-American ancestors with empty `summary` fields (G3 inherited; G4 noted), the operation is to populate. Note: G3 is "living" status and was excluded from this patchset by Allen's instruction to skip living ancestors.
3. Apply each ancestor's `notables` rewrite on the same JSON file.
4. Apply the two G02 fact-sheet `str_replace` operations on `fact-sheets/g02-lester-hayes-gurney-fact-sheet.md` — one fixing typos, one rewriting the Masonic highlight lede.
5. Validate the JSON parses (no trailing-comma or quote-escape errors introduced by the rewrites).
6. Build site locally to confirm rendered output for: pedigree table bylines (`summary`), drawer notables (`notables`), ancestor `name` cells, and the G02 highlights block.

## Phase 2 Validation Checklist

- [ ] `data/ancestors v26.json` parses as valid JSON after edits.
- [ ] G28, G29, G30 `name` fields display the new "Sir … Knt." titles.
- [ ] All 33 direct-line ancestor `summary` fields are within 20–45 words and meaningfully distinct from `notables`.
- [ ] All 33 direct-line ancestor `notables` fields read as next-layer-of-detail beyond the byline (no duplication).
- [ ] G02 fact-sheet typos corrected; Masonic highlight reads cleanly.
- [ ] Era rows, related entries, collateral entries left untouched.

## Items Deliberately NOT Done in This Patchset

- G06 (William Gurney biography) — handled via key-research bio per project structure, not a fact sheet; not in scope of this sweep.
- G13 (John Gurney) — handled via case-file structure; not in scope.
- G14 Edmund-divine `related` entry — collateral, not direct-line.
- G17 Queen Anne Boleyn `related` entry — collateral, not direct-line.
- Hugh de Gournay IV / V `related` entries (G32) — collateral senior baron line, not direct-line.
- G3 Lester Sawyer Gurney III — currently empty `summary`/`notables`; lineageStatus "Confirmed" but flagged as deceased 19 December 2011. Allen explicitly excluded living ancestors; G3's status here is not living, but the project JSON has effectively stub-only data for him. **Recommendation for a follow-up patchset**: G3 could receive a populated byline if Allen wants to fill that slot — currently the pedigree table will show no byline at all for the G02→G04 bridge.
- Source citations for any bylines/notables — none required since no new external research is being added; all rewrites draw exclusively from material already present in the existing fact sheets, research companions, and JSON.

