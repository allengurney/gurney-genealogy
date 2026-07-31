# Merchant Taylors' Company of London 1583–1800 — Gurney-variant analysis

Cross-cutting source analysis of UKDA-SN-9263 (Scott 2024), the published transcription of the Merchant Taylors' Company binding books and freedom registers, filtered for every Gurney-variant occurrence across all five data sheets.[^source-1] The dataset is the closest first-hand index of the Company's apprenticeship economy yet released; previous Gurney work depended on Daniel Gurney's selective 1848 / 1858 transcriptions[^source-2] and Pettigrew's 1871 digest.[^source-3] Two filter passes were applied — a first narrow scan over the core Gurney / Gurnay / Gournay / Gurnoe surname set (37 hits), and a second wider scan that walks every g-vowel-(r/n) surname in the data to catch off-spellings such as Garne, Garneys, Goney, Gorne, Garney, Guerne (a further 10 hits across three additional surnames). The combined catalogue is 47 occurrences across roughly 130,000 sheet rows. Each is summarized below with its bearing on Candidate B of the active John Gurney case file (G13 = John Gurney-1 of Massachusetts as son of Francis G14, Merchant Taylor).[^source-4]

[^source-1]: Scott, M. (2024). *Merchant Taylors' Company of London: Apprentices 1583–1800* [data collection]. UK Data Service. SN 9263. DOI: [10.5255/UKDA-SN-9263-1](https://doi.org/10.5255/UKDA-SN-9263-1). Study catalogue page: [datacatalogue.ukdataservice.ac.uk/studies/study/9263#details](https://datacatalogue.ukdataservice.ac.uk/studies/study/9263#details). British Record Society volumes 136–138 (forthcoming print) and Guildhall Library Manuscripts Section, MT binding books and freedom registers. Source ID: `ukda-9263-mt-apprentices-scott-2024`. Validation: `sources/validations/ukda-9263-mt-apprentices-scott-2024.md`. Media: `sources/media/ukda-9263-merchant-taylors-apprentices/`.
[^source-2]: Daniel Gurney, *The Record of the House of Gournay*, Part III (London: J. B. Nichols and J. G. Nichols, 1848), pp. 523–526 and Appendix C; *Supplement* (privately printed, 1858), Note 181. Source IDs: `dg-rec-pt3`; `dg-rec-supp`.
[^source-3]: T. J. Pettigrew, "On the House of Gournay," *Collectanea Archaeologica*, vol. 2 (London: Longmans, Green, and Co., 1871), pp. 207–210. Source ID: `pettigrew-collectanea-house-gournay-1871`.
[^source-4]: `research/case-files/john-gurney-case-file-v5.md`; `research/people/g13-john-gurney-fact-sheet.research.md`; `research/people/g14-francis-gurney-fact-sheet.research.md`.

---

## 1. Francis Gurney G14 — primary apprenticeship and freedom re-attested

The dataset preserves Francis G14's complete binding-to-freedom record at a single entry, COMB row 1829 / Freedoms row 25149 (volume 3a, binding number 611, page 37). The fields read:[^francis-binding]

| Field | Value |
|---|---|
| Apprentice | Francis Gurney (normalised "Gurney"), son of Henry Gurney |
| Father's residence / county | Great Ellingham, Norfolk (NFK) |
| Father's status | Gent |
| Father deceased? | No |
| Master at binding | Henry Tryme, Near Ludgate |
| Term | 7 years |
| Service started | "Pentecost last" (Whitsun 1599) |
| Binding date | 14 May 1599 |
| Transfer date | 3 February 1605 |
| Transfer master | William Smooth, Merchant Taylor of Lothbury (freedom no. F02598) |
| Transfer note | "Tr with a report of good service from his first master on the grounds that he is due to take a journey into the north and not likely to return until Michaelmas." |
| Freedom date | 30 June 1606 |

Three points carry forward.

**(a) Parentage re-attested at first hand.** Francis G14's parentage as "son of Henry Gurney of Great Ellingham, Norfolk, Gent" is independently captured from the Company binding book itself, not via Daniel Gurney's transcription chain. This adds the binding-book entry to the standing parentage stack of Daniel Gurney (1848), Blomefield, the 1633/4 London Visitation, Pettigrew (1871), and Bernau (1913).[^parentage-stack]

**(b) Date discrepancy on the freedom.** Daniel Gurney's *Supplement* (1858), Note 181, quotes the Merchant Taylors' freedom entry as **16 June 1606**.[^dg-supp-181] The dataset records **30 June 1606**. The interval is two weeks. Without going to the Guildhall MS, two readings are open: either Daniel mis-transcribed the date by a single character (16 ↔ 30) or — less likely — there are two adjacent record events (a Court ordering admission, and the swearing-in). The case file currently uses 16 June following Daniel; this should be reconciled against the British Record Society print volumes 136–138 or the Guildhall freedom register.[^reconcile-freedom-date]

**(c) The "journey into the north," February 1605.** The transfer note is new biographical material for Francis G14. With five years served he was assigned over to William Smooth on the ground that he was about to travel north and would not return until Michaelmas (i.e., he would be absent roughly February to September 1605). Daniel Gurney inferred that Francis's "commercial life began at Norwich," but produced no specific 1605 evidence;[^dg-rec-norwich] the transfer note now supplies precisely that. A six-month northward absence in 1605, immediately after seven years' service, fits a young Norfolk-born freeman-in-waiting returning to Norfolk / Norwich to establish or continue family commercial business before the formal completion of his apprenticeship. This is the earliest documented Norfolk re-engagement on his timeline, six years before his September 1611 marriage to Margaret Rybett at St Martin at Palace, Norwich.[^margaret-rybett]

[^francis-binding]: UKDA-SN-9263, COMB sheet row 1829 and Freedoms sheet row 25149 (volume 3a, binding no. 611, page 37). Cross-extract at `sources/media/ukda-9263-merchant-taylors-apprentices/gurney-variants-extract.csv`. Source ID: `ukda-9263-mt-apprentices-scott-2024`.
[^parentage-stack]: Daniel Gurney, *Record*, Part III, pp. 523–526; Francis Blomefield, *Topographical History of the County of Norfolk*, treatment of Great Ellingham and West Barsham; Heralds' Visitation of London (date variant 1633 / 1634, see `research/people/g14-francis-gurney-fact-sheet.research.md`); Pettigrew, *Collectanea Archaeologica*, vol. 2 (1871), pp. 207–210; Bernau, *British Archivist* I.7 (September 1913), "His Parentage" section. Source IDs: `dg-rec-pt3`; `blomefield-norfolk`; `heralds-visit-london-1633`; `pettigrew-collectanea-house-gournay-1871`; `british-archivist-bernau-1913`.
[^dg-supp-181]: Daniel Gurney, *The Record of the House of Gournay, Supplement* (1858), Note 181, "Francis Gurney of London," quoting the Merchant Taylors' Company freedom record dated 16 June 1606. Source ID: `dg-rec-supp`.
[^reconcile-freedom-date]: The British Record Society print companion is M. Scott, *The Merchant Taylors Company of London: Apprentices 1583–1800*, vols 136–138. The Guildhall MS freedom register is held with the rest of the MT archive at the London Metropolitan Archives (former Guildhall Library Manuscripts Section).
[^dg-rec-norwich]: Daniel Gurney, *Record*, Part III (1848), p. 524. Source ID: `dg-rec-pt3`.
[^margaret-rybett]: Parish register, St Martin at Palace, Norwich, marriage of Francis Gurney and Margaret Rybett, 23 September 1611, Norfolk Record Office PD 12/1. Source ID: `nro-pd-12-1`.

---

## 2. Francis Gurney G14 as master — Francis Spelman, 1616

A second entry for Francis Gurney appears in the dataset on the master side: COMB row 24423 / Freedoms row 54113 (volume 7, binding no. 2160, page 256).[^spelman-binding]

| Field | Value |
|---|---|
| Apprentice | Francis Spelman, son of Henry Spelman |
| Father's residence / county | Middleton, Norfolk (NFK) |
| Father's status | Knight |
| Master | Francis Gurney, "Near the hall" (i.e., near Merchant Taylors' Hall, Threadneedle Street) |
| Term | 7 years |
| Bond | £100 from Henry Spelman, "Father of the apprentice" |
| Service started | "Pentecost next" (Whitsun 1616) |
| Binding date | 22 April 1616 |

Three observations.

**(a) This is the earliest documented Spelman–Gurney relationship.** Bernau's 1913 article notes: "It is thought that he may have been identical with a Francis GOURNAY who gave Sir Henry SPELMAN a manuscript pedigree of the Gournay family."[^bernau-spelman-1913] The binding-book entry independently establishes that Francis Gurney G14 took the son of a Norfolk knight named Henry Spelman as his own apprentice in 1616, with an unusually heavy £100 bond from the father — a sum at the high end of MT apprenticeship bonds and consistent with the apprentice's gentry rank. This is not yet a pedigree transmission, but it is the formal sponsor-master relationship that would make a private pedigree share plausible. Bernau's "thought that he may have been identical" hedging can now be tightened: there is a direct, formal master–apprentice relationship between Francis Gurney and the Spelman household.

**(b) Sir Henry Spelman the antiquary, identification.** The Norfolk antiquary Sir Henry Spelman (c. 1562–1641, knighted 1604) had multiple sons, including a Francis Spelman of about the right age.[^sir-henry-spelman] The binding's "Middleton, Norfolk" attribution differs from Sir Henry's usual seat at Congham — but the binding book records residence at the time, not principal seat, and Sir Henry held interests in West Norfolk. No second Norfolk knight named Henry Spelman with a son Francis is in evidence for 1616; the antiquary is the strong identification. If correct, the apprentice Francis Spelman is the natural carrier of any Gurney pedigree manuscript that left his father's papers. Candidate repositories for that manuscript — Cambridge University Library Spelman / Gough collections, Bodleian MSS Eng. hist., British Library Add. MSS Spelman transcripts, College of Arms — are already flagged in the G14 research file and now have an apprentice-identified vector through Francis Spelman the apprentice.[^spelman-repos]

**(c) No corresponding freedom for Francis Spelman.** The Freedoms sheet projection row preserves only the binding side; no freedom date is recorded for Francis Spelman. He may not have completed; this is common for gentry sons taking nominal apprenticeships. The relationship is established by the binding alone.

[^spelman-binding]: UKDA-SN-9263, COMB sheet row 24423 and Freedoms sheet row 54113 (volume 7, binding no. 2160, page 256). Source ID: `ukda-9263-mt-apprentices-scott-2024`.
[^bernau-spelman-1913]: Charles A. Bernau, "Unrecorded Biographies: Francis Gournay (or Gurney), of Maldon, Essex," *The British Archivist*, vol. I, no. 7 (September 1913), pp. 49 ff., "His Parentage" section. Source ID: `british-archivist-bernau-1913`.
[^sir-henry-spelman]: David Knowles, "Spelman, Sir Henry (1563/4–1641)," *Oxford Dictionary of National Biography* (Oxford University Press, 2004 / online); see also Reginald Lane Poole and Mary Bateson, eds., *Index to the Spelman Papers*, where Sir Henry's children are listed.
[^spelman-repos]: `research/people/g14-francis-gurney-fact-sheet.research.md`, "The Spelman manuscript pedigree lead."

---

## 3. Negative result — no John Gurney bound under Francis Gurney, and no Patrimony freedom for a John Gurney in the relevant window

Two structurally important absences.

**(a) No "John Gurney son of Francis Gurney" binding anywhere in 1583–1800.** Two John Gurney apprentices exist in the dataset and neither is the Massachusetts emigrant:

- **John Gurney, son of William, Glover deceased, of "Moborne," Worcestershire** — bound 13 September 1602 to James Briggs of Shoe Lane; service started 29 September 1601; full term 8 years; volume 3b, binding no. 852, page 114.[^john-1602] Father William, not Francis; Worcestershire-Marches origin; age and decade incompatible with a Massachusetts-1641 emigrant born c. 1603 and aged about 50 in 1653.
- **John Gurny, son of John, Ironmonger of Aylesbury, Buckinghamshire** — bound 30 May 1655 to Alexander Harbin of Gracechurch Street; volume 14, binding no. 514, page 67.[^john-1655] Date entirely too late to be the colonial John, and a clean Aylesbury Vale Gurney match (Aylesbury-cluster context, case file v4 §8.3).

**(b) No Gurney patrimony freedom 1583–1800.** The Patrimony sheet — 3,391 freedom-by-patrimony records — returns zero Gurney variants. If John G13 had been freed by patrimony as Francis G14's son, that admission should appear here. It is absent. Patrimony freedom of John, son of Francis Gurney, is **not present** in the Merchant Taylors record from 1583 to 1800.

**Implication for Candidate B.** The case file's §10.1 occupational argument is "Francis was a Merchant Taylor — John-1 was a tailor — trades passed overwhelmingly through family apprenticeship." That claim is qualified by this dataset: if Candidate B holds, John G13's tailoring trade was **not** transmitted through the Merchant Taylors' Company itself, neither as an apprentice bound to a fellow MT master nor as a patrimony freeman after his father's death. Three pathways consistent with Candidate B remain open:

1. **Apprenticeship in a different London livery.** The Drapers (case-file Candidate D's setting), the Clothworkers, or the Worsted Weavers all admitted tailors and clothworkers and would have been natural alternatives for a Norfolk-born youth in the 1620s. Candidate D's record set has independently been worked through and produced one John Gurney Drapers redemption 1623/4 that is now eliminated as the Massachusetts emigrant on continuity grounds.[^drapers-cross]
2. **Country apprenticeship outside London.** Norwich's own Worsted Weavers' Company, the Norfolk weaver guilds, or a country tailor master in East Anglia could have trained a John Gurney off the London livery books entirely. Norwich's apprentice register survives in the city archives; that record set is not yet indexed for this case.
3. **Informal training inside the household.** A father teaching a son the trade without formal indenture was not unusual in the period for boys of declining-gentry status.

The negative result does not refute Candidate B. It removes a piece of supporting evidence that the case file had not explicitly claimed (the v4 footing is "trades passed through family apprenticeship," not "John G13 was an MT freeman") but it does sharpen the wording: any future statement of the occupational argument should acknowledge that the MT books do not show a son John bound or made free under Francis G14.

[^john-1602]: UKDA-SN-9263, COMB sheet row 7404 and Freedoms sheet row 25155 (volume 3b, binding no. 852, page 114).
[^john-1655]: UKDA-SN-9263, COMB sheet row 25472 and Freedoms sheet row 25159 (volume 14, binding no. 514, page 67).
[^drapers-cross]: `research/people/john-gurney-candidate-d.md`; `research/case-files/john-gurney-case-file-v5.md`, §8.4.

---

## 4. Every other Gurney-variant occurrence, organised by person

This section catalogues the rest of the 37 dataset hits and assesses each for relevance to the John Gurney case. All entries are referenced by sheet, row, volume, and binding number; cross-extract at `sources/media/ukda-9263-merchant-taylors-apprentices/gurney-variants-extract.csv`.

### 4.1 Apprentices

| Bind year | Apprentice | Variant | Father | Father trade / status | Place | County | Master | Vol / no. / pg | Bearing on Candidate B |
|---|---|---|---|---|---|---|---|---|---|
| 1599 | Francis Gurney | Gurney | Henry Gurney | Gent | Great Ellingham | NFK | Henry Tryme (Near Ludgate); Tr 1605 to William Smooth (Lothbury) | 3a / 611 / 37 | §1 above — Francis G14. |
| 1602 | John Gurney | Gurney | William Gurney (decd) | Glover | "Moborne" | WOR | James Briggs (Shoe Lane) | 3b / 852 / 114 | §3 — eliminable John. |
| 1606 | William Girney | Girney | John Girney (decd) | Tailor | Bourton | BKM | John Juxon (Walbrook) | 5 / 570 / 69 | Bucks tailor's son; variant spelling Girney. Comparator for the Bucks John clusters at case-file §8.3, not a candidate himself. |
| 1611 | Andrew Gurney | Gurney | William Gurney | Yeoman | Eccleston | LAN | Richard Hull (Leadenhall Street) | 6b / 1046 / 124 | Lancashire — outside the corridor. |
| 1611 | William Gurney | Gurney | William Gurney | Gent | Coventry | WAR | Hugh Wale (St Thomas Apostle), 9 yrs | 6b / 750 / 89 | Coventry gentry Gurney — chronologically interesting (1611) but no documented link to West Barsham. |
| 1620 | William Gurney | Gurney | Thomas Gurney (decd) | Weaver | Oakley | BED | James Linthwait (Cornhill) | 8b / 250 / 31 | Beds weaver's son; non-direct-line. |
| 1637 | William Gurney | Gurney | John Gurney (decd) | Yeoman | Ashperton | HEF | Arthur Higgins (Newgate Market) | 11 / 1139 / 134 | Herefordshire — outside corridor. |
| 1646 | William Gurney | Gurney | Walter Gurney | Haberdasher | Westminster | LND | Robert Goodwyn (Whitechapel); freed 6 Dec 1654 | 12 / 3046 / 354 | Almost certainly the same person as the William Gurney "silk throwster" of Pettycoat Lane (Whitechapel) recorded as a 1661 master (§4.2). Notable London-Gurney chain but not in evidence as kin to G14. |
| 1655 | John Gurny | Gurney | John Gurney | Ironmonger | Aylesbury | BKM | Alexander Harbin (Gracechurch Street) | 14 / 514 / 67 | §3 — eliminable John. |
| 1709 | Reuben Gurney | Gurney | William Gurney | Gent | "Foxgrave" | NTH | John Simpson; freed 5 Dec 1716 as Oilman, Bread Street | 18 / 2226 / 248 | Northants gentry Gurney; "Foxgrave" likely a register-clerk rendering of a small Northants place. Reuben Gurney became a Bread Street oilman; in turn took apprentices (§4.2). Reuben recurs as a name in the Hunstanton / Norfolk Gurney pedigrees, but this Northants Reuben is not yet tied to those. |
| 1759 | Charles Gurney | Gurney | Jonathan Gurney | Sheriff's officer | St Andrew Holborn | LND | Robert Featley | 19 / 3328 / 370 | Eighteenth-century London Gurney; out of direct-line frame. |
| 1786 | James Gurney | Gurney | Thomas Gurney | Farmer | Winchendon | BKM | Daniel Ward, tailor, Callum Street (St Mary le Strand) | 20 / 1442 / 161 | Late Aylesbury Vale Gurney apprenticed to a London tailor — sustained Bucks-Gurney → London-tailoring trade thread, century after Candidate A's window. Worth flagging in case-file §8.3 supplementary notes. |

### 4.2 Masters and other principals

| Year | Person | Capacity | Trade / location | Counterparty | Vol / no. / pg | Bearing |
|---|---|---|---|---|---|---|
| 1616 | Francis Gurney | Master | "Near the hall" (Merchant Taylors' Hall) | Apprentice Francis Spelman, s. Sir Henry Spelman, Knight, of Middleton, Norfolk; £100 bond from the father | 7 / 2160 / 256 | §2 above — Francis G14 / Spelman. |
| 1628 | Edward Gurney | Witness (W2) | Weaver | At the freedom of Walter Markham, freed 20 Oct 1628 | 7 / 1234 / 147 | Lone reference. An Edward Gurney, Weaver, was on hand at a 1628 freedom event. Edward is a recurrent Norfolk-Gurney name in DG's pedigrees; the bare reference is too thin to attach to any specific Edward but is preserved as a comparator. |
| 1641 / 1652 | William Gurney | Master (turnover) | Barber surgeon; freedom no. F00038 | Apprentice Thomas Henson, originally bound 22 Sep 1641 to Edward Parkinson (Fleet Street); freed under William Gurney 11 Aug 1652 | 12 / 1333 / 154 | A William Gurney with a low freedom number was practising as a barber surgeon in London by the early 1650s, taking on a turnover MT apprentice to completion. Worth carrying as a comparator for any "London William Gurney" leads (e.g., the William Gurney at St Stephen Coleman Street in the 1641–42 Protestation Returns; case-file §10.4) but not in itself probative of kinship. |
| 1661 | William Gurney | Master | Silk throwster, Pettycoat Lane | Apprentice John Tapping, s. Peter, Farmer of Stepney; bound 19 Jun 1661 | 15 / 953 / 111 | Most plausibly the William Gurney bound 1646 and freed 1654 above. A Whitechapel-area silk throwster of the right name and chronology. |
| 1709 / 1716 | Reuben Gurney | Apprentice → Oilman / Master | Oilman, Bread Street | See §4.1 binding; subsequently took John Towes (b. 1720, freed 1726 by transfer to Richard Baylis; tobacconist 1733) and William Bulford (b. 1724, freed 1724 by transfer to William Bulford the father, glass seller) | various | Establishes Reuben Gurney as an active Bread Street oilman c. 1716–1730s; not direct-line. |
| 1747 / 1750 / 1752 | Richard Gurney | Transfer-master | Goldsmith; freedom no. F00774 | Apprentice Thomas Rowe, s. William, Gent of Walthamstow, Essex; bound 3 Jun 1747 to James Slater, transferred 3 May 1750 to Richard Gurney, transferred onward 6 Feb 1752 to James Dennis, gold and silver wire drawer | 19 / 2592 / 288 | Richard Gurney the eighteenth-century London goldsmith (b. 1709, d. 1784; senior partner of the Gurney and Cook / Cook and Gurney goldsmith partnership). Descends from the Norwich plebeian Gurneys — Bernau's "Problem" line, and downstream of Francis of Maldon if the 1655 Maldon John = John of St Gregory's Norwich identification holds.[^richard-goldsmith-context] |

[^richard-goldsmith-context]: `research/people/francis-gurney-of-maldon.md`, "The Problem" section; Walter Rye, "The Gurneys of Norwich," *The Norfolk Antiquarian Miscellany*. Source IDs: `british-archivist-bernau-1913`; `rye-norfolk-antiquarian`.

### 4.3 Off-spelling variants surfaced by the wider scan

A second pass over every g-vowel-(r/n) surname in the data surfaces three further surnames that may represent Gurney off-spellings, plus one separately documented gentry surname.

| Bind year | Apprentice | Variant | Father | Father trade / status | Place | County | Master | Vol / no. / pg | Bearing |
|---|---|---|---|---|---|---|---|---|---|
| 1610 | Henry Goney | Goney | John Goney | Yeoman | Weedon | BKM | Edward Mathew (Cow Lane) | 6a / 725 / 86 | Possible clerk variant of "Gorney"/"Gurney." Weedon sits inside the Aylesbury Vale Gurney territory and the father is a yeoman, fitting the rural-Bucks Gurney profile of case-file §8.3. Worth carrying as a comparator until either confirmed as a Gurney or set aside as a distinct Goney surname.[^goney-binding] |
| 1637 | John Garne | Garne | John Garne (decd) | **Tailor** | Weston under Penyard | HEF | William Coleman (Seacoal Lane); 7 yrs | 11 / 1055 / 124 | **The only "tailor-father → London tailor-apprentice" Gurney-adjacent binding in the dataset.** "Garne" reads as a plausible clerk rendering of "Gerne"/"Gurney." Weston under Penyard, Herefordshire is about 15 miles east of Ashperton (origin parish of the 1637 William Gurney bound in the same year — see §4.1) but the family identification is independent: the Ashperton Gurney father was a yeoman, this one was a tailor. The binding year and county overlap with the Ashperton Gurney binding by accident, not by household. The relevance to Candidate B is real but soft: if "Garne" is a Gurney off-spelling, this household produced a London-apprenticed tailor son in 1637 — exactly the trade and timing profile relevant to a John-1 / tailor parallel — but the apprentice was John Garne, not "John Gurney son of Francis," and the master Coleman has no documented link to Francis G14's circle.[^garne-binding] |
| 1594 | Edward Garneys | Garneys | Nicholas Garneys | Esquire | Kenton | SFK | John Leake, Merchant Adventurer (Friday Street); 8 yrs; freed 8 July 1611 | 2a / 417 / 25 | **Distinct gentry surname.** Garneys is the established Suffolk gentry surname (Mickfield / Kenton / Morningthorpe) treated separately from Gurney in the case file v4 §8 elimination table. The 1594 binding is the founding apprenticeship of an Edward Garneys, son of Nicholas Garneys, Esquire of Kenton, Suffolk, with a £200 bond from his brothers Richard and Charles Garneys. The trade entry "Esquire" for the father, the high bond, and the Kenton Suffolk seat all match the recognised Garneys gentry rather than the Gurney/Gournay line. Carry as catalogue completeness; not a Candidate B comparator.[^garneys-binding] |

The wider scan also surfaced Garne / Garneys / Goney as the only g-r-n / g-n surnames in the dataset that are not Gurney-cluster *or* distinct surnames like Gurnell, Gurnett, Garnett, Garnon, Gunson. No "Gorne," "Garney," "Guerne," or "Gerne" appears in the surname columns at all — those spellings (which do appear in the John Gurney case file's London and Berkshire comparators) are absent from the Merchant Taylors record across 1583–1800.

[^goney-binding]: UKDA-SN-9263, COMB sheet row 37937 and Freedoms sheet row 23488 (volume 6a, binding no. 725, page 86). Source ID: `ukda-9263-mt-apprentices-scott-2024`.
[^garne-binding]: UKDA-SN-9263, COMB sheet row 12199 and Freedoms sheet row 22389 (volume 11, binding no. 1055, page 124). Source ID: `ukda-9263-mt-apprentices-scott-2024`.
[^garneys-binding]: UKDA-SN-9263, COMB sheet row 35186 and Freedoms sheet row 22406 (volume 2a, binding no. 417, page 25). For the established Garneys gentry surname, see `research/case-files/john-gurney-case-file-v5.md` §8 (Mickfield / Morningthorpe Garneys row). Source ID: `ukda-9263-mt-apprentices-scott-2024`.

### 4.4 De-duplication note

The dataset is row-redundant by design: the COMB sheet contains the binding rows, and the Freedoms sheet projects each binding plus its freedom-side details. The 37 hits collapse into roughly 23 distinct person-events (apprenticeship bindings, freedoms, and master roles). No row dropped from the analysis above changes any conclusion; the redundancy provides cross-check confidence on the headline fields (parentage, master, dates).

---

## 5. Net implications for Candidate B

A focused summary of the bearings on the case file.

**(+) Strengthens.**
- Francis G14's parentage, occupation, and freedom are corroborated from the Company binding book itself — a first-hand source not previously read for this project.
- The "journey into the north" transfer note (3 February 1605) supplies a concrete pre-marriage 1605 Norfolk visit for Francis G14, fitting Daniel Gurney's claim that his commercial life began at Norwich and pre-dating the 1611 Margaret Rybett marriage by six years.
- The Francis Spelman apprentice binding (1616) places Francis G14 in a documented mentorship relationship with the Norfolk Spelman household and substantially upgrades the Bernau-cited "Spelman pedigree" lead from speculation to a positively-documented social relationship. The most plausible vector for any surviving Gurney/Gournay pedigree in the Spelman papers is Francis Spelman the apprentice.

**(–) Sharpens against.**
- No John Gurney son of Francis Gurney is bound to any MT master in the 1583–1800 record, and no Gurney appears in the Patrimony sheet at all. Whatever pathway produced the Massachusetts John's tailoring trade, it did **not** run through the Merchant Taylors' Company. The case file's §10.1 occupational-inheritance line should be tightened from "trades passed overwhelmingly through family apprenticeship" to a more specific claim about likely alternative pathways (Drapers redemption / Clothworkers / Worsted Weavers / Norwich apprenticeship / informal household training).

**(○) Neutral but worth carrying forward.**
- An eighteenth-century Aylesbury Vale Gurney apprenticed to a London tailor in 1786 (James Gurney, s. Thomas, Farmer of Winchendon) confirms a sustained Bucks-to-London tailoring trade thread among Aylesbury Vale Gurneys — a small datum sharpening the comparator at case-file §8.3.
- The Edward Gurney Weaver witness reference (1628) is a single isolated mention but preserves a London-resident Edward Gurney plying the weaving trade in the 1620s.
- The William Gurney barber surgeon (active by the early 1650s) and the William Gurney silk throwster of Pettycoat Lane (1661 master) most plausibly join into a single Whitechapel-area Gurney trade chain; nothing in the dataset links them to the Norfolk West Barsham line.
- The 1637 John Garne binding from Weston under Penyard, Herefordshire (son of a tailor) is the dataset's only tailor-father-to-tailor-apprentice Gurney-adjacent record; if "Garne" is a Gurney off-spelling it widens the comparator set with a tailor-line household in the same decade John G13 would have been training, though under a different master and in a different county from Francis G14's London circle.

## 6. Open items

1. **Reconcile the freedom date.** Pull the relevant page of M. Scott, *The Merchant Taylors Company of London: Apprentices 1583–1800* (British Record Society vols 136–138) — or the Guildhall MS freedom register — to decide between 16 June 1606 (Daniel Gurney) and 30 June 1606 (UKDA dataset).
2. **Locate the Spelman papers entry.** Cambridge University Library Spelman / Gough collections; Bodleian MSS Eng. hist.; British Library Add. MSS Spelman transcripts; College of Arms — with Francis Spelman the apprentice (bound 1616) as the carrier.
3. **Cross-check the Drapers, Clothworkers, and Worsted Weavers** for any John Gurney admission in the 1620s–1640s window that the MT books do not capture. Candidate D's Drapers work has already retired one such name on continuity grounds; the other companies remain unsearched at first hand.
4. **Resolve "Moborne, Worcestershire."** The 1602 John Gurney binding cites a "Moborne" in Worcestershire as the father's residence. No modern Worcestershire village of that exact name exists; candidates are Morborne (Hunts.), Mowsley (Leics.), or a register-clerk rendering of a parish that has since been renamed. Worth a short FreeREG / Genuki check.
5. **"Foxgrave, Northants" for Reuben Gurney (1709).** Same register-clerk caveat. Candidates include Foxley (Northants), Foscote, or Foxholes; only one of these is a Gurney-resonant place in any existing project source.

## Crosslinks

- Direct-line ancestor: `research/people/g14-francis-gurney-fact-sheet.research.md` (apprenticeship dates, Spelman master-apprentice link, "journey into the north" transfer note).
- Direct-line ancestor: `research/people/g13-john-gurney-fact-sheet.research.md` and the active case file: `research/case-files/john-gurney-case-file-v5.md` (negative result on a John-son-of-Francis MT binding; date discrepancy on Francis G14's freedom).
- Collateral context: `research/people/francis-gurney-of-maldon.md` (Norwich Quaker line / Richard Gurney goldsmith ancestry).
- Aylesbury Vale comparator cluster: case-file v4 §8.3 (Cublington, Aylesbury, Winchendon, Edlesborough, Chesham, etc.).
- Source: `sources/validations/ukda-9263-mt-apprentices-scott-2024.md`; `sources/media/ukda-9263-merchant-taylors-apprentices/`.
