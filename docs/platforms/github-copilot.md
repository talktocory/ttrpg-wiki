# Set Up Your Campaign in GitHub Copilot

This guide covers Copilot in Visual Studio Code agent mode, Copilot CLI, and repository-backed cloud sessions. The Visual Studio Code workflow was manually validated on 2026-11-19; CLI and cloud-agent behavior still need separate testing. You do not need to write code, but Python 3.11 or newer and the project requirements are the baseline for the complete local workflow.

## 1. Open your campaign folder

Open the folder containing `campaign.yaml` and `wiki/` in your Copilot tool. In Visual Studio Code, trust the folder when Restricted Mode asks whether to enable its features. Open Chat and authenticate to GitHub. The repository includes general instructions in `.github/copilot-instructions.md` and generated project skills under `.github/skills/`.

If you want to confirm access before changing anything, ask:

> Which campaign workspace are you using, and can you read and save it? Do not change anything.

Copilot should identify the right campaign and explain what it can do. If your version shows which instruction files and skills it used, look for `.github/copilot-instructions.md` and the `ttrpg-*` skills.

## 2. Set up Python and the project requirements

From the project root in Windows PowerShell, run:

```powershell
python -m venv .venv
./.venv/Scripts/Activate.ps1
python -m pip install -r requirements-dev.txt
```

Copilot can run these commands for you, but it may ask you to approve PowerShell, Python, Git, and file-processing commands. The requirements provide PyYAML and Pillow for the repository utilities; they do not install a PDF parser. PDF reading still depends on Copilot's available tools and the local environment. See [Python setup and tools](../scripts.md) for other shells.

## 3. Check the skills and configure the campaign

Copilot can load a matching skill automatically or expose it as a slash command. In Visual Studio Code, run **Chat: Open Customizations** from the Command Palette and open **Skills** to inspect the workspace skills. In Copilot CLI, use `/skills list`; after changing skill files during a session, use `/skills reload`, followed by `/skills info ttrpg-campaign-init` to inspect the result.

Before adding notes, invoke the campaign setup skill. The minimum prompt exercised during validation was:

> /ttrpg-campaign-init

Copilot should ask for the essential settings and show a proposed `campaign.yaml` update. Review the proposal and leave any undecided settings open. When it is ready, use its approval control or say:

> The proposed campaign settings are approved. Please update campaign.yaml and record the change in wiki/log.md.

Copilot should change only the approved settings and activity log. If the skill does not appear, start a fresh session and check that `.github/skills/ttrpg-campaign-init/SKILL.md` is present. Asking Copilot to read the canonical `.agents/skills/ttrpg-campaign-init/SKILL.md` and its linked reference remains a fallback when native discovery is unavailable.

## 4. Try one small task

Put one source under `raw/`, then enter:

> /ttrpg-wiki-ingest

When there is more than one plausible source, add the path or describe which source to use. The skill already contains the proposal-first, evidence, status, and privacy rules. Review its suggestion and ask for revisions as needed.

## 5. Save the changes you want

When the proposal is ready, say:

> The proposed changes are approved. Please proceed with the appropriate wiki updates.

Copilot should save the approved changes and tell you which files it updated. If it can only suggest text, ask for complete updated files and save them yourself. Check that the campaign index and activity log are updated too.

For a more detailed first-note workflow, continue with [bring in one set of notes](../getting-started.md#4-bring-in-one-set-of-notes). For ongoing use, see the [everyday GM guide](../gm-guide.md).

## Other prompts exercised during validation

Copilot also recognized these minimal requests:

```text
/ttrpg-session-prep
/ttrpg-map-create Please create a map of the circus grounds.
```

For session preparation, Copilot asked for missing party, focus, duration, and scheduling details. For the map, it offered a locally drawn vector-based illustration because hosted AI image generation was not the selected route. It used Python and took approximately 14 minutes in that test. Image tools, output style, and completion time can differ between sessions; review what Copilot says it can actually produce before approving an asset workflow.

## Personal skills are optional

The committed `.github/skills/` directory shares these workflows with everyone using this campaign repository. If you want a separate personal skill available across repositories, Copilot also supports `~/.copilot/skills/<skill-name>/SKILL.md`. Do not copy the campaign skills there merely to use this project; the repository versions are already discoverable and stay aligned with the framework.

## If you get stuck

- **Copilot cannot find a note:** ask which folder it is using, then point it to the correct file.
- **A skill is missing:** start a fresh session, inspect `.github/skills/`, and use VS Code's Skills view or the CLI `/skills` commands to confirm discovery.
- **It overlooks the campaign instructions:** ask it to read `AGENTS.md` and the relevant skill before continuing.
- **A command is waiting:** review the requested PowerShell, Python, Git, or file-processing command and approve it only when its purpose and target match the task.
- **You are using a cloud session:** check which files it can access. It will not automatically see the campaign folder on your computer.

Other Copilot versions may need different setup. See [what has been tested](compatibility.md) and the [2026-11-19 Visual Studio Code validation record](../validation/github-copilot-vscode-2026-11-19.md). For technical help, use the official guides for [Agent Skills in VS Code](https://code.visualstudio.com/docs/agent-customization/agent-skills), [Copilot repository and cloud-agent skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills), [Copilot CLI skills](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills), and [project instructions](https://docs.github.com/en/copilot/reference/custom-instructions-support), checked 2026-11-18.
