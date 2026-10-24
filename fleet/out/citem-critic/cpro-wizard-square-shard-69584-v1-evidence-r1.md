<!-- fleet job=citem-critic id=cpro-wizard-square-shard-69584-v1-evidence-r1 status=done turns=4 usd=0.0028 tokens(read,write,in,out)=[31188, 14156, 10, 1429] model=claude-haiku-5-5 -->
# Pro Wizard Square Shard

{"lens": "evidence", "pass": true, "wireable": true, "score": 4, "problems": [{"field": "sources[0].where", "issue": "The label 'Coin Shop' for store category 121 is not evidenced. stores.json only gives category_id 121 with no name. A search of the repo found no store-category name table; the only 'id 121' hit is collection_catalogue.json id 121, which is a different table.", "fix": "Keep the price row, but describe the source as 'coin store category 121 (name not in data)' rather than 'Coin Shop' until a named category table or wiki listing confirms it."}]}
