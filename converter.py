# -*- coding: utf-8 -*-
from pathlib import Path
import html

BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH = BASE_DIR / "template.html"
INPUT_FILE = BASE_DIR / "data/words.txt"
OUTPUT_FILE = BASE_DIR / "index.html"

with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip()]

words_html = ""
for line in lines:
    if '\t' in line:
        parts = line.split('\t', 1)
    else:
        parts = line.split(maxsplit=1)

    word = html.escape(parts[0])
    translation = html.escape(parts[1] if len(parts) > 1 else "")

    words_html += '    <div class="word-block">\n'
    words_html += f'        <span class="word">{word}</span>\n'
    words_html += f'        <span class="translation">— {translation}</span>\n'
    words_html += '    </div>\n'

nav_html = ""
bottom_button_html = ""
page_title = "Eesti keel - Anki"
title_html = f"Anki: Sõnavara ({len(lines)} sõna)"

with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
    template = f.read()

html_page = (
    template
    .replace("{{PAGE_TITLE}}", page_title)
    .replace("{{NAV}}", nav_html)
    .replace("{{TITLE}}", title_html)
    .replace("{{WORDS_BLOCKS}}", words_html)
    .replace("{{BOTTOM_BUTTON}}", bottom_button_html)
)

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(html_page)

print(f"Успех! Файл {OUTPUT_FILE} обновлен. Добавлено слов: {len(lines)}")