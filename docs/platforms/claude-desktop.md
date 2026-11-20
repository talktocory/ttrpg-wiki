# Set Up Your Campaign in Claude Desktop or Claude Code

Use Cowork with access to the campaign folder, or open the project in Claude Code. Both routes keep the assistant connected to the persistent wiki. Neither requires Python for writing and organizing your campaign.

## Add the campaign skills for Cowork

Cowork uses skills enabled on your Claude account. Manage those skills through Claude.ai or Claude Desktop. Make sure code execution and file creation are enabled for your account or organization, then:

1. Open [Customize > Skills](https://claude.ai/customize/skills). Some accounts may show the newer unified **Plugins** page instead.
2. Click **+**, choose to create or add a skill, and select **Upload a skill**.
3. Upload the ZIP you need from `dist/skills/`, such as `ttrpg-campaign-init.zip` for initial setup.
4. Confirm that the skill appears in your list and is enabled. Repeat for the other campaign workflows you want Claude to discover automatically.

Enabled account skills can be selected with Claude's `+` or `/` controls where available, and Claude may invoke them automatically when the request matches. Installing a skill supplies its workflow; it does not give Claude access to the campaign folder or install external tools.

## Connect Cowork

1. Select your campaign folder in Cowork. It should contain `campaign.yaml` and the `wiki/` folder.
2. Open [Instructions to Give Claude](claude-folder-instructions.md). Copy **the text in the box** into Claude's instructions for that folder. This tells Claude how to handle your notes and wait for approval.
3. Confirm access without changing anything:

> Help me get started with this campaign notebook. Read the campaign instructions and settings. Tell me which campaign you are using and whether you can read and save its files. Leave everything unchanged for now.

If Cowork cannot read and save the selected campaign folder, correct the folder selection or permissions before continuing, or use Claude Code. An attachment-only chat is not a substitute for the persistent wiki workspace.

## Connect Claude Code

Start Claude Code from the campaign folder. The project includes `CLAUDE.md` for its instructions and generated skill mirrors under `.claude/skills/`. Claude Code can discover those skills automatically or you can invoke one directly, such as `/ttrpg-campaign-init`.

Skills enabled on your Claude account may also sync into Claude Code. The committed `.claude/skills/` copies provide repository-local discovery without requiring account sync. Contributors should edit the canonical `.agents/skills/` sources rather than the generated mirrors.

## Continue the shared setup

Return to [connect and configure your assistant](../getting-started.md#3-connect-and-configure-your-assistant), then follow the shared walkthrough for importing notes and approving wiki updates.

## If you get stuck

- **Claude cannot see the wiki:** select the correct campaign folder and check its permissions. If Cowork still cannot access it, use Claude Code.
- **A skill is missing:** confirm that the account skill is enabled in Cowork or that the repository skill exists under `.claude/skills/` in Claude Code.
- **It cannot make an image:** ask for a useful art brief or work from an image you supply.

These steps cover Cowork and Claude Code. See [what has been tested](compatibility.md) for the remaining setup checks.

Further help: Claude's official guides to [custom skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude), [skill ZIPs](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills), [Claude Code skills](https://code.claude.com/docs/en/skills), and [Cowork folder instructions](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork), checked 2026-11-18. Menu names can vary between versions.
