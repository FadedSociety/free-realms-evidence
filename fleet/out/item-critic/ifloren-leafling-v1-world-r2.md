<!-- fleet job=item-critic id=ifloren-leafling-v1-world-r2 status=no_submit turns=2 usd=0.0012 tokens(read,write,in,out)=[3360, 4967, 6, 1058] model=claude-haiku-5-5 -->
# Floren Leafling

{"lens": "world", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "evidence[3]", "issue": "The claim that the repo spawn data places these NPCs 'in FabledRealms.lua zone scripts' is not supported by what I found. The search hits are all in prototype/osfr-tools/data/content/npc_spawns_extra.json, and I found no FabledRealms.lua reference. The JSON path is the correct source.", "fix": "Cite prototype/osfr-tools/data/content/npc_spawns_extra.json (Floren Leafling entries at lines 32996 to 33634) and drop the FabledRealms.lua attribution unless it is verified."}]}

The answer is true as far as it goes. Floren Leafling is an enemy NPC with no drop, vendor, or quest source in the pack, so `sources: []` and `wireable: false` are right. The wiki's Friendly Leafling page and the Bitterleaf page confirm that the pet pal comes from defeating Bitterleaf, so keeping it as a separate entry is correct. The `live: "unsure"` and null `retired` are honest unknowns.
