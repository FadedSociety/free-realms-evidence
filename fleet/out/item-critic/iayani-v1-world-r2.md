<!-- fleet job=item-critic id=iayani-v1-world-r2 status=done turns=2 usd=0.0014 tokens(read,write,in,out)=[3980, 6432, 6, 1078] model=claude-haiku-5-5 -->
# Ayani

{"lens": "world", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "evidence[1] / open", "issue": "The answer lists Ayani Stamp (locale:1474) among the Ayani-named items. The client tags it as 'place', not 'item', so it is not an item source and should not be offered as a candidate item name.", "fix": "Describe locale:1474 as a place-tagged string (client tag 'place - Ayani Stamp'). Keep it out of the item candidate list, or mark it as a place."}]}
