# Set Up Your Campaign with Ollama

Visual Studio Code is the shared campaign workbench; the Ollama extension connects its native Chat interface to the selected local model.

## Install Ollama for Visual Studio Code

Install [Git for Windows](https://git-scm.com/install/windows), [Python 3.11 or newer](https://www.python.org/), [Visual Studio Code](https://code.visualstudio.com/), [Ollama](https://ollama.com/download), and the [Ollama extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ollama.ollama).

Download the validated model from a Visual Studio Code terminal:

```powershell
ollama pull qwen3-coder:30b
```

The model is a substantial local download and requires considerably more working memory than its download size. Performance depends strongly on the computer running it.

## Connect the campaign folder

Open the campaign folder in Visual Studio Code and trust it if prompted. Open the **Chat** panel with `Ctrl+Alt+I` or the Chat icon. Select the model selector, choose the Ollama provider, and select `qwen3-coder:30b`.

Start a conversation with:

> Help me get started with this campaign notebook. Read AGENTS.md and follow the campaign instructions. Tell me which campaign you are using and whether you can read and save its files. Leave everything unchanged for now.

In the validated session, the extension read the project instructions and automatically discovered the skills under `.agents/skills/`. Typing `/ttrpg` displayed the available project skills, and `/ttrpg-campaign-init` started campaign configuration.

## Ollama-specific capabilities and limitations

The language model runs locally through Ollama. The validated initial request took more than 30 minutes, and campaign initialization took approximately 45 minutes. These are observations from one machine, not performance guarantees.

The validation confirmed instruction and skill discovery and the campaign-initialization question flow. It did not separately record the exact proposal, approved file writes, or resulting files. PDF ingestion, image generation, player-safe review, web access, and the other campaign workflows were not tested.

If PDF access is unavailable, the assistant can use the included `scripts/extract_pdf.py` utility for PDFs with a text layer. Scanned pages still need OCR or supplied extracted text. Image generation requires a separate available image tool or supplied artwork.

Local models vary in instruction following and tool use. Review every proposal, especially visibility labels and player-safe material. A large context window does not make it safe or useful to load the whole campaign when only a few current pages are relevant.

## Continue the shared setup

Return to [connect and configure your assistant](../getting-started.md#3-connect-and-configure-your-assistant), then follow the shared walkthrough for reviewing campaign settings and applying approved wiki updates. In the validated extension, `/ttrpg-campaign-init` selected the setup workflow.

See [what has been tested](compatibility.md) for the current verification status and the [complete validation record](../validation/ollama-vscode-2026-11-22.md) for the supplied observations and limits.
