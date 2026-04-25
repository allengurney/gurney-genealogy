const fs = require("fs");
const path = require("path");

const projectRoot = path.resolve(__dirname, "..");
const repoRoot = path.resolve(projectRoot, "..", "..");

const factSheetSource = path.join(repoRoot, "fact-sheets");
const factSheetTarget = path.join(projectRoot, "fact-sheets");
const companionSource = path.join(repoRoot, "research", "people");
const companionTarget = path.join(projectRoot, "research", "companions");

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

const factCount = syncFactSheets();
const companionCount = syncResearchCompanions();
console.log(`Synced ${factCount} fact sheets and ${companionCount} research companions into the site source.`);
