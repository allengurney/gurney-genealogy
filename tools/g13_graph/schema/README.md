# G13 graph schema

Files under `migrations/` are the canonical, ordered schema definition. Each
numbered migration is applied once and recorded in `schema_migrations`.

Schema migration is a potentially destructive lifecycle operation. An existing
database is migrated only when its rolling recovery export matches the live
database revision. Schema version 2 adds rebuildable FTS5 indexes and their
revision metadata. FTS tables are derived and excluded from logical recovery
exports; they are rebuilt after restore.
