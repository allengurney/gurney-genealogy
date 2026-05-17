const fs = require("fs");
const path = require("path");

const companionsDir = path.join(__dirname, "..", "research", "companions");

function genNumber(value) {
  const match = String(value || "").match(/(\d+)/);
  return match ? Number(match[1]) : null;
}

function readTitle(markdown, fallback) {
  const body = markdown.replace(/^---[\s\S]*?---\s*/, "");
  const match = body.match(/^#\s+(.+)$/m);
  return match ? match[1].trim() : fallback;
}

function companionPublicSlug(slug) {
  return slug.replace(/-fact-sheet$/i, "");
}

if (!fs.existsSync(companionsDir)) {
  module.exports = [];
} else {
  module.exports = fs.readdirSync(companionsDir)
    .filter(file => file.endsWith(".md"))
    .sort((a, b) => a.localeCompare(b))
    .map(file => {
      const slug = file.replace(/\.md$/i, "");
      const content = fs.readFileSync(path.join(companionsDir, file), "utf8");
      const genNum = genNumber(slug);
      return {
        slug,
        genNum,
        gen: genNum === null ? "" : `G${genNum}`,
        title: readTitle(content, slug.replace(/-/g, " ")),
        url: `/research/notes/${companionPublicSlug(slug)}.html`,
      };
    });
}
