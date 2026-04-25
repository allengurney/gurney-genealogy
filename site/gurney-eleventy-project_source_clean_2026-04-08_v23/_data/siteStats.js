const ancestors = require("./ancestors.json");
const placesCatalog = require("./placesCatalog.json");
const researchCompanions = require("./researchCompanions.js");

const directAncestors = ancestors.filter(item => item.type === "ancestor");
const relatedAncestors = ancestors.filter(item => item.type === "related");
const knownGenerations = directAncestors.filter(item => !/[~+]/.test(String(item.gen || "")));
const eras = ancestors.filter(item => item.type === "era");
const places = new Set();
const placeLinkCount = placesCatalog.reduce((sum, place) => sum + (place.ancestorCount || 0), 0);
const placeTypes = new Set(placesCatalog.map(place => place.placeType).filter(Boolean));
const geocodedPlaceCount = placesCatalog.filter(place => place.coordinate && place.coordinate.lat && place.coordinate.lng).length;

directAncestors.forEach(item => {
  (item.placeRefs || []).forEach(placeId => places.add(placeId));
});

module.exports = {
  directAncestorCount: directAncestors.length,
  relatedAncestorCount: relatedAncestors.length,
  knownGenerationCount: knownGenerations.length,
  eraCount: eras.length,
  placeCount: placesCatalog.length || places.size,
  placeLinkCount,
  placeTypeCount: placeTypes.size,
  geocodedPlaceCount,
  researchCompanionCount: researchCompanions.length,
};
