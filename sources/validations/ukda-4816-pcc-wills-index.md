# Validation — PCC Wills index, 1384–1858 (UK Data Service SN 4816)

Source ID: `ukda-4816-pcc-wills-index`

## What was examined
The complete deposited index: twenty-four tab-delimited tables covering 1384–1858 plus the
`wills_piece_data` linking table, held locally under
`sources/media/ukda-4816-pcc-wills/_local/`.

The surname field of every will row was matched against forty-seven curated Gurney variant
forms (the Modern, English and Norman families combined, broad setting), and each hit joined
to its `PROB 11` piece reference. Result: 212 testators, plus twenty-nine further rows
excluded because the Gurney form occurs only as a place-name.

## Method
Column-scoped matching rather than whole-row matching, which is what separates the testators
from the place-name rows. The extraction script is kept beside the data
(`extract_gurney_wills.py`) and the full result set as `gurney-variant-hits.tsv`, so the
sweep is reproducible.

Two hits were carried through to the register copies and read in full — PROB 11/188/136 and
PROB 11/303/284, both Gournay of West Barsham. For those two, the index agreed with The
National Archives' catalogue on register name and quire range, which is a useful check that
the extraction is sound.

## What remains unexamined or uncertain
- Thirty-one of the forty-nine pre-1700 wills have never been examined in any form.
- The whole post-1700 set (163 testators) is unexamined apart from four register pieces
  cited elsewhere for other wills.
- The index's place and occupation fields disagree with the repository's earlier scan
  readings for PROB 11/335, PROB 11/241 with PROB 11/242, and PROB 11/252. Neither witness
  has been checked against the register text; the disagreement is recorded, not resolved.
- The index gives no will text. Every substantive reading requires the register copy.

## Access
Safeguarded: UK Data Service registration and End User Licence acceptance are required to
download. The local copy is licence-restricted and gitignored; the folder README records how
to re-obtain it.

## Where findings were recorded
Full testator list, repository-coverage status, and the three index-versus-scan
disagreements: `sources/corpus_supplement/pcc-wills-gurney-variants-1384-1858.md`.

The two West Barsham wills carried through to full transcription are in
`sources/corpus_supplement/tna-pcc-west-barsham-gournay-wills.md` under source
`tna-pcc-west-barsham-gournay-wills`.
