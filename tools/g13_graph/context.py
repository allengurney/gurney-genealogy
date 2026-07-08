"""Phase G2 context compiler for the canonical G13 graph.

The compiler selects active/open seed items, expands their graph
neighbourhood deterministically, and emits a budget-aware package with a
lossless coverage ledger. Budget pressure may remove detail, but never item
identifiers, short statements, conflict records, negative-result limitations,
or omission notices.
"""

from __future__ import annotations

import json
from collections import deque
from dataclasses import dataclass
from typing import Any, Callable

from .config import GraphConfig
from .constants import RELATION_TYPES
from .db import connect
from .drift import source_hash_state
from .util import canonical_json

CONCLUSION_KINDS = (
    "research_finding",
    "analysis",
    "identity_hypothesis",
    "evidence_conflict",
    "project_statement",
    "published_source_statement",
    "open_question",
)

# None means traverse the complete connected component.
MODE_MAX_HOPS: dict[str, int | None] = {
    "grounding": 1,
    "research": 2,
    "audit": None,
    "exhaustive": None,
}

# Plan 01 §12. The order is part of the public compiler contract.
TRIM_ORDER = (
    "evidence_excerpts",
    "context_only_detail",
    "low_bearing_related_entities",
    "full_source_citations",
)

PROTECTED_KINDS = ("evidence_conflict", "negative_result")


@dataclass(frozen=True)
class _Selection:
    seeds: set[str]
    included: set[str]
    distances: dict[str, int]
    expansion_reasons: dict[str, list[str]]
    matched_entity_ids: set[str]
    missing_item_ids: set[str]
    inactive_item_ids: set[str]
    missing_entity_ids: set[str]


def _normalise_relation_types(values: list[str] | None) -> tuple[str, ...]:
    if values is None:
        return RELATION_TYPES
    normalised = tuple(dict.fromkeys(value.strip().upper() for value in values if value.strip()))
    unknown = sorted(set(normalised) - set(RELATION_TYPES))
    if unknown:
        raise ValueError("Unknown relation type(s): " + ", ".join(unknown))
    return normalised


def _normalise_match(value: str) -> str:
    match = value.strip().lower()
    if match not in {"any", "all"}:
        raise ValueError("Match must be 'any' or 'all'.")
    return match


def _term_match(haystack: str, terms: list[str], match: str) -> bool:
    checks = [term.casefold() in haystack for term in terms]
    return any(checks) if match == "any" else all(checks)


def _matches(item: dict[str, Any], terms: list[str], match: str) -> bool:
    haystack = " ".join(
        str(item.get(field) or "")
        for field in (
            "statement",
            "short_label",
            "summary",
            "qualifiers_json",
            "tags_json",
        )
    ).casefold()
    return _term_match(haystack, terms, match)


def _matching_entities(
    connection: Any, terms: list[str], explicit_ids: list[str], match: str
) -> tuple[set[str], set[str]]:
    known_ids = {
        row["entity_id"]
        for row in connection.execute("SELECT entity_id FROM entities")
    }
    matched = set(explicit_ids) & known_ids
    if terms:
        for row in connection.execute(
            """
            SELECT e.entity_id, e.canonical_label, e.description,
                   group_concat(a.alias, ' ') AS aliases
            FROM entities AS e
            LEFT JOIN entity_aliases AS a ON a.entity_id=e.entity_id
            GROUP BY e.entity_id
            ORDER BY e.entity_id
            """
        ):
            text = " ".join(
                str(row[field] or "")
                for field in ("canonical_label", "description", "aliases")
            ).casefold()
            if _term_match(text, terms, match):
                matched.add(row["entity_id"])
    return matched, set(explicit_ids) - known_ids


def _items_for_entities(
    connection: Any, entity_ids: set[str], active_ids: set[str]
) -> set[str]:
    if not entity_ids:
        return set()
    placeholders = ",".join("?" for _ in entity_ids)
    values = tuple(sorted(entity_ids))
    rows = connection.execute(
        f"""
        SELECT item_id FROM research_items
        WHERE subject_entity_id IN ({placeholders})
        UNION
        SELECT item_id FROM item_entities
        WHERE entity_id IN ({placeholders})
        """,
        values + values,
    )
    return {row["item_id"] for row in rows} & active_ids


def _select_scope(
    connection: Any,
    active_items: dict[str, dict[str, Any]],
    *,
    terms: list[str],
    ids: list[str],
    entity_ids: list[str],
    relation_types: tuple[str, ...],
    mode: str,
    match: str,
) -> _Selection:
    active_ids = set(active_items)
    known_item_ids = {
        row["item_id"]
        for row in connection.execute("SELECT item_id FROM research_items")
    }
    explicit_seeds = set(ids) & active_ids
    inactive_item_ids = (set(ids) & known_item_ids) - active_ids
    term_seeds = {
        item_id
        for item_id, item in active_items.items()
        if terms and _matches(item, terms, match)
    }
    matched_entities, missing_entities = _matching_entities(
        connection, terms, entity_ids, match
    )
    entity_seeds = _items_for_entities(connection, matched_entities, active_ids)
    seeds = explicit_seeds | term_seeds | entity_seeds

    if mode == "exhaustive":
        included = set(active_ids)
    else:
        included = set(seeds)

    adjacency: dict[str, list[tuple[str, str, str, str]]] = {
        item_id: [] for item_id in active_ids
    }
    allowed = set(relation_types)
    for row in connection.execute(
        """
        SELECT from_item_id, relation_type, to_item_id, bearing, strength
        FROM item_relations
        WHERE review_state NOT IN ('rejected', 'superseded')
        ORDER BY from_item_id, relation_type, to_item_id
        """
    ):
        source = row["from_item_id"]
        target = row["to_item_id"]
        relation_type = row["relation_type"]
        if source not in active_ids or target not in active_ids or relation_type not in allowed:
            continue
        adjacency[source].append(
            (target, relation_type, "out", row["bearing"])
        )
        adjacency[target].append(
            (source, relation_type, "in", row["bearing"])
        )

    distances = {item_id: 0 for item_id in seeds}
    reasons: dict[str, list[str]] = {}
    queue = deque(sorted(seeds))
    maximum = MODE_MAX_HOPS[mode]
    while queue:
        current = queue.popleft()
        distance = distances[current]
        if maximum is not None and distance >= maximum:
            continue
        for other, relation_type, direction, bearing in adjacency[current]:
            candidate_distance = distance + 1
            explanation = (
                f"hop {candidate_distance}: {relation_type} "
                f"{'from' if direction == 'out' else 'to'} {current} "
                f"({bearing})"
            )
            if other not in distances:
                distances[other] = candidate_distance
                reasons[other] = [explanation]
                included.add(other)
                queue.append(other)
            elif distances[other] == candidate_distance and other not in seeds:
                reasons.setdefault(other, []).append(explanation)

    return _Selection(
        seeds=seeds,
        included=included,
        distances=distances,
        expansion_reasons={
            item_id: sorted(set(values)) for item_id, values in reasons.items()
        },
        matched_entity_ids=matched_entities,
        missing_item_ids=set(ids) - known_item_ids,
        inactive_item_ids=inactive_item_ids,
        missing_entity_ids=missing_entities,
    )


def _source_states(connection: Any, config: GraphConfig) -> dict[str, str]:
    return {
        row["source_id"]: row["state"]
        for row in source_hash_state(connection, config)["sources"]
    }


def _item_record(
    connection: Any,
    item: dict[str, Any],
    *,
    role: str,
    distance: int | None,
    reasons: list[str],
    included_ids: set[str],
    relation_types: set[str],
    source_states: dict[str, str],
) -> dict[str, Any]:
    item_id = item["item_id"]
    unit = connection.execute(
        "SELECT * FROM research_units WHERE unit_id=?",
        (item["research_unit_id"],),
    ).fetchone()
    sources = [
        {
            "source_id": row["source_id"],
            "role": row["role"],
            "locator": row["locator"],
            "display_title": row["display_title"],
            "canonical_path": row["canonical_path"],
            "evidence_excerpt": row["evidence_excerpt"],
            "alignment_note": row["alignment_note"],
            "verification_level": row["verification_level"],
            "source_hash_state": source_states.get(row["source_id"], "not_cited"),
        }
        for row in connection.execute(
            """
            SELECT s.*, r.display_title, r.canonical_path
            FROM item_sources AS s
            JOIN source_registry AS r ON r.source_id=s.source_id
            WHERE s.item_id=?
            ORDER BY s.source_id, s.role, s.locator
            """,
            (item_id,),
        )
    ]
    relations: list[dict[str, Any]] = []
    for row in connection.execute(
        """
        SELECT * FROM item_relations
        WHERE (from_item_id=? OR to_item_id=?)
          AND review_state NOT IN ('rejected', 'superseded')
        ORDER BY relation_type, from_item_id, to_item_id
        """,
        (item_id, item_id),
    ):
        relation_type = row["relation_type"]
        if relation_type not in relation_types:
            continue
        outgoing = row["from_item_id"] == item_id
        other = row["to_item_id"] if outgoing else row["from_item_id"]
        if other not in included_ids:
            continue
        relations.append(
            {
                "direction": "out" if outgoing else "in",
                "relation_type": relation_type,
                "other": other,
                "bearing": row["bearing"],
                "strength": row["strength"],
                "explanation": row["explanation"],
                "review_state": row["review_state"],
            }
        )
    entities = [
        {
            "entity_id": row["entity_id"],
            "entity_type": row["entity_type"],
            "canonical_label": row["canonical_label"],
            "description": row["description"],
            "role": row["role"],
        }
        for row in connection.execute(
            """
            SELECT e.*, links.role
            FROM (
                SELECT item_id, entity_id, role FROM item_entities
                UNION
                SELECT item_id, subject_entity_id, 'subject'
                FROM research_items WHERE subject_entity_id IS NOT NULL
            ) AS links
            JOIN entities AS e ON e.entity_id=links.entity_id
            WHERE links.item_id=?
            ORDER BY e.entity_id, links.role
            """,
            (item_id,),
        )
    ]
    evidence_groups = []
    for group in connection.execute(
        """
        SELECT g.*, gi.role AS item_role
        FROM evidence_group_items AS gi
        JOIN evidence_groups AS g ON g.evidence_group_id=gi.evidence_group_id
        WHERE gi.item_id=?
        ORDER BY g.evidence_group_id
        """,
        (item_id,),
    ):
        group_record = dict(group)
        group_sources = []
        for source in connection.execute(
            """
            SELECT * FROM evidence_group_sources
            WHERE evidence_group_id=?
            ORDER BY source_id, role, locator
            """,
            (group["evidence_group_id"],),
        ):
            registry = connection.execute(
                """
                SELECT display_title, canonical_path
                FROM source_registry WHERE source_id=?
                """,
                (source["source_id"],),
            ).fetchone()
            group_sources.append(
                {
                    **dict(source),
                    "display_title": registry["display_title"],
                    "canonical_path": registry["canonical_path"],
                    "source_hash_state": source_states.get(
                        source["source_id"], "not_cited"
                    ),
                }
            )
        group_record["sources"] = group_sources
        evidence_groups.append(group_record)
    record: dict[str, Any] = {
        "item_id": item_id,
        "item_kind": item["item_kind"],
        "role_in_context": role,
        "graph_distance": distance,
        "expansion_reasons": reasons,
        "short_statement": item["short_label"] or item["statement"],
        "statement": item["statement"],
        "summary": item["summary"],
        "status": item["status"],
        "confidence_label": item["assessment_confidence_label"],
        "visibility": item["visibility"],
        "review_state": item["review_state"],
        "reviewed_at": item["reviewed_at"],
        "knowledge_valid_to": item["knowledge_valid_to"],
        "qualifiers": json.loads(item["qualifiers_json"]),
        "tags": json.loads(item["tags_json"]),
        "notes": item["notes"],
        "research_location": {
            "unit_id": item["research_unit_id"],
            "path": unit["path"] if unit else None,
            "heading_id": unit["heading_id"] if unit else None,
            "title": unit["title"] if unit else None,
        },
        "dates": [
            dict(row)
            for row in connection.execute(
                "SELECT * FROM item_dates WHERE item_id=? ORDER BY date_role",
                (item_id,),
            )
        ],
        "sources": sources,
        "entities": entities,
        "relations": relations,
        "evidence_groups": evidence_groups,
        "publications": [
            dict(row)
            for row in connection.execute(
                """
                SELECT * FROM item_publications
                WHERE item_id=? ORDER BY publication_path, heading_id
                """,
                (item_id,),
            )
        ],
    }
    if item["item_kind"] == "negative_result":
        scope = connection.execute(
            "SELECT * FROM negative_result_scope WHERE item_id=?", (item_id,)
        ).fetchone()
        if scope is not None:
            record["negative_result_scope"] = {
                "provider": scope["provider"],
                "collection_name": scope["collection_name"],
                "date_start": scope["date_start"],
                "date_end": scope["date_end"],
                "query_description": scope["query_description"],
                "results_reviewed": scope["results_reviewed"],
                "coverage_confirmed": bool(scope["coverage_confirmed"]),
                "limitations": json.loads(scope["limitations_json"]),
            }
    return record


def _order_key(record: dict[str, Any]) -> tuple[int, int, int, str]:
    role_rank = {"seed": 0, "expanded": 1, "exhaustive": 2}[record["role_in_context"]]
    kind_rank = (
        CONCLUSION_KINDS.index(record["item_kind"])
        if record["item_kind"] in CONCLUSION_KINDS
        else len(CONCLUSION_KINDS)
    )
    distance = record["graph_distance"]
    return (
        kind_rank,
        role_rank,
        distance if distance is not None else 1_000_000,
        record["item_id"],
    )


def _package_chars(package: dict[str, Any]) -> int:
    return len(canonical_json(package))


def _protected(record: dict[str, Any]) -> bool:
    return record["item_kind"] in PROTECTED_KINDS


def _trim_evidence_excerpts(records: list[dict[str, Any]]) -> list[str]:
    changed: list[str] = []
    for record in records:
        if _protected(record):
            continue
        for source in record["sources"]:
            if source.get("evidence_excerpt"):
                source["evidence_excerpt"] = None
                changed.append(record["item_id"])
    return sorted(set(changed))


def _trim_context_only_detail(records: list[dict[str, Any]]) -> list[str]:
    changed: list[str] = []
    for record in records:
        if record["role_in_context"] != "expanded" or _protected(record):
            continue
        for field in ("statement", "summary", "qualifiers", "tags", "notes", "dates", "publications"):
            record.pop(field, None)
        changed.append(record["item_id"])
    return sorted(changed)


def _trim_low_bearing_entities(records: list[dict[str, Any]]) -> list[str]:
    changed: list[str] = []
    for record in records:
        if _protected(record):
            continue
        retained = []
        for entity in record["entities"]:
            if entity["role"] == "subject":
                retained.append(entity)
            else:
                changed.append(entity["entity_id"])
        record["entities"] = retained
    return sorted(set(changed))


def _compact_source(source: dict[str, Any]) -> dict[str, Any]:
    return {
        "source_id": source["source_id"],
        "role": source["role"],
        "locator": source["locator"],
    }


def _trim_full_source_citations(records: list[dict[str, Any]]) -> list[str]:
    changed: list[str] = []
    for record in records:
        if _protected(record):
            continue
        if any(set(source) - {"source_id", "role", "locator"} for source in record["sources"]):
            changed.append(record["item_id"])
        record["sources"] = [_compact_source(source) for source in record["sources"]]
        for group in record["evidence_groups"]:
            if any(
                set(source) - {"source_id", "role", "locator"}
                for source in group["sources"]
            ):
                changed.append(record["item_id"])
            group["sources"] = [
                {
                    "source_id": source["source_id"],
                    "role": source["role"],
                    "locator": source["locator"],
                }
                for source in group["sources"]
            ]
    return sorted(set(changed))


TRIMMERS: dict[str, Callable[[list[dict[str, Any]]], list[str]]] = {
    "evidence_excerpts": _trim_evidence_excerpts,
    "context_only_detail": _trim_context_only_detail,
    "low_bearing_related_entities": _trim_low_bearing_entities,
    "full_source_citations": _trim_full_source_citations,
}


def _warnings(
    records: list[dict[str, Any]], source_states: dict[str, str]
) -> list[dict[str, str]]:
    warnings: list[dict[str, str]] = []
    for record in records:
        item_id = record["item_id"]
        if record["review_state"] != "human_reviewed":
            warnings.append(
                {
                    "code": "item_review_needed",
                    "record_id": item_id,
                    "message": f"review_state={record['review_state']}",
                }
            )
        if record.get("knowledge_valid_to"):
            warnings.append(
                {
                    "code": "knowledge_window_closed",
                    "record_id": item_id,
                    "message": f"knowledge_valid_to={record['knowledge_valid_to']}",
                }
            )
        for relation in record["relations"]:
            if relation["direction"] == "out" and relation["review_state"] != "human_reviewed":
                warnings.append(
                    {
                        "code": "relation_review_needed",
                        "record_id": f"{item_id}->{relation['other']}",
                        "message": f"{relation['relation_type']} review_state={relation['review_state']}",
                    }
                )
    cited = {
        source["source_id"]
        for record in records
        for source in record["sources"]
    }
    cited.update(
        source["source_id"]
        for record in records
        for group in record["evidence_groups"]
        for source in group["sources"]
    )
    for source_id in sorted(cited):
        state = source_states.get(source_id)
        if state in {"drifted", "missing_baseline", "missing_file"}:
            warnings.append(
                {
                    "code": f"source_{state}",
                    "record_id": source_id,
                    "message": f"source hash state is {state}",
                }
            )
    return sorted(warnings, key=lambda row: (row["code"], row["record_id"]))


def _item_id_range(item_ids: list[str]) -> dict[str, str | None]:
    if not item_ids:
        return {"first": None, "last": None}
    return {"first": item_ids[0], "last": item_ids[-1]}


def _omitted_coverage(outside: list[str], reason: str, *, audit_detail: bool) -> list[dict[str, Any]]:
    if audit_detail:
        return [{"item_id": item_id, "reason": reason} for item_id in outside]
    if not outside:
        return []
    return [
        {
            "reason": reason,
            "count": len(outside),
            "item_id_range": _item_id_range(outside),
        }
    ]


def _relation_reason(record: dict[str, Any], relation: dict[str, Any]) -> str:
    other = relation["other"]
    direction = "to" if relation["direction"] == "out" else "from"
    detail = relation.get("explanation") or relation["bearing"]
    return (
        f"{relation['relation_type']} {direction} {other} "
        f"({relation['bearing']}, {relation['strength']}): {detail}"
    )


def _source_refs(record: dict[str, Any]) -> list[dict[str, Any]]:
    refs: dict[tuple[str, str | None, str | None], dict[str, Any]] = {}
    for source in record["sources"]:
        key = (source["source_id"], source.get("locator"), source.get("role"))
        refs[key] = {
            "source_id": source["source_id"],
            "locator": source.get("locator"),
            "role": source.get("role"),
        }
    for group in record["evidence_groups"]:
        for source in group["sources"]:
            key = (source["source_id"], source.get("locator"), source.get("role"))
            refs[key] = {
                "source_id": source["source_id"],
                "locator": source.get("locator"),
                "role": source.get("role"),
            }
    return [refs[key] for key in sorted(refs)]


def _ai_item_summary(record: dict[str, Any]) -> dict[str, Any]:
    summary: dict[str, Any] = {
        "item_id": record["item_id"],
        "item_kind": record["item_kind"],
        "short_statement": record["short_statement"],
        "status": record["status"],
        "confidence_label": record["confidence_label"],
        "role_in_context": record["role_in_context"],
        "graph_distance": record["graph_distance"],
        "research_location": record["research_location"],
        "relation_reasons": [
            *record["expansion_reasons"],
            *[_relation_reason(record, relation) for relation in record["relations"]],
        ],
        "sources": _source_refs(record),
    }
    if "negative_result_scope" in record:
        scope = record["negative_result_scope"]
        summary["negative_result_scope"] = {
            "provider": scope["provider"],
            "collection_name": scope["collection_name"],
            "date_start": scope["date_start"],
            "date_end": scope["date_end"],
            "query_description": scope["query_description"],
            "results_reviewed": scope["results_reviewed"],
            "coverage_confirmed": scope["coverage_confirmed"],
            "limitations": scope["limitations"],
        }
    return summary


def format_ai_grounding(package: dict[str, Any]) -> dict[str, Any]:
    """Return a concise AI-facing grounding brief from a raw context package."""
    items = [_ai_item_summary(record) for record in package["items"]]
    conclusion_ids = {
        item["item_id"]
        for item in items
        if item["item_kind"] in CONCLUSION_KINDS
    }
    ledger = package["coverage_ledger"]
    omitted = ledger.get("omitted", [])
    omitted_count = sum(row.get("count", 1) for row in omitted)
    return {
        "query": package["query"],
        "conclusions": [
            item for item in items if item["item_id"] in conclusion_ids
        ],
        "supporting_items": [
            item for item in items if item["item_id"] not in conclusion_ids
        ],
        "coverage": {
            "considered_active_items": ledger["considered"]["count"],
            "considered_item_id_range": ledger["considered"].get("item_id_range"),
            "seed_matched": ledger["seed_matched"],
            "included_total": ledger["included_total"],
            "included_ids": ledger["included_compactly"],
            "omitted_total": omitted_count,
            "omitted": omitted,
            "detail_omissions": ledger["detail_omissions"],
            "unresolved_inputs": ledger["unresolved_inputs"],
            "matched_entity_ids": ledger["matched_entity_ids"],
            "within_budget": ledger["within_budget"],
            "final_chars": ledger["final_chars"],
        },
        "warnings": package["warnings"],
    }


def compile_context(
    config: GraphConfig,
    *,
    terms: list[str] | None = None,
    ids: list[str] | None = None,
    entity_ids: list[str] | None = None,
    budget: int | None = None,
    relation_types: list[str] | None = None,
    mode: str = "grounding",
    match: str = "any",
) -> dict[str, Any]:
    """Compile a deterministic, coverage-accounted context package."""
    terms = [term.strip() for term in (terms or []) if term.strip()]
    ids = list(dict.fromkeys(ids or []))
    entity_ids = list(dict.fromkeys(entity_ids or []))
    mode = mode.strip().lower()
    match = _normalise_match(match)
    if mode not in MODE_MAX_HOPS:
        raise ValueError(
            f"Unknown context mode {mode!r}; choose from "
            + ", ".join(MODE_MAX_HOPS)
        )
    if budget is not None and budget < 1:
        raise ValueError("Budget must be a positive character count.")
    selected_relations = _normalise_relation_types(relation_types)

    connection = connect(config.db_path, read_only=True)
    try:
        active_items = {
            row["item_id"]: dict(row)
            for row in connection.execute(
                """
                SELECT * FROM research_items
                WHERE status IN ('active', 'open')
                ORDER BY item_id
                """
            )
        }
        selection = _select_scope(
            connection,
            active_items,
            terms=terms,
            ids=ids,
            entity_ids=entity_ids,
            relation_types=selected_relations,
            mode=mode,
            match=match,
        )
        source_states = _source_states(connection, config)
        records = []
        for item_id in sorted(selection.included):
            if item_id in selection.seeds:
                role = "seed"
            elif item_id in selection.distances:
                role = "expanded"
            else:
                role = "exhaustive"
            records.append(
                _item_record(
                    connection,
                    active_items[item_id],
                    role=role,
                    distance=selection.distances.get(item_id),
                    reasons=selection.expansion_reasons.get(item_id, []),
                    included_ids=selection.included,
                    relation_types=set(selected_relations),
                    source_states=source_states,
                )
            )
    finally:
        connection.close()
    records.sort(key=_order_key)

    outside = sorted(set(active_items) - selection.included)
    omission_reason = (
        "no_seed_match"
        if not selection.seeds and mode != "exhaustive"
        else f"outside_{mode}_subgraph"
    )
    audit_detail = mode in {"audit", "exhaustive"}
    active_item_ids = sorted(active_items)
    ledger: dict[str, Any] = {
        # Compatibility summaries retained from the Phase P package.
        "considered_active_items": len(active_items),
        "seed_matched": sorted(selection.seeds),
        "expanded": {
            item_id: {
                "distance": selection.distances[item_id],
                "reasons": selection.expansion_reasons.get(item_id, []),
            }
            for item_id in sorted(selection.included - selection.seeds)
            if item_id in selection.distances
        },
        "included_total": len(records),
        "omitted_detail": [],
        "budget_chars": budget,
        # Full G2 accounting.
        "considered": {
            "count": len(active_items),
            "item_id_range": _item_id_range(active_item_ids),
            "scope": "status active/open",
        },
        "included_compactly": [record["item_id"] for record in records],
        "omitted": _omitted_coverage(outside, omission_reason, audit_detail=audit_detail),
        "unresolved_inputs": {
            "missing_item_ids": sorted(selection.missing_item_ids),
            "inactive_item_ids": sorted(selection.inactive_item_ids),
            "missing_entity_ids": sorted(selection.missing_entity_ids),
        },
        "matched_entity_ids": sorted(selection.matched_entity_ids),
        "detail_omissions": [],
    }
    if audit_detail:
        ledger["considered"]["item_ids"] = active_item_ids
    warnings = _warnings(records, source_states)
    package: dict[str, Any] = {
        "query": {
            "terms": terms,
            "ids": ids,
            "entity_ids": entity_ids,
            "relation_types": list(selected_relations),
            "mode": mode,
            "match": match,
            "max_hops": MODE_MAX_HOPS[mode],
        },
        "items": records,
        "coverage_ledger": ledger,
        "warnings": warnings,
        "review_warnings": [
            f"{warning['record_id']}: {warning['message']}"
            for warning in warnings
        ],
    }

    ledger["baseline_chars"] = _package_chars(package)
    if budget is not None:
        for tier in TRIM_ORDER:
            if _package_chars(package) <= budget:
                break
            affected = TRIMMERS[tier](records)
            ledger["omitted_detail"].append(tier)
            ledger["detail_omissions"].append(
                {
                    "tier": tier,
                    "affected_ids": affected,
                    "reason": "character budget exceeded",
                }
            )
    # Stabilize the self-referential final character count and budget flag.
    ledger["final_chars"] = 0
    ledger["within_budget"] = budget is None
    for _ in range(5):
        ledger["final_chars"] = _package_chars(package)
        ledger["within_budget"] = (
            budget is None or ledger["final_chars"] <= budget
        )
    ledger["final_chars"] = _package_chars(package)
    return package
