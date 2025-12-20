#!/usr/bin/env python3
"""
Script to reorder article cards on the homepage according to logical learning path.
"""

import re
from pathlib import Path

# The logical learning order (54 articles)
ARTICLE_ORDER = [
    "what-is-a-trading-edge",
    "how-long-to-become-profitable",
    "crypto-vs-forex-vs-stocks",
    "best-times-to-trade",
    "tradingview-setup-guide",
    "candlestick-basics",
    "support-and-resistance-explained",
    "how-to-identify-a-trend",
    "chart-patterns-that-work",
    "moving-averages-explained",
    "timeframe-selection",
    "why-markets-move-in-cycles",
    "the-only-pattern-that-repeats",
    "cycles-within-cycles",
    "identifying-cycle-length",
    "cycle-failures-and-what-they-mean",
    "accumulation-vs-distribution",
    "how-smart-money-moves",
    "why-your-indicators-keep-failing",
    "volume-profile-basics",
    "multi-timeframe-confirmation",
    "when-to-ignore-divergence",
    "the-confirmation-trap",
    "the-repainting-problem",
    "tradingview-free-scripts",
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
    "why-traders-blow-first-account",
    "why-you-break-trading-rules",
    "psychology-of-getting-stopped-out",
    "trading-while-emotional",
    "the-boredom-trap",
    "revenge-trading-recovery",
    "rules-based-vs-discretionary",
    "what-profitable-traders-know",
    "building-your-first-system",
    "trade-journaling-that-works",
    "trading-journal",
    "backtesting-without-fooling-yourself",
    "why-backtesting-results-are-worthless",
    "system-optimization",
    "free-indicators-vs-professional-tools",
    "inside-signal-pilot",
    "how-to-trade-cycles-with-pentarch",
    "order-types-explained",
    "your-first-trade",
]

BASE_DIR = Path("/home/user/signalpilot-blog")

def extract_article_cards(content):
    """Extract all article cards from homepage HTML."""
    # Pattern to match article cards
    pattern = r'(<a href="articles/([^/]+)/"[^>]*class="article-card"[^>]*>.*?</a>)'
    matches = re.findall(pattern, content, re.DOTALL)

    cards = {}
    for full_match, slug in matches:
        cards[slug] = full_match

    return cards

def reorder_homepage(filepath, lang="en"):
    """Reorder article cards on a homepage."""
    print(f"Processing: {filepath}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the articles-grid section
    grid_pattern = r'(<div class="articles-grid">)(.*?)(</div>\s*</div>\s*</section>)'
    grid_match = re.search(grid_pattern, content, re.DOTALL)

    if not grid_match:
        print(f"  Could not find articles-grid in {filepath}")
        return False

    grid_start = grid_match.group(1)
    grid_content = grid_match.group(2)
    grid_end = grid_match.group(3)

    # Extract all article cards
    cards = extract_article_cards(grid_content)
    print(f"  Found {len(cards)} article cards")

    # Check for missing articles
    missing = [slug for slug in ARTICLE_ORDER if slug not in cards]
    if missing:
        print(f"  Warning: Missing articles: {missing[:5]}...")

    extra = [slug for slug in cards if slug not in ARTICLE_ORDER]
    if extra:
        print(f"  Warning: Extra articles not in order: {extra}")

    # Reorder cards
    ordered_cards = []
    for slug in ARTICLE_ORDER:
        if slug in cards:
            ordered_cards.append(cards[slug])

    # Join with proper formatting
    new_grid_content = "\n\n          ".join(ordered_cards)
    new_grid_content = "\n\n          " + new_grid_content + "\n\n        "

    # Replace the grid content
    new_content = content[:grid_match.start()] + grid_start + new_grid_content + grid_end + content[grid_match.end():]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"  Updated successfully!")
    return True

def main():
    # Update English homepage
    reorder_homepage(BASE_DIR / "index.html", "en")

    # Update language homepages
    languages = ["ar", "de", "es", "fr", "hu", "it", "ja", "nl", "pt", "ru", "tr"]
    for lang in languages:
        lang_homepage = BASE_DIR / lang / "index.html"
        if lang_homepage.exists():
            reorder_homepage(lang_homepage, lang)
        else:
            print(f"Skipping {lang} - file not found")

if __name__ == "__main__":
    main()
