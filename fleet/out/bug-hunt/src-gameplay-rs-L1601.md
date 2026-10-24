<!-- fleet job=bug-hunt id=src-gameplay-rs-L1601 status=nothing_found turns=14 usd=0.0219 tokens(read,write,in,out)=[478664, 57820, 30, 19840] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/gameplay.rs lines 1601-2400 of 5475

No defects I could tie to a client-reachable path in `gameplay.rs` lines 1601-2400.

What I checked, and why each candidate was dropped:

- **Panics on client input.** The `unwrap`s at 1655/1656/1666/1667 (`position[..3]`), 1716, 1749, 1766, 1789, 1981 and 2336-2344 are on server content or on Option fields that are guarded or always set. `patch_gender` (1676 -> `inventory.rs:1278`) validates gender to 1|2 and checks the span, so no index is client-driven. `chat::request` (`chat.rs:37`) bounds-checks through its `Reader`. The dev-only `kart_lobby_reply` path (2302-2315) checks `len < 4` before `inner[2..4]`.
- **Atomicity.** `handle_in_world`, `tick`, `initialize_world` and `on_location` mutate `self` in place, but the gateway stages them (`osfr-gateway.rs:1676`, `commit_outcome` at 1673). Within the window, the soccer, kart, derby and opening branches stage through a clone and commit with `*self = staged`. `settle_pets` clones and commits only on success. `handle_with_inventory` (`pets.rs:1098-1152`) commits the pet and the inventory together.
- **Double payout / trust.** Soccer settlement is gated by the `settled` flag (`soccer_entry.rs:477-503`). The kart `changed` decision is taken after the claim, and `last_paid_unix` is part of `changed_for_save`, so a paid claim is saved. Opening `accepted` flags are never cleared (`opening.rs`, no `accepted = false`), so the 910004/6/13/15 supply grants run at most once per acceptance. Mount and pet ownership come from the authenticated character and inventory, not from request bytes.
- **Logic.** The heading convention `atan2(rotation[0], rotation[2])` matches `osfr-gateway.rs:905`. `settle_mounts`' `heading: 0.0` is cosmetic and I could not show a wrong-player effect. The `fishing.supervise` error swallow at 1874-1875 is a documented "nothing saved" design.

I did not find anything at high or medium severity in this window.
