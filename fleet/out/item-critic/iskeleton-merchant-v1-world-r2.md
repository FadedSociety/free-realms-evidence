<!-- fleet job=item-critic id=iskeleton-merchant-v1-world-r2 status=done turns=2 usd=0.0012 tokens(read,write,in,out)=[3158, 6126, 6, 766] model=claude-haiku-5-5 -->
# Skeleton Merchant

{"lens": "world", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "item.kind", "issue": "The answer lists kind 'other' for an entity that its own evidence calls an NPC character, not an item. This is a minor labelling mismatch, not a wrong source.", "fix": "Mark it as not an item (for example kind 'npc' or an excluded-entity flag). The wiki infobox (name Skeleton Merchant, gender Male, race Skeleton, occupation Merchant) and the 'was a character' sentence in the page text support this, rev 50083."}]}
