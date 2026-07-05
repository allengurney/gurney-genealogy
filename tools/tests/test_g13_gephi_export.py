from __future__ import annotations

import hashlib
import shutil
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

from tools import g13_gephi_export as gephi
from tools.g13_graph.config import GraphConfig
from tools.g13_graph.exporter import export_recovery
from tools.g13_graph.schema_manager import initialize_database
from tools.g13_graph.seed import seed_database
from tools.g13_graph.sources import sync_source_registry


FIXTURES = Path(__file__).resolve().parents[1] / "g13_graph" / "tests" / "fixtures"
NS = {"g": gephi.GEXF_NS}


class GephiExportTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.sources = self.root / "sources.json"
        shutil.copy2(FIXTURES / "sources.json", self.sources)
        self.config = GraphConfig(
            repo_root=Path(__file__).resolve().parents[2],
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

    def _xml(self, view: str) -> tuple[gephi.GraphExport, ET.Element]:
        graph = gephi.build_graph_export(self.config.db_path, view)
        return graph, ET.fromstring(gephi.render_gexf(graph))

    def test_research_flow_contains_only_items_and_explicit_relations(self) -> None:
        graph, root = self._xml("research-flow")
        self.assertTrue(graph.nodes)
        self.assertTrue(graph.edges)
        self.assertEqual(
            {node.attributes["node_type"] for node in graph.nodes},
            {"research_item"},
        )
        self.assertEqual(
            {edge.attributes["edge_class"] for edge in graph.edges},
            {"item_relation"},
        )
        xml_nodes = root.findall(".//g:nodes/g:node", NS)
        xml_edges = root.findall(".//g:edges/g:edge", NS)
        self.assertEqual(len(xml_nodes), len(graph.nodes))
        self.assertEqual(len(xml_edges), len(graph.edges))

    def test_provenance_uses_only_linked_sources_and_has_no_dangling_edges(self) -> None:
        graph, _ = self._xml("provenance")
        node_ids = {node.node_id for node in graph.nodes}
        source_nodes = {
            node.node_id
            for node in graph.nodes
            if node.attributes["node_type"] == "source"
        }
        linked_source_nodes = {
            edge.source
            for edge in graph.edges
            if edge.attributes["edge_class"]
            in {"item_source", "evidence_group_source"}
        }
        self.assertEqual(source_nodes, linked_source_nodes)
        self.assertTrue(source_nodes)
        for edge in graph.edges:
            self.assertIn(edge.source, node_ids)
            self.assertIn(edge.target, node_ids)

    def test_render_is_byte_deterministic_and_uses_no_numeric_weights(self) -> None:
        first = gephi.render_gexf(
            gephi.build_graph_export(self.config.db_path, "provenance")
        )
        second = gephi.render_gexf(
            gephi.build_graph_export(self.config.db_path, "provenance")
        )
        self.assertEqual(first, second)
        self.assertNotIn(b" weight=", first)
        self.assertNotIn(b"<weight", first)

    def test_export_is_read_only_and_writes_revision_stamped_file(self) -> None:
        before = hashlib.sha256(self.config.db_path.read_bytes()).hexdigest()
        result = gephi.export_view(
            self.config.db_path, self.root / "gephi", "research-flow"
        )
        after = hashlib.sha256(self.config.db_path.read_bytes()).hexdigest()
        self.assertEqual(before, after)
        self.assertTrue(result.path.is_file())
        self.assertIn(
            f"r{result.database_revision:06d}",
            result.path.name,
        )
        self.assertEqual(result.path.read_bytes(), gephi.render_gexf(
            gephi.build_graph_export(self.config.db_path, "research-flow")
        ))

    def test_unknown_view_and_missing_database_fail_cleanly(self) -> None:
        with self.assertRaises(gephi.GephiExportError):
            gephi.build_graph_export(self.config.db_path, "unknown")
        with self.assertRaises(gephi.GephiExportError):
            gephi.build_graph_export(self.root / "missing.sqlite", "research-flow")


if __name__ == "__main__":
    unittest.main()
