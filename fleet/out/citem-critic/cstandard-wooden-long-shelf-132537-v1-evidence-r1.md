<!-- fleet job=citem-critic id=cstandard-wooden-long-shelf-132537-v1-evidence-r1 status=no_submit turns=3 usd=0.0017 tokens(read,write,in,out)=[11636, 8201, 8, 1067] model=claude-haiku-5-5 -->
# Standard Wooden Long Shelf

{"lens": "evidence", "pass": true, "wireable": true, "score": 4, "problems": [{"field": "sources[0].type", "issue": "The source is labelled 'vendor', but no vendor or NPC is named anywhere. The only evidence is a coin-store row in stores.json with no vendor field. The type should describe what the evidence shows: a coin-store listing with the vendor unidentified.", "fix": "Type: 'coin store listing (vendor unnamed)'. Keep where: null and cite repo:prototype/osfr-tools/data/content/stores.json line 11800, item_id 36124, category 52, tint group 2."}]}
