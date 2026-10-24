<!-- fleet job=note-refresh id=Pieces-016-Minigame-loss-and-retry status=done turns=9 usd=0.0103 tokens(read,write,in,out)=[147327, 36504, 20, 8481] model=claude-haiku-5-5 -->
# notes/Research/Pieces/016 Minigame loss and retry.md

**Verdict:** minor drift. The files, the 15 Rust tests, the 9 Python tests, the module being unregistered in `lib.rs`, the frame layouts, the native bindings and the reward rules all check out at the tip. Two claims are wrong: the start rule overstates what the ledger allows, and one count in the captured-traffic table is off.

**Corrections:**

1. `old:` a second start before the current
   instance settles is rejected.
   `new:` a start is rejected whenever an instance already exists on the stream, settled or not; after a settle only `retry` begins the next instance.
   `why:` `prototype/osfr-tools/src/restoration/piece_016.rs:321-326`: `start()` returns `AlreadyPlaying` whenever `self.current.is_some()`, and `current` stays `Some` after a settle. `prototype/osfr-tools/tests/piece_016.rs:230-234` asserts that a start is still rejected after a loss has settled. The note's "before the current instance settles" implies a post-settle start is allowed, which the code does not do.

2. `old:` `39/23` `MiniGameKnockOutPacket` | 7 | server to client | soccer 3797/3799, racing 15449/15450, derby 5078/5079
   `new:` `39/23` `MiniGameKnockOutPacket` | 6 | server to client | soccer 3797/3799, racing 15449/15450, derby 5078/5079
   `why:` the three frame pairs listed in that cell are 6 frames (2+2+2). `prototype/osfr-tools/tests/piece_016.rs:8` says "six knockouts share `a6aa7993…`". The total of 7 `39/23` frames is still correct, because the next row (derby 29641) makes up the seventh.

**Unsure:**

- The RED/GREEN test counts (`red-tests.log` 3 passed / 12 failed, `green-tests.log` 15 passed) and the `../lab/reports/piece-016-20261009T0306Z/` evidence sit outside the repo, so I could not check them. The "15 passed" total does match the 15 `#[test]` functions in `tests/piece_016.rs`.
- The sha256 values for the community C# files and `pseudocode.c` could not be re-hashed from the tip. The `39/23` frame hashes match the test file.
- Native bindings were checked in the client decompile: `FUN_008a4420` writes `0x27` (39) at `param_1[1]`; `FUN_009ad480` logs "MiniGame:OnGameOver" and stores the Won byte at `+99` and the three ints at `+0x70/+0x74/+0x78`; `FUN_009bcb60` logs "MiniGame:RequestRestartGame" and sends sub 0xb; `FUN_009be7d0` logs "MiniGame:RequestStartGame" and calls `FUN_009bdc60(5,-1,-1)`; `FUN_009bf190` logs "MiniGame:LeaveMiniGame"; `FUN_009b7170` logs "MiniGame:ShowMiniGameEndDialog". All match the note's table. I did not check the `StateId` lookup detail inside `FUN_009bdc60` beyond its `-1` handling.
- The note says `39/17` "echoes the ids of the `39/5` start request". The ledger instead mints a new `StateId` and writes it into `39/17`, so this is worth a second look, but I did not settle whether the native client echoes or mints.
