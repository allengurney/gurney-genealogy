CREATE TABLE schema_migrations (
    version INTEGER PRIMARY KEY CHECK (version > 0),
    name TEXT NOT NULL,
    applied_at TEXT NOT NULL
) STRICT;

CREATE TABLE graph_meta (
    singleton_id INTEGER PRIMARY KEY CHECK (singleton_id = 1),
    schema_version INTEGER NOT NULL CHECK (schema_version > 0),
    database_revision INTEGER NOT NULL DEFAULT 0 CHECK (database_revision >= 0),
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    source_registry_hash TEXT,
    source_registry_synced_at TEXT,
    application_version TEXT NOT NULL
) STRICT;

CREATE TRIGGER graph_meta_revision_monotonic
BEFORE UPDATE OF database_revision ON graph_meta
WHEN NEW.database_revision < OLD.database_revision
BEGIN
    SELECT RAISE(ABORT, 'database_revision cannot decrease');
END;

CREATE TABLE research_units (
    unit_id TEXT PRIMARY KEY,
    path TEXT NOT NULL,
    heading_id TEXT,
    title TEXT NOT NULL,
    scope_summary TEXT,
    content_hash TEXT,
    review_state TEXT NOT NULL DEFAULT 'human_reviewed'
        CHECK (review_state IN ('machine_suggested', 'human_reviewed', 'needs_revision', 'rejected', 'superseded')),
    UNIQUE (path, heading_id)
) STRICT;

CREATE TABLE entities (
    entity_id TEXT PRIMARY KEY,
    entity_type TEXT NOT NULL
        CHECK (entity_type IN ('person', 'place', 'event', 'source', 'record_collection', 'organization', 'ship', 'research_unit', 'publication', 'hypothesis')),
    canonical_label TEXT NOT NULL,
    description TEXT,
    repo_record_id TEXT,
    UNIQUE (entity_type, repo_record_id)
) STRICT;

CREATE TABLE source_registry (
    source_id TEXT PRIMARY KEY,
    display_title TEXT NOT NULL,
    canonical_path TEXT NOT NULL,
    registry_entry_hash TEXT NOT NULL,
    registry_source_path TEXT NOT NULL,
    synchronized_at TEXT NOT NULL
) STRICT;

CREATE TABLE research_items (
    item_id TEXT PRIMARY KEY,
    item_kind TEXT NOT NULL
        CHECK (item_kind IN ('source_evidence', 'research_finding', 'analysis', 'identity_hypothesis', 'negative_result', 'evidence_conflict', 'published_source_statement', 'project_statement', 'open_question')),
    subject_entity_id TEXT REFERENCES entities(entity_id) ON UPDATE CASCADE ON DELETE RESTRICT,
    statement TEXT NOT NULL CHECK (length(trim(statement)) > 0),
    short_label TEXT,
    summary TEXT,
    status TEXT NOT NULL DEFAULT 'active'
        CHECK (status IN ('active', 'open', 'resolved', 'superseded', 'rejected', 'inactive')),
    assessment_confidence_label TEXT,
    assessment_confidence_value REAL
        CHECK (assessment_confidence_value IS NULL OR assessment_confidence_value BETWEEN 0.0 AND 1.0),
    transcription_confidence_value REAL
        CHECK (transcription_confidence_value IS NULL OR transcription_confidence_value BETWEEN 0.0 AND 1.0),
    knowledge_valid_from TEXT,
    knowledge_valid_to TEXT,
    research_unit_id TEXT NOT NULL REFERENCES research_units(unit_id) ON UPDATE CASCADE ON DELETE RESTRICT,
    superseded_by TEXT REFERENCES research_items(item_id) ON UPDATE CASCADE ON DELETE RESTRICT,
    visibility TEXT NOT NULL DEFAULT 'repo_only'
        CHECK (visibility IN ('repo_only', 'public', 'restricted')),
    excerpt_publishable INTEGER NOT NULL DEFAULT 0
        CHECK (excerpt_publishable IN (0, 1)),
    restriction_reason TEXT,
    review_state TEXT NOT NULL DEFAULT 'human_reviewed'
        CHECK (review_state IN ('machine_suggested', 'human_reviewed', 'needs_revision', 'rejected', 'superseded')),
    reviewed_by TEXT,
    reviewed_at TEXT,
    qualifiers_json TEXT NOT NULL DEFAULT '[]' CHECK (json_valid(qualifiers_json)),
    tags_json TEXT NOT NULL DEFAULT '[]' CHECK (json_valid(tags_json)),
    notes TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    revision INTEGER NOT NULL DEFAULT 1 CHECK (revision > 0),
    provenance_origin TEXT NOT NULL
        CHECK (provenance_origin IN ('machine_suggested', 'human_authored', 'seed')),
    CHECK (superseded_by IS NULL OR superseded_by <> item_id),
    CHECK (visibility <> 'restricted' OR restriction_reason IS NOT NULL)
) STRICT;

CREATE TABLE item_dates (
    item_id TEXT NOT NULL REFERENCES research_items(item_id) ON UPDATE CASCADE ON DELETE CASCADE,
    date_role TEXT NOT NULL DEFAULT 'event',
    plausible_start TEXT,
    plausible_end TEXT,
    probable_start TEXT,
    probable_end TEXT,
    precision TEXT NOT NULL
        CHECK (precision IN ('day', 'month', 'year', 'range', 'before', 'after', 'unknown')),
    original_display TEXT,
    calendar TEXT NOT NULL DEFAULT 'normalized-gregorian',
    chronology_key REAL,
    chronology_key_basis TEXT,
    manual_override INTEGER NOT NULL DEFAULT 0 CHECK (manual_override IN (0, 1)),
    PRIMARY KEY (item_id, date_role),
    CHECK (plausible_start IS NULL OR plausible_end IS NULL OR plausible_start <= plausible_end),
    CHECK (probable_start IS NULL OR probable_end IS NULL OR probable_start <= probable_end),
    CHECK (probable_start IS NULL OR plausible_start IS NULL OR probable_start >= plausible_start),
    CHECK (probable_end IS NULL OR plausible_end IS NULL OR probable_end <= plausible_end),
    CHECK (chronology_key IS NULL OR chronology_key_basis IS NOT NULL)
) STRICT;

CREATE TABLE entity_aliases (
    entity_id TEXT NOT NULL REFERENCES entities(entity_id) ON UPDATE CASCADE ON DELETE CASCADE,
    alias TEXT NOT NULL,
    alias_type TEXT NOT NULL DEFAULT 'name',
    source_item_id TEXT REFERENCES research_items(item_id) ON UPDATE CASCADE ON DELETE SET NULL,
    PRIMARY KEY (entity_id, alias, alias_type)
) STRICT;

CREATE TABLE item_entities (
    item_id TEXT NOT NULL REFERENCES research_items(item_id) ON UPDATE CASCADE ON DELETE CASCADE,
    entity_id TEXT NOT NULL REFERENCES entities(entity_id) ON UPDATE CASCADE ON DELETE RESTRICT,
    role TEXT NOT NULL,
    PRIMARY KEY (item_id, entity_id, role)
) STRICT;

CREATE TABLE item_sources (
    item_source_id INTEGER PRIMARY KEY,
    item_id TEXT NOT NULL REFERENCES research_items(item_id) ON UPDATE CASCADE ON DELETE CASCADE,
    source_id TEXT NOT NULL REFERENCES source_registry(source_id) ON UPDATE CASCADE ON DELETE RESTRICT,
    role TEXT NOT NULL
        CHECK (role IN ('supports', 'contradicts', 'qualifies', 'mentions', 'context_for', 'negative_within_scope', 'discovery_only')),
    locator TEXT NOT NULL DEFAULT '',
    evidence_excerpt TEXT,
    excerpt_publishable INTEGER NOT NULL DEFAULT 0 CHECK (excerpt_publishable IN (0, 1)),
    alignment_note TEXT,
    verification_level TEXT,
    UNIQUE (item_id, source_id, role, locator)
) STRICT;

CREATE TABLE item_relations (
    from_item_id TEXT NOT NULL REFERENCES research_items(item_id) ON UPDATE CASCADE ON DELETE CASCADE,
    relation_type TEXT NOT NULL
        CHECK (relation_type IN ('SUPPORTS', 'CONTRADICTS', 'QUALIFIES', 'DEPENDS_ON', 'ELIMINATES', 'SUPERSEDES', 'CONTEXTUALIZES', 'SAME_EVENT_AS', 'POTENTIALLY_SAME_PERSON_AS', 'DISTINCT_FROM', 'PUBLISHED_AS', 'SUMMARIZED_IN', 'REQUIRES_REVIEW_OF', 'ANALYZES', 'SYNTHESIZES', 'WEIGHS', 'INFORMS')),
    to_item_id TEXT NOT NULL REFERENCES research_items(item_id) ON UPDATE CASCADE ON DELETE CASCADE,
    bearing TEXT NOT NULL DEFAULT 'direct'
        CHECK (bearing IN ('direct', 'indirect', 'contextual', 'methodological')),
    strength TEXT NOT NULL DEFAULT 'unknown'
        CHECK (strength IN ('strong', 'moderate', 'weak', 'unknown')),
    explanation TEXT,
    review_state TEXT NOT NULL DEFAULT 'human_reviewed'
        CHECK (review_state IN ('machine_suggested', 'human_reviewed', 'needs_revision', 'rejected', 'superseded')),
    PRIMARY KEY (from_item_id, relation_type, to_item_id),
    CHECK (from_item_id <> to_item_id)
) STRICT;

CREATE TABLE evidence_groups (
    evidence_group_id TEXT PRIMARY KEY,
    research_unit_id TEXT NOT NULL REFERENCES research_units(unit_id) ON UPDATE CASCADE ON DELETE RESTRICT,
    heading_id TEXT,
    paragraph_locator TEXT,
    footnote_locator TEXT,
    alignment TEXT NOT NULL
        CHECK (alignment IN ('collective', 'probable', 'contextual', 'unclear')),
    individual_assignment_resolved INTEGER NOT NULL DEFAULT 0
        CHECK (individual_assignment_resolved IN (0, 1)),
    explanation TEXT
) STRICT;

CREATE TABLE evidence_group_items (
    evidence_group_id TEXT NOT NULL REFERENCES evidence_groups(evidence_group_id) ON UPDATE CASCADE ON DELETE CASCADE,
    item_id TEXT NOT NULL REFERENCES research_items(item_id) ON UPDATE CASCADE ON DELETE CASCADE,
    role TEXT NOT NULL
        CHECK (role IN ('supports', 'contradicts', 'qualifies', 'mentions', 'context_for', 'negative_within_scope', 'discovery_only')),
    PRIMARY KEY (evidence_group_id, item_id, role)
) STRICT;

CREATE TABLE evidence_group_sources (
    evidence_group_id TEXT NOT NULL REFERENCES evidence_groups(evidence_group_id) ON UPDATE CASCADE ON DELETE CASCADE,
    source_id TEXT NOT NULL REFERENCES source_registry(source_id) ON UPDATE CASCADE ON DELETE RESTRICT,
    locator TEXT NOT NULL DEFAULT '',
    role TEXT NOT NULL
        CHECK (role IN ('supports', 'contradicts', 'qualifies', 'mentions', 'context_for', 'negative_within_scope', 'discovery_only')),
    PRIMARY KEY (evidence_group_id, source_id, role, locator)
) STRICT;

CREATE TABLE item_publications (
    publication_id INTEGER PRIMARY KEY,
    item_id TEXT NOT NULL REFERENCES research_items(item_id) ON UPDATE CASCADE ON DELETE CASCADE,
    publication_path TEXT NOT NULL CHECK (length(trim(publication_path)) > 0),
    heading_id TEXT,
    assertion_summary TEXT,
    status TEXT NOT NULL CHECK (status IN ('proposed', 'published', 'retired')),
    visibility TEXT NOT NULL DEFAULT 'repo_only'
        CHECK (visibility IN ('repo_only', 'public', 'restricted')),
    excerpt_publishable INTEGER NOT NULL DEFAULT 0 CHECK (excerpt_publishable IN (0, 1)),
    UNIQUE (item_id, publication_path, heading_id)
) STRICT;

CREATE TABLE negative_result_scope (
    item_id TEXT PRIMARY KEY REFERENCES research_items(item_id) ON UPDATE CASCADE ON DELETE CASCADE,
    provider TEXT NOT NULL CHECK (length(trim(provider)) > 0),
    collection_name TEXT NOT NULL CHECK (length(trim(collection_name)) > 0),
    date_start TEXT,
    date_end TEXT,
    query_description TEXT NOT NULL CHECK (length(trim(query_description)) > 0),
    results_reviewed INTEGER CHECK (results_reviewed IS NULL OR results_reviewed >= 0),
    coverage_confirmed INTEGER NOT NULL DEFAULT 0 CHECK (coverage_confirmed IN (0, 1)),
    limitations_json TEXT NOT NULL
        CHECK (json_valid(limitations_json) AND json_array_length(limitations_json) > 0),
    CHECK (date_start IS NULL OR date_end IS NULL OR date_start <= date_end)
) STRICT;

CREATE TABLE item_revisions (
    revision_id INTEGER PRIMARY KEY,
    database_revision INTEGER NOT NULL CHECK (database_revision > 0),
    item_id TEXT NOT NULL REFERENCES research_items(item_id) ON UPDATE CASCADE ON DELETE RESTRICT,
    changed_at TEXT NOT NULL,
    changed_by TEXT NOT NULL,
    change_kind TEXT NOT NULL
        CHECK (change_kind IN ('create', 'update', 'supersede', 'review', 'delete')),
    field_summary TEXT NOT NULL,
    before_json TEXT,
    after_json TEXT,
    export_snapshot_id TEXT,
    UNIQUE (database_revision, item_id, change_kind)
) STRICT;

CREATE TABLE source_content_hashes (
    source_id TEXT PRIMARY KEY REFERENCES source_registry(source_id) ON UPDATE CASCADE ON DELETE CASCADE,
    content_hash TEXT NOT NULL,
    hashed_at TEXT NOT NULL
) STRICT;

CREATE TABLE build_issues (
    issue_id INTEGER PRIMARY KEY,
    severity TEXT NOT NULL CHECK (severity IN ('error', 'warning')),
    code TEXT NOT NULL,
    record_id TEXT,
    message TEXT NOT NULL,
    detected_at TEXT NOT NULL
) STRICT;

CREATE INDEX research_items_kind_idx ON research_items(item_kind);
CREATE INDEX research_items_unit_idx ON research_items(research_unit_id);
CREATE INDEX item_sources_source_idx ON item_sources(source_id);
CREATE INDEX item_relations_to_idx ON item_relations(to_item_id, relation_type);
CREATE UNIQUE INDEX research_units_location_uq
    ON research_units(path, COALESCE(heading_id, ''));
CREATE UNIQUE INDEX item_publications_location_uq
    ON item_publications(item_id, publication_path, COALESCE(heading_id, ''));
