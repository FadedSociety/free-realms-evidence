<!-- fleet job=pin-audit id=tests-live-events-rs status=done turns=11 usd=0.0053 tokens(read,write,in,out)=[114065, 18824, 24, 3589] model=claude-haiku-5-5 -->
# tests/live_events.rs

**tests/live_events.rs:285 the_hunt_...(test at lines 269-297) - pins `50` from `data/content/quests/scavenger_hunt.json` `records[id 3000200].rewards[0].coins`.**
- **Fix:** read it through the row: `read_json` on `quests/scavenger_hunt.json`, find record `3000200`, take `rewards[0]["coins"]`. `support/quest_records.rs::read_quests` does not expose rewards, so the test must read the row itself. The `finish_quest(..., 50, 25, now)` argument at line 277 has the same literal and should use the same value.

**tests/live_events.rs:286 the_hunt_...(same test) - pins `25` from `data/content/quests/scavenger_hunt.json` `records[id 3000200].rewards[0].job_xp["1"]`.**
- **Fix:** read it through the row: `rewards[0]["job_xp"]["1"]` (profile 1 is Adventurer, `ADVENTURER`). Use it here and in the `finish_quest(..., 25, now)` argument at line 277.

Both assertions are absolute checks, valid only because the fixture starts at zero coins and zero Adventurer XP, which the test does not state. Reading the row keeps them correct when the payout is retuned.
