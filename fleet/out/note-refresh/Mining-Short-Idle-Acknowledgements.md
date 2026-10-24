<!-- fleet job=note-refresh id=Mining-Short-Idle-Acknowledgements status=nothing_found turns=11 usd=0.0119 tokens(read,write,in,out)=[225997, 38826, 24, 9485] model=claude-haiku-5-5 -->
# notes/Research/Mining Short Idle Acknowledgements.md

**Verdict:** current. Every code-checkable claim in the note holds at the tip. Only the test-count snapshot and the client citations could not be settled, so they are listed under Unsure, with no corrections.

**Corrections:** none.

Checked and confirmed:
- `src/mining.rs:2234` has the shared `coordinate_list(list, minimum_values)`. It strips exactly one trailing comma (`strip_suffix`), refuses an empty interior field, refuses an odd field count and refuses a value above 4096 (`:2235-2251`).
- `coordinates` (chain) calls `coordinate_list(list, 6)` (`:2258-2260`), so the three-tile floor is unchanged.
- `idle_points` calls `coordinate_list(list, 2)` (`:2267-2269`), and `powerup_points` also uses two (`:2273-2274`), as the note says.
- The `OnIdleMsg` arm (`:801-812`) parses first with `idle_points`. It applies marks only when `run.phase == Type8Phase::Playing`. It refuses out-of-board pairs with `invalid("idle outside mining area")`.
- The handler works on a per-message clone (`next = self.state.clone()`, `:619`), so a refusal leaves the run unchanged, as the note says.
- `tests/mining_idle.rs` exists and is new. It imports `write_content` from the production crate and has six `#[test]` functions (`:143, 160, 179, 214, 236, 267`), which matches "`mining_idle` 6". `mining_dead_board` has 3 tests, matching the note. `mining_review` has 13, matching the note.

**Unsure:**
- Focused-suite counts. `tests/mining.rs` has 20 `#[test]` lines, but the note says "`mining` 21". `tests/mining_powerups.rs` has 20 `#[test]` lines, but the note says "`mining_powerups` 22". The counts may have drifted since the fix, or the note may have been wrong when written. I could not run cargo to settle it. Other notes also say 21 and 20 for these files (e.g. `Research/Mining Clickable Powerups Implementation.md:147` says 20).
- Pins (`src/mining.rs` `8B32D7C5…`, `tests/mining_idle.rs` `8C2A45F4…`), the RED/GREEN logs and `lab/reports/mining-idle-ack-20261009T2000Z/receipt.json`. The lab folder is not in the repo and I have no hashing tool, so I could not check them.
- Client citations (`core/Grid.as` 1356-1363, `GameClientNetwork.as` 26-29, `GameLevel.as` 543-552, `ServerGrid.as` 78-102 and 103-133, `GameData.as` 47). The `client_sql` `fn` table and `refs` returned no matches for `OnIdleMsg`, `NowIdle`, `sNowIdle` or `nMINIMUM_CHAIN_LENGTH`, so I could not check them.
- "check --lib clean" and "no release build" are run claims I could not reproduce.
