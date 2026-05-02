# Henry Gurney (G15) — Research Companion

Research companion for `g15-henry-gurney-fact-sheet.md`. See AI-Rules.md §3 for the paired-file rule.

---

## Working Notes

### 2026-04-25 — L'Estrange anecdote: Edmund Gurney's mathematician joke

Sir Nicholas L'Estrange's manuscript anecdote collection preserves a compact example of Henry Gurney's son Edmund in comic mode: "Edm. Gurney used to say that a mathematitian is like one that goes to markett to buy an axe to breake an egg." The Camden Society editor's introductory notice identifies this "Parson Edmund Gurney" as Francis Gurney's brother and places him in the Edgefield and Harpley livings, confirming that the anecdote belongs to Edmund Gurney (1577-1648), Henry's third son, not the later nineteenth-century Edmund Gurney. The full extract and identity note are now in `research/people/edmund-gurney-divine.research.md`.[^thoms-edmund]

[^thoms-edmund]: William J. Thoms, ed., *Anecdotes and Traditions, Illustrative of Early English History and Literature, Derived from MS. Sources*, Camden Society, old series, vol. 5 (London: Printed for the Camden Society by J. B. Nichols and Son, 1839), pp. xviii-xx and p. 6, Internet Archive, https://archive.org/details/anecdotestraditi00thomrich/. Source ID: `thoms-anecdotes-traditions-1839`.

### 2026-04-23 — Bernau, *The British Archivist* (1913): new independent source for Henry's descendants

Charles A. Bernau's 1913 article in *The British Archivist* on Francis Gurney of Maldon (b. 1628) opens with an independent re-attestation of Henry G15 as father of Francis G14: "a member of the Merchant Taylors' Company, and a merchant living in the parish of St. Benet Finck, London, the sixth son of Henry GOURNAY, of Great Ellingham and West Barsham, Norfolk."[^bernau-parentage] This adds a fourth independent published attestation of Henry's paternity of Francis G14 (the others being Daniel Gurney 1848, Blomefield, and the 1633/34 Heralds' Visitation of London). Bernau's source base at the Public Record Office and the St Benet Fink register is separate from Daniel Gurney's manuscript work.

Bernau does not materially extend what is known about Henry himself. The value of the source for this research companion is almost entirely downstream: it documents Henry's **grandchildren through Francis G14** at St Benet Fink (Bernau's 11-item list — see conflict discussion in `research/people/g14-francis-gurney-fact-sheet.research.md`) and his **great-grandchildren through Francis Jr. of Maldon** (ten children at Maldon 1655–1667 — full biography at `research/people/francis-gurney-of-maldon.md`). One of those great-grandchildren, John of Maldon (b. 7 October 1655), is the candidate Bernau's article proposes for identification with John Gurney of St Gregory's Norwich, cordwainer, Quaker, ancestor of the Norwich banking Gurneys — making Henry G15 the shared paternal great-grandfather of both the Norwich banking Gurneys (under Bernau's proposed identification) and Allen's Massachusetts line (under the Candidate B model).

Nothing in Bernau contradicts or revises any item in this companion's Research Appendix. The source is catalogued in `data/sources.json` (proposed `british-archivist-bernau-1913` — see `_CHANGES.md`).

[^bernau-parentage]: Charles A. Bernau, "Unrecorded Biographies: Francis Gournay (or Gurney), of Maldon, Essex," *The British Archivist* vol. I, no. 7 (September 1913), pp. 49 ff., "His Parentage" section. Corpus extract at `sources/corpus_supplement/The_British_Archivist-Unrecorded-Biographies-Francis-Gurney.md`.

---

## Research Appendix

### Lineage Status
**Confirmed by multiple independent witnesses.** Henry Gurney is documented across an exceptional range of independent sources for an Elizabethan Norfolk gentleman:
- **Francis Blomefield** (1705–1752), <em>An Essay Towards a Topographical History of the County of Norfolk</em>, vols. i (1805), ii (1805), and vii (1807) — the Great Ellingham, Hingham, and West Barsham parish entries respectively. Blomefield independently confirms Henry as lord in 1572, gives his complete tenurial structure, names his Holdich grandmother and Blennerhasset wife, and traces the descent of Great Ellingham forward through his grandson Edward to extinction in 1661 and Sir Roger Potts.
- **Daniel Gurney** (1791–1880), <em>The Record of the House of Gournay</em> (1848), pp. 281–287, and the <em>Supplement</em> (1858), pp. 875–1014, including ~120 pages of extracts from Henry's own commonplace book.
- **Bodleian Library MS Tanner 175** itself: Henry's personal commonplace book of 239 leaves, c. 1570s–1608.
- **Steven W. May**, <em>Spenser Studies</em> 20 (2005) — modern academic study.
- **Catalogue of English Literary Manuscripts** (CELM, Folger Shakespeare Library).
- **Sidney Lee, ed., <em>Dictionary of National Biography</em>**, vol. 23 (1890), s.v. "Gurney, Edmund (d. 1648)" — naming Henry as Edmund's father.
- **Verily Anderson**, <em>Friends and Relations</em> (1980), p. 21 — preserves the epitaph verse.
- **Pease/Pennyghael Gurney genealogy** (Charles E. G. Pease, 2016).
- **Charles A. Bernau, *The British Archivist* I.7 (1913)** — re-attests Henry's paternity of Francis G14 from Public Record Office material independently of Daniel Gurney.

Henry's father, grandfather, wife, and most of his twelve children are documented across two or more of these sources independently of Daniel Gurney.

### Friction with the project JSON — for review

1. **Death date.** The project `ancestors_v3.json` gives "21 Jan. 1548 — d. 1623." The 1623 date is "will proved 1623," not a death date. Recommend updating to "21 Jan. 1548 — d. 1615/16 (will proved 1623)."
2. **Burial location.** JSON says St James's Church, Great Ellingham. Pease/Pennyghael says West Barsham. The epitaph verse (Anderson) is associated with Great Ellingham. Most likely reading: formal burial at West Barsham, surviving epitaph verse at Great Ellingham.
3. **Number of children.** JSON says 12; the epitaph verse counts 13 born and 12 surviving. Both correct depending on what is counted.
4. **"Harpham" should be "Harpley".** The JSON references "Harpham, Norfolk" — there is no Harpham in north-west Norfolk; the source is clearly Harpley.

### Henry Gurney's manuscripts, library, and poetic circulation

Steven W. May's article on Henry Gurney and Bodleian MS Tanner 175 remains the central modern scholarly source for Henry's literary life. The supplied abstract describes Henry as a previously unknown Elizabethan poet, critic, and bibliophile at Great Ellingham, Norfolk. In the last decade of Elizabeth's reign he entered into Tanner 175 both an inventory of his library and more than 600 of his own poems. Several poems explain his standards for judging good and bad poetry, and he transcribed verse "censures" of more than twenty borrowed books, including works by John Foxe, Robert Southwell, Richard Hakluyt, Edmund Spenser's *The Faerie Queene*, and "Mother Hubberds Tale."[^may-spenser]

The article metadata needs reconciliation rather than simplification. The user-supplied ResearchGate/DOI lead gives January 2004, *Spenser Studies: A Renaissance Poetry Annual* 19:183-216, DOI 10.1086/SPSv20p183. The existing companion and Swann's bibliography cite May 2005, *Spenser Studies* 20:183-223. Preserve both metadata variants until the DOI/full article is checked; do not drop the finding while resolving the citation.[^may-spenser]

Joel Swann's article on Chetham's Library MS A.4.15 adds a second modern manuscript context for Henry's poems. MC15 contains Henry Gurney's poetry on folios 69r-80r in the main poetry section, where the anthology shifts from metropolitan, witty, and Inns-of-Court-associated material to didactic, practical, rural poems on household, family, conduct, seasons, animals, wives, and agriculture. Swann identifies Henry as an amateur poet/farmer, born 1549 and died 1616.[^swann-chetham]

Swann summarizes May's findings in geographic and social terms: Henry began writing poetry in the 1590s at age 43, from the manor of Great Ellingham, just under 20 miles southwest of Norwich and about 100 miles northeast of London. He circulated poems and lent books to a circle of at least two dozen nearby people, with the most distant about 30 miles away in Suffolk. Outside MC15, the poems survive only in Henry's own notebook, though other copies were made, and Henry himself prepared copies for friends and relatives.[^swann-chetham]

The MC15 copies are themselves important. Swann says the Chetham manuscript preserves thirteen of the seventeen agricultural poems found in Henry's own anthology, drawing from poems scattered through Bodleian MS Tanner 175, folios 49v-232v. The MC15 versions are more coherent and organized than their Tanner 175 originals, suggesting at least one intermediary stage between Henry's notebook and the Chetham manuscript. Swann also notes that Henry may have had a London correspondent, giving a plausible route for Great Ellingham verse to enter wider manuscript circulation.[^swann-chetham]

MC15 also changes the scale of Henry's cultural setting. Swann argues that the manuscript should not be read as only an Inns of Court artifact: it has London, Inns, Norfolk, and East Anglian poles. The Gurney poems were copied by hand D, one of the important hands shaping the manuscript, and the ownership trail may point toward Norfolk book-trade or Norfolk ownership contexts before the manuscript reached Richard Farmer and then Chetham's Library. This makes Henry's rural Norfolk poetry part of the manuscript's social background, not merely an odd insertion into a London collection.[^swann-chetham]

[^may-spenser]: Steven W. May, "Henry Gurney, A Norfolk Farmer, Reads Spenser and Others," *Spenser Studies: A Renaissance Poetry Annual*; user-supplied ResearchGate/DOI lead gives January 2004, vol. 19, pp. 183-216, DOI 10.1086/SPSv20p183; Swann bibliography and existing companion give vol. 20 (2005), pp. 183-223. Source ID: `may-henry-gurney-spenser-2005`.
[^swann-chetham]: Joel Swann, "Chetham's Library MS A.4.15: an Inns of Court Manuscript?" *Journal of the Northern Renaissance*, 13 February 2016, paragraphs 2-4 and 20-38, https://jnr2.hcommons.org/2016/4231/; user-supplied markdown capture summarized at `sources/corpus_supplement/jnr-chethams-library-ms-a4-15-henry-gurney.md`. Source ID: `swann-chethams-library-ms-a4-15-2016`.
[^tanner-175-marco]: Bodleian Library, MS Tanner 175, MARCO manuscript catalogue lead, https://marco.ox.ac.uk/ark:29072/x0n870zq56b5. Source ID: `bodleian-ms-tanner-175-marco`.

### What Bodleian MS Tanner 175 contains
Per Steven W. May's modern article, CELM, and the manuscript-catalogue lead for Bodleian MS Tanner 175, Henry's commonplace book is the central primary corpus for his literary life. The source set describes it as a small folio volume of 239 leaves, c. 1570s-1608, containing:[^may-spenser][^tanner-175-marco]
- 600+ poems of Henry's own composition.
- An inventory of his personal library — uncommonly detailed for a Norfolk country gentleman.
- Verse "censures" (critical reviews in poetic form) of more than twenty borrowed books, including Spenser's <em>Faerie Queene</em> and "Mother Hubberds Tale," Nicholas Breton's <em>The Passions of the Spirit</em> (1599), John Foxe, Robert Southwell, and Richard Hakluyt.
- An extensive coterie of named correspondents — May calls it "the most extensive coterie of named individuals identified to date in the Tudor and early-Stuart period."
- Estate and family records — court rolls of Hingham-Gurneys going back to Edward III, leases for Great Ellingham/West Barsham/Irstead, builders' accounts, letters from Howard, Vere, and Plantagenet correspondents to Henry's predecessors, and personal verses on his own family.

This is the **single richest primary-source corpus for any ancestor in the Gurney lineage before the 19th century**.

### Surviving physical sites associated with Henry
- **Gurney's Manor, Hingham** (Attleborough Road, NR9 4HJ; TG0175201256) — **Grade II listed**, Historic England list entry 1170752. Late-18th-century Georgian red-brick front; brick-faced 17th-century rear wing with chambered ceiling beams, dated by the Historic England survey to "about 1600 (connected with granting of manor to Gurney's 1572?)." The single most direct surviving physical link to G15.
- **St James the Apostle, Great Ellingham** — Grade I listed (Historic England list entry 1248331), mainly early 14th century. Associated with Henry's surviving epitaph verse.
- **West Barsham Hall** (surviving 16th-century north wing, Grade II listed) — the seat where Henry was born and (per Pease) was buried.
- **St Lawrence Church, Harpley** — the medieval ancestral seat Henry repurchased in 1587, where his son Edmund was rector 1620–1648.

### Built-site witnesses: Hingham and Great Ellingham

Two later Norfolk place records now provide stronger built-environment anchors for Henry Gurney's world. DiCamillo identifies Gurney's Manor at Hingham as a fully extant Grade II private country house, circa 1600 with later alterations and earliest elements possibly dating to the 1570s. Norfolk Heritage Explorer identifies Old Hall, Great Ellingham (MNF9108 / NHER 9108), as a medieval moated manorial site with a mid-sixteenth-century great house inside the main moat, "said to be 1573, by Henry Gurney," with fishponds, additional moated enclosures, barns, and Grade II protected status.[^dicamillo-gurneys-manor-g15][^nher-old-hall-g15]

[^dicamillo-gurneys-manor-g15]: Curt DiCamillo, "Gurney's Manor," *The DiCamillo Companion to British & Irish Country Houses*, https://www.thedicamillo.com/house/gurneys-manor/. Source ID: `dicamillo-gurneys-manor`.
[^nher-old-hall-g15]: Norfolk Historic Environment Service, "MNF9108 — Old Hall, Great Ellingham," *Norfolk Heritage Explorer*, https://www.heritage.norfolk.gov.uk/record-details?MNF9108. Source ID: `nher-mnf9108-old-hall-great-ellingham`.

### Landholdings (per Blomefield's three independent parish surveys)
- **West Barsham manor and Hall** — held by one knight's fee of the manor of Castleacre.
- **Great Ellingham manor** — held of the heirs of Lord Bardolph.
- **Harpley manor** — repurchased 1587.
- **Irstead manor** — held of the Bishop of Norwich.
- **Gurney's manor in Hingham** — held of the heirs of Henry Lord Morley.
- **A third part of the advowson of Attleborough church**.
- **West Barsham rectory** — purchased 1595 for £100.
- **Hardingham (Swathings) manor**.

### The descent of Great Ellingham after Henry
Per Blomefield, vol. i, pp. 482–490: "he was lord in 1572, and at his death it went to Edm. [Edward] Gurney, Esq. his son [grandson] and heir, who died seized in 1641, and left Henry his son and heir, then nine years old, who died without issue, and it went to Margaret Gurney, his aunt, who married Mr. Henry Davy of Great Elingham, whose sole daughter and heiress, Mary, married Sir Roger Potts, Bart. of Great Elingham and Mannington."

Note: Blomefield's "Edm. Gurney" here is **Edward Gurney** (Henry G15's grandson via Thomas III, born 1608, died 1641) — Blomefield's printer was inconsistent with Edmund/Edward in the period. The 9-year-old Henry who succeeded him is **Henry Gurney II** of West Barsham, born c. 1632, who married Ellen Adams and died without issue in 1661, ending the senior West Barsham line. The aunt Margaret Davy was Henry G15's daughter; her daughter Mary married Sir Roger Potts of Mannington, Bart., and the Great Ellingham manor passed out of the Gurney name in the female line. This descent is documented in Blomefield independently of Daniel Gurney.

### Sources Consulted
**Primary topographical and biographical:**
- Francis Blomefield, <em>An Essay Towards a Topographical History of the County of Norfolk</em>, vol. i (London: William Miller, 1805), pp. 482–490 (Great Ellingham); vol. ii (1805) (Hingham, in the Hundred of Forehoe); vol. vii (1807), pp. 42–47 (West Barsham). All available via British History Online (https://www.british-history.ac.uk/topographical-hist-norfolk) and via the Internet Archive.
- Bodleian Library, MS Tanner 175 (not consulted directly).
- Sidney Lee, ed., <em>Dictionary of National Biography</em>, vol. 23 (London: Smith, Elder & Co., 1890), s.v. "Gurney, Edmund (d. 1648)."
- Thomas Fuller, <em>The History of the Worthies of England</em> (London, 1662), p. 258.
- Robert Masters, <em>The History of the College of Corpus Christi and the B. Virgin Mary in the University of Cambridge</em> (rev. ed., Cambridge, 1831), p. 338.
- Catalogue of English Literary Manuscripts (CELM), Folger Shakespeare Library, entry on Bodleian Tanner 175.
- William J. Thoms, ed., <em>Anecdotes and Traditions, Illustrative of Early English History and Literature, Derived from MS. Sources</em>, Camden Society, old series, vol. 5 (London: Printed for the Camden Society by J. B. Nichols and Son, 1839), pp. xviii-xx and p. 6.

**Genealogical and modern academic:**
- Daniel Gurney, <em>The Record of the House of Gournay</em> (London, 1848), pp. 281–287, and <em>Supplement to the Record of the House of Gournay</em> (King's Lynn: Thew & Son, 1858), pp. 875–1014. Both digitised on the Internet Archive.
- Steven W. May, "Henry Gurney, A Norfolk Farmer, Reads Spenser and Others," <em>Spenser Studies</em> 20 (2005), pp. 183–223 (DOI 10.1086/SPSv20p183). Source-registry and metadata reconciliation target: `may-henry-gurney-spenser-2005`.
- Joel Swann, "Chetham's Library MS A.4.15: an Inns of Court Manuscript?", *Journal of the Northern Renaissance* (2016). Source-registry target: `swann-chethams-library-ms-a4-15-2016`.
- Bodleian Library, MS Tanner 175, MARCO manuscript-catalogue lead. Source-registry target: `bodleian-ms-tanner-175-marco`.
- Verily Anderson, <em>Friends and Relations: Three Centuries of Quaker Families</em> (London: Hodder & Stoughton, 1980), p. 21.
- Pease/Pennyghael Gurney genealogy (Charles E. G. Pease, 2016), http://www.pennyghael.org.uk/Gurney.pdf.
- Charles A. Bernau, "Unrecorded Biographies: Francis Gournay (or Gurney), of Maldon, Essex," <em>The British Archivist</em> vol. I, no. 7 (September 1913), pp. 49 ff. — independent re-attestation of Henry's paternity of Francis G14 and documentation of Henry's descendants through that branch at St Benet Fink, London, and Maldon, Essex.
- Wikipedia, "Edmund Gurney (divine)" and "Gurney family (Norwich)."
- Historic England, list entry 1170752 (Gurney's Manor, Hingham), and list entry 1248331 (St James, Great Ellingham).
- Pevsner & Wilson, <em>Norfolk 2: North-West and South</em> (Buildings of England, 2nd ed. 1999), pp. 365–366.

### Negative Results
- No portrait or funeral effigy of Henry is known to survive.
- The full text of his 1614 will has not been recovered; needs Norfolk Record Office probate registers.
- The exact location of the surviving epitaph verse (wall monument, ledger slab, lost brass) is not specified.
- Bodleian MS Tanner 175 has not been consulted directly.

### Open Questions for Future Research
1. **Direct examination of Bodleian MS Tanner 175** — highest-value path. The MARCO catalogue lead is now captured as `bodleian-ms-tanner-175-marco`, but the manuscript record did not render during v08 intake; review the Bodleian catalogue and any digitized images directly.
2. **Norwich Consistory Court will registers** at the Norfolk Record Office, for Henry's 1614 will.
3. **Visit Gurney's Manor at Hingham** — the strongest physical link to Henry G15 of any building in Norfolk.
4. **St James the Apostle, Great Ellingham, and All Saints, West Barsham** — physical inspection for surviving Gurney monuments. Walter Rye's <em>Church Heraldry of Norfolk</em> (1887) on the Internet Archive should be checked.
5. **Steven W. May's full 2005 article** through an academic library.
6. **Lady Catherine Howard, Henry's godmother** — likely Catherine, daughter of the executed Earl of Surrey (later Countess of Berkeley). Worth resolving from MS Tanner 175.

### Potential Hero Images
- **Gurney's Manor, Hingham** (current draft pick) — Grade II listed, the surviving rear wing dating to Henry's lifetime.
- **St James the Apostle parish church, Great Ellingham** — Grade I listed; associated with the surviving epitaph verse.
- **West Barsham Hall, surviving 16th-century north wing** — already used as the hero for G23.
- **An opening leaf of MS Tanner 175 itself** — if available through Digital Bodleian.
