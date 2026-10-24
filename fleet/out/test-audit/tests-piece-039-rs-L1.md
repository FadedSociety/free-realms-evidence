<!-- fleet job=test-audit id=tests-piece-039-rs-L1 status=done turns=5 usd=0.0063 tokens(read,write,in,out)=[45264, 22460, 12, 6053] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_039.rs lines 1-334 of 334

Window `prototype/osfr-tools/tests/piece_039.rs` 1-334 (read in full, plus `src/restoration/piece_039.rs` 1-513 as the code under test). No `#[ignore]` and no early-return skips in the window. Most tests check recovered constants or hand-computed values (e.g. `progress(FARM_RANKS_58, 700)` → rank 3, 160/450, 35%; `rank_for_xp` boundaries), which are sound. Four findings:

- **[medium] tests/piece_039.rs:113-122 `members_only_starts_at_the_recovered_rank_five` - the farm loop asserts `entry.members_only()` equals `entry.rank >= FARM_MEMBERS_ONLY_FROM_RANK`, which is the body of `FarmRankRow::members_only` (src line 78) restated.**
  - Why it cannot catch a regression: `members_only` has no stored column; any change to the table's flag data is invisible, and a change to the threshold constant changes both sides together. Only the constant pin at line 73 and the ranch lines 124-125 are independent. The farm rows 58/63 are never checked against concrete expected values.
  - Fix: replace the loop with literal expectations, e.g. `assert!(!FARM_RANKS_58[3].members_only()); assert!(FARM_RANKS_58[4].members_only());` and the same for `FARM_RANKS_63`, plus `assert!(!FARM_RANKS_58[0].members_only())`.

- **[medium] tests/piece_039.rs:271-282 `ledger_authorizes_a_mining_outcome_once` - the replay at line 278 reuses the same amount (30), so the test cannot see a duplicate that overwrites the stored award.**
  - Why it cannot catch a regression: `GrantLedger::authorize` (src lines 486-488) could be changed to `insert(key, amount)` before returning `Duplicate`; the test would still see `Duplicate`, `awarded == 30`, and `len == 1`, because the replay amount equals the original.
  - Fix: after the first grant, call `ledger.authorize(key, 50)` and assert `Ok(GrantDecision::Duplicate)` and `ledger.awarded(key) == Some(30)` and `ledger.total_awarded(key.track) == 30`.

- **[medium] tests/piece_039.rs:285-299 `ledger_keys_mining_and_harvesting_separately` - the mining and harvesting keys use different tracks (Profile(14) vs Profile(45)), so the test does not exercise the `source` field of the key.**
  - Why it cannot catch a regression: `GrantKey` could drop `source` from `Eq`/`Ord` (src lines 394-399) and the keys would still differ by `track`, so both authorizations still return `Granted` and `len() == 2`. The doc comment at src lines 384-385 says the source is what keeps a shared numeric id distinct, and the test does not check that.
  - Fix: build both keys on the same track (e.g. `GrantKey::harvesting(ProgressionTrack::MINER, 7)` vs `GrantKey::mining(7)`), then assert the keys are unequal, both authorize as `Granted`, and `ledger.len() == 2`.

- **[low] tests/piece_039.rs:323-333 `ledger_rejects_zero_amounts_and_bad_outcome_ids` - the name says bad outcome ids are rejected, but the only quest-path check is `GrantKey::quest(..., 12).is_ok()`, a positive case that asserts nothing about rejection.**
  - Why it cannot catch a regression: `GrantKey::quest` (src lines 437-439) could drop the positive-id guard, or `new` could stop rejecting ids ≤ 0 for the Quest source, and the test would still pass, since no quest-path rejection is checked.
  - Fix: add `assert_eq!(GrantKey::quest(ProgressionTrack::Profile(MINER_PROFILE_ID), 0), Err(GrantError::InvalidOutcomeId(0)));` and drop or rename the `is_ok()` line.
