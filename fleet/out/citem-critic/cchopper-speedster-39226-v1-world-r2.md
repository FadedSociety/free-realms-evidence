<!-- fleet job=citem-critic id=cchopper-speedster-39226-v1-world-r2 status=done turns=2 usd=0.0012 tokens(read,write,in,out)=[4294, 5001, 6, 1014] model=claude-haiku-5-5 -->
# Chopper Speedster

{"lens": "world", "pass": true, "wireable": false, "score": 4, "problems": [{"field": "item.kind", "issue": "The answer sets kind to 'mount', but its own evidence (sibling part-items, 'Digs into the race course.', kart-parts family) points to a race kart/vehicle, not a mount. The answer itself flags this in open, but the item object still carries 'mount'.", "fix": "Use a kart/vehicle kind, or leave kind unset until a source confirms it. Client definition shows slot 0 and class 0 only (locale:39226, definition 56982)."}]}
