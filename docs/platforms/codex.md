# Set Up Your Campaign in Codex

Start by giving Codex access to your campaign folder. You do not need Python or terminal commands for these steps.

## 1. Open your campaign folder

In Codex, select the folder containing `campaign.yaml` and `wiki/`. If you keep several campaigns, check that you have opened the right one.

Paste this into a new conversation:

> Help me get started with this campaign notebook. Read AGENTS.md and follow the campaign instructions. Tell me which campaign you are using and whether you can read and save its files. Leave everything unchanged for now.

`AGENTS.md` tells Codex how to look after your notes. It should read your campaign settings and explain what it can do before you begin.

## 2. Try one small task

Point Codex to a set of notes, or paste a short note into the conversation. For example:

> Read these session notes. Show me the updates you would make to the campaign, and flag anything you are unsure about. Do not save changes yet.

Review the proposed text. You can ask for changes, reject an idea, or approve only part of the suggestion.

## 3. Save the changes you want

When the proposal is ready, say:

> The proposed changes are approved. Please proceed with the appropriate wiki updates

Codex should save the approved pages, update the contents page and activity log, and tell you which files changed. If it cannot save directly, ask for the updated files to save yourself.

You are ready to continue with the [first-campaign walkthrough](../getting-started.md) or [everyday GM guide](../gm-guide.md).

## Look up details during play

Ask Codex to find the backstory, lore, or storyline detail you need in the campaign. For example:

> Remind me of this NPC's backstory and how it connects to the current storyline. Keep it brief, link the source pages, and tell me if any detail is still a draft.

A question like this is a lookup, not a request to edit the wiki. You only need the approval step if you want to save new or changed material.

## Generate maps and character tokens

Codex supports built-in image generation. When it is available in your session, the map and token skills can use it to generate new artwork directly from your campaign notes. Reference images are optional. See [OpenAI's image-generation guide](https://learn.chatgpt.com/docs/image-generation).

> Use ttrpg-map-create to generate one map image for this encounter from the wiki. Follow our campaign's map settings and show me the image for review.

> Use ttrpg-token-create to generate one character token image from this NPC's wiki description, using our preferred art style.

Ask for revisions after reviewing the result. The project defaults to one image per review round, and image generation counts toward the tool's usage limits. Approve the selected artwork before final wiki links are saved. If the image tool is unavailable, Codex should explain that and offer a brief or a way to use supplied art.

## If you get stuck

- **It cannot find your notes:** ask which folder it is using and point it to the correct file.
- **It does not follow a task's instructions:** try naming the skill, such as `ttrpg-session-prep`. You can also ask it to read `.agents/skills/ttrpg-session-prep/SKILL.md`. Starting a fresh conversation may help if a newly added skill is missing.
- **It cannot read a PDF or create an image:** ask it to explain what is missing. You can supply text or existing artwork, or ask for a description you can use elsewhere.

See [what has been tested](compatibility.md) for known limits. For further setup help, use the official [Codex skill guide](https://learn.chatgpt.com/docs/build-skills) and [project instruction guide](https://learn.chatgpt.com/docs/agent-configuration/agents-md), checked 2026-11-17.
