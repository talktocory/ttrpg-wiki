# Recording Standards

## Privacy and workspace safety

- Record from a separate local-only demo repository, never a real campaign or the framework-development checkout.
- Hide local usernames and paths, email addresses, notifications, recent-file lists, tokens, and account details.
- Use a non-personal demonstration name and email when showing Git identity commands.
- Do not push or publish during a recording.
- Verify the exact demo path before resetting between takes.

## Source and spoiler safety

- Keep commercial source files out of this repository and public downloads.
- Show the minimum source text needed to understand the workflow.
- Review filenames, thumbnails, bookmarks, Markdown links, image descriptions, and Git history for spoilers.
- Add an on-screen GM spoiler notice where appropriate.

## Visual consistency

- Use the same Visual Studio Code theme, window dimensions, and font sizes across the series.
- Keep Explorer, the agent chat, Markdown Preview, and Source Control legible at normal YouTube playback size.
- Close unrelated tabs and collapse unrelated folders.
- Use consistent callout styling for prompts, approvals, warnings, and expected results.

## Editorial consistency

- Use “Codex IDE extension” and “GitHub Copilot in Visual Studio Code agent mode” in narration.
- Explain that generated wording can vary; demonstrate required behavior rather than a fixed response.
- Remove long waits while preserving enough progress indication that edits do not appear instantaneous.
- Put commands and prompts in the description or linked project documentation when practical.
- Include chapter timestamps in every published video.

## Version record

For each recording, note:

- recording date;
- operating system;
- Visual Studio Code version;
- agent extension/version when available;
- Python version;
- relevant account or plan limitations without exposing account details;
- whether PDF reading and file editing were verified in that exact session.

## Acceptance checks

- The demonstrated agent uses the intended campaign folder.
- The campaign is local-only and fictional.
- `git --version` succeeds in Visual Studio Code's integrated terminal.
- The recording identity is configured without exposing a personal email address.
- The blank template has a clean baseline commit before configuration begins.
- No files change before the proposal is approved.
- Saved changes match the approved proposal.
- `wiki/index.md` and `wiki/log.md` are updated when campaign pages are saved.
- Markdown links work.
- The Git diff is understandable on screen.
- The final edit contains no private information or unintended adventure spoilers.
