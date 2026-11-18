# Set Up Your Campaign in Claude Desktop

You can work with a campaign folder in Cowork, or attach notes to an ordinary chat. Choose whichever is available to you. Neither route requires Python for writing and organizing your campaign.

## If you use Cowork

1. Select your campaign folder in Cowork. It should contain `campaign.yaml` and the `wiki/` folder.
2. Open [Instructions to Give Claude](claude-folder-instructions.md). Copy **the text in the box** into Claude's instructions for that folder. This tells Claude how to handle your notes and wait for approval.
3. Start a conversation with this request:

> Help me get started with this campaign notebook. Read the campaign instructions and settings. Tell me which campaign you are using and whether you can read and save its files. Leave everything unchanged for now.

Check that Claude has the right folder. Then give it one set of notes and ask it to show you proposed updates before saving anything.

## If you use an ordinary chat

1. Paste [the supplied instructions](claude-folder-instructions.md) into the conversation or your project instructions.
2. Attach `AGENTS.md`, `campaign.yaml`, `docs/operating-guide.md`, and `wiki/index.md`, along with the notes and existing pages needed for your task. Start small; you do not need to upload your whole campaign.
3. Ask for help with those files:

> Read these campaign notes and settings. Suggest updates to the session record and relevant NPC pages. Show me the proposed text and where it belongs. Keep ideas for next session separate from what actually happened.

Claude can prepare updated files for you, but a chat using attachments may not be able to save them into your computer's campaign folder. Ask it to say clearly what it has actually done.

## Save the changes you want

Once you have reviewed the proposal, say:

> The proposed changes are approved. Please proceed with the appropriate wiki updates

With folder access, Claude may be able to save the changes directly. Otherwise, ask for complete updated files and their destination names, then save them into your campaign folder. A proposal still sitting in chat has not updated the wiki.

Continue with the [first-campaign walkthrough](../getting-started.md) or [everyday GM guide](../gm-guide.md).

## Do I need to install skills?

You can begin by having Claude read the task instructions supplied with the project. For example, if it can access your folder, ask it to read `.agents/skills/ttrpg-session-prep/SKILL.md` before preparing a session. In a chat, supply that file and any references it needs.

If your download includes prepared skill ZIPs, you can upload and enable them through Claude's custom-skill controls. These give Claude the task instructions; you still need to select the campaign folder or attach your notes. You do not have to build ZIPs yourself to begin.

## If you get stuck

- **Claude cannot see a file:** select the correct folder or attach the file to the chat.
- **It says it saved something, but you cannot find it:** ask for the exact filename and location. If it only returned a download, save that file locally.
- **It cannot make an image:** ask for a useful art brief or work from an image you supply.

These steps cover Cowork and Chat. If you use Claude Code instead, `CLAUDE.md` supplies that mode's project instructions. See [what has been tested](compatibility.md) for the remaining setup checks.

Further help: Claude's official guides to [custom skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude), [skill ZIPs](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills), and [Cowork folder instructions](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork), checked 2026-11-17. Menu names can vary between versions.
