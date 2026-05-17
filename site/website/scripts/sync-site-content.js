const fs = require("fs");
const path = require("path");

const projectRoot = path.resolve(__dirname, "..");
const repoRoot = path.resolve(projectRoot, "..", "..");

const factSheetSource = path.join(repoRoot, "fact-sheets");
const factSheetTarget = path.join(projectRoot, "fact-sheets");
const companionSource = path.join(repoRoot, "research", "people");
const companionTarget = path.join(projectRoot, "research", "companions");
const highlightsSource = path.join(repoRoot, "research", "highlights.md");
const highlightsTarget = path.join(projectRoot, "research", "highlights.md");
const keyResearchTarget = path.join(projectRoot, "key-research");
const keyResearchSources = [
  {
    source: path.join(repoRoot, "research", "case-files", "john-gurney-case-file-v4.md"),
    target: path.join(keyResearchTarget, "john-gurney-case-file.md"),
  },
  {
    source: path.join(repoRoot, "research", "case-files", "brigadier-general-william-gurney.md"),
    target: path.join(keyResearchTarget, "brigadier-general-william-gurney.md"),
  },
];

function ensureDir(dir) {
  fs.mkdirSync(dir, { recursive: true });
}

function removeMarkdownFiles(dir) {
  if (!fs.existsSync(dir)) return;
  fs.readdirSync(dir, { withFileTypes: true })
    .filter(entry => entry.isFile() && entry.name.endsWith(".md"))
    .forEach(entry => fs.rmSync(path.join(dir, entry.name)));
}

function readTitle(markdown, fallback) {
  const withoutFrontMatter = markdown.replace(/^---[\s\S]*?---\s*/, "");
  const match = withoutFrontMatter.match(/^#\s+(.+)$/m);
  return match ? match[1].trim() : fallback;
}

function companionSlug(filename) {
  return filename
    .replace(/\.research\.md$/i, ".md")
    .replace(/\.md$/i, "");
}

function companionPublicSlug(slug) {
  return slug.replace(/-fact-sheet$/i, "");
}

function noteBaseTitle(title, slug) {
  const fallback = slug.replace(/-/g, " ");
  let base = String(title || fallback)
    .replace(/\s+[-\u2013\u2014]\s+Research (?:Companion|Notes)\s*$/i, "")
    .replace(/\s+Research (?:Companion|Notes)\s*$/i, "")
    .trim();

  if (`${base} Notes`.length > 43) {
    const compact = [
      base.split(" / ")[0],
      base.replace(/\s*\([^)]*\)/g, ""),
    ].map(value => value.trim()).find(value => value && `${value} Notes`.length <= 43);
    if (compact) base = compact;
  }

  return base || fallback;
}

function noteTitle(title, slug) {
  return `${noteBaseTitle(title, slug)} Notes`;
}

function noteDescription(title, slug) {
  const base = noteBaseTitle(title, slug);
  return `Research notes for ${base} in the Gurney genealogy library, with source analysis, context, open questions, and supporting evidence.`;
}

function publicCompanionBody(markdown) {
  return markdown
    .replace(/^#\s+(.+?)(?:\s+[-\u2013\u2014]\s+Research (?:Companion|Notes))?\s*$/m, "# $1 Notes")
    .replace(/\bResearch companion for\b/i, "Research notes for");
}

function frontMatter(title, publicSlug, description) {
  return [
    "---",
    `title: ${JSON.stringify(title)}`,
    `description: ${JSON.stringify(description)}`,
    `permalink: /research/notes/${publicSlug}.html`,
    "eleventyExcludeFromCollections: true",
    "---",
    "",
  ].join("\n");
}

function syncFactSheets() {
  ensureDir(factSheetTarget);
  removeMarkdownFiles(factSheetTarget);

  const copied = fs.readdirSync(factSheetSource, { withFileTypes: true })
    .filter(entry => entry.isFile() && entry.name.endsWith(".md") && !["readme.md", "featured-ancestors.md"].includes(entry.name.toLowerCase()))
    .sort((a, b) => a.name.localeCompare(b.name))
    .map(entry => {
      fs.copyFileSync(path.join(factSheetSource, entry.name), path.join(factSheetTarget, entry.name));
      return entry.name;
    });

  return copied.length;
}

function syncResearchCompanions() {
  ensureDir(companionTarget);
  removeMarkdownFiles(companionTarget);

  const copied = fs.readdirSync(companionSource, { withFileTypes: true })
    .filter(entry => entry.isFile() && entry.name.endsWith(".research.md"))
    .sort((a, b) => a.name.localeCompare(b.name))
    .map(entry => {
      const sourcePath = path.join(companionSource, entry.name);
      const source = fs.readFileSync(sourcePath, "utf8");
      const slug = companionSlug(entry.name);
      const publicSlug = companionPublicSlug(slug);
      const sourceTitle = readTitle(source, slug.replace(/-/g, " "));
      const title = noteTitle(sourceTitle, slug);
      const description = noteDescription(sourceTitle, slug);
      const body = publicCompanionBody(source.replace(/^---[\s\S]*?---\s*/, ""));
      const content = `${frontMatter(title, publicSlug, description)}${body}`;
      fs.writeFileSync(path.join(companionTarget, `${slug}.md`), content);
      return slug;
    });

  return copied.length;
}

function syncResearchHighlights() {
  if (!fs.existsSync(highlightsSource)) return false;
  ensureDir(path.dirname(highlightsTarget));
  fs.copyFileSync(highlightsSource, highlightsTarget);
  return true;
}

function syncKeyResearch() {
  ensureDir(keyResearchTarget);

  return keyResearchSources
    .filter(item => fs.existsSync(item.source))
    .map(item => {
      fs.copyFileSync(item.source, item.target);
      return path.basename(item.target);
    }).length;
}

const factCount = syncFactSheets();
const companionCount = syncResearchCompanions();
const highlightsSynced = syncResearchHighlights();
const keyResearchCount = syncKeyResearch();
console.log(`Synced ${factCount} fact sheets, ${companionCount} research companions, ${highlightsSynced ? 1 : 0} highlights file, and ${keyResearchCount} key research files into the site source.`);
