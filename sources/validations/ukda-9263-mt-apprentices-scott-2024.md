# UKDA-SN-9263 — Merchant Taylors' Company of London: Apprentices 1583–1800

Source: Scott, M. (2024), *Merchant Taylors' Company of London: Apprentices 1583–1800* [data collection], UK Data Service, SN 9263, DOI [10.5255/UKDA-SN-9263-1](https://doi.org/10.5255/UKDA-SN-9263-1). Study catalogue page: https://datacatalogue.ukdataservice.ac.uk/studies/study/9263#details. Companion to *The Merchant Taylors Company of London: Apprentices 1583-1800*, British Record Society vols 136–138. Primary records: Guildhall Library Manuscripts Section (binding books and freedom registers of the Merchant Taylors' Company). CC BY-NC-SA 4.0.

## Scope examined
Spreadsheet `merchant_taylors_uk_data_service.xlsx`, all five data sheets in the September 2024 release:

| Sheet | Row count | Function |
|---|---:|---|
| `COMB` | 63,644 | Combined binding records 1583–1800 |
| `Court App` | 330 | Court appearances |
| `Redemptions` | 1,262 | Freedoms by redemption |
| `Patrimony` | 3,391 | Freedoms by patrimony |
| `Freedoms` | 65,392 | Freedom records, projected from the binding side |

All sheets were filtered for surname tokens matching the Gurney variant set (Gurney, Gurnay, Gurnaye, Gourney, Gournay, Gurnee, Gurnie, Gurny, Gerney, Girney, Gyrney, Gurnoe, Gourny, Gourne, Gurne, Gerny, Gerneye, Gourneye, Gurnney, plus "de Gourn-/de Gurn-"). Distinct surnames Gurnell, Gurnett, Gunning, Gerneye, Guernsey, Gorney are not Gurney variants in the Norfolk/Norwich sense and were excluded after inspection.

## Extracts
- `sources/media/ukda-9263-merchant-taylors-apprentices/merchant_taylors_uk_data_service.xlsx` — primary spreadsheet.
- `sources/media/ukda-9263-merchant-taylors-apprentices/9263uguide.pdf` — UK Data Service user guide.
- `sources/media/ukda-9263-merchant-taylors-apprentices/extract_gurney_variants.py` — reproducible filter script.
- `sources/media/ukda-9263-merchant-taylors-apprentices/gurney-variants-extract.csv` — 37 rows surfacing every Gurney-variant occurrence across all five sheets, with full headers.

## Where findings landed
- `research/topics/merchant-taylors-1583-1800-gurney-analysis.md` — substantive analysis, person-by-person, with implications for Candidate B (G13 John Gurney as son of Francis G14).
- Crosslinked update points: `research/people/g14-francis-gurney-fact-sheet.research.md` (Francis G14 own apprenticeship dates, transfer note, Spelman master-apprentice link); `research/case-files/john-gurney-case-file-v4.md` (negative result on a John-son-of-Francis MT binding; reconciliation of the 16 June vs 30 June 1606 freedom date).

## Limits
- The dataset is the published transcription of the Company's binding books and freedom registers; it is not the manuscripts themselves. Where the transcription disagrees with Daniel Gurney's 1858 quotation (notably the freedom date of Francis G14), resolution requires direct examination of the Guildhall MS or of the British Record Society print volumes 136–138.
- Spelling-variant capture relies on the dataset's "Ap Norm" / "Mr Norm" normalised columns when present, plus raw surname columns. Edge spellings (Garney, Gerney as joiner-distinct surnames) are not included by default — they have to be searched separately.
- Place names are recorded as written in the binding book; modern parish identifications (e.g., "Moborne, Worcestershire" → Mowsley Leics. / Morborne Hunts.) are deferred to the analysis file.
