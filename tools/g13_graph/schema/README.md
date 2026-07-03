# G13 graph schema

Files under `migrations/` are the canonical, ordered schema definition. Each
numbered migration is applied once and recorded in `schema_migrations`.

Schema migration is a potentially destructive lifecycle operation. An existing
database is migrated only when its rolling recovery export matches the live
database revision. The current Phase G0/G1A schema is version 1.
