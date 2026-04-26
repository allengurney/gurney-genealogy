(function () {
  const page = document.querySelector("[data-pedigree-explorer]");
  if (!page) return;

  const rows = Array.from(page.querySelectorAll("[data-pedigree-row]"));
  const detailPanels = Array.from(page.querySelectorAll("[data-detail-panel]"));
  const tableRows = Array.from(page.querySelectorAll("[data-table-row]"));
  const resultCount = page.querySelector("[data-result-count]");
  const modeButtons = Array.from(page.querySelectorAll("[data-catalog-mode]"));
  const eraButtons = Array.from(page.querySelectorAll("[data-era-filter]"));
  const relatedButtons = Array.from(page.querySelectorAll("[data-related-mode]"));
  const catalogPanel = page.querySelector("[data-catalog-panel]");
  const tablePanel = page.querySelector("[data-table-panel]");
  const drawer = page.querySelector("[data-detail-drawer]");
  const backdrop = page.querySelector("[data-detail-backdrop]");
  const closeButton = page.querySelector("[data-detail-close]");
  const mapInstances = new WeakMap();

  let activeRecordId = "";
  let eraFilter = "all";
  let includeRelated = false;

  function isRelated(row) {
    return row.dataset.recordType === "related";
  }

  function visibleByFilters(row) {
    const eraOk = eraFilter === "all" || row.dataset.era === eraFilter;
    const relatedOk = includeRelated || !isRelated(row);
    return eraOk && relatedOk;
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

  function updateResultCount() {
    const visibleRows = rows.filter(row => !row.hidden);
    const direct = visibleRows.filter(row => !isRelated(row)).length;
    const related = visibleRows.length - direct;
    if (!resultCount) return;
    resultCount.textContent = includeRelated && related
      ? `${direct} direct + ${related} related`
      : `${direct} direct ancestor${direct === 1 ? "" : "s"}`;
  }

  function closeDrawer() {
    if (!drawer || !backdrop) return;
    drawer.classList.remove("is-open");
    backdrop.classList.remove("is-open");
    drawer.setAttribute("aria-hidden", "true");
    document.body.classList.remove("drawer-open");
    rows.forEach(row => row.classList.remove("is-active"));
    detailPanels.forEach(panel => panel.classList.remove("is-active"));
    activeRecordId = "";
  }

  function escapeHtml(value) {
    return String(value || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function initAncestorMap(panel) {
    if (!panel || !window.L) return;
    const mapNode = panel.querySelector("[data-ancestor-map]");
    if (!mapNode || mapInstances.has(mapNode)) {
      const existing = mapNode ? mapInstances.get(mapNode) : null;
      if (existing) setTimeout(() => existing.invalidateSize(), 30);
      return;
    }

    const points = Array.from(mapNode.querySelectorAll("[data-map-point]"))
      .map(point => ({
        lat: Number(point.dataset.lat),
        lng: Number(point.dataset.lng),
        title: point.dataset.title || "Place",
        url: point.dataset.placeUrl || "",
      }))
      .filter(point => Number.isFinite(point.lat) && Number.isFinite(point.lng));

    if (!points.length) {
      mapNode.hidden = true;
      return;
    }

    const map = window.L.map(mapNode, {
      zoomControl: true,
      attributionControl: true,
      scrollWheelZoom: false,
    });

    window.L.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png", {
      maxZoom: 18,
      attribution: "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors &copy; <a href='https://carto.com/attributions'>CARTO</a>",
    }).addTo(map);

    const bounds = [];
    points.forEach(point => {
      const marker = window.L.circleMarker([point.lat, point.lng], {
        radius: 6,
        color: "#8a4b1e",
        weight: 2,
        fillColor: "#8a4b1e",
        fillOpacity: 0.9,
      }).addTo(map);
      const title = escapeHtml(point.title);
      const popup = point.url ? `<a href="${escapeHtml(point.url)}">${title}</a>` : title;
      marker.bindPopup(popup);
      bounds.push([point.lat, point.lng]);
    });

    if (bounds.length === 1) {
      map.setView(bounds[0], 8);
    } else {
      map.fitBounds(bounds, { padding: [24, 24], maxZoom: 9 });
    }

    mapInstances.set(mapNode, map);
    setTimeout(() => map.invalidateSize(), 30);
  }

  function openDrawer(recordId) {
    const target = rows.find(row => row.dataset.recordId === recordId && !row.hidden);
    if (!target || !drawer || !backdrop) return;
    activeRecordId = target.dataset.recordId;

    rows.forEach(row => row.classList.toggle("is-active", row.dataset.recordId === activeRecordId));
    detailPanels.forEach(panel => panel.classList.toggle("is-active", panel.dataset.detailPanel === activeRecordId));
    drawer.classList.add("is-open");
    backdrop.classList.add("is-open");
    drawer.setAttribute("aria-hidden", "false");
    document.body.classList.add("drawer-open");
    if (closeButton) closeButton.focus({ preventScroll: true });
    initAncestorMap(detailPanels.find(panel => panel.dataset.detailPanel === activeRecordId));
  }

  function applyFilters() {
    rows.forEach(row => {
      row.hidden = !visibleByFilters(row);
    });
    tableRows.forEach(row => {
      row.hidden = !visibleByFilters(row);
    });
    updateEraBands();
    updateResultCount();

    const activeRow = activeRecordId ? rows.find(row => row.dataset.recordId === activeRecordId) : null;
    if (activeRow && activeRow.hidden) closeDrawer();
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

  function setRelated(value) {
    includeRelated = Boolean(value);
    relatedButtons.forEach(button => {
      const active = includeRelated ? button.dataset.relatedMode === "related" : button.dataset.relatedMode === "direct";
      button.classList.toggle("is-active", active);
      button.setAttribute("aria-pressed", active ? "true" : "false");
    });
    try { window.localStorage.setItem("gurneyIncludeRelated", includeRelated ? "true" : "false"); } catch (err) {}
    applyFilters();
  }

  rows.forEach(row => row.addEventListener("click", () => openDrawer(row.dataset.recordId)));
  rows.forEach(row => row.addEventListener("keydown", event => {
    if (event.key === "Enter" || event.key === " ") {
      event.preventDefault();
      openDrawer(row.dataset.recordId);
    }
  }));

  modeButtons.forEach(button => {
    button.addEventListener("click", () => setMode(button.dataset.catalogMode));
  });

  eraButtons.forEach(button => {
    button.addEventListener("click", () => {
      eraFilter = button.dataset.eraFilter;
      eraButtons.forEach(item => {
        const active = item === button;
        item.classList.toggle("is-active", active);
        item.setAttribute("aria-pressed", active ? "true" : "false");
      });
      applyFilters();
    });
  });

  relatedButtons.forEach(button => {
    button.addEventListener("click", () => setRelated(button.dataset.relatedMode === "related"));
  });
  if (closeButton) closeButton.addEventListener("click", closeDrawer);
  if (backdrop) backdrop.addEventListener("click", closeDrawer);

  document.addEventListener("keydown", event => {
    if (event.key === "Escape") closeDrawer();
  });

  const params = new URLSearchParams(window.location.search);
  let mode = "catalog";
  try { mode = window.localStorage.getItem("gurneyCatalogMode") || "catalog"; } catch (err) {}
  try { includeRelated = window.localStorage.getItem("gurneyIncludeRelated") === "true"; } catch (err) {}
  if (params.get("related") === "1") includeRelated = true;

  setMode(mode === "table" ? "table" : "catalog");
  setRelated(includeRelated);

  const requestedRecord = params.get("record");
  const requestedGen = params.get("gen");
  if (requestedRecord) {
    openDrawer(requestedRecord);
  } else if (requestedGen) {
    const row = rows.find(item => item.dataset.gen === requestedGen && !item.hidden);
    if (row) openDrawer(row.dataset.recordId);
  }
})();

(function () {
  const page = document.querySelector("[data-place-explorer]");
  if (!page) return;

  const rows = Array.from(page.querySelectorAll("[data-place-row]"));
  const panels = Array.from(page.querySelectorAll("[data-place-panel]"));
  const regionButtons = Array.from(page.querySelectorAll("[data-place-region-filter]"));
  const drawer = page.querySelector("[data-place-drawer]");
  const backdrop = page.querySelector("[data-place-backdrop]");
  const closeButton = page.querySelector("[data-place-close]");
  let regionFilter = "all";

  function closeDrawer() {
    if (!drawer || !backdrop) return;
    drawer.classList.remove("is-open");
    backdrop.classList.remove("is-open");
    drawer.setAttribute("aria-hidden", "true");
    document.body.classList.remove("drawer-open");
    rows.forEach(row => row.classList.remove("is-active"));
    panels.forEach(panel => panel.classList.remove("is-active"));
  }

  function openDrawer(placeId) {
    const target = rows.find(row => row.dataset.placeId === placeId && !row.hidden);
    if (!target || !drawer || !backdrop) return;
    rows.forEach(row => row.classList.toggle("is-active", row.dataset.placeId === placeId));
    panels.forEach(panel => panel.classList.toggle("is-active", panel.dataset.placePanel === placeId));
    drawer.classList.add("is-open");
    backdrop.classList.add("is-open");
    drawer.setAttribute("aria-hidden", "false");
    document.body.classList.add("drawer-open");
    if (closeButton) closeButton.focus({ preventScroll: true });
  }

  function applyRegionFilter() {
    rows.forEach(row => {
      row.hidden = regionFilter !== "all" && row.dataset.placeRegion !== regionFilter;
    });
    const active = rows.find(row => row.classList.contains("is-active"));
    if (active && active.hidden) closeDrawer();
  }

  rows.forEach(row => row.addEventListener("click", () => openDrawer(row.dataset.placeId)));
  rows.forEach(row => row.addEventListener("keydown", event => {
    if (event.key === "Enter" || event.key === " ") {
      event.preventDefault();
      openDrawer(row.dataset.placeId);
    }
  }));

  if (closeButton) closeButton.addEventListener("click", closeDrawer);
  if (backdrop) backdrop.addEventListener("click", closeDrawer);
  regionButtons.forEach(button => {
    button.addEventListener("click", () => {
      regionFilter = button.dataset.placeRegionFilter || "all";
      regionButtons.forEach(item => {
        const active = item === button;
        item.classList.toggle("is-active", active);
        item.setAttribute("aria-pressed", active ? "true" : "false");
      });
      applyRegionFilter();
    });
  });
  document.addEventListener("keydown", event => {
    if (event.key === "Escape") closeDrawer();
  });

  const params = new URLSearchParams(window.location.search);
  const requestedPlace = params.get("place");
  if (requestedPlace) openDrawer(requestedPlace);
})();
