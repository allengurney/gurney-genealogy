# Intake patchset v22 - John Gurney Candidate A rewrite (Alice Oliffe + Bucks household mapping)

```yaml
patchset_id: v22
created: 2026-05-09
repo_scope: gurney-genealogy
phase: phase_1_patchset_only
primary_case_file: research/case-files/john-gurney-case-file-v4.md
primary_research_file: research/people/g13-john-gurney-fact-sheet.research.md
working_memo: sources/intake/working/john-gurney-audit-state.md
phase_2_rule: Apply only after review and after v20/v21. Do not create corpus-supplement files; the index extracts are short and live in research with thin validation.
```

## 0. Audit report

### 0.1 Scope

Pass 4 used the project's live Findmypast subscription via the Chrome extension to walk the Buckinghamshire Marriage Index, Buckinghamshire Burial Index, and Buckinghamshire Baptism Index for every John Gurney/Alice/Mary/Edward Gurney record relevant to Candidate A's identification. The pass produces case-changing rewrites to the Cand A row.

### 0.2 Direct pulls obtained (Bucks indexes via Findmypast)

| Record | Source / archive | Significance |
|---|---|---|
| **John Gurney + Alice Oliffe**, married 24 Apr 1628, Bierton with Broughton | Bucks Marriage Index, GBPRS/BUCKINGHAMSHIRE/MAR/000221542; Bucks Archives PR16/1/1Q p. 30 | **Cand A wife is Alice OLIFFE, not Collindridge.** Cand A's wife identification is rewritten by primary indexed evidence. |
| John Gurny + Alice Hewet (widow), married 20 Oct 1619, Great Kimble | Bucks Marriage Index; Bucks Archives D/A/T/116 (Bishop's transcripts) | Separate older Bucks John+Alice household. Not Cand A. |
| Jon Gurny burial 2 Feb 1665, Aylesbury, "son of Edward Gurny" | Bucks Burial Index; Bucks Archives B24 | NOT Cand A's burial. Identifies Edward Gurny as a separate Aylesbury Gurney head-of-household. |
| John Gurney burial 17 Apr 1654, East Claydon | Bucks Burial Index; Bucks Archives PR51/1/1 | NOT Cand A. East Claydon John was husband of Elizabeth with children Elinor 1632 + Samuel 1636. |
| John Gurney burial 11 Jun 1678, Chesham; John "G?" burial Jul 1672, Chesham | Bucks Burial Index; Bucks Archives D/A/T/42 | Chesham John + Elizabeth household; not Cand A. |
| Ann Gurny baptism 1666, Aylesbury, father Edward | Bucks Baptism Index | Confirms Edward Gurny continued an Aylesbury Gurney household. |
| Elinor Gurney baptism 1632 + Samuel Gurney baptism 1636, East Claydon, father John mother Elizabeth | Bucks Baptism Index | East Claydon John + Elizabeth household — separately documented. |
| Andtr + Martha Gurney baptisms (date range 1576-1682), Chesham, father John mother Elizabeth | Bucks Baptism Index | Chesham John + Elizabeth household. |
| James Gurney baptism 1650 + Elizabeth Gurney baptism 1652, Wing, father John mother Ann/Anne | Bucks Baptism Index | Wing John + Anne household. |
| Isaac Gurney x 3 baptisms in 1664, Cublington, father John mother Mary | Bucks Baptism Index | Bucks "John + Mary" household with an **Isaac** son in 1664. Cublington is ~5 miles SW of Stewkley. Most plausible identity for the John + Isaac who held the Stewkley manor by 1687 in VCH Bucks vol. 3 pp. 420-426. |

### 0.3 Negative findings (Bucks indexes)

- Zero Jonathan Gurney baptisms in Bucks Baptism Index 1645-1649 with or without father John or Edward filters. The repo's older "Jonathan Gurney baptized Aylesbury 22 Nov 1647 son of John" claim is unsupported by this index and may have originated in FamilySearch's England Births and Christenings or in a derivative online tree. Findmypast Bucks Baptism Index does cover Aylesbury parish (34 indexed Gurney baptisms there), so the absence is real, not a coverage gap.
- Zero indexed children of the 1628 Bierton John Gurney + Alice Oliffe marriage at Bierton with Broughton or any Aylesbury parish. The Cand A marriage produced no Bucks-indexed children. Most plausibly the family had children in Northamptonshire after the 1641 cert of residence (TNA E 115/180/113) and the 1650 Walgrave tenancy (both already in repo notes).

### 0.4 Bucks Gurney household map after Pass 4

| Household | Wife | Place | Children indexed | Burial(s) indexed |
|---|---|---|---|---|
| **Cand A** | **Alice Oliffe** | Bierton with Broughton (m. 1628) | None in Bucks | None in Bucks |
| John + **Elizabeth** | Elizabeth | East Claydon | Elinor 1632, Samuel 1636 | John 17 Apr 1654 East Claydon |
| John + **Elizabeth** | Elizabeth | Chesham | Andtr, Martha (range 1576-1682) | John 1672 + John 1678 Chesham |
| John + **Anne/Ann** | Anne | Wing | James 1650, Elizabeth 1652 | — |
| John + **Mary** | Mary | Cublington | Isaac x3 in 1664 | — |
| John + Alice Hewet (widow) | Alice Hewet | Great Kimble (m. 1619) | — | — |
| John + ? | — | Weston Turville | Elyzabethe 1627 | — |
| **Edward Gurny** | — | Aylesbury (1660s) | Ann 1666 | son Jon Gurny 2 Feb 1665 |

Bucks 17th-century Gurney activity is materially denser than the case file currently expresses.

### 0.5 Candidate implications

- **Candidate A:** The 1628 Bierton marriage to **Alice Oliffe** plus the existing 1641 TNA E 115/180/113 cert of residence (Aylesbury → Northants) plus the 1650 Walgrave tenancy plus the absence of indexed Bucks children all point to Cand A continuing in England (Bucks/Northants corridor) well past 1641. Probability should drop from ~8-10% to **~2-4%** pending the Stewkley Dickson/Putnam 1897 register pull, which would either anchor Cand A's birth and possibly his burial at Stewkley or detach him from the 1602/3 baptism claim entirely.
- **Candidate B/C/Unknown other origin:** No direct effect from Pass 4. The Cand A probability drop tightens the residual "Unknown other origin" bucket by a few percent.

## 1. Source registry operation

Before applying, verify the proposed source IDs are still absent:

```powershell
Select-String -Path data\sources.json -Pattern "findmypast-bucks-marriage-index"
Select-String -Path data\sources.json -Pattern "findmypast-bucks-burial-index"
Select-String -Path data\sources.json -Pattern "findmypast-bucks-baptism-index"
```

Add three source objects in `data/sources.json`:

```json
    "findmypast-bucks-marriage-index": {
      "shortTitle": "Findmypast Buckinghamshire Marriage Index",
      "fullTitle": "Buckinghamshire Marriage Index, Centre for Buckinghamshire Studies (transcribed parish marriage records, Bucks Archives)",
      "publisher": "Findmypast / Centre for Buckinghamshire Studies",
      "type": "parish register index (subscription)",
      "url": "https://search.findmypast.co.uk/search-world-records/buckinghamshire-marriage-index",
      "notes": "Subscription index of Bucks parish marriage records held at Bucks Archives. Cand A entry: John Gurney + Alice Oliffe, 24 Apr 1628, Bierton with Broughton, PR16/1/1Q p. 30."
    },
    "findmypast-bucks-burial-index": {
      "shortTitle": "Findmypast Buckinghamshire Burial Index",
      "fullTitle": "Buckinghamshire Burial Index, Centre for Buckinghamshire Studies (transcribed parish burial records, Bucks Archives)",
      "publisher": "Findmypast / Centre for Buckinghamshire Studies",
      "type": "parish register index (subscription)",
      "url": "https://search.findmypast.co.uk/search-world-records/buckinghamshire-burial-index",
      "notes": "Subscription index. Key entries used: Jon Gurny son of Edward Gurny, Aylesbury, 2 Feb 1665, B24; John Gurney, East Claydon, 17 Apr 1654, PR51/1/1; John Gurney, Chesham, 11 Jun 1678, D/A/T/42."
    },
    "findmypast-bucks-baptism-index": {
      "shortTitle": "Findmypast Buckinghamshire Baptism Index",
      "fullTitle": "Buckinghamshire Baptism Index, Centre for Buckinghamshire Studies (transcribed parish baptism records, Bucks Archives)",
      "publisher": "Findmypast / Centre for Buckinghamshire Studies",
      "type": "parish register index (subscription)",
      "url": "https://search.findmypast.co.uk/search-world-records/buckinghamshire-baptism-index",
      "notes": "Subscription index. Key entries used: Elinor 1632 + Samuel 1636 Gurney at East Claydon (father John mother Elizabeth); Andtr + Martha Gurney at Chesham (father John mother Elizabeth, range 1576-1682); James 1650 + Elizabeth 1652 Gurney at Wing (father John mother Ann); Isaac Gurney x3 1664 at Cublington (father John mother Mary); Ann Gurny 1666 Aylesbury (father Edward); negative: no Jonathan Gurney baptisms 1645-1649 in Bucks."
    }
```

## 2. Validation notes (proposed thin files)

Create `sources/validations/findmypast-bucks-marriage-index.md`:

```markdown
# Validation - Findmypast Buckinghamshire Marriage Index

- Source ID: `findmypast-bucks-marriage-index`
- Title: Buckinghamshire Marriage Index, Centre for Buckinghamshire Studies, served via Findmypast.
- Method: Findmypast subscription search via Chrome extension on 2026-05-09.
- Key entries used in Gurney research: John Gurney + Alice Oliffe, 24 Apr 1628, Bierton with Broughton (Bucks Archives PR16/1/1Q p. 30); John Gurny + Alice Hewet (widow), 20 Oct 1619, Great Kimble (Bucks Archives D/A/T/116).
- Used in: `research/case-files/john-gurney-case-file-v4.md` §8 Cand A row rewrite, and in `research/people/g13-john-gurney-fact-sheet.research.md`.
```

Create `sources/validations/findmypast-bucks-burial-index.md` (parallel content for the burial entries above).

Create `sources/validations/findmypast-bucks-baptism-index.md` (parallel content for the baptism entries above).

## 3. Proposed case-file edits (research/case-files/john-gurney-case-file-v4.md)

### 3.1 Rewrite the §8 Cand A row

Old:

```markdown
| **Candidate A** | Stewkley/Edlesborough, Bucks | **Alice** Collindridge | **Unlikely (~8–10%)** | Wife named Alice, not Mary. Son Jonathan baptized 1647 = still in England. Moved to Northants. |
```

New:

```markdown
| **Candidate A** | Stewkley (1602/3 bapt., per Sprague); married Bierton with Broughton, Bucks (1628); Aylesbury hundred → Northamptonshire (1641-1650) | **Alice Oliffe** (m. 24 Apr 1628, Bierton with Broughton; Bucks Archives PR16/1/1Q p. 30) | **Very unlikely (~2-4%)** | Wife named Alice, not Mary. Continuing presence in Bucks/Northants documented by the 1628 Bierton marriage to Alice Oliffe, TNA E 115/180/113 (1641 certificate of residence Aylesbury half-hundred → Northamptonshire), and a 1650 John Gurney tenancy at Walgrave, Northamptonshire. No indexed children of the 1628 marriage in Bucks. Earlier research had identified the wife as "Alice Collindridge"; the Bucks Marriage Index gives Alice Oliffe.<sup class="fn"><a href="#nXX" id="ref-XX">XX</a></sup> |
```

Add new endnote (number to assign on application; current endnotes run through `n71` with v20/v21 adding others):

```html
<li id="nXX" value="XX">Findmypast Buckinghamshire Marriage Index, transcript record GBPRS/BUCKINGHAMSHIRE/MAR/000221542, John Gurney + Alice Oliffe, married 24 Apr 1628, Bierton with Broughton, Buckinghamshire, citing Bucks Archives PR16/1/1Q p. 30 (Anglican parish register, register year range 1560-1723); accessed 2026-05-09 via the project's Findmypast subscription. Source ID: <code>findmypast-bucks-marriage-index</code>. The certificate of residence and Walgrave tenancy are recorded in <code>research/case-files/Initial foundation work for john-gurney-case-file/Gurney_ProtestationReturns_Analysis.md</code> and <code>research/case-files/Initial foundation work for john-gurney-case-file/Gurney_Research_Findings_V7.md</code>; the underlying TNA image and the Walgrave tenancy source have not yet been independently pulled in this pass. <a class="backref" href="#ref-XX">↩</a></li>
```

### 3.2 Add three explanatory rows to the §8 elimination table for separately-documented Bucks Johns

```markdown
| East Claydon, Bucks (John + Elizabeth) | Bucks | **Elizabeth** | **ELIMINATED** | Bucks Baptism Index: children Elinor 1632 and Samuel 1636 baptized at East Claydon to father John, mother Elizabeth. Bucks Burial Index: John Gurney buried East Claydon 17 Apr 1654 (Bucks Archives PR51/1/1). This is a separate John Gurney household from Cand A; wife Elizabeth, not Alice Oliffe.<sup class="fn"><a href="#nYY" id="ref-YY">YY</a></sup> |
| Chesham, Bucks (John + Elizabeth) | Bucks | **Elizabeth** | **ELIMINATED** | Bucks Baptism Index: children Andtr and Martha Gurney baptized at Chesham (register range 1576-1682) to father John, mother Elizabeth. Bucks Burial Index: John "G?" Gurney buried Chesham Jul 1672 (Bucks Archives D/A/T/42); John Gurney buried Chesham 11 Jun 1678 (same archive ref). Separate Bucks John household; not Cand A.<sup class="fn"><a href="#nYY" id="ref-YY">YY</a></sup> |
| Cublington, Bucks (John + Mary) | Bucks | **Mary** | **ELIMINATED** | Bucks Baptism Index: Isaac Gurney baptized at Cublington 1664 (three index entries) to father John, mother Mary. A Bucks "John + Mary" household with a son Isaac in 1664. Most plausible identity for the John Gurney + son Isaac who held the Stewkley manor by 1687 and sold to Anne Robinson of Stepney in 1701 (VCH Bucks vol. 3 pp. 420-426); Cublington is ~5 miles SW of Stewkley. Separate from the colonial John, whose Massachusetts estate was inventoried 16 Mar. 1662/3 a year before the 1664 Cublington Isaac baptism.<sup class="fn"><a href="#nYY" id="ref-YY">YY</a></sup> |
| Wing, Bucks (John + Anne) | Bucks | **Anne** | **ELIMINATED** | Bucks Baptism Index: James 1650 and Elizabeth 1652 Gurney at Wing, father John mother Anne. Separate Bucks John household with a wife named Anne, not Mary. Not Cand A.<sup class="fn"><a href="#nYY" id="ref-YY">YY</a></sup> |
| Aylesbury, Bucks (Edward Gurny, 1660s) | Bucks | — | **NOT Cand A; separate Aylesbury household** | Bucks Burial Index: Jon Gurny son of Edward Gurny buried Aylesbury 2 Feb 1665 (Bucks Archives B24). Bucks Baptism Index: Ann Gurny baptized Aylesbury 1666, father Edward. Edward Gurny is a separately documented Aylesbury Gurney head-of-household. The case file should de-link the "Jonathan baptized Aylesbury 22 Nov 1647 son of John" claim from any Cand A line pending verification of the original register entry; the 1665 Aylesbury Jon Gurny was son of Edward, not son of John, and was buried as a child.<sup class="fn"><a href="#nYY" id="ref-YY">YY</a></sup> |
```

Add one new endnote covering all five rows:

```html
<li id="nYY" value="YY">Findmypast Buckinghamshire Marriage Index, Burial Index, and Baptism Index, Centre for Buckinghamshire Studies; subscription pulls executed 2026-05-09. East Claydon burial: GBPRS/BUCKINGHAMSHIRE/BUR record for John Gurney 17 Apr 1654, Bucks Archives PR51/1/1. Chesham burials: D/A/T/42 (Bucks Archives), Jul 1672 and 11 Jun 1678. Aylesbury Edward Gurny burial: B24, 2 Feb 1665. Cublington 1664 Isaac baptisms: Bucks Baptism Index, three index entries, father John mother Mary, Cublington. East Claydon, Chesham, Wing, and Cublington baptisms: Bucks Baptism Index entries linked above. Source IDs: <code>findmypast-bucks-marriage-index</code>, <code>findmypast-bucks-burial-index</code>, <code>findmypast-bucks-baptism-index</code>. <a class="backref" href="#ref-YY">↩</a></li>
```

### 3.3 Update §11 Probability Assessment table for Cand A

Old:

```markdown
| **A — Stewkley, Bucks** | ~8–10% | Wife Alice, not Mary. Jonathan 1647. Deep Bucks roots. |
```

New:

```markdown
| **A — Stewkley / Bierton / Aylesbury → Northants** | **~2-4%** | 1628 Bierton marriage to Alice Oliffe (not Collindridge); 1641 Aylesbury → Northants cert; 1650 Walgrave Northants tenancy; no indexed children in Bucks. Pull Stewkley register (Dickson/Putnam 1897) to close the 1602/3 baptism question and re-score. |
```

Adjust "Unknown other origin" upward by the difference (the ~5-7 points freed) so the table totals stay sane. Document this re-scoring in the working memo, not by re-numbering Cand B/C.

## 4. Proposed G13 research-file edits (research/people/g13-john-gurney-fact-sheet.research.md)

### 4.1 Insert a new "Bucks Gurney household map (2026-05-09 Findmypast pull)" section under "Origin Analysis and Elimination Work"

```markdown
### Bucks Gurney household map (Findmypast indexes, 2026-05-09)

A walk of the Buckinghamshire Marriage Index, Buckinghamshire Burial Index, and Buckinghamshire Baptism Index reveals at least five distinct 17th-century Bucks John Gurney households contemporary with the colonial John Gurney's New England career:

- **Cand A — John Gurney + Alice Oliffe**, married 24 Apr 1628, Bierton with Broughton (Bucks Archives PR16/1/1Q p. 30). No Bucks-indexed children of this marriage; family chronology continues with TNA E 115/180/113 (1641 cert of residence Aylesbury → Northants) and 1650 Walgrave Northants tenancy. The wife's surname Oliffe rewrites the older case-file "Alice Collindridge" identification.
- **John Gurney + Elizabeth at East Claydon**, children Elinor 1632 and Samuel 1636 (Bucks Baptism Index). John Gurney of this household buried East Claydon 17 Apr 1654 (Bucks Burial Index, Bucks Archives PR51/1/1). Separate from Cand A.
- **John Gurney + Elizabeth at Chesham**, children Andtr and Martha (Bucks Baptism Index, register range 1576-1682). John Gurney burials at Chesham Jul 1672 and 11 Jun 1678 (Bucks Burial Index, Bucks Archives D/A/T/42). Separate household.
- **John Gurney + Anne at Wing**, children James 1650 and Elizabeth 1652 (Bucks Baptism Index). Separate household.
- **John Gurney + Mary at Cublington**, son Isaac baptized 1664 (three Bucks Baptism Index entries; possibly triplets or duplicate transcriptions). Most plausible identity for the John Gurney + son Isaac who held the Stewkley manor by 1687 and sold to Anne Robinson of Stepney in 1701 per VCH Bucks vol. 3 pp. 420-426; Cublington is ~5 miles SW of Stewkley. A Bucks "John + Mary" household post-dating the colonial John's death (16 Mar. 1662/3 inventory).

Additionally, **Edward Gurny** was a separate Aylesbury Gurney head-of-household in the 1660s: son Jon Gurny buried 2 Feb 1665 (Bucks Archives B24) and daughter Ann Gurny baptized 1666 (Bucks Baptism Index). The older case-file claim "Jonathan baptized Aylesbury 22 Nov 1647 son of John" should be qualified — the 1665 Aylesbury Jon was son of Edward, and the Bucks Baptism Index returns zero Jonathan Gurney baptisms 1645-1649 with father John or father Edward.[^findmypast-bucks-2026-05-09]

[^findmypast-bucks-2026-05-09]: Findmypast Buckinghamshire Marriage Index, Burial Index, and Baptism Index (Centre for Buckinghamshire Studies); subscription pulls executed 2026-05-09. Source IDs: `findmypast-bucks-marriage-index`, `findmypast-bucks-burial-index`, `findmypast-bucks-baptism-index`.
```

### 4.2 Replace the existing "Candidate A" line in the Working Hypotheses block

Old:

```markdown
- **Candidate A** (Stewkley, Buckinghamshire): **~10–12%**. Weakened, but not eliminated.
```

New:

```markdown
- **Candidate A** (Stewkley bapt. 1602/3 → Bierton with Broughton m. 1628 → Aylesbury hundred → Walgrave Northants 1650): **~2-4%**. Materially weakened by the 1628 Bierton marriage to Alice Oliffe (not Collindridge) and by the existing 1641 TNA E 115/180/113 cert of residence and 1650 Walgrave tenancy. Pull Stewkley register (Dickson/Putnam 1897) to close the 1602/3 baptism question.
```

### 4.3 Promote the Stewkley Dickson/Putnam 1897 register to the very top of the Tier-1B target list

Move the entry (already added in v21) to first position under Tier 1B with the explicit framing that closing the 1602/3 baptism is the discriminating pull for Cand A.

## 5. Apply order

When approved (after v20 and v21):

1. Add the three Findmypast Bucks source IDs to `data/sources.json`.
2. Create the three thin validation files in `sources/validations/`.
3. Edit `research/case-files/john-gurney-case-file-v4.md` per §3.
4. Edit `research/people/g13-john-gurney-fact-sheet.research.md` per §4.
5. Update `sources/intake/working/john-gurney-audit-state.md` to mark v22 as applied.
