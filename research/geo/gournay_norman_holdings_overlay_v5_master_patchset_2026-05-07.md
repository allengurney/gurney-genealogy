
# Master Patchset — Gournay Norman Holdings Map Overlay v5 Source-Informed

**Repo:** `allengurney/gurney-genealogy`  
**Prepared:** 2026-05-07  
**Purpose:** Consolidated implementation handoff for creating a source-informed GeoJSON overlay package and website map rendering for Gournay Norman holdings, Conquêts Hue de Gournay / 24 villages, Gournay châtellenie dependencies, and related institutional/endowment geography.

This master patchset supersedes the separate discovery addenda for implementation purposes, while preserving them as research-history artifacts.

---

## 1. Inputs consolidated

This master file consolidates:

```text
gournay_polygon_online_source_discovery_2026-05-07.md
gournay_polygon_online_source_discovery_addendum_v2_2026-05-07.md
gournay_polygon_neighboring_communities_addendum_v3_2026-05-07.md
gournay_polygon_outward_neighboring_communities_addendum_v4_2026-05-07.md
gournay_polygon_outward_neighboring_communities_addendum_v5_2026-05-07.md
gournay_norman_holdings_recommended_overlay.geojson
gournay_norman_holdings_buffer_assumptions.csv
gournay_norman_holdings_overlay_README.md
hugh_de_gournay_reconstructed_holdings.geojson
hugh_de_gournay_reconstructed_vertices.csv
hugh_de_gournay_reconstruction_notes.json
hugh_de_gournay_reconstruction_README.md
```

Expected repo source directory:

```text
research/geo/
```

Expected website asset directory to create or update:

```text
site/website/assets/data/
```

---

## 2. Final modeling decision

Do **not** represent all Gournay-related geography as one continuous blob. The evidence supports a layered model:

1. **Direct/core Gournay geography**
   - Gournay-en-Bray.
   - La Ferté.
   - Gaillefontaine.
   - Sigy / Fry ecclesiastical network.
   - Montigny and Écouché as non-contiguous proof/estate places.

2. **Conquêts Hue de Gournay / 24-village block**
   - Customary-law / jurisdictional block beyond the Epte.
   - Source-backed by ConDÉ and local/community sources.
   - Should use a revised source-informed polygon and subcluster anchors.

3. **Gournay châtellenie dependencies**
   - Cuy-Saint-Fiacre / Quesnoy.
   - Avesnes / Ferrières dependency context.
   - These explain the Gournay–Ferrières–Gancourt connective tissue but should not be merged into the Conquêts polygon.

4. **Northern Gournay-honor context**
   - Gaillefontaine / Haucourt / Criquiers / La Montagne.
   - Supported by Bauduin and Gaillefontaine history.
   - Context layer only, not direct G30–G37 polygon.

5. **G33/Bec endowment geography**
   - Massy / Morimont.
   - Brémontier-Merval.
   - Elbeuf-en-Bray.
   - Gournay, La Ferté, Gaillefontaine, Merval, Laudencourt, etc.
   - Property/revenue/endowment geography; visually distinct from direct holdings.

6. **Later Gournay institutional/collateral geography**
   - Bellozanne.
   - Beaubec.
   - Elbeuf / Brémontier-Merval / Merval.
   - Relevant, but default off after visual review.

7. **Boundary-control / negative-control geography**
   - Neuf-Marché / Lyons.
   - Ernemont / Bouchevilliers.
   - Saint-Germer-de-Fly / Puiseux / Saint-Pierre-es-Champs as nearby but not proven Gournay holdings.
   - Helps prevent over-expansion.

---

## 3. Core evidence hierarchy

### 3.1 Highest-authority / controlling sources

Use these as the primary anchors for map claims:

| Source | URL | Use |
|---|---|---|
| Projet ConDÉ 24-village text | https://pdn-lingua.unicaen.fr/coutumiers/conde/pesnelle_lighter.xml/pesnelle-lighter-beta-002-007.html | Controlling source for Conquêts Hue de Gournay list and customary-law framing |
| Ferrières-en-Bray official history | https://www.ferrieres-en-bray.fr/page/la-commune/l-histoire-de-ferrieres/histoire-de-la-ville | Confirms Ferrières, Le Forêt, Hardencourt, Laudencourt in the Conquêts of Hugues de Gournay |
| Gancourt-Saint-Étienne municipal bulletin | https://gancourtsaintetienne.com/wp-content/uploads/2023/12/bm2023-1.pdf | Confirms Gancourt among the twenty-four conquests and under high justice of Gournay |
| Gaillefontaine official history | https://www.mairiegaillefontaine.fr/pages/decouvrir-et-bouger/histoire/historique.html | Confirms Gaillefontaine fortress tradition, motte survival, Gournay/La Ferté connection |
| Pierre Bauduin, Villedieu/Gourchelles/Criquiers | https://shs.cairn.info/revue-histoire-et-societes-rurales-2001-1-page-131?lang=fr | Scholarly source for northern Gournay-honor dependency context |
| Archives 76, Avesnes-en-Bray | https://www.archivesdepartementales76.net/archive/catalogue/communes76/avesnes-en-bray/n%3A168 | Fiefs at Avesnes tied to Ferrières and châtellenie of Gournay |
| Archives 76, Gournay-en-Bray | https://www.archivesdepartementales76.net/archive/catalogue/communes76/gournay-en-bray | Gournay topographic forms, châtellenie references, regional place names |
| Archives 76, Ferrières-en-Bray | https://www.archivesdepartementales76.net/archive/catalogue/communes76/ferrires-en-bray/n%3A168 | Ferrières medieval forms and 1503 châtellenie de Gournay fief language |

### 3.2 Strong secondary / local-history sources

| Source | URL | Use |
|---|---|---|
| Ferrières-en-Bray tourism page | https://tourismedes4rivieresenbray.com/ferrieres-en-bray/ | Confirms Hugues de Gournay seized 24 villages including Ferrières |
| Gancourt local history post | https://gancourtsaintetienne.com/2017/12/21/un-peu-dhistoire-de-notre-village/ | Corroborates Gancourt / Gournay seigneurie relationship |
| Cuy-Saint-Fiacre history | https://fr.wikipedia.org/wiki/Cuy-Saint-Fiacre | Quesnoy full fief of haubert depended on châtellenie of Gournay |
| Cuy-Saint-Fiacre local heritage | https://seine76.fr/communes/communes_result.php?var=CUY-SAINT-FIACRE | Cuy/Quesnoy local heritage and dependency context |
| Elbeuf-en-Bray tourism | https://tourismedes4rivieresenbray.com/elbeuf-en-bray/ | Parish revenues entrusted to Bellozanne in the 12th century |
| Brémontier-Merval official history | https://www.bremontier-merval.fr/vie-culturelle/histoire | Bellozanne / Brémontier / Merval / Elbeuf institutional context |
| Brémontier-Merval geography | https://www.bremontier-merval.fr/situation-geographique | Spatial context for Brémontier-Merval |
| OpenEdition, Neuf-Marché châtellenie | https://books.openedition.org/purh/20171 | Boundary-control source south of Gournay |
| OpenEdition, frontier customs | https://books.openedition.org/purh/6825?lang=en | Broader Norman frontier-custom context |
| OpenEdition, Sigy foundation table | https://books.openedition.org/pur/49267 | Sigy / monastic foundation corroboration |
| Beaubec-la-Rosière locality | https://fr.wikipedia.org/wiki/Beaubec-la-Rosi%C3%A8re | Later Gournay institutional/collateral site |
| Abbaye Notre-Dame de Bellozanne | https://fr.wikipedia.org/wiki/Abbaye_Notre-Dame_de_Bellozanne | Later Gournay institutional/collateral site |

### 3.3 Locator / supporting sources

Use these for coordinates, hameaux, road names, local geography, or place identification. They should not carry major historical claims alone.

```text
https://fr.wikipedia.org/wiki/Saint-Quentin-des-Pr%C3%A9s
https://www.villes-de-france.eu/ville-saint-quentin-des-pres/
https://www.annuaire-mairie.fr/rue-saint-quentin-des-pres.html
https://mapcarta.com/18371570
https://www.france-voyage.com/villes-villages/saint-quentin-des-pres-23044.htm
https://fr.wikipedia.org/wiki/H%C3%A9ricourt-sur-Th%C3%A9rain
https://www.annuaire-mairie.fr/mairie-hericourt-sur-therain.html
https://www.archivesdepartementales76.net/archive/catalogue/communes76/doudeauville/n%3A168
https://fr.wikipedia.org/wiki/Doudeauville_%28Seine-Maritime%29
https://www.france-voyage.com/villes-villages/doudeauville-30210.htm
https://tourismedes4rivieresenbray.com/molagnies/
https://www.archivesdepartementales76.net/archive/catalogue/communes76/molagnies/n%3A168
https://www.france-voyage.com/villes-villages/molagnies-30430.htm
https://www.archivesdepartementales76.net/archive/catalogue/communes76/massy/n%3A168
https://www.archivesdepartementales76.net/archive/catalogue/communes76/esclavelles
https://www.archivesdepartementales76.net/archive/catalogue/communes76/criquiers/n%3A168
https://seine76.fr/communes/communes_result.php?var=CRIQUIERS
https://fr.wikipedia.org/wiki/Criquiers
https://fr.wikipedia.org/wiki/Haucourt_%28Seine-Maritime%29
https://fr.wikipedia.org/wiki/Fontenay-Torcy
https://www.cirkwi.com/de/point-interet/3634214-scea-ferme-de-torchy
https://www.larousse.fr/encyclopedie/ville/Saint-Germer-de-Fly_60850/142355
https://www.banatic.interieur.gouv.fr/commune/60592-Saint-Pierre-es-Champs
https://www.banatic.interieur.gouv.fr/commune/60516-Puiseux-en-Bray
```

---

## 4. Final overlay output files to create

Create these final files:

```text
research/geo/gournay_norman_holdings_recommended_overlay_v5_source_informed.geojson
research/geo/gournay_norman_holdings_overlay_v5_sources.md
research/geo/gournay_norman_holdings_overlay_v5_README.md
research/geo/gournay_norman_holdings_overlay_v5_buffer_assumptions.csv
site/website/assets/data/gournay-norman-holdings-overlays.geojson
```

Optional helper script, if useful:

```text
tools/geo/generate_gournay_holdings_overlay_v5.py
```

The website asset should be a copy or generated derivative of:

```text
research/geo/gournay_norman_holdings_recommended_overlay_v5_source_informed.geojson
```

---

## 5. Required GeoJSON property schema

Every GeoJSON feature should have these properties where applicable:

```json
{
  "id": "",
  "name": "",
  "feature_type": "",
  "display_group": "",
  "display_default": true,
  "certainty": "",
  "historical_basis": "",
  "interpretation_note": "",
  "source_urls": [],
  "buffer_km": null,
  "source_iterations": ["v1", "v2", "v3", "v4", "v5"]
}
```

Optional properties:

```json
{
  "deprecated_by": "",
  "boundary_complexity_note": "",
  "later_continuity_note": "",
  "survival_note": "",
  "unresolved_name": "",
  "possible_associations": [],
  "status": "",
  "display_opacity_hint": ""
}
```

Use GeoJSON coordinate order:

```text
[longitude, latitude]
```

---

## 6. Final feature/layer definitions

### 6.1 Preserve existing older Gournay core

Preserve the existing polygon from:

```text
research/geo/hugh_de_gournay_reconstructed_holdings.geojson
```

Suggested property normalization:

```json
{
  "id": "older_gournay_core_repo",
  "name": "Older Gournay core",
  "feature_type": "reconstructed_polygon",
  "display_group": "older_gournay_core",
  "display_default": true,
  "certainty": "medium-low",
  "historical_basis": "Existing repo reconstruction of the older Gournay core around Gournay-en-Bray and the Epte frontier.",
  "interpretation_note": "Approximate contextual reconstruction, not a surveyed medieval boundary.",
  "source_urls": [
    "research/geo/hugh_de_gournay_reconstructed_holdings.geojson",
    "research/geo/hugh_de_gournay_reconstruction_notes.json"
  ]
}
```

### 6.2 Preserve existing Epte frontier line

Preserve existing Epte line from the repo GeoJSON.

```json
{
  "id": "epte_frontier_line",
  "name": "Schematic Epte frontier line",
  "feature_type": "frontier_line",
  "display_group": "frontier_context",
  "display_default": true,
  "certainty": "low-medium",
  "interpretation_note": "Schematic line for visual frontier context."
}
```

### 6.3 Add revised Conquêts Hue de Gournay / 24-village polygon

This supersedes earlier 24-village polygon attempts.

```json
{
  "type": "Feature",
  "properties": {
    "id": "beauvaisis_24_villages_revised_source_informed_v5",
    "name": "Beauvaisis acquisitions / Conquêts Hue de Gournay — revised source-informed polygon v5",
    "feature_type": "reconstructed_polygon",
    "display_group": "beauvaisis_24_villages",
    "display_default": true,
    "certainty": "medium",
    "source_iterations": ["v1", "v2", "v3", "v4", "v5"],
    "historical_basis": "ConDÉ list; Ferrières official history; Gancourt municipal bulletin/local history; Saint-Quentin/Beaulévrier hameau and later-continuity evidence; Doudeauville Archives 76; Molagnies/Humermont local history; Héricourt locality evidence.",
    "interpretation_note": "Approximate polygon representing a customary-law / jurisdictional block, not a surveyed medieval boundary. It should include the strongest listed-place anchors but not absorb every neighboring Gournay-related institutional or dependency site.",
    "boundary_complexity_note": "Modern boundaries near Doudeauville, Villers-Vermont, Haussez, and Ferme d’Obus preserve irregularities tied to older Bray / Beauvaisis / diocesan geography; polygon remains schematic.",
    "source_urls": [
      "https://pdn-lingua.unicaen.fr/coutumiers/conde/pesnelle_lighter.xml/pesnelle-lighter-beta-002-007.html",
      "https://www.ferrieres-en-bray.fr/page/la-commune/l-histoire-de-ferrieres/histoire-de-la-ville",
      "https://tourismedes4rivieresenbray.com/ferrieres-en-bray/",
      "https://gancourtsaintetienne.com/wp-content/uploads/2023/12/bm2023-1.pdf",
      "https://gancourtsaintetienne.com/2017/12/21/un-peu-dhistoire-de-notre-village/",
      "https://www.archivesdepartementales76.net/archive/catalogue/communes76/doudeauville/n%3A168",
      "https://tourismedes4rivieresenbray.com/molagnies/"
    ]
  },
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [1.704, 49.573],
      [1.708, 49.548],
      [1.722, 49.522],
      [1.748, 49.482],
      [1.755, 49.521],
      [1.790, 49.505],
      [1.872, 49.545],
      [1.846, 49.600],
      [1.761, 49.583],
      [1.704, 49.573]
    ]]
  }
}
```

### 6.4 Deprecate prior 24-village polygon

Do not delete earlier polygon features immediately. Preserve them with:

```json
{
  "display_default": false,
  "deprecated_by": "beauvaisis_24_villages_revised_source_informed_v5",
  "interpretation_note": "Superseded by v5 source-informed polygon because earlier version risked excluding Ferrières-en-Bray, Gancourt-Saint-Étienne, and related listed anchors."
}
```

### 6.5 Add 24-village expanded buffer

Generate a 3 km buffer around `beauvaisis_24_villages_revised_source_informed_v5`.

```json
{
  "id": "beauvaisis_24_villages_expanded_3km_v5",
  "name": "Expanded Conquêts Hue de Gournay / 24-village land context — 3 km buffer",
  "feature_type": "expanded_buffer",
  "display_group": "beauvaisis_24_villages",
  "display_default": true,
  "certainty": "low-medium",
  "buffer_km": 3,
  "historical_basis": "Interpretive buffer around the revised 24-village polygon to acknowledge that listed settlements represent wider village lands, fields, woods, rights, and dependent hameaux.",
  "interpretation_note": "Useful for visualizing likely land around the villages; not a cadastral reconstruction."
}
```

### 6.6 Add 24-village subcluster anchors

Add visible `Point` features. These are anchor/metadata points, not separate canonical polygons.

```json
[
  {
    "id": "ferrieres_auchy_laudencourt_hardencourt_foret_cluster",
    "name": "Ferrières / Auchy / Laudencourt / Hardencourt / Le Forêt cluster",
    "coordinates": [1.745918, 49.48242],
    "certainty": "high",
    "display_group": "beauvaisis_24_villages",
    "historical_basis": "ConDÉ list plus Ferrières official history; modern Ferrières locality/street data preserve Auchy, Laudencourt, Hardencourt, Le Forêt, and related local names.",
    "source_urls": [
      "https://www.ferrieres-en-bray.fr/page/la-commune/l-histoire-de-ferrieres/histoire-de-la-ville",
      "https://tourismedes4rivieresenbray.com/ferrieres-en-bray/",
      "https://www.archivesdepartementales76.net/archive/catalogue/communes76/ferrires-en-bray/n%3A168"
    ]
  },
  {
    "id": "gancourt_boimont_subcluster",
    "name": "Gancourt-Saint-Étienne / Boimont terroir subcluster",
    "coordinates": [1.708, 49.548],
    "certainty": "high",
    "display_group": "beauvaisis_24_villages",
    "historical_basis": "ConDÉ lists Boymont terroir de Ganicourt; Gancourt local history says Gancourt was among the twenty-four conquests and depended on high justice of Gournay.",
    "source_urls": [
      "https://pdn-lingua.unicaen.fr/coutumiers/conde/pesnelle_lighter.xml/pesnelle-lighter-beta-002-007.html",
      "https://gancourtsaintetienne.com/wp-content/uploads/2023/12/bm2023-1.pdf"
    ]
  },
  {
    "id": "saint_quentin_beaulevrier_hincourt_sully_cluster",
    "name": "Saint-Quentin / Beaulévrier / Hincourt / Sully cluster",
    "coordinates": [1.755, 49.5211],
    "certainty": "medium-high",
    "display_group": "beauvaisis_24_villages",
    "historical_basis": "ConDÉ lists S. Quentin and Beaulevrier/Hincourt; modern Saint-Quentin-des-Prés includes Mothois, Hyancourt, Beaulévrier bas, Beaulévrier haut, and Équennes; later local history places Beaulévrier under the comté de Gournay-en-Bray.",
    "later_continuity_note": "Later Beaulévrier / Lignery evidence supports spatial clustering but should not be treated as primary 11th-century proof.",
    "source_urls": [
      "https://pdn-lingua.unicaen.fr/coutumiers/conde/pesnelle_lighter.xml/pesnelle-lighter-beta-002-007.html",
      "https://fr.wikipedia.org/wiki/Saint-Quentin-des-Pr%C3%A9s",
      "https://www.villes-de-france.eu/ville-saint-quentin-des-pres/",
      "https://www.annuaire-mairie.fr/rue-saint-quentin-des-pres.html"
    ]
  },
  {
    "id": "doudeauville_listed_anchor",
    "name": "Doudeauville listed anchor",
    "coordinates": [1.7056, 49.5731],
    "certainty": "medium-high",
    "display_group": "beauvaisis_24_villages",
    "historical_basis": "ConDÉ lists Doudeauville; Archives 76 gives medieval forms including Dudelvilla in 1152 and places Doudeauville in the canton of Gournay-en-Bray.",
    "source_urls": [
      "https://www.archivesdepartementales76.net/archive/catalogue/communes76/doudeauville/n%3A168"
    ]
  },
  {
    "id": "molagnies_humermont_anchor_pair",
    "name": "Molagnies / Humermont anchor pair",
    "coordinates": [1.7218, 49.5217],
    "certainty": "medium-high",
    "display_group": "beauvaisis_24_villages",
    "historical_basis": "ConDÉ lists Moullonguies and Humermont; modern local history identifies Humermont as a Molagnies hameau / church / manorial context.",
    "source_urls": [
      "https://tourismedes4rivieresenbray.com/molagnies/",
      "https://www.archivesdepartementales76.net/archive/catalogue/communes76/molagnies/n%3A168"
    ]
  },
  {
    "id": "hericourt_beaumont_houssoye_subcluster",
    "name": "Héricourt / Beaumont / La Houssoye subcluster",
    "coordinates": [1.7614, 49.5831],
    "certainty": "medium-high",
    "display_group": "beauvaisis_24_villages",
    "historical_basis": "ConDÉ lists Héricourt and the hameaux Beaumont and La Haus-saye. Modern Héricourt-sur-Thérain provides the locality anchor.",
    "source_urls": [
      "https://fr.wikipedia.org/wiki/H%C3%A9ricourt-sur-Th%C3%A9rain",
      "https://www.annuaire-mairie.fr/mairie-hericourt-sur-therain.html"
    ]
  },
  {
    "id": "songeons_loueuse_anchor_pair",
    "name": "Songeons / Loueuse eastern-northeastern anchors",
    "coordinates": [1.85, 49.56],
    "certainty": "medium-high",
    "display_group": "beauvaisis_24_villages",
    "historical_basis": "ConDÉ lists Songeons and Loyenses / Loueuse; these help define the eastern and northeastern edge of the 24-village polygon.",
    "source_urls": [
      "https://pdn-lingua.unicaen.fr/coutumiers/conde/pesnelle_lighter.xml/pesnelle-lighter-beta-002-007.html"
    ]
  }
]
```

### 6.7 Add Cuy-Saint-Fiacre / Quesnoy Gournay dependency

Generate 2.5 km buffer around `[1.6986, 49.5133]`.

```json
{
  "id": "cuy_saint_fiacre_quesnoy_gournay_dependency",
  "name": "Cuy-Saint-Fiacre / Quesnoy Gournay châtellenie dependency",
  "feature_type": "dependency_buffer",
  "certainty": "medium",
  "display_group": "gournay_chatelainie_dependencies",
  "display_default": true,
  "buffer_km": 2.5,
  "coordinates": [1.6986, 49.5133],
  "source_urls": [
    "https://fr.wikipedia.org/wiki/Cuy-Saint-Fiacre",
    "https://seine76.fr/communes/communes_result.php?var=CUY-SAINT-FIACRE"
  ],
  "historical_basis": "A full fief of haubert at Quesnoy depended on the châtellenie of Gournay; the hameau still exists and the parish church has 12th-century context.",
  "interpretation_note": "Connector / dependency feature between the Gournay core and the 24-village edge. Do not merge into the Conquêts polygon."
}
```

### 6.8 Add Avesnes / Ferrières western dependency context

Recommended geometry: buffered corridor or polygon around:
- Gournay-en-Bray `[1.7247, 49.4814]`
- Ferrières-en-Bray `[1.745918, 49.48242]`
- Avesnes-en-Bray `[1.6733, 49.4697]`

Buffer: 2.5 to 3 km around corridor or point union.

```json
{
  "id": "avesnes_ferrieres_gournay_dependency_context",
  "name": "Avesnes / Ferrières Gournay dependency context",
  "feature_type": "dependency_context_buffer",
  "certainty": "low-medium",
  "display_group": "gournay_western_dependency_context",
  "display_default": true,
  "buffer_km": 3,
  "source_urls": [
    "https://www.archivesdepartementales76.net/archive/catalogue/communes76/avesnes-en-bray/n%3A168",
    "https://www.archivesdepartementales76.net/archive/catalogue/communes76/ferrires-en-bray/n%3A168"
  ],
  "historical_basis": "Archives 76 Avesnes topography preserves 1503 fief language tying Avesnes to the full fief of Ferrières and the châtellenie of Gournay.",
  "interpretation_note": "Western dependency context layer, not part of the Conquêts Hue de Gournay polygon."
}
```

### 6.9 Add Gournay–La Ferté–Gaillefontaine direct frontier corridor

Create a corridor/buffer around:
- Gournay-en-Bray `[1.727303, 49.483148]`
- La Ferté-Saint-Samson `[1.527104, 49.57795]`
- Gaillefontaine `[1.62589488664005, 49.650477933144]`
- optional Sigy `[1.491389, 49.547222]`
- optional Fry `[1.526414, 49.530369]`

Recommended buffer:
- corridor buffer 5 km for Gournay–La Ferté–Gaillefontaine;
- smaller spur buffer 2.5 km for La Ferté–Sigy–Fry.

```json
{
  "id": "gournay_la_ferte_gaillefontaine_frontier_corridor",
  "name": "Gournay–La Ferté–Gaillefontaine frontier corridor",
  "feature_type": "frontier_corridor",
  "certainty": "low-medium",
  "display_group": "direct_gournay_frontier_corridor",
  "display_default": true,
  "historical_basis": "Direct fortress / landholding corridor joining the ancestral seat at Gournay, the La Ferté cadet-line locality, and Gaillefontaine from the Orderic triad; Sigy and Fry represent related ecclesiastical endowment geography.",
  "interpretation_note": "Interpretive corridor only, not a continuous surveyed landholding boundary."
}
```

### 6.10 Strengthen Gaillefontaine point/buffer

Generate or retain 4–5 km buffer around Gaillefontaine, but do not merge into northern context without distinct styling.

```json
{
  "id": "gaillefontaine_castle_motte_buffer",
  "name": "Gaillefontaine castle / motte buffer",
  "feature_type": "castle_buffer",
  "certainty": "medium-high",
  "display_group": "direct_gournay_frontier_corridor",
  "display_default": true,
  "buffer_km": 4,
  "coordinates": [1.62589488664005, 49.650477933144],
  "source_urls": [
    "https://www.mairiegaillefontaine.fr/pages/decouvrir-et-bouger/histoire/historique.html",
    "https://www.plan-du-patrimoine.fr/monument-historique/76/gaillefontaine/domaine-de-gaillefontaine/PA00100670/"
  ],
  "historical_basis": "Orderic triad plus Gaillefontaine official history tying Gaillefontaine to Gournay and La Ferté, describing the fortress, visible motte, and 1472 destruction.",
  "survival_note": "Motte remains visible and wooded; fortress itself destroyed/dismantled."
}
```

### 6.11 Add northern Gournay-honor context corridor

Recommended anchor points:
- Gaillefontaine `[1.6259, 49.6505]`
- Haucourt `[1.6606, 49.6414]`
- Criquiers `[1.7067, 49.6753]`
- optional Les Noyers / Gaillefontaine if located later.

Geometry:
- buffered LineString or simple envelope, 4–6 km buffer.
- Very low opacity.

```json
{
  "id": "northern_gournay_honor_context_corridor",
  "name": "Northern Gournay-honor context: Gaillefontaine / Haucourt / Criquiers",
  "feature_type": "context_corridor",
  "certainty": "low-medium",
  "display_group": "northern_gournay_honor_context",
  "display_default": true,
  "buffer_km": 5,
  "source_urls": [
    "https://shs.cairn.info/revue-histoire-et-societes-rurales-2001-1-page-131?lang=fr",
    "https://www.mairiegaillefontaine.fr/pages/decouvrir-et-bouger/histoire/historique.html",
    "https://www.archivesdepartementales76.net/archive/catalogue/communes76/criquiers/n%3A168"
  ],
  "historical_basis": "Bauduin places the Haucourt lineage on lands principally dependent on the honor of Gournay; Haucourt fief depended on Gaillefontaine; Gaillefontaine official history ties fortress and motte to Gournay and La Ferté.",
  "interpretation_note": "Context layer for Gournay honor dependencies and later frontier settlement, not a direct direct-line landholding polygon."
}
```

### 6.12 Add G33 Bec / Gournay endowment layer

Include as optional/low opacity.

Core points:
- Gournay
- La Ferté
- Gaillefontaine
- Brémontier-Merval
- Elbeuf-en-Bray
- Laudencourt / Ferrières cluster
- Massy / Morimont
- possibly Merval / Bosc-Girard / La Rozière as unresolved components.

```json
{
  "id": "g33_bec_gournay_endowment_cluster_envelope",
  "name": "G33 Bec / Gournay endowment cluster envelope",
  "feature_type": "endowment_context_envelope",
  "certainty": "low-medium",
  "display_group": "g33_bec_endowment_cluster",
  "display_default": true,
  "historical_basis": "Hugh III / Basilia Bec donation geography includes churches, tithes, houses, milling rights, and other property/revenue geography across Gournay, Gaillefontaine, La Ferté, Massy/Morimont, Brémontier/Merval, Elbeuf, Laudencourt, and related places.",
  "interpretation_note": "Property/revenue/endowment geography. Keep visually distinct from direct landholding and 24-village layers.",
  "source_urls": [
    "https://www.archivesdepartementales76.net/archive/catalogue/communes76/massy/n%3A168",
    "https://www.archivesdepartementales76.net/archive/catalogue/communes76/esclavelles",
    "https://tourismedes4rivieresenbray.com/elbeuf-en-bray/",
    "https://www.bremontier-merval.fr/vie-culturelle/histoire"
  ]
}
```

### 6.13 Add Massy / Morimont candidate buffer

Generate 3 km buffer around approximate point `[1.399, 49.690]`, unless Codex finds a better source-backed coordinate.

```json
{
  "id": "massy_morimont_bec_endowment_candidate",
  "name": "Massy / Morimont Bec-endowment candidate",
  "feature_type": "candidate_endowment_buffer",
  "certainty": "medium-low",
  "display_group": "g33_bec_endowment_cluster",
  "display_default": true,
  "buffer_km": 3,
  "coordinates": [1.399, 49.690],
  "historical_basis": "Archives 76 Massy topography includes medieval Gurney-linked Massy forms; related research indicates Hugh III benefactions to Bec included the church of Massy.",
  "interpretation_note": "Use as a separate endowment-network overlay. Do not merge into the Conquêts Hue de Gournay polygon.",
  "source_urls": [
    "https://www.archivesdepartementales76.net/archive/catalogue/communes76/massy/n%3A168",
    "https://www.archivesdepartementales76.net/archive/catalogue/communes76/esclavelles"
  ]
}
```

### 6.14 Add later Gournay institutional layer

Default off after review, but initially visible if the user asked to see all polygons first.

```json
{
  "id": "gournay_later_institutional_layer_bellozanne_beaubec",
  "name": "Later Gournay institutional geography: Bellozanne / Beaubec / Elbeuf / Brémontier-Merval",
  "feature_type": "institutional_context_envelope",
  "certainty": "low-medium",
  "display_group": "later_gournay_institutional",
  "display_default": true,
  "future_default_after_review": false,
  "source_urls": [
    "https://fr.wikipedia.org/wiki/Abbaye_Notre-Dame_de_Bellozanne",
    "https://tourismedes4rivieresenbray.com/elbeuf-en-bray/",
    "https://fr.wikipedia.org/wiki/Beaubec-la-Rosi%C3%A8re",
    "https://www.bremontier-merval.fr/vie-culturelle/histoire"
  ],
  "historical_basis": "Bellozanne and Beaubec are later Gournay institutional foundations / patronage sites; Elbeuf-en-Bray and Brémontier-Merval are linked to Bellozanne patronage and administration.",
  "interpretation_note": "Optional institutional / senior-collateral layer. Do not merge into direct G30-G37 holdings or the Conquêts polygon."
}
```

### 6.15 Add southern boundary-control layer

Default off after review. If displayed initially, use very low opacity or point-only markers.

```json
{
  "id": "southern_boundary_context_neuf_marche_lyons",
  "name": "Southern boundary context: Neuf-Marché / Lyons / Saint-Germer-de-Fly",
  "feature_type": "boundary_context",
  "certainty": "medium",
  "display_group": "southern_boundary_context",
  "display_default": true,
  "future_default_after_review": false,
  "source_urls": [
    "https://books.openedition.org/purh/20171",
    "https://www.larousse.fr/encyclopedie/ville/Saint-Germer-de-Fly_60850/142355",
    "https://www.banatic.interieur.gouv.fr/commune/60592-Saint-Pierre-es-Champs",
    "https://www.banatic.interieur.gouv.fr/commune/60516-Puiseux-en-Bray"
  ],
  "historical_basis": "Outward searches south/southeast of Gournay show important neighboring jurisdictions and abbey geography, but no strong direct Gournay holding evidence in this pass.",
  "interpretation_note": "Negative-control / boundary layer to prevent over-expanding the Gournay overlay southward."
}
```

---

## 7. Unresolved ConDÉ names register

Add to README and optionally top-level GeoJSON metadata.

```json
{
  "unresolved_conde_names": [
    {
      "name": "Raincourt",
      "status": "unresolved",
      "notes": "No confident modern identification found. Do not map separately."
    },
    {
      "name": "Royay",
      "status": "unresolved",
      "candidate_forms": ["Rosay", "Rosoy", "Roy-Boissy", "Roye"],
      "notes": "No confident match. Do not map separately. Avoid using distant Roye/Rosoy candidates without stronger evidence."
    },
    {
      "name": "Torchy",
      "status": "unresolved",
      "candidate_forms": ["Torcy", "Torchy"],
      "candidate_leads": [
        "Ferme de Torchy near Cuy-Saint-Fiacre",
        "Fontenay-Torcy / Torchy forms"
      ],
      "notes": "Cirkwi identifies a modern Ferme de Torchy near Cuy, but no direct evidence ties it to the ConDÉ list. Fontenay-Torcy has historical Torchy/Torci forms but is likely too far north/east. Do not map separately yet."
    },
    {
      "name": "Saint-Sanson sous le Rain",
      "status": "unresolved",
      "candidate_forms": [
        "Saint-Samson-la-Poterie",
        "Héricourt-Saint-Samson / Héricourt-sur-Thérain"
      ],
      "notes": "Geographically plausible candidates exist, but no direct source resolves the ConDÉ phrase. Do not map separately yet."
    },
    {
      "name": "Hincourt / Haincourt",
      "status": "partly unresolved",
      "notes": "ConDÉ compression may associate Hincourt with Beaulévrier / Saint-Quentin cluster. Later Beaulévrier grouping includes Haincourt. Track as subcluster note, not separate map point yet."
    }
  ]
}
```

---

## 8. Buffer assumptions

Create or update:

```text
research/geo/gournay_norman_holdings_overlay_v5_buffer_assumptions.csv
```

Recommended rows:

```csv
feature_id,center_or_basis,buffer_km,confidence,notes
beauvaisis_24_villages_expanded_3km_v5,revised 24-village polygon,3,low-medium,Represents village lands / surrounding fields / hameaux beyond listed settlement points
cuy_saint_fiacre_quesnoy_gournay_dependency,Cuy-Saint-Fiacre / Quesnoy,2.5,medium,Dependency connector only; not part of Conquêts polygon
avesnes_ferrieres_gournay_dependency_context,Avesnes-Ferrières-Gournay corridor,3,low-medium,Western dependency context tied to Ferrières and Gournay châtellenie
gournay_la_ferte_gaillefontaine_frontier_corridor,Gournay-La Ferté-Gaillefontaine corridor,5,low-medium,Interpretive corridor around direct fortress / frontier geography
la_ferte_sigy_fry_ecclesiastical_spur,La Ferté-Sigy-Fry,2.5,low-medium,Ecclesiastical/endowment spur from La Ferté
gaillefontaine_castle_motte_buffer,Gaillefontaine castle/motte,4,medium-high,Castle/motte anchor; official history supports motte survival
northern_gournay_honor_context_corridor,Gaillefontaine-Haucourt-Criquiers corridor,5,low-medium,Context layer for northern dependencies of Gournay honor
g33_bec_gournay_endowment_cluster_envelope,G33/Bec donation geography,variable,low-medium,Use envelope or multipolygon around endowment points; keep visually distinct
massy_morimont_bec_endowment_candidate,Massy/Morimont candidate point,3,medium-low,Candidate endowment site; not Conquêts
later_gournay_institutional_layer_bellozanne_beaubec,Bellozanne/Beaubec/Elbeuf/Brémontier-Merval,variable,low-medium,Later/collateral institutional layer; future default off
southern_boundary_context_neuf_marche_lyons,Neuf-Marché/Lyons/Saint-Germer,variable,medium,Boundary-control layer; not holdings
```

---

## 9. Website implementation requirements

### 9.1 Copy final GeoJSON to website asset path

Create/update:

```text
site/website/assets/data/gournay-norman-holdings-overlays.geojson
```

Source:

```text
research/geo/gournay_norman_holdings_recommended_overlay_v5_source_informed.geojson
```

### 9.2 Update Leaflet map rendering

Modify:

```text
site/website/assets/map-page.js
```

Requirements:

1. Fetch `/assets/data/gournay-norman-holdings-overlays.geojson`.
2. Render polygons/lines/points via `L.geoJSON`.
3. Keep overlays visible by default initially.
4. Ensure point markers remain above polygon overlays.
5. Add popup/tooltip data using:
   - `name`
   - `feature_type`
   - `display_group`
   - `certainty`
   - `historical_basis`
   - `interpretation_note`
   - `source_urls`
6. Do not break existing person/property marker rendering.
7. Do not break `?place=` deep links.
8. Add small overlay checkbox control grouped by `display_group`.

### 9.3 Initial display defaults

For initial review, show all major polygons/layers. Suggested initial defaults:

| Layer | Initial display |
|---|---:|
| Older Gournay core | On |
| Gournay–La Ferté–Gaillefontaine frontier corridor | On |
| Revised 24-village polygon | On |
| 24-village expanded buffer | On |
| Subcluster anchors | On |
| Cuy / Quesnoy dependency | On |
| Avesnes / Ferrières western dependency | On |
| Northern Gournay-honor context | On, very low opacity |
| G33/Bec endowment layer | On, very low opacity |
| Massy / Morimont candidate | On, low opacity |
| Later institutional layer | On initially but marked future default off |
| Southern boundary-control layer | On initially but marked future default off |

### 9.4 Post-review likely defaults

After visual inspection, likely turn off by default:

```text
later_gournay_institutional
southern_boundary_context
individual unresolved candidate leads
```

Keep on by default:

```text
older_gournay_core
direct_gournay_frontier_corridor
beauvaisis_24_villages
gournay_chatelainie_dependencies
gournay_western_dependency_context
```

---

## 10. Styling guidance

Use conservative, readable styling.

Suggested style rules:

```text
beauvaisis_24_villages: fillOpacity 0.18, border weight 2
beauvaisis_24_villages expanded buffer: fillOpacity 0.08–0.12, dashed border
direct_gournay_frontier_corridor: fillOpacity 0.10–0.14
older_gournay_core: fillOpacity 0.12–0.16
gournay_chatelainie_dependencies: fillOpacity 0.10
gournay_western_dependency_context: fillOpacity 0.08
northern_gournay_honor_context: fillOpacity 0.05–0.08
g33_bec_endowment_cluster: fillOpacity 0.06–0.08, dashed border
later_gournay_institutional: fillOpacity 0.04–0.06, dashed border
southern_boundary_context: no fill or very low fill; boundary-control styling
frontier lines: dashed line
subcluster anchors: small icon or small circle marker, not visually dominant
```

No need to hard-code exact colors if the existing site style has a palette. If using colors, choose muted earth tones and make sure point markers are legible.

---

## 11. Documentation updates

### 11.1 Create/update README

Create/update:

```text
research/geo/gournay_norman_holdings_overlay_v5_README.md
```

Include:

- purpose;
- layer model;
- source hierarchy;
- buffer assumptions;
- caution that polygons are interpretive, not cadastral;
- explanation that all polygons are initially visible for review;
- post-review default recommendations;
- unresolved names register;
- source register pointer.

### 11.2 Create source register

Create:

```text
research/geo/gournay_norman_holdings_overlay_v5_sources.md
```

Include the source tables from this master patchset.

### 11.3 Update place file

Update:

```text
research/places/beauvaisis-frontier-acquisitions.md
```

Add a concise section:

```md
## Map overlay note

The ancestor map now uses `research/geo/gournay_norman_holdings_recommended_overlay_v5_source_informed.geojson` as the source-informed visual overlay for the Conquêts Hue de Gournay / Beauvaisis frontier acquisitions. The polygon is interpretive and schematic. It is based on the ConDÉ list, the existing repo geo reconstruction, and later online-source review of Ferrières, Gancourt, Saint-Quentin / Beaulévrier, Doudeauville, Molagnies / Humermont, Héricourt, and related neighboring communities. It should not be read as a surveyed medieval boundary.
```

---

## 12. Validation

Run:

```bash
python -m json.tool "research/geo/gournay_norman_holdings_recommended_overlay_v5_source_informed.geojson" > /tmp/gournay_overlay_v5_research.validate
python -m json.tool "site/website/assets/data/gournay-norman-holdings-overlays.geojson" > /tmp/gournay_overlay_v5_site.validate
```

If using a generation script:

```bash
python tools/geo/generate_gournay_holdings_overlay_v5.py
```

Then rerun JSON validation.

Run repo validation/build:

```bash
npm run validate
npm run package
```

If those scripts do not exist, inspect `package.json` and run the appropriate validation/build commands.

Manual browser validation:

- Map loads without console errors.
- Overlay GeoJSON fetch succeeds.
- All major polygons visible initially.
- Point markers remain visible and clickable above polygons.
- Existing person/property filters still work.
- Overlay group checkboxes work.
- `?place=<placeId>` deep links still focus/open correct marker.
- Popups show name, certainty, historical basis, and source links.
- Mobile/narrow layout does not break.

---

## 13. Explicit non-actions

Do **not** map these as independent first-wave polygons or points unless future evidence appears:

| Name | Reason |
|---|---|
| Raincourt | Unresolved |
| Royay | Unresolved; avoid distant Rosoy/Roye guesses |
| Torchy | Unresolved; Ferme de Torchy and Fontenay-Torcy are leads only |
| Saint-Sanson sous le Rain | Unresolved; plausible associations but no direct proof |
| Hincourt / Haincourt | Treat as Saint-Quentin / Beaulévrier cluster note |
| Bosc-Hyons / Boscum Hugonis | Interesting toponymic lead but no Gournay proof |
| Saint-Germer-de-Fly | Boundary/context only |
| Neuf-Marché / Lyons | Boundary/control only |
| Puiseux / Saint-Pierre-es-Champs | Nearby but no Gournay evidence in this pass |
| Beaubec / Bellozanne | Later institutional/collateral layer, not direct G30–G37 holdings |
| Brémontier-Merval / Elbeuf | Institutional/endowment layer, not direct holdings |

---

## 14. Completeness checklist for Codex

Before returning implementation:

- [ ] `research/geo/gournay_norman_holdings_recommended_overlay_v5_source_informed.geojson` exists.
- [ ] `site/website/assets/data/gournay-norman-holdings-overlays.geojson` exists and validates.
- [ ] v5 revised 24-village polygon exists.
- [ ] prior 24-village polygon is preserved/deprecated/off.
- [ ] 3 km expanded 24-village buffer exists.
- [ ] subcluster anchors exist for Ferrières, Gancourt, Saint-Quentin/Beaulévrier, Doudeauville, Molagnies/Humermont, Héricourt, Songeons/Loueuse.
- [ ] Cuy/Quesnoy dependency feature exists.
- [ ] Avesnes/Ferrières dependency context exists.
- [ ] Gournay–La Ferté–Gaillefontaine corridor exists.
- [ ] Gaillefontaine metadata includes official history and motte survival note.
- [ ] Northern Gournay-honor context exists.
- [ ] G33/Bec endowment layer exists.
- [ ] Massy/Morimont candidate exists.
- [ ] Later institutional layer exists and is marked future default off.
- [ ] Southern boundary-control layer exists and is marked future default off.
- [ ] Unresolved names register exists.
- [ ] Source URLs are embedded on relevant features.
- [ ] Map renders polygons/lines/points with Leaflet.
- [ ] Overlay controls work.
- [ ] Existing map point behavior still works.
- [ ] Validation commands pass.

---

## 15. Final implementation recommendation

Implement this as a new branch and one cohesive overlay update. Do **not** incrementally patch the old v1 overlay unless that is the only way to preserve history. The cleanest artifact is a v5 source-informed overlay GeoJSON that supersedes earlier v1/v2/v3/v4 exploratory layers while preserving older features as deprecated/off where useful.

The most important implementation principle: **visual honesty**. The map should show the territorial logic and uncertainty without implying cadastral precision.
