<!-- fleet job=guide-refresh id=Gameplay-FRTW-Game status=done turns=15 usd=0.0150 tokens(read,write,in,out)=[352061, 50781, 32, 10169] model=claude-haiku-5-5 -->
# notes/Build Guides/Gameplay/FRTW Game.md

**Verdict:** minor drift. The per-function rows and the `wire` claim still match the label table. The header counts and the source-shard list are stale because shard S0802 added two `frtwgame` labels after the note was generated.

**Corrections:**

1. `old:` 282 accepted functions: 168 confirmed, 78 likely, 0 speculative, 36 unknown. Network-linked (`wire`): 0.
   `new:` 284 accepted functions: 169 confirmed, 79 likely, 0 speculative, 36 unknown. Network-linked (`wire`): 0.
   `why:` client label table (`client_sql`, `label` where subsystem LIKE '%frtwgame%'): 284 rows, all `accepted`. Display 54 confirmed / 42 likely / 11 unknown; scaleform 115 / 37 / 25. Totals are 169 / 79 / 0 / 36. Every row has `wire` = `[]`, so "0" holds. The two extra rows are from S0802 (see correction 3).

2. `old:` Subsystems: `ui.frtwgame.scaleform` (175), `game.frtwgame.display` (107)
   `new:` Subsystems: `ui.frtwgame.scaleform` (177), `game.frtwgame.display` (107)
   `why:` `label` rows by subsystem: `ui.frtwgame.scaleform` = 177, `game.frtwgame.display` = 107. The +2 are `01746d40` (likely, GuiFlashMapCleanup) and `01746da0` (confirmed, GuiFlashListCleanup), both shard S0802 (`client_sql`, `label.shard`). Neither address appears in the note (`repo` search for 01746d40 / 01746da0 finds nothing).

3. `old:` [[S0659 01253f30-01257d60|S0659]] (208), [[S0661 0125d190-012619f0|S0661]] (19), [[S0662|S0662]] (55)
   `new:` [[S0659 01253f30-01257d60|S0659]] (208), [[S0661 0125d190-012619f0|S0661]] (19), [[S0662|S0662]] (55), S0802 (2)
   `why:` `label.shard` counts for frtwgame: S0659 208, S0661 19, S0662 55, S0802 2 (`client_sql`). There is no `notes/Native Map/Shards/S0802*` note, so S0802 is left unlinked. The 208 / 19 / 55 figures match the note.

**Unsure:**
- The per-function rows in both tables match the labels I spot-checked (for example `01254d70`, `012551c0`, `01265120`, `012655b0`, `01260690`, `01264270`, `01257200`, `01253f30`). I did not check every row. The `fn.bytes` length column in the client DB did not give a usable byte count, so I did not verify the "6 bytes" claims.
- The "How it works" section is a placeholder ("Not written yet"). That is a status statement, not a code claim, so I left it.
- Outside this note: `notes/Build Guides/Build Guides.md:24` says "282 functions (168 confirmed, 78 likely)". It has the same stale count, but it is a different note and I did not edit it.
