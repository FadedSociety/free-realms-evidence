<!-- fleet job=guide-refresh id=World-Zones-and-Terrain status=done turns=18 usd=0.0268 tokens(read,write,in,out)=[652725, 67889, 38, 23591] model=claude-haiku-5-5 -->
# notes/Build Guides/World/Zones and Terrain.md

**Verdict:** minor drift. The note is a generated map of client functions, so it makes few claims about our server code. Its internal counts match its own tables, and the wire markers and sampled names hold. The world.terrain counts and the overall totals are stale against the current label table. Fourteen shard links in the source list also look dangling.

**Corrections:**

1. `old:` 367 accepted functions: 177 confirmed, 83 likely, 70 speculative, 37 unknown.
   `new:` 468 accepted functions: 212 confirmed, 144 likely, 75 speculative, 37 unknown.
   `why:` The current label table (client_sql, `label` where subsystem in the six listed and status = accepted) gives confirmed 212, likely 144, speculative 75, unknown 37, total 468. The 37 unknown matches the note. The shortfall of 101 is all in world.terrain: the table has 237 terrain labels against the note's 136. The note's own tables agree with 136 (terrain section, repo:notes/Build Guides/World/Zones and Terrain.md:479-705, class headers sum to 136). So the table was generated before the label set grew. Regenerate the table if the header is meant to match the database.

2. `old:` `world.terrain` (136)
   `new:` `world.terrain` (237)
   `why:` Same label-table query: world.terrain has 83 confirmed, 95 likely, 40 speculative, 19 unknown = 237 accepted. The other five subsystem counts on line 21 (engine.area 134, world.pointofinterest 36, ui.campaign 25, engine.campaign 21, world.area 15) match the table exactly, so only this one is stale. Note that the table below still lists 136 rows, so this is a snapshot until the section is regenerated.

**Checked and holding:**
- `wire` count of 2 and the two 🌐 rows: repo:notes/Build Guides/World/Zones and Terrain.md:420 (ClientPointOfInterestManager_SendTeleportRequest, sends PacketZoneTeleportRequest) and :424 (OnDefinitionReply, recv PacketPointOfInterestDefinitionReply). The label table has exactly these two entries with a non-empty wire field.
- Section header counts sum to the stated subsystem totals: engine.area 134, world.terrain 136.
- Sampled addresses and names (about 25 across engine.area, world.area, world.pointofinterest and world.terrain) match the label table.
- Shard links with address ranges (S0220, S0221, S0227, S0276, S0334, S0360, S0376, S0378, S0422, S0443, S0658) resolve to files in repo:notes/Native Map/Shards/.

**Unsure:**
- Fourteen links in the Source shards line have no address and no matching file in notes/Native Map/Shards: [[S0377]], [[S0439]], [[S0440]], [[S0442]], [[S0542]], [[S0567]], [[S0592]], [[S0660]], [[S0689]], [[S0697]], [[S0723]], [[S0739]], [[S0764]], [[S0790]]. Commands.md cites S0697, S0723, S0739, S0764 and S0790 as bare IDs, so the shard pages may simply not exist. I did not confirm that no file of that name exists elsewhere in the vault. Their shard counts also sum to 367, so they would change with the fix in item 1.
- The narrative section ("How it works") is still the placeholder text, so I did not assess it.
