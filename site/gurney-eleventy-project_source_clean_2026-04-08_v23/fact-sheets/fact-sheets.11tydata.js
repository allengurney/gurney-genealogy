
const factsheetIndex = require("../_data/factsheetIndex.js");
const researchCompanions = require("../_data/researchCompanions.js");

function genNumber(gen) {
  const match = String(gen || "").match(/(\d+)/);
  return match ? Number(match[1]) : null;
}

module.exports = {
  eleventyComputed: {
    activeNav: data => data.activeNav || "factsheets",
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
