#!/usr/bin/env python3
"""Normalize Chinese prose punctuation without touching Markdown/code syntax."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


CJK = "\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff"
CLOSE_CHARS = "」』】）》”’"
OPEN_CHARS = "「『【《（“‘"
LEFT_CONTEXT = CJK + CLOSE_CHARS
RIGHT_CONTEXT = CJK + OPEN_CHARS

PROTECTED = re.compile(
    r"`+[^`\n]*`+"                  # inline code
    r"|(?<=\])\([^\n)]*\)"        # Markdown link destination
    r"|https?://[^\s<>]+"          # bare URL
    r"|<[^>\n]+>"                  # HTML tag
    r"|\$[^$\n]+\$"               # inline math
)

ASCII_TO_CJK = {
    ",": "，",
    ":": "：",
    ";": "；",
    "?": "？",
    "!": "！",
    ".": "。",
}


def protect(text: str) -> tuple[str, list[str]]:
    saved: list[str] = []

    def stash(match: re.Match[str]) -> str:
        saved.append(match.group(0))
        return f"\ue000{len(saved) - 1}\ue001"

    return PROTECTED.sub(stash, text), saved


def restore(text: str, saved: list[str]) -> str:
    for index, value in enumerate(saved):
        text = text.replace(f"\ue000{index}\ue001", value)
    return text


def has_cjk(text: str) -> bool:
    return bool(re.search(f"[{CJK}]", text))


def normalize_parentheses(text: str) -> str:
    pair = re.compile(r"\(([^()\n]{0,240})\)")
    chinese_line = has_cjk(text)

    def replace_pair(match: re.Match[str]) -> str:
        previous = text[match.start() - 1] if match.start() else ""
        following = text[match.end()] if match.end() < len(text) else ""
        inner = match.group(1)
        if chinese_line or has_cjk(inner) or has_cjk(previous) or has_cjk(following) or previous in CLOSE_CHARS or following in OPEN_CHARS:
            return f"（{inner}）"
        return match.group(0)

    text = pair.sub(replace_pair, text)
    text = re.sub(r"（([^（）\n]*)\)", r"（\1）", text)
    text = re.sub(r"\(([^（）\n]*)）", r"（\1）", text)
    return text


def normalize_segment(text: str) -> str:
    text = normalize_parentheses(text)
    for ascii_mark, cjk_mark in ASCII_TO_CJK.items():
        escaped = re.escape(ascii_mark)
        text = re.sub(
            rf"(?<=[{LEFT_CONTEXT}]){escaped}|{escaped}(?=[{RIGHT_CONTEXT}])",
            cjk_mark,
            text,
        )
    text = re.sub(rf"(?<=[{CJK}])\s+([，。；：？！])", r"\1", text)
    text = re.sub(rf"([，。；：？！])\s+(?=[{CJK}{RIGHT_CONTEXT}])", r"\1", text)
    # Markdown emphasis delimiters can sit between punctuation and the next
    # Chinese sentence. Remove the source-only spacer so it is not rendered as
    # an unwanted half-width gap, including legacy non-breaking spaces.
    text = re.sub(r"([，。；：？！])[ \t\u00a0]+(?=(?:\*{1,3}|_{1,3}))", r"\1", text)
    text = re.sub(
        rf"([，。；：？！])((?:\*{{1,3}}|_{{1,3}}))[ \t\u00a0]+(?=[{CJK}{OPEN_CHARS}])",
        r"\1\2",
        text,
    )
    return text


def normalize_markdown(source: str) -> str:
    lines: list[str] = []
    in_fence = False
    for line in source.splitlines(keepends=True):
        if re.match(r"^\s*```", line):
            in_fence = not in_fence
            lines.append(line)
            continue
        if in_fence:
            lines.append(line)
            continue
        masked, saved = protect(line)
        lines.append(restore(normalize_segment(masked), saved))
    return "".join(lines)


def issues(source: str) -> list[tuple[int, str]]:
    found: list[tuple[int, str]] = []
    in_fence = False
    direct = re.compile(
        rf"(?<=[{LEFT_CONTEXT}])[,.:;?!]|[,.:;?!](?=[{RIGHT_CONTEXT}])"
    )
    parenthesis = re.compile(
        rf"(?<=[{LEFT_CONTEXT}])\([^\n)]*\)|\([^\n)]*[{CJK}][^\n)]*\)|（[^（）\n]*\)"
    )
    for number, line in enumerate(source.splitlines(), 1):
        if re.match(r"^\s*```", line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        masked, _ = protect(line)
        emphasis_gap = re.search(
            rf"[，。；：？！][ \t\u00a0]+(?:\*{{1,3}}|_{{1,3}})|"
            rf"[，。；：？！](?:\*{{1,3}}|_{{1,3}})[ \t\u00a0]+(?=[{CJK}{OPEN_CHARS}])",
            masked,
        )
        if direct.search(masked) or parenthesis.search(masked) or emphasis_gap or (has_cjk(masked) and re.search(r"\([^\n)]*\)", masked)):
            found.append((number, line.strip()))
    return found


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", type=Path, default=Path("book.md"))
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    source = args.path.read_text(encoding="utf-8")
    normalized = normalize_markdown(source)
    if args.write and normalized != source:
        args.path.write_text(normalized, encoding="utf-8", newline="\n")

    remaining = issues(normalized)
    before_lines = source.splitlines()
    after_lines = normalized.splitlines()
    changed = sum(a != b for a, b in zip(before_lines, after_lines)) + abs(len(before_lines) - len(after_lines))
    print(f"changed_lines={changed}")
    print(f"remaining_issues={len(remaining)}")
    for number, line in remaining[:20]:
        print(f"{number}: {line}")
    return 1 if remaining else 0


if __name__ == "__main__":
    raise SystemExit(main())
