# Set Up Your Campaign in Claude Desktop or Claude Code

Use Cowork with access to the campaign folder, or open the project in Claude Code. Both routes keep the assistant connected to the persistent wiki. Neither requires Python for writing and organizing your campaign.

## Add the campaign skills for Cowork

Cowork uses skills enabled on your Claude account. Manage those skills through Claude.ai or Claude Desktop. Make sure code execution and file creation are enabled for your account or organization, then:

1. Open [Customize > Skills](https://claude.ai/customize/skills). Some accounts may show the newer unified **Plugins** page instead.
2. Click **+**, choose to create or add a skill, and select **Upload a skill**.
3. Upload the ZIP you need from `dist/skills/`, such as `ttrpg-campaign-init.zip` for initial setup.
4. Confirm that the skill appears in your list and is enabled. Repeat for the other campaign workflows you want Claude to discover automatically.

Enabled account skills can be selected with Claude's `+` or `/` controls where available, and Claude may invoke them automatically when the request matches. Installing a skill supplies its workflow; it does not give Claude access to the campaign folder or install external tools.

## If you use Cowork

1. Select your campaign folder in Cowork. It should contain `campaign.yaml` and the `wiki/` folder.
2. Open [Instructions to Give Claude](claude-folder-instructions.md). Copy **the text in the box** into Claude's instructions for that folder. This tells Claude how to handle your notes and wait for approval.
3. Start a conversation with this request:

> Help me get started with this campaign notebook. Read the campaign instructions and settings. Tell me which campaign you are using and whether you can read and save its files. Leave everything unchanged for now.

Check that Claude has the right folder. Before adding notes, ask it to configure the campaign:

> Use ttrpg-campaign-init to help me configure this campaign. Preserve choices already in campaign.yaml, ask about the essential settings first, and show me the exact proposed changes before saving them.

Review the proposal, then approve it when ready:

> The proposed campaign settings are approved. Please update campaign.yaml and record the change in wiki/log.md.

Claude should change only the approved settings and activity log. You can then give it one set of notes and ask it to show proposed wiki updates before saving anything.

If Cowork cannot read and save the selected campaign folder, correct the folder selection or permissions before continuing, or use Claude Code. An attachment-only chat is not a substitute for the persistent wiki workspace.

## If you use Claude Code

The project includes `CLAUDE.md` for its general instructions and generated project-skill mirrors under `.claude/skills/`. Start Claude Code from the campaign folder; it can discover those skills automatically or you can invoke one directly, such as:

> /ttrpg-campaign-init Help me configure this campaign. Preserve existing choices and show the proposed changes before saving them.

Skills enabled on your Claude account may also sync into Claude Code when you sign in with that account. The committed `.claude/skills/` copies provide repository-local discovery without requiring account sync. They are generated from `.agents/skills/`; contributors should edit the canonical source rather than the mirrors.

## Save the changes you want

Once you have reviewed the proposal, say:

> The proposed changes are approved. Please proceed with the appropriate wiki updates.

Claude should save the approved changes directly in the campaign folder and report the files it updated. A proposal still sitting in the conversation has not updated the wiki. If Claude cannot save, correct workspace access before treating the task as complete.

For a more detailed first-note workflow, continue with [bring in one set of notes](../getting-started.md#4-bring-in-one-set-of-notes). For ongoing use, see the [everyday GM guide](../gm-guide.md).

## If you get stuck

- **Claude cannot see the wiki:** select the correct campaign folder and check its permissions. If Cowork still cannot access it, use Claude Code.
- **It says it saved something, but you cannot find it:** ask for the exact filename and location, then verify the file in the campaign folder before continuing.
- **It cannot make an image:** ask for a useful art brief or work from an image you supply.

These steps cover Cowork and Claude Code. See [what has been tested](compatibility.md) for the remaining setup checks.

Further help: Claude's official guides to [custom skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude), [skill ZIPs](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills), [Claude Code skills](https://code.claude.com/docs/en/skills), and [Cowork folder instructions](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork), checked 2026-11-18. Menu names can vary between versions.
