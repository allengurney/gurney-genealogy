"""Batch-authoring tests: one-transaction topic increments, dry-run preview,
ID-collision guard, and full rollback on an introduced validation error."""

from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from tools.g13_graph.authoring import author_batch, preview_batch
from tools.g13_graph.config import GraphConfig
from tools.g13_graph.db import connect
from tools.g13_graph.editor import ValidationBlocked
from tools.g13_graph.exporter import export_recovery
from tools.g13_graph.schema_manager import initialize_database
from tools.g13_graph.seed import seed_database
from tools.g13_graph.sources import sync_source_registry
from tools.g13_graph.status import graph_status

FIXTURES = Path(__file__).with_name("fixtures")


class AuthoringTestCase(unittest.TestCase):
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
        initialize_database(self.config)
        export_recovery(self.config)
        sync_source_registry(self.config)
        seed_database(self.config, FIXTURES / "synthetic-seed.ndjson")
        self.base_revision = graph_status(self.config)["database_revision"]

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _source_id(self) -> str:
        conn = connect(self.config.db_path, read_only=True)
        try:
            return conn.execute("SELECT source_id FROM source_registry LIMIT 1").fetchone()[0]
        finally:
            conn.close()

    def _valid_batch(self) -> dict:
        return {
            "units": [{
                "unit_id": "BATCH-UNIT-1",
                "path": "fixture://batch/unit.md",
                "title": "Batch unit",
                "scope_summary": "A synthetic batch unit.",
            }],
            "entities": [{
                "entity_id": "BATCH-ENT-1",
                "entity_type": "person",
                "canonical_label": "Batch Person",
            }],
            "items": [
                {
                    "item": {
                        "item_id": "BATCH-RI-1", "item_kind": "research_finding",
                        "subject_entity_id": "BATCH-ENT-1", "statement": "Finding one.",
                        "short_label": "F1", "research_unit_id": "BATCH-UNIT-1",
                        "assessment_confidence_label": "high",
                    },
                    "entities": [{"entity_id": "BATCH-ENT-1", "role": "subject"}],
                },
                {
                    "item": {
                        "item_id": "BATCH-RI-2", "item_kind": "source_evidence",
                        "subject_entity_id": "BATCH-ENT-1", "statement": "Evidence two.",
                        "short_label": "E2", "research_unit_id": "BATCH-UNIT-1",
                        "assessment_confidence_label": "high",
                    },
                    "sources": [{
                        "source_id": self._source_id(), "role": "supports",
                        "locator": "p. 1", "verification_level": "printed-secondary",
                    }],
                    "entities": [{"entity_id": "BATCH-ENT-1", "role": "subject"}],
                },
            ],
            "relations": [{
                "from_item_id": "BATCH-RI-2", "relation_type": "SUPPORTS",
                "to_item_id": "BATCH-RI-1", "bearing": "direct", "strength": "strong",
                "explanation": "E2 supports F1.",
            }],
        }

    def _shared_from_item_batch(self) -> dict:
        """A batch where one evidence item is the from_item of two SUPPORTS
        relations — the shape that produced two colliding ("update", item_id)
        item_revisions intents before coalescing."""
        return {
            "units": [{
                "unit_id": "BATCH-UNIT-1",
                "path": "fixture://batch/unit.md",
                "title": "Batch unit",
                "scope_summary": "A synthetic batch unit.",
            }],
            "entities": [{
                "entity_id": "BATCH-ENT-1",
                "entity_type": "person",
                "canonical_label": "Batch Person",
            }],
            "items": [
                {
                    "item": {
                        "item_id": "BATCH-RI-1", "item_kind": "research_finding",
                        "subject_entity_id": "BATCH-ENT-1", "statement": "Finding one.",
                        "short_label": "F1", "research_unit_id": "BATCH-UNIT-1",
                        "assessment_confidence_label": "high",
                    },
                    "entities": [{"entity_id": "BATCH-ENT-1", "role": "subject"}],
                },
                {
                    "item": {
                        "item_id": "BATCH-RI-2", "item_kind": "research_finding",
                        "subject_entity_id": "BATCH-ENT-1", "statement": "Finding two.",
                        "short_label": "F2", "research_unit_id": "BATCH-UNIT-1",
                        "assessment_confidence_label": "high",
                    },
                    "entities": [{"entity_id": "BATCH-ENT-1", "role": "subject"}],
                },
                {
                    "item": {
                        "item_id": "BATCH-RI-3", "item_kind": "source_evidence",
                        "subject_entity_id": "BATCH-ENT-1", "statement": "Evidence three.",
                        "short_label": "E3", "research_unit_id": "BATCH-UNIT-1",
                        "assessment_confidence_label": "high",
                    },
                    "sources": [{
                        "source_id": self._source_id(), "role": "supports",
                        "locator": "p. 1", "verification_level": "printed-secondary",
                    }],
                    "entities": [{"entity_id": "BATCH-ENT-1", "role": "subject"}],
                },
            ],
            "relations": [
                {
                    "from_item_id": "BATCH-RI-3", "relation_type": "SUPPORTS",
                    "to_item_id": "BATCH-RI-1", "bearing": "direct", "strength": "strong",
                    "explanation": "E3 supports F1.",
                },
                {
                    "from_item_id": "BATCH-RI-3", "relation_type": "SUPPORTS",
                    "to_item_id": "BATCH-RI-2", "bearing": "direct", "strength": "strong",
                    "explanation": "E3 supports F2.",
                },
            ],
        }

    def _marker_batch(self) -> dict:
        return {
            "units": [{
                "unit_id": "BATCH-MARKER-UNIT",
                "path": "tools/g13_graph/tests/fixtures/batch-marker-unit.md",
                "title": "Synthetic marker batch unit",
            }],
            "items": [{
                "item": {
                    "item_id": "BATCH-MARKER-RI",
                    "item_kind": "research_finding",
                    "statement": "Synthetic marker batch finding.",
                    "short_label": "Marker batch finding",
                    "research_unit_id": "BATCH-MARKER-UNIT",
                    "visibility": "public",
                },
            }],
            "markers": [{
                "marker_id": "G13-PM-000004",
                "research_unit_id": "BATCH-MARKER-UNIT",
                "primary_item_id": "BATCH-MARKER-RI",
                "visibility": "public",
            }],
            "marker_items": [{
                "marker_id": "G13-PM-000004",
                "item_id": "BATCH-MARKER-RI",
                "marker_role": "primary",
                "display_order": 0,
            }],
        }

    def _count(self, table: str, where: str, arg) -> int:
        conn = connect(self.config.db_path, read_only=True)
        try:
            return conn.execute(f"SELECT count(*) FROM {table} WHERE {where}", (arg,)).fetchone()[0]
        finally:
            conn.close()

    # ------------------------------------------------------------------ #
    def test_dry_run_does_not_commit(self) -> None:
        result = preview_batch(self.config, self._valid_batch())
        self.assertTrue(result["can_commit"])
        self.assertEqual(result["would_write_revisions"], 3)  # 2 item creates + 1 relation-add audit row
        self.assertEqual(result["affected_items"], ["BATCH-RI-1", "BATCH-RI-2"])
        # Nothing persisted.
        self.assertEqual(graph_status(self.config)["database_revision"], self.base_revision)
        self.assertEqual(self._count("research_items", "item_id=?", "BATCH-RI-1"), 0)
        self.assertEqual(self._count("research_units", "unit_id=?", "BATCH-UNIT-1"), 0)

    def test_author_batch_commits_atomically(self) -> None:
        result = author_batch(self.config, self._valid_batch(), changed_by="TEST")
        self.assertTrue(result["committed"])
        self.assertFalse(result["stale"])
        self.assertEqual(result["database_revision"], self.base_revision + 1)
        self.assertEqual(result["revisions_written"], 3)
        # Unit, entity, both items, and the relation are present.
        self.assertEqual(self._count("research_units", "unit_id=?", "BATCH-UNIT-1"), 1)
        self.assertEqual(self._count("entities", "entity_id=?", "BATCH-ENT-1"), 1)
        self.assertEqual(self._count("research_items", "research_unit_id=?", "BATCH-UNIT-1"), 2)
        self.assertEqual(self._count("item_relations", "from_item_id=?", "BATCH-RI-2"), 1)
        # item_revisions written for both created items.
        self.assertEqual(self._count("item_revisions", "item_id=?", "BATCH-RI-1"), 1)
        # Recovery export advanced to the committed revision.
        status = graph_status(self.config)
        self.assertEqual(status["recovery_export_revision"], status["database_revision"])
        self.assertFalse(status["database_ahead_of_recovery"])

    def test_markers_load_with_topic_batch_and_write_marker_revision(self) -> None:
        preview = preview_batch(self.config, self._marker_batch())
        self.assertTrue(preview["can_commit"])
        self.assertEqual(preview["affected_markers"], ["G13-PM-000004"])
        self.assertEqual(preview["would_write_revisions"], 2)
        self.assertEqual(
            self._count("prose_markers", "marker_id=?", "G13-PM-000004"),
            0,
        )

        result = author_batch(self.config, self._marker_batch(), changed_by="TEST")
        self.assertEqual(result["affected_markers"], ["G13-PM-000004"])
        self.assertEqual(result["revisions_written"], 2)
        self.assertEqual(
            self._count("prose_markers", "marker_id=?", "G13-PM-000004"),
            1,
        )
        self.assertEqual(
            self._count("prose_marker_items", "marker_id=?", "G13-PM-000004"),
            1,
        )
        self.assertEqual(
            self._count("marker_revisions", "marker_id=?", "G13-PM-000004"),
            1,
        )

    def test_shared_from_item_coalesces_revision_rows(self) -> None:
        # Regression: one item as the from_item of two relations yields two
        # ("update", item_id) revision intents that collide on
        # item_revisions' UNIQUE(database_revision, item_id, change_kind).
        # Dry-run must agree with commit, and the two intents must fold into one row.
        preview = preview_batch(self.config, self._shared_from_item_batch())
        self.assertTrue(preview["can_commit"])
        self.assertEqual(preview["blocking_errors"], [])
        # 3 item creates + 1 coalesced update for the shared from_item.
        self.assertEqual(preview["would_write_revisions"], 4)

        result = author_batch(self.config, self._shared_from_item_batch(), changed_by="TEST")
        self.assertTrue(result["committed"])
        self.assertFalse(result["stale"])
        self.assertEqual(result["revisions_written"], 4)
        revision = result["database_revision"]
        # Both relations landed on the shared from_item.
        self.assertEqual(self._count("item_relations", "from_item_id=?", "BATCH-RI-3"), 2)
        # Exactly one coalesced 'update' row for the shared from_item at this revision
        # (plus its 'create' row — two rows total, no collision).
        conn = connect(self.config.db_path, read_only=True)
        try:
            update_rows = conn.execute(
                "SELECT count(*) FROM item_revisions "
                "WHERE item_id=? AND change_kind='update' AND database_revision=?",
                ("BATCH-RI-3", revision),
            ).fetchone()[0]
            total_rows = conn.execute(
                "SELECT count(*) FROM item_revisions "
                "WHERE item_id=? AND database_revision=?",
                ("BATCH-RI-3", revision),
            ).fetchone()[0]
        finally:
            conn.close()
        self.assertEqual(update_rows, 1)
        self.assertEqual(total_rows, 2)

    def test_reapplying_batch_is_rejected(self) -> None:
        author_batch(self.config, self._valid_batch())
        with self.assertRaises(ValueError) as ctx:
            author_batch(self.config, self._valid_batch())
        self.assertIn("already exist", str(ctx.exception))

    def test_validation_error_rolls_back_whole_batch(self) -> None:
        # A research unit whose path does not resolve is a semantic-validator error
        # (research_location_invalid) rather than a DB CHECK — it exercises the
        # delta-blocking path and must roll back the entire multi-row batch.
        bad = {
            "units": [{
                "unit_id": "BAD-UNIT",
                "path": "research/people/_staging/does-not-exist-xyz.md",
                "title": "Bad",
            }],
            "entities": [{"entity_id": "BAD-ENT", "entity_type": "person", "canonical_label": "x"}],
            "items": [{
                "item": {
                    "item_id": "BAD-RI-1", "item_kind": "research_finding",
                    "subject_entity_id": "BAD-ENT", "statement": "Otherwise valid.",
                    "short_label": "bad", "research_unit_id": "BAD-UNIT",
                    "assessment_confidence_label": "high",
                },
            }],
        }
        with self.assertRaises(ValidationBlocked) as ctx:
            author_batch(self.config, bad)
        self.assertTrue(any(b["code"] == "research_location_invalid" for b in ctx.exception.blocking))
        # Full rollback: unit, entity, and item all absent.
        self.assertEqual(self._count("research_units", "unit_id=?", "BAD-UNIT"), 0)
        self.assertEqual(self._count("entities", "entity_id=?", "BAD-ENT"), 0)
        self.assertEqual(self._count("research_items", "item_id=?", "BAD-RI-1"), 0)
        self.assertEqual(graph_status(self.config)["database_revision"], self.base_revision)


if __name__ == "__main__":
    unittest.main()
