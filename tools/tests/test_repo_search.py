from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools import repo_search


class RepoSearchUnitTests(unittest.TestCase):
    def test_markdown_parser_attaches_footnote(self) -> None:
        record = repo_search.FileRecord(
            path="research/people/g99-example.md",
            layer="research",
            object_type="person-research",
        )
        text = "# Example\n\nA finding.[^one]\n\n[^one]: Source detail. Source ID: `source-one`.\n"
        sections = repo_search.parse_markdown(record, text)
        self.assertEqual(len(sections), 1)
        self.assertEqual(sections[0].footnote_keys, ["one"])
        self.assertEqual(sections[0].footnotes[0].key, "one")
        self.assertIn("source-one", sections[0].footnotes[0].body)

    def test_daniel_page_marker(self) -> None:
        record = repo_search.FileRecord(
            path="sources/corpus/daniel-gurney-part-2.md",
            layer="sources",
            object_type="corpus",
        )
        sections = repo_search.parse_markdown(record, "## p. 395 (#435)\n\nFilby text.\n")
        self.assertEqual(sections[0].page_marker, "p. 395")

    def test_pagination_preserves_oversize_block(self) -> None:
        blocks = ["A" * 12, "B" * 3]
        pages = repo_search.paginate_blocks(blocks, target=10)
        self.assertEqual(pages[0].strip(), "A" * 12)
        self.assertEqual(pages[1].strip(), "B" * 3)

    def test_staging_keeps_core_and_full_coverage(self) -> None:
        section_core = repo_search.Section(
            path="fact-sheets/g01.md",
            heading="Core",
            heading_path="Core",
            start_line=1,
            end_line=2,
            body="alpha",
            layer="publication",
            object_type="fact-sheet",
        )
        section_full = repo_search.Section(
            path="research/topics/x.md",
            heading="Full",
            heading_path="Full",
            start_line=1,
            end_line=2,
            body="alpha beta",
            layer="research",
            object_type="topic-research",
        )
        results = [
            repo_search.SearchResult(1, section_core, 10, [], [], [], "core", "alpha"),
            repo_search.SearchResult(2, section_full, 9, [], [], [], "supporting", "alpha beta"),
        ]
        staged = repo_search.select_staged_results(results, ["alpha", "beta"], False)
        self.assertEqual([result.result_id for result in staged], [1, 2])

    def test_variant_registry_shape(self) -> None:
        repo_root = repo_search.find_repo_root(Path(__file__).resolve())
        data = json.loads((repo_root / repo_search.VARIANTS_REL).read_text(encoding="utf-8"))
        self.assertEqual(data["schemaVersion"], 1)
        self.assertTrue(any(group["id"] == "surname-gurney" for group in data["variantSets"]))

    def test_external_cache_configuration(self) -> None:
        repo_root = repo_search.find_repo_root(Path(__file__).resolve())
        config = repo_search.load_config(repo_root)
        self.assertNotIn("OneDrive", config["cacheRootResolved"])
        self.assertIn("GitDirs", config["cacheRootResolved"])


if __name__ == "__main__":
    unittest.main()
