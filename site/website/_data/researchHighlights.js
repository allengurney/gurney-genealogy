const fs = require("fs");
const path = require("path");

const ancestors = require("./ancestors.json");
const highlightsPath = path.join(__dirname, "..", "research", "highlights.md");

function readField(block, field) {
  const pattern = new RegExp(`\\*\\*${field}:\\*\\*\\s*([\\s\\S]*?)(?=\\n\\s*\\*\\*[a-z_]+:\\*\\*|$)`, "i");
  const match = block.match(pattern);
  return match ? match[1].trim() : "";
}

function parseHighlights(markdown) {
  return markdown
    .split(/\n-\s+\*\*date:\*\*/)
    .slice(1)
    .map(block => {
      const item = `**date:**${block}`;
      return {
        date: readField(item, "date"),
        title: readField(item, "title"),
        desc: readField(item, "desc"),
        link: readField(item, "link"),
        link_type: readField(item, "link_type"),
        link_ref: readField(item, "link_ref"),
        link_label: readField(item, "link_label"),
      };
    })
    .filter(item => item.date && item.title && item.link);
}

if (!fs.existsSync(highlightsPath)) {
  module.exports = [];
} else {
  const byGen = new Map(
    ancestors
      .filter(item => item.type === "ancestor")
      .map(item => [item.gen, item])
  );

  module.exports = parseHighlights(fs.readFileSync(highlightsPath, "utf8"))
    .map(item => ({
      ...item,
      ancestor: item.link_ref ? byGen.get(item.link_ref) || null : null,
    }));
}
