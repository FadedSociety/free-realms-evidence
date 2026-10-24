<!-- fleet job=bug-hunt id=src-gameplay-npc-rs-L1 status=nothing_found turns=18 usd=0.0236 tokens(read,write,in,out)=[606953, 56096, 38, 20938] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/gameplay/npc.rs lines 1-800 of 1434

No reportable defect in `prototype/osfr-tools/src/gameplay/npc.rs` lines 1-800. I read the whole window (1-800) and traced the callers and the services it hands off to.

Checked and cleared:

- **Slicing and unwraps on client bytes.** Every fixed-offset read is guarded by an earlier check:
  - `inner[4..12]` at line 82 is behind `inner.len() >= 12`.
  - `inner[6..10]` at line 371 is behind `inner.len() != 10`.
  - `inner[4..12]` and `inner[12..16]` at lines 491-492 are behind `inner.len() != 16`.
  - `inner[2]` at line 700 and `inner[2..4]` at lines 723/738 are behind the 4-byte `matches!` pattern at line 686.
  - The `get(4..12)` unwraps at lines 698/707 are on guaranteed 8-byte slices.
  - `inner[4..12]` at line 466 is on a server-built menu packet, not client input.
- **Mutation before error without rollback.** `handle_npc_packet` is called at gameplay.rs:2328 with `?`, and the gateway (osfr-gateway.rs:1644-1661) runs each message on a cloned `staged_gateway` and commits only on success. An `Err` from any NPC handler therefore discards the in-place mutations at lines 349-353, 530-531, 576-620 and 710-726. The `commit_if_changed` and `selected.is_ok()` staging is also consistent.
- **Inventory overwrite on Station Cash (66/x).** Only subtype 3 mutates `shop.inventory` (coin_shop.rs:1081-1101). Line 771 syncs the live inventory before that subtype, so `self.inventory = shop.inventory()` at line 776 cannot drop login-time-to-now gains.
- **Turn-in grants (49/14).** `finish_turnin` (quest_engine.rs:2003) rejects a turn-in that is not the pending one. `apply_grant` refuses locked job profiles and checks bag capacity, and the `bag_capacity = max(len, 100)` floor at line 325 is documented as intentional.
- **Client trust on NPC identity.** The runtime GUID from 26/8 and 26/10 is resolved by `content_npc_key` (line 35) and must map to a known actor. Merchant GUIDs in 165/x are not used for authority, since `check_coin_store` uses the open shop's NPC and range.
- **45/7 client-reported objectives.** `decode_client_complete` (quest_engine.rs:2800) rejects non-positive ids. The engine only matches open objectives and the server does not verify the trigger. This is an explicit design decision ("the client says a goal it judges itself is met"), so I did not report it.
- **InteractNpc keying.** Passing the runtime GUID at line 471 is consistent with `ContentGoal::InteractActor { actor_guid }` (quest_engine.rs:2328-2334) and the opening path (gameplay.rs:4559).

Not verified: the rest of 66/43 (line 800 onward, outside this window), and whether `handle_in_world` turns a full-bag turn-in `Err` into a disconnect. The `quest_reward_save_failure` fixture suggests that path is deliberate.
