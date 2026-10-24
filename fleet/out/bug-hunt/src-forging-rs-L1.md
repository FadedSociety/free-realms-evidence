<!-- fleet job=bug-hunt id=src-forging-rs-L1 status=nothing_found turns=10 usd=0.0238 tokens(read,write,in,out)=[247672, 56504, 22, 28563] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/forging.rs lines 1-800 of 1504

No reportable defects in `prototype/osfr-tools/src/forging.rs` lines 1-800. I read the whole window and the helpers it calls (`validate_chain`, `coordinates`, `number_list`, `number`, `decode_payload`, `validate_run`, `gravity`, `results`, `read_i32`) at lines 800-1210, and checked the production call sites in `gameplay/crafting.rs`.

Candidates checked and dropped:

- **Panics on client input:** `read_i32` offsets 3/7/11 are safe because `handle` requires `len >= 15`. `decode_payload` requires `len >= 20`, `1 <= n <= 4096` and `len == 19+n` before slicing. `number_list` caps the field count at `CELLS*stride` and requires a multiple of the stride. `validate_chain` rejects `len < 3` before `chain.len() - 3` at 512, and checks bounds before `a.board[y*SIDE+x] = 0` at 503. `OnVerifyMsg` bounds-checks x and y before indexing at 559. The hammer drop at 565-571 checks `in_board` before indexing at 571.
- **Overflow:** score and time arithmetic at 512-526 is capped by `filter`/`min`, and `remaining_ms <= 600000` is held by `validate_state`. `number()` caps at 1e9 before `as usize`. `wrapping_mul` is used for the RNG seed.
- **Atomicity:** `handle`, `tick` and `begin_recipe` mutate a clone and assign `self.state` only after `validate_state`/`validate_run` succeed. The reward transaction is emitted once, only on `LevelComplete -> OnNextLevelMsg`, and a second completion is blocked because the phase becomes `Won`.
- **Trusting the client:** the board, score, collected count, completion and reward all come from server state (`validate_chain` against the server board, the bottom-row `COLLECTABLE` check, the quota check). The `FRServer_Game*`/`ScoreSet` reports are informational only. Ingredients are re-checked at completion in `gameplay/crafting.rs:356-365`.
- **Compat `begin()` at 236-249** skips the inventory check by passing the recipe's own `consumes`, but no production code calls it (only tests do), so it is unreachable from a client.
- **`OnLevelEventMsg 50` not gated by `paused`:** this is inconsistent with `OnChainMsg`, but no score, time or reward gain follows from it, so it is not a defect.
- **Unhandled messages return `Err`:** this is the designed behaviour, not a defect.
