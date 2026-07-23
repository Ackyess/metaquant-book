#!/usr/bin/env python3
"""Embed the alternate prose style in both single-file readers."""

from __future__ import annotations

import hashlib
import html
import json
import re
from dataclasses import dataclass
from pathlib import Path

from markdown_compat import markdown_to_html

from build_ebooks import MARKDOWN_EXTENSIONS, SLUGS, transform_callouts


ROOT = Path(__file__).resolve().parents[1]
PAYLOAD_RE = re.compile(
    r'(<script type="application/json" id="conciseContent">).*?(</script>)',
    re.DOTALL,
)
FOOTNOTE_DEFINITION_RE = re.compile(r"(?m)^\[\^([^\]]+)\]:\s*.+$")
FOOTNOTE_REFERENCE_RE = re.compile(r"\[\^([^\]]+)\]")


@dataclass(frozen=True)
class ReaderStyleConfig:
    source: Path
    reader: Path
    section_heading: re.Pattern[str]
    how_to_heading: str
    footnote_label: str


CONFIGS = (
    ReaderStyleConfig(
        source=ROOT / "versions" / "03-humanizer-zh-round2.md",
        reader=ROOT / "index.html",
        section_heading=re.compile(
            r"(?m)^# (前言[:：].*|第\d+章 .*|结语[:：].*|附录A[:：].*|附录B[:：].*)\s*$"
        ),
        how_to_heading="如何阅读本书",
        footnote_label="查看脚注",
    ),
    ReaderStyleConfig(
        source=ROOT / "versions" / "03-humanizer-en-round2.md",
        reader=ROOT / "en" / "index.html",
        section_heading=re.compile(
            r"(?m)^# (Preface:.*|Chapter \d+:.*|Conclusion:.*|Appendix A:.*|Appendix B:.*)\s*$"
        ),
        how_to_heading="How to Read This Book",
        footnote_label="View footnote",
    ),
)


def replace_footnotes(source: str, label: str) -> str:
    without_definitions = FOOTNOTE_DEFINITION_RE.sub("", source)
    numbers: dict[str, int] = {}

    def button(match: re.Match[str]) -> str:
        note_id = match.group(1)
        number = numbers.setdefault(note_id, len(numbers) + 1)
        safe_id = html.escape(note_id, quote=True)
        return (
            f'<button type="button" class="footnote-ref" data-note-id="{safe_id}" '
            f'aria-label="{label} {number}" aria-controls="footnoteCard" '
            f'aria-expanded="false">{number}</button>'
        )

    return FOOTNOTE_REFERENCE_RE.sub(button, without_definitions)


def split_rendered_sections(source: str, config: ReaderStyleConfig) -> dict[str, str]:
    matches = list(config.section_heading.finditer(source))
    if len(matches) != len(SLUGS):
        raise ValueError(
            f"{config.source}: expected {len(SLUGS)} sections, found {len(matches)}"
        )

    sections: dict[str, str] = {}
    for index, (slug, match) in enumerate(zip(SLUGS, matches)):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(source)
        body = source[match.end() : end].strip()
        body = re.sub(r"\n\s*---\s*$", "", body).strip()
        body = re.sub(
            rf"(?m)^# {re.escape(config.how_to_heading)}$",
            f"## {config.how_to_heading}",
            body,
        )
        rendered = markdown_to_html(transform_callouts(body))
        rendered = rendered.replace("<table>", '<div class="tablewrap"><table>').replace(
            "</table>", "</table></div>"
        )
        sections[slug] = rendered
    return sections


def build_payload(config: ReaderStyleConfig) -> str:
    source = config.source.read_text(encoding="utf-8")
    rendered = split_rendered_sections(
        replace_footnotes(source, config.footnote_label), config
    )
    content = {slug: rendered[slug] for slug in SLUGS[1:]}
    assert list(content) == SLUGS[1:]
    payload = {
        "sourceSha256": hashlib.sha256(source.encode()).hexdigest(),
        "sections": content,
    }
    return json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace(
        "</", "<\\/"
    )


def update_reader(config: ReaderStyleConfig) -> None:
    reader = config.reader.read_text(encoding="utf-8")
    payload = build_payload(config)
    updated, count = PAYLOAD_RE.subn(
        lambda match: match.group(1) + payload + match.group(2), reader
    )
    if count != 1:
        raise AssertionError(f"{config.reader}: conciseContent payload marker missing")
    config.reader.write_text(updated, encoding="utf-8", newline="\n")
    print(f"reader styles: embedded {config.source.name} -> {config.reader.relative_to(ROOT)}")


def main() -> None:
    for config in CONFIGS:
        update_reader(config)


if __name__ == "__main__":
    main()
