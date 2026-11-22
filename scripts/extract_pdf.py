#!/usr/bin/env python3
"""Extract page-marked text from a PDF without modifying the source file."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

from pypdf import PdfReader
from pypdf.errors import PdfReadError


def parse_pages(value: str | None, total: int) -> list[int]:
    """Return selected one-based page numbers, preserving the requested order."""
    if total < 1:
        return []
    if value is None:
        return list(range(1, total + 1))
    pages: list[int] = []
    try:
        for item in value.split(','):
            item = item.strip()
            if not item:
                raise ValueError
            if '-' in item:
                start_text, end_text = item.split('-', 1)
                start, end = int(start_text), int(end_text)
                if start > end:
                    raise ValueError
                selected = range(start, end + 1)
            else:
                selected = (int(item),)
            for page in selected:
                if page < 1 or page > total or page in pages:
                    raise ValueError
                pages.append(page)
    except ValueError as exc:
        raise ValueError(f'Pages must be unique values or ascending ranges within 1..{total}.') from exc
    return pages


def extract_pdf(source: Path, page_spec: str | None = None, layout: bool = False) -> tuple[str, int]:
    """Extract selected pages and return marked text plus the empty-page count."""
    if source.suffix.lower() != '.pdf':
        raise ValueError('Source must have a .pdf extension.')
    reader = PdfReader(source)
    if reader.is_encrypted:
        raise ValueError('Encrypted PDFs are not supported by this utility.')
    pages = parse_pages(page_spec, len(reader.pages))
    sections: list[str] = []
    empty = 0
    for number in pages:
        page = reader.pages[number - 1]
        text = page.extract_text(extraction_mode='layout') if layout else page.extract_text()
        text = (text or '').strip()
        if not text:
            empty += 1
            text = '[No extractable text; this page may be blank or image-only and may require OCR.]'
        sections.append(f'===== Page {number} =====\n{text}')
    return '\n\n'.join(sections) + ('\n' if sections else ''), empty


def save_text(source: Path, output: Path, text: str, force: bool = False) -> None:
    """Write extracted text while protecting the source and existing output."""
    if source.resolve() == output.resolve():
        raise ValueError('Source and output must be different files.')
    if output.suffix.lower() == '.pdf':
        raise ValueError('Text output must not use a .pdf extension.')
    if output.exists() and not force:
        raise FileExistsError('Output exists; select a new path or explicitly pass --force.')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text, encoding='utf-8')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path, help='PDF file to read')
    parser.add_argument('output', type=Path, nargs='?', help='Optional text output; omit to print to stdout')
    parser.add_argument('--pages', help='One-based pages, for example 1,3-5')
    parser.add_argument('--layout', action='store_true', help='Use pypdf layout-mode text extraction')
    parser.add_argument('--force', action='store_true', help='Explicitly authorize replacing an existing output')
    args = parser.parse_args()
    try:
        text, empty = extract_pdf(args.source, args.pages, args.layout)
        if args.output is None:
            sys.stdout.write(text)
        else:
            save_text(args.source, args.output, text, args.force)
            print(f'Wrote {args.output} ({len(text.encode("utf-8"))} bytes).')
        if empty:
            print(f'Warning: {empty} selected page(s) had no extractable text; OCR may be required.', file=sys.stderr)
    except (FileExistsError, OSError, PdfReadError, ValueError) as exc:
        parser.error(str(exc))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
