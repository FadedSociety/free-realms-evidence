<!-- fleet job=bug-hunt id=src-restoration-piece-047-rs-L1 status=nothing_found turns=4 usd=0.0051 tokens(read,write,in,out)=[29707, 21155, 10, 4347] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_047.rs lines 1-634 of 634

## Window: `prototype/osfr-tools/src/restoration/piece_047.rs` lines 1-634 (whole file)

No reportable defects in this window.

What I checked:

- **Stat table (lines 71-417):** `stat_row` (434-436) indexes `CHARACTER_STAT_IDS` by `id as usize` with `.get()`, so an out-of-range id returns `None` and cannot panic. The table is ordered 0..68, so the index equals the id. The 69-entry count matches `CHARACTER_STAT_ID_COUNT`.
- **`decode_item_stat` (444-459):** `stat_row` is checked before use. Non-finite values (NaN and infinity) are rejected before the `fract()` check, so NaN cannot slip through the integral test. Integral-only enforcement for `Int` kinds is correct. Integral values outside i32 range are accepted, but nothing in the window or in the notes claims an i32 range, and there is no consumer, so I did not report it.
- **Class rows (475-526) and item rows (546-584):** I decoded the float bit patterns by hand. The parachute values are 8, 2, 20, 0.75, 4, 1, 4, and the Fire Hawk values are 11, 6, 22, 0.75, 3, 1, 4, 5. Both satisfy min <= default <= max, and the int-kind stat 64 is 1.0. The `gear_class` and `gear_stat_item` lookups are plain `find`s and cannot panic.
- **`equip_gate` (609-634):** The `None` class is refused. A non-matching owner is refused. The rank check `profile_rank < required` is the correct direction. `members_only && !member` is correct. The result matches the doc comment and the tests at `tests/piece_047.rs` 168-200.

Reach: a grep over `repo` shows `equip_gate`, `decode_item_stat`, `gear_class`, `gear_stat_item` and `stat_row` are called only from `tests/piece_047.rs` (included via `#[path]`) and the Python checker. No server packet handler or save loader calls them, so nothing in this file is reachable from client input today.

Observation, not a finding: `equip_gate` takes `min_profile_rank` and `members_only` as caller-supplied arguments rather than reading them from the `GearStatItem` row. A future caller that passes `None`/`false` would bypass the item-level gate. Nothing calls it yet, so this is not a current defect. The research note (`notes/Research/Pieces/047 Gear attributes.md` lines 72-76) describes the function as unwired policy.
