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
    "disposition,source_registration_required,research_item_ids,source_ids,"
    "lead_action,lead_ids,notes\n"
)
CITE_HEADER = (
    "topic_id,source_id,registered_in_sources_json,cited_role,"
    "exact_locator_available,media_artifact_path,findings_supported,"
    "findings_contradicted,findings_qualified,notes\n"
)
SUPPLEMENTAL_HEADER = (
    "origin_path,origin_kind,origin_anchor,content_hash,destination_topic,"
    "disposition,research_item_ids,source_ids,friction,notes\n"
)


def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _span_hash(span_text: str) -> str:
    """16-hex block hash matching the checker's span self-verification."""
    return hashlib.sha256(span_text.encode("utf-8")).hexdigest()[:16]


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

    def write_graph(
        self, links: dict[str, list[tuple[str, str]]], *, revision: int = 1
    ) -> None:
        """Write a snapshot NDJSON: unit -> [(item_id, source_id or ''), ...]."""
        lines = [
            json.dumps(
                {"record_type": "manifest", "database_revision": revision}
            )
        ]
        seen_items: set[str] = set()
        for unit, pairs in links.items():
            lines.append(
                json.dumps(
                    {
                        "record_type": "row",
                        "table": "research_units",
                        "row": {"unit_id": unit},
                    }
                )
            )
            for item_id, source_id in pairs:
                if item_id not in seen_items:
                    seen_items.add(item_id)
                    lines.append(
                        json.dumps(
                            {
                                "record_type": "row",
                                "table": "research_items",
                                "row": {
                                    "item_id": item_id,
                                    "research_unit_id": unit,
                                },
                            }
                        )
                    )
                if source_id:
                    lines.append(
                        json.dumps(
                            {
                                "record_type": "row",
                                "table": "item_sources",
                                "row": {
                                    "item_id": item_id,
                                    "source_id": source_id,
                                },
                            }
                        )
                    )
        self.write(
            f"data/context-graphs/g13/exports/snapshots/g13-context-r{revision:06d}.ndjson",
            "\n".join(lines) + "\n",
        )

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
        json.dumps(
            {
                "sources": {
                    "src-alpha": {},
                    "src-alpha-transcript": {},
                    "src-beta": {},
                    "src-gamma": {},
                    "src-delta": {},
                }
            }
        ),
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

    tree.write_graph(
        {
            "topic-a": [("RI-A1", "src-alpha")],
            "topic-b": [("RI-B1", "src-beta")],
        }
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
        + f"{dump_input_rel},F1,First,topic,topic-a,assimilated,,,,,,ok\n"
        + f"{dump_input_rel},F2,Second,topic,topic-b,routed,,,,,,ok\n",
    )
    tree.write(
        "research/people/_staging/g13-john-gurney/coverage/source-and-citation-map.csv",
        CITE_HEADER
        + "topic-a,src-alpha,yes,supports,yes,,F1,,,ok\n"
        + "topic-b,src-beta,yes,supports,yes,,F2,,,ok\n",
    )
    tree.write(
        "research/people/_staging/g13-john-gurney/coverage/supplemental-surfaces-map.csv",
        SUPPLEMENTAL_HEADER,
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
        # Plan 2b categories are all clean and the graph export was found.
        self.assertTrue(report.source_lossless)
        self.assertEqual(report.input_source_set_gaps, [])
        self.assertEqual(report.source_journey_gaps, [])
        self.assertEqual(report.topic_graph_source_gaps, [])
        self.assertEqual(report.publication_mapping_gaps, [])
        self.assertEqual(report.friction_needs_decision, [])
        self.assertFalse(report.graph_export_missing)
        self.assertEqual(report.graph_revision, 1)

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
        self.assertTrue(payload["source_lossless"])
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
            + "sources/intake/dump-files/dump-synthetic.md,F1,First,topic,topic-a,assimilated,,,,,,ok\n"
            + "sources/intake/dump-files/dump-synthetic.md,F2,Second,topic,topic-b,,,,,,,backlog\n",
        )
        # 3) Unit B now cites `src-omega`, absent from the map AND from sources.json.
        tree.write(
            "research/people/_staging/g13-john-gurney/topics/unit-b.md",
            "# Unit B\n\nAnother.[^s] More.[^g]\n\n"
            "[^s]: Other. Source ID: `src-beta`.\n"
            "[^g]: Omega. Source ID: `src-omega`.\n",
        )
        # 4) Map lists `src-epsilon` for topic-a which is not in sources.json.
        tree.write(
            "research/people/_staging/g13-john-gurney/coverage/source-and-citation-map.csv",
            CITE_HEADER
            + "topic-a,src-alpha,yes,supports,yes,,F1,,,ok\n"
            + "topic-a,src-epsilon,yes,supports,yes,,F1,,,unregistered\n"
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

        # Unit cites src-omega that has no citation-map row.
        gap_sources = {g["source_id"] for g in report.unit_citation_gaps}
        self.assertIn("src-omega", gap_sources)

        # Both src-omega (unit) and src-epsilon (map) are unregistered.
        unregistered = {g["source_id"] for g in report.unregistered_sources}
        self.assertIn("src-omega", unregistered)
        self.assertIn("src-epsilon", unregistered)

    def test_dirty_main_exit_nonzero(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tree = self._build_dirty(Path(tmp))
            buf = io.StringIO()
            with redirect_stdout(buf):
                code = cov.main(["--repo-root", str(tree.root)])
            text = buf.getvalue()

        self.assertEqual(code, 1)
        self.assertIn("RESULT: FAIL", text)
        self.assertIn("SOURCE-LOSSLESS: PENDING", text)

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


class Plan2bSourceSetTests(unittest.TestCase):
    """Plan 2b §8.2 — input source-set integrity on anchored blocks."""

    def test_md_footnote_block_source_lost_from_ledger_gates(self) -> None:
        # The frozen block cites src-gamma via a resolved markdown footnote,
        # but the ledger row's source_ids omit it. Span self-verifies via the
        # 16-hex content hash, so the mismatch gates.
        with tempfile.TemporaryDirectory() as tmp:
            tree = _build_clean(Path(tmp))
            legacy = (
                "# Legacy companion\n"
                "\n"
                "## Records\n"
                "\n"
                "A finding.[^g]\n"
                "\n"
                "[^g]: Gamma witness. Source ID: `src-gamma`.\n"
            )
            tree.write("research/people/legacy-companion.md", legacy)
            lines = legacy.splitlines()
            span = "\n".join(lines[2:])  # rows: Intro at 1, Records at 3
            tree.write(
                "research/people/_staging/g13-john-gurney/coverage/legacy-companion-map.csv",
                LEGACY_HEADER
                + "research/people/legacy-companion.md,Intro,1,hash1,topic-a,synthesized,,,ok\n"
                + "research/people/legacy-companion.md,Records,3,"
                + f"{_span_hash(span)},topic-b,moved,,,missing gamma\n",
            )
            # Re-freeze the README hash for the rewritten companion.
            tree.write(
                "research/people/_staging/g13-john-gurney/coverage/README.md",
                "# Coverage ledgers\n\n## Frozen inventory\n\n"
                "| Input | Lines | State | Frozen SHA-256 (whole file) |\n"
                "|---|---|---|---|\n"
                f"| `research/people/legacy-companion.md` (legacy) | 7 | clean | `{_sha256(legacy)}` |\n"
                f"| `sources/intake/dump-files/dump-synthetic.md` (dump) | 3 | clean | `{_sha256('# Dump' + chr(10) + chr(10) + 'Finding.' + chr(10))}` |\n",
            )
            report = tree.run()

        self.assertFalse(report.ok)
        gaps = [g for g in report.input_source_set_gaps if g["ledger"] == "legacy"]
        self.assertEqual(len(gaps), 1)
        self.assertIn("src-gamma", gaps[0]["missing_in_ledger"])
        self.assertIn("Records", gaps[0]["row"])

    def test_dump_heading_anchored_source_set(self) -> None:
        # The dump finding block cites src-gamma inline; the assimilated row
        # omits it from source_ids -> gap anchored on the `### F1` heading.
        with tempfile.TemporaryDirectory() as tmp:
            tree = _build_clean(Path(tmp))
            dump = (
                "# Dump\n\n## Findings\n\n"
                "### F1 — The gamma record [T1]\n\n"
                "Found it. Source ID: `src-gamma`.\n\n"
                "### F2 — Unrelated\n\nNothing.\n"
            )
            tree.write("sources/intake/dump-files/dump-synthetic.md", dump)
            tree.write(
                "research/people/_staging/g13-john-gurney/coverage/dump-findings-map.csv",
                DUMP_HEADER
                + "sources/intake/dump-files/dump-synthetic.md,F1,The gamma record,"
                + "topic,topic-a,assimilated,,,,,,omits gamma\n",
            )
            tree.write(
                "research/people/_staging/g13-john-gurney/coverage/README.md",
                "# Coverage ledgers\n\n## Frozen inventory\n\n"
                "| Input | Lines | State | Frozen SHA-256 (whole file) |\n"
                "|---|---|---|---|\n"
                f"| `research/people/legacy-companion.md` (legacy) | 3 | clean | `{_sha256('# Legacy companion' + chr(10) + chr(10) + 'Body.' + chr(10))}` |\n"
                f"| `sources/intake/dump-files/dump-synthetic.md` (dump) | 9 | clean | `{_sha256(dump)}` |\n",
            )
            report = tree.run()

        gaps = [g for g in report.input_source_set_gaps if g["ledger"] == "dump"]
        self.assertEqual(len(gaps), 1)
        self.assertIn("src-gamma", gaps[0]["missing_in_ledger"])

    def test_html_code_source_ids_and_anchored_supplemental_block(self) -> None:
        # A publication surface cites via `Source ID: <code>...</code>` behind
        # an HTML footnote ref; the supplemental row lists the full set -> clean.
        # A second row omits one -> gap.
        with tempfile.TemporaryDirectory() as tmp:
            tree = _build_clean(Path(tmp))
            fact_sheet = (
                "# Fact sheet\n\n"
                "## Occupation\n\n"
                'He was a tailor.<sup><a href="#n1">1</a></sup>\n\n'
                "## Arrival\n\n"
                'He arrived by 1641.<sup><a href="#n2">2</a></sup>\n\n'
                "## Notes\n\n"
                '<ol>\n'
                '<li id="n1">Deed. Source ID: <code>src-alpha</code>.</li>\n'
                '<li id="n2">Court record. Source ID: <code>src-beta</code>.</li>\n'
                "</ol>\n"
            )
            tree.write("fact-sheets/subject.md", fact_sheet)
            tree.write(
                "research/people/_staging/g13-john-gurney/coverage/supplemental-surfaces-map.csv",
                SUPPLEMENTAL_HEADER
                + "fact-sheets/subject.md,fact_sheet,Occupation,,topic-a,"
                + "incorporated,RI-A1,src-alpha,,ok\n"
                + "fact-sheets/subject.md,fact_sheet,Arrival,,topic-b,"
                + "incorporated,RI-B1,,,omits beta\n",
            )
            report = tree.run()

        gaps = [
            g for g in report.input_source_set_gaps if g["ledger"] == "supplemental"
        ]
        self.assertEqual(len(gaps), 1)
        self.assertIn("src-beta", gaps[0]["missing_in_ledger"])
        self.assertIn("Arrival", gaps[0]["row"])
        # The complete row produced no gap.
        self.assertFalse(any("Occupation" in g["row"] for g in gaps))


class Plan2bJourneyTests(unittest.TestCase):
    """Plan 2b §8.3 — source-journey integrity against the graph export."""

    def test_source_lost_between_input_and_graph_gates(self) -> None:
        # src-gamma is registered and ledgered to topic-a (journey-checked
        # disposition) but linked to no item in that unit -> journey gap.
        with tempfile.TemporaryDirectory() as tmp:
            tree = _build_clean(Path(tmp))
            tree.write(
                "research/people/_staging/g13-john-gurney/coverage/legacy-companion-map.csv",
                LEGACY_HEADER
                + "research/people/legacy-companion.md,Intro,1,hash1,topic-a,"
                + "synthesized,RI-A1,src-alpha;src-gamma,gamma never landed\n"
                + "research/people/legacy-companion.md,Records,30,hash2,topic-b,moved,,,ok\n",
            )
            report = tree.run()

        self.assertFalse(report.ok)
        gaps = report.source_journey_gaps
        self.assertEqual(len(gaps), 1)
        self.assertEqual(gaps[0]["source_id"], "src-gamma")
        self.assertIn("topic-a", gaps[0]["reason"])

    def test_same_record_representations_both_required(self) -> None:
        # Two representations of one record (image + transcript) both listed;
        # only one is linked in the graph -> exactly the missing one gaps.
        with tempfile.TemporaryDirectory() as tmp:
            tree = _build_clean(Path(tmp))
            tree.write(
                "research/people/_staging/g13-john-gurney/coverage/legacy-companion-map.csv",
                LEGACY_HEADER
                + "research/people/legacy-companion.md,Intro,1,hash1,topic-a,"
                + "synthesized,RI-A1,src-alpha;src-alpha-transcript,two representations\n"
                + "research/people/legacy-companion.md,Records,30,hash2,topic-b,moved,,,ok\n",
            )
            report = tree.run()

        gaps = {g["source_id"] for g in report.source_journey_gaps}
        self.assertEqual(gaps, {"src-alpha-transcript"})

    def test_preserved_dispositions_do_not_require_graph_linkage(self) -> None:
        # Discovery-only and derivative-compiler sources preserved through
        # reviewed dispositions (publication_only / duplicate_but_preserved)
        # need no item link.
        with tempfile.TemporaryDirectory() as tmp:
            tree = _build_clean(Path(tmp))
            tree.write("fact-sheets/subject.md", "# FS\n\n## A\n\nx.\n\n## B\n\ny.\n")
            tree.write(
                "research/people/_staging/g13-john-gurney/coverage/supplemental-surfaces-map.csv",
                SUPPLEMENTAL_HEADER
                + "fact-sheets/subject.md,fact_sheet,A,,topic-a,"
                + "publication_only,,src-gamma,,discovery-only index\n"
                + "fact-sheets/subject.md,fact_sheet,B,,topic-a,"
                + "duplicate_but_preserved,,src-delta,,derivative compiler\n",
            )
            report = tree.run()

        self.assertEqual(report.source_journey_gaps, [])
        self.assertTrue(report.ok)

    def test_journey_deferred_when_destination_not_staged(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tree = _build_clean(Path(tmp))
            tree.write(
                "research/people/_staging/g13-john-gurney/coverage/legacy-companion-map.csv",
                LEGACY_HEADER
                + "research/people/legacy-companion.md,Intro,1,hash1,topic-future,"
                + "synthesized,,src-gamma,not staged yet\n"
                + "research/people/legacy-companion.md,Records,30,hash2,topic-b,moved,,,ok\n",
            )
            report = tree.run()

        self.assertEqual(report.source_journey_gaps, [])
        self.assertEqual(len(report.journey_deferred), 1)
        self.assertTrue(report.ok)

    def test_graph_export_missing_gates(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tree = _build_clean(Path(tmp))
            snap = (
                tree.root
                / "data/context-graphs/g13/exports/snapshots/g13-context-r000001.ndjson"
            )
            snap.unlink()
            report = tree.run()

        self.assertTrue(report.graph_export_missing)
        self.assertFalse(report.ok)
        self.assertFalse(report.source_lossless)


class Plan2bParityTests(unittest.TestCase):
    """Plan 2b §8.4 — topic prose <-> graph source parity."""

    def test_prose_cited_but_not_linked_gates(self) -> None:
        # Unit A also cites src-gamma (registered + in the citation map) but
        # no topic-a item links it -> parity gap (the Nash case).
        with tempfile.TemporaryDirectory() as tmp:
            tree = _build_clean(Path(tmp))
            tree.write(
                "research/people/_staging/g13-john-gurney/topics/unit-a.md",
                "# Unit A\n\nA finding.[^s] Also.[^g]\n\n"
                "[^s]: Some source. Source ID: `src-alpha`.\n"
                "[^g]: Gamma. Source ID: `src-gamma`.\n",
            )
            tree.write(
                "research/people/_staging/g13-john-gurney/coverage/source-and-citation-map.csv",
                CITE_HEADER
                + "topic-a,src-alpha,yes,supports,yes,,F1,,,ok\n"
                + "topic-a,src-gamma,yes,supports,yes,,F1,,,not linked\n"
                + "topic-b,src-beta,yes,supports,yes,,F2,,,ok\n",
            )
            report = tree.run()

        gaps = report.topic_graph_source_gaps
        self.assertEqual(len(gaps), 1)
        self.assertEqual(gaps[0]["source_id"], "src-gamma")
        self.assertIn("prose", gaps[0]["direction"])
        self.assertFalse(report.ok)

    def test_linked_but_never_cited_gates(self) -> None:
        # topic-a items link src-gamma but the prose never cites it.
        with tempfile.TemporaryDirectory() as tmp:
            tree = _build_clean(Path(tmp))
            tree.write_graph(
                {
                    "topic-a": [("RI-A1", "src-alpha"), ("RI-A2", "src-gamma")],
                    "topic-b": [("RI-B1", "src-beta")],
                },
                revision=2,
            )
            report = tree.run()

        gaps = report.topic_graph_source_gaps
        self.assertEqual(len(gaps), 1)
        self.assertEqual(gaps[0]["source_id"], "src-gamma")
        self.assertIn("never cited", gaps[0]["direction"])

    def test_context_only_role_exempts_parity(self) -> None:
        # A reviewed context-only citation-map row exempts the pair.
        with tempfile.TemporaryDirectory() as tmp:
            tree = _build_clean(Path(tmp))
            tree.write(
                "research/people/_staging/g13-john-gurney/topics/unit-a.md",
                "# Unit A\n\nA finding.[^s] Context.[^g]\n\n"
                "[^s]: Some source. Source ID: `src-alpha`.\n"
                "[^g]: Gamma. Source ID: `src-gamma`.\n",
            )
            tree.write(
                "research/people/_staging/g13-john-gurney/coverage/source-and-citation-map.csv",
                CITE_HEADER
                + "topic-a,src-alpha,yes,supports,yes,,F1,,,ok\n"
                + "topic-a,src-gamma,yes,context_only,yes,,,,,cross-unit context\n"
                + "topic-b,src-beta,yes,supports,yes,,F2,,,ok\n",
            )
            report = tree.run()

        self.assertEqual(report.topic_graph_source_gaps, [])
        self.assertTrue(report.ok)


class Plan2bPublicationAndFrictionTests(unittest.TestCase):
    """Plan 2b §8.5 mechanical publication mapping + §8.6 friction."""

    def test_incorporated_publication_block_needs_graph_items(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tree = _build_clean(Path(tmp))
            tree.write("fact-sheets/subject.md", "# FS\n\n## A\n\nx.\n\n## B\n\ny.\n")
            tree.write(
                "research/people/_staging/g13-john-gurney/coverage/supplemental-surfaces-map.csv",
                SUPPLEMENTAL_HEADER
                # No research_item_ids at all.
                + "fact-sheets/subject.md,fact_sheet,A,,topic-a,incorporated,,,,no items\n"
                # Maps an item id that does not exist in the graph.
                + "fact-sheets/subject.md,case_file,B,,topic-a,incorporated,RI-GHOST,,,ghost\n",
            )
            report = tree.run()

        self.assertEqual(len(report.publication_mapping_gaps), 2)
        reasons = " | ".join(g["reason"] for g in report.publication_mapping_gaps)
        self.assertIn("maps no research items", reasons)
        self.assertIn("RI-GHOST", reasons)
        self.assertFalse(report.ok)

    def test_needs_decision_disposition_is_gating_friction(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tree = _build_clean(Path(tmp))
            tree.write("fact-sheets/subject.md", "# FS\n\n## A\n\nx.\n")
            tree.write(
                "research/people/_staging/g13-john-gurney/coverage/supplemental-surfaces-map.csv",
                SUPPLEMENTAL_HEADER
                + "fact-sheets/subject.md,fact_sheet,A,,topic-a,needs_decision,,,claim_conflict,disputed\n",
            )
            report = tree.run()

        self.assertEqual(len(report.friction_needs_decision), 1)
        self.assertFalse(report.ok)
        self.assertFalse(report.source_lossless)
        # claim_conflict is recorded as open friction, not a decision gate.
        self.assertEqual(len(report.friction_open), 1)

    def test_needs_source_pull_friction_gates(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tree = _build_clean(Path(tmp))
            tree.write("fact-sheets/subject.md", "# FS\n\n## A\n\nx.\n")
            tree.write(
                "research/people/_staging/g13-john-gurney/coverage/supplemental-surfaces-map.csv",
                SUPPLEMENTAL_HEADER
                + "fact-sheets/subject.md,fact_sheet,A,,topic-a,"
                + "publication_only,,src-gamma,needs_source_pull,unpulled\n",
            )
            report = tree.run()

        self.assertEqual(len(report.friction_needs_decision), 1)
        self.assertFalse(report.ok)


if __name__ == "__main__":
    unittest.main()
