"""Minimal Phase P context compiler.

This is the deliberately small read path that Phase P needs to measure its gate
(§16): seed items by term or explicit id, expand one relation hop, and emit a
compact, budget-aware package with an explicit coverage ledger. The full budget
model, FTS ranking, and §13 gold-set evaluation remain Phase G2 work; this
module implements only what the colonial-arrival slice requires and shares the
schema and read conventions of the accepted G1A plumbing.

Guarantees kept from §12, even in this minimal form:

- The package never silently truncates. Every in-scope item keeps its id and a
  short statement; only detail is shed to meet a budget, in a declared order.
- Conflicts, negative-result limitations, and omitted-coverage notices are never
  dropped to meet a budget.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .config import GraphConfig
from .db import connect
from .util import canonical_json

# Kinds that read as current conclusions rather than raw evidence. Used only to
# order the package (conclusions first); it never filters items out.
CONCLUSION_KINDS = (
    "research_finding",
    "analysis",
    "identity_hypothesis",
    "evidence_conflict",
    "project_statement",
    "published_source_statement",
    "open_question",
)

# Declared detail-shedding order (§12). Earlier tiers are dropped first. Item
# ids, short statements, conflicts, negative-result limitations, and the
# coverage ledger are never in this list — they are structural.
TRIM_ORDER = (
    "evidence_excerpts",   # long exact source extracts
    "context_only_detail",  # detail on items included only as context
    "source_detail",        # source display metadata already addressable by id
    "notes",                # free-text notes/qualifiers on conclusion items
)


@dataclass(frozen=True)
class _Scope:
    seeds: set[str]
    expanded: dict[str, list[str]]  # item_id -> human reasons it was pulled in


def _matches(item: dict[str, Any], terms: list[str]) -> bool:
    haystack = " ".join(
        str(item.get(field) or "")
        for field in ("statement", "short_label", "summary")
    ).casefold()
    return all(term.casefold() in haystack for term in terms)


def _seed_scope(
    connection: Any, terms: list[str], ids: list[str], relation_types: list[str] | None
) -> tuple[_Scope, int]:
    active_items = {
        row["item_id"]: dict(row)
        for row in connection.execute(
            "SELECT * FROM research_items WHERE status IN ('active', 'open')"
        )
    }
    considered = len(active_items)

    seeds: set[str] = {item_id for item_id in ids if item_id in active_items}
    if terms:
        seeds |= {
            item_id
            for item_id, item in active_items.items()
            if _matches(item, terms)
        }

    expanded: dict[str, list[str]] = {}
    for row in connection.execute("SELECT * FROM item_relations"):
        if relation_types and row["relation_type"] not in relation_types:
            continue
        src, dst, rel = row["from_item_id"], row["to_item_id"], row["relation_type"]
        if src in seeds and dst in active_items and dst not in seeds:
            expanded.setdefault(dst, []).append(f"{rel} from {src}")
        if dst in seeds and src in active_items and src not in seeds:
            expanded.setdefault(src, []).append(f"{rel} to {dst}")
    return _Scope(seeds, expanded), considered


def _item_record(connection: Any, item_id: str, *, is_seed: bool, reasons: list[str]) -> dict[str, Any]:
    row = dict(
        connection.execute(
            "SELECT * FROM research_items WHERE item_id=?", (item_id,)
        ).fetchone()
    )
    unit = connection.execute(
        "SELECT path, heading_id FROM research_units WHERE unit_id=?",
        (row["research_unit_id"],),
    ).fetchone()
    sources = [
        {
            "source_id": value["source_id"],
            "role": value["role"],
            "locator": value["locator"],
            "evidence_excerpt": value["evidence_excerpt"],
        }
        for value in connection.execute(
            "SELECT * FROM item_sources WHERE item_id=? ORDER BY source_id, role, locator",
            (item_id,),
        )
    ]
    relations = [
        {"direction": "out", "relation_type": r["relation_type"], "other": r["to_item_id"],
         "bearing": r["bearing"], "strength": r["strength"], "explanation": r["explanation"]}
        for r in connection.execute(
            "SELECT * FROM item_relations WHERE from_item_id=? ORDER BY relation_type, to_item_id",
            (item_id,),
        )
    ] + [
        {"direction": "in", "relation_type": r["relation_type"], "other": r["from_item_id"],
         "bearing": r["bearing"], "strength": r["strength"], "explanation": r["explanation"]}
        for r in connection.execute(
            "SELECT * FROM item_relations WHERE to_item_id=? ORDER BY relation_type, from_item_id",
            (item_id,),
        )
    ]
    record: dict[str, Any] = {
        "item_id": item_id,
        "item_kind": row["item_kind"],
        "role_in_context": "seed" if is_seed else "expanded",
        "expansion_reasons": sorted(reasons),
        "short_statement": row["short_label"] or row["statement"],
        "statement": row["statement"],
        "status": row["status"],
        "confidence_label": row["assessment_confidence_label"],
        "visibility": row["visibility"],
        "review_state": row["review_state"],
        "research_location": {
            "path": unit["path"] if unit else None,
            "heading_id": unit["heading_id"] if unit else None,
        },
        "sources": sources,
        "relations": relations,
        "notes": row["notes"],
    }
    if row["item_kind"] == "negative_result":
        scope = connection.execute(
            "SELECT * FROM negative_result_scope WHERE item_id=?", (item_id,)
        ).fetchone()
        if scope is not None:
            import json

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


def _order_key(record: dict[str, Any]) -> tuple[int, int, str]:
    kind_rank = CONCLUSION_KINDS.index(record["item_kind"]) if record["item_kind"] in CONCLUSION_KINDS else len(CONCLUSION_KINDS)
    seed_rank = 0 if record["role_in_context"] == "seed" else 1
    return (seed_rank, kind_rank, record["item_id"])


def _package_chars(package: dict[str, Any]) -> int:
    return len(canonical_json(package))


def _protected(record: dict[str, Any]) -> bool:
    """Records whose detail may never be shed to meet budget."""
    return record["item_kind"] in ("evidence_conflict", "negative_result")


def _apply_trim(records: list[dict[str, Any]], tier: str) -> None:
    for record in records:
        if _protected(record):
            continue
        if tier == "evidence_excerpts":
            for source in record["sources"]:
                if source.get("evidence_excerpt"):
                    source["evidence_excerpt"] = None
        elif tier == "context_only_detail" and record["role_in_context"] == "expanded":
            record["statement"] = record["short_statement"]
            record["notes"] = None
        elif tier == "source_detail":
            record["sources"] = [
                {"source_id": s["source_id"], "role": s["role"], "locator": s["locator"]}
                for s in record["sources"]
            ]
        elif tier == "notes":
            record["notes"] = None


def compile_context(
    config: GraphConfig,
    *,
    terms: list[str] | None = None,
    ids: list[str] | None = None,
    budget: int | None = None,
    relation_types: list[str] | None = None,
) -> dict[str, Any]:
    terms = list(terms or [])
    ids = list(ids or [])
    connection = connect(config.db_path, read_only=True)
    try:
        scope, considered = _seed_scope(connection, terms, ids, relation_types)
        included = sorted(scope.seeds | set(scope.expanded))
        records = [
            _item_record(
                connection,
                item_id,
                is_seed=item_id in scope.seeds,
                reasons=scope.expanded.get(item_id, []),
            )
            for item_id in included
        ]
    finally:
        connection.close()
    records.sort(key=_order_key)

    warnings = sorted(
        f"{record['item_id']}: review_state={record['review_state']}"
        for record in records
        if record["review_state"] != "human_reviewed"
    )
    ledger: dict[str, Any] = {
        "considered_active_items": considered,
        "seed_matched": sorted(scope.seeds),
        "expanded": {item_id: sorted(reasons) for item_id, reasons in sorted(scope.expanded.items())},
        "included_total": len(records),
        "omitted_detail": [],
        "budget_chars": budget,
    }
    package: dict[str, Any] = {
        "query": {"terms": terms, "ids": ids, "relation_types": relation_types},
        "items": records,
        "coverage_ledger": ledger,
        "review_warnings": warnings,
    }

    if budget is not None:
        for tier in TRIM_ORDER:
            if _package_chars(package) <= budget:
                break
            _apply_trim(records, tier)
            ledger["omitted_detail"].append(tier)
        ledger["final_chars"] = _package_chars(package)
        ledger["within_budget"] = ledger["final_chars"] <= budget
    else:
        ledger["final_chars"] = _package_chars(package)
        ledger["within_budget"] = True
    return package
