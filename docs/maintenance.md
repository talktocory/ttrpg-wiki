# For Contributors: Upgrades and Public Releases

For a GM backing up or updating a campaign, start with the [GM guide](gm-guide.md#common-questions). This page is for people maintaining or publishing the project itself.

The [Python utility reference](scripts.md) explains the validation, adapter generation, skill packaging, release building, and test commands used below. They are optional for normal campaign writing.

## Upgrade a private campaign

Commit or create a backup first. Compare upstream framework changes with local modifications. Update selected `docs/`, `scripts/`, `tests/`, `.agents/skills/`, profiles, and templates through a reviewed diff. Merge `AGENTS.md` intentionally, regenerate adapters, and run the project checks.

Do not overwrite `campaign.yaml`, `wiki/gm/`, `wiki/player-safe/`, `wiki/index.md`, `wiki/log.md`, `raw/`, or `assets/` with blank upstream copies. Propose field-level migrations for schema changes. Resolve metadata and link changes through the approval workflow.

When simplifying older asset-note layouts, migrate any existing notes onto their owning encounter, location, or character pages before removing folders. Preserve provenance, export settings, approval status, reveal restrictions, and incoming links. Keep substantial standalone notes beside their owning page when useful. Leave the image files in `assets/vtt/`.

## Build a release

Use a clean framework checkout, not a populated campaign. Run validation, tests, and adapter checks. `python scripts/build_release.py` uses `release-files.txt`, checks blank campaign scaffolding, and writes `dist/ttrpg-wiki-template.zip` with a SHA-256 manifest. Local environments, Git metadata, credentials, temporary output, and runtime campaign data are excluded. Generate standalone skill ZIPs separately with `python scripts/package_skills.py` only when they are needed.

Review the ZIP manifest, licenses, and compatibility record. Automated checks cannot certify that content is spoiler-free or that you have redistribution rights. Explicitly add new framework files to the release manifest. Blank-scaffold fingerprints in `scripts/template-state.json` use UTF-8 text with normalized newlines; if you deliberately change a blank scaffold, review that exact change before updating its fingerprint. Never regenerate the baseline from a populated campaign. `SHA256SUMS.txt` in the release hashes the archived bytes.

For publication, extract the reviewed ZIP into a new empty directory, initialize a fresh Git repository there, inspect staged files, and create an initial commit. Create the intended public GitHub repository and push only after publication authorization. Do not make a populated private campaign public. Enable GitHub's template-repository setting if desired.

The tooling does not initialize Git, commit, create a remote, publish, or send messages automatically.
