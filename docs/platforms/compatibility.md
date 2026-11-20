# What to Expect from Your AI Tool

The campaign notebook uses the same notes and approval process whichever AI tool you choose. The main difference is what the application can do with files on your computer.

Start with the guide for [Codex](codex.md), [Claude Desktop or Claude Code](claude-desktop.md), [GitHub Copilot](github-copilot.md), or [OpenCode v2 with an Ollama model](opencode-ollama.md). You do not need to run the contributor test suite to prepare a session. For the complete local workflow, install Python 3.11 or newer and `requirements-dev.txt` using the [Python setup instructions](../scripts.md#set-up-the-local-python-environment).

## How tools can vary

| What you want to do | What your AI tool needs |
| --- | --- |
| Read and organize notes | Persistent access to the campaign folder or repository |
| Look up backstory, lore, or storyline details | The relevant campaign pages; a lookup does not require permission to edit files |
| Save approved wiki updates | Permission and tools to edit the campaign workspace |
| Read a PDF | A way to read its text; you can supply the relevant text if needed |
| Create new map or portrait art | An image-generation tool; without one, ask for a description or prompt |
| Crop a supplied portrait into a token | An available image tool, or the optional Python token processor |
| Run the included validation and image utilities | Python 3.11 or newer with `requirements-dev.txt` installed |

Ask the assistant what it can actually do before relying on a feature. It should explain a missing tool and offer a useful next step, rather than claim a file was created or saved.

Codex supports [built-in image generation](https://learn.chatgpt.com/docs/image-generation). When the tool is available, the map and token skills can create or edit actual images from campaign descriptions and optional references. This is separate from the local Python token-export utility. Availability and usage allowances still depend on the session and account; this feature reference does not replace hands-on checks of a finished campaign asset.

## Current verification status

The project has been developed in Codex, and a campaign workflow has now been exercised in GitHub Copilot for Visual Studio Code. Other hosts and Copilot surfaces still need their own hands-on testing.

| Tool | Current testing status |
| --- | --- |
| Codex | Used during development; a fresh installation still needs a separate check |
| Claude Desktop | Setup guides and skill ZIPs prepared; installation and campaign tasks have not yet been tested in the app |
| Claude Code | `CLAUDE.md` and generated `.claude/skills/` project mirrors prepared; skill discovery and campaign tasks have not yet been tested in the app |
| GitHub Copilot | Visual Studio Code manually validated on 2026-11-19: automatic project-skill discovery, campaign initialization, PDF-source ingestion, session preparation, proposal approval, saved updates, and locally drawn map creation worked; exact VS Code and Copilot versions were not recorded. CLI and cloud agent remain untested |
| OpenCode v2 with Ollama | Native `AGENTS.md` and `.agents/skills/` discovery plus an Ollama-default configuration checked against current documentation; installation and campaign tasks have not yet been tested in the app |

The local file checks and utility tests have passed. They help catch mistakes in the project, but they do not prove that another AI application will follow every instruction or keep every spoiler out of a recap. Review proposed changes and player material yourself.

## When a feature is unavailable

Persistent workspace access is required for the supported wiki workflow. If the assistant cannot read and save the campaign folder or repository, correct its configuration or choose another supported tool before relying on it for campaign updates.

Optional capabilities can still have useful fallbacks. If PDF reading is unavailable, provide authorized extracted text. If image generation is unavailable, request an art brief or work from a supplied finished image.

No AI subscription, PDF tool, or image service is included with this project. Your chosen application's features and permissions determine what is available.

<details>
<summary>Technical test record for contributors</summary>

Documentation references were checked on 2026-11-18. GitHub Copilot in Visual Studio Code was manually exercised on Windows 11 Enterprise on 2026-11-19 with Python 3.14.7 and no additional VS Code extensions installed for the test. The project skills were discovered automatically, and minimal slash-command prompts were sufficient. PowerShell and Python were used extensively, command approvals were requested, and the locally drawn vector-map workflow took approximately 14 minutes. See the [complete validation record](../validation/github-copilot-vscode-2026-11-19.md).

Live setup checks remain pending for Claude Desktop Cowork, Claude Code, Copilot CLI, Copilot cloud agent, and OpenCode v2 with Ollama. Do not count one application's results as a test of another. The missing exact Visual Studio Code and Copilot versions prevent a build-specific compatibility claim.

The OpenCode project configuration is parsed by the local test suite, and release validation checks its default Ollama model, approval safeguards, and enabled optional web and image integrations. These are structural checks, not evidence that a particular local model followed the campaign workflow correctly.

Local utility checks used Windows, Python 3.13.7, PyYAML 6.0.3, and Pillow 13.0.0. Configuration, links, skill metadata, generated instructions and host skill mirrors, 19 automated tests, skill ZIP construction, and the template ZIP round trip passed. CI is configured for Ubuntu and Windows on Python 3.11 and 3.13; those hosted jobs have not run as part of the local conversion.

Record the application version, date, task, and observed result when testing. The [contributor evaluation guide](../evaluation.md) has example tasks. Successful file checks alone do not establish working skill discovery or correct assistant behavior.

</details>
