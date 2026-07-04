"""Loopback HTTP backend for the G13 graph editor.

Binds to 127.0.0.1 only. Serves a static browser UI and a small JSON API that
delegates every read/write to ``tools/g13_graph/editor.py`` and the reused G1B
plumbing (validation, revisions, exporter, status). The canonical SQLite
database is the sole store; there is no JSON edit path.

Safety posture:

- **Loopback bind.** Never binds ``0.0.0.0``; the socket is opened on
  ``127.0.0.1`` (§14).
- **Host-header allowlist.** Every request must carry a loopback ``Host`` (and,
  for writes, a loopback/absent ``Origin``). This defeats DNS-rebinding attempts
  that resolve an attacker domain to 127.0.0.1.
- **Live-DB guard.** Refuses to start against the default canonical database
  path unless ``--allow-live`` is passed, so development runs against a
  ``GURNEY_G13_GRAPH_DB`` staging copy by default.
"""

from __future__ import annotations

import json
import sqlite3
import traceback
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Callable
from urllib.parse import parse_qs, unquote, urlparse

from tools.g13_graph.config import DEFAULT_DB, GraphConfig, load_config
from tools.g13_graph.drift import source_hash_state
from tools.g13_graph.editor import (
    ChangeError,
    PICKLISTS,
    ValidationBlocked,
    autocomplete_entities,
    autocomplete_sources,
    commit_change,
    get_item_detail,
    list_items,
    list_units,
    neighborhood,
    preview_change,
    review_queue,
)
from tools.g13_graph.exporter import export_recovery, export_snapshot
from tools.g13_graph.indexes import search_graph
from tools.g13_graph.queries import get_impact
from tools.g13_graph.status import graph_status

STATIC_DIR = Path(__file__).with_name("static")
LOOPBACK_HOSTS = {"127.0.0.1", "localhost", "::1", "[::1]"}
CONTENT_TYPES = {
    ".html": "text/html; charset=utf-8",
    ".js": "text/javascript; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".json": "application/json; charset=utf-8",
    ".svg": "image/svg+xml",
}


class EditorServer(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, address: tuple[str, int], config: GraphConfig) -> None:
        super().__init__(address, EditorHandler)
        self.config = config


def _host_is_local(value: str | None) -> bool:
    if not value:
        return False
    # Normalise "127.0.0.1:8765" / "localhost:8765" / "[::1]:8765" / bare host.
    if value.startswith("["):
        host = value[1:].split("]", 1)[0]
    else:
        host = value.rsplit(":", 1)[0] if ":" in value else value
    return host in LOOPBACK_HOSTS


def _origin_is_local(origin: str | None) -> bool:
    if not origin:
        return True  # Same-origin fetches from our own page omit Origin on GET.
    try:
        parsed = urlparse(origin)
    except ValueError:
        return False
    return parsed.hostname in {"127.0.0.1", "localhost", "::1"}


class EditorHandler(BaseHTTPRequestHandler):
    server_version = "g13-graph-editor/1.0"
    protocol_version = "HTTP/1.1"

    # -- infrastructure ----------------------------------------------------- #
    @property
    def config(self) -> GraphConfig:
        return self.server.config  # type: ignore[attr-defined]

    def log_message(self, fmt: str, *args: Any) -> None:  # quieter default log
        return

    def _send_json(self, status: int, payload: Any) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _send_bytes(self, status: int, body: bytes, content_type: str) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _guard_local(self, *, writing: bool) -> bool:
        if not _host_is_local(self.headers.get("Host")):
            self._send_json(403, {"error": "Non-loopback Host header rejected."})
            return False
        if writing and not _origin_is_local(self.headers.get("Origin")):
            self._send_json(403, {"error": "Cross-origin write rejected."})
            return False
        return True

    def _read_body(self) -> dict[str, Any]:
        length = int(self.headers.get("Content-Length", 0) or 0)
        if length <= 0:
            return {}
        raw = self.rfile.read(length)
        try:
            data = json.loads(raw.decode("utf-8"))
        except (ValueError, UnicodeDecodeError) as exc:
            raise ChangeError(f"Invalid JSON body: {exc}") from exc
        if not isinstance(data, dict):
            raise ChangeError("Request body must be a JSON object.")
        return data

    # -- routing ------------------------------------------------------------ #
    def do_GET(self) -> None:
        if not self._guard_local(writing=False):
            return
        parsed = urlparse(self.path)
        path = parsed.path
        query = {k: v[0] for k, v in parse_qs(parsed.query).items()}
        try:
            if path.startswith("/api/"):
                self._route_get_api(path, query)
            else:
                self._serve_static(path)
        except Exception as exc:  # noqa: BLE001 - surface as JSON error
            self._error(exc)

    def do_POST(self) -> None:
        if not self._guard_local(writing=True):
            return
        parsed = urlparse(self.path)
        path = parsed.path
        try:
            self._route_post_api(path)
        except ValidationBlocked as exc:
            self._send_json(
                409, {"error": "validation_blocked", "blocking_errors": exc.blocking}
            )
        except (ChangeError, KeyError, ValueError) as exc:
            self._send_json(400, {"error": str(exc)})
        except sqlite3.IntegrityError as exc:
            self._send_json(400, {"error": f"integrity_error: {exc}"})
        except Exception as exc:  # noqa: BLE001
            self._error(exc)

    def _error(self, exc: Exception) -> None:
        self._send_json(
            500, {"error": str(exc), "trace": traceback.format_exc(limit=4)}
        )

    # -- static ------------------------------------------------------------- #
    def _serve_static(self, path: str) -> None:
        rel = "index.html" if path in ("/", "") else path.lstrip("/")
        if rel.startswith("static/"):
            rel = rel[len("static/") :]
        base = STATIC_DIR.resolve()
        target = (base / rel).resolve()
        # Reject path traversal outside the static root and any non-file.
        if target != base and base not in target.parents:
            self._send_json(404, {"error": "Not found."})
            return
        if not target.is_file():
            self._send_json(404, {"error": "Not found."})
            return
        content_type = CONTENT_TYPES.get(target.suffix, "application/octet-stream")
        self._send_bytes(200, target.read_bytes(), content_type)

    # -- GET api ------------------------------------------------------------ #
    def _route_get_api(self, path: str, query: dict[str, str]) -> None:
        config = self.config
        if path == "/api/status":
            self._send_json(200, graph_status(config))
        elif path == "/api/picklists":
            self._send_json(
                200,
                {
                    "picklists": {k: list(v) for k, v in PICKLISTS.items()},
                    "units": list_units(config),
                },
            )
        elif path == "/api/items":
            self._send_json(200, list_items(config, query))
        elif path == "/api/review-queue":
            self._send_json(200, review_queue(config))
        elif path == "/api/units":
            self._send_json(200, {"units": list_units(config)})
        elif path == "/api/sources":
            self._send_json(
                200, {"results": autocomplete_sources(config, query.get("q", ""))}
            )
        elif path == "/api/entities":
            self._send_json(
                200, {"results": autocomplete_entities(config, query.get("q", ""))}
            )
        elif path == "/api/source-hashes":
            self._send_json(200, self._source_hash_state())
        elif path == "/api/neighborhood":
            result = neighborhood(
                config, kind=query.get("kind", "item"), node_id=query.get("id", "")
            )
            if result is None:
                self._send_json(404, {"error": "Node not found."})
            else:
                self._send_json(200, result)
        elif path == "/api/search":
            terms = [t for t in query.get("terms", "").split() if t]
            if not terms:
                self._send_json(400, {"error": "search requires terms."})
            else:
                self._send_json(200, search_graph(config, terms))
        elif path.startswith("/api/item/"):
            item_id = unquote(path[len("/api/item/") :])
            detail = get_item_detail(config, item_id)
            if detail is None:
                self._send_json(404, {"error": f"Item not found: {item_id}"})
            else:
                self._send_json(200, detail)
        elif path.startswith("/api/impact/"):
            item_id = unquote(path[len("/api/impact/") :])
            impact = get_impact(config, item_id)
            if impact is None:
                self._send_json(404, {"error": f"Item not found: {item_id}"})
            else:
                self._send_json(200, impact)
        else:
            self._send_json(404, {"error": f"Unknown API route: {path}"})

    def _source_hash_state(self) -> dict[str, Any]:
        from tools.g13_graph.db import connect

        connection = connect(self.config.db_path, read_only=True)
        try:
            return source_hash_state(connection, self.config)
        finally:
            connection.close()

    # -- POST api ----------------------------------------------------------- #
    def _route_post_api(self, path: str) -> None:
        config = self.config
        body = self._read_body()
        if path == "/api/preview":
            self._send_json(200, preview_change(config, body))
        elif path == "/api/commit":
            self._send_json(200, commit_change(config, body))
        elif path == "/api/snapshot":
            snapshot = export_snapshot(config)
            self._send_json(200, {"snapshot": str(snapshot)})
        elif path == "/api/export-recovery":
            recovery = export_recovery(config)
            self._send_json(200, {"recovery": str(recovery)})
        else:
            self._send_json(404, {"error": f"Unknown API route: {path}"})


def run(
    *,
    host: str = "127.0.0.1",
    port: int = 8765,
    db_path: str | None = None,
    export_dir: str | None = None,
    sources_path: str | None = None,
    allow_live: bool = False,
) -> None:
    if host not in {"127.0.0.1", "localhost", "::1"}:
        raise SystemExit(
            f"Refusing to bind non-loopback host {host!r}; the canonical editor "
            "is loopback-only."
        )
    config = load_config(
        db_path=db_path, export_dir=export_dir, sources_path=sources_path
    )
    if config.db_path == DEFAULT_DB.resolve() and not allow_live:
        raise SystemExit(
            "Refusing to open the live canonical database.\n"
            f"  live DB: {config.db_path}\n"
            "Set GURNEY_G13_GRAPH_DB (or --db) to a staging copy, or pass "
            "--allow-live to override intentionally."
        )
    server = EditorServer((host, port), config)
    print("G13 graph editor — local authoring backend")
    print(f"  URL:        http://{host}:{port}/")
    print(f"  database:   {config.db_path}")
    print(f"  export dir: {config.export_dir}")
    print(f"  sources:    {config.sources_path}")
    if config.db_path == DEFAULT_DB.resolve():
        print("  MODE:       LIVE canonical database (--allow-live)")
    else:
        print("  MODE:       staging copy")
    print("  Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping.")
    finally:
        server.server_close()
