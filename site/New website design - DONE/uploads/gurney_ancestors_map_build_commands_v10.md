# Gurney Map Build Commands — v10

## Inputs
- Ancestors source: `/mnt/data/ancestors v26.json`
- Places source: `/mnt/data/places.json`
- Place detail source: `/mnt/data/places_detail.json`
- Build script: `/mnt/data/build_gurney_map_v10.py`

## Command sequence

```bash
cd /mnt/data
python3 build_gurney_map_v10.py \
  --ancestors "/mnt/data/ancestors v26.json" \
  --places "/mnt/data/places.json" \
  --places-detail "/mnt/data/places_detail.json" \
  --output-html "/mnt/data/gurney_ancestors_map_v10.html" \
  --method-md "/mnt/data/gurney_ancestors_map_method_v10.md"
```

## Expected outputs
- `gurney_ancestors_map_v10.html`
- `gurney_ancestors_map_method_v10.md`

## Process notes
- Adapts the v9 map build process to the new canonical place spine model
- Uses `places.json` as the primary place registry
- Uses `places_detail.json` for popup enrichment
- Uses `ancestors v26.json` to resolve people, generations, and era joins
- Preserves the existing UI pattern: title banner, cleaned legend, Homepage link, overlay-only selector, favicon, and Allen Gurney attribution
