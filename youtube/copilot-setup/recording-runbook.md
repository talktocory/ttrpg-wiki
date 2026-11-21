# VS Code and GitHub Copilot Setup: Recording Runbook

Follow [the shared recording standards](../shared/recording-standards.md).

## Prepared inputs

- Git installed, or the official Git installer ready for the missing-Git branch
- A non-personal demonstration commit identity that is safe to display
- The latest `ttrpg-wiki-template.zip` release downloaded but not yet extracted
- An empty local parent folder where the fictional campaign folder will be created
- A fictional campaign name, premise, genre, tone, game, and edition
- Python 3.11 or newer
- Visual Studio Code with GitHub Copilot access and authentication available

## Git prerequisite checks

Run these in Visual Studio Code's integrated terminal before downloading or extracting the campaign template:

```powershell
git --version
git config --global --get user.name
git config --global --get user.email
```

If Git is missing, install it from the official Git site, restart Visual Studio Code, and rerun `git --version`. If either identity value is empty, demonstrate the configuration pattern from the script using the viewer's chosen attribution values. Do not display a personal recording email.

## Workspace confirmation prompt

> Which campaign workspace are you using, and can you read and save it? Do not change anything.

## Git baseline

After extraction, open the folder that directly contains `campaign.yaml`. Initialize it from Visual Studio Code Source Control and create this first commit before running campaign initialization:

> Initialize blank campaign notebook

## Initialization prompt

> Use ttrpg-campaign-init to help me configure this campaign. Preserve choices already in campaign.yaml, ask about the essential settings first, and show me the exact proposed changes before saving them.

If the skill is already visible as a slash command, `/ttrpg-campaign-init` is the minimal validated invocation.

## Approval prompt

> The proposed campaign settings are approved. Please update campaign.yaml and record the change in wiki/log.md.

## Rehearsal checks

- Visual Studio Code is using the local campaign folder, not a cloud agent session.
- `git --version` succeeds and a safe demonstration identity is visible.
- The extracted folder contains `campaign.yaml` directly rather than another unnecessary nested folder.
- Git has no remote and the blank template is captured in the baseline commit.
- Copilot identifies the correct campaign and makes no changes during the access check.
- The Skills view shows the repository's `ttrpg-*` skills.
- The initialization proposal preserves existing values and leaves undecided settings open.
- Only approved settings and the activity log change after approval.
- Command approvals, if shown, have clear purposes and targets.
- The approved configuration is reviewed and committed separately from the blank baseline.
- No remote is created and nothing is pushed.
