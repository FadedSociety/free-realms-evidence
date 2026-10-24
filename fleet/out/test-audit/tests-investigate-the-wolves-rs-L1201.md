<!-- fleet job=test-audit id=tests-investigate-the-wolves-rs-L1201 status=done turns=5 usd=0.0047 tokens(read,write,in,out)=[35696, 16068, 12, 4594] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/investigate_the_wolves.rs lines 1201-1379 of 1379

Window 1201-1379 of `repo:prototype/osfr-tools/tests/investigate_the_wolves.rs` (test `the_quest_record_text_giver_and_battle_resolve`). Four findings. The record, Anne, Adventurer-union and reward-evidence checks are real checks against the fixture JSON, so they are not findings.

- **[medium] prototype/osfr-tools/tests/investigate_the_wolves.rs:1368-1370 the_quest_record_text_giver_and_battle_resolve - `for id in [TITLE, INTRO, DESCRIPTION, END_TEXT] { assert!(id != 0); }` compares file-level constants with 0 and never touches the engine, the JSON or the locale table.**
  - Why it cannot catch a regression: the constants are all non-zero literals, so the assertion is a tautology. Any change to the quest record, the loader or the locale file that zeroes or drops these ids still passes it. It also repeats the id checks already made at 1222-1223 and 1326-1329.
  - Fix: delete the loop, or assert on the real values: `engine.title_string_id(QUEST) == Some(TITLE)` is already there, so add `texts.get(&id).is_some()` for each id in that array, and assert the record's `end_text_string_id` / `intro_text_string_id` equal the constants (already done at 1222-1224).

- **[medium] prototype/osfr-tools/tests/investigate_the_wolves.rs:1358-1363 the_quest_record_text_giver_and_battle_resolve - INTRO and DESCRIPTION are only checked to be non-empty, while TITLE, END_TEXT and GOAL_TEXT are pinned to exact strings.**
  - Why it cannot catch a regression: a locale-table change that swaps the intro or description to a different, wrong, or placeholder non-empty string (for example the text of another id) still passes. The packet-level check at 1327-1329 only compares ids, so nothing checks what the player sees for these two ids.
  - Fix: pin the expected strings for 101_014 and 101_016 the same way as lines 1350-1357 and 1364-1367, after reading them from the locale report. Keep the non-empty check only as a fallback.

- **[medium] prototype/osfr-tools/tests/investigate_the_wolves.rs:1201-1203 (doc) and 1314-1318 the_quest_record_text_giver_and_battle_resolve - the doc and the section comment say the battle "resolves through the split loader", but the battle is only read as raw JSON from `field_battles.json` via `battle_row()`.**
  - Why it cannot catch a regression: `QuestEngine::from_split_content` is never asked about BATTLE (no encounter or objective query exists in the engine calls at 1321-1334). If the loader drops or mis-indexes encounter 12350, or the quest engine stops linking objective `encounter_id` to a field battle, the test still passes because it only checks the file row and the record's `encounter_id` constant.
  - Fix: after building the engine, assert the engine's view of the battle (the encounter/objective lookup that the loader uses for quest 3000061), or rename the test and doc to say it checks the authored battle row only.

- **[low] prototype/osfr-tools/tests/investigate_the_wolves.rs:1331 the_quest_record_text_giver_and_battle_resolve - `assert_eq!(end.len(), 99)` pins the whole 49/13 packet length.**
  - Why it cannot catch a regression: the test is about the quest's record, text and reward, not the packet's total size. Any unrelated trailing field added to the end packet makes this fail (churn), while the offset checks at 1332-1335 already cover the fields that matter.
  - Fix: drop the length assertion, or move it to the packet-format test that owns the 49/13 layout. Keep the offset checks at 14, 18, 27 and 31.
