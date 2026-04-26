const sources = require("./sourcesCatalog.json");

module.exports = {
  sourceCount: sources.length,
  fullCorpusCount: sources.filter(source => source.corpusStatus === "full").length,
  externalLinkCount: sources.filter(source => source.url).length,
  validationCount: sources.filter(source => source.validationPath).length,
};
