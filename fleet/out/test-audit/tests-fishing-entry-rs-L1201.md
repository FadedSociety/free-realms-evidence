<!-- fleet job=test-audit id=tests-fishing-entry-rs-L1201 status=done turns=5 usd=0.0039 tokens(read,write,in,out)=[25483, 11056, 12, 4614] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/fishing_entry.rs lines 1201-1358 of 1358

Window `prototype/osfr-tools/tests/fishing_entry.rs` 1201-1358 (test `private_ordinary_player_fishes_from_the_guide_menu`, `#[ignore]`d with a stated reason, fixture requirement is env-driven and the reason is given, so not a silent skip). Helpers `send_at`, `tick`, `fish_items` (1165-1184) and `set_dev_tools` (gateway.rs:1223) were read. The core payment checks (`fish_items` before/after reel, replay and forged reel, quit, reconnect) are real state comparisons and are not flagged.

- **[medium] prototype/osfr-tools/tests/fishing_entry.rs:1244-1245 private_ordinary_player_fishes_from_the_guide_menu - the comment says `realm` commands stay developer-only, but the `realm race` chat is sent with no assertion on its replies or on state.**
  - Why it cannot catch a regression: if the dev-tools gate were removed (gateway.rs:1223 `set_dev_tools` / gameplay.rs:1197 ignored), `realm race` could relocate or change state and the test would still pass, because nothing is checked after the send.
  - Fix: capture the replies and assert they contain no realm/relocation packet (or that the character position and `snapshot()` are unchanged) after `send_at(&mut g, &chat("realm race"), NOW)`.

- **[medium] prototype/osfr-tools/tests/fishing_entry.rs:1259-1261 (same test) - the comment and assertion message say a second trip is "refused with a chat line", but only `!offers(&again)` is checked; no chat line is looked for.**
  - Why it cannot catch a regression: a change that drops the refusal chat line (or sends a different reply) still passes, and a change that silently does nothing also passes; the stated behaviour is never exercised.
  - Fix: assert the reply contains the refusal chat packet (a specific chat opcode/locale id), and that the open round's instance is unchanged (e.g. a second `lifecycle(5, …)` with the first instance still starts, or the snapshot's fishing state is identical before and after).

- **[low] prototype/osfr-tools/tests/fishing_entry.rs:1223-1227 (same test) - the "no spots file" section has no positive control that the guide menu renders at all.**
  - Why it cannot catch a regression: `offered(...).is_none()` and `!offers(...)` also pass if the NPC menu is broken or empty for every NPC, so a menu regression would look like "nobody offers fishing" here. The positive control only exists in section 2 with a different gateway.
  - Fix: before the `is_none` check, assert the menu for a known NPC with a known non-fishing option is non-empty (or run `menu(&mut g, REED)` and assert it has the expected option count), so the negative result is shown to be meaningful.

- **[low] prototype/osfr-tools/tests/fishing_entry.rs:1268 (same test) - exact packet list `vec![(41, 2), (39, 17), (35, 20)]` pins the full Go reply, including the incidental 35/20 packet that this step's subject (the 39/17 start and fishing flag) does not depend on.**
  - Why it cannot catch a regression: it is not a miss; an unrelated extra or reordered UI packet breaks the test and forces churn while the fishing behaviour is unchanged.
  - Fix: assert the required pairs are present (`contains(&(39, 17))`, `contains(&(41, 2))`) and keep only the exact check for the packet that matters, or pin the set order-insensitively.
