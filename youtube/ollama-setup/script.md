# VS Code and Ollama Setup: Script

Status: Initial scaffold. Exact interface labels and the complete approved-save workflow must be confirmed in the recording environment.

| Section | Narration direction | On screen |
| --- | --- | --- |
| Outcome | Explain that Visual Studio Code is the standard workbench for campaign files, AI chat, the terminal, Markdown Preview, and Source Control. This video connects a local Ollama model and ends, if the recorded workflow succeeds, with a configured campaign ready for source material. | Preview `campaign.yaml`, the campaign index, Chat with the Ollama model selected, and a clean Source Control view. |
| Local-model expectations | Explain that model inference runs locally through Ollama, but storage, memory needs, and response time depend heavily on the computer and selected model. Avoid presenting one machine's timing as a benchmark. | Show the recorded environment details without exposing a username, device name, network address, or other private information. |
| Git prerequisite | Explain that Visual Studio Code provides the Source Control interface but relies on Git installed on the machine. A GitHub account is not required for local history. | Run `git --version` in the integrated terminal. If Git is missing, show the official download location, cut past installation, restart Visual Studio Code, and rerun the check. |
| Commit identity | Explain that each commit records an author name and email. These are attribution fields, not GitHub credentials, and may become visible if the repository is published later. | Check `git config --global --get user.name` and `git config --global --get user.email`. Use a prepared non-personal recording identity. |
| Download and extract | Explain that the release ZIP is a blank campaign template and does not require creating or cloning a GitHub repository. | Download `ttrpg-wiki-template.zip`, extract it into a folder named for the fictional campaign, and open the folder containing `campaign.yaml` in Visual Studio Code. |
| Initialize Git | Explain that Git can track changes locally without publishing the campaign. Create a clean restore point before customization. | Open Source Control, select **Initialize Repository**, stage the blank template, and commit it as `Initialize blank campaign notebook`. |
| Ollama tools | Introduce Ollama as the local model runtime and the Ollama extension as the connection to Visual Studio Code's Chat interface. | Show `ollama --version`, the installed extension, and the trusted campaign workspace. Do not linger on account or machine details. |
| Python environment | Explain that Python supports the included checks and image utilities; the viewer does not need to write Python. | Run the platform-appropriate commands from `docs/getting-started.md`. Cut the dependency-download wait. |
| Model download | Explain that `qwen3-coder:30b` is the combination validated for this workflow and requires substantial storage and working memory. Other models may behave differently. | Run `ollama pull qwen3-coder:30b`. Show the start and successful completion with the intervening wait removed. |
| Connect Chat | Explain that the extension exposes the local model through Visual Studio Code's native Chat panel. | Open Chat, choose the Ollama provider, and select `qwen3-coder:30b`. |
| Access check | Explain that the first prompt checks the intended workspace and instructions without authorizing edits. | Send the workspace-confirmation prompt from the runbook. Retain enough progress to make an edited wait clear, then confirm the named campaign and unchanged Source Control state. |
| Skill discovery | Explain that the validated extension discovered the project skills stored with the campaign. This result is specific to the recorded versions and model. | Type `/ttrpg`, show the available project skills, and select `/ttrpg-campaign-init`. |
| Initialization | Explain that the campaign-init skill preserves existing choices and asks for essential missing settings. | Supply the prepared fictional answers and show the resulting proposal. Shorten long waits without hiding the request or completed response. |
| Review and approval | Reinforce that a proposal in Chat is not saved configuration. Continue only if rehearsal confirms the complete workflow. | Confirm Source Control is unchanged, review the exact proposal, send the approval prompt, inspect `campaign.yaml`, `wiki/log.md`, and the diff, then commit the approved configuration. |
| Limits and handoff | State exactly what this recording verified. Mention that PDF ingestion, web access, and image generation depend on separately available capabilities and are not established merely by connecting a local model. | Show the recorded version note, then end on `wiki/index.md` with a link card to the shared adventure walkthrough. Do not create or push a remote. |

When a viewer has no configured identity, show the following pattern with their own values rather than the recording identity:

```powershell
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## Closing line

Use this closing only if the approved-save workflow succeeds and the final diff has been reviewed:

> The campaign now has a local Git history, is connected to the selected Ollama model, and is configured with the GM's approved settings for the shared adventure walkthrough.

If the take confirms only connection, instruction discovery, or the question flow, end by naming those narrower results and direct viewers to the current compatibility notes instead.
