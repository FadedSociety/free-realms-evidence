<!-- fleet job=note-refresh id=AddPc-Layout status=done turns=30 usd=0.0390 tokens(read,write,in,out)=[1397850, 88977, 62, 27840] model=claude-haiku-5-5 -->
# notes/Research/AddPc Layout.md

**Verdict:** badly stale. The note describes the tip as it was on 2026-10-15 before the Build Plan 1.3 wiring. Four of its current-tense code claims are now false: the yaw quaternion, the suppressed state-only updates, the lost movement flags, and the wield-type gap. Most path:line citations have also drifted. The byte layout itself (offsets, widths, the 195-byte inner length) still matches `build_add_pc`.

**Corrections:**

1. `old:` `` `players.rs:330-335` currently writes a half-angle yaw quaternion. For yaw pi/2 that supplies X=Z=0 and cannot represent the requested facing. Use `[direction.x, direction.y, direction.z, 0]`, or `[sin(heading), 0, cos(heading), 0]` while retaining the heading API. ``
   `new:` `` The yaw fix is in the tip: `players.rs:779-782` (`build_add_pc`) writes `[sin(heading), 0, cos(heading), 0]`, so the half-angle quaternion is gone. ``
   `why:` repo:prototype/osfr-tools/src/players.rs:779-782 (`for value in [player.heading.sin(), 0.0, player.heading.cos(), 0.0]`). players.rs:330-335 is now `set_mount`.

2. `old:` `` The gateway runner's `commit_outcome` (`bin/osfr-gateway.rs:1211-1249`) updates the registry only when position or rotation changed. `players.rs::update_pose` independently suppresses equal-pose updates. Both comparisons must include the two movement bytes for state-only relays to work. ``
   `new:` `` The gateway runner's `commit_outcome` (`bin/osfr-gateway.rs:1688`) treats a state/unknown change as movement (`moved` at `bin/osfr-gateway.rs:1824-1827`). `players.rs::update_pose_with_state` (`players.rs:378-398`) suppresses an update only when pose and both movement bytes are equal. ``
   `why:` repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:1688, 1824-1827 (`|| (state, unknown) != self.gateway.movement_bytes()`); repo:prototype/osfr-tools/src/players.rs:391-397.

3. `old:` `` `bin/osfr-gateway.rs:450-469` joins the registry with only identity GUIDs and pose. ``
   `new:` `` `bin/osfr-gateway.rs:602-630` (`join_player`) joins the registry with identity GUIDs, pose and the authenticated `PlayerPresentation`, via `join_with_presentation`. ``
   `why:` repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:609-620. Lines 450-469 are struct fields now.

4. `old:` `` The values are lost at the registry boundary, not at parsing. ``
   `new:` `` The values now cross the registry boundary: `PlayerSession` stores `movement_state` and `movement_unknown` (set at join and on update), and `build_position_update` writes them instead of `[0,0]`. ``
   `why:` repo:prototype/osfr-tools/src/players.rs:300-301, 414-415, 830.

5. `old:` `` `gateway.rs:510-521` already parses both bytes into `MovementUpdate`, checks the packet GUID against `CharacterState.guid`, and requires complete consumption at 535. ``
   `new:` `` `gateway.rs:616-628` already parses both bytes into `MovementUpdate`, checks the packet GUID against `CharacterState.guid`, and requires complete consumption at `gateway.rs:648`. ``
   `why:` repo:prototype/osfr-tools/src/gateway.rs:616-628 (`state: reader.u8()?, unknown: reader.u8()?`) and gateway.rs:648 (`reader.end()?`).

6. `old:` `**Researched; no implementation or native multiplayer acceptance.**`
   `new:` `**Researched 2026-10-15; the proposed seams are now implemented (Build Plan 1.3 is built, with native acceptance still not run).**`
   `why:` repo:notes/Design/Build Plan.md:58 ("Built 2026-10-15 ... PARTLY: tests pass, native not run"); repo:prototype/osfr-tools/src/players.rs:262 (`join_with_presentation`), 346 (`set_presentation`), 378 (`update_pose_with_state`).

7. `old:` `` Two existing integration defects (lost flags and suppressed state-only updates) and the quaternion error are documented, not fixed. ``
   `new:` `` Two integration defects (lost flags and suppressed state-only updates) and the quaternion error were documented at W77. All three are fixed at the tip (`players.rs:391-415`, `bin/osfr-gateway.rs:1824-1827`, `players.rs:779-782`). ``
   `why:` the same code as corrections 1, 2 and 4.

8. `old:` `` Equipped weapon definition's existing `Definition.wield_type` (`inventory.rs:95,807`); (R) 0 if no weapon. The getter/selection is not yet exposed by inventory; no job-to-wield table should be invented ``
   `new:` `` Equipped weapon definition's `Definition.wield_type` (`inventory.rs:181`), read by `Inventory::equipped_wield_type` (`inventory.rs:632`, slot 7, 0 when empty) and `Gameplay::public_wield_type` (`gameplay/profile_outfit.rs:42`); (R) 0 if no weapon. No job-to-wield table should be invented ``
   `why:` repo:prototype/osfr-tools/src/inventory.rs:181, 632-644; repo:prototype/osfr-tools/src/gameplay/profile_outfit.rs:42-43; repo:prototype/osfr-tools/src/gateway.rs:1061.

9. `old:` `` flair shard override, weapon selection/getter and post-join appearance broadcasts still need implementation/native review. ``
   `new:` `` flair shard override still needs implementation. The weapon getter (`Inventory::equipped_wield_type`) and the post-join presentation refresh (`players.rs::set_presentation`, called from `bin/osfr-gateway.rs:1833-1838`) exist and need native review. ``
   `why:` repo:prototype/osfr-tools/src/inventory.rs:632; repo:prototype/osfr-tools/src/players.rs:346-357; repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:1833-1838.

10. `old:` `` `gateway.rs::build_self_message` (1397-1440) ``
    `new:` `` `gateway.rs::build_self_message` (1925-1965; `apply_profile_state` now at 1967) ``
    `why:` repo:prototype/osfr-tools/src/gateway.rs:1925 and 1967.

11. `old:` `` `inventory.rs::Inventory::profile_attachments:340-365` returns exactly ``
    `new:` `` `inventory.rs::Inventory::profile_attachments:648-674` returns exactly ``
    `why:` repo:prototype/osfr-tools/src/inventory.rs:648-674. The same drift applies to two other citations in that bullet and the table: `write_attachment:991-1009` is now `inventory.rs:1494-1513`, and `profile_equipment:303-316` is now `inventory.rs:591-605`.

12. `old:` `This check proves the reconstructed layout's internal consistency, not that the production stub now sends these values.`
    `new:` `This check proves the reconstructed layout's internal consistency, not that the production build_add_pc (players.rs:755-817) now sends these values; it does. The byte test is tests/players.rs:532.`
    `why:` repo:prototype/osfr-tools/src/players.rs:755-817 (builds from the snapshot, not a stub); repo:prototype/osfr-tools/tests/players.rs:532 (`add_pc_matches_the_research_oracle_schema_byte_for_byte`).

**Unsure:**
- The note cites `tests/players.rs::expected_add_pc`. That function does not exist. The byte-exact test is `tests/players.rs:532`, which compares against `oracle_packet()`. I did not confirm whether `oracle_packet()` is independent of the writer.
- Two more moved citations that I did not put in the list: the base speed `gateway.rs:988-991` is now `gateway.rs:1528` (`base_speed_per_second: 10.0`), and the membership source `bin/osfr-gateway.rs:792,810` is now `bin/osfr-gateway.rs:1186` (`is_member = account.flags.membership`).
- The `Handoff 2026-10-16 evening.md` note mentions a late-joiner AddPc regression. I did not check whether it still holds at the tip.
- The Legacy flair-override gap and the server-side speed/underage/referee policy are design claims. I could not check them against the code.
- `put_string` still `expect`s on oversized lengths (`players.rs:851-857`). The snapshot is now validated first (`players.rs:661-696`), so the note's advice to validate at the snapshot boundary is already followed.
