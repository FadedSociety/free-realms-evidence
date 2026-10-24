<!-- fleet job=note-refresh id=Native-Loss-Boss-Display status=done turns=8 usd=0.0086 tokens(read,write,in,out)=[113969, 31244, 18, 7201] model=claude-haiku-5-5 -->
# notes/Research/Native Loss Boss Display.md

**Verdict:** minor drift. The packet facts, the `boss_display` writer and the October 8 repair description all match the tip. Two sentences still describe the pre-repair source as current or the repair as only proposed.

**Corrections:**

1. `old:` Existing Rust emits false only on a boss death, which explains the difference between killing the win boss and leaving the loss boss alive.
   `new:` Before the October 8 repair, existing Rust emitted false only on a boss death, which explained the difference between killing the win boss and leaving the loss boss alive. The loss-only false path now exists (see the October 8 section).
   `why:` repo:prototype/osfr-tools/src/encounter.rs:1976-1977 (false on boss death) and repo:prototype/osfr-tools/src/enemies.rs:630-631 (false on boss kill). The loss path is repo:prototype/osfr-tools/src/encounter.rs:2557-2566, which is the code the October 8 section describes.

2. `old:` Proposed narrow next repair: emit the existing false packet for surviving active dungeon bosses during one-shot terminal-loss presentation, before results presentation.
   `new:` Implemented narrow repair (see the October 8 section below): the existing false packet is emitted for surviving active dungeon bosses during one-shot terminal-loss presentation, before results presentation.
   `why:` repo:prototype/osfr-tools/src/encounter.rs:2550-2567 (`present_results`: `results_presented` guard, then `boss_display(actor.guid, false)` for `actor.boss && state.health > 0` when the phase is Lost, before `end_scores`). The regression is repo:prototype/osfr-tools/tests/encounter.rs:135-215.

**Checked and holding (no change):**
- `boss_display` writer exists: repo:prototype/osfr-tools/src/encounter.rs:3009-3014 (header 32/9, GUID u64, one bool byte).
- The false packet layout in the note and the test's 13-byte expectation match: repo:prototype/osfr-tools/tests/encounter.rs:174-177.
- Retry or restore re-registers bosses with true: repo:prototype/osfr-tools/src/encounter.rs:1520-1527 (inside `on_zone_ready`, starting at line 1467). The test expects `[display(202, true), display(202, false)]` on restored ready (tests/encounter.rs:207).
- "Ten-line addition": the added block is encounter.rs:2558-2567, which is ten lines.
- "Win behavior remains identical": the new branch only runs for `EncounterPhase::Lost`.

**Unsure:**
- Test counts ("all15 ordinary checks", "17 total") are not verified here. Notes/MODLOG.md:297-301, notes/Reviews/Loss Boss Display Independent Review.md and notes/Tasks.md:95 agree with each other, but I did not run the tests.
- Native claims (the 00a2a030, 00a2a8a0, 00a2b910 and 009852a0/00985200 addresses, the GUID decimal-to-hex vector, the Lua `Target:onDS` behaviour, the proof hashes and the win/loss timestamps) were not checked. The client-side notes I checked (notes/Native Map/Shards/S0292, S0263) agree with the addresses.
- Acceptance is still pending, consistent with notes/Tasks.md:95. I did not change that line.
