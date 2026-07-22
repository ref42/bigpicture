#!/usr/bin/env python3
"""Validate the Big Picture Thinking skill package."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_REFERENCES = {
    "references/lenses.md",
    "references/playbooks.md",
    "references/question-bank.md",
    "references/templates.md",
}


def fail(message: str) -> int:
    print(f"[FAIL] {message}")
    return 1


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text()


def parse_frontmatter(content: str) -> dict[str, str] | None:
    match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if not match:
        return None

    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            return None
        key, raw_value = line.split(":", 1)
        key = key.strip()
        value = raw_value.strip()
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        values[key] = value
    return values


def main() -> int:
    if len(sys.argv) != 2:
        return fail("Usage: python scripts/validate_skill.py <skill-directory>")

    skill_dir = Path(sys.argv[1]).resolve()
    if not skill_dir.is_dir():
        return fail(f"Skill directory not found: {skill_dir}")

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        return fail("Missing SKILL.md")

    content = read_text(skill_md)
    frontmatter = parse_frontmatter(content)
    if frontmatter is None:
        return fail("Invalid SKILL.md frontmatter")

    if set(frontmatter) != {"name", "description"}:
        return fail("SKILL.md frontmatter must contain only name and description")

    name = frontmatter["name"].strip()
    if name != "bigpicture":
        return fail(f"Unexpected skill name: {name}")
    if not re.fullmatch(r"[a-z0-9-]+", name):
        return fail("Skill name must use lowercase letters, digits, and hyphens")

    description = frontmatter["description"].strip()
    if not description:
        return fail("Description is empty")
    if len(description) > 1024:
        return fail("Description is longer than 1024 characters")
    if "<" in description or ">" in description:
        return fail("Description must not contain angle brackets")

    all_markdown = [content]
    for rel_path in REQUIRED_REFERENCES:
        path = skill_dir / rel_path
        if not path.is_file():
            return fail(f"Missing reference file: {rel_path}")
        all_markdown.append(read_text(path))

    joined = "\n".join(all_markdown)
    if re.search(r"TODO|\[TODO|placeholder", joined, re.IGNORECASE):
        return fail("Found TODO or placeholder text")

    for rel_path in REQUIRED_REFERENCES:
        if rel_path not in content:
            return fail(f"SKILL.md does not route to {rel_path}")

    openai_yaml = skill_dir / "agents" / "openai.yaml"
    if not openai_yaml.is_file():
        return fail("Missing agents/openai.yaml")

    metadata = read_text(openai_yaml)
    if "display_name:" not in metadata or "short_description:" not in metadata:
        return fail("agents/openai.yaml is missing interface metadata")
    if "$bigpicture" not in metadata:
        return fail("agents/openai.yaml default prompt must mention $bigpicture")

    print("[OK] Skill package is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
