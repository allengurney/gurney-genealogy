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
  const countNode = page.querySelector("[data-map-count]");
  const markers = [];
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

    if (requestedPlaceId) {
      const requestedMarker = markers.find(marker => marker.__point.placeId === requestedPlaceId);
      if (requestedMarker) {
        const point = requestedMarker.__point;
        map.setView([point.lat, point.lng], 13);
        requestedMarker.openPopup();
      }
    }
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

  if (requestedPlaceId) {
    includeRelated = true;
    relatedButtons.forEach(button => {
      const active = button.dataset.mapRelated === "related";
      button.classList.toggle("is-active", active);
      button.setAttribute("aria-pressed", active ? "true" : "false");
    });
  }

  redraw();
})();
