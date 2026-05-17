const sources = require("./sourcesCatalog.json");

const hasPath = (value, prefix) => typeof value === "string" && value.startsWith(prefix);

const corpusItemCount = sources.filter(source => hasPath(source.corpusPath, "sources/corpus/")).length;
const corpusSupplementItemCount = sources.filter(source => hasPath(source.corpusPath, "sources/corpus_supplement/")).length;
const mediaItemCount = sources.filter(source => hasPath(source.mediaPath, "sources/media/")).length;

module.exports = {
  sourceCount: sources.length,
  fullCorpusCount: sources.filter(source => source.corpusStatus === "full").length,
  corpusItemCount,
  corpusSupplementItemCount,
  mediaItemCount,
  libraryHoldingsCount: corpusItemCount + corpusSupplementItemCount + mediaItemCount,
  externalLinkCount: sources.filter(source => source.url).length,
  validationCount: sources.filter(source => source.validationPath).length,
};
