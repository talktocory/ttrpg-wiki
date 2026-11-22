# Changelog

## Unreleased

- Added `ttrpg-campaign-init` for guided, proposal-first setup of `campaign.yaml` and updated the first-campaign and platform onboarding documentation to use it.
- Retained optional deterministic skill ZIP generation while making all `dist/` artifacts uncommitted build output; removed committed skill archives and their CI freshness check after upload-based hosts left the supported workflow.
- Added generated `.claude/skills/` project mirrors for native Claude Code discovery and documented the Claude Code Visual Studio Code extension workflow.
- Added generated `.github/skills/` project mirrors and native discovery guidance for GitHub Copilot in VS Code, Copilot CLI, and cloud agent.
- Documented the successful 2026-11-19 GitHub Copilot in Visual Studio Code validation, made Python plus the project requirements the baseline for the complete local workflow, and shortened usage examples to the minimal prompts the skills handled successfully.
- Documented the successful 2026-11-21 fresh Codex installation and campaign workflow in Visual Studio Code, including `@`-menu skill selection, PDF ingestion, temporary-file cleanup, and built-in map generation; clarified release extraction, optional Git initialization, and portable skill invocation.
- Added pinned pypdf support and a tested local PDF text-extraction utility with page selection, page markers, layout mode, OCR warnings, and overwrite protection.
- Normalized UTF-8 text line endings inside generated skill packages so committed ZIPs reproduce identically on Windows and Linux.
- Replaced the Claude Desktop and Cowork setup with a concise Claude Code Visual Studio Code extension guide and removed the generated folder-instructions artifact.

## 0.2.0 - 2026-11-18

- Adopted the project name TTRPG Wiki and renamed the template archive and its top-level folder to match.
- Added OpenCode v2 with Ollama as a documented local-model platform, including native skill discovery, guarded web and image integrations, release validation, and a manual acceptance scenario.
- Made campaign configuration easier to find with an example and field guide, emphasized generating map/token artwork, and documented fast, source-linked campaign lookups as a primary use of the wiki.
- Simplified the AI-tool setup guides and testing notes, and gave Claude Desktop a clearly marked copy box containing campaign instructions without developer commands.
- Added the approve-and-apply prompt and everyday GM requests, strengthened the explanation of lasting campaign notes, credited Karpathy's LLM Wiki approach, and clarified how assistants find the campaign folder and return updates when they cannot edit it directly.
- Reworked the documentation for GMs: added an everyday campaign guide and copyable prompts, simplified setup and settings explanations, and moved contributor tooling out of the main reading path while retaining its detailed reference.
- Simplified VTT organization: image files stay in assets; briefs, provenance, export settings, approval, and reveal restrictions live on the relevant campaign pages. Removed parallel VTT-note placeholders and retained optional standalone notes for substantial detail.

## 0.1.0 - 2026-11-17

- Replaced campaign content with an empty, system-neutral template.
- Added eight portable skills, optional profiles, provider guides, and skill packages.
- Separated content status from visibility and retained proposal-first editing.
- Added validation, synthetic scenarios, deterministic token export, and a clean-release manifest.

This template starts a new activity history. Previous campaign content and history are not distributed.
