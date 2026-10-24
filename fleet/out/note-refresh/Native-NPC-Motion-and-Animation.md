<!-- fleet job=note-refresh id=Native-NPC-Motion-and-Animation status=done turns=14 usd=0.0169 tokens(read,write,in,out)=[388172, 51884, 30, 13042] model=claude-haiku-5-5 -->
# notes/Research/Native NPC Motion and Animation.md

**Verdict:** minor drift. The native-address, packet-layout and template facts hold at the tip. Two status sentences about the root agent's combat fixes predate code that has since landed.

**Corrections:**

1. `old:` Root owns the combined Speed3, explicit locomotion IDs, State1 and finite-heading change and its visible retest.
   `new:` The combined Speed3, explicit locomotion IDs, State1 and finite-heading change are now in the field-enemy path: spawn speed is `move_speed` and walk/run/stand IDs are 1/3/1 (`enemies.rs:724-727`), movement is standalone opcode 125 with State1/Unknown0 (`enemies.rs:796-805`), and the heading is horizontal with Y=0 and normalised by the 3-D delta (`enemies.rs:688`; `encounter/field.rs:1061-1062`). A visible native retest is still open and remains the root agent's acceptance step.
   `why:` `repo:prototype/osfr-tools/src/enemies.rs:688`, `:724-727`, `:796-805`; `repo:prototype/osfr-tools/src/encounter/field.rs:1061-1062`

2. `old:` Zero spawn speed and unset locomotion overrides are concrete differences from Sanctuary's moving NPCs.
   `new:` Zero spawn speed and unset locomotion overrides are concrete differences from Sanctuary's moving NPCs for content spawns, which use the `content_spawn_template` (speed left at its derived 0; walk/run/stand IDs -1). Field enemies no longer have these defaults (`enemies.rs:724-727`).
   `why:` `repo:prototype/osfr-tools/src/world.rs:635-656` (template sets walk/run/stand -1 at 645-647 and leaves speed at default); `repo:prototype/osfr-tools/src/enemies.rs:724-727`

**Checked and holding (no change):**
- Native function addresses in the note all resolve in the client decompile: `008e5940`, `0090de90`, `00963840`, `0095dae0`, `0095e890`, `0096c780`, `0096d370`, `007829a0`, `008b3180`, `007776b0`, `00908a50`, `0091cac0`, `00921a10`, `0173c1c0`, `0173c140`. `008b3180` returns Speed×(1.0 or the 0x650 constant) and `0173c1c0` sets the `[1,0,1,0]`-style mask, as the note says.
- AddNpc template: `world.rs:645-651` sets walk/run/stand -1, `is_interactable` 1, `movement_type` 2. `combat.rs:350-362` validates a 334-byte template with `bytes[224] == 1`, and `combat.rs:327-343` patches fixed offsets first, then strings in reverse order. Both match the note's offsets and its "patch before inserting strings" advice.
- Opcode 125 is 36 bytes (`enemies.rs:796-805`; `encounter/field.rs:1053`). Subtype 8 animation is 21 bytes (`enemies.rs:787-794`), and the neutral attack uses Flags 0 (`enemies.rs:457`), as the note says.

**Unsure:**
- `CodeAnimationMappings.txt` (IDs 1/3/1000/1001) is not in the repo or the client root, and the ADR-toolkit refs did not confirm it. I could not check the mapping.
- `00908a50` is described as the subtype-8 reader. Its client decompile looks like a bounded check that calls `008e5dd0`. The label record says its semantics are unresolved. `notes/Autopilot/T359.md:51` also calls it the 35/8 dispatcher, so I left the claim alone.
- Line references such as "1065441", "1093435" and "1127006-1127011" point into an export I could not map, so I did not verify them.
- The Sanctuary revision, lab fixtures and the 13-fixture count live outside the repo (only `scripts/pieces/piece_052.py` mentions the 13 fixtures), so I could not check them.
