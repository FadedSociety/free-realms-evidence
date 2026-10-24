<!-- fleet job=bug-hunt id=src-bin-osfr-gateway-rs-L4001 status=nothing_found turns=19 usd=0.0186 tokens(read,write,in,out)=[518880, 44804, 40, 15600] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/bin/osfr-gateway.rs lines 4001-4671 of 4671

No defect reportable in `osfr-gateway.rs` lines 4001-4671. I read the whole window and the callers/helpers it depends on (`step` 3668-3730, `refuse` 3415, `studio_session`/`studio_content_dir`/`studio_route` 3847-3905, `studio_decode` 47-72, `collect_json_files` 75-89, `join_player` 602-623, login duplicate check 1128-1137, `game_store::save_document`).

Checked and ruled out:
- **Unwraps on client-reachable state (4009, 4331, 4180, 4151, 4102, 4206, 4069):** every `sessions.remove(..).unwrap()` / `sessions[&key]` key comes from `studio_session()` or `session_key_for_peer()`, which read the same map, so they cannot miss. The studio routes are also gated by `dev_tools` and an admin role (3881). `studio_assets[&kind]` is inserted on the line above. The slices after `starts_with` are on ASCII prefixes.
- **Studio path and name traversal (4070-4075, 4103-4111, 4170-4173, 4078-4092):** decoding happens before the `..`, `/`, `\` and charset checks. `/api/content` POST validates JSON before `replace_bytes`. Savestate names are alphanumeric and capped at 48 characters, and `studio_decode` cannot panic.
- **`field_packets_for` / `field_packet` (4545-4607):** all reads use `get(..)`, so short packets return false. Actor and target GUIDs are checked against server-side state (`recipient`, `known_npcs`, `players.knows_character`). `field_recipient_matches` requires loaded, same instance, and ready. The canary is `cfg(test)` only.
- **`accept_handshake` (4309-4397):** the same-peer replacement only ends that peer's own session. `Err` from `accept_handshake` is contained at 3700 and logged, so it cannot end the server. `retired_handshakes` is bounded by time and by `MAX_SESSIONS*4` eviction (4408-4417).
- **`end_session` (4401-4470):** the duplicate-owner save skip matches its comment. The save is contained, and later stages still run after a failure.

Low, not reported: in `accept_handshake` (4371) `world.session_keys.insert` precedes `trace.record(..)?` (4377) and `session.send(..)?` (4383). A failure there leaves a stale id→key entry with no session. I found no reader that can reach that id, because only joined sessions enter `active_sessions`, so I judged it unreachable in practice.
