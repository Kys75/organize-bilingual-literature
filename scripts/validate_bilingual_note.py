#!/usr/bin/env python3
"""Validate the structural conventions of a bilingual Obsidian literature note."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


IMAGE_RE = re.compile(r"^!\[[^\]]*\]\(([^)]+)\)\s*$", re.MULTILINE)
NUMERIC_CITATION_RE = re.compile(r"(?<!\\)\[(\d+(?:[-,]\d+)*)\]")
ESCAPED_CITATION_RE = re.compile(r"\\\[(\d+(?:[-,]\d+)*)\\\]")
FIGURE_CAPTION_RE = re.compile(r"^\*\*图\s*(?:S?\d+|[A-Za-z]\d*)。?\*\*", re.MULTILINE)
READING_GUIDE_RE = re.compile(r"^\*\*读图提示。\*\*", re.MULTILINE)
SEPARATE_TRANSLATED_HEADING_RE = re.compile(
    r"^(#{1,6})\s+([^\n（(]+)\n\s*\n\1\s+([^\n（(]+)$", re.MULTILINE
)


def validate(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not path.is_file():
        return [f"File does not exist: {path}"], warnings

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    if path.suffix != ".md" or not path.name.endswith(".bilingual.md"):
        warnings.append("Filename should normally end in .bilingual.md")

    if not text.startswith("---\n"):
        errors.append("Missing YAML frontmatter opening delimiter")
    elif "\n---\n" not in text[4:]:
        errors.append("Missing YAML frontmatter closing delimiter")

    heading_lines = [line for line in lines if line.startswith("#")]
    if not heading_lines:
        errors.append("No Markdown headings found")
    else:
        for heading in heading_lines:
            if "References" in heading or "参考文献" in heading:
                continue
            if "（" not in heading or "）" not in heading:
                warnings.append(f"Heading may not be bilingual on one line: {heading}")

    if SEPARATE_TRANSLATED_HEADING_RE.search(text):
        warnings.append("Possible duplicated English/Chinese heading nodes found")

    dollar_fences = sum(line.strip() == "$$" for line in lines)
    if dollar_fences % 2:
        errors.append(f"Unbalanced display-math fences: {dollar_fences}")

    unescaped = NUMERIC_CITATION_RE.findall(text)
    if unescaped:
        sample = ", ".join(unescaped[:5])
        errors.append(f"Unescaped numeric citations found (sample: {sample})")

    image_paths = IMAGE_RE.findall(text)
    missing_images: list[str] = []
    for raw_path in image_paths:
        image_path = raw_path.split("#", 1)[0]
        if not (path.parent / image_path).is_file():
            missing_images.append(raw_path)
    if missing_images:
        errors.append("Missing image files: " + ", ".join(missing_images))

    figure_captions = len(FIGURE_CAPTION_RE.findall(text))
    reading_guides = len(READING_GUIDE_RE.findall(text))
    if image_paths and figure_captions != len(image_paths):
        warnings.append(
            f"Image/caption count differs: {len(image_paths)} images, "
            f"{figure_captions} Chinese figure captions"
        )
    if figure_captions != reading_guides:
        errors.append(
            f"Every Chinese figure caption needs one reading guide: "
            f"{figure_captions} captions, {reading_guides} guides"
        )

    if not ESCAPED_CITATION_RE.search(text):
        warnings.append("No escaped numeric citations found; acceptable for citation-free lectures")

    if not re.match(r"^\d{2}-\d{2}-\d{2}.+", path.parent.name):
        warnings.append("Parent folder does not match YY-MM-DD中文标题")

    source_files = [
        item
        for item in path.parent.iterdir()
        if item.is_file() and item != path and not item.name.startswith(".")
    ]
    if not source_files:
        warnings.append("No accompanying original source file found")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("note", type=Path, help="Path to the .bilingual.md note")
    args = parser.parse_args()

    errors, warnings = validate(args.note.resolve())
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1

    print(f"OK: {args.note.resolve()} ({len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
