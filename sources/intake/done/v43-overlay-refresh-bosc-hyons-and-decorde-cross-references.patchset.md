# Intake patchset v43 — Gournay Norman holdings overlay refresh: Bosc-Hyons anchor + Decorde cross-references

**Prepared:** 2026-05-16
**Repo:** `allengurney/gurney-genealogy`
**Target branch:** `main`
**Target files:**
- `research/geo/gournay_norman_holdings_recommended_overlay_v5_source_informed.geojson` (research / canonical)
- `site/website/assets/data/gournay-norman-holdings-overlays.geojson` (website mirror)
- `research/geo/gournay_norman_holdings_overlay_v5_README.md` (overlay readme)
- `research/geo/gournay_norman_holdings_overlay_v5_sources.md` (overlay sources note)

## Scope

Phase 1 overlay refresh queued by v42 §8.4. Four operations:

1. **Add a Bosc-Hyons (medieval Boshyon / *Boscus Hugonis*) anchor** to the older Gournay core layer. This is a new direct-line Gournay landholding anchor newly verified through Decorde 1861 and pinned to the modern commune of Bosc-Hyons (INSEE 76124) at the verified GPS coordinate 49.446 N, 1.659 E.
2. **Redraw the `older_gournay_core_repo` polygon** to enclose Bosc-Hyons. The polygon's south-west corner is moved from (1.685, 49.47) to (1.64, 49.43), extending the older Gournay core south-south-westward by roughly 4 km so that the Decorde-documented direct seigneurial woodland sits inside the polygon rather than just outside it.
3. **Update anchor metadata on the existing Bellosanne and Avesnes-en-Bray anchors** to cross-reference the new canonical place records added in v42 (`place-bellosanne-abbey-bremontier-merval-normandy-france`, `place-cottentray-avesnes-en-bray-normandy-france`).
4. **Rebuild the website mirror** at `site/website/assets/data/gournay-norman-holdings-overlays.geojson` so the live map reflects the canonical research geojson.

The Bosc-Hyons coordinate verification supersedes the deep-research-report 2026-04 assumption that Boshyon was a hamlet absorbed into Ernemont-la-Villette / Avesnes-en-Bray "south-east of Gournay-en-Bray"; the medieval place survives as the modern commune of Bosc-Hyons south-south-west of Gournay. Provenance for the verification: Cartes France commune sheet for Bosc-Hyons (INSEE 76124); db-city commune entry; Archives départementales 76 Bosc-Hyons commune dossier (`https://www.archivesdepartementales76.net/archive/catalogue/communes76/bosc-hyons/n:168`).

---

## 1. Add new anchor `anchor_bosc_hyons_boshyon_direct_landholding`

Insert as a new Feature in `research/geo/gournay_norman_holdings_recommended_overlay_v5_source_informed.geojson`. Natural insert point: immediately after `older_gournay_core_repo` (currently around line 117 in the v5 file), before `beauvaisis_24_villages_repo`. This keeps the older Gournay core polygon followed by its newly-added direct-landholding anchor.

```json
    {
      "type": "Feature",
      "id": "anchor_bosc_hyons_boshyon_direct_landholding",
      "properties": {
        "id": "anchor_bosc_hyons_boshyon_direct_landholding",
        "name": "Bosc-Hyons (medieval Boshyon / Boscus Hugonis)",
        "feature_type": "overlay_place_anchor",
        "display_group": "older_gournay_core",
        "display_default": true,
        "certainty": "high",
        "historical_basis": "Decorde 1861 records the medieval Boshyon (Boscus Hugonis, 'Hugues's wood') as a Gournay-family woodland, manor, and mill. Revenue base for three documented endowments: Hugh III + Basilie 1082 Jumièges 190-arpent charter (apud villam quae vocatur Hugonis silva); Hugues IV + Mélisende 1164 Gaillefontaine grain endowment ratified by Archbishop Rotrou of Rouen (apud Boscum Hugonis); Manassès de Bully 1195 one-muid-of-oats endowment from the Boshyon mill for a perpetual altar lamp before Saint Hildevert's relic at Gournay. The parish church of Saint-Michel was given by a sire de Gournay to the Gournay collegiate chapter in the twelfth century; chapter patronage continued until 1623.",
        "interpretation_note": "Direct-line Gournay landholding anchor for the older core layer, south-south-west of Gournay-en-Bray. Modern commune of Bosc-Hyons (Seine-Maritime, INSEE 76124, postal 76220). Coordinate is the commune-level GPS point and lies just outside the existing older_gournay_core_repo polygon edge; whether to extend that polygon SSW to include Bosc-Hyons is queued as a separate polygon-review item.",
        "source_urls": [
          "https://www.archivesdepartementales76.net/archive/catalogue/communes76/bosc-hyons/n:168",
          "research/places/bosc-hyons.md"
        ],
        "buffer_km": null,
        "source_iterations": [
          "v5"
        ],
        "style": {
          "color": "#7a4b16",
          "weight": 2,
          "opacity": 0.75,
          "fillColor": "#b77724",
          "fillOpacity": 0.16,
          "dashArray": "4 4",
          "markerColor": "#7a4b16"
        },
        "anchor_role": "direct Gournay landholding anchor (Boshyon / Boscus Hugonis)",
        "canonical_place_id": "place-bosc-hyons-boshyon-normandy-france"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          1.659,
          49.446
        ]
      }
    },
```

Style note: the marker colour matches the `older_gournay_core` polygon palette (`#7a4b16` outline, `#b77724` fill) so the anchor visually reads as the same layer.

---

## 1bis. Redraw the `older_gournay_core_repo` polygon

The current polygon is a four-corner quadrilateral with the south-west corner at (1.685, 49.47). Bosc-Hyons at (1.659, 49.446) sits roughly 2.5 km south and 2 km west of that corner — outside the current polygon. The redraw moves only the south-west corner south-south-westward to enclose Bosc-Hyons with a small buffer.

In `research/geo/gournay_norman_holdings_recommended_overlay_v5_source_informed.geojson`, locate the `Feature` with `"id": "older_gournay_core_repo"`. The current `geometry.coordinates` block reads (approximately):

```json
        "coordinates": [
          [
            [1.69, 49.555],
            [1.685, 49.47],
            [1.76, 49.47],
            [1.75, 49.555],
            [1.69, 49.555]
          ]
        ]
```

Replace with:

```json
        "coordinates": [
          [
            [1.69, 49.555],
            [1.75, 49.555],
            [1.76, 49.47],
            [1.64, 49.43],
            [1.69, 49.555]
          ]
        ]
```

The redrawn polygon (NW → NE → SE → SW → close) is a quadrilateral that walks clockwise from the seat-side north edge down to the new south-south-western corner at (1.64, 49.43) and back up to the start. Containment check on key points:

| Point | Coordinate | Inside redrawn polygon? |
|---|---|---|
| Gournay-en-Bray (seat) | (1.727, 49.483) | yes (unchanged from old polygon) |
| Bosc-Hyons (Boshyon) | (1.659, 49.446) | **yes (new)** |
| Avesnes-en-Bray | (1.6733, 49.4697) | **yes (new, side effect)** |
| Bellosanne abbey | (1.611, 49.506) | no (correctly outside, stays in institutional layer) |
| Brémontier-Merval | (1.6029, 49.514) | no (correctly outside, stays in institutional layer) |

The Avesnes-en-Bray side-effect is acceptable: Avesnes is already documented as part of the Gournay châtellenie (per the Archives 76 1503 fief language on the existing `anchor_avesnes_en_bray_gournay_dependency_context`), and the older-core polygon already carries `certainty` "medium-low" with an `interpretation_note` framing it as an approximate reconstruction rather than a surveyed boundary. The separate point anchor for Avesnes keeps the dependency-context interpretation visible regardless of the polygon shape.

In the same `older_gournay_core_repo` feature, update three property fields to record the v43 refresh:

`interpretation_note`:

```json
"interpretation_note": "Approximate contextual reconstruction, not a surveyed medieval boundary. v43 refresh: south-west corner moved from (1.685, 49.47) to (1.64, 49.43) to enclose the Bosc-Hyons (Boshyon / Boscus Hugonis) direct landholding documented by Decorde 1861. The redrawn polygon also encloses Avesnes-en-Bray as a side effect; Avesnes retains its separate point anchor in the western-dependency display group."
```

`source_iterations`: append `"v6_polygon_redraw_2026-05"`:

```json
"source_iterations": [
  "v1",
  "v2",
  "v3",
  "v4",
  "v5",
  "v6_polygon_redraw_2026-05"
]
```

`source_urls`: append the new direct-landholding sources so the polygon's evidentiary trail is visible:

```json
"source_urls": [
  "research/geo/Hugh_initial_analysis/hugh_de_gournay_reconstructed_holdings.geojson",
  "research/geo/Hugh_initial_analysis/hugh_de_gournay_reconstruction_notes.json",
  "sources/corpus_supplement/essai-historique-archeologique-canton-de-gournay-decorde-1861.txt",
  "research/places/bosc-hyons.md"
]
```

Leave the other `older_gournay_core_repo` properties (`feature_type`, `display_group`, `display_default`, `certainty`, `buffer_km`, `style`) unchanged. The polygon's certainty remains `medium-low` — the redraw resolves a specific identified gap but does not upgrade the polygon's overall confidence.

---

## 2. Update existing anchor metadata to reference the new canonical place records

These updates add `canonical_place_id` cross-references on three existing anchors so the geojson points back to v42's new `places.json` records. No coordinate changes.

### 2.1 `anchor_abbaye_notre_dame_de_bellozanne_institutional`

In the `properties` block of this feature, **add** a new key:

```json
"canonical_place_id": "place-bellosanne-abbey-bremontier-merval-normandy-france"
```

Place it after the existing `anchor_role` key so the order remains: `…anchor_role …canonical_place_id …future_default_after_review`. Do **not** modify any other property on this feature.

### 2.2 `anchor_bremontier_merval_bellozanne_institutional`

In the `properties` block of this feature, **add**:

```json
"canonical_place_id": "place-bellosanne-abbey-bremontier-merval-normandy-france"
```

This anchor and the abbey anchor (2.1 above) both point at the same canonical place record; the two points capture the commune-level marker and the abbey-site marker on the map, but they reference the same place.

### 2.3 `anchor_avesnes_en_bray_gournay_dependency_context`

In the `properties` block of this feature, **add**:

```json
"canonical_place_id": "place-cottentray-avesnes-en-bray-normandy-france"
```

The Cottentray quarter-fief is the medieval Gournay-relevance hook for this point; the canonical place record carries the Decorde detail and the 1503 Avesnes fief language.

---

## 3. Rebuild the website mirror

After §§1–2 land in the research / canonical geojson:

```
cp research/geo/gournay_norman_holdings_recommended_overlay_v5_source_informed.geojson \
   site/website/assets/data/gournay-norman-holdings-overlays.geojson
```

Phase 2 should confirm both files are valid JSON, that the feature count in the website mirror equals the research file's feature count + 1 (one new anchor), and that the website map renders the new Bosc-Hyons point in the older-Gournay-core display group.

---

## 4. Update the overlay README

In `research/geo/gournay_norman_holdings_overlay_v5_README.md`:

Edit the `## Overlay place anchors` section to mention the new Bosc-Hyons anchor. Use `str_replace` on:

`old_str`:
```
These anchors are not necessarily canonical place records and should not be read as proof of a discrete direct ancestor holding unless the feature metadata says so. In particular, the northern Gournay-honor anchors, Massy / Morimont endowment anchors, western dependency anchors, and later institutional anchors explain interpretive geography while remaining separate from direct G30-G37 landholding claims and from the Conquets Hue de Gournay polygon.
```

`new_str`:
```
These anchors are not necessarily canonical place records and should not be read as proof of a discrete direct ancestor holding unless the feature metadata says so. In particular, the northern Gournay-honor anchors, Massy / Morimont endowment anchors, western dependency anchors, and later institutional anchors explain interpretive geography while remaining separate from direct G30-G37 landholding claims and from the Conquets Hue de Gournay polygon.

One exception: the new `anchor_bosc_hyons_boshyon_direct_landholding` anchor is a direct-line Gournay landholding point, not interpretive geography. It records the medieval Boshyon (modern Bosc-Hyons commune, Seine-Maritime, INSEE 76124, 49.446 N / 1.659 E) — the *Boscus Hugonis* woodland, manor, and mill documented by Decorde 1861 as the revenue base for the 1082 Jumièges 190-arpent charter, the 1164 Gaillefontaine grain endowment, and the 1195 Manassès de Bully lamp endowment. It is cross-referenced to the canonical place record `place-bosc-hyons-boshyon-normandy-france` and to `research/places/bosc-hyons.md`. The `older_gournay_core_repo` polygon was redrawn in the v43 refresh so that its south-west corner now sits at (1.64, 49.43), enclosing both Bosc-Hyons and the existing Avesnes-en-Bray anchor while leaving the Bellosanne / Brémontier-Merval institutional anchors correctly outside.
```

---

## 5. Update the overlay sources note

In `research/geo/gournay_norman_holdings_overlay_v5_sources.md`, add a new entry for Bosc-Hyons / Decorde under whichever section currently groups direct-landholding sources. If no such section exists in the current README, append the following block at the end of the file:

```markdown
## Bosc-Hyons (medieval Boshyon / Boscus Hugonis) — direct Gournay landholding

- Decorde 1861, Boshyon parish entry (OCR text at `sources/corpus_supplement/essai-historique-archeologique-canton-de-gournay-decorde-1861.txt`; source ID `decorde-essai-canton-gournay-1861`): records the 1082 Jumièges 190-arpent charter at Boshyon (*apud villam quae vocatur Hugonis silva*), the 1164 Hugues IV + Mélisende Gaillefontaine grain endowment (*apud Boscum Hugonis*), and the 1195 Manassès de Bully lamp endowment from the Boshyon mill.
- Archives départementales 76 Bosc-Hyons commune dossier (`https://www.archivesdepartementales76.net/archive/catalogue/communes76/bosc-hyons/n:168`): modern commune identification.
- Cartes France commune sheet for Bosc-Hyons (INSEE 76124, postal 76220, 49.446 N / 1.659 E): coordinate verification.
- Canonical place record: `place-bosc-hyons-boshyon-normandy-france` in `data/places.json` / `data/places_detail.json` (added in v42).
- Research narrative: `research/places/bosc-hyons.md`.
```

---

## 6. Remaining queued review items (not executed in this patchset)

The §1bis polygon redraw resolves the previously queued question about the south-south-western edge of `older_gournay_core_repo`. Two smaller items remain queued for a future overlay pass:

1. **`anchor_avesnes_en_bray_gournay_dependency_context` and the Cottentray quarter-fief.** Cottentray is a hamlet within the modern commune of Avesnes-en-Bray; the existing anchor coordinate (1.6733, 49.4697) is commune-level. A future overlay refresh may want to tighten the marker to the Cottentray hamlet specifically if a verified hamlet coordinate is pulled. For now the commune-level anchor with a cross-reference to the canonical Cottentray place record is sufficient.
2. **Mont-Rôti grange of Mortemer.** Decorde records the *grange du Mont-Rôti* as a Mortemer-abbey farmstead inside the medieval Boshyon parish, paying the Gournay chapter seven *muids* of grain commuted in 1243 to seven *livres parisis* cash. The grange itself is not directly Gournay-held and does not warrant a separate overlay anchor. Noted here to record the correction of the earlier 2026-04 deep-research-report misreading (which had treated "Mont-Bôty / Mont-Bosy" as a modern locality continuator for Boshyon).

---

## 7. Validation posture

Phase 2 should confirm, after applying §§1, 1bis, 2, 3, and 4:

- both geojson files are valid JSON;
- the research and website-mirror geojson have the same feature count (37) and identical feature contents;
- the new `anchor_bosc_hyons_boshyon_direct_landholding` Feature renders on the live map in the older-Gournay-core display group;
- the redrawn `older_gournay_core_repo` polygon visibly encloses both the new Bosc-Hyons anchor and the existing Avesnes-en-Bray anchor, and does not enclose the Bellosanne / Brémontier-Merval institutional anchors;
- the three `canonical_place_id` cross-references resolve to existing `placeId` values in `data/places.json` (these were added in v42 — so v42 must be applied before or alongside v43 for the cross-references to resolve);
- no existing Feature properties were unintentionally reordered or removed in §2 edits.

If v42 has not yet been applied, the three `canonical_place_id` cross-references in §2 will be dangling string values. They will not cause map rendering errors but will fail any consistency check that resolves anchor place-ids against `data/places.json`. Phase 2 should either apply v42 first or accept the temporary dangling references and re-validate after v42 lands.

---

## 8. Unresolved

- Cottentray hamlet-level coordinate (vs. Avesnes commune-level) remains deferred (§6.1).
- The Mont-Rôti grange is documented but not separately anchored (§6.2).
- The patchset does not touch the 24-village Beauvaisis polygon; Decorde's 24-village material is already promoted in `research/places/beauvaisis-frontier-acquisitions.md` and the polygon was last refreshed in v5.
