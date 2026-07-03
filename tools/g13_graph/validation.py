"""Semantic validation that complements database constraints."""

from __future__ import annotations

import json
import re
import sqlite3
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from .config import GraphConfig
from .db import connect
from .drift import source_hash_state
from .exporter import export_identity
from .indexes import derived_index_state
from .schema_manager import current_schema_version
from .sources import mirror_state


@dataclass(frozen=True)
class ValidationIssue:
    severity: str
    code: str
    record_id: str | None
    message: str


def _issue(
    issues: list[ValidationIssue],
    code: str,
    message: str,
    record_id: str | None = None,
    severity: str = "error",
) -> None:
    issues.append(ValidationIssue(severity, code, record_id, message))


def _date_key(value: str | None) -> tuple[int, int, int] | None:
    if value is None:
        return None
    parts = value.split("-")
    try:
        numbers = [int(part) for part in parts]
    except ValueError:
        return None
    if not 1 <= len(numbers) <= 3:
        return None
    return tuple((numbers + [1, 1])[:3])  # type: ignore[return-value]


def _cycle_nodes(edges: dict[str, set[str]]) -> set[str]:
    visiting: set[str] = set()
    visited: set[str] = set()
    cycles: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        if node in visiting:
            start = path.index(node)
            cycles.update(path[start:])
            return
        if node in visited:
            return
        visiting.add(node)
        path.append(node)
        for target in edges.get(node, set()):
            visit(target, path)
        path.pop()
        visiting.remove(node)
        visited.add(node)

    for node in edges:
        visit(node, [])
    return cycles


def _repo_location_exists(repo_root: Path, path_value: str, heading_id: str | None) -> bool:
    if path_value.startswith("fixture://"):
        return True
    path = (repo_root / path_value).resolve()
    try:
        path.relative_to(repo_root)
    except ValueError:
        return False
    if not path.is_file():
        return False
    if heading_id:
        text = path.read_text(encoding="utf-8")
        if f'id="{heading_id}"' in text or f"{{#{heading_id}}}" in text:
            return True
        for heading in re.findall(r"^#{1,6}\s+(.+?)\s*$", text, flags=re.MULTILINE):
            plain = re.sub(r"\s+\{#.+?\}\s*$", "", heading)
            slug = re.sub(r"[^\w\s-]", "", plain.casefold())
            slug = re.sub(r"[\s_-]+", "-", slug).strip("-")
            if slug == heading_id:
                return True
        return False
    return True


def validate_connection(
    connection: sqlite3.Connection,
    config: GraphConfig,
    *,
    include_recovery: bool = True,
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    for row in connection.execute("PRAGMA foreign_key_check"):
        _issue(
            issues,
            "foreign_key_violation",
            f"Foreign-key violation in table {row[0]} at row {row[1]}.",
            str(row[1]),
        )

    edges: dict[str, set[str]] = {}
    statuses = {
        row["item_id"]: row["status"]
        for row in connection.execute("SELECT item_id, status FROM research_items")
    }
    for row in connection.execute(
        "SELECT item_id, superseded_by FROM research_items WHERE superseded_by IS NOT NULL"
    ):
        edges.setdefault(row["item_id"], set()).add(row["superseded_by"])
        if statuses.get(row["item_id"]) == "active" and statuses.get(row["superseded_by"]) == "active":
            _issue(
                issues,
                "active_item_superseded_by_active",
                "An active item is superseded by another active item.",
                row["item_id"],
            )
    for row in connection.execute(
        """
        SELECT from_item_id, to_item_id
        FROM item_relations WHERE relation_type='SUPERSEDES'
        """
    ):
        edges.setdefault(row["from_item_id"], set()).add(row["to_item_id"])
        if statuses.get(row["from_item_id"]) == "active" and statuses.get(row["to_item_id"]) == "active":
            _issue(
                issues,
                "active_supersession_relation",
                "A SUPERSEDES relation connects two active items.",
                row["from_item_id"],
            )
    for item_id in sorted(_cycle_nodes(edges)):
        _issue(
            issues,
            "supersession_cycle",
            "Item participates in a supersession cycle.",
            item_id,
        )

    for row in connection.execute(
        """
        SELECT i.item_id, n.limitations_json
        FROM research_items AS i
        LEFT JOIN negative_result_scope AS n ON n.item_id=i.item_id
        WHERE i.item_kind='negative_result'
        """
    ):
        limitations: Any = None
        if row["limitations_json"]:
            try:
                limitations = json.loads(row["limitations_json"])
            except json.JSONDecodeError:
                limitations = None
        if not isinstance(limitations, list) or not limitations:
            _issue(
                issues,
                "negative_result_scope_missing",
                "Negative result lacks structured scope or limitations.",
                row["item_id"],
            )

    for row in connection.execute("SELECT * FROM item_dates"):
        plausible_start = _date_key(row["plausible_start"])
        plausible_end = _date_key(row["plausible_end"])
        probable_start = _date_key(row["probable_start"])
        probable_end = _date_key(row["probable_end"])
        invalid = (
            plausible_start
            and plausible_end
            and plausible_start > plausible_end
        ) or (
            probable_start and probable_end and probable_start > probable_end
        ) or (
            plausible_start and probable_start and probable_start < plausible_start
        ) or (
            plausible_end and probable_end and probable_end > plausible_end
        )
        if invalid:
            _issue(
                issues,
                "probable_outside_plausible",
                "Probable date range falls outside plausible date range.",
                row["item_id"],
            )
        if row["chronology_key"] is not None and not row["chronology_key_basis"]:
            _issue(
                issues,
                "chronology_basis_missing",
                "Chronology key lacks a declared basis.",
                row["item_id"],
            )

    try:
        state = mirror_state(
            connection, config.sources_path, repo_root=config.repo_root
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        _issue(issues, "source_registry_unreadable", str(exc))
    else:
        if state["state"] != "current":
            _issue(
                issues,
                "source_registry_stale",
                "source_registry does not match the configured sources.json.",
            )

    hash_state = source_hash_state(connection, config)
    for source in hash_state["sources"]:
        if source["state"] == "missing_baseline":
            _issue(
                issues,
                "source_hash_missing",
                "Cited local source has no captured content-hash baseline.",
                source["source_id"],
                severity="warning",
            )
        elif source["state"] == "drifted":
            _issue(
                issues,
                "source_content_drift",
                "Cited source content changed after its hash baseline was captured.",
                source["source_id"],
                severity="warning",
            )
        elif source["state"] == "missing_file":
            _issue(
                issues,
                "source_content_missing",
                "Cited local source path does not resolve to a file.",
                source["source_id"],
                severity="warning",
            )

    index_state = derived_index_state(connection)
    if index_state["state"] != "current":
        _issue(
            issues,
            "derived_indexes_stale",
            "Rebuildable FTS indexes do not match the live database revision.",
        )

    for row in connection.execute(
        """
        SELECT item_id, research_unit_id
        FROM research_items WHERE research_unit_id IS NULL
        """
    ):
        _issue(
            issues,
            "research_unit_missing",
            "Research item has no research unit.",
            row["item_id"],
        )
    for row in connection.execute("SELECT * FROM research_units"):
        if not _repo_location_exists(config.repo_root, row["path"], row["heading_id"]):
            _issue(
                issues,
                "research_location_invalid",
                "Research-unit path or heading does not resolve.",
                row["unit_id"],
            )
    for row in connection.execute("SELECT * FROM item_publications"):
        if not _repo_location_exists(
            config.repo_root, row["publication_path"], row["heading_id"]
        ):
            _issue(
                issues,
                "publication_mapping_invalid",
                "Publication path or heading does not resolve.",
                str(row["publication_id"]),
            )
        if row["visibility"] == "public" and row["status"] == "retired":
            _issue(
                issues,
                "publication_visibility_invalid",
                "A retired publication mapping cannot be public.",
                str(row["publication_id"]),
            )

    for row in connection.execute(
        """
        SELECT r.from_item_id, r.to_item_id, a.visibility AS from_visibility,
               b.visibility AS to_visibility
        FROM item_relations AS r
        JOIN research_items AS a ON a.item_id=r.from_item_id
        JOIN research_items AS b ON b.item_id=r.to_item_id
        WHERE (a.visibility='public' AND b.visibility<>'public')
           OR (b.visibility='public' AND a.visibility<>'public')
        """
    ):
        _issue(
            issues,
            "public_relation_visibility_leak",
            "A public item is connected to a non-public item.",
            f"{row['from_item_id']}->{row['to_item_id']}",
        )
    for row in connection.execute(
        """
        SELECT s.item_source_id, s.item_id
        FROM item_sources AS s
        JOIN research_items AS i ON i.item_id=s.item_id
        WHERE i.visibility='public'
          AND s.evidence_excerpt IS NOT NULL
          AND length(trim(s.evidence_excerpt)) > 0
          AND s.excerpt_publishable=0
        """
    ):
        _issue(
            issues,
            "public_excerpt_not_publishable",
            "Public evidence excerpt lacks excerptPublishable=true.",
            row["item_id"],
        )
    for row in connection.execute(
        """
        SELECT item_id FROM research_items
        WHERE provenance_origin='machine_suggested'
          AND review_state<>'human_reviewed'
        """
    ):
        _issue(
            issues,
            "machine_item_unreviewed",
            "Machine-suggested item has not been human-reviewed.",
            row["item_id"],
        )
    for row in connection.execute(
        """
        SELECT s.item_id FROM item_sources AS s
        JOIN research_items AS i ON i.item_id=s.item_id
        WHERE i.item_kind='source_evidence'
          AND s.role<>'discovery_only'
          AND length(trim(s.locator))=0
        """
    ):
        _issue(
            issues,
            "source_locator_missing",
            "Source-evidence connection lacks a locator.",
            row["item_id"],
            severity="warning",
        )

    if include_recovery:
        live_revision = int(
            connection.execute(
                "SELECT database_revision FROM graph_meta WHERE singleton_id=1"
            ).fetchone()[0]
        )
        recovery = export_identity(config.recovery_path)
        live_schema = current_schema_version(connection)
        if (
            recovery is None
            or recovery["database_revision"] != live_revision
            or recovery["schema_version"] != live_schema
        ):
            _issue(
                issues,
                "recovery_export_stale",
                f"Recovery export identity {recovery!r} does not match "
                f"schema/revision {live_schema}/{live_revision}.",
            )
    return sorted(
        issues,
        key=lambda issue: (
            0 if issue.severity == "error" else 1,
            issue.code,
            issue.record_id or "",
        ),
    )


def validate_database(
    config: GraphConfig, *, include_recovery: bool = True
) -> list[ValidationIssue]:
    connection = connect(config.db_path, read_only=True)
    try:
        return validate_connection(
            connection, config, include_recovery=include_recovery
        )
    finally:
        connection.close()


def issues_as_dicts(issues: list[ValidationIssue]) -> list[dict[str, Any]]:
    return [asdict(issue) for issue in issues]
