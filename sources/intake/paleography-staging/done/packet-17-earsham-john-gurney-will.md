# Packet 17 paleography report: John Gurney of Earsham, Norfolk, yeoman

Date of this report: 2026-06-14

## Scope and status

This is a bounded pilot transcription of the two Packet 17 FamilySearch images for the registered will body of John Gurney of Earsham, Norfolk, yeoman. The reading below is from the page images and generated working crops, not from the machine-transcript snippets.

The main result is strong: the testator is John Gurney of Earsham, yeoman; the will is dated 10 August in the fourteenth regnal year of Charles I (1638); his wife is Mary; his son John is a minor; and the contingent devise names the testator's brother as **Syon Gurney**. I did not obtain a confident reading of every legacy condition, and I did not confidently recover the sister/nephew-William clause suggested by the finding-aid snippet.

## Working snippets saved

Working crops, grids, contact sheets, and manifests were saved in:

`sources/intake/paleography-staging/working-snippets/packet-17-earsham-john-gurney-will/`

Most useful generated files:

- `opening-grid.png`
- `bequests-grid.png`
- `opening-right-upper-contact-sheet.png`
- `opening-right-upper-enhancement-sheet.png`
- `opening-wife-and-legatees-base.png`
- `opening-wife-and-legatees-enhancement-sheet.png`
- `opening-right-lower-continuation-base.png`
- `opening-right-lower-continuation-enhancement-sheet.png`
- `bequests-son-john-syon-brother-base.png`
- `bequests-son-john-syon-brother-enhancement-sheet.png`
- `bequests-right-middle-legacies-base.png`
- `bequests-right-middle-legacies-enhancement-sheet.png`
- `bequests-right-lower-sister-william-base.png`
- `bequests-right-lower-sister-william-enhancement-sheet.png`

The corresponding `*-manifest.md` files in the same folder preserve the crop coordinates.

## Transcription conventions

- Square brackets mark expansions, editorial clarifications, or uncertain readings.
- `y[e]`, `w[hi]ch`, and similar forms preserve common abbreviations.
- Line breaks are approximate.
- I have not silently completed uncertain names or legal phrases from the machine transcript.

## Best-effort transcription

### 17a, image `3WWW`: opening / dating clause

> In the name of God Amen. The tenth day of August in y[e] fourteenth yeare of y[e] Raigne of our Soveraigne Lord Charles by y[e] grace of God of England Scotland France and Ireland King defender of the faith &c. I John Gurney of Earsham in y[e] Countie of Norff[olk], yeoman, being sicke of body but of perfect and sound remembrance, thankes be given to God therefore, doe make and ordaine this my last will and testament in manner and forme following:
>
> First I commend my soule into the mercifull hands of God my maker ...

The opening confirms the README's expected identification: John Gurney of Earsham, Norfolk, yeoman. The date is 10 August, 14 Charles I, which is 10 August 1638.

The next visible clauses include:

> ... my body shall be buried at y[e] discretion of my Executor hereafter in this my will to be named; Item I give & bequeath unto Mary my wife ... during the minority of John Gurney my sonne all those my messuage lands & tenements as well freeholds as copyholds situate lying and being in Earsham aforesaid ...

The central substance is secure: Mary is the wife; John Gurney is the son and a minor; the Earsham estate includes messuage, lands, and tenements, both freehold and copyhold.

### 17b, image `3W7R`: son John / brother Syon contingency

The key contingency reads, best effort:

> ... if y[e] aforesaid John my sonn shall depart this life before he shall accomplish age of one and twenty years then I give & bequeath y[e] said messuage lands tenements unto Syon Gurney my Brother, his heirs [and] assigns forever ...

The brother's forename is best read as **Syon**. I do not read it as Lyon in this crop. The initial letter has the long, looped S form seen elsewhere in the same hand, and the following letters fit `yon`.

The surrounding legacy language is only partially secure. It appears to impose payment conditions on Syon or his heirs/executors/administrators, including payments connected with the testator's sisters/legatees and with named or grouped children. I did not reach a reliable enough reading to name every payee.

The lower-right page also contains enforcement language for unpaid legacies and then names executors:

> ... Item I give & bequeath to my Brother Syon Gurney and my Brother in law John Youngman, Executors of this my last will & testament ...

`John Youngman` is a medium-confidence reading; it should be rechecked before promotion.

## Answers to the packet questions

1. Testator and date: confirmed as John Gurney of Earsham, Norfolk, yeoman; will dated 10 August in 14 Charles I, i.e. 10 August 1638.
2. Opening: confirms sickness of body but sound remembrance; no additional abode beyond Earsham, Norfolk, and the occupation/style `yeoman` is clear.
3. Son John: confirmed as `John my sonn`; he is under 21. Mary is to hold or manage the Earsham messuage/lands/tenements during his minority.
4. Wife: Mary, high confidence.
5. Brother: Syon Gurney, high confidence. This appears to resolve the Lyon/Sion question for this will body in favor of Syon/Sion.
6. Sister / nephew William: not confidently transcribed in this pilot pass. I did not see a secure `William` in the generated crops, and I do not want to promote the snippet's apparent `my Sister, William` language without an image-supported read.
7. Property: the will concerns the testator's messuage, lands, and tenements in Earsham, described as both freehold and copyhold. I did not confidently connect the wording to `Hallsty` or `Tenement Gurneys` in this pilot pass.

## Confidence notes

High confidence:

- John Gurney of Earsham, Norfolk, yeoman.
- Will date: 10 August 1638.
- Wife: Mary.
- Son: John Gurney, a minor under 21.
- Brother: Syon Gurney.
- Property: Earsham messuage, lands, and tenements, both freehold and copyhold.

Medium confidence:

- `John Youngman` as brother-in-law and co-executor with Syon Gurney.

Low confidence / needs re-check:

- Exact payment conditions attached to Syon's contingent devise.
- The sister/nephew-William clause from the finding-aid snippet.
- Whether any wording ties this will directly to Packet 15's Hallsty / Tenement Gurneys.

## Pilot-process feedback

What worked:

- The preflight gave a fast, useful environment check after PowerShell execution policy was bypassed for the process.
- `info` and full-page `grid` were the right starting point. The 500-pixel grid labels made it easy to choose first-pass boxes without coordinate guessing.
- `split-spread` was helpful because both images are two-page spreads and the target text sits on different halves.
- `crop-ladder` was useful for the Syon clause: the broad candidate crop plus nearby shifted crops avoided repeated hand tuning.
- `sheet` was useful for verifying contrast and letterform impressions, especially the Syon/Sion reading.
- The generated manifests are valuable; they make the crops reproducible and should be kept with the staging report until disposition.

What wasted time:

- `crop-ladder --line-strips` over-merged many lines on the dense, slanted register pages. For the opening and right-page bequest sections, it produced one large `line-01` instead of usable line strips.
- Very large 2x contact sheets are useful for reading but slow to open and visually unwieldy. A medium-size contact-sheet option would be better for quick triage.
- The automatic ink-expanded crops sometimes pulled in too much neighboring page/ink for these spreads; they are useful as safety crops but not the best reading images.

Where the tool or skill was unclear:

- The skill says to use `line-strips` and `crop-ladder --line-strips`, but it does not warn that segmentation can fail on slanted/connected register hands and produce one giant strip.
- The workflow would benefit from an explicit "manual banding after failed segmentation" recipe using the same tool, e.g. choose 3-5 horizontal band boxes from the grid and run `crop-ladder` on each.
- It is not obvious whether the preferred output should list every generated file or only selected useful files. This report lists the selected useful outputs and relies on manifests for the rest.

Recommended improvements before the larger batch:

- Add an optional `--max-contact-width` or downsample setting for contact sheets so pilot reviewers can quickly open sheets without losing the full-resolution crops.
- Add a `band-ladder` helper or documented pattern for dense manuscript pages where automatic line segmentation merges lines.
- Add a crop manifest summary command that emits a concise table of selected crop names, boxes, and source image, suitable for pasting into packet reports.
- Consider letting `line-strips` accept an estimated line count or line height to avoid the single-strip failure mode on connected handwriting.

## Recognition-notes decision

A durable recognition lesson probably should be added only after a second confirming packet or re-check: in this NCC registered-will hand, the forename **Syon/Sion** can be misread as **Lyon** when the opening S is faint or looped. This is evidence-tied to Packet 17, but one example is thin; I recommend holding it for now rather than updating `recognition-notes.md` from a single pilot.
