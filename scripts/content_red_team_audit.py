#!/usr/bin/env python3
"""Generate a reproducible content/build red-team audit for both reading styles."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from pypdf import PdfReader

import build_ebooks

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "audit" / "content-audit.json"

SOURCES = {
    "zh_story": ROOT / "book.md",
    "zh_concise": ROOT / "versions" / "03-humanizer-zh-round2.md",
    "en_story": ROOT / "book.en.md",
    "en_concise": ROOT / "versions" / "03-humanizer-en-round2.md",
}

RISK_PHRASES = {
    "zh": (
        "你有可能损失部分、甚至全部的本金",
        "止损能约束你的决定，不能保证你的成交价",
        "熔断不保证能在任何市场里瞬间全平",
        "最小权限和分层隔离",
        "低相关不能替负期望",
    ),
    "en": (
        "you may lose some or even all of your principal",
        "a stop-loss can constrain your decision; it cannot guarantee your execution price",
        "a kill switch does not guarantee that every position can be closed instantly",
        "least privilege and layered isolation",
        "low correlation cannot make negative expectancy acceptable",
    ),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def split_h1(source: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"(?m)^# (.+)$", source))
    return [
        (
            match.group(1).strip(),
            source[match.end() : matches[index + 1].start() if index + 1 < len(matches) else len(source)].strip(),
        )
        for index, match in enumerate(matches)
    ]


def signature(source: str) -> dict[str, object]:
    definitions = re.findall(r"(?m)^\[\^([^\]]+)\]:", source)
    references = re.findall(r"\[\^([^\]]+)\]", source)
    return {
        "h1": len(re.findall(r"(?m)^# ", source)),
        "h2": len(re.findall(r"(?m)^## ", source)),
        "h3": len(re.findall(r"(?m)^### ", source)),
        "footnoteDefinitions": definitions,
        "footnoteReferences": dict(sorted(Counter(references).items())),
        "callouts": {marker: source.count(marker) for marker in ("⚠️", "🔬", "📌", "✍️")},
        "tables": len(re.findall(r"(?m)^\s*\|?\s*:?-{3,}", source)),
        "tasks": len(re.findall(r"(?m)^\s*- \[[ xX]\]", source)),
        "unordered": len(re.findall(r"(?m)^\s*- (?!\[)", source)),
        "ordered": len(re.findall(r"(?m)^\s*\d+\. ", source)),
    }


def paragraph_blocks(body: str) -> list[str]:
    blocks = [re.sub(r"\s+", " ", block).strip() for block in re.split(r"\n\s*\n", body)]
    return [block for block in blocks if block and not block.startswith(("#", "<table", "</table"))]


def source_metrics(path: Path) -> dict[str, object]:
    source = path.read_text(encoding="utf-8")
    sections = split_h1(source)
    adjacent_duplicates: list[dict[str, object]] = []
    for title, body in sections:
        blocks = paragraph_blocks(body)
        for index in range(1, len(blocks)):
            if blocks[index] == blocks[index - 1]:
                adjacent_duplicates.append({"section": title, "block": index, "text": blocks[index][:160]})
    return {
        "path": str(path.relative_to(ROOT)),
        "sha256": sha256(path),
        "bytes": path.stat().st_size,
        "characters": len(source),
        "lines": source.count("\n") + 1,
        "signature": signature(source),
        "adjacentDuplicateParagraphs": adjacent_duplicates,
    }


def pair_metrics(full_path: Path, concise_path: Path) -> dict[str, object]:
    full = full_path.read_text(encoding="utf-8")
    concise = concise_path.read_text(encoding="utf-8")
    full_sections = split_h1(full)
    concise_sections = split_h1(concise)
    assert [title for title, _ in full_sections] == [title for title, _ in concise_sections]
    sections: list[dict[str, object]] = []
    for (title, full_body), (_, concise_body) in zip(full_sections, concise_sections):
        full_chars = len(full_body)
        concise_chars = len(concise_body)
        sections.append(
            {
                "title": title,
                "fullCharacters": full_chars,
                "conciseCharacters": concise_chars,
                "ratio": round(concise_chars / full_chars, 4) if full_chars else 1.0,
                "changed": full_body != concise_body,
                "fullParagraphBlocks": len(paragraph_blocks(full_body)),
                "conciseParagraphBlocks": len(paragraph_blocks(concise_body)),
            }
        )
    return {
        "full": str(full_path.relative_to(ROOT)),
        "concise": str(concise_path.relative_to(ROOT)),
        "overallCharacterRatio": round(len(concise) / len(full), 4),
        "signatureEqual": signature(full) == signature(concise),
        "headingsEqual": [x[0] for x in full_sections] == [x[0] for x in concise_sections],
        "sections": sections,
    }


def audit_pdf(path: Path) -> dict[str, object]:
    reader = PdfReader(str(path))
    raw = "\n".join((page.extract_text() or "") for page in reader.pages)
    radical_ranges = (("\u2e80", "\u2eff"), ("\u2f00", "\u2fdf"), ("\u31c0", "\u31ef"))
    radicals = sorted({char for char in raw if any(start <= char <= end for start, end in radical_ranges)})
    return {
        "path": str(path),
        "sha256": sha256(path),
        "bytes": path.stat().st_size,
        "pages": len(reader.pages),
        "extractedCharacters": len(raw),
        "cjkCharacters": sum("\u3400" <= char <= "\u9fff" for char in raw),
        "radicalOrStrokeCharacters": radicals,
        "replacementCharacters": raw.count("\ufffd"),
        "outlinePresent": bool(reader.outline),
        "lang": str(reader.trailer["/Root"].get("/Lang")),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf-smoke", type=Path)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()

    texts = {key: path.read_text(encoding="utf-8") for key, path in SOURCES.items()}
    sources = {key: source_metrics(path) for key, path in SOURCES.items()}
    pairs = {
        "zh": pair_metrics(SOURCES["zh_story"], SOURCES["zh_concise"]),
        "en": pair_metrics(SOURCES["en_story"], SOURCES["en_concise"]),
    }

    checks = {
        "zhStructurePreserved": pairs["zh"]["signatureEqual"] and pairs["zh"]["headingsEqual"],
        "enStructurePreserved": pairs["en"]["signatureEqual"] and pairs["en"]["headingsEqual"],
        "crossLanguageSignatureParityStory": signature(texts["zh_story"]) == signature(texts["en_story"]),
        "crossLanguageSignatureParityConcise": signature(texts["zh_concise"]) == signature(texts["en_concise"]),
        "noCjkInEnglishConcise": not bool(re.search(r"[\u3400-\u9fff]", texts["en_concise"])),
        "noUnfinishedMarkers": not any(
            token in texts["zh_concise"].lower() + texts["en_concise"].lower()
            for token in ("todo", "tbd", "placeholder", "@@ ")
        ),
        "noFormulaicImagine": "想象" not in texts["zh_concise"] and "imagine" not in texts["en_concise"].lower(),
        "noAdjacentDuplicateParagraphs": all(
            not metrics["adjacentDuplicateParagraphs"] for metrics in sources.values()
        ),
        "riskBoundariesZh": all(phrase in texts["zh_concise"] for phrase in RISK_PHRASES["zh"]),
        "riskBoundariesEn": all(phrase in texts["en_concise"].lower() for phrase in RISK_PHRASES["en"]),
    }

    browser_path = ROOT / "audit" / "browser-reader-audit.json"
    browser = json.loads(browser_path.read_text(encoding="utf-8"))
    checks["browserAuditPassed"] = browser.get("passed") is True and not browser.get("errors")

    # Reuse the executable validators rather than duplicating their contracts.
    build_ebooks.validate_epub(build_ebooks.EPUB_PATH, len(build_ebooks.SLUGS))
    build_ebooks.validate_pdf(build_ebooks.PDF_PATH)
    build_ebooks.validate_bilingual_reader()
    checks["existingEbookAndReaderValidationPassed"] = True

    pdf_smoke = None
    if args.pdf_smoke:
        build_ebooks.validate_pdf(args.pdf_smoke)
        pdf_smoke = audit_pdf(args.pdf_smoke)
        checks["pdfSmokeTextIntegrity"] = (
            not pdf_smoke["radicalOrStrokeCharacters"]
            and pdf_smoke["replacementCharacters"] == 0
            and pdf_smoke["outlinePresent"]
            and pdf_smoke["lang"] == build_ebooks.LANG
        )

    failures = [name for name, passed in checks.items() if not passed]
    report = {
        "generatedAt": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "passed": not failures,
        "failures": failures,
        "checks": checks,
        "sources": sources,
        "editionPairs": pairs,
        "browserAudit": {
            "path": str(browser_path.relative_to(ROOT)),
            "generatedAt": browser.get("generatedAt"),
            "passed": browser.get("passed"),
            "errors": browser.get("errors"),
            "crossLanguage": browser.get("crossLanguage"),
            "mobile": {
                lang: browser["readers"][lang]["mobile"] for lang in ("zh", "en")
            },
        },
        "pdfSmoke": pdf_smoke,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if failures:
        raise AssertionError(f"content red-team audit failed: {failures}")
    print(f"content red-team audit: passed ({args.output})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
