#!/usr/bin/env python3
"""
Populate language homepages with article cards from the English homepage.
Modifies href from 'articles/{slug}/' to '../articles/{slug}/{lang}/'
"""

import re
import os

# Languages to update
LANGUAGES = ['ar', 'de', 'es', 'fr', 'hu', 'it', 'ja', 'nl', 'pt', 'ru', 'tr']

# Paths
BASE_DIR = '/home/user/signalpilot-blog'
ENGLISH_INDEX = os.path.join(BASE_DIR, 'index.html')

def extract_article_cards(html_content):
    """Extract all article cards from the articles-grid div."""
    # Find the articles-grid div and its content
    pattern = r'<div class="articles-grid">(.*?)</div>\s*</div>\s*</section>'
    match = re.search(pattern, html_content, re.DOTALL)

    if match:
        return match.group(1)
    return None

def modify_hrefs_for_language(article_cards_html, lang):
    """Modify hrefs from 'articles/{slug}/' to '../articles/{slug}/{lang}/'"""
    # Pattern to match href="articles/{slug}/"
    pattern = r'href="articles/([^"]+)/"'
    replacement = rf'href="../articles/\1/{lang}/"'

    modified_html = re.sub(pattern, replacement, article_cards_html)
    return modified_html

def update_language_homepage(lang, modified_article_cards):
    """Update a language homepage with the modified article cards."""
    lang_index_path = os.path.join(BASE_DIR, lang, 'index.html')

    # Read the language homepage
    with open(lang_index_path, 'r', encoding='utf-8') as f:
        lang_html = f.read()

    # Find the empty articles-grid div and replace it with the modified content
    # Pattern to match <div class="articles-grid"> ... </div> (including whitespace)
    pattern = r'(<div class="articles-grid">)(.*?)(</div>)'

    def replacer(match):
        return match.group(1) + '\n' + modified_article_cards + '\n          ' + match.group(3)

    updated_html = re.sub(pattern, replacer, lang_html, flags=re.DOTALL)

    # Write the updated HTML back
    with open(lang_index_path, 'w', encoding='utf-8') as f:
        f.write(updated_html)

    print(f'✓ Updated {lang}/index.html')

def main():
    print('Starting to populate language homepages...\n')

    # Read the English homepage
    print('Reading English homepage...')
    with open(ENGLISH_INDEX, 'r', encoding='utf-8') as f:
        english_html = f.read()

    # Extract article cards
    print('Extracting article cards...')
    article_cards = extract_article_cards(english_html)

    if not article_cards:
        print('ERROR: Could not extract article cards from English homepage')
        return

    print(f'Successfully extracted article cards\n')

    # Update each language homepage
    print('Updating language homepages:')
    for lang in LANGUAGES:
        modified_cards = modify_hrefs_for_language(article_cards, lang)
        update_language_homepage(lang, modified_cards)

    print(f'\n✓ Successfully updated all {len(LANGUAGES)} language homepages!')
    print('\nLanguages updated:', ', '.join(LANGUAGES))

if __name__ == '__main__':
    main()
