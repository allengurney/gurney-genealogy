#!/usr/bin/env python3
"""
split-fact-sheets.py — Split fact sheets into narrative + research companion.

Run from the root of the gurney-genealogy repo:
    python split-fact-sheets.py

For each fact sheet in fact-sheets/:
  1. Finds the "## Research Appendix" boundary
  2. Strips the appendix (and preceding ---) from the narrative file
  3. Creates a .research.md companion with the appendix content + a Working Notes section

Files without a Research Appendix section are skipped (with a message).
"""

import os
import re
import glob

FACT_SHEETS_DIR = os.path.join(os.path.dirname(__file__), "fact-sheets")


def split_fact_sheet(filepath):
    """Split a single fact sheet. Returns (narrative, research) or None if no appendix."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the Research Appendix boundary
    # Pattern: optional "---" line, then "## Research Appendix"
    # We want to split just before the "---" that precedes the appendix header
    match = re.search(r'\n---\s*\n+## Research Appendix', content)
    if not match:
        # Try without the --- separator
        match = re.search(r'\n## Research Appendix', content)
        if not match:
            return None

    split_pos = match.start()
    narrative = content[:split_pos].rstrip() + "\n"
    appendix_raw = content[split_pos:].lstrip("-\n ")

    # Build the research companion
    # Extract the person name from the narrative's YAML front matter or heading
    name_match = re.search(r'personName:\s*(.+)', content)
    gen_match = re.search(r'gen:\s*(G\S+)', content)
    person_name = name_match.group(1).strip() if name_match else os.path.basename(filepath)
    gen = gen_match.group(1).strip() if gen_match else "G??"

    research_header = f"# {person_name} ({gen}) — Research Companion\n\n"
    research_header += f"Research companion for `{os.path.basename(filepath)}`. "
    research_header += "See AI-Rules.md §3 for the paired-file rule.\n\n---\n\n"

    # Add a Working Notes section at the top if not already present
    working_notes = ""
    if "## Working Notes" not in appendix_raw:
        working_notes = "## Working Notes\n\n*No entries yet.*\n\n---\n\n"

    research = research_header + working_notes + appendix_raw

    return narrative, research


def main():
    pattern = os.path.join(FACT_SHEETS_DIR, "g*-fact-sheet.md")
    fact_sheets = sorted(glob.glob(pattern))

    if not fact_sheets:
        print(f"No fact sheets found matching {pattern}")
        return

    split_count = 0
    skip_count = 0

    for filepath in fact_sheets:
        basename = os.path.basename(filepath)
        result = split_fact_sheet(filepath)

        if result is None:
            print(f"  SKIP  {basename} — no Research Appendix found")
            skip_count += 1
            continue

        narrative, research = result

        # Write updated narrative (overwrite original)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(narrative)

        # Write research companion
        research_path = filepath.replace("-fact-sheet.md", "-fact-sheet.research.md")
        with open(research_path, "w", encoding="utf-8") as f:
            f.write(research)

        narrative_kb = len(narrative) / 1024
        research_kb = len(research) / 1024
        print(f"  SPLIT {basename} → narrative {narrative_kb:.1f}KB + research {research_kb:.1f}KB")
        split_count += 1

    print(f"\nDone. {split_count} split, {skip_count} skipped.")
    print("Next: git add . && git commit -m 'Split fact sheets into narrative + research companion' && git push")


if __name__ == "__main__":
    main()
