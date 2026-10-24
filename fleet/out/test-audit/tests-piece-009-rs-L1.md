<!-- fleet job=test-audit id=tests-piece-009-rs-L1 status=nothing_found turns=5 usd=0.0093 tokens(read,write,in,out)=[45062, 25964, 12, 11267] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/piece_009.rs lines 1-397 of 397

No findings in `prototype/osfr-tools/tests/piece_009.rs` lines 1-397. I read the whole window and the code under test (`src/restoration/piece_009.rs`, lines 1-757). I hand-checked the expected values against the geometry and the apply/validate order, and each test's assertions do exercise what its name claims.

What I checked:
- **Geometry (`pawn_geometry`, `pawns_move_forward...`, `capture_needs...`, `double_jump...`, `promotion...`):** the expected spots match `spot_from_offset` / `jumped_spot` when worked by hand. For example, 20 has only 16 as a forward step, its jump lands on 13, and the 22→13→6 chain jumps 17 and 9. The expectations are not derived from the code's own output.
- **`a_side_without_legal_moves...`:** black 20 is blocked by 16 and the jump landing 13, so `settle` finishes the game with red as winner, and the later apply returns `GameFinished`.
- **`compulsory_capture...`:** 24→20 is a quiet step, so `validate` returns `CompulsoryCapture`. The board is compared to a clone, so "changes nothing" is checked.
- **`turn_replay...` and `late_replays...`:** `validate` checks range, then empty, then finished, then replay, then turn. The expected error for each call matches that order. The whole-session `PartialEq` comparison does check that no state changed.
- **`illegal_destinations...`:** the error for each of `NoPiece`, `WrongSide`, `IllegalDestination` and `EmptyChain` matches the order of checks in `validate`.
- **Payload tests:** the `split('\t')` and `split(',')` results match each expected error variant.
- **Event sequences:** the exact `MOVE` / `MOVE_JUMPED` / `MOVE_KING` / `TURN_END` / `TURN_START` vectors match `apply`, including the mover's wire index in `TURN_END`.
- **Skips and fixtures:** there are no `#[ignore]` attributes and no early returns in the window.

Non-blocking notes, not reported as findings: `PayloadError::MalformedPayload` (wrong field count) and the `MAX_MOVE_PAYLOAD` length refusal are not exercised anywhere in this window. That is a coverage gap, not a test that cannot fail.
