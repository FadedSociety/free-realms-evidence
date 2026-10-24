<!-- fleet job=note-refresh id=NPC-Greetings status=nothing_found turns=14 usd=0.0114 tokens(read,write,in,out)=[262349, 34417, 30, 9038] model=claude-haiku-5-5 -->
# notes/Research/NPC Greetings.md

**Verdict:** current. The note's claims about our code and data still hold at the tip; no correction needed.

**Corrections:** none.

What I checked:
- **Count (title: "17 added and 2 retained").** The 19 W126 bindings are pinned in `prototype/osfr-tools/tests/npc_greetings_starting_road.rs:145-165` (`EXISTING_GREETINGS`, 19 entries) and `prototype/osfr-tools/tests/npc_greetings_highroad_farnum.rs:163-183` (`W126_GREETINGS`, 19 entries). The note's 19 rows (17 new plus Samantha 9000000189 / 24940 and Merigold 9000000402 / 80) match those lists.
- **Each NPC id, name and greeting id** is bound in the file the note implies: for example Bartle 4420092 at `npcs/cobblestone_village.json:1289`, Raina 104100 at `npcs/highroad_junction.json:7552`, Merigold 80 at `npcs/highroad_junction.json:6986` (under the `9000000402` record starting at line 6553), Samantha 24940 at `npcs/cobblestone_village.json:8648`, Tyra 41268 at `npcs/merry_vale.json:31331`, Honeydew 413082 at `npcs/sunstone_valley.json:11340`. The name fields match the note's NPC names in every file.
- **Locale text.** The `locale` lookup returns the quoted line for every id in the table (e.g. 4420092, 94293, 94297, 4420036, 104100, 41268, 441420, 24842, 37872, 46166, 21602, 441432, 441037, 430860, 5696, 116463, 413082, 24940, 80). The note's "short" quotes are accurate, including the source typos ("Memoral Caverns").
- **Farnum guide row 37** is the Pappy Farnum row in `notes/Build Guides/Content/NPCs/NPCs - Farnum Farmstead.md:37`, and it quotes the same greeting.
- **Retained wording.** The note's "unchanged" label for Samantha and Merigold agrees with the tests, which treat them as pre-existing controls.
- **Later drift.** I found no Autopilot change (F271, F346, F349, T317) that alters a W126 binding; the later slices explicitly leave them untouched.

**Unsure:**
- The `en_us_data.dat` line numbers and JenkinsLookup2 hashes in the Evidence column are not checkable with these tools (no hash or line lookup into the client data). I did not verify them.
- The anchor string ids (e.g. 4420091, 94292, 104097) were not individually checked against the locale table.
- The `lab/reports/npc-greetings-w126/greetings.json` file cited by the data files is not visible under `repo`, so I could not confirm the report itself.
