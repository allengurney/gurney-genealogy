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

function frontMatter(title, slug) {
  return [
    "---",
    `title: ${JSON.stringify(title)}`,
    `permalink: /research/companions/${slug}.html`,
    "eleventyExcludeFromCollections: true",
    "---",
    "",
  ].join("\n");
}

function syncFactSheets() {
  ensureDir(factSheetTarget);
  removeMarkdownFiles(factSheetTarget);

  const copied = fs.readdirSync(factSheetSource, { withFileTypes: true })
    .filter(entry => entry.isFile() && entry.name.endsWith(".md") && entry.name.toLowerCase() !== "readme.md")
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
      const title = readTitle(source, slug.replace(/-/g, " "));
      const content = `${frontMatter(title, slug)}${source.replace(/^---[\s\S]*?---\s*/, "")}`;
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
