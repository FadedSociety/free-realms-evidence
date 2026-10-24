<!-- fleet job=pin-audit id=tests-soccer-service-rs status=nothing_found turns=6 usd=0.0036 tokens(read,write,in,out)=[37885, 18003, 14, 1842] model=claude-haiku-5-5 -->
# tests/soccer_service.rs

No findings in `prototype/osfr-tools/tests/soccer_service.rs` for the four screened lines.

- **:349 / :350 (game clock remaining/elapsed, 180 and 0.25 step)**: the 180 comes from the code constant `HALF_SECONDS` in `src/soccer.rs:19`, reached via `MatchConfig` defaults (`src/soccer_match.rs:147`). It is not a value in any `data/content` file, and the 0.25 is the test's own tick argument. Not a data-file pin, so no finding.
- **:398 (kick power 4.0)**: comes from the test's own `policy()` fixture (`max_power: 4.0`, lines 70-76), which is passed into `SoccerService::new`. The test sets it, so no finding.
- **:403 (ball velocity x 4.0)**: same source. `velocity = charge * policy.max_power` with the fixture's 4.0, so it is computed from the test's own fixture, not a shipped data value. No finding.
