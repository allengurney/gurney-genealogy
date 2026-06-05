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

function walkFiles(dir, predicate, results = []) {
  if (!exists(dir)) return results;
  fs.readdirSync(dir, { withFileTypes: true }).forEach(entry => {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      walkFiles(full, predicate, results);
    } else if (!predicate || predicate(full)) {
      results.push(full);
    }
  });
  return results;
}

function htmlMetaContent(html, name) {
  const pattern = new RegExp(`<meta\\b[^>]*\\bname=["']${name}["'][^>]*\\bcontent=["']([^"']*)["'][^>]*>`, "i");
  const match = html.match(pattern);
  return match ? match[1].replace(/\s+/g, " ").trim() : "";
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
const canonicalPlaces = readJson(path.join(repoRoot, "data", "places.json"), "canonical places data");
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

// Bidirectional place<->ancestor link integrity (canonical data).
// placeRefs (ancestors.json) drive map markers in the pedigree drawer and ancestor map;
// ancestorLinks (places.json) drive the places catalog and place pages. Both sides should
// name each other. Warnings (not errors) so a deliberate asymmetry does not block the build.
if (Array.isArray(canonicalAncestors) && Array.isArray(canonicalPlaces)) {
  const recordIds = new Set(canonicalAncestors.filter(item => item.type !== "era" && item.recordId).map(item => item.recordId));
  const placeIds = new Set(canonicalPlaces.map(place => place.placeId));
  const forward = new Map(); // recordId -> Set(placeId) from placeRefs
  canonicalAncestors.forEach(item => {
    if (item.type === "era" || !item.recordId) return;
    forward.set(item.recordId, new Set(Array.isArray(item.placeRefs) ? item.placeRefs : []));
  });
  const reverse = new Map(); // recordId -> Set(placeId) from ancestorLinks
  canonicalPlaces.forEach(place => {
    (Array.isArray(place.ancestorLinks) ? place.ancestorLinks : []).forEach(link => {
      if (!link || !link.recordId) return;
      if (!reverse.has(link.recordId)) reverse.set(link.recordId, new Set());
      reverse.get(link.recordId).add(place.placeId);
    });
  });

  const danglingRefs = [];    // placeRef -> unknown placeId
  const danglingLinks = [];   // ancestorLink -> unknown recordId
  const missingReverse = [];  // in placeRefs, not in ancestorLinks (place catalog will not list ancestor)
  const missingForward = [];  // in ancestorLinks, not in placeRefs (ancestor gets no map marker)
  forward.forEach((pids, recordId) => {
    pids.forEach(pid => {
      if (!placeIds.has(pid)) danglingRefs.push(`${recordId} -> ${pid}`);
      else if (!(reverse.get(recordId) || new Set()).has(pid)) missingReverse.push(`${recordId} -> ${pid}`);
    });
  });
  reverse.forEach((pids, recordId) => {
    if (!recordIds.has(recordId)) {
      pids.forEach(pid => danglingLinks.push(`${recordId} -> ${pid}`));
      return;
    }
    pids.forEach(pid => {
      if (!(forward.get(recordId) || new Set()).has(pid)) missingForward.push(`${recordId} -> ${pid}`);
    });
  });

  const reportDrift = (list, label) => {
    if (list.length) warnings.push(`place-link ${label}: ${list.length} (e.g. ${list.slice(0, 5).join("; ")})`);
  };
  reportDrift(danglingRefs, "placeRefs reference an unknown placeId");
  reportDrift(danglingLinks, "ancestorLinks reference an unknown ancestor recordId");
  reportDrift(missingForward, "place lists ancestor but ancestor placeRefs omit it (no map marker)");
  reportDrift(missingReverse, "ancestor placeRefs list place but place ancestorLinks omit it (absent from catalog)");
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

if (exists(siteOutputRoot)) {
  const htmlFiles = walkFiles(siteOutputRoot, file => file.endsWith(".html"));
  const shortDescriptions = [];
  const genericDescriptions = [];

  htmlFiles.forEach(file => {
    const html = fs.readFileSync(file, "utf8");
    const description = htmlMetaContent(html, "description");
    const relativeOutput = path.relative(siteOutputRoot, file).replace(/\\/g, "/");

    if (!description) {
      warnings.push(`missing meta description in built output: ${relativeOutput}`);
      return;
    }
    if (description.length < 120) {
      shortDescriptions.push(`${relativeOutput} (${description.length})`);
    }
    if (/^(Research page for|Compact (?:ancestor |related-person )?fact sheet for)\b/i.test(description)) {
      genericDescriptions.push(relativeOutput);
    }
  });

  if (shortDescriptions.length) {
    warnings.push(`short meta descriptions under 120 chars: ${shortDescriptions.length} page(s); first examples: ${shortDescriptions.slice(0, 8).join(", ")}`);
  }
  if (genericDescriptions.length) {
    warnings.push(`generic meta descriptions remain: ${genericDescriptions.length} page(s); first examples: ${genericDescriptions.slice(0, 8).join(", ")}`);
  }
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
