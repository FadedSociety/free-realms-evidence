<!-- fleet job=citem-critic id=craging-rampage-corselet-765-v1-world-r2 status=done turns=2 usd=0.0024 tokens(read,write,in,out)=[4139, 14378, 6, 1210] model=claude-haiku-5-5 -->
# Raging Rampage Corselet

{"lens": "world", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "evidence[0]", "issue": "The stats cited (MinProfileRank 20, PowerRating 5, dyetint) were not re-verified in this pass. Cost 320 and 1266 are client Cost fields, which the answer already flags as not coin-store prices.", "fix": "Verify MinProfileRank and PowerRating against refs:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json at Id 2339 and Id 333 before relying on them. Cost fields are not sale prices."}]}
