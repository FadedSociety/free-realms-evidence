<!-- fleet job=item-critic id=iforeman-moser-v1-world-r2 status=done turns=2 usd=0.0010 tokens(read,write,in,out)=[3649, 4201, 6, 904] model=claude-haiku-5-5 -->
# Foreman Moser

{"lens": "world", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "item.kind", "issue": "The entry is an NPC (npc_name, wiki category NPC/Merchant), not an item. Kind 'other' does not describe it as an acquirable item, so the record belongs under NPCs, not the item acquisition table.", "fix": "Mark as an NPC record (locale:429896 npc_name; wiki Foreman_Moser, rev 50082). It has no item acquisition to set."}]}
