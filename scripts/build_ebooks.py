#!/usr/bin/env python3
"""Build the current Markdown source as EPUB 3 and A5 PDF."""

from __future__ import annotations

import argparse
import base64
import datetime as dt
import hashlib
import html
import re
import tempfile
import unicodedata
import uuid
import zipfile
from dataclasses import dataclass
from pathlib import Path
from pathlib import PurePosixPath
from xml.etree import ElementTree

from markdown_compat import markdown_to_html
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, TextStringObject


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "book.md"
EN_SOURCE = ROOT / "book.en.md"
ZH_READER = ROOT / "index.html"
EN_READER = ROOT / "en" / "index.html"
OUTPUT = ROOT / "output"
EPUB_PATH = OUTPUT / "epub" / "诚实的量化交易-1.1.epub"
PDF_PATH = OUTPUT / "pdf" / "诚实的量化交易-1.1.pdf"
COVER_PATH = ROOT / "assets" / "cover-ai-v2.png"

TITLE = "诚实的量化交易：写给新手的第一堂课"
AUTHOR = "@Ackyess"
LANG = "zh-CN"
UID = "urn:uuid:" + str(uuid.uuid5(uuid.NAMESPACE_URL, "https://quant.leooo.fun/"))


SLUGS = [
    "00-preface",
    "01-what-is-quant",
    "02-almost-efficient-markets",
    "03-day-in-the-life",
    "04-market-microstructure",
    "05-data-lifeblood",
    "06-from-intuition-to-hypothesis",
    "07-backtesting",
    "08-statistical-rigor",
    "09-signals-and-factors",
    "10-transaction-costs",
    "11-risk-management",
    "12-portfolio",
    "13-research-to-live",
    "14-pitfalls-and-psychology",
    "15-negative-results-are-knowledge",
    "16-find-your-corner",
    "90-afterword",
    "91-glossary",
    "92-checklist",
]

SECTION_HEADING = re.compile(
    r"(?m)^# (前言[:：].*|第\d+章 .*|结语[:：].*|附录A[:：].*|附录B[:：].*)\s*$"
)
MARKDOWN_EXTENSIONS = ["extra", "sane_lists"]
CALLOUT_MARKERS = (("⚠", "warn"), ("🔬", "lab"), ("📌", "points"), ("✍", "exercise"))
MARKER_RE = re.compile(r"[⚠🔬📌✍]\ufe0f?[ \t]*")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$")
QUOTE_RE = re.compile(r"^>\s?(.*)$")


@dataclass(frozen=True)
class Section:
    slug: str
    title: str
    markdown: str
    body_html: str


def callout_kind(text: str) -> str | None:
    return next((kind for marker, kind in CALLOUT_MARKERS if marker in text), None)


def without_marker(text: str) -> str:
    return MARKER_RE.sub("", text).strip()


def emit_callout(kind: str, body: list[str]) -> list[str]:
    return ["", f'<aside class="callout {kind}" markdown="1">', "", *body, "", "</aside>", ""]


def transform_callouts(source: str) -> str:
    """Turn emoji-labelled Markdown sections into asset-free EPUB cards."""
    lines = source.splitlines()
    output: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        heading = HEADING_RE.match(line)
        kind = callout_kind(heading.group(2)) if heading else None
        if heading and kind:
            level = len(heading.group(1))
            body = [f"**{without_marker(heading.group(2))}**", ""]
            index += 1
            while index < len(lines):
                following = HEADING_RE.match(lines[index])
                if following and len(following.group(1)) <= level:
                    break
                body.append(lines[index])
                index += 1
            output.extend(emit_callout(kind, body))
            continue

        quote = QUOTE_RE.match(line)
        kind = callout_kind(quote.group(1)) if quote else None
        if quote and kind:
            body = [without_marker(quote.group(1))]
            index += 1
            while index < len(lines):
                following = QUOTE_RE.match(lines[index])
                if following:
                    if callout_kind(following.group(1)):
                        break
                    body.append(following.group(1))
                    index += 1
                    continue
                if not lines[index].strip():
                    next_content = index + 1
                    while next_content < len(lines) and not lines[next_content].strip():
                        next_content += 1
                    if next_content < len(lines) and QUOTE_RE.match(lines[next_content]):
                        body.append("")
                        index = next_content
                        continue
                break
            output.extend(emit_callout(kind, body))
            continue

        output.append(line)
        index += 1
    return MARKER_RE.sub("", "\n".join(output))


def split_sections(source: str) -> list[Section]:
    matches = list(SECTION_HEADING.finditer(source))
    if len(matches) != len(SLUGS):
        raise ValueError(f"expected {len(SLUGS)} sections, found {len(matches)}")

    sections: list[Section] = []
    for index, (slug, match) in enumerate(zip(SLUGS, matches)):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(source)
        title = match.group(1).strip()
        body = source[match.end() : end].strip()
        body = re.sub(r"\n\s*---\s*$", "", body).strip()
        body = re.sub(r"(?m)^# 如何阅读本书$", "## 如何阅读本书", body)
        rendered = markdown_to_html(transform_callouts(body))
        sections.append(Section(slug, title, body, rendered))
    return sections


def build_cover(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(COVER_PATH.read_bytes())


EPUB_CSS = """@charset "utf-8";
html{font-size:100%;}
body{font-family:"Noto Serif SC","Source Han Serif SC","Songti SC",serif;line-height:1.72;color:#20272b;margin:0;padding:0;}
h1,h2,h3{font-family:"Noto Sans SC","Source Han Sans SC","PingFang SC",sans-serif;color:#172229;page-break-after:avoid;letter-spacing:-.01em;overflow-wrap:anywhere;}
h1{font-size:1.65em;line-height:1.35;margin:.1em 0 .85em;}
h2{font-size:1.22em;margin:1.75em 0 .55em;border-bottom:1px solid #ccd3cf;padding-bottom:.2em;}
h3{font-size:1.06em;margin:1.4em 0 .4em;color:#315f5b;}
p{margin:0 0 .82em;text-align:justify;text-justify:inter-ideograph;orphans:2;widows:2;} a{color:#315f5b;text-decoration:none;} strong{font-weight:700;}
ul,ol{margin:0 0 1em;padding-left:1.4em;} li{margin:.35em 0;} hr{border:0;border-top:1px solid #d5d7d3;margin:2em 0;}
blockquote{margin:1.4em 0;padding:.2em 1em;border-left:3px solid #8da5a1;background:#f3f5f3;color:#39423e;}
code{font-family:monospace;background:#f1f1ed;padding:.05em .25em;} pre{white-space:pre-wrap;overflow-wrap:anywhere;}
img,svg{max-width:100%;height:auto;} table{border-collapse:collapse;width:100%;table-layout:fixed;margin:1.25em 0;font-size:.78em;} th,td{border:1px solid #c9cecb;padding:.3em .38em;overflow-wrap:anywhere;word-break:break-word;} th{background:#eef2ef;}
.callout{margin:1.35em 0;padding:.72em .9em;border:1px solid #d2d7d3;border-left:4px solid #7d8780;} .callout.warn{border-left-color:#a86b24}.callout.lab{border-left-color:#39706c}.callout.points{border-left-color:#39434a}.callout.exercise{border-left-color:#9a742f;border-left-style:dashed}
.callout>p:first-child,.callout>h3:first-child{font-family:"Noto Sans SC","Source Han Sans SC","PingFang SC",sans-serif;font-weight:700;margin-top:0;margin-bottom:.65em;color:#24312f}.callout>p:last-child,.callout>ul:last-child,.callout>ol:last-child{margin-bottom:0}
.cover{margin:0;padding:0;text-align:center;} .cover img{display:block;width:100%;height:auto;margin:0 auto;}
.nav ol{list-style:none;padding:0;} .nav li{padding:.35em 0;border-bottom:1px dotted #d2d5d2;}
.footnote{font-size:.84em;color:#4e5652;border-top:1px solid #d5d7d3;margin-top:1.5em;padding-top:.7em;} .footnote>hr{display:none}.footnote ol{padding-left:1.25em}.footnote-backref{margin-left:.25em;} sup{line-height:0}
"""


def xhtml_page(title: str, body: str, body_class: str = "") -> str:
    return f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="{LANG}" xml:lang="{LANG}">
<head><meta charset="utf-8"/><title>{html.escape(title)}</title><link rel="stylesheet" type="text/css" href="style.css"/></head>
<body class="{body_class}">{body}</body></html>'''


def build_epub(sections: list[Section], cover_path: Path, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    modified = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    items = []
    itemrefs = [
        '<itemref idref="cover" linear="yes"/>',
        '<itemref idref="license" linear="yes"/>',
    ]
    nav_items = []
    ncx_items = []
    pages: dict[str, str] = {}

    for order, section in enumerate(sections, 1):
        filename = f"{section.slug}.xhtml"
        item_id = f"s{order}"
        items.append(f'<item id="{item_id}" href="{filename}" media-type="application/xhtml+xml"/>')
        itemrefs.append(f'<itemref idref="{item_id}"/>')
        nav_items.append(f'<li><a href="{filename}">{html.escape(section.title)}</a></li>')
        ncx_items.append(
            f'<navPoint id="n{order}" playOrder="{order}"><navLabel><text>{html.escape(section.title)}</text></navLabel><content src="{filename}"/></navPoint>'
        )
        body = f'<section epub:type="chapter"><h1>{html.escape(section.title)}</h1>{section.body_html}</section>'
        pages[filename] = xhtml_page(section.title, body)

    nav = xhtml_page(
        "目录",
        '<nav epub:type="toc" id="toc" class="nav"><h1>目录</h1><ol>' + "".join(nav_items) + "</ol></nav>",
    )
    ncx = f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE ncx PUBLIC "-//NISO//DTD ncx 2005-1//EN" "http://www.daisy.org/z3986/2005/ncx-2005-1.dtd">
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1"><head><meta name="dtb:uid" content="{UID}"/><meta name="dtb:depth" content="1"/></head><docTitle><text>{TITLE}</text></docTitle><navMap>{''.join(ncx_items)}</navMap></ncx>'''
    manifest = "".join(
        [
            '<item id="css" href="style.css" media-type="text/css"/>',
            '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
            '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
            '<item id="cover-image" href="images/cover.png" media-type="image/png" properties="cover-image"/>',
            '<item id="cover" href="cover.xhtml" media-type="application/xhtml+xml"/>',
            '<item id="license" href="license.xhtml" media-type="application/xhtml+xml"/>',
            *items,
        ]
    )
    opf = f'''<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid" xml:lang="{LANG}">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:identifier id="bookid">{UID}</dc:identifier><dc:title>{TITLE}</dc:title><dc:creator>{AUTHOR}</dc:creator><dc:language>{LANG}</dc:language><dc:description>写给量化交易新手的第一堂课。教育与知识分享用途，不构成投资建议。</dc:description><dc:rights>© 2026 @Ackyess；书籍内容采用 CC BY-SA 4.0</dc:rights><meta property="dcterms:modified">{modified}</meta><meta name="cover" content="cover-image"/></metadata>
<manifest>{manifest}</manifest><spine toc="ncx">{''.join(itemrefs)}</spine></package>'''
    container = '''<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>'''
    cover = xhtml_page(
        "封面",
        '<section epub:type="cover"><img src="images/cover.png" alt="《诚实的量化交易》封面"/></section>',
        "cover",
    )
    license_page = xhtml_page(
        "版权与许可",
        '<section><h1>版权与许可</h1><p>作者：@Ackyess</p><p>© 2026 @Ackyess</p><p>本书文字、封面及生成的 EPUB/PDF 内容采用 <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a> 许可；阅读器代码与构建脚本采用 MIT License。</p><p>项目地址：<a href="https://github.com/Ackyess/metaquant-book">github.com/Ackyess/metaquant-book</a></p></section>',
    )

    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
        mime = zipfile.ZipInfo("mimetype")
        mime.compress_type = zipfile.ZIP_STORED
        archive.writestr(mime, "application/epub+zip")
        archive.writestr("META-INF/container.xml", container)
        archive.writestr("OEBPS/style.css", EPUB_CSS)
        archive.writestr("OEBPS/nav.xhtml", nav)
        archive.writestr("OEBPS/toc.ncx", ncx)
        archive.writestr("OEBPS/content.opf", opf)
        archive.writestr("OEBPS/cover.xhtml", cover)
        archive.writestr("OEBPS/license.xhtml", license_page)
        archive.write(cover_path, "OEBPS/images/cover.png")
        for filename, content in pages.items():
            archive.writestr(f"OEBPS/{filename}", content)


PRINT_CSS = """
*{box-sizing:border-box} html{font-size:10.5pt} body{margin:0;color:#20272b;font-family:SimSun,"Songti SC","Noto Serif CJK SC","Source Han Serif SC",serif;line-height:1.78}
h1,h2,h3{font-family:"Microsoft YaHei","PingFang SC","Noto Sans CJK SC","Source Han Sans SC",sans-serif;page-break-after:avoid;color:#172229}
h1{font-size:24pt;line-height:1.25;margin:0 0 16mm} h2{font-size:15pt;margin:9mm 0 3mm;padding-bottom:1.5mm;border-bottom:.25mm solid #c9ceca} h3{font-size:12pt;margin:6mm 0 2mm;color:#315f5b}
p{margin:0 0 4.2mm;text-align:justify;orphans:3;widows:3} strong{font-weight:700} a{color:inherit;text-decoration:none}
ul,ol{padding-left:1.4em;margin:0 0 4mm} li{margin:1.2mm 0} blockquote{margin:5mm 0;padding:2.5mm 4mm;border-left:1mm solid #8da5a1;background:#f3f5f3;color:#39423e;break-inside:avoid}
hr{border:0;border-top:.25mm solid #d1d4d1;margin:8mm 0} code{font-family:Consolas,monospace;background:#f0f0ec;padding:0 .7mm} pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:8.5pt}
table{border-collapse:collapse;width:100%;table-layout:fixed;margin:5mm 0;font-size:8.7pt;break-inside:avoid} th,td{border:.25mm solid #c4cac6;padding:1.6mm 2mm;overflow-wrap:anywhere} th{background:#eef2ef}
.callout{margin:5mm 0;padding:3mm 4mm;border:.25mm solid #d2d7d3;border-left:1mm solid #7d8780;background:#f8faf8;break-inside:avoid}.callout.warn{border-left-color:#a86b24}.callout.lab{border-left-color:#39706c;break-inside:auto;box-decoration-break:clone;-webkit-box-decoration-break:clone}.callout.points{border-left-color:#39434a}.callout.exercise{border-left-color:#9a742f;border-left-style:dashed}
.callout>p:first-child,.callout>h3:first-child{font-family:"Microsoft YaHei","PingFang SC","Noto Sans CJK SC","Source Han Sans SC",sans-serif;font-weight:700;margin-top:0;margin-bottom:2.5mm;color:#24312f}.callout>p:last-child,.callout>ul:last-child,.callout>ol:last-child{margin-bottom:0}
.colophon{break-after:page;padding-top:42mm}.colophon h1{margin-bottom:9mm}.colophon p{color:#555d59}.toc{break-after:page}.toc h1{margin-bottom:5mm}.toc ol{list-style:none;padding:0;columns:2;column-gap:9mm;font-size:8.7pt;line-height:1.35}.toc li{break-inside:avoid;border-bottom:.25mm dotted #c8cdca;padding:.7mm 0}
.chapter{break-before:page}.chapter:first-of-type{break-before:auto}.chapter>.footnote{font-size:8pt;line-height:1.45;color:#555d59;border-top:.25mm solid #d1d4d1;margin-top:4mm;padding-top:1.5mm}.chapter>.footnote>hr{display:none}.chapter>.footnote ol{margin:0;padding-left:1.2em}.chapter>.footnote li{margin:0}
"""

PRINT_PAGE_CSS = """
@page{size:A5;margin:15mm 14mm 17mm 14mm;@bottom-center{content:counter(page);font:8px Arial;color:#777}}
"""


def print_html(sections: list[Section]) -> str:
    toc = "".join(f'<li><a href="#{s.slug}">{html.escape(s.title)}</a></li>' for s in sections)
    chapters = "".join(
        f'<section class="chapter" id="{s.slug}"><h1>{html.escape(s.title)}</h1>{s.body_html}</section>'
        for s in sections
    )
    colophon = '<section class="colophon"><h1>版权与许可</h1><p>作者：@Ackyess</p><p>© 2026 @Ackyess</p><p>本书文字、封面及生成的 EPUB/PDF 内容采用 CC BY-SA 4.0 许可；阅读器代码与构建脚本采用 MIT License。</p><p>github.com/Ackyess/metaquant-book</p></section>'
    return f'''<!doctype html><html lang="{LANG}"><head><meta charset="utf-8"><title>{TITLE}</title><style>{PRINT_CSS}{PRINT_PAGE_CSS}</style></head><body>{colophon}<nav class="toc"><h1>目录</h1><ol>{toc}</ol></nav>{chapters}</body></html>'''


def build_pdf(sections: list[Section], cover_path: Path, output: Path) -> None:
    try:
        from weasyprint import HTML
    except (ImportError, OSError) as exc:
        raise RuntimeError(
            "PDF generation requires WeasyPrint and its native Pango dependencies. "
            "See https://doc.courtbouillon.org/weasyprint/stable/first_steps.html"
        ) from exc

    output.parent.mkdir(parents=True, exist_ok=True)
    cover_data = base64.b64encode(cover_path.read_bytes()).decode("ascii")
    cover_html = f'''<!doctype html><html lang="{LANG}"><head><meta charset="utf-8"><style>@page{{size:A5;margin:0}}html,body{{margin:0;width:100%;height:100%;background:#0d141c}}img{{width:100%;height:100%;object-fit:cover;display:block}}</style></head><body><img src="data:image/png;base64,{cover_data}" alt="《诚实的量化交易》封面"></body></html>'''

    with tempfile.TemporaryDirectory(prefix="metaquant-pdf-") as temporary:
        temp = Path(temporary)
        cover_pdf, content_pdf = temp / "cover.pdf", temp / "content.pdf"
        HTML(string=cover_html, base_url=str(ROOT)).write_pdf(str(cover_pdf))
        HTML(string=print_html(sections), base_url=str(ROOT)).write_pdf(str(content_pdf))

        writer = PdfWriter()
        writer.append(str(cover_pdf))
        writer.append(str(content_pdf))
        writer.page_mode = "/UseOutlines"
        writer._root_object[NameObject("/Lang")] = TextStringObject(LANG)
        writer.add_metadata({"/Title": TITLE, "/Author": AUTHOR, "/Subject": "量化交易入门", "/Copyright": "© 2026 @Ackyess；书籍内容采用 CC BY-SA 4.0"})
        with output.open("wb") as target:
            writer.write(target)


def validate_epub(path: Path, expected_sections: int) -> None:
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        assert infos[0].filename == "mimetype" and infos[0].compress_type == zipfile.ZIP_STORED
        assert archive.read("mimetype") == b"application/epub+zip"
        assert archive.testzip() is None
        names = set(archive.namelist())
        assert "OEBPS/images/cover.png" in names and "OEBPS/nav.xhtml" in names
        assert len([name for name in names if re.fullmatch(r"OEBPS/(?:\d\d|\d\d\d)-.+\.xhtml", name)]) == expected_sections
        opf = ElementTree.fromstring(archive.read("OEBPS/content.opf"))
        for item in opf.findall(".//{http://www.idpf.org/2007/opf}item"):
            target = str(PurePosixPath("OEBPS") / item.attrib["href"])
            assert target in names, f"missing manifest asset: {target}"
        rendered = "\n".join(
            archive.read(name).decode("utf-8") for name in names if name.endswith(".xhtml")
        )
        assert "**" not in rendered, "EPUB contains unrendered strong markup"
        assert not MARKER_RE.search(rendered), "emoji marker remained in EPUB"
        expected_callouts = sum(
            1
            for line in SOURCE.read_text(encoding="utf-8").splitlines()
            if MARKER_RE.search(line) and (HEADING_RE.match(line) or QUOTE_RE.match(line))
        )
        assert rendered.count('class="callout ') == expected_callouts
        assert 'src="http' not in rendered, "EPUB contains a remote image"
        for name in names:
            if name.endswith((".xhtml", ".xml", ".opf", ".ncx")):
                ElementTree.fromstring(archive.read(name))


def validate_pdf(path: Path) -> None:
    reader = PdfReader(str(path))
    assert len(reader.pages) > 50
    raw_text = "\n".join((page.extract_text() or "") for page in reader.pages)
    text = re.sub(
        r"\s+",
        "",
        unicodedata.normalize("NFKC", raw_text),
    )
    expected = [section.title for section in split_sections(SOURCE.read_text(encoding="utf-8"))]
    missing = [
        title
        for title in expected
        if re.sub(r"\s+", "", unicodedata.normalize("NFKC", title)) not in text
    ]
    assert not missing, f"PDF is missing section titles: {missing}"
    radical_ranges = (("\u2e80", "\u2eff"), ("\u2f00", "\u2fdf"), ("\u31c0", "\u31ef"))
    radicals = sorted(
        {char for char in raw_text if any(start <= char <= end for start, end in radical_ranges)}
    )
    assert not radicals, f"PDF text uses CJK radical/stroke forms: {radicals}"
    assert "\ufffd" not in raw_text, "PDF text contains replacement characters"
    assert "**" not in raw_text, "PDF contains unrendered strong markup"
    assert not MARKER_RE.search(raw_text), "emoji marker remained in PDF"
    assert reader.outline, "PDF has no document outline"
    assert reader.trailer["/Root"].get("/Lang") == LANG


def validate_bilingual_reader() -> None:
    chinese = SOURCE.read_text(encoding="utf-8")
    english = EN_SOURCE.read_text(encoding="utf-8")
    for pattern in (
        r"(?m)^# ",
        r"(?m)^## ",
        r"(?m)^### ",
        r"(?m)^\s*[-*]\s+\[[ xX]\]",
        r"(?m)^\[\^[^]]+\]:",
        r"[⚠🔬📌✍]",
    ):
        assert len(re.findall(pattern, english)) == len(re.findall(pattern, chinese)), pattern
    assert not re.search(r"[\u3400-\u9fff]", english), "English source contains CJK text"

    zh_html = ZH_READER.read_text(encoding="utf-8")
    en_html = EN_READER.read_text(encoding="utf-8")
    screens = re.findall(
        r'<section(?=[^>]*\bclass="[^"]*\bscreen\b[^"]*")(?=[^>]*\bid="([^"]+)")[^>]*>',
        en_html,
    )
    assert screens == ["cover", *SLUGS]
    assert re.findall(r'\bdata-target="([^"]+)"', en_html) == SLUGS
    assert len(re.findall(r'<button\b[^>]*\bclass="footnote-ref"', en_html)) == 6
    assert re.search(r'<html\b[^>]*\blang="en"', en_html)
    assert 'id="langBtn"' in zh_html and 'href="en/?switch=1"' in zh_html
    assert 'id="langBtn"' in en_html and 'href="../?switch=1"' in en_html
    assert "languageLink.hash='#'+ids[cur]" in zh_html
    assert "languageLink.hash='#'+ids[cur]" in en_html
    assert "mq-reading-position-v1-en" in en_html
    source_hash = hashlib.sha256(english.encode()).hexdigest()
    assert re.search(
        rf'<meta(?=[^>]*\bname="source-sha256")(?=[^>]*\bcontent="{source_hash}")[^>]*>',
        en_html,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--format", choices=("all", "epub", "pdf"), default="all")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    if args.check:
        validate_epub(EPUB_PATH, len(SLUGS))
        validate_pdf(PDF_PATH)
        validate_bilingual_reader()
        print(f"EPUB OK: {EPUB_PATH}")
        print(f"PDF OK: {PDF_PATH}")
        print(f"Bilingual reader OK: {EN_READER}")
        return 0

    sections = split_sections(SOURCE.read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory(prefix="metaquant-cover-") as temporary:
        cover = Path(temporary) / "cover.png"
        build_cover(cover)
        if args.format in ("all", "epub"):
            build_epub(sections, cover, EPUB_PATH)
            validate_epub(EPUB_PATH, len(sections))
            print(f"EPUB: {EPUB_PATH} ({EPUB_PATH.stat().st_size} bytes)")
        if args.format in ("all", "pdf"):
            build_pdf(sections, cover, PDF_PATH)
            validate_pdf(PDF_PATH)
            print(f"PDF: {PDF_PATH} ({PDF_PATH.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
