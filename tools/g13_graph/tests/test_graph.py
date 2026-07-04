from __future__ import annotations

import json
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools.g13_graph.config import DEFAULT_DB, GraphConfig
from tools.g13_graph.context import compile_context
from tools.g13_graph.db import connect, transaction
from tools.g13_graph.drift import capture_source_hashes, source_hash_state
from tools.g13_graph.exporter import (
    ExportFormatError,
    build_export,
    export_recovery,
    export_snapshot,
    read_export,
    restore_export,
)
from tools.g13_graph.mutations import update_item
from tools.g13_graph.indexes import (
    derived_index_state,
    rebuild_database_indexes,
    search_graph,
)
from tools.g13_graph.lifecycle import PostCommitRefreshError
from tools.g13_graph.queries import get_impact, get_item, get_source, get_unit
from tools.g13_graph.report import write_build_report
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
    def _create_schema_one_database(self, config: GraphConfig) -> None:
        connection = connect(config.db_path)
        try:
            sql = (
                Path(__file__).resolve().parents[1]
                / "schema"
                / "migrations"
                / "0001_initial.sql"
            ).read_text(encoding="utf-8")
            connection.executescript("BEGIN IMMEDIATE;\n" + sql)
            connection.execute(
                """
                INSERT INTO schema_migrations(version, name, applied_at)
                VALUES (1, 'initial', '2026-07-03T00:00:00Z')
                """
            )
            connection.execute(
                """
                INSERT INTO graph_meta(
                    singleton_id, schema_version, database_revision,
                    created_at, updated_at, application_version
                ) VALUES (
                    1, 1, 0, '2026-07-03T00:00:00Z',
                    '2026-07-03T00:00:00Z', 'g0-g1a'
                )
                """
            )
            connection.commit()
        except BaseException:
            connection.rollback()
            raise
        finally:
            connection.close()

    def test_schema_creation_migration_and_connection_contract(self) -> None:
        self.initialize()
        connection = connect(self.config.db_path)
        try:
            self.assertEqual(current_schema_version(connection), 2)
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

    def test_schema_one_migration_requires_and_accepts_current_recovery(self) -> None:
        legacy = GraphConfig(
            repo_root=self.config.repo_root,
            db_path=self.root / "legacy.sqlite",
            export_dir=self.root / "legacy-exports",
            sources_path=self.sources,
        )
        self._create_schema_one_database(legacy)
        with self.assertRaisesRegex(RuntimeError, "recovery export"):
            migrate_database(legacy)
        export_recovery(legacy)
        self.assertEqual(migrate_database(legacy), 1)
        connection = connect(legacy.db_path, read_only=True)
        try:
            self.assertEqual(current_schema_version(connection), 2)
            self.assertEqual(derived_index_state(connection)["state"], "current")
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
            "tools.g13_graph.exporter.atomic_write",
            side_effect=OSError("synthetic export failure"),
        ):
            with self.assertRaises(PostCommitRefreshError):
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

    def test_restore_rebuilds_derived_indexes(self) -> None:
        self.seed()
        snapshot = export_snapshot(self.config)
        restored = GraphConfig(
            repo_root=self.config.repo_root,
            db_path=self.root / "indexed-restore.sqlite",
            export_dir=self.root / "indexed-restore-exports",
            sources_path=self.sources,
        )
        restore_export(restored, snapshot)
        connection = connect(restored.db_path, read_only=True)
        try:
            self.assertEqual(derived_index_state(connection)["state"], "current")
        finally:
            connection.close()


class CompletePlumbingTests(GraphTestCase):
    def test_fts_search_and_stale_index_detection(self) -> None:
        self.seed()
        result = search_graph(self.config, ["synthetic", "negative"])
        self.assertIn(
            "TEST-RI-000005",
            {row["record_id"] for row in result["results"]},
        )
        update_item(
            self.config,
            "TEST-RI-000005",
            {"statement": "A changed synthetic negative statement."},
            refresh_recovery=False,
        )
        self.assertIn(
            "derived_indexes_stale",
            self.issue_codes(include_recovery=False),
        )
        rebuild_database_indexes(self.config)
        self.assertNotIn(
            "derived_indexes_stale",
            self.issue_codes(include_recovery=False),
        )

    def test_source_hash_capture_drift_and_review_acceptance(self) -> None:
        artifact = self.root / "synthetic-source.txt"
        artifact.write_text("synthetic source version one\n", encoding="utf-8")
        registry = json.loads(self.sources.read_text(encoding="utf-8"))
        registry["sources"]["TEST-SOURCE-000002"]["corpusPath"] = str(artifact)
        self.sources.write_text(
            json.dumps(registry, indent=2) + "\n", encoding="utf-8"
        )
        self.seed()
        captured = capture_source_hashes(self.config)
        self.assertEqual(captured["captured"], ["TEST-SOURCE-000002"])
        connection = connect(self.config.db_path, read_only=True)
        try:
            self.assertEqual(
                source_hash_state(connection, self.config)["counts"]["current"], 1
            )
        finally:
            connection.close()
        artifact.write_text("synthetic source version two\n", encoding="utf-8")
        self.assertIn("source_content_drift", self.issue_codes())
        accepted = capture_source_hashes(
            self.config,
            source_ids=["TEST-SOURCE-000002"],
            replace=True,
            changed_by="TEST-REVIEWER",
        )
        self.assertEqual(accepted["captured"], ["TEST-SOURCE-000002"])
        self.assertNotIn("source_content_drift", self.issue_codes())
        connection = connect(self.config.db_path, read_only=True)
        try:
            review = connection.execute(
                """
                SELECT * FROM item_revisions
                WHERE item_id='TEST-RI-000007' AND change_kind='review'
                ORDER BY revision_id DESC LIMIT 1
                """
            ).fetchone()
            self.assertIsNotNone(review)
        finally:
            connection.close()

    def test_build_report_is_deterministic(self) -> None:
        self.seed()
        first = self.root / "report-one.json"
        second = self.root / "report-two.json"
        write_build_report(self.config, first)
        write_build_report(self.config, second)
        self.assertEqual(first.read_bytes(), second.read_bytes())
        report = json.loads(first.read_text(encoding="utf-8"))
        self.assertEqual(report["schema_version"], 2)
        self.assertEqual(
            report["research_items"]["by_kind"]["negative_result"], 1
        )
        self.assertEqual(report["derived_indexes"]["state"], "current")

    def test_basic_source_unit_and_impact_queries(self) -> None:
        self.seed()
        source = get_source(self.config, "TEST-SOURCE-000001")
        self.assertEqual(source["items"][0]["item_id"], "TEST-RI-000001")
        unit = get_unit(self.config, "TEST-UNIT-000001")
        self.assertGreaterEqual(len(unit["items"]), 1)
        impact = get_impact(self.config, "TEST-RI-000002")
        self.assertEqual(impact["scope"], "direct-only")
        self.assertIn(
            "TEST-RI-000001",
            {
                relation["related_item_id"]
                for relation in impact["direct_relations"]
            },
        )


class ContextCompilerTests(GraphTestCase):
    def test_seed_expands_one_hop_and_reports_ledger(self) -> None:
        self.seed()
        package = compile_context(self.config, ids=["TEST-RI-000002"])
        included = {item["item_id"] for item in package["items"]}
        # One incoming hop pulls the support/inform/qualify neighbours.
        self.assertEqual(
            included,
            {"TEST-RI-000002", "TEST-RI-000001", "TEST-RI-000003", "TEST-RI-000007"},
        )
        ledger = package["coverage_ledger"]
        self.assertEqual(ledger["seed_matched"], ["TEST-RI-000002"])
        self.assertIn("TEST-RI-000001", ledger["expanded"])
        # 'active' and 'open' items are considered; nothing else exists here.
        self.assertEqual(ledger["considered_active_items"], 9)

    def test_term_match_is_conjunctive(self) -> None:
        self.seed()
        package = compile_context(self.config, terms=["synthetic", "negative"])
        self.assertIn(
            "TEST-RI-000005",
            {item["item_id"] for item in package["items"]},
        )

    def test_budget_never_drops_ids_and_protects_negative_scope(self) -> None:
        self.seed()
        package = compile_context(self.config, ids=["TEST-RI-000005"], budget=200)
        ledger = package["coverage_ledger"]
        # Budget is unreachable at this size, but ids/short statements survive.
        self.assertFalse(ledger["within_budget"])
        self.assertTrue(ledger["omitted_detail"])
        self.assertIn("TEST-RI-000005", {i["item_id"] for i in package["items"]})
        negative = next(
            i for i in package["items"] if i["item_id"] == "TEST-RI-000005"
        )
        # Negative-result limitations are structural and never shed for budget.
        self.assertIn("negative_result_scope", negative)
        self.assertTrue(negative["negative_result_scope"]["limitations"])

    def test_research_mode_expands_two_hops_but_grounding_stops_at_one(self) -> None:
        self.seed()
        connection = connect(self.config.db_path)
        try:
            with transaction(connection):
                connection.execute(
                    """
                    INSERT INTO item_relations(
                        from_item_id, relation_type, to_item_id, bearing,
                        strength, explanation, review_state
                    ) VALUES (
                        'TEST-RI-000002', 'SUMMARIZED_IN', 'TEST-RI-000008',
                        'direct', 'strong', 'Synthetic first hop.',
                        'human_reviewed'
                    )
                    """
                )
                connection.execute(
                    """
                    INSERT INTO item_relations(
                        from_item_id, relation_type, to_item_id, bearing,
                        strength, explanation, review_state
                    ) VALUES (
                        'TEST-RI-000008', 'REQUIRES_REVIEW_OF',
                        'TEST-RI-000009', 'direct', 'strong',
                        'Synthetic second hop.', 'human_reviewed'
                    )
                    """
                )
        finally:
            connection.close()
        grounding = compile_context(
            self.config, ids=["TEST-RI-000002"], mode="grounding"
        )
        research = compile_context(
            self.config, ids=["TEST-RI-000002"], mode="research"
        )
        grounding_ids = {item["item_id"] for item in grounding["items"]}
        research_ids = {item["item_id"] for item in research["items"]}
        self.assertIn("TEST-RI-000008", grounding_ids)
        self.assertNotIn("TEST-RI-000009", grounding_ids)
        self.assertIn("TEST-RI-000009", research_ids)
        self.assertEqual(
            research["coverage_ledger"]["expanded"]["TEST-RI-000009"]["distance"],
            2,
        )

    def test_relation_filter_controls_expansion_and_output(self) -> None:
        self.seed()
        package = compile_context(
            self.config,
            ids=["TEST-RI-000002"],
            relation_types=["supports"],
        )
        self.assertEqual(
            {item["item_id"] for item in package["items"]},
            {"TEST-RI-000001", "TEST-RI-000002"},
        )
        self.assertEqual(package["query"]["relation_types"], ["SUPPORTS"])
        self.assertTrue(
            all(
                relation["relation_type"] == "SUPPORTS"
                for item in package["items"]
                for relation in item["relations"]
            )
        )

    def test_rejected_relation_does_not_expand_context(self) -> None:
        self.seed()
        connection = connect(self.config.db_path)
        try:
            with transaction(connection):
                connection.execute(
                    """
                    INSERT INTO item_relations(
                        from_item_id, relation_type, to_item_id, bearing,
                        strength, explanation, review_state
                    ) VALUES (
                        'TEST-RI-000008', 'PUBLISHED_AS', 'TEST-RI-000002',
                        'direct', 'strong', 'Rejected synthetic edge.',
                        'rejected'
                    )
                    """
                )
        finally:
            connection.close()
        package = compile_context(self.config, ids=["TEST-RI-000002"])
        self.assertNotIn(
            "TEST-RI-000008",
            {item["item_id"] for item in package["items"]},
        )

    def test_exhaustive_mode_accounts_for_every_active_item(self) -> None:
        self.seed()
        package = compile_context(self.config, mode="exhaustive")
        ledger = package["coverage_ledger"]
        self.assertEqual(
            set(ledger["considered"]["item_ids"]),
            {item["item_id"] for item in package["items"]},
        )
        self.assertEqual(ledger["omitted"], [])
        self.assertEqual(ledger["included_total"], 9)

    def test_coverage_ledger_accounts_for_items_outside_subgraph(self) -> None:
        self.seed()
        package = compile_context(self.config, ids=["TEST-RI-000002"])
        ledger = package["coverage_ledger"]
        accounted = set(ledger["included_compactly"]) | {
            row["item_id"] for row in ledger["omitted"]
        }
        self.assertEqual(accounted, set(ledger["considered"]["item_ids"]))
        self.assertTrue(
            all(
                row["reason"] == "outside_grounding_subgraph"
                for row in ledger["omitted"]
            )
        )

    def test_entity_seed_and_unresolved_inputs_are_reported(self) -> None:
        self.seed()
        connection = connect(self.config.db_path)
        try:
            with transaction(connection):
                connection.execute(
                    """
                    UPDATE research_items SET status='inactive'
                    WHERE item_id='TEST-RI-000009'
                    """
                )
        finally:
            connection.close()
        package = compile_context(
            self.config,
            entity_ids=["TEST-ENTITY-000002", "TEST-ENTITY-MISSING"],
            ids=["TEST-RI-MISSING", "TEST-RI-000009"],
        )
        ledger = package["coverage_ledger"]
        self.assertIn("TEST-RI-000001", ledger["seed_matched"])
        self.assertEqual(
            ledger["unresolved_inputs"]["missing_item_ids"],
            ["TEST-RI-MISSING"],
        )
        self.assertEqual(
            ledger["unresolved_inputs"]["missing_entity_ids"],
            ["TEST-ENTITY-MISSING"],
        )
        self.assertEqual(
            ledger["unresolved_inputs"]["inactive_item_ids"],
            ["TEST-RI-000009"],
        )

    def test_review_warning_and_protected_conflict_survive_budget(self) -> None:
        self.seed()
        connection = connect(self.config.db_path)
        try:
            with transaction(connection):
                connection.execute(
                    """
                    UPDATE research_items SET review_state='needs_revision'
                    WHERE item_id='TEST-RI-000006'
                    """
                )
        finally:
            connection.close()
        package = compile_context(
            self.config,
            ids=["TEST-RI-000004"],
            mode="research",
            budget=200,
        )
        self.assertFalse(package["coverage_ledger"]["within_budget"])
        conflict = next(
            item
            for item in package["items"]
            if item["item_id"] == "TEST-RI-000006"
        )
        self.assertIn("statement", conflict)
        self.assertEqual(conflict["review_state"], "needs_revision")
        self.assertIn(
            "item_review_needed",
            {warning["code"] for warning in package["warnings"]},
        )

    def test_invalid_mode_relation_and_budget_are_rejected(self) -> None:
        self.seed()
        with self.assertRaises(ValueError):
            compile_context(self.config, mode="unknown")
        with self.assertRaises(ValueError):
            compile_context(self.config, relation_types=["NOT_A_RELATION"])
        with self.assertRaises(ValueError):
            compile_context(self.config, budget=0)


class CliSmokeTests(GraphTestCase):
    def test_complete_g2_cli_lifecycle(self) -> None:
        script = self.config.repo_root / "tools" / "g13_graph.py"

        def run(
            *arguments: str,
            db: Path | None = None,
            exports: Path | None = None,
        ) -> dict:
            completed = subprocess.run(
                [
                    sys.executable,
                    str(script),
                    "--db",
                    str(db or self.config.db_path),
                    "--export-dir",
                    str(exports or self.config.export_dir),
                    "--sources",
                    str(self.sources),
                    *arguments,
                ],
                cwd=self.config.repo_root,
                check=False,
                capture_output=True,
                text=True,
                encoding="utf-8",
            )
            self.assertEqual(
                completed.returncode,
                0,
                msg=f"{completed.stdout}\n{completed.stderr}",
            )
            return json.loads(completed.stdout)

        run("init")
        run("migrate")
        run("sync-sources")
        run("seed", "--file", str(FIXTURES / "synthetic-seed.ndjson"))
        run("validate")
        run("search", "--terms", "synthetic", "negative")
        run("source", "TEST-SOURCE-000001")
        run("unit", "TEST-UNIT-000001")
        run("impact", "TEST-RI-000002")
        context = run(
            "context",
            "--ids",
            "TEST-RI-000002",
            "--mode",
            "research",
            "--relation-types",
            "SUPPORTS",
        )
        self.assertEqual(context["query"]["mode"], "research")
        run("hash-sources")
        report = self.root / "cli-report.json"
        run("report", "--output", str(report))
        self.assertTrue(report.is_file())
        snapshot = Path(run("export", "--snapshot")["export"])
        restored_db = self.root / "cli-restored.sqlite"
        restored_exports = self.root / "cli-restored-exports"
        run(
            "restore",
            "--from",
            str(snapshot),
            db=restored_db,
            exports=restored_exports,
        )
        status = run("status", db=restored_db, exports=restored_exports)
        self.assertEqual(status["schema_version"], 2)
        self.assertEqual(status["derived_index_state"], "current")


if __name__ == "__main__":
    unittest.main()
