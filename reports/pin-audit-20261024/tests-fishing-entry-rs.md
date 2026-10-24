<!-- fleet job=pin-audit id=tests-fishing-entry-rs status=done turns=6 usd=0.0040 tokens(read,write,in,out)=[45994, 14296, 14, 3456] model=claude-haiku-5-5 -->
# tests/fishing_entry.rs

Six of the seven screened lines pin the shipped `fisherman_xp` value of 10. The source is `prototype/osfr-tools/data/content/fishing_spots.json` `payout.by_grade[].fisherman_xp` (all four rows are 10). The test's `spots()` fixture (line 43) parses that same `SPOTS_JSON` file, so these tests inherit the shipped value. Retuning the data row would break them while the code is still right.

- **prototype/osfr-tools/tests/fishing_entry.rs:330 shipped_spots_file_is_valid_and_names_real_npcs - pins `10` from `data/content/fishing_spots.json` `payout.by_grade[].fisherman_xp`.**
  **Fix:** this test reads the file itself, so compare against the row, not a literal. Bound it, for example `row["fisherman_xp"].as_u64().unwrap() <= 1_000` (the bound already enforced by `malformed_spots_files_are_refused` at line 380), or assert it is a non-negative integer. The file-validity check should not pin the tuned value.

- **prototype/osfr-tools/tests/fishing_entry.rs:761 a_fisherman_catch_pays_once_and_a_replayed_reel_pays_nothing - pins `10` from `data/content/fishing_spots.json` `payout.by_grade[].fisherman_xp`.**
  **Fix:** read the expected XP through `spots()` (the parsed `FishingSpots`) or from the `by_grade` row for the caught grade. Alternatively assert the XP equals the value paid by the first catch (`round.fisherman_xp()` after one catch) rather than a literal.

- **prototype/osfr-tools/tests/fishing_entry.rs:780 casting_again_after_a_catch_pays_the_next_catch_once_more - pins `10 * caught` from `data/content/fishing_spots.json` `payout.by_grade[].fisherman_xp`.**
  **Fix:** compute the per-catch expectation from the shipped row (the `by_grade` row for the caught grade, read from `SPOTS_JSON`), then assert the running total is `per_catch * caught`. Or bound it as strictly increasing by a positive amount per catch.

- **prototype/osfr-tools/tests/fishing_entry.rs:792 the_cap_off_path_pays_every_catch_as_before - pins `10 * caught` from `data/content/fishing_spots.json` `payout.by_grade[].fisherman_xp`.**
  **Fix:** same as line 780: read the per-catch XP from the shipped `by_grade` row and multiply by `caught`. The `coins() == 0` check at line 793 is a separate assertion and is not screened here.

- **prototype/osfr-tools/tests/fishing_entry.rs:864 a_session_cap_stops_payouts_and_survives_a_new_trip - pins `20` (two paid catches x `10`) from `data/content/fishing_spots.json` `payout.by_grade[].fisherman_xp`.**
  **Fix:** derive it as `2 * per_catch_xp`, where `per_catch_xp` is read from the shipped `by_grade` row (through `spots()`), not as a literal 20.

- **prototype/osfr-tools/tests/fishing_entry.rs:1223 reconnect_releases_the_round_and_keeps_what_was_already_paid - pins `10` from `data/content/fishing_spots.json` `payout.by_grade[].fisherman_xp`.**
  **Fix:** the one paid catch before the reconnect should be read through the shipped row (`spots()` `by_grade` row for grade 1..4, or the value from the first `catch`), not the literal 10.

Not a finding: line 826 `assert_eq!(round.coins(), grade * 10, ...)`. The `grade * 10` value is set by the test's own `spots_with` fixture (lines 800-811), which overwrites the shipped rows, so it is fixture-owned and the shipped `coins: 0` does not feed it.
