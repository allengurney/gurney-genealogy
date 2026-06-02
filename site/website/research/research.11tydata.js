module.exports = {
  layout: "layouts/research.njk",
  activeNav: "research",
  bodyClass: "research-page",
  eleventyComputed: {
    title: data => data.title || (data.page && data.page.fileSlug ? data.page.fileSlug.replace(/-/g, " ") : "Research notes"),
    description: data => data.description || "Supplemental Gurney genealogy research notes with source analysis, historical context, open questions, supporting evidence, and related records."
  }
};
