<!-- fleet job=note-refresh id=Pieces-078-Zone-transitions status=done turns=11 usd=0.0120 tokens(read,write,in,out)=[206070, 40378, 24, 9833] model=claude-haiku-5-5 -->
# notes/Research/Pieces/078 Zone transitions.md

**Verdict:** minor drift. The core status holds: `restoration/piece_078.rs` exists with the policy (phases, `begin`/`on_client_ready`/`on_initial_data_sent`/`on_finished_loading`, `report_position`, `persisted_location`, `accepts_zone_action`), `tests/piece_078.rs` has 7 `#[test]`s, `tests/pieces/test_piece_078.py` has 6 test methods, `scripts/pieces/piece_078.py` exists, the module is still not registered in `lib.rs` (it is pulled in by `#[path]`), and the gateway still returns `invalid("position before world initialization")` for non-opening gameplay. Two statements are stale.

**Corrections:**

1. `old:` `` `src/gateway.rs:619` ``
   `new:` `` `src/gateway.rs:1501-1502` ``
   `why:` repo:prototype/osfr-tools/src/gateway.rs:1501-1502 holds the quoted comment "Movement from the prior scene can already be queued when a begin-zoning reply is emitted." Line 619 no longer has it. The quote is unchanged; only the citation moved. The same comment is also cited in `tests/piece_078.rs:32` and `src/restoration/piece_078.rs:35` without a line number, so those need no change.

2. `old:` `` `piece_044`, `piece_068`, `piece_074` reference module files that do not exist yet `` 
   `new:` `` `piece_044`, `piece_068`, `piece_074` include their modules by `#[path]` from `src/restoration/piece_044.rs`, `piece_068.rs` and `piece_074.rs`; those files now exist (compile state at tip not re-run) ``
   `why:` repo:prototype/osfr-tools/tests/piece_044.rs:46-48, tests/piece_068.rs:25-27 and tests/piece_074.rs:38-40 point at `../src/restoration/piece_0NN.rs`, and the directory listing of `prototype/osfr-tools/src/restoration` shows all three files. The stated cause of the compile failure therefore no longer holds. I did not confirm whether the full suite now compiles, so the "currently fails" wording needs a fresh run before it is changed further.

**Unsure:**

- The Sanctuary citations are community reference, not our code, so I checked only the easy ones. Confirmed: `Player.cs:365` (`TeleportToZone`), `Player.cs:372` (`StartingZonePosition = Position`), `Player.cs:1075` (`OnZoneChanged`), `ZoneManager.cs:116` (`TryMovePlayerToZone`), `ZoneManager.cs:208` (`EvictIfEmpty`), `BaseZone.cs:137` (`OnClientIsReady`), and `PacketClientFinishedLoadingHandler.cs:26` in the Legacy and Lxzxrus copies. The `GatewayConnection.cs:510-521` range is loose: `SavePlayerToDatabase` starts at `:495` in pinned Sanctuary, and the `StartingZonePosition` assignment is at `:519`. I did not check the `:240-248` world-entry restore claim.
- Capture-derived frame numbers and bit-exact coordinates, the sha256 digests, the test counts in the focused-suite log, and the `lab/reports/...` and `logs/...` paths: these need the private lab bundle, which I could not read from here. The frame offsets are consistent with the cross-reference in `tests/piece_022.rs:42` (frame 27311, inner opcode 31).
- The native developer-teleport numbers (`-1999.9139, -42.6550, 445.8578` then `-2111.0854, -56.19644, 212.10196`) match `notes/Reviews/Native Developer Teleport 005748.md:23`.
- The Rust test file states that `#[path]` is used "until the lead registers" the module; `lib.rs` has no `restoration` module registration, so that claim holds.
