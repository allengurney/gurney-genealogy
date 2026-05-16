# Intake patchset v15 - John Gurney case-file audit cleanup

```yaml
patchset_id: v15
created: 2026-05-09
repo_scope: gurney-genealogy
working_branch: main
phase: phase_1_patchset_only
source_task: "Continuation of Audit John Gurney case file source-completeness/source-lead audit"
primary_case_file: "research/case-files/john-gurney-case-file-v4.md"
primary_research_file: "research/people/g13-john-gurney-fact-sheet.research.md"
phase_2_rule: "Execute the operations below in order. Do not add a source to data/sources.json unless the source has been obtained and is actually used in the Phase 2 edits."
```

## Corrected Source Policy

This patchset intentionally separates source leads from source records.

- Do not add new `data/sources.json` entries for mere leads.
- Do not create `sources/validations/*` files for mere leads.
- Do not cite a lead in research prose until the underlying source has been obtained, reviewed, and used.
- A lead becomes a source only when Phase 2 obtains it and uses it.
- Derivative web profiles may be listed in a future-research lead queue, but should not be promoted to the source registry unless they are actually used as a source.

This corrects the earlier over-broad draft, which would have promoted unpulled leads into source records.

## Scope

This patchset addresses outstanding audit work for the John Gurney case file without prematurely adding source records:

1. Reclassify the open `TAG 10:70-73` lead so it is no longer described as "almost certainly" the source of Anderson's 1636 arrival date.
2. Preserve the Newgate / 1636 / 1615 issue as a high-priority source lead and de-conflation question.
3. Clarify the Phase 2 order: pull sources first, then add source records and case-file prose only for sources actually obtained and used.
4. Add a future-research lead queue for unpulled items rather than registry entries.
5. Keep Candidate A exclusion and Candidate B probability work tied to obtained evidence.

This patchset does not apply the content changes.

## Audit Basis

Local files reviewed:

- `README.md`
- `.claude/CLAUDE.md`
- `.claude/rules/citations.md`
- `.claude/rules/research-case-files.md`
- `.claude/rules/research-writing-style.md`
- `.claude/rules/repo-file-resolution.md`
- `.claude/rules/sources-intake.md`
- `.claude/rules/sources-media.md`
- `.claude/rules/sources-validations.md`
- `.claude/skills/research-intake-prep/SKILL.md`
- `.claude/skills/citation-rigour/SKILL.md`
- `data/sources.json`
- `research/case-files/john-gurney-case-file-v4.md`
- `research/people/g13-john-gurney-fact-sheet.research.md`
- `sources/validations/*`
- `sources/corpus_supplement/*`

Unpulled or not-yet-used leads identified during audit:

- TAG 10:70-73, likely Mary Lovering Holman, "Grissell of the Many Marriages."
- The underlying source behind the derivative tradition that a John Gurney, age 21, had three more years to serve John Newgate of Boston on or about 29 September 1636.
- Winthrop Journal 2:422, cited by Anderson.
- MBCR 1:331, cited by Anderson.
- Suffolk Probate Registry Case #338, cited by Anderson.
- Public/transcribed material about John Newgate of Boston as a feltmaker.
- Derivative compiler/web profiles preserving the Newgate/Handmaid/1615 tradition and related probate or NEHGR leads.

These are leads unless and until Phase 2 obtains and uses them.

## Source-Completeness Findings

### Finding 1 - Anderson's source list needs a pull map, not more source records

`anderson-gmd-2015` records Anderson's John Gurney references as:

- WJ 2:422
- MBCR 1:331
- NEHGR 62:94
- SPR Case #338
- Weymouth Hist 3:251
- TAG 10:70-73

The case file already uses Anderson. v11 already incorporated `history-of-weymouth` and `nehgr-62-94` material. The remaining Anderson-linked items should be handled as a pull map:

- `history-of-weymouth` - already in the registry and incorporated.
- `nehgr-62-94` - already in the registry and incorporated as partial/corroborating material.
- WJ 2:422 - lead to pull.
- MBCR 1:331 - lead to pull.
- SPR Case #338 - lead to pull.
- TAG 10:70-73 - lead to pull; currently over-described as the likely 1636-arrival source.

Do not add placeholder source records for WJ, MBCR, SPR, or derivative Newgate material until those sources are obtained and used.

### Finding 2 - Newgate/1615 tradition is important, but should not be promoted without the underlying source

The G13 research companion already frames the Newgate/1615 tradition as a de-conflation problem. The issue is important because a 1615-born man is difficult to reconcile with the direct-line John's known child chronology and 1653 deposition age. However, the underlying 1636 Newgate/service/apprenticeship source has not been pulled in this audit.

Therefore Phase 2 should not add new case-file claims sourced only to derivative lead material. It should add the Newgate issue to the future-research lead queue, and only promote it into the case-file evidence analysis after the underlying source or a specific obtained derivative source is reviewed and selected for use.

### Finding 3 - TAG 10:70-73 should be reclassified as an open lead

The current case file says TAG 10:70-73 is likely the source of Anderson's 1636 arrival date. That is too strong. Based on the title/context known from the audit, TAG 10:70-73 likely bears on Grissell Fletcher/Kibbee/Gurney and the marriage sequence, but it has not been obtained and should not be used for any specific claim until pulled.

### Finding 4 - Candidate A exclusion should remain evidence-bound

The Newgate/1615 issue can eventually help guard against a two-Johns or composite-source error, but not until the underlying evidence is obtained. Candidate A exclusion should continue to rest on already-used evidence: English chronology/geography, absence of a proved Massachusetts bridge, and the stronger Massachusetts timeline for Candidate B.

## Phase 2 Operations

### 1. Do not add new source records for these leads yet

Do not add source records in this Phase 2 batch for:

- the public/transcribed John Newgate feltmaker item,
- the Genealogical Guide / Savage / Cutter-style derivative Newgate tradition,
- Cybergata or similar derivative web profiles,
- WJ 2:422,
- MBCR 1:331,
- SPR Case #338,
- any other source lead that has not been obtained and used.

If Phase 2 obtains one of these sources and uses it in the case file or G13 companion, then add the corresponding `data/sources.json` entry, validation note, and corpus/media support as part of that same obtained-source intake.

### 2. Revise existing `tag-10-70` note only if keeping it in the registry

`tag-10-70` already exists in `data/sources.json`. Do not expand it into a more complete source record unless the article is obtained.

If the project keeps existing Anderson-cited-but-unpulled items in `data/sources.json`, revise only its `notes` field:

```json
"notes": "Cited by Anderson in the John Gurney sketch. Not yet obtained. Audit correction: do not treat this as the likely source of Anderson's 1636 arrival date until the article is pulled. Current lead hypothesis is that it may support the Grissell Fletcher/Kibbee/Gurney marriage sequence."
```

Do not add `validationPath`, `corpusPath`, or `corpusStatus` changes for `tag-10-70` unless the article has been obtained.

If the project later chooses to remove unpulled lead-only records from `data/sources.json`, handle that as a separate source-registry cleanup batch.

### 3. Update the case-file still-needed language

In `research/case-files/john-gurney-case-file-v4.md`, revise `13.4 What's Still Needed`.

Replace the current TAG item:

```md
1. **TAG 10:70-73** - likely source of Anderson's 1636 arrival date; pull for direct review.
```

with:

```md
1. **TAG 10:70-73** - pull for direct review. Do not assume it is the source of Anderson's 1636 arrival date. The current lead hypothesis is that it may support the Grissell Fletcher/Kibbee/Gurney marriage sequence.
```

Add a new pull item immediately after it:

```md
2. **Newgate / 29 September 1636 service or apprenticeship lead** - identify and pull the underlying source behind the derivative tradition that a John Gurney, age 21, had three more years to serve John Newgate of Boston. Do not use this tradition as direct-line evidence until the underlying source is obtained and reconciled.
```

Renumber the remaining list items.

Do not add new endnotes for these items unless the underlying source is obtained and used.

### 4. Add Anderson reference-control checklist without new source IDs

In `13.4 What's Still Needed`, add this paragraph after the numbered list:

```md
**Anderson reference-control checklist.** Anderson's John Gurney sketch cites WJ 2:422, MBCR 1:331, NEHGR 62:94, SPR Case #338, Weymouth Hist 3:251, and TAG 10:70-73. Weymouth Hist and NEHGR 62:94 have been partially incorporated. The remaining pull targets are WJ 2:422, MBCR 1:331, SPR Case #338, the underlying Newgate 1636 service/apprenticeship source if distinct, and TAG 10:70-73 for the Grissell/marriage-chain question.
```

Do not wrap WJ, MBCR, or SPR in `<code>` source IDs unless those records have been added after obtaining the sources.

### 5. Update G13 research companion without adding new source citations

In `research/people/g13-john-gurney-fact-sheet.research.md`, find the statement that says or implies TAG 10:70-73 is the most likely source feeding Anderson's 1636 date.

Replace it with:

```md
TAG 10:70-73 remains a high-priority pull, but should not be treated as the most likely source for Anderson's 1636 arrival date until obtained. The current lead hypothesis is that it may support the Grissell Fletcher/Kibbee/Gurney marriage sequence. The sharper open targets for the 1636/Boston question are WJ 2:422, MBCR 1:331, SPR Case #338, and the underlying Newgate service/apprenticeship source if distinct.
```

Do not add new source IDs or endnotes for these unpulled leads.

### 6. Create or update a future-research lead queue

Create or update the existing future-research note used for John Gurney leads. If there is no obvious existing file, create:

`research/future-research/john-gurney-source-leads.md`

Add:

```md
## John Gurney source leads from v15 audit

- Pull TAG 10:70-73, likely Mary Lovering Holman, "Grissell of the Many Marriages." Target question: Grissell Fletcher/Kibbee/Gurney and the marriage sequence. Do not use for John Gurney's 1636 arrival unless the article actually says so.
- Identify and pull the underlying source behind the 29 September 1636 Newgate service/apprenticeship tradition for a John Gurney, age 21, with three years remaining to serve John Newgate of Boston.
- Pull Anderson's remaining reference-control targets: WJ 2:422, MBCR 1:331, and SPR Case #338.
- Treat derivative web/compiler profiles as lead indexes only. Convert every useful claim to an obtained source before citing in the case file or adding a source record.
- Side lead: derivative profiles mention Suffolk probate/inventory and NEHGR/Mendon references. Track each as a separate source pull rather than bundling them under a derivative web page.
```

This file is a lead queue, not a source registry substitute.

### 7. Conditional source-promotion rule for later work

When a lead above is actually obtained and used:

1. Add or update the `data/sources.json` record.
2. Create a thin `sources/validations/*` note.
3. Add `sources/corpus_supplement/*` only if the source text is available and an extract is needed.
4. Cite the new source in the case file or G13 companion only after steps 1-3 are complete.
5. Keep derivative/compiler status explicit if the obtained source is not primary.

## Acceptance Checks

After Phase 2 application:

1. Confirm no new `data/sources.json` entry was added for an unobtained lead.
2. Confirm no `sources/validations/*` file was created for an unobtained lead.
3. Confirm every `<code>source-id</code>` added to research prose exists in `data/sources.json` and corresponds to an obtained/used source.
4. Confirm case-file endnotes remain synchronized:
   - every `href="#nNN"` has a matching `<li id="nNN" value="NN">`
   - every endnote backref points to the matching `id="ref-NN"`
   - no duplicated endnote numbers
5. Run:

```powershell
git diff --check
```

6. If site data generation is part of the Phase 2 batch, run the repo's normal validation/package commands from `site/website`.

## Non-Goals

- Do not add source records for leads that have not been obtained and used.
- Do not create validation notes for unobtained leads.
- Do not assert Candidate B's English origin from the Newgate/1615 tradition.
- Do not use derivative web profiles as proof.
- Do not collapse the two-Johns risk into a single clean narrative before the underlying source is pulled.
- Do not claim TAG 10:70-73 has been read until the full article is actually obtained.
