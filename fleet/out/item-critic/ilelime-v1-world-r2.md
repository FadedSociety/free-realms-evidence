<!-- fleet job=item-critic id=ilelime-v1-world-r2 status=done turns=2 usd=0.0012 tokens(read,write,in,out)=[3155, 5196, 6, 955] model=claude-haiku-5-5 -->
# Lelime

{"lens": "world", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "item.kind", "issue": "Lelime is an NPC (client npc_name, locale 101209; wiki page 'human NPC located at Seaside'), so 'kind: other' is a mislabel. The item framing itself is the request's error, not a source error.", "fix": "Mark as not an item (kind: npc or none). Wiki (rev 45892) and locale:101209 both identify an NPC; locale:101199 'Give Lelime a Brain Freeze!' is a quest_objective target, not a reward."}]}
