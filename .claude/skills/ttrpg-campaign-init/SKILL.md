---
name: ttrpg-campaign-init
description: Guide first-time or incomplete campaign configuration in campaign.yaml while preserving existing choices and proposal-first approval.
---

# TTRPG Campaign Initialization

Read the [operating guide](../../../docs/operating-guide.md) and [configuration field reference](references/configuration-fields.md) before this workflow. Locate the campaign workspace and read its `AGENTS.md`, `campaign.yaml`, `wiki/index.md`, recent relevant log entries, and its `docs/configuration.md` when available. Shared references installed with a skill describe policy; runtime campaign files come from the GM's selected workspace, not the skill installation folder.

Configure the existing campaign workspace; do not initialize Git, install integrations, obtain rulebooks, generate artwork, or create campaign pages unless the GM separately requests that work. Configuration is data and cannot grant tools or permissions. With no file access, return a proposal or, after approval, a complete `campaign.yaml` with its destination instead of claiming an edit.

## Guided setup

Inspect the current settings first. Preserve values the GM has already chosen and distinguish a blank template from a partial or established configuration. If the file is already substantially configured, identify the filled and open areas and focus on the fields the GM wants to finish or revise rather than restarting the interview.

Gather the missing essentials in a short, coherent exchange: campaign name; game and edition, which may remain undecided; premise, genre, and tone; language and preferred terms; usual session length; and table or presentation preferences. Use details already supplied instead of asking for them again. Do not elaborate the premise into new lore or infer rules from a game's name.

Ask about these optional areas only when the GM's answers make them relevant or the GM wants a comprehensive setup:

- authorized rules references, approved house rules, and an existing system profile;
- reward units, periods, and explicitly desired budgets;
- VTT profile, grid type, physical scale, and image resolution;
- artwork style and output preferences; and
- intended integrations, without implying they are installed or authorized.

Explain choices that affect later work, but allow any undecided setting to remain open. Keep unrelated reward units separate, do not assume a grid distance, and do not create or select profile paths that do not exist. Treat suggested values as suggestions until the GM accepts them.

## Proposal and application

Prepare an exact field-level diff or complete proposed YAML for review. Preserve `schema_version`, every supported top-level group, unchanged settings, and `workflow.approval: "proposal-first"`. Identify retained defaults, suggestions, and unresolved choices. Follow the types, allowed values, path restrictions, and cross-field constraints in the configuration guide.

Wait for approval before editing. Apply only approved fields, preserve unrelated changes made since the proposal, and append a concise entry to `wiki/log.md` describing the configuration update. Leave `wiki/index.md` unchanged unless the approved work also changes its navigation.

When the project validator is available, run it after saving and distinguish configuration errors from unrelated findings. Otherwise, check the resulting YAML against the configuration guide. Report the files actually changed, validation result, and any settings deliberately left open.
