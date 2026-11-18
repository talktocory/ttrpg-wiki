# What to Expect from Your AI Tool

The campaign notebook uses the same notes and approval process whichever AI tool you choose. The main difference is what the application can do with files on your computer.

Start with the guide for [Codex](codex.md), [Claude Desktop](claude-desktop.md), or [GitHub Copilot](github-copilot.md). You do not need to run the project's tests to prepare a session.

## What can vary?

| What you want to do | What your AI tool needs |
| --- | --- |
| Read and organize notes | Access to the campaign folder, or the relevant files attached to a chat |
| Look up backstory, lore, or storyline details | The relevant campaign pages; a lookup does not require permission to edit files |
| Save approved wiki updates | Permission and tools to edit the folder; otherwise it can return files for you to save |
| Read a PDF | A way to read its text; you can supply the relevant text if needed |
| Create new map or portrait art | An image-generation tool; without one, ask for a description or prompt |
| Crop a supplied portrait into a token | An available image tool, or the optional Python token processor |

Ask the assistant what it can actually do before relying on a feature. It should explain a missing tool and offer a useful next step, rather than claim a file was created or saved.

Codex supports [built-in image generation](https://learn.chatgpt.com/docs/image-generation). When the tool is available, the map and token skills can create or edit actual images from campaign descriptions and optional references. This is separate from the local Python token-export utility. Availability and usage allowances still depend on the session and account; this feature reference does not replace hands-on checks of a finished campaign asset.

## What has been tried so far?

The project has been developed in Codex. The other setup guides follow the providers' documentation, but they still need hands-on testing in those applications.

| Tool | Current testing status |
| --- | --- |
| Codex | Used during development; a fresh installation still needs a separate check |
| Claude Desktop | Setup guides and skill ZIPs prepared; installation and campaign tasks have not yet been tested in the app |
| GitHub Copilot | Setup guides prepared; finding skills and completing campaign tasks have not yet been tested in VS Code or the CLI |

The local file checks and utility tests have passed. They help catch mistakes in the project, but they do not prove that another AI application will follow every instruction or keep every spoiler out of a recap. Review proposed changes and player material yourself.

## If a feature is unavailable

You can still work on a small task using files you attach or text you paste. Ask for a proposed update, approve it, and save the returned files into your campaign folder. For artwork, an art brief or supplied finished image may be enough.

No AI subscription, PDF tool, or image service is included with this project. Your chosen application's features and permissions determine what is available.

<details>
<summary>Technical test record for contributors</summary>

Documentation references were checked on 2026-11-17. Live setup checks remain pending for Claude Desktop Cowork, Claude Desktop Chat, Copilot in VS Code, and Copilot CLI. Do not count one application's results as a test of another.

Local utility checks used Windows, Python 3.13.7, PyYAML 6.0.3, and Pillow 13.0.0. Configuration, links, skill metadata, generated instructions, 15 automated tests, skill ZIP construction, and the template ZIP round trip passed. CI is configured for Ubuntu and Windows on Python 3.11 and 3.13; those hosted jobs have not run as part of the local conversion.

Record the application version, date, task, and observed result when testing. The [contributor evaluation guide](../evaluation.md) has example tasks. Successful file checks alone do not establish working skill discovery or correct assistant behavior.

</details>
