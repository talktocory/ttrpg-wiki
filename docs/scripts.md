# Script Reference

This page documents the included Python utilities. Complete the [Python setup](getting-started.md#2-set-up-the-local-python-environment) first if you want to run them locally.

## Scripts

| Program | Purpose | Intended users | File effects |
| --- | --- | --- | --- |
| [validate.py](#validatepy) | Reports configuration, link, metadata, and visibility problems | GMs wanting a structural check; contributors | No campaign or framework edits |
| [sync_adapters.py](#sync_adapterspy) | Regenerates host instructions and discovered skill mirrors | Contributors changing `AGENTS.md` or skills | Yes, unless using `--check` |
| [package_skills.py](#package_skillspy) | Builds installable ZIP files for the nine skills | Maintainers; users who need to build their own skill packages | Writes skill ZIPs under `dist/skills/` |
| [build_release.py](#build_releasepy) | Builds a distributable copy of the blank project template | Release maintainers | Writes the template ZIP under `dist/` |
| [wiki_tools.py](#wiki_toolspy) | Supplies shared validation, Markdown, path, and checksum functions | Other scripts import it; users do not run it directly | No campaign or framework edits |
| [extract_pdf.py](#extract_pdfpy) | Extracts page-marked text from a PDF with a text layer | GMs and assistants ingesting PDF sources | Prints text or writes the requested output file; never edits the PDF |
| [finalize_token.py](#finalize_tokenpy) | Crops supplied art into a PNG token | GMs who want local token processing | Writes the requested image |
| [test_framework.py](#test_frameworkpy) | Checks that the framework utilities behave as expected | Contributors | Creates temporary test files |

Normal GM use does not require running any of these scripts directly. The AI assistant will make use of them when required.

## validate.py

Source: [scripts/validate.py](../scripts/validate.py).

**Purpose:** find structural mistakes in a campaign or framework checkout and report them without repairing files.

```text
python scripts/validate.py
```

It reads `campaign.yaml`, Markdown files, and the skills' `agents/openai.yaml` metadata. Checks include:

- Required configuration fields, supported values, numeric ranges, duplicate YAML keys, configured reward units, and optional profile paths.
- Local Markdown links, image references, and heading destinations. It checks ordinary inline links and reference definitions, not every possible Markdown or HTML construct.
- The nine canonical skills' names, descriptions, folder names, and selected Codex UI metadata.
- Independent `status` and `visibility` fields on substantive campaign pages, and visibility matching the storage area. Navigation READMEs are exempt from these page checks.
- Player-safe pages linking outside the designated player-safe text/media areas, selected legacy namespace references, and machine-specific paths in Markdown.

It skips generated, local, and temporary directories such as `.venv/`, `.git/`, `dist/`, and editor settings. External web links are not fetched or checked for availability.

**Result:** prints errors with file paths, or a success message. Exit code `0` means the checks passed; `1` means problems were found. Correct the reported source files yourself or ask the assistant to propose fixes, then rerun it.

**Limits:** it cannot decide whether fictional facts contradict one another, whether prose or an image reveals a secret, whether a rule is correct, or whether an AI host follows a skill. A successful check is not permission to publish or share the campaign.

## sync_adapters.py

Source: [scripts/sync_adapters.py](../scripts/sync_adapters.py).

**Purpose:** keep the essential project instructions consistent across the supported hosts. An adapter is an instruction file in the location a particular host expects.

Read-only check:

```text
python scripts/sync_adapters.py --check
```

Regenerate the adapters after deliberately editing `AGENTS.md` or a canonical skill under `.agents/skills/`:

```text
python scripts/sync_adapters.py
```

The generator reads [AGENTS.md](../AGENTS.md) and writes:

- `.github/copilot-instructions.md`
- `CLAUDE.md` for optional Claude Code use
- `docs/platforms/claude-folder-instructions.md` for Desktop folder/task instructions
- `.claude/skills/` mirrors for Claude Code project-skill discovery
- `.github/skills/` mirrors for GitHub Copilot project-skill discovery

The Copilot and Claude Code files receive the full instructions with a short introduction. The Claude Desktop page puts only the campaign instructions into a clearly marked box for the GM to copy; the `Framework development` section and its contributor commands are left out. Claude Code and Copilot mirrors include each skill's instructions, references, scripts, and assets but omit Codex-specific `agents/openai.yaml` metadata. All campaign policy and skill content still come from `AGENTS.md` and `.agents/skills/`. OpenCode v2 reads those canonical locations natively, so it does not need another generated adapter.

**File effects:** generation replaces the three instruction files and managed Claude Code and Copilot skill mirrors. It removes obsolete mirror files recorded in each manifest while preserving unrelated project skills under `.claude/skills/` and `.github/skills/`. Make shared policy edits in `AGENTS.md` and skill edits in `.agents/skills/`. `--check` compares expected content and reports missing, stale, or obsolete generated files without writing anything. A change only to the shared operating guide does not change the generated adapter text; the adapters already direct the assistant to read that guide.

**Result:** exit code `0` after generation or a matching check; `1` when `--check` finds missing or outdated adapters. `--help` lists the supported command options.

**Limits:** it does not install skills, change application settings, configure accounts, or prove that a host loaded its instructions. Follow the relevant platform setup guide as well.

## package_skills.py

Source: [scripts/package_skills.py](../scripts/package_skills.py).

**Purpose:** turn repository skill sources into self-contained installation packages, especially for hosts that accept uploaded skill ZIPs.

```text
python scripts/package_skills.py
```

It first runs the project validation checks. For each skill directory under `.agents/skills/`, it then:

1. Includes the skill's instructions, metadata, scripts, references, and assets, excluding Python bytecode/cache files.
2. Adds the framework license and copies the shared operating guide and page-format reference when linked by the skill.
3. Rewrites those shared reference links inside the packaged `SKILL.md` so they resolve within the ZIP. The source skill is not edited.
4. Checks that local Markdown file links resolve to package members. This package check does not validate heading fragments.
5. Writes one ZIP containing one top-level skill folder. Entry order, timestamps, file permissions, and UTF-8 text line endings are fixed. Skill ZIPs use uncompressed entries so builds match byte for byte across operating systems, Python versions, and compression libraries. The template release ZIP still uses compression.

**Output:** `dist/skills/ttrpg-<skill-name>.zip`, with each path printed. Existing ZIPs with the same names are replaced. The script does not remove unrelated old files from `dist/skills/`. `--help` shows usage; there are no custom packaging options.

Normal campaign directories such as `raw/` and `wiki/gm/` are not bundled. However, files placed inside a skill directory are included: keep private campaign references and personal art out of those authoring directories.

The prepared skill ZIPs are committed so users of upload-based hosts can use them without running Python. Check that the committed packages exactly match their sources without writing files:

```text
python scripts/package_skills.py --check
```

Normal packaging replaces the canonical ZIPs and removes obsolete `ttrpg-*.zip` packages left by renamed or deleted skills. It leaves other files under `dist/skills/` alone. The `--check` form reports missing, stale, or obsolete canonical packages and exits nonzero instead of changing them.

**Limits:** it does not upload or install the ZIPs, include runtime campaign settings, provide image-generation tools, or run live AI-host tests. Validation failures or unresolved package references stop the build with a nonzero exit status. A partially completed build can leave a mix of replaced and earlier packages; rerun the command successfully and use `--check` before distributing them.

## build_release.py

Source: [scripts/build_release.py](../scripts/build_release.py).

**Purpose:** build a distributable copy of the empty framework. This is a maintainer task, not a campaign backup or player-export command.

```text
python scripts/build_release.py
```

It reads [release-files.txt](../release-files.txt), the explicit file allowlist, and [scripts/template-state.json](../scripts/template-state.json), the fingerprints of approved blank campaign scaffolding. It checks that the scaffolding remains unchanged, rejects unexpected campaign files, checks adapter consistency, and runs project validation. It also rejects invalid manifest paths, designated private/generated paths, and credential-like filenames covered by its checks.

**Output:** `dist/ttrpg-wiki-template.zip`, replacing the previous archive only after its pre-build checks succeed. The ZIP contains the allowlisted files under a `ttrpg-wiki/` folder, plus `SHA256SUMS.txt`. These checksums can detect file changes relative to the manifest; they are not a signature or a privacy certification. The archive contains framework source, not the separately built skill ZIPs in `dist/skills/`.

Blank-scaffold fingerprints normalize line endings. The release checksum file hashes the actual archived bytes. The builder does not update the allowlist or fingerprints automatically.

**Result:** exit code `0` with a build summary on success. A refused release prints a reason and exits nonzero. If a previous ZIP already exists, it remains when a new build is refused; do not mistake it for a newly built artifact.

Once you customize `campaign.yaml`, append campaign activity, or add notes and media, refusal is expected. Keep using the campaign; prepare public framework releases from a separate clean template checkout. Do not reset fingerprints merely to make a populated campaign pass.

**Limits:** it does not run unit tests, generate adapters, build skill ZIPs, initialize Git, commit, publish to GitHub, or certify semantic spoiler safety. Review the selected contents before publication. See [release maintenance](maintenance.md).

## wiki_tools.py

Source: [scripts/wiki_tools.py](../scripts/wiki_tools.py).

**Purpose:** provide shared functions to the other utilities. It is a library module, not a command users need to run. Executing it directly performs no project check and prints no result.

Its main responsibilities are:

| Functions | Responsibilities |
| --- | --- |
| `load_yaml`, `UniqueLoader`, `unique_mapping` | Read YAML safely and reject duplicate keys |
| `files` | Enumerate project files while excluding designated local/generated directories |
| `safe_path` | Resolve portable project-relative paths and reject traversal, drive paths, and symlinks in that path |
| `sha256`, `template_digest` | Compute byte-level release hashes and newline-normalized scaffold fingerprints |
| `frontmatter` | Read YAML metadata at the start of Markdown files |
| `markdown_body`, `links`, `heading_ids` | Support the lightweight Markdown link and heading checks |
| `validate_config` | Check the supported configuration schema and values |
| `validate_links` | Check local destinations, heading fragments, and player-safe link boundaries |
| `validate_project` | Combine the configuration, skill, Markdown, and visibility checks |

These functions return parsed data, paths, digests, or error lists to their callers. They do not rewrite the wiki. Keeping them together makes the validator and packaging tools use the same rules. Contributors should test changes here because several commands depend on this module.

## extract_pdf.py

Source: [scripts/extract_pdf.py](../scripts/extract_pdf.py).

**Purpose:** extract text from a PDF source while retaining one-based page markers for later citations. The source PDF is never modified.

Print every page to the terminal:

```text
python scripts/extract_pdf.py raw/pdfs/adventure.pdf
```

Extract selected pages into the ignored temporary area and preserve approximate layout:

```text
python scripts/extract_pdf.py raw/pdfs/adventure.pdf .tmp/adventure-pages.txt --pages 1,3-5 --layout
```

`--pages` accepts unique one-based page numbers and ascending ranges. Without an output path, text goes to standard output. With an output path, the script creates parent directories and refuses to replace an existing file unless `--force` is supplied. It refuses the source path and any `.pdf` destination because the output is UTF-8 text.

Pages without extractable text receive an explicit marker and produce an OCR warning. This can mean the page is blank or that it contains only an image. The utility does not perform OCR, accept passwords for encrypted PDFs, reproduce visual layout exactly, interpret tables, update wiki pages, or establish that extracted content is safe to reveal. Keep the original under `raw/pdfs/`, treat extracted text as source data, and remove temporary output when the task is complete.

**Result:** extracted UTF-8 text with `===== Page N =====` markers, or a nonzero exit status for invalid arguments, unreadable or encrypted PDFs, invalid page selections, and protected output paths.

## finalize_token.py

Source: [the token skill's script](../.agents/skills/ttrpg-token-create/scripts/finalize_token.py).

**Purpose:** process existing artwork into a token PNG. It does not generate a portrait or contact an image service.

```text
python .agents/skills/ttrpg-token-create/scripts/finalize_token.py portrait.png assets/vtt/tokens/portrait-token.png --size 512 --shape circle
```

The script corrects orientation using image metadata, center-crops and resizes the source, applies a circle or square mask, preserves source transparency inside the crop, and optionally adds a border. It writes an RGBA PNG and creates the output's parent directories if needed.

| Argument | Meaning | Default |
| --- | --- | --- |
| `source` | Existing image to process | Required |
| `output` | Destination with a `.png` extension | Required |
| `--size` | Square output size in pixels; supported range 8–8192 | `512` |
| `--shape` | `circle` or `square` | `circle` |
| `--ring-width` | Nonnegative border width in pixels, below half the size | `0` |
| `--ring-color` | Six-digit RGB hex border color | `808080` |
| `--force` | Explicitly allow replacing an existing output | Off |

For example, add `--ring-width 12 --ring-color 808080` for a gray frame. `--help` lists the arguments. The script does not read `campaign.yaml`; pass the appropriate settings explicitly or have the assistant translate your configuration into arguments.

**File effects:** writes the requested image and refuses an existing output unless `--force` is supplied. It always refuses using the source path as the output. It does not update character pages, provenance notes, the index, or the activity log.

**Result:** prints the output path and dimensions on success and exits with status `0`. Invalid arguments or handled processing and file errors print a message and exit with a nonzero status. Center-cropping can remove important details; inspect the output before approval. Processing does not establish artwork rights or player-safe status.

## test_framework.py

Source: [tests/test_framework.py](../tests/test_framework.py).

**Purpose:** verify the utilities' behavior when contributors change them. It uses Python's built-in `unittest` framework and synthetic fixtures.

```text
python -m unittest discover -s tests -v
```

The tests cover campaign and OpenCode configuration validation, duplicate YAML keys, local-path boundaries, player-safe links, self-contained skill packages, reproducible ZIP construction, release refusal for populated campaign state, a clean-template archive round trip, PDF text extraction and output protection, and token dimensions/transparency/overwrite protection. One test extracts the token skill and runs its utility as a standalone process.

**File effects:** creates isolated temporary files and removes them afterward. It reads the framework checkout but does not edit campaign files or write the regular `dist/` packages. The clean-release round-trip test is skipped when the blank-scaffold fingerprints no longer match a populated/customized campaign.

**Result:** prints each test outcome and an overall result; exit code `0` means the tests passed, and nonzero indicates failure. A skipped test is not a pass for that capability. These are utility tests, not live Codex, Claude Desktop, Copilot, or OpenCode/Ollama evaluations; see [behavioral evaluation](evaluation.md).

## Maintainer sequence

After reviewing framework changes, run:

```text
python scripts/sync_adapters.py --check
python scripts/validate.py
python -m unittest discover -s tests -v
python scripts/package_skills.py
python scripts/build_release.py
```

If adapter drift is intentional, regenerate adapters before rerunning the checks. Stop and resolve failures before distributing packages. Build a public template only from blank, reviewed framework scaffolding; ordinary campaign use needs none of this sequence.
