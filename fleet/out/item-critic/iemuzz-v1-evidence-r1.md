<!-- fleet job=item-critic id=iemuzz-v1-evidence-r1 status=done turns=2 usd=0.0010 tokens(read,write,in,out)=[3117, 4111, 6, 811] model=claude-haiku-5-5 -->
# Emuzz

{"lens": "evidence", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "item.kind", "issue": "Kind is set to \"other\" for a name that is an NPC, not an item. The answer does not explain why it still has an item record, and no item category applies.", "fix": "Mark the record as not an item (an NPC name, locale 45586, npc_name). The wiki page (rev 49866) says Emuzz is a bixie NPC in Seaside, with categories NPC, Females, Bixie, Seaside, and quest appearances only. Client strings 95035, 95036, 101404 and 139578 confirm she is a quest NPC."}]}
