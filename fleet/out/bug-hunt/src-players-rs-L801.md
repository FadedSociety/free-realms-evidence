<!-- fleet job=bug-hunt id=src-players-rs-L801 status=nothing_found turns=15 usd=0.0107 tokens(read,write,in,out)=[239018, 33954, 32, 8175] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/players.rs lines 801-873 of 873

No defect found in `prototype/osfr-tools/src/players.rs` lines 801-873 (the AddPc tail, `build_position_update`, `build_remove_player`, `tunnel`, and the `put_*` helpers).

What I checked:

- **`put_string` `expect` (line 854):** the only panic path in the window. Every string it can receive from `build_add_pc` is one of `first_name`, `last_name`, `head`, `hair`, `skin_tone`, `face_paint`, `model_customization`. `PlayerPresentation::validate` (lines 672-685) rejects any of these whose length does not fit in `i32`. Every route that stores a presentation runs `validate`: `join_with_presentation` (line 274) and `set_presentation` (line 354). `presentation` is not a `pub` field of the registry's session map, and `sessions.insert` (line 290) is the only insert, so no unvalidated presentation reaches `build_add_pc`.
- **AddPc size bound:** `ADD_PC_FIXED_INNER_BYTES` (195) plus the 7-byte tunnel header plus string bodies plus attachment rows matches the byte count I derived from the writers in lines 755-817. The 64 KiB cap therefore holds, so `tunnel`'s `as u32` cast and the attachment bytes cannot overflow.
- **Mount block (lines 805-810):** `ride_guid`, `seat`, `queue` and `lift` come from `MountTail`, which the server builds (`RideView::tail`, `MountTail::NONE`) and not from a client packet. `lift` is always `0.0`.
- **Title, VIP, guild, temporary-model and persistent-effect fields (lines 798-804, 812-815):** constants, so no client input reaches them.
- **`wield_type` (line 811):** `validate` rejects negative values (line 666).
- **`build_position_update` (lines 819-832):** `position` and `heading` pass `validate_pose` (finite check) in both `join_with_presentation` (line 273) and `update_pose_with_state` (line 387). `movement_state` and `movement_unknown` are server-side values stored by `update_pose_with_state`, and the registry stores them as opaque bytes. Nothing here panics.
- **`build_remove_player` (lines 834-841):** takes only the session's own `character_guid`, so there is no client authority.

Unverified observation, not reported: `build_remove_player` writes submode `0` ("immediate removal"), while the other 35/3 writers (`mounts.rs:837`, `pets.rs:1686`, `gameplay.rs:2411`) write submode `1`. The client reader (`008d69f0`/`008d6830`) shows only a u16 read and does not show what the submode means, so I cannot demonstrate a defect.
