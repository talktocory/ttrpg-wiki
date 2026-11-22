# Set Up Your Campaign in Codex

## Install Codex for Visual Studio Code

Install [Visual Studio Code](https://code.visualstudio.com/) and the [OpenAI Codex extension](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt), then authenticate for each when prompted. Open the campaign folder in Visual Studio Code and trust the folder if Visual Studio Code asks.
## Connect the campaign folder

In Codex, select the folder containing `campaign.yaml` and `wiki/`. If you keep several campaigns, check that you opened the right one.

Start a conversation with:

> Help me get started with this campaign notebook. Read AGENTS.md and follow the campaign instructions. Tell me which campaign you are using and whether you can read and save its files. Leave everything unchanged for now.

`AGENTS.md` supplies the project instructions, and Codex can discover the task workflows under `.agents/skills/`. In the validated Visual Studio Code extension, typing `@` exposed the available skills, so `@ttrpg-campaign-init` selected the setup workflow. This is a surface-specific composer convention, not a claim that `@` replaces slash commands everywhere. If the menu or prefix changes, name the skill in plain language, such as `Use ttrpg-session-prep for this campaign task.`

## Codex-specific capabilities

Codex supports built-in image generation when that tool is available in the session. The map and token skills can use it to create or edit artwork from campaign notes and optional reference images. Image generation has account and usage limits; see [OpenAI's image-generation guide](https://learn.chatgpt.com/docs/image-generation).

If Codex cannot read a PDF directly, it can use the included `scripts/extract_pdf.py` utility for documents with a text layer. Scanned pages still need OCR or supplied extracted text. If Codex cannot create an image, provide existing artwork or request a reusable brief.

## Continue the shared setup

Return to [connect and configure your assistant](../getting-started.md#3-connect-and-configure-your-assistant), then follow the shared walkthrough for importing notes and approving wiki updates.

If Codex cannot find the campaign, confirm which folder it is using. If a newly added skill is missing, start a fresh conversation or ask it to read the relevant `.agents/skills/<skill-name>/SKILL.md` file.

See [what has been tested](compatibility.md) for known limits. For further help, use the official [Codex skill guide](https://learn.chatgpt.com/docs/build-skills) and [project instruction guide](https://learn.chatgpt.com/docs/agent-configuration/agents-md), checked 2026-11-21.
