CREATE VIRTUAL TABLE research_items_fts USING fts5(
    item_id UNINDEXED,
    statement,
    short_label,
    summary,
    qualifiers,
    alignment_notes,
    tokenize='unicode61 remove_diacritics 2'
);

CREATE VIRTUAL TABLE entities_fts USING fts5(
    entity_id UNINDEXED,
    canonical_label,
    description,
    aliases,
    tokenize='unicode61 remove_diacritics 2'
);

CREATE VIRTUAL TABLE research_units_fts USING fts5(
    unit_id UNINDEXED,
    title,
    scope_summary,
    tokenize='unicode61 remove_diacritics 2'
);

CREATE TABLE derived_index_meta (
    index_name TEXT PRIMARY KEY
        CHECK (index_name IN ('research_items_fts', 'entities_fts', 'research_units_fts')),
    database_revision INTEGER NOT NULL CHECK (database_revision >= 0),
    rebuilt_at TEXT NOT NULL,
    row_count INTEGER NOT NULL CHECK (row_count >= 0)
) STRICT;
