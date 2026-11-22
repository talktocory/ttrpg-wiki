# Video Series Brief

## Purpose

Help Game Masters set up TTRPG Wiki in its standard Visual Studio Code workbench and use it safely for real campaign preparation.

## Audience

Game Masters with access to a supported AI assistant in Visual Studio Code. They may be new to Git, Python, Markdown, or repository-based campaign notes.

## Publishing strategy

Produce modular videos that can stand alone in a playlist and can later be combined into a longer chaptered guide without rerecording the demonstrations.

| Video                                             | Target length | Purpose                                                                                                                                            |
| ------------------------------------------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Set up TTRPG Wiki with VS Code and Codex          | 6–8 minutes   | Download the release, create a local Git repository, connect Codex, and initialize the campaign.                                                   |
| Set up TTRPG Wiki with VS Code and GitHub Copilot | 6–8 minutes   | Create the same local workspace, connect Copilot agent mode, verify project skills, and initialize the campaign.                                   |
| Set up TTRPG Wiki with VS Code and Claude Code    | 6–8 minutes   | Create the same local workspace, connect Claude Code, verify project skills, and initialize the campaign.                                          |
| Set up TTRPG Wiki with VS Code and Ollama         | 6–8 minutes   | Create the same local workspace, connect a local Ollama model through Chat, verify project skills, and initialize the campaign.                     |
| Prepare an adventure with TTRPG Wiki              | 10–12 minutes | Use a focused section of *The Forgotten Circus* to demonstrate source ingestion, proposal review, approval, Markdown Preview, and Git diff review. |
| Complete start-to-finish guide                    | 20–30 minutes | Optional later supercut of the applicable setup module and the adventure walkthrough, with transitions and chapter timestamps.                     |

## Shared message

Visual Studio Code is the standard workbench for the series. It keeps the campaign files, AI chat, terminal, Markdown preview, and Source Control together in one local workspace. Codex, Claude Code, GitHub Copilot, and Ollama provide different assistants inside that shared environment.

The selected AI assistant helps organize campaign material, but the GM remains responsible for campaign truth, privacy, mechanics, and what is saved. A proposal in chat is not yet part of the wiki.

## Shared workflow

```text
Download the latest release ZIP
             ↓
Extract it into a local campaign folder
             ↓
Verify Git and the commit identity
             ↓
Initialize Git and commit the blank baseline
             ↓
Connect the chosen coding agent
             ↓
Configure the campaign with GM approval
             ↓
Add a named source under raw/
             ↓
Review the proposed wiki changes
             ↓
Approve selected changes
             ↓
Inspect the Markdown and Git diff
```

## Series boundaries

- Keep tool-specific installation and interface details in the setup videos.
- Keep the core campaign workflow in the adventure video so it remains useful when setup screens change.
- Use chapters in every video, including the shorter setup videos.
- Record tool and application versions in the description and production notes.
- Link each setup video to the shared adventure walkthrough.
- Present a private GitHub remote or another off-device backup as an optional later step, not a prerequisite.

## Git and privacy framing

The default demonstration uses a **local-only Git repository**. Git provides local change history, but it is not an off-device backup. If viewers later add a remote, instruct them to create a new private repository and verify its visibility before pushing campaign files.

Visual Studio Code supplies the Source Control interface but uses the Git installation on the machine. Both setup videos verify `git --version` and the commit author name and email before making the baseline commit.

## Source links

- [TTRPG Wiki first-campaign walkthrough](../../docs/getting-started.md)
- [Latest blank campaign template](https://github.com/talktocory/ttrpg-wiki/releases/latest/download/ttrpg-wiki-template.zip)
- [Codex setup guide](../../docs/platforms/codex.md)
- [GitHub Copilot setup guide](../../docs/platforms/github-copilot.md)
- [Claude Code setup guide](../../docs/platforms/claude-code.md)
- [Ollama setup guide](../../docs/platforms/ollama.md)
- [The Forgotten Circus product page](https://legacy.drivethrurpg.com/product/511168/The-Forgotten-Circus-A-Cursed-OneShot-Adventure)
