# FamilySearch browser-link triage - 2026-06-13

Source list: `../13June2026-family-search-browser-links.md`

Scope: page-level FamilySearch record access, source details, image number, DGS, citation, machine transcript, and match snippets. Full-resolution JPGs were downloaded for the leads that looked promising enough for future paleography or image-level review. Machine transcripts are noisy and should not be treated as proof without image reading.

## Captured artefacts

- `records/` - 23 FamilySearch record capture files, one per URL, with URL, ARK, image number, DGS, source details, citation, snippets, and machine transcript.
- `images/` - 13 full-resolution JPGs for selected promising or uncertain leads, including the prior image for item 1.
- `batch-results.json` - structured extraction output for all FamilySearch URLs.

Note: short-lived signed image-download URLs were used during capture and then discarded; the durable artefacts are the JPG files in `images/`.

## Triage table

| # | Disposition | Finding | Captures | Next step |
|---|---|---|---|---|
| 1 | High | `Norfolk. Wills 1599-1601`, DGS `008077025`, image 340. Transcript includes "Anne Gurney my Daughter" in a will context; the entry appears to begin on image 339. | `records/01-norfolk-wills-1599-1601-3Q9M-CSND-LGXV.md`; `images/01-norfolk-wills-1599-1601-3Q9M-CSND-LGXV.jpg`; `images/01a-norfolk-wills-1599-1601-image-339-prior-3Q9M-CSND-LGF9.jpg` | Paleography read images 339-340 together. Identify testator before linking to Henry G15's daughter Anne. |
| 2 | Moderate | `Norwich. Court Records 1636-1646, 1654-1659`, DGS `004397113`, image 275. Transcript has "Fr. Gurney" near Norwich civic/court wording and other names. | `records/02-norwich-court-records-1636-1646-1654-1659-S3HY-6983-5V7.md`; `images/02-norwich-court-records-1636-1646-1654-1659-S3HY-6983-5V7.jpg` | Image read the line before treating "Fr. Gurney" as Francis or a forename abbreviation. |
| 3 | Low | `London. Occupation Records 1620-1645, 1598-1620`, DGS `008960701`, image 271. Transcript is dominated by printed/occupation-title wording; no useful Gurney snippet emerged. | `records/03-london-occupation-records-1620-1645-1598-1620-3QHK-935R-XK6N.md` | Park unless a later film sweep finds a clearer hit. |
| 4 | Moderate, caution | `Costessey. Manorial Records 1633-1635`, DGS `004389191`, image 162. Transcript says "John Gurney rental," but Costessey has known lookalike-name noise. | `records/04-costessey-manorial-records-1633-1635-S3HT-6PN9-SW7.md`; `images/04-costessey-manorial-records-1633-1635-S3HT-6PN9-SW7.jpg` | Paleography check the name and rental context; compare against Jernegan/Gurney false-positive patterns. |
| 5 | Low | `Norfolk/Norwich Court Records 1630-1636`, DGS `004397070`, image 231. No clear Gurney-bearing snippet. | `records/05-norfolk-court-records-1630-1636-norwich-court-records-1630-1636-S3HT-D1H3-5D.md` | Park. |
| 6 | Low-moderate | `Norwich. Deposition Records 1639`, DGS `004389254`, image 318. Transcript has a thin "The Gurney" phrase in word salad. | `records/06-norwich-deposition-records-1639-S3HT-D449-TMQ.md` | Only image-read if a later scoped DGS sweep produces adjacent corroborating hits. |
| 7 | Low | `Norfolk/Norwich Court Records 1630-1636`, DGS `004397070`, image 127. Transcript has "Folk Gurney" in highly corrupted text. | `records/07-norfolk-court-records-1630-1636-norwich-court-records-1630-1636-S3HT-D1H9-G6.md` | Park pending film sweep. |
| 8 | Moderate | `Norfolk/Norwich Court Records 1619-1630`, DGS `004397533`, image 304. Transcript contains a names-list/court snippet with "Noble Gurney" or similar. | `records/08-norfolk-court-records-1619-1630-norwich-court-records-1619-1630-S3HY-DRBW-9S.md`; `images/08-norfolk-court-records-1619-1630-norwich-court-records-1619-1630-S3HY-DRBW-9S.jpg` | Image read the name-list line and determine whether this is a person, place, or OCR artifact. |
| 9 | Low-context | `Bridgewater. Property Settlement Records 1642-1823`, DGS `007009746`, image 62. Linked page is an Ames/Bridgewater narrative page, not a clear Gurney source. | `records/09-bridgewater-property-settlement-records-1642-1823-3QS7-9979-W4CM.md` | If the book matters, run a book-level search for Gurney variants and Abington/Bridgewater terms. |
| 10 | Low-context | `Plymouth Directories / Norfolk-Dedham vital records` mixed image group, DGS `007548965`, image 4. No useful snippet from linked page. | `records/10-plymouth-directories-1884-biographical-sketches-1884-norfolk-birth-rec-3QSQ-G9DX-8TYL.md` | Book/film search only if this source is otherwise important. |
| 11 | Moderate, later American | Suffolk Probate file papers, DGS `105278058`, image 788. Transcript names Nathan Gurney of Boston as administrator of Susanna Richardson's estate. | `records/11-probate-and-family-court-department-file-papers-suffolk-probate-record-3Q9M-C3M9-6935-M.md` | Check whether Nathan belongs to the direct American line or a collateral Boston line before promoting. |
| 12 | Moderate | Braintree vital-record index, DGS `007009769`, image 72. Transcript lists "Gurney John" in an alphabetical name index. | `records/12-braintree-birth-records-1640-1848-marriage-records-1640-1848-death-rec-3QSQ-G979-4W67.md`; `images/12-braintree-birth-records-1640-1848-marriage-records-1640-1848-death-rec-3QSQ-G979-4W67.jpg` | Use as a pointer to the underlying Braintree entries; not itself a proof page. |
| 13 | Moderate orientation only | Burke's *Dictionary of the Landed Gentry* (1858), DGS `008087638`, image 262. Printed Gournay/Gurney pedigree material. | `records/13-burke-s-dictionary-of-the-landed-gentry-united-kingdom-genealogies-185-3Q9M-CSNR-N9WT-7.md`; `images/13-burke-s-dictionary-of-the-landed-gentry-united-kingdom-genealogies-185-3Q9M-CSNR-N9WT-7.jpg` | Treat as tertiary orientation. Trace any claim to Daniel Gurney, Blomefield, HoP, records, or primary material before citing. |
| 14 | Low | United Kingdom/Ireland genealogies 1847, DGS `008881667`, image 273. Hit appears to be Gurdon/Gun rather than Gurney. | `records/14-united-kingdom-genealogies-1847-heraldry-records-1847-ireland-genealog-3QHV-5321-PXP2.md` | Reject unless a broader search proves a real Gurney page nearby. |
| 15 | Moderate | `Norwich. Deeds 1910`, DGS `004389182`, image 45. Index says "Gurnell (orig. written Gurney) Jno." and related Gurnell entries. | `records/15-norwich-deeds-1910-S3HY-6DQ9-HY9.md`; `images/15-norwich-deeds-1910-S3HY-6DQ9-HY9.jpg` | Locate the referenced deed/register pages (e.g. page/folio 139/160) before drawing a genealogical conclusion. |
| 16 | Low | `Norfolk. Wills 1370-1763`, DGS `008085264`, image 800. Linked page is Robert Sayer will/abstract material; no clear Gurney hit in the extracted snippet. | `records/16-norfolk-wills-1370-1763-3Q9M-CSNP-DHNH.md` | Park. |
| 17 | Moderate | `Norwich. Deposition Records 1608`, DGS `004389252`, image 104. Transcript has "said Gurney" in a deposition context. | `records/17-norwich-deposition-records-1608-S3HY-696W-GL6.md`; `images/17-norwich-deposition-records-1608-S3HY-696W-GL6.jpg` | Image read the local clause; deposition context may preserve useful litigation/neighborhood evidence. |
| 18 | Low | `Norwich. Wills 1624-1629, 1638-1639`, DGS `008477113`, image 766. No clear Gurney-bearing snippet. | `records/18-norwich-wills-1626-1629-1624-1625-1638-1639-3Q9M-C39F-R9ZV-4.md` | Park. |
| 19 | Moderate | Suffolk Probate file papers, DGS `102907158`, image 964. Transcript says "John Gurney land" in an inventory/account context, likely American. | `records/19-probate-and-family-court-department-file-papers-suffolk-probate-record-3Q9M-CS6K-NQFW-N.md`; `images/19-probate-and-family-court-department-file-papers-suffolk-probate-record-3Q9M-CS6K-NQFW-N.jpg` | Image read to identify the estate/person and whether this touches John Gurney of Braintree or a collateral. |
| 20 | High | `Norfolk. Wills 1370-1763`, DGS `008480295`, image 149. Abstract for Henry Spelman of St James/Ellingham names "Antony Gurney and John Turrell, executors" with probate in 1524. | `records/20-norfolk-wills-1370-1763-3Q9M-C39V-K2VN.md`; `images/20-norfolk-wills-1370-1763-3Q9M-C39V-K2VN.jpg` | High-value image read and source-trace. Test whether Antony Gurney is G17 or a same-name collateral. |
| 21 | Low | Conway cemetery/gravestone index, DGS `008977901`, image 303. Later American cemetery index with many Gurney names. | `records/21-conway-cemetery-records-gravestone-transcription-records-3QHK-93RK-BXXZ.md` | Park unless a later American-line gap needs Conway cemetery data. |
| 22 | Moderate, needs check | `Suffolk. Deeds 1661-1672`, DGS `007442495`, image 631. User note says 12 June 1668, Richard grantee, John Gurney grantor; extracted snippet did not surface the Gurney line clearly. | `records/22-suffolk-deeds-1661-1672-3QS7-89ZS-BJ35.md`; `images/22-suffolk-deeds-1661-1672-3QS7-89ZS-BJ35.jpg` | Manually inspect the image/index around the date and names; if confirmed, pull the deed page named by the index. |
| 23 | Moderate, uncertain identity | Wills 1660-1661, DGS `008472225`, image 175. Transcript says "James Harney ... son of Isacke Harney of Great Ellingham"; user suspected Gurney. | `records/23-cambridgeshire-wills-1660-1661-suffolk-wills-1660-1661-norfolk-wills-1-3Q9M-C39Z-T9PR-F.md`; `images/23-cambridgeshire-wills-1660-1661-suffolk-wills-1660-1661-norfolk-wills-1-3Q9M-C39Z-T9PR-F.jpg` | Paleography check whether the surname is Harney or Gurney. Great Ellingham makes it worth checking, but do not promote without image confirmation. |

## Non-FamilySearch URLs in the source note

These were not part of the FamilySearch extraction pass and were not captured here:

- Archive.org: `https://archive.org/details/bim_eighteenth-century_catalogue-des-rolles-gas_carte-thomas_1743_2/page/124/mode/2up?q=gourney`
- NRO catalogue: `https://nrocatalogue.norfolk.gov.uk/index.php/gurney-gernays-john-cap-de-lodne-holy-trinity`
- NRO catalogue: `https://nrocatalogue.norfolk.gov.uk/index.php/gurnay-thomas-of-great-ellingham-norfolk`
- NRO catalogue: `https://nrocatalogue.norfolk.gov.uk/index.php/gurney-gurnay-alice-formerly-wife-of-william-gurnay-of-heygham-juxta-norwich`

The NRO catalogue items look potentially valuable as catalogue-level medieval/Norfolk leads and should be checked against existing research/leads before any Phase 1 patchset.

## Recommended next steps

1. Create a small paleography packet for items 1, 20, 22, and 23 first. Item 1 needs images 339-340 read together.
2. Secondary paleography/image review: items 2, 4, 8, 17, and 19.
3. Run scoped FamilySearch Full-Text film sweeps for the higher-value DGS numbers: `008077025`, `008480295`, `008472225`, `007442495`, `004389191`, `004389252`, `004397113`, and `004397533`; use at least `Gurn*`, `Gourn*`, `Garn*`, and targeted terms such as `+Great +Ellingham`, `+Anne +daughter`, `+Antony`, and `+Turrell`.
4. For items 12, 15, and 22, treat the captured page as an index page and pull the underlying entry/deed pages before any research promotion.
5. Check the NRO catalogue links as a separate non-FamilySearch mini-triage.

## Caveats

- The attempted broad film-sweep pass timed out before producing a durable result file. The page-level captures and images above are complete.
- The FamilySearch transcripts are AI-generated and often corrupt. Names, relationships, and dates should be promoted only after image review.
