"""Local graph-editing backend for the G13 context graph (Phase G4).

A small loopback-only HTTP service that owns the canonical SQLite connection,
validation, and export, exposing the §14 editing contract (implemented in
``tools/g13_graph/editor.py``) to a browser UI. It reuses the accepted G1B
plumbing wholesale; it adds no second store and no JSON edit path.
"""
