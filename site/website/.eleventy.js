const markdownIt = require("markdown-it");
const markdownItFootnote = require("markdown-it-footnote");

module.exports = function (eleventyConfig) {

  // Markdown with html blocks enabled (used for image-float-right pattern)
  const md = markdownIt({ html: true, linkify: true, typographer: true })
    .use(markdownItFootnote);
  eleventyConfig.setLibrary("md", md);
  eleventyConfig.addFilter("markdown", value => md.render(value || ""));

  // {% figure "src", "alt", "caption", "cssClass" %}
  // CSS-floated <figure> beside following text.
  // For image+prose in one paragraph, use raw HTML <p class="image-float-right"> in .md.
  eleventyConfig.addShortcode("figure", function (src, alt, caption, cssClass) {
    const cls = cssClass ? ` class="${cssClass}"` : "";
    const cap = caption ? `\n  <figcaption>${caption}</figcaption>` : "";
    return `<figure${cls}>\n  <img src="${src}" alt="${alt}">${cap}\n</figure>`;
  });

  // Pass-through: raw research highlights feed used by the next homepage design.
  eleventyConfig.addPassthroughCopy("research/highlights.md");

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
    "site.webmanifest",
  ].forEach(file => eleventyConfig.addPassthroughCopy(file));
  eleventyConfig.addPassthroughCopy("robots.txt");
  eleventyConfig.addPassthroughCopy("sitemap.xml");
  eleventyConfig.addPassthroughCopy("llms.txt");

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
