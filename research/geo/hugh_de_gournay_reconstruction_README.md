# Hugh de Gournay III reconstructed holdings data

## Files
- `hugh_de_gournay_reconstructed_holdings.geojson` — reusable geospatial data in WGS84 / EPSG:4326
- `hugh_de_gournay_reconstructed_vertices.csv` — vertex table for quick inspection or import
- `hugh_de_gournay_reconstruction_notes.json` — structured derivation metadata

## What this is
This is an **approximate historical reconstruction** of:
1. the **older Gournay core**
2. the **Beauvaisis acquisitions / "24 villages"**
3. a **schematic Epte frontier line**
4. modern reference points used as anchors

## What it is not
This is **not** a cadastral map, not a surveyed medieval boundary, and not a claim that the polygons match exact medieval extents.

## Derivation logic
The reconstruction was built from:
- secondary historical material describing Hugh's acquisition of **twenty-four parishes/villages in the Beauvaisis**, on the eastern / left-bank side of the Epte
- a later preserved **place-list** associated with the **"Conquêts Hue de Gournay"**
- modern commune locations used as geographic anchors, especially:
  - Gournay-en-Bray
  - Ferrières-en-Bray
  - Molagnies
  - Cuy-Saint-Fiacre
  - Gancourt-Saint-Étienne
  - Saint-Quentin-des-Prés
  - Sully
  - Héricourt-sur-Thérain
  - Songeons
  - Loueuse
  - Beauvais

## Confidence notes
- **Older Gournay core polygon:** lower confidence; more inferential
- **Beauvaisis acquisitions polygon:** somewhat stronger; constrained by the preserved place-list and modern anchor communes
- **Epte line:** schematic only

## Recommended reuse
Suitable for:
- genealogy website maps
- QGIS / ArcGIS import
- Folium / Leaflet web mapping
- further refinement as additional place identifications are confirmed

## Suggested future refinements
- replace the schematic Epte line with an actual river polyline
- identify more of the place-list names against modern communes or hamlets
- split the acquisition block into smaller confidence-ranked subareas
