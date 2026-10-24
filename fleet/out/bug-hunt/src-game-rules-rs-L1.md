<!-- fleet job=bug-hunt id=src-game-rules-rs-L1 status=nothing_found turns=9 usd=0.0067 tokens(read,write,in,out)=[106624, 20821, 20, 5982] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/game_rules.rs lines 1-319 of 319

No defects that meet the bar in `prototype/osfr-tools/src/game_rules.rs` lines 1-319. I read the whole file (the first read stopped at line 300, so I re-read 300-319).

Checked and cleared:

- **`append_serial_integer` (256-272):** no panic or overflow. `extra_bytes` is at most 4, so `extra_bytes as u8 * 2` is at most 8 and the shifts stay below 32. The sign/magnitude split is consistent. Hand-checked the test vectors: 42 gives `[0x2a, 2]` and 7 gives `[7]`, which matches `tests/game_rules.rs:213`.
- **`encode_trade_allowed_flag_entries` `expect` (246):** the only panic path needs more than 4 billion entries. Its input is server-side `card_trade_flags`, which is populated only from tests, and it has no production caller. Not reachable from a client packet.
- **`is_active_at` (27-33):** `now < expiry` agrees with the test at `tests/game_rules.rs:54-55` (active at 99, inactive at 100).
- **`may` AcceptQuest (179-189):** `active_count < limit` correctly allows the Nth quest only while fewer than `limit` are active.
- **`may` CardTrade (192-200):** `find` takes the first matching key, so duplicate keys are not a concern in practice because the list is server-provided and not client-controlled.
- **`may` OpenChat (202-208), mount/pet trials, Pvp/Trade/Chat:** the boolean logic matches the stated policy.
- **`tunnel` and the fixed-width encoders (283-319):** `inner.len() as u32` is bounded by the fixed-size payloads. No client-controlled lengths are involved.

Observations outside the defect criteria (not reported as findings):

- `GameRuleSet::may` has no production caller. The only callers are in tests, so the Pvp, Trade, Chat, quest-limit and trial gates are not enforced at runtime through this entry point. Quest limits are read directly in `gameplay/npc_quests.rs:123-136`.
- `GameRuleSet::default()` (used at `gameplay.rs:1133`) starts as a member with all permissive policy. The gateway overwrites it at login via `osfr-gateway.rs:1167-1170`, so this is a placeholder and not exploitable.
