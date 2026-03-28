# anki2web

A small Python project for turning Anki-style word lists into a simple Kindle-friendly reading page.

The project includes two separate tools:

- `server.py` — runs a lightweight local web server and shows random words from text files
- `converter.py` — converts a word list into a static `index.html` page

This project was made for relaxed evening vocabulary reading on a Kindle or other e-reader, not as a full flashcard or spaced-repetition system.

## Features

- simple Kindle-friendly layout
- hidden translations
- random word selection in server mode
- multiple word lists
- static HTML export
- no external dependencies, only Python standard library

## Project structure

```text
anki2web/
├─ server.py
├─ converter.py
├─ template.html
├─ words.txt
├─ words2.txt
├─ words3.txt
├─ README.md
└─ .gitignore
````

## Input format

The word list is a plain text file.

Preferred format:

```text
tere	hello
maja	house
õppima	to study
```

Tab-separated lines work best.

If there is no tab, the script will try to split by the first space.

## Usage

### 1. Run the local server

```bash
python server.py
```

Then open the page in your browser:

```text
http://localhost:8021
```

You can also open it from another device in your local network by using your computer's local IP address.

### 2. Generate a static HTML page

```bash
python converter.py
```

This will create or update:

```text
index.html
```

## Files

* `words.txt` — main list
* `words2.txt` — second list
* `words3.txt` — third list
* `template.html` — shared HTML template
* `index.html` — generated output from converter mode

## Notes

* The project is intentionally minimal.
* It is designed for simple reading, not for tracking progress or scheduling reviews.
* The same HTML template is used by both the server and the converter.

## Requirements

* Python 3.x
* any browser or e-reader with basic web support

## License

MIT

