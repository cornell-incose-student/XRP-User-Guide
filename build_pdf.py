#!/usr/bin/env python3
# /// script
# dependencies = [
#   "markdown",
#   "weasyprint",
#   "pymdown-extensions",
# ]
# ///

"""
Generate XRP-Guide.pdf from all markdown files.
Run with: uv run build_pdf.py
"""

import os
import sys

# Help weasyprint find Homebrew's pango/gobject on macOS
homebrew_lib = "/opt/homebrew/lib"
if os.path.isdir(homebrew_lib):
    os.environ["DYLD_LIBRARY_PATH"] = (
        homebrew_lib + ":" + os.environ.get("DYLD_LIBRARY_PATH", "")
    )
    # Re-exec so the updated DYLD_LIBRARY_PATH takes effect before any imports
    if os.environ.get("_WEASYPRINT_REEXEC") != "1":
        os.environ["_WEASYPRINT_REEXEC"] = "1"
        os.execv(sys.executable, [sys.executable] + sys.argv)

import markdown
from weasyprint import HTML
from pathlib import Path

BASE_DIR = Path(__file__).parent

FILES = [
    "README.md",
    "quick-start.md",
    "overview.md",
    "programming.md",
    "sensor-wiring.md",
    "troubleshooting.md",
    "resources.md",
]

MD_EXTENSIONS = [
    "extra",          # tables, fenced_code, inline HTML, attr_list, etc.
    "toc",
    "pymdownx.superfences",  # nested/titled code blocks
]

CSS = """
@page {
    size: A4;
    margin: 2cm 2.5cm;
    @bottom-center {
        content: counter(page);
        font-size: 10pt;
        color: #888;
    }
}

body {
    font-family: -apple-system, "Segoe UI", Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #222;
}

h1 { font-size: 22pt; border-bottom: 2px solid #cc0000; padding-bottom: 6px; margin-top: 0; }
h2 { font-size: 16pt; border-bottom: 1px solid #ddd; padding-bottom: 4px; margin-top: 1.5em; }
h3 { font-size: 13pt; margin-top: 1.2em; }
h4 { font-size: 11pt; margin-top: 1em; }

a { color: #0366d6; }

code {
    font-family: "SFMono-Regular", Consolas, monospace;
    font-size: 9.5pt;
    background: #f5f5f5;
    padding: 1px 4px;
    border-radius: 3px;
}

pre {
    background: #f5f5f5;
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 12px;
    overflow-x: auto;
    font-size: 9pt;
    line-height: 1.5;
}

pre code {
    background: none;
    padding: 0;
}

table {
    border-collapse: collapse;
    width: 100%;
    margin: 1em 0;
    font-size: 10pt;
}

th {
    background: #f0f0f0;
    font-weight: bold;
    text-align: left;
    padding: 8px 10px;
    border: 1px solid #ccc;
}

td {
    padding: 7px 10px;
    border: 1px solid #ddd;
    vertical-align: top;
}

tr:nth-child(even) td { background: #fafafa; }

img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 0.5em auto;
}

blockquote {
    border-left: 4px solid #ddd;
    margin: 1em 0;
    padding: 6px 16px;
    color: #555;
    background: #fafafa;
}

hr {
    border: none;
    border-top: 1px solid #ddd;
    margin: 2em 0;
}

.page-break { page-break-before: always; }

/* Syntax highlighting for fenced code blocks */
.highlight { background: #f5f5f5; }
"""

def build_pdf():
    print("Building XRP-Guide.pdf...")

    sections = []
    for i, filename in enumerate(FILES):
        path = BASE_DIR / filename
        if not path.exists():
            print(f"  WARNING: {filename} not found, skipping.")
            continue

        content = path.read_text()

        # Add a page break before each section except the first
        prefix = '<div class="page-break"></div>\n\n' if i > 0 else ""

        md = markdown.Markdown(extensions=MD_EXTENSIONS)
        html_body = md.convert(content)
        sections.append(prefix + html_body)
        print(f"  Converted {filename}")

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <style>{CSS}</style>
</head>
<body>
{"".join(sections)}
</body>
</html>"""

    output_path = BASE_DIR / "XRP-Guide.pdf"
    HTML(string=full_html, base_url=str(BASE_DIR)).write_pdf(str(output_path))
    print(f"\nDone! Written to {output_path}")

if __name__ == "__main__":
    build_pdf()
