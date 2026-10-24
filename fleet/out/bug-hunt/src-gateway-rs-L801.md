<!-- fleet job=bug-hunt id=src-gateway-rs-L801 status=done turns=18 usd=0.0262 tokens(read,write,in,out)=[644783, 63029, 38, 23659] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/gateway.rs lines 801-1600 of 2232

Reviewed `gateway.rs` 801-1600 in full and traced the callers of the non-trivial paths. Most of the window holds: client positions are checked for finiteness and magnitude at the wire reader (`gateway.rs:205-212`) and in `movement::validate`, and direction is normalised in `accepted_state`. Bundled role changes are rejected before any child is applied, and bundle detection is consistent between `application_messages` and `handle_at`. The one real defect I could show is below. It is low severity and is not reachable from a remote client.

- **[low] `prototype/osfr-tools/src/gateway.rs:1086` - `enable_gameplay` overwrites `self.state` before two fallible steps, so a returned error leaves the gateway with a changed character pose and no gameplay installed.**
  - **Failure scenario:** `enable_gameplay` is called on a gateway whose freshly loaded `Gameplay` reports an abandoned battle, with a valid `return_location`. Step 1: line 1086 sets `self.state = return_location`. Step 2: line 1088 `supports_location(&self.state)` returns false, or line 1094 `gameplay.set_world_dir(...)?` fails. The function returns `Err` at 1089 or 1094. `self.gameplay` is never assigned (line 1097 is not reached), yet `self.state` keeps the battle return pose. A caller that logs the error and keeps using the gateway then snapshots a character at a pose that no installed gameplay backs.
  - **Reach:** `enable_gameplay` (`gateway.rs:1075`) has no caller in `src/` or `bin/`. Its only callers are in `tests/` (`tests/gameplay.rs:71,147`, `tests/dev_teleport.rs:582`, `tests/app_fuzz.rs:465,476`). The production path is `load_gameplay` (`gateway.rs:811`), which works on a local `state` and so cannot leave partial state. No client packet reaches this function, so the defect is latent.
  - **Fix:** Keep the `Gameplay` local and perform the `self.state = return_location` assignment only after `set_world_dir(...)?` and the `supports_location` check succeed, immediately before `self.gameplay = Some(gameplay)`.

Ruled out after reading the code:
- `handle_at` (`gateway.rs:1409-1815`): all mutations go to clones and are committed only at the end, so an early `?` leaves `self` unchanged.
- `change_account_role` (`gateway.rs:1151-1180`): admin authority is checked by `AccountStore::set_account_role` (`account_store.rs:259-271`) against the verified `role_account` binding.
- `stage_instance_transfer` (`gateway.rs:955-994`): every fallible step precedes the mutations.
- `set_identity` (`gateway.rs:1264`): `apply_identity` can partially grant attachments before an error (`gameplay.rs:5255-5259`), but identity comes from the server-validated identity store, not a live packet, and the failure needs an inventory-full condition. I judged it not a reachable defect.
- Movement magnitude and NaN handling, and the `catch_unwind` around `parse_self`: both are handled.
