/*
 * Evidence drawer (Plan 04 §4–§8, §13–§14).
 *
 * Progressive enhancement over the permanent evidence/finding pages: every
 * Evidence link and related-item link keeps an ordinary href, and any failure
 * falls through to normal navigation. With JavaScript, an Evidence link opens
 * a right-side drawer (bottom sheet on small screens) showing the marker
 * bundle; related research items pivot in place with a trail, browser
 * history, and focus management.
 */
(function () {
  "use strict";
  if (typeof window === "undefined" || !window.document) return;
  var render = window.G13GraphRender;
  if (!render || !window.fetch || !window.history || !window.history.pushState) return;

  var DATA_BASE = "/assets/g13-graph/";
  var cache = { json: {} };
  var shared = null; // { labelById, sources, siteMap }
  var drawer = null; // { root, backdrop, body, trail, backButton, closeButton, foot }
  var state = null; // { items: [{type, id}], trigger }
  var closingSteps = 0; // popstate events to swallow while unwinding on close

  // The site header is sticky (z-index 2500); the drawer opens below it.
  function updateDrawerTop() {
    var header = document.querySelector(".site-header");
    var offset = 0;
    if (header) {
      var rect = header.getBoundingClientRect();
      if (rect.bottom > 0) offset = Math.max(0, Math.round(rect.bottom));
    }
    document.documentElement.style.setProperty("--g13-drawer-top", offset + "px");
  }
  window.addEventListener("resize", function () {
    if (drawer && !drawer.root.hidden) updateDrawerTop();
  });

  function fetchJson(relative) {
    if (cache.json[relative]) return cache.json[relative];
    cache.json[relative] = fetch(DATA_BASE + relative, { credentials: "same-origin" }).then(function (response) {
      if (!response.ok) throw new Error("fetch failed: " + relative);
      return response.json();
    });
    return cache.json[relative];
  }

  function loadShared() {
    if (shared) return Promise.resolve(shared);
    return Promise.all([
      fetchJson("findings.json"),
      fetchJson("sources.json"),
      fetchJson("site-map.json"),
      fetchJson("manifest.json"),
    ]).then(function (results) {
      var labelById = {};
      results[0].forEach(function (entry) { labelById[entry.id] = entry; });
      shared = {
        labelById: labelById,
        sources: results[1],
        siteMap: results[2],
        revision: String(results[3].database_revision || ""),
      };
      return shared;
    });
  }

  function buildCtx() {
    return {
      labelFor: function (id) { return shared.labelById[id] || null; },
      source: function (sourceId) { return shared.sources[sourceId] || null; },
      topicUrl: function (unitId) { return (shared.siteMap.topics || {})[unitId] || null; },
      publicationUrl: function (publicationPath) {
        var publications = shared.siteMap.publications || [];
        for (var i = 0; i < publications.length; i += 1) {
          if (publicationPath.indexOf(publications[i].prefix) === 0) return publications[i];
        }
        return null;
      },
    };
  }

  // ------------------------------ drawer DOM ------------------------------
  function ensureDrawer() {
    if (drawer) return drawer;
    var backdrop = document.createElement("div");
    backdrop.className = "g13-drawer-backdrop";
    backdrop.hidden = true;

    var root = document.createElement("aside");
    root.className = "g13-drawer";
    root.setAttribute("role", "dialog");
    root.setAttribute("aria-modal", "true");
    root.setAttribute("aria-label", "Evidence");
    root.hidden = true;
    root.innerHTML =
      '<div class="g13-drawer-head">' +
      '<button type="button" class="g13-drawer-back" hidden>‹ Back</button>' +
      '<span class="g13-drawer-trail"></span>' +
      '<button type="button" class="g13-drawer-close" aria-label="Close evidence drawer">Close</button>' +
      "</div>" +
      '<div class="g13-drawer-body" tabindex="-1"></div>' +
      '<div class="g13-drawer-foot"></div>';

    document.body.appendChild(backdrop);
    document.body.appendChild(root);

    drawer = {
      root: root,
      backdrop: backdrop,
      body: root.querySelector(".g13-drawer-body"),
      trail: root.querySelector(".g13-drawer-trail"),
      backButton: root.querySelector(".g13-drawer-back"),
      closeButton: root.querySelector(".g13-drawer-close"),
      foot: root.querySelector(".g13-drawer-foot"),
    };

    drawer.closeButton.addEventListener("click", function () { requestClose(); });
    drawer.backButton.addEventListener("click", function () { window.history.back(); });
    backdrop.addEventListener("click", function () { requestClose(); });
    root.addEventListener("keydown", function (event) {
      if (event.key === "Escape") {
        event.preventDefault();
        requestClose();
        return;
      }
      if (event.key !== "Tab") return;
      // Simple focus trap while the drawer is modal.
      var focusable = root.querySelectorAll(
        'button:not([hidden]), a[href], summary, [tabindex]:not([tabindex="-1"])'
      );
      if (!focusable.length) return;
      var first = focusable[0];
      var last = focusable[focusable.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    });
    // Related-item pivots inside the drawer replace its contents in place.
    drawer.body.addEventListener("click", function (event) {
      var link = event.target.closest ? event.target.closest("a[data-g13-finding]") : null;
      if (!link) return;
      if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return; // allow new-tab
      event.preventDefault();
      var findingId = link.getAttribute("data-g13-finding");
      var items = state.items.concat([{ type: "finding", id: findingId }]);
      showItems(items, { push: true }).catch(function () {
        window.location.href = link.href;
      });
    });
    return drawer;
  }

  function permanentUrlFor(entry) {
    return entry.type === "marker" ? render.markerUrl(entry.id) : render.findingUrl(entry.id);
  }

  function labelForEntry(entry, payload) {
    if (entry.type === "marker") {
      var primary = payload.primary || {};
      return primary.shortLabel || primary.statement || "Evidence";
    }
    return payload.shortLabel || payload.statement || "Research item";
  }

  function fetchEntry(entry) {
    return entry.type === "marker"
      ? fetchJson("marker-bundles/" + entry.id + ".json")
      : fetchJson("findings/" + entry.id + ".json");
  }

  function renderEntry(entry, payload) {
    var ctx = buildCtx();
    var opts = { compact: true, headingTag: "h2", revision: shared.revision };
    return entry.type === "marker"
      ? render.renderMarkerBundle(payload, ctx, opts)
      : render.renderFinding(payload, ctx, opts);
  }

  function showItems(items, options) {
    ensureDrawer();
    var entry = items[items.length - 1];
    return loadShared()
      .then(function () { return fetchEntry(entry); })
      .then(function (payload) {
        state = state || { items: [], trigger: null };
        state.items = items;
        var label = labelForEntry(entry, payload);

        drawer.body.innerHTML = renderEntry(entry, payload);
        var trailParts = ["Evidence"].concat(
          items.map(function (item, index) {
            if (item.label) return item.label;
            return index === items.length - 1 ? label : item.id;
          })
        );
        entry.label = label;
        drawer.trail.textContent = trailParts.join(" › ");
        drawer.backButton.hidden = items.length < 2;
        drawer.foot.innerHTML =
          '<a href="' + render.escapeHtml(permanentUrlFor(entry)) + '">Open full screen</a>';

        var wasHidden = drawer.root.hidden;
        updateDrawerTop();
        drawer.root.hidden = false;
        drawer.backdrop.hidden = false;
        document.body.style.overflow = "hidden";
        document.body.classList.add("g13-drawer-open");
        if (wasHidden) {
          drawer.root.setAttribute("data-opening", "");
          requestAnimationFrame(function () {
            requestAnimationFrame(function () { drawer.root.removeAttribute("data-opening"); });
          });
        }
        if (options && options.push) {
          window.history.pushState(
            { g13Drawer: { items: items.map(function (item) { return { type: item.type, id: item.id, label: item.label }; }) } },
            "",
            window.location.href
          );
        }
        var heading = drawer.body.querySelector(".g13-heading");
        if (heading) {
          heading.setAttribute("tabindex", "-1");
          heading.focus();
        } else {
          drawer.body.focus();
        }
      });
  }

  function closeDrawer() {
    if (!drawer || drawer.root.hidden) return;
    drawer.root.hidden = true;
    drawer.backdrop.hidden = true;
    document.body.style.overflow = "";
    document.body.classList.remove("g13-drawer-open");
    var trigger = state && state.trigger;
    state = null;
    if (trigger && document.contains(trigger)) trigger.focus();
  }

  // Close via control/Escape/backdrop: close the DOM immediately (never leave
  // the reader stuck), then unwind the history entries this drawer pushed so
  // browser Back stays consistent. A stale g13Drawer entry can survive a page
  // reload, so the unwind swallows its popstate instead of re-rendering.
  function requestClose() {
    var depth = state && state.items ? state.items.length : 0;
    var historyState = window.history.state;
    closeDrawer();
    if (depth && historyState && historyState.g13Drawer) {
      closingSteps = 1;
      try {
        window.history.go(-depth);
      } catch (error) {
        closingSteps = 0;
      }
    }
  }

  window.addEventListener("popstate", function (event) {
    if (closingSteps > 0) {
      closingSteps -= 1;
      closeDrawer();
      return;
    }
    var drawerState = event.state && event.state.g13Drawer;
    if (drawerState && drawerState.items && drawerState.items.length) {
      showItems(drawerState.items.slice(), { push: false }).catch(function () {
        closeDrawer();
      });
    } else {
      closeDrawer();
    }
  });

  document.addEventListener("click", function (event) {
    var link = event.target.closest ? event.target.closest("a.evidence-link[data-evidence-id]") : null;
    if (!link) return;
    if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    var markerId = link.getAttribute("data-evidence-id");
    var opening = { type: "marker", id: markerId };
    state = { items: [], trigger: link };
    showItems([opening], { push: true }).catch(function () {
      // Failed fetch: never leave the reader in an empty drawer.
      window.location.href = link.href;
    });
  });
})();
