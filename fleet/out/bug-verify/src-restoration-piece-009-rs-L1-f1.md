<!-- fleet job=bug-verify id=src-restoration-piece-009-rs-L1-f1 status=done turns=5 usd=0.0045 tokens(read,write,in,out)=[42336, 18984, 12, 3370] model=claude-haiku-5-5 -->
# medium: `piece_009.rs:594-600`

**Verdict:** `refuted` (at check 1: the code is not in the server build)

**Severity if confirmed:** n/a

**Evidence:**

1. **Module tree (decisive).** `piece_009.rs` is not registered anywhere in the real server:
   - `search` for `piece_009` across `prototype/osfr-tools` returns only `tests/piece_009.rs` (lines 2, 12, 13). Its only inclusion is `tests/piece_009.rs:12-13`: `#[path = "../src/restoration/piece_009.rs"] mod piece_009;`.
   - `src/lib.rs` has no `restoration` reference (search returned nothing), and no `mod restoration` / `pub mod restoration` exists anywhere under `src/`. `src/restoration/` has no `mod.rs`.
   - `src/bin/` contains no `piece_009` or checkers reference.
   - The module's own header (`piece_009.rs:1-40`) and the integration comments in other pieces (e.g., `piece_095.rs:57`, `piece_096.rs:34`) say the lead has not yet registered these modules.
   So `CheckersSession::apply` and `validate` are reachable only from the test binary. This makes the defect test-only, and it is not a defect in the running gateway.

2. **Reach (confirms the reviewer's own caveat).** `search` for `CheckersSession|decode_move_payload|MoveError` across `prototype/osfr-tools` finds only `piece_009.rs` and `tests/piece_009.rs`. No gateway, gameplay or save-load path calls `apply`, so no remote packet can reach `validate` (`piece_009.rs:584`).

3. **Behaviour as described (for completeness).** The lines do match the claim: `piece_009.rs:594-600` refuses any `(side, from, path)` that appears in `applied`, and `settle()` (`:695-703`) checks only `board.has_action`. The replay policy is deliberate and tested (`tests/piece_009.rs:342-350` asserts `Replayed` for a later repeat). The module header (`piece_009.rs:30-31`) explicitly labels replay protection as "Reconstructed policy (explicitly not original)". So this is a design choice in unwired code, not a live exploit.

**Corrected fix:** None needed for the current tree. If the checkers engine is later registered in `src/lib.rs` and wired to a gateway handler, re-open this: the position-blind replay key at `piece_009.rs:594-600` would then refuse legal repeated king moves, and the reviewer's suggested fix (key on board/turn, or drop the scan and rely on `NotYourTurn`) would be the right direction. Until then the finding belongs in a notes/backlog item, not a live defect report.
