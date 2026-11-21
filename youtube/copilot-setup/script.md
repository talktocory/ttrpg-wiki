# VS Code and GitHub Copilot Setup: Script

Status: Initial scaffold. Exact interface labels must be confirmed in the recording environment.

| Section | Narration direction | On screen |
| --- | --- | --- |
| Outcome | Explain that this short video ends with a local, configured campaign repository ready for source material. | Preview `campaign.yaml`, the campaign index, and a clean Source Control view. |
| Git prerequisite | Explain that Visual Studio Code provides the Source Control interface but relies on Git installed on the machine. A GitHub account is not required for local history. | Run `git --version` in the integrated terminal. If Git is missing, show the official download location, cut past installation, restart Visual Studio Code, and rerun the check. |
| Commit identity | Explain that each commit records an author name and email. These are attribution fields, not GitHub credentials, and may be visible if the repository is published later. | Check `git config --global --get user.name` and `git config --global --get user.email`. Use a prepared non-personal recording identity; do not reveal a personal email address. |
| Download and extract | Explain that the release ZIP is a blank campaign template and does not require creating or cloning a GitHub repository. | Download `ttrpg-wiki-template.zip`, extract it into a folder named for the fictional campaign, and open the folder containing `campaign.yaml` in Visual Studio Code. |
| Initialize Git | Explain that Git can track changes locally without publishing the campaign. Create a clean restore point before customization. | Open Source Control, select **Initialize Repository**, stage the blank template, and commit it as `Initialize blank campaign notebook`. |
| Copilot | Explain that the demonstration uses GitHub Copilot in Visual Studio Code agent mode so it can work with repository files. | Trust the folder, open Chat, authenticate, and select agent mode. |
| Python environment | Explain that Python supports the included checks and image utilities; the viewer does not need to write Python. | Run the platform-appropriate commands from `docs/getting-started.md`. Cut the dependency-download wait. |
| Instructions and skills | Explain that the repository supplies Copilot instructions and task skills with the campaign. | Run **Chat: Open Customizations**, inspect Skills, and identify the `ttrpg-*` workspace skills. |
| Access check | Explain that the first prompt verifies the campaign folder without authorizing edits. | Send the workspace-confirmation prompt from the runbook. |
| Initialization | Explain that the campaign-init skill preserves existing choices and asks for essential missing settings. | Invoke `/ttrpg-campaign-init` or use the explicit initialization prompt if needed. Supply the prepared fictional answers. |
| Review and approval | Reinforce that the proposal is reviewed before files change. | Review, approve, inspect `campaign.yaml`, `wiki/log.md`, and Source Control, then commit the approved configuration. |
| Handoff | Explain that the local repository is ready for the same adventure workflow used with Codex. Mention that a new private remote can be added later for backup, but it is not required. | End on `wiki/index.md` with a link card to the next video. Do not create or push a remote. |

When a viewer has no configured identity, show the following pattern with their own values rather than the recording identity:

```powershell
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## Closing line

The campaign now has a local Git history, is connected to Copilot, and is configured with the GM's approved settings for the shared adventure walkthrough.
