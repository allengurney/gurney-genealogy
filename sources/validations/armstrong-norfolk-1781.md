# Validation — Armstrong, History and Antiquities of the County of Norfolk (1781)

Source ID: `armstrong-norfolk-1781`

## Source examined

Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, 10 vols. (Norwich, 1781). Per-volume Internet Archive items at `https://archive.org/details/bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_N/` for N in 1..10.

## Portion examined

Full ten-volume text search for surname variants `Gurney`, `Gourney`, `Gournay`, `Gorney`, `Gurnay`, `Gurnoy`, `Gurnie` against each volume's Internet Archive djvu OCR derivative. 118 hits identified across vols 1, 3, 4, 5, 6, 7, 8, 9, 10 (vol. 2 has no Gurney content). Hits are transcribed in `sources/corpus_supplement/armstrong-norfolk-1781-selected-gurney-references.md`, organised by volume → parish → theme.

Coverage map: vol. 1 = Earsham + Guiltcross + Loddon hundreds (plus Eminent Norfolk Men prefatory matter); vol. 2 = Clavering (no hits); vol. 3 = North Erpingham + Humbleyard; vol. 4 = East Flegg + Clackclose + Forehoe (Hingham, Kimberley); vol. 5 = Freebridge and Half + Gallow; vol. 6 = South Erpingham + Grimshoe + Happing + Brothercross; vol. 7 = Happing + Humbleyard + Heath (Lessingham, Bedingham, Bastwick, Langley priory); vol. 8 = Eynsford + Mitford (Cranworth + Swathing + Letton) + Shropham (Great Ellingham); vol. 9 = Gallow + Smithdon (Hunstanton 1637 Sessions) + Freebridge (Heigham, Drayton, Hellesden, Taverham, Irstead, Merton); vol. 10 = Blofield + Hundred of Norwich (Cathedral cloister; Gournay's Place; Sir Richard Gurney biography).

## Method and limitations

Working from each volume's Internet Archive djvu OCR derivative. Long-s normalized to modern `s`. The OCR carries scattered character errors (e.g., "Govnnty" for "Gourney"; "Folas" for "Joh'is"; "Gurnoy" appearing where "Gourney" was intended). Each Gurney-touching slip is flagged inline in the corpus supplement. No page images were captured into `sources/media/`; if a specific page becomes important for downstream citation work (e.g., the West Barsham chancel monument plate, the Walsingham Parva Sessions order, or the Norwich Cathedral cloister arms list), it can be re-photographed in a future patchset.

Volume-specific OCR / editorial caveats documented in the corpus supplement: vol. 5 "Folas de Gournay" → "Joh'is de Gurnay"; vol. 5 North Barsham "Edw. II." → "Edw. III." (Wauncy transfer); vol. 5 West Barsham "Edmund died seised in 1641" → "Edward" (per chancel monument); vol. 5 pedigree skeleton collapses 1316 brother-Edmund and 1373 West Barsham acquirer-Edmund into one figure; vol. 7 Bedingham "rebellion in 1203" is two years earlier than the standard 1205 reading and is most parsimoniously an Armstrong-side editorial shorthand; vol. 8 Hardingham "Anthony Gurney, esq. was lord in the 26th of Henry III" is anachronistic for an Anthony Gurney and should be read as an Armstrong-side regnal-year error; vol. 8 Great Ellingham "Anthony Gurnay buried in this church in 1557" is one year later than the Blomefield-attested 4 Jan 1555/6 death and is most parsimoniously an Armstrong-side editorial slip or a calendar artefact.

## Substantive findings recorded

- `sources/corpus_supplement/armstrong-norfolk-1781-selected-gurney-references.md` — full transcriptions of all 118 hits with parish + theme context, organized by volume.

Downstream routing to the affected research files is documented in the patchset and deferred to a follow-up patchset because each destination file has its own footnote structure.

## Patchset trail

Prepared in `sources/intake/processed/v69-armstrong-norfolk-1781-vol5-selected-gurney-references.patchset.md`; after application, archived to `sources/intake/done/`. (The file name retains the historical "vol5" suffix from the original single-volume scope; the patchset content covers all ten volumes.)
