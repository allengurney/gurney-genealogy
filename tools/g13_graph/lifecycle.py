"""Post-commit refresh of derived indexes and the rolling recovery export."""

from __future__ import annotations

from .config import GraphConfig
from .exporter import export_recovery
from .indexes import rebuild_database_indexes


class PostCommitRefreshError(RuntimeError):
    """Content committed, but one or more required derived refreshes failed."""


def refresh_after_commit(
    config: GraphConfig, *, rebuild_indexes: bool = True
) -> None:
    failures: list[str] = []
    if rebuild_indexes:
        try:
            rebuild_database_indexes(config)
        except Exception as exc:
            failures.append(f"derived index refresh failed: {exc}")
    try:
        export_recovery(config)
    except Exception as exc:
        failures.append(f"recovery export refresh failed: {exc}")
    if failures:
        raise PostCommitRefreshError(
            "Content transaction committed; " + "; ".join(failures)
        )
