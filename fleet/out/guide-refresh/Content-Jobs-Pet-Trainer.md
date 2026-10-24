<!-- fleet job=guide-refresh id=Content-Jobs-Pet-Trainer status=done turns=24 usd=0.0381 tokens(read,write,in,out)=[1313640, 96794, 52, 25786] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Jobs/Pet Trainer.md

**Verdict:** current, with one minor drift. I found no false status claims and no stale code citations. The note makes almost no claims about our Rust server; its code references are to the client's mapped functions and packets, which the Pets guide supports.

**Corrections:**

1. `old:` A quest trainer lends a pet of the right species when the player has none (Rex, Buddy †, June Bug, Sparrow, Juniper, Tuffy).
   `new:` A quest trainer lends a pet of the right species when the player has none (Rex, Buddy †, June Bug, Sparrow, Juniper). Tuffy is not a loaner: he is Scrump's cat, which the player trains for the "Making a Champ" quest (row 12).
   `why:` Locale 90054, 90056 and 115644 ("Train Scrump's cat Tuffy to become really good at Box", "You need to go help Scrump train his cat Tuffy"). Scrump is listed as the troll owner in row 58 of the note itself.

**Checked and holding:**
- Client trick unlock strings: Speak 1; Jump, Sit Up 5; Box, Peek-a-Boo, Roll Over 10; Handstand, Spin 15; Dance, Play Dead 20.
- Command lines: present for Speak, Sit Up, Roll Over, Peekaboo, Handstand, Dance, Play Dead; absent for Jump, Box, Spin, as the note says.
- Gesture round strings "Get Ready!" and "Draw!"; the tutorial exit text; "Do NOT leave crossroads pet tutorial"; the "Oh, no! Want to keep playing as a Pet Trainer?" upgrade prompt; the level 4–20 achievement titles.
- Trainer locations, quotes and the Play Dead reward (1939693444).
- Pets guide mapping: `PetTrickSkillLevel` and `PetTrickAdd` are packets 12 and 13; `PetDecision` and `PetResponse`; `PetGesture` loads `PetTrickGesturePoints.txt` and `PetTrickGestureSettings.txt`; the 10 s timeout and 20 s hard stop; the owner-busy check in `UnlockPetTricksAfterGesture`. Cited at `notes/Build Guides/Gameplay/Pets.md:74-78`. The "What the Rust server must do" item 7 that row 216 cites is at `Pets.md:200`.
- `levelup_pettrainer.gfx` and `tutorial_petgestures.gfx` are in `client:Assets_manifest.txt`.
- Our server has `learn_trick` in `prototype/osfr-tools/src/pets.rs:1397`, with a comment that the caller applies the Pet Trainer job/level gate. The note does not claim otherwise.
- All NPC note links in the Related line exist under `notes/Build Guides/Content/NPCs/`.

**Unsure:**
- Locale id 4195071635 is cited for both Sparrow (row 59 trainer-pets cell) and the Box text "a great trick for cats" (row 11 and the trick table). Both cannot be right. The note's hash ids cannot be resolved with the locale tool, so I could not say which is wrong.
- Row 59 places Prissi at "the Cobblestone Pet Adoption Center tour". The locale ties the Prissi walk to a Sanctuary tour (Flurti's Tour Service, around locale 24881), so the location may be wrong. Not settled.
- The Pets guide's "147 waypoint rows for 23 trick ids" could not be checked. `PetTrickGesturePoints.txt` is in the manifest (3781 bytes) but its contents are not in the client tree.
- The "28 quest titles starting 'Pet Trainer:'" count is consistent with the table rows (19 wiki-list plus 9 client-only), but I did not count the locale directly.
