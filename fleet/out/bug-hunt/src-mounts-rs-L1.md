<!-- fleet job=bug-hunt id=src-mounts-rs-L1 status=nothing_found turns=15 usd=0.0224 tokens(read,write,in,out)=[480262, 59899, 32, 20169] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/mounts.rs lines 1-800 of 951

No reportable defects in `prototype/osfr-tools/src/mounts.rs` lines 1-800. I read the whole window and the helpers it depends on (lines 800-951, `gameplay.rs` 1990-2080 callers, `world.rs` `unframe_tunnel`, and the mount tests that name the behaviours). Each candidate I checked was ruled out:

- **`decode_request` (578-596):** the length guard `inner.len() < 3` runs before `inner[..2]` and `inner[3..]`. The `word(0)` closure is only reached on the `(6, 4)` and `(8, 5)` arms, so its 4-byte slice is always in range. The `(1, 8..=24)` arm slices `body[..8]` safely. Malformed bodies return `Err` before any state change. `mount_routing.rs:151-161` covers these cases.
- **Client-supplied mount ids and item ids (`spawn` 349-423, `spawn_by_item_definition` 425-449):** `Spawn` and `SpawnByItem` both go through `catalog.mount` / `mount_for_item` and then `is_owned` (843-850) against positive-count inventory instances. The ownership check precedes the debounce and every mutation.
- **Mount target (`mount` 451-500):** the client's target GUID must equal `ride.actor_guid`, and `owner_guid == rider_guid` is enforced. The seat check `seat_index >= seat_count` uses `u32::from(u8)` on a catalog value validated to 1..=99.
- **Atomicity:** every error return in `spawn`, `mount`, and `dismount_request` happens before the state is replaced. `dismount_request` uses `mem::replace` but has no fallible step after it. `list_packet` is built after the state change, which is intended.
- **Debounce (375):** the `saturating_sub` comparison matches `tests/mounts.rs:230-281`, which checks 5999 blocked and 6000 allowed.
- **GUID arithmetic (`ride_guid` 711):** `owner ^ 0xc000…` is a bijection, and it never equals the owner. Character GUIDs are sequential from 1 (`account_store.rs:151`), so the ride GUIDs land in `0xc0..` and cannot collide with derby `0xd0..` or housing `0x0f..`. This only breaks for owners with the top two bits set, which the account store cannot produce.
- **`follow` (683-693):** `get(2..10)?` guarantees the length before `copy[2..10]`.
- **Catalog validation (115-183):** duplicate item ids are rejected by `insert().is_some()`, and `mount_type_id` is checked against `types`.
- **`add_ride_npc` returning `None` (818-833):** a silent skip when `model_id` is null. No shipped `mounts.json` entry has a null model, and no client packet can set it, so I dropped it.

I did not find a remote crash, a save corruption, an item or coin gain, or a client-trusted authority in this window.
