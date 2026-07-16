const fs = require("fs");
const path = require("path");

const projectRoot = path.resolve(__dirname, "..");
const siteDir = path.join(projectRoot, "_site");
const redirectsDir = path.join(projectRoot, "redirects");
const researchCompanionsDir = path.join(projectRoot, "research", "companions");
const siteData = require(path.join(projectRoot, "_data", "site.json"));
const siteUrl = String(siteData.url || "https://genealogy.allengurney.com").replace(/\/$/, "");

const privateOutputPaths = new Set([
  "fact-sheets/featured-ancestors/index.html",
]);

function toPosix(value) {
  return value.replace(/\\/g, "/");
}

function escapeXml(value) {
  return String(value || "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function escapeRegex(value) {
  return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function splitUrlSuffix(value) {
  const match = String(value || "").match(/^([^?#]*)([?#].*)?$/);
  return {
    pathPart: match ? match[1] : value,
    suffix: match && match[2] ? match[2] : "",
  };
}

function normalizeInternalUrl(value) {
  if (!value) return value;
  const raw = String(value);
  const sameOriginPrefix = `${siteUrl}/`;
  let prefix = "";
  let working = raw;

  if (working.startsWith(sameOriginPrefix)) {
    prefix = siteUrl;
    working = working.slice(siteUrl.length);
  } else if (/^[a-z][a-z0-9+.-]*:/i.test(working) || working.startsWith("//")) {
    return raw;
  } else if (!working.startsWith("/")) {
    return raw;
  }

  const { pathPart, suffix } = splitUrlSuffix(working);
  let normalized = pathPart
    .replace(/\/index\.html$/i, "/")
    .replace(/\.html$/i, "");

  if (normalized === "/index") normalized = "/";
  if (!normalized) normalized = "/";

  return `${prefix}${normalized}${suffix}`;
}

function outputPathToPublicPath(relativePath) {
  const rel = toPosix(relativePath);
  if (rel === "index.html") return "/";
  return `/${rel.replace(/\/index\.html$/i, "/").replace(/\.html$/i, "")}`;
}

function outputPathToCanonicalUrl(relativePath) {
  return `${siteUrl}${outputPathToPublicPath(relativePath) === "/" ? "/" : outputPathToPublicPath(relativePath)}`;
}

function publicPathSet(publicHtmlFiles) {
  return new Set(
    publicHtmlFiles.map(file =>
      outputPathToPublicPath(toPosix(path.relative(siteDir, file)))
    )
  );
}

function internalPathFromReference(value, relativePath) {
  const { pathPart, suffix } = splitUrlSuffix(value);
  if (!pathPart) return null;
  if (pathPart.startsWith(`${siteUrl}/`)) {
    return { path: pathPart.slice(siteUrl.length), suffix };
  }
  if (/^[a-z][a-z0-9+.-]*:/i.test(pathPart) || pathPart.startsWith("//")) {
    return null;
  }
  if (pathPart.startsWith("/")) return { path: pathPart, suffix };
  return {
    path: new URL(pathPart, `${siteUrl}/${toPosix(relativePath)}`).pathname,
    suffix,
  };
}

function rewritePublicReference(value, relativePath, publicPaths) {
  const normalized = normalizeInternalUrl(value);
  const reference = internalPathFromReference(normalized, relativePath);
  if (!reference) return { value: normalized, unpublishedMarkdown: false };

  let candidate = null;
  const companion = reference.path.match(/^\/research\/companions\/([^/]+)$/i);
  const personResearch = reference.path.match(/^\/research\/people\/(.+?)\.research\.md$/i);
  const topic = reference.path.match(/^\/research\/topics\/(.+?)\.md$/i);
  const markdown = reference.path.match(/^(.*)\.md$/i);

  if (companion) {
    candidate = `/research/notes/${companionPublicSlug(companion[1])}`;
  } else if (personResearch) {
    candidate = `/research/notes/${companionPublicSlug(personResearch[1])}`;
  } else if (topic) {
    candidate = `/key-research/topics/${topic[1]}`;
  } else if (markdown) {
    candidate = markdown[1] || "/";
  }

  if (candidate && publicPaths.has(candidate)) {
    return { value: `${candidate}${reference.suffix}`, unpublishedMarkdown: false };
  }
  return {
    value: normalized,
    unpublishedMarkdown: Boolean(markdown || personResearch),
  };
}

function walkFiles(dir, predicate, results = []) {
  if (!fs.existsSync(dir)) return results;
  fs.readdirSync(dir, { withFileTypes: true }).forEach(entry => {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      walkFiles(full, predicate, results);
    } else if (!predicate || predicate(full)) {
      results.push(full);
    }
  });
  return results;
}

function removePrivateOutputs() {
  privateOutputPaths.forEach(relativePath => {
    const full = path.join(siteDir, relativePath);
    if (fs.existsSync(full)) {
      fs.rmSync(full, { force: true });
      let parent = path.dirname(full);
      while (parent.startsWith(siteDir) && parent !== siteDir) {
        if (fs.existsSync(parent) && fs.readdirSync(parent).length === 0) {
          fs.rmdirSync(parent);
          parent = path.dirname(parent);
        } else {
          break;
        }
      }
    }
  });
}

function parseRedirectSource(file) {
  const source = fs.readFileSync(file, "utf8");
  const permalink = source.match(/permalink:\s*([^\r\n]+)/i);
  const destination = source.match(/url=([^"']+)/i) || source.match(/location\.replace\(['"]([^'"]+)['"]\)/i);
  if (!permalink || !destination) return null;

  return {
    from: normalizeInternalUrl(permalink[1].trim().replace(/^['"]|['"]$/g, "")),
    to: normalizeInternalUrl(destination[1].trim()),
  };
}

function companionPublicSlug(slug) {
  return slug.replace(/-fact-sheet$/i, "");
}

function addLegacyResearchNoteRedirects(rules) {
  if (!fs.existsSync(researchCompanionsDir)) return;

  fs.readdirSync(researchCompanionsDir)
    .filter(file => file.endsWith(".md"))
    .forEach(file => {
      const slug = file.replace(/\.md$/i, "");
      const oldPath = `/research/companions/${slug}`;
      const newPath = `/research/notes/${companionPublicSlug(slug)}`;
      if (oldPath === newPath) return;
      rules.set(oldPath, newPath);
      rules.set(`${oldPath}.html`, newPath);
    });
}

function buildRedirectRules(publicHtmlFiles) {
  const rules = new Map();

  if (fs.existsSync(redirectsDir)) {
    walkFiles(redirectsDir, file => file.endsWith(".md")).forEach(file => {
      const parsed = parseRedirectSource(file);
      if (!parsed || !parsed.from || !parsed.to || parsed.from === parsed.to) return;
      rules.set(parsed.from, parsed.to);

      const htmlAlias = parsed.from.endsWith(".html") ? parsed.from : `${parsed.from}.html`;
      if (htmlAlias !== parsed.from) rules.set(htmlAlias, parsed.to);
    });
  }

  addLegacyResearchNoteRedirects(rules);

  rules.set("/index.html", "/");

  publicHtmlFiles.forEach(file => {
    const rel = toPosix(path.relative(siteDir, file));
    if (rel === "index.html") return;
    const pathWithHtml = `/${rel}`;
    const canonicalPath = outputPathToPublicPath(rel);
    if (pathWithHtml !== canonicalPath) {
      rules.set(pathWithHtml, canonicalPath);
    }
  });

  return [...rules.entries()]
    .sort((a, b) => a[0].localeCompare(b[0]))
    .map(([from, to]) => `${from} ${to} 301`)
    .join("\n") + "\n";
}

function normalizeHtmlFile(file, publicPaths) {
  const relativePath = toPosix(path.relative(siteDir, file));
  const canonicalUrl = outputPathToCanonicalUrl(relativePath);
  let html = fs.readFileSync(file, "utf8");

  html = html.replace(/\s*<link\b[^>]*\brel=["']canonical["'][^>]*>\s*/gi, "\n");
  html = html.replace(/<\/head>/i, `  <link rel="canonical" href="${canonicalUrl}">\n</head>`);
  html = html.replace(/\b(href)=("([^"]*)"|'([^']*)')/gi, (match, attr, quoted, doubleValue, singleValue) => {
    const value = doubleValue !== undefined ? doubleValue : singleValue;
    const normalized = rewritePublicReference(value, relativePath, publicPaths).value;
    const quote = quoted.startsWith("'") ? "'" : "\"";
    return `${attr}=${quote}${normalized}${quote}`;
  });

  // A research file can cite an internal Markdown artifact that is deliberately
  // not published as a page.  Do not leave a public 404 behind: retain its
  // visible label but remove the unavailable link.  Published places, notes,
  // and opt-in topics were rewritten above to their public canonical routes.
  html = html.replace(/<a\b([^>]*?)\bhref=("([^"]*)"|'([^']*)')([^>]*)>([\s\S]*?)<\/a>/gi,
    (match, before, quoted, doubleValue, singleValue, after, contents) => {
      const value = doubleValue !== undefined ? doubleValue : singleValue;
      const reference = rewritePublicReference(value, relativePath, publicPaths);
      return reference.unpublishedMarkdown ? contents : match;
    });

  fs.writeFileSync(file, html);
}

function titleFromHtml(html, fallback) {
  const match = html.match(/<title>([\s\S]*?)<\/title>/i);
  return match ? match[1].replace(/\s+/g, " ").trim() : fallback;
}

function descriptionFromHtml(html) {
  const match = html.match(/<meta\b[^>]*\bname=["']description["'][^>]*\bcontent=["']([^"']*)["'][^>]*>/i);
  return match ? match[1].replace(/\s+/g, " ").trim() : "";
}

function generateSitemap(publicHtmlFiles) {
  const urls = publicHtmlFiles
    .map(file => outputPathToCanonicalUrl(toPosix(path.relative(siteDir, file))))
    .sort((a, b) => {
      if (a === `${siteUrl}/`) return -1;
      if (b === `${siteUrl}/`) return 1;
      return a.localeCompare(b);
    });

  const body = urls
    .map(url => `  <url>\n    <loc>${escapeXml(url)}</loc>\n  </url>`)
    .join("\n");

  fs.writeFileSync(
    path.join(siteDir, "sitemap.xml"),
    `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${body}\n</urlset>\n`
  );
}

function generateLlmsTxt(publicHtmlFiles) {
  const rows = publicHtmlFiles
    .map(file => {
      const rel = toPosix(path.relative(siteDir, file));
      const html = fs.readFileSync(file, "utf8");
      const title = titleFromHtml(html, rel);
      const description = descriptionFromHtml(html);
      const url = outputPathToCanonicalUrl(rel);
      return { rel, title, description, url };
    })
    .sort((a, b) => {
      if (a.rel === "index.html") return -1;
      if (b.rel === "index.html") return 1;
      return a.rel.localeCompare(b.rel);
    });

  const sections = [
    "# Gurney Genealogy Library",
    "",
    "> A working genealogical research library tracing the direct Gurney line across 37+ generations, from modern America to Viking-age Normandy.",
    "",
    "## Public pages",
    "",
    ...rows.map(row => {
      const note = row.description ? `: ${row.description}` : "";
      return `- [${row.title}](${row.url})${note}`;
    }),
    "",
    "## Crawl guidance",
    "",
    "- Canonical URLs are extensionless and use https://genealogy.allengurney.com.",
    "- The XML sitemap is available at https://genealogy.allengurney.com/sitemap.xml.",
    "- Research pages, fact sheets, place pages, source pages, maps, and catalogs are intended for search and AI crawler discovery unless excluded from the sitemap.",
    "",
  ];

  fs.writeFileSync(path.join(siteDir, "llms.txt"), sections.join("\n"));
}

function validatePublicOutput(publicHtmlFiles) {
  const errors = [];
  const sitemap = fs.readFileSync(path.join(siteDir, "sitemap.xml"), "utf8");
  const sitemapUrls = [...sitemap.matchAll(/<loc>(.*?)<\/loc>/g)].map(match => match[1]);
  const publicUrls = publicHtmlFiles.map(file => outputPathToCanonicalUrl(toPosix(path.relative(siteDir, file))));
  const publicUrlSet = new Set(publicUrls);

  publicHtmlFiles.forEach(file => {
    const rel = toPosix(path.relative(siteDir, file));
    const html = fs.readFileSync(file, "utf8");
    if (/http-equiv=["']refresh["']/i.test(html)) {
      errors.push(`public HTML contains meta refresh redirect: ${rel}`);
    }

    if (/[{][{][\s\S]*?[}][}]|[{]%[\s\S]*?%[}]/.test(html)) {
      errors.push(`public HTML contains unresolved template syntax: ${rel}`);
    }

    const h1Count = (html.match(/<h1\b/gi) || []).length;
    if (h1Count !== 1) {
      errors.push(`public HTML should have exactly one h1: ${rel} has ${h1Count}`);
    }

    const canonicalMatches = [...html.matchAll(/<link\b[^>]*\brel=["']canonical["'][^>]*\bhref=["']([^"']+)["'][^>]*>/gi)];
    if (canonicalMatches.length !== 1) {
      errors.push(`public HTML should have exactly one canonical tag: ${rel}`);
    } else {
      const expected = outputPathToCanonicalUrl(rel);
      const actual = canonicalMatches[0][1];
      if (actual !== expected) errors.push(`canonical mismatch in ${rel}: ${actual} != ${expected}`);
      if (/\.html(?:$|[?#])/.test(actual)) errors.push(`canonical still points at .html URL: ${rel}`);
    }

    const htmlInternalLinks = [...html.matchAll(/\bhref=["']([^"']*\.html(?:[?#][^"']*)?)["']/gi)]
      .map(match => match[1])
      .filter(url => url.startsWith("/") || url.startsWith(`${siteUrl}/`));
    htmlInternalLinks.forEach(url => errors.push(`internal .html link remains in ${rel}: ${url}`));

    const markdownInternalLinks = [...html.matchAll(/\bhref=["']([^"']*\.md(?:[?#][^"']*)?)["']/gi)]
      .map(match => match[1])
      .filter(url =>
        url.startsWith("/") ||
        url.startsWith(`${siteUrl}/`) ||
        !/^[a-z][a-z0-9+.-]*:/i.test(url)
      );
    markdownInternalLinks.forEach(url => errors.push(`internal Markdown link remains in ${rel}: ${url}`));
  });

  sitemapUrls.forEach(url => {
    if (/\.html(?:$|[?#])/.test(url)) errors.push(`sitemap URL still points at .html URL: ${url}`);
    if (!publicUrlSet.has(url)) errors.push(`sitemap URL has no public HTML output: ${url}`);
  });

  publicUrls.forEach(url => {
    if (!sitemapUrls.includes(url)) errors.push(`public page missing from sitemap: ${url}`);
  });

  if (errors.length) {
    console.error("Public indexability validation failed:");
    errors.forEach(error => console.error(`- ${error}`));
    process.exit(1);
  }
}

function finalizeNotFoundPage(file) {
  if (!fs.existsSync(file)) return;
  let html = fs.readFileSync(file, "utf8");
  // Force noindex (the layout emits index,follow) so the error page never
  // competes for indexing.
  if (/<meta\b[^>]*\bname=["']robots["'][^>]*>/i.test(html)) {
    html = html.replace(/<meta\b[^>]*\bname=["']robots["'][^>]*>/i, '<meta name="robots" content="noindex">');
  } else {
    html = html.replace(/<\/head>/i, '  <meta name="robots" content="noindex">\n</head>');
  }
  // Drop the self-canonical the normalizer added; a canonical to a
  // non-existent /404 route is meaningless on an error page.
  html = html.replace(/\s*<link\b[^>]*\brel=["']canonical["'][^>]*>\s*/gi, "\n");
  fs.writeFileSync(file, html);
}

if (!fs.existsSync(siteDir)) {
  console.error("Cannot finalize public site: _site/ does not exist.");
  process.exit(1);
}

removePrivateOutputs();

const notFoundRelPath = "404.html";
const allHtmlFiles = walkFiles(siteDir, file => file.endsWith(".html"))
  .filter(file => !privateOutputPaths.has(toPosix(path.relative(siteDir, file))));
// The 404 page is a real styled page, but it must never be indexed, listed in
// the sitemap/llms.txt, treated as a redirect source, or held to the public
// canonical contract. Cloudflare Pages serves /404.html with a genuine 404
// status for any request that matches no static asset or redirect rule, which
// is what replaces the soft-404 (homepage-with-200) fallback.
const publicHtmlFiles = allHtmlFiles
  .filter(file => toPosix(path.relative(siteDir, file)) !== notFoundRelPath);
const publicPaths = publicPathSet(publicHtmlFiles);

// Normalize every emitted page (including 404) so its internal links are
// rewritten to the extensionless public shape; publicPaths is the link-target
// allowlist. The 404 page is then demoted to noindex with its canonical dropped.
allHtmlFiles.forEach(file => normalizeHtmlFile(file, publicPaths));
finalizeNotFoundPage(path.join(siteDir, notFoundRelPath));

fs.writeFileSync(path.join(siteDir, "_redirects"), buildRedirectRules(publicHtmlFiles));
generateSitemap(publicHtmlFiles);
generateLlmsTxt(publicHtmlFiles);
validatePublicOutput(publicHtmlFiles);

console.log(`Finalized public site: ${publicHtmlFiles.length} public HTML pages, ${path.relative(projectRoot, path.join(siteDir, "sitemap.xml")).replace(/\\/g, "/")}, _redirects, llms.txt, and 404.html.`);
