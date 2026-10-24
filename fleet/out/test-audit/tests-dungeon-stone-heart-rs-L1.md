<!-- fleet job=test-audit id=tests-dungeon-stone-heart-rs-L1 status=done turns=8 usd=0.0085 tokens(read,write,in,out)=[120334, 25159, 18, 8250] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/dungeon_stone_heart.rs lines 1-583 of 583

Window reviewed: `prototype/osfr-tools/tests/dungeon_stone_heart.rs` lines 1-583 (single test `stone_heart_hideaway_is_singular_level_gated_and_pays_through_gateway_once`, plus helpers). No `#[ignore]`, no early-return skips. Fixture paths are used with `unwrap()`, so a missing fixture fails loudly. The job-switch and level checks hold up: `realm level` writes XP to the active profile (`gameplay.rs:2905-2914`), and `level(&gateway, BRAWLER)` then fails if the switch did not happen. The Go/portal/developer refusals compare full snapshots, and the win/reward/reconnect checks are substantive. Findings:

- **[medium] tests/dungeon_stone_heart.rs:233-237 `entrance_actors` - parse failures are silently dropped (`parse_add_npc(packet).ok()`), so the "singular entrance" assertion at line 356 only counts AddNpc frames that parse.**
  - Why it cannot catch a regression: a change that emits a second Legacy entrance actor (TITLE_ID name) in a frame that `parse_add_npc` rejects (e.g. a truncated or trailing-byte-corrupted body) is filtered out, so `vec![ENTRANCE]` still matches and the test passes.
  - Fix: map parse errors to a failure instead of filtering, e.g. `.map(|packet| parse_add_npc(packet).expect("35/2 frame parses"))` for every `35/2` frame, then filter by `TITLE_ID`. Assert the count of all 35/2 frames with `name_string_id == TITLE_ID` is exactly one.

- **[low] tests/dungeon_stone_heart.rs:570-581 (the duplicate-Close block) - the message says "changes no saved state", but the body only compares the in-memory `gateway.snapshot()`, and the reloaded file is checked only for economy and zone_id.**
  - Why it cannot catch a regression: a duplicate Close that changes a non-economy field persisted to disk (for example the encounter or pending-entry fields that `reopen` reads back) would still pass, because the reloaded check at 580-582 does not compare the full saved state.
  - Fix: compare `reloaded.snapshot()` with the state saved right after the first Close, and rename the message to match what is compared.

- **[low] tests/dungeon_stone_heart.rs:456-457 vs 442-447 - the simulator checks are substring matches on the whole reply, so "level 15" / "level 20" could match a line that is not an eligible run.**
  - Why it cannot catch a regression: a production change that prints a refusal or header containing "level 15" or "level 20" (for example "needs level 15" if the floor moves) would satisfy the `contains` check while the eligible level never ran.
  - Fix: assert on the per-level line prefix, e.g. `"  level 15:"` followed by a result token, or check that the reply has exactly one line starting with `  level 15` and no `skipped` suffix.
