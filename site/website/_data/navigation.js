const factsheets = require("./factsheetIndex.js");

// The G13 annex (research library + Context Graph explorer) only exists in
// package-mode builds (G13_PACKAGE=staging|production, same gate as
// scripts/sync-g13-package.js); a legacy build must not carry dead menu links.
const g13PackageMode = String(process.env.G13_PACKAGE || "").trim().toLowerCase();
const g13AnnexNavItems = g13PackageMode && g13PackageMode !== "off" && g13PackageMode !== "legacy"
  ? [
      { title: "John Gurney Context Graph Explorer", url: "/research/notes/g13-john-gurney/explorer/", key: "g13-explorer" },
      { title: "John Gurney Research Library", url: "/research/notes/g13-john-gurney.html", key: "g13-library" },
    ]
  : [];

module.exports = {
  items: [
    { title: "Home", url: "/index.html", key: "home", visible: true },
    {
      title: "Key Research",
      key: "research",
      visible: true,
      children: [
        { title: "John Gurney Case File", url: "/key-research/john-gurney-case-file.html", key: "john" },
        ...g13AnnexNavItems,
        { title: "Brig. General William Gurney Bio", url: "/key-research/brigadier-general-william-gurney.html", key: "william" },
        { title: "Heraldic Chain of Evidence", url: "/key-research/gurney-heraldic-chain-of-evidence.html", key: "heraldic-chain" },
        { title: "AI Paleographic Analysis John Gurney baptism record", url: "/key-research/east-dereham-ai-assistant-procedure.html", key: "east-dereham" },
        { title: "AI in Genealogy", url: "/key-research/using-gen-ai-in-genealogy.html", key: "ai-genealogy" },
        { title: "Sources", url: "/key-research/sources.html", key: "sources" },
        { title: "Misc. Topics", url: "/key-research/misc-topics.html", key: "misc-topics" }
      ]
    },
    {
      title: "Maps & Lists",
      key: "maps",
      visible: true,
      children: [
        { title: "Ancestor Map", url: "/maps-and-lists/ancestor-map.html", key: "map" },
        { title: "Pedigree Catalog", url: "/maps-and-lists/ancestor-table.html", key: "catalog" },
        { title: "Places Catalog", url: "/maps-and-lists/places.html", key: "places" }
      ]
    },
    {
      title: "Fact Sheets",
      key: "factsheets",
      visible: true,
      children: factsheets.map(f => ({ title: f.menuLabel, url: f.url, key: f.gen }))
    },
    {
      title: "Placeholder",
      key: "placeholder",
      visible: false,
      children: [
        { title: "SubPlaceholder", url: "#", key: "subplaceholder", visible: false }
      ]
    }
  ]
};
