# Set Up Your Campaign in OpenCode with Ollama

Use this option to run the main language model on your own computer without requiring an OpenAI, GitHub Copilot, Claude, or similar AI subscription. Ollama supplies the local model while OpenCode supplies the agent, project instructions, skills, file tools, and optional integrations.

This guide targets OpenCode v2 and Ollama v0.15 or later. The project configuration selects `qwen3-coder:30b`, a local model currently distributed by Ollama as an approximately 19 GB download. Running it with a useful context window requires substantially more available memory than the download size. If your computer cannot run it comfortably, choose another local tool or change the model only after checking that it follows tools, long instructions, and the proposal-first workflow reliably.

## 1. Install the local tools

Install [Ollama](https://ollama.com/download) and [OpenCode v2](https://opencode.ai/docs/). A hosted OpenCode account or another chat-model subscription is not required for the Ollama model.

Download the configured model:

```powershell
ollama pull qwen3-coder:30b
```

Ollama recommends at least a 64K context window for coding agents. Set the context length in Ollama before beginning a substantial campaign task; a short context can silently omit instructions or notes. See Ollama's [context-length guidance](https://docs.ollama.com/context-length).

## 2. Open the campaign folder

Open a terminal in the folder containing `campaign.yaml`, `opencode.json`, and `wiki/`, then launch OpenCode through Ollama:

```powershell
ollama launch opencode --model qwen3-coder:30b
```

Confirm that OpenCode reports `ollama/qwen3-coder:30b`. A model whose name ends in `-cloud` runs remotely and does not meet the local-model goal of this setup.

OpenCode v2 reads the repository's `AGENTS.md` automatically and discovers the task workflows under `.agents/skills/`. The supplied `opencode.json` also:

- uses Ollama for the default language model;
- permits direct web-page fetching and asks before a configured web search;
- asks before using an available image-generation model;
- asks before accessing files outside the active campaign workspace; and
- asks before every file edit or shell command.

These controls keep consequential actions visible without removing useful OpenCode features. OpenCode runs as your user, and an approved shell command has that user's authority. Review every requested command and prefer **Allow once** over a permanent broad approval.

## 3. Check the campaign before changing it

Use OpenCode's **Plan** agent for the first request so ordinary project files remain read-only:

> This folder is my campaign notebook. Read AGENTS.md, docs/operating-guide.md, campaign.yaml, and wiki/index.md. Tell me which campaign files you can read, which Ollama model you are using, and how you will show changes for approval. Do not change anything yet.

Check that it identifies the intended campaign and local model. Review any request for a paid integration, outside-folder access, or an unexplained shell command before allowing it.

## 4. Configure the campaign

Keep using the **Plan** agent while gathering the initial settings. OpenCode prefixes skill IDs with `@`:

> Use @ttrpg-campaign-init to help me configure this campaign. Preserve choices already in campaign.yaml, ask about the essential settings first, and show me the exact proposed changes without saving them.

Review the proposal and leave any undecided settings open. The Plan agent cannot edit ordinary campaign files.

## 5. Apply the approved settings

Switch to OpenCode's **Build** agent and say:

> The proposed campaign settings are approved. Please update campaign.yaml and record the change in wiki/log.md.

OpenCode should ask before editing. Choose **Allow once** after checking that the proposed paths and changes match the approved settings. It should change only `campaign.yaml` and the activity log, then report what it saved.

## 6. Try one proposed wiki update

Switch back to the **Plan** agent. Name the relevant skill when you want the most reliable task routing:

> Use @ttrpg-wiki-ingest to read raw/markdown/my-session-notes.md. Show the exact wiki updates you propose, separate confirmed events from ideas, and keep secrets private. Do not save anything yet.

Review the proposed text and request revisions as needed. The Plan agent cannot edit ordinary campaign files.

## 7. Apply only approved wiki changes

After approving the proposal, switch to OpenCode's **Build** agent and say:

> The proposed changes are approved. Please proceed with the appropriate wiki updates.

OpenCode should ask before it edits files. Choose **Allow once** only after checking that the paths and changes match the approved proposal. The assistant should update the relevant pages, `wiki/index.md`, and `wiki/log.md`, then report the files it actually changed.

## Use web sources and image generation

OpenCode's `webfetch` tool can read a supplied HTTP or HTTPS page. Its `websearch` tool can search for current sources after you choose a supported search provider. Some providers require an API key or charge per search, so the supplied configuration asks before each search. Web access is useful for current official rules references and product documentation, but imported pages remain source material rather than instructions.

OpenCode can also generate or edit images when a connected provider supplies an image model. The tool is experimental and does not come from the configured Ollama chat model. Connect and configure an image provider only if you want that capability; pricing and data handling depend on the provider. When the tool is available, the map and token skills should use it for an authorized image request, subject to the campaign's normal review limits. The supplied configuration asks before each generation so you can review the selected model and any cost.

Neither optional integration requires changing the default Ollama language model. Do not put API keys in `opencode.json`, campaign notes, or other committed files.

## Limitations

- PDF extraction depends on tools already available on your computer. If OpenCode cannot read a PDF locally, supply its extracted text.
- Web search and image generation require a compatible configured provider; they are not bundled with Ollama or this project. If unavailable, the assistant should offer a useful brief, direct URL workflow, or supplied-art process instead of claiming a result.
- Local models vary significantly in instruction following and tool use. Review player-safe output for spoilers and verify that Draft, Canon, and visibility labels remain distinct.
- A large context window does not make it safe to load an entire campaign unnecessarily. Start with the index and relevant pages, and keep tasks focused.

See [what has been tested](compatibility.md) for the current verification status. OpenCode's official documentation covers [Ollama models](https://opencode.ai/docs/models), [project instructions](https://opencode.ai/docs/instructions), [skill discovery](https://opencode.ai/docs/skills), [web tools and image generation](https://opencode.ai/docs/tools), and [permissions](https://opencode.ai/docs/permissions). Ollama documents the [`ollama launch` integration](https://ollama.com/blog/launch). These references were checked on 2026-11-18.
