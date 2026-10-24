<!-- fleet job=note-refresh id=Native-Opening-Interaction-Audit status=done turns=29 usd=0.0304 tokens(read,write,in,out)=[1201044, 80292, 60, 16734] model=claude-haiku-5-5 -->
# notes/Research/Native Opening Interaction Audit.md

**Verdict:** minor drift. The packet layouts (26/8, 26/9, 26/10, 35/12), the 13/16-byte sizes, the seven-integer menu record, the ID1 option, the proximity and option-1 checks, the 334-byte template offsets, the 27-actor count and the Lua/Native Opening Quest Journal links all match the tip. Three statements are stale or imprecise.

**Corrections:**

1. `old:` currently0→actual global7 m fallback
   `new:` currently written per actor from `interaction_radius` (12 m in the fixture; the global 7 m fallback applies only when the stored float is nonpositive)
   `why:` repo:prototype/osfr-tools/src/opening_world.rs:75 (`bytes[237..241]` = `actor.interaction_radius`, added after the audit); repo:notes/Research/Native Interaction Acquisition Range.md:9 (nonpositive → global fallback) and :32, :38 (the float237 write was integrated and the 12 m reach is the value); repo:prototype/osfr-tools/tests/fixtures/quests/opening.json:24 (12.0). The audit's "currently0" describes the pre-integration template only.

2. `old:` Per-actor fields are patched before inserting the variable name at106.
   `new:` Per-actor fields are patched before inserting the variable name at106: GUID, name ID, model, position, the int at 133 (ceiling of `interaction_radius`) and the float at 237 (`interaction_radius`).
   `why:` repo:prototype/osfr-tools/src/opening_world.rs:63-82 (spawn writes 4..20, 37..53, 133..137, 237..241, then splices the name at 106). The template gate at repo:prototype/osfr-tools/src/combat.rs:351-357 (length 334, byte224 == 1, int133 == 100) still holds for the unpatched template.

3. `old:` NPC labels use recovered locale IDs3300 (*Talk*) and432156 (*Interact*).
   `new:` Opening menus use locale IDs 3300 (*Talk*, for `kind` npc) and 432156 (*Interact*, for all other opening actors such as gather/craft actors); the vendor Shop choice also reuses 432156.
   `why:` repo:prototype/osfr-tools/src/opening_world.rs:91 (`if actor.kind == "npc" { 3300 } else { 432156 }`); repo:prototype/osfr-tools/src/npc_interaction.rs:48-50 and :846 (432156 reused for Shop); locale 3300 = "Talk", 432156 = "Interact".

**Unsure:**
- "Cursor5 is `cursor_talk` in supplied `Resources/Cursors.txt`": the repo emits cursor 5 (opening_world.rs:57; combat.rs:392) and `cursor_talk` appears in the refs manifests, but no `Cursors.txt` was reachable through the refs or client roots, so the mapping rests on repo:notes/Research/Native Combat Controls.md:24.
- "32813 reads the mapped key from `BaseClient.ControllerOptions`": the ui root shows `ControllerOptions` reads at ScriptsBase.lua:32802 and :32814; 32813 may be off by one. The 32784, 43501 and 43539 citations check out.
- "27 actors, 24 of them non-enemy": 27 is corroborated by repo:notes/Research/Starting Area Content Audit.md:38 and Opening Historical Coverage Ledger; the 24 matches repo:notes/Research/Native Interaction Acquisition Range.md:5. The private `opening.json` is not in the tree, so the count was not recomputed.
- Terrain heights, model bounds and `lab/` report hashes live outside the repo and were not checked.
