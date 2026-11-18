# Your First Campaign

Start with a single set of notes. You do not need to fill every folder, learn Python, or write any code.

## 1. Make a private campaign folder

Download and unzip the project, or copy it into a folder named for your campaign. Keep one campaign in each copy. If you prefer GitHub, create a private repository from the template rather than putting campaign notes in a public fork.

Choose the [Codex](platforms/codex.md), [Claude Desktop](platforms/claude-desktop.md), [GitHub Copilot](platforms/github-copilot.md), or [OpenCode v2 with an Ollama model](platforms/opencode-ollama.md) guide to connect your assistant. Some versions can work directly in your folder; others need you to attach the relevant files to a chat.

## 2. Let the assistant get its bearings

Start a new conversation with this request:

> This folder is my campaign notebook. Read AGENTS.md, docs/operating-guide.md, campaign.yaml, and wiki/index.md. Tell me which campaign files you can read and edit. Explain how you will keep my secrets private and show me changes for approval. Do not change anything yet.

If you are attaching files to chat, include those files with your message. The assistant should say when it needs a file or cannot save changes directly.

## 3. Tell it about your game

You can describe your preferences in ordinary language:

> My campaign is called [name]. We play [game and edition], usually for [length of session]. The tone is [your description]. Please propose the campaign settings and explain anything you need me to decide before saving them.

Replace the bracketed text with your own details. Add house rules or rules references if you have them. It is fine to leave maps, reward budgets, and artwork preferences for later. The [settings guide](configuration.md) explains the choices.

The assistant will propose changes to `campaign.yaml`, the settings file. Review them and approve what you want saved. If you have not chosen a game yet, you can still organize fiction and session ideas; mechanics will need checking later.

## 4. Bring in one set of notes

Put a text or Markdown note in `raw/markdown/`, or a PDF in `raw/pdfs/`. You can also paste a short note into chat. Keep the original; the assistant uses it as a source while proposing organized campaign pages.

Try this request, replacing the filename:

> Read raw/markdown/my-session-notes.md. Show me how you would organize it into campaign pages. Separate what happened at the table from ideas for later, flag contradictions, and keep secrets private. Do not save changes yet.

If the assistant needs an explicit skill name, add “Use ttrpg-wiki-ingest.” There is no need to know that name for every request.

## 5. Approve the proposal and apply it to the wiki

This is the step that turns the conversation into lasting campaign notes. The proposal should show the content to be added or changed, where it will go, and any questions. Ask for revisions first if you need them. When you are ready, say:

> The proposed changes are approved. Please proceed with the appropriate wiki updates

That tells the assistant to apply the proposal to the wiki files, rather than leaving it as a suggestion in chat. You can also approve only part of a proposal:

> Save the session summary and NPC updates. Leave the proposed encounter as an idea for now.

After approval, an assistant with folder access should save those changes and update your campaign's contents page and activity log. Check its summary of the files changed. In a chat without folder access, ask for complete updated files and their destinations, then save them locally. The wiki is updated only when the files have actually been saved.

If you use Git, you can then make a separate Git commit to record the saved update in version history. The approval prompt above requests wiki edits; it does not itself request a Git commit or publication. Git remains optional.

Open [the campaign index](../wiki/index.md) to find your new pages.

## 6. Use it for your next session

> Help me prepare our next session from the latest played events and unresolved hooks. Give me flexible scenes and useful NPC reactions. Mark new ideas clearly and show me the plan before saving it.

After the game, bring in what actually happened. Preparing a scene does not make its outcome true. For a player recap, identify which facts the characters learned and review the finished text before sharing it.

Continue with the [GM guide](gm-guide.md). The [fictional example](../examples/relay-station/README.md) shows how original notes, private information, and a player recap differ; it is separate from your campaign.
