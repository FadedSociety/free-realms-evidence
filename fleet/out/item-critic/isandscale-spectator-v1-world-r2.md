<!-- fleet job=item-critic id=isandscale-spectator-v1-world-r2 status=done turns=3 usd=0.0011 tokens(read,write,in,out)=[6940, 5037, 8, 875] model=claude-haiku-5-5 -->
# Sandscale Spectator

{"lens": "world", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "item.kind", "issue": "The subject is an NPC (client locale:442915 is npc_name, and the wiki page is in Category:NPC), not an item. Recording it as an item with kind 'other' is a category mismatch, though the answer's 'NPC, not an item' note makes this clear.", "fix": "Mark it as a non-item (NPC) record, or exclude it from the item pipeline. Source: locale:442915 [npc_name]; wiki Sandscale_Spectator rev 45814 Category:NPC."}]}
