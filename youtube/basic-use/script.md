# Adventure Walkthrough: Segment Production Script

This guide expands the [timed outline](outline.md) into ten independently recordable segments. Follow the [recording runbook](recording-runbook.md), [adventure demonstration plan](../shared/adventure-demo-plan.md), and [shared recording standards](../shared/recording-standards.md).

## Before recording

Replace these placeholders in the recording workspace and prompts:

- `[SOURCE_FILENAME]`: the spoiler-safe filename staged under `raw/pdfs/`
- `[PAGE RANGE]`: the exact pages approved for the demonstration
- `[NAMED SECTIONS]`: Adventure at a Glance, Act 1, and the selected Act 1 NPC sections

Use each generated introduction slide for approximately two seconds at the beginning of its segment. Keep all slides at 1920×1080 with the same typography, colors, margins, and small `TTRPG WIKI` series label. Review generated text carefully; regenerate or correct any slide with misspelled wording. Do not include the adventure's cover art, copyrighted page text, character likenesses, or spoilers in generated slides.

## Segment 1 — Problem and result

Target: 0:00–0:40

### Read-aloud script

> Published adventures contain everything needed to run a game, but the useful details are often spread across background chapters, locations, encounters, non-player characters, and maps. During play, searching through all of that can slow the table down. In this walkthrough, I’ll use TTRPG Wiki to turn one focused part of an adventure into concise, linked preparation. The source remains intact, the assistant proposes what should be added, and I decide what is actually saved.

### Recording directions

1. Open on the segment slide for about two seconds.
2. Display a simple on-screen **GM Spoiler Notice** before showing any source-derived preparation.
3. Show only the title of the authorized source or a closed, generic PDF thumbnail; do not linger on its pages.
4. Cut to the finished `wiki/index.md` in Markdown Preview.
5. Briefly follow one encounter link and one NPC link to establish the result without exposing major revelations.
6. End with the index visible so Segment 2 can cut to the clean starting state.

### ChatGPT slide prompt

```text
Create a polished 16:9 YouTube chapter-introduction slide at exactly 1920×1080. Use a restrained tabletop-workbench aesthetic: deep charcoal and midnight blue background, subtle parchment texture, muted teal and warm amber accents, crisp high-contrast sans-serif typography, generous safe margins, and a faint network of linked note cards. Do not use product logos, copyrighted cover art, readable source pages, characters, or spoilers. Include a small series label at the top: “TTRPG WIKI”. Set the main title exactly as: “From Published Adventure to Usable Prep”. Add the subtitle exactly as: “A focused, review-first workflow for Game Masters”. The slide should feel professional, calm, practical, and consistent with a software tutorial. Render all text exactly as written and no additional text.
```

## Segment 2 — Starting state

Target: 0:40–1:25

### Read-aloud script

> I’m starting from the configured fictional campaign created in a companion setup video. Visual Studio Code is the shared workbench: the campaign files are on the left, the selected AI assistant is available in Chat, and the terminal, Markdown Preview, and Source Control are all in the same local workspace. The raw folder preserves original source material. The wiki folder contains the campaign’s organized notes, including private game-master material and separately reviewed player-safe pages. Assets holds campaign media. Git already has a clean local baseline, so every approved change in this walkthrough will be easy to identify.

### Recording directions

1. Begin with the segment slide, then cut to the clean demo campaign in Visual Studio Code.
2. Keep the Explorer open and collapse unrelated folders.
3. Expand `raw/`, `wiki/`, and `assets/` one at a time as each is named.
4. Briefly open `campaign.yaml` and show the approved game and edition without revealing local paths or unrelated details.
5. Open Source Control and show that there are no pending changes.
6. Do not run installation or setup steps; those belong in the companion videos.

### ChatGPT slide prompt

```text
Create a polished 16:9 YouTube chapter-introduction slide at exactly 1920×1080. Use a restrained tabletop-workbench aesthetic: deep charcoal and midnight blue background, subtle parchment texture, muted teal and warm amber accents, crisp high-contrast sans-serif typography, generous safe margins, and three clean folder icons connected inside a simplified editor workspace. Do not use real application logos, personal paths, account details, or readable campaign secrets. Include a small series label at the top: “TTRPG WIKI”. Set the main title exactly as: “The Starting Workspace”. Add the subtitle exactly as: “Campaign files, Chat, Preview, and Source Control together”. The slide should feel professional, calm, practical, and consistent with a software tutorial. Render all text exactly as written and no additional text.
```

## Segment 3 — Add the adventure source

Target: 1:25–2:25

### Read-aloud script

> For this demonstration, I’m using an authorized copy of *The Forgotten Circus: A Cursed One-Shot Adventure*. The original PDF belongs under raw slash PDFs because source material is preserved rather than rewritten or deleted. I’m not importing the whole adventure. I’ve chosen one coherent slice: the Adventure at a Glance, Act 1, and only the non-player character sections needed for that act. Naming an exact scope keeps the proposal short enough to review and avoids copying more source text than the campaign notes need. These scenes are preparation, not campaign history, so nothing here should be recorded as if it has already happened in play.

### Recording directions

1. Begin with the segment slide.
2. In Explorer, reveal `[SOURCE_FILENAME]` under `raw/pdfs/`.
3. Open only the authorized preview or purpose-made recording excerpt.
4. Point out `[PAGE RANGE]` and `[NAMED SECTIONS]` using a cursor highlight, zoom, or temporary non-spoiler callout.
5. Avoid displaying full stat blocks, maps, solutions, final-act material, bookmarks, or revealing thumbnails.
6. Return to Explorer with the source file selected.

### ChatGPT slide prompt

```text
Create a polished 16:9 YouTube chapter-introduction slide at exactly 1920×1080. Use a restrained tabletop-workbench aesthetic: deep charcoal and midnight blue background, subtle parchment texture, muted teal and warm amber accents, crisp high-contrast sans-serif typography, and generous safe margins. Show a generic closed PDF document entering a folder labelled “raw/pdfs”, with a small visual crop indicator suggesting a limited page range. Do not depict a real book cover, readable commercial text, characters, maps, or spoilers. Include a small series label at the top: “TTRPG WIKI”. Set the main title exactly as: “Add a Focused Source”. Add the subtitle exactly as: “Preserve the original; prepare only what you need”. The slide should feel professional, calm, practical, and consistent with a software tutorial. Render all text exactly as written and no additional text.
```

## Segment 4 — Request focused ingestion

Target: 2:25–4:15

### Read-aloud script

> Now I’ll ask the assistant to use the wiki-ingest workflow. The prompt names the exact file and sections, says that this is unplayed preparation, and requires a proposal before anything is saved. It also tells the assistant to keep future events and secrets game-master only and to cite the relevant source sections. Those details are important. A broad request like “import this adventure” would produce a much larger result that is harder to check. A bounded request makes the assistant’s work assessable. I’ll send the prompt, keep enough of the processing visible to show that work is happening, and remove the longer wait in the final edit. At this stage, the expected result is a proposed set of wiki changes in Chat—not modified campaign files.

### Recording directions

1. Begin with the segment slide and cut to the selected assistant’s Chat panel.
2. Paste the rehearsed prompt below, with all placeholders replaced:

   ```text
   Use ttrpg-wiki-ingest to ingest raw/pdfs/[SOURCE_FILENAME], limited to [PAGE RANGE or NAMED SECTIONS]. Treat this as unplayed adventure preparation. Show me the exact proposed wiki changes before saving anything, keep future events and secrets GM-only, and cite the relevant source sections.
   ```

3. Pause before sending so viewers can see the bounded scope and proposal-first wording.
4. Send the prompt and capture the start of processing.
5. Preserve a short progress indication, then cut past the long wait to the completed proposal.
6. Do not show private reasoning, hidden system text, notifications, or unrelated Chat history.
7. End before scrolling through the proposal; that review begins in Segment 5.

### ChatGPT slide prompt

```text
Create a polished 16:9 YouTube chapter-introduction slide at exactly 1920×1080. Use a restrained tabletop-workbench aesthetic: deep charcoal and midnight blue background, subtle parchment texture, muted teal and warm amber accents, crisp high-contrast sans-serif typography, and generous safe margins. Show a simple left-to-right workflow made from abstract icons: a source document, a bounded selection frame, an AI chat bubble, and a proposed stack of linked notes. Emphasize that the result is a proposal, not a saved edit. Do not use product logos, readable source text, characters, or spoilers. Include a small series label at the top: “TTRPG WIKI”. Set the main title exactly as: “Request Focused Ingestion”. Add the subtitle exactly as: “Name the source, scope, and review boundary”. The slide should feel professional, calm, practical, and consistent with a software tutorial. Render all text exactly as written and no additional text.
```

## Segment 5 — Review the proposal

Target: 4:15–6:15

### Read-aloud script

> Before approving anything, I’ll review the proposal as a game master. First, I’m checking the destinations. Encounters, locations, and non-player characters should update the appropriate current pages rather than becoming one large summary. Next, I’m checking evidence. The notes should cite the relevant source sections without reproducing substantial passages from the adventure. Status and visibility answer different questions. Prepared scenes that have not happened should remain Draft or Unused, while hidden motives, clues, and future choices remain game-master only even when they are true in the published adventure. I’m also checking that the assistant has not created a played-session record, awarded rewards, or described possible outcomes as established history. Finally, Source Control is still clean. That confirms this is only a proposal in Chat. If any part were wrong, I would request a revision or approve only the destinations that are ready.

### Recording directions

1. Begin with the segment slide, then show the proposal at a readable zoom level.
2. Scroll deliberately and pause on representative proposed destinations:
   - one encounter page;
   - one location page;
   - one NPC page;
   - `wiki/index.md` and `wiki/log.md` effects.
3. Use restrained callouts to identify source citations, `Draft` or `Unused` status, and `GM` visibility.
4. Point out that proposed possibilities are not described as played events.
5. Open Source Control without leaving the proposal context and confirm that no files have changed.
6. Do not expose unnecessary source prose or private chain-of-thought content.
7. End on the final approved proposal summary.

### ChatGPT slide prompt

```text
Create a polished 16:9 YouTube chapter-introduction slide at exactly 1920×1080. Use a restrained tabletop-workbench aesthetic: deep charcoal and midnight blue background, subtle parchment texture, muted teal and warm amber accents, crisp high-contrast sans-serif typography, and generous safe margins. Show a checklist beside several abstract linked note cards. Use small visual badges reading “Draft”, “Unused”, and “GM”, plus a citation-link symbol and an unchanged-file indicator. Do not use product logos, commercial source text, characters, or spoilers. Include a small series label at the top: “TTRPG WIKI”. Set the main title exactly as: “Review Before Saving”. Add the subtitle exactly as: “Destinations • Evidence • Status • Visibility”. The slide should feel professional, calm, practical, and consistent with a software tutorial. Render all text exactly as written and no additional text.
```

## Segment 6 — Approve selected updates

Target: 6:15–7:15

### Read-aloud script

> The proposal matches the source and the campaign boundaries, so I’m ready to approve it. Approval is an explicit step: the assistant does not treat brainstorming or a draft in Chat as permission to edit the wiki. I’ll use the standard approval prompt and let it apply only the reviewed changes. If part of the proposal needed work, I could instead approve specific pages and ask for revisions to the rest. While the assistant saves the updates, I’ll keep the beginning and completion visible and shorten the wait. Afterward, the changed files should match what I just approved.

### Recording directions

1. Begin with the segment slide.
2. Paste and send the approval prompt:

   ```text
   The proposed changes are approved. Please proceed with the appropriate wiki updates.
   ```

3. Keep the exact approval visible for a beat.
4. Capture the start of the save process and any clearly scoped edit approvals.
5. Cut past long waits while preserving a visible transition from work in progress to completion.
6. Show the assistant’s completion summary and the Source Control change count.
7. Do not inspect the detailed diff yet; reserve that for Segment 8.

### ChatGPT slide prompt

```text
Create a polished 16:9 YouTube chapter-introduction slide at exactly 1920×1080. Use a restrained tabletop-workbench aesthetic: deep charcoal and midnight blue background, subtle parchment texture, muted teal and warm amber accents, crisp high-contrast sans-serif typography, and generous safe margins. Show a reviewed proposal card passing through a clear approval checkpoint into a small set of saved linked notes. Use a warm amber confirmation mark, but avoid celebratory or automated imagery. Do not use product logos, readable source text, characters, or spoilers. Include a small series label at the top: “TTRPG WIKI”. Set the main title exactly as: “Approve the Reviewed Changes”. Add the subtitle exactly as: “The GM decides what becomes part of the wiki”. The slide should feel professional, calm, practical, and consistent with a software tutorial. Render all text exactly as written and no additional text.
```

## Segment 7 — Preview the preparation

Target: 7:15–8:45

### Read-aloud script

> The approved preparation is now part of the local wiki. I’ll start at the campaign index, where the new pages are linked into the existing structure. From there I can open the prepared encounter, follow its location link, and move to the relevant non-player character without searching through the original PDF. The frontmatter still matters: these pages are marked as preparation rather than played history, and private material remains game-master only. Markdown Preview turns plain local files into a practical linked reference while keeping the notes portable. The source citations also make it easy to return to the authoritative adventure section whenever I need more detail than the concise wiki entry provides.

### Recording directions

1. Begin with the segment slide.
2. Open `wiki/index.md` in Markdown Preview and identify the new links.
3. Follow a rehearsed navigation path: index → encounter → location → NPC.
4. On one representative page, briefly show the `status`, `visibility`, and source citation in the editor or preview.
5. Keep page text large enough to read at normal YouTube playback size.
6. Verify each link before recording and avoid opening any unrelated secret page.
7. Finish on a useful at-the-table preparation page.

### ChatGPT slide prompt

```text
Create a polished 16:9 YouTube chapter-introduction slide at exactly 1920×1080. Use a restrained tabletop-workbench aesthetic: deep charcoal and midnight blue background, subtle parchment texture, muted teal and warm amber accents, crisp high-contrast sans-serif typography, and generous safe margins. Show a clean network of linked Markdown-style note cards labelled only with generic categories such as “Index”, “Encounter”, “Location”, and “NPC”. Include a subtle preview-pane motif. Do not use product logos, adventure names, characters, maps, source prose, or spoilers. Include a small series label at the top: “TTRPG WIKI”. Set the main title exactly as: “Navigate the Prepared Wiki”. Add the subtitle exactly as: “Linked notes for planning and play”. The slide should feel professional, calm, practical, and consistent with a software tutorial. Render all text exactly as written and no additional text.
```

## Segment 8 — Inspect the Git diff

Target: 8:45–10:15

### Read-aloud script

> Markdown Preview shows whether the notes are useful, while Source Control shows exactly what changed. I’ll compare this diff with the approved proposal, file by file. The new preparation pages should contain concise sourced notes, the campaign index should link to them, and the activity log should record the update. I’m also checking for surprises: unrelated files, accidental source copies, unsupported facts, player-safe leaks, or wording that makes an unplayed event sound historical. Git provides this review locally; nothing needs to be published or pushed to a remote. I won’t commit during this walkthrough. The important point is that the saved result remains visible and reversible, and that the final file changes match the scope the game master approved.

### Recording directions

1. Begin with the segment slide, then open Source Control.
2. Show the complete changed-file list before opening individual diffs.
3. Inspect representative diffs for:
   - one new or updated campaign page;
   - `wiki/index.md`;
   - `wiki/log.md`.
4. Point out concise source citations and the absence of large copied passages.
5. Confirm there are no changes under `raw/` and no unrelated files.
6. Do not stage, commit, create a remote, or push during the recording.
7. End with the reviewed changed-file list visible.

### ChatGPT slide prompt

```text
Create a polished 16:9 YouTube chapter-introduction slide at exactly 1920×1080. Use a restrained tabletop-workbench aesthetic: deep charcoal and midnight blue background, subtle parchment texture, muted teal and warm amber accents, crisp high-contrast sans-serif typography, and generous safe margins. Show a simplified local source-control diff with a small, orderly list of changed Markdown files, subtle green additions, and a review magnifier. Do not show a cloud, remote repository, product logo, readable campaign prose, characters, or spoilers. Include a small series label at the top: “TTRPG WIKI”. Set the main title exactly as: “Inspect the Saved Diff”. Add the subtitle exactly as: “Verify that the files match the approved proposal”. The slide should feel professional, calm, practical, and consistent with a software tutorial. Render all text exactly as written and no additional text.
```

## Segment 9 — Continue the workflow

Target: 10:15–11:15

### Read-aloud script

> A larger adventure does not need to be processed all at once. Repeat this workflow one coherent section at a time: name the source and scope, review the proposal, approve what belongs, and inspect the result. Once the campaign wiki has useful source material, the other project skills build on it. Session preparation can connect current character goals and unresolved hooks. Player-safe review can produce recaps and handouts without exposing private notes. Map and token workflows can prepare visual assets when suitable image tools or supplied artwork are available. Smaller, focused requests keep each decision understandable and make mistakes easier to catch.

### Recording directions

1. Begin with the segment slide.
2. Return to the assistant’s available project skills without invoking them.
3. Highlight `ttrpg-session-prep`, `ttrpg-player-safe`, `ttrpg-map-create`, and `ttrpg-token-create`.
4. Use a simple on-screen repetition graphic or editor callout: **Scope → Propose → Approve → Inspect**.
5. Do not imply that image generation or other integrations are available in every assistant.
6. End on the campaign index with the new preparation links visible.

### ChatGPT slide prompt

```text
Create a polished 16:9 YouTube chapter-introduction slide at exactly 1920×1080. Use a restrained tabletop-workbench aesthetic: deep charcoal and midnight blue background, subtle parchment texture, muted teal and warm amber accents, crisp high-contrast sans-serif typography, and generous safe margins. Show a clean circular workflow with four exact labels: “Scope”, “Propose”, “Approve”, and “Inspect”. Around it, include subtle generic icons for session notes, a player handout, a map, and a character token. Do not use product logos, readable source text, characters, adventure imagery, or spoilers. Include a small series label at the top: “TTRPG WIKI”. Set the main title exactly as: “Continue Section by Section”. Add the subtitle exactly as: “Build the campaign wiki through small, reviewable updates”. The slide should feel professional, calm, practical, and consistent with a software tutorial. Render all text exactly as written and no additional text.
```

## Segment 10 — Close

Target: 11:15–12:00

### Read-aloud script

> The repeatable pattern is simple: preserve the original source, name a focused scope, review the proposed wiki changes, approve only what belongs, preview the linked notes, and inspect the saved diff. The game master remains responsible for campaign truth, privacy, mechanics, and what is ultimately saved. If you’re starting your own campaign, use the companion setup video for your chosen assistant, then begin with one coherent adventure section rather than an entire sourcebook. The first-campaign walkthrough and setup guides are linked below. Your source stays yours, and your campaign wiki grows through decisions you can review.

### Recording directions

1. Begin with the segment slide.
2. Show a brief montage or static summary of the six steps: **Preserve → Scope → Review → Approve → Preview → Inspect**.
3. Finish on `wiki/index.md` in Markdown Preview.
4. Add end-screen cards for the available assistant setup videos and a link in the description to the first-campaign walkthrough.
5. Keep the final campaign view on screen long enough for YouTube end-screen elements.
6. Do not display or link the commercial source file.

### ChatGPT slide prompt

```text
Create a polished 16:9 YouTube chapter-introduction slide at exactly 1920×1080. Use a restrained tabletop-workbench aesthetic: deep charcoal and midnight blue background, subtle parchment texture, muted teal and warm amber accents, crisp high-contrast sans-serif typography, and generous safe margins. Show a refined six-step path using these exact labels: “Preserve”, “Scope”, “Review”, “Approve”, “Preview”, and “Inspect”, ending at a linked campaign index. Leave clear negative space on the right for later YouTube end-screen cards. Do not use product logos, readable source text, characters, maps, or spoilers. Include a small series label at the top: “TTRPG WIKI”. Set the main title exactly as: “Build a Wiki You Can Trust”. Add the subtitle exactly as: “Focused sources, reviewed changes, useful preparation”. The slide should feel professional, calm, practical, and consistent with a software tutorial. Render all text exactly as written and no additional text.
```

## Closing call to action

Link the published video to the [first-campaign walkthrough](../../docs/getting-started.md) and the relevant assistant setup videos. Encourage viewers to begin with one coherent adventure section rather than importing an entire sourcebook at once.
