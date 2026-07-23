#!/usr/bin/env python3
"""Small, deterministic Markdown renderer used by the build scripts.

The project previously depended on Python-Markdown without declaring it.  This
wrapper uses Mistune, which supports the table and footnote features used by
the book, and explicitly renders the project's callout containers.
"""

from __future__ import annotations

import re

import mistune


CALLOUT_RE = re.compile(
    r'<aside class="callout ([^"]+)" markdown="1">\s*(.*?)\s*</aside>',
    re.DOTALL,
)


def _renderer() -> mistune.Markdown:
    return mistune.create_markdown(
        escape=False,
        plugins=["table", "footnotes"],
    )


def _normalize_footnotes(rendered: str) -> str:
    # Keep the existing EPUB/PDF CSS contract used by the project without
    # rewriting unrelated raw <section> elements.
    rendered = re.sub(
        r'<section class="footnotes">\s*(.*?)\s*</section>',
        lambda match: '<div class="footnote">\n' + match.group(1) + '\n</div>',
        rendered,
        flags=re.DOTALL,
    )
    rendered = rendered.replace(
        ' class="footnote">&#8617;</a>',
        ' class="footnote-backref">&#8617;</a>',
    )
    return rendered


def markdown_to_html(source: str) -> str:
    """Render the subset of Markdown used in the book to HTML."""
    callouts: list[str] = []

    def reserve_callout(match: re.Match[str]) -> str:
        kind, body = match.group(1), match.group(2)
        inner = _normalize_footnotes(_renderer()(body)).strip()
        index = len(callouts)
        callouts.append(f'<aside class="callout {kind}">\n{inner}\n</aside>')
        return f'\n\n<!--METAQUANT-CALLOUT-{index}-->\n\n'

    reserved = CALLOUT_RE.sub(reserve_callout, source)
    rendered = _normalize_footnotes(_renderer()(reserved))
    for index, callout in enumerate(callouts):
        rendered = rendered.replace(f'<!--METAQUANT-CALLOUT-{index}-->', callout)
    return rendered
