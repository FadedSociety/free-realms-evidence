<!-- fleet job=bug-hunt id=src-startup-world-rs-L801 status=nothing_found turns=6 usd=0.0077 tokens(read,write,in,out)=[69505, 27397, 14, 7204] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/startup_world.rs lines 801-1043 of 1043

Reviewed `prototype/osfr-tools/src/startup_world.rs` lines 801-1043 (tail of `write_npc_body`, `build_add_npc`, `parse_add_npc`) and the helpers they depend on (`Reader` at lines 51-122, `read_f32_array`, `read_npc_attachment`, `read_effect_tag`, `write_npc_attachment`, `write_effect_tag`, `tunnel`, `put_string`, `put_count`). No defect I could show.

What I checked:

- **Field order, writer vs reader.** I matched every field in `write_npc_body` (801-858) against `parse_add_npc` (868-965), in order and by type: the u8 flag pairs, the i32 ids, `customization` (type_id, texture_alias, tint_alias, tint_id, texture_override), the `[f32;4]` arrays (tilt, unknown_vector_54), `rider_id` as u64, the `character_variable_keys` count followed by u32 keys, the three strings head/hair/model_customization, and `name_scale`/`nameplate_image_id` at the end. They line up, so a built packet parses back to the same `NpcSpawn`.
- **Bounds on client-sized input.** `Reader::count` (line 107) rejects negative values and anything above `MAX_ROWS` = 100_000 (line 9). The `Vec::with_capacity` calls at 884 and 915 and the key loop at 942 are therefore capped, and the `Reader::take` path uses `get()` with checked addition, so truncated input returns `Err` rather than panicking. `Reader::string` (98-105) rejects negative lengths before the `as usize` cast.
- **Panics.** The `try_into().unwrap()` calls in `Reader` operate on slices that `take` has already sized exactly. The `expect` calls in `put_string`/`put_count` are on the build side and only fire above i32::MAX, which packet sizes make impossible.
- **Atomicity and trust.** `parse_add_npc` builds a fresh value and has no side effects. `build_add_npc` takes an already-constructed `NpcSpawn` and mutates nothing. Its callers (world.rs, enemies.rs, mounts.rs, pets.rs, encounter/shared.rs, startup_snapshot.rs) are server-side builders, not client packet handlers, so this window is not directly exposed to raw client bytes.
- **Callers of `parse_add_npc`.** These are `startup_snapshot.rs:507` (startup/snapshot data), `gameplay/npc_turnin.rs:24` (scans server-built packets), and tests. None of them passes raw client-originated 35/2 bytes.

Caveat: `parse_add_npc` rejects trailing bytes via `reader.finish()`, which is stricter than a lenient client. I judged that a design choice, not a defect.
