
const ancestors = require("./ancestors.json");
function genNumber(gen) {
  if (!gen) return 999;
  const m = String(gen).match(/(\d+)/);
  return m ? parseInt(m[1], 10) : 999;
}
function genDisplay(gen) {
  if (!gen) return "";
  return String(gen).replace(/^G/, "");
}
const seen = new Set();
const items = ancestors
  .filter(a => a.type === "ancestor" && Array.isArray(a.buttons))
  .map(a => {
    const btn = a.buttons.find(b => b.label === "Fact sheet" && b.url);
    if (!btn || seen.has(btn.url)) return null;
    seen.add(btn.url);
    return {
      gen: a.gen,
      genNum: genNumber(a.gen),
      genDisplay: genDisplay(a.gen),
      name: a.name,
      label: `${a.gen} ${a.name}`,
      menuLabel: `${a.gen} · ${a.name}`,
      url: btn.url
    };
  })
  .filter(Boolean)
  .sort((a, b) => a.genNum - b.genNum || a.name.localeCompare(b.name));
module.exports = items;
