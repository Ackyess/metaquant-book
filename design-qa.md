# Design QA

## Source Visual Truth

- Chinese cover artwork: `C:\Users\admin\Desktop\mojibake\assets\cover-ai-v2.png`
- English cover artwork: `C:\Users\admin\Desktop\mojibake\assets\cover-ai-v2-en.png`
- Source dimensions: 1024 × 1536 px for each image.
- The source truth governs the cover artwork. The surrounding reader shell, preface stage, navigation, and transitions are intentional product context rather than a page-for-page clone of the portrait cover.

## Browser-Rendered Evidence

- Chinese desktop preface: `C:\Users\admin\Desktop\mojibake\tmp\design-qa\zh-preface-book-desktop-1280x720.png`
- English desktop preface: `C:\Users\admin\Desktop\mojibake\tmp\design-qa\en-preface-book-desktop-1280x720.png`
- Chinese mobile cover: `C:\Users\admin\Desktop\mojibake\tmp\design-qa\zh-cover-mobile-390x844.png`
- English mobile cover: `C:\Users\admin\Desktop\mojibake\tmp\design-qa\en-cover-mobile-390x844.png`
- English mobile menu: `C:\Users\admin\Desktop\mojibake\tmp\design-qa\en-mobile-menu-open-390x844.png`
- Chinese opening transition: `C:\Users\admin\Desktop\mojibake\tmp\design-qa\zh-opening-transition-1280x720.png`
- Desktop CSS viewport and screenshot pixels: 1280 × 720 at 1× density.
- Mobile CSS viewport and screenshot pixels: 390 × 844 at 1× density.
- No density resampling was needed for the browser captures.

## Combined Comparison Evidence

- Chinese full comparison: `C:\Users\admin\Desktop\mojibake\tmp\design-qa\compare-zh-full.png`
- Chinese focused comparison: `C:\Users\admin\Desktop\mojibake\tmp\design-qa\compare-zh-focused.png`
- English full comparison: `C:\Users\admin\Desktop\mojibake\tmp\design-qa\compare-en-full.png`
- English focused comparison: `C:\Users\admin\Desktop\mojibake\tmp\design-qa\compare-en-focused.png`
- Full-view comparison checks the supplied portrait artwork inside the complete preface composition.
- Focused comparison normalizes the source and rendered cover to 270 × 405 px. Title hierarchy, subtitle, chart, navy field, brass linework, and signature remain faithful. The subtle corner radius and drop shadow are intentional presentation treatments.

## State

- Languages: `zh-CN` and `en`.
- Themes checked: light and dark.
- Routes checked: cover, preface, chapter 11, and hash-preserving language switch.
- Responsive states checked: desktop, mobile cover, mobile menu open, mobile menu closed.
- Motion checked: opening transition in-browser; reduced-motion bypass logic verified statically.

## Findings

- No actionable P0, P1, or P2 findings remain.
- Fonts and typography: the reader keeps its existing serif/sans/mono system; English navigation now uses concise scan labels while full chapter names remain available as accessible labels and desktop rail-card text.
- Spacing and layout rhythm: Chinese and English covers keep the editorial first-screen hierarchy. At 1280 × 720, both primary CTAs and downloads are visible. At 390 × 844, neither language has horizontal overflow.
- Colors and tokens: the supplied navy, cream, brass, and teal artwork is preserved. Muted UI text now reaches at least 4.5:1 against both light and dark paper tokens.
- Image quality and asset fidelity: both supplied 1024 × 1536 cover assets are used directly; no visible CSS drawing, emoji, placeholder, or inline SVG substitutes the artwork.
- Copy and content: Chinese callout labels are text-only; English download choices are separated into English text and Chinese editions.
- Icons and controls: existing menu, language, and theme controls remain aligned and keep visible focus states.
- Accessibility and behavior: hidden mobile navigation receives both `inert` and `aria-hidden`; opening it focuses the active/first chapter, Escape returns focus to the menu button, and the brand responds to Enter and Space.
- Console errors checked: none.

## Comparison History

### Iteration 1

- Earlier finding: [P2] the English primary CTA fell below the fold at the 1280 × 720 desktop viewport because the title and body rhythm consumed too much vertical space.
- Fix: widened the English cover composition, reduced the display-title ceiling, and tightened kicker, rule, subtitle, thesis line-height, and section gaps.
- Post-fix evidence: `C:\Users\admin\Desktop\mojibake\tmp\design-qa\en-cover-desktop-1280x720-v2.png`; CTA bottom measured at 646 px and download rows at 703 px within the 720 px viewport.

### Iteration 2

- Earlier finding: [P2] the preface object still showed legacy CSS-drawn page/spine details around the real artwork.
- Fix: removed the visible generated frame, page, and spine layers, leaving the supplied cover image with only spatial shadow and motion treatment.
- Post-fix evidence: the four combined comparison images above show the source artwork preserved without a substitute illustration.

## Primary Interactions Tested

- Open the first page in both languages.
- Preserve the current chapter while switching languages.
- Open the mobile contents sheet, move focus into it, close with Escape, and return focus.
- Activate the brand with the keyboard.
- Switch light and dark themes.
- Resolve English Markdown and Chinese EPUB/PDF download targets.

## Follow-up Polish

- [P3] On the English 1280 × 720 cover, the optional motto sits just below the fold while the CTA and downloads remain visible. This is acceptable because it preserves the reading hierarchy and does not affect conversion or navigation.

final result: passed
