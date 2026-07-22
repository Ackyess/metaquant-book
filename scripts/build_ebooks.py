#!/usr/bin/env python3
"""Build the current Markdown source as EPUB 3 and A5 PDF."""

from __future__ import annotations

import argparse
import base64
import datetime as dt
import html
import re
import tempfile
import unicodedata
import uuid
import zipfile
from dataclasses import dataclass
from pathlib import Path
from xml.etree import ElementTree

import markdown
from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "book.md"
OUTPUT = ROOT / "output"
EPUB_PATH = OUTPUT / "epub" / "诚实的量化交易-1.0.epub"
PDF_PATH = OUTPUT / "pdf" / "诚实的量化交易-1.0.pdf"

TITLE = "诚实的量化交易：写给新手的第一堂课"
AUTHOR = "metaquant 实验室"
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


@dataclass(frozen=True)
class Section:
    slug: str
    title: str
    markdown: str
    body_html: str


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
        rendered = markdown.markdown(
            body,
            extensions=MARKDOWN_EXTENSIONS,
            output_format="xhtml",
        )
        sections.append(Section(slug, title, body, rendered))
    return sections


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    path = Path("C:/Windows/Fonts") / name
    if not path.exists():
        raise FileNotFoundError(path)
    return ImageFont.truetype(str(path), size)


def build_cover(path: Path) -> None:
    width, height = 1600, 2400
    image = Image.new("RGB", (width, height), "#0d141c")
    draw = ImageDraw.Draw(image)

    for y in range(height):
        t = y / height
        draw.line((0, y, width, y), fill=(13 + int(8 * t), 20 + int(10 * t), 28 + int(14 * t)))

    brass, teal, paper = "#c99b4a", "#609c98", "#eee8d8"
    draw.rectangle((72, 72, width - 72, height - 72), outline="#765f38", width=3)
    draw.rectangle((91, 91, width - 91, height - 91), outline="#3f433e", width=2)
    draw.text((width / 2, 315), "量 化 交 易 入 门", font=font("NotoSansSC-VF.ttf", 42), fill=teal, anchor="mm")
    draw.text((width / 2, 690), "诚实的", font=font("NotoSerifSC-VF.ttf", 198), fill=paper, anchor="mm")
    draw.text((width / 2, 925), "量化交易", font=font("NotoSerifSC-VF.ttf", 198), fill=paper, anchor="mm")
    draw.line((555, 1070, 1045, 1070), fill=brass, width=4)
    draw.text((width / 2, 1165), "写给新手的第一堂课", font=font("NotoSansSC-VF.ttf", 62), fill=brass, anchor="mm")

    points = []
    for index in range(21):
        x = 180 + index * 62
        y = 1770 - index * 19 + (18 if index % 3 == 0 else -12 if index % 3 == 1 else 4)
        points.append((x, y))
    draw.line(points, fill=brass, width=7, joint="curve")
    for x, y in points[::4]:
        draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill=brass)

    draw.text((width / 2, 2100), "悲观者的工具，乐观者的心", font=font("NotoSerifSC-VF.ttf", 52), fill="#c8ccc7", anchor="mm")
    draw.text((width / 2, 2220), AUTHOR, font=font("NotoSansSC-VF.ttf", 38), fill="#7f8885", anchor="mm")
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, optimize=True)


EPUB_CSS = """@charset "utf-8";
html{font-size:100%;}
body{font-family:"Noto Serif SC","Source Han Serif SC","Songti SC",serif;line-height:1.85;color:#20272b;margin:5% 6%;}
h1,h2,h3{font-family:"Noto Sans SC","Source Han Sans SC","PingFang SC",sans-serif;color:#172229;page-break-after:avoid;}
h1{font-size:1.72em;line-height:1.35;margin:.2em 0 .9em;}
h2{font-size:1.24em;margin:1.9em 0 .6em;border-bottom:1px solid #ccd3cf;padding-bottom:.22em;}
h3{font-size:1.06em;margin:1.4em 0 .4em;color:#315f5b;}
p{margin:0 0 1em;text-align:justify;} a{color:#315f5b;text-decoration:none;} strong{font-weight:700;}
ul,ol{margin:0 0 1em;padding-left:1.4em;} li{margin:.35em 0;} hr{border:0;border-top:1px solid #d5d7d3;margin:2em 0;}
blockquote{margin:1.4em 0;padding:.2em 1em;border-left:3px solid #8da5a1;background:#f3f5f3;color:#39423e;}
code{font-family:monospace;background:#f1f1ed;padding:.05em .25em;} pre{white-space:pre-wrap;overflow-wrap:anywhere;}
table{border-collapse:collapse;width:100%;margin:1.4em 0;font-size:.9em;} th,td{border:1px solid #c9cecb;padding:.4em .55em;} th{background:#eef2ef;}
.cover{margin:0;padding:0;text-align:center;} .cover img{display:block;width:100%;height:auto;margin:0 auto;}
.nav ol{list-style:none;padding:0;} .nav li{padding:.35em 0;border-bottom:1px dotted #d2d5d2;}
.footnote{font-size:.86em;color:#4e5652;} .footnote-backref{margin-left:.25em;}
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
    itemrefs = ['<itemref idref="cover" linear="yes"/>', '<itemref idref="nav" linear="no"/>']
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
            *items,
        ]
    )
    opf = f'''<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid" xml:lang="{LANG}">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:identifier id="bookid">{UID}</dc:identifier><dc:title>{TITLE}</dc:title><dc:creator>{AUTHOR}</dc:creator><dc:language>{LANG}</dc:language><dc:description>写给量化交易新手的第一堂课。教育与知识分享用途，不构成投资建议。</dc:description><meta property="dcterms:modified">{modified}</meta><meta name="cover" content="cover-image"/></metadata>
<manifest>{manifest}</manifest><spine toc="ncx">{''.join(itemrefs)}</spine></package>'''
    container = '''<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>'''
    cover = xhtml_page(
        "封面",
        '<section epub:type="cover"><img src="images/cover.png" alt="《诚实的量化交易》封面"/></section>',
        "cover",
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
        archive.write(cover_path, "OEBPS/images/cover.png")
        for filename, content in pages.items():
            archive.writestr(f"OEBPS/{filename}", content)


PRINT_CSS = """
*{box-sizing:border-box} html{font-size:10.5pt} body{margin:0;color:#20272b;font-family:"Noto Serif SC","Source Han Serif SC","Songti SC",serif;line-height:1.78}
h1,h2,h3{font-family:"Noto Sans SC","Source Han Sans SC","PingFang SC",sans-serif;page-break-after:avoid;color:#172229}
h1{font-size:24pt;line-height:1.25;margin:0 0 16mm} h2{font-size:15pt;margin:9mm 0 3mm;padding-bottom:1.5mm;border-bottom:.25mm solid #c9ceca} h3{font-size:12pt;margin:6mm 0 2mm;color:#315f5b}
p{margin:0 0 4.2mm;text-align:justify} strong{font-weight:700} a{color:inherit;text-decoration:none}
ul,ol{padding-left:1.4em;margin:0 0 4mm} li{margin:1.2mm 0} blockquote{margin:5mm 0;padding:2.5mm 4mm;border-left:1mm solid #8da5a1;background:#f3f5f3;color:#39423e;break-inside:avoid}
hr{border:0;border-top:.25mm solid #d1d4d1;margin:8mm 0} code{font-family:Consolas,monospace;background:#f0f0ec;padding:0 .7mm} pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:8.5pt}
table{border-collapse:collapse;width:100%;margin:5mm 0;font-size:8.7pt;break-inside:avoid} th,td{border:.25mm solid #c4cac6;padding:1.6mm 2mm} th{background:#eef2ef}
.toc{break-after:page}.toc h1{margin-bottom:5mm}.toc ol{list-style:none;padding:0;columns:2;column-gap:9mm;font-size:8.7pt;line-height:1.35}.toc li{break-inside:avoid;border-bottom:.25mm dotted #c8cdca;padding:.7mm 0}
.chapter{break-before:page}.chapter:first-of-type{break-before:auto}.chapter>.footnote{font-size:8.5pt;color:#555d59}
"""


def print_html(sections: list[Section]) -> str:
    toc = "".join(f'<li><a href="#{s.slug}">{html.escape(s.title)}</a></li>' for s in sections)
    chapters = "".join(
        f'<section class="chapter" id="{s.slug}"><h1>{html.escape(s.title)}</h1>{s.body_html}</section>'
        for s in sections
    )
    return f'''<!doctype html><html lang="{LANG}"><head><meta charset="utf-8"><title>{TITLE}</title><style>{PRINT_CSS}</style></head><body><nav class="toc"><h1>目录</h1><ol>{toc}</ol></nav>{chapters}</body></html>'''


def build_pdf(sections: list[Section], cover_path: Path, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    cover_data = base64.b64encode(cover_path.read_bytes()).decode("ascii")
    cover_html = f'''<!doctype html><html><head><style>@page{{size:A5;margin:0}}html,body{{margin:0;width:100%;height:100%;background:#0d141c}}img{{width:100%;height:100%;object-fit:cover;display:block}}</style></head><body><img src="data:image/png;base64,{cover_data}"></body></html>'''

    with tempfile.TemporaryDirectory(prefix="metaquant-pdf-") as temporary:
        temp = Path(temporary)
        cover_pdf, content_pdf = temp / "cover.pdf", temp / "content.pdf"
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(
                executable_path="C:/Program Files/Google/Chrome/Application/chrome.exe",
                headless=True,
            )
            page = browser.new_page()
            page.set_content(cover_html, wait_until="load")
            page.pdf(path=str(cover_pdf), format="A5", print_background=True, margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
            page.set_content(print_html(sections), wait_until="load")
            page.pdf(
                path=str(content_pdf),
                format="A5",
                print_background=True,
                display_header_footer=True,
                header_template="<span></span>",
                footer_template='<div style="font:8px Arial;color:#777;width:100%;text-align:center"><span class="pageNumber"></span></div>',
                margin={"top": "15mm", "right": "14mm", "bottom": "17mm", "left": "14mm"},
            )
            browser.close()

        writer = PdfWriter()
        writer.append(str(cover_pdf))
        writer.append(str(content_pdf))
        writer.add_metadata({"/Title": TITLE, "/Author": AUTHOR, "/Subject": "量化交易入门"})
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
        for name in names:
            if name.endswith((".xhtml", ".xml", ".opf", ".ncx")):
                ElementTree.fromstring(archive.read(name))


def validate_pdf(path: Path) -> None:
    reader = PdfReader(str(path))
    assert len(reader.pages) > 50
    text = re.sub(
        r"\s+",
        "",
        unicodedata.normalize("NFKC", "\n".join((page.extract_text() or "") for page in reader.pages)),
    )
    expected = ("前言：写在最前面", "附录B：新手上路检查清单与延伸阅读")
    assert all(unicodedata.normalize("NFKC", title) in text for title in expected)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--format", choices=("all", "epub", "pdf"), default="all")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    if args.check:
        validate_epub(EPUB_PATH, len(SLUGS))
        validate_pdf(PDF_PATH)
        print(f"EPUB OK: {EPUB_PATH}")
        print(f"PDF OK: {PDF_PATH}")
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
