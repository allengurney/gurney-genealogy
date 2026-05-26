# Intake patchset v47 — corpus consolidation and `John-gurney-research-to-be-assessed/` subdirectory cleanup

**Prepared:** 2026-05-18
**Repo:** `allengurney/gurney-genealogy`
**Target branch:** `main`
**Target files:**
- `data/sources.json` — three new source entries; archive-field path updates on four existing sources
- `research/case-files/john-gurney-case-file-v4.md` — n60 expansion; n77 path update; §1 table second-source citation for the Weymouth fine row
- `research/people/g13-john-gurney-fact-sheet.research.md` — Suffolk Deeds footnote path update
- File-system: move six extract files into `sources/corpus_supplement/`; delete one merge-conflict backup file; remove now-empty `John-gurney-research-to-be-assessed/` directory

**Status:** DRAFT — awaiting application.

## Posture

The `research/case-files/John-gurney-research-to-be-assessed/` directory holds eight files. Four of them are extract notes from sources already promoted to `data/sources.json` whose corpus files were never moved into `sources/corpus_supplement/`; their `data/sources.json` archive fields still point at the unmoved location, which makes the source registry technically misaligned with the canonical-source layout. One file is an unresolved Git merge backup whose content is already captured in the G13 research companion. The remaining three contain substantive material that should either be promoted (Porter and Bartlett are new secondary attestations of John at Weymouth / Braintree / Mendon) or fully cited (the TNA probate analysis underwrites the §8 elimination rows currently cited under the catch-all `n60`).

This patchset relocates everything into its correct repo layer, adds the missing source entries, and updates the inbound footnote references. No case-file body prose changes beyond two narrow citation adjustments (n60 expansion and §1 table Weymouth-fine row second-source).

---

## 1. File-system operations

### 1a. Delete merge-conflict backup

```
DELETE: research/case-files/John-gurney-research-to-be-assessed/Two Directory Entries - English emigrants to New England_backup version.md
```

Rationale: file contains unresolved Git merge markers (`<<<<<<< HEAD` … `=======` … `>>>>>>>`) and the two halves are identical content. The Banks 1937 + Anderson 2015 assessments it carries are already fully captured in `research/people/g13-john-gurney-fact-sheet.research.md` under the "External compiler assessments (Anderson, Banks)" section.

### 1b. Move extracts already tied to existing `data/sources.json` source entries

```
MOVE: research/case-files/John-gurney-research-to-be-assessed/deeds and misc/deeds318904_04_john_gurney_extracts.md
  TO: sources/corpus_supplement/suffolk-deeds-liber-iv-1888-gurney-extracts.md

MOVE: research/case-files/John-gurney-research-to-be-assessed/deeds and misc/proprietors_gurney_extracts.md
  TO: sources/corpus_supplement/mendon-proprietors-records-1899-gurney-extracts.md

MOVE: research/case-files/John-gurney-research-to-be-assessed/deeds and misc/milford_john_gurney_extract_pp27_33.md
  TO: sources/corpus_supplement/ballou-history-of-milford-1882-gurney-extracts.md

MOVE: research/case-files/John-gurney-research-to-be-assessed/deeds and misc/john_gurney_extracts_historicalsketch00nash_0.md
  TO: sources/corpus_supplement/nash-historical-sketch-weymouth-1885-gurney-extracts.md
```

### 1c. Move substantive new extracts that need new source entries

```
MOVE: research/case-files/John-gurney-research-to-be-assessed/deeds and misc/porter_gurney_p238_extract.md
  TO: sources/corpus_supplement/porter-genealogy-richard-porter-1878-gurney-extract.md

MOVE: research/case-files/John-gurney-research-to-be-assessed/deeds and misc/john_gurney_bartlett_note.md
  TO: sources/corpus_supplement/bartlett-bartletts-of-weymouth-1892-gurney-extract.md

MOVE: research/case-files/John-gurney-research-to-be-assessed/tna-probate-analysis-john-gurney.md
  TO: sources/corpus_supplement/tna-pcc-gurney-elimination-corpus.md
```

### 1d. Remove now-empty directory

```
RMDIR: research/case-files/John-gurney-research-to-be-assessed/deeds and misc/
RMDIR: research/case-files/John-gurney-research-to-be-assessed/
```

(After 1a–1c, both directories should be empty.)

---

## 2. `data/sources.json` — three new source entries and four archive-field path updates

### 2a. Archive-field updates on existing source entries

For each of these existing sources, change the `archive` field to remove the now-stale `John-gurney-research-to-be-assessed/...` path and point at the new `sources/corpus_supplement/` location. Also add a `corpusPath` entry where one is missing.

**`suffolk-deeds-liber-iv-1888`:**

Old `archive`:
```
"Suffolk County deed-record printed volume; project extraction note at research/case-files/John-gurney-research-to-be-assessed/deeds and misc/deeds318904_04_john_gurney_extracts.md from source filename deeds318904_04.pdf"
```

New `archive`:
```
"Suffolk County deed-record printed volume."
```

Add field:
```json
"corpusPath": "sources/corpus_supplement/suffolk-deeds-liber-iv-1888-gurney-extracts.md",
"corpusStatus": "partial",
```

**`mendon-proprietors-records-1899`:**

Old `archive`:
```
"Internet Archive; OpenLibrary; project extraction note at research/case-files/John-gurney-research-to-be-assessed/deeds and misc/proprietors_gurney_extracts.md"
```

New `archive`:
```
"Internet Archive; OpenLibrary."
```

Add field:
```json
"corpusPath": "sources/corpus_supplement/mendon-proprietors-records-1899-gurney-extracts.md",
"corpusStatus": "partial",
```

**`ballou-history-of-milford-1882`:**

Old `archive`:
```
"Internet Archive; project extraction note at research/case-files/John-gurney-research-to-be-assessed/deeds and misc/milford_john_gurney_extract_pp27_33.md"
```

New `archive`:
```
"Internet Archive."
```

Add field:
```json
"corpusPath": "sources/corpus_supplement/ballou-history-of-milford-1882-gurney-extracts.md",
"corpusStatus": "partial",
```

**`nash-historical-sketch-weymouth-1885`:**

Old `archive`:
```
"Internet Archive; project extraction note at research/case-files/John-gurney-research-to-be-assessed/deeds and misc/john_gurney_extracts_historicalsketch00nash_0.md"
```

New `archive`:
```
"Internet Archive."
```

Add field:
```json
"corpusPath": "sources/corpus_supplement/nash-historical-sketch-weymouth-1885-gurney-extracts.md",
"corpusStatus": "partial",
```

### 2b. Three new source entries

Insert after the `nash-historical-sketch-weymouth-1885` entry (or anywhere in the file consistent with existing ordering):

```json
"porter-genealogy-richard-porter-1878": {
  "shortTitle": "Porter, Genealogy of the Descendants of Richard Porter (1878)",
  "citation": "Porter, Joseph W. A Genealogy of the Descendants of Richard Porter, Who Settled at Weymouth, Mass., 1635, and Allied Families: Also, Some Account of the Descendants of John Porter, Who Settled at Hingham, Mass., 1635, and Salem (Danvers) Mass., 1644. Bangor, [Maine], 1878, p. 225.",
  "archive": "Internet Archive.",
  "url": "https://archive.org/details/genealogyofdesce00port",
  "corpusStatus": "partial",
  "corpusPath": "sources/corpus_supplement/porter-genealogy-richard-porter-1878-gurney-extract.md",
  "mediaPath": null,
  "validationPath": null,
  "notes": "Secondary attestation: places John Gurney at Weymouth on 2 June 1641, when the General Court remitted the fine of John Porter, James Ludden, and John Gurney 'for want of gunpowder.' The author glosses the quoted record 'Ludden and Gurney were of Weymouth.' Independent confirmation alongside MBCR 1:331 of John's June 1641 Weymouth presence."
},
"bartlett-bartletts-of-weymouth-1892": {
  "shortTitle": "Bartlett, The Bartletts of Weymouth (1892)",
  "citation": "Bartlett, Thomas Edward. The Bartletts: Ancestral, Genealogical, Biographical, Historical: Comprising an Account of the American Progenitors of the Bartlett Family, with Special Reference to the Descendants of John Bartlett, of Weymouth and Cumberland. New Haven, Conn.: Press of the Stafford Printing Co., 1892, pp. 14-15.",
  "archive": "Reprint (Provo, Utah: J. Grant Stevenson, 1973).",
  "url": null,
  "corpusStatus": "partial",
  "corpusPath": "sources/corpus_supplement/bartlett-bartletts-of-weymouth-1892-gurney-extract.md",
  "mediaPath": null,
  "validationPath": null,
  "notes": "Secondary attestation: lists John Gurney among the 'first settlers from Braintree' connected with the early Mendon plantation. The passage relates to the 1660 court action on Braintree's petition, the 1662 Indian deed, and the 30 October 1663 order; given the colonial John died early 1663 he probably did not personally remove to Mendon, but is named as part of the Braintree cohort connected with the grant."
},
"tna-pcc-gurney-elimination-corpus": {
  "shortTitle": "TNA PCC Gurney probate corpus (1577-1682, elimination set)",
  "citation": "The National Archives, Kew, Prerogative Court of Canterbury wills and related probate acts referencing Gurney testators or kin 1577-1682: PROB 11/382/271 (John Gurney, merchant, St Botolph without Aldgate, will 23 April 1666); PROB 11/372/123 (John Gurney, yeoman, Winkfield, Berkshire, will 7 November 1682); PROB 11/337/37 (sentence of John Gurney of Aylesbury, Buckinghamshire, later 17th c.); PROB 11/347/122 (Daniell Gurney of Aylesbury, Buckinghamshire, 1669); PROB 11/260/14 (Anne Gurney, widow of Eythorne, Kent, 20 November 1656, probate 1657/8); PROB 11/338/493 (Richard Gurney, labourer of London, 1 March 1674/5); PROB 11/252/319 (John Gurney, yeoman of East Grinstead, 24 February 1654/5); PROB 11/241/246 and PROB 11/242/723 (John Gurney, shepherd, of East Chilton / East Chiltington, Sussex, mid-1650s); PROB 11/252/152 (William Gurney, sons John, Abell, Walter, London, mid-1650s); PROB 11/335/425 (John Gurney, husbandman, of Albury, Hertfordshire, 1676); PROB 11/201/723 (Sir Richard Gurney, knight, mid-17th c.); PROB 11/54/173 (Tobias Gurney and Edward Gurney, 1577).",
  "archive": "The National Archives, Kew (PROB 11 series, registered copy wills).",
  "url": "https://www.nationalarchives.gov.uk/",
  "corpusStatus": "partial",
  "corpusPath": "sources/corpus_supplement/tna-pcc-gurney-elimination-corpus.md",
  "mediaPath": null,
  "validationPath": null,
  "notes": "Eleven PCC wills and two probate acts. Underwrites the case file §8 elimination rows currently cited under footnote n60. Best-effort working analysis of supplied scans, not full diplomatic transcriptions; uncertain readings flagged in the corpus file. Five of the thirteen items (Anne Gurney widow Eythorne 1656; Richard Gurney labourer London 1674/5; Sir Richard Gurney knight; Tobias/Edward Gurney 1577) are not currently cited as standalone §8 rows; they are catalogued in the corpus file as supporting evidence and context."
}
```

---

## 3. Case file footnote and table updates

### 3a. n60 expansion (the catch-all TNA probate footnote)

Current `n60` reads:
```
<li id="n60" value="60">The National Archives, Kew, PCC will and probate-act series 1639-1682 cited under §8 elimination rows: PROB 11/241/246, PROB 11/242/723, PROB 11/252/152, PROB 11/252/319, PROB 11/335/425, PROB 11/337/37, PROB 11/347/122, PROB 11/372/123, PROB 11/382/271. Source ID: <code>tna-probate-records</code>. <a class="backref" href="#ref-60">↩</a> ...</li>
```

(Confirm exact existing text on application; the case file currently lists nine PROB references in n60 without further commentary.)

Replace with:
```html
<li id="n60" value="60">The National Archives, Kew, Prerogative Court of Canterbury wills and probate acts referencing Gurney testators or kin cited under §8 elimination rows: PROB 11/241/246 and PROB 11/242/723 (John Gurney, shepherd, East Chilton/East Chiltington, Sussex, mid-1650s); PROB 11/252/152 (William Gurney, sons John, Abell, Walter, London, mid-1650s); PROB 11/252/319 (John Gurney, yeoman, East Grinstead, 24 February 1654/5); PROB 11/335/425 (John Gurney, husbandman, Albury, Hertfordshire, 1676); PROB 11/337/37 (sentence of John Gurney of Aylesbury, Buckinghamshire, later 17th c.); PROB 11/347/122 (Daniell Gurney of Aylesbury, Buckinghamshire, brother John named, 1669); PROB 11/372/123 (John Gurney, yeoman of Winkfield, Berkshire, will 7 November 1682, wife Ellice/Alice, children including Benjamin, Henry, John, Richard, Mary, and Jonathan); PROB 11/382/271 (John Gurney, merchant, St Botolph without Aldgate, will 23 April 1666, declared "upon my voyage for my Native Country England"). Each item independently anchors a separately documented post-1637 English John Gurney household or family-network reference and cannot be the colonial John of Braintree. Source ID: <code>tna-pcc-gurney-elimination-corpus</code>. <a class="backref" href="#ref-60">↩</a> <a class="backref" href="#ref-60a">back</a> <a class="backref" href="#ref-60b">back</a> <a class="backref" href="#ref-60c">back</a> <a class="backref" href="#ref-60d">back</a> <a class="backref" href="#ref-60e">back</a> <a class="backref" href="#ref-60f">back</a> <a class="backref" href="#ref-60g">back</a></li>
```

(Existing back-refs preserved; the previous sourceId placeholder `tna-probate-records` is updated to the new compliant ID `tna-pcc-gurney-elimination-corpus`.)

### 3b. n77 path update

Current n77 (case file):
```
<li id="n77" value="77">Thomas F. Temple, Register of Deeds, <em>Suffolk Deeds. Liber IV</em> (Boston: Rockwell and Churchill, City Printers, 1888), pp. 6, 89a-90, index p. 150; project extraction note at <code>research/case-files/John-gurney-research-to-be-assessed/deeds and misc/deeds318904_04_john_gurney_extracts.md</code>. Source ID: <code>suffolk-deeds-liber-iv-1888</code>. <a class="backref" href="#ref-77">↩</a></li>
```

Replace path:
```html
<li id="n77" value="77">Thomas F. Temple, Register of Deeds, <em>Suffolk Deeds. Liber IV</em> (Boston: Rockwell and Churchill, City Printers, 1888), pp. 6, 89a-90, index p. 150. Source ID: <code>suffolk-deeds-liber-iv-1888</code>. <a class="backref" href="#ref-77">↩</a></li>
```

(The corpus path now lives in `data/sources.json` `corpusPath` field, not in the body footnote.)

### 3c. §1 table — add Porter as second source for the Weymouth June 1641 fine row

Current row in the §1 facts table:
```
| **First recorded in <br />Colonial America** | June 1641 General Court fine-remission record | MBCR 1:331<sup class="fn"><a href="#n73" id="ref-73">73</a></sup> |
```

Replace right column:
```
| MBCR 1:331; Porter, *Genealogy of the Descendants of Richard Porter* (1878), p. 225<sup class="fn"><a href="#n73" id="ref-73">73</a></sup> <sup class="fn"><a href="#n109" id="ref-109">109</a></sup> |
```

### 3d. New footnote n109

Insert before the closing `</ol>` of the citation index:

```html
<li id="n109" value="109">Joseph W. Porter, <em>A Genealogy of the Descendants of Richard Porter, Who Settled at Weymouth, Mass., 1635, and Allied Families</em> (Bangor [Maine], 1878), p. 225, quoting and glossing the 2 June 1641 General Court fine-remission of John Porter, James Ludden, and John Gurney "for want of gunpowder" with the editorial note "Ludden and Gurney were of Weymouth." Independent secondary attestation of John Gurney at Weymouth in June 1641 alongside the primary record at MBCR 1:331. <a href="https://archive.org/details/genealogyofdesce00port">https://archive.org/details/genealogyofdesce00port</a>. Source ID: <code>porter-genealogy-richard-porter-1878</code>. <a class="backref" href="#ref-109">↩</a></li>
```

---

## 4. G13 research companion footnote path update

In `research/people/g13-john-gurney-fact-sheet.research.md`, footnote currently reads:
```
[^suffolk-deeds-liber-iv]: Thomas F. Temple, Register of Deeds, *Suffolk Deeds. Liber IV* (Boston: Rockwell and Churchill, City Printers, 1888), pp. 6, 89a-90, index p. 150; project extraction note at `research/case-files/John-gurney-research-to-be-assessed/deeds and misc/deeds318904_04_john_gurney_extracts.md`. Source ID: `suffolk-deeds-liber-iv-1888`.
```

Replace:
```
[^suffolk-deeds-liber-iv]: Thomas F. Temple, Register of Deeds, *Suffolk Deeds. Liber IV* (Boston: Rockwell and Churchill, City Printers, 1888), pp. 6, 89a-90, index p. 150. Source ID: `suffolk-deeds-liber-iv-1888`.
```

---

## 5. Pre-apply integrity checks

- `grep -rn "John-gurney-research-to-be-assessed" --include="*.md" --include="*.json" .` should return zero hits after the patchset is applied.
- `ls -la sources/corpus_supplement/ | grep -E "porter-genealogy|bartlett-bartletts|tna-pcc-gurney|suffolk-deeds-liber-iv|mendon-proprietors|ballou-history|nash-historical"` should list all seven moved files.
- `ls research/case-files/John-gurney-research-to-be-assessed/ 2>/dev/null` should return nothing or "No such file or directory."
- `python -c "import json; json.load(open('data/sources.json'))"` should succeed (JSON validity).
- `grep -n "sourceId.*tna-probate-records" .` should return zero (the placeholder sourceId is fully replaced).

## Reviewer checklist

- [ ] One file deleted (`Two Directory Entries...md`), seven files moved into `sources/corpus_supplement/`, directory tree removed
- [ ] Three new source entries inserted in `data/sources.json` with full citation, corpusPath, and notes fields
- [ ] Four existing source entries updated to remove the stale `John-gurney-research-to-be-assessed/...` archive paths and to gain a `corpusPath` pointing at the new corpus_supplement location
- [ ] Case-file n60 expanded with PROB-by-PROB explanation; sourceId updated from `tna-probate-records` to `tna-pcc-gurney-elimination-corpus`
- [ ] Case-file n77 path tidied
- [ ] Case-file §1 table Weymouth-fine row gains Porter 1878 as a second-source citation; new footnote n109 inserted
- [ ] G13 research-notes Suffolk Deeds footnote tidied
- [ ] Integrity checks pass

## Notes for follow-up

- The TNA PCC corpus file at `sources/corpus_supplement/tna-pcc-gurney-elimination-corpus.md` carries five additional probate items (PROB 11/260/14 Anne Gurney widow Eythorne; PROB 11/338/493 Richard Gurney labourer London; PROB 11/201/723 Sir Richard Gurney knight; PROB 11/54/173 Tobias/Edward Gurney 1577; plus the Sussex item already covered) that are not yet promoted to standalone §8 rows. They are catalogued as context and supporting evidence; promotion would be a future targeted patchset if any of them surface as candidate-relevant.
- v48 (London Hearth Tax cluster) and v49 (case-file prose and table pass) follow.
