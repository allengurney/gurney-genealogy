/*
 * Shared reader-facing projection of the G13 research-graph export (Plan 04).
 * One module, two consumers: the build-time page generator (Node, permanent
 * evidence/finding pages) and the browser evidence drawer. Direction-aware
 * relationship labels and grouping live only here so the two surfaces can
 * never disagree.
 *
 * The module renders HTML strings from the public export JSON. It adds
 * presentation only — it never infers new graph facts. Raw graph IDs stay out
 * of ordinary view; they appear in stable URLs and the collapsed Technical
 * details block.
 */
(function (root, factory) {
  if (typeof module === "object" && module.exports) {
    module.exports = factory();
  } else {
    root.G13GraphRender = factory();
  }
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";

  // Stored relation types → reader labels for each endpoint (Plan 04 §7).
  var RELATIONS = {
    SUPPORTS: { out: "Supports", in: "Supported by", group: "why" },
    CONTRADICTS: { out: "Conflicts with", in: "Conflicts with", group: "qualifications" },
    QUALIFIES: { out: "Qualifies", in: "Qualified by", group: "qualifications" },
    DEPENDS_ON: { out: "Depends on", in: "Required by", group: "why" },
    ELIMINATES: { out: "Rules out", in: "Ruled out by", group: "qualifications" },
    SUPERSEDES: { out: "Replaces", in: "Replaced by", group: "development" },
    CONTEXTUALIZES: { out: "Provides context for", in: "Context from", group: "context" },
    SAME_EVENT_AS: { out: "Same event as", in: "Same event as", group: "context" },
    POTENTIALLY_SAME_PERSON_AS: { out: "Possibly same person as", in: "Possibly same person as", group: "context" },
    DISTINCT_FROM: { out: "Distinct from", in: "Distinct from", group: "context" },
    PUBLISHED_AS: { out: "Published as", in: "Publication of", group: "development" },
    SUMMARIZED_IN: { out: "Summarized in", in: "Summarizes", group: "development" },
    REQUIRES_REVIEW_OF: { out: "Requires review of", in: "Review required by", group: "qualifications" },
    ANALYZES: { out: "Analyzes", in: "Analyzed by", group: "why" },
    SYNTHESIZES: { out: "Synthesizes", in: "Synthesized by", group: "why" },
    WEIGHS: { out: "Weighs", in: "Weighed by", group: "why" },
    INFORMS: { out: "Informs", in: "Informed by", group: "context" },
  };

  var GROUPS = [
    { id: "why", title: "Why this conclusion" },
    { id: "qualifications", title: "Qualifications and conflicts" },
    { id: "development", title: "Development of the conclusion" },
    { id: "context", title: "Related context" },
  ];

  var STRENGTH_ORDER = { strong: 0, moderate: 1, weak: 2, unknown: 3 };

  function escapeHtml(value) {
    return String(value == null ? "" : value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function kindClass(kind) {
    return "g13-kind-" + String(kind || "unknown").replace(/[^a-z_]/gi, "");
  }

  function kindChip(kindLabel, kind) {
    return (
      '<span class="g13-kind ' + kindClass(kind) + '">' + escapeHtml(kindLabel || kind || "Item") + "</span>"
    );
  }

  function titleCase(value) {
    var text = String(value || "");
    return text.charAt(0).toUpperCase() + text.slice(1);
  }

  function findingUrl(id) {
    return "/research/findings/" + String(id).toLowerCase() + "/";
  }

  function markerUrl(id) {
    return "/research/evidence/" + String(id).toLowerCase() + "/";
  }

  // Merge a finding's outgoing + incoming edges into the four reader groups.
  // Every entry names the OTHER item; label is direction-aware.
  function groupRelations(finding) {
    var itemId = finding.id;
    var entries = [];
    var relations = finding.relations || {};
    (relations.outgoing || []).forEach(function (edge) {
      var spec = RELATIONS[edge.type];
      if (!spec) return;
      entries.push({
        otherId: edge.to,
        label: spec.out,
        group: spec.group,
        strength: edge.strength || "unknown",
        explanation: edge.explanation || "",
      });
    });
    (relations.incoming || []).forEach(function (edge) {
      var spec = RELATIONS[edge.type];
      if (!spec) return;
      entries.push({
        otherId: edge.from,
        label: spec.in,
        group: spec.group,
        strength: edge.strength || "unknown",
        explanation: edge.explanation || "",
      });
    });
    // Drop self-loops defensively; sort strongest first within each group.
    entries = entries.filter(function (entry) { return entry.otherId !== itemId; });
    return GROUPS.map(function (group) {
      var groupEntries = entries
        .filter(function (entry) { return entry.group === group.id; })
        .sort(function (a, b) {
          return (STRENGTH_ORDER[a.strength] || 3) - (STRENGTH_ORDER[b.strength] || 3);
        });
      return { id: group.id, title: group.title, entries: groupEntries };
    }).filter(function (group) { return group.entries.length; });
  }

  function relationEntryHtml(entry, ctx) {
    var other = ctx.labelFor(entry.otherId);
    if (!other) return ""; // never render a dead link to a non-public endpoint
    var text = other.shortLabel || other.statement || "Related research item";
    var html =
      '<li class="g13-relation">' +
      '<span class="g13-relation-label">' + escapeHtml(entry.label) + "</span> " +
      kindChip(other.kindLabel, other.kind) + " " +
      '<a class="g13-item-link" data-g13-finding="' + escapeHtml(entry.otherId) + '" href="' +
      escapeHtml(findingUrl(entry.otherId)) + '">' + escapeHtml(text) + "</a>";
    if (entry.explanation) {
      html += '<span class="g13-relation-note">' + escapeHtml(entry.explanation) + "</span>";
    }
    return html + "</li>";
  }

  // Wrap a list, collapsing the tail behind "View all" in compact mode.
  function listHtml(itemsHtml, compact, limit) {
    var visible = itemsHtml;
    var overflow = [];
    if (compact && itemsHtml.length > limit) {
      visible = itemsHtml.slice(0, limit);
      overflow = itemsHtml.slice(limit);
    }
    var html = '<ul class="g13-list">' + visible.join("") + "</ul>";
    if (overflow.length) {
      html +=
        '<details class="g13-view-all"><summary>View all (' +
        (itemsHtml.length) +
        ')</summary><ul class="g13-list">' +
        overflow.join("") +
        "</ul></details>";
    }
    return html;
  }

  function datesHtml(finding) {
    var parts = (finding.dates || [])
      .map(function (date) {
        if (date.display) return date.display;
        var start = date.probableStart || date.plausibleStart;
        var end = date.probableEnd || date.plausibleEnd;
        if (start && end && start !== end) return start + " – " + end;
        return start || end || "";
      })
      .filter(Boolean);
    if (!parts.length) return "";
    return '<p class="g13-dates">Date: ' + escapeHtml(parts.join("; ")) + "</p>";
  }

  function sourcesHtml(finding, ctx, compact) {
    var sources = finding.sources || [];
    if (!sources.length) return "";
    var items = sources.map(function (source) {
      var resolved = ctx.source(source.sourceId) || {};
      var citation = resolved.citation || resolved.shortTitle || source.sourceId;
      var html = '<li class="g13-source">';
      if (resolved.url) {
        html += '<a href="' + escapeHtml(resolved.url) + '" rel="noopener">' + escapeHtml(citation) + "</a>";
      } else {
        html += escapeHtml(citation);
      }
      if (source.locator) html += ", " + escapeHtml(source.locator);
      if (source.excerpt) {
        html += '<blockquote class="g13-excerpt">' + escapeHtml(source.excerpt) + "</blockquote>";
      }
      return html + "</li>";
    });
    return '<section class="g13-section"><h3>Sources</h3>' + listHtml(items, compact, 5) + "</section>";
  }

  function negativeResultHtml(finding) {
    var scope = finding.negativeResult;
    if (!scope) return "";
    var parts = [];
    if (scope.provider || scope.collection) {
      parts.push(
        "<li>Searched: " +
          escapeHtml([scope.provider, scope.collection].filter(Boolean).join(" — ")) +
          "</li>"
      );
    }
    if (scope.dateStart || scope.dateEnd) {
      parts.push("<li>Coverage window: " + escapeHtml([scope.dateStart, scope.dateEnd].filter(Boolean).join(" to ")) + "</li>");
    }
    if (scope.queryDescription) parts.push("<li>Search: " + escapeHtml(scope.queryDescription) + "</li>");
    if (scope.resultsReviewed != null) parts.push("<li>Results reviewed: " + escapeHtml(scope.resultsReviewed) + "</li>");
    if (Array.isArray(scope.limitations) && scope.limitations.length) {
      parts.push("<li>Limitations: " + escapeHtml(scope.limitations.join("; ")) + "</li>");
    }
    if (!parts.length) return "";
    return (
      '<section class="g13-section"><h3>Search scope</h3><ul class="g13-list">' + parts.join("") + "</ul></section>"
    );
  }

  function publicationsHtml(finding, ctx) {
    var publications = finding.publications || [];
    if (!publications.length) return "";
    var items = publications
      .map(function (publication) {
        var target = ctx.publicationUrl(publication.path);
        if (!target) return "";
        var summary = publication.assertionSummary ? " — " + escapeHtml(publication.assertionSummary) : "";
        return (
          '<li><a href="' + escapeHtml(target.url) + '">' + escapeHtml(target.title) + "</a>" + summary + "</li>"
        );
      })
      .filter(Boolean);
    if (!items.length) return "";
    return '<section class="g13-section"><h3>Appears in</h3><ul class="g13-list">' + items.join("") + "</ul></section>";
  }

  function metaLineHtml(finding) {
    var parts = [];
    if (finding.confidence) parts.push("Confidence: " + titleCase(finding.confidence));
    if (finding.status && finding.status !== "active") parts.push("Status: " + titleCase(finding.status));
    if (!parts.length) return "";
    return '<p class="g13-meta">' + escapeHtml(parts.join(" · ")) + "</p>";
  }

  function relationsSectionsHtml(finding, ctx, compact) {
    return groupRelations(finding)
      .map(function (group) {
        var items = group.entries
          .map(function (entry) { return relationEntryHtml(entry, ctx); })
          .filter(Boolean);
        if (!items.length) return "";
        return (
          '<section class="g13-section"><h3>' + escapeHtml(group.title) + "</h3>" +
          listHtml(items, compact, 5) +
          "</section>"
        );
      })
      .filter(Boolean)
      .join("");
  }

  function treatmentLinkHtml(finding, ctx) {
    var unit = finding.unit || {};
    var topic = unit.id ? ctx.topicUrl(unit.id) : null;
    if (!topic) return "";
    return (
      '<p class="g13-treatment"><a href="' + escapeHtml(topic.url) + '">Topic file location: ' +
      escapeHtml(topic.title) + "</a></p>"
    );
  }

  function technicalDetailsHtml(rows) {
    var items = rows
      .filter(function (row) { return row && row[1]; })
      .map(function (row) {
        return "<li>" + escapeHtml(row[0]) + ": <code>" + escapeHtml(row[1]) + "</code></li>";
      });
    if (!items.length) return "";
    return (
      '<details class="g13-technical"><summary>Technical details</summary><ul>' + items.join("") + "</ul></details>"
    );
  }

  // Full treatment of one research item. headingTag: "h1" on the permanent
  // page, "h2" inside the drawer dialog.
  function renderFinding(finding, ctx, opts) {
    opts = opts || {};
    var compact = Boolean(opts.compact);
    var headingTag = opts.headingTag || "h2";
    var heading = finding.shortLabel || finding.statement;
    var html =
      '<div class="g13-finding">' +
      '<p class="g13-chip-row">' + kindChip(finding.kindLabel, finding.kind) + "</p>" +
      "<" + headingTag + ' class="g13-heading">' + escapeHtml(heading) + "</" + headingTag + ">";
    if (finding.shortLabel) {
      html += '<p class="g13-statement">' + escapeHtml(finding.statement) + "</p>";
    }
    if (finding.summary) html += '<p class="g13-summary">' + escapeHtml(finding.summary) + "</p>";
    html += metaLineHtml(finding);
    html += datesHtml(finding);
    html += negativeResultHtml(finding);
    html += relationsSectionsHtml(finding, ctx, compact);
    html += sourcesHtml(finding, ctx, compact);
    html += publicationsHtml(finding, ctx);
    html += treatmentLinkHtml(finding, ctx);
    // Caller-supplied section (e.g. the permanent page's embedded
    // relationship map) between the standard sections and Technical details.
    if (opts.beforeTechnicalHtml) html += opts.beforeTechnicalHtml;
    if (!opts.omitTechnical) {
      html += technicalDetailsHtml([
        ["Research item", finding.id],
        ["Graph revision", opts.revision],
        ["Machine-readable JSON", "/assets/g13-graph/findings/" + finding.id + ".json"],
      ]);
    }
    return html + "</div>";
  }

  // Marker-bundle treatment: primary item first, then any other items the
  // marked passage expresses ("Also covered here"), never a tabbed database.
  function renderMarkerBundle(bundle, ctx, opts) {
    opts = opts || {};
    var primary = bundle.primary;
    var html = renderFinding(primary, ctx, {
      compact: opts.compact,
      headingTag: opts.headingTag,
      omitTechnical: true,
    });
    var others = (bundle.items || []).filter(function (entry) {
      return entry.finding && entry.finding.id !== primary.id;
    });
    if (others.length) {
      var items = others.map(function (entry) {
        var finding = entry.finding;
        var text = finding.shortLabel || finding.statement;
        return (
          '<li class="g13-relation">' + kindChip(finding.kindLabel, finding.kind) + " " +
          '<a class="g13-item-link" data-g13-finding="' + escapeHtml(finding.id) + '" href="' +
          escapeHtml(findingUrl(finding.id)) + '">' + escapeHtml(text) + "</a></li>"
        );
      });
      html +=
        '<section class="g13-section"><h3>Also covered here</h3>' +
        listHtml(items, Boolean(opts.compact), 5) +
        "</section>";
    }
    if (!opts.omitTechnical) {
      html += technicalDetailsHtml([
        ["Evidence marker", bundle.id],
        ["Primary research item", primary.id],
        ["Graph revision", opts.revision],
        ["Machine-readable JSON", "/assets/g13-graph/marker-bundles/" + bundle.id + ".json"],
      ]);
    }
    return html;
  }

  return {
    RELATIONS: RELATIONS,
    GROUPS: GROUPS,
    escapeHtml: escapeHtml,
    kindClass: kindClass,
    findingUrl: findingUrl,
    markerUrl: markerUrl,
    groupRelations: groupRelations,
    renderFinding: renderFinding,
    renderMarkerBundle: renderMarkerBundle,
  };
});
