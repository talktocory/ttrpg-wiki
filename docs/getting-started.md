# Your First Campaign

Start with a single set of notes. You do not need to fill every folder or learn to write code. For the complete local workflow, install Python 3.11 or newer and the project's required packages once; your assistant can then use the included validation and image utilities when needed.

## 1. Create a private campaign folder

Download and unzip the project, or copy it into a folder named for your campaign. Keep one campaign in each copy. If you prefer GitHub, create a private repository from the template rather than putting campaign notes in a public fork.

## 2. Set up the local Python environment

From the project root, create a virtual environment, activate it, and install the requirements. In Windows PowerShell, use:

```powershell
python -m venv .venv
./.venv/Scripts/Activate.ps1
python -m pip install -r requirements-dev.txt
```

You do not need to write Python code. This setup gives the assistant the supported packages used by the project tools. It does not guarantee PDF extraction, which still depends on the capabilities available in your AI tool and local environment. See [Python setup and tools](scripts.md) for other shells and troubleshooting.

## 3. Connect and configure your assistant

Choose the guide for [Codex](platforms/codex.md), [Claude Desktop or Claude Code](platforms/claude-desktop.md), [GitHub Copilot](platforms/github-copilot.md), or [OpenCode v2 with an Ollama model](platforms/opencode-ollama.md). It explains how to connect that assistant, confirm which files it can access, and use `ttrpg-campaign-init` to configure `campaign.yaml` safely.

Follow the access and configuration steps in that guide, then return here. Confirm that the assistant can read and save the campaign workspace before relying on it. It is fine to leave the game or optional settings undecided. The [settings guide](configuration.md) explains every available field.

## 4. Bring in one set of notes

Put a text or Markdown note in `raw/markdown/`, or a PDF in `raw/pdfs/`. You can also paste a short source into the conversation while the assistant remains connected to the campaign workspace. Keep the original; the assistant uses it as a source while proposing organized campaign pages.

Try this minimum request:

> Use ttrpg-wiki-ingest to ingest raw/markdown/my-session-notes.md.

The skill already contains the proposal-first, evidence, status, and privacy instructions. If there is only one obvious source, a host with slash-command support may need only `/ttrpg-wiki-ingest`. Name the source when more than one file could match.

## 5. Approve the proposal and apply it to the wiki

This is the step that turns the conversation into lasting campaign notes. The proposal should show the content to be added or changed, where it will go, and any questions. Ask for revisions first if you need them. When you are ready, say:

> The proposed changes are approved. Please proceed with the appropriate wiki updates.

That tells the assistant to apply the proposal to the wiki files, rather than leaving it as a suggestion in chat. You can also approve only part of a proposal:

> Save the session summary and NPC updates. Leave the proposed encounter as an idea for now.

After approval, the assistant should save those changes and update your campaign's contents page and activity log. Check its summary against the files in the campaign folder. The wiki is updated only when the files have actually been saved; correct workspace access if the assistant cannot do so.

If you use Git, you can then make a separate Git commit to record the saved update in version history. The approval prompt above requests wiki edits; it does not itself request a Git commit or publication. Git remains optional.

Open [the campaign index](../wiki/index.md) to find your new pages.

## 6. Use it for your next session

> Use ttrpg-session-prep to prepare our next session.

After the game, bring in what actually happened. Preparing a scene does not make its outcome true. For a player recap, identify which facts the characters learned and review the finished text before sharing it.

Continue with the [GM guide](gm-guide.md). The [fictional example](../examples/relay-station/README.md) shows how original notes, private information, and a player recap differ; it is separate from your campaign.
