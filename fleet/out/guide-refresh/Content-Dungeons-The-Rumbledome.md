<!-- fleet job=guide-refresh id=Content-Dungeons-The-Rumbledome status=nothing_found turns=22 usd=0.0234 tokens(read,write,in,out)=[906728, 64877, 46, 12359] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/The Rumbledome.md

**Verdict:** current. I found no claim about our code or status that is now false. The note's checkable claims are almost all client-locale and video facts, and every quoted string I spot-checked exists in the locale table with the wording given.

**Corrections:** none.

What I checked:
- **Client strings:** "Defeat the Champion of the Rumbledome!" (locale 410433), "Defeat Bronzeknuckles!" (410421), "Defeat Silverfist!" (410425), "Defeat Goldcrusher, champion of Rumbledome!" (412729), the second-wave Gladiator strings (438816/438817), "Rumbledome Duel!" (440028), the duel description with "Potions and other consumables cannot be used" (440029), the Kraig/Krissy lines (412132, 410576, 410577, 410571), the announcer lines (410368, 438819, 438821, 438828, 412142), the Wade Shatterslag and Dorn quest lines (412743, 412815, 440385), "Complete the Rumbledome TCG Questline." (442367 to 442370 trophies), and "Tattered Short-sleeve Shirt" / "Knee-high Combat Boots" (33976, 33994). "Level 1 Combat Gear" has no match, which agrees with the note.
- **Repo:** `prototype/osfr-tools/data/content/dungeons/the_rumbledome.json` exists and has difficulty 1 and zone Sunstone Valley with no numeric zone ID, as the note's Overview implies. `Dungeons.md:120` lists it as a Battle, difficulty 1, min combat level none, "written". Both match the note. `dungeons_unresolved.json` and `enemies_unresolved.json` hold the Rumbledome entries the note's Enemies table describes (Fire Trap, Gloam Fire Trap, Kraig, Rumbledome Gladiator), and the note's reading of them is consistent.
- **Autopilot:** no report in `notes/Autopilot/` touches the Rumbledome.

**Unsure:**
1. **Status framing.** The lead paragraph calls it "a real combat instance", and Conflicts #1 says it "is treated as a combat instance here." `notes/Design/Build Ledger.md:78` says dungeons beyond the cave are "Researched", with "None are playable." The note never claims the Rumbledome is playable on our server, so I did not correct it. A reader could still take "treated as a combat instance here" as implemented, so the note could say "modelled as a battle record (`data/content/dungeons/the_rumbledome.json`), not playable (Build Ledger line 78)."
2. **Dangling wikilinks.** Lines 92 and 85 link `[[Dorn Geargrinder]]`, `[[Bronzeknuckles]]` and similar names. No such files exist under `notes/Build Guides/Content/NPCs/`; NPCs live in the zone pages such as `NPCs - Sunstone Valley.md`. `Sandscale Oasis.md:92` uses the same pattern, so this looks like a vault-wide convention rather than a drift in this note.
3. **Loc IDs.** Many IDs in the note (e.g. `loc 768596353`, `439732449`, `1793168724`) do not resolve through the `locale` tool, which keys on its own numbering. The strings they name do exist, so I could only confirm the text, not the ID.
4. **Entrance prompt.** "Join The Rumbledome?" / "Press X" does not appear in the locale table. It is probably an on-screen label from the video, so I could not confirm it.
5. **Video and wiki claims** (run timings, "Seen playing at" levels, the wiki infobox and battle-index contents, the "22 coins" reading) are outside this repo and were not checked.
