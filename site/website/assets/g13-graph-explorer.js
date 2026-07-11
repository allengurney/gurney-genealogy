/*
 * G13 Context Graph explorer (view-only, static data).
 *
 * Two consumers in one file:
 *  - the explorer app page (#g13x-app): a filterable item list (mirrors the
 *    graph editor's Items tab), a relationship map (ego view of the selected
 *    item or source, or a whole-result overview map), and the full text
 *    treatment of the selection rendered through the shared G13GraphRender
 *    module — the same projection the evidence drawer and permanent finding
 *    pages use;
 *  - an embedded relationship map (#g13x-embed[data-item]) on each permanent
 *    finding page, drawn by the same scene builder; node clicks navigate to
 *    the target's permanent page or into the explorer.
 *
 * Data: /assets/g13-graph/ static JSON written by scripts/sync-g13-package.js
 * from the public graph export. No editing surface; everything is read-only.
 */
(function () {
  "use strict";
  if (typeof window === "undefined" || !window.document) return;
  var render = window.G13GraphRender;
  var root = document.getElementById("g13x-app");
  var embedRoot = document.getElementById("g13x-embed");
  if (!render || !window.fetch || (!root && !embedRoot)) return;

  var DATA_BASE = "/assets/g13-graph/";
  var SVG_NS = "http://www.w3.org/2000/svg";
  var STRENGTH_WIDTH = { strong: 2.4, moderate: 1.6, weak: 1, unknown: 1 };
  var CONFIDENCE_ORDER = ["high", "moderate-high", "moderate", "low"];
  var markerSerial = 0; // unique <marker> ids when several scenes share a page

  var state = {
    items: [],
    byId: {},
    edges: [],
    edgesByItem: {},
    sources: {},
    sourceUsage: {},
    siteMap: {},
    revision: "",
    filters: { q: "", kind: "", confidence: "", unit: "", year: "" },
    selected: null, // {type: "item"|"source", id} — ego-view center
    preview: null, // overview-map preview (item id)
    jsonCache: {},
  };

  var el = {}; // resolved after shell build

  function fetchJson(relative) {
    if (state.jsonCache[relative]) return state.jsonCache[relative];
    state.jsonCache[relative] = fetch(DATA_BASE + relative, { credentials: "same-origin" }).then(function (response) {
      if (!response.ok) throw new Error("fetch failed: " + relative);
      return response.json();
    });
    return state.jsonCache[relative];
  }

  function loadCore() {
    return Promise.all([
      fetchJson("explorer.json"),
      fetchJson("adjacency.json"),
      fetchJson("sources.json"),
      fetchJson("site-map.json"),
      fetchJson("manifest.json"),
    ]).then(function (results) {
      state.items = results[0].items || results[0];
      state.sourceUsage = results[0].sourceUsage || {};
      state.items.forEach(function (it) { state.byId[it.id] = it; });
      state.edges = results[1].edges || [];
      state.edges.forEach(function (edge) {
        (state.edgesByItem[edge.from] = state.edgesByItem[edge.from] || []).push(edge);
        (state.edgesByItem[edge.to] = state.edgesByItem[edge.to] || []).push(edge);
      });
      state.sources = results[2];
      state.siteMap = results[3];
      state.revision = String(results[4].database_revision || "");
    });
  }

  function ctx() {
    return {
      labelFor: function (id) { return state.byId[id] || null; },
      source: function (sourceId) { return state.sources[sourceId] || null; },
      topicUrl: function (unitId) { return (state.siteMap.topics || {})[unitId] || null; },
      publicationUrl: function (publicationPath) {
        var publications = state.siteMap.publications || [];
        for (var i = 0; i < publications.length; i += 1) {
          if (publicationPath.indexOf(publications[i].prefix) === 0) return publications[i];
        }
        return null;
      },
    };
  }

  function esc(value) { return render.escapeHtml(value); }
  function kindClass(kind) { return "kind-" + String(kind || "unknown").replace(/[^a-z_]/gi, ""); }

  function truncate(text, max) {
    text = String(text || "");
    return text.length > max ? text.slice(0, max - 1).replace(/\s+\S*$/, "") + "…" : text;
  }

  // sourceUsage: sourceId → [{id, role}] of citing research items.
  function usageList(sourceId) {
    var value = state.sourceUsage[sourceId];
    return Array.isArray(value) ? value.filter(function (entry) { return state.byId[entry.id]; }) : [];
  }

  function sourceLabel(sourceId) {
    var resolved = state.sources[sourceId] || {};
    return resolved.shortTitle || resolved.citation || sourceId;
  }

  function edgeVerb(type) {
    var spec = render.RELATIONS[type];
    return spec ? spec.out.toLowerCase() : String(type || "").toLowerCase().replace(/_/g, " ");
  }

  function roleVerb(role) {
    return String(role || "cited").replace(/_/g, " ");
  }

  // ------------------------------ filtering ------------------------------
  function yearBuckets() {
    var buckets = [];
    for (var y = 1600; y < 1670; y += 5) buckets.push([y, y + 4]);
    return buckets;
  }

  function filteredItems() {
    var f = state.filters;
    var q = f.q.trim().toLowerCase();
    var bounds = f.year ? f.year.split("-").map(Number) : null;
    return state.items.filter(function (it) {
      if (f.kind && it.kind !== f.kind) return false;
      if (f.confidence && (it.confidence || "") !== f.confidence) return false;
      if (f.unit && (!it.unit || it.unit.id !== f.unit)) return false;
      if (bounds && (!it.years || it.years[0] > bounds[1] || it.years[1] < bounds[0])) return false;
      if (q) {
        var hay = ((it.shortLabel || "") + " " + (it.statement || "") + " " + it.id + " " +
          (it.unit ? it.unit.title : "")).toLowerCase();
        if (hay.indexOf(q) === -1) return false;
      }
      return true;
    });
  }

  // ----------------------------- SVG helpers -----------------------------
  function svgEl(name, attrs) {
    var node = document.createElementNS(SVG_NS, name);
    Object.keys(attrs || {}).forEach(function (key) { node.setAttribute(key, attrs[key]); });
    return node;
  }

  function nodeBox(group, item, x, y, width, height, isCenter) {
    group.setAttribute("class", "g13x-node " + kindClass(item.kind) + (isCenter ? " g13x-node-center" : ""));
    group.setAttribute("transform", "translate(" + (x - width / 2) + "," + (y - height / 2) + ")");
    group.appendChild(svgEl("rect", { width: width, height: height, rx: 7 }));
    var kindText = svgEl("text", { x: 10, y: isCenter ? 16 : 15, "class": "nkind" });
    kindText.textContent = item.kindLabel;
    group.appendChild(kindText);
    // Three body rows below the kind-label row.
    var lineHeight = isCenter ? 16 : 14;
    var firstLineY = isCenter ? 33 : 30;
    var perLine = Math.floor((width - 20) / (isCenter ? 6.6 : 5.9));
    var label = truncate(item.shortLabel || item.statement, perLine * 3 + 4);
    var words = label.split(/\s+/);
    var lines = [""];
    words.forEach(function (word) {
      var current = lines[lines.length - 1];
      if (current && (current + " " + word).length > perLine) lines.push(word);
      else lines[lines.length - 1] = current ? current + " " + word : word;
    });
    lines.slice(0, 3).forEach(function (line, index) {
      var text = svgEl("text", { x: 10, y: firstLineY + index * lineHeight });
      text.textContent = index === 2 && lines.length > 3 ? line.replace(/\s+\S*$/, "") + "…" : line;
      group.appendChild(text);
    });
    var title = svgEl("title", {});
    title.textContent = (item.shortLabel || item.statement) + " (" + item.kindLabel + ")";
    group.appendChild(title);
    return group;
  }

  function uniqueSourcesOf(finding) {
    var unique = [];
    var seen = {};
    (finding.sources || []).forEach(function (source) {
      if (seen[source.sourceId]) {
        if (source.locator) seen[source.sourceId].locators.push(source.locator);
        return;
      }
      var entry = { sourceId: source.sourceId, role: source.role, locators: source.locator ? [source.locator] : [] };
      seen[source.sourceId] = entry;
      unique.push(entry);
    });
    return unique;
  }

  /*
   * Shared ego-scene builder.
   * center: {type:"item", id, finding} or {type:"source", id}
   * opts:   {width, viewportH, onItem(id), onSource(sourceId)}
   * Returns {svg, inN, outN, srcN, citedByN}.
   */
  function buildScene(center, opts) {
    var isSource = center.type === "source";
    var incoming = [];
    var outgoing = [];
    var sources = [];
    if (isSource) {
      // Every citing item hangs to the right; the stored role reads
      // source → item, so the arrows and verbs read left → right.
      outgoing = usageList(center.id).map(function (entry) {
        return { toItem: entry.id, verb: roleVerb(entry.role), strength: "moderate" };
      });
    } else {
      var edges = state.edgesByItem[center.id] || [];
      incoming = edges.filter(function (e) { return e.to === center.id; });
      outgoing = edges.filter(function (e) { return e.from === center.id; });
      sources = uniqueSourcesOf(center.finding || {});
    }

    var W = Math.max(opts.width, 640);
    var rows = Math.max(incoming.length, outgoing.length, 1);
    var rowGap = 92;
    var nodeH = 74;
    var srcRowGap = nodeH + 50;
    var srcW = Math.min(190, W * 0.24);
    var srcPerRow = Math.max(1, Math.floor((W - 90) / (srcW + 26)));
    var srcRows = Math.ceil(sources.length / srcPerRow);
    var relationH = rows * rowGap + 90;
    var sourcesH = sources.length ? 120 + srcRows * srcRowGap : 0;
    var topHalf = relationH / 2;
    var bottomNeeded = Math.max(relationH / 2, 60 + sourcesH);
    var H = Math.max(opts.viewportH, topHalf + bottomNeeded);

    var svg = svgEl("svg", { viewBox: "0 0 " + W + " " + H, width: W, height: H, role: "img", "class": "g13x-scene" });
    markerSerial += 1;
    var markerId = "g13x-arrow-" + markerSerial;
    var defs = svgEl("defs", {});
    var marker = svgEl("marker", {
      id: markerId, viewBox: "0 0 8 8", refX: 7, refY: 4,
      markerWidth: 7, markerHeight: 7, orient: "auto-start-reverse",
    });
    marker.appendChild(svgEl("path", { d: "M0,0 L8,4 L0,8 z", fill: "#8b98ab" }));
    defs.appendChild(marker);
    svg.appendChild(defs);

    var nodeW = Math.min(190, W * 0.24);
    var centerW = Math.min(230, W * 0.3);
    var cx = W / 2;
    var cy = topHalf + Math.max(0, (H - topHalf - bottomNeeded) / 2);
    var leftX = 24 + nodeW / 2 + 30; // room for stubs on the outer side
    var rightX = W - 24 - nodeW / 2 - 30;

    function place(list, x) {
      return list.map(function (edge, index) {
        var y = cy + (index - (list.length - 1) / 2) * rowGap;
        return { edge: edge, x: x, y: y };
      });
    }

    function drawEdge(from, to, verb, strength, tooltip) {
      var mx = (from.x + to.x) / 2;
      var group = svgEl("g", {});
      group.appendChild(svgEl("path", {
        d: "M" + from.x + "," + from.y + " C" + mx + "," + from.y + " " + mx + "," + to.y + " " + to.x + "," + to.y,
        "class": "g13x-edge",
        "stroke-width": STRENGTH_WIDTH[strength] || 1,
        "marker-end": "url(#" + markerId + ")",
      }));
      // Bezier midpoint at t=0.5 with these controls: x=mx, y=(y0+y1)/2.
      var label = svgEl("text", {
        x: mx, y: (from.y + to.y) / 2 - 6, "text-anchor": "middle", "class": "g13x-edge-label",
      });
      label.textContent = verb;
      group.appendChild(label);
      var title = svgEl("title", {});
      title.textContent = tooltip;
      group.appendChild(title);
      svg.appendChild(group);
    }

    function drawStubs(x, y, direction, count, tooltip) {
      if (!count) return;
      var group = svgEl("g", {});
      var shown = Math.min(count, 3);
      for (var i = 0; i < shown; i += 1) {
        var angle = (i - (shown - 1) / 2) * 0.5;
        group.appendChild(svgEl("line", {
          x1: x, y1: y,
          x2: x + direction * 30 * Math.cos(angle), y2: y + 30 * Math.sin(angle),
          "class": "g13x-stub", "stroke-width": 1.4,
        }));
      }
      var text = svgEl("text", {
        x: x + direction * 36, y: y + 3,
        "text-anchor": direction > 0 ? "start" : "end", "class": "g13x-stub-label",
      });
      text.textContent = "+" + count;
      group.appendChild(text);
      var title = svgEl("title", {});
      title.textContent = tooltip;
      group.appendChild(title);
      svg.appendChild(group);
    }

    function clickable(group, action) {
      group.setAttribute("tabindex", 0);
      group.setAttribute("role", "button");
      group.addEventListener("click", action);
      group.addEventListener("keydown", function (event) {
        if (event.key === "Enter" || event.key === " ") { event.preventDefault(); action(); }
      });
    }

    // How many connections a related item has beyond the one drawn here.
    function otherConnectionCount(itemId) {
      var relations = (state.edgesByItem[itemId] || []).filter(function (e) {
        return isSource || (e.from !== center.id && e.to !== center.id);
      }).length;
      if (isSource) {
        var ownSources = (state.byId[itemId] || {}).sourceCount || 0;
        return relations + Math.max(0, ownSources - 1);
      }
      return relations;
    }

    var centerH = 88;
    var placedIn = place(incoming, leftX);
    var placedOut = place(outgoing, rightX);

    placedIn.forEach(function (p) {
      drawEdge({ x: p.x + nodeW / 2, y: p.y }, { x: cx - centerW / 2 - 4, y: cy },
        edgeVerb(p.edge.type), p.edge.strength,
        p.edge.from + " " + edgeVerb(p.edge.type) + " " + p.edge.to +
        (p.edge.explanation ? " — " + p.edge.explanation : ""));
    });
    placedOut.forEach(function (p) {
      var verb = isSource ? p.edge.verb : edgeVerb(p.edge.type);
      var tooltip = isSource
        ? sourceLabel(center.id) + " " + verb + " " + p.edge.toItem
        : p.edge.from + " " + verb + " " + p.edge.to + (p.edge.explanation ? " — " + p.edge.explanation : "");
      drawEdge({ x: cx + centerW / 2, y: cy }, { x: p.x - nodeW / 2 - 4, y: p.y },
        verb, p.edge.strength, tooltip);
    });

    function itemNode(p, otherId, direction) {
      var other = state.byId[otherId];
      if (!other) return;
      var group = svgEl("g", {});
      nodeBox(group, other, p.x, p.y, nodeW, nodeH, false);
      clickable(group, function () { opts.onItem(otherId); });
      svg.appendChild(group);
      drawStubs(p.x + direction * (nodeW / 2), p.y, direction, otherConnectionCount(otherId),
        (other.shortLabel || otherId) + " has " + otherConnectionCount(otherId) +
        " other connection(s) — click it to recenter");
    }

    placedIn.forEach(function (p) { itemNode(p, p.edge.from, -1); });
    placedOut.forEach(function (p) { itemNode(p, isSource ? p.edge.toItem : p.edge.to, 1); });

    // Cited sources hang below a centered item, connected by their role verb.
    sources.forEach(function (source, index) {
      var row = Math.floor(index / srcPerRow);
      var inRow = Math.min(sources.length - row * srcPerRow, srcPerRow);
      var col = index - row * srcPerRow;
      var sx = cx + (col - (inRow - 1) / 2) * (srcW + 26);
      var sy = cy + centerH / 2 + 110 + row * srcRowGap;
      var shortTitle = sourceLabel(source.sourceId);
      var resolved = state.sources[source.sourceId] || {};

      var endX = cx + ((index + 0.5) / sources.length - 0.5) * centerW * 0.7;
      var yTop = sy - nodeH / 2;
      var yBottom = cy + centerH / 2 + 3;
      var midY = (yTop + yBottom) / 2;
      var edgeGroup = svgEl("g", {});
      edgeGroup.appendChild(svgEl("path", {
        d: "M" + sx + "," + yTop + " C" + sx + "," + midY + " " + endX + "," + midY + " " + endX + "," + yBottom,
        "class": "g13x-edge", "stroke-width": 1.6, "marker-end": "url(#" + markerId + ")",
      }));
      var verb = svgEl("text", {
        x: (sx + endX) / 2, y: midY - 4, "text-anchor": "middle", "class": "g13x-edge-label",
      });
      verb.textContent = roleVerb(source.role);
      edgeGroup.appendChild(verb);
      svg.appendChild(edgeGroup);

      var node = svgEl("g", {});
      nodeBox(node, { kind: "source", kindLabel: "Source", shortLabel: shortTitle }, sx, sy, srcW, nodeH, false);
      node.querySelector("title").textContent = (resolved.citation || shortTitle) +
        (source.locators.length ? " — " + source.locators.join("; ") : "") +
        " (click to center this source)";
      clickable(node, function () { opts.onSource(source.sourceId); });
      svg.appendChild(node);

      // Off-page stubs: this source is also cited by N other research items.
      var usage = usageList(source.sourceId).length - 1;
      if (usage > 0) {
        var stubGroup = svgEl("g", {});
        var shown = Math.min(usage, 3);
        for (var s = 0; s < shown; s += 1) {
          var angle = (s - (shown - 1) / 2) * 0.5;
          stubGroup.appendChild(svgEl("line", {
            x1: sx, y1: sy + nodeH / 2,
            x2: sx + 30 * Math.sin(angle), y2: sy + nodeH / 2 + 30 * Math.cos(angle),
            "class": "g13x-stub", "stroke-width": 1.4,
          }));
        }
        var stubText = svgEl("text", {
          x: sx, y: sy + nodeH / 2 + 44, "text-anchor": "middle", "class": "g13x-stub-label",
        });
        stubText.textContent = "+" + usage;
        stubGroup.appendChild(stubText);
        var stubTitle = svgEl("title", {});
        stubTitle.textContent = shortTitle + " is also cited by " + usage + " other research item" + (usage === 1 ? "" : "s") +
          " — click it to center this source";
        stubGroup.appendChild(stubTitle);
        svg.appendChild(stubGroup);
      }
    });

    var centerNode = svgEl("g", {});
    var centerItem = isSource
      ? { kind: "source", kindLabel: "Source", shortLabel: sourceLabel(center.id) }
      : state.byId[center.id];
    nodeBox(centerNode, centerItem, cx, cy, centerW, centerH, true);
    svg.appendChild(centerNode);

    if (!incoming.length && !outgoing.length && !sources.length) {
      var lonely = svgEl("text", { x: cx, y: cy + centerH, "text-anchor": "middle", "class": "g13x-stub-label" });
      lonely.textContent = "No public relationships or sources recorded here.";
      svg.appendChild(lonely);
    }

    return { svg: svg, inN: incoming.length, outN: outgoing.length, srcN: sources.length };
  }

  // ============================ explorer app =============================
  function bootApp() {
    buildShell();
    renderList();
    renderGraph();
    renderDetail(null);
    applyHash();
  }

  // ------------------------------- shell ---------------------------------
  function buildShell() {
    var kinds = [];
    var seenKinds = {};
    state.items.forEach(function (it) {
      if (!seenKinds[it.kind]) { seenKinds[it.kind] = true; kinds.push({ kind: it.kind, label: it.kindLabel }); }
    });
    kinds.sort(function (a, b) { return a.label.localeCompare(b.label); });

    var confidences = CONFIDENCE_ORDER.filter(function (c) {
      return state.items.some(function (it) { return it.confidence === c; });
    });

    var units = [];
    var seenUnits = {};
    state.items.forEach(function (it) {
      if (it.unit && !seenUnits[it.unit.id]) { seenUnits[it.unit.id] = true; units.push(it.unit); }
    });
    units.sort(function (a, b) { return String(a.title).localeCompare(String(b.title)); });

    var options = function (entries, valueKey, labelKey, blank) {
      return '<option value="">' + esc(blank) + "</option>" + entries.map(function (entry) {
        return '<option value="' + esc(entry[valueKey]) + '">' + esc(entry[labelKey]) + "</option>";
      }).join("");
    };
    var yearOptions = '<option value="">Any year</option>' + yearBuckets().map(function (b) {
      return '<option value="' + b[0] + "-" + b[1] + '">' + b[0] + "–" + b[1] + "</option>";
    }).join("");

    root.innerHTML =
      '<header class="g13x-bar">' +
      '<h1 class="g13x-brand">John Gurney Context Graph <span class="tag">explorer</span></h1>' +
      '<div class="meta" id="g13x-bar-meta"></div>' +
      '<div class="links">' +
      '<a href="' + esc(root.getAttribute("data-hub-url") || "/") + '">‹ Research library</a>' +
      "</div>" +
      "</header>" +
      '<section id="g13x-left" aria-label="Research items">' +
      '<form class="g13x-filters" id="g13x-filters">' +
      '<div class="full"><label for="g13x-q">Search</label>' +
      '<input type="search" id="g13x-q" placeholder="Search titles and statements (e.g. Braintree)" /></div>' +
      '<div><label for="g13x-kind">Kind</label><select id="g13x-kind">' + options(kinds, "kind", "label", "Any kind") + "</select></div>" +
      '<div><label for="g13x-confidence">Confidence</label><select id="g13x-confidence">' +
      options(confidences.map(function (c) { return { v: c, l: c.charAt(0).toUpperCase() + c.slice(1) }; }), "v", "l", "Any confidence") +
      "</select></div>" +
      '<div><label for="g13x-unit">Topic file</label><select id="g13x-unit">' + options(units, "id", "title", "Any topic file") + "</select></div>" +
      '<div><label for="g13x-year">Year</label><select id="g13x-year">' + yearOptions + "</select></div>" +
      "</form>" +
      '<div class="g13x-meta" id="g13x-list-meta"></div>' +
      '<div class="g13x-hint"><kbd>/</kbd> search · <kbd>↑</kbd><kbd>↓</kbd> move · <kbd>Enter</kbd> open</div>' +
      '<ul class="g13x-itemlist" id="g13x-list" role="listbox" aria-label="Research items"></ul>' +
      "</section>" +
      '<section id="g13x-graph" aria-label="Relationship map"></section>' +
      '<section id="g13x-detail" class="empty" aria-label="Item detail" aria-live="polite"></section>';

    el.barMeta = document.getElementById("g13x-bar-meta");
    el.listMeta = document.getElementById("g13x-list-meta");
    el.list = document.getElementById("g13x-list");
    el.graph = document.getElementById("g13x-graph");
    el.detail = document.getElementById("g13x-detail");
    el.q = document.getElementById("g13x-q");

    el.barMeta.textContent = state.items.length + " research items · " + state.edges.length +
      " relationships · Context Graph revision " + state.revision;

    document.getElementById("g13x-filters").addEventListener("submit", function (event) { event.preventDefault(); });
    el.q.addEventListener("input", function () { state.filters.q = el.q.value; refresh(); });
    [["g13x-kind", "kind"], ["g13x-confidence", "confidence"], ["g13x-unit", "unit"], ["g13x-year", "year"]]
      .forEach(function (pair) {
        var select = document.getElementById(pair[0]);
        select.addEventListener("change", function () { state.filters[pair[1]] = select.value; refresh(); });
      });

    document.addEventListener("keydown", function (event) {
      if (event.key === "/" && !/^(INPUT|SELECT|TEXTAREA)$/.test(document.activeElement.tagName)) {
        event.preventDefault();
        el.q.focus();
        el.q.select();
      }
    });
    el.list.addEventListener("keydown", function (event) {
      if (event.key !== "ArrowDown" && event.key !== "ArrowUp") return;
      var rows = Array.prototype.slice.call(el.list.querySelectorAll("li[data-id]"));
      var index = rows.indexOf(document.activeElement);
      var next = rows[index + (event.key === "ArrowDown" ? 1 : -1)];
      if (next) { event.preventDefault(); next.focus(); }
    });

    // Pivot links inside the detail pane recenter the explorer.
    el.detail.addEventListener("click", function (event) {
      var link = event.target.closest ? event.target.closest("a[data-g13-finding]") : null;
      if (!link) return;
      if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      selectItem(link.getAttribute("data-g13-finding"));
    });

    updateTopOffset();
    window.addEventListener("resize", debounce(function () { updateTopOffset(); renderGraph(); }, 150));
    window.addEventListener("hashchange", applyHash);
  }

  // The site header is sticky; the app fills the viewport below it.
  function updateTopOffset() {
    var header = document.querySelector(".site-header");
    var offset = 0;
    if (header) {
      var rect = header.getBoundingClientRect();
      if (rect.bottom > 0) offset = Math.max(0, Math.round(rect.bottom));
    }
    document.documentElement.style.setProperty("--g13x-top", offset + "px");
  }

  function debounce(fn, wait) {
    var timer = null;
    return function () {
      if (timer) clearTimeout(timer);
      timer = setTimeout(fn, wait);
    };
  }

  // ------------------------------ Area 1 list ----------------------------
  function selectedItemId() {
    return state.selected && state.selected.type === "item" ? state.selected.id : null;
  }

  function renderList() {
    var items = filteredItems();
    var selectedId = selectedItemId();
    el.listMeta.textContent = items.length + " of " + state.items.length + " items";
    if (!items.length) {
      el.list.innerHTML = '<li class="emptylist">No items match the current filters.</li>';
      return;
    }
    el.list.innerHTML = items.map(function (it) {
      var degree = (state.edgesByItem[it.id] || []).length;
      var chips = '<span class="g13x-kind ' + kindClass(it.kind) + '">' + esc(it.kindLabel) + "</span>";
      if (it.status && it.status !== "active") chips += '<span class="g13x-chip st-' + esc(it.status) + '">' + esc(it.status) + "</span>";
      return (
        '<li data-id="' + esc(it.id) + '" class="' + kindClass(it.kind) + (it.id === selectedId ? " selected" : "") +
        '" tabindex="0" role="option" aria-selected="' + (it.id === selectedId ? "true" : "false") + '">' +
        '<div class="row1">' + chips +
        '<span class="counts" title="sources · relationships">' + (it.sourceCount || 0) + "s · " + degree + "r</span></div>" +
        '<div class="stmt">' + esc(truncate(it.shortLabel || it.statement, 160)) + "</div>" +
        "</li>"
      );
    }).join("");
    Array.prototype.forEach.call(el.list.querySelectorAll("li[data-id]"), function (li) {
      var open = function () { selectItem(li.getAttribute("data-id")); };
      li.addEventListener("click", open);
      li.addEventListener("keydown", function (event) {
        if (event.key === "Enter" || event.key === " ") { event.preventDefault(); open(); }
      });
    });
  }

  // --------------------------- selection & hash --------------------------
  function selectItem(id) {
    if (!state.byId[id]) return;
    state.selected = { type: "item", id: id };
    state.preview = null;
    if (window.location.hash !== "#item/" + id) {
      try { window.history.replaceState(null, "", "#item/" + id); } catch (error) { /* ignore */ }
    }
    renderList();
    var row = el.list.querySelector('li[data-id="' + id + '"]');
    if (row && row.scrollIntoView) row.scrollIntoView({ block: "nearest" });
    renderGraph();
    renderDetail(id);
  }

  function selectSource(sourceId) {
    if (!state.sources[sourceId] && !usageList(sourceId).length) return;
    state.selected = { type: "source", id: sourceId };
    state.preview = null;
    if (window.location.hash !== "#source/" + sourceId) {
      try { window.history.replaceState(null, "", "#source/" + sourceId); } catch (error) { /* ignore */ }
    }
    renderList();
    renderGraph();
    renderSourceDetail(sourceId);
  }

  function previewItem(id) {
    state.preview = id;
    renderGraph();
    renderDetail(id);
  }

  function clearSelection() {
    state.selected = null;
    state.preview = null;
    try { window.history.replaceState(null, "", window.location.pathname + window.location.search); } catch (error) { /* ignore */ }
    renderList();
    renderGraph();
    renderDetail(null);
  }

  function applyHash() {
    var itemMatch = window.location.hash.match(/^#item\/(G13-RI-\d{6})$/i);
    if (itemMatch) {
      var id = itemMatch[1].toUpperCase();
      if (state.byId[id] && selectedItemId() !== id) selectItem(id);
      return;
    }
    var sourceMatch = window.location.hash.match(/^#source\/([a-z0-9-]+)$/i);
    if (sourceMatch) {
      var sourceId = sourceMatch[1].toLowerCase();
      var current = state.selected && state.selected.type === "source" ? state.selected.id : null;
      if (current !== sourceId) selectSource(sourceId);
    }
  }

  function refresh() {
    renderList();
    // A selection that fell out of the filtered set stays selected (the map
    // and text keep working); the overview map always follows the filters.
    renderGraph();
  }

  // ------------------------------ ego view -------------------------------
  function sceneOpts() {
    var rect = el.graph.getBoundingClientRect();
    return {
      width: rect.width,
      viewportH: rect.height - 2,
      onItem: selectItem,
      onSource: selectSource,
    };
  }

  function egoOverlay(text) {
    var overlay = document.createElement("div");
    overlay.className = "g13x-overlay";
    overlay.innerHTML = '<button type="button" class="g13x-back">‹ Back to map</button><span>' + text + "</span>";
    overlay.querySelector(".g13x-back").addEventListener("click", clearSelection);
    return overlay;
  }

  function renderEgo(sel) {
    if (sel.type === "source") {
      var scene = buildScene({ type: "source", id: sel.id }, sceneOpts());
      el.graph.innerHTML = "";
      el.graph.appendChild(egoOverlay("cited by " + scene.outN + " research item" + (scene.outN === 1 ? "" : "s") +
        " — click any item to recenter"));
      el.graph.appendChild(scene.svg);
      return;
    }
    // The center item's cited sources come from its detail JSON (shared
    // promise cache with Area 3, so no extra request after the first).
    fetchJson("findings/" + sel.id + ".json").catch(function () { return {}; }).then(function (finding) {
      if (selectedItemId() !== sel.id) return; // stale after a rapid recenter
      var scene = buildScene({ type: "item", id: sel.id, finding: finding || {} }, sceneOpts());
      el.graph.innerHTML = "";
      el.graph.appendChild(egoOverlay(scene.inN + " in · " + scene.outN + " out · " + scene.srcN +
        " source" + (scene.srcN === 1 ? "" : "s") + " — click any connected item to recenter"));
      el.graph.appendChild(scene.svg);
    });
  }

  // ----------------------------- overview map ----------------------------
  function renderOverview() {
    var items = filteredItems();
    var rect = el.graph.getBoundingClientRect();
    var W = Math.max(rect.width, 640);
    var H = Math.max(rect.height - 2, 360);

    el.graph.innerHTML = "";
    var overlay = document.createElement("div");
    overlay.className = "g13x-overlay";
    var legendKinds = [];
    var seen = {};
    items.forEach(function (it) {
      if (!seen[it.kind]) { seen[it.kind] = true; legendKinds.push(it); }
    });
    overlay.innerHTML =
      "<span>" + items.length + " item" + (items.length === 1 ? "" : "s") +
      " — click a dot to preview, click again to focus</span>" +
      '<span class="g13x-legend">' + legendKinds.map(function (it) {
        return '<span class="g13-kind ' + render.kindClass(it.kind) + '">' + esc(it.kindLabel) + "</span>";
      }).join("") + "</span>";
    el.graph.appendChild(overlay);

    if (!items.length) return;

    var inSet = {};
    items.forEach(function (it) { inSet[it.id] = true; });
    var edges = state.edges.filter(function (e) { return inSet[e.from] && inSet[e.to]; });

    // Deterministic force layout: circle seed, repulsion + springs + gravity.
    var nodes = items.map(function (it, index) {
      var angle = (2 * Math.PI * index) / items.length;
      return {
        item: it,
        x: W / 2 + Math.cos(angle) * W * 0.33,
        y: H / 2 + Math.sin(angle) * H * 0.33,
      };
    });
    var indexById = {};
    nodes.forEach(function (node, index) { indexById[node.item.id] = index; });
    var iterations = nodes.length > 130 ? 130 : 220;
    var pad = 30;
    for (var k = 0; k < iterations; k += 1) {
      var cool = 1 - k / iterations;
      var i;
      var j;
      for (i = 0; i < nodes.length; i += 1) {
        for (j = i + 1; j < nodes.length; j += 1) {
          var dx = nodes[i].x - nodes[j].x;
          var dy = nodes[i].y - nodes[j].y;
          var d2 = dx * dx + dy * dy + 0.01;
          if (d2 > 40000) continue;
          var force = Math.min(1400 / d2, 6) * cool;
          var d = Math.sqrt(d2);
          dx = (dx / d) * force;
          dy = (dy / d) * force;
          nodes[i].x += dx; nodes[i].y += dy;
          nodes[j].x -= dx; nodes[j].y -= dy;
        }
      }
      edges.forEach(function (edge) {
        var a = nodes[indexById[edge.from]];
        var b = nodes[indexById[edge.to]];
        var ex = b.x - a.x;
        var ey = b.y - a.y;
        var dist = Math.sqrt(ex * ex + ey * ey) + 0.01;
        var pull = (dist - 80) * 0.02 * cool;
        ex = (ex / dist) * pull;
        ey = (ey / dist) * pull;
        a.x += ex; a.y += ey;
        b.x -= ex; b.y -= ey;
      });
      for (i = 0; i < nodes.length; i += 1) {
        nodes[i].x += (W / 2 - nodes[i].x) * 0.012 * cool;
        nodes[i].y += (H / 2 - nodes[i].y) * 0.012 * cool;
        nodes[i].x = Math.max(pad, Math.min(W - pad, nodes[i].x));
        nodes[i].y = Math.max(pad, Math.min(H - pad, nodes[i].y));
      }
    }

    var svg = svgEl("svg", {
      viewBox: "0 0 " + W + " " + H, width: W, height: H, role: "img",
      "class": "g13x-scene" + (nodes.length > 90 ? " g13x-dense" : ""),
    });
    edges.forEach(function (edge) {
      var a = nodes[indexById[edge.from]];
      var b = nodes[indexById[edge.to]];
      var line = svgEl("line", {
        x1: a.x, y1: a.y, x2: b.x, y2: b.y,
        "class": "g13x-ov-edge",
        "stroke-width": (STRENGTH_WIDTH[edge.strength] || 1) * 0.6,
      });
      var title = svgEl("title", {});
      title.textContent = (a.item.shortLabel || edge.from) + " — " + edgeVerb(edge.type) + " → " +
        (b.item.shortLabel || edge.to);
      line.appendChild(title);
      svg.appendChild(line);
    });
    var kindVar = function (kind) { return "var(--k-" + String(kind).replace(/[^a-z_]/gi, "") + ", #8fa3b8)"; };
    nodes.forEach(function (node) {
      var it = node.item;
      var degree = (state.edgesByItem[it.id] || []).length;
      var group = svgEl("g", {
        "class": "g13x-ov-node" + (state.preview === it.id ? " preview" : ""),
        tabindex: 0, role: "button",
      });
      var circle = svgEl("circle", {
        cx: node.x, cy: node.y, r: 5 + Math.min(5, degree * 0.7), fill: kindVar(it.kind),
      });
      group.appendChild(circle);
      var text = svgEl("text", { x: node.x, y: node.y + 18, "text-anchor": "middle" });
      text.textContent = truncate(it.shortLabel || it.statement, 26);
      group.appendChild(text);
      var title = svgEl("title", {});
      title.textContent = (it.shortLabel || it.statement) + " (" + it.kindLabel + ", " + degree + " links)";
      group.appendChild(title);
      var open = function () {
        if (state.preview === it.id) selectItem(it.id);
        else previewItem(it.id);
      };
      group.addEventListener("click", open);
      group.addEventListener("dblclick", function () { selectItem(it.id); });
      group.addEventListener("keydown", function (event) {
        if (event.key === "Enter" || event.key === " ") { event.preventDefault(); open(); }
      });
      svg.appendChild(group);
    });
    el.graph.appendChild(svg);
  }

  function renderGraph() {
    if (state.selected) renderEgo(state.selected);
    else renderOverview();
  }

  // ------------------------------ Area 3 text ----------------------------
  function renderDetail(id) {
    if (!id) {
      el.detail.className = "empty";
      el.detail.innerHTML =
        "<p>Select a research item from the list, or click a dot on the map, to read its full treatment here — " +
        "statement, dates, sources with excerpts, and how it connects to the rest of the research.</p>";
      return;
    }
    fetchJson("findings/" + id + ".json").then(function (finding) {
      el.detail.className = "";
      el.detail.innerHTML =
        render.renderFinding(finding, ctx(), { compact: false, headingTag: "h2", revision: state.revision }) +
        '<p class="g13x-permalink"><a href="' + esc(render.findingUrl(id)) + '">Open this item’s permanent page</a></p>';
      el.detail.scrollTop = 0;
    }).catch(function () {
      el.detail.className = "empty";
      el.detail.innerHTML = '<p>Could not load this item. <a href="' + esc(render.findingUrl(id)) +
        '">Open its permanent page instead.</a></p>';
    });
  }

  function renderSourceDetail(sourceId) {
    var resolved = state.sources[sourceId] || {};
    var citing = usageList(sourceId);
    var html =
      '<div class="g13-finding">' +
      '<p class="g13-chip-row"><span class="g13-kind kind-source">Source</span></p>' +
      '<h2 class="g13-heading">' + esc(sourceLabel(sourceId)) + "</h2>";
    if (resolved.citation && resolved.citation !== sourceLabel(sourceId)) {
      html += '<p class="g13-statement">' + esc(resolved.citation) + "</p>";
    }
    if (resolved.url) {
      html += '<section class="g13-section"><h3>Source links</h3><ul class="g13-list">' +
        '<li><a href="' + esc(resolved.url) + '" rel="noopener" target="_blank">' + esc(resolved.url) + "</a></li>" +
        "</ul></section>";
    }
    if (citing.length) {
      html += '<section class="g13-section"><h3>Cited by</h3><ul class="g13-list">' +
        citing.map(function (entry) {
          var item = state.byId[entry.id];
          return '<li class="g13-relation">' +
            '<span class="g13-relation-label">' + esc(roleVerb(entry.role)) + "</span> " +
            '<span class="g13-kind ' + esc(render.kindClass(item.kind)) + '">' + esc(item.kindLabel) + "</span> " +
            '<a class="g13-item-link" data-g13-finding="' + esc(item.id) + '" href="' +
            esc(render.findingUrl(item.id)) + '">' + esc(item.shortLabel || item.statement) + "</a></li>";
        }).join("") + "</ul></section>";
    }
    html += '<details class="g13-technical"><summary>Technical details</summary><ul>' +
      "<li>Source ID: <code>" + esc(sourceId) + "</code></li>" +
      "<li>Context Graph revision: <code>" + esc(state.revision) + "</code></li>" +
      "</ul></details></div>";
    el.detail.className = "";
    el.detail.innerHTML = html;
    el.detail.scrollTop = 0;
  }

  // ============================= page embed ===============================
  // Permanent finding pages carry <div id="g13x-embed" data-item="…"
  // data-explorer-url="…">: draw the same ego scene; item clicks navigate to
  // that item's permanent page, source clicks open the explorer on the source.
  function bootEmbed() {
    var itemId = String(embedRoot.getAttribute("data-item") || "").toUpperCase();
    var explorerUrl = embedRoot.getAttribute("data-explorer-url") || "";
    var section = embedRoot.closest ? embedRoot.closest("section") : null;
    var fail = function () { if (section) section.hidden = true; else embedRoot.hidden = true; };
    if (!itemId) { fail(); return; }
    fetchJson("findings/" + itemId + ".json").then(function (finding) {
      if (!state.byId[itemId]) { fail(); return; }
      var width = Math.max(embedRoot.getBoundingClientRect().width, 640);
      var scene = buildScene({ type: "item", id: itemId, finding: finding }, {
        width: width,
        viewportH: 300,
        onItem: function (otherId) { window.location.href = render.findingUrl(otherId); },
        onSource: function (sourceId) {
          if (explorerUrl) window.location.href = explorerUrl + "#source/" + sourceId;
        },
      });
      embedRoot.innerHTML = "";
      embedRoot.appendChild(scene.svg);
      var caption = document.createElement("p");
      caption.className = "g13x-embed-caption";
      caption.innerHTML = scene.inN + " in · " + scene.outN + " out · " + scene.srcN +
        " source" + (scene.srcN === 1 ? "" : "s") + " — click a box to follow it" +
        (explorerUrl
          ? ' · <a href="' + esc(explorerUrl) + "#item/" + esc(itemId) + '">Open in the Context Graph Explorer</a>'
          : "");
      embedRoot.appendChild(caption);
    }).catch(fail);
  }

  // -------------------------------- boot ---------------------------------
  loadCore().then(function () {
    if (root) bootApp();
    else bootEmbed();
  }).catch(function (error) {
    if (root) {
      root.innerHTML = '<p style="padding:2rem;color:#97a1b0">The Context Graph explorer could not load its data (' +
        esc(error.message) + "). The <a href=\"" + esc(root.getAttribute("data-hub-url") || "/") +
        '">research library</a> lists every topic and finding as ordinary pages.</p>';
    } else if (embedRoot) {
      var section = embedRoot.closest ? embedRoot.closest("section") : null;
      if (section) section.hidden = true; else embedRoot.hidden = true;
    }
  });
})();
