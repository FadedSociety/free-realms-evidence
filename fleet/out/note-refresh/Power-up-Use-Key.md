<!-- fleet job=note-refresh id=Power-up-Use-Key status=done turns=11 usd=0.0153 tokens(read,write,in,out)=[271484, 57797, 24, 10647] model=claude-haiku-5-5 -->
# notes/Research/Power-up Use Key.md

**Verdict:** minor drift. The client-side findings (key table, `ActionBarSlot3` -> slot 2 -> 36/10, `UsePowerup` not a combat key, `E` taken by StrafeRight/Juke, GameDock and Key Binds Lua) hold against the tip. Every repo claim I checked is still true, with one exception: the note describes T222 as future work, but T222 has landed on the tip, so the "wires it" and "Decision" sentences are stale.

**Corrections:**

1. `old:` so T222 wires it server-side:
   `new:` so T222 has wired it server-side (`src/gameplay/power_up_use.rs`, `src/encounter/power_up_use.rs`, `tests/power_up_use.rs`; the report is `notes/Autopilot/T222.md`):
   `why:` `prototype/osfr-tools/src/gameplay/power_up_use.rs:50-110` (`use_power_up_request` takes the bar 1 slot 2 request and restores the bar), `prototype/osfr-tools/src/gameplay.rs:4642-4646` (the 36/10 branch calls it before the job-ability fall-through), `prototype/osfr-tools/src/opening_abilities.rs:326-374` (`activation_with_power_up` replaces only slot 2 and leaves the job row unmoved), `notes/Autopilot/T222.md:9`.

2. `old:` **Decision for T222.**
   `new:` **Decision for T222 (built).**
   `why:` `notes/Autopilot/T222.md:1-9` records the build. `prototype/osfr-tools/src/gameplay/power_up_use.rs:1-7` names the request as this seam.

3. `old:` and wire the server use. The client is not patched.
   `new:` and wired the server use (`src/gameplay/power_up_use.rs:50`, `use_power_up_request`; `src/encounter/power_up_use.rs`). The client is not patched.
   `why:` `prototype/osfr-tools/src/gameplay/power_up_use.rs:50`; `notes/Autopilot/T222.md:14`.

**Checked and still true (no change needed):**
- `abilities::unsupported_cast` refuses non-mode-0 casts, bars other than 1, and slots outside 0..=7. It accepts only the 24/32 byte shapes. `prototype/osfr-tools/src/abilities.rs:821-837`. The "refused by the server today" line in §2 is accurate.
- The 36/5 toolbar carries eight entries (slot 0 basic, 1..7 job bar). `prototype/osfr-tools/src/opening_abilities.rs:335-337, 262-265`.
- `power_ups::SLOT` = 2. `prototype/osfr-tools/src/power_ups.rs:104`.
- `src/opening_abilities.rs`, `src/abilities.rs`, `src/restoration/piece_035.rs` and `piece_046.rs` all exist at the cited paths.
- Lua citations: `GameDock` at `ui:ScriptsBase.lua:30028/30481`, Key Binds at `ScriptsBase.lua:32871-32913`, FtesPowerUp/PowerUpIcons at `ScriptsBase.lua:40968/41102`, `FirstTimeEvent.PowerUpFTE` at `41390`.
- Client resource: `Resources/ControllerElements.txt:19` is the `a3` ActionBarSlot3 row, and `:79` is the commented `#dd1 ... UsePowerup` row.
- `notes/Native Map/Default Key Bindings.md` rows 6, 11, 15, 21 show StrafeRight 'E', Juke 'E', UsePowerup Control_L and ActionBarSlot3 '3'.

**Unsure:**
- The locale hashes and the W153 extracts (`lab/reports/combat-powerups-w153/...`, the Hewey frames) sit under `lab/`, which is not in my roots. I could not verify them.
- The IDA addresses (`00b02880`, `00a35150`, `008a7eb0`, `0094c760`, `00cd7010`) and the binding-table bytes are client-side and outside my tools. I did not verify them. The T222 report (F263) says the dispatcher's case 21 -> slot 2 was re-confirmed.
- The claim that the 38/25 handler edits only the item and minigame bars is client-side. I did not verify it.
