#!/usr/bin/env python3
"""Check local Markdown links and the canonical 21-card task ID set."""

from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"\[[^]]+\]\(([^)]+)\)")
CARD_HEADING = re.compile(r"^### ([ABC]\d{2}) —", re.MULTILINE)
TASK_ID = re.compile(r"^[ABC]\d{2}$")


def check_local_links() -> int:
    checked = 0
    failures: list[str] = []
    for markdown in sorted(ROOT.rglob("*.md")):
        if any(part.startswith(".") and part not in {"."} for part in markdown.relative_to(ROOT).parts):
            continue
        content = markdown.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(content):
            target = raw_target.strip().split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            checked += 1
            resolved = (markdown.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                failures.append(f"{markdown.relative_to(ROOT)}: link escapes repo: {raw_target}")
                continue
            if not resolved.exists():
                failures.append(f"{markdown.relative_to(ROOT)}: missing target: {raw_target}")
    if failures:
        raise AssertionError("\n".join(failures))
    return checked


def check_task_ids() -> set[str]:
    kanban = (ROOT / "ai_artifacts" / "plans" / "kanban.md").read_text(encoding="utf-8")
    markdown_ids = set(CARD_HEADING.findall(kanban))
    with (ROOT / "ai_artifacts" / "plans" / "kanban.csv").open(
        encoding="utf-8-sig", newline=""
    ) as handle:
        csv_ids = {row["id"] for row in csv.DictReader(handle) if TASK_ID.fullmatch(row["id"])}
    if len(markdown_ids) != 21:
        raise AssertionError(f"expected 21 detailed task cards, found {len(markdown_ids)}")
    if markdown_ids != csv_ids:
        raise AssertionError(
            f"task ID drift: markdown-only={sorted(markdown_ids - csv_ids)}, "
            f"csv-only={sorted(csv_ids - markdown_ids)}"
        )
    return markdown_ids


def main() -> None:
    links = check_local_links()
    task_ids = check_task_ids()
    print(f"PASS docs: {links} local links resolve")
    print(f"PASS tasks: {len(task_ids)} IDs match between kanban.md and kanban.csv")


if __name__ == "__main__":
    main()
