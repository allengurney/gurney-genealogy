# Packet 15 paleography report: Earsham manorial, Hallsty / Syon Gurney

Date of this report: 2026-06-14

## Scope and status

This is a bounded pilot transcription of Packet 15 from the paleography staging README. It covers two Earsham manorial images:

- 15a, `packet15-earsham-tenement-gurneys-hallsty-recital-TZT.jpg`, ark `3:1:S3HY-6XPS-TZT`, 23 April 1811.
- 15b, `packet15-earsham-1719-lyon-gurney-admission-H4R.jpg`, ark `3:1:S3HY-6XP3-H4R`, 16 November 1719.

The 1811 English recital is readable enough for a useful partial result. The 1719 court hand is much harder; I could identify repeated `Syon Gurney` forms, but I could not make a reliable full Latin transcription.

## Working snippets saved

Working crops, grids, contact sheets, enhancement sheets, and manifests were saved in:

`sources/intake/paleography-staging/working-snippets/packet-15-earsham-manorial/`

Most useful generated files:

- `15a-grid.png`
- `15a-full-sheet.png`
- `15a-manual-bands-contact-sheet.png`
- `15a-hallsty-enhancement-sheet.png`
- `15a-hallsty-token-bands-contact-sheet.png`
- `15b-grid.png`
- `15b-full-sheet.png`
- `15b-manual-bands-contact-sheet.png`
- `15b-lyon-zone-enhancement-sheet.png`
- `15b-syon-token-bands-contact-sheet.png`
- `selected-crop-summary.md`

The generated `selected-crop-summary.md` gives the selected crop labels, coordinates, and output paths.

## 15a transcription: Tenement Gurneys / Hallsty recital

Best-effort extract from the relevant English recital:

> To one acre of Copyhold Land of the Tenement Gurneys heretofore of John Plough called Hallsty as it lyes between the lands late of Robert Gooch on the part of the North and the lands formerly of Thomas King on the part of the South and abutts upon the lands late of William Woolmer towards the East and the lands late of Robert Gooch towards the West, which premises were formerly of Robert Woolmer.
>
> And also to one piece of meadow containing by estimation one acre lying in Priest Meadow in Earsham ... as appears at a court held the fourteenth day of October one thousand six hundred and forty five ...

The strongest result is the property phrase:

> one acre of Copyhold Land of the Tenement Gurneys heretofore of John Plough called Hallsty

I read the former holder as **John Plough**, not Clough, though the name should be rechecked before promotion because the image is a later copy/recital and the packet question anticipates Plough/Clough.

## 15a answers

1. The image confirms **Tenement Gurneys** and **Hallsty**.
2. The Hallsty acre is described as one acre of copyhold land, bounded by lands late of Robert Gooch to the north, lands formerly of Thomas King to the south, lands late of William Woolmer to the east, and lands late of Robert Gooch to the west.
3. The recital says the premises were heretofore of **John Plough** and formerly of **Robert Woolmer**.
4. I did not recover the expected 1642 / 1649 / 1654 chain in this crop. The visible older court date I read is **14 October 1645**.
5. The image does not identify the original Gurney holder. It shows a tenement name preserving Gurney ownership/association, but not the transfer from a Gurney to John Plough.

## 15b transcription: 1719 Syon/Lyon Gurney admission

The packet brief calls this a `Lyon Gurney` admission, but the readable name tokens in the image appear to be **Syon Gurney**, not Lyon. Two independent token crops support that reading:

- `15b-syon-token-bands-15b-syon-right.png`
- `15b-syon-token-bands-15b-syon-context-left.png`

Best-effort partial reading of the key name context:

> ... 16 Nov[ember] 1719 ... [tenement / land] ... Syon Gurney ...

and elsewhere:

> ... Syon Gurney ...

The Latin/court-hand text is too dense and degraded for me to produce a reliable full admission or predecessor chain from this pilot pass. I can say the image contains Syon Gurney as a named property/person reference; I cannot confidently say from this pass whether the named Gurney is the admitted tenant, a former holder, or part of a boundary/tenement description.

## 15b answers

1. I do not confirm `Lyon Gurney`; I read the visible name as **Syon Gurney**.
2. I did not recover a secure father/predecessor recital.
3. I did not obtain a full transcription of the admission. The page likely needs either a Latin-specialist pass or a narrower set of page-context crops around the court heading and entry start.

## Confidence notes

High confidence:

- 15a confirms `Tenement Gurneys`.
- 15a confirms the place/name `Hallsty`.
- 15a says the Hallsty acre was heretofore of John Plough.
- 15b contains `Syon Gurney` forms.

Medium confidence:

- 15a's older court date is 14 October 1645.
- 15a's former holder is John Plough rather than John Clough.

Low confidence / needs re-check:

- The full 1719 Latin entry.
- Whether 15b is an admission of Syon Gurney, or a later admission involving land formerly held by Syon Gurney.
- Any bridge from Syon Gurney back to the 1638 John Gurney testator.

## Updated-process feedback

What worked better after the tool changes:

- `bootstrap_python_toolchain.cmd -CheckOnly` avoided the PowerShell execution-policy stumble and completed cleanly.
- `--tile-max-width 700` / `800` made full-page sheets and contact sheets much easier to open and scan.
- `band-ladder` was the right tool for this packet. It let me select answer-bearing bands directly from the grid instead of fighting line segmentation.
- `manifest-summary --selected-only` produced a useful pasteable table for report traceability.

What still needs care:

- Do not run `manifest-summary` in parallel with the crop commands that create its input manifests. It can race the filesystem and fail if the manifests are not written yet.
- `band-ladder` is only as good as the grid-driven boxes selected by the reader; the workflow should still start with a grid.
- For Latin/court-hand entries like 15b, the crop tooling helps with visibility but does not substitute for a specialist reading of the formulae.

Recognition-note decision:

This packet, combined with Packet 17, gives enough evidence for a durable note: in these Earsham/NCC-family manuscript contexts, **Syon/Sion Gurney** is a real target form and can be misread or pre-labeled as **Lyon**. I added that lesson to `recognition-notes.md`.
