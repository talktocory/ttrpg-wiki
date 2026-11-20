# Tell the Assistant About Your Campaign

Your campaign settings help the assistant use the right game, tone, and table preferences. They are saved in [campaign.yaml](../campaign.yaml), a small text file. The `ttrpg-campaign-init` skill can guide the initial setup or help complete a partially configured file.

## Start with what you know

> Use ttrpg-campaign-init.

On hosts that expose skills as slash commands, `/ttrpg-campaign-init` is sufficient. The skill already instructs the assistant to preserve existing choices, ask for essential settings, and show a proposal before saving.

The assistant should begin with the campaign, system, language or terminology, session length, and table preferences. It should ask about rules references, rewards, VTT use, artwork, and integrations only when they matter to your campaign or when you request a comprehensive setup. You can also provide everything you know in one message; it should not ask for the same details again. You do not need to decide every setting before your first session.

After the interview, review the proposed field-level changes. The assistant should leave undecided values open and wait for your approval before editing `campaign.yaml`. You may approve all or only part of the proposal.

> The proposed campaign settings are approved. Please update campaign.yaml and record the change in wiki/log.md.

| Tell the assistant about | Why it matters |
| --- | --- |
| Campaign name, premise, genre, and tone | Keeps summaries and preparation appropriate to your game |
| Game system and edition | Identifies which mechanics need checking |
| Rules references and house rules | Separates published procedures from your table's decisions |
| Preferred terms and language | Uses the names your group uses |
| Session length and table preferences | Shapes how much material to prepare and how to present it |
| Rewards you track | Supports money, reputation, supplies, or other resources without mixing them together |
| Maps and virtual tabletop, if used | Sets grid type, scale, and image requirements |
| Artwork preferences, if used | Sets visual style, token shape and size, and images per review round |

## Leave optional choices for later

If you have not selected a game yet, the assistant can still organize fiction and ideas while flagging mechanics that need verification. A system name alone does not give it access to the rules; provide relevant material you are authorized to use or suitable references.

You do not need a reward budget, a virtual tabletop, or AI-generated artwork. You can leave these unset and add them later. Reward units are kept separate; the assistant will not turn reputation or favors into money without an approved policy.

For maps, a grid does not automatically mean five feet, one meter, or any other distance. Tell the assistant your preferred scale when it matters. The default artwork allowance is one image per review round; changing that setting does not order images or authorize a paid service.

## If you prefer to edit the file

Keep the existing headings and indentation, and change the values you understand. `null` means a choice has not been set. `[]` means there are no entries yet. Text values may be enclosed in quotation marks. Ask the assistant to check your proposed edits if you are unsure.

## Example: your first settings

Here is an example of the `campaign`, `system`, and `table` sections. Replace the sample text with your own choices, and keep the other sections already present in the file. This is an example to copy selectively, not a complete replacement for `campaign.yaml`.

```yaml
campaign:
  name: "Our Thursday Game"
  premise: "Travelers investigating a string of disappearances"
  genre: "mystery"
  tone: "Uneasy discoveries, with room for humor"
  language: "English"
system:
  name: "Your game"
  edition: "Your edition"
  profile: null
  references: []
  house_rules: []
table:
  session_minutes: 180
  preferences:
    - "Flexible scenes with several possible approaches"
    - "Short notes I can scan at the table"
```

To add rules references or house rules, put each entry on its own indented line under the relevant field instead of `[]`. Refer to a file that exists in your copy or to an appropriate official URL. The assistant can help choose and format the entries.

## What each setting means

| Section | Fields and choices |
| --- | --- |
| `campaign` | `name`, `premise`, `genre`, `tone`, and `language` describe the game you want to run. |
| `system` | `name` and `edition` identify the rules. `references` lists sources, `house_rules` records your approved changes, and `profile` can point to an optional Markdown guidance file within the project. |
| `terminology` | `gm`, `player_character`, and `advancement` are the words the assistant should use for those concepts. |
| `table` | `session_minutes` is the usual session length, or `null` if undecided. `preferences` is a list of presentation or table preferences. |
| `rewards` | `units` lists resources you track. `period` names how to group awards, such as session or mission. `budgets` is optional; each target has a `period`, `unit`, and nonnegative `target`. A budget's unit must appear in `units`. |
| `vtt` | `profile` can point to optional VTT guidance. `grid` is `none`, `square`, `hex`, or `zones`. Set `distance_unit`, `distance_per_cell`, and `pixels_per_cell` when needed; otherwise leave them `null`. Physical scale and image resolution are separate choices. |
| `artwork` | `style` describes the look you want. `token_shape` is `circle` or `square`; `token_pixels` sets the intended token size (8–8192 pixels). `map_format` is `jpg` or `png`. `images_per_round` is the positive whole number of images allowed in each review round; the default is one. |
| `workflow` | Keep `approval` as `proposal-first`. `integrations` can list tools you intend to use, but naming a tool does not install it or give the assistant access to it. |

For generated images, describe your preferred visual style, then agree on the map footprint and scale for that particular scene. The image tool may not return the requested dimensions exactly, so the exported file still needs to be checked. The optional token-processing script has its own command options; the assistant must pass your chosen settings when using it.

## Keep the rest of the file in place

The file's groups are `campaign`, `system`, `terminology`, `table`, `rewards`, `vtt`, `artwork`, and `workflow`. `schema_version` identifies the settings format and should stay unchanged. Keep `workflow.approval` set to `proposal-first` so the assistant shows campaign changes before saving them.

An optional **profile** is a short note with extra guidance for a game or virtual tabletop. The [profile folder](../profiles/README.md) has starting examples. You can ignore profiles until you need one; they do not install tools or include rulebooks. Your explicit campaign choices and approved house rules take precedence over suggested profile defaults.

The [optional validator](scripts.md#validatepy) checks field names, value types, positive dimensions, reward-budget units, and profile paths. You do not need to run it for ordinary campaign work. Utility developers can find the complete set of supported settings in [validate_config](../scripts/wiki_tools.py).

When updating the project, preserve your campaign settings rather than replacing this file with the blank copy from a new download.
