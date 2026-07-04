from __future__ import annotations

import hashlib
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from tools import g13_coverage_check as cov


LEGACY_HEADER = (
    "legacy_path,legacy_heading,line_start_at_inventory,content_hash,"
    "destination_topic,disposition,research_item_ids,source_ids,notes\n"
)
DUMP_HEADER = (
    "dump_file,finding_id,finding_heading,destination_type,destination_path,"
    "disposition,source_registration_required,research_item_ids,lead_action,"
    "lead_ids,notes\n"
)
CITE_HEADER = (
    "topic_id,source_id,registered_in_sources_json,cited_role,"
    "exact_locator_available,media_artifact_path,findings_supported,"
    "findings_contradicted,findings_qualified,notes\n"
)


def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


class SyntheticTree:
    """Builds a minimal repo tree the checker can run against."""

    def __init__(self, root: Path) -> None:
        self.root = root
        self.coverage = root / "research/people/_staging/g13-john-gurney/coverage"
        self.topics = root / "research/people/_staging/g13-john-gurney/topics"
        self.coverage.mkdir(parents=True, exist_ok=True)
        self.topics.mkdir(parents=True, exist_ok=True)
        (root / "data").mkdir(parents=True, exist_ok=True)
        (root / "sources/intake/dump-files").mkdir(parents=True, exist_ok=True)

    def write(self, rel: str, text: str) -> str:
        target = self.root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        # newline="" disables translation so on-disk bytes match `text` exactly,
        # keeping the SHA-256 we embed in the inventory README reproducible.
        target.write_text(text, encoding="utf-8", newline="")
        return text

    def run(self) -> cov.CoverageReport:
        return cov.run_check(
            coverage_dir=self.coverage,
            sources_path=self.root / "data/sources.json",
            repo_root=self.root,
        )


def _build_clean(root: Path) -> SyntheticTree:
    tree = SyntheticTree(root)

    legacy_input_rel = "research/people/legacy-companion.md"
    dump_input_rel = "sources/intake/dump-files/dump-synthetic.md"
    legacy_text = tree.write(legacy_input_rel, "# Legacy companion\n\nBody.\n")
    dump_text = tree.write(dump_input_rel, "# Dump\n\nFinding.\n")

    # Two staged units, each citing exactly the sources the map records.
    unit_a_rel = "research/people/_staging/g13-john-gurney/topics/unit-a.md"
    unit_b_rel = "research/people/_staging/g13-john-gurney/topics/unit-b.md"
    tree.write(
        unit_a_rel,
        "# Unit A\n\nA finding.[^s]\n\n[^s]: Some source. Source ID: `src-alpha`.\n",
    )
    tree.write(
        unit_b_rel,
        "# Unit B\n\nAnother.[^s]\n\n[^s]: Other. Source ID: `src-beta`.\n",
    )

    tree.write(
        "data/sources.json",
        json.dumps({"sources": {"src-alpha": {}, "src-beta": {}}}),
    )

    tree.write(
        "research/people/_staging/g13-john-gurney/manifest.json",
        json.dumps(
            {
                "topics": [
                    {"topicId": "topic-a", "path": unit_a_rel},
                    {"topicId": "topic-b", "path": unit_b_rel},
                ]
            }
        ),
    )

    tree.write(
        "research/people/_staging/g13-john-gurney/coverage/legacy-companion-map.csv",
        LEGACY_HEADER
        + f"{legacy_input_rel},Intro,1,hash1,topic-a,synthesized,,,ok\n"
        + f"{legacy_input_rel},Records,30,hash2,topic-b,moved,,,ok\n",
    )
    tree.write(
        "research/people/_staging/g13-john-gurney/coverage/dump-findings-map.csv",
        DUMP_HEADER
        + f"{dump_input_rel},F1,First,topic,topic-a,assimilated,,,,,ok\n"
        + f"{dump_input_rel},F2,Second,topic,topic-b,routed,,,,,ok\n",
    )
    tree.write(
        "research/people/_staging/g13-john-gurney/coverage/source-and-citation-map.csv",
        CITE_HEADER
        + "topic-a,src-alpha,yes,supports,yes,,F1,,,ok\n"
        + "topic-b,src-beta,yes,supports,yes,,F2,,,ok\n",
    )

    readme = (
        "# Coverage ledgers\n\n"
        "## Frozen inventory\n\n"
        "| Input | Lines | State | Frozen SHA-256 (whole file) |\n"
        "|---|---|---|---|\n"
        f"| `{legacy_input_rel}` (legacy companion) | 3 | clean | `{_sha256(legacy_text)}` |\n"
        f"| `{dump_input_rel}` (dump) | 3 | clean | `{_sha256(dump_text)}` |\n"
    )
    tree.write(
        "research/people/_staging/g13-john-gurney/coverage/README.md", readme
    )
    return tree


class CleanLedgerTests(unittest.TestCase):
    def test_clean_set_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            report = _build_clean(Path(tmp)).run()

        self.assertTrue(report.ok)
        self.assertEqual(report.gating_problem_count, 0)
        self.assertEqual(report.legacy.coverage_pct, 100.0)
        self.assertEqual(report.dump.coverage_pct, 100.0)
        self.assertEqual(report.unit_citation_gaps, [])
        self.assertEqual(report.unregistered_sources, [])
        self.assertEqual(report.hash_mismatches, [])
        self.assertEqual(report.inputs_without_rows, [])
        self.assertEqual(report.inventory_inputs, 2)

    def test_main_exit_zero_and_json(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tree = _build_clean(Path(tmp))
            buf = io.StringIO()
            with redirect_stdout(buf):
                code = cov.main(
                    [
                        "--repo-root",
                        str(tree.root),
                        "--json",
                    ]
                )
            payload = json.loads(buf.getvalue())

        self.assertEqual(code, 0)
        self.assertTrue(payload["ok"])
        self.assertEqual(payload["ledgers"]["combined"]["coverage_pct"], 100.0)


class DirtyLedgerTests(unittest.TestCase):
    def _build_dirty(self, root: Path) -> SyntheticTree:
        tree = _build_clean(root)

        # 1) Un-dispositioned legacy row (empty disposition).
        tree.write(
            "research/people/_staging/g13-john-gurney/coverage/legacy-companion-map.csv",
            LEGACY_HEADER
            + "research/people/legacy-companion.md,Intro,1,hash1,topic-a,synthesized,,,ok\n"
            + "research/people/legacy-companion.md,Records,30,hash2,,,,,backlog\n",
        )
        # 2) Un-dispositioned dump finding (empty disposition).
        tree.write(
            "research/people/_staging/g13-john-gurney/coverage/dump-findings-map.csv",
            DUMP_HEADER
            + "sources/intake/dump-files/dump-synthetic.md,F1,First,topic,topic-a,assimilated,,,,,ok\n"
            + "sources/intake/dump-files/dump-synthetic.md,F2,Second,topic,topic-b,,,,,,backlog\n",
        )
        # 3) Unit B now cites `src-gamma`, absent from the map AND from sources.json.
        tree.write(
            "research/people/_staging/g13-john-gurney/topics/unit-b.md",
            "# Unit B\n\nAnother.[^s] More.[^g]\n\n"
            "[^s]: Other. Source ID: `src-beta`.\n"
            "[^g]: Gamma. Source ID: `src-gamma`.\n",
        )
        # 4) Map lists `src-delta` for topic-a which is not in sources.json.
        tree.write(
            "research/people/_staging/g13-john-gurney/coverage/source-and-citation-map.csv",
            CITE_HEADER
            + "topic-a,src-alpha,yes,supports,yes,,F1,,,ok\n"
            + "topic-a,src-delta,yes,supports,yes,,F1,,,unregistered\n"
            + "topic-b,src-beta,yes,supports,yes,,F2,,,ok\n",
        )
        return tree

    def test_dirty_set_gates(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            report = self._build_dirty(Path(tmp)).run()

        self.assertFalse(report.ok)
        # Backlog surfaced in both disposition ledgers.
        self.assertEqual(report.legacy.backlog, 1)
        self.assertEqual(report.dump.backlog, 1)
        self.assertIn("Records", report.legacy.gaps[0])
        self.assertTrue(any("F2" in g for g in report.dump.gaps))

        # Unit cites src-gamma that has no citation-map row.
        gap_sources = {g["source_id"] for g in report.unit_citation_gaps}
        self.assertIn("src-gamma", gap_sources)

        # Both src-gamma (unit) and src-delta (map) are unregistered.
        unregistered = {g["source_id"] for g in report.unregistered_sources}
        self.assertIn("src-gamma", unregistered)
        self.assertIn("src-delta", unregistered)

    def test_dirty_main_exit_nonzero(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tree = self._build_dirty(Path(tmp))
            buf = io.StringIO()
            with redirect_stdout(buf):
                code = cov.main(["--repo-root", str(tree.root)])
            text = buf.getvalue()

        self.assertEqual(code, 1)
        self.assertIn("RESULT: FAIL", text)

    def test_hash_drift_gates(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tree = _build_clean(Path(tmp))
            # Mutate a frozen input after the freeze; its SHA no longer matches.
            (tree.root / "sources/intake/dump-files/dump-synthetic.md").write_text(
                "# Dump\n\nMUTATED after freeze.\n", encoding="utf-8"
            )
            report = tree.run()

        self.assertFalse(report.ok)
        self.assertEqual(len(report.hash_mismatches), 1)
        self.assertIn("dump-synthetic.md", report.hash_mismatches[0]["path"])


if __name__ == "__main__":
    unittest.main()
