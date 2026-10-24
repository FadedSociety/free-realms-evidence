<!-- fleet job=bug-hunt id=src-mounts-rs-L801 status=nothing_found turns=19 usd=0.0166 tokens(read,write,in,out)=[485915, 49971, 40, 11054] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/mounts.rs lines 801-951 of 951

No reportable defects in `prototype/osfr-tools/src/mounts.rs` lines 801-951. I read the whole window and the callers it depends on (`wire()`, `RideView::packets`, `handle`, `spawn`, `mount`, `dismount_request`, `MountCatalog::new`/`owned_mounts`, `decode_request`, `gameplay.rs` `handle_mounts`/`settle_mounts`, `startup_world::build_add_npc`/`tunnel`, `world::unframe_tunnel`). What I checked and ruled out:

- **`add_ride_npc` (818-833):** `mount.model_id?` silently yields no AddNpc, but every ride in `data/content/mounts.json` has a `model_id` (for example 715 has 3339; the seat/name/model fields are present on each record), and the catalog never stores null. `.ok()` on `unframe_tunnel` can't fail: `startup_world::tunnel` writes the `[5,0,1]` prefix and matching u32 length that `unframe_tunnel` checks. `put_string`'s `expect` in `startup_world` is unreachable because `tint_alias` is capped at 4096 bytes by `MountCatalog::new` (line 157). Heading is `atan2` of the character rotation, so `sin`/`cos` stay finite unless the upstream rotation is non-finite, and `gateway.rs:209` bounds those components.
- **`remove_actor` (836-841):** the `35/3` shape matches the other removers at `gameplay.rs:2411`, `pets.rs:1686` and `world.rs:613`.
- **`is_owned` (843-850):** it uses the same positive-count, candidate-id rule as `owned_mounts` (210-224), so the list and the ownership gate agree.
- **`encode_mount_list` (852-877):** the count is bounded by the catalog's 4096-mount cap, and the tint string by 4096 bytes.
- **`encode_mount_response` (879-889):** `seat_index` is checked against `seat_count` (1..=99) at line 484 before it reaches this encoder, so the `as i32` cast cannot wrap.
- **`recipients` (912-920), `put_*` helpers, `valid_sources`, `invalid_data`:** no client-sized allocation, no unchecked indexing, and no swallowed error on a path that changes state.
- **`wire()` routing (801-804):** `nearby()` sends the list packet (sub-op 5) privately and everything else to shared, consistent with the header sub-opcodes used here.

I found no path where a remote client can crash the server, grow a collection without bound, corrupt state, or gain items or coins through this window.
