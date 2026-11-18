"""Package the explicit framework allowlist, refusing populated campaign state."""
from __future__ import annotations

import json
from pathlib import Path
from wiki_tools import ROOT, safe_path, sha256, template_digest, validate_project
from package_skills import zip_bytes
from sync_adapters import adapter_drift

def release_entries(root: Path = ROOT) -> dict[str, bytes]:
    manifest = root / 'release-files.txt'
    names = [line.strip() for line in manifest.read_text(encoding='utf-8').splitlines() if line.strip() and not line.startswith('#')]
    if len(names) != len(set(names)):
        raise ValueError('Duplicate release manifest entries')
    state = json.loads((root / 'scripts/template-state.json').read_text(encoding='utf-8'))
    for name, digest in state.items():
        if name not in names or template_digest(safe_path(root, name)) != digest:
            raise ValueError(f'Template state changed: {name}; release from a blank framework checkout')
    for area in ('wiki', 'raw', 'assets'):
        for path in (root / area).rglob('*'):
            if path.is_symlink():
                raise ValueError(f'Symlink in campaign area: {path}')
            if path.is_file():
                name = path.relative_to(root).as_posix()
                if name not in names or (not name.startswith('wiki/_templates/') and name not in state):
                    raise ValueError(f'Unexpected campaign file: {path.relative_to(root)}')
    drift = adapter_drift(root)
    if drift:
        raise ValueError('Adapter drift: ' + ', '.join(drift))
    errors = validate_project(root)
    if errors:
        raise ValueError('\n'.join(errors))
    entries = {}
    for name in names:
        path = safe_path(root, name)
        if not path.is_file():
            raise ValueError(f'Manifest entry is not a file: {name}')
        if any(part in {'.git', '.venv', '.tmp', '__pycache__', 'dist'} for part in path.relative_to(root).parts):
            raise ValueError(f'Private/generated directory in manifest: {name}')
        if path.name.startswith('.env') or path.suffix in {'.key', '.pem'}:
            raise ValueError(f'Credential-like file in manifest: {name}')
        entries['ttrpg-wiki/' + name] = path.read_bytes()
    hashes = ''.join(f'{sha256(safe_path(root, name))}  {name}\n' for name in names)
    entries['ttrpg-wiki/SHA256SUMS.txt'] = hashes.encode('utf-8')
    return entries

def main() -> int:
    try:
        entries = release_entries()
    except (ValueError, OSError) as exc:
        print('Release refused:', exc)
        return 1
    output = ROOT / 'dist/ttrpg-wiki-template.zip'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(zip_bytes(entries))
    print(f'Built {output.relative_to(ROOT)} ({len(entries)} files); review before publishing.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
