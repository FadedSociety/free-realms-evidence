<!-- fleet job=item-critic id=iroberge-v1-evidence-r1 status=no_submit turns=2 usd=0.0010 tokens(read,write,in,out)=[3498, 4220, 6, 802] model=claude-haiku-5-5 -->
# Roberge

{"lens": "evidence", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "item.kind", "issue": "The answer labels Roberge as an item with kind \"other\", but its own evidence says the locale string is an NPC name and the wiki page is an NPC merchant page. Kind \"other\" hides that this is not an item at all.", "fix": "Mark the record as not an item (an NPC name, locale 5101978, client tag npc_name). Source: locale:5101978 returns 'Roberge', and the wiki page 'Roberge' describes a human NPC merchant at the Greenwood Forest Cooking Table."}]}
