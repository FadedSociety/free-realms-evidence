<!-- fleet job=citem-critic id=cpro-algae-square-shard-8346-v1-evidence-r1 status=done turns=4 usd=0.0025 tokens(read,write,in,out)=[26797, 11983, 10, 1516] model=claude-haiku-5-5 -->
# Pro Algae Square Shard

{"lens": "evidence", "pass": true, "wireable": true, "score": 4, "problems": [{"field": "sources[0].type", "issue": "Labelled 'vendor', but the only evidence is a coin-store row (stores.json line 621: item_id 2158, category_id 121). No NPC, shop or vendor name is tied to category 121 anywhere in the repo, so 'vendor' is an inference, not evidenced.", "fix": "Relabel as a coin store listing (store category 121, stores.json line 621) with the vendor marked unidentified. Keep the price claim as is."}]}
