<!-- fleet job=note-refresh id=Pieces-017-Minigame-disconnect-recovery status=done turns=15 usd=0.0105 tokens(read,write,in,out)=[253513, 27727, 32, 8920] model=claude-haiku-5-5 -->
# notes/Research/Pieces/017 Minigame disconnect recovery.md

**Verdict:** minor drift. The semantics hold at the tip (cancel without consuming or awarding, attempt counter kept, checker and tests present with the stated counts). Three citations moved, and one scope statement is slightly overbroad.

**Corrections:**

1. old: `prototype/osfr-tools/src/gameplay.rs:425-441`: `initialize_world` cancels
   new: `prototype/osfr-tools/src/gameplay.rs:1680-1734`: `initialize_world` cancels
   why: repo:prototype/osfr-tools/src/gameplay.rs:425-441 is `npc_visibility_revision`/`shared_npc_view`. `initialize_world` is at gameplay.rs:1680; its cancel block (smelting, cooking, forging) is at gameplay.rs:1716-1734.

2. old: `smelting`, `cooking` and `forging` on every world load, "Keep attempt
   new: `smelting`, `cooking` and `forging` on a world load that has an opening movie state (housing, soccer and kart return earlier, and the cancel block is skipped when `opening` is none), "Keep attempt
   why: repo:prototype/osfr-tools/src/gameplay.rs:1685-1703 (early returns for housing, soccer, kart and `self.opening.is_none()`) before the cancel block at 1716-1734. The same function also cancels Mining/Harvesting at gameplay.rs:1738-1745, which the note does not mention.

3. old: The service `cancel()`
   methods (`cooking.rs:257`, `smelting.rs:245`, `forging.rs:239`)
   new: The service `cancel()` methods (`cooking.rs:338`, `smelting.rs:326`, `forging.rs:325`)
   why: repo:prototype/osfr-tools/src/cooking.rs:338, repo:prototype/osfr-tools/src/smelting.rs:326, repo:prototype/osfr-tools/src/forging.rs:325. Each takes `state.active`, emits header 19 unless `results_presented`, and returns `changed: true`. Only the line numbers are stale.

4. old: disconnect persisted mid-movie is cleared on the next `Loaded` event.
   new: disconnect persisted mid-movie is cleared on the next `Loaded` event (`prototype/osfr-tools/src/gateway.rs:1477-1487` calls `initialize_world` there).
   why: repo:prototype/osfr-tools/src/gateway.rs:1477-1487 is the `Event::Loaded` handler that calls `game.initialize_world`. `src/bin/osfr-gateway.rs` only reloads the snapshot (`load_gateway_from`, bin:908-973) and saves before queueing replies (bin:1928-1936). The note's cite to the bin alone is incomplete, not false.

**Checked and holding:**
- `src/restoration/piece_017.rs` exists, with `audit_conservation` (line 111) and `audit_recovery` (line 204). Terminal runs are refused (line 174), and reused ids (line 183) and regressed counters (line 155) are rejected.
- `tests/piece_017.rs`: 7 `#[test]` plus 2 `#[ignore]` (lines 64-213), matching "seven always-on contract tests" and "2 ignored".
- `scripts/pieces/piece_017.py` exists with the three check ids (lines 181, 211, 230) and `MOVIES = ("cooking", "smelting", "forging")`.
- `tests/pieces/test_piece_017.py` exists.

**Unsure:**
- "re-loads the persisted snapshot for every new session": true for the local path (`bin:1017-1018`). With an account store, the session clones a startup template (`bin:1012-1016`) and the character loads at login. I did not trace the login path.
- The `GameClientDisconnect`, `SoeGameFramework.as` and `lab/` claims cannot be checked at this tip; `refs` has no `GameClientDisconnect` match.
- The command-result counts (24 lib, 9 Python, 2 cooking_gameplay ignored) were not re-run.
