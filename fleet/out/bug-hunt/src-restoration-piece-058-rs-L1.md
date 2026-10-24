<!-- fleet job=bug-hunt id=src-restoration-piece-058-rs-L1 status=nothing_found turns=6 usd=0.0069 tokens(read,write,in,out)=[65458, 26689, 14, 5855] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_058.rs lines 1-488 of 488

No reportable defects in `prototype/osfr-tools/src/restoration/piece_058.rs` lines 1-488.

What I checked:
- **Wire decoders (`decode_respawn_window`, L190-224; `decode_safe_teleport_request`, L234-253).** Every index is preceded by a length check (`len < 4`, then `len < 20`; `len < 2`), so no panic on short or long input. Trailing bytes are rejected. Opcode and sub mismatches return `WrongPacket`.
- **`ReviveArbiter::revive` (L408-449).** Validation runs before any mutation. `NotKnockedOut`, invalid position and `NotEnoughCoins` all return before `coins`, `health`, `knocked_out` or `revives` change. The debit `self.coins -= charged_coins` cannot underflow, because the paid branch is guarded by `coins < revive_cost` and the safe branch charges 0. Replays hit `NotKnockedOut`.
- **`knock_out` / `apply_damage` (L372-404).** The once-only window behaviour matches its doc comment and the tests at tests/piece_058.rs L152-205. Saturating counters are used throughout.
- **`valid_vector` (L272-276).** Rejects NaN, infinity and out-of-bound coordinates, and the rotation is checked as well as the position.
- **`TerminalLedger::settle` (L466-474).** Matches its doc comment (first settlement only, replays return false).

Notes, not findings (I could not tie these to a client-reachable path):
- `TerminalLedger` (L458-487) keys a `BTreeMap` by `i32` instance id and never evicts. If a future caller feeds it client-sent instance ids, memory grows without bound. No caller exists today.
- The whole module is unregistered. `src/lib.rs` has no `pub mod restoration`, and only `tests/piece_058.rs` (via `#[path]`) and `notes/` reference it. Nothing in `src/` calls `ReviveArbiter`, `decode_respawn_window`, `decode_safe_teleport_request` or `TerminalLedger`, so no client packet reaches the code in this window.
- Known wire-format gaps (the trailing field names and the paid-revive request) are already disclosed in the module header as MISSING. They are not code defects.
