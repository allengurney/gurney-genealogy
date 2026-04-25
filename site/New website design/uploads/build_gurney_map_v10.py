
from __future__ import annotations

import argparse
import html
import json
import re
from collections import OrderedDict, defaultdict
from pathlib import Path
from typing import Any

import folium
from branca.element import Element
from bs4 import BeautifulSoup
from folium.features import DivIcon, RegularPolygonMarker

TITLE_TEXT = "Gurney Ancestors and Land Holdings"
LEGEND_TITLE = "Gurney Ancestors Map"
HOMEPAGE_URL = "https://genealogy.allengurney.com"
HOMEPAGE_LABEL = "Homepage"
FAVICON_HREF = "/favicon.png"
MAX_DESCRIPTION_CHARS = 700

ERA_COLORS = OrderedDict([
    ("Modern America", "#2c7fb8"),
    ("Gilded Age & Civil War", "#6a3d9a"),
    ("Early Republic", "#5e4fa2"),
    ("Massachusetts Farming Generations", "#1b9e77"),
    ("The Emigrant", "#33a02c"),
    ("Tudor England", "#ff7f00"),
    ("Medieval Norfolk Gurneys", "#e31a1c"),
    ("Junior Norfolk Branch", "#5a4530"),
    ("Norman Barons of England", "#1f78b4"),
    ("Viking Origin", "#636363"),
    ("End of Known Record", "#969696"),
])

LEGEND_ERA_LINES = [
    ("Modern America", "1900s–2000s"),
    ("Gilded Age & Civil War", "1800s"),
    ("Early Republic", "late 1700s–mid 1800s"),
    ("Massachusetts Farming Generations", "1600s–1700s"),
    ("The Emigrant", "1600s"),
    ("Tudor England", "1500s–early 1600s"),
    ("Medieval Norfolk Gurneys", "1300s–1400s"),
    ("Norman Barons of England", "1000s–1200s"),
    ("Viking Origin", "900s"),
    ("End of Known Record", "before 900s"),
]

CIRCLE_ROLES = {"individual geography", "residence", "address reference"}
HOLDING_ROLES = {"landholding / property reference"}

TITLE_STYLE = (
    "position: fixed; top: 10px; left: 50%; transform: translateX(-50%); z-index:9999;"
    "background: rgba(255,255,255,0.92); padding:8px 12px; border:1px solid #bbb; border-radius:6px;"
    "font-family:Arial, sans-serif; font-size:14px; font-weight:700;"
)
LEGEND_STYLE = (
    "position: fixed; bottom: 28px; left: 28px; width: 310px; max-height: 70vh; overflow-y: auto;"
    "z-index: 9999; font-size: 11px; background: rgba(255,255,255,0.95); border: 1px solid #999;"
    "border-radius: 6px; padding: 10px; box-shadow: 0 1px 6px rgba(0,0,0,0.2);"
)
OVERLAY_HEADING_STYLE = (
    "font-family:Arial,sans-serif;font-size:11px;font-weight:700;padding:2px 4px 6px 4px;"
    "margin-bottom:4px;border-bottom:1px solid #ddd;"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the Gurney ancestors map using the v9 process adapted for place-centric JSON.")
    parser.add_argument("--ancestors", required=True, help="Path to ancestors JSON")
    parser.add_argument("--places", required=True, help="Path to places JSON")
    parser.add_argument("--places-detail", required=True, help="Path to places_detail JSON")
    parser.add_argument("--output-html", required=True, help="Output HTML file")
    parser.add_argument("--method-md", required=True, help="Output method markdown")
    parser.add_argument("--description", default="Interactive map of Gurney ancestors and land holdings.")
    return parser.parse_args()


def clean_text(value: Any) -> str:
    if value is None:
        return ""
    return str(value).replace("`", "'").strip()


def esc(value: Any) -> str:
    return html.escape(clean_text(value))


def root_era_key(label: str) -> str:
    label = clean_text(label)
    if "—" in label:
        return label.split("—", 1)[0].strip()
    return label


def gen_number(gen: str) -> int:
    m = re.search(r"(\d+)", clean_text(gen))
    return int(m.group(1)) if m else 999


def gen_sort_tuple(gen: str) -> tuple[int, str]:
    return (gen_number(gen), clean_text(gen))


def generation_range(gens: list[str]) -> str:
    uniq = sorted(set([clean_text(g) for g in gens if clean_text(g)]), key=gen_sort_tuple)
    if not uniq:
        return "Unknown"
    if len(uniq) == 1:
        return uniq[0]
    return f"{uniq[0]}–{uniq[-1]}"


def truncate_description(text: str, max_chars: int = MAX_DESCRIPTION_CHARS) -> str:
    text = clean_text(text)
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 3].rstrip() + "..."


def era_color(era_key: str) -> str:
    return ERA_COLORS.get(clean_text(era_key), "#444444")


def place_label(place_name: str, site_name: str) -> str:
    site_name = clean_text(site_name)
    if site_name:
        if site_name == "West Barsham Hall":
            return "West Barsham"
        if site_name.endswith("/ historic centre"):
            return site_name
        return site_name
    return clean_text(place_name).split(",", 1)[0].strip()


def popup_image_block(url: str, title: str) -> str:
    url = clean_text(url)
    if not url:
        return ""
    title = esc(title or "Reference image")
    return (
        f"<div style='margin-top:8px; margin-bottom:6px;'>"
        f"<img src='{html.escape(url, quote=True)}' alt='{title}' "
        f"style='max-width:220px; width:220px; height:auto; border:1px solid #bbb; border-radius:4px; display:block;'>"
        f"<div style='font-size:11px; color:#555; margin-top:3px;'>{title}</div></div>"
    )


def popup_link_block(url: str, label: str) -> str:
    url = clean_text(url)
    if not url:
        return ""
    return (
        f"<div style='margin-top:4px;'><a href='{html.escape(url, quote=True)}' "
        f"target='_blank' rel='noopener noreferrer'>{esc(label or 'Reference page')}</a></div>"
    )


def make_title_html() -> str:
    return f'<div style="{TITLE_STYLE}">{html.escape(TITLE_TEXT)}</div>'


def make_legend_html() -> str:
    lines = [
        f'<div style="{LEGEND_STYLE}">',
        '<div style="display:flex; align-items:center; justify-content:space-between; gap:8px; margin-bottom:6px;">',
        f'<div style="font-weight:700;">{html.escape(LEGEND_TITLE)}</div>',
        f'<div><a href="{HOMEPAGE_URL}" target="_blank" rel="noopener noreferrer">{html.escape(HOMEPAGE_LABEL)}</a></div>',
        "</div>",
    ]
    for name, years in LEGEND_ERA_LINES:
        lines.append(
            f'<div><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:{ERA_COLORS[name]};margin-right:6px;"></span>{html.escape(name)} ({html.escape(years)})</div>'
        )
    lines.extend([
        '<div style="margin-top:6px;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#444;margin-right:6px;"></span>Circle = ancestor geography</div>',
        '<div><span style="display:inline-block;width:10px;height:10px;background:#444;transform:rotate(45deg);margin-right:6px;"></span>Square = landholding / property reference</div>',
        "</div>",
    ])
    return "".join(lines)


def overlay_heading_script() -> str:
    return f"""
<script>
setTimeout(function() {{
  var root = document.querySelector('.leaflet-control-layers-list');
  if (root && !root.querySelector('.gurney-layer-heading')) {{
    var heading = document.createElement('div');
    heading.className = 'gurney-layer-heading';
    heading.setAttribute('style', '{OVERLAY_HEADING_STYLE}');
    heading.textContent = 'Category Displayed';
    root.insertBefore(heading, root.firstChild);
  }}
}}, 0);
</script>
"""


def patch_html(output_html: Path, meta_description: str) -> None:
    soup = BeautifulSoup(output_html.read_text(encoding="utf-8"), "html.parser")
    if soup.html:
        soup.html["lang"] = "en"
    if soup.head:
        # title
        if soup.title is None:
            title_tag = soup.new_tag("title")
            title_tag.string = TITLE_TEXT
            soup.head.append(title_tag)
        else:
            soup.title.string = TITLE_TEXT
        # meta description
        for tag in soup.head.find_all("meta", attrs={"name": "description"}):
            tag.decompose()
        meta = soup.new_tag("meta")
        meta.attrs["name"] = "description"
        meta.attrs["content"] = meta_description
        soup.head.append(meta)
        # favicon
        for tag in soup.head.find_all("link", attrs={"rel": lambda v: v and ("icon" in v if isinstance(v, list) else v == "icon")}):
            tag.decompose()
        favicon = soup.new_tag("link")
        favicon.attrs["rel"] = "icon"
        favicon.attrs["href"] = FAVICON_HREF
        favicon.attrs["type"] = "image/png"
        soup.head.append(favicon)
        # overlay css
        style = soup.new_tag("style")
        style.string = """
.leaflet-control-layers-base { display: none !important; }
.leaflet-control-layers-separator { display: none !important; }
"""
        soup.head.append(style)
    output_html.write_text(str(soup), encoding="utf-8")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(ancestors: list[dict[str, Any]], places: list[dict[str, Any]], details: list[dict[str, Any]]) -> None:
    if not isinstance(ancestors, list) or not isinstance(places, list) or not isinstance(details, list):
        raise ValueError("Expected top-level lists in all JSON inputs.")
    required_place = {"placeId", "name", "coordinate", "coordinatePrecision", "roles", "ancestorLinks"}
    required_detail = {"placeId", "longDescription", "siteName", "streetAddress", "coordinateBasis", "imageUrl", "imageTitle", "heritageUrl", "heritageLabel"}
    for p in places:
        missing = required_place - set(p.keys())
        if missing:
            raise ValueError(f"Place record missing keys: {missing}")
    for d in details:
        missing = required_detail - set(d.keys())
        if missing:
            raise ValueError(f"Place detail record missing keys: {missing}")


def build_records(ancestors: list[dict[str, Any]], places: list[dict[str, Any]], details: list[dict[str, Any]]):
    people_by_id: dict[str, dict[str, Any]] = {}
    eras_by_id: dict[str, dict[str, Any]] = {}
    for item in ancestors:
        t = item.get("type")
        if t == "era":
            eras_by_id[item.get("recordId", "")] = item
        elif t in {"ancestor", "related", "collateral"}:
            people_by_id[item.get("recordId", "")] = item

    details_by_id = {d["placeId"]: d for d in details}

    circle_records: list[dict[str, Any]] = []
    square_records: list[dict[str, Any]] = []
    bounds: list[tuple[float, float]] = []

    for place in places:
        detail = details_by_id.get(place["placeId"], {})
        coord = place.get("coordinate", {})
        lat = coord.get("lat")
        lng = coord.get("lng")
        if lat is None or lng is None:
            continue
        lat = float(lat)
        lng = float(lng)
        bounds.append((lat, lng))

        links = place.get("ancestorLinks", [])
        circle_links = [lnk for lnk in links if clean_text(lnk.get("role")) in CIRCLE_ROLES]
        square_links = [lnk for lnk in links if clean_text(lnk.get("role")) in HOLDING_ROLES]

        def build_base(role_links: list[dict[str, Any]], shape: str) -> dict[str, Any]:
            people = [people_by_id[lnk["recordId"]] for lnk in role_links if lnk.get("recordId") in people_by_id]
            gens = [p.get("gen", "") for p in people]
            people_sorted = sorted(people, key=lambda p: gen_sort_tuple(p.get("gen", "")))
            holders = []
            for p in people_sorted:
                nm = clean_text(p.get("name"))
                if nm and nm not in holders:
                    holders.append(nm)
            era_names = []
            for p in people_sorted:
                era_rec = eras_by_id.get(clean_text(p.get("eraId")))
                era_name = root_era_key(era_rec.get("label", "")) if era_rec else ""
                if era_name and era_name not in era_names:
                    era_names.append(era_name)
            desc = clean_text(detail.get("longDescription") or place.get("shortDescription"))
            return {
                "shape": shape,
                "place_id": place["placeId"],
                "place_name": clean_text(place.get("name")),
                "site_name": clean_text(detail.get("siteName")),
                "street_address": clean_text(detail.get("streetAddress")),
                "extant_status": clean_text(detail.get("extantStatus")),
                "extant_status_description": clean_text(detail.get("extantStatusDescription")),
                "description": truncate_description(desc),
                "roles": sorted(set(clean_text(lnk.get("role")) for lnk in role_links if clean_text(lnk.get("role")))),
                "generation_range": generation_range(gens),
                "people_names": holders,
                "era_names": era_names,
                "lat": lat,
                "lng": lng,
                "color": era_color(era_names[0] if era_names else ""),
                "coordinate_precision": clean_text(place.get("coordinatePrecision")),
                "coordinate_basis": clean_text(detail.get("coordinateBasis")),
                "image_url": clean_text(detail.get("imageUrl")),
                "image_title": clean_text(detail.get("imageTitle")),
                "heritage_url": clean_text(detail.get("heritageUrl")),
                "heritage_label": clean_text(detail.get("heritageLabel")),
            }

        if circle_links:
            circle_records.append(build_base(circle_links, "circle"))
        if square_links:
            square_records.append(build_base(square_links, "square"))

    return circle_records, square_records, bounds


def circle_popup(rec: dict[str, Any]) -> str:
    rows = []
    def add(label: str, value: Any):
        value = clean_text(value)
        if value:
            rows.append(f"<div style='margin-bottom:4px;'><b>{html.escape(label)}:</b> {html.escape(value)}</div>")
    add("Generations represented", rec["generation_range"])
    add("Ancestors represented", "; ".join(rec["people_names"]))
    add("Roles", "; ".join(rec["roles"]))
    add("Place", rec["place_name"])
    add("Site", rec["site_name"])
    add("Street address", rec["street_address"])
    add("Era", "; ".join(rec["era_names"]))
    add("Description", rec["description"])
    add("Extant status", rec["extant_status"])
    add("Extant detail", rec["extant_status_description"])
    add("Confidence", rec["coordinate_precision"])
    add("Geocode basis", rec["coordinate_basis"])
    inner = "".join(rows)
    inner += popup_image_block(rec["image_url"], rec["image_title"])
    inner += popup_link_block(rec["heritage_url"], rec["heritage_label"])
    return f"<div style='width:340px; font-size:12px; line-height:1.3;'>{inner}</div>"


def square_popup(rec: dict[str, Any]) -> str:
    rows = []
    def add(label: str, value: Any):
        value = clean_text(value)
        if value:
            rows.append(f"<div style='margin-bottom:4px;'><b>{html.escape(label)}:</b> {html.escape(value)}</div>")
    add("Holding label", f"{rec['generation_range']} {place_label(rec['place_name'], rec['site_name'])}")
    add("Generations represented", rec["generation_range"])
    add("Holders represented", "; ".join(rec["people_names"]))
    add("Place", rec["place_name"])
    add("Site", rec["site_name"])
    add("Street address", rec["street_address"])
    add("Era", "; ".join(rec["era_names"]))
    add("Description", rec["description"])
    add("Extant status", rec["extant_status"])
    add("Extant detail", rec["extant_status_description"])
    add("Confidence", rec["coordinate_precision"])
    add("Geocode basis", rec["coordinate_basis"])
    inner = "".join(rows)
    inner += popup_image_block(rec["image_url"], rec["image_title"])
    inner += popup_link_block(rec["heritage_url"], rec["heritage_label"])
    return f"<div style='width:340px; font-size:12px; line-height:1.3;'>{inner}</div>"


def label_for_circle(rec: dict[str, Any]) -> str:
    return f"{rec['generation_range']} {place_label(rec['place_name'], rec['site_name'])}"[:42]


def label_for_square(rec: dict[str, Any]) -> str:
    return f"{rec['generation_range']} {place_label(rec['place_name'], rec['site_name'])}"[:42]


def write_method(md_path: Path, ancestors_path: Path, places_path: Path, detail_path: Path, circles: list[dict[str, Any]], squares: list[dict[str, Any]], ancestors_data: list[dict[str, Any]], places_data: list[dict[str, Any]]) -> None:
    lines = [
        "# Gurney Ancestors Map — Method Note v10",
        "",
        "## Build basis",
        "This map updates the retained v9 process to the newer place-spine JSON model.",
        "",
        f"- ancestors input: `{ancestors_path.name}`",
        f"- places input: `{places_path.name}`",
        f"- place detail input: `{detail_path.name}`",
        "- build script: `build_gurney_map_v10.py`",
        "- stack: Python + Folium/Leaflet + CartoDB Positron",
        "- circle markers built from canonical place records with non-property roles",
        "- square markers built from canonical place records with landholding/property roles",
        "",
        "## Validation summary",
        f"- era records: {sum(1 for x in ancestors_data if x.get('type') == 'era')}",
        f"- people records: {sum(1 for x in ancestors_data if x.get('type') in {'ancestor', 'related', 'collateral'})}",
        f"- canonical place records: {len(places_data)}",
        f"- rendered circle markers: {len(circles)}",
        f"- rendered square markers: {len(squares)}",
        "",
        "## Process adaptation",
        "- uses `places.json` as the primary place spine",
        "- uses `places_detail.json` for popup enrichment",
        "- uses `ancestors v26.json` to resolve person, generation, and era joins via `recordId` and `eraId`",
        "",
        "## Popup rules retained from v9",
        "- no `Reference count merged` field",
        "- `Era` label retained",
        "- no generic JSON/merge notes",
        "- no `Source document` field",
        "- description values truncated at 700 characters",
    ]
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()
    ancestors_path = Path(args.ancestors)
    places_path = Path(args.places)
    detail_path = Path(args.places_detail)
    output_html = Path(args.output_html)
    method_md = Path(args.method_md)

    ancestors_data = load_json(ancestors_path)
    places_data = load_json(places_path)
    detail_data = load_json(detail_path)
    validate(ancestors_data, places_data, detail_data)
    circles, squares, bounds = build_records(ancestors_data, places_data, detail_data)

    if not bounds:
        raise ValueError("No mappable coordinates found.")

    center_lat = sum(lat for lat, _ in bounds) / len(bounds)
    center_lng = sum(lng for _, lng in bounds) / len(bounds)

    m = folium.Map(location=[center_lat, center_lng], zoom_start=5, tiles=None, control_scale=False)
    folium.TileLayer(
        tiles="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
        attr="&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors &copy; <a href='https://carto.com/attributions'>CARTO</a>",
        name="cartodbpositron",
        overlay=False,
        control=False,
        max_zoom=20,
        max_native_zoom=20,
    ).add_to(m)

    circle_group = folium.FeatureGroup(name="Individuals", overlay=True, control=True, show=True)
    square_group = folium.FeatureGroup(name="Land holdings", overlay=True, control=True, show=True)

    for rec in circles:
        folium.CircleMarker(
            location=[rec["lat"], rec["lng"]],
            radius=6,
            color=rec["color"],
            weight=1,
            fill=True,
            fill_color=rec["color"],
            fill_opacity=0.9,
            opacity=1.0,
            popup=folium.Popup(circle_popup(rec), max_width=360),
            tooltip=folium.Tooltip(label_for_circle(rec), sticky=True),
        ).add_to(circle_group)
        folium.Marker(
            location=[rec["lat"], rec["lng"]],
            icon=DivIcon(
                icon_size=(150, 12),
                icon_anchor=(-2, 7),
                class_name="empty",
                html=(
                    '<div style="font-size:9px;font-family:Arial,sans-serif;color:#222;white-space:nowrap;'
                    'text-shadow:-1px -1px 0 #fff,1px -1px 0 #fff,-1px 1px 0 #fff,1px 1px 0 #fff,0 0 2px #fff;">'
                    + html.escape(label_for_circle(rec)) +
                    '</div>'
                ),
            ),
        ).add_to(circle_group)

    for rec in squares:
        RegularPolygonMarker(
            location=[rec["lat"], rec["lng"]],
            number_of_sides=4,
            rotation=45,
            radius=9,
            color="#333333",
            weight=1,
            opacity=1.0,
            fill=True,
            fill_color=rec["color"],
            fill_opacity=0.9,
            popup=folium.Popup(square_popup(rec), max_width=360),
            tooltip=folium.Tooltip(label_for_square(rec), sticky=True),
        ).add_to(square_group)

    circle_group.add_to(m)
    square_group.add_to(m)
    folium.LayerControl(collapsed=False, position="topright", autoZIndex=True).add_to(m)

    m.get_root().html.add_child(Element(make_title_html()))
    m.get_root().html.add_child(Element(make_legend_html()))
    m.get_root().html.add_child(Element(overlay_heading_script()))
    map_name = m.get_name()
    m.get_root().html.add_child(Element(f"<script>setTimeout(function(){{ {map_name}.attributionControl.addAttribution('&copy; Allen Gurney'); }}, 0);</script>"))

    min_lat = min(lat for lat, _ in bounds)
    max_lat = max(lat for lat, _ in bounds)
    min_lng = min(lng for _, lng in bounds)
    max_lng = max(lng for _, lng in bounds)
    m.fit_bounds([[min_lat, min_lng], [max_lat, max_lng]], padding=(30, 30))

    m.save(str(output_html))
    patch_html(output_html, args.description)
    write_method(method_md, ancestors_path, places_path, detail_path, circles, squares, ancestors_data, places_data)


if __name__ == "__main__":
    main()
