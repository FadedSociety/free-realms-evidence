<!-- fleet job=pin-audit id=tests-gameplay-rs status=done turns=6 usd=0.0048 tokens(read,write,in,out)=[45269, 24494, 14, 2570] model=claude-haiku-5-5 -->
# tests/gameplay.rs

**prototype/osfr-tools/tests/gameplay.rs:103 private_complete_loop_reward_once_atomic_bundle_and_fresh_restore - pins `25` from the gameplay content `quests.json` (quest id 900001, `definitions[].coins`).**
- The 25 is the quest-900001 coin reward. `scripts/prepare-gameplay-quests.py:153` writes it as `"coins": 25` into `quests.json`, the file the test loads through `OSFR_GAMEPLAY_CONTENT` at line 67. Retuning that row would break the assertion while the reward path is still correct. The reward is also repeated as a literal in `tests/economy_review.rs:44` (`QUEST_ID` comment), so that file has the same pin.
- Fix: read it through the content row. Load `quests.json` from `content` and take `coins` from the definition with `id == 900001`, then assert `progress.inventory.coins == that value` (or bound it as `> 0`). Do not hard-code 25.

Not findings:
- `gameplay.rs:136` `assert!(gateway.handle_at(&bundle, clock + 1600).is_err())`: 1600 is just a clock offset the test chose. The expected error comes from the invalid equip child inside the bundle, not from any session or bundle timeout. The README's 60-second idle expiry is not what this line checks, so there is no data value pinned.
