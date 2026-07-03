"""Stable G0 contracts shared by schema, validation, and export code."""

from __future__ import annotations

SCHEMA_VERSION = 1
APPLICATION_VERSION = "g0-g1a"

ITEM_KINDS = (
    "source_evidence",
    "research_finding",
    "analysis",
    "identity_hypothesis",
    "negative_result",
    "evidence_conflict",
    "published_source_statement",
    "project_statement",
    "open_question",
)

VISIBILITIES = ("repo_only", "public", "restricted")

SOURCE_ROLES = (
    "supports",
    "contradicts",
    "qualifies",
    "mentions",
    "context_for",
    "negative_within_scope",
    "discovery_only",
)

RELATION_TYPES = (
    "SUPPORTS",
    "CONTRADICTS",
    "QUALIFIES",
    "DEPENDS_ON",
    "ELIMINATES",
    "SUPERSEDES",
    "CONTEXTUALIZES",
    "SAME_EVENT_AS",
    "POTENTIALLY_SAME_PERSON_AS",
    "DISTINCT_FROM",
    "PUBLISHED_AS",
    "SUMMARIZED_IN",
    "REQUIRES_REVIEW_OF",
    "ANALYZES",
    "SYNTHESIZES",
    "WEIGHS",
    "INFORMS",
)

LOGICAL_TABLE_ORDER = (
    "graph_meta",
    "research_units",
    "entities",
    "source_registry",
    "research_items",
    "item_dates",
    "entity_aliases",
    "item_entities",
    "item_sources",
    "item_relations",
    "evidence_groups",
    "evidence_group_items",
    "evidence_group_sources",
    "item_publications",
    "negative_result_scope",
    "item_revisions",
    "source_content_hashes",
    "build_issues",
)

SEEDABLE_TABLES = tuple(
    table
    for table in LOGICAL_TABLE_ORDER
    if table not in {"graph_meta", "source_registry", "item_revisions", "build_issues"}
)
