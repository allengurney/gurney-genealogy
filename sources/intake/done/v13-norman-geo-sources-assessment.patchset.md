# v13 Norman geo sources assessment patchset

## Purpose

Assess the online sources collected during the Norman geographic overlay work and identify which sources appear to have research value beyond coordinate or locator support.

This patchset does not apply ancestor/place prose. It records a follow-up path so the geo-only source work can be promoted deliberately.

## Source tracking added

The following bundle source records were added to `data/sources.json`:

- `norman-geo-controlling-sources-2026`
- `norman-geo-archives76-commune-dossiers-2026`
- `norman-geo-local-history-tourism-2026`
- `norman-geo-institutional-localities-2026`
- `norman-geo-locator-saint-quentin-hericourt-2026`
- `norman-geo-locator-criquiers-torchy-2026`
- `norman-geo-locator-southern-boundary-2026`

These bundle records are source-tracking entries for the original web sources used in `research/geo/gournay_norman_holdings_overlay_v5_sources.md`, not for the intermediary overlay files.

## Assessment

### Promote in a later research pass

1. Projet ConDE 24-village text
   - Value: controlling witness for the Conquets Hue de Gournay / 24-village list and customary-law framing.
   - Suggested destination: `research/places/g36-conquets-hue-de-gournay-24-villages.md` or the existing aggregate place file if that is the current canonical location.
   - Suggested sourceId: `norman-geo-controlling-sources-2026`.

2. Ferrieres-en-Bray official history and Ferrieres tourism page
   - Value: local tradition tying Ferrieres, Le Foret, Hardencourt, and Laudencourt to the Conquets of Hugues de Gournay.
   - Suggested destination: aggregate 24-village place note and Ferrieres place note if a distinct note exists.
   - Suggested sourceIds: `norman-geo-controlling-sources-2026`; `norman-geo-local-history-tourism-2026`.

3. Gancourt-Saint-Etienne municipal bulletin and local history post
   - Value: Gancourt among the twenty-four conquests and under high justice of Gournay.
   - Suggested destination: aggregate 24-village place note.
   - Suggested sourceIds: `norman-geo-controlling-sources-2026`; `norman-geo-local-history-tourism-2026`.

4. Gaillefontaine official history and Painchault 2012
   - Value: Gaillefontaine fortress/motte tradition and the Gournay-La Ferte-Gaillefontaine frontier-fortification frame.
   - Suggested destination: Gaillefontaine place note and G32/G36 place context if not already captured.
   - Suggested sourceIds: `norman-geo-controlling-sources-2026`; existing `painchault-gaillefontaine-2012`.

5. Pierre Bauduin article on Villedieu/Gourchelles/Criquiers
   - Value: scholarly support for northern Gournay-honor dependency context.
   - Suggested destination: northern Gournay-honor place/context note.
   - Suggested sourceId: `norman-geo-controlling-sources-2026`.

6. Archives 76 commune dossiers for Avesnes, Gournay, Ferrieres, Massy, Esclavelles, and Criquiers
   - Value: medieval forms, fief language, chatellenie references, and candidate anchors for Morimont/Esclavelles and northern context.
   - Suggested destination: relevant place notes, with care not to overclaim direct ancestor holding from a commune dossier alone.
   - Suggested sourceId: `norman-geo-archives76-commune-dossiers-2026`.

7. OpenEdition Sigy/Beaubec table and Bellozanne benefices note
   - Value: monastic foundation and patronage-network context for Sigy, Beaubec, Bellozanne, Saint-Lucien, Le Thil, and Riberpre.
   - Suggested destination: existing Sigy, Bec/Gournay endowment, Bellozanne, and Beaubec institutional place notes.
   - Suggested sourceIds: `norman-geo-controlling-sources-2026`; `norman-geo-institutional-localities-2026`.

8. Cuy-Saint-Fiacre and Quesnoy sources
   - Value: Quesnoy full fief of haubert dependency on the chatellenie of Gournay.
   - Suggested destination: Cuy/Quesnoy place note or aggregate Gournay chatellenie dependencies note.
   - Suggested sourceId: `norman-geo-local-history-tourism-2026`.

### Keep as geo-only unless later evidence changes

- Saint-Quentin, Hericourt, Doudeauville, Molagnies, Criquiers, Haucourt, Fontenay-Torcy, Torchy, Saint-Germer-de-Fly, Saint-Pierre-es-Champs, and Puiseux-en-Bray locator pages should remain coordinate and place-identification aids unless a future source pass finds actual medieval/Gournay substance on the page.
- BANATIC, Mapcarta, Annuaire-Mairie, France Voyage, and most Wikipedia locality pages should not carry major historical claims by themselves.

## Proposed later patch operations

1. Read the current aggregate 24-village, Gaillefontaine, Sigy, Bec/Gournay endowment, Bellozanne, Beaubec, Cuy/Quesnoy, and northern-honor place files.
2. For each source above, verify the exact passage in the live page or saved extract before adding claims.
3. Add only the historical or interpretive facts, not the map-building mechanics.
4. Cite bundle source IDs in footnotes while preserving enough title/URL detail for the original source inside the note.
5. Keep locator-only pages out of ancestor or place prose unless the claim is specifically about modern identification or coordinates.
