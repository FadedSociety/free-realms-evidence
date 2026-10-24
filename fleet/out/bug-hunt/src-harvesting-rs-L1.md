<!-- fleet job=bug-hunt id=src-harvesting-rs-L1 status=nothing_found turns=6 usd=0.0076 tokens(read,write,in,out)=[81875, 29063, 14, 6255] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/harvesting.rs lines 1-800 of 1320

## Window: `prototype/osfr-tools/src/harvesting.rs` lines 1-800

No reportable defects in this window. Every candidate I examined either cannot be reached from a client packet or save, or is guarded upstream.

**Candidates examined and dropped (none are findings):**

- **`harvesting.rs:131-135` `chain_time_bonus_seconds`**: `chain_tiles * 2` is unchecked u32 and would overflow for values above 2^31. The only callers are in `tests/harvesting.rs` (lines 170-171). Nothing in `src/` calls it, so no client value reaches it.
- **`harvesting.rs:738-756` `evaluate`**: the u32 `sum()` of cluster counts and `produce_value(slot).unwrap_or(0)` for slots beyond 16 are only reached from `tests/harvesting.rs:181-190`. `src/` never calls `evaluate`.
- **`harvesting.rs:140-146` `collectable_score`, `120-126` `chain_score`**: test-only callers. The subtraction in `chain_score` is guarded by `> MIN_CHAIN_TILES`.
- **`harvesting.rs:657-695` `parse_grid_templates`**: the only callers are in tests (`tests/harvesting.rs:79`). The `templates[index]` indexing is safe because `current` is only set after a push. Parsing uses `?`, not unwrap, and row growth is bounded by the file, which is server content, not client input.
- **`harvesting.rs:100-116` `produce_value`, `produce_index`, `produce_value_for`**: all arithmetic is bounds-checked (`index < PRODUCE.len()`, `checked_sub`). `produce_index` has no production callers.
- **`harvesting.rs:283-285` `produce`, `356-358` `region`**: these return `Option`. The production caller `harvesting_lifecycle.rs:129` (`player_guid == 0 || region(game_id).is_none()` → error) and `:431` (`ok_or_else`) reject unknown client-supplied `game_id`s before use.
- **`harvesting.rs:391-423` `parse_caret_exact` / `parse_caret`**: the column count is checked before the `v[i]` indexing in `SpawnRow`/`LevelRow`/`ProgressionRow`/`TimerRow::parse`, so those indexes cannot go out of range. Parse failures return `Err`.
- **`harvesting.rs:612-645` `TimerRow`**: the f64 division and `(v*10).round() as i32` are saturating casts and cannot panic.
- **`harvesting.rs:721-726` `GoalProgress::complete`**: `quota == 0` counts as complete. This matches the doc comment and `tests/harvesting.rs:189-190` ("returns true with no quota goals"). It is consistent, not a logic error.
- **Region produce slugs (`harvesting.rs:306-353`)**: all 16 slugs used by the six regions exist in `PRODUCE`, so `produce_value_for(...).unwrap()` in the tests cannot fail.

**Out-of-window context:** the client-facing path (`harvesting_lifecycle.rs`) was only spot-checked at the lines that consume `region()`. I did not audit it, since it belongs to another window.
