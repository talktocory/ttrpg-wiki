"""Shared validation and safe local-path helpers for framework utilities."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit
import yaml

ROOT = Path(__file__).resolve().parents[1]
IGNORED = {'.git', '.venv', '.tmp', 'dist', '__pycache__', '.pytest_cache', '.obsidian', '.vscode', '.idea'}
STATUSES = {'Canon', 'Draft', 'Unused', 'Retired'}
VISIBILITIES = {'GM', 'Player-safe'}

OPENCODE_PERMISSIONS = [
    ('external_directory', '*', 'ask'),
    ('edit', '*', 'ask'),
    ('shell', '*', 'ask'),
    ('webfetch', '*', 'allow'),
    ('websearch', '*', 'ask'),
    ('experimental_image_generate', '*', 'ask'),
]

class UniqueLoader(yaml.SafeLoader):
    pass

def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            hash(key)
        except TypeError as exc:
            raise ValueError('YAML mapping keys must be scalar values') from exc
        if key in result:
            raise ValueError(f'Duplicate YAML key: {key}')
        result[key] = loader.construct_object(value_node, deep=deep)
    return result

UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)

def load_yaml(text: str):
    return yaml.load(text, Loader=UniqueLoader)

def validate_opencode_config(data) -> list[str]:
    """Validate the distributed Ollama default and guarded optional integrations."""
    errors = []
    if not isinstance(data, dict):
        return ['configuration must be a JSON object']
    if data.get('$schema') != 'https://opencode.ai/config.json':
        errors.append('missing OpenCode v2 schema')
    if data.get('model') != 'ollama/qwen3-coder:30b':
        errors.append('model must be the reviewed local Ollama model')

    def rules(name):
        value = data.get(name)
        if not isinstance(value, list) or not all(isinstance(rule, dict) for rule in value):
            errors.append(f'{name} must be a list of rule objects')
            return []
        return [(rule.get('action'), rule.get('resource'), rule.get('effect')) for rule in value]

    permissions = rules('permissions')
    if permissions != OPENCODE_PERMISSIONS:
        errors.append('permissions must match the reviewed OpenCode workspace policy')
    if 'policies' in data:
        errors.append('provider policies must not prevent optional OpenCode integrations')
    return errors

def files(root: Path):
    for path in sorted(root.rglob('*')):
        if not any(part in IGNORED for part in path.relative_to(root).parts) and path.is_file():
            yield path

def safe_path(root: Path, relative: str, must_exist: bool = True) -> Path:
    """Resolve a portable project path; reject traversal, symlinks, and drives."""
    parts = PurePosixPath(relative)
    if not relative or '\\' in relative or ':' in relative or parts.is_absolute() or '..' in parts.parts:
        raise ValueError(f'Not a portable project-relative path: {relative}')
    path = root.joinpath(*parts.parts)
    for parent in (path, *path.parents):
        if parent == root.parent:
            break
        if parent.is_symlink():
            raise ValueError(f'Symlink is not permitted here: {relative}')
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f'Path escapes workspace: {relative}')
    if must_exist and not path.exists():
        raise ValueError(f'Missing path: {relative}')
    return path

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def template_digest(path: Path) -> str:
    """Scaffold comparison ignores platform newline conversion; release hashes do not."""
    return hashlib.sha256(path.read_text(encoding='utf-8').encode('utf-8')).hexdigest()

def frontmatter(text: str):
    if not text.startswith('---\n'):
        return None
    match = re.match(r'^---\n(.*?)\n---(?:\n|$)', text, re.S)
    if not match:
        raise ValueError('Unclosed YAML frontmatter')
    value = load_yaml(match.group(1))
    if not isinstance(value, dict):
        raise ValueError('Frontmatter must be a mapping')
    return value

def markdown_body(text: str) -> str:
    return re.sub(r'^(`{3,}|~{3,}).*?^\1\s*$', '', text, flags=re.M | re.S)

def links(text: str):
    text = markdown_body(text)
    # Inline Markdown links/images plus reference-style definitions.
    pattern = r'!?\[[^\]\n]*\]\(\s*(?:<([^>]+)>|([^\s)]+))(?:\s+["\'][^\n]*?["\'])?\s*\)|^\s*\[[^\]]+\]:\s*(?:<([^>]+)>|(\S+))'
    for match in re.finditer(pattern, text, re.M):
        yield next(value for value in match.groups() if value is not None)

def heading_ids(text: str) -> set[str]:
    result, counts = set(), {}
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', markdown_body(text), re.M):
        heading = re.sub(r'!?\[([^\]]+)\]\([^)]*\)', r'\1', heading)
        slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        result.add(f'{slug}-{count}' if count else slug)
    return result

def validate_links(path: Path, root: Path) -> list[str]:
    errors = []
    text = path.read_text(encoding='utf-8')
    player = path.is_relative_to(root / 'wiki/player-safe') and path.name != 'README.md'
    for destination in links(text):
        url = urlsplit(destination)
        if url.scheme in ('https', 'http', 'mailto'):
            continue
        if url.scheme or url.netloc or destination.startswith('/'):
            errors.append(f'Nonportable local link: {destination}')
            continue
        local = unquote(url.path)
        target = (path.parent / local).resolve() if local else path.resolve()
        if not target.is_relative_to(root.resolve()):
            errors.append(f'Link escapes workspace: {destination}')
            continue
        if not target.exists():
            errors.append(f'Broken link: {destination}')
            continue
        if player and not any(target.is_relative_to((root / base).resolve()) for base in ('wiki/player-safe', 'assets/player-safe')):
            errors.append(f'Player-safe link points outside reviewed areas: {destination}')
        if url.fragment and target.is_file() and target.suffix == '.md':
            if unquote(url.fragment) not in heading_ids(target.read_text(encoding='utf-8')):
                errors.append(f'Unknown heading: {destination}')
    return errors

def validate_config(data, root: Path) -> list[str]:
    errors = []
    schema = {
        'campaign': {'name': str, 'premise': str, 'genre': str, 'tone': str, 'language': str},
        'system': {'name': (str, type(None)), 'edition': (str, type(None)), 'profile': (str, type(None)), 'references': list, 'house_rules': list},
        'terminology': {'gm': str, 'player_character': str, 'advancement': str},
        'table': {'session_minutes': (int, type(None)), 'preferences': list},
        'rewards': {'units': list, 'period': str, 'budgets': list},
        'vtt': {'profile': (str, type(None)), 'grid': str, 'distance_unit': (str, type(None)), 'distance_per_cell': (int, float, type(None)), 'pixels_per_cell': (int, type(None))},
        'artwork': {'style': str, 'token_shape': str, 'token_pixels': int, 'map_format': str, 'images_per_round': int},
        'workflow': {'approval': str, 'integrations': list},
    }
    if not isinstance(data, dict):
        return ['Configuration must be a mapping']
    if type(data.get('schema_version')) is not int or data.get('schema_version') != 1:
        errors.append('schema_version must be 1')
    if set(data) != set(schema) | {'schema_version'}:
        errors.append('Configuration has missing or unknown sections')
    for section, fields in schema.items():
        value = data.get(section)
        if not isinstance(value, dict) or set(value) != set(fields):
            errors.append(f'{section}: missing or unknown fields')
            continue
        for key, expected in fields.items():
            types = expected if isinstance(expected, tuple) else (expected,)
            if type(value[key]) not in types:
                errors.append(f'{section}.{key}: invalid type')
    if errors:
        return errors
    for section, key in [('system', 'references'), ('system', 'house_rules'), ('table', 'preferences'), ('rewards', 'units'), ('workflow', 'integrations')]:
        if any(not isinstance(v, str) or not v.strip() for v in data[section][key]):
            errors.append(f'{section}.{key}: entries must be nonempty strings')
    units = data['rewards']['units']
    if all(isinstance(unit, str) for unit in units) and len(set(units)) != len(units):
        errors.append('rewards.units: duplicate units')
    if not data['campaign']['name'].strip() or not data['rewards']['period'].strip():
        errors.append('Campaign name and reward period must not be blank')
    for section in ('system', 'vtt'):
        profile = data[section]['profile']
        if profile:
            try:
                target = safe_path(root, profile)
                if not target.is_file() or target.suffix != '.md':
                    raise ValueError('Profile must be a Markdown file')
            except ValueError as exc:
                errors.append(f'{section}.profile: {exc}')
    for section, key, allowed in [('vtt', 'grid', {'none', 'square', 'hex', 'zones'}), ('artwork', 'token_shape', {'circle', 'square'}), ('artwork', 'map_format', {'jpg', 'png'}), ('workflow', 'approval', {'proposal-first'})]:
        if data[section][key] not in allowed:
            errors.append(f'{section}.{key}: unsupported value')
    for section, key in [('table', 'session_minutes'), ('vtt', 'distance_per_cell'), ('vtt', 'pixels_per_cell'), ('artwork', 'token_pixels'), ('artwork', 'images_per_round')]:
        value = data[section][key]
        if value is not None and (value <= 0 or value != value or value == float('inf')):
            errors.append(f'{section}.{key}: must be finite and positive')
    if not 8 <= data['artwork']['token_pixels'] <= 8192:
        errors.append('artwork.token_pixels: supported range is 8..8192')
    seen = set()
    for budget in data['rewards']['budgets']:
        if not isinstance(budget, dict) or set(budget) != {'period', 'unit', 'target'}:
            errors.append('Budget needs period, unit, and target')
            continue
        if not isinstance(budget['period'], str) or not budget['period'].strip() or not isinstance(budget['unit'], str):
            errors.append('Budget period and unit must be nonempty strings')
            continue
        target = budget['target']
        if budget['unit'] not in units or type(target) not in (int, float) or target < 0 or target != target or target == float('inf'):
            errors.append('Budget requires a configured unit and finite nonnegative target')
        key = (budget['period'], budget['unit'])
        if key in seen:
            errors.append('Duplicate budget period/unit')
        seen.add(key)
    return errors

def validate_project(root: Path = ROOT) -> list[str]:
    errors = []
    try:
        errors.extend(f'campaign.yaml: {e}' for e in validate_config(load_yaml((root / 'campaign.yaml').read_text(encoding='utf-8')), root))
    except (ValueError, yaml.YAMLError, OSError) as exc:
        errors.append(f'campaign.yaml: {exc}')
    try:
        errors.extend(f'opencode.json: {e}' for e in validate_opencode_config(json.loads((root / 'opencode.json').read_text(encoding='utf-8'))))
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        errors.append(f'opencode.json: {exc}')
    skill_count = 0
    for path in files(root):
        relative = path.relative_to(root).as_posix()
        if path.is_symlink():
            errors.append(f'{relative}: symlinks are not portable release files')
        if path.suffix != '.md':
            continue
        try:
            text = path.read_text(encoding='utf-8')
            metadata = frontmatter(text)
            errors.extend(f'{relative}: {e}' for e in validate_links(path, root))
            if path.name == 'SKILL.md' and relative.startswith('.agents/skills/'):
                skill_count += 1
                if not metadata or set(metadata) != {'name', 'description'}:
                    raise ValueError('Skill frontmatter needs only name and description')
                if metadata['name'] != path.parent.name or not re.fullmatch(r'ttrpg-[a-z0-9-]{1,57}', metadata['name']):
                    raise ValueError('Skill name must match its portable folder name')
                if not isinstance(metadata['description'], str) or not 1 <= len(metadata['description']) <= 200:
                    raise ValueError('Portable skill descriptions must be 1..200 characters')
                ui = load_yaml((path.parent / 'agents/openai.yaml').read_text(encoding='utf-8'))['interface']
                if not 25 <= len(ui['short_description']) <= 64 or '$' + metadata['name'] not in ui['default_prompt']:
                    raise ValueError('Invalid Codex UI metadata')
            substantive = relative.startswith(('wiki/gm/', 'wiki/player-safe/')) and path.name != 'README.md'
            if substantive:
                if not metadata or metadata.get('status') not in STATUSES or metadata.get('visibility') not in VISIBILITIES:
                    raise ValueError('Campaign page needs valid independent status and visibility')
                expected = 'Player-safe' if relative.startswith('wiki/player-safe/') else 'GM'
                if metadata['visibility'] != expected:
                    raise ValueError('Visibility does not match storage area')
            # Portable namespace/path checks; game names are allowed in optional profiles.
            if re.search(r'wiki/dm/|\bdnd-[a-z]|\b[A-Za-z]:[/\\]', text):
                raise ValueError('Legacy namespace or machine-specific path')
        except (ValueError, yaml.YAMLError, OSError, KeyError, TypeError) as exc:
            errors.append(f'{relative}: {exc}')
    if skill_count != 8:
        errors.append(f'Expected eight canonical skills; found {skill_count}')
    return errors
