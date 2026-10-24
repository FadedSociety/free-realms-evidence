<!-- fleet job=note-refresh id=Mining-Clickable-Powerups-Implementation status=done turns=14 usd=0.0180 tokens(read,write,in,out)=[346254, 49426, 30, 16617] model=claude-haiku-5-5 -->
# notes/Research/Mining Clickable Powerups Implementation.md

**Verdict:** minor drift. The core design claims hold at the tip (validation, action dispatch, the four effects, the queue discipline, the shuffle walk and the default-path guard). Three things are stale: the reply-echo claim, the test count, and the collected-range numbers.

**Corrections:**

1. `old:`
   ```
   `list` is the recovered trailing-comma `x,y,...` form; the reply echoes
      `index` and the same coordinates.
   ```
   `new:`
   ```
   `list` is the recovered trailing-comma `x,y,...` form; no reply echoes the action.
      The server answers only through the tile-queue and gravity events it already sends.
   ```
   `why:` `repo:prototype/osfr-tools/src/mining.rs:776-800` (the `OnActionMsg` arm only calls `apply_powerup_action`, which writes no reply). `repo:prototype/osfr-tools/src/mining.rs:1773-1813` writes no `OnActionMsg` message. `repo:prototype/osfr-tools/tests/mining_powerups.rs:851` asserts no `OnActionMsg` text comes back. The note's own review correction 1 says the echo is gone, so this bullet contradicts it.

2. `old:` `20 behavioral tests`
   `new:` `22 behavioral tests`
   `why:` `repo:prototype/osfr-tools/tests/mining_powerups.rs` has 22 `#[test]` functions (lines 285 through 875). The note's own repair section (“22 tests, all passing”) agrees.

3. `old:` `- \`tests/mining_powerups.rs\`: 20 passed, 0 failed.`
   `new:` `- \`tests/mining_powerups.rs\`: 22 tests in the file at the tip (the 20-pass run above predates the shuffle repair; see the repair section below).`
   `why:` `repo:prototype/osfr-tools/tests/mining_powerups.rs` (22 `#[test]` functions); the note's repair section at lines 190-192.

4. `old:` `` `mining_powerups` 20 — all green `` (in the Mining family line)
   `new:` `` `mining_powerups` 22 — all green (per the repair section) ``
   `why:` same as correction 2 and 3.

5. `old:` `` `900..=902` collected powerups: `validate_powerup_definitions` refuses any definition in that range ``
   `new:` `` `900..=949` collected powerups: `validate_powerup_definitions` refuses any definition in that range ``
   `why:` `repo:prototype/osfr-tools/src/mining.rs:1092-1095` refuses `TILE_POWERUP_START..TILE_POWERUP_PRESSME`, which is 900..=949, with “collected mining powerups 900..=949 are not implemented”.

6. `old:` `A \`900..=902\` tile that still reached the bottom`
   `new:` `A \`900..=949\` tile that still reached the bottom`
   `why:` `repo:prototype/osfr-tools/src/mining.rs:1569-1574`. The fall handler accepts `TILE_POWERUP_START..TILE_POWERUP_PRESSME` (900..949), and its comment cites the 600..949 fall range.

**Checked and holding (no change):**
- `validate_powerup_definitions` refuses unknown values, duplicates, zero or oversized power, out-of-range tuning, and `powerup_percent > 0` with no weighted definition (`mining.rs:1076-1128`).
- `OnPowerupInitMsg value, duration, power` is emitted per row, sorted ascending, in `initialize_board` (`mining.rs:1380-1395`).
- `has_move` returns true for any `950..=953` tile (`mining.rs:2087-2098`).
- Shatter neighbour order is down, up, right, left (`mining.rs:1994-1995`).
- Shuffle pops the pressed tile and keeps it as `200` (`mining.rs:1906-1912`).
- `action_draw` pops from the front and refills by `QUEUE_BATCH` while short (`mining.rs:2172-2191`, with `QUEUE_MIN` 50 and `QUEUE_BATCH` 20 at lines 107-108).
- The `shuffle_placements` walk gives `[401,402,403] -> [403,401,402]` and `[401,401,402] -> [402,401,401]` when I traced `mining.rs:2034-2073` by hand.
- Short lists are refused for all four powerups (`mining.rs:1791-1793`, `1837-1839`, `1876-1877`, `1920-1922`, `1983`).
- `powerup_percent == 0` takes the original `random_tile` branch (`mining.rs:1482`).
- `mining_spec()` ships `powerup_percent: 0` (`mining.rs:1039`).
- `TILE_POWERUP_*` constants are in `mining.rs:68-76`.
- The `default_writer_bytes_carry_no_powerup_key` and `default_powerup_percent_matches_the_old_engine_byte_for_byte` tests exist.
- The `Content` serde attribute `skip_serializing_if = "Vec::is_empty"` is at `mining.rs:253`.

**Unsure:**
- Test counts for the other Mining-family and gateway suites (`mining` 21, `mining_review` 13, `type8_gateway` 10, and the rest) were not counted, and the cargo and clippy results cannot be checked by reading.
- The `*.rs:NNN` and `ServerGrid.as` / `Grid.as` / `GameLevel.as` line numbers in the note point at client references, not at our code, so I did not verify them.
- The “wildtile pressed tile popped first (`StartWildTiles` 1013-1024)” and similar client-reference citations were not checked.
