#!/usr/bin/env python3
"""Check local Markdown links and the canonical 21-card task ID set."""

from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"\[[^]]+\]\(([^)]+)\)")
CARD_HEADING = re.compile(r"^### ([ABC]\d{2}) —", re.MULTILINE)
CARD_REVIEWER = re.compile(
    r"^### ([ABC]\d{2}) —.*?^\*\*Reviewer:\*\* ([^\n]+)$",
    re.MULTILINE | re.DOTALL,
)
TASK_ID = re.compile(r"^[ABC]\d{2}$")

GOVERNANCE_FILES = (
    "AGENTS.md",
    "README.md",
    ".github/pull_request_template.md",
    "ai_artifacts/README.md",
    "ai_artifacts/contracts/README.md",
    "ai_artifacts/docs/api-contracts.md",
    "ai_artifacts/docs/current-state.md",
    "ai_artifacts/docs/decision-log.md",
    "ai_artifacts/docs/integration-workflow.md",
    "ai_artifacts/docs/release-checklist.md",
    "ai_artifacts/plans/kanban.md",
    "ai_artifacts/plans/kanban.csv",
    "ai_artifacts/prompts/Agent_Prompt.md",
    "ai_artifacts/prompts/Integration_Lead_Prompt.md",
    "ai_artifacts/skeletons/README.md",
)

OBSOLETE_GOVERNANCE = (
    "A/B/C approve before implementation",
    "A/B/C cùng duyệt",
    "Task B: A or C is independent approving reviewer",
    "A/C review current B00 head",
    "Independent approval recorded (B reviews A/C; A/C reviews B)",
    "All affected consumers explicitly approve",
    "sau independent review",
    "có independent review",
    "thiếu independent approval",
)

REQUIRED_GOVERNANCE = {
    "AGENTS.md": (
        "Member B là reviewer và integration decision-maker",
        "AI agent không tự approve, merge",
    ),
    ".github/pull_request_template.md": (
        "Member B review / integration closure",
        "B verdict: authorize integration / request changes / blocked",
    ),
    "ai_artifacts/docs/integration-workflow.md": (
        "Member B is the sole integration decision-maker",
        "Do not require a minimum human approval count",
        "separate read-only AI review session",
    ),
}


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


def check_governance() -> int:
    kanban = (ROOT / "ai_artifacts" / "plans" / "kanban.md").read_text(
        encoding="utf-8"
    )
    markdown_reviewers = dict(CARD_REVIEWER.findall(kanban))
    if len(markdown_reviewers) != 21:
        raise AssertionError(
            f"expected 21 Markdown reviewer assignments, found {len(markdown_reviewers)}"
        )

    with (ROOT / "ai_artifacts" / "plans" / "kanban.csv").open(
        encoding="utf-8-sig", newline=""
    ) as handle:
        csv_reviewers = {
            row["id"]: row["reviewer"]
            for row in csv.DictReader(handle)
            if TASK_ID.fullmatch(row["id"])
        }

    if markdown_reviewers != csv_reviewers:
        raise AssertionError("reviewer assignments drift between kanban.md and kanban.csv")
    invalid = {
        task_id: reviewer
        for task_id, reviewer in markdown_reviewers.items()
        if reviewer != "B"
    }
    if invalid:
        raise AssertionError(f"centralized reviewer must be B for every card: {invalid}")

    conflicts: list[str] = []
    for relative in GOVERNANCE_FILES:
        content = (ROOT / relative).read_text(encoding="utf-8")
        for phrase in OBSOLETE_GOVERNANCE:
            if phrase.casefold() in content.casefold():
                conflicts.append(f"{relative}: obsolete governance phrase: {phrase}")
    if conflicts:
        raise AssertionError("\n".join(conflicts))

    missing: list[str] = []
    for relative, phrases in REQUIRED_GOVERNANCE.items():
        content = (ROOT / relative).read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in content:
                missing.append(f"{relative}: missing centralized governance phrase: {phrase}")
    if missing:
        raise AssertionError("\n".join(missing))
    return len(markdown_reviewers)


def main() -> None:
    links = check_local_links()
    task_ids = check_task_ids()
    reviewer_assignments = check_governance()
    print(f"PASS docs: {links} local links resolve")
    print(f"PASS tasks: {len(task_ids)} IDs match between kanban.md and kanban.csv")
    print(
        "PASS governance: "
        f"{reviewer_assignments} reviewer assignments map to Member B with no obsolete rule"
    )


if __name__ == "__main__":
    main()
