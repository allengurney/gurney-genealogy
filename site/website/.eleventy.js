const markdownIt = require("markdown-it");
const markdownItFootnote = require("markdown-it-footnote");

module.exports = function (eleventyConfig) {

  // Markdown with html blocks enabled (used for image-float-right pattern)
  const md = markdownIt({ html: true, linkify: true, typographer: true })
    .use(markdownItFootnote);
  eleventyConfig.setLibrary("md", md);
  eleventyConfig.addFilter("markdown", value => md.render(value || ""));
  eleventyConfig.addFilter("json", value => JSON.stringify(value || ""));
  // De-duplicate a place's ancestorLinks (a place can link the same person
  // under several roles) into a distinct name+generation list for text indexes.
  eleventyConfig.addFilter("uniqueAncestors", links => {
    const out = [];
    const seen = new Set();
    (links || []).forEach(link => {
      const key = `${link.name || ""}|${link.gen || ""}`;
      if (seen.has(key)) return;
      seen.add(key);
      out.push({ name: link.name, gen: link.gen });
    });
    return out;
  });
  eleventyConfig.addFilter("stripFirstMarkdownHeading", value => {
    return String(value || "")
      .replace(/^\s*#\s+.*(?:\r?\n|$)/, "")
      .replace(/^\s*\r?\n/, "");
  });

  // {% figure "src", "alt", "caption", "cssClass" %}
  // CSS-floated <figure> beside following text.
  // For image+prose in one paragraph, use raw HTML <p class="image-float-right"> in .md.
  eleventyConfig.addShortcode("figure", function (src, alt, caption, cssClass) {
    const cls = cssClass ? ` class="${cssClass}"` : "";
    const cap = caption ? `\n  <figcaption>${caption}</figcaption>` : "";
    return `<figure${cls}>\n  <img src="${src}" alt="${alt}">${cap}\n</figure>`;
  });

  // research/highlights.md is a data feed for the homepage (read server-side by
  // _data/researchHighlights.js), not a public page — it is excluded from output
  // via .eleventyignore and is not passthrough-copied.

  // Pass-through: assets, media, favicons, crawler files.
  eleventyConfig.addPassthroughCopy("assets");
  eleventyConfig.addPassthroughCopy("media");
  [
    "android-chrome-192x192.png",
    "android-chrome-512x512.png",
    "apple-touch-icon.png",
    "favicon-128.png",
    "favicon-16.png",
    "favicon-180.png",
    "favicon-192.png",
    "favicon-32.png",
    "favicon-48.png",
    "favicon-512.png",
    "favicon-64.png",
    "favicon.ico",
    "favicon.png",
    "favicon.svg",
    "c92d52678d864c4bb06b70ef3c08f6f8.txt",
    "site.webmanifest",
  ].forEach(file => eleventyConfig.addPassthroughCopy(file));
  eleventyConfig.addPassthroughCopy("robots.txt");

  // Published fact sheets should not expose source-only Research Appendix sections.
  // Authors may retain a Markdown section headed "Research Appendix" in the source file;
  // this transform strips the appendix from rendered HTML under /fact-sheets/.
  eleventyConfig.addTransform("stripFactsheetResearchAppendix", function (content, outputPath) {
    if (!outputPath || !outputPath.endsWith(".html") || !outputPath.replace(/\\/g, "/").includes("/fact-sheets/")) {
      return content;
    }
    return content.replace(/\s*<hr\s*\/?>(?:\s*<h2[^>]*>\s*Research Appendix\s*<\/h2>|\s*<h2[^>]*class="unnumbered"[^>]*>\s*Research Appendix\s*<\/h2>)[\s\S]*?(?=<\/div>\s*<\/div>\s*<\/article>|<\/main>|<footer|<\/body>)/i, "");
  });

  return {
    templateFormats: ["md", "njk"],
    markdownTemplateEngine: "njk",
    dir: {
      input: ".",
      includes: "_includes",
      data: "_data",
      output: "_site",
    },
  };
};
