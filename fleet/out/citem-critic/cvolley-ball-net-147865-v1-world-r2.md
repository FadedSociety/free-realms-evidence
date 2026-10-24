<!-- fleet job=citem-critic id=cvolley-ball-net-147865-v1-world-r2 status=done turns=2 usd=0.0014 tokens(read,write,in,out)=[3474, 7017, 6, 1072] model=claude-haiku-5-5 -->
# Volley Ball Net

{"lens": "world", "pass": true, "wireable": true, "score": 4, "problems": [{"field": "sources[0].price", "issue": "The 15000-coin figure is an outlier for category 57 (pool decor). Sibling rows in stores.json (16871-16893) are mostly 50 or 1000 coins, and the article gives no price. The answer already flags this in open, so it is not a false claim, but it rests on one store row.", "fix": "Keep 15000 / member 13500 as the stored row value (stores.json:4246, item 16883, purchase_price_coins 15000, member_price_coins 13500), and mark it as unconfirmed against a live Coin Shop listing."}]}
