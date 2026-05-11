# Intake patchset v27 - Case file §8 consolidation (table + detail subsections)

```yaml
patchset_id: v27
created: 2026-05-11
repo_scope: gurney-genealogy
phase: phase_1_patchset_only
primary_case_file: research/case-files/john-gurney-case-file-v4.md
working_memo: sources/intake/working/john-gurney-audit-state.md
phase_2_rule: Apply v27 §3 as the FULL replacement for §8 in the case file. The §8-table-row edits proposed in v21, v22, v23, v24, v25, and v26 are SUPERSEDED by v27. The non-§8 edits in those patchsets (sources.json, G13 sections, §1, §11, §13, endnotes, validations) remain valid as written.
```

## 0. Audit report

### 0.1 Why v27

Across v21-v26, each new evidence pass appended a longer "Primary Elimination Reason" cell to its candidate row in §8. The cell text is now several sentences per row, which is poor table form. Per project rule (research-writing-style.md: "Use headings only when they improve retrieval... Keep entries compact."), the §8 table should carry short cells with crumb references and the detailed evidence should live in named subsections below the table.

v27 restructures §8 to:

- A compact elimination table where each candidate's "Primary Elimination Reason" is 10-15 words plus a cross-reference such as "(see §8.X)";
- Detail subsections §8.1 Candidate A, §8.2 Candidate C, §8.3 Buckinghamshire same-county Aylesbury cluster (the prior §8.1 note, revised), and §8.4 New Norfolk John Gurney households (Pass 7 add).

### 0.2 What v27 does NOT change

- Sources, validations, endnotes (n7, n9, nXX, nYY, nZA, nZB, nZC, etc.) and §1, §11, §13.2, §13.3 cell-level edits proposed in v20-v26 are unchanged.
- G13 research-companion edits (Cand A Aylesbury family group; Cand C Berkhamsted family group; Bucks Gurney household map; Anne Cowheard note; FS Tree LT9Z-KQ1 note; Norfolk Gurney density; Stewkley 1603 FS-indexed) remain as written in those patchsets.
- The probability assessment in §11 is not changed by v27.

### 0.3 Note on Cand A vs Cand C ordering

The case file's existing §8 row order leads with Candidate B (this case file's preferred candidate), then Candidate A, then Candidate C. v27 preserves that row order in the table. The §8.1 subsection covers Candidate A and §8.2 covers Candidate C, matching the user's requested numbering. The earlier §8.1 "Buckinghamshire Cluster Note" is renumbered to §8.3 with the title "Buckinghamshire same-county cluster and Aylesbury households."

## 1. Source registry operation

None. v27 is purely a case-file structural edit.

## 2. Validation note

None. v27 is purely a case-file structural edit.

## 3. Proposed case-file edits (research/case-files/john-gurney-case-file-v4.md)

### 3.1 Replace the existing §8 elimination table

Old table (post-v20 baseline; v21-v26 edits superseded):

```html
<h2 id="s9">8. PROCESS OF ELIMINATION: OTHER JOHN GURNEYS</h2>

A central method in emigrant-identification is eliminating other John Gurneys who remained in England. The following table combines parish-register evidence with TNA Prerogative Court of Canterbury probate records. Anyone documented in England after 1641 — alive or dead there — is eliminated.<sup class="fn"><a href="#n60" id="ref-60">60</a></sup>

| John Gurney | Location | Wife | Status | Primary Elimination Reason |
|---|---|---|---|---|
| **Candidate B** (this case file) | East Dereham, Norfolk | Unknown | **PROBABLE (~55–60%)** | Son of Merchant Taylor. Occupational, geographic, financial match. |
| **Candidate A** | Stewkley/Edlesborough, Bucks | **Alice** Collindridge | **Unlikely (~8–10%)** | Wife named Alice, not Mary. Son Jonathan baptized 1647 = still in England. Moved to Northants. |
| **Candidate C** | Berkhamsted, Herts | Unknown | **Open (~3–5%)** | Father of Richard (1626) and Sara (1634). No disqualifying evidence. |
... (rest of rows unchanged through Cripplegate joiner row) ...
```

New table (v27 replacement):

```html
<h2 id="s9">8. PROCESS OF ELIMINATION: OTHER JOHN GURNEYS</h2>

A central method in emigrant-identification is eliminating other John Gurneys who remained in England. The following table combines parish-register evidence with TNA Prerogative Court of Canterbury probate records and post-2026 Findmypast and FamilySearch index pulls. Anyone documented in England after 1641 — alive or dead there — is eliminated. Detailed evidence chains for the most-worked candidates live in §8.1 through §8.4 below.<sup class="fn"><a href="#n60" id="ref-60">60</a></sup>

| John Gurney | Location | Wife | Status | Primary Elimination Reason |
|---|---|---|---|---|
| **Candidate B** (this case file) | East Dereham, Norfolk | Unknown | **PROBABLE (~55–60%)** | Son of Merchant Taylor. Occupational, geographic, financial match. |
| **Candidate A** | Stewkley → Bierton → Aylesbury → Northants | **Alice Oliffe** | **Effectively eliminated (~1–2%)** | Continuous English residence 1603–1653 documented (see §8.1). |
| **Candidate C** | Berkhamsted, Herts | Unknown | **Effectively eliminated (~0–1%)** | Eight-child Berkhamsted family 1610–1636; age and naming mismatches (see §8.2). |
| Earsham, Norfolk | Norfolk | **Elizabeth** Singler | **ELIMINATED** | Died in England. Will proved 1639. |
| Eythorne, Kent | Kent | **Mary** Marsh | **ELIMINATED** | Died and buried Eythorne 1648. Full pedigree. |
| Toddington, Beds | Beds | **Elizabeth** Moreton | **ELIMINATED** | Wife Elizabeth, not Mary. |
| Norwich (m. 1639) | Norfolk | **Jane** Wright | **ELIMINATED** | Married 1639 — still present after emigrant departed. |
| St Botolph Aldgate, London | London | **Mary** | **ELIMINATED** | Alive 1666. Merchant. Will (PROB 11/382/271). |
| Winkfield, Berkshire | Berkshire | **Alice/Ellice** | **ELIMINATED** | Alive 1682. Yeoman. Will (PROB 11/372/123). |
| Aylesbury, Bucks (probate) | Bucks | **Sarah** (prob.) | **ELIMINATED** | Alive late 17th c. Probate sentence (PROB 11/337/37). |
| East Grinstead, Sussex | Sussex | **Dorothy** | **ELIMINATED** | Alive 1654. Yeoman. Will (PROB 11/252/319). |
| Albury, Herts | Herts | **Jane** | **ELIMINATED** | Alive 1676. Husbandman. Will (PROB 11/335/425). |
| East Chiltington, Sussex | Sussex | Unknown | **ELIMINATED** | Alive mid-1650s. Shepherd. Probate (PROB 11/241/246; PROB 11/242/723). |
| Ackworth, Yorkshire | Yorkshire | **Mary** Barton (claimed) | **Unlikely** | Yorkshire outside emigrant corridor; v2 attribution unconfirmed in 2026 pass. |
| Cheddington, Bucks | Bucks | — | **ELIMINATED** | Father Richard Gurney, not John. Isaac Gurney clan. |
| St Giles Cripplegate, London (Francis B) | London | — | **ELIMINATED** | Died age 2 days. Son of Francis B laceweaver. |
| Maldon, Essex (bachelor) | Essex | (unmarried) | **ELIMINATED** | Bachelor; died 1681; hearth tax 1674.<sup class="fn"><a href="#n65" id="ref-65">65</a></sup> |
| Harrow on the Hill / Okington | Middlesex | **Mary** | **ELIMINATED** | Active in England 1669; six years after MA John died.<sup class="fn"><a href="#n69" id="ref-69">69</a></sup> |
| St Giles Cripplegate (Francis Garney joiner) | London | — | **ELIMINATED** | Burial 1640 of "John sonne of ffrancis Garney Joyner."<sup class="fn"><a href="#n70" id="ref-70">70</a></sup> |
| East Claydon, Bucks (John + Elizabeth) | Bucks | **Elizabeth** | **ELIMINATED** | Children Elinor 1632, Samuel 1636; John buried East Claydon 1654 (see §8.3). |
| Chesham, Bucks (John + Elizabeth) | Bucks | **Elizabeth** | **ELIMINATED** | Children Andtr, Martha; John buried Chesham 1672 and 1678 (see §8.3). |
| Cublington, Bucks (John + Mary) | Bucks | **Mary** | **ELIMINATED** | Son Isaac 1664; likely the Stewkley manor 1687 holder (see §8.3). |
| Wing, Bucks (John + Anne) | Bucks | **Anne** | **ELIMINATED** | Children James 1650, Elizabeth 1652 (see §8.3). |
| Aylesbury, Bucks (Edward Gurny) | Bucks | — | **Not Cand A** | Edward Gurny household, distinct from Cand A (see §8.3). |
| Denton, Norfolk (John + Rachell) | Norfolk | **Rachell** | **ELIMINATED** | Mary 1638, Thomas 1639, Sarah 1644 to John + Rachell (see §8.4). |
| Hempnall, Norfolk | Norfolk | Unknown | **ELIMINATED** | Anna 1640, Elizabeth 1641 to John (see §8.4). |
```

(Note: the §10 "9. SEPARATING THE TWO FRANCIS GURNEYS" heading and onwards remains as in v4. The 8.1 Buckinghamshire Cluster Note paragraph in v4 is moved into the new §8.3 subsection below.)

### 3.2 Replace the existing "8.1 Buckinghamshire Cluster Note" with four subsections

Old (case-file v4, immediately under the §8 table):

```html
### 8.1 Buckinghamshire Cluster Note

Multiple Gurney branches existed simultaneously in Buckinghamshire. The Aylesbury probate records show a Bucks family (Daniel Gurney d.1669, with brother John and wife Sarah) distinct from Candidate A's Stewkley/Edlesborough line. No PCC record directly names Stewkley, Edlesborough, or Alice Collindridge.
```

New (four subsections):

```html
### 8.1 Candidate A — Stewkley → Bierton → Aylesbury → Northants

Candidate A's complete English residence chain is documented end-to-end by indexed primary records.

- **Birth: 21 February 1603, Stewkley, Buckinghamshire.** FamilySearch, "England, Births and Christenings, 1538-1975," Jhon Gurney son of Jhon Gurney, FS ID <a href="https://www.familysearch.org/ark:/61903/1:1:JMRS-DX6">JMRS-DX6</a>. Confirms the Sprague Stewkley attribution at primary-index level.
- **Marriage: 24 April 1628, Bierton with Broughton, Bucks.** Findmypast Buckinghamshire Marriage Index, transcript GBPRS/BUCKINGHAMSHIRE/MAR/000221542, John Gurney + Alice Oliffe, Buckinghamshire Archives PR16/1/1Q p. 30. The bride's surname is Oliffe, not Collindridge (the older repo Collindridge attribution is unsupported by the Bucks index).
- **Children, Saint Mary, Aylesbury, 1639-1653.** FS England Births and Christenings index entries: Sarah Gurney bapt. 22 August 1639 dau. of John; Daniell Gurney bapt. 26 December 1645 son of John (FS ID JWN5-W5B); Jonathan Gurney bapt. 22 November 1647 son of John (FS ID JMBC-P2G); Hannah Gurney bapt. 12 November 1653 dau. of John.
- **Residence transition: 1641, Aylesbury half-hundred → Northamptonshire.** TNA E 115/180/113 certificate of residence (recorded in <code>research/case-files/Initial foundation work for john-gurney-case-file/Gurney_ProtestationReturns_Analysis.md</code>; underlying image not yet pulled).
- **1650: tenant at Walgrave, Northamptonshire.** Recorded in <code>Gurney_Research_Findings_V7.md</code>.

The 1639-1653 Aylesbury family group is structurally incompatible with the colonial John Gurney's continuous New England career (Weymouth fine June 1641; Wilson v. Faxon deposition 1653 at Braintree; Braintree death 1662/3). Cand A is therefore the Aylesbury John, not the MA emigrant. The case file's earlier "Alice Collindridge" wife identification is unsupported and is replaced here by Alice Oliffe per the 1628 Bucks Marriage Index entry. The Stewkley Dickson/Putnam 1897 printed register remains useful for sibling and burial context but is no longer the discriminating instrument for closing Cand A.

A separate FamilySearch entry surfaces John Gurney + Anne Cowheard, married 25 October 1638, Saint Mary, Aylesbury (FS ID N2TD-Z9Z). Either (a) a separately documented Aylesbury John, or (b) Cand A remarrying at Aylesbury after Alice Oliffe died. The 1645 Daniell, 1647 Jonathan, and 1653 Hannah FS index records do not carry an indexed mother, so the marriage-to-children link cannot be proven from FS alone. Carry as a wife-uncertainty note rather than a controlling fact.<sup class="fn"><a href="#nZA" id="ref-ZA">ZA</a></sup>

### 8.2 Candidate C — Berkhamsted, Hertfordshire

Findmypast Hertfordshire Baptism Index documents an eight-child Berkhamsted family with father John Gurney 1610-1636:

- Henry Gourney, 1610
- Sara Gourney, 1615 (first daughter Sara; presumably died young)
- Jhon Gourney, 1624
- Richard Gourney, 1626 (case-file standing)
- Elizabeth Gourney, 1629
- Michael Gourney, 1631
- Sarah Gourney, 1634 (second daughter Sara; case-file standing)
- Francis Gurney, 1636

Three independent elimination reasons:

1. **Age mismatch.** Henry's 1610 baptism requires Cand C's John to be born no later than ~1585-1590. The colonial John was b. ~1603 per the 1653 deposition ("aged about 50 years," NEHGR 62:94 / Suffolk Court Files item 188). Cand C's John is ~13-18 years too old.
2. **A Francis son in 1636.** The colonial John named no child Francis (the case file's strongest naming-pattern argument against Candidate B applies here equally).
3. **No Mary, no Peter.** The colonial John's two distinctive children (Mary m. Daniel Shed; Peter, name foreign to most Gurney branches) are absent from the Berkhamsted family group.

Findmypast Hertfordshire Burial Index returned 48 John Gurney burials county-wide; only two pre-1700 Berkhamsted entries (Jhon Gourney 1612 and 1620), both predating Cand C's documented children. Zero John Gurney burials at Berkhamsted 1640-1700.<sup class="fn"><a href="#nZB" id="ref-ZB">ZB</a></sup>

### 8.3 Buckinghamshire same-county cluster and Aylesbury households

Buckinghamshire in the mid-17th century supported at least six distinct contemporaneously-active John Gurney households separate from Cand A:

- **East Claydon (John + Elizabeth):** children Elinor 1632, Samuel 1636 (Bucks Baptism Index); John buried East Claydon 17 April 1654 (Bucks Burial Index, Bucks Archives PR51/1/1).
- **Chesham (John + Elizabeth):** children Andtr and Martha (register range 1576-1682, Bucks Baptism Index); John burials at Chesham July 1672 and 11 June 1678 (Bucks Burial Index, Bucks Archives D/A/T/42).
- **Wing (John + Anne):** children James 1650, Elizabeth 1652 (Bucks Baptism Index).
- **Cublington (John + Mary):** son Isaac baptized 1664 (three Bucks Baptism Index entries; possibly triplets or duplicate transcriptions). Most plausible identity for the John Gurney + son Isaac who held the Stewkley manor by 1687 and sold to Anne Robinson of Stepney in 1701 per VCH Bucks vol. 3 pp. 420-426; Cublington is ~5 miles SW of Stewkley.
- **Weston Turville (John):** child Elyzabethe 1627 (Bucks Baptism Index).
- **Great Kimble (John + Alice Hewet, widow):** earlier marriage 20 October 1619 (Bucks Marriage Index, D/A/T/116). Generational predecessor.

Additionally, Aylesbury parish records show a separately-documented **Edward Gurny household** in the 1660s: son Jon Gurny buried 2 February 1665 (Bucks Burial Index, Bucks Archives B24) and daughter Ann Gurny baptized 1666 (Bucks Baptism Index). Edward Gurny is distinct from Cand A and from the Aylesbury family group in §8.1.

The Aylesbury probate records also show a separate Bucks family — Daniel Gurney d. 1669, with brother John and wife Sarah (PROB 11/347/122 + PROB 11/337/37) — distinct from Cand A's line. No PCC record directly names Stewkley, Edlesborough, or Alice Oliffe.<sup class="fn"><a href="#nYY" id="ref-YY">YY</a></sup>

### 8.4 New Norfolk John Gurney households (Pass 7)

A Findmypast UK Parish Baptisms search for Norfolk Gurney baptisms with father John, 1623-1643, returned 14 results across six Norfolk parishes. Two new households (not previously in the case file) are listed in the §8 table:

- **Denton, Norfolk — John Gurney + Rachell.** Mary Gurney christened 10 August 1638 (FS ID `NNDF-V9K`, mother Rachell on the index record); Thomas Gurney 24 January 1639; Sarah Gurney 1644. Wife Rachell ≠ Mary, and the children's dates are ~10 years too late for the colonial John's Mary (c.1628) and Sarah (c.1625-1632).
- **Hempnall and the Hempnall Group of Parishes, Norfolk — John Gurney.** Anna Gurney 1640, Elizabeth Gurney 1641 (Norfolk Baptisms). No Mary or Peter in the indexed children.

The Norfolk Gurney density (six distinct John Gurney households in mid-17th-century Norfolk including Earsham, Stanfield, Norwich St Margaret & St Swithin, and North Runcton — see G13 for the full map) is consistent with Cand B's geographic plausibility but does not individually match the colonial John's full distinctive children pattern.<sup class="fn"><a href="#nZC" id="ref-ZC">ZC</a></sup>
```

### 3.3 No other case-file changes in v27

§§1, 2, 3, 4, 5, 6, 7 are unchanged.  
§§9-13 are unchanged (probability table in §11 is unchanged from v23/v24 levels; §13 demotion of the Stewkley Dickson/Putnam pull remains as in v26).

## 4. Apply order

When approved:

1. Replace §8 in `research/case-files/john-gurney-case-file-v4.md` with the v27 §3 content.
2. Confirm that the endnote references in the new table (`n60`, `n65`, `n69`, `n70`, `nZA`, `nZB`, `nZC`, `nYY`) match the endnote IDs that v22-v25 propose (or will be renumbered on application). The endnote bodies themselves come from v22-v25; v27 does not add new endnote bodies.
3. Update `sources/intake/working/john-gurney-audit-state.md` to mark v27 as applied.
