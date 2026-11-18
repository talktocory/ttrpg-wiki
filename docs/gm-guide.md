# Using Your Campaign Notebook

This project helps you turn a growing collection of notes into something useful at the table. Ask for the task you need, review the result, and decide what to keep. You remain the authority on your campaign.

## Ask your campaign a question

You can use the wiki as a reference during preparation or in the middle of a session. You do not have to remember which document contains the answer. Ask the assistant to search the campaign and give you the relevant details:

| What you need | Example request |
| --- | --- |
| An NPC's backstory | “Remind me of this character's history, motives, and important relationships.” |
| Lore for a place or object | “What do we know about this place's origins, and which details are still secret?” |
| Storyline context | “Explain how the current situation connects to the earlier storyline.” |
| A quick timeline | “What happened between the party's first visit and the latest session?” |
| Player knowledge | “What has the party actually learned about this mystery? Keep GM-only truths separate.” |
| Unfinished business | “What loose ends need to be dealt with?” |

Add “Keep it brief and link the source pages” when you need a fast answer at the table. The assistant should use established notes, identify drafts or conflicting accounts, and say when a detail is missing. If you want new lore instead, ask for creative suggestions separately so they are not confused with remembered facts.

Questions can draw on private GM notes when the answer is for you. For a recap or text you will share with players, name that audience so only approved revealed information is included.

**A lookup needs no save or approval step.** It should not edit the wiki just because you asked a question. If you want to retain an analysis or develop a missing detail, review the proposed addition and use the approval prompt below.

## The important last step: save what you approve

Brainstorming and proposed edits are still in the conversation until they are saved into the wiki. Once you have reviewed a proposal and want to keep it, use:

> The proposed changes are approved. Please proceed with the appropriate wiki updates

The assistant should apply the approved changes, update the index and activity log, and report which files changed. If only part is approved, name those parts. If it cannot edit local files, it should provide updated files for you to save. You do not need to repeat approval for the same changes once it has been given.

This is how good ideas, answers, and played events become part of your campaign's ongoing reference. A separate Git commit can record saved files in version history if you use Git, but it is not required to use the notebook.

## Everyday requests

You can ask for a small piece of creative help or a question about the whole campaign:

| Prompt | What to look for in the response |
| --- | --- |
| “Create a table of random items for the wizard's chamber” | Items that suit the room and tone, with any new details clearly proposed. Creating the table does not mean the party found or received its contents. |
| “Add a tragic backstory for Princess Darla” | A story that respects her existing notes and relationships. New history remains proposed until you approve it; it is not automatically known to the players. |
| “What loose ends need to be dealt with?” | Unanswered clues, promises, character goals, NPC/faction issues, and unfinished scenes, grounded in current pages. Uncertain conclusions should be identified. |

These are examples of requests, not established details in your campaign. A question about loose ends can be answered without changing any files. If you want to keep the resulting analysis or turn it into preparation, review the proposed destinations and use the approval prompt above.

## Before a session

Ask the assistant to start with the last played session, unresolved hooks, character goals, and relevant NPCs. A request like this gives it a useful focus:

> We have about three hours next session. Review where we stopped and suggest a few flexible scenes. Include likely player choices, clues, NPC reactions, and anything I still need to decide. Keep new ideas separate from established facts.

Once you like the direction, ask for short notes you can use during play. You can request dialogue, random tables, rules reminders, and map or token needs. Not every session needs all of them.

> For the approved plan, give me short sample lines for the NPCs the party could meet. Keep each speaker's knowledge and secrets in mind.

Prepared dialogue and possible outcomes remain ideas until they happen at the table. The assistant should not turn a planned payment, reveal, or faction move into a completed event.

## After a session

Add your original notes to `raw/` or paste them into chat. Ask what should change in the campaign notebook:

> Organize these session notes. Show me the proposed session record, updates to NPCs and locations, confirmed rewards, and open questions. Do not advance plans beyond what we actually played.

Review the proposed updates, then use “The proposed changes are approved. Please proceed with the appropriate wiki updates” when ready. You can approve only selected changes. Once applied, `wiki/index.md` helps you find the pages, while `wiki/log.md` records that the update was made. You do not need to maintain those files by hand when your assistant can edit the folder.

For rewards, ask what was actually received. Promised payments, planned treasure, purchases, and current spending money are different things. The reward skill keeps those distinctions and can compare awards with a budget only if you have chosen one. It does not assume levels, gold, or a particular game economy.

## Make something for the players

Tell the assistant which events and facts are known to the characters:

> Draft a short player recap of the latest session. Use the revealed facts listed here and anything already approved in the player-safe notes. If you are unsure whether a detail is known, leave it out and ask me privately.

Review the result, including titles, image contents, and links. Save approved player text under `wiki/player-safe/` and reviewed images under `assets/player-safe/`. Share those selected files. Do not give players the whole campaign folder.

An NPC's motive can be true without being known to the players. Likewise, a rumor the characters heard can be recorded as a rumor without becoming an objective fact.

## Generate maps and token images

The `ttrpg-map-create` and `ttrpg-token-create` skills can generate actual artwork from your wiki descriptions, edit a selected image, and help prepare the final map or token file. In Codex with built-in image generation available, ask for the image itself; you do not need to stop at a written prompt or supply an existing portrait.

> Use ttrpg-map-create to generate one map image for this encounter from its wiki notes. Use our map settings and established geography, and keep player-visible artwork free of secrets.

> Use ttrpg-token-create to generate one token image for this NPC from their wiki description. Use our preferred art style and token format.

You can attach a sketch, existing portrait, or reference art if you want the image to follow it. After reviewing the result, ask for a particular revision, such as a clearer doorway or a different expression. The default is one generated image per review round, with no automatic extra alternatives or retries. Image generation uses your tool's allowance; switching to a paid alternative requires your approval.

Once you approve the image, have the assistant check its actual dimensions and format and propose the final wiki links. Keep image files in `assets/vtt/`; descriptions, sources, export settings, approval, and hidden details belong on the relevant campaign page. Use a separate linked note only for substantial detail. Artwork approval does not make a new visual detail campaign canon.

The local Python token script is an optional way to crop or frame supplied art; it is not what generates the new illustration. If your AI tool has no image-generation capability, the skills can still prepare a description, prompt, and export requirements or process artwork you supply. The assistant should say which of these it actually produced.

## Understand the page labels

| Label | What it means in play |
| --- | --- |
| Canon | Established at the table or explicitly accepted by you as true |
| Draft | An idea still being developed or checked |
| Unused | Prepared material that has not entered play |
| Retired | Material you no longer use or that has been superseded |

A separate label says whether a page is private to the GM or reviewed for players. The assistant handles these labels when proposing pages. “Canon” by itself never means “safe to share.”

## Find your way around

Start at [the campaign index](../wiki/index.md). Your private notes are grouped under `wiki/gm/`: sessions, session planning, characters, NPCs, places, scenes, lore, factions, rules, items, and rewards. Templates are starting points, not forms you must fill completely.

The `.md` files are ordinary text with simple formatting and links. You may edit them yourself. Keep original source notes in `raw/`; use the organized wiki pages for the current version of your campaign. The assistant should propose how to resolve conflicting notes rather than quietly choosing an answer.

## Common questions

**Do I need Python or coding experience?** No, not for normal writing and organization. The [optional tools reference](scripts.md) explains the checks and image utility if you want them. Most of the other scripts are for people maintaining the project itself.

**Do I need to edit the settings file myself?** No. Describe your game and preferences, ask for proposed settings, and review them before saving. See [campaign settings](configuration.md).

**What are AGENTS.md and CLAUDE.md telling the assistant to do?** They tell it to find your campaign folder, read the wiki's rules and game settings, and follow the instructions for the task. A skill may be installed elsewhere on your computer; its installation folder is not where your campaign notes belong. If the assistant only has files you attach to chat, it should return proposed edits and, after approval, updated files for you to save. It must not claim to have edited your computer's files when it cannot access them. You do not need to move your campaign into the skill folder.

**What if the assistant cannot see a file?** Attach the relevant file or select the correct campaign folder in your AI tool. Ask it to say which sources it actually read. A chat with attached files may return updated files for you to save rather than editing your computer directly.

**What if the assistant invents a rule or campaign fact?** Ask for its source. Keep unsupported fiction as Draft and rules as Unverified until you decide or provide the correct reference. No game system's mechanics are assumed by default.

**How do I back up my campaign?** Keep a separate private copy of the whole campaign folder, especially before large reorganizations or project updates. Git is optional if you already use it. When updating the project, preserve your settings, notes, original sources, images, and history; do not replace them with blank template files.

## If you want to name a skill

Use these names when your assistant needs a more explicit instruction. A skill is a saved set of instructions for a type of task, not a separate application you must run.

| Task | Skill name |
| --- | --- |
| Organize source or session notes | `ttrpg-wiki-ingest` |
| Check and tidy the notebook | `ttrpg-wiki-maintenance` |
| Prepare a session | `ttrpg-session-prep` |
| Write or review player material | `ttrpg-player-safe` |
| Prepare NPC dialogue for a chosen plan | `ttrpg-npc-dialogue` |
| Check confirmed awards | `ttrpg-reward-ledger` |
| Prepare a map | `ttrpg-map-create` |
| Prepare a character token | `ttrpg-token-create` |
