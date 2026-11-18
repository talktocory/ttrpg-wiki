# Contributing to the Project

This page is for people changing the shared project, including its instructions, documentation, and utilities. To run your own campaign, start with the [GM guide](docs/gm-guide.md); you do not need the development commands below.

Keep the core independent of game system, genre, VTT, and provider. Put optional details in profiles and platform guides. Do not contribute real campaign data, personal paths, secrets, purchased source text, or media without reviewed redistribution terms.

Edit skills in `.agents/skills/`. Shared policy lives in `docs/operating-guide.md`; root instructions retain essential boundaries. Regenerate adapters using `python scripts/sync_adapters.py`. ZIPs bundle references from source; do not edit `dist/`.

Install `requirements-dev.txt` in a Python 3.11+ virtual environment and run `AGENTS.md` checks. Add meaningful tests for calculations, file handling, validation, or packaging changes. Documentation changes need relevant link checks.

See the [Python utility reference](docs/scripts.md) for each script's purpose, inputs, outputs, dependencies, file changes, command examples, and limits. It also covers the shared library, token processor, test runner, and the maintainer command sequence.

Use original synthetic fixtures for behavioral evaluations. Record host/version, prompt, observed result, and limitations. Metadata validation does not prove live provider behavior. Describe user-visible changes and validation in pull requests. Upgrade procedures must preserve campaign content and settings.
