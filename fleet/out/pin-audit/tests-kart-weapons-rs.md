<!-- fleet job=pin-audit id=tests-kart-weapons-rs status=nothing_found turns=6 usd=0.0029 tokens(read,write,in,out)=[38073, 12446, 14, 1907] model=claude-haiku-5-5 -->
# tests/kart_weapons.rs

No findings in `prototype/osfr-tools/tests/kart_weapons.rs` for the three screened lines (319, 352, 368).

- **Line 319 (`RACE_START + 99` / 10 Hz slot):** the 99 ms is a test-side probe just under the update cadence. The cadence is `MISSILE_UPDATE_INTERVAL_MS = 100` in `src/kart_weapons.rs:86`, a code constant. No data file carries it, so this is not a data-file pin.
- **Line 352 (`MISSILE_CREATE_FORWARD_M + 2.0 * expected`):** `expected` is `MISSILE_SPEED_MPS * (MISSILE_UPDATE_INTERVAL_MS / 1000)`. `MISSILE_SPEED_MPS = 35.0` (`src/kart_weapons.rs:79`), `MISSILE_CREATE_FORWARD_M = 3.0` (`:83`), and `MISSILE_UPDATE_INTERVAL_MS` is at `:86`. All three are reconstructed code constants. The test imports them rather than hard-coding numbers, and no shipped data file has a missile speed.
- **Line 368 (`full_flight` from `MISSILE_TTL_MS`):** `MISSILE_TTL_MS = 4_000` (`src/kart_weapons.rs:76`) is a code constant, computed from the imported symbols. The only `ttl_ms` in `data/content` is `power_ups.json` `pickup.ttl_ms = 30000`, which is the power-up pickup despawn and has no link to the missile lifetime.

Mine arm and trigger delays are not present in any data file, so nothing in this file pins them. The only related gap is that these weapon constants live in code instead of `data/content`. That is a separate design question, not a test-pins-a-data-value finding.
