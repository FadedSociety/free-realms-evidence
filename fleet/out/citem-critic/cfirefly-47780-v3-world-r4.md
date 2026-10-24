<!-- fleet job=citem-critic id=cfirefly-47780-v3-world-r4 status=done turns=3 usd=0.0020 tokens(read,write,in,out)=[12434, 9224, 8, 1455] model=claude-haiku-5-5 -->
# Firefly

{"lens": "world", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "open", "issue": "The answer says the block 17525-17557 is 'identical category-200 rows', but row 17554 in stores.json (line 4345) is priced 15000 coins (member 13500), not 10000. The block is not uniformly 10000.", "fix": "Note that the block is mostly 10000/9000 with one 15000/13500 row (item_id 17554). The 17543 row itself is 10000/9000, no_sale, tint group 3 (stores.json:4334). Checked: the collection_catalogue name_id 17543 maps to item_definition_id 9175 (collection_catalogue.json:18301-18304), as the answer says."}]}
