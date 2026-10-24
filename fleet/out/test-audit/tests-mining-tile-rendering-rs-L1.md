<!-- fleet job=test-audit id=tests-mining-tile-rendering-rs-L1 status=done turns=7 usd=0.0055 tokens(read,write,in,out)=[68601, 22285, 16, 4058] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/mining_tile_rendering.rs lines 1-178 of 178

Two findings in lines 1-178. The first initialize_board test and the malformed-content refusal test check what their names claim. The `tile_index_never_underflows_on_malformed_content` refusal path is real: `mining.rs:1369-1372` uses `checked_sub` with the "mining tile value below its category" error, and `validate_spec` (`mining.rs:1130-1175`) does not police `spec.tiles`.

- **[medium] tests/mining_tile_rendering.rs:162 tile_index_fix_keeps_run_state_and_snapshot_bytes - the name promises snapshot bytes are kept, but the body never pins any bytes and never touches tile info.**
  - Why it cannot catch a regression: the test only checks `state.version == 1`, `next_instance_id == FIRST_INSTANCE + 1`, and that a `serde_json` round trip of the state is equal to itself (lines 168-173). It does not compare against a golden byte string or a pre-fix snapshot. A change that renames or reorders serialized fields, or adds a field with a new default, still round-trips and still passes. A change that reverts the tile-index fix (emitting `category` as the second field) also leaves `Type8State` untouched, so it also passes.
  - Fix: pin the serialized snapshot against a literal byte string or JSON fixture captured from the current engine (`assert_eq!(text, EXPECTED_SNAPSHOT_BYTES)`), or rename the test to something like `..._round_trips_run_state` and drop the "snapshot bytes" claim.

- **[low] tests/mining_tile_rendering.rs:177 tile_index_fix_keeps_run_state_and_snapshot_bytes - `assert!(run.board.iter().any(|value| (401..=405).contains(value)))` is a weak, unrelated check.**
  - Why it cannot catch a regression: any board that contains one selectable tile passes, regardless of whether the tile index is correct, the board is laid out correctly, or the board was built from `mining_spec`. It only shows the random fill produced some 401-405 value.
  - Fix: assert the exact board, or at least the exact count and positions of the 401-405 cells for the fixed seed (for example, the positions produced by `shape` code 1 with `random_tile`), so that a change in board generation fails.
