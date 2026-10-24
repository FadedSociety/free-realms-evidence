<!-- fleet job=citem-critic id=cscuba-fins-396342-v2-world-r2 status=no_submit turns=2 usd=0.0015 tokens(read,write,in,out)=[3485, 7533, 6, 1144] model=claude-haiku-5-5 -->
# Scuba Fins

{"lens": "world", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "sources", "issue": "The 270-coin figure is a client-definition coin_store_prices value with no vendor or stores.json row. The answer keeps it out of sources, which is correct, but it is not stated as an unplaced price anywhere in the source list. Note it as a price-only fact so a builder does not read it as a sale.", "fix": "Record coin_store_prices [270] from the client definition pack as an unplaced price with no vendor. Lookup and locale searches found no store, vendor or quest naming Scuba Fins."}]}
