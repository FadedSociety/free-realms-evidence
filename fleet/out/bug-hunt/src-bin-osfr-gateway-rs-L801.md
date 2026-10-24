<!-- fleet job=bug-hunt id=src-bin-osfr-gateway-rs-L801 status=done turns=24 usd=0.0255 tokens(read,write,in,out)=[805101, 52716, 50, 21662] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/bin/osfr-gateway.rs lines 801-1600 of 4671

Reviewed `prototype/osfr-tools/src/bin/osfr-gateway.rs` lines 801-1600 in full, and followed the callers and helpers they depend on: `decode_kart_pose_datagram` (soe.rs:176-219), `login_character_binding` / `WireReader` (osfr-gateway.rs:2767-2830), `application_messages` / `ordered_messages` / `application_requests` (gateway.rs:655-729), `SessionRequest::parse` (session.rs:16-33), `ReliableSender::new` (soe_send.rs:95-121), `ActionBudgets::allow` (social_chat.rs:62-82), and the disconnect save path (osfr-gateway.rs:4421-4433). Most of the window holds up:

- `wire.get(..2)` and `payload.get(..2)` guard the short-packet cases.
- `message[6..]` at 1248 is safe: the kart datagram is always 96 bytes (`application` is `[5] + 95-byte payload`, soe.rs:215-218).
- `packet.payload[..4]` at 1461 is guarded by `len() == 6`.
- The `unwrap`s in `WireReader` (2803-2812) are fed fixed-length slices from `take`.
- `string()` caps length before allocating.
- The `options.account_store.unwrap()` calls are preceded by an `is_none` early return.
- `buffer_size` is bounded to 64..=65507 at parse time and re-checked in `ReliableSender::new`.
- The duplicate-session check runs before any save is read or written.
- Unselected sessions never save on disconnect (osfr-gateway.rs:4428).

One low-severity finding:

**[low] prototype/osfr-tools/src/bin/osfr-gateway.rs:1584-1597 - The account action budget is charged request by request, so a bundle refused partway through leaves the tokens for its earlier children consumed, although the comment at 1577-1579 says a refusal drops the bundle "without mutations".**
- **Failure scenario:** An authenticated player sends a bundle of N budgeted children (for example chat or tells, families in `ActionBudgets::allow`, social_chat.rs:68-80) where the account has room for only k-1 of them. The loop at 1584-1589 calls `security.budgets.allow` for children 1..k-1, which each consume a token and return true. Child k returns false, so the loop breaks and the bundle is dropped at 1590-1596 with `Ok(())`. The account has lost k-1 tokens for work that never ran. Those tokens refill over time, so the effect is self-inflicted rate-limit drain that can delay the same player's next legitimate action. Another player's budget is not affected, so the impact is limited.
- **Reach:** Any authenticated client bundle (opcode `[0, 25]`) reaches `dispatch_message` (1509) → `dispatch_message_inner` (1530), with `budget_checked == false`. `application_requests` (gateway.rs:719) supplies the children. No upstream check prevents the partial charge.
- **Fix:** Check all children without consuming (add a non-consuming peek to `ActionBudgets`), or refund the tokens already taken when a later child is refused.

No other defects in this window met the bar. Nothing in the window reaches a panic, unbounded allocation, a trusted client authority field, or an error-swallowing mutation.
