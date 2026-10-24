<!-- fleet job=item-critic id=imiguel-v1-evidence-r1 status=done turns=2 usd=0.0009 tokens(read,write,in,out)=[3253, 4326, 6, 689] model=claude-haiku-5-5 -->
# Miguel

{"lens": "evidence", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "item.kind", "issue": "Labelling 'Miguel' as kind 'other' is loose. The name matches only an NPC (locale:101989 is npc_name, and the wiki page is an NPC page). Nothing in the pack makes it an item.", "fix": "Mark it as not an item: an NPC (npc_name, locale:101989, wiki 'Miguel', categories NPC/Males/Human/Seaside). The answer already says this in its claims and open notes, so only the kind label needs changing."}]}
