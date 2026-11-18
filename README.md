# TTRPG Wiki

Spend more time preparing the next game and less time piecing together what happened in the last six.

Turn session notes and chat ideas into a private campaign notebook you can question during play. Your AI assistant helps organize, link, and update the pages. You review the proposals and decide what becomes part of your campaign—so useful work survives beyond the conversation.

```mermaid
flowchart LR
    accTitle: Campaign wiki workflow
    accDescr: Add files to raw or develop an idea in chat, ask the agent to ingest the material, review the proposed wiki changes, and approve them before the agent applies the updates.
    files["Add files to raw/"] --> ingest["Ask the agent to ingest<br/>the files or chat history"]
    chat["Develop an idea<br/>live in chat"] --> ingest
    ingest --> review["Review the proposed<br/>wiki changes"]
    review -->|Approve the changes| apply["Agent applies<br/>the wiki updates"]
    review -->|Request revisions| ingest
```

Use any TTRPG system. **No coding or Python is needed for everyday campaign work.** You need access to your chosen AI tool; available features vary. See [setup and testing notes](docs/platforms/compatibility.md).

## What you can ask

| Task | Example prompt |
| --- | --- |
| Look up backstory, lore, or a storyline | “Remind me of this NPC's history and its connection to the current story. Link the source notes.” |
| Find unfinished business | “What loose ends need to be dealt with?” |
| Prepare a session | “Prepare our next session from the last played events and unresolved character goals.” |
| Make a random table | “Create a table of random items for the wizard's chamber” |
| Develop a character | “Add a tragic backstory for Princess Darla” |
| Write a player recap | “Summarize what the characters learned, keeping GM secrets out.” |
| Check rewards | “What did the group actually receive? Flag uncertain amounts.” |
| Generate a map image | “Use ttrpg-map-create to generate one map image from this encounter's notes.” |
| Generate a token image | “Use ttrpg-token-create to generate one token image from this NPC's description.” |

**Campaign lookups are read-only:** ask for source links and uncertain details. No approval is needed unless you want to save new or changed material.

**Maps and tokens can be generated as actual images.** In Codex with image generation available, the two image skills use that tool directly. Reference art is optional, and the default is one image per review round. See [image creation](docs/gm-guide.md#generate-maps-and-token-images) for review and export details.

A **skill** is a prepared set of task instructions. You can usually ask in ordinary language; the [GM guide](docs/gm-guide.md) lists skill names when you need them.

## Start your campaign

1. Download or copy the project into a **private folder for one campaign**. A private GitHub repository is optional.
2. Follow the setup guide for [Codex](docs/platforms/codex.md), [Claude Desktop](docs/platforms/claude-desktop.md), or [GitHub Copilot](docs/platforms/github-copilot.md).
3. Tell the assistant your game, edition, campaign name, and preferences. Ask it to propose your [campaign settings](docs/configuration.md).
4. Add notes to `raw/` or develop an idea in chat. Ask the assistant to ingest that material and propose wiki updates.
5. Review the proposed changes and request revisions. When ready, approve the parts you want saved:

> The proposed changes are approved. Please proceed with the appropriate wiki updates

The assistant should save the approved pages, update the campaign index and activity log, and report what changed. If it cannot edit your folder, save the updated files it provides. A proposal left in chat has not updated the wiki. A Git commit is a separate, optional record of saved changes.

For a guided first task, follow the [first-campaign walkthrough](docs/getting-started.md).

## Where things go

| Folder | Contents |
| --- | --- |
| `raw/` | Original notes and reference documents, preserved during normal use |
| `wiki/gm/` | Private campaign knowledge, session plans, NPCs, places, and rules reminders |
| `wiki/player-safe/` | Reviewed recaps, handouts, and revealed lore |
| `assets/vtt/` | Map and token files; their notes belong on the relevant campaign pages |
| `assets/player-safe/` | Images reviewed for sharing with players |

Start at [wiki/index.md](wiki/index.md) to browse your campaign. Pages are ordinary Markdown text files; use any text editor. Obsidian is optional.

## Keep control of your campaign

New ideas stay separate from established facts. Preparing a scene, reward, or reveal does not mean it happened in play.

Keep the campaign folder private and share only selected, reviewed player files. A “player-safe” folder helps organize those files; it does not prevent access to the rest of the project. Check text, images, and links before sharing.

## More help

- [GM guide](docs/gm-guide.md): everyday requests, session routines, and common questions.
- [Optional tools](docs/scripts.md): Python utilities for checks, token processing, and project maintenance.
- [Sharing text and artwork](docs/provenance.md): sources, permissions, and attribution.
- [Contributing](CONTRIBUTING.md): instructions for people changing the project itself.

This project adapts [Andrej Karpathy's LLM Wiki approach](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) for campaign preparation, GM review, and spoiler protection. The framework and original examples use the [MIT License](LICENSE); imported rules, adventures, and artwork retain their own terms.
