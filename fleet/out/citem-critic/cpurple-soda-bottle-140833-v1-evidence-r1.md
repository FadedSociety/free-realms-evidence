<!-- fleet job=citem-critic id=cpurple-soda-bottle-140833-v1-evidence-r1 status=done turns=2 usd=0.0009 tokens(read,write,in,out)=[3806, 4225, 6, 756] model=claude-haiku-5-5 -->
# Purple Soda Bottle

{"lens": "evidence", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "item.kind", "issue": "The top-level kind 'collection' is taken only from the cheap first-pass tag. No source in the pack or my lookups names this item's kind. The answer's own open list admits this.", "fix": "Set kind to unknown (or leave unset) until a source shows what the item is. My lookup of 'Purple Soda Bottle' across client, wiki, articles and video returns only locale:140833, which is the name line itself."}]}
