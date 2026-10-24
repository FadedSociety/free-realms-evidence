<!-- fleet job=pin-audit id=tests-scavenger-hunt-two-players-rs status=done turns=8 usd=0.0069 tokens(read,write,in,out)=[94555, 23364, 18, 6049] model=claude-haiku-5-5 -->
# tests/scavenger_hunt_two_players.rs

The hunt's reward is the shipped record `data/content/quests/scavenger_hunt.json` (record id 3000200), `records[0].rewards[0]`: `coins: 50` and `job_xp: {"1": 25}`. The fixtures don't set it. `fresh_in` loads the real bundled content, and `finish_quest` / `end_screen_reward` only take the values the test passes in. Every listed literal 50 or 25 is therefore that data value, and each one would break on a retune while the code stays correct. Lines 309 and 332 are `a_coins_before + 50`, and 310 is `a_xp_before + 25`; the 50/25 is the same data value added to a fixture-set baseline.

- **tests/scavenger_hunt_two_players.rs:280 test_name (the two-player reward test, the one that starts at line ~240) - pins `50` and `25` from `data/content/quests/scavenger_hunt.json` `records[0].rewards[0].coins` / `job_xp["1"]`.**
  **Fix:** read the row through the `hunt` / `reward` lookup already built at lines 659-663 (move it to a shared `hunt_reward()` helper in `tests/support/scavenger_hunt.rs`) and compare `end_screen_reward(&a_screen)` to `(reward["coins"], reward["job_xp"]["1"])`.

- **tests/scavenger_hunt_two_players.rs:281 test_name (same test as 280) - pins `50` and `25` from `scavenger_hunt.json` `rewards[0].coins` / `job_xp["1"]`.**
  **Fix:** same as 280: compare to the row values from `hunt_reward()`.

- **tests/scavenger_hunt_two_players.rs:309 test_name (same test as 280) - pins `50` from `scavenger_hunt.json` `rewards[0].coins`.**
  **Fix:** `a_coins_before + reward_coins`, with `reward_coins` read from the row.

- **tests/scavenger_hunt_two_players.rs:310 test_name (same test as 280) - pins `25` from `scavenger_hunt.json` `rewards[0].job_xp["1"]`.**
  **Fix:** `a_xp_before + reward_xp`, with `reward_xp` read from the row.

- **tests/scavenger_hunt_two_players.rs:326 test_name (same test as 280) - pins `50` from `scavenger_hunt.json` `rewards[0].coins`.**
  **Fix:** compare to `reward_coins` from the row.

- **tests/scavenger_hunt_two_players.rs:327 test_name (same test as 280) - pins `25` from `scavenger_hunt.json` `rewards[0].job_xp["1"]`.**
  **Fix:** compare to `reward_xp` from the row.

- **tests/scavenger_hunt_two_players.rs:332 test_name (same test as 280) - pins `50` from `scavenger_hunt.json` `rewards[0].coins`.**
  **Fix:** `a_coins_before + reward_coins`.

- **tests/scavenger_hunt_two_players.rs:364 test_name (same suite, later in the file) - pins `50` from `scavenger_hunt.json` `rewards[0].coins`.**
  **Fix:** `a_coins_before + reward_coins`.

- **tests/scavenger_hunt_two_players.rs:365 test_name (same suite) - pins `50` from `scavenger_hunt.json` `rewards[0].coins`.**
  **Fix:** compare to `reward_coins`.

- **tests/scavenger_hunt_two_players.rs:527 test_name (same suite) - pins `50` from `scavenger_hunt.json` `rewards[0].coins`.**
  **Fix:** compare to `reward_coins`.

- **tests/scavenger_hunt_two_players.rs:528 test_name (same suite) - pins `50` from `scavenger_hunt.json` `rewards[0].coins`.**
  **Fix:** compare to `reward_coins`.

- **tests/scavenger_hunt_two_players.rs:529 test_name (same suite) - pins `25` from `scavenger_hunt.json` `rewards[0].job_xp["1"]`.**
  **Fix:** compare to `reward_xp`.

- **tests/scavenger_hunt_two_players.rs:530 test_name (same suite) - pins `25` from `scavenger_hunt.json` `rewards[0].job_xp["1"]`.**
  **Fix:** compare to `reward_xp`.

- **tests/scavenger_hunt_two_players.rs:547 test_name (same suite) - pins `50` from `scavenger_hunt.json` `rewards[0].coins`.**
  **Fix:** compare to `reward_coins`.

- **tests/scavenger_hunt_two_players.rs:548 test_name (same suite) - pins `50` from `scavenger_hunt.json` `rewards[0].coins`.**
  **Fix:** compare to `reward_coins`.

- **tests/scavenger_hunt_two_players.rs:549 test_name (same suite) - pins `25` from `scavenger_hunt.json` `rewards[0].job_xp["1"]`.**
  **Fix:** compare to `reward_xp`.

- **tests/scavenger_hunt_two_players.rs:550 test_name (same suite) - pins `25` from `scavenger_hunt.json` `rewards[0].job_xp["1"]`.**
  **Fix:** compare to `reward_xp`.

- **tests/scavenger_hunt_two_players.rs:578 test_name (same suite) - pins `(50, 25)` from `scavenger_hunt.json` `rewards[0].coins` / `job_xp["1"]`.**
  **Fix:** compare to `(reward_coins, reward_xp)` from the row.

- **tests/scavenger_hunt_two_players.rs:579 test_name (same suite) - pins `(50, 25)` from `scavenger_hunt.json` `rewards[0].coins` / `job_xp["1"]`.**
  **Fix:** compare to `(reward_coins, reward_xp)` from the row.

- **tests/scavenger_hunt_two_players.rs:649 test_name (same suite) - pins `50` from `scavenger_hunt.json` `rewards[0].coins`.**
  **Fix:** compare to `reward_coins`.

- **tests/scavenger_hunt_two_players.rs:650 test_name (same suite) - pins `25` from `scavenger_hunt.json` `rewards[0].job_xp["1"]`.**
  **Fix:** compare to `reward_xp`.

- **tests/scavenger_hunt_two_players.rs:653 test_name (same suite) - pins `50` from `scavenger_hunt.json` `rewards[0].coins`.**
  **Fix:** compare to `reward_coins`.

- **tests/scavenger_hunt_two_players.rs:654 test_name (same suite) - pins `25` from `scavenger_hunt.json` `rewards[0].job_xp["1"]`.**
  **Fix:** compare to `reward_xp`.

- **tests/scavenger_hunt_two_players.rs:664 test_name (the shipped-data test at lines ~656-666) - pins `50` from `scavenger_hunt.json` `records[0].rewards[0].coins`.** This one reads the row and then asserts the exact shipped value, so it pins the tunable itself.
  **Fix:** bound it, e.g. `reward["coins"].as_u64().unwrap() > 0`, and keep the structural checks (`items == []`, the job id key "1").

- **tests/scavenger_hunt_two_players.rs:665 test_name (same as 664) - pins `{"1": 25}` from `scavenger_hunt.json` `records[0].rewards[0].job_xp`.**
  **Fix:** assert `job_xp` has key "1" with a positive integer value, and that the profile key is 1 (ADVENTURER).

- **tests/scavenger_hunt_two_players.rs:710 test_name (the later hunt test) - pins `(50, 25)` from `scavenger_hunt.json` `rewards[0].coins` / `job_xp["1"]`.**
  **Fix:** compare to `(reward_coins, reward_xp)` from the row.

- **tests/scavenger_hunt_two_players.rs:713 test_name (same as 710) - pins `50` from `scavenger_hunt.json` `rewards[0].coins`.**
  **Fix:** compare to `reward_coins`.

- **tests/scavenger_hunt_two_players.rs:714 test_name (same as 710) - pins `25` from `scavenger_hunt.json` `rewards[0].job_xp["1"]`.**
  **Fix:** compare to `reward_xp`.

Shared fix: add a helper (for example `hunt_reward() -> (u32, u32)` in `tests/support/scavenger_hunt.rs`) that reads `quests/scavenger_hunt.json` `records[0].rewards[0]` via `read_json(&content_dir()...)`, and use it in every assertion above. The existing `read_json` / `content_dir` helpers are in `tests/support/npc_quest_chain.rs`.

I did not open every listed line individually (e.g. 364, 527-550, 578, 710). The screen gives the literal 50/25 on each, and the fixture doesn't set the reward, so they are treated as findings on that basis.
