# my_resume

Resume content lives in `lance_resume.md`. `lance_resume.html` is a rendered,
styled copy generated from it.

### Prerequisites
* Python 3 (no external packages required for the md -> html step)
* For html -> pdf: a project-local virtualenv with [WeasyPrint](https://weasyprint.org/)
    ```sh
    python3 -m venv .venv
    .venv/bin/pip install weasyprint
    ```

### Demo

* from md to html
    ```sh
    python3 scripts/md_to_html.py
    ```
    This reads `lance_resume.md` and writes `lance_resume.html`, linked to
    `style.css`. Paths can be overridden:
    ```sh
    python3 scripts/md_to_html.py <input.md> <output.html>
    ```

* from html to pdf
    ```sh
    .venv/bin/python3 scripts/html_to_pdf.py
    ```
    This reads `lance_resume.html` and writes `lance_resume.pdf` (git-ignored
    build artifact). Paths can be overridden the same way as above.

See `scripts/md_to_html.py` and `scripts/html_to_pdf.py` for the converters
(dependency-free markdown-to-HTML, and WeasyPrint-based HTML-to-PDF - no
pandoc/wkhtmltopdf/Chrome needed), and `.claude/skills/resume-to-html/SKILL.md`
/ `.claude/skills/resume-to-pdf/SKILL.md` for the Claude Code skills that
automate the edit/regenerate workflow.

### Git issue
* https://www.designcise.com/web/tutorial/how-to-fix-permission-to-x-git-denied-to-user-error-in-git-when-using-multiple-local-accounts