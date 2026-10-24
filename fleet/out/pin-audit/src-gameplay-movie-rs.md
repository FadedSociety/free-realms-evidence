<!-- fleet job=pin-audit id=src-gameplay-movie-rs status=nothing_found turns=5 usd=0.0022 tokens(read,write,in,out)=[22052, 10504, 12, 1376] model=claude-haiku-5-5 -->
# src/gameplay/movie.rs

Screened line 159 (`forging_tick_advances_once_per_250ms_step`, `src/gameplay/movie.rs`) is not a finding.

The `250` in `assert_eq!(wall(&game), before + 250, ...)` is the step of the movie clock, which is the code constant `const MOVIE_TICK_MS: u64 = 250;` (movie.rs:8, used by `elapsed_if_due` at movie.rs:94). It is not read from any file under `data/content`: a search of `data/` for movie tick or `tick_ms` values finds nothing. The test's own name says "once per 250ms step", so it is pinning the code's cadence constant, not a tunable data value. Retuning a data file would not affect it. No change is required under the data-file rule. If Bryce wants the cadence to be tunable later, the fix would be to move `MOVIE_TICK_MS` into a data file and have the test read it, or to reference the constant itself (`MOVIE_TICK_MS`) instead of the literal.
