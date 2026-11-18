# Set Up Your Campaign in GitHub Copilot

This guide covers Copilot in Visual Studio Code agent mode, Copilot CLI, and repository-backed cloud sessions. Python is not needed for campaign writing.

## 1. Open your campaign folder

Open the folder containing `campaign.yaml` and `wiki/` in your Copilot tool. The repository includes general instructions in `.github/copilot-instructions.md` and generated project skills under `.github/skills/`.

Start a conversation with:

> Help me get started with this campaign notebook. Read AGENTS.md and follow the campaign instructions. Tell me which campaign you are using and whether you can read and save its files. Leave everything unchanged for now.

Copilot should identify the right campaign and explain what it can do. If your version shows which instruction files and skills it used, look for `.github/copilot-instructions.md` and the `ttrpg-*` skills.

## 2. Check the skills and configure the campaign

Copilot can load a matching skill automatically or expose it as a slash command. In Visual Studio Code, run **Chat: Open Customizations** from the Command Palette and open **Skills** to inspect the workspace skills. In Copilot CLI, use `/skills list`; after changing skill files during a session, use `/skills reload`, followed by `/skills info ttrpg-campaign-init` to inspect the result.

Before adding notes, invoke the campaign setup skill:

> /ttrpg-campaign-init Help me configure this campaign. Preserve choices already in campaign.yaml, ask about the essential settings first, and show me the exact proposed changes before saving them.

Review the proposal and leave any undecided settings open. When it is ready, say:

> The proposed campaign settings are approved. Please update campaign.yaml and record the change in wiki/log.md.

Copilot should change only the approved settings and activity log. If the skill does not appear, start a fresh session and check that `.github/skills/ttrpg-campaign-init/SKILL.md` is present. Asking Copilot to read the canonical `.agents/skills/ttrpg-campaign-init/SKILL.md` and its linked reference remains a fallback when native discovery is unavailable.

## 3. Try one small task

Give Copilot a set of notes or point it to the file you want it to read:

> Read these session notes. Show me the updates you would make to the campaign. Separate confirmed events from ideas for later, and do not save anything yet.

Review its suggestion and ask for revisions as needed. To invoke the ingest workflow explicitly, begin the request with `/ttrpg-wiki-ingest`.

## 4. Save the changes you want

When the proposal is ready, say:

> The proposed changes are approved. Please proceed with the appropriate wiki updates.

Copilot should save the approved changes and tell you which files it updated. If it can only suggest text, ask for complete updated files and save them yourself. Check that the campaign index and activity log are updated too.

For a more detailed first-note workflow, continue with [bring in one set of notes](../getting-started.md#3-bring-in-one-set-of-notes). For ongoing use, see the [everyday GM guide](../gm-guide.md).

## Personal skills are optional

The committed `.github/skills/` directory shares these workflows with everyone using this campaign repository. If you want a separate personal skill available across repositories, Copilot also supports `~/.copilot/skills/<skill-name>/SKILL.md`. Do not copy the campaign skills there merely to use this project; the repository versions are already discoverable and stay aligned with the framework.

## If you get stuck

- **Copilot cannot find a note:** ask which folder it is using, then point it to the correct file.
- **A skill is missing:** start a fresh session, inspect `.github/skills/`, and use VS Code's Skills view or the CLI `/skills` commands to confirm discovery.
- **It overlooks the campaign instructions:** ask it to read `AGENTS.md` and the relevant skill before continuing.
- **You are using a cloud session:** check which files it can access. It will not automatically see the campaign folder on your computer.

Other Copilot versions may need different setup. See [what has been tested](compatibility.md). For technical help, use the official guides for [Agent Skills in VS Code](https://code.visualstudio.com/docs/agent-customization/agent-skills), [Copilot repository and cloud-agent skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills), [Copilot CLI skills](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills), and [project instructions](https://docs.github.com/en/copilot/reference/custom-instructions-support), checked 2026-11-18.
