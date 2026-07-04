"""Phase G5 static-export tests: public-only items, publishable-only excerpts,
public-only adjacency edges, band-only confidence, and byte-deterministic output.

The publication-safety assertions deliberately inject rows that the semantic
validator would normally reject (a public->non-public edge, a non-publishable
excerpt on a public item, a retired publication) to prove the exporter itself is
the last line of defence and strips them regardless of upstream state.
"""

from __future__ import annotations

import shutil
import sqlite3
import tempfile
import unittest
from pathlib import Path

from tools.g13_graph.config import GraphConfig
from tools.g13_graph.db import connect
from tools.g13_graph.exporter import export_recovery
from tools.g13_graph.schema_manager import initialize_database
from tools.g13_graph.seed import seed_database
from tools.g13_graph.sources import sync_source_registry
from tools.g13_graph.util import canonical_json
from tools.g13_graph.website import build_website_export, export_website

FIXTURES = Path(__file__).with_name("fixtures")


class WebsiteExportTestCase(unittest.TestCase):
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

    def tearDown(self) -> None:
        self.temporary.cleanup()

    # ------------------------------------------------------------------ #
    def _conn(self, read_only: bool = True) -> sqlite3.Connection:
        return connect(self.config.db_path, read_only=read_only)

    def _public_ids(self) -> list[str]:
        conn = self._conn()
        try:
            return [
                r["item_id"]
                for r in conn.execute(
                    "SELECT item_id FROM research_items WHERE visibility='public' ORDER BY item_id"
                )
            ]
        finally:
            conn.close()

    def _build(self) -> dict:
        conn = self._conn()
        try:
            return build_website_export(conn)
        finally:
            conn.close()

    # ------------------------------------------------------------------ #
    def test_only_public_items_exported(self) -> None:
        doc = self._build()
        exported = [f["id"] for f in doc["findings"]]
        self.assertEqual(exported, self._public_ids())
        conn = self._conn()
        try:
            repo_only = [
                r["item_id"]
                for r in conn.execute(
                    "SELECT item_id FROM research_items WHERE visibility<>'public'"
                )
            ]
        finally:
            conn.close()
        for item_id in repo_only:
            self.assertNotIn(item_id, exported)
        # Index mirrors findings; adjacency nodes are exactly the public items.
        self.assertEqual([i["id"] for i in doc["index"]], exported)

    def test_deterministic_build(self) -> None:
        self.assertEqual(canonical_json(self._build()), canonical_json(self._build()))

    def test_confidence_numeric_value_never_leaks(self) -> None:
        target = self._public_ids()[0]
        conn = self._conn(read_only=False)
        try:
            conn.execute(
                "UPDATE research_items SET assessment_confidence_label='high', "
                "assessment_confidence_value=0.987654 WHERE item_id=?",
                (target,),
            )
            conn.commit()
        finally:
            conn.close()
        doc = self._build()
        blob = canonical_json(doc)
        self.assertNotIn("0.987654", blob)
        finding = next(f for f in doc["findings"] if f["id"] == target)
        self.assertEqual(finding["confidence"], "high")

    def test_leaks_are_stripped(self) -> None:
        public = self._public_ids()
        pub_item, repo_item = public[0], None
        conn = self._conn(read_only=False)
        try:
            repo_item = conn.execute(
                "SELECT item_id FROM research_items WHERE visibility='repo_only' LIMIT 1"
            ).fetchone()["item_id"]
            # A restricted item, cloned from an existing row so all columns are valid.
            row = dict(
                conn.execute(
                    "SELECT * FROM research_items WHERE item_id=?", (pub_item,)
                ).fetchone()
            )
            row.update(
                item_id="WEB-RI-REST",
                visibility="restricted",
                short_label="SECRET-RESTRICTED-LABEL",
                statement="SECRET-RESTRICTED-STATEMENT",
                restriction_reason="SECRET-RESTRICTION-REASON",
            )
            cols = list(row)
            conn.execute(
                f'INSERT INTO research_items ({",".join(cols)}) '
                f'VALUES ({",".join("?" for _ in cols)})',
                [row[c] for c in cols],
            )
            # Public -> non-public edges (validator would forbid these).
            for target in (repo_item, "WEB-RI-REST"):
                conn.execute(
                    "INSERT INTO item_relations(from_item_id, relation_type, to_item_id, "
                    "bearing, strength, review_state) VALUES (?, 'SUPPORTS', ?, 'direct', "
                    "'strong', 'human_reviewed')",
                    (pub_item, target),
                )
            # A non-publishable excerpt and a publishable excerpt on the public item.
            src = conn.execute("SELECT source_id FROM source_registry LIMIT 1").fetchone()[0]
            conn.execute(
                "INSERT INTO item_sources(item_id, source_id, role, locator, evidence_excerpt, "
                "excerpt_publishable) VALUES (?, ?, 'mentions', 'loc-a', 'SECRET-EXCERPT', 0)",
                (pub_item, src),
            )
            conn.execute(
                "INSERT INTO item_sources(item_id, source_id, role, locator, evidence_excerpt, "
                "excerpt_publishable) VALUES (?, ?, 'supports', 'loc-b', 'PUBLISHABLE-EXCERPT', 1)",
                (pub_item, src),
            )
            # A published and a retired publication mapping.
            conn.execute(
                "INSERT INTO item_publications(item_id, publication_path, assertion_summary, "
                "status, visibility) VALUES (?, 'AGENTS.md', 'PUB-OK', 'published', 'public')",
                (pub_item,),
            )
            conn.execute(
                "INSERT INTO item_publications(item_id, publication_path, assertion_summary, "
                "status, visibility) VALUES (?, 'README.md', 'SECRET-RETIRED', 'retired', 'public')",
                (pub_item,),
            )
            conn.commit()
        finally:
            conn.close()

        doc = self._build()
        blob = canonical_json(doc)
        # Restricted content and non-publishable/retired content never appear.
        for secret in (
            "SECRET-RESTRICTED-LABEL",
            "SECRET-RESTRICTED-STATEMENT",
            "SECRET-EXCERPT",
            "SECRET-RETIRED",
            "SECRET-RESTRICTION-REASON",
            "WEB-RI-REST",
        ):
            self.assertNotIn(secret, blob)
        # Publishable content does appear.
        self.assertIn("PUBLISHABLE-EXCERPT", blob)
        self.assertIn("PUB-OK", blob)
        # Every adjacency edge connects two public items only.
        public_set = set(self._public_ids())
        for edge in doc["adjacency"]:
            self.assertIn(edge["from"], public_set)
            self.assertIn(edge["to"], public_set)
        self.assertNotIn(repo_item, [f["id"] for f in doc["findings"]])

    def test_export_writes_deterministic_files(self) -> None:
        out = self.root / "site"
        path = export_website(self.config, out)
        self.assertEqual(path, out)
        for name in ("manifest.json", "findings.json", "adjacency.json"):
            self.assertTrue((out / name).is_file(), name)
        for item_id in self._public_ids():
            self.assertTrue((out / "findings" / f"{item_id}.json").is_file(), item_id)
        first = (out / "manifest.json").read_bytes()
        export_website(self.config, out)
        self.assertEqual(first, (out / "manifest.json").read_bytes())
        import json

        manifest = json.loads(first)
        self.assertEqual(manifest["counts"]["public_findings"], len(self._public_ids()))
        self.assertEqual(manifest["format"], "gurney-g13-website")


if __name__ == "__main__":
    unittest.main()
