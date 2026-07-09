"""Editor-service tests: transactional save/rollback, revision logging,
validate-before-save, and post-save recovery-export refresh (§14)."""

from __future__ import annotations

import shutil
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools.g13_graph.config import GraphConfig
from tools.g13_graph.db import connect, transaction
from tools.g13_graph.editor import (
    ValidationBlocked,
    commit_change,
    get_item_detail,
    get_marker,
    list_items,
    lookup_ids,
    preview_change,
    review_queue,
)
from tools.g13_graph.lifecycle import PostCommitRefreshError
from tools.g13_graph.queries import get_item
from tools.g13_graph.schema_manager import initialize_database
from tools.g13_graph.seed import seed_database
from tools.g13_graph.exporter import export_recovery
from tools.g13_graph.sources import sync_source_registry
from tools.g13_graph.status import graph_status
from tools.g13_graph.validation import validate_database

FIXTURES = Path(__file__).with_name("fixtures")


class EditorTestCase(unittest.TestCase):
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
        # After init/sync/seed the live DB and recovery export are both at r2.
        self.assertEqual(graph_status(self.config)["database_revision"], 2)
        self.assertEqual(graph_status(self.config)["recovery_export_revision"], 2)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _revision(self) -> int:
        connection = connect(self.config.db_path, read_only=True)
        try:
            return int(
                connection.execute(
                    "SELECT database_revision FROM graph_meta WHERE singleton_id=1"
                ).fetchone()[0]
            )
        finally:
            connection.close()

    def issue_codes(self) -> set[str]:
        return {issue.code for issue in validate_database(self.config, include_recovery=False)}


class SaveSemanticsTests(EditorTestCase):
    def test_commit_writes_revision_refreshes_recovery_and_audits(self) -> None:
        result = commit_change(
            self.config,
            {
                "op": "update_item",
                "params": {
                    "item_id": "TEST-RI-000003",
                    "changes": {"summary": "Edited through the editor service."},
                },
                "changed_by": "TEST",
            },
        )
        self.assertTrue(result["committed"])
        self.assertFalse(result["stale"])
        self.assertEqual(result["database_revision"], 3)
        self.assertEqual(result["affected_items"], ["TEST-RI-000003"])
        # Content edit is visible.
        self.assertEqual(
            get_item(self.config, "TEST-RI-000003")["summary"],
            "Edited through the editor service.",
        )
        # Recovery export advanced with the DB (no unsafe-backup drift).
        status = graph_status(self.config)
        self.assertEqual(status["recovery_export_revision"], 3)
        self.assertFalse(status["database_ahead_of_recovery"])
        # Audit row written in the same revision.
        connection = connect(self.config.db_path, read_only=True)
        try:
            audit = connection.execute(
                """
                SELECT change_kind, field_summary, before_json, after_json, changed_by
                FROM item_revisions
                WHERE database_revision=3 AND item_id='TEST-RI-000003'
                """
            ).fetchone()
        finally:
            connection.close()
        self.assertIsNotNone(audit)
        self.assertEqual(audit["change_kind"], "update")
        self.assertEqual(audit["changed_by"], "TEST")
        self.assertIn("summary", audit["field_summary"] or "")

    def test_validate_before_save_blocks_and_rolls_back(self) -> None:
        # A negative_result item with no scope introduces a new blocking error.
        change = {
            "op": "create_item",
            "params": {
                "item": {
                    "item_kind": "negative_result",
                    "statement": "No qualifying baptism located within the searched scope.",
                    "research_unit_id": "TEST-UNIT-000001",
                    "subject_entity_id": "TEST-ENTITY-000001",
                }
            },
        }
        preview = preview_change(self.config, change)
        self.assertFalse(preview["can_commit"])
        self.assertIn(
            "negative_result_scope_missing",
            {b["code"] for b in preview["blocking_errors"]},
        )
        # Preview never mutates.
        self.assertEqual(self._revision(), 2)

        with self.assertRaises(ValidationBlocked):
            commit_change(self.config, change)
        # Commit rolled back completely: no revision bump, no orphan item.
        self.assertEqual(self._revision(), 2)
        self.assertEqual(self.issue_codes(), {"marker_contextual_one_hop"})

    def test_integrity_error_rolls_back_transaction(self) -> None:
        change = {
            "op": "add_relation",
            "params": {
                "from_item_id": "TEST-RI-000001",
                "relation_type": "SUPPORTS",
                "to_item_id": "TEST-RI-DOES-NOT-EXIST",
            },
        }
        with self.assertRaises(sqlite3.IntegrityError):
            commit_change(self.config, change)
        self.assertEqual(self._revision(), 2)
        connection = connect(self.config.db_path, read_only=True)
        try:
            self.assertIsNone(
                connection.execute(
                    "SELECT 1 FROM item_relations WHERE to_item_id='TEST-RI-DOES-NOT-EXIST'"
                ).fetchone()
            )
        finally:
            connection.close()

    def test_derived_refresh_failure_keeps_edit_and_marks_stale(self) -> None:
        with mock.patch(
            "tools.g13_graph.exporter.atomic_write",
            side_effect=OSError("synthetic export failure"),
        ):
            result = commit_change(
                self.config,
                {
                    "op": "update_item",
                    "params": {
                        "item_id": "TEST-RI-000003",
                        "changes": {"summary": "Committed before synthetic export failure."},
                    },
                },
            )
        # Content edit stands; only the derived export is stale.
        self.assertTrue(result["committed"])
        self.assertTrue(result["stale"])
        self.assertIsNotNone(result["refresh_error"])
        self.assertEqual(self._revision(), 3)
        status = graph_status(self.config)
        self.assertEqual(status["database_revision"], 3)
        self.assertEqual(status["recovery_export_revision"], 2)
        self.assertTrue(status["database_ahead_of_recovery"])


class RoundTripTests(EditorTestCase):
    def test_create_item_with_source_entity_and_relation(self) -> None:
        create = commit_change(
            self.config,
            {
                "op": "create_item",
                "params": {
                    "item": {
                        "item_kind": "research_finding",
                        "statement": "A new editor-authored finding for round-trip testing.",
                        "short_label": "Editor round-trip finding",
                        "research_unit_id": "TEST-UNIT-000001",
                        "subject_entity_id": "TEST-ENTITY-000001",
                        "assessment_confidence_label": "probable",
                    },
                    "sources": [
                        {
                            "source_id": "TEST-SOURCE-000001",
                            "role": "supports",
                            "locator": "p. 5",
                        }
                    ],
                    "entities": [
                        {"entity_id": "TEST-ENTITY-000002", "role": "mentions"}
                    ],
                },
            },
        )
        self.assertTrue(create["committed"])
        new_id = create["affected_items"][0]
        self.assertTrue(new_id.startswith("G13-RI-"))

        relation = commit_change(
            self.config,
            {
                "op": "add_relation",
                "params": {
                    "from_item_id": new_id,
                    "relation_type": "SUPPORTS",
                    # Both ends repo_only — a public target would (correctly) trip
                    # the reused public_relation_visibility_leak validator.
                    "to_item_id": "TEST-RI-000004",
                    "strength": "moderate",
                },
            },
        )
        self.assertTrue(relation["committed"])

        detail = get_item_detail(self.config, new_id)
        self.assertEqual(detail["sources"][0]["source_id"], "TEST-SOURCE-000001")
        self.assertEqual(
            {e["entity_id"] for e in detail["entities"]}, {"TEST-ENTITY-000002"}
        )
        self.assertEqual(detail["outgoing_relations"][0]["to_item_id"], "TEST-RI-000004")
        # The whole graph still validates.
        self.assertEqual(self.issue_codes(), {"marker_contextual_one_hop"})
        # Two audited creates/updates now exist for the new item.
        self.assertTrue(any(r["change_kind"] == "create" for r in detail["revisions"]))

    def test_unregistered_source_is_rejected(self) -> None:
        with self.assertRaises(sqlite3.IntegrityError):
            commit_change(
                self.config,
                {
                    "op": "add_source_link",
                    "params": {
                        "item_id": "TEST-RI-000001",
                        "source_id": "NOT-A-REGISTERED-SOURCE",
                        "role": "supports",
                    },
                },
            )
        self.assertEqual(self._revision(), 2)


class ReviewQueueTests(EditorTestCase):
    def _set_review_fields(
        self,
        item_id: str,
        *,
        review_state: str,
        provenance_origin: str | None = None,
    ) -> None:
        connection = connect(self.config.db_path)
        try:
            with transaction(connection):
                changes = ["review_state=?"]
                args = [review_state]
                if provenance_origin is not None:
                    changes.append("provenance_origin=?")
                    args.append(provenance_origin)
                args.append(item_id)
                connection.execute(
                    f"UPDATE research_items SET {', '.join(changes)} WHERE item_id=?",
                    args,
                )
        finally:
            connection.close()

    def test_batch_accept_clears_review_queue_and_audits(self) -> None:
        self._set_review_fields(
            "TEST-RI-000008",
            review_state="machine_suggested",
            provenance_origin="machine_suggested",
        )
        self._set_review_fields("TEST-RI-000009", review_state="needs_revision")
        self.assertIn("machine_item_unreviewed", self.issue_codes())
        queued = {row["item_id"] for row in review_queue(self.config)["queue"]}
        self.assertEqual(queued, {"TEST-RI-000008", "TEST-RI-000009"})

        result = commit_change(
            self.config,
            {
                "op": "set_review_state",
                "params": {
                    "item_ids": ["TEST-RI-000008", "TEST-RI-000009"],
                    "review_state": "human_reviewed",
                },
                "changed_by": "REVIEWER",
            },
        )
        self.assertTrue(result["committed"])
        self.assertEqual(sorted(result["affected_items"]), ["TEST-RI-000008", "TEST-RI-000009"])
        self.assertEqual(review_queue(self.config)["count"], 0)
        self.assertNotIn("machine_item_unreviewed", self.issue_codes())
        # Each accepted item carries a 'review' audit row.
        connection = connect(self.config.db_path, read_only=True)
        try:
            reviews = connection.execute(
                "SELECT count(*) FROM item_revisions WHERE change_kind='review'"
            ).fetchone()[0]
        finally:
            connection.close()
        self.assertEqual(reviews, 2)

    def test_list_items_filters_by_kind_and_review_state(self) -> None:
        result = list_items(self.config, {"kind": "negative_result"})
        self.assertEqual({i["item_id"] for i in result["items"]}, {"TEST-RI-000005"})
        conflicts = list_items(self.config, {"conflict": "1"})
        self.assertIn("TEST-RI-000006", {i["item_id"] for i in conflicts["items"]})


class MarkerTests(EditorTestCase):
    def test_item_detail_and_list_surface_markers(self) -> None:
        detail = get_item_detail(self.config, "TEST-RI-000001")
        by_marker = {m["marker_id"]: m for m in detail["markers"]}
        self.assertEqual(
            set(by_marker), {"G13-PM-000001", "G13-PM-000003"}
        )
        self.assertEqual(by_marker["G13-PM-000001"]["marker_role"], "primary")
        self.assertEqual(by_marker["G13-PM-000003"]["marker_role"], "contextual")
        self.assertEqual(
            by_marker["G13-PM-000001"]["unit_path"],
            "tools/g13_graph/tests/fixtures/marker-unit-one.md",
        )
        # A pasted marker id in the text filter finds its mapped items.
        result = list_items(self.config, {"q": "G13-PM-000003"})
        self.assertEqual(
            {i["item_id"] for i in result["items"]},
            {"TEST-RI-000001", "TEST-RI-000002", "TEST-RI-000003"},
        )
        self.assertTrue(all("marker_count" in i for i in result["items"]))
        scoped = list_items(self.config, {"marker": "G13-PM-000001"})
        self.assertEqual({i["item_id"] for i in scoped["items"]}, {"TEST-RI-000001"})

    def test_get_marker_read_surface(self) -> None:
        marker = get_marker(self.config, "G13-PM-000003")
        self.assertEqual(marker["token"], "<!-- graph-marker: G13-PM-000003 -->")
        self.assertEqual(
            marker["unit_path"], "tools/g13_graph/tests/fixtures/marker-unit-one.md"
        )
        self.assertEqual(
            [(m["item_id"], m["marker_role"]) for m in marker["items"]],
            [
                ("TEST-RI-000002", "primary"),
                ("TEST-RI-000003", "expressed"),
                ("TEST-RI-000001", "contextual"),
            ],
        )
        self.assertIsNone(get_marker(self.config, "G13-PM-999999"))

    def test_lookup_ids_finds_markers_and_items(self) -> None:
        hits = lookup_ids(self.config, ["G13-PM-000002"])
        self.assertEqual(
            [(h["record_type"], h["record_id"]) for h in hits],
            [("prose_marker", "G13-PM-000002")],
        )
        hits = lookup_ids(self.config, ["TEST-RI-000004"])
        self.assertIn(
            ("research_item", "TEST-RI-000004"),
            {(h["record_type"], h["record_id"]) for h in hits},
        )

    def test_marker_membership_ops_round_trip_with_audit(self) -> None:
        added = commit_change(
            self.config,
            {
                "op": "add_marker_item",
                "params": {
                    "marker_id": "G13-PM-000002",
                    "item_id": "TEST-RI-000005",
                    "marker_role": "expressed",
                },
                "changed_by": "TEST",
            },
        )
        self.assertTrue(added["committed"])
        self.assertEqual(added["affected_markers"], ["G13-PM-000002"])

        promoted = commit_change(
            self.config,
            {
                "op": "set_marker_primary",
                "params": {"marker_id": "G13-PM-000002", "item_id": "TEST-RI-000005"},
                "changed_by": "TEST",
            },
        )
        self.assertTrue(promoted["committed"])
        marker = get_marker(self.config, "G13-PM-000002")
        self.assertEqual(marker["primary_item_id"], "TEST-RI-000005")
        roles = {m["item_id"]: m["marker_role"] for m in marker["items"]}
        self.assertEqual(
            roles, {"TEST-RI-000005": "primary", "TEST-RI-000004": "expressed"}
        )

        removed = commit_change(
            self.config,
            {
                "op": "remove_marker_item",
                "params": {"marker_id": "G13-PM-000002", "item_id": "TEST-RI-000004"},
                "changed_by": "TEST",
            },
        )
        self.assertTrue(removed["committed"])
        marker = get_marker(self.config, "G13-PM-000002")
        self.assertEqual([m["item_id"] for m in marker["items"]], ["TEST-RI-000005"])
        # No new validation issues beyond the pre-existing baseline warning.
        self.assertEqual(self.issue_codes(), {"marker_contextual_one_hop"})
        # Each op wrote a marker_revisions audit row with before/after snapshots.
        connection = connect(self.config.db_path, read_only=True)
        try:
            audits = connection.execute(
                """
                SELECT change_kind, before_json, after_json
                FROM marker_revisions
                WHERE marker_id='G13-PM-000002' AND change_kind='update'
                ORDER BY revision_id
                """
            ).fetchall()
        finally:
            connection.close()
        # Three editor ops → three update audit rows (the seed wrote 'create').
        self.assertEqual(len(audits), 3)
        self.assertTrue(all(a["before_json"] and a["after_json"] for a in audits))

    def test_create_marker_blocked_without_prose_token(self) -> None:
        change = {
            "op": "create_marker",
            "params": {
                "marker": {
                    "research_unit_id": "TEST-UNIT-000001",
                    "primary_item_id": "TEST-RI-000007",
                }
            },
        }
        preview = preview_change(self.config, change)
        self.assertFalse(preview["can_commit"])
        self.assertIn(
            "marker_token_count_invalid",
            {b["code"] for b in preview["blocking_errors"]},
        )
        with self.assertRaises(ValidationBlocked):
            commit_change(self.config, change)
        self.assertEqual(self._revision(), 2)

    def test_create_marker_with_prose_token_commits(self) -> None:
        commit_change(
            self.config,
            {
                "op": "create_research_unit",
                "params": {
                    "unit": {
                        "unit_id": "BATCH-MARKER-UNIT",
                        "path": "tools/g13_graph/tests/fixtures/batch-marker-unit.md",
                        "title": "Editor marker round-trip unit",
                    }
                },
            },
        )
        created_item = commit_change(
            self.config,
            {
                "op": "create_item",
                "params": {
                    "item": {
                        "item_kind": "research_finding",
                        "statement": "Editor-created finding for the marker round trip.",
                        "research_unit_id": "BATCH-MARKER-UNIT",
                    }
                },
            },
        )
        item_id = created_item["affected_items"][0]
        # The fixture file carries the G13-PM-000004 token, so the active
        # marker validates on creation.
        result = commit_change(
            self.config,
            {
                "op": "create_marker",
                "params": {
                    "marker": {
                        "marker_id": "G13-PM-000004",
                        "research_unit_id": "BATCH-MARKER-UNIT",
                        "primary_item_id": item_id,
                    }
                },
                "changed_by": "TEST",
            },
        )
        self.assertTrue(result["committed"])
        self.assertEqual(result["affected_markers"], ["G13-PM-000004"])
        marker = get_marker(self.config, "G13-PM-000004")
        self.assertEqual(marker["primary_item_id"], item_id)
        self.assertEqual(
            [(m["item_id"], m["marker_role"]) for m in marker["items"]],
            [(item_id, "primary")],
        )
        self.assertEqual(marker["revisions"][0]["change_kind"], "create")
        self.assertEqual(self.issue_codes(), {"marker_contextual_one_hop"})

    def test_set_visibility_batch_items_and_markers_one_revision(self) -> None:
        # A partial flip whose relations cross the visibility boundary is
        # blocked by public_relation_visibility_leak — so flip the whole
        # fixture set, which is also the real bulk-publication shape.
        connection = connect(self.config.db_path, read_only=True)
        try:
            item_ids = [
                row["item_id"]
                for row in connection.execute(
                    "SELECT item_id FROM research_items ORDER BY item_id"
                )
            ]
        finally:
            connection.close()
        result = commit_change(
            self.config,
            {
                "op": "set_visibility",
                "params": {
                    "item_ids": item_ids,
                    "marker_ids": ["G13-PM-000002"],
                    "visibility": "public",
                },
                "changed_by": "TEST",
            },
        )
        self.assertTrue(result["committed"])
        self.assertEqual(result["affected_items"], item_ids)
        self.assertEqual(result["affected_markers"], ["G13-PM-000002"])
        self.assertEqual(
            get_item(self.config, "TEST-RI-000003")["visibility"], "public"
        )
        self.assertEqual(get_marker(self.config, "G13-PM-000002")["visibility"], "public")
        # One bulk decision advances the revision once.
        self.assertEqual(self._revision(), 3)

    def test_set_visibility_partial_flip_with_leaking_relation_blocks(self) -> None:
        with self.assertRaises(ValidationBlocked):
            commit_change(
                self.config,
                {
                    "op": "set_visibility",
                    "params": {"item_ids": ["TEST-RI-000004"], "visibility": "public"},
                },
            )
        self.assertEqual(self._revision(), 2)


if __name__ == "__main__":
    unittest.main()
