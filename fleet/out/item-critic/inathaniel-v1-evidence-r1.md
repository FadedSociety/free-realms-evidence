<!-- fleet job=item-critic id=inathaniel-v1-evidence-r1 status=done turns=2 usd=0.0011 tokens(read,write,in,out)=[3045, 4043, 6, 1078] model=claude-haiku-5-5 -->
# Nathaniel

{"lens": "evidence", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "evidence[2]", "issue": "Says Nathaniel is 'placed as a Seaside NPC spawn' citing seaside.json:5454. That line is one comma-joined name list (Betsy, Connie, ... Nathaniel, ...) in a group entry, not a per-NPC spawn record. Only npc_spawns_extra.json:8857 has Nathaniel as its own 'name' field.", "fix": "Cite npc_spawns_extra.json:8857 as the spawn record and describe seaside.json:5454 as a grouped Seaside NPC name list (also noted in notes/Build Guides/Content/NPCs/NPCs - Seaside.md:149)."}]}
