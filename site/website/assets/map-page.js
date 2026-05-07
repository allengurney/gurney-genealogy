(function () {
  const page = document.querySelector("[data-generated-map]");
  if (!page || !window.L) return;

  const canvas = page.querySelector("[data-map-canvas]");
  const points = Array.from(page.querySelectorAll("[data-map-point]"))
    .map(point => ({
      recordType: point.dataset.recordType,
      kind: point.dataset.kind,
      gen: point.dataset.gen,
      name: point.dataset.name,
      dates: point.dataset.dates,
      era: point.dataset.era,
      eraClass: point.dataset.eraClass,
      color: point.dataset.color || "#8a4b1e",
      place: point.dataset.place,
      placeId: point.dataset.placeId,
      region: point.dataset.region,
      event: point.dataset.event,
      description: point.dataset.description,
      lat: Number(point.dataset.lat),
      lng: Number(point.dataset.lng),
      placeUrl: point.dataset.placeUrl,
      personUrl: point.dataset.personUrl,
    }))
    .filter(point => Number.isFinite(point.lat) && Number.isFinite(point.lng));

  const relatedButtons = Array.from(page.querySelectorAll("[data-map-related]"));
  const kindButtons = Array.from(page.querySelectorAll("[data-map-kind]"));
  const eraButtons = Array.from(page.querySelectorAll("[data-map-era]"));
  const overlayToggles = Array.from(page.querySelectorAll("[data-overlay-toggle]"));
  const overlayZoomButton = page.querySelector("[data-overlay-zoom]");
  const countNode = page.querySelector("[data-map-count]");
  const markers = [];
  const overlayLayers = new Map();
  const overlayGeometries = new Set(["Polygon", "MultiPolygon", "LineString", "MultiLineString"]);
  const params = new URLSearchParams(window.location.search);
  const requestedPlaceId = params.get("place");
  let includeRelated = false;
  let kind = "all";
  let era = "all";
  let overlayBounds = null;

  function escapeHtml(value) {
    return String(value || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  const map = window.L.map(canvas, {
    zoomControl: true,
    attributionControl: true,
    scrollWheelZoom: true,
  });

  const holdingsPane = map.createPane("gournayHoldingsPane");
  holdingsPane.style.zIndex = 350;

  const markerPane = map.createPane("gurneyMarkerPane");
  markerPane.style.zIndex = 650;

  window.L.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png", {
    maxZoom: 18,
    attribution: "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors &copy; <a href='https://carto.com/attributions'>CARTO</a>",
  }).addTo(map);

  function groupKey(point) {
    return [
      point.kind,
      point.placeId,
      point.placeUrl,
      point.place,
      point.lat.toFixed(6),
      point.lng.toFixed(6),
    ].join("|");
  }

  function groupedPoints(items) {
    const groups = new Map();
    items.forEach(point => {
      const key = groupKey(point);
      if (!groups.has(key)) groups.set(key, { ...point, people: [] });
      groups.get(key).people.push(point);
    });
    return Array.from(groups.values());
  }

  function personLine(point, compact) {
    const label = `${escapeHtml(point.gen)} ${escapeHtml(point.name)}`;
    const linked = point.personUrl ? `<a href="${escapeHtml(point.personUrl)}">${label}</a>` : label;
    return compact || !point.dates ? linked : `${linked} <span>${escapeHtml(point.dates)}</span>`;
  }

  function popup(group) {
    const placeLink = group.placeUrl ? `<a href="${escapeHtml(group.placeUrl)}">${escapeHtml(group.place)}</a>` : escapeHtml(group.place);
    const compactPeople = group.people.length > 2;
    const people = group.people
      .map(point => `<li>${personLine(point, compactPeople)}</li>`)
      .join("");
    return `<div class="map-popup">
      <ul class="map-popup-people">${people}</ul>
      <hr>
      <strong>${placeLink}</strong>
      <span>${escapeHtml(group.region)}</span>
      <span>${escapeHtml(group.event)}</span>
      <p>${escapeHtml(group.description)}</p>
    </div>`;
  }

  function makeMarker(group) {
    const marker = group.kind === "property"
      ? window.L.marker([group.lat, group.lng], {
          pane: "gurneyMarkerPane",
          icon: window.L.divIcon({
            className: "map-square-marker",
            html: `<span style="background:${escapeHtml(group.color)}"></span>`,
            iconSize: [16, 16],
            iconAnchor: [8, 8],
          }),
        })
      : window.L.circleMarker([group.lat, group.lng], {
          radius: 6,
          color: group.color,
          weight: 2,
          fillColor: group.color,
          fillOpacity: 0.88,
          pane: "gurneyMarkerPane",
        });
    marker.bindPopup(popup(group));
    marker.bindTooltip(group.people.length > 1 ? `${group.people.length} records: ${group.place}` : `${group.people[0].gen} ${group.place}`);
    marker.__point = group;
    return marker;
  }

  function visible(point) {
    const relatedOk = includeRelated || point.recordType !== "related";
    const kindOk = kind === "all" || point.kind === kind;
    const eraOk = era === "all" || point.eraClass === era;
    return relatedOk && kindOk && eraOk;
  }

  function overlayGroup(feature) {
    const id = feature.id || "";
    const featureType = feature.properties && feature.properties.feature_type;
    if (id === "older_gournay_core_repo") return "older-gournay-core";
    if (id === "beauvaisis_24_villages_repo") return "beauvaisis-24-villages";
    if (id === "beauvaisis_24_villages_expanded_3km") return "expanded-24-village-buffer";
    if (id === "gournay_la_ferte_gaillefontaine_frontier_corridor") return "frontier-corridor";
    if (id === "pays_de_bray_context_envelope") return "pays-de-bray-context";
    if (id === "norman_gournay_landholding_network_envelope") return "network-envelope";
    if (id === "epte_frontier_line") return "epte-frontier-line";
    if (featureType === "source_point_buffer" || id.startsWith("buffer_")) return "individual-buffers";
    return "";
  }

  function overlayStyle(feature) {
    const properties = feature.properties || {};
    const sourceStyle = properties.style || {};
    const style = {
      color: "#7a4b16",
      weight: 2,
      opacity: 0.65,
      fillColor: "#c58a2b",
      fillOpacity: 0.12,
      ...sourceStyle,
      pane: "gournayHoldingsPane",
    };

    if (feature.geometry && feature.geometry.type.includes("LineString")) {
      style.fillOpacity = 0;
      style.fill = false;
    }

    return style;
  }

  function overlayPopup(feature) {
    const properties = feature.properties || {};
    const rows = [
      ["Type", properties.feature_type],
      ["Certainty", properties.certainty],
      ["Group", properties.display_group || properties.layer_group],
      ["Buffer", properties.buffer_km ? `${properties.buffer_km} km` : properties.buffer_meters],
      ["Basis", properties.historical_basis],
      ["Note", properties.interpretation_note],
    ]
      .filter(([, value]) => value !== undefined && value !== null && value !== "")
      .map(([label, value]) => `<dt>${escapeHtml(label)}</dt><dd>${escapeHtml(value)}</dd>`)
      .join("");

    return `<div class="map-popup overlay-popup">
      <strong>${escapeHtml(properties.name || feature.id || "Gournay holdings overlay")}</strong>
      <dl>${rows}</dl>
    </div>`;
  }

  function focusRequestedPlace() {
    if (!requestedPlaceId) return;
    const requestedMarker = markers.find(marker => marker.__point.placeId === requestedPlaceId);
    if (requestedMarker) {
      const point = requestedMarker.__point;
      map.setView([point.lat, point.lng], 13);
      requestedMarker.openPopup();
    }
  }

  function setOverlayVisibility(group, enabled) {
    const layer = overlayLayers.get(group);
    if (!layer) return;
    if (enabled && !map.hasLayer(layer)) {
      layer.addTo(map);
      layer.bringToBack();
    }
    if (!enabled && map.hasLayer(layer)) map.removeLayer(layer);
  }

  function renderHoldingOverlays(data) {
    const groups = Array.from(new Set(overlayToggles.map(toggle => toggle.dataset.overlayToggle)));
    groups.forEach(group => {
      const layer = window.L.geoJSON(data, {
        pane: "gournayHoldingsPane",
        filter: feature => overlayGeometries.has(feature.geometry && feature.geometry.type) && overlayGroup(feature) === group,
        style: overlayStyle,
        onEachFeature: (feature, layer) => {
          const name = feature.properties && feature.properties.name;
          layer.bindPopup(overlayPopup(feature));
          if (name) layer.bindTooltip(name, { sticky: true });
        },
      });

      overlayLayers.set(group, layer);

      if (layer.getBounds && layer.getBounds().isValid()) {
        overlayBounds = overlayBounds ? overlayBounds.extend(layer.getBounds()) : layer.getBounds();
      }

      const toggle = overlayToggles.find(item => item.dataset.overlayToggle === group);
      if (!toggle || toggle.checked) {
        layer.addTo(map);
        layer.bringToBack();
      }
    });

    focusRequestedPlace();
  }

  function loadHoldingOverlays() {
    if (!overlayToggles.length) return;
    fetch("/assets/data/gournay-norman-holdings-overlays.geojson")
      .then(response => {
        if (!response.ok) throw new Error(`Overlay request failed: ${response.status}`);
        return response.json();
      })
      .then(renderHoldingOverlays)
      .catch(error => {
        console.warn("Unable to load Gournay holdings overlays", error);
      });
  }

  function redraw() {
    markers.forEach(marker => map.removeLayer(marker));
    markers.length = 0;

    const visiblePoints = points.filter(visible);
    const groups = groupedPoints(visiblePoints);
    const bounds = [];
    groups.forEach(group => {
      const marker = makeMarker(group).addTo(map);
      markers.push(marker);
      bounds.push([group.lat, group.lng]);
    });

    if (countNode) countNode.textContent = `${visiblePoints.length} mapped record${visiblePoints.length === 1 ? "" : "s"} / ${groups.length} place${groups.length === 1 ? "" : "s"}`;
    if (bounds.length) map.fitBounds(bounds, { padding: [30, 30], maxZoom: 7 });

    focusRequestedPlace();
  }

  relatedButtons.forEach(button => {
    button.addEventListener("click", () => {
      includeRelated = button.dataset.mapRelated === "related";
      relatedButtons.forEach(item => {
        const active = item === button;
        item.classList.toggle("is-active", active);
        item.setAttribute("aria-pressed", active ? "true" : "false");
      });
      redraw();
    });
  });

  kindButtons.forEach(button => {
    button.addEventListener("click", () => {
      kind = button.dataset.mapKind || "all";
      kindButtons.forEach(item => {
        const active = item === button;
        item.classList.toggle("is-active", active);
        item.setAttribute("aria-pressed", active ? "true" : "false");
      });
      redraw();
    });
  });

  eraButtons.forEach(button => {
    button.addEventListener("click", () => {
      era = button.dataset.mapEra || "all";
      eraButtons.forEach(item => {
        const active = item === button;
        item.classList.toggle("is-active", active);
        item.setAttribute("aria-pressed", active ? "true" : "false");
      });
      redraw();
    });
  });

  overlayToggles.forEach(toggle => {
    toggle.addEventListener("change", () => {
      setOverlayVisibility(toggle.dataset.overlayToggle, toggle.checked);
    });
  });

  if (overlayZoomButton) {
    overlayZoomButton.addEventListener("click", () => {
      if (overlayBounds && overlayBounds.isValid()) {
        map.fitBounds(overlayBounds, { padding: [34, 34], maxZoom: 10 });
      }
    });
  }

  if (requestedPlaceId) {
    includeRelated = true;
    relatedButtons.forEach(button => {
      const active = button.dataset.mapRelated === "related";
      button.classList.toggle("is-active", active);
      button.setAttribute("aria-pressed", active ? "true" : "false");
    });
  }

  redraw();
  loadHoldingOverlays();
})();
