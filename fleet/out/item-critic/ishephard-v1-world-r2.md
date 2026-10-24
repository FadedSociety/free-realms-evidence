<!-- fleet job=item-critic id=ishephard-v1-world-r2 status=done turns=1 usd=0.0009 tokens(read,write,in,out)=[0, 3575, 4, 823] model=claude-haiku-5-5 -->
# Shephard

{"lens": "world", "pass": true, "wireable": false, "score": 3, "problems": [{"field": "item.kind", "issue": "The pack's item is 'Shephard', an NPC name (npc_name, locale 5102254), so it is not an item and cannot carry item acquisition sources. Kind 'other' does not say that. The answer correctly declines to assign sources, so this is a labeling issue, not a wrong acquisition.", "fix": "Mark the record as an NPC (not an item) and do not wire it as an item. Its stock items (Medic Job gear and shards) each need their own item-level evidence from their own wiki pages, as the answer's open list already says."}]}
