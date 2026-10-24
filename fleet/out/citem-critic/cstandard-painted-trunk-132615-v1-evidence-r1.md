<!-- fleet job=citem-critic id=cstandard-painted-trunk-132615-v1-evidence-r1 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[3727, 10900, 6, 1199] model=claude-haiku-5-5 -->
# Standard Painted Trunk

{"lens": "evidence", "pass": true, "wireable": true, "score": 4, "problems": [{"field": "where", "issue": "The 'where' value 'Coin Shop (category 53; shop name unconfirmed)' names a shop called 'Coin Shop' that no source in the pack evidences. The only evidence is the store row's category_id 53. The 'open' note already says the shop is unconfirmed, so this is a labelling overstatement, not a wrong price.", "fix": "Set where to 'Coin store, category 53 (shop/NPC not identified)' per repo:prototype/osfr-tools/data/content/stores.json:11874. Pricing is unaffected."}]}
