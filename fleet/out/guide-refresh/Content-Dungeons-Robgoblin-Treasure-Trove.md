<!-- fleet job=guide-refresh id=Content-Dungeons-Robgoblin-Treasure-Trove status=done turns=12 usd=0.0121 tokens(read,write,in,out)=[267416, 41929, 26, 8375] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Robgoblin Treasure Trove.md

**Verdict:** current, with minor drift. The note is almost entirely client-text and video claims, which the repo does not record. The only checkable repo-side problem is a broken link block.

**Corrections:**

- `old:` NPCs: [[Wizard Hildegarde]], [[Blatt]], [[Terrence]], [[Clover]].
  `new:` NPCs (rows in [[NPCs - Wilds]]; no standalone pages exist): Wizard Hildegarde, Blatt, Terrence, Clover.
  `why:` No note files exist for these four names. A search of `notes/` for `Wizard Hildegarde.md`, `Blatt.md`, `Terrence.md`, `Clover.md` and for `aliases:` entries matching them returned nothing. The NPC rows are at `repo:notes/Build Guides/Content/NPCs/NPCs - Wilds.md:36` (Terrence), `:96` (Wizard Hildegarde), `:97` (Blatt) and `:246` (Clover). Only `[[Tavern Cellar]]` and `[[NPCs - Wilds]]` resolve among the links in that line.

**Checked and holding:**

- The dungeon row matches `repo:prototype/osfr-tools/src/restoration/piece_059.rs:150`: "Robgoblin Treasure Trove", difficulty 2, gate "northeast Wilds, at the Robgoblin Camp". This supports the Overview and Conflict 3 entrance wording.
- The client text "The trove can be found near the robgoblin camp to the northwest." and the "Defeat Wizard Hildegarde!", "Find Wizard Hildegarde's Spellbook!" and "Hildegarde's Spellbook" strings are present in the locale table. The locale tool uses its own ids, so I matched by text, not by the note's `loc` hashes.
- Nothing in `repo` or `notes/Autopilot/` states that the Trove is built, unbuilt or routed, so the note makes no status claim that could now be false.

**Unsure:**

- Whether the Robgoblin Treasure Trove is playable on our server. `piece_059.rs:150` gives it a gate and zone id 30447 but no recovered zone definition (the `Z(...)` field is `None`). The header of `piece_059.rs` says 29 dungeons have no zone definition. The note does not claim playability, so I made no correction.
- The "Atlas icon exists", the video frame keys and the exact `loc` hashes. These cite client or video sources I could not reach from the tools.
- The "Medic: Clover's Crisis" and "Medic on a Mission" chain pairings. These are client-text pairings I could not confirm from code.
