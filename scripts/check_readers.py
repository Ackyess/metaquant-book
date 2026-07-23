#!/usr/bin/env python3
"""Static integrity checks for the bilingual single-file readers."""

from __future__ import annotations

import hashlib
import struct
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


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
            self.description = values.get("content", "")
        if tag == "link" and values.get("rel") == "canonical":
            self.canonical = values.get("href", "")
        if tag == "link" and values.get("rel") == "alternate":
            self.alternates[values.get("hreflang", "")] = values.get("href", "")
        classes = set((values.get("class") or "").split())
        if tag == "section" and "screen" in classes and values.get("id"):
            self.screen_ids.add(values["id"])
        if "toc-a" in classes and values.get("data-target"):
            self.toc_targets.add(values["data-target"])


def relative_luminance(hex_color: str) -> float:
    channels = [int(hex_color[i : i + 2], 16) / 255 for i in (0, 2, 4)]
    linear = [value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4 for value in channels]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast_ratio(a: str, b: str) -> float:
    lighter, darker = sorted((relative_luminance(a), relative_luminance(b)), reverse=True)
    return (lighter + 0.05) / (darker + 0.05)


def png_size(path: Path) -> tuple[int, int]:
    data = path.read_bytes()[:24]
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise AssertionError(f"{path} is not a PNG")
    return struct.unpack(">II", data[16:24])


def check_reader(relative_path: str, canonical: str, cover_path: str) -> None:
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
    assert len(parser.screen_ids) == 21 and len(parser.toc_targets) == 20, f"{relative_path}: unexpected reader structure"
    assert cover_path in html, f"{relative_path}: supplied cover is not referenced"
    assert "sidebar.inert=narrow&&!open" in html, f"{relative_path}: mobile TOC is not inert when hidden"
    assert "brandHome.addEventListener('keydown'" in html, f"{relative_path}: brand keyboard activation missing"
    assert "cover-transition-book" in html and "openFirstPage" in html, f"{relative_path}: opening transition missing"
    assert ".book-frame{display:none}" in html and ".book-spine{display:block" in html, (
        f"{relative_path}: 3D book layers are not configured"
    )
    assert ".book-volume::after{z-index:0" in html, f"{relative_path}: page-block depth is missing"
    for kind in ("warn", "lab", "points", "exercise"):
        assert f".callout.{kind}::before" in html, f"{relative_path}: {kind} callout design is missing"


def main() -> None:
    check_reader("index.html", "https://quant.leooo.fun/", 'assets/cover-ai-v2.png')
    check_reader("en/index.html", "https://quant.leooo.fun/en/", '../assets/cover-ai-v2-en.png')

    zh = (ROOT / "index.html").read_text(encoding="utf-8")
    en = (ROOT / "en" / "index.html").read_text(encoding="utf-8")
    book = (ROOT / "book.md").read_text(encoding="utf-8")
    book_en = (ROOT / "book.en.md").read_text(encoding="utf-8")
    sw = (ROOT / "sw.js").read_text(encoding="utf-8")
    assert "first.nodeValue.replace(/^(?:⚠️|🔬|📌|✍️)" in zh, "Chinese callout label cleanup missing"
    assert "'01-what-is-quant':'What Is Quant Trading?'" in en, "English short TOC labels missing"
    assert 'class="download-row"' in en, "English download hierarchy missing"
    assert 'href="en/?switch=1"' in zh, "Chinese language link is not cache-routed"
    assert 'href="../?switch=1"' in en, "English language link is not cache-routed"
    assert 'navigator.serviceWorker.register("/sw.js")' in zh, "Chinese language cache is not registered"
    assert 'navigator.serviceWorker.register("/sw.js")' in en, "English language cache is not registered"
    assert 'event.request.mode !== "navigate"' in sw, "service worker must only handle navigations"
    assert 'url.search === "?switch=1"' in sw, "service worker language-switch guard is missing"
    assert "想象" not in book and "想象" not in zh, "formulaic 想象 wording returned"
    assert "imagine" not in book_en.lower() and "imagine" not in en.lower(), "formulaic Imagine wording returned"
    assert hashlib.sha256(book.encode()).hexdigest() in zh, "Chinese source hash is stale"
    assert hashlib.sha256(book_en.encode()).hexdigest() in en, "English source hash is stale"

    assert contrast_ratio("ece7da", "5f6961") >= 4.5, "light muted text contrast is too low"
    assert contrast_ratio("0f151c", "8c968e") >= 4.5, "dark muted text contrast is too low"

    for cover in (ROOT / "assets" / "cover-ai-v2.png", ROOT / "assets" / "cover-ai-v2-en.png"):
        assert png_size(cover) == (1024, 1536), f"{cover}: unexpected cover dimensions"

    print("reader checks: passed")


if __name__ == "__main__":
    main()
