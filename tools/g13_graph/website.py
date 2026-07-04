"""Static website export for the G13 context graph (Phase G5).

Emits deterministic, read-only JSON for the future graph-enhanced website:
per-finding pages, a finding index, and an adjacency slice. It never mutates the
database, prose, or source files.

Publication-safety contract (Plan 01 §14, §16 G5):

- **Public items only.** Only research items with ``visibility='public'`` are
  exported. ``repo_only`` and ``restricted`` items — and every repo-internal
  field (research location, reviewer, notes, restriction reason, the numeric
  confidence mirror) — are omitted entirely.
- **Publishable excerpts only.** A source ``evidence_excerpt`` is emitted only
  when its ``excerpt_publishable`` flag is set; the ``sourceId`` and locator are
  citation metadata and are always safe to publish.
- **Edges only between public endpoints.** An adjacency edge is emitted only when
  *both* items are public, so a restricted item's id/label can never leak through
  a relation. Publication mappings are emitted only for ``published`` status.
- **Band confidence only.** The controlled confidence *label* is exported; the
  numeric ``value`` is never emitted (Plan 01 §8.2 — it must never be treated as
  an orderable probability).

Determinism mirrors the NDJSON recovery export: items sorted by id, edges by
(from, type, to), JSON keys sorted, and the manifest timestamp is the database
revision's committed timestamp, so re-exporting an unchanged revision is
byte-identical.
"""

from __future__ import annotations

import json
import shutil
import sqlite3
from html import escape
from pathlib import Path
from typing import Any

from .config import GraphConfig
from .db import connect
from .util import atomic_write, canonical_json, sha256_json

# Reader-facing kind labels (Plan 01 §8.1). Repo-internal kind codes are the
# stable identity; these are the display strings the website shows.
KIND_LABELS: dict[str, str] = {
    "source_evidence": "Evidence",
    "research_finding": "Finding",
    "analysis": "Analysis",
    "identity_hypothesis": "Identity hypothesis",
    "negative_result": "Negative result",
    "evidence_conflict": "Evidence conflict",
    "published_source_statement": "Published-source statement",
    "project_statement": "Project statement",
    "open_question": "Open question",
}


class PublicMarkerExportError(RuntimeError):
    """A public marker could not be emitted as one complete public bundle."""

    def __init__(self, marker_ids: list[str]):
        self.marker_ids = sorted(marker_ids)
        super().__init__(
            "Public marker export blocked; incomplete marker bundle(s): "
            + ", ".join(self.marker_ids)
        )


def _public_item_ids(connection: sqlite3.Connection) -> set[str]:
    return {
        row["item_id"]
        for row in connection.execute(
            "SELECT item_id FROM research_items WHERE visibility='public'"
        )
    }


def _entity_labels(connection: sqlite3.Connection) -> dict[str, dict[str, Any]]:
    return {
        row["entity_id"]: {"id": row["entity_id"], "label": row["canonical_label"],
                           "type": row["entity_type"]}
        for row in connection.execute(
            "SELECT entity_id, canonical_label, entity_type FROM entities"
        )
    }


def _unit_titles(connection: sqlite3.Connection) -> dict[str, str]:
    return {
        row["unit_id"]: row["title"]
        for row in connection.execute("SELECT unit_id, title FROM research_units")
    }


def _item_dates(connection: sqlite3.Connection, item_id: str) -> list[dict[str, Any]]:
    return [
        {
            "role": row["date_role"],
            "plausibleStart": row["plausible_start"],
            "plausibleEnd": row["plausible_end"],
            "probableStart": row["probable_start"],
            "probableEnd": row["probable_end"],
            "precision": row["precision"],
            "display": row["original_display"],
            "chronologyKey": row["chronology_key"],
            "chronologyKeyBasis": row["chronology_key_basis"],
        }
        for row in connection.execute(
            "SELECT * FROM item_dates WHERE item_id=? ORDER BY date_role", (item_id,)
        )
    ]


def _item_sources(connection: sqlite3.Connection, item_id: str) -> list[dict[str, Any]]:
    sources: list[dict[str, Any]] = []
    for row in connection.execute(
        "SELECT * FROM item_sources WHERE item_id=? ORDER BY source_id, locator, item_source_id",
        (item_id,),
    ):
        entry: dict[str, Any] = {
            "sourceId": row["source_id"],
            "role": row["role"],
            "locator": row["locator"],
        }
        # Publication-safety: only a cleared excerpt is emitted.
        excerpt = (row["evidence_excerpt"] or "").strip()
        if excerpt and row["excerpt_publishable"]:
            entry["excerpt"] = excerpt
        if row["alignment_note"]:
            entry["alignmentNote"] = row["alignment_note"]
        sources.append(entry)
    return sources


def _item_entities(
    connection: sqlite3.Connection, item_id: str, labels: dict[str, dict[str, Any]]
) -> list[dict[str, Any]]:
    entities: list[dict[str, Any]] = []
    for row in connection.execute(
        "SELECT entity_id, role FROM item_entities WHERE item_id=? ORDER BY entity_id, role",
        (item_id,),
    ):
        base = labels.get(row["entity_id"], {"id": row["entity_id"], "label": None, "type": None})
        entities.append({**base, "role": row["role"]})
    return entities


def _item_publications(connection: sqlite3.Connection, item_id: str) -> list[dict[str, Any]]:
    return [
        {
            "path": row["publication_path"],
            "headingId": row["heading_id"],
            "assertionSummary": row["assertion_summary"],
            "status": row["status"],
        }
        for row in connection.execute(
            "SELECT * FROM item_publications WHERE item_id=? AND status='published' "
            "ORDER BY publication_path, publication_id",
            (item_id,),
        )
    ]


def _negative_scope(connection: sqlite3.Connection, item_id: str) -> dict[str, Any] | None:
    row = connection.execute(
        "SELECT * FROM negative_result_scope WHERE item_id=?", (item_id,)
    ).fetchone()
    if row is None:
        return None
    try:
        limitations = json.loads(row["limitations_json"] or "[]")
    except json.JSONDecodeError:
        limitations = []
    return {
        "provider": row["provider"],
        "collection": row["collection_name"],
        "dateStart": row["date_start"],
        "dateEnd": row["date_end"],
        "queryDescription": row["query_description"],
        "resultsReviewed": row["results_reviewed"],
        "coverageConfirmed": bool(row["coverage_confirmed"]),
        "limitations": limitations,
    }


def _public_edges(
    connection: sqlite3.Connection, public_ids: set[str]
) -> list[dict[str, Any]]:
    edges: list[dict[str, Any]] = []
    for row in connection.execute(
        "SELECT * FROM item_relations ORDER BY from_item_id, relation_type, to_item_id"
    ):
        # An edge is only safe to publish when BOTH endpoints are public.
        if row["from_item_id"] not in public_ids or row["to_item_id"] not in public_ids:
            continue
        edges.append({
            "from": row["from_item_id"],
            "type": row["relation_type"],
            "to": row["to_item_id"],
            "bearing": row["bearing"],
            "strength": row["strength"],
            "explanation": row["explanation"],
        })
    return edges


def _finding(
    connection: sqlite3.Connection,
    row: sqlite3.Row,
    *,
    entity_labels: dict[str, dict[str, Any]],
    unit_titles: dict[str, str],
    edges: list[dict[str, Any]],
) -> dict[str, Any]:
    item_id = row["item_id"]
    finding: dict[str, Any] = {
        "id": item_id,
        "kind": row["item_kind"],
        "kindLabel": KIND_LABELS.get(row["item_kind"], row["item_kind"]),
        "statement": row["statement"],
        "shortLabel": row["short_label"],
        "status": row["status"],
        # Band label only — never the numeric confidence mirror (§8.2).
        "confidence": row["assessment_confidence_label"],
        "subject": entity_labels.get(row["subject_entity_id"]) if row["subject_entity_id"] else None,
        "unit": (
            {"id": row["research_unit_id"], "title": unit_titles.get(row["research_unit_id"])}
            if row["research_unit_id"]
            else None
        ),
        "dates": _item_dates(connection, item_id),
        "sources": _item_sources(connection, item_id),
        "entities": _item_entities(connection, item_id, entity_labels),
        "publications": _item_publications(connection, item_id),
        "relations": {
            "outgoing": [e for e in edges if e["from"] == item_id],
            "incoming": [e for e in edges if e["to"] == item_id],
        },
    }
    if row["summary"]:
        finding["summary"] = row["summary"]
    negative = _negative_scope(connection, item_id)
    if negative is not None:
        finding["negativeResult"] = negative
    return finding


def _public_marker_exports(
    connection: sqlite3.Connection,
    findings: list[dict[str, Any]],
    unit_titles: dict[str, str],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[str]]:
    finding_by_id = {finding["id"]: finding for finding in findings}
    index: list[dict[str, Any]] = []
    bundles: list[dict[str, Any]] = []
    blocked: list[str] = []
    for marker in connection.execute(
        """
        SELECT * FROM prose_markers
        WHERE visibility='public' AND status='active'
        ORDER BY marker_id
        """
    ):
        members = [
            dict(row)
            for row in connection.execute(
                """
                SELECT mi.*, i.visibility AS item_visibility
                FROM prose_marker_items AS mi
                JOIN research_items AS i ON i.item_id=mi.item_id
                WHERE mi.marker_id=?
                ORDER BY mi.display_order, mi.item_id
                """,
                (marker["marker_id"],),
            )
        ]
        primaries = [row for row in members if row["marker_role"] == "primary"]
        complete = (
            len(primaries) == 1
            and primaries[0]["item_id"] == marker["primary_item_id"]
            and all(
                row["item_visibility"] == "public"
                and row["item_id"] in finding_by_id
                for row in members
            )
        )
        if not complete:
            blocked.append(marker["marker_id"])
            continue
        public_members = [
            {
                "role": row["marker_role"],
                "displayOrder": row["display_order"],
                "finding": finding_by_id[row["item_id"]],
            }
            for row in members
        ]
        primary = finding_by_id[marker["primary_item_id"]]
        url = f"/research/evidence/{marker['marker_id'].lower()}/"
        bundle = {
            "id": marker["marker_id"],
            "url": url,
            "unit": {
                "id": marker["research_unit_id"],
                "title": unit_titles.get(marker["research_unit_id"]),
            },
            "primary": primary,
            "items": public_members,
        }
        bundles.append(bundle)
        index.append(
            {
                "id": marker["marker_id"],
                "url": url,
                "primaryItemId": primary["id"],
                "primaryLabel": primary["shortLabel"] or primary["statement"],
                "itemCount": len(public_members),
                "unit": bundle["unit"],
            }
        )
    return index, bundles, blocked


def build_website_export(connection: sqlite3.Connection) -> dict[str, Any]:
    """Assemble the deterministic public export document in memory (no file I/O)."""
    meta = dict(connection.execute("SELECT * FROM graph_meta WHERE singleton_id=1").fetchone())
    public_ids = _public_item_ids(connection)
    entity_labels = _entity_labels(connection)
    unit_titles = _unit_titles(connection)
    edges = _public_edges(connection, public_ids)

    findings: list[dict[str, Any]] = []
    for row in connection.execute(
        "SELECT * FROM research_items WHERE visibility='public' ORDER BY item_id"
    ):
        findings.append(
            _finding(connection, row, entity_labels=entity_labels,
                     unit_titles=unit_titles, edges=edges)
        )

    index = [
        {
            "id": f["id"],
            "url": f"/research/findings/{f['id'].lower()}/",
            "kind": f["kind"],
            "kindLabel": f["kindLabel"],
            "shortLabel": f["shortLabel"],
            "statement": f["statement"],
            "status": f["status"],
            "confidence": f["confidence"],
            "unit": f["unit"],
        }
        for f in findings
    ]
    marker_index, marker_bundles, blocked_markers = _public_marker_exports(
        connection, findings, unit_titles
    )
    content_hash = sha256_json(
        {
            "findings": findings,
            "adjacency": edges,
            "markers": marker_index,
            "marker_bundles": marker_bundles,
        }
    )
    manifest = {
        "format": "gurney-g13-website",
        "format_version": 1,
        "schema_version": meta["schema_version"],
        "database_revision": meta["database_revision"],
        # Revision's committed timestamp → byte-stable re-exports.
        "generated_from_revision_at": meta["updated_at"],
        "counts": {
            "public_findings": len(findings),
            "public_edges": len(edges),
            "public_markers": len(marker_index),
        },
        "content_hash": content_hash,
    }
    return {
        "manifest": manifest,
        "findings": findings,
        "index": index,
        "adjacency": edges,
        "markers": marker_index,
        "marker_bundles": marker_bundles,
        "blocked_markers": blocked_markers,
    }


def _finding_fallback(finding: dict[str, Any]) -> str:
    title = finding["shortLabel"] or finding["statement"]
    sources = "".join(
        "<li>"
        + escape(source["sourceId"])
        + (f" — {escape(source['locator'])}" if source.get("locator") else "")
        + "</li>"
        for source in finding["sources"]
    )
    return (
        "<!doctype html>\n"
        '<html lang="en"><meta charset="utf-8">'
        f"<title>{escape(title)}</title>"
        f"<main><h1>{escape(title)}</h1>"
        f"<p>{escape(finding['statement'])}</p>"
        f"<p>Type: {escape(finding['kindLabel'])}</p>"
        + (f"<h2>Sources</h2><ul>{sources}</ul>" if sources else "")
        + "</main></html>\n"
    )


def _marker_fallback(bundle: dict[str, Any]) -> str:
    primary = bundle["primary"]
    title = primary["shortLabel"] or primary["statement"]
    role_labels = {
        "primary": "Primary finding",
        "expressed": "Also expressed",
        "contextual": "Additional context",
    }
    items = "".join(
        "<li>"
        f"<a href=\"/research/findings/{entry['finding']['id'].lower()}/\">"
        f"{escape(entry['finding']['shortLabel'] or entry['finding']['statement'])}</a>"
        f" — {escape(role_labels[entry['role']])}</li>"
        for entry in bundle["items"]
    )
    return (
        "<!doctype html>\n"
        '<html lang="en"><meta charset="utf-8">'
        f"<title>Evidence — {escape(title)}</title>"
        f"<main><h1>Evidence — {escape(title)}</h1>"
        f"<p>{escape(primary['statement'])}</p>"
        f"<h2>Mapped findings</h2><ul>{items}</ul>"
        "</main></html>\n"
    )


def export_website(config: GraphConfig, out_dir: Path | None = None) -> Path:
    """Write the static website export under ``out_dir`` (default
    ``<export_dir>/website``). Returns the output directory. Read-only w.r.t. the
    database, prose, and sources."""
    target = out_dir or (config.export_dir / "website")
    connection = connect(config.db_path, read_only=True)
    try:
        document = build_website_export(connection)
    finally:
        connection.close()
    if document["blocked_markers"]:
        raise PublicMarkerExportError(document["blocked_markers"])

    # These trees are wholly derived. Prune them only after the new build has
    # passed fail-closed checks so visibility changes cannot leave stale pages.
    for relative in (
        Path("findings"),
        Path("marker-bundles"),
        Path("research") / "evidence",
        Path("research") / "findings",
    ):
        path = target / relative
        if path.exists():
            shutil.rmtree(path)

    def write(rel: str, value: Any) -> None:
        atomic_write((target / rel), (canonical_json(value) + "\n").encode("utf-8"))

    write("manifest.json", document["manifest"])
    write("findings.json", document["index"])
    write("markers.json", document["markers"])
    write("adjacency.json", {
        "nodes": [
            {"id": f["id"], "kind": f["kind"], "kindLabel": f["kindLabel"],
             "shortLabel": f["shortLabel"]}
            for f in document["findings"]
        ],
        "edges": document["adjacency"],
    })
    for finding in document["findings"]:
        write(f"findings/{finding['id']}.json", finding)
        atomic_write(
            target / "research" / "findings" / finding["id"].lower() / "index.html",
            _finding_fallback(finding).encode("utf-8"),
        )
    for bundle in document["marker_bundles"]:
        write(f"marker-bundles/{bundle['id']}.json", bundle)
        atomic_write(
            target / "research" / "evidence" / bundle["id"].lower() / "index.html",
            _marker_fallback(bundle).encode("utf-8"),
        )
    return target
