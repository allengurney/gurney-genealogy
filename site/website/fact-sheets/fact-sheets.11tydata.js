
const factsheetIndex = require("../_data/factsheetIndex.js");
const researchCompanions = require("../_data/researchCompanions.js");

function cleanText(value) {
  return String(value || "")
    .replace(/<[^>]+>/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function trimSeoDescription(value, maxLength = 160) {
  const clean = cleanText(value);
  if (clean.length <= maxLength) return clean;

  const slice = clean.slice(0, maxLength + 1);
  const wordBreak = slice.lastIndexOf(" ");
  const trimmed = clean.slice(0, wordBreak > 120 ? wordBreak : maxLength).replace(/[,:;–-]\s*$/u, "").trim();
  return /[.!?]$/.test(trimmed) ? trimmed : `${trimmed}.`;
}

function isGenericDescription(value) {
  return /^Compact (?:ancestor |related-person )?fact sheet for /i.test(String(value || "").trim());
}

function factsheetDescription(data) {
  const existing = cleanText(data.description);
  if (existing && existing.length >= 140 && !isGenericDescription(existing)) return existing;

  const factsheet = data.factsheet || {};
  const personName = factsheet.personName || cleanText(data.pageHeading || data.title).replace(/\s*\([^)]*\)\s*$/, "");
  const gen = factsheet.gen ? ` (${factsheet.gen})` : "";
  const subtitle = cleanText(data.subtitle);
  const lead = subtitle
    ? `${personName}${gen}: ${subtitle}`
    : `${personName}${gen} fact sheet in the Gurney genealogy library.`;
  return trimSeoDescription(`${lead} Includes sourced vital records, family links, narrative context, and citations.`);
}

function genNumber(gen) {
  const match = String(gen || "").match(/(\d+)/);
  return match ? Number(match[1]) : null;
}

module.exports = {
  eleventyComputed: {
    activeNav: data => data.activeNav || "factsheets",
    description: data => factsheetDescription(data),
    researchCompanion: data => {
      const factsheet = data.factsheet || {};
      const currentGen = genNumber(factsheet.gen);
      return researchCompanions.find(item => item.slug === factsheet.slug || (currentGen !== null && item.genNum === currentGen)) || null;
    },
    factsheetNav: data => {
      const url = data.page && data.page.url;
      const i = factsheetIndex.findIndex(item => item.url === url);
      if (i === -1) return null;
      return {
        current: factsheetIndex[i],
        earlier: factsheetIndex[i + 1] || null,
        later: factsheetIndex[i - 1] || null
      };
    }
  }
};
