#!/usr/bin/env python3
"""Convert lance_resume.md to lance_resume.html.

Small, dependency-free markdown -> HTML converter tailored to this resume's
markdown conventions (headers, horizontal rules, nested bullet lists, bold/
italic, inline code, links and autolinks). No pandoc/wkhtmltopdf required.

Usage:
    python3 scripts/md_to_html.py [input.md] [output.html]

Defaults to lance_resume.md -> lance_resume.html in the repo root.
"""
import html
import re
import sys
from pathlib import Path

LIST_ITEM_RE = re.compile(r'^(\s*)[-*]\s+(.*)$')
HEADER_RE = re.compile(r'^(#{1,6})\s+(.*)$')


def slugify(text):
    s = text.lower()
    s = re.sub(r'&\w+;', '', s)
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_]+', '-', s).strip('-')
    return s


def convert_inline(text):
    tokens = []

    def store(snippet):
        tokens.append(snippet)
        return f'\x00{len(tokens) - 1}\x00'

    def autolink_sub(m):
        target = m.group(1)
        href = f'mailto:{target}' if '@' in target and not target.startswith('http') else target
        return store(f'<a href="{href}">{html.escape(target)}</a>')

    text = re.sub(r'<([^\s>]+@[^\s>]+|https?://[^\s>]+)>', autolink_sub, text)

    def code_sub(m):
        return store(f'<code>{html.escape(m.group(1))}</code>')

    text = re.sub(r'`([^`]+)`', code_sub, text)

    def link_sub(m):
        return store(f'<a href="{m.group(2)}">{html.escape(m.group(1))}</a>')

    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link_sub, text)

    text = html.escape(text, quote=False)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'__([^_]+)__', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', text)
    text = re.sub(r'(?<!_)_([^_]+)_(?!_)', r'<em>\1</em>', text)

    return re.sub(r'\x00(\d+)\x00', lambda m: tokens[int(m.group(1))], text)


def parse_list(items, idx, indent):
    parts = ['<ul>']
    n = len(items)
    while idx < n and items[idx][0] == indent:
        _, text = items[idx]
        idx += 1
        li_html = convert_inline(text)
        if idx < n and items[idx][0] > indent:
            child_html, idx = parse_list(items, idx, items[idx][0])
            parts.append(f'<li>{li_html}\n{child_html}</li>')
        else:
            parts.append(f'<li>{li_html}</li>')
    parts.append('</ul>')
    return '\n'.join(parts), idx


def parse_markdown(text):
    lines = text.split('\n')
    n = len(lines)
    i = 0
    out = []
    while i < n:
        line = lines[i]

        if line.strip() == '':
            i += 1
            continue

        if line.strip() == '---':
            out.append('<hr />')
            i += 1
            continue

        m = HEADER_RE.match(line)
        if m:
            level = len(m.group(1))
            heading_text = m.group(2).strip()
            slug = slugify(heading_text)
            out.append(f'<h{level} id="{slug}">{convert_inline(heading_text)}</h{level}>')
            i += 1
            continue

        if LIST_ITEM_RE.match(line):
            items = []
            while i < n and LIST_ITEM_RE.match(lines[i]):
                mm = LIST_ITEM_RE.match(lines[i])
                items.append((len(mm.group(1)), mm.group(2)))
                i += 1
            list_html, _ = parse_list(items, 0, items[0][0])
            out.append(list_html)
            continue

        para_lines = []
        while i < n and lines[i].strip() != '' and lines[i].strip() != '---' \
                and not HEADER_RE.match(lines[i]) and not LIST_ITEM_RE.match(lines[i]):
            para_lines.append(lines[i])
            i += 1
        out.append(f'<p>{convert_inline(" ".join(para_lines))}</p>')

    return '\n\n'.join(out)


def build_document(body_html, title, stylesheet):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="{stylesheet}" />
</head>
<body>
{body_html}
</body>
</html>
'''


def main():
    root = Path(__file__).resolve().parent.parent
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else root / 'lance_resume.md'
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else root / 'lance_resume.html'

    markdown_text = src.read_text(encoding='utf-8')
    body_html = parse_markdown(markdown_text)
    document = build_document(body_html, title='Lance Chang - Resume', stylesheet='style.css')
    dst.write_text(document, encoding='utf-8')
    print(f'Wrote {dst}')


if __name__ == '__main__':
    main()
