const fs = require("fs");
const path = require("path");

const projectRoot = path.resolve(__dirname, "..");
const repoRoot = path.resolve(projectRoot, "..", "..");
const siteOutputRoot = path.join(projectRoot, "_site");
const errors = [];
const warnings = [];

function rel(file) {
  return path.relative(projectRoot, file).replace(/\\/g, "/");
}

function exists(file) {
  return fs.existsSync(file);
}

function readJson(file, label) {
  if (!exists(file)) {
    errors.push(`${label} missing: ${rel(file)}`);
    return null;
  }
  try {
    return JSON.parse(fs.readFileSync(file, "utf8"));
  } catch (err) {
    errors.push(`${label} is invalid JSON: ${err.message}`);
    return null;
  }
}

function routeCandidates(url) {
  if (!url || url === "#" || /^https?:\/\//i.test(url) || /^mailto:/i.test(url)) {
    return [];
  }

  const clean = url.split("#")[0].split("?")[0];
  if (!clean || clean === "/") {
    return ["index.njk", "index.md", "index.html"];
  }

  const route = clean.replace(/^\//, "");
  const noHtml = route.replace(/\.html$/, "");
  return [
    route,
    `${noHtml}.njk`,
    `${noHtml}.md`,
    `${noHtml}.html`,
    path.join(noHtml, "index.njk"),
    path.join(noHtml, "index.md"),
    path.join(noHtml, "index.html"),
  ];
}

function routeExists(url) {
  const candidates = routeCandidates(url);
  if (!candidates.length) return true;
  return candidates.some(candidate => exists(path.join(projectRoot, candidate)) || exists(path.join(siteOutputRoot, candidate)));
}

function checkRoute(url, label) {
  if (!url || url === "#") {
    errors.push(`${label} has placeholder or empty URL`);
    return;
  }
  if (!routeExists(url)) {
    errors.push(`${label} points to missing source route: ${url}`);
  }
}

const siteAncestors = readJson(path.join(projectRoot, "_data", "ancestors.json"), "site ancestors data");
const sitePlaces = readJson(path.join(projectRoot, "_data", "placesCatalog.json"), "site places catalog data");
const placePages = readJson(path.join(projectRoot, "_data", "placePages.json"), "site place pages data");
const sourcesCatalog = readJson(path.join(projectRoot, "_data", "sourcesCatalog.json"), "site sources catalog data");
const canonicalAncestors = readJson(path.join(repoRoot, "data", "ancestors.json"), "canonical ancestors data");
readJson(path.join(repoRoot, "data", "places.json"), "canonical places data");
readJson(path.join(repoRoot, "data", "places_detail.json"), "canonical places detail data");
readJson(path.join(repoRoot, "data", "sources.json"), "canonical sources data");

if (Array.isArray(siteAncestors)) {
  const ancestorCount = siteAncestors.filter(item => item.type === "ancestor").length;
  const relatedCount = siteAncestors.filter(item => item.type === "related").length;
  const eraCount = siteAncestors.filter(item => item.type === "era").length;
  if (!ancestorCount) errors.push("_data/ancestors.json has no ancestor records");
  if (!relatedCount) warnings.push("_data/ancestors.json has no related records");
  if (!eraCount) warnings.push("_data/ancestors.json has no era records");

  siteAncestors.forEach(item => {
    if (Array.isArray(item.buttons)) {
      const seenButtonUrls = new Set();
      item.buttons.forEach(button => {
        if (!button || !button.url) return;
        if (seenButtonUrls.has(button.url)) {
          warnings.push(`duplicate ancestor button URL for ${item.gen || item.name || "record"}: ${button.url}`);
        }
        seenButtonUrls.add(button.url);
        checkRoute(button.url, `ancestor button for ${item.gen || item.name || "unknown"}`);
      });
    }
  });
}

if (Array.isArray(sitePlaces)) {
  if (!sitePlaces.length) errors.push("_data/placesCatalog.json has no place records");
  const linkedPlaceCount = sitePlaces.filter(place => Array.isArray(place.ancestorLinks) && place.ancestorLinks.length).length;
  if (!linkedPlaceCount) warnings.push("_data/placesCatalog.json has no linked place records");
}

if (Array.isArray(placePages) && !placePages.length) {
  errors.push("_data/placePages.json has no place page records");
}

if (Array.isArray(sourcesCatalog) && !sourcesCatalog.length) {
  errors.push("_data/sourcesCatalog.json has no source records");
}

if (Array.isArray(canonicalAncestors)) {
  const currentCount = canonicalAncestors.filter(item => item.type === "ancestor").length;
  if (!currentCount) errors.push("data/ancestors.json has no ancestor records");
}

const requiredFiles = [
  "maps-and-lists/ancestor-map.njk",
  "maps-and-lists/ancestor-table.njk",
  "maps-and-lists/places.njk",
  "key-research/sources.njk",
  "research/places/place-pages.njk",
  "research/highlights.md",
  "_data/researchHighlights.js",
  "_data/researchCompanions.js",
  "_data/siteStats.js",
  "_data/sourceStats.js",
  "assets/phase2.css",
  "_data/placesCatalog.json",
  "_data/placePages.json",
  "_data/sourcesCatalog.json",
  "assets/explorer.css",
  "assets/pedigree-explorer.js",
  "assets/map-page.js",
  "scripts/clean-site.js",
  "scripts/sync-site-content.js",
  "scripts/generate-site-data.js",
  "scripts/finalize-public-site.js",
  "robots.txt",
];
requiredFiles.forEach(file => {
  if (!exists(path.join(projectRoot, file))) errors.push(`required site file missing: ${file}`);
});

const highlightsPath = path.join(projectRoot, "research", "highlights.md");
if (exists(highlightsPath)) {
  const highlights = fs.readFileSync(highlightsPath, "utf8");
  const entries = highlights.split(/\n-\s+\*\*date:\*\*/).length - 1;
  if (!entries) warnings.push("research/highlights.md has no highlight entries");
  ["title", "desc", "link", "link_type"].forEach(field => {
    if (!new RegExp(`\\*\\*${field}:\\*\\*`, "i").test(highlights)) {
      warnings.push(`research/highlights.md has no ${field} field`);
    }
  });
}

const companionsDir = path.join(projectRoot, "research", "companions");
if (!exists(companionsDir)) {
  errors.push("generated research companions missing: run npm run sync:content");
} else {
  const companionCount = fs.readdirSync(companionsDir).filter(file => file.endsWith(".md")).length;
  if (!companionCount) errors.push("generated research companions directory has no markdown files");
}

try {
  const navigation = require(path.join(projectRoot, "_data", "navigation.js"));
  const items = Array.isArray(navigation.items) ? navigation.items : [];
  function walkNav(navItems, prefix = "nav") {
    navItems.forEach(item => {
      if (item.visible === false) return;
      const label = `${prefix} ${item.title || item.key || "item"}`;
      if (item.url) checkRoute(item.url, label);
      if (Array.isArray(item.children)) walkNav(item.children, label);
    });
  }
  walkNav(items);
} catch (err) {
  errors.push(`navigation data could not be loaded: ${err.message}`);
}

if (warnings.length) {
  console.warn("Site validation warnings:");
  warnings.forEach(warning => console.warn(`- ${warning}`));
}

if (errors.length) {
  console.error("Site validation failed:");
  errors.forEach(error => console.error(`- ${error}`));
  process.exit(1);
}

console.log("Site validation passed.");
