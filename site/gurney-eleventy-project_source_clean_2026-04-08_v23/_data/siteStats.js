const ancestors = require("./ancestors.json");
const researchCompanions = require("./researchCompanions.js");

const directAncestors = ancestors.filter(item => item.type === "ancestor");
const knownGenerations = directAncestors.filter(item => !/[~+]/.test(String(item.gen || "")));
const eras = ancestors.filter(item => item.type === "era");
const places = new Set();

directAncestors.forEach(item => {
  (item.placeRefs || []).forEach(placeId => places.add(placeId));
});

module.exports = {
  directAncestorCount: directAncestors.length,
  knownGenerationCount: knownGenerations.length,
  eraCount: eras.length,
  placeCount: places.size,
  researchCompanionCount: researchCompanions.length,
};
