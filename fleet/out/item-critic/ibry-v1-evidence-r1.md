<!-- fleet job=item-critic id=ibry-v1-evidence-r1 status=no_submit turns=3 usd=0.0012 tokens(read,write,in,out)=[8175, 4561, 8, 1029] model=claude-haiku-5-5 -->
# Bry

{"lens": "evidence", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "live", "issue": "The answer sets live to \"no\" but no source in the pack says the NPC name is retired or non-live. The pack only shows that locale 38107 is the npc_name string 'Bry' and that the wiki page has no price or source fields. 'live: no' is an inference, not evidence.", "fix": "Leave live as unknown (null) unless a source states otherwise. The evidence supports only that the item has no acquisition sources (wiki page: no Coins, Station Cash or IGD entries; vendor_stock empty; no quest reward naming Bry as an item)."}]}
