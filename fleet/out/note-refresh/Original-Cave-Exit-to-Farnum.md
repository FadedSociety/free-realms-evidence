<!-- fleet job=note-refresh id=Original-Cave-Exit-to-Farnum status=done turns=14 usd=0.0115 tokens(read,write,in,out)=[271398, 33983, 30, 9141] model=claude-haiku-5-5 -->
# notes/Research/Original Cave Exit to Farnum.md

**Verdict:** minor drift. The research claims (Magic Door to Farnum, Pappy spawn, locale meaning) still hold. The "Implementation boundary" section is written as a plan, but the story-gated travel is now in the code.

**Corrections:**

1. `old:` Use the existing verified normal zone-transition delivery for a legitimate **story-gated guide/door travel action**.
   `new:` The story-gated guide/door travel action is implemented. Darkthorne's interaction returns the Farnum zone transition (`opening_dungeon_destination`, with the message "Darkthorne's magic door takes you to Farnum's Farmstead."), and a won cave encounter's exit uses the same destination.
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:4519-4527 (interaction path); gameplay.rs:4933-4936 (won-encounter exit path); gameplay.rs:4946-4948 (helper comment: "Locale 4420033/4420043 prove the magic-door journey"). Also notes/Reviews/Native Farm Travel 090058.md:7, a native run that travelled to Farnum.

2. `old:` Gate it on accepted/unrewarded Last Best Hope with cave goal complete and Pappy talk pending, plus the completed encounter411 state.
   `new:` The implemented gate (`opening_dungeon_destination`) requires the accepted Last Best Hope stage, the cave's `DungeonCompleted` goal (encounter 411) rewarded in the encounter state, and the Pappy `Talk` goal still uncounted. It returns no destination otherwise. The arrival is the Pappy actor position plus a 3.0 m x-offset, labelled as a reconstructed placement.
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:4948-4990 (gate and +3.0 offset); repo:prototype/osfr-tools/data/content/dungeons/opening_cave.json:975 (encounter_id 411); repo:prototype/osfr-tools/data/content/npcs/farnum_farmstead.json:5473-5475 (Pappy spawn `[-2184.513,-31.53728,328.1112]`, which matches the note).

**Unsure:**

- "The prior generic activity return to the old overworld spawn requires crossing an impassable cliff." I found no code or note evidence for the cliff. The code returns a cave exit to the cave's `return_location`, which is validated against the cave's world zone (repo:prototype/osfr-tools/src/encounter.rs:1369-1370, 2583-2586). The cave-return comment says "Old checkpoints returned to the cave's original world location" (gameplay.rs:4519-4520). I did not confirm the "impassable cliff" detail.
- "Private proof: `lab/reports/...`" cites a path that is not in the repo. `.gitignore:28` ignores `/lab/`, and `.gitignore:27` says lab data lives in the sibling `../lab`. I could not open the report or helper, so the 14-record count and hashes are unverified.
- Locale IDs: the note maps 4420042/4420043 to Saving Farnum's Farm, while the code comment cites 4420033/4420043 for the magic-door journey (gameplay.rs:4947). My locale tool searches text, not IDs, so I could not confirm the ID mapping.
- The note's requirement that the arrival be "independently terrain-checked" is still open. The code applies only the +3.0 x-offset and does no terrain check (gameplay.rs:4984-4986).
