<!-- fleet job=citem-critic id=cstandard-painted-trunk-132615-v1-world-r2 status=no_submit turns=3 usd=0.0022 tokens(read,write,in,out)=[14747, 11521, 8, 1268] model=claude-haiku-5-5 -->
# Standard Painted Trunk

{"lens": "world", "pass": true, "wireable": true, "score": 4, "problems": [{"field": "where", "issue": "The label 'Coin Shop' is asserted as the shop name, but no source names a shop. The answer's own open note says the shop name is unconfirmed, so the field overstates what is known.", "fix": "Set where to 'Coin store, category 53 (shop name unknown)'. Evidence: repo stores.json line 11874 (category_id 53) and FreeRealms-Legacy CoinStoreItems.json line 53324 (Id 36202, CategoryId 53)."}]}
