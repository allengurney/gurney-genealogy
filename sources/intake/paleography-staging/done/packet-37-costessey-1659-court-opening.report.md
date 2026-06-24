# Packet 37 paleography report: Costessey 1659 court opening

Date of this report: 2026-06-23

## Scope and status

This is a bounded staging read of Packet 37. It attempts to answer whether the April 1659 default memorandum naming `John Gurney sen[ior]` can be tied to Costessey or to another manor bundled on FamilySearch DGS 004389191.

This report is staging only. Nothing has been promoted into research files, corpus supplement, data, or media.

## Images checked

Packet-staged images:

- `images/packet-37-costessey-1659-court-opening/img-1707-3-1-S3HT-6PN9-9TS.jpg` - manuscript opening/page 302.
- `images/packet-37-costessey-1659-court-opening/img-1708-3-1-S3HT-6PNG-DX.jpg` - manuscript opening/page 303.
- `images/packet-37-costessey-1659-court-opening/img-1709-3-1-S3HT-6PNK-3Z.jpg` - pulled 2026-06-23 from the viewer's preceding-image ark; byte-identical to the staged page-304 file below.
- `images/packet-37-costessey-1659-court-opening/img-1710-3-1-S3HT-6PN9-SXB.jpg` - manuscript opening/page 304, but this file does not match the expected SXB target page.

Local master used for the actual SXB target:

- `sources/media/costessey-manorial-court-fts/_local/costessey-son-of-john-sxb.jpg` - manuscript opening/page 305, ark `3:1:S3HT-6PN9-SXB`.

The packet-staged `img-1710-3-1-S3HT-6PN9-SXB.jpg` appears to be an adjacent or mis-collapsed capture rather than the actual SXB image previously used for packet 4. After opening the standard FamilySearch viewer for `SXB`, the in-page image array placed `SXB` at index 1709 and the preceding ark as `3:1:S3HT-6PNK-3Z`; downloading that preceding ark returned the same JPG already staged as `img-1710-3-1-S3HT-6PN9-SXB.jpg` (same SHA-256 hash `169D89ABA1D29B42C0F9CEE8378701F986C6843995CA9909FCD20E3046C7FC57`). The real SXB master is already preserved locally under `sources/media/costessey-manorial-court-fts/_local/`.

## Working snippets saved

Generated grids, enhancement sheets, and strips were saved in:

`sources/intake/paleography-staging/snippets/packet-37-costessey-1659-court-opening/`

Most useful files:

- `actual-sxb-grid.png`
- `actual-sxb-right-top-date-sheet.png`
- `actual-sxb-right-default-list-sheet.png`
- `actual-sxb-right-default-list-contact-sheet.png`
- `img-1707-grid.png`
- `img-1708-grid.png`
- `img-1710-grid.png`
- `image-array-probe.json`

## Bottom line

The provided adjacent images do not recover the missing court opening/manor heading. A fresh pull of the preceding ark `3:1:S3HT-6PNK-3Z` succeeded but returned a duplicate of the staged page-304 image, so it does not add a new leaf. The real SXB image confirms the already-known April 1659 default/suit list and supports `John Gurney sen` / `senior`, but it does not name the manor. The phrase `in Burton aforesaid` was not confirmed from the reviewed images.

The likely next image needed is still the true opening immediately before manuscript page 305, but FamilySearch's `3Z`/page-304 path currently returns the same page-304 scan already staged.

## Heading and date

On the actual SXB image, the top of the right page continues an entry from the preceding page. The visible date/context reads in substance:

```text
... and twentieth daye of Aprill in the yeare of our lord one
thousand six hundred fiftie nine ...
... of Anthony Dobbs of Marsham Esq[uire] ...
```

This confirms the April 1659 / Anthony Dobbs of Marsham context, but not the manor name. The wording is a continuation or subsequent memorandum, not a full court opening formula.

The packet-staged context pages 302-304 show ordinary copyhold/admission material and several `At this Court...` formulae, but I did not find a heading of the form "the court leet/baron of [manor] held at [place] for Anthony Dobbs..." on those images.

## Target name-list

The actual SXB right page contains the expected compact name list. The target line still reads best as:

```text
... Richard Knight, John [Burbis?], John Gurney sen, John [...]
```

A few nearby names can be read or partly read, though many are crowded:

```text
... John Windage, John Brereton gent, Edward Tyler, Albert [...]
Wandulff gent, Richard Knight, John [Burbis?], John Gurney sen, John [...]
Gurney jun[?], Thomasine Rookwood, Gregory Moore, Thomas [...]
Gibson, Thomas [ffre?], Wearyard, Edward [...]
```

I would not promote a second Gurney from the crowded list. The secure useful reading remains `John Gurney sen` / `senior`; any possible `Gurney jun[?]`-looking form in the adjacent crowding is too uncertain and may be a different surname or a visual carryover from the target line.

## Answers to packet questions

1. **Manor name:** not recovered. The reviewed images do not show the court opening/manor heading. They confirm the April 1659 and Anthony Dobbs of Marsham context but do not say whether the court was Costessey or another bundled manor.
2. **Suitor/tenant list around John Gurney:** confirmed in substance as `... Richard Knight, John [Burbis?], John Gurney sen, John [...]`. No occupation, residence, or property descriptor is attached to John in the visible list.
3. **Second Gurne/Gurney name or Gurney land:** no secure second Gurney name, junior style, Margaret/William Gurne, or Gurney-land abuttal was found on the reviewed leaves.

## Confidence notes

High confidence:

- The actual SXB image is the local media master `costessey-son-of-john-sxb.jpg`, not the packet-staged `img-1710-3-1-S3HT-6PN9-SXB.jpg`.
- The freshly pulled `3:1:S3HT-6PNK-3Z` image is byte-identical to the packet-staged page-304 image.
- `John Gurney sen` / `senior` is the best reading of the target list item.
- No Gurney parcel, abuttal, surrender, admission, or residence descriptor is visible in the target list.

Medium confidence:

- The visible date/context belongs to an April 1659 court context for Anthony Dobbs of Marsham, esquire.
- The flanking name immediately before John is `John [Burbis?]` or similar.

Low confidence / unresolved:

- The court/manor name.
- The exact court-opening formula.
- The machine-reported `in Burton aforesaid` place token.

## Recommendation

Do not update the Costessey companion's open question yet. The open question should remain: which manor held the April 1659 court for Anthony Dobbs of Marsham?

Before restaging, verify the FamilySearch capture against the manuscript page number and the existing local master. The ordinary preceding-image pull for `3:1:S3HT-6PNK-3Z` duplicates page 304, so the next useful route is a wider browse sequence around the original SXB image in the FamilySearch viewer, looking for another ark or film-image position that actually displays the missing court opening.
