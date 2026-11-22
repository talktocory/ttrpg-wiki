# GitHub Copilot in Visual Studio Code Validation — 2026-11-19

This is a manual validation record for one GitHub Copilot session in Visual Studio Code. It documents the observed workflow; it is not evidence for Copilot CLI, Copilot cloud agents, or every Copilot and Visual Studio Code build.

## Environment

| Item | Observed value |
| --- | --- |
| Date | 2026-11-19 |
| Operating system | Windows 11 Enterprise |
| AI assistant | GitHub Copilot |
| Host | Visual Studio Code |
| Python | 3.14.7 |
| Additional VS Code extensions | None installed for the test |

The exact Visual Studio Code and GitHub Copilot versions were not recorded. The folder was cloned from GitHub, opened in Visual Studio Code, and trusted when Visual Studio Code displayed its Restricted Mode warning. The tester then opened Chat and authenticated to GitHub.

## Setup and dependency observations

The repository's project skills were discovered automatically. Entering `/ttrpg-campaign-init` opened the configured campaign-initialization workflow without manually installing a skill.

The test relied extensively on PowerShell and Python commands. During the run, the tester created and activated a local virtual environment and installed the repository requirements:

```powershell
python -m venv .venv
./.venv/Scripts/Activate.ps1
python -m pip install -r requirements-dev.txt
```

Copilot requested approval before running several Git, Python, PowerShell, and PDF-processing commands. Python and the installed requirements should therefore be treated as the baseline for the complete local workflow, even though simple Markdown reading and writing may not invoke them.

At the time of this validation, the requirements file supplied PyYAML and Pillow but did not install a PDF parser, so extraction depended on tools available to the selected AI host and local environment. The framework later added a local pypdf utility; that later capability was not part of this test.

## Workflows exercised

### Campaign initialization

Minimal prompt:

```text
/ttrpg-campaign-init
```

Copilot asked for the campaign name, game and edition, premise and tone, language and terminology, usual session length, and table preferences. It showed a proposed `campaign.yaml` update and offered approval, revision, or no-change choices. After approval, it saved the selected settings.

### Source ingestion

A PDF one-shot adventure was placed under `raw/pdfs/`, followed by:

```text
/ttrpg-wiki-ingest
```

Copilot found the single relevant PDF, described its intent to prepare a sourced GM-only proposal, and requested permission for commands used to inspect the document. After the proposal was approved, it created organized GM material for campaign information, encounters, and NPCs.

### Session preparation

Minimal prompt:

```text
/ttrpg-session-prep
```

Copilot asked for party size and character levels, desired focus, available play time, and scheduled date. It prepared a proposal, then saved the approved session plan together with the proposed index and activity-log updates.

### Map creation

Minimal prompt:

```text
/ttrpg-map-create Please create a map of the circus grounds.
```

Copilot inspected the campaign pages with approved PowerShell commands, explained that its local result would be a stylized illustration rather than hosted AI-generated artwork, and offered a locally drawn map. After the tester supplied grid and scale choices, Copilot wrote a Python program that produced vector-based artwork. The image workflow took approximately 14 minutes. The tester approved the map and related wiki updates.

This is one observed fallback, not a guarantee that Copilot will always draw a map locally, use the same visual style, or finish in the same time. Available image tools and the selected generation route determine the result.

## Result and limits

- Workspace skills were discovered and invoked successfully with minimal slash-command prompts.
- Proposal-first review and approval worked for the exercised tasks.
- PowerShell and Python were important to the complete workflow.
- Copilot in Visual Studio Code was noticeably slower than the comparison Codex sessions observed by the tester, especially for map creation. No controlled performance benchmark was performed.
- The test did not validate Copilot CLI, Copilot cloud agents, player-safe spoiler review, reward reconciliation, maintenance, token creation, or every acceptance scenario in the contributor evaluation guide.
- Exact host and Copilot versions were not captured, so this record should not be used as a build-specific compatibility claim.
