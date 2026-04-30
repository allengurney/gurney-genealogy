# Daniel Gurney Image Extract - v4 Combined

This package continues the Daniel Gurney image extraction after the v3 catalog repair. It adds the missing **Part I / Norman origins** material from `Daniel Gurney Complete in PDF first half.pdf` and carries forward the previously extracted images from v3 repaired content.

## New in v4

- Added `38` cropped Part I images.
- Added `10` Part I catalog-only image candidates.
- Added corrected rich metadata for every new Part I crop: filename, source PDF, PDF page, printed page/plate placement, caption, ancestor/place applicability, scope judgment, and adjacent-text narrative description.
- Added `catalog/page_coverage_tracker_v4.md`.

## Important metadata note

For the Part II / Part III / early Part IV images added in v3, use:

`catalog/daniel_gurney_v3_repaired_catalog.md`

That file supersedes any thinner v3 catalog metadata.

## Folder map

```text
daniel_gurney_image_extract_v4_combined/
  README.md
  manifest.json
  catalog/
    page_coverage_tracker_v4.md
    daniel_gurney_v3_repaired_catalog.md
    daniel_gurney_v3_repaired_catalog_fields.csv
  part1_norman_origins/
    images/
    catalog/
      daniel_gurney_part1_norman_origins_image_catalog.md
      daniel_gurney_part1_norman_origins_catalog.csv
      part1_norman_origins_contact_sheet.png
    manifest.json
  part2_norfolk_line/
  part4_first_pass/
  supplement_second_pass/
```

## Processing

Images are grayscale PNGs rendered at approximately 300 dpi with light autocontrast. No generative enhancement, sharpening, or binarization was applied.
