<!-- fleet job=citem-critic id=cshadow-infused-long-cloak-124913-v2-world-r2 status=no_submit turns=2 usd=0.0012 tokens(read,write,in,out)=[4282, 5874, 6, 876] model=claude-haiku-5-5 -->
# Shadow Infused Long Cloak

{"lens": "world", "pass": true, "wireable": true, "score": 4, "problems": [{"field": "sources[0].source / open", "issue": "The answer labels the source tag 'L1' as 'Legacy CoinStoreItems'. I found no evidence for that expansion in the stores.json rows I read. The rows only carry the bare tag list [L1, L2, L4, R2, T633, R1]. The label is an unsupported gloss, not a sourced fact.", "fix": "State only that stores.json line 8116 carries source_tags [L1, L2, L4, R2, T633, R1] and that the tag meaning is unverified. The price and item_id claims are correct as written."}]}
