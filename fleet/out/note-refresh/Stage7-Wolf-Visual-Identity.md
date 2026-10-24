<!-- fleet job=note-refresh id=Stage7-Wolf-Visual-Identity status=done turns=32 usd=0.0301 tokens(read,write,in,out)=[1325489, 71517, 66, 15863] model=claude-haiku-5-5 -->
# notes/Research/Stage7 Wolf Visual Identity.md

**Verdict:** minor drift. The code-side claims hold at the tip. One Models.txt citation is wrong and would send a reader to the wrong line.

**Corrections:**

- `old:` Preserved Models.txt row3284 is `wolf_generic.adr`.
  `new:` Preserved Models.txt row 2470 (model ID 3284) is `wolf_generic.adr`.
  `why:` `client:Resources/Models.txt` line 2470 is `3284^wolf_generic.adr^...`. Line 3284 of the same file is `4102^hsg_piano_block_01.adr`, so "row3284" read as a line number points at the wrong row. The repo already cites this as `Models.txt:2470` (`prototype/osfr-tools/data/content/enemies.json` ~L1469 and L2015) and `notes/Design/Field Enemies.md:127` says "row 2470".

**Checked and holding:**

- Five stage7 wolves with model 3284, name 5100200, empty texture alias, pinned to definition 3156: `prototype/osfr-tools/data/content/encounters.json` L22–50 and the four following entries; `refs:Sanctuary/src/Resources/Npcs.json` L11010–11014 (Id 3156, NameId 5100200, ModelId 3284, `wolf_generic.adr`).
- Wolf `max_health` 180, `move_speed` 3.0: `enemies.json` L16–26.
- Encounter spawn path uses the bundled template and overwrites position, disposition, name, model, walk/run/stand 2/3/1 and MovementType at offset 233 = 2: `prototype/osfr-tools/src/encounter.rs:3135–3158`. This matches "model/name/position/disposition and base animation override". Scale is only overwritten when `Actor.scale` is `Some`; wolf actors come from `world_enemies` with no scale field (`encounter.rs:2174` is the summon/power-up path), so the template scale stays.
- Animation IDs 1/3/1001 map to `loc_stand`/`loc_run`/`com_h2h_attack_01`: `prototype/osfr-tools/src/restoration/piece_052.rs:20–23`.
- The 33-slot / 48-bone / 36-file dependency counts are not contradicted in `repo`. `MODLOG.md:342` repeats the 48-bone and 33-slot figures.

**Unsure:**

- "The current encounter packet template has uniformScale1, VerticalOffset−0.1, HasTilt false and MovementType2." `prototype/osfr-tools/data/content/encounter-template.bin` exists, and `encounter.rs:3135–3158` keeps its HasTilt, VerticalOffset and scale bytes. Its bytes at offsets 33 (scale) and the VerticalOffset/HasTilt fields were not decoded, so I could not confirm the values.
- `prototype/osfr-tools/src/enemies.rs:713` sets `actor.scale = 3.0` for the field-enemy `spawn_packets` path. That path is not the stage7 encounter path, so it does not contradict the note, but a reader could confuse the two.
- The Sanctuary "row" and the "pinned community" hashes and the flora/scene placement (`sg_fairy_flora_01_cluster03`, object 1254768278) live outside `repo` (lab artifacts and external scenes). I did not check them.
