<!-- fleet job=note-refresh id=Chat-Core status=done turns=21 usd=0.0242 tokens(read,write,in,out)=[716523, 66644, 44, 17499] model=claude-haiku-5-5 -->
# notes/Research/Chat Core.md

**Verdict:** Module facts and test coverage are current. The "Lead integration" list and the offline-tell delivery sentence are stale: the gateway wiring they ask for now exists. Client addresses all resolve in the client DB.

**Corrections:**

1. `old:` `1. Register `social_chat` from the lead-owned module tree; do not copy the existing `chat.rs` developer-command helper into it.`
   `new:` `1. Done: `social_chat` is registered in the module tree (`pub mod social_chat;`). Do not copy the existing `chat.rs` developer-command helper into it.`
   `why:` repo:prototype/osfr-tools/src/lib.rs:85 (`pub mod social_chat;`)

2. `old:` `2. Build `ChatSession` values from the live registry, including account membership, zone and chat area, group/guild ids, and authoritative position. Pass account flags from `AccountFlags` to `AccountChatPermissions`. Call `ChatHistory::record` for each accepted line so reports remain available when the speaker disconnects.`
   `new:` `2. Done for typed chat: the gateway's `chat_session` builds `ChatSession` from the live registry (zone, position, group, guild, membership). Its chat area is still `None`. `AccountChatPermissions::new(account.flags.underage, account.flags.open_chat)` is set from `AccountFlags`, and `ChatHistory::record` runs for each accepted typed line. Quick-chat lines are not recorded.`
   `why:` repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:837-852 (`chat_area_id: None` at 847), :1185 (AccountFlags), :2283 (`chat_history.record`); no `chat_history` call in `route_quick_chat` (:2293-2360)

3. `old:` `3. Route typed 15/1 and quick-chat 67/2–3 through the parser, account/filter checks, spam gate, quick-chat catalogue, recipient resolver, and server-message builders. Send family 22 for offline tells.`
   `new:` `3. Routed: typed 15/1 (`route_typed_chat`) and quick-chat 67/2–3 (`route_quick_chat`) both go through the parser, permissions/filter, recipient resolver and builders. Only the typed path calls `SpamGate`; `route_quick_chat` does not. Family 22 offline tells are sent through `chat_error_delivery`.`
   `why:` repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:2138-2142 (dispatch), :2241-2291 (typed, `spam_gate.allow` at :2250), :2293-2360 (quick chat, no spam_gate call)

4. `old:` `Its delivery point remains the gateway integration.`
   `new:` `The gateway delivers it: `chat_error_delivery` wraps `ChatError::client_reply` for typed and quick-chat tells.`
   `why:` repo:prototype/osfr-tools/src/bin/osfr_gateway/delivery.rs:97-110; called at repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:2244, :2262, :2296, :2321

**Unsure:**

- Report intake: `intake_report` (social_chat.rs:1066) has no caller outside `social_chat.rs` and `tests/social_chat.rs`. Family 68 is not dispatched in the gateway. The "Implemented behavior" bullet does not claim routing, so I left it. Adding "not routed from the gateway" would prevent misreading. Item 4 (ReportInbox not connected to a store) is still accurate.
- Item 5 (native two-account acceptance "still required"): Build Ledger line 44 records "Two-bot say and tell delivered (W103)". Say and tell may now be covered, but reporting, quick chat, ignore and offline tell are not confirmed in my reads. I did not check the W103 report.
- Yell scope: `resolve_recipients` filters Yell by `zone_id` only (social_chat.rs:843-846). The instance restriction comes from `chat_candidates` (osfr-gateway.rs:859-874), which compares the full zone, so the note's "instance-local" is consistent with the code.
- Client addresses in the note (`00b14fa0` through `009471a0`, `00944fe0`, `00b97380`, `00b97580`) all exist in the client function table. I did not verify the channel tables or the 10-line history claims in the pseudocode.
