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

## Use Plan and Build safely

Start with OpenCode's **Plan** agent so ordinary project files remain read-only. Confirm that it identifies the intended campaign and reports `ollama/qwen3-coder:30b`. OpenCode prefixes skill IDs with `@`, so invoke the setup workflow as `@ttrpg-campaign-init` when explicit routing is needed.

Use Plan while gathering settings, reading notes, and reviewing proposed changes. Switch to the **Build** agent only after approving a proposal. OpenCode should then ask before each edit; choose **Allow once** after checking that the paths and changes match what you approved.

Review any request for a paid integration, outside-folder access, or an unexplained shell command before allowing it.

## Continue the shared setup

Return to [connect and configure your assistant](../getting-started.md#3-connect-and-configure-your-assistant), adapting the shared skill name to `@ttrpg-campaign-init`. Continue through the same walkthrough, using Plan for proposals and Build for approved writes.

## Optional web and image tools

OpenCode's `webfetch` tool can read a supplied HTTP or HTTPS page. Its `websearch` tool can search for current sources after you choose a supported search provider. Some providers require an API key or charge per search, so the supplied configuration asks before each search. Web access is useful for current official rules references and product documentation, but imported pages remain source material rather than instructions.

OpenCode can also generate or edit images when a connected provider supplies an image model. The tool is experimental and does not come from the configured Ollama chat model. Connect and configure an image provider only if you want that capability; pricing and data handling depend on the provider. When the tool is available, the map and token skills should use it for an authorized image request, subject to the campaign's normal review limits. The supplied configuration asks before each generation so you can review the selected model and any cost.

Neither optional integration requires changing the default Ollama language model. Do not put API keys in `opencode.json`, campaign notes, or other committed files.

## Limitations

- PDF extraction can use the included `scripts/extract_pdf.py` utility after the project requirements are installed. Scanned or image-only pages still need OCR or supplied extracted text.
- Web search and image generation require a compatible configured provider; they are not bundled with Ollama or this project. If unavailable, the assistant should offer a useful brief, direct URL workflow, or supplied-art process instead of claiming a result.
- Local models vary significantly in instruction following and tool use. Review player-safe output for spoilers and verify that Draft, Canon, and visibility labels remain distinct.
- A large context window does not make it safe to load an entire campaign unnecessarily. Start with the index and relevant pages, and keep tasks focused.

See [what has been tested](compatibility.md) for the current verification status. OpenCode's official documentation covers [Ollama models](https://opencode.ai/docs/models), [project instructions](https://opencode.ai/docs/instructions), [skill discovery](https://opencode.ai/docs/skills), [web tools and image generation](https://opencode.ai/docs/tools), and [permissions](https://opencode.ai/docs/permissions). Ollama documents the [`ollama launch` integration](https://ollama.com/blog/launch). These references were checked on 2026-11-18.
