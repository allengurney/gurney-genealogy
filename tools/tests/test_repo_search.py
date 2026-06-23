from __future__ import annotations

import json
import re
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
        self.assertEqual(data["schemaVersion"], 2)
        self.assertEqual(
            [group["id"] for group in data["nameVariantFamilies"]],
            ["modern", "english", "norman"],
        )

    def test_auto_family_selection_uses_ancestor_generation(self) -> None:
        repo_root = repo_search.find_repo_root(Path(__file__).resolve())
        entity = repo_search.Entity(
            kind="ancestor",
            id="ancestor-g32-gerard-de-gournay",
            label="Gerard de Gournay",
            generation="G32",
        )
        specs, expansions, selection = repo_search.expand_variants(
            repo_root,
            [],
            "conservative",
            "auto",
            entity,
        )
        self.assertEqual(selection["selected"], "norman")
        self.assertTrue(selection["inferred"])
        self.assertIn("Gerard de Gournay", [spec.term for spec in specs])
        self.assertTrue(any(item["family"] == "norman" for item in expansions))

    def test_raw_auto_search_does_not_expand_name_variants(self) -> None:
        repo_root = repo_search.find_repo_root(Path(__file__).resolve())
        specs, expansions, selection = repo_search.expand_variants(
            repo_root,
            ["Gurney"],
            "broad",
            "auto",
        )
        self.assertEqual([spec.term for spec in specs], ["Gurney"])
        self.assertEqual(expansions, [])
        self.assertEqual(selection["selected"], "none")

    def test_broad_family_is_cumulative_and_warns_on_collisions(self) -> None:
        repo_root = repo_search.find_repo_root(Path(__file__).resolve())
        specs, _expansions, selection = repo_search.expand_variants(
            repo_root,
            ["John Gurney"],
            "broad",
            "modern",
        )
        terms = {spec.term for spec in specs}
        self.assertEqual(selection["selected"], "modern")
        self.assertIn("John Gurnay", terms)
        self.assertIn("John Gurnoe", terms)
        gurnoe = next(spec for spec in specs if spec.term == "John Gurnoe")
        self.assertTrue(gurnoe.collision_warning)
        self.assertEqual(gurnoe.match_mode, "whole-token")

    def test_source_specific_ocr_expansion_retains_path_scope(self) -> None:
        repo_root = repo_search.find_repo_root(Path(__file__).resolve())
        specs, _expansions, _selection = repo_search.expand_variants(
            repo_root,
            ["William"],
            "broad",
            "none",
        )
        wilham = next(spec for spec in specs if spec.term == "Wilham")
        self.assertEqual(wilham.origin, "source-specific-ocr")
        self.assertTrue(wilham.source_paths)
        self.assertTrue(all("daniel-gurney-part-" in path for path in wilham.source_paths))
        self.assertTrue(repo_search.spec_applies_to_path(wilham, wilham.source_paths[0]))
        self.assertFalse(repo_search.spec_applies_to_path(wilham, "AGENTS.md"))

    def test_whole_token_pattern_does_not_match_longer_name(self) -> None:
        pcre_pattern = repo_search.term_pattern("Gurne", "whole-token")
        pattern = re.compile(pcre_pattern.replace(r"[\p{L}\p{N}_]", r"\w"), re.I)
        self.assertIsNotNone(pattern.search("John Gurne"))
        self.assertIsNone(pattern.search("John Gurney"))

    def test_stale_ranking_id_is_ignored(self) -> None:
        class EmptyIndex:
            def all_sections(self):
                return []

        results = repo_search.build_results(
            EmptyIndex(),
            exact_matches=[],
            fts_scores={999: 10.0},
            effective_terms=["Gurney"],
            term_specs=[repo_search.SearchTermSpec("Gurney", "whole-token")],
            entity=None,
            entity_map=False,
            config={},
            lead_sections=[],
            explicit_terms=["Gurney"],
        )
        self.assertEqual(results, [])

    def test_name_variant_cli_is_case_insensitive(self) -> None:
        args = repo_search.build_parser().parse_args(
            ["search", "--terms", "Gurney", "--name-variants", "Modern"]
        )
        self.assertEqual(args.name_variants, "modern")

    def test_external_cache_configuration(self) -> None:
        repo_root = repo_search.find_repo_root(Path(__file__).resolve())
        config = repo_search.load_config(repo_root)
        self.assertNotIn("OneDrive", config["cacheRootResolved"])
        self.assertIn("GitDirs", config["cacheRootResolved"])

    def test_locate_scratch_dir_live(self) -> None:
        if not repo_search.find_ripgrep():
            self.skipTest("ripgrep not available")
        import contextlib
        import io
        with tempfile.TemporaryDirectory() as tmp:
            scratch = Path(tmp)
            (scratch / "bulk.txt").write_text(
                "line one\nROBERT GURNAY of Parva Cressingham\nline three\n",
                encoding="utf-8",
            )
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                rc = repo_search.main(["locate", "Cressingham", "--path", str(scratch)])
            out = buffer.getvalue()
        self.assertEqual(rc, 0)
        self.assertIn("bulk.txt:2:", out)  # real path:line, forward-slash, live read
        self.assertIn("1 matching line(s)", out)

    def test_locate_no_match_reports_zero(self) -> None:
        if not repo_search.find_ripgrep():
            self.skipTest("ripgrep not available")
        import contextlib
        import io
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "f.txt").write_text("nothing here\n", encoding="utf-8")
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                rc = repo_search.main(["locate", "zzzqxabsent", "--path", tmp])
        self.assertEqual(rc, 0)
        self.assertIn("0 matching line(s)", buffer.getvalue())


if __name__ == "__main__":
    unittest.main()
