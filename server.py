# -*- coding: utf-8 -*-
import random
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
import html

BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH = BASE_DIR / "template.html"

PORT = 8021
WORDS_AMOUNT = 21

class KindleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/2':
            filename = 'data/words2.txt'
            current_path = '/2'
        elif self.path == '/3':
            filename = 'data/words3.txt'
            current_path = '/3'
        else:
            filename = 'data/words.txt'
            current_path = '/'

        file_path = BASE_DIR / filename

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            lines = [f"Ошибка\tФайл {file_path} не найден"]

        selected_words = random.sample(lines, min(WORDS_AMOUNT, len(lines)))

        nav_html = f"""
<div class="nav-container">
    <a href="/" class="nav-btn {'active-btn' if current_path == '/' else ''}">Список 1</a>
    <a href="/2" class="nav-btn {'active-btn' if current_path == '/2' else ''}">Список 2</a>
    <a href="/3" class="nav-btn {'active-btn' if current_path == '/3' else ''}">Список 3</a>
</div>
"""

        words_html = ""
        for line in selected_words:
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

        bottom_button_html = f'''
<a href="{current_path}" class="btn">Uued sõnad</a>
'''

        page_title = "Eesti keel"
        title_html = f"{len(selected_words)} juhuslikku sõna ({filename})"

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

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html_page.encode('utf-8'))

if __name__ == "__main__":
    server_address = ('', PORT)
    print(f"Server started at port{PORT}!")
    print("Press Ctrl+C for stop")
    httpd = HTTPServer(server_address, KindleHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer Stopped!.")