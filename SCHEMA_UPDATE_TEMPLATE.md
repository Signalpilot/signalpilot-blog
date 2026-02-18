# Schema Update Template - Manual Implementation Guide

## Overview
This document provides the exact manual changes needed to implement TIER 1 schema enhancements for all 54 articles across 12 languages (648 files total).

**Changes Made So Far:**
- ✅ best-times-to-trade (EN + JA)
- ✅ inside-signal-pilot (EN)

**Remaining: 51 articles × 12 languages = 612 files**

---

## Category Mapping (Map Each Article to Its Category)

Based on the api/articles.json tags, here are all articles with their categories:

### Markets & Sessions
- best-times-to-trade ✅
- crypto-vs-forex-vs-stocks

### Technical Indicators
- why-your-indicators-keep-failing
- the-repainting-problem
- moving-averages-explained
- volume-profile-basics
- when-to-ignore-divergence
- free-indicators-vs-professional-tools
- tradingview-free-scripts

### Market Structure
- candlestick-basics
- support-and-resistance-explained
- how-to-identify-a-trend
- chart-patterns-that-work
- the-only-pattern-that-repeats

### Trading Psychology
- what-profitable-traders-know
- the-confirmation-trap
- trading-while-emotional
- why-you-break-trading-rules
- the-boredom-trap
- revenge-trading-recovery
- how-long-to-become-profitable
- rules-based-vs-discretionary
- trading-while-emotional

### Risk Management
- your-first-trade
- position-sizing-101
- risk-reward-ratio
- drawdown-management
- the-1-percent-rule
- when-to-cut-losses-early
- stop-loss-placement
- psychology-of-getting-stopped-out
- the-3-questions-before-every-trade
- when-to-size-up
- building-a-pre-trade-checklist

### Backtesting & Systems
- system-optimization
- trading-journal
- why-backtesting-results-are-worthless
- the-confirmation-trap
- building-your-first-system
- backtesting-without-fooling-yourself
- what-is-a-trading-edge

### Market Cycles
- why-markets-move-in-cycles
- how-smart-money-moves
- accumulation-vs-distribution
- identifying-cycle-length
- cycles-within-cycles
- cycle-failures-and-what-they-mean

### Signal Pilot Product ✅
- inside-signal-pilot
- how-to-trade-cycles-with-pentarch

### Practical Trading
- tradingview-setup-guide
- trading-around-news
- trade-journaling-that-works
- order-types-explained

---

## Three Changes Required for Each File

### CHANGE 1: Update BlogPosting Schema

**Location:** First `<script type="application/ld+json">` block with `"@type": "BlogPosting"`

**Add/Update these fields:**
- `"inLanguage": "en"` (or appropriate language code: es, de, fr, it, pt, nl, ru, ja, ar, tr, hu)
- `"articleSection": "[CATEGORY_NAME]"` (from mapping above)

**Example - BEFORE:**
```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Best Times to Trade: Sessions, Overlaps, and When to Stay Out",
  ...
  "inLanguage": "en"
}
```

**Example - AFTER:**
```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Best Times to Trade: Sessions, Overlaps, and When to Stay Out",
  ...
  "inLanguage": "en",
  "articleSection": "Markets & Sessions"
}
```

---

### CHANGE 2: Update BreadcrumbList Schema

**Location:** Second `<script type="application/ld+json">` block with `"@type": "BreadcrumbList"`

**Task:** Ensure 4-level breadcrumb with correct category URL

**Example - BEFORE:**
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
      {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://www.signalpilot.io"
      },
      {
          "@type": "ListItem",
          "position": 2,
          "name": "Blog",
          "item": "https://blog.signalpilot.io"
      },
      {
          "@type": "ListItem",
          "position": 3,
          "name": "Markets",
          "item": "https://blog.signalpilot.io"
      },
      {
          "@type": "ListItem",
          "position": 4,
          "name": "Best Times to Trade: Sessions, Overlaps, and When to Stay Out",
          "item": "https://blog.signalpilot.io/articles/best-times-to-trade/"
      }
  ]
}
```

**Example - AFTER:**
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
      {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://www.signalpilot.io"
      },
      {
          "@type": "ListItem",
          "position": 2,
          "name": "Blog",
          "item": "https://blog.signalpilot.io"
      },
      {
          "@type": "ListItem",
          "position": 3,
          "name": "Markets & Sessions",
          "item": "https://blog.signalpilot.io/categories/markets-sessions/"
      },
      {
          "@type": "ListItem",
          "position": 4,
          "name": "Best Times to Trade: Sessions, Overlaps, and When to Stay Out",
          "item": "https://blog.signalpilot.io/articles/best-times-to-trade/"
      }
  ]
}
```

**Key Points:**
- Position 3 name = Category name from mapping
- Position 3 item = `https://blog.signalpilot.io/categories/[slug-version-of-category]/`
  - Example: "Markets & Sessions" → "markets-sessions"
  - Example: "Signal Pilot Product" → "signal-pilot-product"
  - Example: "Technical Indicators" → "technical-indicators"

---

### CHANGE 3: Add NewsArticle Schema

**Location:** Insert AFTER the BreadcrumbList script and BEFORE the `<link rel="preconnect">` tags

**Template:**
```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "NewsArticle",
  "headline": "[EXACT ARTICLE TITLE FROM og:title]",
  "description": "[EXACT ARTICLE DESCRIPTION FROM og:description]",
  "image": "[EXACT IMAGE URL FROM og:image]",
  "datePublished": "[EXACT DATE FROM article:published_time]",
  "dateModified": "[EXACT DATE FROM article:published_time]",
  "author": {
    "@type": "Organization",
    "name": "Signal Pilot Team",
    "url": "https://www.signalpilot.io"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Signal Pilot",
    "url": "https://www.signalpilot.io",
    "logo": {
      "@type": "ImageObject",
      "url": "https://signalpilot.io/assets/og-image.png"
    }
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "[CANONICAL URL]"
  }
}
</script>
```

**Example for "best-times-to-trade":**
```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "NewsArticle",
  "headline": "Best Times to Trade: Sessions, Overlaps, and When to Stay Out",
  "description": "Not all trading hours are equal. Learn when each market is most active, which session overlaps create the best opportunities, and when staying out is the smartest move.",
  "image": "https://blog.signalpilot.io/articles/best-times-to-trade/hero.png",
  "datePublished": "2025-11-02",
  "dateModified": "2025-11-02",
  "author": {
    "@type": "Organization",
    "name": "Signal Pilot Team",
    "url": "https://www.signalpilot.io"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Signal Pilot",
    "url": "https://www.signalpilot.io",
    "logo": {
      "@type": "ImageObject",
      "url": "https://signalpilot.io/assets/og-image.png"
    }
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://blog.signalpilot.io/articles/best-times-to-trade/"
  }
}
</script>
```

---

## Language-Specific Notes

### English Articles (articles/[slug]/index.html)
- Use language code: `"en"`
- Breadcrumb item 3 name: Use English category name
- NewsArticle headline/description: English text

### Spanish (articles/[slug]/es/index.html)
- Use language code: `"es"`
- Breadcrumb item 3 name: Spanish category name (translate from English)
- NewsArticle headline/description: Spanish text from article file

### German (articles/[slug]/de/index.html)
- Use language code: `"de"`
- Similar pattern - translate category name, use German text

### And so on for: fr, it, pt, nl, ru, ja, ar, tr, hu

**Important:** Keep the category slug CONSISTENT across all languages (e.g., always `markets-sessions`, not translations)

---

## Complete Article List for Processing

### 1. 3-questions-before-every-trade
Category: Risk Management
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 2. accumulation-vs-distribution
Category: Market Cycles
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 3. backtesting-without-fooling-yourself
Category: Backtesting & Systems
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 4. best-times-to-trade ✅
Category: Markets & Sessions
Languages: en ✅, es, de, fr, it, pt, nl, ru, ja ✅, ar, tr, hu

### 5. building-a-pre-trade-checklist
Category: Risk Management
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 6. building-your-first-system
Category: Backtesting & Systems
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 7. candlestick-basics
Category: Market Structure
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 8. chart-patterns-that-work
Category: Market Structure
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 9. crypto-vs-forex-vs-stocks
Category: Markets & Sessions
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 10. cycle-failures-and-what-they-mean
Category: Market Cycles
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 11. cycles-within-cycles
Category: Market Cycles
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 12. drawdown-management
Category: Risk Management
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 13. free-indicators-vs-professional-tools
Category: Technical Indicators
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 14. how-long-to-become-profitable
Category: Trading Psychology
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 15. how-smart-money-moves
Category: Market Cycles
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 16. how-to-identify-a-trend
Category: Market Structure
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 17. how-to-trade-cycles-with-pentarch
Category: Signal Pilot Product
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 18. identifying-cycle-length
Category: Market Cycles
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 19. inside-signal-pilot ✅
Category: Signal Pilot Product
Languages: en ✅, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 20. moving-averages-explained
Category: Technical Indicators
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 21. multi-timeframe-confirmation
Category: Technical Indicators
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 22. order-types-explained
Category: Practical Trading
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 23. position-sizing-101
Category: Risk Management
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 24. psychology-of-getting-stopped-out
Category: Risk Management
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 25. revenge-trading-recovery
Category: Trading Psychology
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 26. risk-reward-ratio
Category: Risk Management
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 27. rules-based-vs-discretionary
Category: Trading Psychology
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 28. stop-loss-placement
Category: Risk Management
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 29. support-and-resistance-explained
Category: Market Structure
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 30. system-optimization
Category: Backtesting & Systems
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 31. the-1-percent-rule
Category: Risk Management
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 32. the-boredom-trap
Category: Trading Psychology
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 33. the-confirmation-trap
Category: Backtesting & Systems
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 34. the-only-pattern-that-repeats
Category: Market Structure
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 35. the-repainting-problem
Category: Technical Indicators
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 36. timeframe-selection
Category: Technical Indicators
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 37. trade-journaling-that-works
Category: Practical Trading
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 38. trading-around-news
Category: Practical Trading
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 39. trading-journal
Category: Backtesting & Systems
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 40. trading-while-emotional
Category: Trading Psychology
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 41. tradingview-free-scripts
Category: Technical Indicators
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 42. tradingview-setup-guide
Category: Practical Trading
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 43. volume-profile-basics
Category: Technical Indicators
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 44. what-is-a-trading-edge
Category: Backtesting & Systems
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 45. what-profitable-traders-know
Category: Trading Psychology
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 46. when-to-cut-losses-early
Category: Risk Management
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 47. when-to-ignore-divergence
Category: Technical Indicators
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 48. when-to-size-up
Category: Risk Management
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 49. why-backtesting-results-are-worthless
Category: Backtesting & Systems
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 50. why-markets-move-in-cycles
Category: Market Cycles
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 51. why-traders-blow-first-account
Category: Trading Psychology
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 52. why-you-break-trading-rules
Category: Trading Psychology
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 53. why-your-indicators-keep-failing
Category: Technical Indicators
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

### 54. your-first-trade
Category: Risk Management
Languages: en, es, de, fr, it, pt, nl, ru, ja, ar, tr, hu

---

## Next Steps After Schema Updates

Once all 648 files are updated with the three changes above:

1. **Create Category Index Pages** (TIER 2)
   - Create `/categories/[category-slug]/index.html` for each category
   - Add CollectionPage schema

2. **Add Internal Linking** (TIER 1)
   - Related articles section improvements
   - Product feature links from relevant articles

3. **Add signalpilot.io Links & CTAs** (TIER 1)
   - Resource links back to main site
   - CTA improvements

4. **Implement Cross-Repo Linking**
   - Add navigation between blog/docs/education/main site

---

## Verification Checklist

For each file, verify:
- [ ] BlogPosting has `inLanguage` field
- [ ] BlogPosting has `articleSection` field matching category
- [ ] BreadcrumbList has 4 items (Home, Blog, Category, Article)
- [ ] BreadcrumbList position 3 points to correct category slug
- [ ] NewsArticle schema is present
- [ ] File saves without errors
- [ ] Language is maintained (en, es, de, etc.)

