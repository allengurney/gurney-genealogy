from __future__ import annotations

import json
import shutil
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools.g13_graph.config import DEFAULT_DB, GraphConfig
from tools.g13_graph.db import connect, transaction
from tools.g13_graph.exporter import (
    ExportFormatError,
    build_export,
    export_recovery,
    export_snapshot,
    read_export,
    restore_export,
)
from tools.g13_graph.mutations import update_item
from tools.g13_graph.queries import get_item
from tools.g13_graph.schema_manager import (
    current_schema_version,
    initialize_database,
    migrate_database,
)
from tools.g13_graph.seed import seed_database
from tools.g13_graph.sources import load_source_registry, mirror_state, sync_source_registry
from tools.g13_graph.status import graph_status
from tools.g13_graph.validation import validate_database


FIXTURES = Path(__file__).with_name("fixtures")


class GraphTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.sources = self.root / "sources.json"
        shutil.copy2(FIXTURES / "sources.json", self.sources)
        self.config = GraphConfig(
            repo_root=Path(__file__).resolve().parents[3],
            db_path=self.root / "graph.sqlite",
            export_dir=self.root / "exports",
            sources_path=self.sources,
        )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def initialize(self) -> None:
        initialize_database(self.config)
        export_recovery(self.config)

    def seed(self) -> None:
        self.initialize()
        sync_source_registry(self.config)
        seed_database(self.config, FIXTURES / "synthetic-seed.ndjson")

    def issue_codes(self, *, include_recovery: bool = True) -> set[str]:
        return {
            issue.code
            for issue in validate_database(
                self.config, include_recovery=include_recovery
            )
        }


class SchemaAndTransactionTests(GraphTestCase):
    def test_schema_creation_migration_and_connection_contract(self) -> None:
        self.initialize()
        connection = connect(self.config.db_path)
        try:
            self.assertEqual(current_schema_version(connection), 1)
            self.assertEqual(connection.execute("PRAGMA foreign_keys").fetchone()[0], 1)
            self.assertEqual(connection.execute("PRAGMA journal_mode").fetchone()[0], "wal")
        finally:
            connection.close()
        self.assertEqual(migrate_database(self.config), 0)

    def test_duplicate_and_dangling_ids_are_rejected(self) -> None:
        self.seed()
        connection = connect(self.config.db_path)
        try:
            with self.assertRaises(sqlite3.IntegrityError):
                with transaction(connection):
                    connection.execute(
                        """
                        INSERT INTO research_items
                        SELECT * FROM research_items
                        WHERE item_id='TEST-RI-000001'
                        """
                    )
            with self.assertRaises(sqlite3.IntegrityError):
                with transaction(connection):
                    connection.execute(
                        """
                        INSERT INTO item_relations(
                            from_item_id, relation_type, to_item_id,
                            bearing, strength, review_state
                        ) VALUES (
                            'TEST-RI-000001', 'SUPPORTS', 'TEST-RI-DANGLING',
                            'direct', 'strong', 'human_reviewed'
                        )
                        """
                    )
        finally:
            connection.close()

    def test_seed_rolls_back_complete_batch_on_forced_failure(self) -> None:
        self.initialize()
        sync_source_registry(self.config)
        broken = self.root / "broken-seed.ndjson"
        rows = [
            {
                "table": "research_units",
                "row": {
                    "unit_id": "TEST-UNIT-ROLLBACK",
                    "path": "fixture://rollback",
                    "heading_id": None,
                    "title": "Rollback fixture",
                    "scope_summary": None,
                    "content_hash": None,
                    "review_state": "human_reviewed",
                },
            },
            {
                "table": "research_items",
                "row": {
                    "item_id": "TEST-RI-ROLLBACK",
                    "item_kind": "analysis",
                    "subject_entity_id": "TEST-ENTITY-MISSING",
                    "statement": "This insert must fail.",
                    "research_unit_id": "TEST-UNIT-ROLLBACK",
                    "visibility": "repo_only",
                    "excerpt_publishable": 0,
                    "review_state": "human_reviewed",
                    "created_at": "2026-07-03T00:00:00Z",
                    "updated_at": "2026-07-03T00:00:00Z",
                    "revision": 1,
                    "provenance_origin": "seed",
                },
            },
        ]
        broken.write_text(
            "\n".join(json.dumps(row) for row in rows) + "\n", encoding="utf-8"
        )
        with self.assertRaises(sqlite3.IntegrityError):
            seed_database(self.config, broken, refresh_recovery=False)
        connection = connect(self.config.db_path, read_only=True)
        try:
            self.assertIsNone(
                connection.execute(
                    "SELECT 1 FROM research_units WHERE unit_id='TEST-UNIT-ROLLBACK'"
                ).fetchone()
            )
            self.assertEqual(
                connection.execute(
                    "SELECT database_revision FROM graph_meta"
                ).fetchone()[0],
                1,
            )
        finally:
            connection.close()


class SourceAndRevisionTests(GraphTestCase):
    def test_source_registry_sync_and_stale_hash_detection(self) -> None:
        self.initialize()
        sync_source_registry(self.config)
        connection = connect(self.config.db_path, read_only=True)
        try:
            self.assertEqual(mirror_state(connection, self.sources)["state"], "current")
        finally:
            connection.close()
        registry = json.loads(self.sources.read_text(encoding="utf-8"))
        registry["sources"]["TEST-SOURCE-000001"]["notes"] = "Changed synthetic note."
        self.sources.write_text(
            json.dumps(registry, indent=2) + "\n", encoding="utf-8"
        )
        connection = connect(self.config.db_path, read_only=True)
        try:
            self.assertEqual(mirror_state(connection, self.sources)["state"], "stale")
        finally:
            connection.close()
        self.assertIn("source_registry_stale", self.issue_codes())

    def test_real_source_registry_read_is_read_only_and_parseable(self) -> None:
        real = self.config.repo_root / "data" / "sources.json"
        before = real.stat().st_mtime_ns
        mirror = load_source_registry(real)
        self.assertGreater(len(mirror.rows), 300)
        self.assertEqual(real.stat().st_mtime_ns, before)

    def test_kind_reclassification_preserves_id_relations_and_adds_revision(self) -> None:
        self.seed()
        before = get_item(self.config, "TEST-RI-000003")
        revision = update_item(
            self.config,
            "TEST-RI-000003",
            {"item_kind": "identity_hypothesis"},
            changed_by="TEST",
        )
        after = get_item(self.config, "TEST-RI-000003")
        self.assertEqual(before["item_id"], after["item_id"])
        self.assertEqual(after["item_kind"], "identity_hypothesis")
        self.assertEqual(before["outgoing_relations"], after["outgoing_relations"])
        connection = connect(self.config.db_path, read_only=True)
        try:
            self.assertEqual(revision, 3)
            audit = connection.execute(
                """
                SELECT change_kind, before_json, after_json
                FROM item_revisions
                WHERE database_revision=3 AND item_id='TEST-RI-000003'
                """
            ).fetchone()
            self.assertEqual(audit["change_kind"], "update")
            self.assertEqual(json.loads(audit["before_json"])["item_kind"], "analysis")
            self.assertEqual(
                json.loads(audit["after_json"])["item_kind"], "identity_hypothesis"
            )
        finally:
            connection.close()

    def test_export_failure_leaves_committed_revision_visible_as_unsafe(self) -> None:
        self.seed()
        with mock.patch(
            "tools.g13_graph.exporter._atomic_write",
            side_effect=OSError("synthetic export failure"),
        ):
            with self.assertRaises(OSError):
                update_item(
                    self.config,
                    "TEST-RI-000003",
                    {"summary": "Committed before synthetic export failure."},
                )
        status = graph_status(self.config)
        self.assertEqual(status["database_revision"], 3)
        self.assertEqual(status["recovery_export_revision"], 2)
        self.assertTrue(status["database_ahead_of_recovery"])


class ValidationTests(GraphTestCase):
    def test_clean_fixture_validates_and_basic_query_is_joined(self) -> None:
        self.seed()
        self.assertEqual(self.issue_codes(), set())
        item = get_item(self.config, "TEST-RI-000001")
        self.assertEqual(item["sources"][0]["source_id"], "TEST-SOURCE-000001")
        self.assertEqual(item["entities"][0]["entity_id"], "TEST-ENTITY-000001")

    def test_negative_result_validation(self) -> None:
        self.seed()
        connection = connect(self.config.db_path)
        try:
            with transaction(connection):
                connection.execute(
                    "DELETE FROM negative_result_scope WHERE item_id='TEST-RI-000005'"
                )
        finally:
            connection.close()
        self.assertIn(
            "negative_result_scope_missing",
            self.issue_codes(include_recovery=False),
        )

    def test_date_envelope_validation(self) -> None:
        self.seed()
        connection = connect(self.config.db_path)
        try:
            connection.execute("PRAGMA ignore_check_constraints=ON")
            with transaction(connection):
                connection.execute(
                    """
                    UPDATE item_dates
                    SET probable_start='1890', probable_end='1920',
                        chronology_key_basis=NULL
                    WHERE item_id='TEST-RI-000002'
                    """
                )
        finally:
            connection.close()
        codes = self.issue_codes(include_recovery=False)
        self.assertIn("probable_outside_plausible", codes)
        self.assertIn("chronology_basis_missing", codes)

    def test_public_restricted_relationship_is_rejected_for_export(self) -> None:
        self.seed()
        connection = connect(self.config.db_path)
        try:
            with transaction(connection):
                connection.execute(
                    """
                    UPDATE research_items
                    SET visibility='restricted', restriction_reason='TEST restriction'
                    WHERE item_id='TEST-RI-000004'
                    """
                )
                connection.execute(
                    """
                    INSERT INTO item_relations(
                        from_item_id, relation_type, to_item_id,
                        bearing, strength, explanation, review_state
                    ) VALUES (
                        'TEST-RI-000002', 'DEPENDS_ON', 'TEST-RI-000004',
                        'direct', 'strong', 'Synthetic invalid public edge.',
                        'human_reviewed'
                    )
                    """
                )
        finally:
            connection.close()
        self.assertIn(
            "public_relation_visibility_leak",
            self.issue_codes(include_recovery=False),
        )

    def test_supersession_machine_review_and_excerpt_rules(self) -> None:
        self.seed()
        connection = connect(self.config.db_path)
        try:
            with transaction(connection):
                connection.execute(
                    """
                    UPDATE research_items
                    SET provenance_origin='machine_suggested',
                        review_state='machine_suggested'
                    WHERE item_id='TEST-RI-000009'
                    """
                )
                connection.execute(
                    """
                    UPDATE item_sources
                    SET excerpt_publishable=0
                    WHERE item_id='TEST-RI-000001'
                    """
                )
                connection.execute(
                    """
                    INSERT INTO item_relations(
                        from_item_id, relation_type, to_item_id,
                        bearing, strength, explanation, review_state
                    ) VALUES (
                        'TEST-RI-000004', 'SUPERSEDES', 'TEST-RI-000005',
                        'direct', 'strong', 'Synthetic cycle edge one.',
                        'human_reviewed'
                    )
                    """
                )
                connection.execute(
                    """
                    INSERT INTO item_relations(
                        from_item_id, relation_type, to_item_id,
                        bearing, strength, explanation, review_state
                    ) VALUES (
                        'TEST-RI-000005', 'SUPERSEDES', 'TEST-RI-000004',
                        'direct', 'strong', 'Synthetic cycle edge two.',
                        'human_reviewed'
                    )
                    """
                )
        finally:
            connection.close()
        codes = self.issue_codes(include_recovery=False)
        self.assertIn("machine_item_unreviewed", codes)
        self.assertIn("public_excerpt_not_publishable", codes)
        self.assertIn("supersession_cycle", codes)


class ExportRestoreAndStatusTests(GraphTestCase):
    def test_repeated_exports_are_deterministic_and_atomic(self) -> None:
        self.seed()
        first = export_recovery(self.config).read_bytes()
        self.config.recovery_path.write_text("old\n", encoding="utf-8")
        second_path = export_recovery(self.config)
        self.assertEqual(first, second_path.read_bytes())
        self.assertEqual(list(self.config.export_dir.glob("current.ndjson.tmp-*")), [])
        self.assertEqual(
            read_export(second_path).manifest["logical_content_hash"],
            read_export(second_path).manifest["logical_content_hash"],
        )

    def test_export_restore_round_trip_is_logically_exact(self) -> None:
        self.seed()
        snapshot = export_snapshot(self.config)
        restored = GraphConfig(
            repo_root=self.config.repo_root,
            db_path=self.root / "restored.sqlite",
            export_dir=self.root / "restored-exports",
            sources_path=self.sources,
        )
        self.assertIsNone(restore_export(restored, snapshot))
        restored_export = export_recovery(restored)
        self.assertEqual(snapshot.read_bytes(), restored_export.read_bytes())
        original_connection = connect(self.config.db_path, read_only=True)
        restored_connection = connect(restored.db_path, read_only=True)
        try:
            self.assertEqual(
                build_export(original_connection).manifest["logical_content_hash"],
                build_export(restored_connection).manifest["logical_content_hash"],
            )
        finally:
            original_connection.close()
            restored_connection.close()

    def test_corrupt_or_incomplete_export_is_rejected_without_replacement(self) -> None:
        self.seed()
        original = get_item(self.config, "TEST-RI-000001")
        corrupt = self.root / "corrupt.ndjson"
        corrupt.write_text('{"record_type":"manifest"}\n', encoding="utf-8")
        with self.assertRaises(ExportFormatError):
            restore_export(self.config, corrupt)
        self.assertEqual(get_item(self.config, "TEST-RI-000001"), original)

    def test_restore_refuses_when_recovery_is_stale(self) -> None:
        self.seed()
        snapshot = export_snapshot(self.config)
        update_item(
            self.config,
            "TEST-RI-000003",
            {"summary": "Revision ahead of recovery."},
            refresh_recovery=False,
        )
        with self.assertRaisesRegex(RuntimeError, "recovery export"):
            restore_export(self.config, snapshot)

    def test_status_reports_backup_tiers_ahead_and_behind(self) -> None:
        self.seed()
        snapshot = export_snapshot(self.config)
        update_item(
            self.config,
            "TEST-RI-000003",
            {"summary": "Newer than snapshot."},
        )
        status = graph_status(self.config)
        self.assertEqual(status["recovery_state"], "current")
        self.assertEqual(status["snapshot_state"], "behind")
        self.assertTrue(status["database_ahead_of_snapshot"])
        self.config.recovery_path.write_bytes(snapshot.read_bytes())
        status = graph_status(self.config)
        self.assertEqual(status["recovery_state"], "behind")
        self.assertTrue(status["database_ahead_of_recovery"])

    def test_all_test_state_is_outside_repo_and_durable_default(self) -> None:
        self.seed()
        self.assertNotEqual(self.config.db_path, DEFAULT_DB)
        self.assertTrue(self.config.db_path.is_relative_to(self.root))
        self.assertTrue(self.config.export_dir.is_relative_to(self.root))


if __name__ == "__main__":
    unittest.main()
