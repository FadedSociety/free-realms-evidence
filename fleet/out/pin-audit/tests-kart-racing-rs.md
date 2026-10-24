<!-- fleet job=pin-audit id=tests-kart-racing-rs status=nothing_found turns=2 usd=0.0010 tokens(read,write,in,out)=[1816, 5369, 6, 645] model=claude-haiku-5-5 -->
# tests/kart_racing.rs

No findings for `prototype/osfr-tools/tests/kart_racing.rs:596` (`snapshots_keep_the_reward_schedule_and_reject_incoherent_progress`).

The expected `RewardSchedule { coins: 10, xp: 25 }` is not read from any data file. The test builds its own fixture at lines 579-590: `TrackLayout::new(31, 2, vec![11, 12], Some(kart_racing::RewardSchedule { coins: 10, xp: 25 }))`. Line 596 checks that the snapshot round-trips that same fixture value, and line 605 checks the restored claim pays the same fixture amounts. Retuning `data/content/*.json` cannot break these lines, so this is the test's own fixture value, not a pinned tunable. No change needed.
