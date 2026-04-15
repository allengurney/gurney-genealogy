# site/

Eleventy site source. Builds to the public site at genealogy.allengurney.com.

## Currently

Placeholder. The existing Eleventy site is deployed from elsewhere; migration into this folder is deferred until the MCP research workflow is proven over a few sessions.

## Planned structure (once migrated)

```
site/
├── _data/          # Eleventy data files (or symlink to /data/)
├── _includes/      # Nunjucks templates and partials
├── pages/          # Generated ancestor pages, index, about, etc.
├── .eleventy.js    # Eleventy config
└── package.json    # Build dependencies
```

## Relationship to other folders

The site is *generated* from `data/` and `fact-sheets/`. It shouldn't hold canonical facts — those live upstream. Templates read from the data files; fact sheet prose is rendered into ancestor pages.
