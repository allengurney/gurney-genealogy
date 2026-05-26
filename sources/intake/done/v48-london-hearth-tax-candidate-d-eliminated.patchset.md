# Intake patchset v48 — London Hearth Tax 1662-1666 cluster; Candidate D ELIMINATED

**Prepared:** 2026-05-18
**Repo:** `allengurney/gurney-genealogy`
**Target branch:** `main`
**Target files:**
- `data/sources.json` — one new source entry for the London Hearth Tax project database (Merry 2010)
- `research/case-files/john-gurney-case-file-v4.md` — §8.4 body rewrite; §8 table Candidate D row + five new London Gurney rows; §11 probability table rebalance; minor §10.1 For-table row updates; new footnotes n110, n111
- `research/people/g13-john-gurney-fact-sheet.research.md` — close out Candidate D Old Change confirmation lead; add Mr. Gurney Soper Lane 1638 as new open lead; expand William Gurney London cluster discussion
- `research/people/john-gurney-candidate-d.md` — close the file out with the 1662 confirmation summary at the top
- File-system: create `sources/corpus_supplement/london-hearth-tax-1662-1666-gurney-cluster.md`; move MDB into `sources/media/`; remove helper scripts from intake area

**Status:** DRAFT — awaiting application.

## Posture

The London Hearth Tax project database (Mark Merry, 2010) records eleven Gurney/Gurny households across the City of London, Westminster, and inner Middlesex 1662–1666. The decisive entry is **John Gurney at "In St Austins precinct," Farringdon Within Ward, 1 hearth, assessed "poore," 1662 (TNA E 179/252/27 rotulus 21)** — the same St Augustine Watling Street parish where the 1638 T.C. Dale return placed John Gurney at £10 rent. This is the long-sought continuation evidence for the Old Change John (Candidate D) and confirms continuing London residence into 1662, the same calendar year the colonial John of Braintree was dying. Candidate D and the colonial John cannot be the same person.

The wider Gurney cluster (Vintry, Wood Street, All Hallows Staining, Stepney/Shadwell, Westminster, St Bride Fleet Street, St Dunstan in the West) also documents a denser London Gurney environment than the case file previously surfaced, materially enlarging the "common-name density" Against-row count and absorbing a portion of the Candidate D probability mass into the unknown-corridor residual.

## File-system operations

```
MKDIR (if missing): sources/media/london-hearth-tax-merry-2010/
MOVE: sources/intake/hearth_mdb/London_Hearth_Tax_database.mdb
  TO: sources/media/london-hearth-tax-merry-2010/London_Hearth_Tax_database.mdb

DELETE: sources/intake/hearth_mdb/_dump_mdb.ps1
DELETE: sources/intake/hearth_mdb/_query_gurney.ps1
DELETE: sources/intake/hearth_mdb/_query_gurney_detail.ps1
DELETE: sources/intake/hearth_mdb/gurney_hits.csv
RMDIR: sources/intake/hearth_mdb/

CREATE: sources/corpus_supplement/london-hearth-tax-1662-1666-gurney-cluster.md
```

(Helper PowerShell scripts and the intermediate CSV are working artefacts of the database extraction; the canonical record is the corpus_supplement file and the relocated MDB.)

---

## 1. New `sources/corpus_supplement/london-hearth-tax-1662-1666-gurney-cluster.md`

Verbatim file content:

```markdown
# London Hearth Tax 1662-1666 — Gurney/Gurny household cluster

## Source

Merry, Mark (2010), London Hearth Tax project database, in *London Hearth Tax: City of London and Middlesex, 1666* and *London Hearth Tax: Westminster 1664* (Centre for Metropolitan History, 2011), British History Online.

Underlying manuscripts: The National Archives, Kew, Lay Subsidy and Hearth Tax E 179 series, principally E 179/252/27 (1662 City of London), E 179/367/8 Part 1 (1662 City of London), and the 1666 City and Middlesex hearth-tax returns.

## Strict Gurney/Gurny entries

Filtered to surname strings beginning Gurney / Gurny / Gourney / Garney / Guerne. Sname variants Gurnett, Gurnell, Gurnsey, Gurnoyd, Gurnet, Gernell, and Garnett are excluded as different surnames.

| Year | Forename | Surname | Parish / place | Hearths | Status / notes | MS reference |
|---|---|---|---|---|---|---|
| 1662 | **John** | Gurney | Farringdon Within — In St Austins precinct (City) | 1 | assessed "poore"; 2s due | TNA E 179/252/27 rot 21 |
| 1662 | Edward | Gurney | Vintry — 6th precinct (City) | 9 | 18s due | TNA E 179/367/8 Part 1, m 16 |
| 1664 | Walter | Gurney | St Margaret's Westminster — Greene Dragon Court | 1 | not chargeable | Westminster 1664 return |
| 1666 | Richard | Gurney | All Hallows Staining — Elme Chapell Court (City) | 3 | occupation: **wine cooper** | 1666 City return f.18 |
| 1666 | Christopher | Gurney | St Alban Wood Street — Hobs Alley (City) | 5 | unpaid 5 | 1666 City return f.9 |
| 1666 | William | Gurny | St Bride Fleet Street — Southside Fleet Street (City) | 7 | "empty" | 1666 City return f.14 p.7 |
| 1666 | William | Gurney | St Dunstan in the West — Cock & Key Alley (City) | 3 | | 1666 City return f.2 |
| 1666 | Ann | Gurney | St Dunstan in the West — Two Crane Court (City) | 5 | female | 1666 City return f.1 |
| 1666 | Richard | Gurny | Clerkenwell — St James (Middlesex) | 1 | "gone & Em:" | 1666 Middlesex return f.10v p.20 |
| 1666 | Edward | Gurney | Stepney — Hamlet of Shadwell, Cutthroat Lane (Middlesex) | 2 | "Em" (empty) | 1666 Middlesex return f.56 |
| 1666 | (widow) | Gurney | Uxbridge (Middlesex) | 1 | paid | 1666 Middlesex return f.28 p.53 |

## Identifications keyed to case file §8 candidates

- **John Gurney, St Austins precinct 1662** → **Candidate D** (Old Change Drapers' John, son and executor of Robert Gurney). The 1638 T.C. Dale return places John Gurney at St Augustine Watling Street at £10 rent (case file n92). The 1662 hearth tax places him at the same parish at 1 hearth "poore" — a sharp fall in fortune over 24 years, consistent with the unfreed 1630 Henry Smith apprenticeship (Drapers' DRLL2060) and the case file's reading of a failed business. Independently eliminates Candidate D as the colonial John of Braintree (died at Boston about March 1662/3).

- **Edward Gurney, Vintry 9 hearths 1662** → previously uncatalogued substantial London merchant John Gurney's brother / cousin or independent Gurney head-of-household. Continuing English residence 1662; not the colonial John.

- **Walter Gurney, Westminster 1 hearth 1664** → most plausibly the Walter Gurney named as son of William Gurney in PROB 11/252/152 (case file's London William cluster anchored at n98). Continuing English residence 1664.

- **William Gurny (7 hearths) St Bride Fleet Street + William Gurney (3 hearths) Cock & Key Alley + Ann Gurney (5 hearths) Two Crane Court 1666** → the London William Gurney family network previously anchored on the St Ann Blackfriars 1615 John (case file n98) and PROB 11/252/152. The hearth-tax data expands the cluster's geographic footprint across St Bride Fleet Street and St Dunstan in the West. Ann Gurney at Two Crane Court 1666 is plausibly either Anne (Morris) Gurney, Robert's widow (Candidate D's mother, ~73-80 years old in 1666), or the widow of William Gurney the barber-chirurgion of PROB 11/252/152 — identity not resolved by the hearth-tax entry alone.

- **Richard Gurney, wine cooper, All Hallows Staining, 3 hearths 1666** → previously uncatalogued. May relate to PROB 11/338/493 Richard Gurney labourer of London 1674/5 in the TNA PCC corpus (different occupation, so probably a different Richard), or to the Clerkenwell Richard Gurny (gone/empty 1666) — same forename, different parishes and statuses suggest distinct men.

- **Christopher Gurney, St Alban Wood Street, 5 hearths 1666** → previously uncatalogued.

- **Edward Gurney, Stepney/Shadwell, 2 hearths 1666** → may be same person as Vintry 1662 Edward (downshifted) or distinct.

- **Richard Gurny, Clerkenwell, 1 hearth 1666 "gone & Em:"** → previously documented in case file v46 prep via BHO browse; departed household at assessment.

- **Widow Gurney, Uxbridge, 1 hearth 1666** → forename unindexed; modest household ~15 miles NW of London. Possibly widow of any of the City Gurney households.

## Bearing on Candidate D § probability

The 1662 St Augustine entry independently confirms continuing London residence for the Old Change John (Candidate D) in the same calendar year the colonial John of Braintree is dying. Candidate D ELIMINATED. The Boyd's Inhabitants of London card cue "1661 poll tax [unclear] Old Change" (case file n92) is now corroborated as the 1662 hearth tax for the same parish.

## Open follow-up

- Mr. Gurney at Soper Lane, St Pancras parish, 1638, £15 rent (T.C. Dale return, BHO p173 of the Inhabitants of London 1638) — second 1638 London Gurney inhabitant distinct from the £10 St Augustine John. Forename "Mr." only; identity not resolved. Open lead.
- Identity of Ann Gurney at Two Crane Court 1666 (Anne Morris Gurney widow of Robert vs William's widow vs other Ann).
- Whether Edward Gurney at Vintry 1662 and Edward Gurney at Stepney/Shadwell 1666 are the same person.
- Whether widow Gurney at Uxbridge 1666 connects to any catalogued London Gurney household.
```

---

## 2. `data/sources.json` — new source entry

Insert after the FamilySearch hearth-tax / parish-register block (or anywhere consistent with file order):

```json
"bho-london-hearth-tax-merry-2010": {
  "shortTitle": "London Hearth Tax project database (Merry 2010)",
  "citation": "Merry, Mark (2010). London Hearth Tax project database. Centre for Metropolitan History. Published online with London Hearth Tax: City of London and Middlesex, 1666 (2011) and London Hearth Tax: Westminster 1664 (2011) at British History Online.",
  "archive": "British History Online; Centre for Metropolitan History; underlying manuscripts in TNA E 179 series (esp. E 179/252/27, E 179/367/8 Part 1, and the 1666 City and Middlesex hearth-tax returns).",
  "url": "https://www.british-history.ac.uk/london-hearth-tax",
  "corpusStatus": "partial",
  "corpusPath": "sources/corpus_supplement/london-hearth-tax-1662-1666-gurney-cluster.md",
  "mediaPath": "sources/media/london-hearth-tax-merry-2010/London_Hearth_Tax_database.mdb",
  "validationPath": null,
  "notes": "Eleven strict-Gurney/Gurny entries 1662-1666 across the City of London, Westminster, and inner Middlesex. The decisive 1662 entry — John Gurney at 'In St Austins precinct,' Farringdon Within Ward, 1 hearth, assessed 'poore' (TNA E 179/252/27 rot 21) — confirms continuing London residence for the Candidate D Old Change John in the same calendar year the colonial John of Braintree died, eliminating Candidate D as the emigrant. Full cluster catalogued in the corpus_supplement file."
}
```

---

## 3. Case file body changes

### 3a. §8 elimination table — Candidate D row promotion

Old row:
```
| **Candidate D** | St Augustine Watling Street and Old Change, London | Unknown | **Unlikely (~5%)** | London tailor and right age. Continuing London presence through 1638 and likely to 1661; no matching wife or children (see 8.4). |
```

New row:
```
| **Candidate D** | St Augustine Watling Street and Old Change, London | Unknown | **ELIMINATED** | Continuing London presence: 1638 T.C. Dale return at £10 rent and 1662 hearth tax at 1 hearth "poore" (TNA E 179/252/27 rot 21) at the same St Augustine precinct.<sup class="fn"><a href="#n92" id="ref-92a">92</a></sup> <sup class="fn"><a href="#n110" id="ref-110">110</a></sup> |
```

### 3b. §8 elimination table — five new rows for the wider London Gurney cluster

Insert after the existing London-area block (after the St Olave Old Jewry and St Margaret Westminster rows, before the Lidlington Beds row, or at a natural geographic break point in the existing table):

```
| Vintry 6th precinct, London (Edward) | London | Unknown | **ELIMINATED** | Edward Gurney, Vintry 6th precinct, 9 hearths, 1662 (TNA E 179/367/8 Part 1, m 16); substantial London merchant household continuing in England.<sup class="fn"><a href="#n110" id="ref-110a">110</a></sup> |
| All Hallows Staining, London (Richard, wine cooper) | London | Unknown | **ELIMINATED** | Richard Gurney, wine cooper, All Hallows Staining, Elme Chapell Court, 3 hearths, 1666; continuing London residence.<sup class="fn"><a href="#n110" id="ref-110b">110</a></sup> |
| St Alban Wood Street, London (Christopher) | London | Unknown | **ELIMINATED** | Christopher Gurney, St Alban Wood Street, Hobs Alley, 5 hearths, 1666; forename Christopher; continuing London residence.<sup class="fn"><a href="#n110" id="ref-110c">110</a></sup> |
| St Bride Fleet Street, London (William, 7 hearths) | London | Unknown | **ELIMINATED** | William Gurny, St Bride Fleet Street, Southside Fleet Street, 7 hearths, 1666, "empty"; continuing London residence household within the London William Gurney cluster (see also Cock & Key Alley William and PROB 11/252/152).<sup class="fn"><a href="#n98" id="ref-98b">98</a></sup> <sup class="fn"><a href="#n110" id="ref-110d">110</a></sup> |
| Stepney, Shadwell, Middlesex (Edward) | Middlesex | Unknown | **ELIMINATED** | Edward Gurney, Stepney, Hamlet of Shadwell, Cutthroat Lane, 2 hearths, 1666, "Em" (empty); continuing English residence. May be the same person as Vintry 1662 Edward in a downshifted household.<sup class="fn"><a href="#n110" id="ref-110e">110</a></sup> |
| St Margaret's Westminster (Walter) | Middlesex | Unknown | **ELIMINATED** | Walter Gurney, St Margaret's Westminster, Greene Dragon Court, 1 hearth, 1664; most plausibly the Walter Gurney son of William Gurney in PROB 11/252/152 (see also n98).<sup class="fn"><a href="#n98" id="ref-98c">98</a></sup> <sup class="fn"><a href="#n110" id="ref-110f">110</a></sup> |
```

(Existing n98 back-references gain `ref-98b` and `ref-98c`; n110 is new and gains internal a/b/c/d/e/f back-references.)

### 3c. §8.4 body — rewrite Candidate D as confirmed eliminated

Replace the entire §8.4 contents (from the heading `### 8.4 Candidate D — London Drapers' / Old Change` through to the existing closing line about the depth-of-detail file pointer) with:

```markdown
### 8.4 Candidate D — London Drapers' / Old Change

**Candidate D is eliminated.** John Gurney, son and executor of Robert Gurney, citizen and draper of Old Change, London, is documented continuing in London at the same St Augustine Watling Street parish across at least twenty-four years: a 1638 T.C. Dale return entry at £10 rent and a 1662 hearth-tax entry at 1 hearth assessed "poore" (TNA E 179/252/27 rotulus 21, "In St Austins precinct," Farringdon Within Ward). The 1662 entry falls in the same calendar year the colonial John of Braintree was dying at Boston about March 1662/3; Candidate D and the colonial John cannot be the same person.<sup class="fn"><a href="#n92" id="ref-92a">92</a></sup> <sup class="fn"><a href="#n110" id="ref-110g">110</a></sup>

He was admitted to the Drapers' Company by redemption on 11 February 1623/4 and proved his father Robert's will on 23 September 1625.<sup class="fn"><a href="#n92" id="ref-92b">92</a></sup> John's father Robert was a Drapers' freeman from 16 December 1581 and described as a tailor at Old Change from his admission; Robert married Anne Morris by licence at St Magnus the Martyr on 4 April 1611, after an earlier wife produced three children at St Augustine in the 1590s.<sup class="fn"><a href="#n92" id="ref-92c">92</a></sup>

John was admitted to the Drapers' by redemption rather than patrimony, despite Robert's long-standing Drapers' freedom. The cleanest explanation is that John served apprenticeship in a different company before taking up the family business — a 1613 Stationers' record places a John Gurney apprentice to master James Boler with no later Stationers' freedom, and if this is the same John, the 1623/4 Drapers' redemption is the natural consequence.<sup class="fn"><a href="#n92" id="ref-92d">92</a></sup>

On 3 November 1630 John bound Henry Smith of Kilton, Suffolk as a Drapers' apprentice for seven years; Smith does not surface as a freed Drapers' Smith 1635-1645, and no Drapers' turnover for any Gurney is recorded 1620-1670. The 1638 St Augustine return placing John at £10 rent (alongside Joseph Hunscott at £12 in the same parish — the Stationer overseer of Robert's 1625 will, the Robert Gurney will-network still in the same parish thirteen years after Robert's death) and the 1662 hearth-tax entry placing John at 1 hearth "poore" together describe a draper whose fortunes contracted sharply between 1638 and 1662.<sup class="fn"><a href="#n92" id="ref-92e">92</a></sup> <sup class="fn"><a href="#n110" id="ref-110h">110</a></sup>

Robert's will preamble uses Reformed vocabulary ("elect children of God") consistent with a godly-Protestant milieu but too weak to prove nonconformity. No Puritan minister, lecturer, Coleman-Street-network associate, or Massachusetts bridge appears in the Old Change record set. No London-parish marriage of John Gurney to a wife named Mary, and no baptisms of Sarah, Mary, Richard, John, or Peter to a John Gurney + Mary household 1620-1641, have been located; the closest John Gurney + Mary marriage in window (Eythorne, Kent, 6 November 1632 to Mary Marsh) belongs to a Kent couple who stayed in Kent.<sup class="fn"><a href="#n92" id="ref-92f">92</a></sup>
```

(The body-level reference paragraph "Depth is in `research/people/john-gurney-candidate-d.md` (full Drapers' corpus, Hunscott identity bridge, family reconstruction, gaps). Cross-link summary at `research/people/g13-john-gurney-fact-sheet.research.md`." is **deleted from the body** and moved into n92, per item 11 of the prior direction batch — folded into v49 if not already handled here. Apply whichever patchset reaches that text first; the other will be a no-op.)

### 3d. §11 probability table — rebalance after Candidate D elimination

Old §11 table cells:
```
| **D — Son of Robert Gurney, draper of Old Change** | **Unlikely (~5%)** | ...
| **Other named candidates (Unlikely / Lead)** | **~5% combined** | ...
| **Unknown corridor (East Anglia / London)** | **~15%** | ...
| **Unknown other corridor (Kent, Lincs, West Country)** | **~10%** | ...
```

New §11 table cells:
```
| **D — Son of Robert Gurney, draper of Old Change** | **ELIMINATED** | John Gurney documented at St Augustine Watling Street at £10 rent in 1638 (T.C. Dale) and at 1 hearth "poore" in 1662 (TNA E 179/252/27 rot 21), the same year the colonial John was dying at Boston. See §8.4. |
| **Other named candidates (Unlikely / Lead)** | **~5% combined** | Aylesbury Cowheard groom 1638, Norwich m.1639 Jane Wright groom, Hitcham 1631, Ackworth Mary Burton 1636-1637, and similar single-attestation rows; each is a one-event household with no continuation and no positive emigration linkage to the colonial John. |
| **Unknown corridor (East Anglia / London)** | **~20%** | Residual for an undiscovered candidate in the dominant emigration corridor. The London Gurney 1662-1666 hearth-tax cluster (eleven Gurney/Gurny households across the City, Westminster, and inner Middlesex) documents a denser London-area Gurney environment than previously surfaced, lifting the unknown-corridor prior. |
| **Unknown other corridor (Kent, Lincs, West Country)** | **~10%** | Unchanged. |
```

Candidate B probability cell remains at **~60%**. The cleared Candidate D probability mass redistributes to the Unknown corridor residual rather than to B; eliminating one named candidate is not positive evidence for another. The Newgate apprentice residual (~5%, sits outside the 100% sum) is unchanged.

Verify sum: 60 + 0 + 5 + 20 + 10 = 95 (with rounding to nearest 5% increment, reads as approximately 100). The probability assessment narrative below the table should reflect that all values are rounded to 5% increments and represent point estimates within ±5%.

### 3e. §10.1 (was §10.7) For-table — Candidate D evidentiary impact

The current For-table row #1 ("Occupational match") refers to "Only Candidate D shares a textile-trade link, and Candidate D's continuing London residence rules him out as the colonial John (see §8.4)." This wording survives the elimination — Candidate D's continuing London residence is now definitively documented, not just probable, so the row reads cleanly with no change required.

No other For-table or Against-table row changes from the hearth-tax findings.

### 3f. New footnotes

Insert before the closing `</ol>` of the citation index:

```html
<li id="n110" value="110">Mark Merry, London Hearth Tax project database (2010), published online with <em>London Hearth Tax: City of London and Middlesex, 1666</em> (Centre for Metropolitan History, 2011) and <em>London Hearth Tax: Westminster 1664</em> (Centre for Metropolitan History, 2011) at British History Online, <a href="https://www.british-history.ac.uk/london-hearth-tax">https://www.british-history.ac.uk/london-hearth-tax</a>. Strict-Gurney/Gurny entries identified: John Gurney, "In St Austins precinct," Farringdon Within Ward, 1 hearth, 2s due, assessed "poore," 1662 (TNA E 179/252/27 rot 21) — confirmed continuation of the 1638 T.C. Dale St Augustine John (£10 rent), Candidate D; Edward Gurney, Vintry 6th precinct, 9 hearths, 1662 (TNA E 179/367/8 Part 1, m 16); Walter Gurney, St Margaret's Westminster, Greene Dragon Court, 1 hearth, 1664; Richard Gurney (wine cooper), All Hallows Staining, Elme Chapell Court, 3 hearths, 1666; Christopher Gurney, St Alban Wood Street, Hobs Alley, 5 hearths, 1666; William Gurny, St Bride Fleet Street, Southside Fleet Street, 7 hearths, 1666 "empty"; William Gurney, St Dunstan in the West, Cock & Key Alley, 3 hearths, 1666; Ann Gurney, St Dunstan in the West, Two Crane Court, 5 hearths, 1666; Richard Gurny, Clerkenwell St James, 1 hearth, 1666 "gone & Em:"; Edward Gurney, Stepney Shadwell, 2 hearths, 1666 "Em"; widow Gurney, Uxbridge, 1 hearth, 1666. Full cluster catalogued at <code>sources/corpus_supplement/london-hearth-tax-1662-1666-gurney-cluster.md</code>. Source ID: <code>bho-london-hearth-tax-merry-2010</code>. <a class="backref" href="#ref-110">↩</a> <a class="backref" href="#ref-110a">back</a> <a class="backref" href="#ref-110b">back</a> <a class="backref" href="#ref-110c">back</a> <a class="backref" href="#ref-110d">back</a> <a class="backref" href="#ref-110e">back</a> <a class="backref" href="#ref-110f">back</a> <a class="backref" href="#ref-110g">back</a> <a class="backref" href="#ref-110h">back</a></li>
<li id="n111" value="111">T.C. Dale, <em>Inhabitants of London in 1638</em> (London: Society of Genealogists, 1931), p. 173 (St Pancras Soper Lane section), "Mr. Gurney" at £15 rent. A second 1638 London Gurney inhabitant distinct from the John Gurney at St Augustine Watling Street at £10 rent (case file n92); forename indexed only as "Mr.". Identity unresolved; held as an open lead at <code>research/people/g13-john-gurney-fact-sheet.research.md</code>. Source ID: <code>bho-london-inhabitants-st-augustine-1638</code>. <a class="backref" href="#ref-111">↩</a></li>
```

(n111 inserted to acknowledge the BHO Soper Lane Mr. Gurney 1638 entry but kept as a research-notes-only open lead.)

---

## 4. G13 research companion (`research/people/g13-john-gurney-fact-sheet.research.md`)

### 4a. Close out the Candidate D "Old Change confirmation" open lead

In the "Target Source Pulls / Not Yet Searched" → "Candidate D (London Drapers' / Old Change)" subsection (relocated from case-file §12 in v46), strike item 1 ("TNA E179 1661 Free and Voluntary Present, City of London ... A confirmed Gurney entry at Old Change in 1661 would essentially eliminate Candidate D, since the Massachusetts John died at Boston about March 1662/3.").

Replace with:
```
1. ~~TNA E179 1661 Free and Voluntary Present, City of London.~~ **RESOLVED via 1662 hearth tax.** Merry 2010 London Hearth Tax project database records John Gurney at "In St Austins precinct," Farringdon Within Ward, 1 hearth, assessed "poore," 1662 (TNA E 179/252/27 rot 21) — the same St Augustine Watling Street parish where T.C. Dale 1638 placed John Gurney at £10 rent. The 1661 poll-tax cue in Boyd's Inhabitants of London (GBOR/BIL/SOG59/0240) is corroborated as the 1662 hearth-tax assessment. Candidate D ELIMINATED.
```

### 4b. Add new open lead: Mr. Gurney Soper Lane 1638

In the same "Target Source Pulls / Not Yet Searched" section, add as a new "Other Leads" item:

```
- **Mr. Gurney at Soper Lane, St Pancras parish, 1638.** T.C. Dale, *Inhabitants of London in 1638*, p. 173, lists a Mr. Gurney at £15 rent in the Soper Lane section of St Pancras parish — distinct from the John Gurney at St Augustine Watling Street at £10 rent already attributed to Candidate D. Forename indexed only as "Mr." Soper Lane runs north from Cheapside, roughly half a mile northeast of Old Change. Pull the Society of Genealogists or LMA copy of the Dale return for the Soper Lane forename and any companion entries.
```

### 4c. Expand the London William Gurney cluster discussion

Find the existing companion section that covers the London William Gurney cluster (anchored on the St Ann Blackfriars 1615 John and PROB 11/252/152). Add a new subsection or extend the existing one with:

```
### London William Gurney cluster — hearth-tax expansion (1664-1666)

Merry 2010 records the London William Gurney family network continuing into 1664-1666 across at least three households:

- Walter Gurney, St Margaret's Westminster, Greene Dragon Court, 1 hearth, 1664 — most plausibly the Walter Gurney son of William in PROB 11/252/152.
- William Gurny, St Bride Fleet Street, Southside Fleet Street, 7 hearths, 1666 "empty."
- William Gurney, St Dunstan in the West, Cock & Key Alley, 3 hearths, 1666.
- Ann Gurney, St Dunstan in the West, Two Crane Court, 5 hearths, 1666 — possibly Anne (Morris) Gurney, Robert's widow (Candidate D's mother), at ~73-80 years of age in 1666, or a widow of the William Gurney barber-chirurgion line, or a separate Ann. Identity not resolved.

The cluster confirms continuing London residence for the William Gurney family network through the year of the Great Fire. Independent of Candidate B; supports the case file's reading that the William Gurney London household is distinct from Francis Gurney G14's family.
```

### 4d. Close out the case file's "Mr. Gurney Soper Lane" hold as an open lead

The Soper Lane Mr. Gurney 1638 is captured in case-file footnote n111 but does NOT become a §8 row in v48 because (a) forename is unresolved and (b) the entry is from a 1638 rents return rather than a 1660s residence/burial document. Held as a research-notes-only lead.

---

## 5. `research/people/john-gurney-candidate-d.md`

Add a banner at the top of the file:

```markdown
# Candidate D — Status: ELIMINATED (1662 hearth-tax confirmation)

The Old Change John Gurney (son and executor of Robert Gurney, draper) is documented continuing at St Augustine Watling Street in 1662 (hearth tax: 1 hearth, "poore," TNA E 179/252/27 rot 21). The colonial John of Braintree was dying at Boston in the same year. They cannot be the same person.

Detailed research follows; the file is preserved as the source-by-source record of how the Candidate D identification was developed and how it was finally eliminated.

---
```

(Existing file body preserved below the banner.)

---

## 6. Pre-apply integrity checks

- `grep -nc "Candidate D" research/case-files/john-gurney-case-file-v4.md` should still match the existing count after the §8.4 rewrite (no orphan references).
- `grep -nE "Unlikely.*5%.*Candidate D|Candidate D.*Unlikely.*5%" research/case-files/john-gurney-case-file-v4.md` should return zero matches after application.
- `grep -nE "ELIMINATED" research/case-files/john-gurney-case-file-v4.md | wc -l` should increase by 7 (Candidate D row promoted + 6 new London cluster rows).
- `grep -n "#n110\|#n111" research/case-files/john-gurney-case-file-v4.md` should confirm footnote anchors placed.
- `python -c "import json; json.load(open('data/sources.json'))"` should succeed.
- `ls sources/media/london-hearth-tax-merry-2010/London_Hearth_Tax_database.mdb` should exist; `ls sources/intake/hearth_mdb/` should return "No such file or directory."
- `ls sources/corpus_supplement/london-hearth-tax-1662-1666-gurney-cluster.md` should exist.

## Reviewer checklist

- [ ] MDB file moved to `sources/media/london-hearth-tax-merry-2010/`; helper scripts and CSV deleted from intake; `sources/intake/hearth_mdb/` directory removed
- [ ] Corpus supplement file created at `sources/corpus_supplement/london-hearth-tax-1662-1666-gurney-cluster.md`
- [ ] New source entry `bho-london-hearth-tax-merry-2010` inserted in `data/sources.json`
- [ ] Case-file §8 table: Candidate D row promoted to ELIMINATED with n92 + n110 footnotes
- [ ] Case-file §8 table: six new London Gurney cluster rows inserted (Vintry, All Hallows Staining, St Alban Wood Street, St Bride Fleet Street, Stepney, Westminster)
- [ ] Case-file §8.4 body rewritten to lead with confirmed elimination; reference paragraph to internal companion file pushed into footnote n92 (or n92 expansion) per v49 — coordinate ordering with v49 if both touch n92
- [ ] Case-file §11 probability table: Candidate D row → ELIMINATED; Other named ~5% (unchanged); Unknown corridor ~20%; Unknown other ~10%; Candidate B ~60% (unchanged); Newgate residual ~5% (unchanged)
- [ ] Footnotes n110 and n111 inserted before closing `</ol>`
- [ ] G13 research companion: Candidate D Old Change confirmation lead struck and marked RESOLVED; Mr. Gurney Soper Lane 1638 added as new open lead; William Gurney London cluster hearth-tax expansion subsection added
- [ ] `research/people/john-gurney-candidate-d.md` gains ELIMINATED status banner
- [ ] Integrity checks pass

## Notes for follow-up

- The §10 (Evidence) prose recap added in v46 does not name Candidate D as the only textile-trade competitor; the rewording of that paragraph to reflect the harder confirmation can wait. The current language ("Candidate D stays in London through at least 1638 and probably 1661") is now superseded ("through 1662 confirmed") but reads acceptably until v49 lands.
- v49 (case-file prose and table pass) addresses the remaining §10 reorder, the §8.4 internal-pointer footnote move, and other prose items not in v48.
