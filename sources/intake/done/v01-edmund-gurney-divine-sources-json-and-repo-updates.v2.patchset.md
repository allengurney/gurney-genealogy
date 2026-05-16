# Patchset v2: Edmund Gurney / Edmund Gurnay (divine) update

**Prepared:** 2026-04-26  
**Target repo:** `allengurney/gurney-genealogy`  
**Scope:** Replacement markdown for Edmund Gurney related fact sheet and research companion; `sources.json` insertions; optional corpus/validation source files; optional generated-site mirrors.

## `data/sources.json` patch

### 1. Update metadata date

Change:

```json
"lastUpdated": "2026-04-19"
```

to:

```json
"lastUpdated": "2026-04-27"
```

### 2. Insert / update source entries

Insert the following entries under `"sources"` near the existing Edmund-related and early-modern Gurney sources. If a nearby related entry already exists, preserve sort conventions used in the file.

```json
    "dnb-edmund-gurney-1890": {
      "shortTitle": "DNB — Edmund Gurney (d.1648)",
      "citation": "Kingsford, Charles Lethbridge. "Gurney or Gurnay, Edmund (d. 1648)." In Sidney Lee, ed., Dictionary of National Biography, vol. 23. London: Smith, Elder & Co., 1890.",
      "archive": "Wikisource transcription of Dictionary of National Biography, 1885-1900, vol. 23",
      "url": "https://en.wikisource.org/wiki/Dictionary_of_National_Biography,_1885-1900/Gurney,_Edmund_(d.1648)",
      "corpusStatus": "full",
      "corpusPath": "sources/corpus_supplement/dnb-edmund-gurney-1890.md",
      "mediaPath": null,
      "validationPath": "sources/validations/dnb-edmund-gurney-1890.md",
      "notes": "Core public-domain biographical source for Edmund Gurney/Gurnay, d.1648: parentage, Cambridge chronology, Edgefield and Harpley livings, Puritan inclination, surplice anecdote, burial at St Peter Mancroft Norwich on 14 May 1648, wife Ellen, apparent son Protestant, works list, and Gurnay/Gurney spelling note."
    },
    "ggm-benefice-harpley-rectors": {
      "shortTitle": "GGM Benefice — Harpley Register of Rectors",
      "citation": ""Register of Rectors." GGM Benefice, Harpley, St Lawrence.",
      "archive": "GGM Benefice website",
      "url": "https://www.ggmbenefice.uk/our-churches/harpley/register-of-rectors/",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/ggm-benefice-harpley-rectors-edmund-gurnay.md",
      "mediaPath": null,
      "validationPath": null,
      "notes": "Local Harpley rector list and biographical synthesis. Useful for Edmund Gurnay's 1620-1648 Harpley rectorship, local 'Puritan Rector' tradition, ordination and Oxford-incorporation leads, Protestant Gurnay epitaph transcription, alehouse note, and Wren-visitation/excommunication lead. Treat as secondary/local synthesis and verify contested details."
    },
    "gurnay-redivivus-1660": {
      "shortTitle": "Gurnay Redivivus (1660)",
      "citation": "Gurnay, Edmund. Gurnay redivivus, or an appendix unto the homily against images in churches. London: Printed for J. Rothwel at the Fountain in Goldsmiths-Row in Cheap-side, 1660.",
      "archive": "Folger Shakespeare Library catalog / Internet Archive scan",
      "url": "https://catalog.folger.edu/record/154518",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/gurnay-redivivus-1660-research-extract.md",
      "mediaPath": null,
      "validationPath": null,
      "notes": "Primary printed anti-image tract by Edmund Gurnay, B.D., minister at Harpley. Folger records this as a 1660 second edition, originally published in 1641, with a same-year reissue/cancel title issue. DNB reports republication in 1661; preserve this bibliographic discrepancy pending ESTC/Wing and scan-level review."
    },
    "folger-corpus-christi-1619": {
      "shortTitle": "Folger — Corpus Christi (1619)",
      "citation": "Gurnay, Edmund. Corpus Christi. Cambridge: Cantrell Legge, printer to the University of Cambridge, 1619.",
      "archive": "Folger Shakespeare Library catalog",
      "url": "https://catalog.folger.edu/record/159988",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Bibliographic control for Edmund Gurnay's 1619 treatise against transubstantiation; sermon on Matthew 26:26; STC 12527."
    },
    "ota-corpus-christi-1619": {
      "shortTitle": "OTA — Corpus Christi (1619)",
      "citation": "Gurnay, Edmund. Corpus Christi. Oxford Text Archive, OTA A02396.",
      "archive": "Oxford Text Archive / Text Creation Partnership",
      "url": "https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/A02396",
      "corpusStatus": "available",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Publicly available text/corpus files for Corpus Christi, useful for future direct textual analysis."
    },
    "folger-romish-chaine-1624": {
      "shortTitle": "Folger — The Romish chaine (1624)",
      "citation": "Gurnay, Edmund. The Romish chaine. By Edmund Gurnay, parson of Harpley. London: Printed by Augustine Mathewes for Mathew Law, 1624.",
      "archive": "Folger Shakespeare Library catalog",
      "url": "https://catalog.folger.edu/record/401784",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Bibliographic control for Edmund Gurnay's 1624 anti-Roman tract; STC 12530; title identifies him as parson of Harpley."
    },
    "ota-romish-chaine-1624": {
      "shortTitle": "OTA — The Romish chaine (1624)",
      "citation": "Gurnay, Edmund. The Romish chaine. Oxford Text Archive, OTA A02400.",
      "archive": "Oxford Text Archive / Text Creation Partnership",
      "url": "https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/A02400",
      "corpusStatus": "available",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Publicly available text/corpus files for The Romish chaine, useful for future direct textual analysis."
    },
    "folger-demonstration-antichrist-1631": {
      "shortTitle": "Folger — Demonstration of Antichrist (1631)",
      "citation": "Gurnay, Edmund. The demonstration of Antichrist. London: Printed by John Beale for James Boler, 1631.",
      "archive": "Folger Shakespeare Library catalog",
      "url": "https://catalog.folger.edu/record/168785",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Bibliographic control for Edmund Gurnay's 1631 anti-Roman tract; title identifies him as B.D. and parson of Harpley, Norfolk; STC 12529."
    },
    "folger-second-commandment-1639": {
      "shortTitle": "Folger — Toward the vindication of the Second Commandment (1639)",
      "citation": "Gurnay, Edmund. Toward the vindication of the Second Commandment. Cambridge: Thomas Buck, one of the printers to the University of Cambridge, 1639.",
      "archive": "Folger Shakespeare Library catalog",
      "url": "https://catalog.folger.edu/record/159994",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Bibliographic control for Edmund Gurnay's 1639 anti-image tract; title identifies him as Bachelor in Divinity and minister of God's word at Harpley in Norfolk; STC 12531."
    },
    "grokipedia-edmund-gurney-divine": {
      "shortTitle": "Grokipedia — Edmund Gurney (divine)",
      "citation": ""Edmund Gurney (divine)." Grokipedia. User-supplied article capture, 2026-04-26.",
      "archive": "User-supplied capture in ChatGPT conversation",
      "url": "https://grokipedia.com/page/edmund_gurney_divine",
      "corpusStatus": "captured",
      "corpusPath": "sources/corpus_supplement/grokipedia-edmund-gurney-divine-capture.md",
      "mediaPath": null,
      "validationPath": "sources/validations/grokipedia-edmund-gurney-divine.md",
      "notes": "Tertiary online encyclopedia article supplied by user. Useful as a digest and as a claim checklist, but not as a core authority. Contains apparent conflicts or errors including a stray Happisburgh reference and a Harpley patron reference to Sir Robert Barker; validate each claim against DNB, Thoms, Folger/OTA, CCEd, parish, and diocesan sources before use."
    },
```

### JSON syntax note

If these entries are inserted before the final source object, the last inserted object needs a trailing comma. If inserted at the end of `"sources"`, remove the trailing comma after `grokipedia-edmund-gurney-divine`.

Validate:

```bash
python -m json.tool data/sources.json >/tmp/sources-json-check.json
```

## New corpus / validation files

Create these files if the repo practice is to keep source extracts close to the source catalog.

### `sources/corpus_supplement/dnb-edmund-gurney-1890.md`

```markdown
# DNB — Edmund Gurney / Gurnay (d.1648)

**Source ID:** `dnb-edmund-gurney-1890`

**Citation:** Charles Lethbridge Kingsford, "Gurney or Gurnay, Edmund (d. 1648)," in Sidney Lee, ed., *Dictionary of National Biography*, vol. 23 (London: Smith, Elder & Co., 1890).

**URL:** https://en.wikisource.org/wiki/Dictionary_of_National_Biography,_1885-1900/Gurney,_Edmund_(d.1648)

## Extracted facts

- Son of Henry Gurney of West Barsham and Ellingham, Norfolk, and Ellen Blennerhasset, daughter of John Blennerhasset of Barsham, Suffolk.
- Matriculated Queens' College, Cambridge, 30 Oct. 1594; B.A. 1600.
- Norfolk fellow of Corpus Christi College, 1601; M.A. 1602; B.D. 1609.
- Suspended in 1607 for not being in orders; reinstated by the vice-chancellor.
- Presented to Edgefield in 1614; held it until 1620; then received Harpley.
- Inclined to Puritanism; cited for not using a surplice.
- Died in 1648; buried at St Peter Mancroft, Norwich, 14 May 1648.
- Successor at Harpley instituted the next day.
- Married; wife Ellen; apparently had a son named Protestant.
- Works include `Corpus Christi`, `The Romish Chain`, `The Demonstration of Antichrist`, `Toward the Vindication of Second Commandment`, and continuation later known as `Gurnay Redivivus`.
- Title pages use Gurnay; family usually described as Gurney.
```

### `sources/corpus_supplement/ggm-benefice-harpley-rectors-edmund-gurnay.md`

```markdown
# GGM Benefice — Harpley Register of Rectors: Edmund Gurnay

**Source ID:** `ggm-benefice-harpley-rectors`

**URL:** https://www.ggmbenefice.uk/our-churches/harpley/register-of-rectors/

## Extracted facts and leads

- Harpley rector 1620-1648.
- Styled "The Puritan Rector."
- Gives birth as 1578 and family context at Great Ellingham.
- Gives Cambridge and Oxford-incorporation details; verify against university records.
- Gives ordination details; verify against CCEd/diocesan registers.
- Gives Edgefield patron as Sir Richard Stubbs of Sedgeford.
- Gives Harpley patronage context through Sir William Yelverton and the Stubbe/Yelverton chain.
- Gives a transcription of the Protestant [Gur]nay epitaph, dated 1623.
- Notes alehouse suppression and Wren-visitation/excommunication traditions; verify against primary records.
```

### `sources/corpus_supplement/grokipedia-edmund-gurney-divine-capture.md`

Use the user-supplied article text as the source capture, with this header:

```markdown
# Grokipedia — Edmund Gurney (divine): User-supplied capture

**Source ID:** `grokipedia-edmund-gurney-divine`

**URL:** https://grokipedia.com/page/edmund_gurney_divine

**Capture date:** 2026-04-26

## Source status

Tertiary digest. Use only as a claim checklist and interpretive prompt. Do not use as sole support for contested facts.

## Validation cautions

- Contains one unsupported/conflicting reference to Happisburgh; DNB, Thoms, and Harpley support Edgefield.
- Contains one conflicting Harpley patron reference to Sir Robert Barker; Thoms and Harpley support the Yelverton/Stubbe chain.
- Extended interpretive summaries of Edmund's theology require direct checking against the printed works.
```

### `sources/validations/grokipedia-edmund-gurney-divine.md`

```markdown
# Source validation: Grokipedia — Edmund Gurney (divine)

**Source ID:** `grokipedia-edmund-gurney-divine`

## Validation result

Partially useful as a tertiary article; not a core authority.

## Confirmed against better sources

- Edmund/Gurnay, d.1648, son of Henry Gurney and Ellen Blennerhasset.
- Cambridge education and B.D.
- Edgefield then Harpley.
- Anti-Catholic / anti-image works.
- Burial at St Peter Mancroft, Norwich, 14 May 1648.

## Conflicts / quarantined claims

- "Happisburgh" appears to be an error for Edgefield.
- "Sir Robert Barker" as Harpley patron conflicts with Thoms and the Harpley/Yelverton context.
- Ordination specifics are plausible but need CCEd or diocesan confirmation.
```



## Validation checklist

```bash
python -m json.tool data/sources.json >/tmp/sources-json-check.json

grep -R "dnb-edmund-gurney-1890\|ggm-benefice-harpley-rectors\|gurnay-redivivus-1660\|grokipedia-edmund-gurney-divine" -n   data fact-sheets research sources site | head -100
```

Manual review:

- Fact sheet renders all footnotes and return links.
- Birth year appears as c.1577/8, not a false exact date.
- Protestant Gurnay is marked as probable/apparent and date discrepancy is preserved.
- Edgefield is used as the supported 1614 living; Happisburgh is quarantined as a Grokipedia conflict.
- Harpley patron is not changed to Sir Robert Barker without further proof.
- `Gurnay Redivivus` date remains flagged as 1660/1661 discrepancy.
- Grokipedia is catalogued as captured tertiary, not treated as primary evidence.
