
const factsheets = require("./factsheetIndex.js");
module.exports = {
  items: [
    { title: "Home", url: "/index.html", key: "home", visible: true },
    {
      title: "Key Research",
      key: "research",
      visible: true,
      children: [
        { title: "John Gurney Case File", url: "/key-research/john-gurney-case-file.html", key: "john" },
        { title: "Brig. General William Gurney Bio", url: "/key-research/brigadier-general-william-gurney.html", key: "william" },
        { title: "AI Paleographic Analysis John Gurney baptism record", url: "/key-research/east-dereham-ai-assistant-procedure.html", key: "east-dereham" },
        { title: "AI in Genealogy", url: "/key-research/using-gen-ai-in-genealogy.html", key: "ai-genealogy" }
      ]
    },
    {
      title: "Maps & Lists",
      key: "maps",
      visible: true,
      children: [
        { title: "Ancestor Map", url: "/maps-and-lists/ancestor-map.html", key: "map" },
        { title: "Pedigree Catalog", url: "/maps-and-lists/ancestor-table.html", key: "catalog" }
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
