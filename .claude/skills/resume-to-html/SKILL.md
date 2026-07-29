---
name: resume-to-html
description: Regenerate lance_resume.html from lance_resume.md in this repo using the dependency-free converter (scripts/md_to_html.py) and style.css. Use whenever the resume markdown is edited and the HTML needs to be refreshed, or when asked to convert the resume md to html, without using pandoc/wkhtmltopdf.
---

# Resume: markdown -> HTML

This repo keeps the source of truth in `lance_resume.md` and renders it to
`lance_resume.html` for viewing/printing. The HTML is generated with a small
in-repo script, not pandoc/wkhtmltopdf (see `README.md` for the old pandoc
approach, which is intentionally not used here).

## When to use this skill
- The user edited or asked you to edit `lance_resume.md` and wants the HTML
  regenerated.
- The user asks to "convert the md to html" for this project.
- The user asks to restyle the resume (`style.css`).

## How to regenerate the HTML

```sh
python3 scripts/md_to_html.py
```

This reads `lance_resume.md` and writes `lance_resume.html` (both default
paths, overridable via `python3 scripts/md_to_html.py <in.md> <out.html>`),
linking to `style.css`. No external dependencies (pure standard library).

## Making content edits

1. Edit `lance_resume.md` directly (headers `#`/`##`/`###`, `-`/`*` bullets
   with 4-space nested indentation, `**bold**`, `_italic_`, `` `code` ``,
   `[text](url)` links, and `<email>`/`<url>` autolinks are all supported by
   the converter).
2. Re-run the script above to refresh `lance_resume.html`.
3. Open `lance_resume.html` in a browser to sanity-check rendering,
   especially after structural changes (new nesting levels, new inline
   syntax) since the converter is a small custom implementation, not a full
   CommonMark parser.

## Restyling

`style.css` is a standalone, modern stylesheet (not the original pandoc
resume theme). It targets plain semantic tags emitted by the converter:
`h1`/`h2`/`h3`, `ul`/`li` (including nested `ul` for sub-bullets), `strong`,
`em`, `a`, `code`. The contact-info line right under the name/title relies on
the `h1 + h2 + ul` sibling selector, so keep that structure (name as `h1`,
title as the very next `h2`, contact bullets as the very next `ul`) if you
restyle further.

## Extending the converter

`scripts/md_to_html.py` is intentionally minimal and tuned to this resume's
markdown conventions (see its module docstring). If new markdown syntax is
introduced in `lance_resume.md` (e.g. tables, blockquotes, code fences) and
the converter doesn't handle it, extend `parse_markdown`/`convert_inline`
rather than reaching for pandoc.
