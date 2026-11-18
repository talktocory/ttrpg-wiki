# Set Up Your Campaign in GitHub Copilot

This guide is for using Copilot with a campaign folder on your computer, particularly in Visual Studio Code's agent mode. If you already use Copilot CLI, you can use the same project instructions there. Python is not needed for campaign writing.

## 1. Open your campaign folder

Open the folder containing `campaign.yaml` and `wiki/` in your Copilot tool. Make sure project instructions are enabled; the supplied `.github/copilot-instructions.md` tells Copilot how to look after your notes.

Start a conversation with:

> Help me get started with this campaign notebook. Read AGENTS.md and follow the campaign instructions. Tell me which campaign you are using and whether you can read and save its files. Leave everything unchanged for now.

Copilot should identify the right campaign and explain what it can do. If your version shows which instruction files it used, look for `.github/copilot-instructions.md`.

## 2. Try one small task

Give Copilot a set of notes or point it to the file you want it to read:

> Read these session notes. Show me the updates you would make to the campaign. Separate confirmed events from ideas for later, and do not save anything yet.

Review its suggestion and ask for revisions as needed. If it needs a skill named explicitly, add “Use ttrpg-wiki-ingest,” or ask it to read `.agents/skills/ttrpg-wiki-ingest/SKILL.md` and the references linked there.

## 3. Save the changes you want

When the proposal is ready, say:

> The proposed changes are approved. Please proceed with the appropriate wiki updates

Copilot should save the approved changes and tell you which files it updated. If it can only suggest text, ask for complete updated files and save them yourself. Check that the campaign index and activity log are updated too.

Continue with the [first-campaign walkthrough](../getting-started.md) or [everyday GM guide](../gm-guide.md).

## If you get stuck

- **Copilot cannot find a note:** ask which folder it is using, then point it to the correct file.
- **It overlooks the campaign instructions:** ask it to read `AGENTS.md` and the relevant skill before continuing.
- **You are using a cloud session:** check which files it can access. It will not automatically see the campaign folder on your computer.

Other Copilot versions may need different setup. See [what has been tested](compatibility.md). For technical help, use the official [skill guide](https://docs.github.com/en/copilot/concepts/customizations/agent-skills) and [project instruction guide](https://docs.github.com/en/copilot/reference/custom-instructions-support), checked 2026-11-17.
