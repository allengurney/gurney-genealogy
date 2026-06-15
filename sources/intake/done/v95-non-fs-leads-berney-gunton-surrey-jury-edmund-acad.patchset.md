**Done:** 2026-06-14 07:18 PT

# Patchset v95 â€” Non-FamilySearch lead findings (Berney/Gunton, Surrey jury, Edmund ACAD)

**Phase 1 prepared 2026-06-13.** Promotes four web-research findings from the 2026-06-13
non-FamilySearch lead sweep (highest-priority open, non-FS leads explored directly after a
batch of subagents was cut off by a session-usage limit):

- **L-78 / L-79 (G22 network):** the History of Parliament biography of Sir Robert Berney was
  captured. It corroborates John Gurney V as Berney's fellow Norfolk shire knight of 1399 and
  co-trustee of Erpingham's lands, and it **resolves the long-standing "Gurney of Gunton"
  puzzle**: the "Sir Robert of Gunton, deputy to Erpingham at Dover in 1400" is **Sir Robert
  Berney of Gunton**, not a Gurney.
- **L-27 (G17 Anthony):** the *Letters and Papers, Henry VIII* indictment of the Earl of
  Surrey (vol. 21 pt 2, no. 697) was consulted; it lists Anthony Gurney first among the
  sixteen-man Norfolk grand jury, corroborating Daniel Gurney's foreman claim from the
  primary calendar.
- **L-15 (Edmund Gurney the Divine):** the *Alumni Cantabrigienses* (ACAD/Venn) entry was
  retrieved; it confirms the Cambridge chronology, adjudicates the DNB-vs-Harpley date
  splits, and independently confirms the ordination dates that previously rested only on the
  tertiary Grokipedia capture.
- **L-25 (G15 Henry):** a lead-attribution correction â€” the *Church Heraldry of Norfolk* is
  Rev. Edmund Farrer's (1887), not Walter Rye's, and Bodleian MS Tanner 175 is already
  identified on the G15 companion as Henry's commonplace book; the residual heraldic pull is
  refined.

Two further leads (**L-35**, **L-28**) turned out already resolved in the people-companions â€”
the CSV "Open" status simply lagged â€” so they carry CSV-status reconciliation only, no new
content. No `corpus_supplement` files are written: every extract here is short (<150 words)
and lands verbatim inline in its research companion, per `sources/README.md`'s
short-quotation rule.

All edits are scripted below for mechanical Phase-2 application. No `research/`, `data/`, or
CSV file is modified during Phase 1.

---

## Item 1 â€” L-78 / L-79: Berney biography captured; the Gunton attribution resolved

**Outcome: promote.** Destination: `research/people/g22-robert-gournay-fact-sheet.research.md`
(existing Berney-network section), plus the existing `hop-berney` `sources.json` entry.
Existing sourceIds `hop-berney` and `trevor-john-erpingham-1970` are reused; no new sourceId.

### Action 1a â€” `str_replace` in `research/people/g22-robert-gournay-fact-sheet.research.md` (section heading)

**old_string:**
```
### Berney-side network corroboration, and the Gunton caution (added 2026-05-30)
```

**new_string:**
```
### Berney-side network corroboration; the Gunton attribution resolved (updated 2026-06-13)
```

### Action 1b â€” `str_replace` in `research/people/g22-robert-gournay-fact-sheet.research.md` (body: flip the caution to the resolution)

**old_string:**
```
Pending that check, the "Gurney of Gunton" reading is treated as a probable Berney/Gurney error and is **not** used as a Robert G22 lead.
```

**new_string:**
```
The Berney biography now settles this: the figure is **Sir Robert Berney of Gunton**, whose seat, office (deputy to Erpingham at Dover castle and warden of the Cinque Ports), and date (returned to Parliament 1402 while in that office, which he held c. May 1400 to after March 1406) match the contested phrase exactly. The "Gurney of Gunton" reading is a Berney/Gurney surname confusion and stays excluded as a Robert G22 lead.
```

### Action 1c â€” `str_replace` in `research/people/g22-robert-gournay-fact-sheet.research.md` (footnote `hop-berney`)

**old_string:**
```
[^v75-hop-berney]: "BERNEY, Sir Robert (c.1365-1415), of Reedham and Gunton, Norf.," *The House of Commons 1386-1421* (1993), History of Parliament Online, [historyofparliamentonline.org](https://www.historyofparliamentonline.org/volume/1386-1421/member/berney-sir-robert-1365-1415). Berney-side corroboration, independent of `hop-gurney`, of John Gurney V as fellow shire knight 1399 and Erpingham co-trustee within the Saxthorpe/Loundhall feoffee circle. Full page text not yet captured (lead L-78). Source ID: `hop-berney`.
```

**new_string:**
```
[^v75-hop-berney]: "BERNEY, Sir Robert (bef.1365-1415), of Great Witchingham and Gunton, Norf.," *The House of Commons 1386-1421* (1993), History of Parliament Online, [historyofparliamentonline.org](https://www.historyofparliamentonline.org/volume/1386-1421/member/berney-sir-robert-1365-1415). Berney-side corroboration, independent of `hop-gurney`, of John Gurney V's place in the Lancastrian Norfolk affinity. Page text captured 2026-06-13: the biography states John Gurney "was Berney's fellow shire knight of 1399 and his co-trustee of Erpingham's lands," names Berney among the July 1396 feoffees of the extensive FitzAlan (Arundel) estates and among those Erpingham asked to administer his lands at his October 1398 exile, and records Berney as deputy to Erpingham at Dover castle and warden of the Cinque Ports c. May 1400 to after March 1406 (returned to Parliament 1402 in that office) â€” which identifies the "Sir Robert ... of Gunton, deputy at Dover 1400" as Berney, not a Gurney. The HoP title gives Berney's seats as Great Witchingham and Gunton; his elder brother Sir Thomas held the Reedham branch. Source ID: `hop-berney`.
```

### Action 1d â€” `str_replace` in `research/people/g22-robert-gournay-fact-sheet.research.md` (footnote `trevor-john`)

**old_string:**
```
[^v75-trevor-john]: Trevor John, "Sir Thomas Erpingham, East Anglian Society and the Dynastic Revolution of 1399," *Norfolk Archaeology* 35, no. 1 (1970): 96-108, DOI 10.5284/1078024. The scholarly account of the Erpingham/Berney/Shelton/Gurney bloc and the origin of the "Gunton/Dover 1400" reading; not yet pulled (lead L-79). Source ID: `trevor-john-erpingham-1970`.
```

**new_string:**
```
[^v75-trevor-john]: Trevor John, "Sir Thomas Erpingham, East Anglian Society and the Dynastic Revolution of 1399," *Norfolk Archaeology* 35, no. 1 (1970): 96-108, DOI 10.5284/1078024. The scholarly root of the Erpingham/Berney/Wynter/Shelton/Gurney bloc; the Archaeology Data Service copy is access-gated (an automated fetch returned HTTP 403) and was not retrieved, but it is no longer needed to settle the Gunton attribution, which the Berney biography decides on its own. Source ID: `trevor-john-erpingham-1970`.
```

### Action 1e â€” `str_replace` in `data/sources.json` (`hop-berney` citation: correct the seats)

**old_string:**
```
      "citation": "\"BERNEY, Sir Robert (c.1365-1415), of Reedham and Gunton, Norf.,\" in J. S. Roskell, L. Clark and C. Rawcliffe (eds.), The History of Parliament: The House of Commons 1386-1421 (1993), History of Parliament Online.",
```

**new_string:**
```
      "citation": "\"BERNEY, Sir Robert (bef.1365-1415), of Great Witchingham and Gunton, Norf.,\" in J. S. Roskell, L. Clark and C. Rawcliffe (eds.), The History of Parliament: The House of Commons 1386-1421 (1993), History of Parliament Online.",
```

### Action 1f â€” `str_replace` in `data/sources.json` (`hop-berney` notes: mark captured)

**old_string:**
```
 Also bears on whether the 'Sir Robert Gurney of Gunton, deputy at Dover 1400' phrasing is in fact Sir Robert Berney of Gunton. Full page text not yet captured (leads L-78, L-79)."
```

**new_string:**
```
 Page text captured 2026-06-13: confirms John Gurney V as Berney's fellow shire knight of 1399 and co-trustee of Erpingham's lands, and identifies the 'Sir Robert of Gunton, deputy at Dover 1400' as Berney (deputy to Erpingham at Dover c. May 1400 to March 1406), not a Gurney."
```

### Action 1g â€” `str_replace` in `research/future-research/research-leads.csv` (L-78 status)

**old_string:**
```
from a non-Gurney biography.",Y,Open,research/people/g22-robert-gournay-fact-sheet.research.md
```

**new_string:**
```
from a non-Gurney biography.",Y,"Done 2026-06-13 â€” HoP Berney bio captured on the G22 companion: John Gurney V 'Berney's fellow shire knight of 1399 and his co-trustee of Erpingham's lands'; Berney also a July 1396 FitzAlan (Arundel) feoffee and a 1398 administrator of Erpingham's lands. sourceId hop-berney updated (citation corrected to 'Great Witchingham and Gunton')",research/people/g22-robert-gournay-fact-sheet.research.md
```

### Action 1h â€” `str_replace` in `research/future-research/research-leads.csv` (L-79 status)

**old_string:**
```
Archaeology Data Service.",Y,Open,research/people/g22-robert-gournay-fact-sheet.research.md
```

**new_string:**
```
Archaeology Data Service.",Y,"Resolved 2026-06-13 â€” the Gunton attribution is settled from the HoP Berney bio (Sir Robert Berney of Gunton was deputy to Erpingham at Dover c. May 1400 to March 1406): the 'Sir Robert of Gunton, deputy at Dover 1400' phrase = Berney, not Gurney. The Trevor John article itself is ADS-gated (automated fetch HTTP 403), not retrieved, and no longer needed for this point",research/people/g22-robert-gournay-fact-sheet.research.md
```

---

## Item 2 â€” L-27: Anthony Gurney on the Surrey grand jury (*L&P* no. 697)

**Outcome: promote.** Destination: `research/people/g17-anthony-gurney-fact-sheet.research.md`.
New sourceId `letters-papers-henry-viii` (+ default-on validation worksheet).

### Action 2a â€” `str_replace` in `research/people/g17-anthony-gurney-fact-sheet.research.md` (new Working Notes entry at top)

**old_string:**
```
---

## Working Notes

### 2026-06-11
```

**new_string:**
```
---

## Working Notes

### 2026-06-13 â€” Anthony on the Surrey grand jury: the *Letters and Papers* indictment text

The contemporary calendar confirms the family tradition that Anthony was foreman of the Norfolk grand jury that indicted Henry Howard, Earl of Surrey, for treason. *Letters and Papers, Foreign and Domestic, Henry VIII*, vol. 21 part 2, no. 697 (the indictment and trial record, 13 January 1547) lists the sixteen-man Norfolk jury empanelled at Norwich Castle on 7 January 1547 to find the true bill, opening: **"Anthony Gurney, William Brampton, John Berney, George Horsman, Ralph Shelton, Edmund Wode, Robert Rugge, William Rogers, Thomas Codde, Robert Lovedaie, Richard Sponer, William Drake, Thomas Aldriche, John Thetford, Thomas Hare and Henry Dengeyn."** Anthony Gurney heads the list â€” the first-named position that by convention identifies the foreman â€” corroborating Daniel Gurney's *Supplement* claim from the primary calendar; the calendar abstract itself lists the panel without printing the word "foreman," so the foremanship rests on that first-named convention rather than an explicit designation. The jury places Anthony in the front rank of mid-Tudor Norfolk gentry, returning a treason bill against the Duke of Norfolk's heir two weeks before Henry VIII's own death.[^anthony-lp-surrey-jury]

[^anthony-lp-surrey-jury]: *Letters and Papers, Foreign and Domestic, of the Reign of Henry VIII*, vol. 21 part 2 (London: HMSO, 1910), no. 697 (indictment and trial of Henry Howard, Earl of Surrey, 13 Jan. 1547; Norfolk jury panel, m. 14), British History Online, [www.british-history.ac.uk/letters-papers-hen8/vol21/no2/pp362-378](https://www.british-history.ac.uk/letters-papers-hen8/vol21/no2/pp362-378). The jury opens "Anthony Gurney, William Brampton, John Berney â€¦"; Anthony first-named (foreman by convention). Source ID: `letters-papers-henry-viii`.

### 2026-06-11
```

### Action 2b â€” `str_replace` in `research/people/g17-anthony-gurney-fact-sheet.research.md` (Research Appendix: jury-foreman paragraph close)

**old_string:**
```
This needs further investigation in the State Papers of Henry VIII (Letters and Papers, Foreign and Domestic, vol. 21 part 2,
```

**new_string:**
```
The *Letters and Papers* indictment text has now been consulted (vol. 21 part 2, no. 697); it lists Anthony first among the sixteen Norfolk jurors â€” see the Working Notes entry above. The fuller setting remains in the State Papers (Letters and Papers, Foreign and Domestic, vol. 21 part 2,
```

### Action 2c â€” `str_replace` in `research/people/g17-anthony-gurney-fact-sheet.research.md` (Negative Results)

**old_string:**
```
- The Letters and Papers of Henry VIII have not been directly consulted for the January 1547 grand jury foreman role.
```

**new_string:**
```
- ~~The Letters and Papers of Henry VIII have not been directly consulted for the January 1547 grand jury foreman role.~~ **Consulted 2026-06-13** â€” vol. 21 pt 2, no. 697 lists Anthony Gurney first among the sixteen-man Norfolk grand jury; see Working Notes.
```

### Action 2d â€” `str_replace` in `research/people/g17-anthony-gurney-fact-sheet.research.md` (Open Questions #1)

**old_string:**
```
direct consultation for the 7 January 1546/7 grand jury composition.
```

**new_string:**
```
RESOLVED 2026-06-13 â€” no. 697 lists the sixteen-man Norfolk jury (Anthony Gurney first); see Working Notes. Remaining: modern Surrey biographies (Sessions 1999; Brigden 2012) for any narrative on the jury's selection.
```

### Action 2e â€” `str_replace` in `data/sources.json` (new sourceId `letters-papers-henry-viii`)

Insert immediately before the `hop-berney` entry.

**old_string:**
```
    "hop-berney": {
```

**new_string:**
```
    "letters-papers-henry-viii": {
      "shortTitle": "Letters and Papers, Foreign and Domestic, Henry VIII",
      "citation": "Letters and Papers, Foreign and Domestic, of the Reign of Henry VIII, ed. J. S. Brewer, James Gairdner and R. H. Brodie, 21 vols. and addenda (London: HMSO, 1862-1932). Calendar of state papers; cite by volume, part, and entry number.",
      "archive": "British History Online (full calendar text); The National Archives (originals)",
      "url": "https://www.british-history.ac.uk/letters-papers-hen8",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/letters-papers-henry-viii.md",
      "notes": "Calendar/abstract of the Henry VIII state papers (distinguish the abstract from the original instrument). Cited so far for vol. 21 pt 2 no. 697 (the indictment and trial of Henry Howard, Earl of Surrey, 13 Jan. 1547), whose sixteen-man Norfolk grand-jury panel opens with Anthony Gurney (G17) â€” corroborating Daniel Gurney's foreman claim. Read via British History Online 2026-06-13."
    },
    "hop-berney": {
```

### Action 2f â€” `new file write` â†’ `sources/validations/letters-papers-henry-viii.md`

```markdown
# Validation â€” Letters and Papers, Foreign and Domestic, Henry VIII

**Source:** `letters-papers-henry-viii` (`data/sources.json`). Calendar/abstract of the
Henry VIII state papers (21 vols. + addenda), full text on British History Online.

**Examined:** vol. 21 part 2, no. 697 (indictment and trial of Henry Howard, Earl of Surrey,
13 Jan. 1547), via British History Online
(`letters-papers-hen8/vol21/no2/pp362-378`), 2026-06-13. The entry's Norfolk grand-jury
panel (m. 14) was read in full.

**Nature of the source:** a calendar abstract, not the original indictment roll; the panel of
jurors is listed without an explicit "foreman" designation.

**Remains / uncertain:** the original King's Bench indictment (TNA) not consulted; the rest
of vol. 21 pt 2 not swept for other Gurney mentions.

**Findings recorded in:** `research/people/g17-anthony-gurney-fact-sheet.research.md`
(Anthony first-named on the sixteen-man Norfolk grand jury). Execution trail: patchset
`sources/intake/done/v95-non-fs-leads-berney-gunton-surrey-jury-edmund-acad.patchset.md`.
```

### Action 2g â€” `str_replace` in `research/future-research/research-leads.csv` (L-27 status)

**old_string:**
```
,Y,Open,research/people/g17-anthony-gurney-fact-sheet.research.md
```

**new_string:**
```
,Y,"Done 2026-06-13 â€” L&P Hen VIII vol. 21 pt 2 no. 697 consulted (G17 companion): the Norfolk grand jury that found the true bill against Surrey (Norwich Castle, 7 Jan 1547) opens 'Anthony Gurney, William Brampton, John Berney...', Anthony first-named (foreman by convention), corroborating Daniel Gurney's Supplement; sourceId letters-papers-henry-viii",research/people/g17-anthony-gurney-fact-sheet.research.md
```

---

## Item 3 â€” L-15: ACAD/Venn confirms Edmund the Divine's chronology and ordination

**Outcome: promote.** Destination: `research/people/edmund-gurney-divine.research.md`.
New sourceId `alumni-cantabrigienses-venn` (+ default-on validation worksheet).

### Action 3a â€” `str_replace` in `research/people/edmund-gurney-divine.research.md` (new dated section before Identity boundary)

**old_string:**
```
## Identity boundary
```

**new_string:**
```
## 2026-06-13 â€” Venn/ACAD confirms the academic and ordination chronology

The *Alumni Cantabrigienses* (ACAD/Venn) record for Edmund Gurney adjudicates the small date discrepancies between DNB and the Harpley rectors' register and independently confirms the ordination dates that previously rested only on the tertiary Grokipedia capture. The entry: admitted pensioner at Queens' College **30 October 1594** (matriculated 1595), **son of Henry Gurney of West Barsham, Norfolk** (= G15); **B.A. 1598/9**; fellow of Corpus Christi **1601-14**; **M.A. (Corpus Christi) 1602**; **B.D. 1609**; **ordained deacon (Ely) 18 December 1608** and **priest (Norwich) 1614**; rector of **Edgefield 1614-20** and **Harpley 1620-48**; buried St Peter Mancroft, Norwich, **14 May 1648**; "author of anti-Romanist treatises" and "one of Fuller's Worthies."[^acad-edmund]

Two reconciliations follow. The B.A. reads **1598/9** (with the Harpley register), not DNB's "1600"; and the matriculation splits cleanly into admission (30 Oct 1594, DNB) and formal matriculation (1595, Harpley register), so the two registers were recording different steps rather than conflicting. The **deacon-1608 / priest-1614** dates â€” earlier carried only from Grokipedia and explicitly quarantined â€” are now confirmed from a compiled scholarly authority. The parentage line ("son of Henry Gurney of West Barsham") re-confirms Edmund's place as Henry G15's son and Francis G14's brother, independently of DNB and Daniel Gurney.

[^acad-edmund]: *Alumni Cantabrigienses*, comp. John Venn and J. A. Venn, Part I (to 1751), s.v. "Gurney, Edmund"; consulted via the online ACAD database (A Cambridge Alumni Database), [venn.lib.cam.ac.uk](https://venn.lib.cam.ac.uk/), 2026-06-13. Fields: matric. pens. Queens' (adm. 1594:10:30, matric. 1595), son of Henry Gurney of West Barsham; B.A. 1598/9; M.A. Corpus Christi 1602; Fellow Corpus Christi 1601-14; B.D. 1609; ord. deacon (Ely) 1608:12:18, priest (Norwich) 1614; R. Edgefield 1614-20, R. Harpley 1620-48; bur. St Peter Mancroft, Norwich, 1648:05:14. Source ID: `alumni-cantabrigienses-venn`.

## Identity boundary
```

### Action 3b â€” `str_replace` in `research/people/edmund-gurney-divine.research.md` (Open question #1)

**old_string:**
```
1. **Cambridge Alumni / Venn check.** Confirm DNB's dates and Harpley's alternate dates through <em>Alumni Cantabrigienses</em> or Cambridge records.
```

**new_string:**
```
1. ~~**Cambridge Alumni / Venn check.**~~ **Resolved 2026-06-13** â€” the ACAD/Venn entry confirms the chronology and adjudicates the DNB/Harpley date splits (B.A. 1598/9; adm. 1594 / matric. 1595); see the Venn/ACAD section above.
```

### Action 3c â€” `str_replace` in `research/people/edmund-gurney-divine.research.md` (Open question #2)

**old_string:**
```
2. **CCEd / diocesan ordination records.** Verify deaconing date, priesting date, and any 1608/1614 discrepancy.
```

**new_string:**
```
2. **CCEd / diocesan ordination records.** ACAD now supplies the ordination dates (deacon Ely 18 Dec 1608; priest Norwich 1614), confirming the formerly Grokipedia-only dates. A direct CCEd or Ely/Norwich diocesan-register pull would add the patron and document references but is confirmatory.
```

### Action 3d â€” `str_replace` in `data/sources.json` (new sourceId `alumni-cantabrigienses-venn`)

Insert immediately before the `letters-papers-henry-viii` entry created in Action 2e.

**old_string:**
```
    "letters-papers-henry-viii": {
```

**new_string:**
```
    "alumni-cantabrigienses-venn": {
      "shortTitle": "Alumni Cantabrigienses (Venn) â€” ACAD database",
      "citation": "John Venn and J. A. Venn (comps.), Alumni Cantabrigienses: A Biographical List of All Known Students, Graduates and Holders of Office at the University of Cambridge, from the Earliest Times to 1900 (Cambridge: Cambridge University Press, 1922-1954); consulted via the online ACAD database (A Cambridge Alumni Database).",
      "archive": "University of Cambridge (ACAD online); Cambridge University Press (print)",
      "url": "https://venn.lib.cam.ac.uk/",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/alumni-cantabrigienses-venn.md",
      "notes": "Compiled Cambridge alumni authority. Cited for the entry on Edmund Gurney the Divine (son of Henry Gurney G15): Queens' adm. 1594 / matric. 1595, BA 1598/9, MA Corpus Christi 1602, BD 1609, ord. deacon Ely 18 Dec 1608, priest Norwich 1614, R. Edgefield 1614-20, R. Harpley 1620-48, bur. St Peter Mancroft 14 May 1648. A compiled register, not a primary record; it adjudicates the DNB/Harpley date splits and confirms the ordination dates."
    },
    "letters-papers-henry-viii": {
```

### Action 3e â€” `new file write` â†’ `sources/validations/alumni-cantabrigienses-venn.md`

```markdown
# Validation â€” Alumni Cantabrigienses (Venn) / ACAD

**Source:** `alumni-cantabrigienses-venn` (`data/sources.json`). Compiled Cambridge alumni
register (Venn & Venn), consulted via the online ACAD database (venn.lib.cam.ac.uk).

**Examined:** the entry for Edmund Gurney the Divine, 2026-06-13. Full fielded record read
(college, parentage, matriculation, degrees, orders, livings, burial).

**Nature of the source:** a compiled biographical authority, not a primary register; useful
to adjudicate DNB-vs-local-register date conflicts and to confirm ordination dates.

**Remains / uncertain:** the underlying Ely/Norwich diocesan ordination registers and the
Edgefield/Harpley institution records (patrons, document references) not pulled directly; CCEd
not separately consulted.

**Findings recorded in:** `research/people/edmund-gurney-divine.research.md` (Venn/ACAD
section). Execution trail: patchset
`sources/intake/done/v95-non-fs-leads-berney-gunton-surrey-jury-edmund-acad.patchset.md`.
```

### Action 3f â€” `str_replace` in `research/future-research/research-leads.csv` (L-15 status)

**old_string:**
```
,Y,Open,research/people/edmund-gurney-divine.research.md
```

**new_string:**
```
,Y,"Done 2026-06-13 â€” ACAD/Venn entry retrieved (edmund-divine companion): adm. Queens' 30 Oct 1594 / matric. 1595, son of Henry Gurney of West Barsham, BA 1598/9, MA 1602, BD 1609, ord. deacon Ely 18 Dec 1608 and priest Norwich 1614, R. Edgefield 1614-20, R. Harpley 1620-48, bur. St Peter Mancroft 14 May 1648; confirms ordination dates previously only in Grokipedia; sourceId alumni-cantabrigienses-venn",research/people/edmund-gurney-divine.research.md
```

---

## Item 4 â€” L-25: *Church Heraldry of Norfolk* attribution correction (Farrer, not Rye)

**Outcome: promote (lead refinement + attribution correction).** Destination:
`research/people/g15-henry-gurney-fact-sheet.research.md` (Open Questions). No new sourceId â€”
the Farrer volume was not yet quoted, only correctly identified; Bodleian MS Tanner 175 is
already documented on the G15 companion (sourceId `bodleian-ms-tanner-175-marco`).

### Action 4a â€” `str_replace` in `research/people/g15-henry-gurney-fact-sheet.research.md` (Open Questions #4)

**old_string:**
```
Walter Rye's <em>Church Heraldry of Norfolk</em> (1887) on the Internet Archive should be checked.
```

**new_string:**
```
Rev. Edmund Farrer's <em>The Church Heraldry of Norfolk</em> (1887; the research-leads CSV's "Walter Rye" attribution is an error) on the Internet Archive should be checked for recorded Gurney shields â€” note its first volume covers only the Earsham and Diss hundreds, so the West Barsham (Gallow/Brothercross), Great Ellingham (Shropham), and Harpley (Freebridge-Lynn) entries sit in the later hundred-volumes.
```

### Action 4b â€” `str_replace` in `research/future-research/research-leads.csv` (L-25 status)

**old_string:**
```
,Unk,Open,research/people/g15-henry-gurney-fact-sheet.research.md
```

**new_string:**
```
,Unk,"Refined 2026-06-13 â€” author correction: the work is Rev. Edmund Farrer, The Church Heraldry of Norfolk (1887), not Walter Rye; on archive.org (vol. I covers Earsham/Diss hundreds only, so the Gurney parishes sit in later hundred-volumes). Tanner MS 175 already identified on the G15 companion as Henry Gurnay's commonplace book (the 'fo.175' wording is a garbled whole-volume reference). Open: the Farrer hundred-volume covering West Barsham / Great Ellingham / Harpley shields",research/people/g15-henry-gurney-fact-sheet.research.md
```

---

## Item 5 â€” L-35 and L-28: CSV-status reconciliation (already resolved in the companions)

**Outcome: reject (no new content).** Both leads were already worked in the people-companions;
only the CSV "Open" status lagged. No research/source edits â€” CSV status correction only.

### Action 5a â€” `str_replace` in `research/future-research/research-leads.csv` (L-35 status: already done in v56)

**old_string:**
```
Cressingham identity uncertain.",Y,Open,research/people/g22-robert-gournay-fact-sheet.research.md
```

**new_string:**
```
Cressingham identity uncertain.",Y,"Done (v56) â€” Rye Short Calendar of Feet of Fines Pt II no. 64 read on the G22 companion: 'Robert Gurnay of Parva Cressingham' v. Edward Howard, no parentage recital; residence ~25 mi S of West Barsham argues AGAINST the G22 identification (the Hopton/Cressingham foldcourse re-enters the line only later, via Anthony's 1527/8 Lovell marriage). CSV status was stale",research/people/g22-robert-gournay-fact-sheet.research.md
```

### Action 5b â€” `str_replace` in `research/future-research/research-leads.csv` (L-28 status: Saxthorpe done in v62)

**old_string:**
```
,Y,Open,research/people/g19-william-gurney-iv-fact-sheet.research.md
```

**new_string:**
```
,Y,"Partial â€” Saxthorpe 1472 episode already promoted (v62; G22 companion); open piece: identify the 'cousin Gurney' / William Gurney of Tharston (Duke of Norfolk retainer, former Norfolk escheator) versus William IV himself",research/people/g19-william-gurney-iv-fact-sheet.research.md
```

---

## Source tracking

- **Existing sourceIds reused:** `hop-berney` (Item 1; citation + notes corrected, Actions 1e/1f),
  `trevor-john-erpingham-1970` (Item 1; still unpulled â€” ADS-gated), `bodleian-ms-tanner-175-marco`
  (Item 4; already on the G15 companion).
- **New sourceId `letters-papers-henry-viii`** (Item 2, Action 2e) â†’ validation worksheet
  created (Action 2f), per default-on discipline.
- **New sourceId `alumni-cantabrigienses-venn`** (Item 3, Action 3d) â†’ validation worksheet
  created (Action 3e), per default-on discipline.
- **No `corpus_supplement` files:** every promoted extract â€” the *L&P* jury list, the ACAD
  fielded entry, the Berney-bio quotations â€” is short (<150 words) and lands verbatim inline
  in its research companion, per `sources/README.md`'s short-quotation rule. (Phase 2 may
  write a supplement directly only if a fuller verbatim transcript is later captured.)
- **No new leads registered:** the only open onward items (the Tharston "cousin Gurney"
  identity; the correct Farrer hundred-volume; a direct CCEd pull) are recorded inline in the
  relevant companions and the refined CSV statuses, not as new `L-` rows.

## Concurrency note

This patchset was numbered **v95** because a concurrent session created
`v94-late-medieval-gurney-gentry-marriages.patchset.md` and advanced the stub during this
session. v94 (Calthorpe 1494 / L'Estrange 1505 marriages) is unrelated and does not overlap
these edits. If both patchsets are applied, apply v94 and v95 independently; the CSV row
edits here target existing rows (L-15, L-25, L-27, L-28, L-35, L-78, L-79) and do not collide
with v94's new-lead appends (L-122/L-123).

## Phase 2 completion

After Items 1-5, prepend `**Done:** YYYY-MM-DD HH:MM PT` and move this file to
`sources/intake/done/`.
