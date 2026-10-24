<!-- fleet job=citem-critic id=celite-pink-rock-digger-helmet-6125-v1-world-r2 status=no_submit turns=3 usd=0.0018 tokens(read,write,in,out)=[10798, 8362, 8, 1281] model=claude-haiku-5-5 -->
# Elite Pink Rock Digger Helmet

{"lens": "world", "pass": true, "wireable": true, "score": 4, "problems": [{"field": "sources[0].where", "issue": "The store row is only evidenced as a store listing in category 101. Its source_tags (L1, L2, L4, R2, T633, R1) are unexplained, so 'Coin store' is the only label the data supports, not a named vendor or shop page.", "fix": "Keep the source as 'coin store listing, store item 2487, category 101' with no vendor claim. The stores.json row at line 667 is the only evidence, and the client definition's coin_store_prices [9453] matches it."}]}
