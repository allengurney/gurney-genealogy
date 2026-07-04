CREATE TABLE prose_markers (
    marker_id TEXT PRIMARY KEY,
    research_unit_id TEXT NOT NULL
        REFERENCES research_units(unit_id) ON UPDATE CASCADE ON DELETE RESTRICT,
    primary_item_id TEXT
        REFERENCES research_items(item_id) ON UPDATE CASCADE ON DELETE RESTRICT,
    primary_role TEXT NOT NULL DEFAULT 'primary' CHECK (primary_role = 'primary'),
    visibility TEXT NOT NULL DEFAULT 'repo_only'
        CHECK (visibility IN ('repo_only', 'public', 'restricted')),
    status TEXT NOT NULL DEFAULT 'active'
        CHECK (status IN ('active', 'suppressed', 'retired')),
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    CHECK (status <> 'active' OR primary_item_id IS NOT NULL),
    UNIQUE (marker_id, primary_item_id, primary_role),
    FOREIGN KEY (marker_id, primary_item_id, primary_role)
        REFERENCES prose_marker_items(marker_id, item_id, marker_role)
        ON UPDATE CASCADE ON DELETE RESTRICT
        DEFERRABLE INITIALLY DEFERRED
) STRICT;

CREATE TABLE prose_marker_items (
    marker_id TEXT NOT NULL
        REFERENCES prose_markers(marker_id) ON UPDATE CASCADE ON DELETE CASCADE
        DEFERRABLE INITIALLY DEFERRED,
    item_id TEXT NOT NULL
        REFERENCES research_items(item_id) ON UPDATE CASCADE ON DELETE RESTRICT,
    marker_role TEXT NOT NULL
        CHECK (marker_role IN ('primary', 'expressed', 'contextual')),
    display_order INTEGER NOT NULL CHECK (display_order >= 0),
    cross_unit_reason TEXT,
    cross_unit_reviewed_by TEXT,
    PRIMARY KEY (marker_id, item_id),
    UNIQUE (marker_id, item_id, marker_role),
    UNIQUE (marker_id, display_order),
    CHECK (
        (cross_unit_reason IS NULL AND cross_unit_reviewed_by IS NULL)
        OR (
            length(trim(cross_unit_reason)) > 0
            AND length(trim(cross_unit_reviewed_by)) > 0
        )
    )
) STRICT;

CREATE UNIQUE INDEX prose_marker_one_primary_uq
    ON prose_marker_items(marker_id)
    WHERE marker_role = 'primary';
CREATE INDEX prose_markers_unit_idx
    ON prose_markers(research_unit_id, status, marker_id);
CREATE INDEX prose_marker_items_item_idx
    ON prose_marker_items(item_id, marker_id);

CREATE TABLE marker_revisions (
    revision_id INTEGER PRIMARY KEY,
    marker_id TEXT NOT NULL
        REFERENCES prose_markers(marker_id) ON UPDATE CASCADE ON DELETE RESTRICT,
    database_revision INTEGER NOT NULL CHECK (database_revision > 0),
    changed_at TEXT NOT NULL,
    changed_by TEXT NOT NULL,
    change_kind TEXT NOT NULL
        CHECK (change_kind IN ('create', 'update', 'retire', 'review', 'delete')),
    before_json TEXT CHECK (before_json IS NULL OR json_valid(before_json)),
    after_json TEXT CHECK (after_json IS NULL OR json_valid(after_json)),
    UNIQUE (database_revision, marker_id, change_kind)
) STRICT;
