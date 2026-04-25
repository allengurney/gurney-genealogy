const fs = require("fs");
const path = require("path");

const projectRoot = path.resolve(__dirname, "..");
const repoRoot = path.resolve(projectRoot, "..", "..");

const ancestorsPath = path.join(repoRoot, "data", "ancestors v26.json");
const placesPath = path.join(repoRoot, "data", "places.json");
const placeDetailsPath = path.join(repoRoot, "data", "places_detail.json");
const outputPath = path.join(projectRoot, "_data", "ancestors.json");
const placesOutputPath = path.join(projectRoot, "_data", "placesCatalog.json");
const factSheetsDir = path.join(projectRoot, "fact-sheets");
const companionsDir = path.join(projectRoot, "research", "companions");

function readJson(file) {
  return JSON.parse(fs.readFileSync(file, "utf8"));
}

function genNumber(gen) {
  const match = String(gen || "").match(/(\d+)/);
  return match ? Number(match[1]) : null;
}

function compactEra(label) {
  return String(label || "").split(/\s+(?:\u2014|\u00e2\u20ac\u201d|-)\s+/)[0].trim();
}

function confidenceFromPrecision(precision) {
  const value = String(precision || "").toLowerCase();
  if (value.includes("high")) return "High";
  if (value.includes("medium")) return "Medium";
  if (value.includes("low")) return "Low";
  if (value.includes("approx")) return "Medium";
  return "";
}

function regionFromPlaceName(name) {
  const parts = String(name || "").split(",").map(part => part.trim()).filter(Boolean);
  return parts.length > 1 ? parts.slice(1).join(", ") : "";
}

function cleanButton(button) {
  return {
    label: button.label,
    url: button.url,
    style: button.style || "bio",
  };
}

function hasMeaningfulValue(value) {
  return Boolean(value && !/^\s*(?:-|\u2014)\s*$/.test(String(value)));
}

function displayLineageStatus(status) {
  const value = String(status || "").trim();
  return value && value.toLowerCase() !== "confirmed" ? value : "";
}

function indexFactSheets() {
  const byGen = new Map();
  if (!fs.existsSync(factSheetsDir)) return byGen;

  fs.readdirSync(factSheetsDir)
    .filter(file => /^g\d+-.+\.md$/i.test(file))
    .forEach(file => {
      const num = genNumber(file);
      if (num === null) return;
      const slug = file.replace(/\.md$/i, "");
      byGen.set(num, {
        label: "Fact sheet",
        url: `/fact-sheets/${slug}.html`,
        style: "bio",
      });
    });

  return byGen;
}

function indexCompanions() {
  const byGen = new Map();
  if (!fs.existsSync(companionsDir)) return byGen;

  fs.readdirSync(companionsDir)
    .filter(file => /^g\d+-.+\.md$/i.test(file))
    .forEach(file => {
      const num = genNumber(file);
      if (num === null) return;
      const slug = file.replace(/\.md$/i, "");
      byGen.set(num, {
        label: "Research notes",
        url: `/research/companions/${slug}.html`,
        style: "research",
      });
    });

  return byGen;
}

function buildLocations(item, placesById, detailsById, eraById) {
  const era = eraById.get(item.eraId) || {};
  const refs = Array.isArray(item.placeRefs) ? item.placeRefs : [];

  return refs
    .map(placeId => {
      const place = placesById.get(placeId);
      if (!place) return null;

      const detail = detailsById.get(placeId) || {};
      const coordinate = place.coordinate || {};
      const links = Array.isArray(place.ancestorLinks) ? place.ancestorLinks : [];
      const matchingRoles = links
        .filter(link => link.recordId === item.recordId)
        .map(link => link.role)
        .filter(Boolean);
      const roles = matchingRoles.length ? matchingRoles : (place.roles || []);

      return {
        placeId,
        place: place.name || detail.placeName || "",
        siteName: detail.siteName || "",
        region: regionFromPlaceName(place.name || detail.placeName || ""),
        eventType: roles.join("; ") || place.placeType || "place",
        eventDate: item.dates || era.dates || "",
        sourceQuote: detail.longDescription || place.shortDescription || place.name || "",
        lat: coordinate.lat,
        lng: coordinate.lng,
        geocodeBasis: detail.coordinateBasis || place.coordinatePrecision || "",
        confidence: confidenceFromPrecision(place.coordinatePrecision),
        photoUrl: detail.imageUrl || "",
        photoTitle: detail.imageTitle || "",
        siteUrl: detail.heritageUrl || "",
        siteLabel: detail.heritageLabel || "",
      };
    })
    .filter(Boolean);
}

function placeSummary(locations) {
  const names = [...new Set(locations.map(location => location.siteName || location.place).filter(Boolean))];
  if (names.length <= 3) return names.join("; ");
  return `${names.slice(0, 3).join("; ")}; +${names.length - 3} more`;
}

function buildPlacesCatalog(places, placeDetails, generatedAncestors) {
  const detailsById = new Map(placeDetails.map(detail => [detail.placeId, detail]));
  const ancestorsByRecordId = new Map(
    generatedAncestors
      .filter(item => item.type !== "era")
      .map(item => [item.recordId, item])
  );

  return places.map(place => {
    const detail = detailsById.get(place.placeId) || {};
    const coordinate = place.coordinate || {};
    const links = Array.isArray(place.ancestorLinks) ? place.ancestorLinks : [];
    const linkedAncestors = links
      .map(link => {
        const ancestor = ancestorsByRecordId.get(link.recordId);
        if (!ancestor) return null;
        const primaryButton = Array.isArray(ancestor.buttons) ? ancestor.buttons[0] : null;
        return {
          recordId: ancestor.recordId,
          type: ancestor.type,
          gen: ancestor.gen,
          name: ancestor.name,
          dates: ancestor.dates,
          role: link.role || "",
          lineageStatus: ancestor.lineageStatus,
          displayLineageStatus: ancestor.displayLineageStatus,
          url: primaryButton ? primaryButton.url : "",
        };
      })
      .filter(Boolean);

    return {
      placeId: place.placeId,
      name: place.name || detail.placeName || "",
      title: detail.siteName || place.name || detail.placeName || "",
      siteName: detail.siteName || "",
      region: regionFromPlaceName(place.name || detail.placeName || ""),
      aliases: place.aliases || [],
      shortDescription: place.shortDescription || "",
      longDescription: detail.longDescription || place.shortDescription || "",
      placeType: place.placeType || "",
      extantStatus: detail.extantStatus || "",
      extantStatusDescription: detail.extantStatusDescription || "",
      coordinate: {
        lat: coordinate.lat,
        lng: coordinate.lng,
      },
      coordinatePrecision: place.coordinatePrecision || "",
      coordinateBasis: detail.coordinateBasis || place.coordinatePrecision || "",
      roles: place.roles || [],
      imageUrl: detail.imageUrl || "",
      imageTitle: detail.imageTitle || "",
      siteUrl: detail.heritageUrl || "",
      siteLabel: detail.heritageLabel || "",
      ancestorLinks: linkedAncestors,
      ancestorCount: linkedAncestors.length,
    };
  });
}

const ancestors = readJson(ancestorsPath);
const places = readJson(placesPath);
const placeDetails = readJson(placeDetailsPath);

const eraById = new Map(
  ancestors
    .filter(item => item.type === "era")
    .map(item => [item.recordId, item])
);
const placesById = new Map(places.map(place => [place.placeId, place]));
const detailsById = new Map(placeDetails.map(detail => [detail.placeId, detail]));
const factSheetsByGen = indexFactSheets();
const companionsByGen = indexCompanions();

const generated = ancestors.map(item => {
  if (item.type === "era") {
    return {
      type: "era",
      label: item.label,
      dates: item.dates || "",
      sequenceId: item.sequenceId,
      cssClass: item.cssClass,
      colorFrom: item.colorFrom,
      colorTo: item.colorTo,
      recordId: item.recordId,
    };
  }

  const num = genNumber(item.gen);
  const era = eraById.get(item.eraId) || {};
  const locations = buildLocations(item, placesById, detailsById, eraById);
  const buttons = Array.isArray(item.buttons) ? item.buttons.map(cleanButton) : [];
  const factSheet = num === null ? null : factSheetsByGen.get(num);
  const companion = num === null ? null : companionsByGen.get(num);

  if (factSheet && !buttons.some(button => button.url === factSheet.url)) {
    buttons.push(factSheet);
  }
  if (companion && !buttons.some(button => button.url === companion.url)) {
    buttons.push(companion);
  }

  return {
    type: item.type,
    isRelated: item.type === "related",
    gen: item.gen,
    genNumber: num,
    name: item.name,
    dates: item.dates || "",
    geography: item.geography || "",
    eraId: item.eraId || "",
    eraLabel: era.label || "",
    eraKey: compactEra(era.label),
    eraDates: era.dates || "",
    eraClass: era.cssClass || "",
    colorFrom: era.colorFrom || "",
    colorTo: era.colorTo || "",
    lineageStatus: item.lineageStatus || "",
    displayLineageStatus: displayLineageStatus(item.lineageStatus),
    summary: item.summary || "",
    notables: item.notables || "",
    landHoldings: item.landHoldings || "",
    hasLandHoldings: hasMeaningfulValue(item.landHoldings),
    spouses: item.spouses || [],
    children: item.children || [],
    buttons,
    recordId: item.recordId || "",
    placeRefs: item.placeRefs || [],
    placeSummary: placeSummary(locations),
    locations,
  };
});

fs.writeFileSync(outputPath, `${JSON.stringify(generated, null, 2)}\n`);
fs.writeFileSync(placesOutputPath, `${JSON.stringify(buildPlacesCatalog(places, placeDetails, generated), null, 2)}\n`);
console.log(`Generated ${path.relative(projectRoot, outputPath).replace(/\\/g, "/")} from data/ancestors v26.json.`);
console.log(`Generated ${path.relative(projectRoot, placesOutputPath).replace(/\\/g, "/")} from data/places.json.`);
