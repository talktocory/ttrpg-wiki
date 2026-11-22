# Codex in Visual Studio Code Validation — 2026-11-21

This is a manual validation record for one fresh Codex installation and campaign workflow in Visual Studio Code. It documents the supplied observations; it is not evidence for every Codex surface, account, model, or future build.

## Environment

| Item | Observed value |
| --- | --- |
| Date | 2026-11-21 |
| Operating system | Windows 11 Home |
| Host | Visual Studio Code 1.147.0 |
| AI assistant | OpenAI Codex extension 26.1117.41037 |
| Git | 2.40.0.windows.1 |
| Python | 3.13.7 |

The notes did not record the selected Codex model, reasoning setting, permission mode, account plan, command approvals, or elapsed task times.

## Fresh installation and workspace setup

The tester installed Git from `git-scm.com`, Python from `python.org`, Visual Studio Code from `code.visualstudio.com`, and the OpenAI Codex extension from the Visual Studio Marketplace.

The latest `ttrpg-wiki-template.zip` release was downloaded and extracted. The archive's `ttrpg-wiki/` folder was moved into a local `Campaigns/` directory and renamed `The Forgotten Circus`. The downloaded archive and now-empty extraction folder were removed. The resulting campaign folder contained the framework directories, including `.agents/`, `.claude/`, `.github/`, and `assets/`.

Visual Studio Code opened the campaign folder, and the tester trusted it when prompted. In the project root, PowerShell created and activated a virtual environment and installed the development requirements:

```powershell
python -m venv .venv
./.venv/Scripts/Activate.ps1
python -m pip install -r requirements-dev.txt
```

The tester then selected Source Control, initialized a local Git repository, and created an initial commit with the message `feat: initial campaign commit`.

## Campaign connection and skill discovery

The first prompt was:

```text
Help me get started with this campaign notebook. Read AGENTS.md and follow the campaign instructions. Tell me which campaign you are using and whether you can read and save its files. Leave everything unchanged for now.
```

Codex was then asked to use:

```text
@ttrpg-campaign-init
```

In this extension build, the tester used the `@` composer menu to select project skills. Earlier Codex usage had used a `/` prefix. This is an observed interface convention for this build, not evidence that every Codex surface uses `@` or that slash commands have been universally replaced.

The tester supplied these settings:

- Campaign name: The Forgotten Circus
- Game and edition: Dungeons & Dragons 5.5e (2024)
- Premise: Discover, explore, and survive a haunted circus.
- Genre and tone: Fantasy, haunted, circus, creepy
- Session length: A one-shot of about three hours

After reviewing the proposal, the tester approved it with:

```text
Proposal is approved. Please proceed with the appropriate updates.
```

The notes report that the campaign configuration proposal was accepted and applied.

## PDF-source ingestion

The tester copied `The Forgotten Circus_ A Cursed One-Shot Adventure - Printer Friendly - v2.pdf` into `raw/pdfs/` and invoked:

```text
@ttrpg-wiki-ingest
```

Codex created a temporary working directory containing scripts and intermediate files while processing the source. After the proposal was approved with the standard approve-and-apply prompt, Codex applied the wiki ingest and removed the temporary files. The tester committed the result with `feat: initial ingest of The Forgotten Circus`.

This confirms that PDF access was available in this Codex session. It does not identify the underlying extraction mechanism or establish PDF support for every account and environment.

## Map generation

The tester invoked:

```text
@ttrpg-map-create Please create a map of the circus grounds.
```

Codex generated a photorealistic fantasy image of the circus grounds using an available image-generation capability. The tester then approved the proposed map and asked Codex to add it to the wiki.

The supplied notes do not record the final asset path, pixel dimensions, file format, generation time, provenance entry, or the exact wiki files saved after approval. The observation therefore establishes successful image generation, but not verification of every final export and wiki-link requirement.

## Session preparation and NPC dialogue

The tester invoked session preparation for a one-shot:

```text
@ttrpg-session-prep This adventure will be run as a one-shot. Please help me plan the session.
```

The resulting proposal was approved with the standard approve-and-apply prompt. The tester then invoked:

```text
@ttrpg-npc-dialogue
```

and approved that proposal as well. The supplied notes do not explicitly identify the final files or state that they were inspected on disk, so this record confirms successful invocation and proposal approval but does not make a stronger saved-output claim for these two tasks.

## Result and limits

- A release ZIP could be turned into a named campaign folder without a pre-existing Git clone.
- The project worked with Python 3.13.7 and the pinned requirements.
- Codex read the workspace instructions and discovered project skills through the extension's `@` menu.
- Proposal-first campaign initialization and PDF ingestion worked, and the approved ingest was committed locally.
- Task-specific temporary files were cleaned up after ingestion.
- Built-in image generation produced requested map artwork.
- Session preparation and NPC dialogue reached reviewed approval; final saved-file inspection was not included in the notes.
- Player-safe review, rewards, maintenance, token creation, partial approval, interrupted temporary cleanup, and framework upgrades were not tested.
- The test does not establish minimum supported versions or behavior in Codex CLI, the ChatGPT desktop app, Codex cloud, or later extension builds.
