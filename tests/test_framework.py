from __future__ import annotations

import copy
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from zipfile import ZipFile
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from wiki_tools import load_yaml, validate_config, validate_links, validate_opencode_config, safe_path, template_digest
from package_skills import BUNDLED, archive_errors, skill_archives, skill_entries, zip_bytes
from build_release import release_entries
from sync_adapters import claude_skill_drift, copilot_skill_drift, expected_claude_skills, expected_copilot_skills, sync_claude_skills, sync_copilot_skills

spec = importlib.util.spec_from_file_location('token_export', ROOT / '.agents/skills/ttrpg-token-create/scripts/finalize_token.py')
token = importlib.util.module_from_spec(spec)
spec.loader.exec_module(token)

class ConfigTests(unittest.TestCase):
    def setUp(self):
        self.config = load_yaml((ROOT / 'campaign.yaml').read_text(encoding='utf-8'))

    def test_system_without_levels_or_currency_is_valid(self):
        self.config['system']['name'] = 'Synthetic narrative game'
        self.config['rewards']['units'] = ['reputation', 'supplies']
        self.config['vtt']['grid'] = 'zones'
        self.assertEqual(validate_config(self.config, ROOT), [])

    def test_invalid_numeric_and_budget_inputs(self):
        for section, key, bad in [('artwork', 'token_pixels', True), ('artwork', 'images_per_round', 0), ('vtt', 'distance_per_cell', float('nan')), ('vtt', 'pixels_per_cell', -1)]:
            with self.subTest(section=section, key=key):
                data = copy.deepcopy(self.config)
                data[section][key] = bad
                self.assertTrue(validate_config(data, ROOT))
        self.config['rewards']['budgets'] = [{'period': 'mission-1', 'unit': 'unconfigured', 'target': 20}]
        self.assertTrue(validate_config(self.config, ROOT))

    def test_profile_cannot_escape_workspace(self):
        self.config['system']['profile'] = '../outside.md'
        self.assertTrue(validate_config(self.config, ROOT))

    def test_yaml_duplicate_keys_fail(self):
        with self.assertRaisesRegex(ValueError, 'Duplicate YAML key'):
            load_yaml('status: Draft\nstatus: Canon\n')

class BoundaryTests(unittest.TestCase):
    def test_private_link_and_missing_heading_are_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            player = root / 'wiki/player-safe/recap.md'
            private = root / 'wiki/gm/reference.md'
            player.parent.mkdir(parents=True)
            private.parent.mkdir(parents=True)
            private.write_text('# Current state\n', encoding='utf-8')
            player.write_text('[secret](../gm/reference.md#missing)\n', encoding='utf-8')
            errors = validate_links(player, root)
            self.assertTrue(any('outside reviewed areas' in e for e in errors))
            self.assertTrue(any('Unknown heading' in e for e in errors))

    def test_safe_asset_and_encoded_path_links(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            player = root / 'wiki/player-safe/recap.md'
            asset = root / 'assets/player-safe/beacon art.png'
            player.parent.mkdir(parents=True)
            asset.parent.mkdir(parents=True)
            asset.write_bytes(b'fixture')
            player.write_text('# Report\n\n![beacon](../../assets/player-safe/beacon%20art.png)\n[here](#report)\n', encoding='utf-8')
            self.assertEqual(validate_links(player, root), [])

    def test_manifest_path_traversal_and_drives_fail(self):
        for path in ('../outside', '/absolute', 'C:/private', 'sub\\file'):
            with self.subTest(path=path), self.assertRaises(ValueError):
                safe_path(ROOT, path, must_exist=False)

class OpenCodeConfigTests(unittest.TestCase):
    def setUp(self):
        self.config = json.loads((ROOT / 'opencode.json').read_text(encoding='utf-8'))

    def test_distributed_profile_uses_ollama_with_guarded_integrations(self):
        self.assertEqual(validate_opencode_config(self.config), [])

    def test_wrong_model_or_changed_safeguards_fail(self):
        cloud = copy.deepcopy(self.config)
        cloud['model'] = 'ollama/qwen3-coder:480b-cloud'
        self.assertTrue(validate_opencode_config(cloud))
        unguarded = copy.deepcopy(self.config)
        unguarded['permissions'] = [rule for rule in unguarded['permissions'] if rule['action'] != 'edit']
        self.assertTrue(validate_opencode_config(unguarded))
        restricted = copy.deepcopy(self.config)
        restricted['policies'] = [{'action': 'provider.use', 'resource': '*', 'effect': 'deny'}]
        self.assertTrue(validate_opencode_config(restricted))

class PackageTests(unittest.TestCase):
    def test_skill_packages_do_not_depend_on_compression_library(self):
        expected = skill_archives()
        with patch('zipfile.zlib', None):
            self.assertEqual(skill_archives(), expected)
            for name, content in expected.items():
                with self.subTest(package=name), ZipFile(io.BytesIO(content)) as archive:
                    skill = ROOT / '.agents/skills' / Path(name).stem
                    self.assertEqual(
                        {member: archive.read(member) for member in archive.namelist()},
                        skill_entries(skill),
                    )

    def test_committed_package_check_reports_drift(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            expected = {'ttrpg-current.zip': b'current'}
            self.assertEqual(archive_errors(output, expected), ['Missing committed skill package: ttrpg-current.zip'])
            (output / 'ttrpg-current.zip').write_bytes(b'stale')
            self.assertEqual(archive_errors(output, expected), ['Stale committed skill package: ttrpg-current.zip'])
            (output / 'ttrpg-current.zip').write_bytes(b'current')
            (output / 'ttrpg-retired.zip').write_bytes(b'retired')
            self.assertEqual(archive_errors(output, expected), ['Obsolete committed skill package: ttrpg-retired.zip'])

    def test_extracted_token_package_runs_independently(self):
        skill = ROOT / '.agents/skills/ttrpg-token-create'
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with ZipFile(io.BytesIO(zip_bytes(skill_entries(skill)))) as archive:
                archive.extractall(root)
            source, output = root / 'supplied art.png', root / 'export token.png'
            Image.new('RGB', (48, 24), 'green').save(source)
            script = root / 'ttrpg-token-create/scripts/finalize_token.py'
            result = subprocess.run([sys.executable, str(script), str(source), str(output), '--size', '64', '--shape', 'square'], capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 0, result.stderr)
            with Image.open(output) as image:
                self.assertEqual(image.size, (64, 64))
                self.assertEqual(image.format, 'PNG')

    def test_every_skill_is_self_contained_and_reproducible(self):
        for skill in sorted((ROOT / '.agents/skills').iterdir()):
            with self.subTest(skill=skill.name):
                entries = skill_entries(skill)
                self.assertIn(f'{skill.name}/SKILL.md', entries)
                self.assertIn(f'{skill.name}/LICENSE', entries)
                source_text = (skill / 'SKILL.md').read_text(encoding='utf-8')
                for original, bundled in BUNDLED.items():
                    if original in source_text:
                        self.assertIn(f'{skill.name}/{bundled}', entries)
                first = zip_bytes(entries)
                self.assertEqual(first, zip_bytes(entries))
                with ZipFile(io.BytesIO(first)) as archive:
                    self.assertIsNone(archive.testzip())
                    self.assertEqual({Path(n).parts[0] for n in archive.namelist()}, {skill.name})

    def test_unbundled_reference_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            skill = Path(directory) / 'ttrpg-test'
            skill.mkdir()
            (skill / 'SKILL.md').write_text('[missing](../private.md)\n', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'Unbundled'):
                skill_entries(skill, Path(directory))

    def test_host_skill_mirrors_preserve_unmanaged_files(self):
        mirrors = [
            ('.claude/skills', expected_claude_skills, sync_claude_skills, claude_skill_drift),
            ('.github/skills', expected_copilot_skills, sync_copilot_skills, copilot_skill_drift),
        ]
        for mirror_root, expected_fn, sync_fn, drift_fn in mirrors:
            with self.subTest(mirror=mirror_root), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                skill = root / '.agents/skills/ttrpg-test'
                (skill / 'agents').mkdir(parents=True)
                (skill / 'references').mkdir()
                (skill / 'SKILL.md').write_text('---\nname: ttrpg-test\ndescription: Synthetic test skill.\n---\n', encoding='utf-8')
                (skill / 'agents/openai.yaml').write_text('interface: {}\n', encoding='utf-8')
                (skill / 'references/guide.md').write_text('# Guide\n', encoding='utf-8')
                unrelated = root / mirror_root / 'personal/SKILL.md'
                unrelated.parent.mkdir(parents=True)
                unrelated.write_text('personal\n', encoding='utf-8')
                outputs = expected_fn(root)
                self.assertIn(f'{mirror_root}/ttrpg-test/SKILL.md', outputs)
                self.assertNotIn(f'{mirror_root}/ttrpg-test/agents/openai.yaml', outputs)
                self.assertEqual(sync_fn(root), 2)
                self.assertEqual(drift_fn(root), [])
                (skill / 'references/guide.md').unlink()
                self.assertTrue(drift_fn(root))
                sync_fn(root)
                self.assertFalse((root / mirror_root / 'ttrpg-test/references/guide.md').exists())
                self.assertEqual(unrelated.read_text(encoding='utf-8'), 'personal\n')

    def test_release_refuses_campaign_data_even_if_added_to_allowlist(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'scripts').mkdir()
            (root / 'scripts/template-state.json').write_text('{}', encoding='utf-8')
            (root / 'raw').mkdir()
            (root / 'raw/private.md').write_text('Synthetic private fixture', encoding='utf-8')
            (root / 'release-files.txt').write_text('raw/private.md\n', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'Unexpected campaign file'):
                release_entries(root)

    def test_release_refuses_modified_blank_campaign(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'scripts').mkdir()
            (root / 'campaign.yaml').write_text('name: private campaign', encoding='utf-8')
            (root / 'scripts/template-state.json').write_text(json.dumps({'campaign.yaml': 'incorrect'}), encoding='utf-8')
            (root / 'release-files.txt').write_text('campaign.yaml\n', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'Template state changed'):
                release_entries(root)

    def test_clean_release_roundtrip_validates(self):
        state = json.loads((ROOT / 'scripts/template-state.json').read_text(encoding='utf-8'))
        if any(template_digest(ROOT / name) != digest for name, digest in state.items()):
            self.skipTest('Release round trip applies only to an unpopulated template checkout')
        entries = release_entries(ROOT)
        with tempfile.TemporaryDirectory() as directory:
            with ZipFile(io.BytesIO(zip_bytes(entries))) as archive:
                archive.extractall(directory)
            from wiki_tools import validate_project
            self.assertEqual(validate_project(Path(directory) / 'ttrpg-wiki'), [])
            self.assertFalse(any('.venv' in name or '.tmp/' in name or '__pycache__' in name for name in entries))

class TokenTests(unittest.TestCase):
    def test_export_preserves_alpha_and_circle_corners(self):
        with tempfile.TemporaryDirectory() as directory:
            source, output = Path(directory) / 'source.png', Path(directory) / 'token.png'
            image = Image.new('RGBA', (80, 40), (100, 160, 200, 128))
            image.save(source)
            token.make_token(source, output, size=64, ring_width=4)
            with Image.open(output) as result:
                self.assertEqual(result.size, (64, 64))
                self.assertEqual(result.mode, 'RGBA')
                self.assertEqual(result.getpixel((0, 0))[3], 0)
                self.assertEqual(result.getpixel((32, 32))[3], 128)
            with self.assertRaises(FileExistsError):
                token.make_token(source, output, size=64)

    def test_square_export_and_invalid_dimensions(self):
        with tempfile.TemporaryDirectory() as directory:
            source, output = Path(directory) / 'source.png', Path(directory) / 'token.png'
            Image.new('RGB', (20, 40), 'blue').save(source)
            token.make_token(source, output, size=32, shape='square')
            with Image.open(output) as result:
                self.assertEqual(result.getpixel((0, 0))[3], 255)
            with self.assertRaises(ValueError):
                token.make_token(source, output, size=32, ring_width=16, force=True)
            with self.assertRaises(ValueError):
                token.make_token(source, source, force=True)

if __name__ == '__main__':
    unittest.main()
