"use strict";

// ------------------------------------------------------------------ helpers
const state = {
  status: null,
  picklists: {},
  units: [],
  selectedId: null,
  filters: {},
  tab: "items",
  queueSelection: new Set(),
};

async function api(path, options) {
  const res = await fetch(path, options);
  let data = null;
  try { data = await res.json(); } catch (_) { data = null; }
  if (!res.ok) {
    const err = new Error((data && (data.error || JSON.stringify(data))) || res.statusText);
    err.status = res.status;
    err.data = data;
    throw err;
  }
  return data;
}
async function apiGet(path) { return api(path); }
async function apiPost(path, body) {
  return api(path, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body || {}),
  });
}

function el(tag, attrs, children) {
  const node = document.createElement(tag);
  if (attrs) for (const [k, v] of Object.entries(attrs)) {
    if (k === "class") node.className = v;
    else if (k === "html") node.innerHTML = v;
    else if (k === "text") node.textContent = v;
    else if (k.startsWith("on") && typeof v === "function") node.addEventListener(k.slice(2), v);
    else if (v !== null && v !== undefined) node.setAttribute(k, v);
  }
  if (children) for (const c of [].concat(children)) {
    if (c === null || c === undefined) continue;
    node.appendChild(typeof c === "string" ? document.createTextNode(c) : c);
  }
  return node;
}
const $ = (sel) => document.querySelector(sel);
function short(s, n = 140) { s = s || ""; return s.length > n ? s.slice(0, n) + "…" : s; }

function banner(msg, kind) {
  const b = $("#banner");
  b.className = "banner " + (kind || "ok");
  b.textContent = msg;
  b.classList.remove("hidden");
  if (kind !== "err") setTimeout(() => b.classList.add("hidden"), 4000);
}

function pick(name, current, opts) {
  const s = el("select", { "aria-label": name }, [el("option", { value: "" }, "—")]);
  for (const v of (opts || state.picklists[name] || [])) {
    const o = el("option", { value: v }, v);
    if (v === current) o.selected = true;
    s.appendChild(o);
  }
  return s;
}

// presentation-only class helpers (values come from fixed picklists)
function kindClass(kind) { return "kind-" + String(kind || "").replace(/[^a-z_]/g, ""); }
function relTypeClass(t) {
  if (["SUPPORTS", "PUBLISHED_AS"].includes(t)) return "pos";
  if (["CONTRADICTS", "ELIMINATES", "DISTINCT_FROM"].includes(t)) return "neg";
  if (["QUALIFIES", "REQUIRES_REVIEW_OF", "SUPERSEDES"].includes(t)) return "mid";
  return "neutral";
}
function roleClass(role) {
  if (role === "supports") return "pos";
  if (role === "contradicts") return "neg";
  if (["qualifies", "negative_within_scope"].includes(role)) return "mid";
  return "";
}

async function copyText(text, label) {
  try {
    await navigator.clipboard.writeText(text);
    banner((label || "Copied") + " to clipboard.", "ok");
  } catch (_) {
    banner("Clipboard unavailable — select and copy manually.", "warn");
  }
}

// arrow-key navigation within an item list; Enter/Space opens the focused row
function listKeydown(e) {
  const li = e.target.closest("li");
  if (!li) return;
  if (e.key === "ArrowDown" || e.key === "ArrowUp") {
    e.preventDefault();
    const next = e.key === "ArrowDown" ? li.nextElementSibling : li.previousElementSibling;
    if (next) next.focus();
  } else if (e.key === "Enter" || e.key === " ") {
    if (e.target.tagName === "INPUT") return; // let checkboxes toggle natively
    e.preventDefault();
    li.click();
  }
}

// ------------------------------------------------------------------ status
function renderStatus() {
  const s = state.status;
  const box = $("#status-metrics");
  box.innerHTML = "";
  if (!s) return;
  const add = (label, value, cls) =>
    box.appendChild(el("span", { class: "m " + (cls || "") }, [label + " ", el("b", {}, String(value))]));
  add("rev", s.database_revision);
  add("recovery r", s.recovery_export_revision ?? "—",
    s.database_ahead_of_recovery ? "bad" : "good");
  add("snapshot r", s.latest_snapshot_revision ?? "—",
    s.database_ahead_of_snapshot ? "warn" : "good");
  add("errors", s.validation_errors, s.validation_errors ? "bad" : "good");
  add("warnings", s.validation_warnings, s.validation_warnings ? "warn" : "");
  add("indexes", s.derived_index_state, s.derived_index_state === "current" ? "good" : "warn");

  const notes = [];
  if (s.database_ahead_of_recovery) notes.push("DB is AHEAD of the recovery export — unsafe-backup state; refresh the export.");
  if (s.database_ahead_of_snapshot) notes.push("DB is ahead of the latest milestone snapshot — consider a snapshot.");
  if (s.source_registry_state && s.source_registry_state !== "current") notes.push("source_registry is " + s.source_registry_state + ".");
  // don't clobber a fresh success/error banner; the metrics chips carry the
  // same state, so the note banner only fills an otherwise-empty slot
  const b = $("#banner");
  if (notes.length && (b.classList.contains("hidden") || b.className.indexOf("warn") !== -1)) {
    b.className = "banner warn"; b.textContent = notes.join("  •  "); b.classList.remove("hidden");
  }
}

async function refreshStatus() {
  state.status = await apiGet("/api/status");
  renderStatus();
}

// ------------------------------------------------------------------ filters + item list
const FILTER_FIELDS = [
  ["kind", "item_kind"],
  ["status", "status"],
  ["confidence", "confidence_label"],
  ["visibility", "visibility"],
  ["review_state", "review_state"],
];
function renderFilters() {
  const form = $("#filters");
  form.innerHTML = "";
  form.appendChild(el("input", {
    class: "full", type: "text", placeholder: "text / id filter…  ( / )",
    "aria-label": "Text or id filter", value: state.filters.q || "",
    oninput: (e) => { state.filters.q = e.target.value; debouncedLoad(); },
  }));
  for (const [key, plist] of FILTER_FIELDS) {
    const wrap = el("div", {}, [el("label", {}, key)]);
    const sel = pick(plist, state.filters[key]);
    sel.addEventListener("change", (e) => { state.filters[key] = e.target.value; loadItems(); });
    wrap.appendChild(sel);
    form.appendChild(wrap);
  }
  const unitWrap = el("div", {}, [el("label", {}, "unit")]);
  const unitSel = el("select", {}, [el("option", { value: "" }, "—")]);
  for (const u of state.units) {
    const o = el("option", { value: u.unit_id }, u.title || u.unit_id);
    if (u.unit_id === state.filters.unit) o.selected = true;
    unitSel.appendChild(o);
  }
  unitSel.addEventListener("change", (e) => { state.filters.unit = e.target.value; loadItems(); });
  unitWrap.appendChild(unitSel);
  form.appendChild(unitWrap);

  const checks = [
    ["conflict", "unresolved conflict"],
    ["pub_impact", "publication impact"],
    ["needs_pub_decision", "needs pub decision"],
  ];
  for (const [key, label] of checks) {
    const c = el("label", { class: "check full" }, [
      el("input", {
        type: "checkbox", checked: state.filters[key] ? "checked" : null,
        onchange: (e) => { state.filters[key] = e.target.checked ? "1" : ""; loadItems(); },
      }),
      label,
    ]);
    form.appendChild(c);
  }
}

let loadTimer = null;
function debouncedLoad() { clearTimeout(loadTimer); loadTimer = setTimeout(loadItems, 250); }

function queryString(obj) {
  const parts = [];
  for (const [k, v] of Object.entries(obj)) if (v) parts.push(encodeURIComponent(k) + "=" + encodeURIComponent(v));
  return parts.length ? "?" + parts.join("&") : "";
}

function itemLi(it, onClick) {
  const selected = it.item_id === state.selectedId;
  const li = el("li", {
    class: (selected ? "selected " : "") + kindClass(it.item_kind),
    tabindex: "0", role: "option", "aria-selected": selected ? "true" : "false",
  }, [
    el("div", { class: "row1" }, [
      el("span", { class: "kind " + kindClass(it.item_kind) }, it.item_kind),
      el("span", { class: "id" }, it.item_id),
      el("span", { class: "chip vis-" + it.visibility }, it.visibility),
      it.status && it.status !== "active" ? el("span", { class: "chip st-" + it.status }, it.status) : null,
      it.review_state === "machine_suggested" ? el("span", { class: "chip rev-machine_suggested" }, "machine") : null,
      el("span", { class: "counts", title: "sources · relations · publications" },
        `${it.source_count ?? 0}s · ${it.relation_count ?? 0}r · ${it.publication_count ?? 0}p`),
    ]),
    el("div", { class: "stmt" }, short(it.short_label || it.statement)),
  ]);
  li.dataset.id = it.item_id;
  li.addEventListener("click", () => onClick(it.item_id));
  return li;
}

async function loadItems() {
  let data;
  try { data = await apiGet("/api/items" + queryString(state.filters)); }
  catch (e) { banner("Loading items failed: " + e.message, "err"); return; }
  $("#items-meta").textContent = `${data.count} of ${data.total_items} items`;
  const list = $("#item-list");
  list.innerHTML = "";
  for (const it of data.items) list.appendChild(itemLi(it, selectItem));
  if (!data.items.length) list.appendChild(el("li", { class: "emptylist" }, "No items match the current filters."));
}

// ------------------------------------------------------------------ detail
async function selectItem(id) {
  state.selectedId = id;
  document.querySelectorAll("#item-list li, #queue-list li, #search-list li")
    .forEach((li) => { li.classList.remove("selected"); li.setAttribute("aria-selected", "false"); });
  let detail;
  try { detail = await apiGet("/api/item/" + encodeURIComponent(id)); }
  catch (e) { banner("Loading " + id + " failed: " + e.message, "err"); return; }
  renderDetail(detail);
  // deep-linkable selection (also lets an AI session see what is on screen)
  if (location.hash !== "#item/" + id) history.replaceState(null, "", "#item/" + id);
  // reflect selection in visible lists
  document.querySelectorAll(".itemlist li").forEach((li) => {
    if (li.dataset && li.dataset.id === id) { li.classList.add("selected"); li.setAttribute("aria-selected", "true"); }
  });
  $("#right").scrollTop = 0;
}

function card(title, extraHeader, body) {
  const h = el("h4", {}, [title]);
  if (extraHeader) { h.appendChild(el("span", { class: "spacer" })); [].concat(extraHeader).forEach((x) => h.appendChild(x)); }
  return el("section", { class: "card" }, [h, ...[].concat(body)]);
}
function kv(pairs) {
  const g = el("div", { class: "kv" });
  for (const [k, v] of pairs) {
    g.appendChild(el("div", { class: "k" }, k));
    g.appendChild(v instanceof Node ? v : el("div", {}, String(v ?? "—")));
  }
  return g;
}

function renderDetail(it) {
  state.currentDetail = it;
  const root = $("#detail");
  root.className = "detail";
  root.innerHTML = "";

  root.appendChild(el("div", { class: "detail-head" }, [
    el("h2", {}, it.short_label || short(it.statement, 90)),
    el("div", { class: "headactions" }, [
      el("button", { class: "small", title: "Copy the item id", onclick: () => copyText(it.item_id, it.item_id) }, "Copy id"),
      el("button", { class: "small", title: "Copy a self-contained context block for an AI session", onclick: () => copyText(buildAIContext(it), "AI context for " + it.item_id) }, "Copy AI context"),
      el("button", { class: "small", title: "Revert this item to its previous audited state", onclick: () => undoItem(it.item_id) }, "Undo last"),
      el("button", { class: "small danger", title: "Soft-delete: mark rejected, kept in the audit trail", onclick: () => retireItem(it.item_id) }, "Retire"),
    ]),
  ]));
  root.appendChild(el("div", { class: "headchips" }, [
    el("span", { class: "kind " + kindClass(it.item_kind) }, it.item_kind),
    el("span", { class: "id" }, it.item_id),
    el("span", { class: "chip vis-" + it.visibility }, it.visibility),
    it.status && it.status !== "active" ? el("span", { class: "chip st-" + it.status }, it.status) : el("span", { class: "chip" }, it.status || "—"),
    el("span", { class: "chip", title: "assessment confidence" }, it.assessment_confidence_label || "no confidence"),
    el("span", { class: "chip" + (it.review_state === "machine_suggested" ? " rev-machine_suggested" : ""), title: "review state" }, it.review_state),
  ]));

  // publication readiness advisory
  const pr = it.publication_readiness || {};
  if ((pr.export_blockers || []).length || pr.excerpt_decisions_pending) {
    root.appendChild(el("div", { class: "advisory" },
      "Publication decisions pending before static export: " +
      ((pr.export_blockers || []).join(" ") || `${pr.excerpt_decisions_pending} excerpt decision(s).`)));
  }

  // core editable fields
  root.appendChild(renderEditCard(it));

  // sources
  root.appendChild(renderSourcesCard(it));
  // relations
  root.appendChild(renderRelationsCard(it));
  // entities
  root.appendChild(renderEntitiesCard(it));
  // dates
  if ((it.dates || []).length) root.appendChild(renderDatesCard(it));
  // negative scope
  if (it.item_kind === "negative_result" || it.negative_result_scope)
    root.appendChild(renderNegativeCard(it));
  // publications / impact
  root.appendChild(renderPublicationsCard(it));
  // duplicates
  if ((it.duplicate_candidates || []).length) root.appendChild(renderDuplicatesCard(it));
  // revisions
  root.appendChild(renderRevisionsCard(it));
}

function renderEditCard(it) {
  const fields = {};
  const grid = el("div", { class: "formgrid" });
  const addRow = (label, node, key) => {
    grid.appendChild(el("div", { class: "label" }, label));
    grid.appendChild(node);
    if (key) fields[key] = node;
  };
  const statement = el("textarea", { rows: "3" }); statement.value = it.statement || "";
  addRow("statement", statement, "statement");
  const shortLabel = el("input", { type: "text", value: it.short_label || "" }); addRow("short label", shortLabel, "short_label");
  const summary = el("textarea", { rows: "2" }); summary.value = it.summary || ""; addRow("summary", summary, "summary");

  const kindSel = pick("item_kind", it.item_kind); addRow("kind", kindSel, "item_kind");
  const statusSel = pick("status", it.status); addRow("status", statusSel, "status");
  const confSel = pick("confidence_label", it.assessment_confidence_label); addRow("confidence", confSel, "assessment_confidence_label");
  const visSel = pick("visibility", it.visibility); addRow("visibility", visSel, "visibility");
  const reviewSel = pick("review_state", it.review_state); addRow("review state", reviewSel, "review_state");

  const excerptCb = el("input", { type: "checkbox", checked: it.excerpt_publishable ? "checked" : null });
  addRow("excerpt publishable", el("div", { class: "check" }, [excerptCb]));
  const restr = el("input", { type: "text", value: it.restriction_reason || "" }); addRow("restriction reason", restr, "restriction_reason");
  const notes = el("textarea", { rows: "2" }); notes.value = it.notes || ""; addRow("notes", notes, "notes");

  // research location + subject (read-only display + navigation)
  const locNode = it.research_path
    ? el("span", { class: "mono" }, `${it.research_path}${it.research_heading ? " #" + it.research_heading : ""}`)
    : el("span", { class: "muted" }, "—");
  addRow("research location", locNode);
  const subjNode = it.subject_entity
    ? el("a", { class: "link", onclick: () => openNeighborhood("entity", it.subject_entity_id) }, it.subject_entity.canonical_label)
    : el("span", { class: "muted" }, it.subject_entity_id || "—");
  addRow("subject entity", subjNode);
  addRow("provenance", el("span", { class: "muted" }, it.provenance_origin));

  const save = el("button", { class: "ok" }, "Preview & save");
  save.addEventListener("click", () => {
    const changes = {};
    const setIf = (key, val) => { if (val !== (it[key] ?? "")) changes[key] = val; };
    setIf("statement", statement.value.trim());
    setIf("short_label", shortLabel.value.trim() || null);
    setIf("summary", summary.value.trim() || null);
    if (kindSel.value && kindSel.value !== it.item_kind) changes.item_kind = kindSel.value;
    if (statusSel.value && statusSel.value !== it.status) changes.status = statusSel.value;
    if (confSel.value !== (it.assessment_confidence_label || "")) changes.assessment_confidence_label = confSel.value || null;
    if (visSel.value && visSel.value !== it.visibility) changes.visibility = visSel.value;
    if (reviewSel.value && reviewSel.value !== it.review_state) changes.review_state = reviewSel.value;
    const ex = excerptCb.checked ? 1 : 0;
    if (ex !== (it.excerpt_publishable || 0)) changes.excerpt_publishable = ex;
    setIf("restriction_reason", restr.value.trim() || null);
    setIf("notes", notes.value.trim() || null);
    if (Object.keys(changes).length === 0) { banner("No field changes.", "warn"); return; }
    stageChange({ op: "update_item", params: { item_id: it.item_id, changes } });
  });
  return card("Edit fields", null, [grid, el("div", { class: "inline-actions" }, [save])]);
}

// self-contained markdown block describing the on-screen item, for pasting
// into an AI (Claude) session; presentation-only, built from /api/item data
function buildAIContext(it) {
  const L = [];
  const add = (s) => L.push(s);
  add(`## G13 graph item ${it.item_id} (${it.item_kind})`);
  if (state.status) add(`Database: ${state.status.database_path} (rev ${state.status.database_revision})`);
  add(`Editor: http://${location.host}/#item/${it.item_id} · JSON: GET http://${location.host}/api/item/${encodeURIComponent(it.item_id)}`);
  add("");
  add(`**Statement:** ${it.statement || "—"}`);
  if (it.short_label) add(`**Short label:** ${it.short_label}`);
  if (it.summary) add(`**Summary:** ${it.summary}`);
  add(`**Status:** ${it.status} · confidence ${it.assessment_confidence_label || "—"} · visibility ${it.visibility} · review ${it.review_state} · provenance ${it.provenance_origin}`);
  if (it.research_path) add(`**Research location:** ${it.research_path}${it.research_heading ? " #" + it.research_heading : ""}`);
  if (it.subject_entity) add(`**Subject entity:** ${it.subject_entity_id} (${it.subject_entity.canonical_label})`);
  if (it.notes) add(`**Notes:** ${it.notes}`);
  const srcs = it.sources || [];
  if (srcs.length) {
    add("");
    add("**Sources:**");
    for (const s of srcs) add(`- [${s.role}] ${s.source_id}${s.locator ? " @ " + s.locator : ""}${s.evidence_excerpt ? ` — "${s.evidence_excerpt}"` : ""}`);
  }
  const rels = [
    ...(it.outgoing_relations || []).map((r) => `- this → ${r.relation_type} → ${r.to_item_id}${r.explanation ? ` (${r.explanation})` : ""}`),
    ...(it.incoming_relations || []).map((r) => `- ${r.from_item_id} → ${r.relation_type} → this${r.explanation ? ` (${r.explanation})` : ""}`),
  ];
  if (rels.length) { add(""); add("**Relations:**"); L.push(...rels); }
  const ents = it.entities || [];
  if (ents.length) { add(""); add("**Linked entities:**"); for (const e of ents) add(`- [${e.role}] ${e.entity_id} (${e.canonical_label || ""})`); }
  const dates = it.dates || [];
  if (dates.length) { add(""); add("**Dates:**"); for (const d of dates) add(`- [${d.date_role}] ${d.original_display || ""} [${d.precision}] plausible ${d.plausible_start || "?"}–${d.plausible_end || "?"}`); }
  const pubs = it.publications || [];
  if (pubs.length) { add(""); add("**Publication mappings:**"); for (const p of pubs) add(`- [${p.status}] ${p.publication_path}${p.heading_id ? " #" + p.heading_id : ""}${p.assertion_summary ? " — " + p.assertion_summary : ""}`); }
  const dups = it.duplicate_candidates || [];
  if (dups.length) { add(""); add("**Possible duplicates:**"); for (const d of dups) add(`- ${d.item_id} (${d.similarity}) ${d.short_label || short(d.statement, 80)}`); }
  add("");
  add("Changes go through the transactional editor ops (update_item, supersede_item, create_item, add/remove_relation, add/remove_source_link, …) via `tools/g13_graph/editor.py` / `tools/g13_graph.py author-batch` against the database above — never by editing SQLite rows directly.");
  return L.join("\n");
}

function renderSourcesCard(it) {
  const rows = (it.sources || []).map((s) =>
    el("div", { class: "src" }, [
      el("span", { class: "chip " + roleClass(s.role) }, s.role),
      el("a", { class: "link mono", onclick: () => openNeighborhood("source", s.source_id) }, s.source_id),
      s.locator ? el("span", { class: "muted" }, s.locator) : null,
      el("span", { class: "pushright" }),
      el("a", { class: "link", "aria-label": "Remove source link " + s.source_id, onclick: () => stageChange({ op: "remove_source_link", params: { item_source_id: s.item_source_id } }) }, "remove"),
      s.evidence_excerpt ? el("div", { class: "excerpt-line" }, [
        el("span", { class: "excerpt" }, "“" + short(s.evidence_excerpt, 220) + "”"),
        !s.excerpt_publishable ? el("span", { class: "warnflag" }, " (excerpt not publishable)") : null,
      ]) : null,
    ]));
  return card("Sources", el("button", { class: "small", onclick: () => addSourceForm(it) }, "+ source"),
    rows.length ? rows : [el("div", { class: "muted" }, "No source links.")]);
}

function renderRelationsCard(it) {
  const mk = (r, dir) => el("div", { class: "rel" }, [
    el("span", { class: "muted", title: dir === "out" ? "outgoing" : "incoming", "aria-label": dir === "out" ? "outgoing" : "incoming" }, dir === "out" ? "→" : "←"),
    el("span", { class: "rtype " + relTypeClass(r.relation_type) }, r.relation_type),
    el("a", { class: "link mono", onclick: () => selectItem(dir === "out" ? r.to_item_id : r.from_item_id) },
      dir === "out" ? r.to_item_id : r.from_item_id),
    el("span", { class: "chip" }, r.strength),
    r.explanation ? el("span", { class: "muted" }, short(r.explanation, 80)) : null,
    el("span", { class: "pushright" }),
    el("a", { class: "link", "aria-label": "Remove relation " + r.relation_type, onclick: () => stageChange({ op: "remove_relation", params: { from_item_id: r.from_item_id, relation_type: r.relation_type, to_item_id: r.to_item_id } }) }, "remove"),
  ]);
  const out = (it.outgoing_relations || []).map((r) => mk(r, "out"));
  const inc = (it.incoming_relations || []).map((r) => mk(r, "in"));
  const body = [...out, ...inc];
  return card("Relations", el("button", { class: "small", onclick: () => addRelationForm(it) }, "+ relation"),
    body.length ? body : [el("div", { class: "muted" }, "No relations.")]);
}

function renderEntitiesCard(it) {
  const rows = (it.entities || []).map((e) =>
    el("div", { class: "ent" }, [
      el("span", { class: "chip" }, e.role),
      el("a", { class: "link", onclick: () => openNeighborhood("entity", e.entity_id) }, e.canonical_label || e.entity_id),
      el("span", { class: "muted mono" }, e.entity_id),
      el("span", { style: "margin-left:auto" }),
      el("a", { class: "link", onclick: () => stageChange({ op: "remove_entity_link", params: { item_id: it.item_id, entity_id: e.entity_id, role: e.role } }) }, "remove"),
    ]));
  return card("Linked entities", el("button", { class: "small", onclick: () => addEntityForm(it) }, "+ entity"),
    rows.length ? rows : [el("div", { class: "muted" }, "No linked entities.")]);
}

function renderDatesCard(it) {
  const rows = (it.dates || []).map((d) => el("div", { class: "src" }, [
    el("span", { class: "chip" }, d.date_role),
    el("span", { class: "muted" }, `${d.original_display || ""} [${d.precision}]`),
    el("span", { class: "mono muted" }, `plaus ${d.plausible_start || "?"}–${d.plausible_end || "?"} / prob ${d.probable_start || "?"}–${d.probable_end || "?"}`),
  ]));
  return card("Dates", null, rows);
}

function renderNegativeCard(it) {
  const n = it.negative_result_scope;
  if (!n) return card("Negative-result scope", el("button", { class: "small", onclick: () => negativeScopeForm(it) }, "set scope"),
    [el("div", { class: "badflag" }, "No scope recorded — required for a negative_result.")]);
  return card("Negative-result scope", el("button", { class: "small", onclick: () => negativeScopeForm(it) }, "edit scope"), [
    kv([
      ["provider", n.provider],
      ["collection", n.collection_name],
      ["dates", `${n.date_start || "?"} – ${n.date_end || "?"}`],
      ["query", n.query_description],
      ["reviewed", n.results_reviewed ?? "—"],
      ["coverage confirmed", n.coverage_confirmed ? "yes" : "no"],
      ["limitations", el("ul", {}, (n.limitations || []).map((l) => el("li", {}, l)))],
    ]),
  ]);
}

function renderPublicationsCard(it) {
  const rows = (it.publications || []).map((p) => el("div", { class: "pub" }, [
    el("span", { class: "chip" }, p.status),
    el("span", { class: "mono" }, p.publication_path + (p.heading_id ? " #" + p.heading_id : "")),
    el("span", { class: "muted" }, short(p.assertion_summary || "", 50)),
    el("span", { style: "margin-left:auto" }),
    el("a", { class: "link", onclick: () => stageChange({ op: "remove_publication", params: { publication_id: p.publication_id } }) }, "remove"),
  ]));
  const pr = it.publication_readiness || {};
  const flag = pr.export_ready
    ? el("span", { class: "goodflag" }, "export-ready")
    : el("span", { class: "warnflag" }, "decisions pending");
  return card("Publication impact", [flag, el("button", { class: "small", onclick: () => addPublicationForm(it) }, "+ mapping")],
    rows.length ? rows : [el("div", { class: "muted" }, "No publication mappings.")]);
}

function renderDuplicatesCard(it) {
  return card("Possible duplicates", null,
    (it.duplicate_candidates || []).map((d) => el("div", { class: "dup" }, [
      el("a", { class: "link mono", onclick: () => selectItem(d.item_id) }, d.item_id),
      ` (${d.similarity}) `, short(d.short_label || d.statement, 70),
    ])));
}

function renderRevisionsCard(it) {
  const rows = (it.revisions || []).map((r) => el("div", { class: "revrow" }, [
    el("span", { class: "mono muted" }, "r" + r.database_revision),
    el("span", { class: "chip" }, r.change_kind),
    el("span", {}, short(r.field_summary, 60)),
    el("span", { class: "muted", style: "margin-left:auto" }, `${r.changed_by} · ${(r.changed_at || "").slice(0, 19)}`),
  ]));
  return card("Revision history (in-model audit)", null, rows.length ? rows : [el("div", { class: "muted" }, "None.")]);
}

// ------------------------------------------------------------------ item-scoped sub-forms
function subForm(title, fieldNodes, onSubmit) {
  const wrap = el("div", { class: "card", style: "margin-top:8px" }, [el("h4", {}, title)]);
  const grid = el("div", { class: "formgrid" });
  for (const [label, node] of fieldNodes) {
    grid.appendChild(el("div", { class: "label" }, label));
    grid.appendChild(node);
  }
  wrap.appendChild(grid);
  const submit = el("button", { class: "ok" }, "Preview & save");
  submit.addEventListener("click", onSubmit);
  wrap.appendChild(el("div", { class: "inline-actions" }, [submit]));
  // insert after detail top; simplest: append to detail and scroll
  $("#detail").appendChild(wrap);
  wrap.scrollIntoView({ behavior: "smooth", block: "center" });
}

function addSourceForm(it) {
  const srcInput = autocompleteInput("/api/sources", "results", "source_id", "display_title");
  const roleSel = pick("source_role");
  const locator = el("input", { type: "text", placeholder: "e.g. vol 1, p. 331" });
  const excerpt = el("textarea", { rows: "2", placeholder: "optional exact excerpt" });
  const pubCb = el("input", { type: "checkbox" });
  const verif = el("input", { type: "text", placeholder: "verification level" });
  subForm("Add source link", [
    ["source", srcInput.node], ["role", roleSel], ["locator", locator],
    ["excerpt", excerpt], ["excerpt publishable", el("div", { class: "check" }, [pubCb])],
    ["verification", verif],
  ], () => stageChange({
    op: "add_source_link", params: {
      item_id: it.item_id, source_id: srcInput.value(), role: roleSel.value,
      locator: locator.value.trim(), evidence_excerpt: excerpt.value.trim() || null,
      excerpt_publishable: pubCb.checked ? 1 : 0, verification_level: verif.value.trim() || null,
    },
  }));
}

function addRelationForm(it) {
  const relSel = pick("relation_type");
  const toInput = el("input", { type: "text", placeholder: "to item id (G13-RI-… )" });
  const bearingSel = pick("relation_bearing");
  const strengthSel = pick("relation_strength");
  const expl = el("textarea", { rows: "2", placeholder: "explanation" });
  subForm("Add relation (from this item)", [
    ["relation type", relSel], ["to item", toInput], ["bearing", bearingSel],
    ["strength", strengthSel], ["explanation", expl],
  ], () => stageChange({
    op: "add_relation", params: {
      from_item_id: it.item_id, relation_type: relSel.value, to_item_id: toInput.value.trim(),
      bearing: bearingSel.value || "direct", strength: strengthSel.value || "unknown",
      explanation: expl.value.trim() || null,
    },
  }));
}

function addEntityForm(it) {
  const entInput = autocompleteInput("/api/entities", "results", "entity_id", "canonical_label");
  const role = el("input", { type: "text", placeholder: "role (e.g. subject, mentions, place)" });
  subForm("Link entity", [["entity", entInput.node], ["role", role]],
    () => stageChange({ op: "add_entity_link", params: { item_id: it.item_id, entity_id: entInput.value(), role: role.value.trim() } }));
}

function addPublicationForm(it) {
  const path = el("input", { type: "text", placeholder: "fact-sheets/… or research/…" });
  const heading = el("input", { type: "text", placeholder: "heading id (optional)" });
  const summary = el("textarea", { rows: "2", placeholder: "assertion summary" });
  const statusSel = pick("publication_status");
  const visSel = pick("visibility", "repo_only");
  subForm("Add publication mapping", [
    ["path", path], ["heading", heading], ["assertion", summary],
    ["status", statusSel], ["visibility", visSel],
  ], () => stageChange({
    op: "add_publication", params: {
      item_id: it.item_id, publication_path: path.value.trim(), heading_id: heading.value.trim() || null,
      assertion_summary: summary.value.trim() || null, status: statusSel.value, visibility: visSel.value || "repo_only",
    },
  }));
}

function negativeScopeForm(it) {
  const n = it.negative_result_scope || {};
  const provider = el("input", { type: "text", value: n.provider || "" });
  const collection = el("input", { type: "text", value: n.collection_name || "" });
  const dateStart = el("input", { type: "text", value: n.date_start || "", placeholder: "YYYY" });
  const dateEnd = el("input", { type: "text", value: n.date_end || "", placeholder: "YYYY" });
  const query = el("textarea", { rows: "2" }); query.value = n.query_description || "";
  const reviewed = el("input", { type: "number", value: n.results_reviewed ?? "" });
  const coverage = el("input", { type: "checkbox", checked: n.coverage_confirmed ? "checked" : null });
  const limits = el("textarea", { rows: "3", placeholder: "one limitation per line" });
  limits.value = (n.limitations || []).join("\n");
  subForm("Negative-result scope", [
    ["provider", provider], ["collection", collection], ["date start", dateStart], ["date end", dateEnd],
    ["query", query], ["results reviewed", reviewed], ["coverage confirmed", el("div", { class: "check" }, [coverage])],
    ["limitations", limits],
  ], () => stageChange({
    op: "set_negative_scope", params: {
      item_id: it.item_id, provider: provider.value.trim(), collection_name: collection.value.trim(),
      date_start: dateStart.value.trim() || null, date_end: dateEnd.value.trim() || null,
      query_description: query.value.trim(), results_reviewed: reviewed.value ? Number(reviewed.value) : null,
      coverage_confirmed: coverage.checked ? 1 : 0,
      limitations: limits.value.split("\n").map((s) => s.trim()).filter(Boolean),
    },
  }));
}

function undoItem(id) { stageChange({ op: "undo_item", params: { item_id: id } }); }
function retireItem(id) {
  if (confirm("Retire (soft-delete) " + id + "? It stays in the audit trail but is marked rejected.")) {
    stageChange({ op: "retire_item", params: { item_id: id } });
  }
}

// ------------------------------------------------------------------ autocomplete
function autocompleteInput(endpoint, listKey, idKey, labelKey) {
  const input = el("input", {
    type: "text", placeholder: "type to search…", autocomplete: "off",
    role: "combobox", "aria-expanded": "false", "aria-autocomplete": "list",
  });
  const listDiv = el("div", { class: "ac-list hidden", role: "listbox" });
  const wrap = el("div", { class: "ac-wrap" }, [input, listDiv]);
  let chosen = "";
  let timer = null;
  const hide = () => { listDiv.classList.add("hidden"); input.setAttribute("aria-expanded", "false"); };
  const choose = (d) => { input.value = d.dataset.id; chosen = d.dataset.id; hide(); };
  input.addEventListener("input", () => {
    chosen = input.value.trim();
    clearTimeout(timer);
    timer = setTimeout(async () => {
      if (input.value.trim().length < 1) { hide(); return; }
      const data = await apiGet(endpoint + "?q=" + encodeURIComponent(input.value.trim()));
      listDiv.innerHTML = "";
      for (const row of (data[listKey] || []).slice(0, 15)) {
        const d = el("div", { role: "option" }, `${row[idKey]} — ${short(row[labelKey] || "", 50)}`);
        d.dataset.id = row[idKey];
        d.addEventListener("click", () => choose(d));
        listDiv.appendChild(d);
      }
      const open = listDiv.childElementCount > 0;
      listDiv.classList.toggle("hidden", !open);
      input.setAttribute("aria-expanded", open ? "true" : "false");
    }, 200);
  });
  input.addEventListener("keydown", (e) => {
    if (listDiv.classList.contains("hidden")) return;
    const options = [...listDiv.children];
    const activeIdx = options.findIndex((d) => d.classList.contains("active"));
    if (e.key === "ArrowDown" || e.key === "ArrowUp") {
      e.preventDefault();
      const next = e.key === "ArrowDown"
        ? Math.min(activeIdx + 1, options.length - 1)
        : Math.max(activeIdx - 1, 0);
      options.forEach((d, i) => d.classList.toggle("active", i === next));
      options[next].scrollIntoView({ block: "nearest" });
    } else if (e.key === "Enter" && activeIdx >= 0) {
      e.preventDefault();
      choose(options[activeIdx]);
    } else if (e.key === "Escape") {
      e.stopPropagation();
      hide();
    }
  });
  input.addEventListener("blur", () => setTimeout(hide, 200));
  return { node: wrap, value: () => chosen || input.value.trim() };
}

// ------------------------------------------------------------------ change staging (preview -> diff modal -> commit)
async function stageChange(change) {
  let preview;
  try {
    preview = await apiPost("/api/preview", change);
  } catch (e) {
    banner("Preview failed: " + e.message, "err");
    return;
  }
  showModal(change, preview);
}

function showModal(change, preview) {
  $("#modal-title").textContent = preview.summary || "Confirm change";
  const body = $("#modal-body");
  body.innerHTML = "";

  const blocked = !!(preview.blocking_errors && preview.blocking_errors.length);
  if (blocked) {
    const block = el("div", { class: "blocklist", role: "alert" },
      [el("b", {}, "✕ Blocked — this change introduces validation errors:")]);
    for (const b of preview.blocking_errors)
      block.appendChild(el("div", {}, `• ${b.code}${b.record_id ? " (" + b.record_id + ")" : ""}${b.message ? " — " + b.message : ""}`));
    body.appendChild(block);
  }

  for (const d of preview.diff || []) {
    body.appendChild(el("div", { class: "diffhead" }, [
      el("span", { class: "mono" }, d.item_id), el("b", {}, ` ${d.change_kind}`),
      d.summary ? el("span", { class: "muted" }, " — " + d.summary) : null,
    ]));
    for (const fc of d.field_changes || []) {
      body.appendChild(el("div", { class: "diffrow diff-before" }, `− ${fc.field}  ${fmtVal(fc.before)}`));
      body.appendChild(el("div", { class: "diffrow diff-after" }, `+ ${fc.field}  ${fmtVal(fc.after)}`));
    }
  }
  if (!(preview.diff || []).length && !blocked)
    body.appendChild(el("div", { class: "muted" }, "No item-field changes (structural or reference-data edit)."));

  // publication-readiness advisory: warn when the edited item is already
  // mapped into published prose, so re-wording is a conscious decision
  const cur = state.currentDetail;
  const targetId = change.params ? change.params.item_id : null;
  if (cur && targetId === cur.item_id) {
    const pubs = cur.publications || [];
    const pr = cur.publication_readiness || {};
    const notes = [];
    if (pubs.length) notes.push(`This item is mapped to ${pubs.length} publication location(s); check the prose still matches after this change.`);
    if ((pr.export_blockers || []).length || pr.excerpt_decisions_pending) notes.push("Publication decisions are still pending for this item.");
    if (notes.length) body.appendChild(el("div", { class: "warnpanel" }, notes.join(" ")));
  }

  const errs = (preview.validation_issues || []).filter((i) => i.severity === "error");
  const warns = (preview.validation_issues || []).filter((i) => i.severity === "warning");
  if (warns.length) {
    const panel = el("div", { class: "warnpanel" }, [el("b", {}, `Advisory — ${warns.length} warning(s) after this change (do not block):`)]);
    for (const w of warns.slice(0, 8))
      panel.appendChild(el("div", {}, `• ${w.code}${w.record_id ? " (" + w.record_id + ")" : ""}`));
    if (warns.length > 8) panel.appendChild(el("div", { class: "muted" }, `… and ${warns.length - 8} more`));
    body.appendChild(panel);
  }
  body.appendChild(el("div", { class: "issuelist", style: "margin-top:8px" },
    `Post-change validation: ${errs.length} error(s)` +
    (errs.length && !blocked ? " (pre-existing, not introduced by this change)" : "") +
    `, ${warns.length} warning(s).`));

  const commitBtn = $("#modal-commit");
  commitBtn.disabled = !preview.can_commit;
  commitBtn.onclick = async () => {
    commitBtn.disabled = true;
    try {
      const res = await apiPost("/api/commit", change);
      closeModal();
      if (res.stale) banner("Committed r" + res.database_revision + " — but the recovery export FAILED (stale/unsafe): " + res.refresh_error, "err");
      else banner("Committed r" + res.database_revision + " · " + (res.summary || ""), "ok");
      await afterCommit(res);
    } catch (e) {
      commitBtn.disabled = !preview.can_commit;
      if (e.status === 409) {
        banner("Commit blocked by validation.", "err");
      } else {
        banner("Commit failed: " + e.message, "err");
      }
    }
  };
  openModal(blocked);
}

let modalReturnFocus = null;
function openModal(blocked) {
  modalReturnFocus = document.activeElement;
  $("#modal-backdrop").classList.remove("hidden");
  // focus the safe default: Commit when allowed, Discard when blocked
  (blocked ? $("#modal-cancel") : $("#modal-commit")).focus();
}
function closeModal() {
  $("#modal-backdrop").classList.add("hidden");
  if (modalReturnFocus && document.contains(modalReturnFocus)) modalReturnFocus.focus();
  modalReturnFocus = null;
}
function modalKeydown(e) {
  if ($("#modal-backdrop").classList.contains("hidden")) return;
  if (e.key === "Escape") { e.preventDefault(); closeModal(); return; }
  if (e.key !== "Tab") return;
  // keep Tab cycling inside the dialog
  const focusable = [...$("#modal-backdrop").querySelectorAll("button, [href], input, select, textarea, [tabindex]")]
    .filter((n) => !n.disabled && n.offsetParent !== null);
  if (!focusable.length) return;
  const first = focusable[0], last = focusable[focusable.length - 1];
  if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
  else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
}
function fmtVal(v) {
  if (v === null || v === undefined) return "∅";
  if (typeof v === "object") return short(JSON.stringify(v), 400);
  return short(String(v), 400);
}

async function afterCommit(res) {
  await refreshStatus();
  await loadUnits();
  const focus = (res.affected_items && res.affected_items[0]) || state.selectedId;
  if (state.tab === "queue") await loadQueue();
  else await loadItems();
  if (focus) { try { await selectItem(focus); } catch (_) {} }
}

// ------------------------------------------------------------------ create item
function renderCreateForm() {
  const host = $("#create-form");
  host.innerHTML = "";
  const kind = pick("item_kind", "research_finding");
  const statement = el("textarea", { rows: "3", placeholder: "statement (required)" });
  const shortLabel = el("input", { type: "text", placeholder: "short label" });
  const unitSel = el("select", {}, [el("option", { value: "" }, "— research unit (required) —")]);
  for (const u of state.units) unitSel.appendChild(el("option", { value: u.unit_id }, u.title || u.unit_id));
  const subj = autocompleteInput("/api/entities", "results", "entity_id", "canonical_label");
  const conf = pick("confidence_label");
  const vis = pick("visibility", "repo_only");
  const dupBox = el("div", {});
  statement.addEventListener("input", () => scheduleDupCheck(statement, shortLabel, subj, dupBox));
  shortLabel.addEventListener("input", () => scheduleDupCheck(statement, shortLabel, subj, dupBox));

  const grid = el("div", { class: "formgrid" });
  const rows = [["kind", kind], ["statement", statement], ["short label", shortLabel],
    ["research unit", unitSel], ["subject entity", subj.node], ["confidence", conf], ["visibility", vis]];
  for (const [l, n] of rows) { grid.appendChild(el("div", { class: "label" }, l)); grid.appendChild(n); }

  const btn = el("button", { class: "ok" }, "Preview & create");
  btn.addEventListener("click", () => {
    if (!statement.value.trim() || !unitSel.value) { banner("Statement and research unit are required.", "err"); return; }
    const item = {
      item_kind: kind.value, statement: statement.value.trim(),
      short_label: shortLabel.value.trim() || null, research_unit_id: unitSel.value,
      assessment_confidence_label: conf.value || null, visibility: vis.value || "repo_only",
    };
    const sv = subj.value();
    if (sv) item.subject_entity_id = sv;
    stageChange({ op: "create_item", params: { item } });
  });
  host.appendChild(el("div", { class: "card" }, [el("h4", {}, "Create research item"), grid, dupBox, el("div", { class: "inline-actions" }, [btn])]));
  host.appendChild(el("div", { class: "muted", style: "margin-top:8px" },
    "Reminder: a negative_result also needs scope; add it from the item detail after creating. Sources, relations, entities are added from the item detail."));
}

let dupTimer = null;
function scheduleDupCheck(statement, shortLabel, subj, box) {
  clearTimeout(dupTimer);
  dupTimer = setTimeout(async () => {
    const q = (shortLabel.value + " " + statement.value).trim();
    if (q.length < 8) { box.innerHTML = ""; return; }
    // reuse text filter as a lightweight duplicate probe
    const data = await apiGet("/api/items?q=" + encodeURIComponent(shortLabel.value.trim() || statement.value.trim().slice(0, 24)));
    box.innerHTML = "";
    const hits = (data.items || []).slice(0, 4);
    if (hits.length) {
      box.appendChild(el("div", { class: "dup" }, [el("b", {}, "Similar existing items: "),
        ...hits.map((h) => el("a", { class: "link mono", style: "margin-right:8px", onclick: () => { switchTab("items"); selectItem(h.item_id); } }, h.item_id))]));
    }
  }, 350);
}

// ------------------------------------------------------------------ review queue
async function loadQueue() {
  const data = await apiGet("/api/review-queue");
  $("#queue-meta").textContent = `${data.count} machine-suggested item(s) awaiting review`;
  const list = $("#queue-list");
  list.innerHTML = "";
  state.queueSelection.clear();
  for (const it of data.queue) {
    const cb = el("input", { type: "checkbox", "aria-label": "Select " + it.item_id + " for batch review", style: "width:auto" });
    cb.addEventListener("click", (e) => { e.stopPropagation(); if (cb.checked) state.queueSelection.add(it.item_id); else state.queueSelection.delete(it.item_id); });
    const li = el("li", { class: kindClass(it.item_kind), tabindex: "0", role: "option", "aria-selected": "false" }, [
      el("div", { class: "row1" }, [cb, el("span", { class: "kind " + kindClass(it.item_kind) }, it.item_kind), el("span", { class: "id" }, it.item_id)]),
      el("div", { class: "stmt" }, short(it.short_label || it.statement)),
    ]);
    li.dataset.id = it.item_id;
    li.addEventListener("click", () => selectItem(it.item_id));
    list.appendChild(li);
  }
  if (!data.queue.length) list.appendChild(el("li", { class: "emptylist" }, "Review queue is empty."));
}
async function queueReview(reviewState, status) {
  const ids = [...state.queueSelection];
  if (!ids.length) { banner("Select queue items first.", "warn"); return; }
  stageChange({ op: "set_review_state", params: { item_ids: ids, review_state: reviewState, status } });
}

// ------------------------------------------------------------------ search + neighborhood
async function runSearch(ev) {
  ev.preventDefault();
  const terms = $("#search-terms").value.trim();
  if (!terms) return;
  let data;
  try { data = await apiGet("/api/search?terms=" + encodeURIComponent(terms)); }
  catch (e) { banner("Search failed: " + e.message, "err"); return; }
  const list = $("#search-list");
  list.innerHTML = "";
  for (const r of data.results || []) {
    const li = el("li", { tabindex: "0", role: "option", "aria-selected": "false" }, [
      el("div", { class: "row1" }, [el("span", { class: "chip" }, r.record_type), el("span", { class: "id" }, r.record_id)]),
      snippetNode(r.snippet || ""),
    ]);
    li.dataset.id = r.record_id;
    if (r.record_type === "research_item") li.addEventListener("click", () => { switchTab("items"); selectItem(r.record_id); });
    else if (r.record_type === "entity") li.addEventListener("click", () => openNeighborhood("entity", r.record_id));
    else if (r.record_type === "research_unit") li.addEventListener("click", () => openNeighborhood("unit", r.record_id));
    list.appendChild(li);
  }
  if (!(data.results || []).length) list.appendChild(el("li", { class: "emptylist" }, "No matches."));
}

// FTS snippets mark hits as [term]; render them as highlights without innerHTML
function snippetNode(snippet) {
  const div = el("div", { class: "stmt" });
  const parts = snippet.split(/\[([^\]]*)\]/);
  parts.forEach((p, i) => {
    if (!p) return;
    div.appendChild(i % 2 ? el("mark", {}, p) : document.createTextNode(p));
  });
  return div;
}

async function openNeighborhood(kind, id) {
  let data;
  try { data = await apiGet(`/api/neighborhood?kind=${encodeURIComponent(kind)}&id=${encodeURIComponent(id)}`); }
  catch (e) { banner("Not found: " + id, "err"); return; }
  const root = $("#detail");
  root.className = "detail";
  root.innerHTML = "";
  if (data.kind === "entity") {
    root.appendChild(el("h2", {}, data.entity.canonical_label));
    root.appendChild(el("div", { class: "sub" }, `${data.entity.entity_id} · ${data.entity.entity_type}`));
    root.appendChild(card("Aliases", null, (data.aliases || []).length ? data.aliases.map((a) => el("div", {}, `${a.alias} (${a.alias_type})`)) : [el("div", { class: "muted" }, "None.")]));
    root.appendChild(card("Items in this neighborhood", null, (data.items || []).map((i) =>
      el("div", { class: "ent" }, [el("span", { class: "kind" }, i.item_kind), el("a", { class: "link mono", onclick: () => { switchTab("items"); selectItem(i.item_id); } }, i.item_id), short(i.short_label || i.statement, 70)]))));
  } else if (data.kind === "source") {
    const s = data.source;
    root.appendChild(el("h2", {}, s.display_title));
    root.appendChild(el("div", { class: "sub" }, `${s.source_id}`));
    root.appendChild(card("Cited by", null, (s.items || []).map((i) =>
      el("div", { class: "src" }, [el("span", { class: "chip" }, i.role), el("a", { class: "link mono", onclick: () => { switchTab("items"); selectItem(i.item_id); } }, i.item_id), short(i.statement, 60)]))));
  } else if (data.kind === "unit") {
    const u = data.unit;
    root.appendChild(el("h2", {}, u.title));
    root.appendChild(el("div", { class: "sub" }, `${u.unit_id} · ${u.path}`));
    root.appendChild(card("Items", null, (u.items || []).map((i) =>
      el("div", { class: "ent" }, [el("span", { class: "kind" }, i.item_kind), el("a", { class: "link mono", onclick: () => { switchTab("items"); selectItem(i.item_id); } }, i.item_id), short(i.statement, 70)]))));
  }
}

// ------------------------------------------------------------------ tabs + wiring
function switchTab(name) {
  state.tab = name;
  document.querySelectorAll(".tab").forEach((t) => {
    const active = t.dataset.tab === name;
    t.classList.toggle("active", active);
    t.setAttribute("aria-selected", active ? "true" : "false");
  });
  document.querySelectorAll(".tabpane").forEach((p) => p.classList.toggle("active", p.id === "tab-" + name));
  if (name === "queue") loadQueue();
  if (name === "create") renderCreateForm();
}

async function loadUnits() {
  const data = await apiGet("/api/units");
  state.units = data.units || [];
}

async function init() {
  document.querySelectorAll(".tab").forEach((t) => t.addEventListener("click", () => switchTab(t.dataset.tab)));
  // arrow keys move between tabs (roving focus)
  $(".tabs").addEventListener("keydown", (e) => {
    if (e.key !== "ArrowLeft" && e.key !== "ArrowRight") return;
    const tabs = [...document.querySelectorAll(".tab")];
    const i = tabs.indexOf(document.activeElement);
    if (i === -1) return;
    e.preventDefault();
    const next = tabs[(i + (e.key === "ArrowRight" ? 1 : tabs.length - 1)) % tabs.length];
    next.focus();
    switchTab(next.dataset.tab);
  });
  for (const id of ["#item-list", "#queue-list", "#search-list"])
    $(id).addEventListener("keydown", listKeydown);
  document.addEventListener("keydown", modalKeydown, true);
  // "/" focuses the filter or search box of the active tab
  document.addEventListener("keydown", (e) => {
    if (e.key !== "/" || e.ctrlKey || e.metaKey || e.altKey) return;
    const t = e.target;
    if (t && (t.tagName === "INPUT" || t.tagName === "TEXTAREA" || t.tagName === "SELECT")) return;
    if (!$("#modal-backdrop").classList.contains("hidden")) return;
    const target = state.tab === "search" ? $("#search-terms") : $("#filters input[type=text]");
    if (target) { e.preventDefault(); target.focus(); target.select(); }
  });
  $("#btn-refresh").addEventListener("click", async () => { await refreshStatus(); await loadItems(); });
  $("#btn-snapshot").addEventListener("click", async () => {
    try { const r = await apiPost("/api/snapshot", {}); banner("Snapshot written: " + r.snapshot, "ok"); await refreshStatus(); }
    catch (e) { banner("Snapshot failed: " + e.message, "err"); }
  });
  $("#btn-export-recovery").addEventListener("click", async () => {
    try { await apiPost("/api/export-recovery", {}); banner("Recovery export refreshed.", "ok"); await refreshStatus(); }
    catch (e) { banner("Export failed: " + e.message, "err"); }
  });
  $("#queue-accept").addEventListener("click", () => queueReview("human_reviewed"));
  $("#queue-reject").addEventListener("click", () => queueReview("rejected", "rejected"));
  $("#search-form").addEventListener("submit", runSearch);
  $("#modal-cancel").addEventListener("click", closeModal);
  $("#modal-backdrop").addEventListener("click", (e) => { if (e.target.id === "modal-backdrop") closeModal(); });

  const pl = await apiGet("/api/picklists");
  state.picklists = pl.picklists || {};
  state.units = pl.units || [];
  await refreshStatus();
  renderFilters();
  await loadItems();

  // deep link: #item/<id> selects that item on load and on hash change
  const openFromHash = () => {
    const m = location.hash.match(/^#item\/(.+)$/);
    if (m && decodeURIComponent(m[1]) !== state.selectedId) selectItem(decodeURIComponent(m[1]));
  };
  window.addEventListener("hashchange", openFromHash);
  openFromHash();
}

init().catch((e) => banner("Init failed: " + e.message, "err"));
