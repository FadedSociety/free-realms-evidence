<!-- fleet job=bug-hunt id=src-pets-rs-L1601 status=nothing_found turns=18 usd=0.0163 tokens(read,write,in,out)=[407056, 42892, 38, 13752] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/pets.rs lines 1601-1819 of 1819

Window `prototype/osfr-tools/src/pets.rs` 1601-1819 read in full, plus the callers and upstream checks it depends on (`handle` 1019-1080, `handle_with_inventory` 1098-1152, `wire` 1154-1179, `list_packet`, `follow_location`, `equip_item`, `care`, `play`, `set_favorite`, `validate_roster` 1487-1528, `advance_roster`, `pet_mut`, `summon`/`summon_by_item_owned` 885-1015, `rename_selected` 871-883, `adopt_with_replies` 793-824, `validate_name`/`valid_model`, and `world::unframe_tunnel` / `startup_world::tunnel` / `build_add_npc`). I found no defect I can tie to a client-reachable path.

Checked and dropped:

- **`put_count` / `put_string` `expect` (1752-1765):** the counts are bounded by `MAX_PETS`, the trick set and fixed-size arrays. Pet names are validated to at most 64 chars (about 256 bytes) by `validate_name` at rename and again in `validate_roster`, so the u32 conversions cannot fail.
- **`owned_item_for_record` (1569-1584):** the `i32::try_from` checks reject out-of-range client values, and the lookup requires `count > 0` plus an exact definition and tint match. No fallback.
- **`add_need` (1615-1622):** the clamp to `maximum` is correct. Its amounts come from content config or the fixed `20.0` in `play`, not from the client.
- **`clear_equipped_instance` (1624-1641):** called only from `care` (1368-1370), which clears stale references across all pets after the consume. Staged on a clone, so there is no partial mutation.
- **`pet_removal_packet` (1684-1690) and `pet_set_name_packet` (1652-1661):** the 35/3 shape matches `enemies.rs:807` and `mounts.rs:836`. The name length conversion is a plain `as u32` on a validated name.
- **`PetPresence::spawn_packet` `.ok()` (1667-1681):** `unframe_tunnel` accepts exactly what `startup_world::tunnel` produces, so the `None` branch is unreachable in practice.
- **`refusal_text` (1801-1811):** the error strings match what is produced (`pet is not owned`, `pet adoption item is not owned`, `that pet is not summoned`, `cannot summon a pet during a minigame`). The `pet has no adoption item` arm is dead but harmless.
- **`pet_status_packet`, `pet_favorite_packet`, `pet_can_go_packet`, `pet_active_packet` (1643-1650, 1767-1799):** fixed-width encoders with no client-length input. `set_favorite` checks `client_slot` in 1..=4 before `- 1`.

Reachability note (not a finding): `care`, `play`, `equip_item`/`unequip_item`, `set_favorite`, `learn_trick`, `follow_location` and `set_in_water` have no production caller. `decode` (pets.rs:560-601) only produces Summon, Dismiss, SummonByItem, Rename and UiMode. Their client-input safety therefore cannot be exercised yet. Revisit them if they get wired to subtype 3/14/26/28 and the care subtypes.
