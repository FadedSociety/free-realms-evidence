<!-- fleet job=test-audit id=tests-fishing-guide-drawable-rs-L1 status=done turns=3 usd=0.0054 tokens(read,write,in,out)=[14561, 15143, 8, 6662] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/fishing_guide_drawable.rs lines 1-560 of 560

Window reviewed: `prototype/osfr-tools/tests/fishing_guide_drawable.rs` lines 1-560. Two findings in the reconnect test, plus one low-severity pin. The rest of the window checks real values from shipped content and the live route, so I found nothing there.

- **[medium] prototype/osfr-tools/tests/fishing_guide_drawable.rs:528-534 `a_trip_can_be_quit_and_a_reconnect_releases_the_round` - the "dropped cast pays nothing" negative runs with no positive control that the cast and hook actually landed before the drop.**
  - The second half calls `player.send(&register(ACTOR))` (line 528) and `player.cast_and_hook()` (line 529) without checking either outcome. `cast_and_hook` (lines 229-237) discards the reply from `send(...)` and only calls `tick(...).expect`.
  - The only assertion on the late reel is `assert!(!late.is_ok_and(|out| find(&out.replies, &[138, 0, 14, 0]).is_some()))` (line 533). That passes whenever the reel produces no catch, for any reason.
  - Why it cannot catch a regression: if the cast or hook silently stops working (for example `cast_at` is refused or the hook never fires), the late reel yields nothing, and `fish_held() == 1` and the unchanged XP still hold because nothing was caught in the first place. The test would pass with the fishing mechanism broken on the second attempt. The first half (line 517) does prove the mechanism works, but only for the first attempt.
  - Fix: after line 529, assert the hook landed, e.g. `assert!(find(&cast.replies, &[138, 0, 4, 0]).is_some())` or whatever opcode the hook produces, and assert the registered/cast replies are present. Alternatively, before the drop, reel once and check 138/14 succeeds, then compare the late result against that. Also replace `!late.is_ok_and(...)` with an explicit `Ok` or `Err` expectation so an error path is not silently treated as a refusal.

- **[low] prototype/osfr-tools/tests/fishing_guide_drawable.rs:538 `a_trip_can_be_quit_and_a_reconnect_releases_the_round` - the hard-coded `game_id, 597` is a content pin, not a derived value.**
  - The value matches `fishing_spots.json` line 66 for the Gunther spot today, but the test does not read it from the spot table. Any reshuffle of game ids will fail this test even if the reconnect behaviour is correct.
  - Fix: look up the Gunther row from `spots()` (npc == GUNTHER) and compare `game_id` to `spot.game_id`, as `each_guide_opens_its_spot_and_starts_the_matching_trip` already does. The "Brambleback's Bayou" claim can stay as a comment.

- **[low] prototype/osfr-tools/tests/fishing_guide_drawable.rs:422 `the_four_new_spawns_use_recovered_or_documented_models` - the provenance check only asserts that the `legacy-data` and `client` source lists are non-empty.**
  - Why it cannot catch a regression: the spawn row could cite any evidence string, including one that does not support the model or name, and the check would still pass. The real model check (lines 414-421) and the (R) substitute-body check (lines 428-436) do catch some errors, so the gap is limited.
  - Fix: assert that the `client` evidence mentions `model_file_name` (or the model id), so provenance is tied to the chosen model rather than merely present.
