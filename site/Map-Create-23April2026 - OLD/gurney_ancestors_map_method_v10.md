# Gurney Ancestors Map — Method Note v10

## Build basis
This map updates the retained v9 process to the newer place-spine JSON model.

- ancestors input: `ancestors v26.json`
- places input: `places.json`
- place detail input: `places_detail.json`
- build script: `build_gurney_map_v10.py`
- stack: Python + Folium/Leaflet + CartoDB Positron
- circle markers built from canonical place records with non-property roles
- square markers built from canonical place records with landholding/property roles

## Validation summary
- era records: 11
- people records: 43
- canonical place records: 59
- rendered circle markers: 44
- rendered square markers: 37

## Process adaptation
- uses `places.json` as the primary place spine
- uses `places_detail.json` for popup enrichment
- uses `ancestors v26.json` to resolve person, generation, and era joins via `recordId` and `eraId`

## Popup rules retained from v9
- no `Reference count merged` field
- `Era` label retained
- no generic JSON/merge notes
- no `Source document` field
- description values truncated at 700 characters
