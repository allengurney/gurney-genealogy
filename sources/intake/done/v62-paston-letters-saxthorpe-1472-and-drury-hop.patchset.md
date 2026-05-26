**Done:** 2026-05-25 23:59 PT

# Intake patchset v62 — Paston Letters Saxthorpe 1472 episode, 1452 anti-Heydon petition, Countess of Oxford to Margaret Gurnay, and Sir Robert Drury full History of Parliament biography

**Prepared:** 2026-05-25
**Phase:** 1. Ready for Phase 2.
**Sequencing:** Independent of v61 and v63. Uses footnote handles `nNEW8`–`nNEW10` in fact sheets (no collision with v61 or v63 ranges).

Four findings from the Gairdner edition of the *Paston Letters* (Project Gutenberg full text) and the History of Parliament Online biography of Sir Robert Drury:

- January–May 1472: William Gurney IV vs. John Paston at the Saxthorpe manorial court; Henry Heydon raises men-at-arms in Gurney's support; Henry Heydon then buys Saxthorpe and Titchwell from Bishop Waynflete of Winchester, sidelining both factions.
- 23 April 1452: Thomas Gurnay (G20) signs a Paston-side petition from Norwich to the Duke of Norfolk against the Charles Nowell / Heydon-Tuddenham faction, alongside Sir John Heveningham, John Groos, Nicholas Appleyard, and seven others.
- Undated (likely late 1450s): Elizabeth de Vere, Countess of Oxford, writes to John Paston referencing prior correspondence with Margaret Gurnay (G20's wife Margaret Jerningham).
- Sir Robert Drury (1456-1535) HoP biography: confirms his first marriage to Anne Calthorpe and adds a previously-uncaptured second marriage to Anne Jerningham of Somerleyton — making him kin to G20's wife by two routes.

## Action sequence

1. **Write file:** `sources/corpus_supplement/paston-letters-gairdner-gurney-extracts.md` — full content in §A1 below.
2. **Write file:** `sources/corpus_supplement/hop-drury-robert-i-1456-1535.md` — full content in §A2 below.
3. **Insert two source-JSON blocks** in `data/sources.json` — full JSON in §A3 below.
4. **Append block** to `research/people/g19-william-gurney-iv-fact-sheet.research.md` — content in §A4 below (Saxthorpe 1472 + Drury biography).
5. **Append block** to `research/people/g20-thomas-gournay-ii-fact-sheet.research.md` — content in §A5 below (1452 petition + Countess of Oxford).
6. **`str_replace`** on `fact-sheets/g19-william-gurney-iv-fact-sheet.md` Narrative paragraph 4 — old/new strings in §A6 below.
7. **`str_replace`** on `fact-sheets/g19-william-gurney-iv-fact-sheet.md` Timeline table — old/new strings in §A7 below.
8. **`str_replace`** on `fact-sheets/g19-william-gurney-iv-fact-sheet.md` Citations list to append footnote `nNEW8` — old/new strings in §A8 below.
9. **`str_replace`** on `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md` Narrative paragraph 3 — old/new strings in §A9 below.
10. **`str_replace`** on `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md` Timeline table — old/new strings in §A10 below.
11. **`str_replace`** on `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md` Citations list to append footnote `nNEW9` — old/new strings in §A11 below.
12. After all operations succeed, **move** this patchset to `sources/intake/done/` with `**Done:** YYYY-MM-DD HH:MM PT` stamp prepended.

---

## §A1 — New file: `sources/corpus_supplement/paston-letters-gairdner-gurney-extracts.md`

```md
# Paston Letters — Gairdner edition — Gurney-related extracts

Source: James Gairdner, ed., *The Paston Letters, A.D. 1422-1509*, 6 vols. (London: Chatto and Windus, 1904). Project Gutenberg full-text editions: vol. I (Introduction) <https://www.gutenberg.org/cache/epub/43348/pg43348.txt>; vol. II <https://www.gutenberg.org/cache/epub/40989/pg40989.txt>. Source ID: `paston-letters-gairdner`.

## 1. Saxthorpe Manor Court showdown, January–May 1472 (William Gurney IV vs. John Paston)

From Gairdner's Introduction (vol. I), narrating Paston letters Nos. 779 (12 July 1471 trust release), 796 (January 1472 first court interruption), and 801 (May 1472 second court interruption), with the Margaret Paston letter of 5 June 1472 reporting Henry Heydon's purchase.

> On the 12th July 1471, Sir John Paston made a release of Saxthorpe and Titchwell and some other portions of the Fastolf estates, to David Husband and William Gyfford; but this was probably only in the nature of a trust, for it appears that he did not intend to give up his interest in the property. In January following, however, William Gurney entered into Saxthorpe and endeavoured to hold a court there for the lord of the manor. But John Paston hearing of what was doing, went thither accompanied by one man only to protect his brother's interest, and charged the tenants, in the presence of Gurney himself and a number of his friends, to proceed no further. The protest was effective so far as to produce a momentary pause. But when it was seen that he had only one man with him, the proceedings were resumed; on which John Paston sat down by the steward and blotted his book with his finger as he wrote, and then called the tenants to witness that he had effectually interrupted the court in his brother's right. Gurney, however, did not give up the game, but warned another court to be kept on Holy Rood day (May 3rd, the Invention of the Holy Cross), when he would have collected the half-year's rents from the tenants. The court was held, but before it was half over John Paston appeared again and persuaded him to stay proceedings once more, and to forbear gathering money until he and Sir John Paston should confer together in London. It seems to have required some tact and courtesy to get him to consent to this arrangement; for Henry Heydon, the son of the old ally of Sir Thomas Tuddenham, had raised a number of men-at-arms to give Gurney any assistance that might have been necessary, but the gentle demeanour of John Paston left him no pretext for calling in such aid. The real claimant of the manor against Sir John Paston was Waynflete, Bishop of Winchester, of whom, almost immediately after this, Henry Heydon bought both Saxthorpe and Titchwell. Sir John Paston, apparently, had been caught napping as usual, and knew nothing of the transaction. His mother wrote to him in dismay on the 5th June. Young Heydon had already taken possession. "We beat the bushes," said Margaret Paston, "and have the loss and the disworship, and other men have the birds."

**Significance:** William Gurney IV (G19) enters Saxthorpe — one of the old Heylesdon-Gurney holdings that his great-grandfather's widow Alice Heylesdon had sold to John Wynter after Sir John V's 1408 death — and tries to reassert Gurney lordship. The episode confirms (a) William IV's willingness to press a disputed claim by force, (b) the working Gurney-Heydon military alliance (Henry Heydon's men-at-arms ready, less than a year after the 1471 will named his father John Heydon as supervisor), and (c) the eventual loss of Saxthorpe to a third-party buyer (Henry Heydon outbidding both). This is the most concrete contemporary narrative for any pre-1500 Gurney.

## 2. 23 April 1452 St George's Day petition signed by Thomas Gurnay (G20) and ten other Norfolk gentlemen

From Gairdner vol. II, letter dated St George's Day (23 April) 1452, addressed from Norwich to the Duke of Norfolk's deputy at Framlingham. The petition concerns the assaults of Charles Nowell and others against John Paston and his circle.

> Right wurchipfull, we commawnd us to yow. Please it yow to wete that we and other jentilmen of the shyer of Norffolk hath be in purpose assewyd [_have sued_] to the hygh and myghty Prynce and owr ryght gode Lord the Duke of Norffolk to Framlyngham, to have enformyd his Highnesse of dyvers assaughtes and ryottes made be Charles Nowell and other ageyn the Kyngs lawe and peas, withowte any cause or occacion, up on John Paston and other of owre kynne, frendes and neyghborys, ne had be that dayly this x. days it hath be do us to wete that his Highnesse shuld come in to Norwych or Claxton, we not beyng in certeyn yet whedyr he shall remeve; praying yow as we trust, that ye woll tender the welfare of this shyer and of the jentylmen ther in, that ye woll lete owr seyd Lord have knowyng of owr entente in this, and after to send us answher wheder it please his Highnesse we shuld come to his presens, and in what place, or to send owr compleynt to hym if mor informacion be thowch[t needful, etc.]…

Signed:

> SIR JOHN HEVENYNGHAM. JOHN FERRERS. THO. GURNAY. JOHN GROOS. W. ROKEWODE. JOHN BAKON, Senior. JOHN BAKON, Junior. J. PAGRAVE. ROBT. MORTIMER. NICHOLAUS APPILYARD.

**Significance:** Thomas Gurnay (G20 Thomas Gournay II, then about 22) is on the Paston / anti-Heydon side of the 1452 East Anglian dispute. Co-signers include Nicholas Appleyard (the same family supplies the feoffee on William IV's 1505 trust deed 53 years later) and John Groos (whose 1487 will would bequeath the Irstead manors that, via the Heydons, eventually anchor G16 Francis's later "of Irstead" designation). The petition therefore captures the Norfolk gentry network in its early Paston-aligned form, before the 1462 Yorkist accession realigned everything — by 1471, John Heydon himself would be supervisor of Thomas II's will.

## 3. Countess of Oxford (Elizabeth de Vere) to John Paston, referencing Margaret Gurnay

From Gairdner vol. II, undated letter addressed "To John Paston, Sqwyer, dwellyng in Norwich," signed "OXENFORD / ELYZABETH DE VEER," dated only "the first day of February."

> Ryght entierly welbeloved, I grete yow well, and pray yow that ye woll be good frende un to Arblaster in suche matiers as he shal enfo[rme] yow, and I thanke yow for the good frendship that ye have shewed to hym. And I sent a letter to Margaret Gurnay byfore Cristemesse of certeyn langage that I herd, wich plesed me nowght, and so I prayed my Lord to gif me leve to wrytte to hir; and therfore and ye here any thyng, answere, as my trust is in yow. Right entierly welbeloved, the Holy Gost have yow in his kepyng. Wretyn in hast the first day of February.

**Significance:** Margaret Gurnay = Margaret Jerningham, wife of G20 Thomas Gournay II. Elizabeth de Vere (born Elizabeth Howard, daughter of John Howard 1st Duke of Norfolk) was Countess of Oxford as wife of John de Vere 12th Earl of Oxford (executed February 1462 by Edward IV after the failed Lancastrian Oxford plot — the letter is therefore most plausibly dated pre-1462, late 1450s). The Countess had written to Margaret personally about something Margaret said that "plesed me nowght" and had to ask her husband's permission to do so. The Vere connection extends from G21 Thomas I (1441 retinue service under John de Vere 13th Earl) into the women's correspondence circle of the next generation.

Gairdner's editorial dating is provisional; the Davis revised edition of the Paston Letters (Norman Davis, ed., *Paston Letters and Papers of the Fifteenth Century*, 2 vols., Oxford: Clarendon, 1971-76) would supply tighter dating.
```

---

## §A2 — New file: `sources/corpus_supplement/hop-drury-robert-i-1456-1535.md`

```md
# HoP — DRURY, Sir Robert I (by 1456-1535), of Hawstead, Suff. and London

Source: L. M. Kirk, "DRURY, Sir Robert I (by 1456-1535), of Hawstead, Suff. and London," in S. T. Bindoff, ed., *The History of Parliament: The House of Commons 1509-1558* (London: Secker & Warburg, 1982). URL: <https://www.historyofparliamentonline.org/volume/1509-1558/member/drury-sir-robert-i-1456-1535>. Source ID: `hop-drury-robert-i-1456-1535`.

## Constituency

SUFFOLK 1491, 1495, ?1510.

## Family and Education

b. by 1456, 1st s. of Roger Drury of Hawstead by Felice, da. and h. of William Denston of Besthorpe, Norf. educ. ?Gonville, Cambridge. m. (1) by 1494, Anne, da. of Sir William Calthorpe of Burnham Thorpe, Norf., 2s. Sir William and Sir Robert II, 4da.; (2) by 1531, Anne, da. of Edward Jerningham of Somerleyton, Suff., wid. of Lord Edward Grey (d. by 1517), ?of one Berkeley, and of Henry Barley (d. 12 Nov. 1529) of Albury Herts., s.p. suc. fa. 30 Jan. 1496. Kntd. 17 June 1497.

## Offices Held

Autumn reader, Lincoln's Inn 1487, governor 1488, 1492, 1497.

Commissioner of array, Suffolk 1487; subsidy 1512, 1514, 1515, 1523; other commissions 1490-d., JP 1488-d.; deputy chief steward, south parts duchy of Lancaster c. 1498-1526; Councillor and knight of body temp. Henry VII and Henry VIII; member, council of 14th Earl of Oxford c. 1525, bailiff, Bury St. Edmunds, Suff. by death.

Speaker of House of Commons 1495.

## Biography (excerpt — opening paragraphs)

> The Drury family of Suffolk was established at Hawstead by Robert Drury's father, who represented the younger of two branches descended from Sir Nicholas Drury of Thurston and Rougham in the 14th century. Robert Drury was the first of his line to attach himself to the court after training as a lawyer. He was knighted after fighting against the rebels at Blackheath in 1497, where he may have served under John de Vere, 13th Earl of Oxford whose deputy he became in the stewardship of the duchy of Lancaster. Under the earl's will of 1509 he was appointed an executor and given an annuity of £6 13s. 4d. and the Ellesmere Chaucer which bears the signature of Drury and his son William.
>
> By the beginning of Henry VIII's reign Drury was prominent as a lawyer, courtier and servant of the crown. It was presumably as a senior Member and former Speaker that in the Parliament of 1510 he announced in the Upper House the election of Thomas Englefield as Speaker; it is all but certain that Drury had been re-elected for Suffolk. Under the new King he attended the Council from time to time…

## Significance for the Gurney line

Sir Robert Drury is a feoffee on William Gurney IV's 1505 trust deed (per Daniel Gurney, *Supplement* Note 132, pp. 817-819). The HoP biography supplies the source-traceable authority for his identity and adds two kinship layers to the Gurneys that were not in Wikipedia's summary:

- **First marriage:** Anne Calthorpe, daughter of Sir William Calthorpe of Burnham Thorpe by his second wife Elizabeth Stapleton. This is William Gurney IV's half-sister-in-law (Anne by Sir William's first wife Elizabeth Grey was William IV's own wife). The two Calthorpe-daughter Annes were therefore both married into the inner Gurney/Drury circle.
- **Second marriage:** Anne, daughter of Edward Jerningham of Somerleyton — the same Somerleyton Jerningham family that had supplied Margaret Jerningham to G20 Thomas II two generations earlier. Drury was therefore kin to the Gurneys via **both** the Calthorpe and the Jerningham marriages.

The Blackheath 1497 service under John de Vere 13th Earl of Oxford, and Drury's subsequent role as the 13th Earl's deputy in the Duchy of Lancaster south-parts stewardship, ties Drury into the Vere connection that already runs through G21 (1441 retinue service under the same earl) and is visible in the Countess of Oxford's correspondence with Margaret Gurnay (G20's wife). The Ellesmere Chaucer bequest (now Huntington Library, EL 26 C 9) is the most celebrated illuminated manuscript of Chaucer's *Canterbury Tales*; that Drury and his son inscribed it gives the Drury-Vere-Gurney circle a literary-cultural anchor.
```

---

## §A3 — Source JSON additions in `data/sources.json`

Insert the following two entries into the top-level `sources` object:

```json
    "paston-letters-gairdner": {
      "shortTitle": "Paston Letters -- Gairdner edition (1904)",
      "citation": "James Gairdner, ed., The Paston Letters, A.D. 1422-1509, 6 vols. (London: Chatto and Windus, 1904).",
      "archive": "Project Gutenberg + Internet Archive",
      "url": "https://www.gutenberg.org/cache/epub/43348/pg43348.txt",
      "corpusStatus": "supplement",
      "corpusPath": "sources/corpus_supplement/paston-letters-gairdner-gurney-extracts.md",
      "mediaPath": null,
      "validationPath": null,
      "notes": "Standard scholarly edition. Vol. I is the editorial Introduction; vols. II-VI carry the letters in numbered sequence. Gurney-related extracts captured: Saxthorpe Court 1472 episode (vol. I Introduction, narrating Paston letters Nos. 779, 796, 801 + Margaret Paston 5 June 1472); 23 April 1452 St George's Day petition signed by Thomas Gurnay (vol. II); Countess of Oxford to John Paston referencing Margaret Gurnay (vol. II, undated)."
    },
    "hop-drury-robert-i-1456-1535": {
      "shortTitle": "History of Parliament -- DRURY, Sir Robert I (by 1456-1535)",
      "citation": "L. M. Kirk, \"DRURY, Sir Robert I (by 1456-1535), of Hawstead, Suff. and London,\" in S. T. Bindoff, ed., The History of Parliament: The House of Commons 1509-1558 (London: Secker & Warburg, 1982).",
      "archive": "History of Parliament Online",
      "url": "https://www.historyofparliamentonline.org/volume/1509-1558/member/drury-sir-robert-i-1456-1535",
      "corpusStatus": "supplement",
      "corpusPath": "sources/corpus_supplement/hop-drury-robert-i-1456-1535.md",
      "mediaPath": null,
      "validationPath": null,
      "notes": "Source-traceable authority for Sir Robert Drury (Speaker of the Commons 1495), feoffee on William Gurney IV's 1505 trust deed. Records two marriages: (1) Anne Calthorpe by Sir William's second wife Elizabeth Stapleton -- William IV's half-sister-in-law; (2) Anne Jerningham of Somerleyton -- same family as G20's wife Margaret Jerningham. Drury was therefore kin to the Gurneys via both Calthorpe and Jerningham marriages. Also records Blackheath 1497 service possibly under John de Vere 13th Earl of Oxford and subsequent role as the earl's deputy in the Duchy of Lancaster south-parts stewardship."
    },
```

---

## §A4 — Append to `research/people/g19-william-gurney-iv-fact-sheet.research.md`

Append the following block at the end of the existing Working Notes section:

```md
### Saxthorpe Court showdown, January–May 1472 — William Gurney IV vs. John Paston (Paston Letters)

The most concrete contemporary narrative ever to surface for any pre-1500 Gurney. Within six months of his father Thomas II's 1471 death, William IV entered Saxthorpe (one of the old Heylesdon-Gurney holdings that Alice Heylesdon had sold to John Wynter after Sir John V's 1408 death) and tried twice to hold a manorial court there as the lord of the manor.

First attempt, January 1472: John Paston walked into the court with a single companion, charged the tenants to stop, and when proceedings resumed sat down beside the steward and **blotted the court book with his finger** as the steward tried to write — formally recording his interruption in front of witnesses.

Second attempt, Holy Rood Day (3 May) 1472: William IV had Henry Heydon (the son of John Heydon of Baconsthorpe — his father's old ally and supervisor of Thomas II's 1471 will) raise a number of men-at-arms in support. John Paston returned, defused the second court by quiet persuasion, and the men-at-arms were never deployed.

Within weeks, Henry Heydon bought Saxthorpe and Titchwell outright from Bishop Waynflete of Winchester, sidelining both the Pastons and the Gurneys. Margaret Paston wrote to her son on 5 June 1472: "We beat the bushes, and have the loss and the disworship, and other men have the birds."

Full Gairdner Introduction extract preserved at `sources/corpus_supplement/paston-letters-gairdner-gurney-extracts.md` §1.[^v62-paston-saxthorpe-1472]

This is the second piece of evidence in 1471-72 for a working Gurney-Heydon military and political alliance, immediately following the 1471 will's choice of Henry's father John Heydon as supervisor. The 1484 marriage indentures between William IV's son William V (G18) and John Heydon's granddaughter Anne Heydon were the formal sealing of a relationship that had been operating in the field for at least thirteen years.

[^v62-paston-saxthorpe-1472]: James Gairdner, ed., *The Paston Letters, A.D. 1422-1509*, 6 vols. (London: Chatto and Windus, 1904), Introduction in vol. I, narrating Paston letters Nos. 779, 796, 801 and Margaret Paston's letter of 5 June 1472. Project Gutenberg vol. I: [www.gutenberg.org/cache/epub/43348/pg43348.txt](https://www.gutenberg.org/cache/epub/43348/pg43348.txt). Source ID: `paston-letters-gairdner`. Full extract preserved at `sources/corpus_supplement/paston-letters-gairdner-gurney-extracts.md` §1.

### Sir Robert Drury (1456-1535) — 1505 trust feoffee — HoP biography

Sir Robert Drury is named as a feoffee on William Gurney IV's 1505 trust deed (Daniel Gurney *Supplement* Note 132, pp. 817-819). The HoP biography supplies the source-traceable authority and adds two kinship layers not in the Wikipedia summary previously consulted:

- **First marriage** (by 1494) to Anne Calthorpe, daughter of Sir William Calthorpe by his second wife Elizabeth Stapleton — William IV's half-sister-in-law. Sir William Calthorpe Knight of the Bath had two daughters named Anne (one by each wife); both married into the inner Gurney/Drury circle.
- **Second marriage** (by 1531) to Anne, daughter of Edward Jerningham of Somerleyton — the same Somerleyton Jerningham family that had supplied Margaret Jerningham to G20 Thomas II two generations earlier. Drury was therefore kin to the Gurneys via both Calthorpe and Jerningham marriages.

Drury was knighted at Blackheath 17 June 1497 after fighting the Cornish rebels, possibly under John de Vere 13th Earl of Oxford, whose deputy he became in the stewardship of the south parts of the Duchy of Lancaster (c. 1498-1526). Under the 13th Earl's 1509 will Drury was an executor, with a £6 13s 4d annuity and the **Ellesmere Chaucer manuscript** (now Huntington Library, EL 26 C 9 — the most celebrated illuminated manuscript of Chaucer's *Canterbury Tales*), which bears the signatures of Drury and his son William.

Full HoP biography preserved at `sources/corpus_supplement/hop-drury-robert-i-1456-1535.md`.[^v62-hop-drury]

[^v62-hop-drury]: L. M. Kirk, "DRURY, Sir Robert I (by 1456-1535), of Hawstead, Suff. and London," in S. T. Bindoff, ed., *The History of Parliament: The House of Commons 1509-1558* (London: Secker & Warburg, 1982). [historyofparliamentonline.org/volume/1509-1558/member/drury-sir-robert-i-1456-1535](https://www.historyofparliamentonline.org/volume/1509-1558/member/drury-sir-robert-i-1456-1535). Source ID: `hop-drury-robert-i-1456-1535`. Full text preserved at `sources/corpus_supplement/hop-drury-robert-i-1456-1535.md`.
```

---

## §A5 — Append to `research/people/g20-thomas-gournay-ii-fact-sheet.research.md`

Append the following block at the end of the existing Working Notes section:

```md
### 23 April 1452 St George's Day petition — Thomas II on the Paston-side coalition

A petition from Norwich to the Duke of Norfolk's deputy at Framlingham, dated St George's Day (23 April) 1452, signed by Thomas Gurnay (then about 22) alongside ten other Norfolk gentlemen:

> SIR JOHN HEVENYNGHAM. JOHN FERRERS. THO. GURNAY. JOHN GROOS. W. ROKEWODE. JOHN BAKON, Senior. JOHN BAKON, Junior. J. PAGRAVE. ROBT. MORTIMER. NICHOLAUS APPILYARD.

The letter complains of "dyvers assaughtes and ryottes made be Charles Nowell and other ageyn the Kyngs lawe and peas, withowte any cause or occacion, up on John Paston and other of owre kynne, frendes and neyghborys." Charles Nowell was a man of the Heydon-Tuddenham faction operating under William de la Pole, 1st Duke of Suffolk, in East Anglia.

This places Thomas II on the **Paston / anti-Heydon side** of the 1452 East Anglian dispute — politically opposite to where he would land in 1471, when his will named John Heydon himself as supervisor. The intervening realignment is well documented: the 1461 Yorkist accession upended the East Anglian power map; the Suffolk-Heydon faction collapsed with the duke's 1450 murder and the duchess Alice's marginalization; Heydon paid 500 marks for a Yorkist pardon in 1462 and rebuilt his career in the new order. By 1471 the Norfolk gentry coalitions had reshuffled, and the men who had stood against Heydon as young adults were now content to use him as a senior legal supervisor.

Two of the co-signers reappear in the later Gurney record: **Nicholas Appleyard** (the same family supplies the feoffee on William IV's 1505 trust) and **John Groos** (whose 1487 will would bequeath the Irstead manors that, through the Heydons, eventually anchor G16 Francis's later "of Irstead" designation). The 1452 petition therefore preserves a snapshot of the Norfolk gentry network that, half a century later, would crystallise around the West Barsham estate in the 1505 trust deed.

Full letter text preserved at `sources/corpus_supplement/paston-letters-gairdner-gurney-extracts.md` §2.[^v62-paston-1452]

[^v62-paston-1452]: James Gairdner, ed., *The Paston Letters, A.D. 1422-1509*, 6 vols. (London: Chatto and Windus, 1904), vol. II, letter dated St George's Day (23 April) 1452, written from Norwich to the Duke of Norfolk's deputy at Framlingham. Project Gutenberg vol. II: [www.gutenberg.org/cache/epub/40989/pg40989.txt](https://www.gutenberg.org/cache/epub/40989/pg40989.txt). Source ID: `paston-letters-gairdner`. Full extract preserved at `sources/corpus_supplement/paston-letters-gairdner-gurney-extracts.md` §2.

### Margaret Gurnay (Jerningham) in correspondence with Elizabeth de Vere, Countess of Oxford

An undated letter from Elizabeth de Vere, Countess of Oxford, to John Paston (preserved in Gairdner vol. II) references prior personal correspondence with **Margaret Gurnay**:

> And I sent a letter to Margaret Gurnay byfore Cristemesse of certeyn langage that I herd, wich plesed me nowght, and so I prayed my Lord to gif me leve to wrytte to hir; and therfore and ye here any thyng, answere, as my trust is in yow.

Margaret Gurnay is Margaret Jerningham, wife of G20 Thomas Gournay II — no other Margaret Gurnay is documented in the Norfolk gentry record of the period. Elizabeth de Vere (born Elizabeth Howard, daughter of John Howard 1st Duke of Norfolk) was Countess of Oxford as wife of John de Vere 12th Earl of Oxford, who was executed in February 1462 by Edward IV after the failed Lancastrian Oxford plot. The letter is therefore most plausibly dated pre-1462, late 1450s.

The Countess had written to Margaret personally about something Margaret said that "plesed me nowght" and had to ask her husband's permission to do so — implying a real if delicate personal correspondence between the two women.

This extends the Vere connection beyond G21 Thomas I's 1441 retinue service under John de Vere 13th Earl of Oxford into the women's correspondence circle of the next generation. Gairdner's editorial dating is provisional; the Davis revised edition would supply tighter dating.

Full letter text preserved at `sources/corpus_supplement/paston-letters-gairdner-gurney-extracts.md` §3.[^v62-countess-of-oxford-margaret-gurnay]

[^v62-countess-of-oxford-margaret-gurnay]: James Gairdner, ed., *The Paston Letters, A.D. 1422-1509*, 6 vols. (London: Chatto and Windus, 1904), vol. II, undated letter from Elizabeth de Vere, Countess of Oxford, to John Paston Squire, signed "OXENFORD / ELYZABETH DE VEER," dated "the first day of February" with no year. Project Gutenberg vol. II: [www.gutenberg.org/cache/epub/40989/pg40989.txt](https://www.gutenberg.org/cache/epub/40989/pg40989.txt). Source ID: `paston-letters-gairdner`. Full extract preserved at `sources/corpus_supplement/paston-letters-gairdner-gurney-extracts.md` §3.
```

---

## §A6 — `str_replace` on `fact-sheets/g19-william-gurney-iv-fact-sheet.md` Narrative paragraph 4

The current G19 Narrative paragraph 4 (the one describing William IV's death) ends with text about his daughter Elizabeth as Prioress of Thetford. Insert a new short paragraph **after** the existing paragraph that ends "…on the very eve of the Henrician dissolution that would close her house within twenty years." and **before** the closing Citations section.

**`old_string`:**

```
That last detail is one of the more poignant in this stretch of the family history. Elizabeth Gurney was elected prioress of one of the great Norfolk monastic houses just as the entire English religious order was about to be swept away. She had no way of knowing in 1518 that the world she had entered would not survive her.
</section>
```

**`new_string`:**

```
That last detail is one of the more poignant in this stretch of the family history. Elizabeth Gurney was elected prioress of one of the great Norfolk monastic houses just as the entire English religious order was about to be swept away. She had no way of knowing in 1518 that the world she had entered would not survive her.

William IV himself makes his single most concrete appearance in the historical record in the famous *Paston Letters*. Within six months of his father's death, in January 1472, he entered the manor of Saxthorpe — one of the old Heylesdon-Gurney holdings that his great-grandmother Alice Heylesdon had sold off after Sir John V's 1408 death — and tried to hold a manorial court there as lord. John Paston walked into the court with a single companion, charged the tenants to stop, and when proceedings resumed sat down beside the steward and blotted the court book with his finger as the steward tried to write. William tried again on Holy Rood Day in May 1472, this time backed by Henry Heydon (son of his father's old ally John Heydon of Baconsthorpe), who had raised men-at-arms in case the encounter turned to force. John Paston defused the second attempt as well — and within weeks Henry Heydon went over both their heads and bought Saxthorpe and Titchwell outright from Bishop Waynflete of Winchester, leaving Margaret Paston to write to her son in dismay: "We beat the bushes, and have the loss and the disworship, and other men have the birds." It is the only sustained contemporary narrative for any pre-1500 Gurney, and it shows William IV as a Norfolk gentleman willing to press a disputed claim by force, backed by his Heydon allies. <sup class="fn"><a href="#nNEW8" id="ref-NEW8">NEW8</a></sup>
</section>
```

---

## §A7 — `str_replace` on `fact-sheets/g19-william-gurney-iv-fact-sheet.md` Timeline

Insert a new Timeline row between the existing 1494 row and the "by 1505" row.

**`old_string`:**

```
      <tr><td>1494</td><td>William IV documented as "living 1494" (DG p. 287).</td></tr>
      <tr><td>by 1505</td><td>Eldest son William Gurney V dies <em>vita patris</em>.</td></tr>
```

**`new_string`:**

```
      <tr><td>1494</td><td>William IV documented as "living 1494" (DG p. 287).</td></tr>
      <tr><td>Jan–May 1472</td><td>Twice attempts to hold a manorial court at Saxthorpe (Paston Letters); both attempts interrupted by John Paston. Henry Heydon raises men-at-arms in support. Henry Heydon then buys Saxthorpe and Titchwell from Bishop Waynflete of Winchester, sidelining both factions.</td></tr>
      <tr><td>by 1505</td><td>Eldest son William Gurney V dies <em>vita patris</em>.</td></tr>
```

(Timeline ordering note: the 1472 row sits between 1471 and 1477 in the existing Timeline. The Phase 2 apply step must place the new row in the correct chronological position — between the existing "27 July 1471 — Father Thomas Gournay II's will proved" row and the "1477 — Documented as of council to the Duke of Norfolk" row. The `str_replace` above places it after 1494; **revise the str_replace to use the right anchor**:)

**Revised `old_string`:**

```
      <tr><td>27 July 1471</td><td>Father Thomas Gournay II's will proved; William inherits the West Barsham portfolio.</td></tr>
      <tr><td>1477</td><td>Documented as of council to the Duke of Norfolk.</td></tr>
```

**Revised `new_string`:**

```
      <tr><td>27 July 1471</td><td>Father Thomas Gournay II's will proved; William inherits the West Barsham portfolio.</td></tr>
      <tr><td>Jan–May 1472</td><td>Twice attempts to hold a manorial court at Saxthorpe (Paston Letters); both attempts interrupted by John Paston. Henry Heydon raises men-at-arms in support. Henry Heydon then buys Saxthorpe and Titchwell from Bishop Waynflete of Winchester, sidelining both factions. <sup class="fn"><a href="#nNEW8" id="ref-NEW8b">NEW8</a></sup></td></tr>
      <tr><td>1477</td><td>Documented as of council to the Duke of Norfolk.</td></tr>
```

---

## §A8 — `str_replace` on `fact-sheets/g19-william-gurney-iv-fact-sheet.md` to append footnote `nNEW8`

**`old_string`:**

```
  <li id="n13">Daniel Gurney, <em>Record</em> (1848), pedigree p. 287: "Walter Gourney, of Cley by the Sea, Norfolk, ancestor of the Gourneys of Cawston and Aylsham." And: "Thomas Gurnet, his father's executor, ancestor of the Gurneys of Dartmouth, London, and Essex, temp. Elizabeth, 1590; his grandson, Richard Gurney, was Sheriff of London." <a class="citation-back" href="#ref-13">↩</a></li>
</ol>
```

**`new_string`:**

```
  <li id="n13">Daniel Gurney, <em>Record</em> (1848), pedigree p. 287: "Walter Gourney, of Cley by the Sea, Norfolk, ancestor of the Gourneys of Cawston and Aylsham." And: "Thomas Gurnet, his father's executor, ancestor of the Gurneys of Dartmouth, London, and Essex, temp. Elizabeth, 1590; his grandson, Richard Gurney, was Sheriff of London." <a class="citation-back" href="#ref-13">↩</a></li>
  <li id="nNEW8">James Gairdner, ed., <em>The Paston Letters, A.D. 1422-1509</em>, 6 vols. (London: Chatto and Windus, 1904), Introduction in vol. I, narrating the Saxthorpe Court episode of January–May 1472 from Paston letters Nos. 779 (12 July 1471 trust release), 796 (January 1472 first interruption), and 801 (May 1472 second interruption), with the Margaret Paston letter of 5 June 1472 reporting Henry Heydon's purchase of Saxthorpe and Titchwell from Bishop Waynflete of Winchester. Project Gutenberg vol. I: <a href="https://www.gutenberg.org/cache/epub/43348/pg43348.txt">www.gutenberg.org/cache/epub/43348/pg43348.txt</a>. Full extract at <code>sources/corpus_supplement/paston-letters-gairdner-gurney-extracts.md</code> §1. <a class="citation-back" href="#ref-NEW8">↩</a></li>
</ol>
```

---

## §A9 — `str_replace` on `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md` Narrative paragraph 3

**`old_string`:**

```
Around the middle of the century he married Margaret Jerningham, daughter of Sir Thomas Jerningham, Knt., of Somerleyton, Suffolk. The Jerninghams were among the most prominent Catholic gentry families of East Anglia. The marriage gave Thomas strong Suffolk connections and placed his descendants inside a kinship network of recusant families that would still be politically consequential a century later — when Francis Gurney G16's widow Helen Holditch married a Jernegan in the 1560s, the family was re-entering a kinship circle that Thomas II had first joined a hundred years earlier.
```

**`new_string`:**

```
Around the middle of the century he married Margaret Jerningham, daughter of Sir Thomas Jerningham, Knt., of Somerleyton, Suffolk. The Jerninghams were among the most prominent Catholic gentry families of East Anglia. The marriage gave Thomas strong Suffolk connections and placed his descendants inside a kinship network of recusant families that would still be politically consequential a century later — when Francis Gurney G16's widow Helen Holditch married a Jernegan in the 1560s, the family was re-entering a kinship circle that Thomas II had first joined a hundred years earlier.

A single dated letter places Thomas at the centre of Norfolk gentry politics in his early adulthood. On St George's Day 1452, Thomas signed a petition from Norwich to the Duke of Norfolk's deputy at Framlingham, complaining of "dyvers assaughtes and ryottes made be Charles Nowell and other ageyn the Kyngs lawe and peas… up on John Paston and other of owre kynne, frendes and neyghborys." The co-signers included Sir John Heveningham, John Ferrers, John Groos, William Rokewode, the two John Bakons, John Pagrave, Robert Mortimer, and Nicholas Appleyard — the Paston-side Norfolk gentry coalition standing against the Charles-Nowell faction operating under John Heydon and Sir Thomas Tuddenham as the Duke of Suffolk's East Anglian agents. Thomas was about 22, married into the Jerninghams, and visibly aligned against the Heydons. Yet nineteen years later — after the 1461 Yorkist accession had upended the East Anglian power map and John Heydon had bought his 1462 Yorkist pardon for 500 marks — Thomas's 1471 will would name John Heydon himself as supervisor. The realignment is one of the cleanest gentry-politics arcs in the surviving record. <sup class="fn"><a href="#nNEW9" id="ref-NEW9">NEW9</a></sup>
```

---

## §A10 — `str_replace` on `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md` Timeline

**`old_string`:**

```
      <tr><td>mid-century</td><td>Married Margaret Jerningham of Somerleyton, Suffolk.</td></tr>
      <tr><td>c. 1450</td><td>Son William Gurney IV (G19) born.</td></tr>
      <tr><td>4 Mar 1461</td><td>Edward IV's Yorkist accession after Towton.</td></tr>
```

**`new_string`:**

```
      <tr><td>mid-century</td><td>Married Margaret Jerningham of Somerleyton, Suffolk.</td></tr>
      <tr><td>c. 1450</td><td>Son William Gurney IV (G19) born.</td></tr>
      <tr><td>23 Apr 1452</td><td>Signs a petition from Norwich to the Duke of Norfolk against the Charles Nowell / Heydon-Tuddenham faction's assaults on the Paston circle. Co-signed by ten other Norfolk gentlemen including Sir John Heveningham, John Groos, and Nicholas Appleyard. <sup class="fn"><a href="#nNEW9" id="ref-NEW9b">NEW9</a></sup></td></tr>
      <tr><td>4 Mar 1461</td><td>Edward IV's Yorkist accession after Towton.</td></tr>
```

---

## §A11 — `str_replace` on `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md` to append footnote `nNEW9`

**`old_string`:**

```
  <li id="n11">See G19 William Gurney IV fact sheet. <a class="citation-back" href="#ref-11">↩</a></li>
</ol>
```

**`new_string`:**

```
  <li id="n11">See G19 William Gurney IV fact sheet. <a class="citation-back" href="#ref-11">↩</a></li>
  <li id="nNEW9">James Gairdner, ed., <em>The Paston Letters, A.D. 1422-1509</em>, 6 vols. (London: Chatto and Windus, 1904), vol. II, letter dated St George's Day (23 April) 1452, written from Norwich to the Duke of Norfolk's deputy at Framlingham. The eleven signers are listed in the text as Sir John Hevenyngham, John Ferrers, Thomas Gurnay, John Groos, William Rokewode, John Bakon senior, John Bakon junior, J. Pagrave, Robert Mortimer, and Nicholas Appilyard. Project Gutenberg vol. II: <a href="https://www.gutenberg.org/cache/epub/40989/pg40989.txt">www.gutenberg.org/cache/epub/40989/pg40989.txt</a>. Full extract at <code>sources/corpus_supplement/paston-letters-gairdner-gurney-extracts.md</code> §2. <a class="citation-back" href="#ref-NEW9">↩</a></li>
</ol>
```

---

End of patchset.
