# Set Up Your Campaign in Claude Code

Visual Studio Code is the shared campaign workbench; the Claude Code extension supplies the AI assistant within it.

## Install Claude Code for Visual Studio Code

Install [Visual Studio Code](https://code.visualstudio.com/) and the [Claude Code extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code), then sign in with your Anthropic account when prompted. Open the campaign folder in Visual Studio Code and trust the folder if Visual Studio Code asks. See the official [Claude Code for VS Code guide](https://code.claude.com/docs/en/vs-code) for account and installation options.

## Connect the campaign folder

Start a conversation with:

> Help me get started with this campaign notebook. Read CLAUDE.md and follow the campaign instructions. Tell me which campaign you are using and whether you can read and save its files. Leave everything unchanged for now.

## Claude Code-specific capabilities

The project supplies instructions in `CLAUDE.md` and generated skills under `.claude/skills/`. Claude Code can discover the project skills automatically or invoke one directly, such as `/ttrpg-campaign-init`. If a skill is missing, start a fresh conversation or ask Claude to read the relevant `.agents/skills/<skill-name>/SKILL.md` file.

Claude Code can attach PDFs in the Visual Studio Code panel, and the included `scripts/extract_pdf.py` utility provides local extraction for documents with a text layer. Scanned pages still need OCR or supplied extracted text. If image generation is unavailable, provide existing artwork or request a reusable brief.

## Continue the shared setup

Return to [connect and configure your assistant](../getting-started.md#3-connect-and-configure-your-assistant), then follow the shared walkthrough for importing notes and approving wiki updates.
