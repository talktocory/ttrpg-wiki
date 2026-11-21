# Adventure Walkthrough: Recording Runbook

Follow [the shared recording standards](../shared/recording-standards.md) and [adventure demonstration plan](../shared/adventure-demo-plan.md).

## Recording workspace

Use the final clean local state produced by one of the setup-video demo repositories. Do not record from the framework-development checkout or a real campaign.

Before recording:

1. Confirm the demo campaign has an approved `campaign.yaml` and no adventure-derived wiki pages.
2. Stage an authorized copy, public preview, or creator-prepared excerpt of *The Forgotten Circus* under `raw/pdfs/`.
3. Record the exact filename, selected page range, and named sections in the prompt below.
4. Ensure the source PDF will not be added to a remote later, published, or included in public downloads.
5. Confirm the working tree baseline makes the later wiki diff easy to read.
6. Confirm the selected agent can read the PDF and save files in the demo repository.
7. Open the files needed for the folder tour and close unrelated editor tabs.
8. Disable or hide notifications and account-identifying UI.
9. Increase Explorer, Source Control, Markdown Preview, and agent-chat text to a legible recording size.

## Ingest prompt

> Use ttrpg-wiki-ingest to ingest [raw/pdfs/filename.pdf], limited to [page range or named sections]. Treat this as unplayed adventure preparation. Show me the exact proposed wiki changes before saving anything, keep future events and secrets GM-only, and cite the relevant source sections.

## Approval prompt

> The proposed changes are approved. Please proceed with the appropriate wiki updates.

## Rehearsal checks

- The selected PDF pages are readable in the recording environment.
- The ingest proposal covers only the rehearsed source sections.
- Prepared scenes and outcomes are Draft or Unused rather than played events.
- Private backstory, motives, clues, and future choices remain GM-only.
- Concise wiki notes cite the source instead of reproducing substantial adventure text.
- Codex proposes exact wiki destinations before editing them.
- No wiki files change during the proposal stage.
- Approval causes the expected wiki files, `wiki/index.md`, and `wiki/log.md` to change.
- Markdown links work in Preview.
- The Source Control diff is short enough to explain on screen.
- The complete workflow fits the target time after waits are removed.
- The final edit does not expose unintended spoilers or commercial source pages.

## Reset between takes

Return the separate demo repository to its recorded clean baseline using a safe, rehearsed reset method. Verify the exact repository path before discarding any changes. Never use the framework-development checkout or a real campaign as the reset target.

## Expected variability

The agent may phrase its proposal differently between takes. Judge the result by the workflow requirements rather than expecting identical prose. If the output introduces unsupported facts, treats preparation as played history, reproduces too much source text, or skips proposal-first review, stop the take and correct the prompt or demo baseline before recording again.
