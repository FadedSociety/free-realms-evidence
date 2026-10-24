<!-- fleet job=note-refresh id=Combat-Power-ups status=done turns=17 usd=0.0268 tokens(read,write,in,out)=[608995, 76791, 36, 22134] model=claude-haiku-5-5 -->
# notes/Research/Combat Power-ups.md

**Verdict:** badly stale on status. The Part 1 client facts I checked still hold (the 36/10 slot-2 path, the 24-byte request shape, the `UsePowerup` binding). Part 2 and the Summary still describe the feature as unbuilt and undecided, but `power_ups.rs`, `power_ups.json`, the encounter pickup/use code and the tests all exist at the tip (`b3dcbc9`, `f261`, `T222`, `F263`).

**Corrections:**

1. `old:` - Two things need a decision from Bryce before building (section "Open questions"): the key-3 slot collides with existing job-ability content, and the Flame Wave description differs between eras.
   `new:` - The power-up is built and wired (`power_ups.rs`, `encounter/power_up_use.rs`, `gameplay/power_up_use.rs`, `tests/power_up_drops.rs`, `tests/power_up_use.rs`). The key-3 slot collision is handled in code: while a kind is held, it overlays job-bar index 2 and the authored row returns after use. The Flame Wave description still differs between eras (see Open questions).
   `why:` repo:prototype/osfr-tools/src/opening_abilities.rs:321-325 and :356-358; repo:prototype/osfr-tools/src/gameplay/power_up_use.rs:21-28; repo:notes/Research/Power-up Use Key.md:72

2. `old:` Recommendation: (a) after one native check of the dock at job level 5 or higher.
   `new:` Decided in code: the held kind overlays index 2 while held and the authored row is not moved (option (b) in effect). Still needs one native check of the dock.
   `why:` repo:prototype/osfr-tools/src/opening_abilities.rs:321-325 ("The authored job row below it is not moved"); repo:notes/Design/Build Ledger.md:65 still says "Key-3 use still waits on Bryce's slot decision" (see Unsure).

3. `old:` **Shared-file patches (not applied; the owner of those files should take them).**
   `new:` **Shared-file patches (status: (a) and (c) applied; (b) not applied).**
   `why:` (a) repo:prototype/osfr-tools/src/encounter/field_rewards.rs:227-263 calls `drop_power_ups`, defined at repo:prototype/osfr-tools/src/encounter.rs:2126. (c) repo:prototype/osfr-tools/src/gameplay.rs:491-496 routes slot 2 to the held kind before the job-ability lookup. (b) repo:prototype/osfr-tools/src/abilities.rs:159 still reads `(0.1..=3.0).contains(&damage_taken_multiplier)`, so `JobEffect::valid` was not extended.

4. `old:` `encounter.rs` kill branch (`if hp == 0`, about line 3243) and tick
   `new:` `encounter/field_rewards.rs` `credit_field_kill` (about line 227), `encounter.rs` `drop_power_ups` (line 2126) and `tick_power_ups` (line 2193)
   `why:` repo:prototype/osfr-tools/src/encounter.rs is 3158 lines long, so line 3243 does not exist. The kill path is at repo:prototype/osfr-tools/src/encounter/field_rewards.rs:227 and encounter.rs:2126/2193.

5. `old:` `AreaDamage` + `Stun` (`skill_stuns`, animation 1401 `com_stunned`)
   `new:` `AreaDamage` + `Stun` (`apply_stun` in `encounter/skills.rs` line 405; animation 1401 `com_stunned` at `encounter/skills.rs` line 422)
   `why:` no `skill_stuns` symbol exists in the tree; repo:prototype/osfr-tools/src/encounter/skills.rs:405 and :422.

6. `old:` so the 55 definitions in `enemies.json` and the field enemies need only one optional field.
   `new:` so the 20 enemy definitions in `enemies.json` (20 `reward` blocks) and the field enemies need only one optional field. `field_enemies.json` and `field_battles.json` already carry `power_up_table`; `enemies.json` has none.
   `why:` repo:prototype/osfr-tools/data/content/enemies.json (20 `"reward": {` matches, no `power_up_table`); repo:prototype/osfr-tools/data/content/field_enemies.json:393 and field_battles.json:581.

7. `old:` clears the slot (36/13 + 36/5 with an empty slot 2) and sets no cooldown, no energy cost.
   `new:` consumes the held kind before any effect runs, then resends 36/13 + 36/5 with the authored job row back in slot 2 (no empty slot). No cooldown, no energy cost.
   `why:` repo:prototype/osfr-tools/src/encounter/power_up_use.rs:82-83 (consume first); repo:prototype/osfr-tools/src/gameplay/power_up_use.rs:33-44 (`refresh_power_up_slot` resends the toolbar); repo:prototype/osfr-tools/src/opening_abilities.rs:323-325 ("the same row comes back on the next activation once the kind is used").

8. `old:` `JobEffect::Buff` cannot do it: `damage_taken_multiplier` is bounded to 0.1 to 3.0 in `JobEffect::valid`, so invulnerability needs either a new `invulnerable` flag or a `0.0` allowance; the client side is status bit 8 via `35/20` and a speed effect tag
   `new:` `JobEffect::Buff` still cannot do it (`damage_taken_multiplier` is bounded to 0.1 to 3.0 in `JobEffect::valid`). The built code bypasses `JobEffect` and applies a `SkillBuff` with `taken: 0.0` directly, with a status-bit-8 effect tag built from the slot record.
   `why:` repo:prototype/osfr-tools/src/abilities.rs:159; repo:prototype/osfr-tools/src/encounter/power_up_use.rs:124-146.

9. `old:` as a failure message; native check needed
   `new:` as feedback text (`out.feedback`), not a failure reply; native check needed
   `why:` repo:prototype/osfr-tools/src/encounter.rs:2224-2227 (`out.feedback = Some(ONE_POWER_UP_TEXT)`), with the constant at encounter.rs:111.

**Unsure:**
- **Build Ledger vs code on key 3.** `notes/Design/Build Ledger.md:65` says "Key-3 use still waits on Bryce's slot decision", but the overlay is in code (see 1 and 2). I could not tell whether Bryce signed off on it. Left as-is for the owner.
- **`realm powerup <kind>` and `realm powerup roll <table> <n>`** (Part 2.3, "Tuning live") are not found in `src/` or `studio/`. `realm reload power_ups` does exist (`gameplay/content_reload.rs:95`). I did not change the text because 2.3 is a proposal, but it reads as present tense.
- **Open question 3 (mid-fight `36/5`)** is still unverified. Nothing in the tree settles it, and it needs a native run.
- **Super Shield asset gap** (missing `.dme`/`.dds`): not checked, since it is not a code claim.
- **Client-side claims in Part 1.1** (binding table rows, `00b02880` case 21, `36/10` writer) were not re-read in the client. The repo's `notes/Research/Power-up Use Key.md` and `encounter/power_up_use.rs:3-13` agree with them.
