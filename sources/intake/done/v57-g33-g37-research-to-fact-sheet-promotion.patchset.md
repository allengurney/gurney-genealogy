# Intake patchset v57 — G33–G37 research-to-fact-sheet promotion candidates

**Prepared:** 2026-05-24
**Applied:** 2026-05-24 (same session)
**Repo:** `allengurney/gurney-genealogy`
**Target branch:** `main`
**Phase:** 1 (preparation) — now applied directly per user direction.
**Status:** APPLIED. Approved candidates G37-A, G37-B, G35-A, G35-B, G34-A, G34-B, G34-C, G33-A, G33-B, G33-C, G33-D are landed on `main` in both `fact-sheets/` and `site/website/fact-sheets/`. G34-D was a no-op. G36-B was rejected. **G36-A remains unmarked and is pending a user decision.**
**Origin:** In-session review, not from `sources/intake/new/`. No raw intake to archive.

## Application notes
- G37 footnote n12 was occupied at apply-time by an in-session Eulde/Hugues name-equivalence addition; the patchset's G37-B footnote was therefore landed as `n13` rather than `n12`. Body anchor updated accordingly.
- G35-A was approved on the "promote chain to footnote" option (override of the default recommendation); the verbatim text was drafted at apply time and landed as new footnote `n8`, anchored from the Gautier row in the children table.
- G33-A landed as `n12`; G33-B landed as `n13`.
- G34-A, G34-B, G34-C anchored to existing footnotes (`n5`, `n5`, `n2`) — no renumbering required.
- G33-D appended into existing `n7`.
- G33-C added one Timeline row and one narrative sentence; no new footnote.
- No `data/sources.json` changes were made in this application; the proposed entries (`palmer-perlustration-yarmouth-1872`, `decorde-essai-canton-gournay-1861`, `powell-historie-cambria-1584`, `guillaume-de-poitou-gesta`, `histoire-chronique-normandie-1610`, `dumoulin-histoire-generale-normandie-1631`) remain to be reconciled in a follow-up sources pass.

## Scope

For ancestors G33–G37 (Hugh III through Eudes), review the paired research companion files in `research/people/` against the published fact sheets in `fact-sheets/` and identify substantive findings that meet the fact-sheet promotion standard:

- claim is durable enough for publication
- evidence is strong enough or appropriately phrased
- confidence level can be set honestly
- a future reader can trace the support quickly

Per the user direction in this session, the patchset proposes each candidate for explicit approval rather than promoting in bulk. Phase 2 will apply only approved candidates.

Out of scope for this patchset: writing-style corrections, footnote renumbering, repo-vocabulary cleanup, acronym expansion, and the G35→G34 ordinal-numbering move — all of those are precision edits applied directly to `main` ahead of this patchset.

## Sources / data referenced

All candidates anchor to existing or proposed `data/sources.json` entries already documented in the research companions:

- `dg-rec-pt1`, `dg-rec-supp` — Daniel Gurney 1848 and Supplement 1858
- `three-hundred-years-norman-house` — Hannay 1867
- `pattou-racines-histoire-gournay-2025` — Étienne Pattou, *Racines Histoire*
- `fmg-medlands-normacre` — Foundation for Medieval Genealogy MedLands (Cawley)
- `potin-recherches-ville-gournay-1842`, `nrp-recherches-possessions-1852`
- `painchault-gaillefontaine-2012` (PURH)
- `decorde-essai-canton-gournay-1861` — Decorde, *Essai…sur le Canton de Gournay*
- `powell-historie-cambria-1584` — Powell's *Historie of Cambria*
- `chron-beccensis-abbatiae` (proposed), `anselm-opera-schmitt` (proposed)
- `wace-roman-de-rou` (proposed)

No new `sourceId` entries are required for the candidates below; the proposed entries above are already used in research and would be promoted as part of the candidate adoption.

## How to read each candidate

Each candidate has:

- **Source in research:** which research-companion section the finding comes from.
- **Why promote:** the reader value.
- **Proposed location:** where it would go on the fact sheet (Highlight, Narrative, Vitals, footnote, or Timeline row).
- **Proposed text (verbatim):** exact markup to insert if approved.
- **Approval gate:** explicit `[ ] APPROVED / [ ] REJECTED / [ ] DEFER` line for the user.

---

## G37 — Eudes de Gournay

### Candidate G37-A — The two-arms heraldic history

**Source in research:** `g37-eudes-de-gournay-fact-sheet.research.md` §2.4 (the "écu noir" tradition).

**Why promote:** The current fact sheet has a strong "knight with the black shield" highlight (Highlight 5). The research adds a concrete, visible piece of supporting evidence — the original *sable plein* arms remained on Gournay town's civic escutcheon long after the family adopted new arms under Hugues V (c. 1190s). The 1844 NRP de la Mairie engraving series explicitly labels the two phases "Premières armoiries" and "Secondes armoiries." This makes the legend more than a romantic tag — it leaves a physical footprint that survives today.

**Proposed location:** Extend Highlight 5 with one additional sentence.

**Proposed text (replacement for Highlight 5, additions in *italic* in this diff only):**

```html
<li><strong>Eudes — "the knight with the black shield."</strong> A French local history tradition describes Eudes as <em>"le chevalier à l'écu noir"</em> — the knight with the black shield. The Gournay arms were later recorded as <em><a href="https://en.wikipedia.org/wiki/Sable_(heraldry)">pure sable</a></em> (a plain black shield), one of the simplest and most ancient <a href="https://en.wikipedia.org/wiki/Heraldry">heraldic</a> designs in Norman genealogy, consistent with an origin before the formalisation of heraldry. The original black shield remained on Gournay-en-Bray's civic arms even after the family itself adopted a new device — an engrailed red cross on silver — under Hugues V around the 1190s; the 1844 N.-R. P. de la Mairie engraving series explicitly contrasts the two phases as "Premières armoiries" and "Secondes armoiries." <sup class="fn"><a href="#n10" id="ref-10">10</a></sup></li>
```

**Footnote n10 update (append to existing):**

```html
<li id="n10">"Les remparts de Gournay-en-Bray" (remparts-de-normandie.eklablog.com): "Eudes, le chevalier à l'écu noir, prend possession de ses terres en 912." Traditional Gournay arms were <em>pure sable</em> (plain black shield) per Daniel Gurney, <em>Record</em>, Part I (1848), p. 79. Étienne Pattou, <em>Racines Histoire</em>, "Seigneurs de Gournay," p. 1, records the heraldic origin as "Gournay (origine): «De sable plein»" — plain black — and notes that the family later adopted "D'argent, à une croix engrelée de gueules" (argent, an engrailed cross gules) under Hugues V c. 1190s, the device that was carried into England. N.-R. P. de la Mairie's 1844 engraving series, reproduced in Pattou pp. 16–17, contrasts the two as "Premières armoiries" (original sable) and "Secondes armoiries des Sires Normands de Gournay" (engrailed cross). Source IDs: <code>pattou-racines-histoire-gournay-2025</code>, <code>nrp-recherches-possessions-1852</code>. <a class="citation-back" href="#ref-10">↩</a></li>
```

**Approval gate:** `[X] APPROVED  [ ] REJECTED  [ ] DEFER`

---

### Candidate G37-B — The Cordier MS provenance chain

**Source in research:** `g37-eudes-de-gournay-fact-sheet.research.md` §2.2 + §8 open question 1.

**Why promote:** The fact sheet's Highlight 3 currently grounds Eudes in "tradition" without making the chain of transmission visible. Showing the chain (Cordier c. 1710–1738 → Langloys → René Potin → Pierre Potin 1842 → DG 1845) lets a reader judge the depth of the tradition rather than treat it as floating. Belongs in a footnote, not in the body.

**Proposed location:** New footnote `n12` appended to the existing list, anchored from Highlight 3's "no document survives" clause.

**Proposed text — body change:**

Edit Highlight 3 last sentence from:

```html
<a href="https://en.wikipedia.org/wiki/L%C3%A9opold_Delisle">Léopold Delisle</a>, the leading 19th-century Norman charter scholar, challenged Daniel Gurney's early genealogy — but the challenge itself confirms that no document survives. The name rests on tradition; the person behind it almost certainly existed. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup>
```

to:

```html
<a href="https://en.wikipedia.org/wiki/L%C3%A9opold_Delisle">Léopold Delisle</a>, the leading 19th-century Norman charter scholar, challenged Daniel Gurney's early genealogy — but the challenge itself confirms that no document survives. The name rests on tradition; the person behind it almost certainly existed. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup><sup class="fn"><a href="#n12" id="ref-12">12</a></sup>
```

**Proposed text — new footnote n12 (append to citation list):**

```html
<li id="n12">The chain of transmission for the Eudes tradition is reconstructible: Nicolas Cordier, curé of Notre-Dame de Gournay 1710–1738, wrote a manuscript <em>Histoire de Gournay</em>; from him the tradition passed through Langloys (an avocat, late 17th century), René Potin, and Pierre Potin de la Mairie, who printed it in <em>Recherches historiques sur la ville de Gournay-en-Bray</em> (1842). Daniel Gurney drew on the same chain for his <em>Record</em> in 1845. The chain is recoverable but each link is a local-tradition transmission, not a primary medieval document. <a class="citation-back" href="#ref-12">↩</a></li>
```

**Approval gate:** `[X] APPROVED  [ ] REJECTED  [ ] DEFER`

---

## G36 — Hugh de Gournay I

### Candidate G36-A — The Gournay–La Ferté–Gaillefontaine frontier triad

**Source in research:** `g36-hugh-de-gournay-i-fact-sheet.research.md` §2.4 (Painchault 2012).

**Why promote:** The current fact sheet treats Hugh I's fortifications as a single-site achievement (La Tour Hue). Painchault's 2012 archaeological survey reframes the work as one corner of a *triad* of fortresses at the head of the Bresle valley — Gournay, La Ferté, and Gaillefontaine — held by the Gournay seigneurie at the Normandy/France frontier. This is a genuinely new strategic context that is not in the fact sheet but is well-sourced and concrete.

**Proposed location:** New Highlight bullet, fourth in the Highlights list, before the existing William Longsword bullet.

**Proposed text (new highlight bullet, to insert after the current third bullet):**

```html
  <li><strong>One fortress of a frontier triad.</strong> Hugh's citadel at Gournay was not isolated. The family seigneurie controlled the head of the <a href="https://en.wikipedia.org/wiki/Bresle">Bresle valley</a> through a coordinated triad of fortresses — Gournay, La Ferté (built by his grandson Gautier's branch by year 1000), and Gaillefontaine (forteresse from c. 1050) — pinning the eastern Norman border against the kingdom of France. Modern archaeology frames the three together as "a political stake of the first order on both the French and the Norman side." <sup class="fn"><a href="#n5" id="ref-5c">5</a></sup></li>
```

(Footnote n5 already covers Painchault 2012; no new footnote required.)

**Approval gate:** `[X] APPROVED  [ ] REJECTED  [ ] DEFER`

---

### Candidate G36-B — Hugh I → Hugh II succession as editorial inference

**Source in research:** `g36-hugh-de-gournay-i-fact-sheet.research.md` §5 (Potin 1842 p. 89).

**Why promote:** Potin's candid acknowledgment — "Nor is it known whether his successor was his son; I think so, however" — is the deepest local-tradition acknowledgment that the Hugh I → Hugh II link is editorial inference, not documented. A reader trusting the family-tree shape deserves to see this honestly. Belongs in a footnote, not the body.

**Proposed location:** Extend existing footnote `n2` (the "Active generation estimated" footnote) with an additional sentence.

**Proposed text — replace existing footnote n2:**

```html
<li id="n2">No death date in any source. Active generation estimated c. 960–1000 based on son Renaud's documented dates. The Hugh I → Renaud succession itself is editorial inference rather than documented: Pierre Potin de la Mairie, <em>Recherches historiques sur la ville de Gournay-en-Bray</em> (1842), p. 89, candidly writes, "Nor is it known whether his successor was his son; I think so, however." The repo treats them as father and son following Potin's editorial position. <a class="citation-back" href="#ref-2">↩</a></li>
```

**Approval gate:** `[ ] APPROVED  [X] REJECTED  [ ] DEFER`

---

## G35 — Renaud de Gournay

### Candidate G35-A — La Ferté reversion to senior line (Hugues II de la Ferté)

**Source in research:** `g35-renaud-de-gournay-fact-sheet.research.md` §8.

**Why promote:** The current Gautier row in the Children table already mentions the reversion ("his line ended with his great-grandson Hugues II de la Ferté"). The research has the full chain (Gauthier → Turold → Hugues I de la Ferté → Hugues II) and the precise reversion path back to Hugues III (G33) and Girard (G32). A reader curious about how a cadet line reattaches deserves the chain — but this may be more research-tier detail than fact-sheet warrants.

**Recommendation:** Leave in research only. The current one-line reversion mention on the fact sheet is sufficient.

**Approval gate:** `[X] APPROVED (promote chain to footnote)  [ ] REJECTED (keep in research only — default)  [ ] DEFER`

---

### Candidate G35-B — Witness identification of "a count also named Robert"

**Source in research:** `g35-renaud-de-gournay-fact-sheet.research.md` §2.2 (NRP-I 1852).

**Why promote:** The current Highlight 1 lists witnesses but flags "a count also named Robert" without identification. NRP-I 1852 p. 77–78 makes the identification more concrete: probably Robert Comte d'Évreux, the brother of the Archbishop in his secular role.

**Proposed location:** Edit Highlight 1 — replace "a count also named Robert" with a more specific identification, footnote-anchored.

**Proposed text — replace in Highlight 1:**

From:
```
Witnesses: Duke Richard I (Sans-Peur), his son Richard II, Robert Archbishop of Rouen, a count also named Robert, and a dedicating Bishop named Hugues.
```

To:
```
Witnesses: Duke Richard I (Sans-Peur), his son Richard II, Robert Archbishop of Rouen, a Count Robert (probably Robert, Count of Évreux, the Archbishop's brother in his secular role), and a dedicating Bishop named Hugues.
```

**Approval gate:** `[X] APPROVED  [ ] REJECTED  [ ] DEFER`

---

## G34 — Hugh de Gournay II

### Candidate G34-A — The Eulde/Hugues name equivalence in chronicles

**Source in research:** `g34-hugh-de-gournay-ii-fact-sheet.research.md` §3.1.

**Why promote:** This is one of the most interesting textual findings in the companion. Two chronicles narrating the *same* event — the 1054 Mortemer command — name the Lord of Gournay differently: *l'Histoire et Chronique de Normandie* writes "Eulde, seigneur de Gournay" where Dumoulin writes "Hugues de Gournay." This is direct textual evidence for Hannay's observation that Hugh and Eudes were interchangeable Norse-derived names in early Norman usage — and it explains why FamilySearch's family-tree label conflates the two ("Eudes ou Hugues de Gournay"). Concrete, sourced, and quietly amusing for a reader.

**Proposed location:** New Highlight bullet, inserted after the existing Mortemer highlight (currently Highlight 1).

**Proposed text (new highlight bullet):**

```html
  <li><strong>Hugh — or Eulde? Two chronicles, one battle, two names.</strong> The 1054 Mortemer story is told by two Norman chronicles that disagree on the lord of Gournay's name. Gabriel Dumoulin's <em>Histoire générale de Normandie</em> (1631) calls him "Hugues de Gournay." The earlier <em>Histoire et Chronique de Normandie</em> (printed Rouen 1610) calls him "Eulde, seigneur de Gournay." Hannay observed that in this era Hugh's name "was convertible with Eudes or Eude" — the two Norse-derived names were interchangeable, and writers two centuries removed from the events could pick either. <sup class="fn"><a href="#n5" id="ref-5d">5</a></sup></li>
```

(Footnote n5 already cites both chronicles; no new footnote required.)

**Approval gate:** `[X] APPROVED  [ ] REJECTED  [ ] DEFER`

---

### Candidate G34-B — William of Poitou primary-source corroboration

**Source in research:** `g34-hugh-de-gournay-ii-fact-sheet.research.md` §3.2.

**Why promote:** William of Poitou — the Conqueror's own biographer — records "Hugonis Gornacensis" allied with "Roberti Aucensis comitis" (Robert d'Eu), the same Robert who commanded at Mortemer. This is named-source attestation in an independent primary text from the Conqueror's circle. It strengthens Hugh II's Mortemer-era footing significantly over Norman-chronicle-only sourcing.

**Proposed location:** Append to existing footnote `n5` (the Mortemer footnote).

**Proposed text — append to existing footnote n5 (after the current "Franceiz, levez" attribution):**

```
Independently corroborated by William of Poitou (Guillaume de Poitiers), the Conqueror's own biographer: his <em>Gesta Guillelmi</em> (ed. Davis & Chibnall, Oxford Medieval Texts, 1998) records "Hugonis Gornacensis" allied with "Roberti Aucensis comitis" — Robert d'Eu, the same Robert who commanded the Norman force at Mortemer — in the period after 1053. Source ID: <code>guillaume-de-poitou-gesta</code>; cross-referenced at Foundation for Medieval Genealogy MedLands [889].
```

**Approval gate:** `[X] APPROVED  [ ] REJECTED  [ ] DEFER`

---

### Candidate G34-C — Powell 1584 Welsh-chronicle parallel of the "Cardiff" tradition

**Source in research:** `g34-hugh-de-gournay-ii-fact-sheet.research.md` §6.7.

**Why promote:** This is the most consequential research finding for G34 not yet on the fact sheet. David Powell's *Historie of Cambria* (1584), continuing Humphrey Llwyd's translation of *Brut y Tywysogion*, places a near-identical name list (Roger of Montgomery, Néel le Vicomte, Arnoult de Harcourt, "Hue de Gournay" wounded and dying in Normandy, the Count of Évreux likewise wounded) at a battle between Cardiff and Brecknock — but in **1094**, not 1074. The Welsh and French traditions are textually independent; their convergence on the same name list at different dates is diagnostic: the legend was free-floating, and each chronicle community attached it to a date plausible in its own framing. This is genuinely new framing that the current "Cardiff was probably Norwich" footnote can absorb.

**Proposed location:** Append to existing footnote `n2` (the Cardiff death-tradition footnote).

**Proposed text — append to existing footnote n2 (after the current Hannay quote):**

```
A textually independent Welsh chronicle tradition transmits a near-identical name list at a different date: David Powell, <em>The Historie of Cambria, now called Wales</em> (London, 1584), continuing Humphrey Llwyd's translation of <em>Brut y Tywysogion</em>, records under the year 1094 that "Roger Montgomery, Earl of Salop and Arundell, William Fitz-Eustace, Earl of Gloucester, Arnold de Harcourt and Neale le Vicount were slain between Cardiff and Brecknock by the Welshmen; also Walter Evereux, Earl of Sarum, and Hugh Earl Gourney were there hurt, and died after in Normandy." The same wounded-at-a-Welsh-battle, died-in-Normandy template attaches to the same name list — but transposed by twenty years. The convergence is diagnostic: the legend appears to have been free-floating, with the French tradition attaching it to the 1074–75 Earls' Revolt and the Welsh tradition attaching it to the 1093–95 Welsh frontier campaigns. Source ID: <code>powell-historie-cambria-1584</code>.
```

**Approval gate:** `[x] APPROVED  [ ] REJECTED  [ ] DEFER`

---

### Candidate G34-D — Bayeux "Brenerias"/Bernières and Saint-Benoît-sur-Loire charters

**Source in research:** `g34-hugh-de-gournay-ii-fact-sheet.research.md` §5.

**Why promote:** Footnote n7 already enumerates four charter witnesses. The research adds nothing materially new beyond what is already in n7. **Recommend leave in research.**

**Approval gate:** `[X] APPROVED (no-op)  [ ] REJECTED  [ ] DEFER`

---

## G33 — Hugh de Gournay III

### Candidate G33-A — Caister and Cantley tithes given to Saint-Hildevert

**Source in research:** `g33-hugh-de-gournay-iii-fact-sheet.research.md` §5.3.

**Why promote:** A documented Channel-spanning ecclesiastical link not currently in the fact sheet: Hugh III gave the tithes of Caister and Cantley (Norfolk) to the Saint-Hildevert chapter at Gournay-en-Bray, confirmed by the Bishop of Norwich. Saint-Hildevert held those English-parish tithes through to the Hundred Years War. This is concrete, well-sourced, and rich in reader value — it shows the family treating England and Normandy as a single estate, with their home Norman collégiale drawing income from East Anglia.

**Proposed location:** New Highlight bullet between the existing "Caen abbeys" and "Beauvaisis 24 villages" bullets.

**Proposed text (new highlight bullet):**

```html
  <li><strong>His Norfolk manors paid tithes to a Norman church — for centuries.</strong> Hugh granted the tithes of Caister and Cantley in Norfolk to the chapter of <a href="https://en.normandie-tourisme.fr/museums-and-heritage-sites/collegiale-saint-hildevert/">Saint-Hildevert</a> at Gournay-en-Bray, the home collégiale of his ancestors. The grant was confirmed by the Bishop of Norwich and the chapter continued to receive the English tithes through to the Hundred Years War — an ecclesiastical thread tying the Norfolk barony directly to the Pays de Bray for roughly three centuries. <sup class="fn"><a href="#n12" id="ref-12">12</a></sup></li>
```

**Proposed text — new footnote n12 (append to citation list):**

```html
<li id="n12">Pierre Potin de la Mairie, <em>Recherches historiques sur la ville de Gournay-en-Bray</em> (1842), p. 110: the tithes of Caister and Cantley (Norfolk) given by Hugh de Gournay to the Saint-Hildevert chapter at Gournay-en-Bray, confirmed by the Bishop of Norwich; the chapter retained those tithes until the Hundred Years War. The Caister manor itself came into the family by 1075–76 forfeiture redistribution after the East Anglian earls' revolt (Charles John Palmer, <em>The Perlustration of Great Yarmouth</em>, 1872). Source IDs: <code>potin-recherches-ville-gournay-1842</code>, <code>palmer-perlustration-yarmouth-1872</code> (proposed). <a class="citation-back" href="#ref-12">↩</a></li>
```

**Approval gate:** `[X] APPROVED  [ ] REJECTED  [ ] DEFER`

---

### Candidate G33-B — Boshyon (Bosc-Hyons) — the *Boscus Hugonis* toponym

**Source in research:** `g33-hugh-de-gournay-iii-fact-sheet.research.md` §2.13 (Decorde 1861 Jumièges 1082 charter).

**Why promote:** A quietly satisfying historical fingerprint: the modern commune of Bosc-Hyons preserves the name *Boscus Hugonis* — "Hugh's wood" — almost certainly named for Hugh I de Gournay, and used as a Gournay-family endowment base from 1082 (Hugh III and Basilea ratifying a 190-arpent donation to Jumièges) through to a 1195 oat-mill endowment for an altar lamp at Saint-Hildevert. A toponym that is a thousand years old and still on the map is the kind of detail this site does well.

**Proposed location:** New short Highlight bullet near the bottom of the list, or as an addition to the Beauvaisis villages bullet.

**Proposed text (new short highlight bullet):**

```html
  <li><strong>His name is still on the map.</strong> The modern Seine-Maritime commune of <a href="https://fr.wikipedia.org/wiki/Bosc-Hyons">Bosc-Hyons</a> preserves <em>Boscus Hugonis</em> — "Hugh's wood" — almost certainly named for Hugh I de Gournay, the fortifier. In 1082 Hugh III and Basilea ratified a 190-arpent donation of land at Boshyon to the abbey of Jumièges by their vassal Raoul Havot; the same place would be used as a Gournay endowment base for at least another century. <sup class="fn"><a href="#n13" id="ref-13">13</a></sup></li>
```

**Proposed text — new footnote n13 (append to citation list):**

```html
<li id="n13">J.-E. Decorde, <em>Essai historique et archéologique sur le Canton de Gournay</em> (Paris: Derache and Didron; Rouen: Lebrument, 1861), Boshyon parish entry: 1082 ratification by Hugh III and Basilia of Raoul Havot's 190-arpent donation at <em>apud villam quæ vocatur Hugonis silva</em> ("at the village called Hugh's wood") to the abbey of Jumièges. The toponym recurs in two later Gournay-side endowments: in 1164 Hugues IV and Mélisende assign grain rents from their Boshyon manor to the new church of Gaillefontaine; in 1195 the Boshyon mill is endowed by Manassès de Bully to fund a perpetual altar lamp before St Hildevert's relic at the Gournay collegiate church. Detailed place narrative: `research/places/bosc-hyons.md`. Source ID: <code>decorde-essai-canton-gournay-1861</code>. <a class="citation-back" href="#ref-13">↩</a></li>
```

**Approval gate:** `[X] APPROVED  [ ] REJECTED  [ ] DEFER`

---

### Candidate G33-C — 1067 Saint-Benoît-sur-Loire as earliest datable Hugh III appearance

**Source in research:** `g33-hugh-de-gournay-iii-fact-sheet.research.md` §6.4.

**Why promote:** The fact sheet's Timeline begins Hugh III's documentary trail at 1076 (the Bec tithe grant). The 1067 Saint-Benoît-sur-Loire confirmation pushes the trail back nine years and places him in the Conqueror's documented entourage in the spring immediately after Hastings. Small, factual, sourced.

**Proposed location:** New row in the sidebar Timeline; brief mention in narrative.

**Proposed Timeline insertion (between current "14 Oct. 1066" and "1076" rows):**

```html
      <tr><td>Apr. 1067</td><td>Subscribes William's confirmation of rights to the abbey of Saint-Benoît-sur-Loire — earliest datable charter appearance.</td></tr>
```

**Proposed narrative addition** (one sentence in the "His post-Conquest rewards" paragraph, before the existing 1076 mention):

```
Hugh's name first appears in a datable charter in April 1067, subscribing King William's confirmation of rights to the abbey of <a href="https://en.wikipedia.org/wiki/Fleury_Abbey">Saint-Benoît-sur-Loire</a> — placing him in the king's documented entourage in the spring immediately after Hastings.
```

(Anchors to existing footnote n3, which already cites Daniel Gurney's *Record* pp. 25–27 for charter witnessing.)

**Approval gate:** `[X] APPROVED  [ ] REJECTED  [ ] DEFER`

---

### Candidate G33-D — Beauvaisis "Conquêts" as a recognised legal-historical institution

**Source in research:** `g33-hugh-de-gournay-iii-fact-sheet.research.md` §5.5 (Vallez 1970 / Basnage / Lemoine 2006).

**Why promote:** The "Conquêts Hue de Gournai" highlight currently treats the 24 Beauvaisis villages as a one-off acquisition. The research adds that this acquisition was so distinctive that the *Coutume de Normandie* commentary tradition recognised "conquêts Hue de Gournay" as a named legal-historical institution into the 19th century (Basnage's commentary, traced by Vallez 1970). This is a strong "still echoes today" detail — but it may be too legal-history-dense for a fact-sheet reader.

**Recommendation:** Add as a one-sentence footnote enrichment to existing n7, not as a new highlight.

**Proposed text — append to existing footnote n7:**

```
The phrase "<em>conquêts Hue de Gournay</em>" was sufficiently distinctive that it was recognised as a named legal-historical institution in the <em>Coutume de Normandie</em> commentary tradition: Basnage's <em>Commentaire sur la coutume de Normandie</em>, vol. II, "Additions et usages locaux," pp. 3–4, was still citing the term in the early 18th century, and Vallez's 1970 study (<em>Revue historique de droit français et étranger</em>, 4e série, no. 48, p. 353) traces it into 19th-century legal scholarship.
```

**Approval gate:** `[X] APPROVED  [ ] REJECTED  [ ] DEFER`

---

## Summary table

| Candidate | Ancestor | Type | Recommended |
|---|---|---|---|
| G37-A | Eudes | Highlight enrichment + footnote (two-arms heraldic history) | **Promote** |
| G37-B | Eudes | Footnote (Cordier MS chain) | **Promote** |
| G36-A | Hugh I | New Highlight (fortress triad) | **Promote** |
| G36-B | Hugh I | Footnote (succession is editorial inference) | **Promote** |
| G35-A | Renaud | Footnote (La Ferté reversion chain) | Keep in research |
| G35-B | Renaud | Highlight edit (Count Robert identification) | **Promote** |
| G34-A | Hugh II | New Highlight (Eulde/Hugues name equivalence) | **Promote** |
| G34-B | Hugh II | Footnote (William of Poitou corroboration) | **Promote** |
| G34-C | Hugh II | Footnote (Powell 1584 Welsh-chronicle parallel) | **Promote** |
| G34-D | Hugh II | (No-op — already covered in n7) | No change |
| G33-A | Hugh III | New Highlight + footnote (Caister/Cantley tithes to Saint-Hildevert) | **Promote** |
| G33-B | Hugh III | New Highlight + footnote (Bosc-Hyons toponym) | **Promote** |
| G33-C | Hugh III | Timeline row + narrative sentence (1067 Saint-Benoît) | **Promote** |
| G33-D | Hugh III | Footnote enrichment (Coutume de Normandie recognition) | **Promote** |

## Phase 2 application notes

When approved candidates are applied:

1. Apply each candidate exactly as the proposed text above shows, preserving footnote numbering offsets where new footnotes are added.
2. Mirror every fact-sheet edit to `site/website/fact-sheets/`.
3. For G33-B, also confirm `research/places/bosc-hyons.md` exists or stub it.
4. For G33-A, confirm or add `palmer-perlustration-yarmouth-1872` as a `data/sources.json` entry.
5. No `data/ancestors v26.json` changes are required by any candidate.
6. After application, run any site validation step that catches stale `.html` links, missing canonicals, or broken footnote anchors.
