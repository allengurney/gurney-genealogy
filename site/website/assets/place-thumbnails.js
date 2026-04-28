(function () {
  const page = document.querySelector("[data-place-explorer]");
  if (!page || !window.L) return;

  const thumbs = Array.from(page.querySelectorAll("[data-place-map-thumb]"))
    .map(item => ({
      root: item,
      mapNode: item.querySelector("[data-place-mini-map]"),
      button: item.querySelector(".place-map-button"),
      popover: item.querySelector("[data-place-map-popover]"),
      lat: Number(item.dataset.lat),
      lng: Number(item.dataset.lng),
      title: item.dataset.placeTitle || "Place",
    }))
    .filter(item => item.mapNode && Number.isFinite(item.lat) && Number.isFinite(item.lng));

  if (!thumbs.length) return;

  function closePopovers(except) {
    thumbs.forEach(item => {
      if (item !== except) item.root.classList.remove("is-open");
    });
  }

  function initMap(item) {
    if (item.map) return;

    item.map = window.L.map(item.mapNode, {
      attributionControl: false,
      dragging: false,
      scrollWheelZoom: false,
      doubleClickZoom: false,
      boxZoom: false,
      keyboard: false,
      zoomControl: false,
      tap: false,
    }).setView([item.lat, item.lng], 15);

    window.L.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png", {
      maxZoom: 18,
    }).addTo(item.map);

    window.L.marker([item.lat, item.lng], {
      title: item.title,
      interactive: false,
    }).addTo(item.map);
  }

  const observer = "IntersectionObserver" in window
    ? new IntersectionObserver(entries => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            const item = thumbs.find(candidate => candidate.root === entry.target);
            if (item) initMap(item);
            observer.unobserve(entry.target);
          }
        });
      }, { rootMargin: "180px 0px" })
    : null;

  thumbs.forEach(item => {
    if (observer) observer.observe(item.root);
    else initMap(item);

    item.root.addEventListener("click", event => event.stopPropagation());
    item.root.addEventListener("keydown", event => event.stopPropagation());

    if (item.button) {
      item.button.addEventListener("click", event => {
        event.preventDefault();
        closePopovers(item);
        item.root.classList.toggle("is-open");
      });
    }
  });

  page.querySelectorAll("[data-place-interactive]").forEach(item => {
    item.addEventListener("click", event => event.stopPropagation());
    item.addEventListener("keydown", event => event.stopPropagation());
  });

  document.addEventListener("click", () => closePopovers());
  document.addEventListener("keydown", event => {
    if (event.key === "Escape") closePopovers();
  });
})();
