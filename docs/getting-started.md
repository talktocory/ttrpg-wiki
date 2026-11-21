# Your First Campaign

## 1. Create a private campaign folder

Download and unzip the project, or copy it into a folder named for your campaign. Keep one campaign in each copy. If you prefer GitHub, create a private repository from the template rather than putting campaign notes in a public fork.

## 2. Set up the local Python environment

Install [Python 3.11 or newer](https://www.python.org/downloads/) and the project's required packages once. This lets the AI assistant use the included validation, configuration, and image tools when needed; you do not need to write Python code.

Open a terminal in the project root and run the commands for your shell.

### Windows PowerShell

```powershell
python -m venv .venv
./.venv/Scripts/Activate.ps1
python -m pip install -r requirements-dev.txt
```

### macOS or Linux

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
```

The requirements install the supported versions of PyYAML for configuration files and Pillow for image processing. They do not install a PDF parser; PDF support depends on the tools available to your AI assistant and local environment.

## 3. Connect and configure your assistant

Choose the guide for:

* [OpenAI Codex](platforms/codex.md),
* [Claude Desktop or Claude Code](platforms/claude-desktop.md),
* [GitHub Copilot](platforms/github-copilot.md), or
* [OpenCode v2 with an Ollama model](platforms/opencode-ollama.md).

Follow that guide to connect the assistant and confirm that it can read and save the campaign folder. Then ask it to configure the campaign:

> Use ttrpg-campaign-init to help me configure this campaign. Preserve choices already in campaign.yaml, ask about the essential settings first, and show me the exact proposed changes before saving them.

Review the proposal and leave any undecided settings open. When it is ready, say:

> The proposed campaign settings are approved. Please update campaign.yaml and record the change in wiki/log.md.

The assistant should change only the approved settings and activity log, then report what it saved. If your platform separates planning from editing, follow its guide when moving between those modes.

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

Continue with the [GM guide](gm-guide.md).
