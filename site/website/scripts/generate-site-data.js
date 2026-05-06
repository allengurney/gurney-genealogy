const fs = require("fs");
const path = require("path");

const projectRoot = path.resolve(__dirname, "..");
const repoRoot = path.resolve(projectRoot, "..", "..");

const ancestorsPath = path.join(repoRoot, "data", "ancestors v26.json");
const placesPath = path.join(repoRoot, "data", "places.json");
const placeDetailsPath = path.join(repoRoot, "data", "places_detail.json");
const sourcesPath = path.join(repoRoot, "data", "sources.json");
const researchPlacesDir = path.join(repoRoot, "research", "places");
const outputPath = path.join(projectRoot, "_data", "ancestors.json");
const placesOutputPath = path.join(projectRoot, "_data", "placesCatalog.json");
const placePagesOutputPath = path.join(projectRoot, "_data", "placePages.json");
const sourcesOutputPath = path.join(projectRoot, "_data", "sourcesCatalog.json");
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

function shortEraLabel(item) {
  if (item.shortLabel) return item.shortLabel;
  const byClass = {
    "era-modern": "Modern America",
    "era-gilded": "Gilded Age",
    "era-republic": "Early Republic",
    "era-massachusetts": "Massachusetts",
    "era-emigrant": "The Emigrant",
    "era-tudor": "Tudor England",
    "era-medieval": "Medieval Norfolk",
    "era-junior-norfolk": "Junior Norfolk",
    "era-norman": "Norman Barons",
    "era-viking": "Viking Origins",
    "era-end": "End of Known Record",
  };
  return byClass[item.cssClass] || compactEra(item.label);
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

function regionGroupFromPlace(place) {
  const value = [
    place.name,
    place.placeId,
    Array.isArray(place.aliases) ? place.aliases.join(" ") : "",
  ].join(" ").toLowerCase();

  if (/\b(usa|united states|massachusetts|new york|indiana|oregon|michigan|south carolina|missouri|ny|ma|in|or|mi|sc|mo)\b/.test(value)) {
    return "north-america";
  }
  if (/\b(england|norfolk|suffolk|essex|bedfordshire|buckinghamshire|oxfordshire|london|somerset|sussex)\b/.test(value)) {
    return "england";
  }
  if (/\b(france|normandy|scandinavia|norman|europe)\b/.test(value)) {
    return "europe";
  }
  return "other";
}

function cleanButton(button) {
  const url = button.url || "";
  const style = button.style || "bio";
  const isExternal = /^https?:\/\//i.test(url);
  return {
    label: button.label,
    url,
    style,
    isExternal,
  };
}

function buttonRank(button) {
  if (!button) return 99;
  if (button.style === "bio") return 10;
  if (button.style === "research") return 20;
  if (button.style === "tree") return 30;
  if (button.style === "family-search") return 80;
  if (button.style === "external" || button.isExternal) return 90;
  return 40;
}

function sortButtons(buttons) {
  return buttons
    .map((button, index) => ({ button, index }))
    .sort((a, b) => buttonRank(a.button) - buttonRank(b.button) || a.index - b.index)
    .map(item => item.button);
}

function hasMeaningfulValue(value) {
  return Boolean(value && !/^\s*(?:-|\u2014)\s*$/.test(String(value)));
}

function stripFrontMatter(markdown) {
  return String(markdown || "").replace(/^---[\s\S]*?---\s*/, "");
}

function stripGeneratedPlaceRegistry(markdown) {
  return stripFrontMatter(markdown).replace(/\n?<!-- GENERATED:PLACE-REGISTRY:START -->[\s\S]*?<!-- GENERATED:PLACE-REGISTRY:END -->\s*/m, "").trim();
}

function markdownTitle(markdown, fallback) {
  const match = stripFrontMatter(markdown).match(/^#\s+(.+)$/m);
  return match ? match[1].trim() : fallback;
}

function slugFromFilename(file) {
  return file.replace(/\.md$/i, "");
}

function placeIdFromMarkdown(markdown) {
  const match = String(markdown || "").match(/-\s+`placeId`:\s+`([^`]+)`/);
  return match ? match[1] : "";
}

function displayLineageStatus(status) {
  const value = String(status || "").trim();
  return value && value.toLowerCase() !== "confirmed" ? value : "";
}

function indexFactSheets() {
  const byGen = new Map();
  if (!fs.existsSync(factSheetsDir)) return byGen;

  fs.readdirSync(factSheetsDir)
    .filter(file => /^g\d+-.+\.md$/i.test(file) && !/-related-/i.test(file))
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

function indexPlaceResearch() {
  const byPlaceId = new Map();
  if (!fs.existsSync(researchPlacesDir)) return byPlaceId;

  fs.readdirSync(researchPlacesDir, { withFileTypes: true })
    .filter(entry => entry.isFile() && entry.name.endsWith(".md"))
    .forEach(entry => {
      const source = fs.readFileSync(path.join(researchPlacesDir, entry.name), "utf8");
      const placeId = placeIdFromMarkdown(source);
      if (!placeId) return;
      const slug = slugFromFilename(entry.name);
      byPlaceId.set(placeId, {
        slug,
        url: `/research/places/${slug}.html`,
        title: markdownTitle(source, slug.replace(/-/g, " ")),
        markdown: stripGeneratedPlaceRegistry(source),
      });
    });

  return byPlaceId;
}

function buildPlacesCatalog(places, placeDetails, generatedAncestors, placeResearchById) {
  const detailsById = new Map(placeDetails.map(detail => [detail.placeId, detail]));
  const ancestorsByRecordId = new Map(
    generatedAncestors
      .filter(item => item.type !== "era")
      .map(item => [item.recordId, item])
  );

  return places.map(place => {
    const detail = detailsById.get(place.placeId) || {};
    const research = placeResearchById.get(place.placeId) || {};
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
      streetAddress: detail.streetAddress || "",
      region: regionFromPlaceName(place.name || detail.placeName || ""),
      regionGroup: regionGroupFromPlace(place),
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
      researchUrl: research.url || "",
      researchSlug: research.slug || "",
      ancestorLinks: linkedAncestors,
      ancestorCount: linkedAncestors.length,
    };
  }).sort((a, b) => (b.ancestorCount - a.ancestorCount) || a.title.localeCompare(b.title));
}

function buildPlacePages(placesCatalog, placeResearchById) {
  return placesCatalog
    .filter(place => place.researchSlug || place.longDescription)
    .map(place => {
      const research = placeResearchById.get(place.placeId) || {};
      return {
        ...place,
        slug: place.researchSlug || place.placeId.replace(/^place-/, ""),
        url: place.researchUrl || `/research/places/${place.placeId.replace(/^place-/, "")}.html`,
        researchTitle: research.title || "",
        researchMarkdown: research.markdown || "",
      };
    })
    .sort((a, b) => a.title.localeCompare(b.title));
}

function buildSourcesCatalog(sourceRegistry) {
  const sources = sourceRegistry.sources || {};
  return Object.entries(sources)
    .map(([sourceId, source]) => ({
      sourceId,
      shortTitle: source.shortTitle || sourceId,
      citation: source.citation || "",
      archive: source.archive || "",
      url: source.url || "",
      corpusStatus: source.corpusStatus || "",
      corpusPath: source.corpusPath || "",
      mediaPath: source.mediaPath || "",
      validationPath: source.validationPath || "",
      notes: source.notes || "",
    }))
    .sort((a, b) => a.shortTitle.localeCompare(b.shortTitle));
}

const ancestors = readJson(ancestorsPath);
const places = readJson(placesPath);
const placeDetails = readJson(placeDetailsPath);
const sources = readJson(sourcesPath);

const eraById = new Map(
  ancestors
    .filter(item => item.type === "era")
    .map(item => [item.recordId, item])
);
const placesById = new Map(places.map(place => [place.placeId, place]));
const detailsById = new Map(placeDetails.map(detail => [detail.placeId, detail]));
const factSheetsByGen = indexFactSheets();
const companionsByGen = indexCompanions();
const placeResearchById = indexPlaceResearch();

const generated = ancestors.map(item => {
  if (item.type === "era") {
    return {
      type: "era",
      label: item.label,
      shortLabel: shortEraLabel(item),
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
  const allowGeneratedButtons = item.type !== "related" || buttons.length === 0;

  if (allowGeneratedButtons && factSheet && !buttons.some(button => button.url === factSheet.url)) {
    buttons.push(factSheet);
  }
  if (allowGeneratedButtons && companion && !buttons.some(button => button.url === companion.url)) {
    buttons.push(companion);
  }

  const output = {
    type: item.type,
    isRelated: item.type === "related",
    gen: item.gen,
    genNumber: num,
    name: item.name,
    dates: item.dates || "",
    geography: item.geography || "",
    eraId: item.eraId || "",
    eraLabel: era.label || "",
    eraShortLabel: shortEraLabel(era),
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
    buttons: sortButtons(buttons),
    recordId: item.recordId || "",
    placeRefs: item.placeRefs || [],
    placeSummary: placeSummary(locations),
    locations,
  };
  if (item.externalIds && Object.keys(item.externalIds).length) {
    output.externalIds = item.externalIds;
  }
  return output;
});

const placesCatalog = buildPlacesCatalog(places, placeDetails, generated, placeResearchById);

fs.writeFileSync(outputPath, `${JSON.stringify(generated, null, 2)}\n`);
fs.writeFileSync(placesOutputPath, `${JSON.stringify(placesCatalog, null, 2)}\n`);
fs.writeFileSync(placePagesOutputPath, `${JSON.stringify(buildPlacePages(placesCatalog, placeResearchById), null, 2)}\n`);
fs.writeFileSync(sourcesOutputPath, `${JSON.stringify(buildSourcesCatalog(sources), null, 2)}\n`);
console.log(`Generated ${path.relative(projectRoot, outputPath).replace(/\\/g, "/")} from data/ancestors v26.json.`);
console.log(`Generated ${path.relative(projectRoot, placesOutputPath).replace(/\\/g, "/")} from data/places.json.`);
console.log(`Generated ${path.relative(projectRoot, placePagesOutputPath).replace(/\\/g, "/")} from research/places/*.md and place data.`);
console.log(`Generated ${path.relative(projectRoot, sourcesOutputPath).replace(/\\/g, "/")} from data/sources.json.`);
