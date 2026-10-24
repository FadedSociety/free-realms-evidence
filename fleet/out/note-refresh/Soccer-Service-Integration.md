<!-- fleet job=note-refresh id=Soccer-Service-Integration status=done turns=15 usd=0.0179 tokens(read,write,in,out)=[379565, 46182, 32, 16672] model=claude-haiku-5-5 -->
# notes/Research/Soccer Service Integration.md

**Verdict:** badly stale. The module has since been registered in `lib.rs`, extended with a minigame lifecycle and reward settlement, and wired into the gateway through `soccer_entry`. The test file no longer has the env-gated capture test the note describes, and `CAPTURED_BALL_SPAWN` does not exist. The core API names (`join`, `leave`, `start`, `second_half`, `tick`, `handle_client`, `snapshot`, `restore`, `entry_frame`, `emit_packet`, `Authority::unregister`) all still exist.

**Corrections:**

1. `old:` No native playability, world entry, gateway wiring or live client run; the module is unregistered and the test includes it by path. The lead owns `lib.rs` registration and native acceptance.
   `new:` No native playability, world entry or live client run is claimed. The module is registered at `lib.rs:84` (`pub mod soccer_service;`), its test imports it as `osfr_tools::soccer_service`, and the gateway reaches it through `soccer_entry` (`gameplay.rs:192`, `gameplay.rs:3300`). Native acceptance remains open.
   `why:` `repo:prototype/osfr-tools/src/lib.rs:84`; `repo:prototype/osfr-tools/tests/soccer_service.rs:14`; `repo:prototype/osfr-tools/src/gameplay.rs:192,3300`; `repo:prototype/osfr-tools/src/soccer_entry.rs:26`.

2. `old:` No native playability, no gateway registration, no packet sent.
   `new:` No native playability claim; registered in `lib.rs:84` and reached from the gateway through `soccer_entry` (`gameplay.rs:192`). No packet sent.
   `why:` same as correction 1. I did not verify the "no packet sent" part; see Unsure.

3. `old:` `soccer_match::CAPTURED_BALL_SPAWN`; `half_seconds` defaults to the captured
   `new:` the caller's spawn (`MatchConfig::new` defaults to the R origin `[0.0, 0.0, 0.0]`); `half_seconds` defaults to the captured
   `why:` no `CAPTURED_BALL_SPAWN` symbol exists anywhere under `repo:prototype/`. `repo:prototype/osfr-tools/src/soccer_match.rs:141` (`kickoff_spawn` is a plain field) and `:155` (default origin).

4. `old:` The env-gated test decodes the preserved
   file, re-encodes it byte-exact and compares it to `entry_frame()`.
   `new:` No env-gated capture test exists. `reconstructed_entry_frame_round_trips_its_candidate_values` encodes `entry_frame()` from the R candidate values and round-trips it; no test reads a preserved capture file.
   `why:` `repo:prototype/osfr-tools/tests/soccer_service.rs:262-263`; the file contains no `env::var` and no `OSFR_SOCCER_ENTRY_CAPTURE`.

5. `old:` | 13 passed, 0 failed, 1 ignored | `green.log` |
   `new:` | 16 passed, 0 failed, 0 ignored (16 `#[test]` functions, none `#[ignore]`) | `green.log` |
   `why:` `repo:prototype/osfr-tools/tests/soccer_service.rs` has 16 `#[test]` lines (261 to 965) and no `#[ignore]`. `repo:notes/Autopilot/T259.md:136` and `F226.md:194` also record 16 passed.

6. `old:` 1 passed: captured frame decodes, re-encodes byte-exact, equals `entry_frame()`
   `new:` no such test at the tip: `tests/soccer_service.rs` has no `#[ignore]` and no `OSFR_SOCCER_ENTRY_CAPTURE` read; this log row is historical only.
   `why:` `repo:prototype/osfr-tools/tests/soccer_service.rs` (whole file); `repo:prototype/` grep for `OSFR_SOCCER_ENTRY_CAPTURE` returns nothing.

7. `old:` No economic value exists anywhere in this slice; rewards remain `Missing`.
   `new:` The terminal result is settled through the shared minigame lifecycle: `finish_minigame` applies the R win grant to the caller's live reward state for the winning team. `Outcome.reward` alone remains `Evidence::Missing`.
   `why:` `repo:prototype/osfr-tools/src/soccer_service.rs:755-772` (`finish_minigame` with `RewardGrant` settlement); `repo:prototype/osfr-tools/src/soccer_entry.rs:17-18`; `repo:prototype/osfr-tools/src/soccer_match.rs:397,973` (`reward: Evidence::Missing` still holds).

**Unsure:**
- The "Verified artifacts" sha256 pins (`5e156eaa…`, `92a88677…`, `eb73cc17…`) and the frozen-adapter "14 tests" line could not be checked with the read-only tools.
- "No packet sent": I did not trace whether `soccer_entry` or gameplay sends the `emit_packet` output to a client, so I left this unchanged apart from the gateway wording.
- The "existing soccer suite" counts (11+1 ignored / 27 / 8 / 10) were not re-run. `soccer.rs:530` does carry one `#[ignore]`, which is consistent with the note.
- Another note, `repo:notes/Research/Soccer Match Authority.md:18`, also cites `CAPTURED_BALL_SPAWN` as an offered constant. That note is outside this check and should be reviewed by its owner.
- The `emit_packet` gate and the refusal of result families (`soccer_service.rs:414-431`) still match the note.
