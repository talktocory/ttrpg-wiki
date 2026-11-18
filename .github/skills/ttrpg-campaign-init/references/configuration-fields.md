# Campaign Configuration Fields

Preserve the existing structure and types in `campaign.yaml`. A blank string means an optional description has not been supplied, `null` means a nullable choice is undecided, and an empty list means no entries are configured.

| Section | Fields |
| --- | --- |
| `campaign` | `name`, `premise`, `genre`, `tone`, `language` |
| `system` | `name`, `edition`, `profile`, `references`, `house_rules` |
| `terminology` | `gm`, `player_character`, `advancement` |
| `table` | `session_minutes`, `preferences` |
| `rewards` | `units`, `period`, `budgets` |
| `vtt` | `profile`, `grid`, `distance_unit`, `distance_per_cell`, `pixels_per_cell` |
| `artwork` | `style`, `token_shape`, `token_pixels`, `map_format`, `images_per_round` |
| `workflow` | `approval`, `integrations` |

Keep `schema_version: 1`. Do not add or remove top-level sections or fields. Campaign name and reward period must be nonempty. List entries must be nonempty strings except reward budgets, which are mappings with exactly `period`, `unit`, and `target`.

System name, edition, and profile; VTT profile, distance unit, distance per cell, and pixels per cell; and session minutes may be `null`. All other scalar fields use their existing string or numeric types. Session minutes and configured VTT distances or resolutions must be positive. Artwork token size must be a whole number from 8 through 8192, and images per round must be a positive whole number.

Use only these controlled values:

- `vtt.grid`: `none`, `square`, `hex`, or `zones`;
- `artwork.token_shape`: `circle` or `square`;
- `artwork.map_format`: `jpg` or `png`; and
- `workflow.approval`: `proposal-first`.

Profile values are project-relative paths to existing Markdown files. Rules references are authorized local paths or appropriate official URLs; listing one does not make an inaccessible source available. House rules are only rules the GM has approved.

Reward units must be unique. Each budget needs a nonempty period, a unit already listed in `rewards.units`, and a finite nonnegative target. Do not add unrelated units together or invent a budget because a campaign tracks rewards.

Grid scale and image resolution are independent. Do not infer a distance from a grid type. Integration names record intended tools only; they do not install, connect, authorize, or grant access to those tools.
