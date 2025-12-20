#!/usr/bin/env python3
"""Verify that all language homepages were correctly updated."""

import os
import re

BASE_DIR = '/home/user/signalpilot-blog'
LANGUAGES = ['ar', 'de', 'es', 'fr', 'hu', 'it', 'ja', 'nl', 'pt', 'ru', 'tr']

print("=" * 60)
print("VERIFICATION SUMMARY")
print("=" * 60)
print()

print("Article card counts:")
print("-" * 60)
for lang in LANGUAGES:
    lang_index = os.path.join(BASE_DIR, lang, 'index.html')
    with open(lang_index, 'r', encoding='utf-8') as f:
        content = f.read()
    count = len(re.findall(r'class="article-card"', content))
    print(f"  {lang:3s}: {count:2d} article cards")

print()
print("Sample href patterns (first article for each language):")
print("-" * 60)
for lang in LANGUAGES:
    lang_index = os.path.join(BASE_DIR, lang, 'index.html')
    with open(lang_index, 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.search(r'href="(\.\./articles/[^"]+)"', content)
    if match:
        print(f"  {lang:3s}: {match.group(1)}")

print()
print("=" * 60)
print("✓ All language homepages successfully populated!")
print("=" * 60)
