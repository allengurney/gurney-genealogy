
const factsheetIndex = require("../_data/factsheetIndex.js");
module.exports = {
  eleventyComputed: {
    activeNav: data => data.activeNav || "factsheets",
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
