const fs = require("fs");
const path = require("path");

const ancestors = require("./ancestors.json");

// Source markdown lives at the repo root, not inside site/website.
// site/website/_data/  -> repo root is three levels up.
const featuredPath = path.join(
  __dirname,
  "..",
  "..",
  "..",
  "fact-sheets",
  "featured-ancestors.md"
);

function parseFeatured(markdown) {
  return markdown
    .split(/\r?\n\s*---\s*\r?\n/)
    .map(block => block.trim())
    .filter(Boolean)
    .map(block => {
      const lines = block
        .split(/\r?\n+/)
        .map(line => line.trim())
        .filter(Boolean);
      if (!lines.length) return null;
      const gen = lines[0];
      const feature = lines.slice(1).join(" ").trim();
      return { gen, feature };
    })
    .filter(item => item && item.gen);
}

if (!fs.existsSync(featuredPath)) {
  module.exports = [];
} else {
  const md = fs.readFileSync(featuredPath, "utf8");
  const entries = parseFeatured(md);
  const byGen = new Map(
    ancestors
      .filter(item => item.type === "ancestor")
      .map(item => [item.gen, item])
  );
  module.exports = entries
    .map(entry => {
      const ancestor = byGen.get(entry.gen);
      if (!ancestor) return null;
      return {
        gen: entry.gen,
        feature: entry.feature,
        name: ancestor.name,
        dates: ancestor.dates,
        colorFrom: ancestor.colorFrom,
        colorTo: ancestor.colorTo,
      };
    })
    .filter(Boolean);
}
