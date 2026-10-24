<!-- fleet job=note-refresh id=Pieces-060-Dungeon-instance-lifecycle status=done turns=14 usd=0.0229 tokens(read,write,in,out)=[493235, 69959, 30, 18376] model=claude-haiku-5-5 -->
# notes/Research/Pieces/060 Dungeon instance lifecycle.md

**Verdict:** minor drift. The note is current on the code: the module, the 16 Rust tests, the 14 checker tests, the policy rules, the Registry behaviour and the op41/op39 layouts all match the tip. One count is wrong.

**Corrections:**

- `old:` No roster-removal, invite, kick or leader packet is written; only the four bodies with recovered byte layouts are emitted.
  `new:` No roster-removal, invite, kick or leader packet is written; only the five bodies with recovered byte layouts are emitted (`41/2`, `41/106`, `41/107`, `39/18`, `39/19`).
  `why:` `repo:prototype/osfr-tools/src/restoration/piece_060.rs:119,127,134,149,159` define five encoders (`encode_player_enter`, `encode_encounter_state`, `encode_zone_ready`, `encode_game_over`, `encode_state_remove`). They are emitted from `enter` (L362), `zone_ready` (L392), `start` (L412-415), `reset` (L475), `complete` (L515-518) and `exit`/`reap` (L536, L604). The module's own header at `piece_060.rs:59` also says "four", so that comment needs the same fix when the module is next touched.

**Checked and current:**

- Module, tests and checker: `piece_060.rs` exists and is not registered in `src/restoration` (no `piece_06x` mod line in the tree), which matches "`#[path]`-included by the test until the lead registers it". `tests/piece_060.rs` has 16 `#[test]` functions. `tests/pieces/test_piece_060.py` has 14 `def test_` functions. `scripts/pieces/piece_060.py` exists and takes `--reports-dir`.
- Three frame hashes match the test and module vectors (`ecf5eda4…e7bf`, `625e25ea…4b91`, `95c4e623…c3c3`).
- The 41 header and the 106/107/2 layouts match the note (`piece_060.rs:108-136`). Settlement `39/18` = `u8 Won` + `0,0,1` and `39/19` = bare header match `piece_060.rs:149-160`.
- Policy: entry is gated by the difficulty table and capacity, and the roster closes at GO (`enter`, L341-367). Duplicate entry is rejected. One live instance per player is enforced in `Registry::enter` (L688-702). Reset retires actor ids and resumes at state 6 (L470-480). Completion is once-only and emits `39/18` + `39/19` with ids and roster only (L484-520). The last member's exit or reap closes the instance and sends `39/19` unless completion already sent it (L524-542, L583-610). A reconnect before the deadline restores the member without touching the spawn (L566-580). `Registry::exit` frees the player (L704-708).
- Handler names exist in the client: `MiniGame:OnGameOver` (FUN_009ad480), `SetMiniGameReady` (FUN_009b0cc0), `RequestRestartGame` (FUN_009bcb60), `LeaveMiniGame` (FUN_009bd240, FUN_009bf190), `RequestStartGame` (FUN_009be7d0).
- Community sub-opcodes (2, 106, 114, 107, 133) are present in the pinned Sanctuary trees under `refs`.
- Piece 016 records the `39/23` (seven frames), `39/7` (two frames) and "nine frames" counts, and the `39/18`/`39/19` capture gap, as the note says.

**Unsure:**

- The client line numbers in the note (1195728, 1206499, 1205447, 1206939, 1205032, 1192885) could not be checked. The handler names resolve, but `pseudocode.c` line numbers are not reachable through these tools.
- `lab/reports/...` counts (59 frames, 11 family/sub pairs), `evidence.json`, `findings.json` and the wiki revisions (49285, 49119, 45235, 48170) sit outside the readable roots, so I did not verify them.
- Gaps wording: "No wipe/defeat condition ... is modelled" (note line 92). The code does model actor defeat as a completion gate (`defeat` L455-466, `complete` L506-508), though it has no player-wipe rule, and `reset` is caller-driven. The gap is probably meant as "wipe" only. If the wording is kept, a reader could take it as "no defeat state at all". I did not change it.</result>
</invoke>
