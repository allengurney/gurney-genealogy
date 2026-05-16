# v09 patchset - 1066.co.nz Gurney/Gournay texts

Status: applied in the same pass on branch `codex/1066-gurney-gournay-intake`.

## Intake sources

Archived raw user-supplied markdown:

- `sources/intake/archive/v09-1066-gournay-texts/THE CONQUEROR AND HIS COMPANIONS.md`
- `sources/intake/archive/v09-1066-gournay-texts/The History of England and Normandy.md`
- `sources/intake/archive/v09-1066-gournay-texts/Introduction-Roll of Battle Abbey.md`

Add source records:

- `planche-conqueror-companions-1874`
- `palgrave-history-england-normandy-1864`
- `cleveland-battle-abbey-roll-introduction`

Add corpus supplements:

- `sources/corpus_supplement/planche-conqueror-companions-hugh-de-gournay.md`
- `sources/corpus_supplement/palgrave-history-england-normandy-gournay-extracts.md`
- `sources/corpus_supplement/cleveland-battle-abbey-roll-introduction-gurnay.md`

Add validations:

- `sources/validations/planche-conqueror-companions-1874.md`
- `sources/validations/palgrave-history-england-normandy-1864.md`
- `sources/validations/cleveland-battle-abbey-roll-introduction.md`

## Apply commands

1. In `research/people/g34-hugh-de-gournay-ii-fact-sheet.research.md`, add Planché and Palgrave material to the 1035/Mortemer/Hastings/Cardiff working notes:
   - Planché reinforces the 1035 expedition with Walter Giffard.
   - Planché lists Hugh among the Mortemer commanders.
   - Planché preserves the three-Gournay-at-Hastings problem and keeps the generational assignment cautious.
   - Planché preserves a Welsh/Powell Cardiff/Brecknock wounded-Hugh tradition while rejecting the garbled 1074 French version.
   - Palgrave supplies Pays de Bray context for Hugh's weight at Mortemer.
2. In `research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md`, add:
   - Palgrave's Gerberoi geography and mediation list.
   - Planché's Basilia Flaitel description and warning against flattening the Hastings roll forms.
3. In `research/people/g32-gerard-de-gournay-fact-sheet.research.md`, add Planché's Gerard material:
   - Evreux/Conches command under William Rufus.
   - Ecouchi held by Gerard.
   - Gundred/Nigel de Albini/Mowbray collateral.
   - Edith de Warenne's second marriage to Drogo/Dreux de Monceaux and the Dunstable charter witness note.
4. In `research/people/g36-hugh-de-gournay-i-fact-sheet.research.md`, add Planché's fortification summary for Hugh son of Eudes and La Tour Hue.
5. In `research/people/g35-renaud-de-gournay-fact-sheet.research.md`, add Planché's Renaud/Alberada/Gautier/La Ferté charter summary and the caution that Wace's Sire de la Ferté at Hastings should not be identified as this cadet Gournay line without stronger evidence.
6. In `research/people/g37-eudes-de-gournay-fact-sheet.research.md`, add Planché's Le Brai founding tradition and preserve the documentary caution.
7. In `research/places/gournay-en-bray.md`, add Planché/Palgrave Pays de Bray setting material.
8. In `research/places/la-ferte-en-bray.md`, add Planché's La Ferté cadet-line caution.
9. In `research/places/beauvaisis-frontier-acquisitions.md`, add Planché's De la Marie wording for the Conquets Hue de Gournay as independent support for the left-bank/eastern-Epte acquisition framing.
10. In `research/topics/anderson-yvery-harpetre-gournay-collateral.md`, add a 1066.co.nz comparison-source section for Planché, Palgrave, and the Battle Abbey Roll introduction, including Gurnay/Gurney spelling variants and the duplicated Hue/earl title caution.

## Validation commands

Run repository/site validation after applying:

- `node -e "JSON.parse(require('fs').readFileSync('data/sources.json','utf8')); console.log('sources ok')"`
- from `site/website`: `npm.cmd run validate`
- from `site/website`: `npm.cmd run build`
