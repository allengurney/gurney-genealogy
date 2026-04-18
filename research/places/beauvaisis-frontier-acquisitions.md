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

## Open items

- [ ] Pull more direct extract material from Decorde's *Essai historique et archéologique sur le Canton de Gournay* into this note or a source extract companion.
- [ ] Identify more of the preserved place-list names against modern communes or hamlets.
- [ ] Replace the schematic Epte line with an actual river polyline if the GIS work is revisited.
- [ ] Consider separate place files only for villages that recur independently elsewhere in the family corpus.

## Sources

- Daniel Gurney, *Record of the House of Gournay*, Part I (1848). [DG-I]
- Abbé J.-E. Decorde, *Essai historique et archéologique sur le Canton de Gournay* (1861), especially the discussion of the **Conquêts Hue de Gournay** and the twenty-four-village list. [Decorde 1861]
- `research/geo/hugh_de_gournay_reconstruction_README.md` [Reconstruction README]
- `research/geo/hugh_de_gournay_reconstruction_notes.json` [Reconstruction notes]

## Crosslinks

- `research/places/gournay-en-bray.md`
- `research/places/normandy.md`
- `research/places/montigny-sur-andelle.md`
