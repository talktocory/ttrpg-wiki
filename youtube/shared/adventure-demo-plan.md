# Adventure Demonstration Plan

## Source

Use *The Forgotten Circus: A Cursed One-Shot Adventure* as the authentic source material for the walkthrough.

The commercial PDF is not stored in this repository. Stage an authorized copy, public preview, or purpose-made recording excerpt only in the separate local recording workspace under `raw/pdfs/`.

## Demonstration goal

Show how TTRPG Wiki turns part of a published adventure into useful private GM preparation without treating planned scenes as played events or copying the entire source into the wiki.

## Focused ingestion scope

Use a small, coherent selection rather than ingesting the full adventure during recording. The preferred slice is:

1. Adventure at a Glance
2. Act 1
3. One or two NPC sections needed for Act 1

Confirm the final page range against the exact recording PDF. Name those pages or sections in the prompt so the proposal and Git diff remain reviewable.

## Expected wiki treatment

- Preserve the original PDF in `raw/pdfs/`.
- Record prepared encounters, locations, and possible outcomes as `Unused` or `Draft`, as appropriate.
- Do not create a played-session record for events that have not happened.
- Keep GM-only backstory, motives, clues, and future choices private.
- Link concise preparation notes back to the named source sections rather than reproducing substantial adventure text.
- Use the game and edition already approved in `campaign.yaml` before discussing mechanics.

## Spoiler and product-value policy

- Display only the pages needed to explain the workflow.
- Avoid lingering on complete adventure text, maps, stat blocks, solutions, or final-act revelations.
- Add a brief GM-facing spoiler notice.
- Prefer a creator-prepared excerpt or publicly available preview for unrestricted screen capture.
- Do not include the commercial PDF in this repository, a remote demo repository, downloads, or video attachments.

## Baseline ingest prompt

Replace the bracketed values after the final recording excerpt is chosen.

> Use ttrpg-wiki-ingest to ingest [raw/pdfs/filename.pdf], limited to [page range or named sections]. Treat this as unplayed adventure preparation. Show me the exact proposed wiki changes before saving anything, keep future events and secrets GM-only, and cite the relevant source sections.

## Approval prompt

> The proposed changes are approved. Please proceed with the appropriate wiki updates.

Use a precise partial approval instead when rehearsal shows that only part of the proposal belongs in the walkthrough.
