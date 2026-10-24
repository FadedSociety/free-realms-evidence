<!-- fleet job=note-refresh id=Derby-Restoration status=done turns=11 usd=0.0185 tokens(read,write,in,out)=[264136, 53608, 24, 18259] model=claude-haiku-5-5 -->
# notes/Research/Derby Restoration.md

**Verdict:** badly stale. The capture facts (frame counts, subtype payload lengths, participant keys) are outside the repo and I did not re-derive them. The code half of the note describes an API that the tip no longer has. The derby module was replaced by the `Derby Service` work (`notes/Research/Derby Service.md` says the earlier note is "quarantined"), and this note was not updated.

**Corrections:**

1. `old:` `` `src/derby.rs` adds a bounded bout state machine because no original server-side derby exists to ``
   `new:` `` `src/derby.rs` now holds a full server-side match service, `DerbyService` (derby.rs:783), in place of the thin contract described here (see [[Research/Derby Service]]). It is written because no original server-side derby exists to ``
   `why:` repo:prototype/osfr-tools/src/derby.rs:783 (`pub struct DerbyService`), derby.rs:1-12 (module doc: rules, NPC fill, combat, timers, results are all in `DerbyRules`/`DerbyService`); `grep DerbySession|observe_hit|claim_reward|AlreadyClaimed` over `src/` returns nothing.

2. `old:` `` `DerbySession`: `Lobby -> Running -> Finished | Abandoned`, at most eight participants, unique ``
   `new:` `` `DerbyService` (derby.rs:783): `Lobby -> Starting -> WaitingForState -> Countdown -> Running -> Results -> CloseEnabled -> Closed`, or `Aborted` (derby.rs:739-748), at most eight participants (derby.rs:23), unique ``
   `why:` repo:prototype/osfr-tools/src/derby.rs:739-749 (`enum DerbyPhase`), :23 (`MAX_DERBY_DRIVERS: usize = 8`), :783.

3. `old:` `` `observe_hit` records a `VehicleHit` only while running and only for a joined victim; the per ``
   `new:` `` Hits arrive as `VehicleHit` reports through `DerbyService::handle_client` (derby.rs:1086; decoded at derby.rs:602) and apply only while running; the per ``
   `why:` repo:prototype/osfr-tools/src/derby.rs:1086 (`pub fn handle_client`), :602-606 (subtype 16 → `VehicleHitReport`); no `observe_hit` exists.

4. `old:` `` `finish(results)` validates the original result-table shape (1-based places in order, unique ``
   `new:` `` `finish_match(now_ms)` (derby.rs:1602) orders the connected drivers by score, then damage margin, and enters `Results` (derby.rs:1606-1627); there is no `finish(results)` at the tip (unique ``
   `why:` repo:prototype/osfr-tools/src/derby.rs:1602-1630; the only `fn finish` in derby.rs is a private decoder helper at :1924.

5. `old:` `` The module never moves currency or items; `claim_reward` is the ``
   `new:` `` The module never moves currency or items, and the tip has no `claim_reward` gate: `handle_close` (derby.rs:1766) retires the match once and F164 withholds derby payouts (derby.rs:1764-1765). Delete the remainder of the sentence (line 142-143, "once-only gate … `AlreadyClaimed` … on a second call.") ``
   `why:` repo:prototype/osfr-tools/src/derby.rs:1764-1765 (F164 comment), :1766-1775; no `claim_reward`/`AlreadyClaimed` in `src/`.

6. `old:` `` | `prototype/osfr-tools/tests/derby.rs` | 11 tests; includes the module with `#[path]` until the lead registers it | ``
   `new:` `` | `prototype/osfr-tools/tests/derby.rs` | 7 tests; uses `osfr_tools::derby` directly (module registered in `src/lib.rs`) | ``
   `why:` repo:prototype/osfr-tools/tests/derby.rs:185, 309, 350, 388, 450, 521, 558 (seven `#[test]`s), :1 (`use osfr_tools::derby::{…}`); repo:prototype/osfr-tools/src/lib.rs:16 (`pub mod derby;`).

7. `old:` `` Lead integration step: add `pub mod derby;` to `src/lib.rs` and drop the `#[path]` include from ``
   `new:` `` Lead integration step (done): `pub mod derby;` is in `src/lib.rs`, and `tests/derby.rs` imports the crate module directly. ``
   `why:` repo:prototype/osfr-tools/src/lib.rs:16; tests/derby.rs:1.

8. `old:` `` Subtypes 8, 9 and 17 appear in the enum but never in the capture; they have no recovered length and `` (line 68-69, next line is `stay opaque.`)
   `new:` `` Subtypes 8, 9 and 17 appear in the enum but never in the capture; the tip decodes them (8/9 as a participant key, 17 as a u32; derby.rs:549-550, 607), though their lengths are not recovered and ``
   `why:` repo:prototype/osfr-tools/src/derby.rs:549 (`8 => DestroyVehicle(reader.key()?)`), :550 (`9 => KickVehicle`), :607 (`17 => ItemExpired(reader.u32()?)`).

9. `old:` `` stay opaque. `` (line 69, the end of the sentence in correction 8)
   `new:` `` are typed at the tip (derby.rs:549-550, 607), not byte-opaque. ``
   `why:` same as correction 8.

10. `old:` `` neither has a proven field layout, so both stay byte-preserved ``
    `new:` `` neither has a proven field layout, so the tip keeps their unproven fields as raw words (derby.rs:532-540, 576-585) ``
    `why:` repo:prototype/osfr-tools/src/derby.rs:532-540 (subtype 5 → `VehiclePose` with `*_bits` words and `flags`), :576-585 (subtype 11 → `VehicleState`); the module doc at :11 says unknown reader fields "remain raw words/bytes".

11. `old:` `` and opaque. No health, elimination threshold or score value is claimed from the wire. ``
    `new:` `` No health, elimination threshold or score value is claimed from the wire; the tip names subtype 11 fields `health`/`score` (unverified against the capture; derby.rs:578-579). ``
    `why:` repo:prototype/osfr-tools/src/derby.rs:578-579, :759-770 (`DerbyDriverState` health/score/damage fields).

12. `old:` `` 4. Reward granting and racer/derby progression (queue item 041): the module only refuses a second `` (line 167)
    `new:` `` 4. Reward granting and racer/derby progression (queue item 041): the tip has no reward gate (no `claim_reward`; `handle_close` retires the match once, derby.rs:1764-1765), so a second `` (the rest of the sentence, "claim; it does not pay anything.", stays)
    `why:` repo:prototype/osfr-tools/src/derby.rs:1764-1765, 1766-1775; `notes/Autopilot/F164.md` and `F206.md` (derby payouts withdrawn).

Not corrected, for the next editor: the verification-table row `GREEN, --test derby | 11 of 11 pass` is a historical log result, but `tests/derby.rs` now has seven tests, so the row no longer describes the current file.

**Unsure:**

- **Subtype 10 layout.** The note's capture layout (`u32 marker = 1`, `u8 len_with_nul`, `u8 len`, two zero bytes, flag, NUL-terminated asset) differs from the tip's reader (`u64` key, `i32` name length, name bytes, then a 69-byte tail; derby.rs:551-574). The tip may fail to parse the eight capture frames. I did not run the tests, so I cannot tell.
- **Hit tally.** The note says the per-victim tally "sums the recovered impact magnitudes … not a health model." The tip keeps `health`, `score`, `damage_dealt` and `damage_received` and applies server-side combat (derby.rs:759-770, 1602-1620). Whether the tip's `damage` logic matches the note's "not a health model" claim needs a closer read of the combat code.
- **`start` requires a non-empty lobby** and **`abandon` makes later finish/reward impossible.** I did not find the note's functions. `DerbyPhase::Aborted` is set at derby.rs:1076, 1640 and 1745, which is probably the closest equivalent, but I did not confirm it.
- **Capture facts** (frame counts, payload lengths, the 8 participant keys, the 92 hits / 27 mirrored pairs) and the Python checker counts (12 checks, 40,214 bodies) depend on `../lab/` paths outside the repo. `scripts/pieces/piece_007.py` and `tests/pieces/test_piece_007.py` exist. I did not run either.
- **Lobby ids 6678/6705/3052/3053** and the locale ids cited in the "Original facts (client and data side)" section are in `../lab/`, outside this repo. Not checked. The repo does use 3053 as `DEMO_DERBY_LOBBY_NAME_ID` (derby.rs:21).
