<!-- fleet job=item-critic id=iconnie-v1-world-r2 status=done turns=2 usd=0.0010 tokens(read,write,in,out)=[3148, 4069, 6, 919] model=claude-haiku-5-5 -->
# Connie

{"lens": "world", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "item.kind", "issue": "Kind 'other' is a loose label for a target that is an NPC, not an item. The answer is honest that Connie is not an item, but the record should say so explicitly rather than filing her as an item of kind 'other'.", "fix": "Mark the target as not an item (an NPC name, locale 93122, npc_name type). Evidence: lookup returns only locale:93122 (npc_name) and the wiki page 'Connie' (female human NPC at Seaside, Category:NPC). Nothing else matches."}]}
