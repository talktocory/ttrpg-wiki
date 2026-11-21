# VS Code and Codex Setup: Recording Runbook

Follow [the shared recording standards](../shared/recording-standards.md).

## Prepared inputs

- Git installed, or the official Git installer ready for the missing-Git branch
- A non-personal demonstration commit identity that is safe to display
- The latest `ttrpg-wiki-template.zip` release downloaded but not yet extracted
- An empty local parent folder where the fictional campaign folder will be created
- A fictional campaign name, premise, genre, tone, game, and edition
- Python 3.11 or newer
- Visual Studio Code with the Codex IDE extension available and authenticated

## Git prerequisite checks

Run these in Visual Studio Code's integrated terminal before downloading or extracting the campaign template:

```powershell
git --version
git config --global --get user.name
git config --global --get user.email
```

If Git is missing, install it from the official Git site, restart Visual Studio Code, and rerun `git --version`. If either identity value is empty, demonstrate the configuration pattern from the script using the viewer's chosen attribution values. Do not display a personal recording email.

## Workspace confirmation prompt

> Help me get started with this campaign notebook. Read AGENTS.md and follow the campaign instructions. Tell me which campaign you are using and whether you can read and save its files. Leave everything unchanged for now.

## Git baseline

After extraction, open the folder that directly contains `campaign.yaml`. Initialize it from Visual Studio Code Source Control and create this first commit before running campaign initialization:

> Initialize blank campaign notebook

## Initialization prompt

> Use ttrpg-campaign-init to help me configure this campaign. Preserve choices already in campaign.yaml, ask about the essential settings first, and show me the exact proposed changes before saving them.

## Approval prompt

> The proposed campaign settings are approved. Please update campaign.yaml and record the change in wiki/log.md.

## Rehearsal checks

- Codex identifies the correct campaign folder.
- `git --version` succeeds and a safe demonstration identity is visible.
- The extracted folder contains `campaign.yaml` directly rather than another unnecessary nested folder.
- Git has no remote and the blank template is captured in the baseline commit.
- The access-check prompt makes no changes.
- The initialization proposal preserves existing values and leaves undecided settings open.
- Only approved settings and the activity log change after approval.
- The approved configuration is reviewed and committed separately from the blank baseline.
- No remote is created and nothing is pushed.
- The final repository state matches the starting point required by the adventure walkthrough.
