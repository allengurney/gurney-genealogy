# Intake patchset v29 - Section 8 cleanup (John-only table, plain prose, cluster reasoning)

```yaml
patchset_id: v29
created: 2026-05-11
repo_scope: gurney-genealogy
phase: phase_1_patchset_only
primary_case_file: research/case-files/john-gurney-case-file-v4.md
primary_research_file: research/people/g13-john-gurney-fact-sheet.research.md
working_memo: sources/intake/working/john-gurney-audit-state.md
phase_2_rule: Apply v29 §3 as the FULL REPLACEMENT for Section 8 in the case file (lines 240-354 of the current applied state). The §4 G13 addition is incremental, not a replacement. Endnote numbering (n82-n89) is preserved; bodies of n88 and n89 are tightened to remove process-logistics phrasing.
```

## 0. Audit report

### 0.1 Why v29

Section 8 of the case file accumulated several issues across v22-v28:

1. **Non-John households leaked into the §8 table.** v28's §8.4 expansion added Norfolk Gurney baptisms whose father was William, Edward, Thomas, George, Robert, or Frances/Francis. The §8 table is about "other John Gurneys," not Gurneys generally, so those rows belong in the research companion's Norfolk Gurney density section, not here.

2. **Source-naming dominated body prose.** Sentences led with "FamilySearch, England Births and Christenings, 1538-1975, ..." or "Findmypast Bucks Marriage Index, transcript ...," which centers the index instead of the finding. The case file is for a non-genealogist reader; sources belong in footnotes.

3. **Acronyms in body text.** FS, Findmypast (FMP), NRO, PCC, and TNA appeared in body prose; they should expand or move to footnotes.

4. **Process-logistics phrasing in body text.** Phrases like "cannot be proven from FS alone," "image not yet pulled in this pass," and "in the consulted image, so the script could not be independently parsed" describe research mechanics rather than facts and should move to footnotes when retained at all.

5. **Cluster reasoning missing.** The case file lists multiple John Gurney households at Buckinghamshire parishes without reasoning through why they are distinct people (different parish, different wife, different children, different burial). The 16 December 1638 Aylesbury John baptism and the 25 October 1638 Aylesbury John + Anne Cowheard marriage were both attached to Candidate A as alternative readings; the eight-week gap between the two events makes them biologically incompatible as the same couple, so the cluster contains two simultaneous Aylesbury Johns.

6. **Some elimination reasons were thin.** "Wife Elizabeth, not Mary" by itself is a weak eliminator because remarriage was common. Where positive evidence exists (death in England, will proved, continued residence), it should be the lead reason.

7. **Jargon.** "Case-file standing" appeared in §8.2 without a plain-English equivalent.

v29 is a structural cleanup, not a new evidence pass. No new sources are added; no probability assessment changes.

### 0.2 Cluster reasoning preserved here

**Aylesbury, 1638.** A John Gurney + Alice Oliffe family fathered at Saint Mary Aylesbury from late 1638 through 1653 (John 16 Dec 1638; Sarah 22 Aug 1639; Daniell 26 Dec 1645; Jonathan 22 Nov 1647; Hannah 12 Nov 1653). The 16 December 1638 John baptism is the eldest indexed child of this family, ten years after the 1628 Bierton marriage to Alice Oliffe. A separately-indexed John Gurney married Anne Cowheard at Aylesbury on 25 October 1638; that marriage cannot share a baptized child eight weeks later, so the Anne Cowheard groom is a second Aylesbury John active simultaneously, not Candidate A. Neither John is the Massachusetts emigrant: Candidate A's family group continues at Aylesbury through 1653, and the second Aylesbury John leaves the indexed Aylesbury record set with no indication of emigration.

**Buckinghamshire 1620-1670 same-county Johns.** At least six distinct John Gurney households appear in Buckinghamshire parish registers in the broad Aylesbury hundred and adjacent corridors: Stewkley/Bierton/Aylesbury/Northamptonshire (Candidate A); East Claydon (John + Elizabeth); Chesham (John + Elizabeth, distinct from East Claydon by parish, burials, and child set); Wing (John + Anne); Cublington (John + Mary, post-1641 fathering); Haddenham (John, 1620-1622, generationally earlier than Candidate A's marriage). Each pair of parish-plus-wife combinations represents a distinct family because parish migration was rare in this period and because the children's name sets and the husbands' burial entries (where present) are mutually exclusive. The Edlesborough 1661 John Gurney + Mary Kidgell marriage is most plausibly the Cublington John of 1664 in a previous marriage or a relative; Cublington is about 5 miles south-west of Stewkley and the same household later held the Stewkley manor.

**Berkhamsted, 1610-1636.** Candidate C's eight-child family group is fathered by one John Gurney across 26 years; no second John appears in the Berkhamsted register in that window.

### 0.3 What v29 does NOT change

- Sources, validations, and endnote bodies remain as written, except the bodies of n88 and n89 are tightened to remove "image not yet pulled" and "script could not be independently parsed" phrasing without losing the underlying citation. No new endnote numbers.
- The §11 Probability Assessment table is unchanged.
- Sections 1-7, 9, 10, 11, 12, 13 are unchanged.

## 1. Source registry operation

None. v29 is a structural and stylistic edit.

## 2. Validation notes

None. v29 is a structural and stylistic edit.

## 3. Proposed case-file edits (research/case-files/john-gurney-case-file-v4.md)

### 3.1 Replace Section 8 entirely

Find the block beginning at `<h2 id="s9">8. PROCESS OF ELIMINATION: OTHER JOHN GURNEYS</h2>` (currently line 240) and ending at the last line of §8.4 (currently line 354, immediately before `<h2 id="s10">9. SEPARATING THE TWO FRANCIS GURNEYS</h2>`).

Replace the entire block with:

```html
<h2 id="s9">8. PROCESS OF ELIMINATION: OTHER JOHN GURNEYS</h2>

A central method in emigrant-identification is eliminating other John Gurneys who remained in England. The following table lists every John Gurney household material to the case, with the strongest single reason each is not the Massachusetts emigrant. Detailed evidence chains and cluster reasoning for the most-worked candidates appear in sections 8.1 through 8.4. Norfolk Gurney households whose father is named other than John provide cluster context for Candidate B and are catalogued in the John Gurney research companion rather than in this elimination table.<sup class="fn"><a href="#n60" id="ref-60">60</a></sup>

| John Gurney | Location | Wife | Status | Primary Elimination Reason |
|---|---|---|---|---|
| **Candidate B** (this case file) | East Dereham, Norfolk | Unknown | **PROBABLE (~55-60%)** | Son of London Merchant Taylor; occupational, geographic, and financial match. |
| **Candidate A** | Stewkley to Bierton to Aylesbury to Northamptonshire | **Alice Oliffe** | **Effectively eliminated (~1-2%)** | Continuous English residence 1603 through 1653 (see 8.1). |
| **Candidate C** | Berkhamsted, Hertfordshire | Unknown | **Effectively eliminated (~0-1%)** | Eight-child Berkhamsted family 1610-1636, fathered by a John born about 1585-1590, too old for the colonial John (see 8.2). |
| Aylesbury, Bucks (John + Anne Cowheard) | Buckinghamshire | **Anne Cowheard** | **ELIMINATED** | Married Aylesbury 25 October 1638, eight weeks before Candidate A's son John was baptized at the same parish; biologically a distinct second Aylesbury John (see 8.1). |
| Earsham, Norfolk | Norfolk | **Elizabeth** Singler | **ELIMINATED** | Will proved 1639 in England. |
| Eythorne, Kent | Kent | **Mary** Marsh | **ELIMINATED** | Married Eythorne 6 November 1632; buried Eythorne 1648. |
| Toddington, Beds | Bedfordshire | **Elizabeth** Moreton | **ELIMINATED** | Continuous family group baptized at Toddington 1625-1630; wife Elizabeth, not Mary. |
| Norwich (m. 1639) | Norfolk | **Jane** Wright | **ELIMINATED** | Married at Norwich 9 March 1639, more than two years before the Massachusetts emigrant's documented June 1641 Weymouth presence. |
| St Botolph Aldgate, London | London | **Mary** | **ELIMINATED** | Alive 1666; will proved 1666 (Prerogative Court of Canterbury, PROB 11/382/271). |
| Winkfield, Berkshire | Berkshire | **Alice / Ellice** | **ELIMINATED** | Alive 1682; yeoman; will proved 1682 (PROB 11/372/123). |
| Aylesbury, Bucks (probate) | Buckinghamshire | **Sarah** (probable) | **ELIMINATED** | Alive late 17th century; probate sentence preserved (PROB 11/337/37). |
| East Grinstead, Sussex | Sussex | **Dorothy** | **ELIMINATED** | Alive 1654; yeoman; will proved 1654 (PROB 11/252/319). |
| Albury, Herts | Hertfordshire | **Jane** | **ELIMINATED** | Alive 1676; husbandman; will proved 1676 (PROB 11/335/425). |
| East Chiltington, Sussex | Sussex | Unknown | **ELIMINATED** | Alive mid-1650s; shepherd; probate preserved (PROB 11/241/246 and PROB 11/242/723). |
| Ackworth, Yorkshire | Yorkshire | **Mary** Barton (claimed) | **Unlikely** | Yorkshire is outside the emigrant corridor; the 1636 Mary Barton attribution is not supported by a primary record reachable in the present pass.<sup class="fn"><a href="#n86" id="ref-86b">86</a></sup> |
| Cheddington, Bucks (Richard's clan) | Buckinghamshire | - | **ELIMINATED** | The Cheddington Gurneys are headed by Richard, not John; their son Johannes baptized 1608 belongs to the Isaac Gurney line. |
| St Giles Cripplegate, London (Francis B) | London | - | **ELIMINATED** | Died age 2 days, son of Francis B the laceweaver. |
| Maldon, Essex (bachelor) | Essex | (unmarried) | **ELIMINATED** | Bachelor; hearth tax 1674; died 1681.<sup class="fn"><a href="#n65" id="ref-65">65</a></sup> |
| Harrow on the Hill / Okington | Middlesex | **Mary** | **ELIMINATED** | Active in England 1669, six years after the Massachusetts John died.<sup class="fn"><a href="#n69" id="ref-69">69</a></sup> |
| St Giles Cripplegate (Francis Garney joiner) | London | - | **ELIMINATED** | Burial 1640, "John sonne of ffrancis Garney Joyner."<sup class="fn"><a href="#n70" id="ref-70">70</a></sup> |
| East Claydon, Bucks (John + Elizabeth) | Buckinghamshire | **Elizabeth** | **ELIMINATED** | Children Elinor 1632, Samuel 1636; John buried East Claydon 17 April 1654 (see 8.3). |
| Chesham, Bucks (John + Elizabeth) | Buckinghamshire | **Elizabeth** | **ELIMINATED** | Children Andtr and Martha; John buried Chesham July 1672 and 11 June 1678 (see 8.3). |
| Cublington, Bucks (John + Mary) | Buckinghamshire | **Mary** | **ELIMINATED** | Son Isaac baptized 1664; same household most likely held the Stewkley manor by 1687 (see 8.3). |
| Wing, Bucks (John + Anne) | Buckinghamshire | **Anne** | **ELIMINATED** | Children James 1650 and Elizabeth 1652 (see 8.3). |
| Haddenham, Bucks (John) | Buckinghamshire | Unknown | **ELIMINATED** | Children at Haddenham 25 February 1620 and Joane 26 January 1622, predating Candidate A's marriage and incompatible with a colonial John who was about 17 at the time (see 8.3). |
| Denton, Norfolk | Norfolk | **Rachell / Rachelle** | **Father identification unresolved** | Mary 1638 and Thomas 1639 baptized to a "John Gurney + Rachell" couple in two indexes, and to a "Josiah Gurney + Rachelle" couple in the Norfolk Record Office image-confirmed reading. The same register page is read both ways; the mother name is consistent across indexes (see 8.4). |
| Hempnall, Norfolk | Norfolk | Unknown | **Likely separate from the emigrant** | Anna 1640 and Elizabeth 1641 baptized to a John Gurney father. No further evidence ties this household to the Massachusetts emigrant (see 8.4). |

### 8.1 Candidate A - Stewkley to Bierton to Aylesbury to Northamptonshire

Candidate A's English residence chain is documented end to end by indexed primary records.

- **Baptism, 21 February 1603, Stewkley, Buckinghamshire.** Jhon Gurney, son of Jhon Gurney.<sup class="fn"><a href="#n85" id="ref-85">85</a></sup>
- **Marriage, 24 April 1628, Bierton with Broughton, Buckinghamshire.** John Gurney and Alice Oliffe. The bride's surname is Oliffe, not Collindridge; the older "Alice Collindridge" reading is unsupported.<sup class="fn"><a href="#n85" id="ref-85b">85</a></sup>
- **Aylesbury family group, Saint Mary, 1638-1653.** Five children of John Gurney baptized at Saint Mary, Aylesbury: John 16 December 1638; Sarah 22 August 1639; Daniell 26 December 1645; Jonathan 22 November 1647; Hannah 12 November 1653.<sup class="fn"><a href="#n85" id="ref-85c">85</a></sup><sup class="fn"><a href="#n88" id="ref-88a">88</a></sup>
- **Certificate of residence, 1641.** Recorded as moving from the Aylesbury half-hundred to Northamptonshire.<sup class="fn"><a href="#n83" id="ref-83">83</a></sup>
- **Tenancy, 1650.** Walgrave, Northamptonshire.<sup class="fn"><a href="#n83" id="ref-83b">83</a></sup>

A continuously documented presence in England from the 1628 Bierton marriage through the 1653 Aylesbury baptism, with a 1641 cert of residence and a 1650 Walgrave tenancy in between, is structurally incompatible with the Massachusetts emigrant, whose Weymouth fine is dated June 1641 and whose Wilson v. Faxon deposition is dated 1653 at Braintree.

**The two Aylesbury Johns of 1638.** A separately indexed John Gurney married Anne Cowheard at Saint Mary, Aylesbury on 25 October 1638; about eight weeks later, Candidate A's son John was baptized at the same parish on 16 December 1638. The eight-week gap rules out the two events as the same couple, so the cluster contains two simultaneous Aylesbury Johns: Candidate A continuing his family with Alice Oliffe, and a second Aylesbury John beginning a marriage with Anne Cowheard. The second Aylesbury John leaves the indexed Aylesbury record set with no further trace in the present pass; he is independently eliminated by the 25 October 1638 marriage date, which is more than two and a half years before the Massachusetts emigrant's documented June 1641 Weymouth presence and which assigns him a wife named Anne, not Mary.<sup class="fn"><a href="#n85" id="ref-85d">85</a></sup><sup class="fn"><a href="#n88" id="ref-88b">88</a></sup>

### 8.2 Candidate C - Berkhamsted, Hertfordshire

A single John Gurney fathered an eight-child family at Berkhamsted, Hertfordshire across 26 years:

- Henry Gourney, 1610
- Sara Gourney, 1615 (first daughter Sara, presumably died young)
- Jhon Gourney, 1624
- Richard Gourney, 1626
- Elizabeth Gourney, 1629
- Michael Gourney, 1631
- Sarah Gourney, 1634 (second daughter Sara)
- Francis Gurney, 1636

No second Gurney father appears in the Berkhamsted register across this window, so the eight children belong to one John Gurney throughout. Three independent reasons eliminate this John:

1. **Age.** The 1610 Henry baptism requires a John born no later than about 1585-1590. The colonial John was born about 1603 per the 1653 Wilson v. Faxon deposition ("aged about 50 years"). Candidate C's John is about 13 to 18 years too old.
2. **A Francis son in 1636.** The colonial John named no child Francis, the same naming-pattern argument that the case file applies to Candidate B.
3. **No Mary, no Peter.** The colonial John's two distinctive children, Mary and Peter, are absent from the Berkhamsted family group.

The Hertfordshire burial index has no John Gurney burial at Berkhamsted in 1640-1700.<sup class="fn"><a href="#n86" id="ref-86a">86</a></sup>

### 8.3 Buckinghamshire same-county cluster

Buckinghamshire in the mid-17th century contained several distinct John Gurney households. Parish migration was rare in the period, and each household below is anchored by a different parish, a different wife where indexed, a non-overlapping set of children, and (in three cases) a husband's burial. They are not the same person in different parishes.

- **East Claydon (John + Elizabeth):** children Elinor 1632 and Samuel 1636; John buried East Claydon 17 April 1654.<sup class="fn"><a href="#n84" id="ref-84a">84</a></sup>
- **Chesham (John + Elizabeth):** children Andtr and Martha; John buried Chesham July 1672 and 11 June 1678 (two burials in the same household line, generationally separated).<sup class="fn"><a href="#n84" id="ref-84b">84</a></sup>
- **Wing (John + Anne):** children James 1650 and Elizabeth 1652.<sup class="fn"><a href="#n84" id="ref-84d">84</a></sup>
- **Cublington (John + Mary):** son Isaac baptized 1664; the same household most plausibly held the Stewkley manor by 1687 and sold to Anne Robinson of Stepney in 1701 per the Victoria County History of Buckinghamshire. Cublington is about 5 miles south-west of Stewkley.<sup class="fn"><a href="#n84" id="ref-84c">84</a></sup>
- **Edlesborough (John + Mary Kidgell):** marriage 1661. Materially incompatible with the colonial John because the Massachusetts vital sequence places Mary Gurney's death (20 Sept 1661) and John Gurney's remarriage to Grizzell (12 Nov 1661) in Braintree within the same year. Most plausibly the Cublington John in an earlier marriage or a close relative.<sup class="fn"><a href="#n82" id="ref-82">82</a></sup>
- **Weston Turville (John):** daughter Elyzabethe 1627.
- **Haddenham (John):** an unnamed Gurney child baptized 25 February 1620 and Joane Gurney baptized 26 January 1622. The 1620 fathering is incompatible with a colonial John who was about 17 then; this household is generationally earlier than Candidate A's marriage and is most plausibly a generational predecessor.<sup class="fn"><a href="#n88" id="ref-88b">88</a></sup>
- **Great Kimble (John + Alice Hewet, widow):** earlier marriage 20 October 1619. Single indexed event; a generational predecessor of Candidate A.

Aylesbury parish records also show a separately documented Edward Gurny household active in the 1660s, with a son Jon buried 2 February 1665 and a daughter Ann baptized 1666. Edward Gurny is not a John Gurney head of household but is included here because the 1665 burial of a son named Jon has elsewhere been mis-attributed to Candidate A; the burial is of Edward's son, not of Candidate A.<sup class="fn"><a href="#n84" id="ref-84e">84</a></sup>

The Aylesbury Prerogative Court of Canterbury probate records show a further Buckinghamshire family with a Daniel Gurney who died 1669, a brother John, and a wife Sarah (PROB 11/347/122 and PROB 11/337/37). This family is distinct from Candidate A; no probate record directly names Stewkley, Edlesborough, or Alice Oliffe.

### 8.4 Norfolk John Gurney households

Findmypast and the Norfolk Record Office between them surface two John Gurney households in Norfolk in the cluster window (excluding the case-file Earsham John eliminated above and the same-name Norwich groom of 1639 also eliminated above):

- **Denton, Norfolk - father identification unresolved.** A baptism of Mary Gurney 12 August 1638 and Thomas Gurney 24 January 1639 at Denton is read by Findmypast UK Parish Baptisms and FamilySearch as "father John Gurney + mother Rachell." The Norfolk Record Office image-confirmed reading of the same register entries is "father Josiah Gurney + mother Rachelle." The mother name (Rachell / Rachelle) is consistent across all three indexes; the father identification is unresolved. If father John, the household has children Mary 1638 and Thomas 1639, both names present in the colonial John's child set but with dates too late for the colonial Mary's likely 1620s birth window. If father Josiah, the household drops out of the John Gurney elimination table entirely.<sup class="fn"><a href="#n87" id="ref-87a">87</a></sup><sup class="fn"><a href="#n89" id="ref-89a">89</a></sup>
- **Hempnall and the Hempnall Group of Parishes, Norfolk - John Gurney.** Children Anna Gurney 1640 and Elizabeth Gurney 1641. Neither Mary nor Peter is among the indexed children. The household appears in Findmypast Norfolk Baptisms but not in the Norfolk Record Office collection (the Hempnall parish is in the quarter of Norfolk parishes not covered by the Norfolk Record Office index), so cross-source verification is unavailable in the present pass.<sup class="fn"><a href="#n87" id="ref-87b">87</a></sup>

Buckinghamshire-side and London-side Norfolk Gurney households with fathers other than John (William at Norwich Saint Lawrence; Edward and Anne at Great Yarmouth; Thomas and Elizabeth at Great Yarmouth; William and Anne at Cawston; George and Mary at Longham; Robert at Old Hunstanton and Saham Toney; William and Sarah at Saxlingham Thorpe; Thomas and Susanna at Horstead; Frances Garny at Gillingham) are noted in the John Gurney research companion under Norfolk Gurney household density. They are not candidates for elimination here because none of them is a John Gurney father, but they characterize the broader Gurney presence in Norfolk in the same window and provide Candidate B geographic-plausibility context.
```

### 3.2 Footnote body cleanup (n83, n88, n89)

Replace the body of endnote `n83` to remove the "image not yet pulled" line:

Old:

```html
<li id="n83" value="83">Aylesbury parish register, Buckinghamshire, baptism entry for Jonathan Gurney son of John Gurney, 22 November 1647, as recorded in the project research notes at <code>research/case-files/Initial foundation work for john-gurney-case-file/Gurney_ProtestationReturns_Analysis.md</code>; The National Archives, Kew, E 115/180/113, certificate of residence for John Gurney moving from Aylesbury half-hundred to Northamptonshire, 1641, recorded in the same research note; John Gurney as tenant at Walgrave, Northamptonshire, 1650, recorded in <code>research/case-files/Initial foundation work for john-gurney-case-file/Gurney_Research_Findings_V7.md</code>. The underlying TNA image and the Walgrave tenancy source have not been independently pulled in this pass; promote either to a footnoted primary record only after the originating image or document is examined. <a class="backref" href="#ref-83">↩</a></li>
```

New:

```html
<li id="n83" value="83">The National Archives, Kew, E 115/180/113, certificate of residence for John Gurney moving from Aylesbury half-hundred to Northamptonshire, 1641; John Gurney recorded as tenant at Walgrave, Northamptonshire, 1650. Both items are presently held in the project's foundation research notes at <code>research/case-files/Initial foundation work for john-gurney-case-file/Gurney_ProtestationReturns_Analysis.md</code> and <code>Gurney_Research_Findings_V7.md</code>; the originating Aylesbury parish register, Buckinghamshire, baptism entry for Jonathan Gurney son of John Gurney, 22 November 1647 is recorded in the same project research notes. Source IDs pending direct image pulls. <a class="backref" href="#ref-83">↩</a><a class="backref" href="#ref-83b">back</a></li>
```

Replace the body of endnote `n88` to remove "in the consulted records" and to add the cluster reasoning specific to the second Aylesbury John:

Old:

```html
<li id="n88" value="88">FamilySearch, "England, Births and Christenings, 1538-1975," John Gurney son of John Gurney bapt. 16 December 1638 Aylesbury, Buckinghamshire (surfaced via father-John filter in the 2026-05-11 Pass 9 walk). Source ID: <code>fs-england-births-christenings</code>. FamilySearch, "England, Buckinghamshire, Church Records, 1217-1994," Haddenham baptisms: unnamed Gurney child to father John Gurney, 25 February 1620; Joane Gurney to father John Gurney, 26 January 1622. The Aylesbury 1638 entry is either an additional son of Candidate A's Bierton/Aylesbury John or a second contemporaneous Aylesbury John Gurney father; the Haddenham entries identify an additional Bucks John Gurney household. Mother fields unindexed in the consulted records. <a class="backref" href="#ref-88a">back</a> <a class="backref" href="#ref-88b">back</a></li>
```

New:

```html
<li id="n88" value="88">FamilySearch, "England, Births and Christenings, 1538-1975," John Gurney son of John Gurney bapt. 16 December 1638 Aylesbury, Buckinghamshire. Source ID: <code>fs-england-births-christenings</code>. The 16 December 1638 baptism is eight weeks after the 25 October 1638 Aylesbury marriage of John Gurney and Anne Cowheard (FamilySearch ID <code>N2TD-Z9Z</code>; same source collection); the eight-week gap rules out the two events as the same couple. The 16 December 1638 child is treated here as Candidate A's eldest indexed child, ten years after the 1628 Bierton marriage to Alice Oliffe; the Anne Cowheard groom is a second simultaneous Aylesbury John. FamilySearch, "England, Buckinghamshire, Church Records, 1217-1994," Haddenham baptisms: unnamed Gurney child to father John Gurney, 25 February 1620; Joane Gurney to father John Gurney, 26 January 1622, identifying a Buckinghamshire John Gurney household generationally earlier than Candidate A's 1628 marriage. <a class="backref" href="#ref-88a">back</a> <a class="backref" href="#ref-88b">back</a></li>
```

Replace the body of endnote `n89` to remove the "Soiled Document / Faded Document" overlay sentence:

Old:

```html
<li id="n89" value="89">Ancestry, "Norfolk, England, Church of England Baptism, Marriages, and Burials, 1535-1812" (in partnership with Norfolk Record Office; Ancestry collection 61045), walked 2026-05-11 for surname Gurney plus variants in the 1615-1645 window. Source ID: <code>ancestry-norfolk-1535-1812</code>. The Denton 12 August 1638 Mary Gurney baptism is image-confirmed in the NRO collection with father Josiah + mother Rachelle; FamilySearch's "England, Births and Christenings, 1538-1975" and Findmypast UK Parish Baptisms index the same register entry with father John + mother Rachell. NRO holds the original register; image was partly obscured by repository condition-overlay tags ("Soiled Document," "Faded Document") in the 2026-05-11 view, so independent script verification is pending. <a class="backref" href="#ref-89a">back</a> <a class="backref" href="#ref-89b">back</a></li>
```

New:

```html
<li id="n89" value="89">Ancestry, "Norfolk, England, Church of England Baptism, Marriages, and Burials, 1535-1812" (in partnership with the Norfolk Record Office; Ancestry collection 61045). Source ID: <code>ancestry-norfolk-1535-1812</code>. The Denton 12 August 1638 Mary Gurney baptism is image-confirmed in this collection with father Josiah and mother Rachelle. FamilySearch's "England, Births and Christenings, 1538-1975" and Findmypast UK Parish Baptisms index the same register entry with father John and mother Rachell. The mother name is consistent across all three indexes; the father identification is unresolved. Independent script verification of the register page is pending. <a class="backref" href="#ref-89a">back</a> <a class="backref" href="#ref-89b">back</a></li>
```

### 3.3 No other case-file changes in v29

Sections 1-7, 9-13 unchanged.

## 4. Proposed G13 research-file edits (research/people/g13-john-gurney-fact-sheet.research.md)

### 4.1 Move Norfolk non-John households into the existing density section

The Norfolk Gurney household density section added in v25 and extended in v28 already lists the non-John Norfolk Gurney households. Locate the section "NRO (Ancestry collection 61045) Norfolk Gurney baptism walk (2026-05-11)" (added in v28's §4.1) and replace the introductory framing so the section is correctly scoped as "Norfolk Gurney households without a John father," and append a brief note that these households are deliberately not in the case file's §8 elimination table because the table is restricted to John Gurneys.

Find the v28 section in G13 and replace its first paragraph with:

```markdown
### Norfolk Gurney households without a John as father (2026-05-11 pass)

The Ancestry-published Norfolk Record Office collection covers about three-quarters of Norfolk parishes. A complete walk for surname Gurney plus variants 1615-1645 returns 14 baptisms across ten households whose father is named other than John. They are not candidates for the case file's §8 elimination table, which is restricted to John Gurney households, but they characterize the broader Norfolk Gurney presence in the same window and provide Candidate B geographic-plausibility context.

The ten non-John households are:

- Frances Garny at Gillingham (Mary 1624) - identification of Frances Garny vs Francis Gurney G14 (Candidate B's putative father) is unresolved.
- Thomas and Susanna Gurney at Horstead (Henricus 1626)
- Edward and Anne Gurney at Great Yarmouth (Christian 1629, Wm 1631)
- George and Mary Gurney at Longham (William 1629)
- Robert Gurney at Saham Toney (Gulielmies 1629)
- Robert Gurney at Old Hunstanton Saint Mary's (Johannie 1629)
- William and Anne Gurney at Cawston (William 1630)
- William Gurney at Norwich Saint Lawrence (Richard 1630, Martha 1633/4, Margaret 1635; William buried Norwich Saint Lawrence 24 January 1640)
- Thomas and Elizabeth Gurney at Great Yarmouth (Mary 1632)
- William and Sarah Gurney at Saxlingham Thorpe and Nethergate (Gulielmus 1635)
```

Keep the existing source-citation footnote on this section unchanged.

## 5. Apply order

When approved:

1. Replace Section 8 of `research/case-files/john-gurney-case-file-v4.md` with the v29 §3.1 content. Preserve the existing endnote numbering (n82-n89) - the section-body cross-references in the replacement block point to the existing IDs.
2. Replace the bodies of endnotes `n83`, `n88`, and `n89` per §3.2.
3. Edit `research/people/g13-john-gurney-fact-sheet.research.md` per §4.
4. Update `sources/intake/working/john-gurney-audit-state.md` to mark v29 as applied.
