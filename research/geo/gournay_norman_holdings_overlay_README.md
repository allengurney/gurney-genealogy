# Gournay Norman Holdings Recommended Overlay

**Created:** 2026-05-07  
**Format:** RFC 7946 GeoJSON (`FeatureCollection`)  
**Coordinate order:** `[longitude, latitude]`  
**Primary file:** `gournay_norman_holdings_recommended_overlay.geojson`
**Website asset:** `site/website/assets/data/gournay-norman-holdings-overlays.geojson`

## Website map implementation

**Implemented:** 2026-05-07

The ancestor map now serves a frontend copy of the recommended overlay package from:

```text
site/website/assets/data/gournay-norman-holdings-overlays.geojson
```

The source-of-truth research artifact remains:

```text
research/geo/gournay_norman_holdings_recommended_overlay.geojson
```

All polygon and line overlay groups are visible by default for initial visual review, including derived buffers and low-confidence context envelopes. This first-pass visibility is intentional so the shapes can be evaluated in Leaflet before later reducing opacity, changing defaults, or hiding lower-confidence layers.

These polygons are interpretive modern-reference approximations, not surveyed medieval cadastral or jurisdictional boundaries. The 24-village / Beauvaisis polygon builds on the existing Hugh de Gournay reconstruction package in `research/geo/Hugh_initial_analysis/hugh_de_gournay_reconstructed_holdings.geojson`.

## Purpose

This dataset is a recommended shaded-region overlay for the Gurney/Gournay genealogy website map. It is designed to visualize the likely geographic footprint and network of the Norman Gournay landholding system without pretending that the reconstructed shapes are surveyed medieval boundaries.

## Design principles

1. Keep source-backed polygons and derived buffers separate.
2. Preserve uncertainty in feature properties.
3. Use low-opacity fills and confidence labels.
4. Do not merge non-contiguous places into a single “lordship boundary” without warning.
5. Treat individual map points as centers or anchors for broader holdings, not as full representations of land.

## Main overlay features

| Feature ID | Purpose | Confidence |
|---|---|---|
| `older_gournay_core_repo` | Existing repo reconstruction of older Gournay core | medium-low |
| `beauvaisis_24_villages_repo` | Existing repo reconstruction of Conquêts Hue de Gournay / 24 villages | medium |
| `beauvaisis_24_villages_expanded_3km` | 3 km expanded buffer around the 24-village polygon | low-medium |
| `gournay_la_ferte_gaillefontaine_frontier_corridor` | Estimated buffered corridor linking Gournay, La Ferté, Gaillefontaine, Sigy, and Fry | low-medium |
| `pays_de_bray_context_envelope` | Broad contextual envelope around the frontier landscape | low |
| `norman_gournay_landholding_network_envelope` | Composite MultiPolygon containing the frontier core, 24 villages, Montigny, and Écouché | low |
| `epte_frontier_line` | Existing repo schematic line for the Epte frontier | low-medium |

## Buffer assumptions

The CSV `gournay_norman_holdings_buffer_assumptions.csv` lists the individual source-point buffers. These are interpretive estimates:

- Gournay-en-Bray: 4 km
- La Ferté: 3 km
- Gaillefontaine: 4 km
- Sigy: 2 km
- Fry: 1.5 km
- Montigny-sur-Andelle: 3 km
- Écouché: 2.5 km

The corridor buffer uses 5 km along the Gournay–La Ferté–Gaillefontaine line and 2.5 km along the Sigy/Fry ecclesiastical spur.

## What this should and should not show

Use the dataset to show:

- the older Gournay frontier core;
- the Beauvaisis / Conquêts Hue de Gournay block;
- a conservative landholding corridor around the best-supported fortress and cadet-line sites;
- separate non-contiguous proof/estate places such as Montigny and Écouché.

Do not use the dataset to claim:

- exact medieval boundaries;
- a complete cadastral reconstruction;
- that all Gournay lands were contiguous;
- that the 24-village polygon captures every surrounding field, pasture, wood, or tithe right.

## Suggested Leaflet rendering

```js
fetch('/assets/data/gournay_norman_holdings_recommended_overlay.geojson')
  .then(response => response.json())
  .then(data => {
    const overlay = L.geoJSON(data, {
      filter: feature => feature.properties.display_default !== false,
      style: feature => feature.properties.style || {
        color: '#7a4b16',
        weight: 2,
        opacity: 0.65,
        fillColor: '#c58a2b',
        fillOpacity: 0.14
      },
      onEachFeature: (feature, layer) => {
        const p = feature.properties || {};
        layer.bindPopup(`
          <strong>${p.name || feature.id}</strong>
          <p><em>Certainty:</em> ${p.certainty || 'unknown'}</p>
          <p>${p.interpretation_note || ''}</p>
        `);
      }
    }).addTo(map);
  });
```

## Source notes

Key public sources used to validate site locations and interpretation:

- Normandie Tourisme and Seine-Maritime Tourisme describe Gournay’s Tour du Rempart as the remaining tower/base/ditches of the medieval fortifications.
- Cirkwi provides a coordinate for Tour du Rempart: `49.48211, 1.72608`.
- Plan du Patrimoine / POP provides the Gaillefontaine coordinate and describes the motte castrale as evidence of the site’s importance on the old Normandy / royal-domain frontier.
- Normandy Abbeys ties Sigy to the lords of La Ferté, descendants of the lords of Gournay.
- Cirkwi provides a coordinate for Sigy’s Abbaye Saint-Martin: `49.5473684, 1.4918346`.
- Projet ConDÉ preserves the customary-law heading for the Conquêts Hue de Gournay / 24 villages.
- RFC 7946 defines GeoJSON geometry types and coordinate order.

## Recommended repository destination

Suggested path after review:

```text
research/geo/gournay_norman_holdings_recommended_overlay.geojson
research/geo/gournay_norman_holdings_buffer_assumptions.csv
research/geo/gournay_norman_holdings_overlay_README.md
```

For website rendering, copy or generate the GeoJSON into:

```text
site/website/assets/data/gournay_norman_holdings_recommended_overlay.geojson
```
