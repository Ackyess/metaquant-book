#!/usr/bin/env python3
"""End-to-end regression audit for both bilingual reading-style selectors."""

from __future__ import annotations

import argparse
import functools
import http.server
import json
import os
import shutil
import threading
import time
from pathlib import Path
from typing import Any

from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright


ROOT = Path(__file__).resolve().parents[1]
AUDIT_DIR = ROOT / "audit"
SCREENSHOT_DIR = AUDIT_DIR / "screenshots"
KEY_SLUGS = (
    "01-what-is-quant",
    "04-market-microstructure",
    "07-backtesting",
    "11-risk-management",
)


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args: object) -> None:
        return


def find_chromium() -> str | None:
    configured = os.environ.get("METAQUANT_CHROMIUM")
    candidates = [
        configured,
        shutil.which("chromium"),
        shutil.which("chromium-browser"),
        shutil.which("google-chrome"),
        shutil.which("google-chrome-stable"),
        "C:/Program Files/Google/Chrome/Application/chrome.exe",
    ]
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            return str(candidate)
    return None


def start_server() -> tuple[http.server.ThreadingHTTPServer, str]:
    handler = functools.partial(QuietHandler, directory=str(ROOT))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    host, port = server.server_address
    return server, f"http://{host}:{port}"


def attach_error_capture(page: Page, errors: list[dict[str, str]], scope: str) -> None:
    def on_console(message: Any) -> None:
        if message.type == "error":
            errors.append({"scope": scope, "kind": "console", "message": message.text})

    def on_page_error(error: Exception) -> None:
        errors.append({"scope": scope, "kind": "pageerror", "message": str(error)})

    page.on("console", on_console)
    page.on("pageerror", on_page_error)


def active_id(page: Page) -> str:
    return page.locator("section.screen.active").get_attribute("id") or ""


def wait_active(page: Page, slug: str) -> None:
    page.wait_for_function(
        "expected => document.querySelector('section.screen.active')?.id === expected",
        arg=slug,
    )


def active_content_font_size(page: Page) -> float:
    return page.locator("section.screen.active .content").evaluate(
        "el => parseFloat(getComputedStyle(el).fontSize)"
    )


def assert_topbar_offscreen(page: Page) -> None:
    assert page.locator(".topbar").evaluate(
        """bar => Math.max(
            bar.getBoundingClientRect().bottom,
            ...Array.from(bar.children, child => child.getBoundingClientRect().bottom)
        ) <= 0"""
    )


def choose(page: Page, style: str) -> None:
    page.locator(f'button[data-reading-style="{style}"]').click()
    page.wait_for_function("document.getElementById('styleDialog').hidden === true")
    assert page.evaluate("localStorage.getItem('mq-reading-style-v1')") == style


def open_selector(page: Page) -> None:
    viewport = page.viewport_size
    if viewport and viewport["width"] > 820:
        page.mouse.move(8, 2)
        page.wait_for_function(
            "document.querySelector('.topbar').getBoundingClientRect().bottom >= 54"
        )
    page.locator("#styleBtn").click()
    page.wait_for_function("document.getElementById('styleDialog').hidden === false")
    assert page.evaluate("document.getElementById('reader').inert") is True
    page.wait_for_function(
        "document.querySelector('button[data-reading-style=\"story\"]') === document.activeElement"
    )
    assert page.locator('button[data-reading-style="story"]').evaluate("el => el === document.activeElement")
    page.keyboard.press("Shift+Tab")
    assert page.locator('button[data-reading-style="concise"]').evaluate("el => el === document.activeElement")
    page.keyboard.press("Tab")
    assert page.locator('button[data-reading-style="story"]').evaluate("el => el === document.activeElement")


def chapter_texts(page: Page) -> dict[str, str]:
    return {slug: page.locator(f'section[id="{slug}"] .content').inner_html() for slug in KEY_SLUGS}


def assert_dialog_within_viewport(page: Page) -> dict[str, float]:
    # Measure the settled sheet, not its entrance transform.
    page.wait_for_timeout(380)
    box = page.locator(".style-sheet").bounding_box()
    assert box is not None
    viewport = page.viewport_size
    assert viewport is not None
    tolerance = 1.5
    assert box["x"] >= -tolerance and box["y"] >= -tolerance
    assert box["x"] + box["width"] <= viewport["width"] + tolerance
    assert box["y"] + box["height"] <= viewport["height"] + tolerance
    metrics = page.locator(".style-sheet").evaluate(
        "el => ({clientHeight:el.clientHeight,scrollHeight:el.scrollHeight,clientWidth:el.clientWidth,scrollWidth:el.scrollWidth})"
    )
    assert metrics["scrollWidth"] <= metrics["clientWidth"] + 1
    return {**box, **metrics}


def reader_smoke(
    browser: Browser,
    base: str,
    path: str,
    language: str,
    errors: list[dict[str, str]],
) -> dict[str, Any]:
    context = browser.new_context(viewport={"width": 1280, "height": 900})
    page = context.new_page()
    attach_error_capture(page, errors, f"{language}-desktop")
    page.goto(base + path, wait_until="networkidle")
    assert active_id(page) == "cover"
    assert not page.locator("#styleDialog").is_visible()

    page.locator("#coverCta").click()
    wait_active(page, "00-preface")
    assert not page.locator("#styleDialog").is_visible()
    page.locator("#nextBtn").click()
    assert page.locator("#styleDialog").is_visible()
    assert page.evaluate("document.getElementById('reader').inert") is True
    desktop_box = assert_dialog_within_viewport(page)
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    page.screenshot(path=str(SCREENSHOT_DIR / f"{language}-selector-desktop.png"), full_page=True)

    choose(page, "story")
    wait_active(page, "01-what-is-quant")
    assert page.locator("#styleBtn").is_visible()
    page.locator("#main").evaluate("el => { el.scrollTop = 180; }")
    page.wait_for_function("document.getElementById('reader').classList.contains('topbar-hidden')")
    page.wait_for_timeout(220)
    assert_topbar_offscreen(page)
    page.mouse.move(8, 2)
    page.wait_for_function("!document.getElementById('reader').classList.contains('topbar-hidden')")
    font_button = page.locator("#fontBtn")
    normal_font = active_content_font_size(page)
    assert font_button.inner_text().strip() == "A"
    font_button.click()
    large_font = active_content_font_size(page)
    assert font_button.inner_text().strip() == "A+" and large_font > normal_font
    font_button.click()
    small_font = active_content_font_size(page)
    assert font_button.inner_text().strip() == "A−" and small_font < normal_font
    font_button.click()
    assert font_button.inner_text().strip() == "A"
    assert active_content_font_size(page) == normal_font
    story = chapter_texts(page)

    open_selector(page)
    choose(page, "concise")
    concise = chapter_texts(page)
    differences = {slug: story[slug] != concise[slug] for slug in KEY_SLUGS}
    assert all(differences.values()), differences

    # Persistence after refresh at a deep chapter.
    page.evaluate("location.hash='#11-risk-management'")
    wait_active(page, "11-risk-management")
    concise_risk = page.locator('section[id="11-risk-management"] .content').inner_text()
    page.reload(wait_until="networkidle")
    wait_active(page, "11-risk-management")
    assert not page.locator("#styleDialog").is_visible()
    assert page.evaluate("localStorage.getItem('mq-reading-style-v1')") == "concise"
    assert page.locator('section[id="11-risk-management"] .content').inner_text() == concise_risk

    # Swapped footnotes remain interactive and do not survive as stale nodes.
    page.evaluate("location.hash='#02-almost-efficient-markets'")
    wait_active(page, "02-almost-efficient-markets")
    footnote = page.locator('section[id="02-almost-efficient-markets"] .footnote-ref').first
    assert footnote.count() == 1
    footnote.scroll_into_view_if_needed()
    page.wait_for_timeout(180)
    footnote.dispatch_event("click")
    page.locator("#footnoteCard").wait_for(state="visible")
    assert len(page.locator("#footnoteText").inner_text().strip()) > 20
    open_selector(page)
    choose(page, "story")
    assert not page.locator("#footnoteCard").is_visible()

    # Story can be restored, and keyboard navigation uses the same guard/path.
    assert chapter_texts(page) == story
    page.evaluate("location.hash='#01-what-is-quant'")
    wait_active(page, "01-what-is-quant")
    page.keyboard.press("ArrowRight")
    wait_active(page, "02-almost-efficient-markets")
    page.keyboard.press("ArrowLeft")
    wait_active(page, "01-what-is-quant")

    # TOC navigation remains functional.
    page.locator('[data-target="07-backtesting"]').click()
    wait_active(page, "07-backtesting")

    result = {
        "desktopDialog": desktop_box,
        "hoverRevealsTopbar": True,
        "fontSizes": {"small": small_font, "normal": normal_font, "large": large_font},
        "keyChapterDifferences": differences,
        "persistence": True,
        "reselection": True,
        "footnoteAfterSwap": True,
        "keyboardNavigation": True,
        "tocNavigation": True,
    }
    context.close()
    return result


def deep_link_guard(
    browser: Browser,
    base: str,
    path: str,
    language: str,
    errors: list[dict[str, str]],
) -> dict[str, Any]:
    context = browser.new_context(viewport={"width": 1180, "height": 820})
    page = context.new_page()
    attach_error_capture(page, errors, f"{language}-deeplink")
    page.goto(base + path + "#04-market-microstructure", wait_until="networkidle")
    assert page.locator("#styleDialog").is_visible()
    assert active_id(page) == "cover"
    page.keyboard.press("ArrowRight")
    assert active_id(page) == "cover"
    choose(page, "concise")
    wait_active(page, "04-market-microstructure")
    assert page.evaluate("location.hash") == "#04-market-microstructure"
    context.close()

    # Preface is intentionally readable before a style is selected.
    context = browser.new_context(viewport={"width": 1180, "height": 820})
    page = context.new_page()
    attach_error_capture(page, errors, f"{language}-preface-link")
    page.goto(base + path + "#00-preface", wait_until="networkidle")
    wait_active(page, "00-preface")
    assert not page.locator("#styleDialog").is_visible()
    context.close()
    return {"postPrefaceBlocked": True, "prefaceAllowed": True}


def mobile_audit(
    browser: Browser,
    base: str,
    path: str,
    language: str,
    errors: list[dict[str, str]],
) -> dict[str, Any]:
    context = browser.new_context(viewport={"width": 390, "height": 844}, is_mobile=True)
    page = context.new_page()
    attach_error_capture(page, errors, f"{language}-mobile")
    page.goto(base + path + "#04-market-microstructure", wait_until="networkidle")
    assert page.locator("#styleDialog").is_visible()
    mobile_box = assert_dialog_within_viewport(page)
    page.screenshot(path=str(SCREENSHOT_DIR / f"{language}-selector-mobile.png"), full_page=True)
    sheet_metrics = page.locator(".style-sheet").evaluate(
        "el => ({clientHeight:el.clientHeight,scrollHeight:el.scrollHeight})"
    )
    last_choice = page.locator(".style-option").last
    last_choice.scroll_into_view_if_needed()
    last_choice.wait_for(state="visible")
    last_choice_box = last_choice.bounding_box()
    assert last_choice_box is not None and last_choice_box["y"] + last_choice_box["height"] <= 844 + 1.5
    choose(page, "concise")
    wait_active(page, "04-market-microstructure")
    overflow = page.evaluate(
        "({doc:document.documentElement.scrollWidth-innerWidth, body:document.body.scrollWidth-innerWidth})"
    )
    assert overflow["doc"] <= 1 and overflow["body"] <= 1, overflow
    page.locator("#main").evaluate("el => { el.scrollTop = 180; }")
    page.wait_for_function("document.getElementById('reader').classList.contains('topbar-hidden')")
    page.wait_for_timeout(220)
    assert_topbar_offscreen(page)
    page.locator("#main").evaluate("el => { el.scrollTop = 110; }")
    page.wait_for_function("!document.getElementById('reader').classList.contains('topbar-hidden')")
    assert page.locator("#toolsBtn").is_visible()
    assert not page.locator("#topbarTools").is_visible()
    page.locator("#toolsBtn").click()
    page.locator("#topbarTools").wait_for(state="visible")
    assert page.locator("#toolsBtn").get_attribute("aria-expanded") == "true"
    topbar_controls = page.evaluate(
        """Object.fromEntries(
            ['styleBtn','fontBtn','langBtn','themeBtn'].map(id => {
                const rect = document.getElementById(id).getBoundingClientRect();
                return [id, {left: rect.left, right: rect.right, width: rect.width}];
            })
        )"""
    )
    assert all(item["left"] >= -1 and item["right"] <= 391 for item in topbar_controls.values())
    page.keyboard.press("Escape")
    page.locator("#topbarTools").wait_for(state="hidden")
    assert page.locator("#toolsBtn").get_attribute("aria-expanded") == "false"

    page.locator("#menuBtn").click()
    assert page.locator("#sidebar").get_attribute("aria-hidden") == "false"
    page.locator('[data-target="07-backtesting"]').click()
    wait_active(page, "07-backtesting")
    assert page.locator("#sidebar").get_attribute("aria-hidden") == "true"
    context.close()
    return {
        "dialog": mobile_box,
        "internalScroll": sheet_metrics["scrollHeight"] > sheet_metrics["clientHeight"] + 1,
        "footerReachable": True,
        "horizontalOverflow": overflow,
        "autoHideTopbar": True,
        "topbarControls": topbar_controls,
        "mobileToc": True,
    }


def cross_language_memory(browser: Browser, base: str, errors: list[dict[str, str]]) -> dict[str, Any]:
    context = browser.new_context(viewport={"width": 1180, "height": 820})
    page = context.new_page()
    attach_error_capture(page, errors, "cross-language")
    page.goto(base + "/#04-market-microstructure", wait_until="networkidle")
    choose(page, "concise")
    wait_active(page, "04-market-microstructure")
    page.locator("#fontBtn").click()
    assert page.locator("#fontBtn").inner_text().strip() == "A+"
    assert page.evaluate("localStorage.getItem('mq-font-size-v1')") == "large"
    page.locator("#langBtn").click()
    page.wait_for_url("**/en/**")
    wait_active(page, "04-market-microstructure")
    assert not page.locator("#styleDialog").is_visible()
    assert page.evaluate("localStorage.getItem('mq-reading-style-v1')") == "concise"
    page.wait_for_function("document.getElementById('styleBtn').textContent.trim() === 'C'")
    assert page.locator("#styleBtn").inner_text().strip() == "C"
    assert page.locator("#fontBtn").inner_text().strip() == "A+"

    open_selector(page)
    choose(page, "story")
    page.locator("#langBtn").click()
    page.wait_for_url(lambda url: "/en/" not in url)
    wait_active(page, "04-market-microstructure")
    assert page.evaluate("localStorage.getItem('mq-reading-style-v1')") == "story"
    page.wait_for_function("document.getElementById('styleBtn').textContent.trim() === '叙'")
    assert page.locator("#styleBtn").inner_text().strip() == "叙"
    assert page.locator("#fontBtn").inner_text().strip() == "A+"
    context.close()
    return {"conciseZhToEn": True, "storyEnToZh": True, "fontSizePreserved": True}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=AUDIT_DIR / "browser-reader-audit.json")
    args = parser.parse_args()
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

    server, base = start_server()
    errors: list[dict[str, str]] = []
    report: dict[str, Any] = {
        "generatedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "baseUrl": base,
        "viewportDesktop": {"width": 1280, "height": 900},
        "viewportMobile": {"width": 390, "height": 844},
        "readers": {},
    }
    try:
        executable = find_chromium()
        with sync_playwright() as playwright:
            launch_args: dict[str, Any] = {"headless": True}
            if executable:
                launch_args["executable_path"] = executable
            browser = playwright.chromium.launch(**launch_args)
            try:
                for language, path in (("zh", "/"), ("en", "/en/")):
                    report["readers"][language] = {
                        "smoke": reader_smoke(browser, base, path, language, errors),
                        "deepLinks": deep_link_guard(browser, base, path, language, errors),
                        "mobile": mobile_audit(browser, base, path, language, errors),
                    }
                report["crossLanguage"] = cross_language_memory(browser, base, errors)
            finally:
                browser.close()
    finally:
        server.shutdown()
        server.server_close()

    report["errors"] = errors
    report["passed"] = not errors
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if errors:
        raise AssertionError(f"Browser console/page errors: {errors}")
    print(f"browser audit: passed ({args.output})")


if __name__ == "__main__":
    main()
