# Beauvaisis frontier acquisitions ("24 villages"), Oise / Pays de Bray

Aggregate research note for the **twenty-four villages / parishes** associated in later tradition with the **conquests of Hugh de Gournay III** on the **Beauvaisis** side of the frontier. This is currently the right level of treatment for the library: the territorial block is historically important, but the evidence does **not** yet justify twenty-four separate place files.

## Why this place note exists

This record captures a **territorial acquisition zone**, not a single manor or village. It belongs in the library because it helps explain the eastward / south-eastward expansion of the Gournay lordship beyond the older Norman-side core around **Gournay-en-Bray**. [DG-I] [Decorde 1861] [Reconstruction README] [Reconstruction notes]

The corresponding GIS work should be treated as a **modern-reference reconstruction for research reuse**, not as a surveyed medieval boundary. The library therefore needs:
- one aggregate historical place note
- the reusable geospatial files
- links outward to any individual villages that later prove important enough to deserve their own place files

## Historical basis

Two strands of evidence underlie the current reconstruction.

### 1. The family-history summary

The project's existing Norman/Gournay work has long treated **Hugh de Gournay III** as having added **twenty-four villages / parishes in the Beauvaisis** on the **left-bank / eastern side of the Epte**. That is the historical proposition the reconstruction is trying to localize geographically. [DG-I] [Reconstruction README]

### 2. The preserved local-history place list

The nineteenth-century local history by **Abbé J.-E. Decorde** is especially valuable because it preserves a later remembered list of the villages attributed to the **Conquêts Hue de Gournay** and says these conquests probably go back to **Hugh III**, who seized the villages and obtained confirmed possession from **Louis VII**. [Decorde 1861]

The place list preserved in that tradition is:

- Auchy
- Beaulevrier
- Beaumont
- Boimont
- Doudeauville
- Ferrières
- Forêt
- Haincourt
- Hardencourt
- Héricourt
- Houssoye
- Humermont
- Hyancourt
- Laudencourt
- Loueuse
- Molagnies
- Mothois
- Renicourt
- Rosay
- Saint-Quentin-des-Prés
- Saint-Samson
- Songeons
- Sully
- Torcy

This list is currently the best preserved historical clue to the territorial block, even though several names still need tighter modern identification. [Decorde 1861]

### Planché / de la Marie wording

Planché preserves a concise label for the acquisition block: certain parishes on the left bank of the Epte, annexed by Hugh de Gournay in the twelfth century, were known as the Conquets Hue de Gournay, citing De la Marie's historical researches. This is not as detailed as Decorde's twenty-four-place list, but it independently supports three elements already used by this file: the left-bank/eastern-Epte orientation, the conquest/acquisition language, and the association with a Hugh de Gournay.[^planche-conquets]

## Geographic interpretation now adopted in the library

The uploaded reconstruction work divides the geography into two main polygons plus a schematic frontier line:

### Older Gournay core
A conservative reconstructed core around:
- Gournay-en-Bray
- Ferrières-en-Bray
- Cuy-Saint-Fiacre

This polygon is explicitly lower-confidence and more inferential, meant to represent the **older hereditary Gournay core** before the Beauvaisis additions. [Reconstruction README] [Reconstruction notes]

### Beauvaisis acquisitions / "24 villages"
A stronger but still approximate polygon east / south-east of Gournay, constrained by the preserved place-list and modern anchor communes including:
- Molagnies
- Saint-Quentin-des-Prés
- Sully
- Héricourt-sur-Thérain
- Songeons
- Loueuse
- Beauvais (orientation city only)

This is best understood as a **compact frontier acquisition block**, not a cadastral boundary and not a claim that the medieval jurisdiction formed one neat modern polygon. [Reconstruction README] [Reconstruction notes]

### Epte frontier line
The current line feature is **schematic only**. It exists to preserve the historical orientation of the expansion — toward the **left bank / eastern side of the Epte** — and should eventually be replaced by a proper river polyline if the map work is revisited. [Reconstruction README] [Reconstruction notes]

## What the current reconstruction does well

The uploaded work gets several important historical-library points right:

- it distinguishes the **older Gournay core** from the **later Beauvaisis-side acquisitions** [Reconstruction README]
- it treats the result as a **frontier block**, which matches the historical logic of a marchland expansion better than a loose honorific label [Reconstruction notes]
- it preserves the place-list and the modern anchor logic so the work can be reused later in GIS, Leaflet, QGIS, or future website maps [Reconstruction README] [Reconstruction notes]

## What the reconstruction does not claim

The reconstruction is **not**:
- a medieval cadastral survey
- an exact jurisdictional polygon
- a claim that every listed place has already been identified with certainty
- a replacement for individual place research where stronger evidence later emerges

That caution is important enough to preserve in the library because it protects the research from becoming more precise than the evidence allows. [Reconstruction README] [Reconstruction notes]

## Reusable research assets now associated with this note

The following files should be treated as the canonical reusable geography package for this topic:

- `research/geo/hugh_de_gournay_reconstruction_README.md`
- `research/geo/hugh_de_gournay_reconstructed_holdings.geojson`
- `research/geo/hugh_de_gournay_reconstruction_notes.json`
- `research/geo/hugh_de_gournay_reconstructed_vertices.csv`

## How this should connect to the rest of the library

This note should be read together with:
- `research/places/gournay-en-bray.md`
- `research/places/normandy.md`

Likely future crosslinks, if more place-specific evidence is developed:
- Ferrières-en-Bray
- Molagnies
- Saint-Quentin-des-Prés
- Songeons
- Loueuse
- Sully
- Héricourt-sur-Thérain

But at present, **one aggregate place note is cleaner than twenty-four thin village stubs**.

## Place-model decision

This file should now be treated as a canonical aggregate place, not only as a research note. The acquisition block is too important to remain outside `data/places.json`, but the individual villages should not all become separate place files until their modern identifications are ranked.

## Legal / customary-law significance

Projet ConDÉ preserves the heading of the local customs for the twenty-four parishes, hamlets, and villages “du ressort de Gournay,” seated beyond the river Epte and called the Conquêts Hue de Gournay and specialties of Beauvaisis. This is valuable because it shows the block was remembered as a jurisdictional / customary-law territory, not merely as a loose genealogical tradition.

The same heading lists the component parishes, hamlets, and villages. This supports the file's current aggregate approach: the block should be a single canonical place record until individual modern identifications are stable.

## Later legal memory

A modern OpenEdition study of Norman frontier customs also treats the Conquêts Hue de Gournay as an example of frontier custom that survived into the later Norman customary-law tradition. It notes that these territories depended on the honor and were situated beyond the Epte in French territory.

This is an important refinement: the Conquêts were not only a medieval military acquisition; they became a durable customary-law geography.

## Geo package now canonical for this place

The following files should be treated as the reusable geography package for the aggregate place:

- `research/geo/hugh_de_gournay_reconstruction_README.md`
- `research/geo/hugh_de_gournay_reconstructed_holdings.geojson`
- `research/geo/hugh_de_gournay_reconstructed_vertices.csv`
- `research/geo/hugh_de_gournay_reconstruction_notes.json`

The GeoJSON includes:
- an “Older Gournay core” polygon with medium-low certainty;
- a “Beauvaisis acquisitions / 24 villages” polygon with medium certainty;
- a schematic Epte frontier line;
- modern anchor / listed-place points for Gournay-en-Bray, Ferrières-en-Bray, Molagnies, Cuy-Saint-Fiacre, Gancourt-Saint-Étienne, Saint-Quentin-des-Prés, Sully, Héricourt-sur-Thérain, Songeons, Loueuse, and Beauvais.

The map coordinate in `data/places.json` is only a low-precision aggregate anchor. Use the GeoJSON polygon for any actual map rendering of the acquisition block.

## Map overlay note

The ancestor map now uses `research/geo/gournay_norman_holdings_recommended_overlay_v5_source_informed.geojson` as the source-informed visual overlay for the Conquêts Hue de Gournay / Beauvaisis frontier acquisitions. The polygon is interpretive and schematic. It is based on the ConDÉ list, the existing repo geo reconstruction, and later online-source review of Ferrières, Gancourt, Saint-Quentin / Beaulévrier, Doudeauville, Molagnies / Humermont, Héricourt, and related neighboring communities. It should not be read as a surveyed medieval boundary.

## Component-place tracking

| Repo normalized name | ConDÉ / early form | GeoJSON / modern-anchor status | Immediate action |
|---|---|---:|---|
| Auchy | Anchy en partie | Listed but not anchor point | Defer |
| Beaulevrier | Beaulevrier | Listed but not anchor point | Defer |
| Beaumont | Beaumont | Listed but not anchor point; within Héricourt parish per ConDÉ | Defer |
| Boimont | Boymont terroir de Ganicourt | Listed; tied to Gancourt territory | Defer |
| Doudeauville | Doudeauville | Listed but not anchor point | Defer |
| Ferrières | Ferriere | High; Ferrières-en-Bray is GeoJSON anchor | Candidate later |
| Forêt | Forest | Listed but not anchor point | Defer |
| Haincourt | Hincourt | Listed but not anchor point | Defer |
| Hardencourt | Hardencourt | Listed but not anchor point | Defer |
| Héricourt | Héricourt | High; Héricourt-sur-Thérain is GeoJSON anchor | Candidate later |
| Houssoye | la Haus-saye | Listed but not anchor point | Defer |
| Humermont | Humermont | Listed but not anchor point | Defer |
| Hyancourt | Iencourt | Listed but not anchor point | Defer |
| Laudencourt | Laudencourt la Forest | Appears also in G33 Bec donation cluster; needs disambiguation | Defer |
| Loueuse | Loyenses | High; Loueuse is GeoJSON anchor | Candidate later |
| Molagnies | Moullonguies | High; Molagnies is GeoJSON anchor | Candidate later |
| Mothois | Monthois | Listed but not anchor point | Defer |
| Renicourt | Raincourt | Listed but not anchor point | Defer |
| Rosay | Royay | Listed but not anchor point | Defer |
| Saint-Quentin-des-Prés | S. Quentin | High; GeoJSON anchor | Candidate later |
| Saint-Samson | Saint-Sanson sous le Rain | Needs disambiguation against La Ferté-Saint-Samson / Saint-Samson-la-Poterie | Defer |
| Songeons | Songeons | High; GeoJSON anchor | Candidate later |
| Sully | Sullys | High; GeoJSON anchor | Candidate later |
| Torcy | Torchy | Listed but not anchor point | Defer |
| Gancourt-Saint-Étienne | Ganicourt | Anchor territory for Boimont | Candidate later |

## Open items

- [ ] Pull more direct extract material from Decorde's *Essai historique et archéologique sur le Canton de Gournay* into this note or a source extract companion.
- [ ] Identify more of the preserved place-list names against modern communes or hamlets.
- [ ] Replace the schematic Epte line with an actual river polyline if the GIS work is revisited.
- [ ] Consider separate place files only for villages that recur independently elsewhere in the family corpus.

## Sources

- Daniel Gurney, *Record of the House of Gournay*, Part I (1848). [DG-I]
- Abbé J.-E. Decorde, *Essai historique et archéologique sur le Canton de Gournay* (1861), especially the discussion of the **Conquêts Hue de Gournay** and the twenty-four-village list. [Decorde 1861]
- J. R. Planché, *The Conqueror and His Companions* (1874), Hugh de Gournay / De la Marie reference. [planche-conqueror-companions-1874]
- `research/geo/hugh_de_gournay_reconstruction_README.md` [Reconstruction README]
- `research/geo/hugh_de_gournay_reconstruction_notes.json` [Reconstruction notes]

## Crosslinks

- `research/places/gournay-en-bray.md`
- `research/places/normandy.md`
- `research/places/montigny-sur-andelle.md`

[^planche-conquets]: J. R. Planché, *The Conqueror and His Companions*, vol. 1 (London: Tinsley Brothers, 1874), Gournay/De la Marie note, 1066.co.nz electronic edition, https://www.1066.co.nz/Mosaic%20DVD/library/conquerorcompanion/companion.htm. Source ID: `planche-conqueror-companions-1874`.

<!-- GENERATED:PLACE-REGISTRY:START -->
## Place registry

- `placeId`: `place-conquets-hue-de-gournay-beauvaisis-france`
- Short description: Aggregate frontier-acquisition block east of the Epte
- Place type: territorial block / aggregate landholding
- Aliases: Conquêts Hue de Gournay, Les Conquêts Hue de Gournay, Beauvaisis frontier acquisitions, 24 villages, twenty-four parishes, twenty-four villages, Conquests of Hugh de Gournay, Specialties of Beauvaisis, Speciautez de Beauvoisis, Vingt quatre Paroisses, Hameaux & Villages, Paroisses au-delà de l'Epte
- Coordinate: 49.5556, 1.7988 (low)
- Roles: landholding / property reference, frontier acquisition, territorial expansion, dual-vassalage context, customary-law geography
- Detail: Aggregate territorial place for the twenty-four parishes, hamlets, and villages beyond the Epte associated with the Conquêts Hue de Gournay. The current library should represent this as one territorial block rather than twenty-four separate records until the individual modern identifications are stable.
- Current-site status: historical territorial block; modern component villages survive in whole or part - Historical territorial block / local customary-law geography. The modern component villages and hamlets survive in whole or part, but the medieval jurisdictional boundary is reconstructed rather than surveyed. Projet ConDÉ preserves the customary-law heading listing the twenty-four parishes, hamlets, and villages beyond the Epte, under the jurisdiction of Gournay, called the Conquêts Hue de Gournay and specialties of Beauvaisis.
- Coordinate basis: approximate centroid of existing repo Beauvaisis-acquisitions reconstruction polygon; use `research/geo/hugh_de_gournay_reconstructed_holdings.geojson` for map polygon
- Links: [Projet ConDÉ: Coutumes et usages des Conquêts Hue de Gournay](https://pdn-lingua.unicaen.fr/coutumiers/conde/pesnelle_lighter.xml/pesnelle-lighter-beta-002-007.html)

### Linked ancestors

- G33 Hugh de Gournay III - traditional acquirer of the 24 villages

### Review notes

- Promote existing research file to canonical place registry.
- Do not create twenty-four thin village records yet.
- Reuse the existing geojson / vertex package.
- Coordinate is an aggregate map anchor, not a medieval cadastral centroid.

<!-- GENERATED:PLACE-REGISTRY:END -->
