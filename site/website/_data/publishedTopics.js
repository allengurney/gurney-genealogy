const fs = require("fs");
const path = require("path");

// Drives the Key Research -> Misc. Topics index page. Reads the canonical
// designation list at research/topics/_published-topics.csv (filename,displayName)
// and exposes the published-topic pages synced into key-research/topics/ by
// scripts/sync-site-content.js.
const csvPath = path.join(__dirname, "..", "..", "..", "research", "topics", "_published-topics.csv");

function parse(text) {
  return text
    .split(/\r?\n/)
    .map(line => line.trim())
    .filter(line => line && !/^filename\s*,/i.test(line))
    .map(line => {
      const idx = line.indexOf(",");
      if (idx === -1) return null;
      const filename = line.slice(0, idx).trim();
      const displayName = line.slice(idx + 1).trim().replace(/^"|"$/g, "");
      if (!filename || !displayName) return null;
      const slug = filename.replace(/\.md$/i, "");
      return { slug, displayName, url: `/key-research/topics/${slug}.html` };
    })
    .filter(Boolean);
}

if (!fs.existsSync(csvPath)) {
  module.exports = [];
} else {
  module.exports = parse(fs.readFileSync(csvPath, "utf8"));
}
