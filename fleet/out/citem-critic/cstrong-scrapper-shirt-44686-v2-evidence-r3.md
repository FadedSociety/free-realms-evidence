<!-- fleet job=citem-critic id=cstrong-scrapper-shirt-44686-v2-evidence-r3 status=done turns=2 usd=0.0014 tokens(read,write,in,out)=[4040, 6526, 6, 1112] model=claude-haiku-5-5 -->
# Strong Scrapper Shirt

{"lens": "evidence", "pass": true, "wireable": true, "score": 4, "problems": [{"field": "sources[0..1].where", "issue": "Both coin_shop sources have where: null. This is honest, since the store file names no NPC or shop location, but a builder cannot place the sale without a vendor. The answer already says so in open.", "fix": "No change needed for pass. If a vendor is later found, add it to where with its source."}]}
