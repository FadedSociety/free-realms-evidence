<!-- fleet job=note-refresh id=Multiplayer-Routing status=done turns=30 usd=0.0292 tokens(read,write,in,out)=[1173374, 64570, 62, 18822] model=claude-haiku-5-5 -->
# notes/Research/Multiplayer Routing.md

**Verdict:** minor drift. The architecture claims hold at the tip: the session map, the single `Server::step` boundary, the account-store paths, the 26/30 flag, `SocialService` derives, file locations, and the client addresses. One security statement is stale, and two smaller attributions need fixing.

**Corrections:**

1. `old:` The gateway receives only a selected character GUID here; account-ticket validation remains the separate login service's responsibility.
   `new:` The gateway login carries the selected character GUID plus a login binding ticket. The gateway checks that ticket itself, as an HMAC over the owner account and GUID, against the 16-byte `--handoff-key-file`, before it loads the save. Issuing the ticket remains the separate login service's job.
   `why:` repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:1111-1127 (`select_character_from_login` calls `login::verify_gateway_binding_ticket` and rejects a bad ticket); repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:2767-2776 (`login_character_binding` reads the ticket and GUID); repo:prototype/osfr-tools/src/login.rs:555-581 (`gateway_binding_ticket` and `verify_gateway_binding_ticket`); repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:382-383 (16-byte handoff key required).

2. `old:` Opcode-125 position changes call `update_pose`; every returned spawn, movement, or despawn tunnel is queued for the recipient session.
   `new:` Opcode-125 position changes call `update_pose_with_state` (the `update_pose` wrapper forwards to it); every returned spawn, movement, or despawn tunnel is queued for the recipient session.
   `why:` repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:1857-1868 (calls `staged_world.players.update_pose_with_state`); repo:prototype/osfr-tools/src/players.rs:361-378 (`update_pose` forwards to `update_pose_with_state`).

3. `old:` Enabled `realm` developer commands are processed by `Gateway`/`chat.rs` first and excluded from normal chat delivery.
   `new:` Enabled `realm` developer commands run through Gameplay's developer command path first (`chat::request` only extracts the text); the gateway then skips routing any application whose text starts with `realm ` and so keeps it out of normal chat delivery.
   `why:` repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:1893-1901 (the skip, with the comment "Gameplay's developer command path ran first"); repo:prototype/osfr-tools/src/chat.rs:37 (`request` returns the text only).

**Unsure:**

- "Without `--account-store`, only one session may own the configured `--state` file at a time." I found no guard for this in the non-account path. Sessions there are set as selected (`osfr-gateway.rs:1025`), and the duplicate-owner check at `osfr-gateway.rs:1132-1136` runs only in the account-store path. The save guard at `osfr-gateway.rs:4421-4428` only stops a stale copy from overwriting a live one. `osfr-bot.rs:311` does say "only one session without --account-store", so the rule may be intended. Left unchanged.
- "A native account-authentication handoff is not established by this integration." The gateway now verifies a handoff-keyed binding ticket (see correction 1), so this may be overstated. I did not settle the wording.
- Test counts in the "Tests and checks" section. `tests/game_store.rs` has three `#[test]` functions (lines 19, 54, 73), not the "game store 2/2" recorded. `tests/gateway.rs` has 14 `#[test]` functions, two of them `#[ignore]` (so 12 unignored), not "gateway 8/8". These are dated run records, so the source may have moved since. I did not count `tests/multiplayer.rs`; the search tool treats it as binary.
- Verified and current: `SessionKey{peer, connection_id}` `BTreeMap` (osfr-gateway.rs:409-415); `Server` at :2950 and `step` at :3668; `characters/<guid>.json` and `<guid>.social.json` for account-store sessions (paths.rs:23-29; osfr-gateway.rs:1145, 1175); `SocialService` derives `Clone, Debug` (social_lists.rs:326-327); `SharedWorld` derives `Clone` (osfr-gateway.rs:464); 26/30 flag 1 adds and 0 removes (osfr-gateway.rs:2885-2898); queued deliveries go through `sender.queue_message` (osfr-gateway.rs:2736-2746); 112/2 and 112/3 are read as server updates (social_lists.rs:1363-1380). Client addresses `00c24b00`/`00c24c00` call `00c1dc10` with 1 and 0, and the 35/1 and 26/30 function addresses resolve in the client database.
