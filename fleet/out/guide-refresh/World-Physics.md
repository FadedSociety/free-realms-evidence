<!-- fleet job=guide-refresh id=World-Physics status=done turns=27 usd=0.0259 tokens(read,write,in,out)=[822382, 60926, 56, 20070] model=claude-haiku-5-5 -->
# notes/Build Guides/World/Physics.md

**Verdict:** minor drift. The per-function rows, names, confidences, subsystem and class subtotals, shard counts and the "wire: 0" claim all match the label store (`client_sql`). The summary counts at the top are a stale snapshot of the label store, which now holds more accepted functions for these subsystems than the note reports. "How it works" is still an unwritten placeholder, which is accurate.

**Corrections:**

1. `old:` 334 accepted functions: 106 confirmed, 84 likely, 91 speculative, 53 unknown. Network-linked (`wire`): 0.
   `new:` 1344 accepted functions: 510 confirmed, 634 likely, 143 speculative, 57 unknown. Network-linked (`wire`): 0.
   `why:` The label store has 1344 accepted rows for `lib.bullet` and the `physics*` subsystems listed on the next line (994 + 107 + 82 + 83 + 36 + 26 + 8 + 8), with confidences 510 / 634 / 143 / 57 (`client_sql`, label table, status `accepted`, pass 1). Every row has an empty `wire` array, so the "0" stands. The note's tables list only a subset of shards (see "Source shards"), e.g. S0550 and S0607-S0626 are absent, so the header describes an old generation run.

2. `old:` Subsystems: `lib.bullet` (99), `physics.dynamics` (80), `physics.collision` (52), `physics.query` (31), `physics.shape` (31), `physics` (25), `physics.ship` (8), `physics.mesh` (8)
   `new:` Subsystems: `lib.bullet` (994), `physics.dynamics` (107), `physics.collision` (82), `physics.query` (83), `physics.shape` (36), `physics` (26), `physics.ship` (8), `physics.mesh` (8)
   `why:` Label-store counts by `subsystem` (`client_sql`). The `physics.ship` and `physics.mesh` counts still match. The note's per-section subtotals (e.g. `lib.bullet` 99, `physics.collision` 52, `physics.ship` 8, `physics.mesh` 8) add up to its own tables, so only the generator's scope is stale, not the rows.

**Unsure:**
- Whether the 334-row scope is deliberate. The tables and "Source shards" list are internally consistent (shard subtotals match the label store for the shards they name). If the generator is meant to cover only those shards, correction 1 should instead say the table is a shard-limited subset. I did not find a scope statement in the note.
- `physics.vehicle` (166 accepted rows in the label store: 28 confirmed, 44 likely, 76 speculative, 18 unknown) is not in the note's subsystem list. It may belong to the Kart Racing note; I did not check that note.
- The `physics.dynamics` section (80 rows) and its per-class subtotals were not checked row by row. Sampled rows in the other sections all matched the label store (names, confidences, subsystems).
- The note makes no claims about `repo` code paths or `path:line`, so no repo-side correction was needed.
