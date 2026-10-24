<!-- fleet job=note-refresh id=Opening-Cave-Replay status=done turns=14 usd=0.0125 tokens(read,write,in,out)=[273517, 33710, 30, 11081] model=claude-haiku-5-5 -->
# notes/Research/Opening Cave Replay.md

**Verdict:** minor drift. The behaviour the note describes holds at the tip (replay gate, fail-closed conditions, `stages()` getter, five-test file, no `411` literal in `gameplay.rs`, `begin` allocating a new instance and resetting health). The line citations have moved, most by 2,000 to 3,500 lines, and one XP claim is too broad.

**Corrections:**

1. `old:` - XP disclosure: this build has **no per-enemy XP path**; the only experience grant is `profiles.add_experience(25)` per opening stage reward ([gameplay.rs:1473](../prototype/osfr-tools/src/gameplay.rs:1473)), which fires once per stage because the stage is already rewarded. A replayed dungeon therefore cannot farm XP, coins or items.
   `new:` - XP disclosure: the cave grants **no per-enemy job XP**. Its battle reward carries `job_xp: 0` because the dungeon has a guide, so the only experience grant on a cave clear is `profiles.add_experience(25)` per opening stage reward ([gameplay.rs:4847](../prototype/osfr-tools/src/gameplay.rs:4847)), which fires once per stage because the stage is already rewarded. Field kills do grant per-enemy job XP, and non-guide battle wins grant 50. A replayed dungeon therefore cannot farm XP, coins or items.
   `why:` repo:prototype/osfr-tools/src/enemies.rs:600-604 (per-enemy `job_xp` on field kills); repo:prototype/osfr-tools/src/encounter.rs:2012 (`job_xp: if d.guide.is_none() { BATTLE_JOB_XP } else { 0 }`); repo:prototype/osfr-tools/src/gameplay.rs:4838-4847 (`apply_opening`, where the 25 XP is granted per opening reward).

2. `old:` ([gameplay.rs:1092-1097](../prototype/osfr-tools/src/gameplay.rs:1092))
   `new:` ([gameplay.rs:4608-4614](../prototype/osfr-tools/src/gameplay.rs:4608))
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:4608-4614 (`if let Some(id) = pending { … } else if selection { completed_dungeon_replay(guid) }`).

3. `old:` `completed_dungeon_replay` ([gameplay.rs:1625](../prototype/osfr-tools/src/gameplay.rs:1625))
   `new:` `completed_dungeon_replay` ([gameplay.rs:5035](../prototype/osfr-tools/src/gameplay.rs:5035))
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:5035 (`fn completed_dungeon_replay`).

4. `old:` through the new read-only `stages()` getter ([opening.rs:427](../prototype/osfr-tools/src/opening.rs:427))
   `new:` through the new read-only `stages()` getter ([opening.rs:431](../prototype/osfr-tools/src/opening.rs:431))
   `why:` repo:prototype/osfr-tools/src/opening.rs:427-433 (doc comment at 427, `pub fn stages` at 431).

5. `old:` The menu (`26/0/8/0`), talk/gather/craft interactions and the magic-door flow ([opening_dungeon_destination](../prototype/osfr-tools/src/gameplay.rs:1541)) are untouched.
   `new:` The menu (`26/0/8/0`), talk/gather/craft interactions and the magic-door flow ([opening_dungeon_destination](../prototype/osfr-tools/src/gameplay.rs:4948)) are untouched.
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:4948 (`fn opening_dungeon_destination`).

6. `old:` `enter_opening_cave` ([gameplay.rs:1586](../prototype/osfr-tools/src/gameplay.rs:1586))
   `new:` `enter_opening_cave` ([gameplay.rs:4993](../prototype/osfr-tools/src/gameplay.rs:4993))
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:4993 (`fn enter_opening_cave`).

7. `old:` the completion reward is emitted only when `rewarded.insert(id)` is new ([encounter.rs:784](../prototype/osfr-tools/src/encounter.rs:784))
   `new:` the cave's completion reward is emitted only when `rewarded.insert(id)` is new; non-guide battles always reward ([encounter.rs:2028](../prototype/osfr-tools/src/encounter.rs:2028))
   `why:` repo:prototype/osfr-tools/src/encounter.rs:2022-2028 (`let repeatable = d.guide.is_none();` … `if repeatable || self.state.rewarded.insert(id)`).

8. `old:` ([gameplay.rs:1473](../prototype/osfr-tools/src/gameplay.rs:1473))
   `new:` ([gameplay.rs:4847](../prototype/osfr-tools/src/gameplay.rs:4847))
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:4847 (`out.changed |= profiles.add_experience(25)?;`). This is the second citation in the XP bullet. Apply it together with correction 1, or skip it if correction 1 is applied as written, since that text already carries the new link.

**Unsure:**
- The test counts, RED/GREEN results, the regression-set counts, the rustfmt exit code and the SHA-256 prefixes are not checked. They depend on lab logs under `../lab/` and on running `cargo`, which I did not do.
- The "selection-1 variant" wording. `selection` is set around `gameplay.rs:4484-4510`, and the `inner[12..16] != 1` check is at `gameplay.rs:4510`. That matches the note, but I did not trace the whole branch.
- The test file `tests/opening_cave_replay.rs` exists with five `#[test]` functions (lines 275, 306, 336, 386, 407), as the note says. The individual assertions were not checked beyond the first 200 lines.
- The "no `411` or giver-guid literal in `gameplay.rs`" claim: a search for `\b411\b` found no match in `gameplay.rs`. The giver-guid literal was not searched.
