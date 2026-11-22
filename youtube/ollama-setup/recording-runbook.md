# VS Code and Ollama Setup: Recording Runbook

Follow [the shared recording standards](../shared/recording-standards.md).

## Prepared inputs

- Git installed, or the official Git installer ready for the missing-Git branch
- A non-personal demonstration commit identity that is safe to display
- The latest `ttrpg-wiki-template.zip` release downloaded but not yet extracted
- An empty local parent folder where the fictional campaign folder will be created
- A fictional campaign name, premise, genre, tone, game, and edition
- Python 3.11 or newer
- Visual Studio Code and the Ollama runtime installed
- The Ollama extension for Visual Studio Code available
- Enough free storage and working memory for `qwen3-coder:30b`
- A plan to record download and response progress without retaining the full wait in the edit

Record the operating system, Visual Studio Code version, Ollama version, extension version when available, selected model, Python version, and relevant hardware details before the take.

## Prerequisite checks

Run these in Visual Studio Code's integrated terminal before downloading or extracting the campaign template:

```powershell
git --version
git config --global --get user.name
git config --global --get user.email
ollama --version
```

If Git or Ollama is missing, use its official installer, restart Visual Studio Code when required, and rerun the applicable version check. If either Git identity value is empty, demonstrate the configuration pattern from the script using the viewer's chosen attribution values. Do not display a personal recording email.

## Git baseline

After extraction, open the folder that directly contains `campaign.yaml`. Initialize it from Visual Studio Code Source Control and create this first commit before running campaign initialization:

> Initialize blank campaign notebook

## Model setup

Run the documented model command in the integrated terminal:

```powershell
ollama pull qwen3-coder:30b
```

Capture the command, early progress, and successful completion as separate edit points. Open Chat with `Ctrl+Alt+I` or the Chat icon, choose the Ollama provider, and select `qwen3-coder:30b`. Confirm the current interface labels during rehearsal.

## Workspace confirmation prompt

> Help me get started with this campaign notebook. Read AGENTS.md and follow the campaign instructions. Tell me which campaign you are using and whether you can read and save its files. Leave everything unchanged for now.

## Initialization prompt

Use the discovered slash command:

```text
/ttrpg-campaign-init
```

If explicit direction is needed, follow with:

> Help me configure this campaign. Preserve choices already in campaign.yaml, ask about the essential settings first, and show me the exact proposed changes before saving them.

## Approval prompt

> The proposed campaign settings are approved. Please update campaign.yaml and record the change in wiki/log.md.

## Rehearsal checks

- Visual Studio Code is using the local campaign folder and the intended Ollama model.
- `git --version` and `ollama --version` succeed, and a safe demonstration Git identity is visible.
- The extracted folder contains `campaign.yaml` directly rather than another unnecessary nested folder.
- Git has no remote and the blank template is captured in the baseline commit.
- The model selector shows the Ollama provider and `qwen3-coder:30b`.
- The workspace-confirmation prompt identifies the correct campaign and makes no changes.
- Typing `/ttrpg` exposes the repository's project skills, including `ttrpg-campaign-init`.
- The initialization proposal preserves existing values and leaves undecided settings open.
- No campaign files change before approval.
- Only approved settings and `wiki/log.md` change after approval.
- Any requested command or edit approval has a clear purpose and target.
- The approved configuration is reviewed and committed separately from the blank baseline.
- No remote is created and nothing is pushed.
- Long waits are shortened honestly: the edit retains the request, some progress, and the completed response.

The existing validation record did not independently establish the approved-save sequence. If rehearsal does not confirm the proposal, approval, exact file changes, and final diff, stop the take and do not claim that complete workflow in narration.

## Recording the limits

Record the actual timings and results from this take. Describe them as observations from the recorded computer, not guarantees. Do not claim that every Ollama model will discover skills, follow approval boundaries, edit files correctly, read PDFs, browse the web, or generate images.

