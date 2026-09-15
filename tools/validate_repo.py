"""Validate the redistributable repository structure and documentation links."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    ".github/workflows/validate.yml",
    "docs/ae-depth-workflow.md",
    "docs/bcc-depth-map-ml.md",
    "docs/capcut-finishing.md",
    "docs/color-audio-handoff.md",
    "docs/checklist.md",
    "examples/metadata.example.json",
    "examples/export-settings.example.yml",
)
REQUIRED_DIRS = (
    "docs",
    "examples",
    "templates/project-structure",
    "tools",
    "tests",
)


def markdown_links(path: Path) -> list[str]:
    return re.findall(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]+)?\)", path.read_text(encoding="utf-8"))


def validate() -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")
    for relative in REQUIRED_DIRS:
        if not (ROOT / relative).is_dir():
            errors.append(f"missing required directory: {relative}")

    for markdown in ROOT.rglob("*.md"):
        for target in markdown_links(markdown):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (markdown.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"broken link in {markdown.relative_to(ROOT)}: {target}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for required_phrase in ("proprietary", "Quick start", "Troubleshooting", "Contributing"):
        if required_phrase.lower() not in readme.lower():
            errors.append(f"README is missing required topic: {required_phrase}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print("Repository structure and local documentation links are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
