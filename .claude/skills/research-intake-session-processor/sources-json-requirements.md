# Sources JSON requirements

Source tracking is mandatory for retained intake items.

## Core rule

If an intake item is retained in any meaningful way, it must be connected to `data/sources.json`.

That means one of the following must happen:

1. match the item to an existing source entry, or
2. create a new compliant source entry, following the existing schema and conventions already used in `data/sources.json`

## Research insertion block

Do not add research content to `research/*.md` unless source tracking has been resolved.

If source tracking cannot be resolved:
- do not promote
- use `hold-review`

## Duplicate handling

For a duplicate:
- map it to the existing source entry where possible
- do not create a redundant new source entry unless the existing one is materially incorrect or too broad

## Hold-review handling

For `hold-review`:
- if enough bibliographic/source metadata is known, create or match the source entry now
- if not enough metadata is known to create a compliant entry, keep the item out of research insertion and flag it clearly in the processed report

## New source entries

When creating a new source entry:
- follow the existing schema already present in `data/sources.json`
- prefer complete human-readable source titles
- include URL when available
- include publication/repository/source context when known
- avoid unexplained shorthand
- do not create vague junk entries if the source cannot be identified meaningfully

## Processed report requirements

The processed report must state for each retained item:
- sourceId matched or created
- whether the source entry was new or existing
- any source-metadata gaps that still need manual cleanup
