(function () {
  const page = document.querySelector("[data-pedigree-explorer]");
  if (!page) return;

  const rows = Array.from(page.querySelectorAll("[data-pedigree-row]"));
  const detailPanels = Array.from(page.querySelectorAll("[data-detail-panel]"));
  const tableRows = Array.from(page.querySelectorAll("[data-table-row]"));
  const resultCount = page.querySelector("[data-result-count]");
  const modeButtons = Array.from(page.querySelectorAll("[data-catalog-mode]"));
  const eraButtons = Array.from(page.querySelectorAll("[data-era-filter]"));
  const statusButtons = Array.from(page.querySelectorAll("[data-status-filter]"));
  const catalogPanel = page.querySelector("[data-catalog-panel]");
  const tablePanel = page.querySelector("[data-table-panel]");

  let activeGen = "";
  let eraFilter = "all";
  let statusFilter = "all";

  function visibleByFilters(row) {
    const eraOk = eraFilter === "all" || row.dataset.era === eraFilter;
    const statusOk = statusFilter === "all" || row.dataset.status === statusFilter;
    return eraOk && statusOk;
  }

  function updateEraBands() {
    Array.from(page.querySelectorAll("[data-era-band]")).forEach(band => {
      let visible = false;
      let cursor = band.nextElementSibling;
      while (cursor && !cursor.matches("[data-era-band]")) {
        if (cursor.matches("[data-pedigree-row]") && !cursor.hidden) visible = true;
        cursor = cursor.nextElementSibling;
      }
      band.hidden = !visible;
    });
  }

  function selectGen(gen) {
    const target = rows.find(row => row.dataset.gen === gen && !row.hidden) || rows.find(row => !row.hidden);
    if (!target) return;
    activeGen = target.dataset.gen;
    try { window.localStorage.setItem("gurneyPedigreeGen", activeGen); } catch (err) {}

    rows.forEach(row => row.classList.toggle("is-active", row.dataset.gen === activeGen));
    detailPanels.forEach(panel => panel.classList.toggle("is-active", panel.dataset.detailPanel === activeGen));
  }

  function applyFilters() {
    let count = 0;
    rows.forEach(row => {
      const visible = visibleByFilters(row);
      row.hidden = !visible;
      if (visible) count += 1;
    });
    tableRows.forEach(row => {
      row.hidden = !visibleByFilters(row);
    });
    updateEraBands();
    if (resultCount) resultCount.textContent = `${count} ancestor${count === 1 ? "" : "s"}`;
    selectGen(activeGen);
  }

  function setMode(mode) {
    const tableMode = mode === "table";
    if (catalogPanel) catalogPanel.classList.toggle("is-hidden", tableMode);
    if (tablePanel) tablePanel.classList.toggle("is-active", tableMode);
    modeButtons.forEach(button => {
      const active = button.dataset.catalogMode === mode;
      button.classList.toggle("is-active", active);
      button.setAttribute("aria-pressed", active ? "true" : "false");
    });
    try { window.localStorage.setItem("gurneyCatalogMode", mode); } catch (err) {}
  }

  rows.forEach(row => row.addEventListener("click", () => selectGen(row.dataset.gen)));
  rows.forEach(row => row.addEventListener("keydown", event => {
    if (event.key === "Enter" || event.key === " ") {
      event.preventDefault();
      selectGen(row.dataset.gen);
    }
  }));

  modeButtons.forEach(button => {
    button.addEventListener("click", () => setMode(button.dataset.catalogMode));
  });

  eraButtons.forEach(button => {
    button.addEventListener("click", () => {
      eraFilter = button.dataset.eraFilter;
      eraButtons.forEach(item => item.classList.toggle("is-active", item === button));
      applyFilters();
    });
  });

  statusButtons.forEach(button => {
    button.addEventListener("click", () => {
      statusFilter = button.dataset.statusFilter;
      statusButtons.forEach(item => item.classList.toggle("is-active", item === button));
      applyFilters();
    });
  });

  try { activeGen = window.localStorage.getItem("gurneyPedigreeGen") || ""; } catch (err) {}
  const params = new URLSearchParams(window.location.search);
  if (params.get("gen")) activeGen = params.get("gen");

  let mode = "catalog";
  try { mode = window.localStorage.getItem("gurneyCatalogMode") || "catalog"; } catch (err) {}
  setMode(mode === "table" ? "table" : "catalog");
  applyFilters();
})();
