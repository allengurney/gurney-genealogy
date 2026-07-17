# Dump — G13 colonial round 3, part 2: pending ward-line + county-framed threads, new leads (2026-07-02)

Raw research dump, self-contained (assume the chat thread is gone). Not repo-integrated; a
synthesis worker processes this later. Continues, same day:
`dump-2026-07-02-g13-colonial-round3-english-network.md` (round 3 part 1 — findings F-R3.1–F-R3.5;
its §3–§6 ledgers were left unpopulated when that session ended; THIS file carries the round-3
part-2 findings AND consolidates ledger entries for part-2 work only — part 1's own ledger debt
is flagged in §4 below). Prior rounds: `dump-2026-07-01-g13-colonial-massbay-campaign.md`
(round 1, F1–F11), `dump-2026-07-01-g13-colonial-round2-ward-county.md` (round 2, F-R1–F-R7).
Images (if any) in sibling `dump-2026-07-02-images/`.

## 0. Ground / baseline for part 2

- Part 1 (same day) completed W1 (Muskett/Gurdon), W2 (Winthrop Papers I:363 — MHS editors did
  NOT identify Warford or Mrs. Gurny; repo's F9 identification is original), W7 (Samuel × Sarah
  Shapley year = 1693 confirmed), W11 (Roxbury/Dedham/Muddy River clean; Dedham 1670/1 "Goodman
  Gurney of Dorchester, a Tanner" = Gurnell). Major part-1 gains: Muriel Gurdon was a
  Sedley–Knyvett (of Ashwellthorpe) granddaughter; Martha Heigham's 1591 will (Muskett pp.
  289–290) names Martha Lewkenor as one of seven under-21 Lewkenor sisters and endows an
  Emmanuel College scholarship.
- Pending from part-1 worklist: W3 (Lewkenor-of-Denham emigration connections), W4 (West
  Barsham-orbit advowson change c. 1627–28 in Blomefield/BHO), W5 (FTS Suffolk file papers:
  Wilson v. Faxon 1653 deposition image, L-147; Isaac files 792/911, L-94), W6 (1664 Braintree
  "meadowes" arks 3Q9M-C9YP-P29C / -P29P), W8 (Braintree film 1701 Gurney arks 3QSQ-G979-4W1D /
  -449L), W9 (Middlesex court — Isaac 1666), W10 (Norfolk-Co.-framed FTS probates 1700–1760).
- Pursuit-D leads selected this round (from `research_leads.py list --gen G13`): **L-94** (P80,
  Isaac Gurney court records 1666–67 — Middlesex sessions + Suffolk files 911/792), **L-170**
  (P38, Coldham *Complete Book of Emigrants* + TNA E 157/20 1635 port register — "Richard
  Gummy" check), **L-22** (P30, "Mr. Gurney, Soper Lane, St Pancras" in Dale, *Inhabitants of
  London in 1638*, p. 173 — potential Candidate-B London tie: Francis Gurney G14 was a London
  Merchant Taylor).
- Variant net per rounds 1–2: regex `G[aeiouvy]rn[aeiouy]|Gourn` (case-sens.) +
  `(?i)g[aeiouvy]rn(ey|ay|y|ie|ee|e)\b`, plus colonial additions Surney/Gurnet/Gornet/Girny/
  Garney. False-friend control table: Gurnell/Gornell + Garnsey/Guernsey (Dorchester),
  Garnet=Gardner (Hingham), Garnet (Providence), GARNEYS (Suffolk gentry, Muskett), Gurnet's
  Nose (place), Legorne=Livorno (Winthrop print series), Gorne=corn.

## 1. Part-2 worklist

| # | Thread | Basis | Status |
|---|---|---|---|
| W3 | Lewkenor-of-Denham emigration connections | pursuit A | pending |
| W4 | West Barsham-orbit advowson change c. 1627–28 (Blomefield/BHO) | pursuit A | pending |
| W5 | FTS Suffolk file papers: Wilson v. Faxon 1653 deposition (L-147); Isaac files 792/911 (L-94) | pursuit B | pending |
| W6 | 1664 Braintree "meadowes" legal arks | pursuit B (round-1 F8) | pending |
| W8 | Braintree film 1701 Gurney pages | pursuit B (round-1 F7.5) | pending |
| W9 | Isaac 1666 Middlesex court matter (creative; = L-94 half) | pursuit C/D | pending |
| W10 | Norfolk-Co.-framed FTS probates 1700–1760 — Richard-G12 descendant map | pursuit C | pending |
| W12 | L-22: Dale 1638 London "Mr. Gurney, Soper Lane" — Candidate-B London tie | pursuit D | pending |
| W13 | L-170: Coldham/E157 emigration-list check | pursuit D | pending |
| W14 | Creative: alternative web-index (Bing/Google) sweeps for uncatalogued G13 material | pursuit C | pending |

## 2. Findings

### F-R3.6 — Blomefield advowson sweep (W4): West Barsham vicarage was GURNEY-patronage in 1603; its institution list gaps 1603–1743, so the 1627–28 Warford institution is invisible in Blomefield; Harpley and Great Ellingham are EXCLUDED as the 1627 living [W4 resolved as far as Blomefield allows]

All from Blomefield, *An Essay towards a Topographical History of the County of Norfolk* (BHO,
read in-browser 2026-07-02; content pages not bot-gated).

1. **West Barsham (vol. vii, pp. 42–47, BHO `topographical-hist-norfolk/vol7/pp42-47`):**
   vicars list runs "...1583, Christopher Breese, by Thomas Fermer, Esq. of East-Barsham.
   **In 1603, Leonard Metcalf occurs vicar, and certified 420 communicants. patron then,
   Henry Gurney.** Mr. Rice died vicar in 1743..." — i.e. (a) the **Gurneys held the West
   Barsham patronage in 1603** (Henry G15); (b) the printed list records **no institution
   between 1603 and 1743**, so a c. 1627–28 presentation of Warford at West Barsham would be
   invisible here. West Barsham vicarage is now the **leading candidate** for the 1627
   presentation (PWF01d256). Counter-thread to keep visible: Blomefield also says Thomas
   Fermour possessed a West Barsham lordship "with the advowson of the church of this town"
   in 12 Eliz., a Kemp release to the Fermors 1603, and "William Fermor, Esq. son of Thomas,
   was lord of it in 1627" — a competing/alternating Fermor advowson interest (their 1583
   presentation is on the list). The wardship angle cuts through this: with Edward in ward,
   a 1627–28 institution would likely show **the Crown (Master of the Wards)** as patron,
   whoever held the advowson in fee — so Norwich institution books/CCEd remain the clincher.
   Curio: "1555, Richard **Gogney**, by the Duke of Norfolk" — possible Gurney-form vicar,
   flag only.
2. **Blomefield's West Barsham descent quotes the 1641 inquisition directly**: Henry [G15]
   "had Edmund Gurney, Esq. his son and heir, who (**as by an inquisition taken at
   East-Dereham, October 13th in the 17th of Charles I.**) died August 6th, in 1641, seized
   of this manor, and that of NorthBarsham, Lingham-Magna, &c. and left by **Frances his
   wife, daughter of Richard Hovell, Esq.** Henry, his son and heir, **aged nine years**" —
   so C 142/613/60 was taken **at East Dereham, 13 Oct 1641**, and per Blomefield's read it
   names the widow Frances (Hovell). Note Blomefield collapses Thomas III out of the descent
   (calls the decedent Henry's "son" Edmund); the brass + WARD/C142 series correct him
   (Edward, Henry's grandson via Thomas III). "Lingham-Magna" in the estates recital is
   plausibly "[El]lingham Magna" = Great Ellingham (see 4 below — Blomefield's Great
   Ellingham entry runs the same manor to the same 1641 decedent). Blomefield fn. 6 adds a
   NEW senior-branch terminus datum: "This Henry [II] is said to have married —, **daughter
   of — Adams, a barrister at law**, and to die without issue."
3. **Harpley (vol. viii, pp. 452–459) EXCLUDED — and Edmund the Divine's institution pinned:**
   rectors list: "**1620, Edmund Gurnay, B. D. by Sir William Yelverton, Knt.** 1648, George
   Heyhoo, by Robert Heyhoo." So Harpley was occupied 1620–1648 (no 1627 vacancy), and the
   advowson had left the family: earlier entries are "1443, Robert Wylton, by Thomas Gurnay,
   Esq.; 1485, Christopher Gurnay, by William Gurnay, Esq.; 1511, Thomas Higney, by Anthony
   Gurnay; **1537, William Ugge, by Thomas Godsalve, assignee of Anthony Gurnay**; 1579,
   Robert Kenyon, by the Queen, on the minority of Thomas Curson" — the Harpley advowson ran
   with the Curson→Stubbs→**Yelverton** manor by 1620 ("In 1620, Sir William Yelverton
   presented"). Edmund Gurney the Divine's Harpley institution year (1620) and patron
   (Yelverton, not a Gurney) are both NEW for the Divine's file.
4. **Great Ellingham (vol. i, pp. 482–490) EXCLUDED:** vicars: "1601, 20 Octob. Henry Womock
   ... **1628, 7 Nov. Nathaniel Scot, A. M. on Womock's death** [patron the Earl of Sussex
   line]. 1631, 24 Nov. Samuel Harding... Edward Earl of Sussex." The one institution in the
   window is a Sussex (Radcliffe) presentation. Same page confirms the senior-branch manor:
   a Great Ellingham lordship went "to Edm. Gurney, Esq. his son and heir, who died seized
   in 1641, and left Henry his son and heir, then nine years old, who died without issue."
5. **North Barsham (vol. vii, pp. 47–52) UNRESOLVED:** rectors: "1589, Samuel Stallon, by
   Richard Percy, Gent.; died 1613. **Joseph Lawson, died rector 1643**" — no institution
   year/patron printed for Lawson, so a 1613/14 vs 1627/28 institution cannot be
   distinguished from Blomefield. North Barsham (in the 1641 IPM estates) stays a secondary
   candidate for the Warford living.

### F-R3.7 — Winthrop Papers I (W3): Adam Winthrop's diary personally memorializes the deaths of Sir Edward Lewkenor and Susan (Heigham) — Martha (Lewkenor) Gurney's parents — Oct 1605; and the MHS index itself proposes "Warford (Walford?)" [MAJOR network + new Warford spelling]

Winthrop Papers vol. I (archive.org `winthroppapersvo0000comm`, djvu swept via repo_search
2026-07-02), printed p. 153 (Adam Winthrop's diary/almanac notes, arranged by calendar day):

> "The 3 of Octobre 1605. Sir Edwarde Lewkenor of Denham in Suff[olk] Knight died of the
> smalpocks. **Vir bonus et doctus fuit et patriae amans.** The lady his wife died 2 dayes
> before him." (djvu lines 15423–15425)

John Winthrop's father recorded the double smallpox death of the Denham Lewkenors — the
emigrant governor's family held Martha (Lewkenor) Gurney's parents in personal regard ("a
good and learned man, and a lover of his country") a generation before the 1627 Gurdon
letter. The editors' footnote 37 (same page) gives Sir Edward's parliamentary career
(Tamworth 1571, New Shoreham 1572, **Maldon, Essex 1584–1604**, Newport 1597; knighted 1603;
died at Denham Hall) and cites the memorial volume *Threnodia in Obitum D. Edovardi
Lewkenor, Equitis, et D. Susannae Conjugis charissimae. Funerall Verses upon the death of
the right Worshipfull Sir Edward Lewkenor, Knight, and Madame Susan his Lady* (1606) — a
printed funeral-verses volume for the couple (a future full-text target; Cambridge puritan
contributors would map the family's godly network). Incidental: Lewkenor sat for MALDON —
same town as the L-14 "John Gurney of Maldon" 1681 admin; noted as coincidence only.

**Index discovery:** the volume index reads "**Warford (Walford?), ——, 363**" — the MHS
editors themselves flag **Walford** as the alternative reading of the 1627 schoolmaster's
name. Round-2's Venn/Foster negative searched Warford spellings only; re-run Venn/Foster/CCEd
under **Walford** (a much commoner surname). Volume-level negative: zero Gurney-variant hits
in vol. I beyond the known p. 363 letter (index "Gurney, Mrs., 363; Gurney, ——, son of the
preceding, 363").

### F-R3.8 — NEW PERSON: Elizabeth Gournay, sister of Edward of West Barsham, married Bozoune Crowe of East Bilney (before 20 Dec 1636) — a senior-branch household in the EAST DEREHAM orbit in John G13's era [MAJOR]

Muskett, *Suffolk Manorial Families* vol. 2, L'Estrange-of-Hunstanton/Bozoune pedigree,
printed p. 176 (archive.org `suffolkmanorialf02john`, djvu lines 21249–21277):

> "Elizabeth Bozoune, marriage settlement dat. 26 April 37 Eliz. 1595 =
> Christopher Crowe, of E. Bilney, Norf., gent.; Will proved 15 Nov. 1637. (For Pedigree
> see Carthew's Launditch ii, 621.) … (Inter alios.) **Bozoune Crowe, of E. Bilney; mar.
> before 20 Dec. 1636 = Elizabeth, dau. of Thomas, sister of Edward Gournay, of West
> Barsham, Esq.**; Will dated 15 Sept. 1658, proved 11 March following. … Christopher Crowe,
> of E. Bilney, Esq. [their son] = Abigail Spelman, bapt. 17 Feb. 1641; mar. 13 April 1662;
> bur. at E. Bilney 23 Aug. 1721."

Readings:
1. **A previously unrecorded child of Thomas Gurney III & Martha (Lewkenor): Elizabeth
   (Gournay) Crowe** — sister of Edward (b. c. 1607), married before 20 Dec 1636 to Bozoune
   Crowe of East Bilney, gent./Esq. (son of Christopher Crowe d. 1637 by Elizabeth Bozoune).
   Chronology fits cleanly (b. c. 1605–1616; father d. 1616/17).
2. **Geography is the payload:** East Bilney is in Launditch hundred, ~5 miles from EAST
   DEREHAM — the parish of the "Entry E" c. 1609/10 John Gurney baptism candidate — and the
   1641 IPM of her brother was taken AT East Dereham (F-R3.6.2). Under Candidate B this puts
   a senior-branch sister's household inside the East Dereham corridor exactly when the
   emigrant was of age there, and gives the family a concrete Launditch-hundred presence.
3. Follow-ups: **Carthew, *The Hundred of Launditch and Deanery of Brisley*, vol. ii p. 621**
   (Crowe pedigree — should state her parentage and issue outright; archive.org/Google Books);
   **Bozoune Crowe's will (dated 15 Sept 1658, proved 11 Mar 1658/9)** — could name Gournay
   kin (which court, NCC or PCC, to determine); East Bilney parish registers for Crowe×Gournay
   children.

### F-R3.9 — The L'Estrange jest-book's Gurney anecdotes are KIN-SOURCED: Sir Nicholas L'Estrange, 1st Bt., married Anne Lewkenor of Denham — Edward Gournay's first cousin [upgrades the Thoms 1839 anecdotes]

Same Muskett v2 chart (printed pp. ~174–176, djvu lines 20758–20772): "Sir Nicholas Le
Strange, of Hunstanton, Norfolk; created a Baronet, 5 Chas. I, 26 Aug. 1630; ob. 1655 =
**Anne, da. of Sir Edward Lewknor of Denham, co. Suffolk**." (An adjacent OCR-scrambled cell
carries "Will prov. 1563," which belongs to an earlier-generation Lewkenor cell, not Anne's
father.) Sir Nicholas L'Estrange 1st Bt. (d. 1655) is the compiler of the jest-book behind
the Thoms 1839 *Anecdotes and Traditions* Gurney items (Thomas Gurney of West Barsham "died
in 1614"; Edward "married Frances Hood, and died in 1641"). His wife Anne Lewkenor was
daughter of Sir Edward Lewkenor II (d. 1618) of Denham — i.e. **niece of Martha (Lewkenor)
Gurney and first cousin of Edward Gournay**. The jest-book's Gurney anecdotes therefore came
from inside the family (via Lady L'Estrange), which (a) raises their weight as family
tradition, and (b) explains "Frances **Hood**" as the jest-book/Thoms rendering of Frances
**Hovell** (see F-R3.10). The L'Estrange×Lewkenor tie also loops back to round-1 F-R3's
West Barsham Calthorpe purchasers (Sir L'Estrange Calthorpe's forename).

### F-R3.10 — The Hovell family's own records confirm Frances Hovell as Edward Gournay's wife, alive as kin in 1647: visitation charts + Mary Goodwin's 1647 will ("Cozen Gurney") [resolves the Hovell/Hood/Lewkenor senior-branch tangle]

Muskett v2, Hovell-of-Hillington material:
1. Visitation-style chart (printed p. ~10, djvu lines 1039–1051): among the children of the
   Hillington Hovell house — "**Frances Howell maried to Edward Gurney of East Basham in
   Com' Norf. Esqr.**" (chart also carries "Willm. 2.", "Thomas. 3.", "Richard ob'. s.p. at
   six months", "William Hovell Esq: sonne and Heire apparent", and a knighting note "26th
   of March 1641").
2. Second chart (printed p. ~36, djvu lines 4021–4028): "**Frances, wife of Edward Gurney of
   East Barsham, co. Norfolk, Esq., 1647.** Elizabeth, wife of Thomas Coulson; devisee of
   her aunt Goodwin, 1647."
3. **Will of Mary Goodwin, 1647** (printed pp. ~28–29, djvu lines 3189–3210): Mary Goodwin
   of St Giles', Norwich, widow, 27 Nov 1647, to be buried in **Hillington** church; a
   Hovell by birth (brothers William Hovell of Little Massingham, Thomas, Richard); refers
   to "suit in the Court of Wards for money due from Thomas Skipp Esq. deceased"; names
   "Sister Byng: **sister Frances Hovell of Hillington Cozen Gurney**: cozen Coulson"; exec.
   Sir Richard Hovell of Sprowston, Knight; proved Archdeaconry of Norwich 19 Feb 1647/8.
   (The strung list "sister Frances Hovell of Hillington **Cozen Gurney**: cozen Coulson"
   pairs with chart (2)'s Frances-1647 and Elizabeth-Coulson-1647 entries — Muskett read the
   will as attesting both kinships in 1647.)

Reading: the **Hovells' own pedigree and testamentary record confirm Blomefield's IPM-based
statement** (F-R3.6.2) that Edward Gournay's wife was Frances Hovell (of the Hillington
house; Blomefield says "daughter of Richard Hovell, Esq."), and show Gurney kin still
acknowledged by the Hovells in Nov 1647 (Edward d. 1641; so "Cozen Gurney" most plausibly =
the widow Frances and/or her children). Muskett's "East Basham/East Barsham" reads as the
visitation's or Muskett's slip for West Barsham (or the widow's later residence — East
Barsham was the Fermors'; flag, don't resolve). Combined with the brass (parents: Thomas +
Martha Lewkenor) the senior-branch record is now coherent: **Thomas Gurney III (d. 1616/17)
m. Martha Lewkenor → Edward Gournay (b. c. 1607, ward to 1628, m. Frances Hovell of
Hillington, d. 6 Aug 1641, IPM East Dereham 13 Oct 1641) → Henry II (b. c. 1632, m. a dau.
of Adams, d.s.p., sold to Calthorpe by 1661)** — with Blomefield's "Edmund" a name-slip and
Thoms's "Frances Hood" a Hovell garble. Elizabeth (Gournay) Crowe (F-R3.8) joins as Edward's
sister.

### F-R3.11 — Bury St Edmunds ⇄ New England conduit document: Thomas Chaplin's 1672 Bury will leaves £40 to "Mary Gurney my servant" beside a New England debt (Jeremy Houchin) [Banks/Bury cluster, L-21-adjacent]

Muskett v3 pt. 1, "CHAPLIN OF SEMER, BURY, ETC." (printed p. ~109+, djvu lines 12522–12542):
Will of **Thomas Chaplin of Bury St. Edmund's, gent, "being aged," 24 April 1672**, proved
25 Nov 1672 (Arch. Sudbury Reg. 1672, fo. 349): grandchildren Thomas and William Chaplin
(sons of deceased son William); houses in Cooke Rowe & Whiting Street, Bury;

> "Whereas there is a debt owing to me from **Jeremy Houchin, late in New England**, as soon
> as it is collected, £60 to be divided among the six children my daughter Shepherd left
> behind her. To Abigail Whiteing my daughter £5. **To Mary Gurney my servant £40.** All the
> rest to my wife Elizabethe, sole executrix."

Readings: (a) a **Bury Gurney woman in 1672** — joins the three 1653–56 Bury St Mary Gurney
burials (L-21) and Banks's "Bury St. Edmunds" attribution for John G13 as the Bury-cluster
evidence base; (b) the **£40 legacy is extraordinary for a servant** (8× the daughter's £5)
— kinswoman-in-service is a live reading; (c) the same will's New England debtor (Jeremy
Houchin = the Boston tanner/selectman family, ex-Hingham) makes the household itself a
Bury⇄Boston conduit — a concrete example of the Suffolk↔Massachusetts traffic in exactly
the milieu Banks pointed at. Follow-ups: Chaplin household/parish (Chevington/Bury St
Mary?) registers for Mary Gurney; the Houchin debt's colonial side.

### F-R3.12 — False-friend addition: Muskett renders GARNEYS as "Gurneys" (Mirabel)

Muskett v2 prose (djvu line 237): "Margaret, daughter of Edmond Poley Esq., of Badley, by
**Mirabel, daughter of John Garneys, of Kenton**" — the same woman appears in Muskett's
charts as "Mirabel **Gurneys**" (lines 1199–1200, 1519). So Muskett's "Gurneys" (with -s) =
the Suffolk GARNEYS family (Kenton/Boyland), extending round-3 part 1's GARNEYS false-friend
note (F-R3.1.4): in Suffolk sources "Gurneys" as a surname is Garneys until proven otherwise.

## 3. Negative results ledger (part 2)

(populated below)

## 4. Recommended repo changes (do not edit repo this turn)

- **Part 1's §3–§6 ledgers were left unpopulated** by the earlier session; when synthesizing,
  reconstruct part-1 source tracking from its findings text (all sources are cited inline in
  F-R3.1–F-R3.5).

## 5. Human-required / gated / outsourced follow-ups (part 2)

(populated below)

## 6. Source tracking (citation-ready, part 2)

(populated below)
