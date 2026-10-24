<!-- fleet job=bug-hunt id=src-restoration-piece-039-rs-L1 status=nothing_found turns=5 usd=0.0054 tokens(read,write,in,out)=[45971, 23261, 12, 3993] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_039.rs lines 1-513 of 513

## Window: `prototype/osfr-tools/src/restoration/piece_039.rs` lines 1-513 (whole file read)

No defect I can tie to a client-reachable path. Nothing reported.

**Why nothing is reachable from a client or save:**
- The module is not compiled into the server crate. No `mod restoration` or `mod piece_039` exists under `prototype/osfr-tools` (outside comments). The only include is `prototype/osfr-tools/tests/piece_039.rs:30-32`, a `#[path]` test include.
- No `src/` caller of `GrantLedger`, `GrantKey::*`, `authorize`, `rank_of`, `progress`, `rank_for_xp` or `total_awarded` exists. The notes (`notes/Reviews/Delegated Task Readiness.v1.json`, `notes/Research/Pieces/039 Gathering job progression.md`) say the wiring is a pending lead integration.

**Checked and found sound (so a later reviewer need not redo them):**
- `progress()` at lines 221-238: `rows.len() - 1` is a constant 19. `rank` is always 1..=20, so the index is safe. `rank_experience * 100` at line 203 cannot overflow: the non-capped branch only runs when `xp < next threshold <= 90000`.
- `rank_for_xp()` at lines 209-219: the ladder is strictly increasing, so the result is the highest qualifying rank. The doc at line 208 says "the first row whose requirement is `<= xp` wins", which reads oddly, but the code's behaviour is the intended one. It is wording only, not a defect.
- `GrantKey::new` at lines 402-415 rejects non-positive ids. `GrantLedger::authorize` at lines 482-491 checks the zero amount before the duplicate lookup and mutates only on the `Granted` path, so there is no partial state.
- `total_awarded()` at lines 498-504 sums `u32` values into `u64`, which cannot overflow in any realistic ledger.

**Design gap, not a defect in reachable code:** `GrantLedger` is an in-memory `BTreeMap` with no persistence. A future wiring would need to persist the ledger, or a restart would allow replayed mining/harvesting outcomes to be granted again. Revisit this when the lead wires the module in.
