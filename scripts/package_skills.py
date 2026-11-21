"""Build self-contained skill ZIPs without including campaign material."""
from __future__ import annotations

import argparse
import io
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED, ZIP_STORED
from wiki_tools import ROOT, links, validate_project

BUNDLED = {
    '../../../docs/operating-guide.md': 'references/framework/operating-guide.md',
    '../../../wiki/_templates/page-format.md': 'references/framework/page-format.md',
}

def zip_bytes(entries: dict[str, bytes], *, compression: int = ZIP_DEFLATED) -> bytes:
    stream = io.BytesIO()
    with ZipFile(stream, 'w', compression=compression) as archive:
        for name, content in sorted(entries.items()):
            info = ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = compression
            info.create_system = 3  # Unix, matching the file mode stored below.
            info.external_attr = 0o100644 << 16
            archive.writestr(info, content)
    return stream.getvalue()

def skill_archives(root: Path = ROOT) -> dict[str, bytes]:
    # Deflate output varies between zlib builds, including zlib-ng on Windows.
    # Store these small packages uncompressed so --check is portable across CI.
    return {
        skill.name + '.zip': zip_bytes(skill_entries(skill, root), compression=ZIP_STORED)
        for skill in sorted((root / '.agents/skills').iterdir())
        if skill.is_dir()
    }

def archive_errors(output: Path, expected: dict[str, bytes]) -> list[str]:
    existing = {path.name: path for path in output.glob('ttrpg-*.zip') if path.is_file()} if output.is_dir() else {}
    errors = [f'Missing committed skill package: {name}' for name in sorted(set(expected) - set(existing))]
    errors.extend(f'Obsolete committed skill package: {name}' for name in sorted(set(existing) - set(expected)))
    for name in sorted(set(expected) & set(existing)):
        if existing[name].read_bytes() != expected[name]:
            errors.append(f'Stale committed skill package: {name}')
    return errors

def skill_entries(skill: Path, root: Path = ROOT) -> dict[str, bytes]:
    entries = {}
    if (root / 'LICENSE').is_file():
        entries[f'{skill.name}/LICENSE'] = (root / 'LICENSE').read_bytes()
    for source in sorted(skill.rglob('*')):
        if '__pycache__' in source.parts or source.suffix in ('.pyc', '.pyo'):
            continue
        if source.is_symlink():
            raise ValueError(f'Symlink in skill: {source}')
        if source.is_file():
            relative = source.relative_to(skill).as_posix()
            content = source.read_bytes()
            if relative == 'SKILL.md':
                text = content.decode('utf-8')
                for original, bundled in BUNDLED.items():
                    if original in text:
                        reference = (source.parent / original).resolve()
                        if not reference.is_relative_to(root.resolve()):
                            raise ValueError('Shared reference escapes repository')
                        entries[f'{skill.name}/{bundled}'] = reference.read_bytes()
                        text = text.replace(original, bundled)
                content = text.encode('utf-8')
            entries[f'{skill.name}/{relative}'] = content
    # Check every local Markdown link against ZIP members, not the source checkout.
    from posixpath import normpath, join, dirname
    from urllib.parse import urlsplit, unquote
    for name, content in list(entries.items()):
        if not name.endswith('.md'):
            continue
        for destination in links(content.decode('utf-8')):
            url = urlsplit(destination)
            if url.scheme:
                continue
            target = normpath(join(dirname(name), unquote(url.path))) if url.path else name
            if not target.startswith(skill.name + '/') or target not in entries:
                raise ValueError(f'Unbundled skill reference in {name}: {destination}')
    return entries

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='check committed packages without writing files')
    args = parser.parse_args()
    errors = validate_project()
    if errors:
        print('\n'.join(errors))
        return 1
    output = ROOT / 'dist/skills'
    archives = skill_archives()
    if args.check:
        errors = archive_errors(output, archives)
        if errors:
            print('\n'.join(errors))
            return 1
        print(f'Committed skill packages match {len(archives)} source skills.')
        return 0
    output.mkdir(parents=True, exist_ok=True)
    for obsolete in sorted(output.glob('ttrpg-*.zip')):
        if obsolete.name not in archives:
            obsolete.unlink()
            print(f'Removed {obsolete.relative_to(ROOT).as_posix()}')
    for name, content in archives.items():
        archive = output / name
        archive.write_bytes(content)
        print(archive.relative_to(ROOT).as_posix())
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
