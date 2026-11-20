# Set Up Your Campaign in GitHub Copilot

This guide covers Copilot in Visual Studio Code agent mode, Copilot CLI, and repository-backed cloud sessions. The Visual Studio Code workflow was manually validated on 2026-11-19; CLI and cloud-agent behavior still need separate testing.

## Open the campaign folder

Open the folder containing `campaign.yaml` and `wiki/` in your Copilot tool. In Visual Studio Code, trust the folder when Restricted Mode asks whether to enable its features. Open Chat and authenticate to GitHub. The repository includes general instructions in `.github/copilot-instructions.md` and generated project skills under `.github/skills/`.

If you want to confirm access before changing anything, ask:

> Which campaign workspace are you using, and can you read and save it? Do not change anything.

Copilot should identify the right campaign and explain what it can do. If your version shows which instruction files and skills it used, look for `.github/copilot-instructions.md` and the `ttrpg-*` skills.

## Check skill discovery

Copilot can load a matching skill automatically or expose it as a slash command. In Visual Studio Code, run **Chat: Open Customizations** from the Command Palette and open **Skills** to inspect the workspace skills. In Copilot CLI, use `/skills list`; after changing skill files during a session, use `/skills reload`, followed by `/skills info ttrpg-campaign-init` to inspect the result.

The minimum validated invocation was `/ttrpg-campaign-init`. If a skill does not appear, start a fresh session and check that its `SKILL.md` exists under `.github/skills/`. Asking Copilot to read the canonical `.agents/skills/<skill-name>/SKILL.md` remains a fallback when native discovery is unavailable.

The committed `.github/skills/` directory is sufficient for this project; personal copies are not required.

## Permissions and capabilities

Copilot may ask you to approve PowerShell, Python, Git, and file-processing commands. Review each command's purpose and target. A cloud session sees only the repository or files made available to it, not an unrelated campaign folder on your computer.

Image tools and output styles vary between Copilot surfaces. The validated Visual Studio Code session created a local vector map rather than using hosted image generation; see the [validation record](../validation/github-copilot-vscode-2026-11-19.md) for those test details.

## Continue the shared setup

Return to [connect and configure your assistant](../getting-started.md#3-connect-and-configure-your-assistant), then follow the shared walkthrough for importing notes and approving wiki updates.

## If you get stuck

- **Copilot cannot find a note:** ask which folder it is using, then point it to the correct file.
- **A skill is missing:** start a fresh session, inspect `.github/skills/`, and use VS Code's Skills view or the CLI `/skills` commands to confirm discovery.
- **It overlooks the campaign instructions:** ask it to read `AGENTS.md` and the relevant skill before continuing.
- **A command is waiting:** approve it only when its purpose and target match the task.
- **You are using a cloud session:** check which files it can access. It will not automatically see the campaign folder on your computer.

Other Copilot versions may need different setup. See [what has been tested](compatibility.md). For technical help, use the official guides for [Agent Skills in VS Code](https://code.visualstudio.com/docs/agent-customization/agent-skills), [Copilot repository and cloud-agent skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills), [Copilot CLI skills](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills), and [project instructions](https://docs.github.com/en/copilot/reference/custom-instructions-support), checked 2026-11-18.
