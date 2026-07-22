# G13 graph breadcrumb — 2026-07-22 — West Barsham PCC wills and the PCC index sweep

**Not applied to the graph.** This is a holding note recording what from the 22 July 2026
work has a G13 bearing, so the graph increment can be authored later without re-deriving it.
Derive live RI/PM ids from the database at authoring time.

## Source anchors to register first

| Source ID | What it is |
|---|---|
| `tna-pcc-west-barsham-gournay-wills` | PROB 11/188/136 (Edward Gournay, pr. 8 Feb 1642) and PROB 11/303/284 (Henry Gourney, pr. 11 Feb 1661), both read in full |
| `ukda-4816-pcc-wills-index` | PCC will index 1384–1858; 212 Gurney-variant testators extracted |

## Candidate findings with a G13 bearing

1. **The paternal-uncle fostering branch is materially weakened.** The childhood-household
   topic flagged that if Thomas Gurnay died c. 1615, his household could not have fostered
   the motherless John (b. c. 1609/10). That conditional has now largely resolved: the Norris
   memorandum of 23 March 1615 (Daniel Gurney, *Record* Pt II, p. 370) records Thomas already
   dead, his widow Martha holding the evidences, and his son and heir aged about five with an
   inquisition pending. With the indexed 1615–16 inventory and Edward's succession as a minor,
   three witnesses converge on death by early 1615. Bearing: **downgrade** the Thomas-household
   branch of the fostering hypothesis; the paternal-uncle route now runs better through
   Anthony, Henry, or Edmund.

2. **The 1627 Court of Wards "Mrs Gurny" identification is corroborated.** Edward Gournay's
   will asks to be buried near **Martha Gournay** at West Barsham — his mother, the widow of
   the 1615 memorandum. That is the same Martha (Lewkenor) already read into the Gurdon–
   Winthrop letter of 20 October 1627 as guardian of her near-majority son Edward. The
   guardian/ward pair is now documented from two independent directions.

3. **A new collateral sibling group at the senior seat.** Edward's will names brother
   **Thomas** and sisters **Susan, Dorothy, Elizabeth, Ellin, Margarett** — children of Thomas
   Gurnay and Martha, i.e. first cousins of John G13's father Francis G14's generation once
   removed. These are new people, and they independently corroborate the L'Estrange anecdote
   roster (which names Ed./Ned Gurney, Tho. Gurney "his brother", Dol. Gurney "Dorothy, his
   sister, died single", and Fra. Gurney as "an uncle of Edward").

4. **A clean structural negative for the elimination plane.** No direct-line ancestor appears
   anywhere in the PCC index across 1384–1858. The Norfolk line proved in the Norwich
   Consistory Court; the absence is jurisdictional, not evidential. This is worth carrying as
   an explicit negative so future work does not re-run the search.

5. **Three §8-relevant elimination rows may rest on wrong places.** The SN 4816 index and the
   repository's earlier scan readings disagree on PROB 11/335 (Aylesbury, Bucks vs Albury,
   Herts), PROB 11/241 + 11/242 (East Claydon, Bucks vs East Chiltington, Sussex), and
   PROB 11/252 (East Greenwich, Kent vs East Grinstead). These were used as elimination rows.
   The Aylesbury reading is the one that matters most, because it touches the live
   Aylesbury-candidate topic. Tracked as lead L-260. **Do not restate the affected elimination
   rows in the graph until this is settled.**

6. **A bounded backlog worth a coverage node.** Thirty-one of the forty-nine pre-1700 PCC
   Gurney-variant wills have never been examined, fully enumerated in the corpus supplement.
   The pre-1620 London merchant/draper cluster (PROB 11/46, 11/75, 11/89, 11/132) sits on the
   London-draper candidate thread. Tracked as lead L-262.

## Added 2026-07-22 (second pass) — a superseded claim carried in the graph

**`G13-RI-000153` states something the maternal-family research has overturned.** It says the
Rybett/Ryvett family "were Norfolk and Suffolk gentry" and that "St Martin at Palace was their
own Norwich parish, with Rivett entries running 1539–1603, so Margaret almost certainly
married from her family's church." Its sources are the Suffolk Visitation pedigrees, FreeREG
transcriptions of St Martin at Palace, and `nro-pd-12-1` described as "the Rybett family's
parish."

The later Garveston work establishes Margaret as a **Rivet of Garveston** — a **copyhold**
family in a village about fifteen miles west of Norwich, whose relationship to the Suffolk
gentry Ryvetts is explicitly unresolved (lead L-133) and whose status marker points *against*
the connection: the Suffolk Ryvetts generated Court of Wards business because they held land
in chief, and no mid-Norfolk Rivett appears in that series at all. "Rybett" is the 1611
clerk's one-off spelling; the family writes itself *Rivet*. The Garveston companion states
plainly that the marriage was "not Garveston, East Dereham, or any parish either family is
otherwise documented in."

There may well be Rivetts at St Martin at Palace 1539–1603, but they are **Norwich city
Rivetts**, and nothing links them to the Garveston copyholders. The inference "her family's
church" only held while Margaret was believed to be a gentry Ryvett.

**Graph actions when the increment is authored:** revise or retire `G13-RI-000153`'s middle
clause; the marriage-parish question should become an open question rather than a settled
explanation. `G13-RI-000086` already handles the chronological friction correctly and needs no
change. The same superseded sentence appears in the identification case file at §2.2 and
should be corrected there in the same pass.

## Where the prose already lives

- `sources/corpus_supplement/pcc-wills-gurney-variants-1384-1858.md` — full testator list and coverage status
- `sources/corpus_supplement/tna-pcc-west-barsham-gournay-wills.md` — the two transcriptions
- `research/people/g15-henry-gurney-fact-sheet.research.md` — the succession, the Thomas re-weighting, the Chancery identifications
- `research/places/west-barsham.md`, `research/places/north-barsham.md` — estate and Scotts Hall
- Leads: L-113, L-115, L-258 updated; L-260, L-261, L-262 opened
