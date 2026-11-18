# Tell the Assistant About Your Campaign

Your campaign settings help the assistant use the right game, tone, and table preferences. They are saved in [campaign.yaml](../campaign.yaml), a small text file. You can ask the assistant to prepare it for your review rather than editing it yourself.

## Start with what you know

> Help me set up this campaign. Ask me about its name, game and edition, tone, and usual session length. Suggest sensible settings for what I tell you, leave undecided details open, and show me the proposed changes before saving them.

You can also provide everything in one message. You do not need to decide every setting before your first session.

| Tell it about… | Why it helps |
| --- | --- |
| Campaign name, premise, genre, and tone | Keeps summaries and preparation appropriate to your game |
| Game system and edition | Identifies which mechanics need checking |
| Rules references and house rules | Separates published procedures from your table's decisions |
| Preferred terms and language | Uses the names your group uses |
| Session length and table preferences | Shapes how much material to prepare and how to present it |
| Rewards you track | Supports money, reputation, supplies, or other resources without mixing them together |
| Maps and virtual tabletop, if used | Sets grid type, scale, and image requirements |
| Artwork preferences, if used | Sets visual style, token shape/size, and images per review round |

## Leave optional choices for later

No game selected yet? The assistant can organize fiction and ideas while flagging mechanics that still need checking. A system name alone does not give it access to the rules: provide relevant material you are authorized to use or suitable references.

You do not need a reward budget, a virtual tabletop, or AI-generated artwork. You can leave these unset and add them later. Reward units are kept separate; the assistant will not turn reputation or favors into money without an approved policy.

For maps, a grid does not automatically mean five feet, one meter, or any other distance. Tell the assistant your preferred scale when it matters. The default artwork allowance is one image per review round; changing that setting does not order images or authorize a paid service.

## If you prefer to edit the file

Keep the existing headings and indentation, and change the values you understand. `null` means a choice has not been set. `[]` means there are no entries yet. Text values can be put in quotes. Ask the assistant to check your proposed edits if you are unsure.

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

To add rules references or house rules, put each entry on its own indented line under the relevant field instead of `[]`. Reference a file that actually exists in your copy, or an appropriate official URL. The assistant can help choose and format the entries.

## What each setting means

| Section | Fields and choices |
| --- | --- |
| `campaign` | `name`, `premise`, `genre`, `tone`, and `language` describe the game you want to run. |
| `system` | `name` and `edition` identify the rules. `references` lists sources, `house_rules` records your approved changes, and `profile` can point to an optional Markdown guidance file within the project. |
| `terminology` | `gm`, `player_character`, and `advancement` are the words the assistant should use for those concepts. |
| `table` | `session_minutes` is the usual session length, or `null` if undecided. `preferences` is a list of presentation or table preferences. |
| `rewards` | `units` lists resources you track. `period` names how to group awards, such as session or mission. `budgets` is optional; each target has a `period`, `unit`, and nonnegative `target`. A budget's unit must appear in `units`. |
| `vtt` | `profile` can point to optional VTT guidance. `grid` is `none`, `square`, `hex`, or `zones`. Set `distance_unit`, `distance_per_cell`, and `pixels_per_cell` when needed; otherwise leave them `null`. Physical scale and image resolution are separate choices. |
| `artwork` | `style` describes the look you want. `token_shape` is `circle` or `square`; `token_pixels` sets the intended token size (8–8192 pixels). `map_format` is `jpg` or `png`. `images_per_round` is a positive whole-number generation allowance, defaulting to one. |
| `workflow` | Keep `approval` as `proposal-first`. `integrations` can list tools you intend to use, but naming a tool does not install it or give the assistant access to it. |

For generated images, describe your preferred visual style, then agree any map footprint and scale with the assistant for that particular scene. The image tool may not return the requested dimensions exactly, so actual exports still need checking. The optional token-processing script has its own command options; the assistant must pass your chosen settings when using it.

## Keep the rest of the file in place

The file's groups are `campaign`, `system`, `terminology`, `table`, `rewards`, `vtt`, `artwork`, and `workflow`. `schema_version` identifies the settings format and should stay unchanged. Keep `workflow.approval` set to `proposal-first` so the assistant shows campaign changes before saving them.

An optional **profile** is a short note with extra guidance for a game or virtual tabletop. The [profile folder](../profiles/README.md) has starting examples. You can ignore profiles until you need one; they do not install tools or include rulebooks. Your explicit campaign choices and approved house rules take precedence over suggested profile defaults.

For people using the [optional validator](scripts.md#validatepy): it checks field names, value types, positive dimensions, reward-budget units, and profile paths. This check is optional for ordinary campaign work. Utility developers can find the full supported settings in [validate_config](../scripts/wiki_tools.py).

When updating the project, preserve your campaign settings rather than replacing this file with the blank copy from a new download.
