<!-- fleet job=item-critic id=igreen-watch-v1-world-r2 status=done turns=2 usd=0.0013 tokens(read,write,in,out)=[3506, 6979, 6, 881] model=claude-haiku-5-5 -->
# Green Watch

{"lens": "world", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "live", "issue": "The answer sets live to \"unsure\" for an entity that is not an item. Status does not apply, so the field should be null or not-applicable rather than an open question.", "fix": "Set live to null with the note that Green Watch is a Pony Vale location (wiki rev 46575, infobox Type = Camp), not an item. Client quest text (locale:413225, 413224) uses it only as a place name."}]}
