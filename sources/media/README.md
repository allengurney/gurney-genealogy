# sources/media/

Source media organized by sourceId. One folder per source.

## Structure

```
media/
├── {sourceId}/
│   ├── original.png           # The primary capture
│   ├── detail-{name}.png      # Zoomed crops of specific entries
│   ├── annotated-{name}.png   # Annotated versions (highlights, notes)
│   └── context.md             # Optional: notes on capture provenance
└── ...
```

## Naming

Folder names match the `sourceId` in `data/sources.json` exactly. Examples:

- `nro-pd-12-1/` — St Martin at Palace marriage register
- `nro-pd-86-41/` — East Dereham baptism register
- `anderson-gmd-2015/` — *Great Migration Directory*
- `dg-rec-pt2/` — Daniel Gurney, *Record of the House of Gournay*, Part 2

Filenames within a folder are descriptive, not numbered. `detail-entry-e.png` is useful three months later; `detail-03.png` is not.

## File formats

- **PNG** preferred for screenshots (lossless, good for text).
- **JPG** acceptable for photographs of physical documents.
- **PDF** fine for multi-page record extracts when splitting into images is awkward.

## Size discipline

Aim for files under ~500KB each. Crop and compress before committing. A full high-resolution scan that belongs somewhere else (OneDrive) should stay out of the repo; the repo holds the working-reference versions.
