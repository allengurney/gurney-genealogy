# v121 — G13 John Gurney companion: chronology table, Tyng/Adams + Weymouth assimilation, Billerica synthesis, Boston negative

Phase 1 patchset. Assimilates the June 2026 thread's findings into the research companion `research/people/g13-john-gurney-fact-sheet.research.md` (and the Billerica/Mendon place files). Pairs with **v120** (sources/corpus/media/place-spine) and precedes **v122** (fact sheet). All edits merge into existing prose — no dated append blocks.

New companion footnotes added by this patchset: `[^weymouth-msbook]`, `[^nehgr-30-432-g13]`, `[^nps-clr-g13]`, `[^hist-weymouth-g13]`, `[^braintree-petition-g13]`. All other footnotes referenced already exist in the companion.

---

## Item 1 — Replace the partial property table with the G-13 chronology table — PROMOTE

The companion's "Land and property records" section opens with a partial property table. Replace that table with the maintained G-13 chronology table (plain-reading, modern-style dates, Tyng rows updated to the 1647 NPS finding, footnotes mapped to the companion's source set). `str_replace`:

`old_string`:
```
| Event | Date (or inferred range) | Detail and basis for the date | Source |
|---|---|---|---|
| Arrival in New England | 1638–early 1641 (inferred range) | Bounded by the records: present at Weymouth by the 30 May / 2 June 1641 gunpowder matter, and an original Weymouth grantee before the 1643 property record; the Great Migration tail (sharp falloff after 1640) favours the later part of the range. Cannot be later than early 1641. | MBCR 1:331; Mass. State Archives calendar |
| Original grant of East Field (2 ac) + Mill Field (4 ac) parcels, Weymouth | c. 1637–1642; best estimate c. 1640–41 | The grants are undated. The small open-field system was active before 1636, so an earlier start is not excluded, but John is absent from the distinct 1636 Fresh Pond great-lot roll of sixteen householders — evidence against a 1636 presence — while the narrower c. 1640–41 estimate fits Weymouth's substantial new-settler influx around 1640 and his first surviving Weymouth appearance. The parcels are recorded by the c. 1643 possession register, already held by other men; that register cannot predate William Fry's death on 26 October 1642 and carries recited instruments to at least 21 May 1644, so its conventional "1643" heading is an approximation, not a grant date. The same open-field division includes the Nathaniel Adams parcels "granted between 1642 and 1644." | Nash, App. C; *History of Weymouth* |
| Those parcels reassigned to other holders (East Field → Robert Randoll; Mill Field, under Thomas Richardes) | by 1643 | The 1643 record lists the parcels under their new holders with the memory that each was "first granted/given to John Gurny/Gurnie" — so the reassignment is complete by 1643. | Nash, App. C (pp. 258, 278) |
| 1643 Weymouth property record (documents the above) | 1643 | Nash's Appendix C is "a partial record of the then property owners… made in 1643" — it records the post-reassignment state, not the original grant. | Nash, App. C |
| Move from Weymouth to Braintree | c. 1642–1645 (inferred range) | Bounded by his Weymouth parcels being already divested by the 1643 record (so the move can be as early as c. 1642) and "in Braintree before 1645." Use "moved," not "removed." | *History of Weymouth* |
| Petition for the new plantation at Braintree | May 1645 | Signed the petition — a marker of established Braintree standing. | Colonial petition record |
| Great lot no. 16, Weymouth Second Division | 2 February 1651-52 | A separate, later Weymouth grant (not the 1640s East/Mill Field parcels); itself "subsequently granted to others" (reassignment date not recorded). | Nash, App. C (p. 282) |
| Held 48 Braintree acres "by lease" (Tyng estate) | documented 25 May 1653; lease already in place before that date | The Tyng probate inventory (25 May 1653) lists "48 Akers land at Brantree, and Marsh in the possession of John Gurney," enumerated **separately** from the Tyng "Salters Farme" (the ~500-acre Mount Wollaston farm John Read carried under a ten-year agreement from 14 April 1639 and Gregory Belcher leased in 1657). John's 48 acres were therefore a distinct Tyng holding, and his tenancy was already running at Tyng's death — not begun afterward. *Suffolk Deeds, Liber IV* describes the messuage as "in the Occupation and by lease in the hands of John Gurney." Tenant, not owner. The figure is 48 acres at primary level (a later NPS cultural-landscape report's 45 acres is looser). | NEHGR 30:432; *Suffolk Deeds. Liber IV* |
| Deposition, Wilson v. Faxon ("aged about 50") | 17 March 1652/3 | A same-place age witness placing John at Braintree; implies birth ~1602/3 if the stated age is close (to be reconciled with the c.1607–12 band). | Suffolk Court Files 188; NEHGR 62:94 |
| Sold Braintree house & orchard to Richard Thayer (£14) | 12 February 1661 | House, orchard, a five-acre Monatiquot-River parcel, and an adjacent half-acre; deed witnessed by son John Jr. | Bates, *Ancient Iron Works* |
| Accepted to a Mendon allotment | 1662 | Among Braintree men accepted to allotments; later proprietors' records list John Gurny and (after his death) Grisel Gurney as twenty-acre lot holders, with house-lot/meadow/swamp-lot title references. | Ballou; Mendon Proprietors' Records |
| Death; estate inventory taken | 1662/3; inventory 16 March 1662/3 | Inventory £55 14s 6d; included a frontier land interest "at Quinapaug wch we know not." | SPR Case 338; NEHGR 12 |
```
`new_string`:
```
A plain-reading colonial chronology, arrival to estate inventory. Dates are given in modern (New Style) years; the records' Old-Style dual years (e.g. 1661/2, 1662/3) are simplified here and carried in the footnotes.

| Event | Date | Detail |
|---|---|---|
| Arrives in Weymouth | c. 1636–May 1641; most likely 1638–1640 | Bounded by two records: John is absent from the 1636 Weymouth property list (so he arrived after it), and he is present at Weymouth in the 30 May / 2 June 1641 gunpowder matter (so before it). The later part of that range (1638–1640, the height of the Great Migration) is when Weymouth's largest influx came.[^mbcr-gurney-1641][^msa-colonial-porter] |
| Obtains Weymouth land grants in the East Field and Mill Field | c. 1637–1642; best estimate 1639–1641 | The grants are undated. John is the first grantee of three parcels: two two-acre lots in the East Field and one four-acre lot in the Mill Field, about eight acres in all. He is absent from the 1636 Fresh Pond great-lot roll, which argues against a 1636 presence, while c. 1639–1641 fits Weymouth's new-settler influx and his first appearance in 1641.[^nash-weymouth-1885][^weymouth-msbook] |
| Gets a gunpowder fine cancelled | 30 May / 2 June 1641 | John, with James Ludden and Richard Porter of Weymouth, was fined for not keeping the gunpowder the law required; the three asked the court to cancel the fines, and it did. His first solid record in the colony.[^mbcr-gurney-1641][^msa-colonial-porter] |
| Surrenders Weymouth land grants in the East Field and Mill Field | c. 1639–1643; best estimate c. 1641–1643 | All three parcels pass from John to other settlers (the East Field lots to Robert Randoll and Nathaniel Addames, the Mill Field lot under Thomas Richardes), each recorded as "first granted/given to John Gurny/Gurnie."[^nash-weymouth-1885][^weymouth-msbook] |
| Appears in the 1643 Weymouth land inventory | c. 1643 | The c. 1643 possession register records the parcels under their new holders. The "1643" date is an estimate: it cannot be earlier than William Fry's death (26 October 1642), yet records property events into 21 May 1644, so Nash settles on 1643.[^nash-weymouth-1885] |
| Settles a £5 debt for the former minister | 30 October 1644 | The colony counts John's bill for £3 16s 4d, with Thomas Lake's note for £1 3s 8d, as the £5 owed by Mr. Jenner (Rev. Thomas Jenner), Weymouth's former minister. A paper-and-credit tie; the bill's purpose is unstated.[^ginner-jenner-2026-06] |
| Moves from Weymouth to Braintree | c. 1640–1645; best estimate c. 1642–1644 | His Weymouth parcels were gone by 1643 and he was at Braintree by 1645, so the move falls in that span.[^hist-weymouth-g13] |
| Signs petition for the new plantation at Braintree | May 1645 | Signed the petition, a marker of established Braintree standing.[^braintree-petition-g13] |
| Leases a 45-acre Tyng farm (later the Adams Old House) | 1647, for ten years | William Tyng leased John a 45-acre Braintree farm in 1647 for ten years; the northern part of "the Gurney farm" later became the Adams family seat in Quincy.[^nps-clr-g13] |
| Receives Weymouth land grant for Great lot no. 16 | 2 February 1652 | A new Weymouth grant in the Second Division, separate from the 1640s East/Mill Field parcels. Like his earlier parcels, this lot was later given to other men, though the record does not say when.[^nash-weymouth-1885] |
| Gives testimony for Wilson v. Faxon | 17 March 1653 | A deposition in a Braintree-context suit; the file reads "John Gurney of Brayntree aged 50 Yeares or thereabouts."[^nehgr-62-94] |
| Holds the 45/48-acre Tyng farm | 25 May 1653 | The Tyng probate inventory records the farm "in the possession of John Gurney" — 45 acres per the NPS/Sargent reading, 48 acres per the NEHGR abstract — separate from the larger Tyng "Salters Farme" (the ~500-acre Mount Wollaston farm leased to John Read 1639–49 and Gregory Belcher from 1657). Tenant, not owner.[^nehgr-30-432-g13][^suffolk-deeds-liber-iv] |
| Witnesses and appraises Gregory Baxter's estate, Braintree | June–July 1659 | John witnessed Baxter's will (with Moses Paine and Richard Brackett) and helped take the inventory (7 July 1659), a sign of community trust.[^anderson-gmb-baxter] |
| Receives grant for 10 acres in Billerica | 15 August 1659 | Granted a ten-acre house-lot on condition he settle it himself; the town accepted "his son Richard" as a fellow inhabitant. He never moved there.[^billerica-grant-2026-06][^hazen-billerica] |
| Appears in the Billerica Dudley Farm rate | 10 September 1659 | Assessed £2 5s 10d toward the half-payment for the Dudley Farm purchase, though the record shows he did not reside there.[^hazen-billerica] |
| Receives two Billerica meadow lots | c. 1659 | Two great-meadow lots laid out to John (4¼ acres at James Paterson's bounds; 4½ acres at the mouth of Horse Brook). Undated in the town book but within the 1659 division cycle.[^billerica-followup-2026-06] |
| Holds a Billerica share through two other men | November 1659 | In the upland division (39 lots, 40 persons), Peter Brackett and Joseph Thompson hold "the right of John Gurney, of Braintree" — an absentee share, not a personal lot.[^hazen-billerica] |
| Surrenders Billerica grant | December 1659 | Daniel Shed, "in answer for his father John Gurney," gave the house-lot back; half was re-granted to John Hall in March 1659/60. John never relocated.[^billerica-grant-2026-06][^billerica-followup-2026-06] |
| Still leases the Tyng farm | 28 March 1661 | The Tyng estate-division names John as sitting tenant of the same farm; he kept leasing it from Tyng's daughters Bethia and Mercy until 1662 — one continuous tenancy from 1647.[^tyng-dated-2026-06][^nps-clr-g13] |
| Sells Braintree house & orchard to Richard Thayer | 12 February 1662 (16 April 1662) | His own freehold: house, orchard, a five-acre Monatiquot-River parcel, and an adjoining half-acre, for £14; possession given 16 April 1662; signed by mark, witnessed by Peter Brackett and John Rockwell.[^thayer-deed-full-2026-06][^bates-ironworks-gurney] |
| Accepts a Mendon allotment | 1662 | Among Braintree men accepted to allotments at the new Mendon plantation.[^ballou-milford-1882] |
| Gives up the Tyng farm | c. 1662 | The Tyng-farm lease ended around 1662; with the farm given up and his freehold sold, his 1663 estate inventory shows no land.[^nps-clr-g13] |
| Dies; estate inventory taken | c. 1663; inventory 16 March 1663 | Inventory £55 14s 6d, taken by Gregory Belcher, Edmund Quincy, and Thomas Faxon; included a frontier land interest "at Quinapaug wch we know not."[^spr-case-338-john-gurney-probate][^nehgr-12-suffolk-wills]
```

---

## Item 2 — Assimilate the Weymouth three-parcel and Tyng/Adams findings into the prose — PROMOTE

**2a. Weymouth three-parcel correction.** `str_replace`:

`old_string`:
```
John's colonial land trail runs Weymouth → Braintree → the Mendon frontier. The Weymouth phase is earlier and more residential than the bare lot-list implies: Nash's Appendix C is the **1643** property record, and John's East Field (p. 258) and Mill Field (p. 278) parcels are "first granted to John Gurny/Gurnie" but already in other men's hands by 1643, with the great-lot entry (p. 282) the later 2 February 1651-52 Second Division.
```
`new_string`:
```
John's colonial land trail runs Weymouth → Braintree → the Mendon frontier. The Weymouth phase is earlier and more residential than the bare lot-list implies: Nash's Appendix C is the **1643** property record, and the manuscript Land Grants book (film 007009659) confirms John as original grantee of **three** distinct parcels — two two-acre East Field lots (ms p. 12 under Robert Randoll, "John Gurny"; ms p. 23 under Nathaniel Addames, "John Gurnie") and one four-acre Mill Field lot (ms p. 31 under Thomas Richardes, "John Gurnie"), about eight acres in all — all "first granted/given to" John but already in other men's hands by 1643, with the great-lot entry (p. 282) the later 2 February 1651-52 Second Division. Full place records: [East Field](https://github.com/allengurney/gurney-genealogy/blob/main/research/places/east-field-weymouth-ma.md), [Mill Field](https://github.com/allengurney/gurney-genealogy/blob/main/research/places/mill-field-weymouth-ma.md).[^weymouth-msbook]
```

**2b. Tyng leasehold → the 1647–1662 / Adams farm account** (replaces the brief Braintree-leasehold paragraph). `str_replace`:

`old_string`:
```
The Braintree evidence is leasehold and community-context evidence, not ownership proof. *Suffolk Deeds. Liber IV* records one Ting/Tyng estate property at Braintree as occupied "by lease" by John Gurney, matching the existing Tyng-property context while identifying the legal setting more precisely.[^suffolk-deeds-liber-iv]
```
`new_string`:
```
The Braintree evidence is leasehold and community-context evidence, not ownership proof — but the leasehold is now dated and located. In **1647 William Tyng leased John a 45-acre Braintree farm for ten years**; John kept leasing it from Tyng's daughters **Bethia and Mercy until 1662**, so it is one continuous tenancy (~1647–1662), the same property recorded in the 1653 Tyng inventory ("in the possession of John Gurney," 45 acres per the National Park Service/Ezekiel Sargent reading, 48 per the *NEHGR* abstract) and in the 28 March 1661 Tyng estate-division indenture. The northern portion of "the Gurney farm" later became the **Adams family seat** in Quincy — the Old House (Peace field), acquired by the Adamses in 1787, beside the birthplaces of Presidents John Adams and John Quincy Adams. It was distinct from the larger ~500-acre Tyng farm (Salter's Farm / Mount Wollaston, leased to John Read then Gregory Belcher), and from John's own Monatiquot freehold. Full place record: [the leased Tyng farm](https://github.com/allengurney/gurney-genealogy/blob/main/research/places/gurney-tyng-farm-quincy-ma.md).[^suffolk-deeds-liber-iv][^nps-clr-g13]
```

**2c. Assimilate the "Further primary records" Tyng paragraphs** (the two paragraphs framing the 1661 leasehold as a possibly-separate "second tenement" are superseded by the same-property/1647 finding). `str_replace`:

`old_string`:
```
**New instrument — John Gurney held a second Braintree tenement *by lease* from the Tyng family.** The Tyng estate-division indenture recited in Suffolk Deeds Lib. IV (pp. 6 and 89a–90) describes two messuages or tenements in Braintree allotted to Bethia and Mercy Tyng: "one of them is now in ye occupation & by lease in the hands of Gregory Belshare [Belcher]: the other in the Occupation and by lease in the hands of **John Gurney both of Braintree aforesaid**." A John Gurney as leasehold tenant of a Tyng messuage — paired with Gregory Belcher, one of Braintree's most prominent settlers — is a wholly new tenure record: it shows the household renting a substantial tenement alongside (or after selling) the five-acre freehold. Whether the lessee is G13 or his son John Jr. depends on the indenture's date, not yet read (William Tyng died 1653; the reciting deeds sit in the 1661–1671 registry window); the page images are an open pull.[^tyng-lease-2026-06]

- **The Tyng leasehold is dated.** The Tyng division is an "Indenture Quadriparte, bearing date the eight and Twenteth day of march … one Thousand Six hundred Sixty one" (28 March 1661), made when Capt. William Tyng's four daughters came of age (he died with "noe male Children then living," his whole landed estate to the daughters). The Braintree messuage "in the Occupation and by lease in the hands of John Gurney" is therefore a **March 1661 snapshot of G13 alive and leasing a Tyng tenement** — paired with Gregory Belcher's — while still holding the five-acre freehold he sold the following February. The final-years tenure picture now reads: freehold + Tyng leasehold (March 1661) → freehold sold (12 Feb 1661/2) → death (1662/3).[^tyng-dated-2026-06]
```
`new_string`:
```
**The Tyng leasehold is the same 45-acre farm, held continuously ~1647–1662 — the future Adams seat.** The National Park Service *Cultural Landscape Report* (1997), drawing on the Ezekiel Sargent manuscripts (Quincy Historical Society, "Land Formerly of William Tyng"), dates and locates the tenancy: William Tyng leased John a 45-acre Braintree farm in **1647 for ten years**, and John "continued to lease the farm from Tyng's daughters, Bethia and Mercy until 1662." The 28 March 1661 Tyng estate-division indenture — "Indenture Quadriparte … the eight and Twenteth day of march … one Thousand Six hundred Sixty one," made when Capt. William Tyng's daughters came of age — names John as the sitting tenant of that same farm, paired with Gregory Belcher on the larger Salter's Farm. So the 1653 inventory and the 1661 indenture are two snapshots of one continuous lease, not a second separate tenement; the lessee is G13 (named "of Braintree," with the farm passing to Bethia and Mercy). The northern portion of "the Gurney farm" became the Adams Old House (Peace field), acquired by the Adams family in 1787, beside the Adams Birthplaces of the second and sixth U.S. presidents. The final-years picture: the Tyng-farm leasehold (1647–1662) running alongside the Monatiquot freehold John sold 12 Feb 1661/2, then his death (1662/3). Full place record and the 45-vs-48-acre discrepancy: [the leased Tyng farm](https://github.com/allengurney/gurney-genealogy/blob/main/research/places/gurney-tyng-farm-quincy-ma.md).[^nps-clr-g13][^tyng-dated-2026-06]
```

---

## Item 3 — Replace the scattered Billerica passages with one cohesive section — PROMOTE

Three passages currently hold Billerica (the Hazen rate paragraph in "Community and probate records," and the two "Further primary records" paragraphs). Consolidate into one section in place of the Hazen paragraph; remove the two "Further primary records" paragraphs (their content moves into the consolidated section). The validated pre-draft `sources/intake/new/g13-billerica-synthesis-predraft.md` is the source; reject it (its content lands here) and Phase 2 deletes the pre-draft.

**3a. Replace the Hazen paragraph with the consolidated section.** `str_replace`:

`old_string`:
```
Hazen's Billerica history gives a separate 1659 town-finance context. On the 10 September 1659 rate for the half payment of the Dudley Farm purchase, John Gurney appears with an assessment of 2-5-10. Hazen explains that the Dudley Farm price was 110 pounds and that the remaining balance of the 55-pound half payment was probably assessed on later town purchasers. This links John to the Billerica purchase-rate context, but it should not be inflated into proof of permanent Billerica residence without the underlying town and land records.[^hazen-billerica]
```
`new_string`:
```
#### John Gurney and Billerica (1659–1660)

John Gurney appears in the Billerica records only across about seven months in 1659–60, always as "John Gurney of Braintree." He took up a proprietor's place in the new town's first land divisions but never moved there: within four months he handed the house-lot back, and the rest of his interest was a paper share other men held for him. No record places him living in Billerica or shows any Billerica land becoming a lasting Gurney holding.

On **15 August 1659** the town granted John a ten-acre house-lot on the express condition that he "come and inhabit the said Lott himselfe," and at his request accepted **his son Richard** — Richard G12, of settling age in 1659 — as a fellow inhabitant; a 56-acre layout (bounded by William Browne and William Hamlett) went with it. He was carried as a full proprietor: in the lot-draw list ("John Gurney I"), with a house valued at £3, town charges of 10s 7d, and a rate of £2 5s 10d toward the half-payment for the Dudley Farm purchase — the same rate Hazen's printed history records under 10 September 1659.[^billerica-grant-2026-06][^hazen-billerica] In the **November 1659 upland division** (thirty-nine lots among forty persons, east of the Concord River below the great bridge) John did not take a lot in person: **Peter Brackett and Joseph Thompson held "the right of John Gurney, of Braintree" in common** — the clearest sign he was an absentee proprietor. The town also laid out to him two great-meadow lots (4¼ acres at James Paterson's bounds; 4½ acres at the mouth of Horse Brook, John Rogers to the south).[^hazen-billerica][^billerica-followup-2026-06] On **26 December 1659** he gave the house-lot back: **Daniel Shed, "in answer for his father John Gurney,"** surrendered it to the town, and one half was re-granted to John Hall on 19 March 1659/60. Daniel Shed had married John's daughter Mary in 1647, so John was his father-in-law — a Shed–Gurney tie no compiled genealogy states.[^billerica-grant-2026-06][^billerica-followup-2026-06][^shedd-1920-mary-bounding]

The episode reads as a relocation explored and dropped: John took up a proprietor's place to settle his son Richard, was assessed and laid out lots, then surrendered the house-lot before year's end, handing it off through his son-in-law. Every dated Billerica record (1659–60) is John Sr. of Braintree; no record names a John Jr. there (John Jr. is documented at Weymouth and Mendon). A few undated abuttal entries still describe land by John Gurney's name, so a Gurney interest could in principle have lingered, but there is no positive evidence any Billerica parcel passed to John Jr. or was occupied by a Gurney. **Peter Brackett** ties the threads together: he held John's Billerica right (1659), witnessed John's 1661/2 Thayer deed, was a creditor of the 1663 estate, and was a Braintree man tied to the Mendon purchase. (An earlier reading of a degraded accounts page as "Gurney Tanner" is a dead OCR garble of "Towne Charges" — there was no tanner.) Full place record: [Billerica](https://github.com/allengurney/gurney-genealogy/blob/main/research/places/billerica-ma.md).[^hazen-billerica][^billerica-followup-2026-06][^spr-case-338-john-gurney-probate]
```

**3b. Remove the two superseded "Further primary records" Billerica paragraphs** (now in the consolidated section). `str_replace`:

`old_string`:
```
**Billerica, August–December 1659 — the grant entry read in full: John Gurney's son Richard named, and the lot surrendered.** Working transcription (town book, image 173): "15.6.59 [15 August 1659] John Gurney is Granted a te[n] acor Lott upon condition[] that he does come and inhabit the said Lott himselfe, and the Towne doe upon his request except [accept] of **his son Richard** as an inhabitant to set down with him upon what [par]t of the Lott that the said John please to settle him upon. 26.10.1659 [26 December 1659] **Daniel Shead in answer for his father John Gurney; the said John Gurney surrendred up the Lott**: It is granted unto him by the towne as above said…" Three observations. (1) The grantee John Gurney had a **son Richard** of settling age in 1659 — matching Richard G12 (b. c.1630–34) exactly. (2) **Daniel Shed** — the Braintree man who became a Billerica founder — answers "for his father John Gurney"; in period usage that most naturally makes John his father-in-law (or stepfather), a Shed–Gurney family tie no compiled source states. (3) John **surrendered** the lot within four months — he never moved; the relocation was explored and abandoned in the year before he sold the Braintree freehold (Feb 1661/2) and died (1662/3). The town book nonetheless carries further John Gurney matter — the rate entry (2-5-10, image 14), "John Gurney for ye house 3-0-0" in a valuation list, abuttals ("John Gurney South and ye ministers Land…"; "bounded with Will Brown … & John Gurney North"), "John Gurney, [l]ayed out to him four acors and a quarter," and a possible "Gurney Tanne[r] Charges" line — so either the surrendered grant was re-granted and held, or a John Gurney (Jr.?) had a continuing Billerica interest; the surrounding pages need reading before choosing.[^billerica-grant-2026-06]

**Billerica (L-104) — the surrendered lot was re-granted, and John Gurney's footprint was larger than "explored and abandoned" implies.** After John Gurney surrendered his ten-acre Billerica house-lot (26 December 1659; Daniel Shead "in answer for his father John Gurney"), the town **re-granted one half of it to John Hall on 19 March 1659/60** ("the Towne Doe grant to John Hall one halfe of the Lot yt was granted to John Gurney"); no second-half recipient is recorded. But Gurney was not a mere transient applicant: the town book carries him in the proprietors' lot-draw list ("John Gurney I"), a house valuation of £3, a rate of £2 5s 10d and town charges of 10s 7d (autumn 1659), the 56-acre layout named in the surrender entry, and **two great-meadow lots** — 4¼ acres "beging at the bonds of James Paterson" and 4½ acres at "the mouth of Horse Brook bounded with John Rogers South." The "Gurney Tanner" reading previously flagged is a **dead OCR garble of "Towne Charges"** — image 13 reads the same list cleanly, "John Gurney : Towne Charges of -10-7"; there is no tanner occupation for any Billerica Gurney. The Shead tie recurs (Daniel Shed sequential with Gurney in the proprietors list; "Sheads corner" a survey landmark; a Nathan Shead still an assessor in 1707).[^billerica-followup-2026-06]

```
`new_string`:
```
```

---

## Item 4 — Add the Boston / Book of Possessions negative — PROMOTE

Bears on Anderson's unverified "Boston" settlement attribution. Insert after the Baxter probate-roles paragraph, before the Suffolk-probate-index paragraph. `str_replace`:

`old_string`:
```
The Suffolk probate index for vol. 2, G to O, identifies the Gurney/Gurny probate-index entry for John Gurney/Gurny administration case no. 338 in the 1663 context.
```
`new_string`:
```
John Gurney is **absent from the Boston Town Records and Book of Possessions, 1634–1660.** A broad Gurney-variant sweep of the published transcription (the 1881 Record Commissioners' *Second Report*) — confirmed across two independent text copies — returns no Gurney in any spelling; the body reaches 1659–1660 and includes the Book of Possessions. The "Garnsey" that appears in the FamilySearch manuscript-film index is the distinct **Garnsey/Guernsey** family (Henry Garnsey of Dorchester, died 1692), not Gurney. William Tyng (Boston's treasurer) and John Newgate are pervasive, but John Gurney holds no Boston land in the definitive landholder list — a clean negative against Anderson's "Boston" settlement, consistent with that attribution tracking the 1636 Newgate apprentice rather than the Braintree John. (The FamilySearch manuscript itself, film 007939452, of different page count, was not read directly; a wider survey of pre-1650 Boston / Massachusetts Bay collections remains open, lead L-193.)[^boston-possessions-g13]

The Suffolk probate index for vol. 2, G to O, identifies the Gurney/Gurny probate-index entry for John Gurney/Gurny administration case no. 338 in the 1663 context.
```

---

## Item 5 — Add the five new companion footnote definitions — PROMOTE

Insert after the `[^hazen-billerica]` definition. `str_replace`:

`old_string`:
```
[^hazen-billerica]: Henry A. Hazen, [*History of Billerica, Massachusetts, with a Genealogical Register*](https://archive.org/details/historyofbilleri00hazen) (Boston: A. Williams and Co., 1883), historical p. 33 / image p. 54, Internet Archive. Source ID: `hazen-billerica-1883`.
```
`new_string`:
```
[^hazen-billerica]: Henry A. Hazen, [*History of Billerica, Massachusetts, with a Genealogical Register*](https://archive.org/details/historyofbilleri00hazen) (Boston: A. Williams and Co., 1883), historical pp. 33–34 / image p. 54 (the 10 September 1659 Dudley-Farm rate and the November 1659 upland division, "Peter Bracket and Joseph Tompson holding in common the right of John Gurney, of Braintree"), Internet Archive. Source ID: `hazen-billerica-1883`.
[^weymouth-msbook]: Weymouth proprietors' Land Grants book (manuscript), FamilySearch film 007009659, images 00135 (ms p. 12, "John Gurny" under Robert Randoll), 00140 (ms p. 23, "John Gurnie" under Nathaniel Addames), 00144 (ms p. 31, "John Gurnie" under Thomas Richardes); extract at [`sources/corpus_supplement/weymouth-land-grants-book-1643-gurney-manuscript-extracts.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/weymouth-land-grants-book-1643-gurney-manuscript-extracts.md). Source ID: `weymouth-land-grants-book-ms`.
[^nehgr-30-432-g13]: Capt. William Tyng inventory abstract, *New England Historical and Genealogical Register*, vol. 30 (1876), p. 432 ("48 Akers land at Braintree and Marsh in possession of John Gurney"; the NPS/Sargent reading of the same inventory gives 45 acres). Source ID: `nehgr-30-432`.
[^nps-clr-g13]: National Park Service, *Cultural Landscape Report, Adams National Historic Site* (1997), pp. 12–13 (Site Chronology) and Figure 1, "William Tyng's 45-acre farm, Braintree, 1649," citing the Ezekiel Sargent manuscripts (Quincy Historical Society, "Land Formerly of William Tyng"); [npshistory.com/publications/adam/clr-1997.pdf](https://npshistory.com/publications/adam/clr-1997.pdf); extract at [`sources/corpus_supplement/nps-adams-clr-1997-gurney-tyng-extracts.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/nps-adams-clr-1997-gurney-tyng-extracts.md). Source ID: `nps-adams-nhp`.
[^hist-weymouth-g13]: *History of Weymouth, Massachusetts* (Weymouth: Weymouth Historical Society, 1923), vol. 3, John Gurney family entry (the Weymouth→Braintree move). Source ID: `history-of-weymouth`.
[^braintree-petition-g13]: Petition of the inhabitants for the new plantation at Braintree (Mount Wollaston), May 1645, in the colonial petition record; firm primary page not yet pinned (lead L-191). Source ID: `history-of-weymouth`.
[^boston-possessions-g13]: *Second Report of the Record Commissioners of the City of Boston: Boston Town Records, 1634–1660, and the Book of Possessions*, 2nd ed. (Boston, 1881), [Internet Archive `secondreportofre00bost`](https://archive.org/details/secondreportofre00bost). A broad Gurney-variant sweep (the Modern variant set plus OCR-garble forms, fuzzy-matched) of the body text — run on two independent copies (the Internet Archive text and a second download at `sources/intake/new/pdfs/secondreportofre00bost.txt`) — returns no Gurney in any spelling; the body reaches 1659–1660 and carries the Book of Possessions. The "Garnsey" in the FamilySearch film index is the separate Garnsey/Guernsey family (Henry Garnsey of Dorchester). Source ID: `boston-town-records-1634-1660`.
```

---

## Item 6 — Refresh the Billerica place file — PROMOTE

`research/places/billerica-ma.md` still frames Billerica via the Hazen rate alone and lists "Open items" the manuscript sweep already answered. Replace the framing paragraph and the open-items list.

**6a.** `str_replace`:

`old_string`:
```
Billerica enters the John Gurney-1 research library through the Dudley Farm purchase-rate context rather than through a proved residence or family event.

## John Gurney and the 1659 Dudley Farm rate

Hazen's printed Billerica history gives the 10 September 1659 rate list for the half payment of the Dudley Farm purchase. John Gurney appears in the list with an assessment of 2-5-10. Hazen frames the list as fulfilling the agreement that later inhabitants should repay the original farm proprietors one-half of the farm's cost. The Dudley Farm price was 110 pounds, so the half-payment target was 55 pounds; Hazen adds that the balance of that 55 pounds was probably assessed on later town purchasers.[^hazen-billerica]

This is a useful expansion of John Gurney's Massachusetts geography, but it should be handled carefully. The printed list shows participation in a purchase-rate assessment connected to Billerica; it does not, without the underlying town record and related land records, prove that John permanently resided there or held a specific parcel.

[^hazen-billerica]: Henry A. Hazen, *History of Billerica, Massachusetts, with a Genealogical Register* (Boston: A. Williams and Co., 1883), historical p. 33 / image p. 54, [Internet Archive](https://archive.org/details/historyofbilleri00hazen). Source ID: `hazen-billerica-1883`.

## Open items

- [ ] Pull the underlying Billerica town record for the 10 September 1659 Dudley Farm rate.
- [ ] Check whether John Gurney appears in any Billerica land, tax, or proprietors' records after the 1659 assessment.
- [ ] Reconcile this Billerica lead with the existing Weymouth/Braintree chronology before adding stronger residence language.
```
`new_string`:
```
John Gurney's whole Billerica footprint falls in about seven months of 1659–60, always as "John Gurney of Braintree." He took up a proprietor's place in the new town's first land divisions, surrendered the house-lot within four months, and never moved there; nothing became a lasting Gurney holding.

## John Gurney at Billerica, 1659–1660

The manuscript town book and Hazen's printed history together give the full picture: a ten-acre house-lot granted 15 August 1659 on condition John settle it himself, with his son Richard accepted as a fellow inhabitant; a £3 house valuation, town charges of 10s 7d, and the £2 5s 10d Dudley-Farm rate of 10 September 1659; an absentee share in the November 1659 upland division, where Peter Brackett and Joseph Thompson held "the right of John Gurney, of Braintree"; two great-meadow lots (at James Paterson's bounds and the mouth of Horse Brook); and the surrender on 26 December 1659, when Daniel Shed — John's son-in-law — answered "for his father John Gurney," after which half the lot was re-granted to John Hall. Full treatment and citations on the [John Gurney (G13) companion](https://github.com/allengurney/gurney-genealogy/blob/main/research/people/g13-john-gurney-fact-sheet.research.md); manuscript extract at [`billerica-town-records-gurney-1659-1660.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/billerica-town-records-gurney-1659-1660.md).
```

---

## Item 7 — Mendon place file: record John's 1662 allotment — PROMOTE

`research/places/mendon-ma.md` notes only Grissell's post-death application. Add John's own 1662 acceptance. `str_replace`:

`old_string`:
```
- Detail: Grissell applied for John's Mendon lot after his death (NEHGR 22:44).
```
`new_string`:
```
- Detail: John Gurney was accepted to a Mendon allotment among Braintree men in 1662; Grissell applied for his Mendon lot after his death (NEHGR 22:44). Mendon was not incorporated until 15 May 1667, so the post-incorporation proprietor entries for John Gurny and Grisel Gurney are retrospective.
```

---

## Source tracking

All sources cited here are already registered (`nash-historical-sketch-weymouth-1885`, `mbcr-gurney-1641`→`massachusetts-bay-records-v1-1853`, `massachusetts-state-archives-colonial`, `nehgr-62-94`, `suffolk-deeds-liber-iv-1888`, `anderson-gmb-baxter`→`anderson-great-migration-begins-v1-baxter`, `hazen-billerica-1883`, `billerica-town-records-ms`, `ballou-history-of-milford-1882`, `spr-case-338-john-gurney-probate-1663`, `nehgr-12-suffolk-wills-1858`, `bates-ancient-iron-works-braintree-1898`, `mendon-proprietors-records-1899`, `shedd-daniel-shed-genealogy-1920`, `familysearch-fulltext-search`, `history-of-weymouth`) **plus** the v120 additions (`weymouth-land-grants-book-ms`, `nps-adams-nhp`) and one new source for the Boston volume:

- **New sourceId `boston-town-records-1634-1660`** (referenced by `[^boston-possessions-g13]`): add to `data/sources.json` —
```
    "boston-town-records-1634-1660": {
      "shortTitle": "Boston Town Records 1634-1660 (Book of Possessions)",
      "citation": "Second Report of the Record Commissioners of the City of Boston: Boston Town Records, 1634-1660, and the Book of Possessions. 2nd ed. Boston, 1881.",
      "archive": "Internet Archive",
      "url": "https://archive.org/details/secondreportofre00bost",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/boston-town-records-1634-1660.md",
      "notes": "Broad Gurney-variant sweep of the body (Modern set + OCR garbles, fuzzy), confirmed on two independent text copies (IA + sources/intake/new/pdfs/secondreportofre00bost.txt): NEGATIVE for Gurney in any spelling; body reaches 1659-1660, Book of Possessions present. The FS-index 'Garnsey' = the separate Garnsey/Guernsey family of Dorchester, not Gurney. William Tyng and John Newgate pervasive. Bears on Anderson's unverified 'Boston' settlement (lead L-193). FS manuscript film 007939452 not read directly."
    },
```
- **New validation `sources/validations/boston-town-records-1634-1660.md`:**
```
# Validation — Boston Town Records 1634-1660 (Book of Possessions)

**Source ID:** `boston-town-records-1634-1660`

**What was examined.** The published *Second Report of the Boston Record Commissioners* (1881), Internet Archive `secondreportofre00bost` (the transcription of the manuscript on FamilySearch film 007939452), including the Book of Possessions and the index. Full text downloaded and searched June 2026.

**What portion.** Whole volume (19,480 lines), searched for the full Gurney variant set and Garnsey/Guernsey, exact and fuzzy.

**What remains uncertain.** The login-gated FamilySearch manuscript image (film 007939452) was not opened directly; the published transcription is the authoritative proxy. The FS film's own index entry "Garnsey" should be eyeballed at the image to confirm it points to the Guernsey/Garnsey family.

**Where findings landed.** `research/people/g13-john-gurney-fact-sheet.research.md` (the Boston/Book-of-Possessions negative). Lead L-193 tracks the wider Boston/Mass Bay collection survey.
```

## Items rejected / consumed
- `sources/intake/new/g13-billerica-synthesis-predraft.md` — **consumed**: its content is assimilated into Item 3; Phase 2 deletes the pre-draft file.

## Leads
No new leads. L-182/L-144/L-192/L-193 already updated live in the thread (see v120 for state).
