from __future__ import annotations

import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
PLACES_DIR = ROOT / "research" / "places"
LOG_DIR = ROOT / "research" / "log"

PLACES_JSON = DATA_DIR / "places.json"
PLACES_DETAIL_JSON = DATA_DIR / "places_detail.json"
ANCESTORS_JSON = DATA_DIR / "ancestors v24.json"
HARPHAM_MD = PLACES_DIR / "harpham.md"
LOG_FILE = LOG_DIR / "2026-04-17--harpham-structured-cleanup.md"

HARPHAM_ID = "place-harpham-norfolk-england"
HARPLEY_ID = "place-harpley-norfolk-england"

RETIRE_NOTE = """# Harpham, Norfolk, England

## Status of this place record

This file is retained only as a **retired / superseded record note**.

Current project review indicates that the structured place record previously normalized as **Harpham, Norfolk, England** was likely a mistaken duplication of **Harpley, Norfolk** rather than a secure independent Gurney place. The strongest basis for that conclusion is the **Henry Gurney (G15) research companion**, which explicitly notes that the JSON's "Harpham" should be **Harpley**. [Henry G15 companion]

## What changed

- the structured `Harpham` place record was removed from `data/places.json`
- the structured `Harpham` detail record was removed from `data/places_detail.json`
- any ancestor `placeRefs` pointing to `place-harpham-norfolk-england` were removed
- where appropriate, Harpley remains the active place record for the related family history

## Why keep this file

This note is preserved so future reviewers can understand **why Harpham disappeared from the structured place layer** and so the branch history does not look like the record vanished without explanation.

## Next review item

- [ ] Confirm from the raw extraction path or original source trail exactly how `Harpham` entered the structured layer.
- [ ] If a real independent Norfolk Harpham connection ever emerges, restore it only with source-backed evidence.

## Sources

- `research/people/g15-henry-gurney-fact-sheet.research.md`
- `research/places/harpley.md`
- `data/places.json`
- `data/places_detail.json`
"""

LOG_TEXT = """# 2026-04-17 — structured cleanup for Harpham duplicate

Targeted reconciliation after manual place-file review.

Updated:
- `data/places.json` — removed `place-harpham-norfolk-england`
- `data/places_detail.json` — removed `place-harpham-norfolk-england`
- `data/ancestors v24.json` — removed stale Harpham `placeRefs`; ensured Harpley survives where already linked
- `research/places/harpham.md` — converted into a retired/superseded explanatory note

Reason:
- the reviewed narrative and the Henry G15 companion indicate that `Harpham` was likely a mistaken duplicate of `Harpley`, not a secure independent place record.
"""


def dedupe(values: list[str]) -> list[str]:
    out: list[str] = []
    seen = set()
    for value in values:
        if not value:
            continue
        if value not in seen:
            seen.add(value)
            out.append(value)
    return out


def main() -> None:
    places = json.loads(PLACES_JSON.read_text(encoding="utf-8"))
    details = json.loads(PLACES_DETAIL_JSON.read_text(encoding="utf-8"))
    ancestors = json.loads(ANCESTORS_JSON.read_text(encoding="utf-8"))

    harpham_place = next((p for p in places if p.get("placeId") == HARPHAM_ID), None)
    harpley_place = next((p for p in places if p.get("placeId") == HARPLEY_ID), None)

    if harpham_place and harpley_place:
        existing_links = {(link.get("recordId"), link.get("role")) for link in harpley_place.get("ancestorLinks", [])}
        for link in harpham_place.get("ancestorLinks", []):
            key = (link.get("recordId"), link.get("role"))
            if key not in existing_links:
                harpley_place.setdefault("ancestorLinks", []).append(copy.deepcopy(link))
                existing_links.add(key)
        harpley_place["ancestorLinks"] = sorted(
            harpley_place.get("ancestorLinks", []),
            key=lambda x: (x.get("recordId") or "", x.get("role") or ""),
        )
        if harpham_place.get("roles"):
            harpley_place["roles"] = dedupe((harpley_place.get("roles") or []) + list(harpham_place.get("roles") or []))

    places = [p for p in places if p.get("placeId") != HARPHAM_ID]
    details = [d for d in details if d.get("placeId") != HARPHAM_ID]

    updated_ancestors = []
    for rec in ancestors:
        rec2 = copy.deepcopy(rec)
        if rec2.get("type") in ("ancestor", "collateral"):
            refs = [r for r in rec2.get("placeRefs", []) if r != HARPHAM_ID]
            if HARPLEY_ID not in refs and rec2.get("recordId") == "ancestor-g15-henry-gurney":
                refs.append(HARPLEY_ID)
            rec2["placeRefs"] = dedupe(refs)
        updated_ancestors.append(rec2)

    places.sort(key=lambda x: x.get("name") or "")
    details.sort(key=lambda x: x.get("placeName") or "")

    PLACES_JSON.write_text(json.dumps(places, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    PLACES_DETAIL_JSON.write_text(json.dumps(details, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    ANCESTORS_JSON.write_text(json.dumps(updated_ancestors, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    HARPHAM_MD.write_text(RETIRE_NOTE + "\n", encoding="utf-8")
    LOG_FILE.write_text(LOG_TEXT + "\n", encoding="utf-8")

    print(f"Updated {PLACES_JSON.relative_to(ROOT)}")
    print(f"Updated {PLACES_DETAIL_JSON.relative_to(ROOT)}")
    print(f"Updated {ANCESTORS_JSON.relative_to(ROOT)}")
    print(f"Updated {HARPHAM_MD.relative_to(ROOT)}")
    print(f"Wrote {LOG_FILE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
