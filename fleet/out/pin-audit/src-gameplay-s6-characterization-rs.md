<!-- fleet job=pin-audit id=src-gameplay-s6-characterization-rs status=nothing_found turns=3 usd=0.0020 tokens(read,write,in,out)=[8379, 10189, 8, 1219] model=claude-haiku-5-5 -->
# src/gameplay/s6_characterization.rs

No findings. All five screened assertions (s6_characterization.rs lines 207, 242, 686, 726, 743) expect `NOW + 250`, and the 250 comes from a compiled code constant, not a shipped data file:

- `prototype/osfr-tools/src/gameplay/movie.rs:8` `const MOVIE_TICK_MS: u64 = 250;`, used by `elapsed_if_due` (movie.rs:94) and documented as the 250 ms movie step.
- No `data/content/*.json` file holds a tick-interval field with this value. The only `max_tick` 0.25 rows are soccer data, which is unrelated.
- The test fixtures only set `NOW` and the tick times they pass in. The 250 is not a fixture value.

So these lines do not pin a data-file value, and the rule does not make them findings. Side note for the owner: the notes (`notes/Autopilot/F310.md:297`, `F327.md:223`) record that `MOVIE_TICK_MS` is still compiled and that moving it into content is a pending follow-up. If that move happens, these five assertions should then read the interval from the new content row rather than hard-code 250.
