<!-- fleet job=test-audit id=tests-player-radial-rs-L1 status=done turns=4 usd=0.0055 tokens(read,write,in,out)=[32690, 18790, 10, 5660] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/player_radial.rs lines 1-599 of 599

Window reviewed: `prototype/osfr-tools/tests/player_radial.rs` lines 1-599. Code under test read: `src/player_radial.rs` 174-232 (`select_player`/`select_menu` order: visibility check, then `offer`/look lookup, then menu set). The hidden-target and refusal tests are sound against that ordering and are not reported. Findings:

- **[medium] tests/player_radial.rs:349-350 inspect_choice_sends_the_public_look_only - the "canary" scan can never fail.** `CANARY` is never planted in any input: `look()` (lines 82-101) and `PublicLook` contain no field that could carry it, so `!out[0].windows(4).any(|w| w == CANARY.to_le_bytes())` is true for any implementation that sends the look. The comment at 349 concedes "nothing private exists to leak", so the check gives no evidence of the claimed "public look only" property.
  - **Why it cannot catch a regression:** a change where `choose` or `look_of` pulls private data from the registry (e.g. the target's presentation or inventory) and writes it into the packet would still pass, because the marker is never in that data.
  - **Fix:** plant `CANARY` bytes in a private, non-look field of the target's registry presentation (or in a second `PublicLook`-adjacent source the code could reach) and assert the marker is absent from `out[0]`. Alternatively, drop the canary and rename the comment to say the look fixture is the only source.

- **[low] tests/player_radial.rs:316 name_is_bounded_and_utf8_safe - the bound check passes for an empty name.** `assert!(n <= 64)` and the UTF-8 check both succeed if `visible_name` returns an empty string or truncates to nothing. The input is 200 × "é" (400 bytes), so the expected result is exactly 64 bytes (32 chars); the test does not pin it.
  - **Why it cannot catch a regression:** an implementation that drops the name entirely (or truncates to 0 bytes) still satisfies both asserts, so the "bounded" claim is only half-tested.
  - **Fix:** assert `n == 64` and `std::str::from_utf8(&m[49..49 + n]).unwrap() == "é".repeat(32)`.

- **[low] tests/player_radial.rs:206 select_builds_a_one_entry_menu_for_the_target - the row pins icon/label ids `133, 3902` that the test is not about.** The test name is about the menu shape and target; the exact icon and label ids are presentation constants, so unrelated changes to the menu's icon table would fail this test with no bearing on target selection.
  - **Why it cannot catch a regression / why it is churn:** the assertion is not what the name claims to check; it mainly fails on unrelated asset/icon changes.
  - **Fix:** assert `row[0] == INSPECT_ENTRY_ID` and the entry count/shape, and keep the icon/label pair in a dedicated menu-format test.

- **[low] tests/player_radial.rs:347 inspect_choice_sends_the_public_look_only - the tail is pinned to exact values the look does not supply.** `p.tail == [0,0,0,0,0,0,0,2,0,0]` checks eight scalars (VIP rank, coins, levels, etc.) that come from fixed encoder defaults, not from `PublicLook`. The test is about which look data is sent, so any unrelated change to a default scalar fails it.
  - **Fix:** assert only the fields that the look controls (profiles, active, items, and `tail[0] == 0` already at line 150), and assert the tail's length/position rather than its values.
