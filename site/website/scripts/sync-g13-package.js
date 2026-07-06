/*
 * G13 package adapter (Plan 03 §8, Plan 04 §11).
 *
 * A sync step in the sync-site-content.js family: reads the selected G13
 * topic package (manifest + staged Markdown) and the public research-graph
 * export, and generates the annex hub, topic pages, permanent evidence and
 * finding pages, and the drawer's static JSON into the Eleventy site source.
 *
 * Mode is selected by the G13_PACKAGE environment variable:
 *   (unset)/off  → disabled; generated targets are cleaned and nothing is
 *                  written, so the ordinary build stays pure legacy.
 *   staging      → read research/people/_staging/g13-john-gurney (preview).
 *   production   → read research/people/g13-john-gurney (post-cutover).
 *
 * The adapter is a content-discovery and presentation-input step, not a
 * second static-site generator: everything it writes renders through the
 * ordinary Eleventy layouts, finalizer, and validators.
 */
const fs = require("fs");
const path = require("path");

const projectRoot = path.resolve(__dirname, "..");
const repoRoot = path.resolve(projectRoot, "..", "..");
const render = require(path.join(projectRoot, "assets", "g13-graph-render.js"));

const annexTarget = path.join(projectRoot, "research", "g13-annex");
const graphAssetsTarget = path.join(projectRoot, "assets", "g13-graph");
const graphExportDir = path.join(repoRoot, "data", "context-graphs", "g13", "exports", "website");
const githubBlobBase = "https://github.com/allengurney/gurney-genealogy/blob/main/";

const PACKAGE_ROOTS = {
  staging: path.join(repoRoot, "research", "people", "_staging", "g13-john-gurney"),
  production: path.join(repoRoot, "research", "people", "g13-john-gurney"),
};

function getPackageConfig() {
  const mode = String(process.env.G13_PACKAGE || "").trim().toLowerCase();
  if (!mode || mode === "off" || mode === "legacy") {
    return { enabled: false, mode: "off" };
  }
  const packageRoot = PACKAGE_ROOTS[mode];
  if (!packageRoot) {
    throw new Error(`Unknown G13_PACKAGE mode: ${mode} (expected off|staging|production)`);
  }
  return { enabled: true, mode, packageRoot, hubSlug: "g13-john-gurney" };
}

function toPosix(value) {
  return value.replace(/\\/g, "/");
}

function readJson(file, label) {
  if (!fs.existsSync(file)) throw new Error(`${label} missing: ${file}`);
  return JSON.parse(fs.readFileSync(file, "utf8"));
}

function cleanDir(dir) {
  fs.rmSync(dir, { recursive: true, force: true });
}

function ensureDir(dir) {
  fs.mkdirSync(dir, { recursive: true });
}

function stripLeadingComment(markdown) {
  return String(markdown || "").replace(/^\s*<!--[\s\S]*?-->\s*/, "");
}

function trimDescription(value, maxLength = 160) {
  const clean = String(value || "").replace(/\s+/g, " ").trim();
  if (clean.length <= maxLength) return clean;
  const slice = clean.slice(0, maxLength + 1);
  const wordBreak = slice.lastIndexOf(" ");
  const trimmed = clean.slice(0, wordBreak > 120 ? wordBreak : maxLength).replace(/[,:;–—-]\s*$/u, "").trim();
  return /[.!?]$/.test(trimmed) ? trimmed : `${trimmed}.`;
}

function frontMatter(fields) {
  const lines = ["---"];
  Object.entries(fields).forEach(([key, value]) => {
    lines.push(`${key}: ${typeof value === "string" ? JSON.stringify(value) : value}`);
  });
  lines.push("---", "", "");
  return lines.join("\n");
}

// ---------------------------------------------------------------------------
// Manifest validation (Plan 03 §12)
// ---------------------------------------------------------------------------
function validateManifest(manifest, packageRoot) {
  const errors = [];
  const website = manifest.website;
  if (!website || !website.title || !website.hubSlug || !website.introFile) {
    errors.push("manifest.website must define title, hubSlug, and introFile");
  }
  const groups = (website && website.groups) || [];
  const groupIds = new Set(groups.map(group => group.id));
  const seen = { topicId: new Set(), publicSlug: new Set(), title: new Set() };
  (manifest.topics || []).forEach(topic => {
    ["topicId", "path", "title", "summary", "group", "publicSlug"].forEach(field => {
      if (!topic[field]) errors.push(`topic ${topic.topicId || topic.path} missing ${field}`);
    });
    ["topicId", "publicSlug", "title"].forEach(field => {
      if (topic[field]) {
        if (seen[field].has(topic[field])) errors.push(`duplicate topic ${field}: ${topic[field]}`);
        seen[field].add(topic[field]);
      }
    });
    if (topic.group && !groupIds.has(topic.group)) {
      errors.push(`topic ${topic.topicId} references unknown group: ${topic.group}`);
    }
    if (topic.path && !fs.existsSync(path.join(repoRoot, topic.path))) {
      errors.push(`topic file missing: ${topic.path}`);
    }
  });
  if (website && website.introFile && !fs.existsSync(path.join(repoRoot, website.introFile))) {
    errors.push(`website.introFile missing: ${website.introFile}`);
  }
  if (!toPosix(path.join(repoRoot, manifest.topics?.[0]?.path || "")).startsWith(toPosix(packageRoot))) {
    errors.push("manifest topic paths must live under the selected package root");
  }
  if (errors.length) {
    throw new Error(`G13 package manifest validation failed:\n- ${errors.join("\n- ")}`);
  }
}

// ---------------------------------------------------------------------------
// Link rewriting: staged prose → public URLs / GitHub artifact links
// ---------------------------------------------------------------------------
function loadPlacePageSlugs() {
  const placePagesPath = path.join(projectRoot, "_data", "placePages.json");
  const slugs = new Set();
  try {
    JSON.parse(fs.readFileSync(placePagesPath, "utf8")).forEach(page => {
      if (page.researchSlug) slugs.add(page.researchSlug);
      if (page.slug) slugs.add(page.slug);
    });
  } catch {
    // Best effort: _data/placePages.json regenerates later in the pipeline.
  }
  return slugs;
}

function loadPublishedTopicSlugs() {
  const csvPath = path.join(repoRoot, "research", "topics", "_published-topics.csv");
  const slugs = new Set();
  if (!fs.existsSync(csvPath)) return slugs;
  fs.readFileSync(csvPath, "utf8").split(/\r?\n/).forEach(line => {
    const filename = line.split(",")[0].trim();
    if (filename && filename.endsWith(".md") && !/^filename$/i.test(filename)) {
      slugs.add(filename.replace(/\.md$/i, ""));
    }
  });
  return slugs;
}

function buildLinkRewriter(topicsByRepoPath, hubUrl, placeSlugs, publishedTopicSlugs) {
  return function rewriteLinks(markdown, sourceRepoDir) {
    return markdown.replace(
      /\[([^\]]*)\]\(([^)\s]+)(\s+"[^"]*")?\)/g,
      (match, text, target, title) => {
        if (/^(?:[a-z][a-z0-9+.-]*:|\/\/|#|\/)/i.test(target)) return match;
        const [rawPath, anchor = ""] = target.split(/(#.*)$/, 2);
        if (!/\.md$/i.test(rawPath)) return match;
        const resolved = toPosix(path.posix.normalize(path.posix.join(toPosix(sourceRepoDir), rawPath)));

        const topic = topicsByRepoPath.get(resolved);
        if (topic) {
          const newText = /\.md$/i.test(text.trim()) || text.trim() === rawPath ? topic.title : text;
          return `[${newText}](${topic.url}${anchor})`;
        }
        const placeMatch = resolved.match(/^research\/places\/([a-z0-9-]+)\.md$/i);
        if (placeMatch && placeSlugs.has(placeMatch[1])) {
          return `[${text}](/research/places/${placeMatch[1]}${anchor})`;
        }
        const topicMatch = resolved.match(/^research\/topics\/([a-z0-9-]+)\.md$/i);
        if (topicMatch && publishedTopicSlugs.has(topicMatch[1])) {
          return `[${text}](/key-research/topics/${topicMatch[1]}${anchor})`;
        }
        return `[${text}](${githubBlobBase}${resolved}${title || ""})`;
      }
    );
  };
}

// ---------------------------------------------------------------------------
// Evidence-link substitution (Plan 04 §4)
// ---------------------------------------------------------------------------
function buildMarkerReplacer(markerIndexById, dropped) {
  return function replaceMarkers(markdown) {
    return markdown.replace(/\s*<!--\s*graph-marker:\s*(G13-PM-\d{6})\s*-->/g, (match, markerId) => {
      const marker = markerIndexById.get(markerId);
      if (!marker) {
        dropped.push(markerId);
        return "";
      }
      const label = marker.primaryLabel || "this passage";
      return (
        ` <a class="evidence-link" href="${render.markerUrl(markerId)}"` +
        ` data-evidence-id="${markerId}"` +
        ` aria-label="Evidence explaining: ${render.escapeHtml(label)}">Evidence</a>`
      );
    });
  };
}

// ---------------------------------------------------------------------------
// Graph export → site context
// ---------------------------------------------------------------------------
function buildGraphContext(manifest, hubUrl, topicUrlByTopicId) {
  const exportManifest = readJson(path.join(graphExportDir, "manifest.json"), "graph export manifest");
  const findingsIndex = readJson(path.join(graphExportDir, "findings.json"), "graph findings index");
  const markersIndex = readJson(path.join(graphExportDir, "markers.json"), "graph markers index");
  const sourcesRegistry = readJson(path.join(repoRoot, "data", "sources.json"), "canonical sources").sources || {};

  const labelById = new Map(findingsIndex.map(entry => [entry.id, entry]));
  const markerById = new Map(markersIndex.map(entry => [entry.id, entry]));

  const relatedWebsite = manifest.website.related || {};
  const publicationTargets = [
    {
      pattern: /^fact-sheets\/g13-john-gurney-fact-sheet\.md$/,
      url: relatedWebsite.factSheetUrl,
      title: relatedWebsite.factSheetTitle || "John Gurney fact sheet",
    },
    {
      pattern: /^research\/case-files\/john-gurney-case-file/,
      url: relatedWebsite.caseFileUrl,
      title: relatedWebsite.caseFileTitle || "John Gurney case file",
    },
  ];

  const ctx = {
    labelFor: id => labelById.get(id) || null,
    source: sourceId => {
      const source = sourcesRegistry[sourceId];
      return source ? { citation: source.citation, shortTitle: source.shortTitle, url: source.url } : null;
    },
    topicUrl: unitId => topicUrlByTopicId.get(unitId) || null,
    publicationUrl: publicationPath => {
      const target = publicationTargets.find(entry => entry.pattern.test(publicationPath) && entry.url);
      return target ? { url: target.url, title: target.title } : null;
    },
  };
  return { ctx, exportManifest, findingsIndex, markersIndex, markerById, labelById, sourcesRegistry };
}

function copyGraphAssets(graph, topicUrlByTopicId, relatedWebsite) {
  ensureDir(graphAssetsTarget);
  // Drawer-side counterpart of ctx.topicUrl/ctx.publicationUrl.
  const siteMap = {
    topics: Object.fromEntries(topicUrlByTopicId),
    publications: [
      relatedWebsite.factSheetUrl && {
        prefix: "fact-sheets/g13-john-gurney-fact-sheet.md",
        url: relatedWebsite.factSheetUrl,
        title: relatedWebsite.factSheetTitle || "John Gurney fact sheet",
      },
      relatedWebsite.caseFileUrl && {
        prefix: "research/case-files/john-gurney-case-file",
        url: relatedWebsite.caseFileUrl,
        title: relatedWebsite.caseFileTitle || "John Gurney case file",
      },
    ].filter(Boolean),
  };
  fs.writeFileSync(path.join(graphAssetsTarget, "site-map.json"), `${JSON.stringify(siteMap)}\n`);
  ["manifest.json", "findings.json", "markers.json"].forEach(file => {
    fs.copyFileSync(path.join(graphExportDir, file), path.join(graphAssetsTarget, file));
  });
  ["findings", "marker-bundles"].forEach(dir => {
    const sourceDir = path.join(graphExportDir, dir);
    const targetDir = path.join(graphAssetsTarget, dir);
    ensureDir(targetDir);
    fs.readdirSync(sourceDir)
      .filter(file => file.endsWith(".json"))
      .forEach(file => fs.copyFileSync(path.join(sourceDir, file), path.join(targetDir, file)));
  });
  // Compact citation lookup so the drawer resolves sourceIds like the
  // permanent pages do, without shipping all of data/sources.json.
  const cited = new Set();
  fs.readdirSync(path.join(graphExportDir, "findings"))
    .filter(file => file.endsWith(".json"))
    .forEach(file => {
      const finding = readJson(path.join(graphExportDir, "findings", file), file);
      (finding.sources || []).forEach(source => cited.add(source.sourceId));
    });
  const subset = {};
  [...cited].sort().forEach(sourceId => {
    const source = graph.sourcesRegistry[sourceId];
    if (source) subset[sourceId] = { citation: source.citation || "", shortTitle: source.shortTitle || "", url: source.url || "" };
  });
  fs.writeFileSync(path.join(graphAssetsTarget, "sources.json"), `${JSON.stringify(subset)}\n`);
}

// ---------------------------------------------------------------------------
// Page generation
// ---------------------------------------------------------------------------
function breadcrumbsHtml(entries) {
  const parts = entries
    .map(entry =>
      entry.url
        ? `<a href="${entry.url}">${render.escapeHtml(entry.title)}</a>`
        : `<span aria-current="page">${render.escapeHtml(entry.title)}</span>`
    )
    .join(' <span class="g13-crumb-sep" aria-hidden="true">›</span> ');
  return `<nav class="g13-breadcrumbs" aria-label="Breadcrumb">${parts}</nav>`;
}

function writeHubPage(manifest, orderedGroups, topicsByGroup, hubUrl) {
  const website = manifest.website;
  const intro = stripLeadingComment(fs.readFileSync(path.join(repoRoot, website.introFile), "utf8")).trim();
  const related = website.related || {};

  const sections = orderedGroups
    .map(group => {
      const topics = topicsByGroup.get(group.id) || [];
      if (!topics.length) return "";
      const cards = topics
        .map(topic =>
          `<a class="g13-card" href="${topic.url}"><span class="g13-card-title">${render.escapeHtml(topic.title)}</span><span class="g13-card-summary">${render.escapeHtml(topic.summary)}</span></a>`
        )
        .join("");
      return `<section class="g13-group" id="group-${group.id}"><h2>${render.escapeHtml(group.title)}</h2><div class="g13-cards">${cards}</div></section>`;
    })
    .join("\n");

  const relatedLinks = [
    related.factSheetUrl ? `<li><a href="${related.factSheetUrl}">${render.escapeHtml(related.factSheetTitle || "Fact sheet")}</a> — the concise published biography.</li>` : "",
    related.caseFileUrl ? `<li><a href="${related.caseFileUrl}">${render.escapeHtml(related.caseFileTitle || "Case file")}</a> — the polished identification argument.</li>` : "",
  ].filter(Boolean).join("");

  const indexList = orderedGroups
    .map(group => {
      const topics = topicsByGroup.get(group.id) || [];
      if (!topics.length) return "";
      const items = topics.map(topic => `<li><a href="${topic.url}">${render.escapeHtml(topic.title)}</a></li>`).join("");
      return `<li>${render.escapeHtml(group.title)}<ul>${items}</ul></li>`;
    })
    .join("");

  const body = [
    intro,
    "",
    sections,
    relatedLinks ? `<section class="g13-group"><h2>Fact sheet and case file</h2><ul class="g13-list">${relatedLinks}</ul></section>` : "",
    `<section class="g13-group"><h2>All topics</h2><ul class="g13-topic-index">${indexList}</ul></section>`,
    "",
  ].join("\n");

  const content = frontMatter({
    title: website.title,
    description:
      "The comprehensive working research on John Gurney of Weymouth and Braintree, Massachusetts (G13), organized by topic: colonial life, family, and the research state of the open English-origin question.",
    permalink: `/research/notes/${manifest.website.hubSlug}.html`,
    g13Annex: true,
    eleventyExcludeFromCollections: true,
  }) + body;
  fs.writeFileSync(path.join(annexTarget, "index.md"), content);
}

function writeTopicPages(manifest, orderedTopics, hubUrl, transforms) {
  orderedTopics.forEach((topic, index) => {
    const raw = fs.readFileSync(path.join(repoRoot, topic.path), "utf8");
    const sourceRepoDir = toPosix(path.posix.dirname(toPosix(topic.path)));
    let body = stripLeadingComment(raw);
    body = transforms.rewriteLinks(body, sourceRepoDir);
    body = transforms.replaceMarkers(body);

    const prev = orderedTopics[index - 1];
    const next = orderedTopics[index + 1];
    const navParts = [
      prev ? `<a class="g13-prev" rel="prev" href="${prev.url}">← ${render.escapeHtml(prev.title)}</a>` : "<span></span>",
      `<a class="g13-up" href="${hubUrl}">All topics</a>`,
      next ? `<a class="g13-next" rel="next" href="${next.url}">${render.escapeHtml(next.title)} →</a>` : "<span></span>",
    ].join("");

    const content =
      frontMatter({
        title: topic.title,
        description: trimDescription(topic.summary),
        permalink: `${topic.url}.html`,
        g13Annex: true,
        eleventyExcludeFromCollections: true,
      }) +
      breadcrumbsHtml([
        { title: "John Gurney Research Library", url: hubUrl },
        { title: topic.groupTitle, url: `${hubUrl}#group-${topic.group}` },
        { title: topic.title },
      ]) +
      "\n\n" +
      body.trim() +
      "\n\n" +
      `<nav class="g13-topic-nav" aria-label="Topic navigation">${navParts}</nav>\n`;

    fs.writeFileSync(path.join(annexTarget, `topic-${topic.publicSlug.replace(/\//g, "--")}.md`), content);
  });
}

function writeEvidencePages(graph, hubUrl) {
  const revision = String(graph.exportManifest.database_revision);
  const evidenceDir = path.join(annexTarget, "evidence");
  ensureDir(evidenceDir);
  fs.readdirSync(path.join(graphExportDir, "marker-bundles"))
    .filter(file => file.endsWith(".json"))
    .sort()
    .forEach(file => {
      const bundle = readJson(path.join(graphExportDir, "marker-bundles", file), file);
      const primary = bundle.primary;
      const label = primary.shortLabel || primary.statement;
      const topic = graph.ctx.topicUrl(bundle.unit && bundle.unit.id);
      const contextLine = topic
        ? `<p class="g13-context-line">This page expands an <strong>Evidence</strong> link in <a href="${topic.url}">${render.escapeHtml(topic.title)}</a>: the findings, sources, and qualifications behind the marked passage.</p>`
        : "";
      const body =
        breadcrumbsHtml([
          { title: "John Gurney Research Library", url: hubUrl },
          { title: "Evidence" },
        ]) +
        "\n\n" +
        contextLine +
        render.renderMarkerBundle(bundle, graph.ctx, { headingTag: "h1", compact: false, revision }) +
        "\n";
      const content =
        frontMatter({
          title: `Evidence — ${label}`,
          description: trimDescription(
            `${primary.statement} The findings, sources, and qualifications behind this conclusion in the John Gurney (G13) research graph.`
          ),
          permalink: `${bundle.url}index.html`,
          g13Annex: true,
          eleventyExcludeFromCollections: true,
        }) + body;
      fs.writeFileSync(path.join(evidenceDir, `${bundle.id}.md`), content);
    });
}

function writeFindingPages(graph, hubUrl) {
  const revision = String(graph.exportManifest.database_revision);
  const findingsDir = path.join(annexTarget, "findings");
  ensureDir(findingsDir);
  fs.readdirSync(path.join(graphExportDir, "findings"))
    .filter(file => file.endsWith(".json"))
    .sort()
    .forEach(file => {
      const finding = readJson(path.join(graphExportDir, "findings", file), file);
      const label = finding.shortLabel || finding.statement;
      const body =
        breadcrumbsHtml([
          { title: "John Gurney Research Library", url: hubUrl },
          { title: "Research findings" },
        ]) +
        "\n\n" +
        render.renderFinding(finding, graph.ctx, { headingTag: "h1", compact: false, revision }) +
        `\n<p class="g13-context-line">This is one research item from the John Gurney research graph; the fuller narrative treatment is in the linked topic above and the <a href="${hubUrl}">research library</a>.</p>\n`;
      const content =
        frontMatter({
          title: `${finding.kindLabel}: ${label}`,
          description: trimDescription(
            `${finding.statement} One ${finding.kindLabel.toLowerCase()} from the John Gurney (G13) research graph, with its sources and related findings.`
          ),
          permalink: `/research/findings/${finding.id.toLowerCase()}/index.html`,
          g13Annex: true,
          eleventyExcludeFromCollections: true,
        }) + body;
      fs.writeFileSync(path.join(findingsDir, `${finding.id}.md`), content);
    });
}

// ---------------------------------------------------------------------------
// Entry point
// ---------------------------------------------------------------------------
function syncG13Package() {
  // Always clean the generated targets first: a disabled run leaves nothing
  // behind, so an ordinary build can never publish leftover preview inputs.
  cleanDir(annexTarget);
  cleanDir(graphAssetsTarget);

  const config = getPackageConfig();
  if (!config.enabled) return { enabled: false, pages: 0 };

  const manifest = readJson(path.join(config.packageRoot, "manifest.json"), "G13 package manifest");
  validateManifest(manifest, config.packageRoot);

  const hubUrl = `/research/notes/${manifest.website.hubSlug}`;
  const orderedGroups = [...manifest.website.groups].sort((a, b) => a.order - b.order);
  const groupTitleById = new Map(orderedGroups.map(group => [group.id, group.title]));
  const groupOrderById = new Map(orderedGroups.map(group => [group.id, group.order]));

  const topics = manifest.topics
    .map(topic => ({
      ...topic,
      url: `${hubUrl}/${topic.publicSlug}`,
      groupTitle: groupTitleById.get(topic.group) || topic.group,
    }))
    .sort(
      (a, b) =>
        (groupOrderById.get(a.group) || 0) - (groupOrderById.get(b.group) || 0) || a.order - b.order
    );
  const topicsByGroup = new Map();
  topics.forEach(topic => {
    if (!topicsByGroup.has(topic.group)) topicsByGroup.set(topic.group, []);
    topicsByGroup.get(topic.group).push(topic);
  });
  const topicsByRepoPath = new Map(topics.map(topic => [toPosix(topic.path), topic]));
  const topicUrlByTopicId = new Map(topics.map(topic => [topic.topicId, { url: topic.url, title: topic.title }]));

  const graph = buildGraphContext(manifest, hubUrl, topicUrlByTopicId);

  ensureDir(annexTarget);
  copyGraphAssets(graph, topicUrlByTopicId, manifest.website.related || {});

  const droppedMarkers = [];
  const transforms = {
    rewriteLinks: buildLinkRewriter(topicsByRepoPath, hubUrl, loadPlacePageSlugs(), loadPublishedTopicSlugs()),
    replaceMarkers: buildMarkerReplacer(graph.markerById, droppedMarkers),
  };

  writeHubPage(manifest, orderedGroups, topicsByGroup, hubUrl);
  writeTopicPages(manifest, topics, hubUrl, transforms);
  writeEvidencePages(graph, hubUrl);
  writeFindingPages(graph, hubUrl);

  if (droppedMarkers.length) {
    console.warn(
      `G13 package: ${droppedMarkers.length} prose marker(s) not in the public export; Evidence links omitted: ${[...new Set(droppedMarkers)].join(", ")}`
    );
  }
  return {
    enabled: true,
    mode: config.mode,
    hubSlug: manifest.website.hubSlug,
    pages: 1 + topics.length + graph.markersIndex.length + graph.findingsIndex.length,
  };
}

module.exports = { getPackageConfig, syncG13Package };
