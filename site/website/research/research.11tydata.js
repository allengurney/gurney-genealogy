module.exports = {
  layout: "layouts/research.njk",
  activeNav: "research",
  bodyClass: "research-page",
  eleventyComputed: {
    title: data => data.title || (data.page && data.page.fileSlug ? data.page.fileSlug.replace(/-/g, " ") : "Research companion"),
    description: data => data.description || "Supplemental Gurney genealogy research companion."
  }
};
