(function () {
  const page = document.querySelector("[data-generated-map]");
  if (!page || !window.L) return;

  const canvas = page.querySelector("[data-map-canvas]");
  const allPoints = Array.from(page.querySelectorAll("[data-map-point]"))
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
  const mappedPlaceIds = new Set(
    allPoints
      .filter(point => point.recordType !== "place")
      .map(point => point.placeId)
      .filter(Boolean)
  );
  const points = allPoints.filter(point => point.recordType !== "place" || !mappedPlaceIds.has(point.placeId));

  const relatedButtons = Array.from(page.querySelectorAll("[data-map-related]"));
  const kindButtons = Array.from(page.querySelectorAll("[data-map-kind]"));
  const eraButtons = Array.from(page.querySelectorAll("[data-map-era]"));
  const overlayMenu = page.querySelector("[data-overlay-menu]");
  const overlayMenuButton = page.querySelector("[data-overlay-menu-button]");
  const overlayMenuPanel = page.querySelector("[data-overlay-menu-panel]");
  let overlayToggles = Array.from(page.querySelectorAll("[data-overlay-toggle]"));
  const countNode = page.querySelector("[data-map-count]");
  const markers = [];
  const overlayLayers = new Map();
  const overlayGeometries = new Set(["Polygon", "MultiPolygon", "LineString", "MultiLineString", "Point", "MultiPoint"]);
  const params = new URLSearchParams(window.location.search);
  const requestedPlaceId = params.get("place");
  let includeRelated = false;
  let kind = "all";
  let era = "all";

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

  const overlayPointPane = map.createPane("gournayOverlayPointPane");
  overlayPointPane.style.zIndex = 575;

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
    if (group.recordType === "place") {
      return `<div class="map-popup">
        <strong>${placeLink}</strong>
        <span>${escapeHtml(group.region)}</span>
        <span>${escapeHtml(group.event)}</span>
        <p>${escapeHtml(group.description)}</p>
      </div>`;
    }

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
    const marker = group.kind === "registry"
      ? window.L.circleMarker([group.lat, group.lng], {
          radius: 4.5,
          color: "#2f5e74",
          weight: 1.5,
          fillColor: group.color,
          fillOpacity: 0.62,
          pane: "gurneyMarkerPane",
        })
      : group.kind === "property"
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
    marker.bindTooltip(group.recordType === "place" ? group.place : group.people.length > 1 ? `${group.people.length} records: ${group.place}` : `${group.people[0].gen} ${group.place}`);
    marker.__point = group;
    return marker;
  }

  function visible(point) {
    const relatedOk = includeRelated || point.recordType !== "related";
    const kindOk = kind === "all" || point.kind === kind;
    const eraOk = era === "all" || point.eraClass === era;
    return relatedOk && kindOk && eraOk;
  }

  const overlayGroupLabels = {
    older_gournay_core: "Older Gournay core",
    frontier_context: "Epte frontier context",
    direct_gournay_frontier_corridor: "Direct frontier corridor",
    beauvaisis_24_villages: "Beauvaisis / 24 villages",
    gournay_chatelainie_dependencies: "Gournay chatellenie dependencies",
    gournay_western_dependency_context: "Avesnes / Ferrieres dependency",
    northern_gournay_honor_context: "Northern honor context",
    g33_bec_endowment_cluster: "G33 Bec endowment cluster",
    later_gournay_institutional: "Later institutional context",
    southern_boundary_context: "Southern boundary context",
  };

  function groupLabel(group) {
    return overlayGroupLabels[group] || String(group || "Overlay").replace(/[_-]+/g, " ");
  }

  function overlayGroup(feature) {
    const properties = feature.properties || {};
    if (properties.display_group) return properties.display_group;

    const id = feature.id || "";
    const featureType = properties.feature_type;

    if ([
      "older_gournay_core_repo",
      "buffer_gournay_4km",
      "point_gournay_en_bray",
      "point_ferrieres_en_bray",
      "point_cuy_saint_fiacre",
    ].includes(id)) return "older_gournay_core";

    if ([
      "beauvaisis_24_villages_repo",
      "beauvaisis_24_villages_expanded_3km",
      "point_beauvaisis_acquisitions_centroid",
      "point_molagnies",
      "point_gancourt_saint_etienne",
      "point_saint_quentin_des_pres",
      "point_sully",
      "point_hericourt_sur_therain",
      "point_songeons",
      "point_loueuse",
      "point_beauvais",
    ].includes(id)) return "beauvaisis_24_villages";

    if ([
      "gournay_la_ferte_gaillefontaine_frontier_corridor",
      "buffer_la_ferte_3km",
      "buffer_gaillefontaine_4km",
      "buffer_sigy_2km",
      "buffer_fry_1_5km",
      "point_la_ferte_saint_samson_la_ferte_en_bray",
      "point_gaillefontaine",
      "point_sigy_abbaye_saint_martin",
      "point_fry_eglise_saint_martin",
    ].includes(id)) return "direct_gournay_frontier_corridor";

    if ([
      "pays_de_bray_context_envelope",
      "point_pays_de_bray_centroid",
    ].includes(id)) return "older_gournay_core";

    if ([
      "norman_gournay_landholding_network_envelope",
      "buffer_montigny_3km",
      "buffer_ecouche_2_5km",
      "point_montigny_sur_andelle",
      "point_ecouche",
      "point_abbey_of_bec_le_bec_hellouin",
    ].includes(id)) return "g33_bec_endowment_cluster";

    if (id === "epte_frontier_line") return "frontier_context";
    if (featureType === "source_point_buffer" || id.startsWith("buffer_")) return "g33_bec_endowment_cluster";
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

  function overlayPointStyle(feature) {
    const properties = feature.properties || {};
    const sourceStyle = properties.style || {};
    const color = sourceStyle.markerColor || sourceStyle.color || "#7a4b16";
    const listedPlace = properties.feature_type === "listed_place";
    const centroid = String(properties.feature_type || "").includes("centroid");

    return {
      pane: "gournayOverlayPointPane",
      radius: centroid ? 4 : listedPlace ? 4.5 : 5.5,
      color,
      weight: centroid ? 1.5 : 2,
      opacity: 0.9,
      fillColor: "#ffffff",
      fillOpacity: centroid ? 0.55 : 0.85,
      dashArray: centroid ? "3 3" : null,
    };
  }

  function overlayPointLayer(feature, latlng) {
    const properties = feature.properties || {};
    const sourceStyle = properties.style || {};
    const color = sourceStyle.markerColor || sourceStyle.color || "#446b58";
    if (properties.feature_type === "overlay_place_anchor") {
      return window.L.marker(latlng, {
        pane: "gournayOverlayPointPane",
        icon: window.L.divIcon({
          className: "map-overlay-anchor-marker",
          html: `<span style="--anchor-color:${escapeHtml(color)}"></span>`,
          iconSize: [14, 14],
          iconAnchor: [7, 7],
        }),
      });
    }
    return window.L.circleMarker(latlng, overlayPointStyle(feature));
  }

  function overlaySourceLinks(sourceUrls) {
    if (!Array.isArray(sourceUrls) || !sourceUrls.length) return "";
    const links = sourceUrls
      .map(url => {
        const safeUrl = escapeHtml(url);
        if (/^https?:\/\//.test(url)) {
          return `<li><a href="${safeUrl}" target="_blank" rel="noopener">${safeUrl}</a></li>`;
        }
        return `<li>${safeUrl}</li>`;
      })
      .join("");
    return `<dt>Sources</dt><dd><ul class="overlay-source-links">${links}</ul></dd>`;
  }

  function overlayPopup(feature) {
    const properties = feature.properties || {};
    const rows = [
      ["Type", properties.feature_type],
      ["Role", properties.anchor_role],
      ["Certainty", properties.certainty],
      ["Display group", properties.display_group || properties.layer_group],
      ["Precision", properties.coordinate_precision],
      ["Buffer", properties.buffer_km ? `${properties.buffer_km} km` : properties.buffer_meters],
      ["Status", properties.status],
      ["Future default", properties.future_default_after_review === false ? "Off after review" : ""],
      ["Basis", properties.historical_basis],
      ["Note", properties.interpretation_note],
    ]
      .filter(([, value]) => value !== undefined && value !== null && value !== "")
      .map(([label, value]) => `<dt>${escapeHtml(label)}</dt><dd>${escapeHtml(value)}</dd>`)
      .join("");

    return `<div class="map-popup overlay-popup">
      <strong>${escapeHtml(properties.name || feature.id || "Gournay holdings overlay")}</strong>
      <dl>${rows}${overlaySourceLinks(properties.source_urls)}</dl>
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

  function setOverlayMenuOpen(open) {
    if (!overlayMenu || !overlayMenuButton || !overlayMenuPanel) return;
    overlayMenu.classList.toggle("is-open", open);
    overlayMenuButton.setAttribute("aria-expanded", open ? "true" : "false");
    overlayMenuPanel.hidden = !open;
  }

  function renderHoldingOverlays(data) {
    ensureOverlayControls(data);
    const groups = Array.from(new Set(overlayToggles.map(toggle => toggle.dataset.overlayToggle)));
    groups.forEach(group => {
      const groupFeatures = (data.features || []).filter(feature => overlayGroup(feature) === group);
      const groupHasDefaultFeatures = groupFeatures.some(feature => (feature.properties || {}).display_default !== false);
      const layer = window.L.geoJSON(data, {
        pane: "gournayHoldingsPane",
        filter: feature => {
          const properties = feature.properties || {};
          return overlayGeometries.has(feature.geometry && feature.geometry.type)
            && overlayGroup(feature) === group
            && (!groupHasDefaultFeatures || properties.display_default !== false);
        },
        style: overlayStyle,
        pointToLayer: overlayPointLayer,
        onEachFeature: (feature, layer) => {
          const name = feature.properties && feature.properties.name;
          layer.bindPopup(overlayPopup(feature));
          if (name) layer.bindTooltip(name, { sticky: true });
        },
      });

      overlayLayers.set(group, layer);

      const toggle = overlayToggles.find(item => item.dataset.overlayToggle === group);
      if (!toggle || toggle.checked) {
        layer.addTo(map);
        layer.bringToBack();
      }
    });

    focusRequestedPlace();
  }

  function bindOverlayToggle(toggle) {
    toggle.addEventListener("change", () => {
      setOverlayVisibility(toggle.dataset.overlayToggle, toggle.checked);
    });
  }

  function ensureOverlayControls(data) {
    if (!overlayMenuPanel) return;
    const existingGroups = new Set(overlayToggles.map(toggle => toggle.dataset.overlayToggle));
    const groups = Array.from(new Set((data.features || []).map(overlayGroup).filter(Boolean)));
    groups.forEach(group => {
      if (existingGroups.has(group)) return;
      const groupFeatures = (data.features || []).filter(feature => overlayGroup(feature) === group);
      const checked = groupFeatures.some(feature => (feature.properties || {}).display_default !== false);
      const label = document.createElement("label");
      const input = document.createElement("input");
      input.type = "checkbox";
      input.dataset.overlayToggle = group;
      input.checked = checked;
      label.appendChild(input);
      label.append(` ${groupLabel(group)}`);
      overlayMenuPanel.appendChild(label);
      bindOverlayToggle(input);
      overlayToggles.push(input);
      existingGroups.add(group);
    });
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

  overlayToggles.forEach(bindOverlayToggle);

  if (overlayMenuButton && overlayMenuPanel) {
    overlayMenuButton.addEventListener("click", event => {
      event.stopPropagation();
      setOverlayMenuOpen(overlayMenuPanel.hidden);
    });
    overlayMenuPanel.addEventListener("click", event => event.stopPropagation());
    document.addEventListener("click", () => setOverlayMenuOpen(false));
    document.addEventListener("keydown", event => {
      if (event.key === "Escape") setOverlayMenuOpen(false);
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
