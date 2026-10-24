<!-- fleet job=citem-critic id=ccheese-wedge-block-8682-v1-world-r2 status=done turns=3 usd=0.0026 tokens(read,write,in,out)=[13893, 13708, 8, 1555] model=claude-haiku-5-5 -->
# Cheese Wedge Block

{"lens": "world", "pass": true, "wireable": true, "score": 4, "problems": [{"field": "sources[0].where", "issue": "Minor: the coin-store source has no vendor or store-to-NPC mapping, so it is a price-only source. The answer states this honestly in open[0]. Not a failure, but the source cannot be placed in the world yet.", "fix": "Keep where as null until a store-to-NPC mapping is found. Store row confirmed: repo prototype/osfr-tools/data/content/stores.json line 8299 has item_id 32668, category_id 147, purchase 5, member 4, sell 1, no_sale false. Client coin_store_prices [5] matches."}]}
