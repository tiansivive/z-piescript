#!/usr/bin/env python3
"""Generate REFERENCES.md from paper-tagged zettels.

Each paper-tagged zettel (excluding the papers.hub index) contributes one entry. Papers are
grouped by their primary topic tag and sorted alphabetically within each section.

Usage:
    python3 scripts/references.py              # Rich terminal output
    python3 scripts/references.py --markdown   # plain markdown (for dist/)
"""

import re
import signal
import sys
from pathlib import Path

from rich.console import Console

from lib.zettel import ZETTELS_DIR, load_all_zettels, refs_with_prefix, zettels_by_tag

signal.signal(signal.SIGPIPE, signal.SIG_DFL)

# Section tags in display order. Each paper is placed in the first matching section.
SECTIONS = [
    ("pi-calculus", "Pi-Calculus and Process Algebra"),
    ("effects", "Free Monads and Algebraic Effects"),
    ("esql", "Language-Integrated Query and Comprehensions"),
    ("data-processing", "Data Parallelism and Materialization"),
    ("distributed", "Distributed Data Management"),
    ("types", "Type Theory"),
    ("beam", "BEAM / Erlang"),
    ("coordination", "Coordination and Concurrency"),
]
FALLBACK_SECTION = "Other References"


def _section_for(z: dict) -> str:
    for tag, label in SECTIONS:
        if tag in z["tags"]:
            return label
    return FALLBACK_SECTION


def _full_body(z: dict) -> str:
    """Return the full body text between the title and the edges section."""
    path = ZETTELS_DIR / z["file"]
    text = path.read_text()
    parts = text.split("---", 2)
    if len(parts) < 3:
        return ""
    body = parts[2].strip()
    lines = body.split("\n")
    # Skip the title line
    start = 0
    for i, line in enumerate(lines):
        if line.startswith("# "):
            start = i + 1
            break
    # Collect until the first bold section header (**Depends on**, **Enables**, **Connections**)
    result: list[str] = []
    for line in lines[start:]:
        if line.startswith("**"):
            break
        result.append(line)
    return "\n".join(result).strip()


def _urls(z: dict) -> list[str]:
    return refs_with_prefix(z, "resource:")


def _group_papers(papers: list[dict]) -> dict[str, list[dict]]:
    groups: dict[str, list[dict]] = {}
    for z in papers:
        sec = _section_for(z)
        groups.setdefault(sec, []).append(z)
    for sec in groups:
        groups[sec].sort(key=lambda z: z["title"].lower())
    return groups


def main() -> None:
    args = sys.argv[1:]
    markdown = "--markdown" in args

    all_zettels = load_all_zettels()
    papers = [z for z in zettels_by_tag(all_zettels, "paper") if "hub" not in z["tags"]]
    groups = _group_papers(papers)

    section_order = [label for _, label in SECTIONS] + [FALLBACK_SECTION]

    if markdown:
        _print_markdown(groups, section_order, len(papers))
    else:
        _print_rich(groups, section_order, len(papers))


def _print_markdown(groups: dict, section_order: list, total: int) -> None:
    print("# References\n")
    print(
        f"> Generated from {total} paper-tagged zettels in `docs/z-piescript/zettels/`.\n"
        "> Run `python3 scripts/references.py --markdown` to regenerate.\n"
    )
    for label in section_order:
        if label not in groups:
            continue
        print(f"## {label}\n")
        for z in groups[label]:
            print(f"### {z['title']}\n")
            body = _full_body(z)
            if body:
                print(f"{body}\n")
            for url in _urls(z):
                print(f"- <{url}>")
            if _urls(z):
                print()


def _print_rich(groups: dict, section_order: list, total: int) -> None:
    console = Console()
    console.print(f"\n[bold]References[/bold] ({total} papers)\n")
    for label in section_order:
        if label not in groups:
            continue
        console.print(f"[bold cyan]{label}[/bold cyan]\n")
        for z in groups[label]:
            console.print(f"  [bold]{z['title']}[/bold]")
            body = _full_body(z)
            if body:
                # Show only the first sentence (citation line) in terminal view
                first = body.split("\n")[0]
                preview = first[:120] + "..." if len(first) > 120 else first
                console.print(f"  [dim]{preview}[/dim]")
            for url in _urls(z):
                console.print(f"  [blue]{url}[/blue]")
            console.print()


if __name__ == "__main__":
    main()
