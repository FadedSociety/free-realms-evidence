<!-- fleet job=test-audit id=tests-common-smelting-movie-rs-L1 status=nothing_found turns=7 usd=0.0035 tokens(read,write,in,out)=[40668, 12317, 16, 3075] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/common/smelting_movie.rs lines 1-82 of 82

Reviewed `prototype/osfr-tools/tests/common/smelting_movie.rs` lines 1-82. No findings.

The window contains only helper functions (`wrap`, `send`, `instance`, `payload_packet`, `start`, `rounds`, `play`), with no `#[test]` functions, no `#[ignore]`, and no early returns on missing fixtures. Checked against the code under test in `src/smelting.rs`:

- `payload_packet` overwrites bytes 11..15 (the game field) with -1. That matches the server's `native_payload` path (`sub == 14 && game == -1`, smelting.rs:393), so the helper builds packets the server accepts for the intended reason. The instance id is left intact.
- `start` asserts exactly 2 replies (header plus `launch_packet`). That matches the Offered→Playing launch branch (smelting.rs:401-413), so it is a real check, not an incidental count.
- `rounds` discards its outcomes with no assertion. This is not a hole: if a StatUpdate were rejected (smelting.rs:446-483), the following GameWon would fail the "before four rounds" check (smelting.rs:500-504). `play` would then fail on its `completed + 1` assertion.
- `play` compares `completed` against a value snapshotted before the run (`previous + 1`), not against the code's own output. It then asserts `active.is_none()` after the close packet. Both are meaningful. `completed` is incremented only on a real win (smelting.rs:505-510).

Nothing here can pass on a regression that a meaningful test would catch.
