#!/usr/bin/env python3
"""Static integrity and bilingual parity checks for the single-file readers."""

from __future__ import annotations

import hashlib
import json
import re
import struct
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STYLE_KEY = "mq-reading-style-v1"
KEY_CHAPTER_H1_INDEXES = (3, 6, 9, 13)  # Chapters 1, 4, 7, and 11.


class ReaderParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.canonical = ""
        self.alternates: dict[str, str] = {}
        self.description = ""
        self.screen_ids: set[str] = set()
        self.toc_targets: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "meta" and values.get("name") == "description":
            self.description = values.get("content", "") or ""
        if tag == "link" and values.get("rel") == "canonical":
            self.canonical = values.get("href", "") or ""
        if tag == "link" and values.get("rel") == "alternate":
            self.alternates[values.get("hreflang", "") or ""] = values.get("href", "") or ""
        classes = set((values.get("class") or "").split())
        if tag == "section" and "screen" in classes and values.get("id"):
            self.screen_ids.add(values["id"])
        if "toc-a" in classes and values.get("data-target"):
            self.toc_targets.add(values["data-target"])


def relative_luminance(hex_color: str) -> float:
    channels = [int(hex_color[i : i + 2], 16) / 255 for i in (0, 2, 4)]
    linear = [
        value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4
        for value in channels
    ]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast_ratio(a: str, b: str) -> float:
    lighter, darker = sorted((relative_luminance(a), relative_luminance(b)), reverse=True)
    return (lighter + 0.05) / (darker + 0.05)


def png_size(path: Path) -> tuple[int, int]:
    data = path.read_bytes()[:24]
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise AssertionError(f"{path} is not a PNG")
    return struct.unpack(">II", data[16:24])


def payload_from_reader(html: str, relative_path: str) -> dict[str, object]:
    marker = '<script type="application/json" id="conciseContent">'
    assert html.count(marker) == 1, f"{relative_path}: concise payload marker count changed"
    raw = html.split(marker, 1)[1].split("</script>", 1)[0]
    payload = json.loads(raw)
    assert isinstance(payload.get("sections"), dict), f"{relative_path}: invalid concise payload"
    return payload


def split_h1_sections(source: str) -> tuple[list[str], list[str]]:
    matches = list(re.finditer(r"(?m)^# (.+)$", source))
    headings = [match.group(1).strip() for match in matches]
    bodies: list[str] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(source)
        bodies.append(source[match.end() : end].strip())
    return headings, bodies


def markdown_signature(source: str) -> dict[str, object]:
    definitions = re.findall(r"(?m)^\[\^([^\]]+)\]:", source)
    references = re.findall(r"\[\^([^\]]+)\]", source)
    return {
        "h1": len(re.findall(r"(?m)^# ", source)),
        "h2": len(re.findall(r"(?m)^## ", source)),
        "h3": len(re.findall(r"(?m)^### ", source)),
        "definitions": definitions,
        "references": Counter(references),
        "callouts": tuple(source.count(marker) for marker in ("⚠️", "🔬", "📌", "✍️")),
        "tables": len(re.findall(r"(?m)^\s*\|?\s*:?-{3,}", source)),
        "tasks": len(re.findall(r"(?m)^\s*- \[[ xX]\]", source)),
        "unordered": len(re.findall(r"(?m)^\s*- (?!\[)", source)),
        "ordered": len(re.findall(r"(?m)^\s*\d+\. ", source)),
    }


def check_style_source_pair(full: str, concise: str, language: str) -> None:
    full_headings, full_bodies = split_h1_sections(full)
    concise_headings, concise_bodies = split_h1_sections(concise)
    assert full_headings == concise_headings, f"{language}: concise edition changed the H1 structure"
    assert len(full_headings) == 22, f"{language}: unexpected H1 count"
    assert markdown_signature(full) == markdown_signature(concise), (
        f"{language}: headings, footnotes, callouts, tables, exercises, or list structure drifted"
    )
    ratio = len(concise) / len(full)
    assert 0.70 <= ratio <= 0.97, f"{language}: concise/full size ratio {ratio:.3f} is implausible"
    for index in KEY_CHAPTER_H1_INDEXES:
        assert full_bodies[index] != concise_bodies[index], (
            f"{language}: key Chapter H1 index {index} did not change between editions"
        )
    lowered = concise.lower()
    assert not any(token in lowered for token in ("todo", "tbd", "placeholder", "@@ ")), (
        f"{language}: unfinished marker found in concise source"
    )


def check_reader(
    relative_path: str,
    canonical: str,
    cover_path: str,
    concise_source: str,
    expected_language_tokens: tuple[str, ...],
) -> tuple[str, ReaderParser, dict[str, object]]:
    path = ROOT / relative_path
    html = path.read_text(encoding="utf-8")
    parser = ReaderParser()
    parser.feed(html)

    assert parser.description, f"{relative_path}: missing description"
    assert parser.canonical == canonical, f"{relative_path}: wrong canonical"
    assert parser.alternates == {
        "zh-CN": "https://quant.leooo.fun/",
        "en": "https://quant.leooo.fun/en/",
        "x-default": "https://quant.leooo.fun/",
    }, f"{relative_path}: incomplete hreflang set"
    assert parser.toc_targets <= parser.screen_ids, f"{relative_path}: TOC target without a screen"
    assert len(parser.screen_ids) == 21 and len(parser.toc_targets) == 20, (
        f"{relative_path}: unexpected reader structure"
    )
    assert cover_path in html, f"{relative_path}: supplied cover is not referenced"
    assert "sidebar.inert=narrow&&!open" in html, f"{relative_path}: mobile TOC is not inert when hidden"
    assert "brandHome.addEventListener('keydown'" in html, f"{relative_path}: brand keyboard activation missing"
    assert "cover-transition-book" not in html, f"{relative_path}: removed opening transition returned"
    assert "function openFirstPage(){go(idx('00-preface'));focusMain();}" in html, (
        f"{relative_path}: direct preface navigation missing"
    )
    assert ".book-frame{display:none}" in html and ".book-spine{display:block" in html, (
        f"{relative_path}: 3D book layers are not configured"
    )
    assert ".book-volume::after{z-index:0" in html, f"{relative_path}: page-block depth is missing"
    assert ".preface-book-stage{border-bottom:0;background:none}" in html, (
        f"{relative_path}: preface stage background returned"
    )
    assert ".book-volume::before{inset:9px -14px 7px 12px}.book-volume::after{content:none}" in html, (
        f"{relative_path}: page block protrudes below the cover"
    )
    for kind in ("warn", "lab", "points", "exercise"):
        assert f".callout.{kind}::before" in html, f"{relative_path}: {kind} callout design is missing"

    # Reading-style selector and state boundary.
    assert html.count('data-reading-style="') == 2, f"{relative_path}: style choice must remain binary"
    assert f"styleKey='{STYLE_KEY}'" in html, f"{relative_path}: shared style key changed"
    assert "if(!readingStyle&&i>idx('00-preface'))" in html, (
        f"{relative_path}: style choice navigation guard missing"
    )
    assert "function bindFootnotes(root)" in html, f"{relative_path}: swapped footnotes are not rebound"
    assert "if(activeFootnote)closeFootnote(false);" in html, (
        f"{relative_path}: style swap can leave a stale open footnote"
    )
    assert "reader.inert=true" in html and "reader.inert=false" in html, (
        f"{relative_path}: modal does not isolate the reader"
    )
    assert all(token in html for token in expected_language_tokens), (
        f"{relative_path}: localized selector copy missing"
    )

    source = (ROOT / concise_source).read_text(encoding="utf-8")
    payload = payload_from_reader(html, relative_path)
    assert payload["sourceSha256"] == hashlib.sha256(source.encode()).hexdigest(), (
        f"{relative_path}: concise source hash is stale"
    )
    sections = payload["sections"]
    assert set(sections) == parser.screen_ids - {"cover", "00-preface"}, (
        f"{relative_path}: concise style does not cover every post-preface section"
    )
    assert all(isinstance(value, str) and len(value) > 100 for value in sections.values()), (
        f"{relative_path}: empty or implausibly short concise section"
    )
    payload_html = "".join(sections.values())
    assert "**" not in payload_html, f"{relative_path}: unrendered strong markup remains"
    assert payload_html.count('<div class="tablewrap">') == payload_html.count("<table>"), (
        f"{relative_path}: concise tables are not mobile-scroll wrapped"
    )
    assert payload_html.count('class="callout ') == 61, (
        f"{relative_path}: concise callout count changed"
    )
    assert payload_html.count('class="footnote-ref"') == 5, (
        f"{relative_path}: concise post-preface footnote references changed"
    )
    return html, parser, payload


def main() -> None:
    zh, zh_parser, zh_payload = check_reader(
        "index.html",
        "https://quant.leooo.fun/",
        "assets/cover-ai-v2.png",
        "versions/03-humanizer-zh-round2.md",
        ("正文有两种讲法", "生活化版", "精炼版"),
    )
    en, en_parser, en_payload = check_reader(
        "en/index.html",
        "https://quant.leooo.fun/en/",
        "../assets/cover-ai-v2-en.png",
        "versions/03-humanizer-en-round2.md",
        ("TWO WAYS TO READ THE MAIN TEXT", "Story Edition", "Concise Edition"),
    )

    book = (ROOT / "book.md").read_text(encoding="utf-8")
    book_en = (ROOT / "book.en.md").read_text(encoding="utf-8")
    concise_zh = (ROOT / "versions" / "03-humanizer-zh-round2.md").read_text(encoding="utf-8")
    concise_en = (ROOT / "versions" / "03-humanizer-en-round2.md").read_text(encoding="utf-8")
    sw = (ROOT / "sw.js").read_text(encoding="utf-8")

    check_style_source_pair(book, concise_zh, "Chinese")
    check_style_source_pair(book_en, concise_en, "English")
    assert "想象" not in concise_zh and "imagine" not in concise_en.lower(), (
        "formulaic Imagine wording returned"
    )
    assert not re.search(r"[\u3400-\u9fff]", concise_en), "English concise source contains CJK text"

    # Critical risk boundaries that must survive condensation and translation.
    for phrase in (
        "你有可能损失部分、甚至全部的本金",
        "止损能约束你的决定，不能保证你的成交价",
        "熔断不保证能在任何市场里瞬间全平",
        "最小权限和分层隔离",
        "低相关不能替负期望",
    ):
        assert phrase in concise_zh, f"Chinese concise risk boundary missing: {phrase}"
    for phrase in (
        "you may lose some or even all of your principal",
        "a stop-loss can constrain your decision; it cannot guarantee your execution price",
        "a kill switch does not guarantee that every position can be closed instantly",
        "least privilege and layered isolation",
        "Low correlation cannot make negative expectancy acceptable",
    ):
        assert phrase.lower() in concise_en.lower(), f"English concise risk boundary missing: {phrase}"

    assert "first.nodeValue.replace(/^(?:⚠️|🔬|📌|✍️)" in zh, "Chinese callout label cleanup missing"
    assert "first.nodeValue.replace(/^(?:⚠️|🔬|📌|✍️)" in en, "English callout label cleanup missing"
    assert "'01-what-is-quant':'What Is Quant Trading?'" in en, "English short TOC labels missing"
    assert 'class="download-row"' in en, "English download hierarchy missing"
    assert 'href="en/?switch=1"' in zh, "Chinese language link is not cache-routed"
    assert 'href="../?switch=1"' in en, "English language link is not cache-routed"
    assert 'navigator.serviceWorker.register("/sw.js?v=1.1")' in zh, "Chinese language cache is not registered"
    assert 'navigator.serviceWorker.register("/sw.js?v=1.1")' in en, "English language cache is not registered"
    assert 'cacheName="mq-language-v2"' in zh and 'cacheName="mq-language-v2"' in en, (
        "reader language caches are not release-versioned"
    )
    assert 'LANGUAGE_CACHE = "mq-language-v2"' in sw, "service worker cache is stale"
    assert 'event.request.mode !== "navigate"' in sw, "service worker must only handle navigations"
    assert 'url.search === "?switch=1"' in sw, "service worker language-switch guard is missing"
    assert hashlib.sha256(book.encode()).hexdigest() in zh, "Chinese full-source hash is stale"
    assert hashlib.sha256(book_en.encode()).hexdigest() in en, "English full-source hash is stale"
    assert zh_payload["sections"].keys() == en_payload["sections"].keys(), (
        "Chinese and English concise payload section sets differ"
    )

    assert contrast_ratio("ece7da", "5f6961") >= 4.5, "light muted text contrast is too low"
    assert contrast_ratio("0f151c", "8c968e") >= 4.5, "dark muted text contrast is too low"

    for cover in (ROOT / "assets" / "cover-ai-v2.png", ROOT / "assets" / "cover-ai-v2-en.png"):
        assert png_size(cover) == (1024, 1536), f"{cover}: unexpected cover dimensions"

    print("reader checks: passed")


if __name__ == "__main__":
    main()
