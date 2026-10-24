<!-- fleet job=note-refresh id=Pieces-099-Multi-client-integration-harness status=done turns=19 usd=0.0192 tokens(read,write,in,out)=[612787, 53003, 40, 12976] model=claude-haiku-5-5 -->
# notes/Research/Pieces/099 Multi-client integration harness.md

**Verdict:** minor drift. Most claims hold at the tip (file paths, 9 Rust tests, 16 Python tests, the scripted steps per case, the 18-row trade table, the six grouping intents, and the client constructor `FUN_00c6a7b0`, which I confirmed in the client). One claim about dispatch is false for the shipped binary.

**Corrections:**

1. `old:` The local server currently dispatches neither family: a gateway without gameplay content drops application messages, and `Gameplay::handle` ends in a silent `Ok(out)` for unknown families.
   `new:` The library `Gateway` that the harness drives dispatches neither family: a gateway without gameplay content drops application messages, and `Gameplay::handle` ends in a silent `Ok(out)` for unknown families. The shipped `osfr-gateway` binary does route family 59 (sub-opcodes 3 and 6-10) to `Session::route_trade`, which calls `TradeService::handle` and queues `settle_trades`. Family 175 still has no dispatcher anywhere.
   `why:` repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:2121-2122 (`if inner.starts_with(&[59, 0]) { return self.route_trade(...) }`), :2095-2107 (`route_trade` → `world.trades.handle`), :1902 (caller in `route_application`), :2008 (`settle_trades`). The application classifier at repo:prototype/osfr-tools/src/gateway.rs:507-508 names family 59 subtypes 3 and 6-10 as "trade". No `175` route exists in the gateway files (search of `src` for `GROUPING_FAMILY`, `starts_with(&[175` and `(Some(175)` finds only piece_099.rs:57 and :396). `repo:notes/Design/Build Ledger.md:47` also lists the trade commit in `bin/osfr-gateway.rs`.

**Checked and holding:**
- `src/restoration/piece_099.rs` and `scripts/pieces/piece_099.py` exist. `tests/pieces/test_piece_099.py` has 16 test methods.
- `tests/piece_099.rs` has 9 `#[test]` functions (lines 127-574). The `#[path]` includes of `piece_020.rs` and `piece_099.rs` are at lines 28-33.
- `src/lib.rs` does not register `piece_099` or `piece_020`, so the "lead registers" gate is still open.
- Case scripts: Party (9 steps), Trade (8 steps; the test asserts 8), Activity (8 steps) match the note's descriptions (`piece_099.rs:590-768`).
- `TradeMessage::CLASS_TABLE` has 18 rows (`piece_099.rs:120-139`). `GroupRequest` sub-opcodes 20/17/18/21/19/22 are as stated (`piece_099.rs:369-389`).
- `Gameplay::handle` ends in `Ok(out)` (`gameplay.rs:5374`).
- The `trade_case_records_the_silent_drop_on_the_real_gateway` test drives the library `Gateway`, so the "unhandled" record is still accurate for that path (`tests/piece_099.rs:456-501`).

**Unsure:**
- The note's counts that depend on running tools (`--lib` 24 passed, 18 trade rows / 6 grouping intents, `evidence_sha256`) and the private `../lab` paths. I did not run the tests or read the lab bundle.
- Remaining gate 2 says the trade module (085) "plugs in as a dispatcher". `src/trade.rs` already exists and is wired into the shipped binary (see correction 1). Whether the gate should be reworded depends on whether the owner means the harness's library `Gateway` or the binary. I did not edit it.
- Build Ledger line 47 calls player trading "Wired, never run natively". I did not check whether the trade settlement tests in `tests/player_trade.rs` pass.
