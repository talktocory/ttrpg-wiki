# VS Code and Ollama Setup: Timed Outline

Target running time: 9–11 minutes.

| Time | Section | Teaching goal |
| --- | --- | --- |
| 0:00–0:35 | Outcome and prerequisites | Show the initialized local campaign and explain that the language model runs locally through Ollama. |
| 0:35–1:25 | Verify Git and commit identity | Confirm that Git is installed, explain how to install it if missing, and verify the author name and email used for commits. |
| 1:25–2:15 | Download and extract | Download the latest release ZIP and extract it into a folder named for the campaign. |
| 2:15–3:00 | Open the folder and initialize Git | Open the folder containing `campaign.yaml`, initialize a repository, and commit the blank baseline. |
| 3:00–4:00 | Install Ollama and the extension | Identify the Ollama runtime and Visual Studio Code extension used by the documented workflow. |
| 4:00–4:45 | Install the local Python environment | Prepare the supported validation and image-processing dependencies. |
| 4:45–5:35 | Download and select the model | Pull `qwen3-coder:30b`, select the Ollama provider in Chat, and explain the hardware and performance tradeoff. |
| 5:35–6:30 | Confirm workspace access and skills | Verify the intended campaign without changing it, then show automatic discovery of the `ttrpg-*` skills. |
| 6:30–8:35 | Initialize the campaign | Invoke `/ttrpg-campaign-init`, answer essential questions, and review the exact proposal. |
| 8:35–10:05 | Approve and inspect | Save the approved settings, inspect the Git diff, and commit the campaign configuration. |
| 10:05–11:00 | Limits and handoff | State what was verified in this recording and point to the shared adventure walkthrough. |

Cut the model download and local-model waits while leaving each command, visible progress, and successful result on screen. Do not imply that the observed response time is typical for other hardware.

