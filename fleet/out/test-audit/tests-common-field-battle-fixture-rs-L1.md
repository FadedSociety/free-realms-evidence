<!-- fleet job=test-audit id=tests-common-field-battle-fixture-rs-L1 status=done turns=8 usd=0.0116 tokens(read,write,in,out)=[153345, 36623, 18, 10909] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/common/field_battle_fixture.rs lines 1-1009 of 1009

Window reviewed: `prototype/osfr-tools/tests/common/field_battle_fixture.rs` lines 1-1009. Three findings. Most of the window holds up: `assert_start_screen`, `assert_payout`, `full_bag`, `decode_list`, `walk` and `fight_to_win` all compare against row data or packet bytes that the code under test does not compute. I checked the `decode_list` field offsets against the client reader (`FUN_00be63e0`, offsets +0x10 category, +0x14 icon, +0x20 title, +0x24 description, +0x28 name) and they agree, so I did not report them.

- **[medium] prototype/osfr-tools/tests/common/field_battle_fixture.rs:333 `level` - the helper re-implements the XP-to-level formula without the production cap, so it can disagree with the game.**
  - Why it cannot catch a regression: `level` returns `1 + xp / 100` with no cap. Production `profiles.rs:229` returns `(1 + xp / 100).min(20)`. A regression that removes the cap, or changes the curve in `profiles.rs` but not here, still passes any test that asserts through this helper (for example `bixie_hive_dungeon.rs:391`). Above 2000 XP the helper reports level 21+ where the game reports 20.
  - Fix: read the level from the production profile API (`profiles.rs`) instead of re-deriving it, or add a canary at 2000 and 2500 XP that asserts the capped value 20 against the production function.

- **[medium] prototype/osfr-tools/tests/common/field_battle_fixture.rs:444 `restore` (called from `reopen_with` at 403-416 and `reopen_at` at 420-431) - the world-entry replies are discarded and `entered_world` is never asserted.**
  - Why it cannot catch a regression: `restore` ignores the outcomes of `send(&mut restored, 13/10)` at lines 444-445. A reconnect that stops entering the world still returns a gateway, so the reopen tests go on to check state that the save snapshot already holds. `gateway_with_bag_seeded` at lines 138-140 does assert `loaded.entered_world`, so the two paths are inconsistent.
  - Fix: assert `entered_world` on the 10/13 outcome inside `restore`, e.g. `let loaded = send(&mut restored, &10_u16.to_le_bytes(), now_ms + 100); assert!(loaded.entered_world, "reconnect enters the world");`.

- **[low] prototype/osfr-tools/tests/common/field_battle_fixture.rs:589-599 `enter_battle` - the "row's goal reaches the client" check scans every reply for the 4-byte objective id rather than checking the 41/114 screen.**
  - Why it cannot catch a regression: the `windows(4)` search over all unframed packets matches the objective bytes anywhere, including packets unrelated to the battle screen. A change that drops the goal from 41/114, while the same bytes still appear in another packet, still passes. The check is also not tied to the screen named in the message.
  - Fix: restrict the search to the `[41, 0, 114, 0]` packet (as `details()` already does) and assert the objective id at its known offset in that screen, not as a substring anywhere in the replies.
