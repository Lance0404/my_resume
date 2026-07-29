#!/usr/bin/env python3
"""Convert lance_resume.html to lance_resume.pdf using WeasyPrint.

WeasyPrint renders the actual style.css (flexbox, CSS variables, @media
print all supported), so the PDF matches what a browser shows - no
wkhtmltopdf/Chrome dependency required.

Usage:
    .venv/bin/python3 scripts/html_to_pdf.py [input.html] [output.pdf]

Defaults to lance_resume.html -> lance_resume.pdf in the repo root. Run via
the project's .venv (see scripts/README or the resume-to-pdf skill) since
WeasyPrint is only installed there, not system-wide.
"""
import sys
from pathlib import Path

from weasyprint import HTML


def main():
    root = Path(__file__).resolve().parent.parent
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else root / 'lance_resume.html'
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else root / 'lance_resume.pdf'

    HTML(filename=str(src), base_url=str(src.parent)).write_pdf(str(dst))
    print(f'Wrote {dst}')


if __name__ == '__main__':
    main()
