"""Generate the v5 source-informed Gournay Norman holdings overlay.

The output is intentionally schematic. Coordinates are GeoJSON order:
[longitude, latitude].
"""

from __future__ import annotations

import json
import math
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RESEARCH_OUT = ROOT / "research/geo/gournay_norman_holdings_recommended_overlay_v5_source_informed.geojson"
SITE_OUT = ROOT / "site/website/assets/data/gournay-norman-holdings-overlays.geojson"
SOURCE_OVERLAY = ROOT / "research/geo/gournay_norman_holdings_recommended_overlay.geojson"

SOURCE_ITERATIONS = ["v1", "v2", "v3", "v4", "v5"]


GROUP_STYLES = {
    "older_gournay_core": {
        "color": "#7a4b16",
        "weight": 2,
        "opacity": 0.72,
        "fillColor": "#b77724",
        "fillOpacity": 0.14,
        "dashArray": "4 4",
    },
    "frontier_context": {
        "color": "#44606f",
        "weight": 2,
        "opacity": 0.64,
        "fillOpacity": 0,
        "dashArray": "7 5",
    },
    "beauvaisis_24_villages": {
        "color": "#596f2a",
        "weight": 2,
        "opacity": 0.8,
        "fillColor": "#9ab04a",
        "fillOpacity": 0.16,
    },
    "direct_gournay_frontier_corridor": {
        "color": "#8a4b1e",
        "weight": 2,
        "opacity": 0.68,
        "fillColor": "#c58a2b",
        "fillOpacity": 0.11,
    },
    "gournay_chatelainie_dependencies": {
        "color": "#76518c",
        "weight": 2,
        "opacity": 0.64,
        "fillColor": "#8f6aa5",
        "fillOpacity": 0.1,
    },
    "gournay_western_dependency_context": {
        "color": "#6b5a2a",
        "weight": 2,
        "opacity": 0.58,
        "fillColor": "#b7a15a",
        "fillOpacity": 0.08,
        "dashArray": "6 4",
    },
    "northern_gournay_honor_context": {
        "color": "#446b58",
        "weight": 2,
        "opacity": 0.5,
        "fillColor": "#6d9a81",
        "fillOpacity": 0.06,
        "dashArray": "6 5",
    },
    "g33_bec_endowment_cluster": {
        "color": "#7a5963",
        "weight": 2,
        "opacity": 0.52,
        "fillColor": "#b17b86",
        "fillOpacity": 0.065,
        "dashArray": "5 5",
    },
    "later_gournay_institutional": {
        "color": "#5b6f78",
        "weight": 2,
        "opacity": 0.48,
        "fillColor": "#8ba5ad",
        "fillOpacity": 0.05,
        "dashArray": "4 6",
    },
    "southern_boundary_context": {
        "color": "#6b6670",
        "weight": 2,
        "opacity": 0.48,
        "fillColor": "#aaa6af",
        "fillOpacity": 0.035,
        "dashArray": "2 7",
    },
}


def load_source_features() -> dict[str, dict]:
    with SOURCE_OVERLAY.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return {feature.get("id") or feature.get("properties", {}).get("id"): feature for feature in data["features"]}


def km_per_degree_lon(lat: float) -> float:
    return 111.32 * math.cos(math.radians(lat))


def lonlat_to_xy(point: list[float], origin: list[float]) -> tuple[float, float]:
    lon, lat = point
    olon, olat = origin
    return ((lon - olon) * km_per_degree_lon(olat), (lat - olat) * 111.32)


def xy_to_lonlat(point: tuple[float, float], origin: list[float]) -> list[float]:
    x, y = point
    olon, olat = origin
    return [round(olon + x / km_per_degree_lon(olat), 6), round(olat + y / 111.32, 6)]


def centroid(points: list[list[float]]) -> list[float]:
    if points[0] == points[-1]:
        points = points[:-1]
    return [
        sum(point[0] for point in points) / len(points),
        sum(point[1] for point in points) / len(points),
    ]


def circle(center: list[float], radius_km: float, steps: int = 48) -> list[list[float]]:
    coords = []
    for idx in range(steps):
        angle = (math.tau * idx) / steps
        x = math.cos(angle) * radius_km
        y = math.sin(angle) * radius_km
        coords.append(xy_to_lonlat((x, y), center))
    coords.append(coords[0])
    return coords


def multipoint_buffers(points: list[list[float]], radius_km: float) -> list[list[list[list[float]]]]:
    return [[circle(point, radius_km)] for point in points]


def radial_expand_polygon(ring: list[list[float]], radius_km: float) -> list[list[float]]:
    origin = centroid(ring)
    expanded = []
    source_ring = ring[:-1] if ring[0] == ring[-1] else ring
    for point in source_ring:
        x, y = lonlat_to_xy(point, origin)
        distance = math.hypot(x, y)
        if distance == 0:
            expanded.append(point)
            continue
        scale = (distance + radius_km) / distance
        expanded.append(xy_to_lonlat((x * scale, y * scale), origin))
    expanded.append(expanded[0])
    return expanded


def convex_hull(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    unique = sorted(set(points))
    if len(unique) <= 1:
        return unique

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for point in unique:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)

    upper = []
    for point in reversed(unique):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)

    return lower[:-1] + upper[:-1]


def buffered_hull(points: list[list[float]], radius_km: float, samples: int = 32) -> list[list[float]]:
    origin = centroid(points)
    cloud = []
    for point in points:
        px, py = lonlat_to_xy(point, origin)
        for idx in range(samples):
            angle = (math.tau * idx) / samples
            cloud.append((round(px + math.cos(angle) * radius_km, 6), round(py + math.sin(angle) * radius_km, 6)))
    hull = [xy_to_lonlat(point, origin) for point in convex_hull(cloud)]
    hull.append(hull[0])
    return hull


def style_for(group: str, overrides: dict | None = None) -> dict:
    style = dict(GROUP_STYLES[group])
    if overrides:
        style.update(overrides)
    return style


def feature(
    feature_id: str,
    name: str,
    feature_type: str,
    display_group: str,
    geometry: dict,
    certainty: str,
    historical_basis: str,
    interpretation_note: str,
    source_urls: list[str] | None = None,
    display_default: bool = True,
    buffer_km: float | int | str | None = None,
    style: dict | None = None,
    **extra,
) -> dict:
    properties = {
        "id": feature_id,
        "name": name,
        "feature_type": feature_type,
        "display_group": display_group,
        "display_default": display_default,
        "certainty": certainty,
        "historical_basis": historical_basis,
        "interpretation_note": interpretation_note,
        "source_urls": source_urls or [],
        "buffer_km": buffer_km,
        "source_iterations": SOURCE_ITERATIONS,
        "style": style or style_for(display_group),
    }
    properties.update(extra)
    return {
        "type": "Feature",
        "id": feature_id,
        "properties": properties,
        "geometry": geometry,
    }


def normalized_existing(source: dict, group: str, **props) -> dict:
    source_props = dict(source.get("properties", {}))
    feature_id = source.get("id") or source_props.get("id")
    name = props.pop("name", source_props.get("name", feature_id))
    feature_type = props.pop("feature_type", source_props.get("feature_type", "reconstructed_polygon"))
    certainty = props.pop("certainty", source_props.get("certainty", "low-medium"))
    historical_basis = props.pop("historical_basis", source_props.get("historical_basis", "Existing repo overlay feature."))
    interpretation_note = props.pop(
        "interpretation_note",
        source_props.get("interpretation_note", "Approximate interpretive feature; not a surveyed medieval boundary."),
    )
    return feature(
        feature_id,
        name,
        feature_type,
        group,
        source["geometry"],
        certainty,
        historical_basis,
        interpretation_note,
        source_urls=props.pop("source_urls", source_props.get("source_urls", [])),
        display_default=props.pop("display_default", source_props.get("display_default", True)),
        buffer_km=props.pop("buffer_km", source_props.get("buffer_km")),
        style=props.pop("style", style_for(group, source_props.get("style", {}))),
        **props,
    )


def main() -> None:
    source = load_source_features()
    revised_ring = [
        [1.704, 49.573],
        [1.708, 49.548],
        [1.722, 49.522],
        [1.748, 49.482],
        [1.755, 49.521],
        [1.790, 49.505],
        [1.872, 49.545],
        [1.846, 49.600],
        [1.761, 49.583],
        [1.704, 49.573],
    ]

    features = [
        normalized_existing(
            source["older_gournay_core_repo"],
            "older_gournay_core",
            name="Older Gournay core",
            source_urls=[
                "research/geo/Hugh_initial_analysis/hugh_de_gournay_reconstructed_holdings.geojson",
                "research/geo/Hugh_initial_analysis/hugh_de_gournay_reconstruction_notes.json",
            ],
            historical_basis="Existing repo reconstruction of the older Gournay core around Gournay-en-Bray and the Epte frontier.",
            interpretation_note="Approximate contextual reconstruction, not a surveyed medieval boundary.",
        ),
        normalized_existing(
            source["beauvaisis_24_villages_repo"],
            "beauvaisis_24_villages",
            display_default=False,
            deprecated_by="beauvaisis_24_villages_revised_source_informed_v5",
            status="deprecated",
            style=style_for("beauvaisis_24_villages", {"fillOpacity": 0.04, "dashArray": "3 6"}),
            interpretation_note="Superseded by v5 source-informed polygon because the earlier version risked excluding Ferrieres-en-Bray, Gancourt-Saint-Etienne, and related listed anchors.",
        ),
        normalized_existing(
            source["epte_frontier_line"],
            "frontier_context",
            name="Schematic Epte frontier line",
            feature_type="frontier_line",
            interpretation_note="Schematic line for visual frontier context.",
            style=style_for("frontier_context"),
        ),
        feature(
            "beauvaisis_24_villages_revised_source_informed_v5",
            "Beauvaisis acquisitions / Conquets Hue de Gournay - revised source-informed polygon v5",
            "reconstructed_polygon",
            "beauvaisis_24_villages",
            {"type": "Polygon", "coordinates": [revised_ring]},
            "medium",
            "ConDE list; Ferrieres official history; Gancourt municipal bulletin/local history; Saint-Quentin/Beaulevrier hameau and later-continuity evidence; Doudeauville Archives 76; Molagnies/Humermont local history; Hericourt locality evidence.",
            "Approximate polygon representing a customary-law / jurisdictional block, not a surveyed medieval boundary. It includes the strongest listed-place anchors without absorbing every neighboring Gournay-related institutional or dependency site.",
            [
                "https://pdn-lingua.unicaen.fr/coutumiers/conde/pesnelle_lighter.xml/pesnelle-lighter-beta-002-007.html",
                "https://www.ferrieres-en-bray.fr/page/la-commune/l-histoire-de-ferrieres/histoire-de-la-ville",
                "https://tourismedes4rivieresenbray.com/ferrieres-en-bray/",
                "https://gancourtsaintetienne.com/wp-content/uploads/2023/12/bm2023-1.pdf",
                "https://gancourtsaintetienne.com/2017/12/21/un-peu-dhistoire-de-notre-village/",
                "https://www.archivesdepartementales76.net/archive/catalogue/communes76/doudeauville/n%3A168",
                "https://tourismedes4rivieresenbray.com/molagnies/",
            ],
            boundary_complexity_note="Modern boundaries near Doudeauville, Villers-Vermont, Haussez, and Ferme d'Obus preserve irregularities tied to older Bray / Beauvaisis / diocesan geography; polygon remains schematic.",
        ),
        feature(
            "beauvaisis_24_villages_expanded_3km_v5",
            "Expanded Conquets Hue de Gournay / 24-village land context - 3 km buffer",
            "expanded_buffer",
            "beauvaisis_24_villages",
            {"type": "Polygon", "coordinates": [radial_expand_polygon(revised_ring, 3)]},
            "low-medium",
            "Interpretive buffer around the revised 24-village polygon to acknowledge that listed settlements represent wider village lands, fields, woods, rights, and dependent hameaux.",
            "Useful for visualizing likely land around the villages; not a cadastral reconstruction.",
            [
                "https://pdn-lingua.unicaen.fr/coutumiers/conde/pesnelle_lighter.xml/pesnelle-lighter-beta-002-007.html",
            ],
            buffer_km=3,
            style=style_for("beauvaisis_24_villages", {"fillOpacity": 0.09, "weight": 1, "dashArray": "6 4"}),
        ),
    ]

    subclusters = [
        (
            "ferrieres_auchy_laudencourt_hardencourt_foret_cluster",
            "Ferrieres / Auchy / Laudencourt / Hardencourt / Le Foret cluster",
            [1.745918, 49.48242],
            "high",
            "ConDE list plus Ferrieres official history; modern Ferrieres locality/street data preserve Auchy, Laudencourt, Hardencourt, Le Foret, and related local names.",
            [
                "https://www.ferrieres-en-bray.fr/page/la-commune/l-histoire-de-ferrieres/histoire-de-la-ville",
                "https://tourismedes4rivieresenbray.com/ferrieres-en-bray/",
                "https://www.archivesdepartementales76.net/archive/catalogue/communes76/ferrires-en-bray/n%3A168",
            ],
        ),
        (
            "gancourt_boimont_subcluster",
            "Gancourt-Saint-Etienne / Boimont terroir subcluster",
            [1.708, 49.548],
            "high",
            "ConDE lists Boymont terroir de Ganicourt; Gancourt local history says Gancourt was among the twenty-four conquests and depended on high justice of Gournay.",
            [
                "https://pdn-lingua.unicaen.fr/coutumiers/conde/pesnelle_lighter.xml/pesnelle-lighter-beta-002-007.html",
                "https://gancourtsaintetienne.com/wp-content/uploads/2023/12/bm2023-1.pdf",
            ],
        ),
        (
            "saint_quentin_beaulevrier_hincourt_sully_cluster",
            "Saint-Quentin / Beaulevrier / Hincourt / Sully cluster",
            [1.755, 49.5211],
            "medium-high",
            "ConDE lists S. Quentin and Beaulevrier/Hincourt; modern Saint-Quentin-des-Pres includes Mothois, Hyancourt, Beaulevrier bas, Beaulevrier haut, and Equennes; later local history places Beaulevrier under the comte de Gournay-en-Bray.",
            [
                "https://pdn-lingua.unicaen.fr/coutumiers/conde/pesnelle_lighter.xml/pesnelle-lighter-beta-002-007.html",
                "https://fr.wikipedia.org/wiki/Saint-Quentin-des-Pr%C3%A9s",
                "https://www.villes-de-france.eu/ville-saint-quentin-des-pres/",
                "https://www.annuaire-mairie.fr/rue-saint-quentin-des-pres.html",
            ],
        ),
        (
            "doudeauville_listed_anchor",
            "Doudeauville listed anchor",
            [1.7056, 49.5731],
            "medium-high",
            "ConDE lists Doudeauville; Archives 76 gives medieval forms including Dudelvilla in 1152 and places Doudeauville in the canton of Gournay-en-Bray.",
            ["https://www.archivesdepartementales76.net/archive/catalogue/communes76/doudeauville/n%3A168"],
        ),
        (
            "molagnies_humermont_anchor_pair",
            "Molagnies / Humermont anchor pair",
            [1.7218, 49.5217],
            "medium-high",
            "ConDE lists Moullonguies and Humermont; modern local history identifies Humermont as a Molagnies hameau / church / manorial context.",
            [
                "https://tourismedes4rivieresenbray.com/molagnies/",
                "https://www.archivesdepartementales76.net/archive/catalogue/communes76/molagnies/n%3A168",
            ],
        ),
        (
            "hericourt_beaumont_houssoye_subcluster",
            "Hericourt / Beaumont / La Houssoye subcluster",
            [1.7614, 49.5831],
            "medium-high",
            "ConDE lists Hericourt and the hameaux Beaumont and La Haus-saye. Modern Hericourt-sur-Therain provides the locality anchor.",
            [
                "https://fr.wikipedia.org/wiki/H%C3%A9ricourt-sur-Th%C3%A9rain",
                "https://www.annuaire-mairie.fr/mairie-hericourt-sur-therain.html",
            ],
        ),
        (
            "songeons_loueuse_anchor_pair",
            "Songeons / Loueuse eastern-northeastern anchors",
            [1.85, 49.56],
            "medium-high",
            "ConDE lists Songeons and Loyenses / Loueuse; these help define the eastern and northeastern edge of the 24-village polygon.",
            [
                "https://pdn-lingua.unicaen.fr/coutumiers/conde/pesnelle_lighter.xml/pesnelle-lighter-beta-002-007.html",
            ],
        ),
    ]
    for item_id, name, point, certainty, basis, urls in subclusters:
        features.append(
            feature(
                item_id,
                name,
                "subcluster_anchor",
                "beauvaisis_24_villages",
                {"type": "Point", "coordinates": point},
                certainty,
                basis,
                "Anchor/metadata point only; do not read as a separate surveyed polygon.",
                urls,
                style=style_for("beauvaisis_24_villages", {"markerColor": "#596f2a"}),
            )
        )

    overlay_place_anchors = [
        (
            "anchor_haucourt_northern_gournay_honor_context",
            "Haucourt",
            "northern_gournay_honor_context",
            [1.6606, 49.6414],
            "medium",
            "northern Gournay-honor dependency context",
            "Pierre Bauduin places the Haucourt lineage on lands principally dependent on the honor of Gournay and describes Haucourt's fief as dependent on Gaillefontaine.",
            "Anchor point explaining the northern Gournay-honor context corridor. This is contextual dependency geography, not a direct G30-G37 landholding point.",
            ["https://shs.cairn.info/revue-histoire-et-societes-rurales-2001-1-page-131?lang=fr"],
            {},
        ),
        (
            "anchor_les_noyers_gaillefontaine_vavassory",
            "Les Noyers / Gaillefontaine vavassory",
            "northern_gournay_honor_context",
            [1.6259, 49.6505],
            "medium-low",
            "Gournay-honor dependency / vavassory context",
            "Bauduin notes a vavassory at Les Noyers on the present commune of Gaillefontaine held from the lord of Gournay.",
            "Use as an explanatory anchor for the northern context corridor. Refine coordinate if a stronger Les Noyers-specific point is found.",
            [
                "https://shs.cairn.info/revue-histoire-et-societes-rurales-2001-1-page-131?lang=fr",
                "https://www.mairiegaillefontaine.fr/pages/decouvrir-et-bouger/histoire/historique.html",
            ],
            {"coordinate_precision": "approximate"},
        ),
        (
            "anchor_criquiers_northern_gournay_honor_context",
            "Criquiers",
            "northern_gournay_honor_context",
            [1.7067, 49.6753],
            "medium-low",
            "northern frontier / institutional context",
            "Criquiers belongs to the northern La Montagne / Gaillefontaine / Haucourt context discussed by Bauduin and appears in Archives 76 topography.",
            "Context anchor for the northern corridor. Do not treat as a direct G30-G37 holding.",
            [
                "https://shs.cairn.info/revue-histoire-et-societes-rurales-2001-1-page-131?lang=fr",
                "https://www.archivesdepartementales76.net/archive/catalogue/communes76/criquiers/n%3A168",
            ],
            {},
        ),
        (
            "anchor_massy_bec_endowment_candidate",
            "Massy",
            "g33_bec_endowment_cluster",
            [1.399, 49.690],
            "medium",
            "Bec / Gournay endowment candidate",
            "Archives 76 Massy topography includes medieval Gurney-linked Massy forms, tithe/church/fief language, and later châtellenie de La Ferté-en-Bray references.",
            "Anchor point explaining the Massy / Morimont Bec-endowment candidate lobe. Do not merge into the Conquets Hue de Gournay polygon.",
            ["https://www.archivesdepartementales76.net/archive/catalogue/communes76/massy/n%3A168"],
            {},
        ),
        (
            "anchor_morimont_esclavelles_bec_endowment_candidate",
            "Morimont / Esclavelles",
            "g33_bec_endowment_cluster",
            [1.405, 49.705],
            "medium-low",
            "Massy / Morimont endowment context",
            "Archives 76 Esclavelles topography anchors Morimont / Mont-Remond across Esclavelles and Massy.",
            "Candidate/context anchor for the Massy-Morimont endowment lobe. Refine coordinate if a precise Morimont point is found.",
            ["https://www.archivesdepartementales76.net/archive/catalogue/communes76/esclavelles"],
            {"coordinate_precision": "approximate"},
        ),
        (
            "anchor_avesnes_en_bray_gournay_dependency_context",
            "Avesnes-en-Bray",
            "gournay_western_dependency_context",
            [1.6733, 49.4697],
            "medium-high",
            "western Gournay dependency context",
            "Archives 76 Avesnes-en-Bray topography preserves 1503 fief language tying Avesnes to the full fief of Ferrières and the châtellenie of Gournay.",
            "Anchor point explaining the Avesnes / Ferrieres western dependency context. This should remain separate from the Conquets Hue de Gournay polygon.",
            ["https://www.archivesdepartementales76.net/archive/catalogue/communes76/avesnes-en-bray/n%3A168"],
            {},
        ),
        (
            "anchor_bremontier_merval_bellozanne_institutional",
            "Brémontier-Merval / Bellozanne",
            "later_gournay_institutional",
            [1.6029, 49.514],
            "medium",
            "later Gournay institutional geography",
            "Brémontier-Merval official history ties Bellozanne to Hugues V de Gournay and to the later administration of Bellozanne, Brémontier, Merval, and Elbeuf-en-Bray.",
            "Institutional / senior-collateral Gournay geography. Keep separate from direct G30-G37 holdings and the Conquets polygon.",
            [
                "https://www.bremontier-merval.fr/vie-culturelle/histoire",
                "https://fr.wikipedia.org/wiki/Abbaye_Notre-Dame_de_Bellozanne",
            ],
            {"future_default_after_review": False},
        ),
        (
            "anchor_abbaye_notre_dame_de_bellozanne_institutional",
            "Abbaye Notre-Dame de Bellozanne",
            "later_gournay_institutional",
            [1.611111, 49.505556],
            "high",
            "Bellozanne institutional foundation and patronage center",
            "Bellozanne was founded in 1198 by Hugues V de Gournay and had patronage over several parishes, including Brémontier/Merval, Elbeuf-en-Bray, Saint-Lucien, Le Thil, and Riberpré.",
            "Institutional / senior-collateral Gournay geography. This is the central anchor for the Bellozanne patronage finger, not a direct G30-G37 landholding point.",
            [
                "https://fr.wikipedia.org/wiki/Abbaye_Notre-Dame_de_Bellozanne",
                "https://fr-academic.com/dic.nsf/frwiki/1804352/",
            ],
            {"future_default_after_review": False},
        ),
        (
            "anchor_saint_lucien_bellozanne_patronage",
            "Saint-Lucien",
            "later_gournay_institutional",
            [1.448715, 49.508484],
            "high",
            "Bellozanne patronage parish",
            "Saint-Lucien's church patronage was given to the abbey of Bellozanne and confirmed by the archbishop of Rouen; Bellozanne's benefices also list Saint-Lucien.",
            "Explains the institutional/collateral Bellozanne finger. Do not treat as a direct G30-G37 landholding point.",
            [
                "https://fr.wikipedia.org/wiki/Saint-Lucien_%28Seine-Maritime%29",
                "https://books.openedition.org/purh/12434?lang=en",
            ],
            {"future_default_after_review": False},
        ),
        (
            "anchor_le_thil_riberpre_bellozanne_patronage",
            "Le Thil-Riberpré",
            "later_gournay_institutional",
            [1.5797, 49.6439],
            "high",
            "Bellozanne patronage parish and Riberpré annex context",
            "The patronage of the church of Le Thil and that of its Riberpré annex depended on the abbey of Bellozanne; Le Thil and Riberpré are also named in summaries of Bellozanne's benefices.",
            "Explains the institutional/collateral Bellozanne finger. Do not treat as a direct G30-G37 landholding point.",
            [
                "https://tourismedes4rivieresenbray.com/le-thil-riberpre/",
                "https://fr.wikipedia.org/wiki/Le_Thil-Riberpr%C3%A9",
                "https://books.openedition.org/purh/12434?lang=en",
            ],
            {"future_default_after_review": False},
        ),
        (
            "anchor_elbeuf_en_bray_bellozanne_institutional",
            "Elbeuf-en-Bray",
            "later_gournay_institutional",
            [1.631, 49.498],
            "medium",
            "Bellozanne / institutional geography",
            "Elbeuf-en-Bray tourism history says parish revenues were entrusted to Bellozanne in the 12th century.",
            "Institutional / later-collateral geography. Keep visually distinct from direct landholding layers.",
            ["https://tourismedes4rivieresenbray.com/elbeuf-en-bray/"],
            {"future_default_after_review": False},
        ),
        (
            "anchor_beaubec_la_rosiere_gournay_foundation",
            "Abbaye Saint-Laurent de Beaubec / Beaubec-la-Rosière",
            "later_gournay_institutional",
            [1.500000, 49.633333],
            "medium-high",
            "Gournay institutional foundation",
            "Beaubec-la-Rosière was founded in 1127 by a Hugues de Gournay; the abbey location is approximately 49°38'N, 1°30'E.",
            "Institutional/collateral Gournay geography. Keep separate from direct G30-G37 holdings and the Conquêts polygon.",
            [
                "https://en.wikipedia.org/wiki/Beaubec-la-Rosi%C3%A8re",
                "https://commons.wikimedia.org/wiki/Category:Abbaye_Saint-Laurent_de_Beaubec",
            ],
            {"future_default_after_review": False, "coordinate_precision": "approximate abbey coordinate"},
        ),
        (
            "anchor_cuy_saint_fiacre_quesnoy_gournay_dependency",
            "Cuy-Saint-Fiacre / Quesnoy",
            "gournay_chatelainie_dependencies",
            [1.6986, 49.5133],
            "medium-high",
            "Gournay châtellenie dependency connector",
            "Cuy-Saint-Fiacre history says the hameau of Quesnoy was the chief manor of a full fief of haubert dependent on the châtellenie of Gournay.",
            "Connector between the Gournay core and the 24-village edge. Do not merge into the Conquets Hue de Gournay polygon.",
            [
                "https://fr.wikipedia.org/wiki/Cuy-Saint-Fiacre",
                "https://seine76.fr/communes/communes_result.php?var=CUY-SAINT-FIACRE",
            ],
            {},
        ),
    ]
    for item_id, name, group, point, certainty, anchor_role, basis, note, urls, extra in overlay_place_anchors:
        features.append(
            feature(
                item_id,
                name,
                "overlay_place_anchor",
                group,
                {"type": "Point", "coordinates": point},
                certainty,
                basis,
                note,
                urls,
                style=style_for(group, {"markerColor": GROUP_STYLES[group]["color"]}),
                anchor_role=anchor_role,
                **extra,
            )
        )

    features.extend(
        [
            feature(
                "cuy_saint_fiacre_quesnoy_gournay_dependency",
                "Cuy-Saint-Fiacre / Quesnoy Gournay chatellenie dependency",
                "dependency_buffer",
                "gournay_chatelainie_dependencies",
                {"type": "Polygon", "coordinates": [circle([1.6986, 49.5133], 2.5)]},
                "medium",
                "A full fief of haubert at Quesnoy depended on the chatellenie of Gournay; the hameau still exists and the parish church has 12th-century context.",
                "Connector / dependency feature between the Gournay core and the 24-village edge. Do not merge into the Conquets polygon.",
                ["https://fr.wikipedia.org/wiki/Cuy-Saint-Fiacre", "https://seine76.fr/communes/communes_result.php?var=CUY-SAINT-FIACRE"],
                buffer_km=2.5,
            ),
            feature(
                "avesnes_ferrieres_gournay_dependency_context",
                "Avesnes / Ferrieres Gournay dependency context",
                "dependency_context_buffer",
                "gournay_western_dependency_context",
                {
                    "type": "Polygon",
                    "coordinates": [[
                        *buffered_hull([[1.7247, 49.4814], [1.745918, 49.48242], [1.6733, 49.4697]], 3)
                    ]],
                },
                "low-medium",
                "Archives 76 Avesnes topography preserves 1503 fief language tying Avesnes to the full fief of Ferrieres and the chatellenie of Gournay.",
                "Western dependency context layer, not part of the Conquets Hue de Gournay polygon.",
                [
                    "https://www.archivesdepartementales76.net/archive/catalogue/communes76/avesnes-en-bray/n%3A168",
                    "https://www.archivesdepartementales76.net/archive/catalogue/communes76/ferrires-en-bray/n%3A168",
                ],
                buffer_km=3,
            ),
            feature(
                "gournay_la_ferte_gaillefontaine_frontier_corridor",
                "Gournay-La Ferte-Gaillefontaine frontier corridor",
                "frontier_corridor",
                "direct_gournay_frontier_corridor",
                {
                    "type": "Polygon",
                    "coordinates": [[
                        *buffered_hull([[1.727303, 49.483148], [1.527104, 49.57795], [1.62589488664005, 49.650477933144]], 5)
                    ]],
                },
                "low-medium",
                "Direct fortress / landholding corridor joining the ancestral seat at Gournay, the La Ferte cadet-line locality, and Gaillefontaine from the Orderic triad; Sigy and Fry represent related ecclesiastical endowment geography.",
                "Interpretive corridor only, not a continuous surveyed landholding boundary.",
                [
                    "research/places/gournay-en-bray.md",
                    "research/places/la-ferte-en-bray.md",
                    "research/places/gaillefontaine.md",
                ],
                buffer_km=5,
            ),
            feature(
                "la_ferte_sigy_fry_ecclesiastical_spur",
                "La Ferte-Sigy-Fry ecclesiastical spur",
                "ecclesiastical_spur_buffer",
                "direct_gournay_frontier_corridor",
                {
                    "type": "Polygon",
                    "coordinates": [[
                        *buffered_hull([[1.527104, 49.57795], [1.491389, 49.547222], [1.526414, 49.530369]], 2.5)
                    ]],
                },
                "low-medium",
                "La Ferte foundation and later Sigy/Fry ecclesiastical geography identify a cadet-line church and priory network adjoining the direct frontier corridor.",
                "Ecclesiastical/endowment spur only; do not read as a secular jurisdictional boundary.",
                [
                    "https://books.openedition.org/pur/49267",
                    "research/places/sigy-normandy.md",
                    "research/places/fry-eglise-saint-martin.md",
                ],
                buffer_km=2.5,
                style=style_for("direct_gournay_frontier_corridor", {"fillOpacity": 0.07, "dashArray": "5 4"}),
            ),
            feature(
                "gaillefontaine_castle_motte_buffer",
                "Gaillefontaine castle / motte buffer",
                "castle_buffer",
                "direct_gournay_frontier_corridor",
                {"type": "Polygon", "coordinates": [circle([1.62589488664005, 49.650477933144], 4)]},
                "medium-high",
                "Orderic triad plus Gaillefontaine official history tying Gaillefontaine to Gournay and La Ferte, describing the fortress, visible motte, and 1472 destruction.",
                "Castle/motte anchor buffer. It is not merged into the northern context layer.",
                [
                    "https://www.mairiegaillefontaine.fr/pages/decouvrir-et-bouger/histoire/historique.html",
                    "https://www.plan-du-patrimoine.fr/monument-historique/76/gaillefontaine/domaine-de-gaillefontaine/PA00100670/",
                ],
                buffer_km=4,
                survival_note="Motte remains visible and wooded; fortress itself destroyed/dismantled.",
            ),
            feature(
                "northern_gournay_honor_context_corridor",
                "Northern Gournay-honor context: Gaillefontaine / Haucourt / Criquiers",
                "context_corridor",
                "northern_gournay_honor_context",
                {
                    "type": "Polygon",
                    "coordinates": [[
                        *buffered_hull([[1.6259, 49.6505], [1.6606, 49.6414], [1.7067, 49.6753]], 5)
                    ]],
                },
                "low-medium",
                "Bauduin places the Haucourt lineage on lands principally dependent on the honor of Gournay; Haucourt fief depended on Gaillefontaine; Gaillefontaine official history ties fortress and motte to Gournay and La Ferte.",
                "Context layer for Gournay honor dependencies and later frontier settlement, not a direct direct-line landholding polygon.",
                [
                    "https://shs.cairn.info/revue-histoire-et-societes-rurales-2001-1-page-131?lang=fr",
                    "https://www.mairiegaillefontaine.fr/pages/decouvrir-et-bouger/histoire/historique.html",
                    "https://www.archivesdepartementales76.net/archive/catalogue/communes76/criquiers/n%3A168",
                ],
                buffer_km=5,
            ),
            feature(
                "g33_bec_gournay_endowment_cluster_envelope",
                "G33 Bec / Gournay endowment cluster envelope",
                "endowment_context_envelope",
                "g33_bec_endowment_cluster",
                {
                    "type": "Polygon",
                    "coordinates": [[
                        *buffered_hull(
                            [
                                [1.727303, 49.483148],
                                [1.527104, 49.57795],
                                [1.62589488664005, 49.650477933144],
                                [1.590, 49.515],
                                [1.615, 49.492],
                                [1.745918, 49.48242],
                                [1.399, 49.690],
                            ],
                            4,
                        )
                    ]],
                },
                "low-medium",
                "Hugh III / Basilia Bec donation geography includes churches, tithes, houses, milling rights, and other property/revenue geography across Gournay, Gaillefontaine, La Ferte, Massy/Morimont, Bremontier/Merval, Elbeuf, Laudencourt, and related places.",
                "Property/revenue/endowment geography. Keep visually distinct from direct landholding and 24-village layers.",
                [
                    "https://www.archivesdepartementales76.net/archive/catalogue/communes76/massy/n%3A168",
                    "https://www.archivesdepartementales76.net/archive/catalogue/communes76/esclavelles",
                    "https://tourismedes4rivieresenbray.com/elbeuf-en-bray/",
                    "https://www.bremontier-merval.fr/vie-culturelle/histoire",
                    "research/places/g33-bec-gournay-endowment-cluster.md",
                ],
                buffer_km="variable",
            ),
            feature(
                "massy_morimont_bec_endowment_candidate",
                "Massy / Morimont Bec-endowment candidate",
                "candidate_endowment_buffer",
                "g33_bec_endowment_cluster",
                {"type": "Polygon", "coordinates": [circle([1.399, 49.690], 3)]},
                "medium-low",
                "Archives 76 Massy topography includes medieval Gurney-linked Massy forms; related research indicates Hugh III benefactions to Bec included the church of Massy.",
                "Use as a separate endowment-network overlay. Do not merge into the Conquets Hue de Gournay polygon.",
                [
                    "https://www.archivesdepartementales76.net/archive/catalogue/communes76/massy/n%3A168",
                    "https://www.archivesdepartementales76.net/archive/catalogue/communes76/esclavelles",
                ],
                buffer_km=3,
            ),
            feature(
                "gournay_later_institutional_layer_bellozanne_beaubec",
                "Later Gournay institutional geography: Bellozanne / Beaubec / Elbeuf / Bremontier-Merval",
                "institutional_context_envelope_deprecated",
                "later_gournay_institutional",
                {
                    "type": "Polygon",
                    "coordinates": [[
                        *buffered_hull([[1.60, 49.51], [1.615, 49.492], [1.52, 49.66], [1.54, 49.76]], 4)
                    ]],
                },
                "low-medium",
                "Bellozanne and Beaubec are later Gournay institutional foundations / patronage sites; Elbeuf-en-Bray and Bremontier-Merval are linked to Bellozanne patronage and administration.",
                "Optional institutional / senior-collateral layer. Do not merge into direct G30-G37 holdings or the Conquets polygon.",
                [
                    "https://fr.wikipedia.org/wiki/Abbaye_Notre-Dame_de_Bellozanne",
                    "https://tourismedes4rivieresenbray.com/elbeuf-en-bray/",
                    "https://fr.wikipedia.org/wiki/Beaubec-la-Rosi%C3%A8re",
                    "https://www.bremontier-merval.fr/vie-culturelle/histoire",
                ],
                display_default=False,
                buffer_km="variable",
                future_default_after_review=False,
                deprecated_by="gournay_later_institutional_layer_bellozanne_beaubec_v2",
                status="deprecated after visual review",
            ),
            feature(
                "gournay_later_institutional_layer_bellozanne_beaubec_v2",
                "Later Gournay institutional geography: Bellozanne / Beaubec / Elbeuf / Bremontier-Merval",
                "institutional_context_grouped_buffers",
                "later_gournay_institutional",
                {
                    "type": "MultiPolygon",
                    "coordinates": [
                        *multipoint_buffers(
                            [
                                [1.611111, 49.505556],
                                [1.6029, 49.514],
                                [1.631, 49.498],
                                [1.448715, 49.508484],
                                [1.5797, 49.6439],
                            ],
                            3.5,
                        ),
                        *multipoint_buffers([[1.500000, 49.633333]], 2.5),
                    ],
                },
                "medium",
                "Bellozanne patronage geography is modeled from source-backed institutional anchors at Bellozanne, Brémontier-Merval, Elbeuf-en-Bray, Saint-Lucien, and Le Thil-Riberpré; Beaubec is modeled as a separate institutional satellite at the approximate abbey coordinate.",
                "Grouped institutional buffers after visual review. Saint-Lucien is included, while the unsupported northern lobe around Ménonval / Auvilliers is not carried forward. This remains institutional / senior-collateral geography, not a direct G30-G37 landholding claim.",
                [
                    "https://fr.wikipedia.org/wiki/Abbaye_Notre-Dame_de_Bellozanne",
                    "https://fr-academic.com/dic.nsf/frwiki/1804352/",
                    "https://tourismedes4rivieresenbray.com/elbeuf-en-bray/",
                    "https://www.bremontier-merval.fr/vie-culturelle/histoire",
                    "https://fr.wikipedia.org/wiki/Saint-Lucien_%28Seine-Maritime%29",
                    "https://tourismedes4rivieresenbray.com/le-thil-riberpre/",
                    "https://fr.wikipedia.org/wiki/Le_Thil-Riberpr%C3%A9",
                    "https://books.openedition.org/purh/12434?lang=en",
                    "https://en.wikipedia.org/wiki/Beaubec-la-Rosi%C3%A8re",
                    "https://commons.wikimedia.org/wiki/Category:Abbaye_Saint-Laurent_de_Beaubec",
                ],
                buffer_km="Bellozanne patronage anchors 3.5 km; Beaubec satellite 2.5 km",
                future_default_after_review=False,
            ),
            feature(
                "southern_boundary_context_neuf_marche_lyons",
                "Southern boundary context: Neuf-Marche / Lyons / Saint-Germer-de-Fly",
                "boundary_context",
                "southern_boundary_context",
                {
                    "type": "Polygon",
                    "coordinates": [[
                        *buffered_hull([[1.720, 49.425], [1.600, 49.405], [1.780, 49.445], [1.900, 49.435]], 5)
                    ]],
                },
                "medium",
                "Outward searches south/southeast of Gournay show important neighboring jurisdictions and abbey geography, but no strong direct Gournay holding evidence in this pass.",
                "Negative-control / boundary layer to prevent over-expanding the Gournay overlay southward.",
                [
                    "https://books.openedition.org/purh/20171",
                    "https://www.larousse.fr/encyclopedie/ville/Saint-Germer-de-Fly_60850/142355",
                    "https://www.banatic.interieur.gouv.fr/commune/60592-Saint-Pierre-es-Champs",
                    "https://www.banatic.interieur.gouv.fr/commune/60516-Puiseux-en-Bray",
                ],
                display_default=False,
                buffer_km="variable",
                future_default_after_review=False,
            ),
        ]
    )

    data = {
        "type": "FeatureCollection",
        "name": "Gournay Norman holdings overlay v5 source-informed",
        "metadata": {
            "purpose": "Source-informed interpretive overlay for visual review on the ancestor map.",
            "coordinate_order": "[longitude, latitude]",
            "source_patchset": "research/geo/gournay_norman_holdings_overlay_v5_master_patchset_2026-05-07.md",
            "not_cadastral": True,
            "display_policy": "Major interpretive holdings groups remain visible by default; southern boundary-control context is available but default-off after review.",
            "unresolved_conde_names": [
                {"name": "Raincourt", "status": "unresolved", "notes": "No confident modern identification found. Do not map separately."},
                {"name": "Royay", "status": "unresolved", "candidate_forms": ["Rosay", "Rosoy", "Roy-Boissy", "Roye"], "notes": "No confident match. Do not map separately."},
                {"name": "Torchy", "status": "unresolved", "candidate_forms": ["Torcy", "Torchy"], "candidate_leads": ["Ferme de Torchy near Cuy-Saint-Fiacre", "Fontenay-Torcy / Torchy forms"], "notes": "Do not map separately yet."},
                {"name": "Saint-Sanson sous le Rain", "status": "unresolved", "candidate_forms": ["Saint-Samson-la-Poterie", "Hericourt-Saint-Samson / Hericourt-sur-Therain"], "notes": "Do not map separately yet."},
                {"name": "Hincourt / Haincourt", "status": "partly unresolved", "notes": "Track as a Saint-Quentin / Beaulevrier cluster note, not a separate map point yet."},
            ],
        },
        "features": features,
    }

    RESEARCH_OUT.parent.mkdir(parents=True, exist_ok=True)
    SITE_OUT.parent.mkdir(parents=True, exist_ok=True)
    RESEARCH_OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    shutil.copyfile(RESEARCH_OUT, SITE_OUT)


if __name__ == "__main__":
    main()
