# Set Up Your Campaign in Codex

Visual Studio Code is the shared campaign workbench; the Codex extension supplies the AI assistant within it.

## Install Codex for Visual Studio Code

Install [Visual Studio Code](https://code.visualstudio.com/) and the [OpenAI Codex extension](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt), then authenticate for each when prompted. Open the campaign folder in Visual Studio Code and trust the folder if Visual Studio Code asks.
## Connect the campaign folder

Start a conversation with:

> Help me get started with this campaign notebook. Read AGENTS.md and follow the campaign instructions. Tell me which campaign you are using and whether you can read and save its files. Leave everything unchanged for now.
## Codex-specific capabilities

Codex supports built-in image generation when that tool is available in the session. The map and token skills can use it to create or edit artwork from campaign notes and optional reference images. Image generation has account and usage limits; see [OpenAI's image-generation guide](https://learn.chatgpt.com/docs/image-generation).

If Codex cannot read a PDF directly, it can use the included `scripts/extract_pdf.py` utility for documents with a text layer. Scanned pages still need OCR or supplied extracted text. If Codex cannot create an image, provide existing artwork or request a reusable brief.

## Continue the shared setup

Return to [connect and configure your assistant](../getting-started.md#3-connect-and-configure-your-assistant), then follow the shared walkthrough for importing notes and approving wiki updates.

