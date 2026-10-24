<!-- fleet job=pin-audit id=tests-derby-chapter-rs status=done turns=4 usd=0.0020 tokens(read,write,in,out)=[12688, 8287, 10, 1598] model=claude-haiku-5-5 -->
# tests/derby_chapter.rs

**prototype/osfr-tools/tests/derby_chapter.rs:613 derby_chapter test (the test containing the line; the `assert_eq!(live_coins, before_coins + 2 * COMPLETION_COINS)` assertion) - pins `25` from `data/content/derby_entry.json` `completion_reward_coins`.**
- The local `const COMPLETION_COINS: u32 = 25;` (derby_chapter.rs:74) is a hand-copied literal of the shipped data value. Retuning `derby_entry.json` would fail this assertion even though the payout code is correct.
- **Fix:** read it through the data row: load `data/content/derby_entry.json` (the test already loads that file in its fixture setup near line 94) and take `completion_reward_coins` from it, then assert `before_coins + 2 * completion_reward_coins`. Do not keep the literal constant.

**prototype/osfr-tools/tests/derby_chapter.rs:614 derby_chapter test (the `assert_eq!(live_xp, before_xp + 2 * COMPLETION_XP)` assertion) - pins `10` from `data/content/derby_entry.json` `completion_reward_xp`.**
- Same cause: `const COMPLETION_XP: u32 = 10;` (derby_chapter.rs:75) mirrors the shipped `completion_reward_xp`.
- **Fix:** read `completion_reward_xp` from the `derby_entry.json` row the test already loads, and assert `before_xp + 2 * completion_reward_xp`.

Note: the same literal constants also feed other assertions in this file (lines 571, 576, 908, 911, 1005, 1017, 1018). They were not on the screened list, so I did not rule on them; if they are edited, switch them to the same data read.
