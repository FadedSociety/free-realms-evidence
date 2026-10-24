<!-- fleet job=citem-critic id=ccobblestone-small-pillar-148420-v1-world-r2 status=done turns=3 usd=0.0019 tokens(read,write,in,out)=[13188, 9509, 8, 1096] model=claude-haiku-5-5 -->
# Cobblestone Small Pillar

{"lens": "world", "pass": true, "wireable": true, "score": 4, "problems": [{"field": "sources[0].where", "issue": "The store row has no vendor NPC or shop page, so `where` is null. The answer says this honestly, and the world lens does not require it. Still, the row is a legacy CoinStoreItems listing (tag L1), so the source is a coin-store listing, not a named vendor.", "fix": "Keep `where` null and label the source as 'Legacy coin store listing, category 4'. Confirm the vendor from the category 4 store listing before naming one."}]}
