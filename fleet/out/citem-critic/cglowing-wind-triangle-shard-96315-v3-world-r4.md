<!-- fleet job=citem-critic id=cglowing-wind-triangle-shard-96315-v3-world-r4 status=done turns=2 usd=0.0014 tokens(read,write,in,out)=[3896, 6882, 6, 901] model=claude-haiku-5-5 -->
# Glowing Wind Triangle Shard

{"lens": "world", "pass": true, "wireable": false, "score": 3, "problems": [{"field": "sources[0].type", "issue": "The source is typed 'vendor', but the evidence is only a coin price-list row in category 121 with no NPC, seller or location. Calling it a vendor source slightly overstates it. The answer's own open note says the seller is unknown.", "fix": "Label it a coin store price row (category 121, unassigned to an NPC), not a vendor. Stores.json:8078 confirms item 30909, category 121, 540 / 486 member / 54 sell, no_sale false, so the numbers are correct."}]}
