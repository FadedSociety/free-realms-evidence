<!-- fleet job=test-audit id=tests-bixie-hive-dungeon-rs-L1 status=done turns=7 usd=0.0131 tokens(read,write,in,out)=[152580, 43317, 16, 12245] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/bixie_hive_dungeon.rs lines 1-1200 of 1427

Window reviewed: `prototype/osfr-tools/tests/bixie_hive_dungeon.rs` lines 1-1200. Most of the window is sound: the content-row pins, packet offsets, refusal/no-mutation comparisons and the payout checks compare against authored data or the real reader, not against the code's own output. No `#[ignore]`, no early `return` on a missing fixture. The duplicate-row and duplicate-GUID error strings match `src/encounter/field.rs:330-352`. Three findings:

- **[medium] tests/bixie_hive_dungeon.rs:459-477 `the_marker_is_terrain_safe_and_clear_of_the_bixie_camp` - the comments and the header promise a 20 m exclusion and "at least 27 m" from the nearest Bixie home (line 495-496), but the body only asserts `distance >= 25.0` (line 472) and `enemy >= 25.0` (line 477).**
  - Why it cannot catch a regression: moving the marker about 2 m closer to Bixie field actor 131000102009 (currently 27.17 m) to any distance from 25 m up still passes, though the documented gate is 27 m; the claim "clear of the bixie camp" is only enforced at 25 m.
  - Fix: assert the documented threshold (`>= 27.0` for the nearest Bixie home, `>= 20.0` if that is the exclusion), or change the comments to match the 25 m that is enforced.

- **[low] tests/bixie_hive_dungeon.rs:588-590 `the_full_route_pays_sixty_eight_coins_and_one_prize` - the doc says "replayed win/close packets pay nothing", but the body replays only a 36/10 melee (lines 618-622) and a 26/42 Close (lines 633-639); no replayed win/results packet is sent.**
  - Why it cannot catch a regression: a change that paid on a replayed results packet (39/18, 39/47 or 39/19 arriving again) would not be exercised by this test.
  - Fix: after the win, re-send the results-producing packet path (or re-run `results_lifecycle` on a replayed tick) and assert `economy` is unchanged, or drop "win" from the doc.

- **[low] tests/bixie_hive_dungeon.rs:233-234 and 856 `prize["quantity"].as_u64().unwrap_or(1)` - a missing `quantity` in the authored row silently defaults to 1 in the expected value, so the test never checks that the row states a quantity.**
  - Why it cannot catch a regression: if the content row drops `quantity` and the production reader also defaults to 1, both sides agree and the packet/preflight checks still pass, even though the authored slice is no longer "exactly" as the doc at lines 275-278 claims.
  - Fix: `i32_field`/`u64` on `quantity` with `.expect(...)` (no default), so a missing field fails the test.
