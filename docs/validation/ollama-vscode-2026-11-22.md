# Ollama in Visual Studio Code Validation — 2026-11-22 Record

This is a manual validation record for one local Ollama campaign workflow in Visual Studio Code. The notes were recorded on 2026-11-22; the execution date was not stated separately. The record documents the supplied observations and is not evidence for every computer, Ollama model, extension build, or future release.

## Environment

| Component | Recorded value |
| --- | --- |
| Operating system | Windows 11 Home |
| Host | Visual Studio Code 1.147.0 |
| AI integration | Ollama extension for Visual Studio Code (`ollama.ollama`); extension version not recorded |
| Ollama | 0.40.17 |
| Model | `qwen3-coder:30b` |
| Git | 2.40.0.windows.1 |
| Python | 3.13.7 |

The hardware, RAM, GPU, effective model context, and extension version were not recorded.

## Installation and campaign workspace

The tester installed Git from `git-scm.com`, Python from `python.org`, Visual Studio Code from `code.visualstudio.com`, Ollama from `ollama.com`, and the Ollama extension from the Visual Studio Marketplace. Ollama's context-length setting was set to 64K. The model selector later displayed a 262K maximum, but the effective context used by the session was not measured.

The tester downloaded the latest `ttrpg-wiki-template.zip` release, extracted its top-level `ttrpg-wiki/` folder into a local `Campaigns/` directory, renamed it `The Forgotten Circus`, and removed the downloaded archive and empty extraction directory. The resulting campaign folder contained `.agents/`, `.claude/`, `.github/`, `assets/`, `campaign.yaml`, `wiki/`, and the other framework files.

Visual Studio Code opened and trusted that folder. In its PowerShell terminal, the tester prepared the project environment:

```powershell
python -m venv .venv
./.venv/Scripts/Activate.ps1
python -m pip install -r requirements-dev.txt
```

The tester then initialized a local Git repository from Visual Studio Code's Source Control view and created the commit `feat: initial campaign commit`.

## Local model and Chat connection

The tester downloaded the model from the Visual Studio Code terminal:

```powershell
ollama pull qwen3-coder:30b
```

They opened Visual Studio Code's Chat panel with `Ctrl+Alt+I`, opened the model selector, chose the Ollama provider, and selected `qwen3-coder:30b`.

The first request was:

> Help me get started with this campaign notebook. Read AGENTS.md and follow the campaign instructions. Tell me which campaign you are using and whether you can read and save its files. Leave everything unchanged for now.

The request took more than 30 minutes and worked as expected according to the supplied notes. This confirms that the selected local model could be reached through the native Visual Studio Code Chat interface and could use the workspace instructions in this session.

## Skill discovery and campaign initialization

Typing `/ttrpg` displayed the installed project skills automatically. The tester selected:

```text
/ttrpg-campaign-init
```

The assistant asked campaign-configuration questions including the title, game system, genre, tone, usual session length, and premise. Campaign initialization took approximately 45 minutes and worked as expected according to the supplied notes.

The notes do not preserve the proposed `campaign.yaml` diff, the approval exchange, command or edit approvals, or the exact resulting files. This record therefore confirms instruction discovery, automatic skill discovery, and the initialization question flow, but does not independently establish the complete proposal-and-approved-save sequence.

## Result and limits

- Ollama `qwen3-coder:30b` was available through Visual Studio Code's native Chat panel.
- The extension read `AGENTS.md` and automatically exposed the project skills through slash commands.
- `/ttrpg-campaign-init` gathered the expected essential campaign settings.
- The observed response times were more than 30 minutes for the first request and approximately 45 minutes for initialization; no controlled performance benchmark was performed.
- The extension version, hardware, RAM, GPU, effective context, permission prompts, and exact changed files were not recorded.
- PDF ingestion, web access, image generation, player-safe review, note ingestion, session preparation, and the remaining skills were not tested.
- One successful model and application combination does not establish compatibility with every Ollama model, extension version, computer, or later build.
