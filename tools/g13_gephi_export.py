#!/usr/bin/env python3
"""Export the canonical G13 SQLite context graph for Gephi Desktop.

This is a read-only analytical export. It does not modify the database and is
not an editing or restore format. Two views are available:

* ``research-flow``: research items and explicit item-to-item relations.
* ``provenance``: the research flow plus linked sources, entities, research
  units, prose markers, and soft evidence groups.

The output is deterministic for an unchanged database revision. Relation
strength and confidence are exported as categorical attributes, never as GEXF
weights or calculated probabilities.
"""

from __future__ import annotations

import argparse
import sqlite3
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping, Sequence

if __package__:
    from tools.g13_graph.config import DEFAULT_DB, find_repo_root
    from tools.g13_graph.util import atomic_write
else:
    from g13_graph.config import DEFAULT_DB, find_repo_root
    from g13_graph.util import atomic_write


GEXF_NS = "http://gexf.net/1.3"
XSI_NS = "http://www.w3.org/2001/XMLSchema-instance"
SCHEMA_LOCATION = "http://gexf.net/1.3 https://gexf.net/1.3/gexf.xsd"
VIEWS = ("research-flow", "provenance")

ET.register_namespace("", GEXF_NS)
ET.register_namespace("xsi", XSI_NS)


class GephiExportError(RuntimeError):
    """The database cannot be represented as a valid Gephi export."""


@dataclass(frozen=True)
class GraphNode:
    node_id: str
    label: str
    attributes: Mapping[str, str | int | float | bool | None]


@dataclass(frozen=True)
class GraphEdge:
    source: str
    target: str
    label: str
    attributes: Mapping[str, str | int | float | bool | None]


@dataclass(frozen=True)
class GraphExport:
    view: str
    database_revision: int
    schema_version: int
    updated_at: str
    nodes: tuple[GraphNode, ...]
    edges: tuple[GraphEdge, ...]


@dataclass(frozen=True)
class ExportResult:
    path: Path
    view: str
    database_revision: int
    node_count: int
    edge_count: int


NODE_ATTRIBUTES = (
    ("record_id", "Record ID", "string"),
    ("node_type", "Node type", "string"),
    ("item_kind", "Item kind", "string"),
    ("entity_type", "Entity type", "string"),
    ("status", "Status", "string"),
    ("review_state", "Review state", "string"),
    ("visibility", "Visibility", "string"),
    ("confidence_label", "Confidence band", "string"),
    ("research_unit_id", "Research unit ID", "string"),
    ("research_unit_title", "Research unit title", "string"),
    ("statement", "Statement", "string"),
    ("description", "Description", "string"),
    ("repo_path", "Repository path", "string"),
    ("heading_id", "Heading ID", "string"),
    ("canonical_path", "Canonical source path", "string"),
    ("primary_item_id", "Primary item ID", "string"),
    ("date_summary", "Date summary", "string"),
    ("chronology_key", "Chronology key", "double"),
    ("source_count", "Linked source count", "integer"),
    ("entity_count", "Linked entity count", "integer"),
    ("incoming_relation_count", "Incoming relation count", "integer"),
    ("outgoing_relation_count", "Outgoing relation count", "integer"),
    ("marker_count", "Prose marker count", "integer"),
    ("publication_count", "Publication mapping count", "integer"),
)

EDGE_ATTRIBUTES = (
    ("edge_class", "Edge class", "string"),
    ("relation_type", "Relation type", "string"),
    ("role", "Role", "string"),
    ("bearing", "Bearing", "string"),
    ("strength", "Strength", "string"),
    ("review_state", "Review state", "string"),
    ("explanation", "Explanation", "string"),
    ("locator", "Source locator", "string"),
    ("verification_level", "Verification level", "string"),
)


def _tag(name: str) -> str:
    return f"{{{GEXF_NS}}}{name}"


def _clean_label(value: str | None, fallback: str, limit: int = 140) -> str:
    text = " ".join((value or fallback).split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def _stringify(value: object) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def _connect_read_only(db_path: Path) -> sqlite3.Connection:
    if not db_path.is_file():
        raise GephiExportError(f"G13 graph database does not exist: {db_path}")
    uri = f"{db_path.resolve().as_uri()}?mode=ro"
    connection = sqlite3.connect(uri, uri=True, timeout=5.0)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA query_only=ON")
    return connection


def _rows(
    connection: sqlite3.Connection, sql: str, parameters: Sequence[object] = ()
) -> list[dict[str, object]]:
    return [dict(row) for row in connection.execute(sql, parameters)]


def _date_details(
    rows: Iterable[Mapping[str, object]],
) -> tuple[dict[str, str], dict[str, float]]:
    summaries: dict[str, list[str]] = {}
    chronology: dict[str, float] = {}
    for row in rows:
        item_id = str(row["item_id"])
        display = row.get("original_display")
        if display:
            rendered = str(display)
        else:
            plausible = "..".join(
                str(value or "?")
                for value in (row.get("plausible_start"), row.get("plausible_end"))
            )
            probable_values = (row.get("probable_start"), row.get("probable_end"))
            rendered = f"plausible {plausible}"
            if any(probable_values):
                probable = "..".join(str(value or "?") for value in probable_values)
                rendered += f"; probable {probable}"
        summaries.setdefault(item_id, []).append(f"{row['date_role']}: {rendered}")
        key = row.get("chronology_key")
        if key is not None and item_id not in chronology:
            chronology[item_id] = float(key)
    return (
        {item_id: " | ".join(values) for item_id, values in summaries.items()},
        chronology,
    )


def _item_node_id(item_id: object) -> str:
    return str(item_id)


def _source_node_id(source_id: object) -> str:
    return f"source:{source_id}"


def _entity_node_id(entity_id: object) -> str:
    return f"entity:{entity_id}"


def _unit_node_id(unit_id: object) -> str:
    return f"unit:{unit_id}"


def _marker_node_id(marker_id: object) -> str:
    return f"marker:{marker_id}"


def _group_node_id(group_id: object) -> str:
    return f"evidence-group:{group_id}"


def build_graph_export(db_path: Path, view: str) -> GraphExport:
    """Read one consistent SQLite snapshot and assemble a Gephi graph."""
    if view not in VIEWS:
        raise GephiExportError(f"Unknown view {view!r}; expected one of {VIEWS}.")

    connection = _connect_read_only(db_path)
    try:
        connection.execute("BEGIN")
        meta_rows = _rows(
            connection,
            "SELECT schema_version, database_revision, updated_at "
            "FROM graph_meta WHERE singleton_id=1",
        )
        if len(meta_rows) != 1:
            raise GephiExportError("graph_meta must contain exactly one singleton row.")
        meta = meta_rows[0]

        units = _rows(connection, "SELECT * FROM research_units ORDER BY unit_id")
        items = _rows(connection, "SELECT * FROM research_items ORDER BY item_id")
        relations = _rows(
            connection,
            "SELECT * FROM item_relations "
            "ORDER BY from_item_id, relation_type, to_item_id",
        )
        item_sources = _rows(
            connection,
            "SELECT * FROM item_sources "
            "ORDER BY item_id, source_id, role, locator",
        )
        item_entities = _rows(
            connection,
            "SELECT * FROM item_entities ORDER BY item_id, entity_id, role",
        )
        marker_items = _rows(
            connection,
            "SELECT * FROM prose_marker_items "
            "ORDER BY marker_id, display_order, item_id",
        )
        publications = _rows(
            connection,
            "SELECT item_id FROM item_publications ORDER BY item_id, publication_id",
        )
        dates = _rows(
            connection,
            "SELECT * FROM item_dates ORDER BY item_id, date_role",
        )

        unit_by_id = {str(row["unit_id"]): row for row in units}
        item_by_id = {str(row["item_id"]): row for row in items}
        date_summaries, chronology_keys = _date_details(dates)
        source_counts = Counter(str(row["item_id"]) for row in item_sources)
        entity_counts = Counter(str(row["item_id"]) for row in item_entities)
        marker_counts = Counter(str(row["item_id"]) for row in marker_items)
        publication_counts = Counter(str(row["item_id"]) for row in publications)
        outgoing_counts = Counter(str(row["from_item_id"]) for row in relations)
        incoming_counts = Counter(str(row["to_item_id"]) for row in relations)

        nodes: list[GraphNode] = []
        for row in items:
            item_id = str(row["item_id"])
            unit_id = str(row["research_unit_id"])
            unit = unit_by_id.get(unit_id, {})
            nodes.append(
                GraphNode(
                    node_id=_item_node_id(item_id),
                    label=_clean_label(
                        row.get("short_label"), str(row["statement"])
                    ),
                    attributes={
                        "record_id": item_id,
                        "node_type": "research_item",
                        "item_kind": row["item_kind"],
                        "status": row["status"],
                        "review_state": row["review_state"],
                        "visibility": row["visibility"],
                        "confidence_label": row["assessment_confidence_label"],
                        "research_unit_id": unit_id,
                        "research_unit_title": unit.get("title"),
                        "statement": row["statement"],
                        "date_summary": date_summaries.get(item_id),
                        "chronology_key": chronology_keys.get(item_id),
                        "source_count": source_counts[item_id],
                        "entity_count": entity_counts[item_id],
                        "incoming_relation_count": incoming_counts[item_id],
                        "outgoing_relation_count": outgoing_counts[item_id],
                        "marker_count": marker_counts[item_id],
                        "publication_count": publication_counts[item_id],
                    },
                )
            )

        edges: list[GraphEdge] = [
            GraphEdge(
                source=_item_node_id(row["from_item_id"]),
                target=_item_node_id(row["to_item_id"]),
                label=str(row["relation_type"]),
                attributes={
                    "edge_class": "item_relation",
                    "relation_type": row["relation_type"],
                    "bearing": row["bearing"],
                    "strength": row["strength"],
                    "review_state": row["review_state"],
                    "explanation": row["explanation"],
                },
            )
            for row in relations
        ]

        if view == "provenance":
            linked_source_ids = sorted({str(row["source_id"]) for row in item_sources})
            linked_entity_ids = sorted({str(row["entity_id"]) for row in item_entities})
            markers = _rows(
                connection, "SELECT * FROM prose_markers ORDER BY marker_id"
            )
            evidence_groups = _rows(
                connection,
                "SELECT * FROM evidence_groups ORDER BY evidence_group_id",
            )
            group_items = _rows(
                connection,
                "SELECT * FROM evidence_group_items "
                "ORDER BY evidence_group_id, item_id, role",
            )
            group_sources = _rows(
                connection,
                "SELECT * FROM evidence_group_sources "
                "ORDER BY evidence_group_id, source_id, role, locator",
            )

            source_ids = linked_source_ids + sorted(
                {str(row["source_id"]) for row in group_sources}
                - set(linked_source_ids)
            )
            sources: list[dict[str, object]] = []
            if source_ids:
                placeholders = ",".join("?" for _ in source_ids)
                sources = _rows(
                    connection,
                    f"SELECT * FROM source_registry WHERE source_id IN ({placeholders}) "
                    "ORDER BY source_id",
                    source_ids,
                )
            entities: list[dict[str, object]] = []
            if linked_entity_ids:
                placeholders = ",".join("?" for _ in linked_entity_ids)
                entities = _rows(
                    connection,
                    f"SELECT * FROM entities WHERE entity_id IN ({placeholders}) "
                    "ORDER BY entity_id",
                    linked_entity_ids,
                )

            for row in sources:
                source_id = str(row["source_id"])
                nodes.append(
                    GraphNode(
                        node_id=_source_node_id(source_id),
                        label=_clean_label(
                            str(row["display_title"]), source_id
                        ),
                        attributes={
                            "record_id": source_id,
                            "node_type": "source",
                            "description": row["display_title"],
                            "canonical_path": row["canonical_path"],
                        },
                    )
                )
            for row in entities:
                entity_id = str(row["entity_id"])
                nodes.append(
                    GraphNode(
                        node_id=_entity_node_id(entity_id),
                        label=_clean_label(
                            str(row["canonical_label"]), entity_id
                        ),
                        attributes={
                            "record_id": entity_id,
                            "node_type": "entity",
                            "entity_type": row["entity_type"],
                            "description": row["description"],
                        },
                    )
                )
            for row in units:
                unit_id = str(row["unit_id"])
                nodes.append(
                    GraphNode(
                        node_id=_unit_node_id(unit_id),
                        label=_clean_label(str(row["title"]), unit_id),
                        attributes={
                            "record_id": unit_id,
                            "node_type": "research_unit",
                            "review_state": row["review_state"],
                            "description": row["scope_summary"],
                            "repo_path": row["path"],
                            "heading_id": row["heading_id"],
                        },
                    )
                )
            for row in markers:
                marker_id = str(row["marker_id"])
                primary = item_by_id.get(str(row["primary_item_id"]), {})
                primary_label = _clean_label(
                    primary.get("short_label"),
                    str(primary.get("statement") or marker_id),
                    limit=110,
                )
                nodes.append(
                    GraphNode(
                        node_id=_marker_node_id(marker_id),
                        label=f"Marker: {primary_label}",
                        attributes={
                            "record_id": marker_id,
                            "node_type": "prose_marker",
                            "status": row["status"],
                            "visibility": row["visibility"],
                            "research_unit_id": row["research_unit_id"],
                            "primary_item_id": row["primary_item_id"],
                        },
                    )
                )
            for row in evidence_groups:
                group_id = str(row["evidence_group_id"])
                nodes.append(
                    GraphNode(
                        node_id=_group_node_id(group_id),
                        label=f"Evidence group: {group_id}",
                        attributes={
                            "record_id": group_id,
                            "node_type": "evidence_group",
                            "research_unit_id": row["research_unit_id"],
                            "description": row["explanation"],
                            "heading_id": row["heading_id"],
                        },
                    )
                )

            edges.extend(
                GraphEdge(
                    source=_source_node_id(row["source_id"]),
                    target=_item_node_id(row["item_id"]),
                    label=f"source:{row['role']}",
                    attributes={
                        "edge_class": "item_source",
                        "role": row["role"],
                        "locator": row["locator"],
                        "verification_level": row["verification_level"],
                        "explanation": row["alignment_note"],
                    },
                )
                for row in item_sources
            )
            edges.extend(
                GraphEdge(
                    source=_entity_node_id(row["entity_id"]),
                    target=_item_node_id(row["item_id"]),
                    label=f"entity:{row['role']}",
                    attributes={
                        "edge_class": "item_entity",
                        "role": row["role"],
                    },
                )
                for row in item_entities
            )
            edges.extend(
                GraphEdge(
                    source=_unit_node_id(row["research_unit_id"]),
                    target=_item_node_id(row["item_id"]),
                    label="contains",
                    attributes={
                        "edge_class": "unit_item",
                        "role": "contains",
                    },
                )
                for row in items
            )
            edges.extend(
                GraphEdge(
                    source=_marker_node_id(row["marker_id"]),
                    target=_item_node_id(row["item_id"]),
                    label=f"marker:{row['marker_role']}",
                    attributes={
                        "edge_class": "marker_item",
                        "role": row["marker_role"],
                    },
                )
                for row in marker_items
            )
            edges.extend(
                GraphEdge(
                    source=_group_node_id(row["evidence_group_id"]),
                    target=_item_node_id(row["item_id"]),
                    label=f"evidence-group:{row['role']}",
                    attributes={
                        "edge_class": "evidence_group_item",
                        "role": row["role"],
                    },
                )
                for row in group_items
            )
            edges.extend(
                GraphEdge(
                    source=_source_node_id(row["source_id"]),
                    target=_group_node_id(row["evidence_group_id"]),
                    label=f"evidence-group-source:{row['role']}",
                    attributes={
                        "edge_class": "evidence_group_source",
                        "role": row["role"],
                        "locator": row["locator"],
                    },
                )
                for row in group_sources
            )
            edges.extend(
                GraphEdge(
                    source=_unit_node_id(row["research_unit_id"]),
                    target=_group_node_id(row["evidence_group_id"]),
                    label="contains",
                    attributes={
                        "edge_class": "unit_evidence_group",
                        "role": "contains",
                    },
                )
                for row in evidence_groups
            )

        connection.rollback()
    except sqlite3.Error as exc:
        raise GephiExportError(f"Could not read the G13 graph: {exc}") from exc
    finally:
        connection.close()

    nodes.sort(key=lambda node: node.node_id)
    edges.sort(
        key=lambda edge: (
            str(edge.attributes.get("edge_class") or ""),
            edge.source,
            edge.target,
            edge.label,
            str(edge.attributes.get("role") or ""),
            str(edge.attributes.get("locator") or ""),
        )
    )
    graph = GraphExport(
        view=view,
        database_revision=int(meta["database_revision"]),
        schema_version=int(meta["schema_version"]),
        updated_at=str(meta["updated_at"]),
        nodes=tuple(nodes),
        edges=tuple(edges),
    )
    validate_graph_export(graph)
    return graph


def validate_graph_export(graph: GraphExport) -> None:
    """Reject duplicate IDs, dangling endpoints, or unsupported attributes."""
    node_ids = [node.node_id for node in graph.nodes]
    if len(node_ids) != len(set(node_ids)):
        duplicates = sorted(
            node_id for node_id, count in Counter(node_ids).items() if count > 1
        )
        raise GephiExportError(f"Duplicate Gephi node IDs: {duplicates}")
    node_id_set = set(node_ids)
    for edge in graph.edges:
        if edge.source not in node_id_set or edge.target not in node_id_set:
            raise GephiExportError(
                f"Dangling Gephi edge endpoint: {edge.source} -> {edge.target}"
            )

    allowed_node = {attribute_id for attribute_id, _, _ in NODE_ATTRIBUTES}
    allowed_edge = {attribute_id for attribute_id, _, _ in EDGE_ATTRIBUTES}
    for node in graph.nodes:
        unknown = set(node.attributes) - allowed_node
        if unknown:
            raise GephiExportError(
                f"Unknown node attribute(s) on {node.node_id}: {sorted(unknown)}"
            )
    for edge in graph.edges:
        unknown = set(edge.attributes) - allowed_edge
        if unknown:
            raise GephiExportError(
                f"Unknown edge attribute(s) on {edge.source}->{edge.target}: "
                f"{sorted(unknown)}"
            )


def render_gexf(graph: GraphExport) -> bytes:
    """Serialize a validated graph as deterministic GEXF 1.3 XML."""
    validate_graph_export(graph)
    root = ET.Element(
        _tag("gexf"),
        {
            "version": "1.3",
            f"{{{XSI_NS}}}schemaLocation": SCHEMA_LOCATION,
        },
    )
    meta = ET.SubElement(
        root,
        _tag("meta"),
        {"lastmodifieddate": graph.updated_at[:10]},
    )
    ET.SubElement(meta, _tag("creator")).text = "gurney-genealogy"
    ET.SubElement(meta, _tag("description")).text = (
        f"G13 SQLite context graph; {graph.view} view; "
        f"database revision {graph.database_revision}; read-only derived export"
    )
    graph_element = ET.SubElement(
        root,
        _tag("graph"),
        {
            "defaultedgetype": "directed",
            "mode": "static",
            "name": f"G13 context graph — {graph.view}",
        },
    )

    node_attributes = ET.SubElement(
        graph_element, _tag("attributes"), {"class": "node", "mode": "static"}
    )
    for attribute_id, title, attribute_type in NODE_ATTRIBUTES:
        ET.SubElement(
            node_attributes,
            _tag("attribute"),
            {"id": attribute_id, "title": title, "type": attribute_type},
        )
    edge_attributes = ET.SubElement(
        graph_element, _tag("attributes"), {"class": "edge", "mode": "static"}
    )
    for attribute_id, title, attribute_type in EDGE_ATTRIBUTES:
        ET.SubElement(
            edge_attributes,
            _tag("attribute"),
            {"id": attribute_id, "title": title, "type": attribute_type},
        )

    nodes_element = ET.SubElement(
        graph_element, _tag("nodes"), {"count": str(len(graph.nodes))}
    )
    for node in graph.nodes:
        node_element = ET.SubElement(
            nodes_element,
            _tag("node"),
            {"id": node.node_id, "label": node.label},
        )
        attvalues = ET.SubElement(node_element, _tag("attvalues"))
        for attribute_id, _, _ in NODE_ATTRIBUTES:
            value = node.attributes.get(attribute_id)
            if value is None or value == "":
                continue
            ET.SubElement(
                attvalues,
                _tag("attvalue"),
                {"for": attribute_id, "value": _stringify(value)},
            )

    edges_element = ET.SubElement(
        graph_element, _tag("edges"), {"count": str(len(graph.edges))}
    )
    for index, edge in enumerate(graph.edges, start=1):
        edge_element = ET.SubElement(
            edges_element,
            _tag("edge"),
            {
                "id": f"e{index:06d}",
                "source": edge.source,
                "target": edge.target,
                "label": edge.label,
            },
        )
        attvalues = ET.SubElement(edge_element, _tag("attvalues"))
        for attribute_id, _, _ in EDGE_ATTRIBUTES:
            value = edge.attributes.get(attribute_id)
            if value is None or value == "":
                continue
            ET.SubElement(
                attvalues,
                _tag("attvalue"),
                {"for": attribute_id, "value": _stringify(value)},
            )

    ET.indent(root, space="  ")
    content = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    # Parse our own output before it reaches disk.
    ET.fromstring(content)
    return content + b"\n"


def export_view(db_path: Path, out_dir: Path, view: str) -> ExportResult:
    graph = build_graph_export(db_path, view)
    filename = (
        f"g13-{view}-r{graph.database_revision:06d}.gexf"
    )
    target = out_dir.resolve() / filename
    atomic_write(target, render_gexf(graph))
    return ExportResult(
        path=target,
        view=view,
        database_revision=graph.database_revision,
        node_count=len(graph.nodes),
        edge_count=len(graph.edges),
    )


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Export the canonical G13 SQLite context graph for Gephi."
    )
    parser.add_argument(
        "--db",
        type=Path,
        default=DEFAULT_DB,
        help=f"SQLite database path (default: {DEFAULT_DB})",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=None,
        help=(
            "Output directory (default: "
            "data/context-graphs/g13/exports/gephi under the repository root)"
        ),
    )
    parser.add_argument(
        "--view",
        choices=(*VIEWS, "both"),
        default="both",
        help="Graph view to export (default: both).",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    out_dir = (
        args.out_dir
        if args.out_dir is not None
        else find_repo_root() / "data/context-graphs/g13/exports/gephi"
    )
    views = VIEWS if args.view == "both" else (args.view,)
    try:
        results = [
            export_view(args.db.resolve(), out_dir.resolve(), view)
            for view in views
        ]
    except GephiExportError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    for result in results:
        print(
            f"{result.view}: {result.path} "
            f"({result.node_count} nodes, {result.edge_count} edges, "
            f"revision {result.database_revision})"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
