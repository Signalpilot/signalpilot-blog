#!/usr/bin/env python3
"""
Script to reorder articles on Signal Pilot blog according to logical learning path.
Updates: homepages (all languages) and article navigation (prev/next links).
"""

import os
import re
from pathlib import Path

# The logical learning order (54 articles)
ARTICLE_ORDER = [
    # Phase 1: Getting Started (5)
    "what-is-a-trading-edge",
    "how-long-to-become-profitable",
    "crypto-vs-forex-vs-stocks",
    "best-times-to-trade",
    "tradingview-setup-guide",

    # Phase 2: Reading Charts (6)
    "candlestick-basics",
    "support-and-resistance-explained",
    "how-to-identify-a-trend",
    "chart-patterns-that-work",
    "moving-averages-explained",
    "timeframe-selection",

    # Phase 3: Understanding Cycles (7)
    "why-markets-move-in-cycles",
    "the-only-pattern-that-repeats",
    "cycles-within-cycles",
    "identifying-cycle-length",
    "cycle-failures-and-what-they-mean",
    "accumulation-vs-distribution",
    "how-smart-money-moves",

    # Phase 4: Indicators (7)
    "why-your-indicators-keep-failing",
    "volume-profile-basics",
    "multi-timeframe-confirmation",
    "when-to-ignore-divergence",
    "the-confirmation-trap",
    "the-repainting-problem",
    "tradingview-free-scripts",

    # Phase 5: Risk Management (10)
    "position-sizing-101",
    "the-1-percent-rule",
    "risk-reward-ratio",
    "stop-loss-placement",
    "3-questions-before-every-trade",
    "building-a-pre-trade-checklist",
    "drawdown-management",
    "when-to-cut-losses-early",
    "when-to-size-up",
    "trading-around-news",

    # Phase 6: Psychology (8)
    "why-traders-blow-first-account",
    "why-you-break-trading-rules",
    "psychology-of-getting-stopped-out",
    "trading-while-emotional",
    "the-boredom-trap",
    "revenge-trading-recovery",
    "rules-based-vs-discretionary",
    "what-profitable-traders-know",

    # Phase 7: Building Systems (6)
    "building-your-first-system",
    "trade-journaling-that-works",
    "trading-journal",
    "backtesting-without-fooling-yourself",
    "why-backtesting-results-are-worthless",
    "system-optimization",

    # Phase 8: Signal Pilot Product (3)
    "free-indicators-vs-professional-tools",
    "inside-signal-pilot",
    "how-to-trade-cycles-with-pentarch",

    # Phase 9: Execute! (2)
    "order-types-explained",
    "your-first-trade",
]

# Article titles for each language (English only for now, will extract from files)
ARTICLE_TITLES = {}

BASE_DIR = Path("/home/user/signalpilot-blog")
ARTICLES_DIR = BASE_DIR / "articles"
LANGUAGES = ["en", "ar", "de", "es", "fr", "hu", "it", "ja", "nl", "pt", "ru", "tr"]

def get_article_title(slug, lang="en"):
    """Extract article title from the HTML file."""
    if lang == "en":
        filepath = ARTICLES_DIR / slug / "index.html"
    else:
        filepath = ARTICLES_DIR / slug / lang / "index.html"

    if not filepath.exists():
        return slug.replace("-", " ").title()

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract title from <title> tag
    match = re.search(r'<title>([^<]+) - Signal Pilot Blog</title>', content)
    if match:
        return match.group(1)

    # Fallback: extract from h1
    match = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
    if match:
        return match.group(1)

    return slug.replace("-", " ").title()

def get_nav_label(lang, direction):
    """Get the navigation label for a given language."""
    labels = {
        "en": {"prev": "Previous", "next": "Next"},
        "ar": {"prev": "السابق", "next": "التالي"},
        "de": {"prev": "Zurück", "next": "Weiter"},
        "es": {"prev": "Anterior", "next": "Siguiente"},
        "fr": {"prev": "Précédent", "next": "Suivant"},
        "hu": {"prev": "Előző", "next": "Következő"},
        "it": {"prev": "Precedente", "next": "Successivo"},
        "ja": {"prev": "前の記事", "next": "次の記事"},
        "nl": {"prev": "Vorige", "next": "Volgende"},
        "pt": {"prev": "Anterior", "next": "Próximo"},
        "ru": {"prev": "Предыдущая", "next": "Далее"},
        "tr": {"prev": "Önceki", "next": "Sonraki"},
    }
    return labels.get(lang, labels["en"])[direction]

def update_article_navigation(slug, lang="en"):
    """Update the prev/next navigation links in an article."""
    idx = ARTICLE_ORDER.index(slug)
    prev_slug = ARTICLE_ORDER[idx - 1] if idx > 0 else None
    next_slug = ARTICLE_ORDER[idx + 1] if idx < len(ARTICLE_ORDER) - 1 else None

    # Determine file path
    if lang == "en":
        filepath = ARTICLES_DIR / slug / "index.html"
        prev_href = f"../{prev_slug}/" if prev_slug else None
        next_href = f"../{next_slug}/" if next_slug else None
    else:
        filepath = ARTICLES_DIR / slug / lang / "index.html"
        prev_href = f"../../{prev_slug}/{lang}/" if prev_slug else None
        next_href = f"../../{next_slug}/{lang}/" if next_slug else None

    if not filepath.exists():
        print(f"  Skipping {filepath} - file not found")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Get titles
    prev_title = get_article_title(prev_slug, lang) if prev_slug else None
    next_title = get_article_title(next_slug, lang) if next_slug else None

    # Build new navigation HTML
    prev_svg = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>'
    next_svg = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>'

    prev_label = get_nav_label(lang, "prev")
    next_label = get_nav_label(lang, "next")

    if prev_slug:
        prev_html = f'''            <a href="{prev_href}" class="article-nav-link prev">
              <span class="article-nav-label">
                {prev_svg}
                {prev_label}
              </span>
              <span class="article-nav-title">{prev_title}</span>
            </a>'''
    else:
        prev_html = '            <div class="article-nav-link placeholder"></div>'

    if next_slug:
        next_html = f'''            <a href="{next_href}" class="article-nav-link next">
              <span class="article-nav-label">
                {next_label} {next_svg}
              </span>
              <span class="article-nav-title">{next_title}</span>
            </a>'''
    else:
        next_html = '            <div class="article-nav-link placeholder"></div>'

    new_nav = f'''          <nav class="article-nav">
{prev_html}
{next_html}
          </nav>'''

    # Replace existing nav
    pattern = r'<nav class="article-nav">.*?</nav>'
    new_content = re.sub(pattern, new_nav, content, flags=re.DOTALL)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    print(f"Article order has {len(ARTICLE_ORDER)} articles")
    print("\nUpdating article navigation links...")

    updated_count = 0
    for slug in ARTICLE_ORDER:
        print(f"\nProcessing: {slug}")

        # Update English version
        if update_article_navigation(slug, "en"):
            updated_count += 1
            print(f"  Updated: en")

        # Update language variants
        for lang in LANGUAGES[1:]:  # Skip 'en'
            if update_article_navigation(slug, lang):
                updated_count += 1
                print(f"  Updated: {lang}")

    print(f"\n\nTotal files updated: {updated_count}")

if __name__ == "__main__":
    main()
