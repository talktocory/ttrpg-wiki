"""Validate campaign settings, skill metadata, Markdown links, and visibility."""
from wiki_tools import validate_project

if __name__ == '__main__':
    errors = validate_project()
    for error in errors:
        print('ERROR:', error)
    print(f'Validation failed: {len(errors)} error(s).' if errors else 'Campaign and OpenCode configuration, nine skills, links, and visibility checks passed.')
    raise SystemExit(bool(errors))
