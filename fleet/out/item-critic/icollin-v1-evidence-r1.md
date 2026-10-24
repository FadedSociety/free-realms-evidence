<!-- fleet job=item-critic id=icollin-v1-evidence-r1 status=done turns=3 usd=0.0011 tokens(read,write,in,out)=[7188, 4085, 8, 938] model=claude-haiku-5-5 -->
# Collin

{"lens": "evidence", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "evidence[1]", "issue": "The locale claim gives the zone 'Lakeshore' for locale:38372 and 'Shady Shores' for locale:5100267. I confirmed that locale:38372 reads 'Collin' but could not confirm its npc_name type or the Lakeshore zone tag from the locale lookup.", "fix": "locale:38372 = 'Collin' is confirmed. The zone and npc_name tags come only from the evidence pack, so cite them as pack metadata, not as checked text."}]}
