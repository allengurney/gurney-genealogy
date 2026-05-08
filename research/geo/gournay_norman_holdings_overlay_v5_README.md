# Gournay Norman holdings overlay v5

This package is the source-informed v5 overlay for the ancestor map. It models the early Norman Gournay geography as layered, interpretive context rather than a single continuous estate polygon.

The canonical research GeoJSON is:

- `research/geo/gournay_norman_holdings_recommended_overlay_v5_source_informed.geojson`

The website-facing copy is:

- `site/website/assets/data/gournay-norman-holdings-overlays.geojson`

## Layer model

The overlay deliberately separates:

- older Gournay core around Gournay-en-Bray and the Epte frontier;
- the revised Conquets Hue de Gournay / Beauvaisis 24-village block;
- a 3 km interpretive buffer around that block;
- subcluster anchors for Ferrieres, Gancourt, Saint-Quentin / Beaulevrier, Doudeauville, Molagnies / Humermont, Hericourt, and Songeons / Loueuse;
- Cuy / Quesnoy and Avesnes / Ferrieres dependency context;
- the Gournay-La Ferte-Gaillefontaine direct frontier corridor and La Ferte-Sigy-Fry ecclesiastical spur;
- the northern Gournay-honor context around Gaillefontaine, Haucourt, and Criquiers;
- the G33 Bec / Gournay endowment geography, including Massy / Morimont;
- later institutional context for Bellozanne / Beaubec / Elbeuf / Brémontier-Merval;
- southern boundary-control context around Neuf-Marche / Lyons / Saint-Germer.

## Overlay place anchors

`overlay_place_anchor` features are explanatory map anchors for the interpretive overlay geometry. They make the source-backed reasons for outward corridors, lobes, and dependency fingers visible on the map.

These anchors are not necessarily canonical place records and should not be read as proof of a discrete direct ancestor holding unless the feature metadata says so. In particular, the northern Gournay-honor anchors, Massy / Morimont endowment anchors, western dependency anchors, and later institutional anchors explain interpretive geography while remaining separate from direct G30-G37 landholding claims and from the Conquets Hue de Gournay polygon.

## Later institutional overlay anchors

The Bellozanne / Beaubec / Elbeuf / Brémontier-Merval layer includes explicit patronage-network anchors so the institutional/collateral finger has visible source-backed explanation points:

- Abbaye Notre-Dame de Bellozanne;
- Saint-Lucien;
- Le Thil-Riberpré;
- Beaubec-la-Rosière / Saint-Laurent de Beaubec.

These are institutional/collateral overlay anchors, not direct G30-G37 landholding claims. Riberpré is covered by the Le Thil-Riberpré anchor because the commune-level point and the optional annex point are effectively overlapping at this map scale.

## Interpretation cautions

All polygons are schematic and source-informed. They are not cadastral medieval boundaries, surveyed parish limits, or proof that every enclosed point was held by the same lord at the same date.

The v5 map is meant to make uncertainty visible. Each feature carries `certainty`, `historical_basis`, `interpretation_note`, `source_urls`, and, where relevant, `buffer_km`, `future_default_after_review`, or `deprecated_by` metadata.

## Display defaults

Most major layers remain visible for review, including the overlay place anchors that explain the outward lobes. The southern boundary context layer is now default-off because it served its purpose as a negative-control layer during review.

Current defaults:

- keep visible: older Gournay core, direct frontier corridor, Beauvaisis / 24 villages, Gournay chatellenie dependencies, Avesnes / Ferrieres context;
- available but unchecked by default: southern boundary-control context.

## Source hierarchy

The highest-weight sources are the ConDE 24-village text, Ferrieres official history, Gancourt municipal material, Gaillefontaine official history, Bauduin's northern dependency work, and Archives 76 commune dossiers for Avesnes, Gournay, and Ferrieres.

See `research/geo/gournay_norman_holdings_overlay_v5_sources.md` for the source register and `research/geo/gournay_norman_holdings_overlay_v5_buffer_assumptions.csv` for buffer assumptions.

## Unresolved ConDE names

The following are intentionally not mapped as independent first-wave points:

- Raincourt: unresolved.
- Royay: unresolved; avoid distant Rosoy/Roye/Roy-Boissy candidates without stronger evidence.
- Torchy: unresolved; Ferme de Torchy and Fontenay-Torcy remain leads only.
- Saint-Sanson sous le Rain: unresolved between plausible Saint-Samson / Hericourt-Saint-Samson possibilities.
- Hincourt / Haincourt: treated as a Saint-Quentin / Beaulevrier cluster note, not a separate point.

## Regeneration

Run:

```bash
python tools/geo/generate_gournay_holdings_overlay_v5.py
```

In the Codex Windows environment, use the bundled Python if the system `python` shim is blocked.
