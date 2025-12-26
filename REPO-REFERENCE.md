# SIGNALPILOT-BLOG - Repository Reference Document

> **Last Updated:** 2025-12-26
> **Purpose:** Centralized reference for all important repository information

---

## Quick Reference

| Property | Value |
|----------|-------|
| **Domain** | blog.signalpilot.io |
| **Type** | Static HTML Blog/Website |
| **Hosting** | GitHub Pages |
| **Total Size** | 746 MB |
| **Articles** | 54 |
| **Languages** | 12 (EN + 11 translations) |
| **Total Commits** | 425+ |
| **Google Analytics** | G-TVTPDWHNP6 |

---

## 1. Repository Purpose

**What it is:** Static HTML trading education blog for Signal Pilot trading indicator platform.

**Primary Functions:**
- Educational content about trading, market psychology, risk management, technical analysis
- Feature Signal Pilot indicator products and practical applications
- Multi-language trading education content

**Target Audience:** Retail traders (beginner to advanced) interested in trading psychology, indicators, risk management, and market structure.

---

## 2. Directory Structure

```
signalpilot-blog/
├── index.html                    # Main homepage (74 KB)
├── CNAME                         # Domain: blog.signalpilot.io
├── IMAGE-CONCEPTS.md             # Hero image generation guidelines
├── feed.xml                      # RSS feed
├── sitemap.xml                   # XML sitemap (129 KB)
│
├── api/
│   └── articles.json             # Article metadata API (54 articles)
│
├── articles/                     # Main content (322 MB, 54 articles)
│   └── [article-slug]/
│       ├── index.html            # English version
│       ├── hero.png              # Hero image
│       └── [lang]/index.html     # Translations (ar,de,es,fr,hu,it,ja,nl,pt,ru,tr)
│
├── assets/
│   ├── css/
│   │   └── blog.css              # Main stylesheet (1,446 lines)
│   └── images/
│       └── categories/           # 11 category icons (PNG)
│
└── [language-code]/              # Homepage translations (ar,de,es,fr,hu,it,ja,nl,pt,ru,tr)
    └── index.html
```

---

## 3. Technologies Used

### Stack
- **HTML5** - Static pages
- **CSS3** - Styling with CSS variables for theming
- **Vanilla JavaScript** - Client-side interactivity
- **XML** - Feed/sitemap
- **JSON** - API data

### External Services
- **Google Fonts:** Space Grotesk, EB Garamond, Gugi
- **Google Analytics:** G-TVTPDWHNP6
- **GitHub Pages:** Hosting

### Design System
- **Dark Theme (Default):** #05070d background
- **Light Theme:** #ffffff background
- **Brand Color:** #5b8aff (blue)
- **Accent Color:** #76ddff (cyan)

---

## 4. Key Files

| File | Purpose | Size |
|------|---------|------|
| `index.html` | Main homepage with article grid | 74 KB |
| `assets/css/blog.css` | All styles + theming | 1,446 lines |
| `api/articles.json` | Article metadata | 388 lines |
| `sitemap.xml` | SEO sitemap | 129 KB |
| `feed.xml` | RSS feed | 15 KB |
| `CNAME` | Custom domain config | - |
| `IMAGE-CONCEPTS.md` | Hero image guidelines | 8 KB |

---

## 5. Content Structure

### 11 Article Categories:
1. Beginner Foundations
2. Technical Analysis
3. Markets
4. Indicators
5. Psychology
6. Market Cycles
7. Practical
8. Risk Management
9. Trading Systems
10. Signal Pilot (product)
11. Advanced

### 12 Supported Languages:
| Code | Language | Notes |
|------|----------|-------|
| en | English | Primary |
| ar | Arabic | RTL support |
| de | German | - |
| es | Spanish | - |
| fr | French | - |
| hu | Hungarian | - |
| it | Italian | - |
| ja | Japanese | - |
| nl | Dutch | - |
| pt | Portuguese | - |
| ru | Russian | - |
| tr | Turkish | - |

---

## 6. Deployment

### Method
- **Static HTML** - No build process required
- **GitHub Pages** - Push to deploy
- **Domain:** blog.signalpilot.io (CNAME configured)

### Workflow
- PR-based development
- Branch naming: `claude/[feature]-[id]`
- Human review before merge

---

## 7. CSS Theme Variables

```css
/* Dark Theme (Default) */
:root {
  --bg: #05070d;
  --text: #ecf1ff;
  --brand: #5b8aff;
  --accent: #76ddff;
  --success: #3ed598;
  --warning: #f9a23c;
}

/* Light Theme */
[data-theme="light"] {
  --bg: #ffffff;
  --text: #0f172a;
  --brand: #3b82f6;
  --accent: #0ea5e9;
}
```

---

## 8. JavaScript Features

| Feature | Description |
|---------|-------------|
| Theme Toggle | Dark/light mode with localStorage |
| Category Filtering | 11 filter buttons for articles |
| Mobile Menu | Hamburger navigation |
| Share Buttons | Twitter, LinkedIn, Copy link |

---

## 9. SEO Configuration

- **XML Sitemap:** All URLs with priorities (1.0 homepage, 0.9 articles)
- **RSS Feed:** 2.0 with Atom namespace
- **hreflang Tags:** Proper language alternate links
- **Meta Tags:** Title, description, OG tags on all pages
- **Cache Control:** no-cache, no-store, must-revalidate

---

## 10. Article Structure

Each article contains:
```
articles/[slug]/
├── index.html       # Full HTML document
├── hero.png         # 1600x900px hero image
└── [lang]/
    └── index.html   # Translated versions
```

### Article HTML Structure:
- Meta tags + hreflang
- Google Analytics script
- Responsive header
- Breadcrumb navigation
- Hero image
- Article content (semantic HTML)
- Reading time (7-11 min avg)
- Share buttons
- Related articles (3 links)
- Footer

---

## 11. Important Notes

### Image Guidelines (from IMAGE-CONCEPTS.md)
- **Format:** WebP preferred, <200KB
- **Dimensions:** 1600x900px (16:9)
- **Style:** Minimalist, dark backgrounds, glowing elements
- **Color Palette:** Dark blue/purple backgrounds, cyan/orange accents

### Content Generation
- Articles generated/translated via Claude automation
- Google Analytics added via bulk automation
- Multi-language support automated

### No Build System
- Pure static HTML - no npm, no bundler
- Direct file edits, push to deploy
- All files pre-rendered

---

## 12. Related Repositories

*To be filled in after unifying with other repo documentation*

---

## 13. Maintenance Commands

```bash
# Deploy (just push to main)
git push origin main

# Check current status
git status

# View recent commits
git log --oneline -10
```

---

## 14. Contact & Resources

- **Website:** blog.signalpilot.io
- **Google Analytics:** G-TVTPDWHNP6
- **RSS Feed:** blog.signalpilot.io/feed.xml
- **Sitemap:** blog.signalpilot.io/sitemap.xml

---

*Document created for cross-repository reference and unification.*
