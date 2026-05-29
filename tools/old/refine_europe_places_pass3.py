from __future__ import annotations

import copy
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
PLACES_DIR = ROOT / "research" / "places"
LOG_DIR = ROOT / "research" / "log"

PLACES_JSON = DATA_DIR / "places.json"
PLACES_DETAIL_JSON = DATA_DIR / "places_detail.json"
ANCESTORS_V24 = DATA_DIR / "ancestors v24.json"
LOG_PATH = LOG_DIR / "2026-04-17--place-normalization-pass3b-europe.md"

GEN_START = "<!-- GENERATED:PLACE-REGISTRY:START -->"
GEN_END = "<!-- GENERATED:PLACE-REGISTRY:END -->"

ROLE_ORDER = {
    "landholding / property reference": 10,
    "residence": 20,
    "address reference": 30,
    "individual geography": 40,
    "associated place": 90,
}

EUROPE_OVERRIDES = {
    "Ardleigh, Essex, England": {
        "shortDescription": "Domesday manor locality",
        "longDescription": "Ardleigh, one of the Essex Domesday manors associated with Hugh de Gournay III.",
        "reviewNotes": [],
    },
    "Attleborough, Norfolk, England": {
        "shortDescription": "Advowson locality",
        "longDescription": "Attleborough church-advowson context associated with Henry Gurney.",
        "reviewNotes": [],
    },
    "Bedfordshire, England": {
        "shortDescription": "Regional holdings context",
        "longDescription": "County-level umbrella record for scattered Bedfordshire holdings documented in exchequer and royal records.",
        "reviewNotes": ["Regional umbrella record, not a single site."],
        "siteName": "",
        "extantStatus": "",
        "extantStatusDescription": "",
    },
    "Buckinghamshire, England": {
        "shortDescription": "Regional holdings context",
        "longDescription": "County-level umbrella record for scattered Buckinghamshire holdings documented in exchequer and royal records.",
        "reviewNotes": ["Regional umbrella record, not a single site."],
        "siteName": "",
        "extantStatus": "",
        "extantStatusDescription": "",
    },
    "Burnham Thorpe, Norfolk, England": {
        "shortDescription": "Later family locality",
        "longDescription": "Burnham Thorpe, a later Norfolk locality associated with William Gurney IV and possible land interest.",
        "reviewNotes": [],
    },
    "Caister-on-Sea, Norfolk, England": {
        "shortDescription": "Gerard de Gournay holding",
        "longDescription": "Caister-on-Sea, one of the documented Norfolk holdings associated with Gerard de Gournay's English expansion.",
        "reviewNotes": [],
    },
    "Cantley, Norfolk, England": {
        "shortDescription": "Gerard de Gournay holding",
        "longDescription": "Cantley, one of the documented Norfolk holdings associated with Gerard de Gournay's English expansion.",
        "reviewNotes": [],
    },
    "City of London, England": {
        "shortDescription": "Historic commercial site",
        "longDescription": "City of London commercial context linked to St Benet Fink parish and the La Selde Coronata warehouse tradition.",
        "siteName": "St Benet Fink",
        "coordinate": {"lat": 51.51389, "lng": -0.08611},
        "coordinatePrecision": "exact",
        "coordinateBasis": "exact historical church site",
        "extantStatus": "site only",
        "extantStatusDescription": "St Benet Fink church is lost; the historic site lies within the modern Bank of England east-wing area.",
        "reviewNotes": ["City-level record aggregates more than one London sub-site; keep the narrative file for separation."],
    },
    "Essex, England": {
        "shortDescription": "Regional holdings context",
        "longDescription": "County-level umbrella record for Essex holdings including the Domesday manors of Ardleigh, Fordham, and Liston.",
        "reviewNotes": ["Regional umbrella record, not a single site."],
        "siteName": "",
        "extantStatus": "",
        "extantStatusDescription": "",
    },
    "Flegg, Norfolk, England": {
        "shortDescription": "District-level holdings context",
        "longDescription": "Flegg district umbrella record for dispersed Norfolk manorial interests associated with the Gournay line.",
        "reviewNotes": ["District-level umbrella record, not a single site."],
        "siteName": "",
        "extantStatus": "",
        "extantStatusDescription": "",
    },
    "Fordham, Essex, England": {
        "shortDescription": "Domesday manor locality",
        "longDescription": "Fordham, one of the Essex Domesday manors associated with Hugh de Gournay III.",
        "reviewNotes": [],
    },
    "Gournay-en-Bray, Normandy, France": {
        "shortDescription": "Ancestral fortress town",
        "longDescription": "Ancestral fortress town and frontier seigneury of the Gournay family in the Pays de Bray.",
        "siteName": "Collégiale Saint-Hildevert",
        "coordinate": {"lat": 49.483148, "lng": 1.727303},
        "coordinatePrecision": "exact",
        "coordinateBasis": "exact church site used as historic town anchor",
        "extantStatus": "extant",
        "extantStatusDescription": "Modern town survives; the church site is used as the best historic anchor for the lost fortress town.",
        "reviewNotes": [],
    },
    "Great Ellingham, Norfolk, England": {
        "shortDescription": "Lovell inheritance manor",
        "longDescription": "Great Ellingham manor, later associated with the Lovell inheritance through Margaret Lovell.",
        "reviewNotes": [],
    },
    "Hardingham, Norfolk, England": {
        "shortDescription": "Junior-branch core manor",
        "longDescription": "Swathings in Hardingham, a long-running junior-line holding documented from the Henry II period onward.",
        "reviewNotes": [],
    },
    "Harpham, Norfolk, England": {
        "shortDescription": "Later Gurney manor",
        "longDescription": "Harpham manor, purchased in 1587 and reflected in later church presentations.",
        "reviewNotes": [],
    },
    "Harpley, Norfolk, England": {
        "shortDescription": "Junior-branch core manor",
        "longDescription": "Gurney's manor in Harpley, acquired c.1183 through Rose de Burnham and the Hameline de Warenne connection.",
        "reviewNotes": [],
    },
    "Hellesdon, Norfolk, England": {
        "shortDescription": "Heylesdon inheritance manor",
        "longDescription": "Hellesdon / Heylesdon manor context associated with the Alice Heylesdon inheritance.",
        "reviewNotes": [],
    },
    "Hingham, Norfolk, England": {
        "shortDescription": "Ancient junior-line manor",
        "longDescription": "Manor of Hingham-Gurneys, an ancient junior-line holding later held of the Bardolf and Morley interests.",
        "reviewNotes": [],
    },
    "Irstead, Norfolk, England": {
        "shortDescription": "Later junior-line manor",
        "longDescription": "Irstead manor, a primary documented later junior-line holding in Norfolk.",
        "reviewNotes": [],
    },
    "King's Lynn, Norfolk, England": {
        "shortDescription": "Historic commercial site",
        "longDescription": "St James's Chapel site in King's Lynn, leased for a failed textile-manufacture venture in the early seventeenth century.",
        "siteName": "St James's Chapel ruins",
        "coordinate": {"lat": 52.7515, "lng": 0.401},
        "coordinatePrecision": "exact",
        "coordinateBasis": "exact historical chapel ruins",
        "extantStatus": "ruins",
        "extantStatusDescription": "Ruins of St James's Chapel survive and provide the historic site anchor.",
        "reviewNotes": [],
    },
    "La Ferté-en-Bray, Normandy, France": {
        "shortDescription": "Priory foundation locality",
        "longDescription": "Priory foundation site whose 989–996 charter first names Renaud de Gournay, Alberade, Hugh, and Gautier.",
        "siteName": "Église Saint-Pierre-et-Saint-Paul",
        "coordinate": {"lat": 49.57795, "lng": 1.527104},
        "coordinatePrecision": "high",
        "coordinateBasis": "historic parish church / former La Ferté-en-Bray core",
        "extantStatus": "site only",
        "extantStatusDescription": "Former priory no longer stands; the parish church of Saint-Pierre-et-Saint-Paul occupies or adjoins the historic core.",
        "reviewNotes": [],
    },
    "Le Bec-Hellouin, Normandy, France": {
        "shortDescription": "Abbey burial site",
        "longDescription": "Abbey of Bec, endowed by the Gournays and associated with Hugh III's burial.",
        "siteName": "Abbey of Bec",
        "coordinate": {"lat": 49.2288, "lng": 0.722},
        "coordinatePrecision": "exact",
        "coordinateBasis": "exact abbey site",
        "extantStatus": "extant",
        "extantStatusDescription": "The abbey complex still stands and anchors the historic burial and endowment site.",
        "reviewNotes": [],
    },
    "Lessingham, Norfolk, England": {
        "shortDescription": "Priory foundation locality",
        "longDescription": "Lessingham Priory foundation linked to the Abbey of Bec.",
        "reviewNotes": [],
    },
    "Lewes, Sussex, England": {
        "shortDescription": "Battlefield locality",
        "longDescription": "Lewes, associated with the 1264 battle in which Sir John de Gournay I was active.",
        "reviewNotes": [],
    },
    "Liston, Essex, England": {
        "shortDescription": "Domesday manor locality",
        "longDescription": "Liston, one of the Essex Domesday manors associated with Hugh de Gournay III.",
        "reviewNotes": [],
    },
    "Montigny-sur-Andelle, Normandy, France": {
        "shortDescription": "Parage tenure locality",
        "longDescription": "Montigny-sur-Andelle parage tenure, cited as proof of junior-line descent from the Barons of Gournay.",
        "reviewNotes": [],
    },
    "Norfolk, England": {
        "shortDescription": "Regional holdings context",
        "longDescription": "County-level umbrella record for dispersed Norfolk holdings; use individual manor and village files for site-specific work.",
        "reviewNotes": ["Regional umbrella record, not a single site."],
        "siteName": "",
        "extantStatus": "",
        "extantStatusDescription": "",
    },
    "Normandy, France": {
        "shortDescription": "Regional holdings context",
        "longDescription": "Regional umbrella record for Norman holdings and priory contexts not yet assigned to a tighter single locality.",
        "reviewNotes": ["Regional umbrella record, not a single site."],
        "siteName": "",
        "coordinateBasis": "regional centroid",
        "extantStatus": "",
        "extantStatusDescription": "",
    },
    "Oxfordshire, England": {
        "shortDescription": "Regional holdings context",
        "longDescription": "County-level umbrella record for scattered Oxfordshire holdings documented in exchequer and royal records.",
        "reviewNotes": ["Regional umbrella record, not a single site."],
        "siteName": "",
        "extantStatus": "",
        "extantStatusDescription": "",
    },
    "Runhall, Norfolk, England": {
        "shortDescription": "Junior-line manor locality",
        "longDescription": "Runhall manor, paired with Hardingham in the junior line's Norfolk holdings.",
        "extantStatus": "approximate area",
        "extantStatusDescription": "Modern village location is the best surviving anchor for the historic manor.",
        "reviewNotes": [],
    },
    "Saxthorpe, Norfolk, England": {
        "shortDescription": "Loundhall locality",
        "longDescription": "Saxthorpe locality associated with the holding called Loundhall.",
        "reviewNotes": [],
    },
    "Scandinavia": {
        "shortDescription": "Traditional origin region",
        "longDescription": "Traditional Scandinavian origin context only; no specific Denmark-or-Norway locality is established, and Rollo's ancestry should not be treated as direct Gournay ancestry.",
        "reviewNotes": [
            "Origin-region record only; no tighter locality is established yet.",
            "Traditional context only; not an attested Gournay family seat or documented locality."
        ],
        "siteName": "",
        "coordinateBasis": "regional centroid",
        "extantStatus": "",
        "extantStatusDescription": "",
    },
    "Suffolk, England": {
        "shortDescription": "Regional holdings context",
        "longDescription": "County-level record for Suffolk holdings held under Manasser de Dampmartin.",
        "reviewNotes": ["Regional umbrella record, not a single site."],
        "siteName": "",
        "extantStatus": "",
        "extantStatusDescription": "",
    },
    "West Barsham, Norfolk, England": {
        "shortDescription": "Principal family seat",
        "longDescription": "Principal Gurney family seat from 1372 until Francis Gurney sold the Norfolk lands in 1634.",
        "siteName": "West Barsham Hall",
        "coordinate": {"lat": 52.867826, "lng": 0.830094},
        "coordinatePrecision": "exact",
        "coordinateBasis": "exact extant hall site",
        "extantStatus": "extant",
        "extantStatusDescription": "Surviving north wing of West Barsham Hall still marks the historic manor site.",
        "reviewNotes": [],
        "removeAncestorLinks": [["ancestor-g-37-eudes-odon-de-gournay", "landholding / property reference"]],
    },
}

LOG_TEXT = """# 2026-04-17 — place normalization pass 3b (England and Europe)

Targeted corrective cleanup after the Europe-focused pass 3 sweep.

Updated:
- `data/places_detail.json` — removed remaining umbrella-record site-status contamination and refined selected Europe detail text
- `research/places/*.md` — refreshed generated blocks for corrected Europe umbrella and origin-region records

Key actions:
- removed the lingering Clairruissel-specific status artifact from the Normandy regional umbrella record
- tightened the Scandinavia origin-region wording to reflect tradition rather than attested locality
- refined Gournay-en-Bray and La Ferté-en-Bray wording to align more closely with the narrative place files
"""


def is_europe_place(name: str) -> bool:
    return not name.endswith(", USA")


def sort_roles(values: list[str]) -> list[str]:
    return sorted(values, key=lambda v: (ROLE_ORDER.get(v, 80), v))


def dedupe(values: list[str]) -> list[str]:
    out = []
    seen = set()
    for value in values:
        if not value:
            continue
        key = value.casefold()
        if key not in seen:
            seen.add(key)
            out.append(value)
    return out


def remove_generated_block(text: str) -> str:
    text = re.sub(re.escape(GEN_START) + r".*?" + re.escape(GEN_END), "", text, flags=re.DOTALL)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + ("\n" if text.strip() else "")


def label_map(ancestors: list[dict]) -> dict[str, str]:
    out = {}
    for rec in ancestors:
        if rec.get("recordId"):
            out[rec["recordId"]] = f"{rec.get('gen')} {rec.get('name')}"
    return out


def apply_overrides(place: dict, detail: dict) -> tuple[dict, dict]:
    name = place["name"]
    override = EUROPE_OVERRIDES.get(name)
    if not override:
        return place, detail

    place2 = copy.deepcopy(place)
    detail2 = copy.deepcopy(detail)

    if override.get("removeAncestorLinks"):
        removals = {tuple(x) for x in override["removeAncestorLinks"]}
        place2["ancestorLinks"] = [
            link for link in place2.get("ancestorLinks", [])
            if (link.get("recordId"), link.get("role")) not in removals
        ]
    if "shortDescription" in override:
        place2["shortDescription"] = override["shortDescription"]
    if "coordinate" in override:
        place2["coordinate"] = override["coordinate"]
    if "coordinatePrecision" in override:
        place2["coordinatePrecision"] = override["coordinatePrecision"]
    if "longDescription" in override:
        detail2["longDescription"] = override["longDescription"]
    if "coordinateBasis" in override:
        detail2["coordinateBasis"] = override["coordinateBasis"]
    if "siteName" in override:
        detail2["siteName"] = override["siteName"]
    if "extantStatus" in override:
        detail2["extantStatus"] = override["extantStatus"]
    if "extantStatusDescription" in override:
        detail2["extantStatusDescription"] = override["extantStatusDescription"]
    if "reviewNotes" in override:
        detail2["reviewNotes"] = override["reviewNotes"]

    place2["roles"] = sort_roles(dedupe(place2.get("roles", [])))
    grouped = defaultdict(list)
    for link in place2.get("ancestorLinks", []):
        grouped[link["recordId"]].append(link["role"])
    ancestor_links = []
    for record_id_key in sorted(grouped):
        for role in sort_roles(dedupe(grouped[record_id_key])):
            ancestor_links.append({"recordId": record_id_key, "role": role})
    place2["ancestorLinks"] = ancestor_links

    return place2, detail2


def regenerate_place_refs(ancestors: list[dict], places: list[dict]) -> list[dict]:
    refs_by_record = defaultdict(list)
    for place in places:
        for link in place.get("ancestorLinks", []):
            refs_by_record[link["recordId"]].append(place["placeId"])
    out = []
    for rec in ancestors:
        rec2 = copy.deepcopy(rec)
        if rec2.get("type") in ("ancestor", "collateral"):
            rec2["placeRefs"] = dedupe(refs_by_record.get(rec2.get("recordId"), []))
        out.append(rec2)
    return out


def format_links(detail: dict) -> str:
    links = []
    if detail.get("heritageUrl"):
        label = detail.get("heritageLabel") or detail["heritageUrl"]
        links.append(f"[{label}]({detail['heritageUrl']})")
    if detail.get("imageUrl"):
        label = detail.get("imageTitle") or "image"
        links.append(f"[{label}]({detail['imageUrl']})")
    return " · ".join(links)


def make_block(place: dict, detail: dict, labels: dict[str, str]) -> str:
    lines = [GEN_START, "## Place registry", ""]
    lines.append(f"- `placeId`: `{place['placeId']}`")
    lines.append(f"- Short description: {place['shortDescription']}")
    lines.append(f"- Place type: {place['placeType']}")
    if place.get("aliases"):
        lines.append(f"- Aliases: {', '.join(place['aliases'])}")
    if place.get("coordinate"):
        coord = place["coordinate"]
        lines.append(f"- Coordinate: {coord['lat']}, {coord['lng']} ({place['coordinatePrecision']})")
    if place.get("roles"):
        lines.append(f"- Roles: {', '.join(place['roles'])}")
    if detail.get("siteName"):
        lines.append(f"- Site name: {detail['siteName']}")
    if detail.get("streetAddress"):
        lines.append(f"- Street address: {detail['streetAddress']}")
    if detail.get("longDescription"):
        lines.append(f"- Detail: {detail['longDescription']}")
    if detail.get("extantStatus"):
        status_line = f"- Current-site status: {detail['extantStatus']}"
        if detail.get("extantStatusDescription"):
            status_line += f" — {detail['extantStatusDescription']}"
        lines.append(status_line)
    links = format_links(detail)
    if links:
        lines.append(f"- Links: {links}")
    lines.append("")
    lines.append("### Linked ancestors")
    lines.append("")
    grouped = defaultdict(list)
    for link in place.get("ancestorLinks", []):
        grouped[link["recordId"]].append(link["role"])
    for record_id_key, roles in sorted(grouped.items(), key=lambda kv: labels.get(kv[0], kv[0])):
        lines.append(f"- {labels.get(record_id_key, record_id_key)} — {', '.join(sort_roles(dedupe(roles)))}")
    lines.append("")
    lines.append("### Review notes")
    lines.append("")
    notes = detail.get("reviewNotes") or []
    if not notes:
        lines.append("- None in cleanup pass 3b.")
    else:
        for note in notes:
            lines.append(f"- {note}")
    lines.append("")
    lines.append(GEN_END)
    return "\n".join(lines)


def update_place_file(path: Path, place: dict, detail: dict, labels: dict[str, str]) -> None:
    block = make_block(place, detail, labels)
    if path.exists():
        existing = path.read_text(encoding="utf-8")
        base = remove_generated_block(existing).rstrip()
        content = base + "\n\n" + block + "\n" if base else f"# {place['name']}\n\n{block}\n"
    else:
        content = f"# {place['name']}\n\n{block}\n"
    path.write_text(content, encoding="utf-8")


def main() -> None:
    places = json.loads(PLACES_JSON.read_text(encoding="utf-8"))
    details = json.loads(PLACES_DETAIL_JSON.read_text(encoding="utf-8"))
    ancestors = json.loads(ANCESTORS_V24.read_text(encoding="utf-8"))

    detail_by_id = {item["placeId"]: item for item in details}
    updated_places = []
    updated_details = []

    for place in places:
        detail = copy.deepcopy(detail_by_id[place["placeId"]])
        place2 = copy.deepcopy(place)
        if is_europe_place(place2["name"]):
            place2, detail = apply_overrides(place2, detail)
        updated_places.append(place2)
        updated_details.append(detail)

    updated_places.sort(key=lambda x: x["name"])
    updated_details.sort(key=lambda x: x["placeName"])
    updated_ancestors = regenerate_place_refs(ancestors, updated_places)
    labels = label_map(updated_ancestors)

    PLACES_JSON.write_text(json.dumps(updated_places, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    PLACES_DETAIL_JSON.write_text(json.dumps(updated_details, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    ANCESTORS_V24.write_text(json.dumps(updated_ancestors, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    detail_by_id = {item["placeId"]: item for item in updated_details}
    for place in updated_places:
        if is_europe_place(place["name"]):
            update_place_file(PLACES_DIR / place["filename"], place, detail_by_id[place["placeId"]], labels)

    LOG_PATH.write_text(LOG_TEXT + "\n", encoding="utf-8")

    print(f"Updated {PLACES_JSON.relative_to(ROOT)}")
    print(f"Updated {PLACES_DETAIL_JSON.relative_to(ROOT)}")
    print(f"Updated {ANCESTORS_V24.relative_to(ROOT)}")
    print(f"Updated Europe/England place files under {PLACES_DIR.relative_to(ROOT)}")
    print(f"Wrote {LOG_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
