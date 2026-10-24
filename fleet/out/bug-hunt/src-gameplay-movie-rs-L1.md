<!-- fleet job=bug-hunt id=src-gameplay-movie-rs-L1 status=nothing_found turns=10 usd=0.0073 tokens(read,write,in,out)=[128049, 24457, 22, 6002] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/gameplay/movie.rs lines 1-201 of 201

No defects found in `prototype/osfr-tools/src/gameplay/movie.rs` lines 1-201.

What I checked:

- **`elapsed_if_due` (movie.rs:92-95):** `now_ms.saturating_sub(clock?)` cannot underflow, and the `u32::MAX` clamp prevents truncation. Its doc says "in `MOVIE_TICK_MS` steps", but it returns the raw elapsed time, not a multiple of 250. I did not count this as a defect. The callers stamp the clock to `now_ms` after each tick (crafting.rs:91, 110), so no time is lost or double-counted. The engines add `elapsed_ms` with `saturating_add` and cap at `MAX_WALL_MS` (forging.rs:353, mining.rs:544), so a long gap cannot overflow.
- **Atomicity of the tick path:** `movie_tick` and `tick_gather` (crafting.rs:88-110) can leave the engine advanced if `apply_craft` fails after `tick()`. The clock is then not restamped. However, `gateway.rs:1841-1842` runs `gameplay.tick` on a clone (`game.clone()`) and discards it on `Err`, so no partial state is saved.
- **`Movie` helpers (movie.rs:14-88):** the match arms are exhaustive and the strings are static. `running_movie` (crafting.rs:9-13) picks the first match in `Movie::ALL`, so overlapping occupations cannot panic.
- **Test helper `start_forging` and the tests (movie.rs:100-201):** these are `cfg(test)` only and excluded from the defect criteria. Their assertions match the tick behaviour in forging.rs:343-373.

The window has no client-reachable panic, unbounded growth, lost-atomicity save, client-trusted authority, or wrong comparison.
