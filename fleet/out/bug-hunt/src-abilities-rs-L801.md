<!-- fleet job=bug-hunt id=src-abilities-rs-L801 status=nothing_found turns=6 usd=0.0042 tokens(read,write,in,out)=[49706, 15850, 14, 3434] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/abilities.rs lines 801-1008 of 1008

No defects found in `repo:prototype/osfr-tools/src/abilities.rs` lines 801-1008 that I can tie to a client-reachable input.

What I checked:

- **`unsupported_cast` (821-837):** the client-supplied `bar`, `slot` and `mode` dwords are read with `inner.get(at..at+4)`, so a truncated packet returns `Err`, not a panic. The length check (24 bytes for mode 0, 32 otherwise) runs before any use, and `slot` is range-checked with `(0..=7).contains`. The caller at `gameplay.rs:4630` runs it before any state change. The `unwrap` on `try_into` is safe because the slice is exactly 4 bytes. Its unit test matches the doc comment and the byte counts.
- **`build_attack_processed`, `build_actor_health`, `build_health`, `build_energy`, `build_hitpoint_delta`, `build_character_state`, `build_respawn_window` (839-918):** these are fixed-layout encoders over server-computed values (`CombatState`, `RespawnWindow`, applied deltas). No slicing, no unwraps, no client-controlled lengths.
- **`build_effect_tag` (920-955):** `duration_ms` uses `saturating_add` and `i32::try_from(...).unwrap_or(i32::MAX)`, so there is no overflow. The `tag_id`, icon and name come from the authored catalogue (`abilities.rs:706-727`, which uses `.expect("catalogue validated")`), not from a packet. `encode_add_effect_tag` (`restoration/piece_056.rs:653`) is a fixed-size write.
- **`header`, `put_i32` (957-963):** trivial.
- **Lookup helper at 801-811:** the `DEFINITION_LEN` length check short-circuits before `m[4..8]`, so the slice is in range.

The `#[cfg(test)]` module (965-1008) is out of scope.

Two things I noticed but did not count as defects: a malformed 36/10 returns `Err` (by design, per the doc comment), and the `build_*` helpers are only ever given server-side state.
