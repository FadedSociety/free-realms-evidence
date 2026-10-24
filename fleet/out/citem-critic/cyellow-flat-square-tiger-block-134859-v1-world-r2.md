<!-- fleet job=citem-critic id=cyellow-flat-square-tiger-block-134859-v1-world-r2 status=no_submit turns=2 usd=0.0014 tokens(read,write,in,out)=[3896, 6974, 6, 899] model=claude-haiku-5-5 -->
# Yellow Flat Square Tiger Block

{"lens": "world", "pass": true, "wireable": true, "score": 4, "problems": [{"field": "sources[0].detail", "issue": "The vendor is described only as a coin store sale with no NPC or shop name. The store row is real, but the source is a store entry, not a named vendor, so a builder has to attach it to store category 147 rather than to a vendor.", "fix": "Keep the source as a coin store entry: stores.json line 16645, item_id 77314, category_id 147, purchase_price_coins 250, member_price_coins 225, no_sale false. The NPC stays open, as the answer already says."}]}
