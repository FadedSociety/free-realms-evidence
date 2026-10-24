<!-- fleet job=bug-hunt id=src-mining-rs-L1 status=nothing_found turns=14 usd=0.0215 tokens(read,write,in,out)=[400935, 54775, 30, 21289] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/mining.rs lines 1-800 of 2434

No defects reported for `prototype/osfr-tools/src/mining.rs` lines 1-800 (read through 830 to finish the `OnIdleMsg` / `OnVerifyMsg` arms). I traced each candidate to its guard, and none is reachable from a client packet or save as a defect.

Candidates checked and dropped:

- **Chain score underflow, `mining.rs:727`** (`chain.len() as u32 - 3`): `validate_chain` (`mining.rs:1728`) rejects fewer than 3 points before this line runs, so it cannot underflow.
- **Chain index math, `mining.rs:718`, `:743`, `:809`, `:818-824`**: every index is bounded by `in_board` (`mining.rs:2151`, `x < left+width ≤ spec.width`, `y < top+height ≤ spec.height`). `OnVerifyMsg` checks `x < width` and `y < height` directly. `coordinate_list` caps each value at 4096.
- **Time-bonus arithmetic, `mining.rs:739-744`**: `remaining_ms` starts at `duration_seconds*1000` (≤600 000, `validate_spec` at `:1180`). `applied*1000 ≤ MAX_REMAINING_MS - remaining`, so neither the `saturating_sub` nor the `+=` can overflow.
- **Score and chain-count overflow, `:720-732`**: both use `checked_add`, with a ≤1e9 filter on score.
- **`read_i32` past the end, `handle` `:602-613`**: `handle` requires `inner.len() ≥ 15` before any `read_i32(inner, 11)`. `decode_payload` requires `len ≥ 20` before `read_i32(b,15)` and the `[19..len-1]` slice.
- **Division by zero, `validate_spec:1162-1163`**: `per_reward == 0` is rejected before `quota % per_reward`.
- **`unwrap` in `tick` (`:543`) and the `handle` payload path (`:631`)**: `active` is confirmed `Some` on both paths.
- **Shape-code and allocation bounds**: `width`/`height ≤ 32` is checked before the `width*height` product, and `MAX_PAYLOAD` / `MAX_CONTENT` / `MAX_GOALS` / `MAX_POWERUP_DEFINITIONS` cap the client-sized inputs.
- **All-wildcard chains (`validate_chain:1761`)**: they score and clear tiles but grant nothing. `wildcard_matches_the_chain_value_and_all_wildcards_are_legal` in `tests/mining.rs` shows this is intended. Score (`run.score`) feeds only the results packets and no reward transaction (the only other `.score` uses are at `:459`, `:728-732`, `:1592`, `:2391`, `:2395`).
- **Atomicity**: `handle` (`:916-922`) and `tick` (`:568`) mutate a cloned `next` and assign `self.state = next` only after the last `?`. Mid-chain errors therefore leave the saved state untouched.
- **Quit and offer gating, `:598-618`**: the sentinel and instance-id checks are present, and `native_offer_start` requires `phase == Offered`. Quit is refused for Won/Lost runs.

Not reviewed in depth: the post-800 handlers (`OnLevelEventMsg 50`, the win and loss arms around `:830-880`, `reward_transaction`), `gravity`, `collect_chain_goals` and `apply_powerup_action`. The window's mutations are atomic only if those later arms also keep their mutations on the clone, which I confirmed only for the end-of-`handle` commit.
