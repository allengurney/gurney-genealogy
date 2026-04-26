---
layout: layouts/base.njk
permalink: false
# Copy this file into `fact-sheets/`, rename it using g##-normalized-name-fact-sheet.md,
# and assign a real permalink such as /fact-sheets/g14-francis-gurney-fact-sheet.html.
title: Ancestor Name Fact Sheet
pageHeading: Ancestor Name (Birth–Death)
subtitle: "Ancestor fact sheet for G## in the direct Gurney line. One-sentence identity summary. Published MONTH YEAR."
description: "Compact fact sheet for Ancestor Name in the direct Gurney line."
bodyClass: bio-page factsheet-page
updated: 2 April 2026
factsheet:
  gen: G##
  slug: g##-normalized-name-fact-sheet
  personName: Ancestor Name
  heroImage: /media/factsheets/g##-normalized-name-hero.png
  heroAlt: Historical image or associated site for Ancestor Name
  heroCaption: One-sentence caption.
  heroCredit: Source/credit note.
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfilePage",
  "name": "{{ factsheet.personName }} — Fact Sheet",
  "description": "{{ description }}",
  "mainEntity": {
    "@type": "Person",
    "name": "{{ factsheet.personName }}",
    "birthDate": "",
    "deathDate": "",
    "birthPlace": { "@type": "Place", "name": "" },
    "deathPlace": { "@type": "Place", "name": "" },
    "description": ""
  }
}
</script>

<div class="factsheet-top">
  <div class="factsheet-main">

<section class="fact-section fact-section-vitals" id="vital-records">
<div class="facts-vitals-grid">
  <div class="fact-item">
    <div class="fact-label">Born</div>
    <div class="fact-value">Replace with birth details. <sup class="fn"><a href="#n1" id="ref-1">1</a></sup></div>
  </div>
  <div class="fact-item">
    <div class="fact-label">Died</div>
    <div class="fact-value">Replace with death details. <sup class="fn"><a href="#n2" id="ref-2">2</a></sup></div>
  </div>
  <div class="fact-item">
    <div class="fact-label">Occupation / Education / Religion</div>
    <div class="fact-value">Replace with concise occupational and religious summary. <sup class="fn"><a href="#n4" id="ref-4">4</a></sup></div>
  </div>
  <div class="fact-item">
    <div class="fact-label">Buried</div>
    <div class="fact-value">Replace as needed. <sup class="fn"><a href="#n3" id="ref-3">3</a></sup></div>
  </div>
  <div class="fact-item fact-item-span-2">
    <div class="fact-label">Marriage(s)</div>
    <div class="fact-value">
      <div class="stacked-records">
        <div><strong>Spouse One</strong> — marriage summary. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></div>
        <div><strong>Spouse Two</strong> — marriage summary. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></div>
      </div>
    </div>
  </div>
</div>
</section>

<section class="fact-panel fact-panel-highlights" id="highlights">
<h2 class="unnumbered">Highlights</h2>

<ul>
  <li><strong>Replace headline point.</strong> Replace with one sharp supporting sentence. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></li>
  <li><strong>Replace headline point.</strong> Replace with one sharp supporting sentence. <sup class="fn"><a href="#n8" id="ref-8">8</a></sup></li>
  <li><strong>Replace headline point.</strong> Replace with one sharp supporting sentence. <sup class="fn"><a href="#n9" id="ref-9">9</a></sup></li>
</ul>
</section>


<section class="fact-section" id="children">
<h2 class="unnumbered">Children</h2>

<table class="facts-children">
  <thead>
    <tr>
      <th>Name</th>
      <th>Dates</th>
      <th>Mother</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Child Name</td><td>Dates</td><td>Mother</td><td>Replace with concise note. <sup class="fn"><a href="#n10" id="ref-10">10</a></sup></td></tr>
  </tbody>
</table>
</section>

<section class="fact-section fact-narrative" id="narrative">
<h2 class="unnumbered">Narrative</h2>

Paragraph one.

Paragraph two.

Paragraph three.
</section>

<section class="fact-section" id="citations">
<h2 class="unnumbered">Citations</h2>

<ol class="citation-list">
  <li id="n1">Replace citation text. <a class="citation-back" href="#ref-1">↩</a></li>
  <li id="n2">Replace citation text. <a class="citation-back" href="#ref-2">↩</a></li>
  <li id="n3">Replace citation text. <a class="citation-back" href="#ref-3">↩</a></li>
  <li id="n4">Replace citation text. <a class="citation-back" href="#ref-4">↩</a></li>
  <li id="n5">Replace citation text. <a class="citation-back" href="#ref-5">↩</a></li>
</ol>
</section>

  </div>

  <aside class="factsheet-side">

{% if factsheet.heroImage %}
<figure class="fact-panel fact-hero">
  <img src="{{ factsheet.heroImage }}" alt="{{ factsheet.heroAlt or ('Historical image associated with ' + factsheet.personName) }}">
  <figcaption>{{ factsheet.heroCaption }}{% if factsheet.heroCredit %} {{ factsheet.heroCredit }}{% endif %}</figcaption>
</figure>
{% endif %}

<div class="fact-panel">
  <h2>Related Links</h2>
  <div class="fact-buttons">
    <a href="/key-research/john-gurney-case-file.html">Case File</a>
    <a href="/maps-and-lists/ancestor-table.html">Ancestor Table</a>
  </div>
</div>

<div class="fact-panel">
  <h2>Timeline</h2>
  <table class="fact-timeline-table">
    <tbody>
      <tr><th>Year</th><th>Event</th></tr>
      <tr><td>0000</td><td>Replace with concise milestone.</td></tr>
      <tr><td>0000</td><td>Replace with concise milestone.</td></tr>
      <tr><td>0000</td><td>Replace with concise milestone.</td></tr>
    </tbody>
  </table>
</div>



  </aside>
</div>


---

## Research Appendix

*Source-only working notes may go here. This section is intentionally suppressed from published fact-sheet HTML.*
