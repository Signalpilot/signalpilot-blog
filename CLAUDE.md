# Claude Code Project Instructions

This is a static blog site with articles translated into multiple languages (AR, DE, ES, FR, HU, IT, JA, NL, PT, RU, TR).

## Working with Large Files

This repository contains many HTML files that can be quite large (50KB+ for index files, 25KB+ for article translations). To avoid token limit errors:

1. **Read files selectively** - Use `limit` and `offset` parameters when reading large files
2. **Process one language at a time** - Don't try to read/modify all translations simultaneously
3. **Use targeted searches** - Use Grep/Glob to find specific content rather than reading entire files

## Repository Structure

- `/articles/` - English article source files
- `/ar/`, `/de/`, `/es/`, etc. - Language-specific translations
- `/api/articles.json` - Article metadata index
- `/assets/` - Images and static assets
- `/index.html` - Main homepage (65KB)

## Common Tasks

### Adding a New Article
1. Create the article in `/articles/{slug}/index.html`
2. Create translations in each language folder: `/{lang}/articles/{slug}/index.html`
3. Update `/api/articles.json` with article metadata

### Modifying Articles
- Work on one article and one language at a time to avoid large responses
- Use search tools to locate specific sections before making edits

## Token Limit Configuration

If you encounter "output token maximum" errors, set the environment variable:

```bash
export CLAUDE_CODE_MAX_OUTPUT_TOKENS=64000
```

This allows longer responses when working with large files.
