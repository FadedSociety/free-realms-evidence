<!-- fleet job=note-refresh id=Stage7-NPC-Grounding-Semantics status=done turns=16 usd=0.0167 tokens(read,write,in,out)=[485693, 53231, 34, 10410] model=claude-haiku-5-5 -->
# notes/Research/Stage7 NPC Grounding Semantics.md

**Verdict:** minor drift. The status claims hold: the wolves are still unproved, no repair or migration exists, and the template fields match the code. Two statements about our Rust code are incomplete or misnamed.

**Corrections:**

1. `old:` The Rust encounter AI computes 3D distance and interpolates all three authoritative coordinates toward the player.
   `new:` The Rust encounter AI computes 3D distance and interpolates all three authoritative coordinates toward the player, then calls `ground.snap` on the new position. When a terrain grid is loaded, the server replaces Y with the grid height if the difference is within `MAX_SNAP` (6.0 m), so the server's Y is terrain-rewritten during pursuit.
   `why:` repo:prototype/osfr-tools/src/encounter.rs:2445-2450 (the step loop, then `ground.snap(&mut s.position)`); repo:prototype/osfr-tools/src/encounter.rs:778-798 (`Ground::snap`, `MAX_SNAP = 6.0`). The grid is wired in by repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:954 and repo:prototype/osfr-tools/src/encounter.rs:897-904. The field-engine path does the same in repo:prototype/osfr-tools/src/encounter/field.rs:1072-1084 (`advance` → `ground.field_position`).

2. `old:` `Encounter::spawn` supplies actor XYZ and explicit locomotion/speed while preserving those tilt/offset values.
   `new:` `EncounterEngine::spawn` (encounter.rs:2637, delegating to the free function `spawn_actor` at encounter.rs:3135) supplies actor XYZ and explicit locomotion/speed while preserving those tilt/offset values. The caller passes the authoritative state position (encounter.rs:1436, 2305).
   `why:` repo:prototype/osfr-tools/src/encounter.rs:817 (`impl EncounterEngine`), 2637-2639, 3135-3158. `spawn_actor` writes XYZ at bytes 37-49, speed/locomotion at 128-149 and MovementType at 233. It never touches bytes 94 (VerticalOffset) or 175 (HasTilt). There is no `Encounter` type in this file.

**Unsure:**

- The template values (HasTilt=false, Unknown42=false, VerticalOffset −0.10000000149, MovementType2) and the byte offsets 94/175/174/233 could not be checked. The template lives in the lab tree, which is not in the repo. The repo does pin `template_sha256` 602c66b1… in data/content/encounters.json:4, which I could not tie to the byte values.
- The five wolves sit at Y −45.98195 (data/content/encounters.json:31-109). This matches the note's "five copied spawn heights".
- "No migration has been prepared." is a negative claim. I found no migration in the repo, but I did not search every Autopilot report.
- The native-client claims (0092f460, 010ba6e0, 00fd4290, the proof hash) are outside this repo and were not checked.
