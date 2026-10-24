<!-- fleet job=note-refresh id=Native-Mining-Dead-Board status=done turns=8 usd=0.0106 tokens(read,write,in,out)=[127893, 35875, 18, 9623] model=claude-haiku-5-5 -->
# notes/Research/Native Mining Dead Board.md

**Verdict:** minor drift in the Rust-side sections (§1, §3, §5). The diagnosis (§1–§4) is accurate for the e6e4 revision it pins. The reshuffle-suppressor bug it describes was repaired by the §6 receipt, and §7 is consistent with the tip. Several present-tense statements about "the current source" are now false.

**Corrections:**

1. `old:` On the current source this is RED: `reshuffles` stays 0.
   `new:` On the e6e4 source this was RED: `reshuffles` stayed 0. The tip is GREEN after the §6 repair (`tests/mining_dead_board.rs` has 3 tests, `:242`, `:271`, `:298`).
   `why:` repo:prototype/osfr-tools/src/mining.rs:1677-1678 and :1809-1811 call `initialize_board(..., true, ...)` on `!has_move` with no collectable suppressor. repo:prototype/osfr-tools/tests/mining_dead_board.rs:242-298.

2. `old:` `LevelReshuffle`. Rust instead suppresses that reshuffle because a collectable is parked in the
   `new:` `LevelReshuffle`. Rust did suppress that reshuffle at e6e4 (see §6; the tip no longer does, so the deadlock is closed):
   `why:` repo:prototype/osfr-tools/src/mining.rs:1656-1681 (`settle_after_collect`, the shared chain and collect tail, calls only `!has_move`); the chain caller is at :766. The `has_bottom_collectable` term no longer exists.

3. `old:` ## 3. Rust counterpart (mining.rs `e6e421d8e7cd`)
   `new:` ## 3. Rust counterpart (mining.rs `e6e421d8e7cd`; historical, tip anchors: `gravity` 1502, `collect_fall` 1554, `OnLevelEventMsg 50` 830, `settle_after_collect` 1656, `has_move` 2087)
   `why:` repo:prototype/osfr-tools/src/mining.rs:1502, :1554, :830, :1656, :2087. The e6e4 anchors (1198-1247, 1249-1311, 658-671, 1394-1441) no longer match these lines.

4. `old:` `has_bottom_collectable` (1443-1449) is true whenever any goal collectable sits anywhere in the
   `new:` `has_bottom_collectable` (1443-1449 at e6e4; deleted by the §6 repair, zero occurrences in the tip source) is true whenever any goal collectable sits anywhere in the
   `why:` a search of repo:prototype/osfr-tools/src finds no `has_bottom_collectable` definition or call. The only tip hit is a comment in repo:prototype/osfr-tools/tests/mining_dead_board.rs:5. Also see repo:notes/Reviews/Mining Drop and Reshuffle Parity Review.md:34-36.

5. `old:` 616-617 (post-chain) and 1307 (post-collect) are
   `new:` 616-617 and 1307 at e6e4 (post-chain, post-collect) were (removed by §6; tip citations are `settle_after_collect` :1677 and the powerup-action path :1809)
   `why:` repo:prototype/osfr-tools/src/mining.rs:1677, :1809; the chain caller is at :766.

6. `old:` root already verified a 3 s unpause changes nothing... (no change). The §1 citation `(mining.rs 1394-1441)` should read: `(mining.rs 1394-1441 at e6e4; `has_move` is now at mining.rs:2087)`.
   `why:` repo:prototype/osfr-tools/src/mining.rs:2087 (`fn has_move`).

**Unsure:**
- The §6/§7 test counts (mining 21/21, mining_review 13/13, mining_shape_parity 4/4) could not be verified. My grep was capped at 60 lines, and `tests/mining.rs` shows 20 `#[test]` attributes. The receipt logs are the only source for the counts.
- The §6 and §7 `bytes=` and sha256 values, the lab bundle paths, and the frame-capture figures (13857 frames, 13 `OnLevelEventMsg` frames) are outside the repo and were not checked.
- The §2 original-client anchors (`Tile.as`, `Grid.as`, `ServerGrid.as`, `GameData.as`) could not be checked: the `client_sql` `fn` lookup by name returned no rows, and the refs search for `bHasToFallOffBottom` found nothing.
- The §7 comment anchors (ServerTileGenerator.as 107-110, 126-137; ServerGrid.as 357-361) were not checked against refs. The code arm itself matches: `1 => random_tile(..., false)` at repo:prototype/osfr-tools/src/mining.rs:1345, `2` and the refill queues at :1346, :1356, :1539 keep `true`.
