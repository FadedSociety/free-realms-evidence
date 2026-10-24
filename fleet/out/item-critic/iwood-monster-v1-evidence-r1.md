<!-- fleet job=item-critic id=iwood-monster-v1-evidence-r1 status=done turns=2 usd=0.0018 tokens(read,write,in,out)=[3140, 10254, 6, 877] model=claude-haiku-5-5 -->
# Wood Monster

{"lens": "evidence", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "item.kind", "issue": "The answer keeps an item record with kind \"other\" for a subject its own evidence says is a comic character with no in-game presence. The record is harmless only if it is read as 'not an item'.", "fix": "Mark the entry as not an item (for example, nothing_found or a non-item status) rather than an item with kind \"other\". Source: wiki page Wood_Monster (rev 50035) says it appears only in Free Realms Issue 1 and 2 and its Trivia lists it among characters who don't appear in-game."}]}
