<!-- fleet job=bug-verify id=src-mining-rs-L1601-f1 status=done turns=12 usd=0.0126 tokens(read,write,in,out)=[200444, 34756, 26, 12454] model=claude-haiku-5-5 -->
# medium: prototype/osfr-tools/src/mining.rs:2039

**Verdict:** confirmed (the code defect is real), but the reach is narrow and I would downgrade the severity.

**Severity if confirmed:** low. The claim rated it medium; I think low is more accurate because the trigger needs non-default content or an unusual board state, and the failure only ends one session.

**Evidence**

1. **Real module.** `src/lib.rs:54` has `pub mod mining;`, so `mining.rs` is in the library. `shuffle_placements` is `pub`, and `shuffle_tiles` calls it at `mining.rs:1940`. This is not test-only code.

2. **Input reaches it.** `mining.rs:776-798`: `["OnActionMsg", index, list]` in the Playing phase calls `apply_powerup_action` with the client's list. `apply_powerup_action` (1773-1813) checks the definition exists (1783-1788), that `points.len() <= power` (1791), and that the pressed tile matches (1795-1800). Then it calls `shuffle_tiles` (1805).
   - `shuffle_tiles` (1894-1948): `candidates.retain` removes the pressed tile (1910). `cap = (power-1).min(candidates.len())` (1916). `points.len() != cap+1` is checked (1920). If `candidates` is empty, `cap = 0` and one point passes. The loop over `points.skip(1)` is empty, so `placements` is empty and `n = 0`. `shuffle_placements(&[], &[])` runs at 1940.
   - `shuffle_placements` (2034-2039): `vec![positions[0]; n]` is evaluated before the `n == 0` guard at 2040. Indexing an empty slice panics. The claim is correct on this point.

3. **Panic is contained.** `Cargo`/`spine_rules.rs:127-128` requires `panic = "unwind"`. `osfr-gateway.rs:4478-4481` (`contain`) turns the panic into `internal_error`, ending only that session. The panic is raised before `next` is committed, so no save is corrupted.

4. **Preconditions (why it is narrow).**
   - **Power 1 route:** `validate_powerup_definitions` only requires `power >= 1` (`mining.rs:1100`). With `power == 1`, any shuffle press leads to `n == 0`. But `Type8PowerupDefinition` is `skip_serializing_if = "Vec::is_empty"` (`mining.rs:253`), and `tests/mining_powerups.rs:364` asserts that the default written content has no `powerup_definitions`. So the shipped content never services shuffle at all (`unsupported mining action` at 1787). The operator must author a shuffle definition with power 1.
   - **Empty pool route (any power >= 2):** `candidates` is empty only if every other idle tile with value 200..=799 (except 800) is non-idle. Idle is set true by `initialize_board` (`mining.rs:1336`) and by the client's `OnIdleMsg` (809). It is cleared only for tiles moved or refilled by gravity (1524, 1535), and for tiles picked by wild/shuffle/shatter. A fresh board is fully idle, so this needs a client to withhold `OnIdleMsg` after gravity, and every eligible tile on the board must have moved. That is possible on a contrived or small board, but it is not a routine state.

**Corrected fix:** The proposed fix is right. Move the guard above the index, for example `if drawn_values.is_empty() || positions.is_empty() { return Vec::new(); }` at the top of `shuffle_placements`, so `positions[0]` is never evaluated on an empty slice. Optionally also reject `n == 0` in `shuffle_tiles` with `invalid("mining shuffle needs a tile")`.
