# Set Up Your Campaign in GitHub Copilot

Visual Studio Code is the shared campaign workbench; GitHub Copilot supplies the AI assistant within it.

## Set up GitHub Copilot in Visual Studio Code

Install [Visual Studio Code](https://code.visualstudio.com/), select the Copilot icon and **Use AI Features**, then authenticate with GitHub when prompted. Open the campaign folder in Visual Studio Code and trust the folder if Visual Studio Code asks. See the official [GitHub Copilot setup guide](https://code.visualstudio.com/docs/setup/copilot) for account and plan options.

## Connect the campaign folder

Start a conversation with:

> Help me get started with this campaign notebook. Read AGENTS.md and follow the campaign instructions. Tell me which campaign you are using and whether you can read and save its files. Leave everything unchanged for now.

## GitHub Copilot-specific capabilities

The project supplies Copilot instructions under `.github/copilot-instructions.md` and generated skills under `.github/skills/`. In the validated Visual Studio Code session, `/ttrpg-campaign-init` selected the setup workflow. If a skill is missing, start a fresh conversation or ask Copilot to read the relevant `.agents/skills/<skill-name>/SKILL.md` file.

If Copilot cannot read a PDF directly, it can use the included `scripts/extract_pdf.py` utility for documents with a text layer. Scanned pages still need OCR or supplied extracted text. Image capabilities vary between Copilot surfaces.

## Continue the shared setup

Return to [connect and configure your assistant](../getting-started.md#3-connect-and-configure-your-assistant), then follow the shared walkthrough for importing notes and approving wiki updates.
