const fs = require("fs");
const path = require("path");

const projectRoot = path.resolve(__dirname, "..");
const repoRoot = path.resolve(projectRoot, "..", "..");
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
  return candidates.some(candidate => exists(path.join(projectRoot, candidate)));
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
const canonicalAncestors = readJson(path.join(repoRoot, "data", "ancestors v26.json"), "canonical ancestors v26 data");
readJson(path.join(repoRoot, "data", "places.json"), "canonical places data");
readJson(path.join(repoRoot, "data", "places_detail.json"), "canonical places detail data");
readJson(path.join(repoRoot, "data", "sources.json"), "canonical sources data");

if (Array.isArray(siteAncestors)) {
  const ancestorCount = siteAncestors.filter(item => item.type === "ancestor").length;
  const eraCount = siteAncestors.filter(item => item.type === "era").length;
  if (!ancestorCount) errors.push("_data/ancestors.json has no ancestor records");
  if (!eraCount) warnings.push("_data/ancestors.json has no era records");

  const seenButtonUrls = new Set();
  siteAncestors.forEach(item => {
    if (Array.isArray(item.buttons)) {
      item.buttons.forEach(button => {
        if (!button || !button.url) return;
        const key = `${item.gen || item.name || "record"}: ${button.url}`;
        if (seenButtonUrls.has(key)) warnings.push(`duplicate ancestor button URL: ${key}`);
        seenButtonUrls.add(key);
        checkRoute(button.url, `ancestor button for ${item.gen || item.name || "unknown"}`);
      });
    }
  });
}

if (Array.isArray(canonicalAncestors)) {
  const currentCount = canonicalAncestors.filter(item => item.type === "ancestor").length;
  if (!currentCount) errors.push("data/ancestors v26.json has no ancestor records");
}

const requiredFiles = [
  "maps-and-lists/ancestor-map.html",
  "maps-and-lists/ancestor-table.njk",
  "research/highlights.md",
  "robots.txt",
  "sitemap.xml",
  "llms.txt",
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
